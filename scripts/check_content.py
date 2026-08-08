#!/usr/bin/env python3
"""Repository-specific checks that OSCAL schema validation cannot express."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalogs/eu-ai-act/catalog.json"


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


catalog_doc = json.loads(CATALOG_PATH.read_text())
catalog = catalog_doc["catalog"]
objects = list(walk(catalog))
controls = {item["id"]: item for item in objects if item.get("class") == "eu-ai-act-obligation"}

if len(controls) != 50:
    fail(f"expected 50 controls, found {len(controls)}")

params = {param["id"] for item in controls.values() for param in item.get("params", [])}
prose = "\n".join(item.get("prose", "") for item in objects)
inserted = set(re.findall(r"\{\{ insert: param, ([^ }]+) \}\}", prose))
if params != inserted:
    fail(f"parameter mismatch; unreferenced={sorted(params - inserted)}, undefined={sorted(inserted - params)}")

if "Article 10(2)-(5)" in prose or "Article 10(5) permits" in prose:
    fail("stale Article 10(5) requirement remains")

required_fragments = {
    "aia-2": ["Article 2(13)", "currently applicable delegated act"],
    "aia-4a": ["records of processing explain why", "why other data could not adequately"],
    "aia-5.1.ba": ["reasonably foreseeable and reproducible", "purposefully use", "does not alter its sexual nature or meaning"],
    "aia-5.1.bb": ["reasonably foreseeable and reproducible", "purposefully use"],
    "aia-6": ["2 December 2027", "2 August 2028", "Article 6(1a)", "Article 6(1b)", "Article 6(1c)"],
    "aia-10": ["Article 10(2)-(4)", "deleted Article 10(5)"],
    "aia-17": ["amended Article 17(2)"],
    "aia-99": ["Where the offender is an undertaking"],
}
for control_id, fragments in required_fragments.items():
    control_prose = " ".join(part.get("prose", "") for part in controls[control_id].get("parts", []))
    missing = [fragment for fragment in fragments if fragment not in control_prose]
    if missing:
        fail(f"{control_id} missing required content: {missing}")

for path in sorted(ROOT.glob("profiles/*/profile.json")) + [
    ROOT / "assessment-plans/high-risk-provider-readiness/assessment-plan.json",
    ROOT / "docs/examples/template-system-security-plan.json",
]:
    text = path.read_text()
    if '"version": "0.1.1"' not in text:
        fail(f"{path.relative_to(ROOT)} is not version 0.1.1")
    if '"name": "amendment-in-force"' in text:
        fail(f"{path.relative_to(ROOT)} uses the obsolete amendment property name")

assessment = (ROOT / "assessment-plans/high-risk-provider-readiness/assessment-plan.json").read_text()
if "Annex III, 2 December 2027" not in assessment or "ready for the 2 December 2027" not in assessment:
    fail("assessment plan does not use the current Annex III date")

provider = (ROOT / "profiles/high-risk-provider-annex-iii/profile.json").read_text()
if "2 August 2028 application date" not in provider:
    fail("provider profile does not use the current Annex I date")

print(f"OK: {len(controls)} controls, {len(params)} parameters, legal-content regressions checked")
