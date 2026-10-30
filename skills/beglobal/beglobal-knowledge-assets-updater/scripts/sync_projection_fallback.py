#!/usr/bin/env python3
"""Sincroniza una proyección pública con el fallback JSON del dashboard."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path


REQUIRED_SECTIONS = {
    "inventory",
    "timeline",
    "final_validation",
    "member_contributions",
    "commerce_workflow",
    "member_atlas",
    "case_maps",
}
FORBIDDEN = (
    ".m3u8",
    "authorization:",
    "cookie:",
    "bearer ",
    "x-amz-signature",
    "/users/",
    "media/original",
    "transcript/transcript",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--projection", required=True, type=Path)
    parser.add_argument("--dashboard", required=True, type=Path)
    return parser.parse_args()


def atomic_write(path: Path, text: str) -> None:
    descriptor, temp_name = tempfile.mkstemp(prefix=path.name, suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(text)
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def main() -> int:
    args = parse_args()
    projection = json.loads(args.projection.read_text(encoding="utf-8"))
    missing = REQUIRED_SECTIONS - set(projection.get("section_integrations", {}))
    if missing:
        raise SystemExit(f"Proyección incompleta: {sorted(missing)}")
    serialized = json.dumps(projection, ensure_ascii=False, separators=(",", ":"))
    lowered = serialized.lower()
    leaks = [marker for marker in FORBIDDEN if marker in lowered]
    if leaks:
        raise SystemExit(f"Marcadores privados detectados: {leaks}")
    dashboard = args.dashboard.read_text(encoding="utf-8")
    pattern = re.compile(r"const amazonProFallback=.*?;\nlet amazonProKnowledge=", re.DOTALL)
    replacement = f"const amazonProFallback={serialized};\nlet amazonProKnowledge="
    updated, count = pattern.subn(lambda _: replacement, dashboard)
    if count != 1:
        raise SystemExit(f"Se esperaba un fallback; encontrados: {count}")
    atomic_write(args.dashboard, updated)
    digest = hashlib.sha256(updated.encode("utf-8")).hexdigest()
    print(json.dumps({"status": "ok", "dashboard_sha256": digest, "schema_version": projection["schema_version"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
