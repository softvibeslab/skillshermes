#!/usr/bin/env python3
"""Private, interactive cntb setup. No API requests and no credential logging."""
import argparse
import getpass
import json
import os
from pathlib import Path
import sys
import tempfile

FIELDS = ("oauth2-clientid", "oauth2-client-secret", "oauth2-user", "oauth2-password")


def save(home, credentials):
    if not home.is_dir():
        raise ValueError("Hermes home must already exist")
    if any(not isinstance(credentials.get(k), str) or not credentials[k].strip() for k in FIELDS):
        raise ValueError("All four credentials are required")
    directory = home / "integrations" / "contabo"
    # ponytail: same-user profile isolation, not a security sandbox; use containers for that.
    for p in (home / "integrations", directory, directory / ".cache", directory / ".cache" / "cntb"):
        if p.is_symlink():
            raise ValueError("Refusing symlink in credential/cache path")
        p.mkdir(mode=0o700, exist_ok=True)
    for p in (directory, directory / ".cache", directory / ".cache" / "cntb"):
        p.chmod(0o700)
    path = directory / ".cntb.yaml"
    config = {**{k: credentials[k] for k in FIELDS}, "debug": "warn",
              "api": "https://api.contabo.com",
              "oauth2-tokenurl": "https://auth.contabo.com/auth/realms/contabo/protocol/openid-connect/token"}
    # JSON is valid YAML; stdlib avoids adding a YAML dependency.
    payload = json.dumps(config, ensure_ascii=True, indent=2) + "\n"
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "w") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
    except BaseException:
        path.unlink(missing_ok=True)
        raise
    return path


def self_test():
    with tempfile.TemporaryDirectory() as tmp:
        home = Path(tmp)
        credentials = {k: 'dummy-"\\value\nñ' for k in FIELDS}
        path = save(home, credentials)
        data = json.loads(path.read_text())
        assert all(data[k] == credentials[k] for k in FIELDS)
        assert path.stat().st_mode & 0o777 == 0o600
        assert path.parent.stat().st_mode & 0o777 == 0o700
        try:
            save(home, credentials)
        except FileExistsError:
            pass
        else:
            raise AssertionError("Existing config overwritten")
        try:
            save(home, {})
        except ValueError:
            pass
        else:
            raise AssertionError("Empty credentials accepted")
        assert json.loads(path.read_text()) == data
    print("PASS: round-trip, private permissions, no overwrite, required fields")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hermes-home", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if args.hermes_home is None:
        parser.error("Specify --hermes-home explicitly")
    home = args.hermes_home.expanduser().resolve()
    if not home.is_dir():
        parser.error("Hermes home does not exist")
    config = home / "integrations" / "contabo" / ".cntb.yaml"
    if config.exists() or config.is_symlink():
        parser.error("Config already exists; refusing to overwrite")
    if not sys.stdin.isatty():
        parser.error("Run in your own interactive terminal; do not pipe credentials")
    print("Credentials from https://my.contabo.com/api/details")
    print("Inputs are hidden. Saved plaintext with mode 0600; never share this file.")
    credentials = {k: getpass.getpass(k + ": ") for k in FIELDS}
    try:
        path = save(home, credentials)
    except (OSError, ValueError):
        sys.exit("Configuration not saved. Check directory permissions and fill all fields.")
    print("Saved:", path)
    print("Authentication has not been verified. Ask Hermes for a read-only instance check.")


if __name__ == "__main__":
    main()
