#!/usr/bin/env python3
"""Materializa un corpus Graphify privado desde notas normalizadas por lección."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path


FORBIDDEN = (
    ".m3u8",
    "authorization:",
    "cookie:",
    "bearer ",
    "session_token",
    "x-amz-",
    "signature=",
    "/users/",
)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def atomic_write(path: Path, value: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temp_name = tempfile.mkstemp(prefix=path.name, suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(value)
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course-root", required=True, type=Path)
    args = parser.parse_args()
    root = args.course_root.resolve()
    if not root.is_dir() or not (root / "lesson-queue.json").is_file():
        raise SystemExit("El paquete de curso no contiene una cola de lecciones")
    queue = json.loads((root / "lesson-queue.json").read_text(encoding="utf-8"))
    expected = [
        str(lesson["lesson_id"])
        for section in queue.get("sections", [])
        for lesson in section.get("lessons", [])
        if lesson.get("lesson_id")
    ]
    corpus = root / "graphify" / "corpus"
    records = []
    for position, lesson_id in enumerate(expected, start=1):
        source = root / "lessons" / lesson_id / "graphify" / "lesson.md"
        if not source.is_file() or source.stat().st_size == 0:
            raise SystemExit(f"Falta la nota Graphify de la lección {lesson_id}")
        payload = source.read_bytes()
        lowered = payload.decode("utf-8", errors="replace").lower()
        leaks = [marker for marker in FORBIDDEN if marker in lowered]
        if leaks:
            raise SystemExit(f"La nota Graphify {lesson_id} contiene marcadores privados prohibidos")
        destination = corpus / f"lesson-{lesson_id}.md"
        if not destination.exists() or destination.read_bytes() != payload:
            atomic_write(destination, payload)
        records.append(
            {
                "position": position,
                "lesson_id": lesson_id,
                "path": f"corpus/{destination.name}",
                "bytes": len(payload),
                "sha256": sha256_bytes(payload),
            }
        )
    manifest = {
        "schema_version": "1.0.0",
        "course_id": root.name,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "expected_lessons": len(expected),
        "materialized_lessons": len(records),
        "records": records,
        "premium_private": True,
        "transcripts_copied": False,
        "media_copied": False,
    }
    atomic_write(
        root / "graphify" / "corpus-manifest.json",
        (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
    )
    print(json.dumps({"status": "ok", "lessons": len(records), "corpus": "graphify/corpus"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
