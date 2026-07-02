#!/usr/bin/env python3
"""
Red-green tests for scripts/check-defs.py — prove the Definitions DB gate actually CATCHES
drift, missing fields, and id mismatch ("runs without errors is never a passing test").
No external deps; run: python3 scripts/tests/test_check_defs.py

Manifest-independent (day-1) subset: every fixture is a `consensus`/`original` shard
(source: internal), so no refs/ source or checksum is required. The two cited-source tests
(bad sha256 in manifest; unknown cited source-id) are DEFERRED — re-add them once refs/ holds
at least one byte-verified source (see scripts/tests/test_check_defs.py history in AIPM for the
template). They are tracked in RESEARCH_NOTES / beads, not silently dropped.
"""
import importlib.util
import pathlib
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
MANIFEST = ROOT / "refs" / "manifest" / "checksums.sha256"  # may be empty/absent on day 1

# import the hyphenated gate module by path
_spec = importlib.util.spec_from_file_location("check_defs", ROOT / "scripts" / "check-defs.py")
cd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cd)

GOOD_ALPHA = (
    "---\nid: def-alpha\nterm: Alpha\naliases: A\nkind: consensus\nstatus: locked\n"
    "source: internal\nsha256: -\nconsensus: A+B\n---\nbody\n"
)
GOOD_BETA = (
    "---\nid: def-beta\nterm: Beta\nkind: consensus\nstatus: locked\n"
    "source: internal\nsha256: -\nconsensus: A+B\n---\nbody\n"
)

passed = failed = 0
def check(name, cond):
    global passed, failed
    if cond:
        passed += 1; print(f"PASS  {name}")
    else:
        failed += 1; print(f"FAIL  {name}")

def run(files):
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        for fn, content in files.items():
            (d / fn).write_text(content, encoding="utf-8")
        return cd.check_defs(d, MANIFEST, generate_index=False)

def has(msgs, sub):
    return any(sub in m for m in msgs)

# 1. GREEN: two valid shards -> no errors
e, w, p = run({"def-alpha.md": GOOD_ALPHA, "def-beta.md": GOOD_BETA})
check("valid DB has no errors", e == [])
check("valid DB parsed 2 shards", len(p) == 2)

# 2. RED: drift — two shards claim the same alias 'A'
drift = GOOD_BETA.replace("term: Beta\n", "term: Beta\naliases: A\n")
e, w, p = run({"def-alpha.md": GOOD_ALPHA, "def-beta.md": drift})
check("drift collision is caught", has(e, "DRIFT"))

# 3. RED: missing required field 'kind'
nokind = GOOD_BETA.replace("kind: consensus\n", "")
e, w, p = run({"def-beta.md": nokind})
check("missing 'kind' is caught", has(e, "missing required field 'kind'"))

# 4. RED: id does not match filename stem
e, w, p = run({"def-gamma.md": GOOD_ALPHA})  # frontmatter id is def-alpha
check("id/filename mismatch is caught", has(e, "!= filename stem"))

# 5. WARN (not error): consensus shard left as draft
draft = GOOD_BETA.replace("status: locked\n", "status: draft\n")
e, w, p = run({"def-beta.md": draft})
check("draft shard warns, not errors", e == [] and has(w, "status=draft"))

print(f"\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
