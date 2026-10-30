#!/usr/bin/env python3
"""Verify a staged static directory against its deployed public URL."""

import argparse
import hashlib
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

TEXT_EXTS = {".html", ".css", ".js", ".json", ".xml", ".txt", ".svg"}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    parser.add_argument("base_url")
    parser.add_argument("--strict-binary", action="store_true")
    args = parser.parse_args()

    failures = []
    optimized = []
    files = sorted(path for path in args.directory.rglob("*") if path.is_file())
    for path in files:
        relative = path.relative_to(args.directory).as_posix()
        url = f"{args.base_url.rstrip('/')}/{quote(relative)}"
        try:
            with urlopen(Request(url, headers={"User-Agent": "static-deploy-verifier/1"}), timeout=30) as response:
                remote = response.read()
                if response.status != 200:
                    failures.append(f"{relative}: HTTP {response.status}")
                    continue
        except Exception as exc:
            failures.append(f"{relative}: {exc}")
            continue

        if sha256(path.read_bytes()) != sha256(remote):
            if path.suffix.lower() in TEXT_EXTS or args.strict_binary:
                failures.append(f"{relative}: SHA-256 mismatch")
            else:
                optimized.append(relative)

    print(f"files={len(files)} failures={len(failures)} optimized_binary={len(optimized)}")
    for item in failures:
        print(f"FAIL {item}")
    for item in optimized:
        print(f"NOTE {item}: binary differs; inspect visually for host optimization")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
