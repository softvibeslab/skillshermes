#!/usr/bin/env python3
"""Valida contrato, privacidad y filtros del dashboard Knowledge Assets."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


TARGET_SECTIONS = (
    "assets",
    "contribution-timeline",
    "final-validation",
    "people",
    "commerce-map",
    "member-atlas",
    "case-maps",
)
REQUIRED_ADAPTERS = (
    "inventory",
    "timeline",
    "final_validation",
    "member_contributions",
    "commerce_workflow",
    "member_atlas",
    "case_maps",
)
FORBIDDEN = (
    ".m3u8",
    "authorization:",
    "cookie:",
    "bearer ",
    "x-amz-signature",
    "/users/rogergv/",
    "media/original",
    "transcript/transcript",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--projection", required=True, type=Path)
    parser.add_argument("--dashboard", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    data = json.loads(args.projection.read_text(encoding="utf-8"))
    html = args.dashboard.read_text(encoding="utf-8")
    errors: list[str] = []
    if data.get("schema_version") != "2.0.0":
        errors.append("schema_version debe ser 2.0.0")
    adapters = data.get("section_integrations", {})
    for key in REQUIRED_ADAPTERS:
        if key not in adapters:
            errors.append(f"falta section_integrations.{key}")
    if data.get("governance", {}).get("human_approved") is not False:
        errors.append("human_approved debe permanecer false")
    maps = adapters.get("case_maps", [])
    strengthened = [item for item in maps if item.get("relationship") == "strengthens_existing"]
    new = [item for item in maps if item.get("relationship") == "new_use_case"]
    expected_strengthened = len(data.get("existing_use_case_contributions", []))
    expected_new = len(data.get("new_use_case_families", []))
    if (len(strengthened), len(new)) != (expected_strengthened, expected_new):
        errors.append(
            "mapas no coinciden con la proyección: "
            f"esperados {expected_strengthened}/{expected_new}; "
            f"encontrados {len(strengthened)}/{len(new)}"
        )
    baseline_use_cases = int(data.get("comparison", {}).get("baseline", {}).get("use_cases") or 0)
    expected_unique = baseline_use_cases + expected_new
    actual_unique = adapters.get("member_atlas", {}).get("unique_combined_use_cases")
    if actual_unique != expected_unique:
        errors.append(
            "member_atlas.unique_combined_use_cases no coincide: "
            f"esperado {expected_unique}; encontrado {actual_unique}"
        )
    for section_id in TARGET_SECTIONS:
        if f'id="{section_id}"' not in html:
            errors.append(f"falta sección HTML #{section_id}")
    if "data-global-knowledge-mode" not in html or "installKnowledgeScopeControls" not in html:
        errors.append("faltan controles globales Base/PRO/Comparativa")
    serialized = json.dumps(data, ensure_ascii=False).lower()
    public_html = re.sub(r"const amazonProFallback=.*?;\nlet amazonProKnowledge=", "", html, flags=re.DOTALL).lower()
    leaks = [marker for marker in FORBIDDEN if marker in serialized or marker in public_html]
    if leaks:
        errors.append(f"marcadores privados detectados: {sorted(set(leaks))}")
    match = re.search(r"const amazonProFallback=(.*?);\nlet amazonProKnowledge=", html, re.DOTALL)
    if not match:
        errors.append("fallback JSON no encontrado")
    else:
        try:
            if json.loads(match.group(1)) != data:
                errors.append("fallback embebido no coincide con la proyección")
        except json.JSONDecodeError:
            errors.append("fallback embebido no es JSON válido")
    result = {
        "status": "error" if errors else "ok",
        "filters": len(TARGET_SECTIONS),
        "strengthened_existing": len(strengthened),
        "new_use_cases": len(new),
        "unique_combined": adapters.get("member_atlas", {}).get("unique_combined_use_cases"),
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
