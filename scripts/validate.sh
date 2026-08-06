#!/usr/bin/env bash
# Validate every OSCAL document, and confirm every profile actually RESOLVES.
# Schema validity alone is not enough: a profile can validate and still be
# unresolvable if its back-matter references do not resolve.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== trestle validate --all"
trestle validate --all

echo "== profile resolution"
python3 - <<'PY'
import pathlib, sys
from trestle.core.profile_resolver import ProfileResolver
def count(n):
    return len(getattr(n, "controls", None) or []) + sum(
        count(g) for g in (getattr(n, "groups", None) or []))
fail = 0
for prof in sorted(pathlib.Path("profiles").glob("*/profile.json")):
    try:
        cat = ProfileResolver.get_resolved_profile_catalog(pathlib.Path("."), str(prof))
        print(f"  OK   {prof.parent.name}: {count(cat)} controls")
    except Exception as e:
        print(f"  FAIL {prof.parent.name}: {type(e).__name__}: {e}")
        fail = 1
sys.exit(fail)
PY
echo "== all checks passed"
