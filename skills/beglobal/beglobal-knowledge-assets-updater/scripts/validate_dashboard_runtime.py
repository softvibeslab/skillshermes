#!/usr/bin/env python3
"""Valida carga HTTP local y sintaxis JS del dashboard sin navegador externo."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
import threading
import urllib.request
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class ScriptCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.scripts: list[str] = []
        self._capture = False
        self._parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "script":
            return
        values = dict(attrs)
        script_type = (values.get("type") or "text/javascript").lower()
        self._capture = "src" not in values and script_type in {"text/javascript", "application/javascript", "module"}
        self._parts = []

    def handle_data(self, data: str) -> None:
        if self._capture:
            self._parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._capture:
            self.scripts.append("".join(self._parts))
            self._capture = False
            self._parts = []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dashboard", required=True, type=Path)
    parser.add_argument("--projection", required=True, type=Path)
    args = parser.parse_args()
    dashboard = args.dashboard.resolve()
    projection = args.projection.resolve()
    errors: list[str] = []

    html = dashboard.read_text(encoding="utf-8")
    expected_fetch = f"fetch('{projection.name}'"
    if expected_fetch not in html:
        errors.append(f"dashboard no carga {projection.name}")

    collector = ScriptCollector()
    collector.feed(html)
    node = shutil.which("node")
    if node is None:
        errors.append("node no disponible para comprobar JavaScript")
    else:
        with tempfile.TemporaryDirectory(prefix="beglobal-dashboard-js-") as folder:
            for index, source in enumerate(collector.scripts, start=1):
                target = Path(folder) / f"inline-{index}.js"
                target.write_text(source, encoding="utf-8")
                result = subprocess.run([node, "--check", str(target)], text=True, capture_output=True)
                if result.returncode:
                    errors.append(f"script embebido {index}: sintaxis inválida")

    handler = partial(SimpleHTTPRequestHandler, directory=str(dashboard.parent))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        base = f"http://127.0.0.1:{server.server_address[1]}"
        with urllib.request.urlopen(f"{base}/{dashboard.name}", timeout=5) as response:
            if response.status != 200 or not response.read():
                errors.append("dashboard no respondió correctamente por HTTP")
        with urllib.request.urlopen(f"{base}/{projection.name}", timeout=5) as response:
            remote_projection = json.loads(response.read().decode("utf-8"))
        local_projection = json.loads(projection.read_text(encoding="utf-8"))
        if remote_projection != local_projection:
            errors.append("la proyección servida no coincide con el archivo local")
    except Exception as exc:  # noqa: BLE001 - el reporte evita revelar contenido
        errors.append(f"falló la prueba HTTP local ({exc.__class__.__name__})")
    finally:
        server.shutdown()
        server.server_close()

    result = {
        "status": "error" if errors else "ok",
        "inline_scripts_checked": len(collector.scripts),
        "http_dashboard": not any("dashboard no respondió" in item for item in errors),
        "http_projection": not any("proyección servida" in item or "prueba HTTP" in item for item in errors),
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
