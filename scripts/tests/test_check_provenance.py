#!/usr/bin/env python3
r"""
Red-green tests for scripts/check-provenance.py — prove the report<->registry sync gate actually
CATCHES the drifts it claims to ("runs without errors is never a passing test"; every case asserts a
verdict against a known-correct value). Pure-helper unit tests only: each fixture is synthetic data
fed to a pure check function, so there is no dependence on the live report/ or argument/ trees.

RED->GREEN evidence (Rule 1 — each documented as a one-line perturbation of the REAL checker that
flips the named assertion RED; restoring turns it GREEN. Verified by the harness that ships this file):

  * OVERCLAIM (check_status_drift):
      perturb line ~314 `if status_of.get(rid) == "open" and not any_open:` -> `if False:`
      => "OVERCLAIM: open result framed proved is an ERROR" goes RED.
  * stale source hash (check_source_hashes):
      perturb the `if actual != sha:` compare to `if False:` (line ~363)
      => "a stale/edited source hash is caught" goes RED.
  * bad sha format (check_source_hashes):
      perturb the `re.fullmatch(r"[0-9a-f]{16}", sha)` guard to always-true
      => "a malformed sha (not 16 hex) is caught" goes RED.
  * dangling claim label (check_claim_labels):
      perturb `if lab not in texlabels:` -> `if False:` (line ~262)
      => "a claim-ledger row with no \\label{} is caught" goes RED.
  * dangling forward label (check_forward_labels):
      perturb `if lab not in texlabels:` -> `if False:` (line ~243)
      => "a provenance forward-ref to a missing \\label{} is caught" goes RED.
  * duplicate source key (parse_provenance):
      perturb the `if key in out["source_registry"] ...` dup guard to `if False:`
      => "a duplicate source-registry key is surfaced" goes RED.
  * anchor whitelist (check_anchor / load_unwired):
      perturb `if s["id"] in whitelist:` -> `if True:`
      => "an unanchored NON-whitelisted id is an ERROR" goes RED (it would warn instead).

No external deps; run: python3 scripts/tests/test_check_provenance.py
"""
import importlib.util
import pathlib
import tempfile
import hashlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent

_spec = importlib.util.spec_from_file_location("check_provenance", ROOT / "scripts" / "check-provenance.py")
cp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cp)

passed = failed = 0


def check(name, cond):
    global passed, failed
    if cond:
        passed += 1
        print(f"PASS  {name}")
    else:
        failed += 1
        print(f"FAIL  {name}")


def has(msgs, sub):
    return any(sub in m for m in msgs)


# -------------------------------------------------------------------------------------------------
# 1. STATUS OVERCLAIM (the project's #1 guarded failure mode: an open result framed as proved).
# -------------------------------------------------------------------------------------------------
SHARD_OPEN = {"id": "op-kernel", "status": "open", "af": "none", "provenance": "report op:kernel"}
TEX = {"op:kernel"}

# GREEN: an open result framed 'open' in tab:status -> no error.
e, w = cp.check_status_drift([("open", ["op:kernel"])], [SHARD_OPEN], TEX)
check("open result framed 'open' -> no overclaim error", e == [])

# RED->GREEN target: the SAME open result framed ONLY 'proved' -> OVERCLAIM error.
e, w = cp.check_status_drift([("proved", ["op:kernel"])], [SHARD_OPEN], TEX)
check("OVERCLAIM: open result framed proved is an ERROR", has(e, "OVERCLAIM") and has(e, "op-kernel"))

# A result Cref'd by BOTH an 'open' row and a 'proved, cond.' row is consistent (one row frames it
# open) -> no error. Guards against a false-positive on multiply-listed results.
e, w = cp.check_status_drift([("open", ["op:kernel"]), ("proved, cond.", ["op:kernel"])], [SHARD_OPEN], TEX)
check("open result with one consistent 'open' row -> no overclaim", e == [])

# UNDERCLAIM (validated result framed only 'open') is a WARN, not an error.
SHARD_VALID = {"id": "lem-bridge", "status": "proved", "af": "validated", "provenance": "report lem:bridge"}
e, w = cp.check_status_drift([("open", ["lem:bridge"])], [SHARD_VALID], {"lem:bridge"})
check("underclaim (validated framed 'open') warns, not errors", e == [] and has(w, "lem-bridge"))


# -------------------------------------------------------------------------------------------------
# 2. STALE / MALFORMED SOURCE HASHES.
# -------------------------------------------------------------------------------------------------
tmp = pathlib.Path(tempfile.mkdtemp())
(tmp / "refs").mkdir()
payload = b"the exact ground-truth bytes of a local source file\n"
(tmp / "refs" / "src.md").write_text(payload.decode(), encoding="utf-8")
good_sha = hashlib.sha256(payload).hexdigest()[:16]
relpath = "refs/src.md"

# GREEN: recorded hash matches the file (tracked) -> no error.
e, w = cp.check_source_hashes([("SRC", relpath, good_sha)], root=tmp, tracked={relpath})
check("matching source hash -> no error", e == [])

# RED->GREEN target: an edited/stale hash (recorded != actual) -> error.
e, w = cp.check_source_hashes([("SRC", relpath, "0" * 16)], root=tmp, tracked={relpath})
check("a stale/edited source hash is caught", has(e, "stale") and has(e, "SRC"))

# RED->GREEN target: a malformed sha (not 16 lowercase hex) -> error.
e, w = cp.check_source_hashes([("SRC", relpath, "NOTHEX")], root=tmp, tracked={relpath})
check("a malformed sha (not 16 hex) is caught", has(e, "not 16 lowercase hex"))

# An untracked (gitignored) payload only WARNS — verdict must match a clean CI checkout.
e, w = cp.check_source_hashes([("SRC", relpath, "0" * 16)], root=tmp, tracked=set())
check("an untracked payload warns, never errors (clean-checkout parity)", e == [] and w != [])


# -------------------------------------------------------------------------------------------------
# 3. DANGLING / DUPLICATE LABELS.
# -------------------------------------------------------------------------------------------------
# Dangling per-claim ledger row (label with no \label{} in the report).
e = cp.check_claim_labels([("lem:live", "SRC"), ("lem:ghost", "SRC")], {"lem:live"})
check("a claim-ledger row with no \\label{} is caught", has(e, "lem:ghost") and not has(e, "lem:live"))

# Dangling forward label (a registry provenance `report <label>` naming a missing \label{}).
e = cp.check_forward_labels([{"id": "lem-x", "provenance": "report lem:missing"}], {"lem:present"})
check("a provenance forward-ref to a missing \\label{} is caught", has(e, "lem:missing"))

# Duplicate source-registry key surfaced by parse_provenance (a would-be SILENT drop).
prov_dir = pathlib.Path(tempfile.mkdtemp())
prov_file = prov_dir / "PROVENANCE.md"
prov_file.write_text(
    "## Ground-truth source registry\n"
    "| Key | Path | sha |\n|---|---|---|\n"
    "| `SRC` | `refs/a.md` | `0123456789abcdef` |\n"
    "| `SRC` | `refs/b.md` | `fedcba9876543210` |\n"
    "\n## Per-claim ledger\n"
    "| Report label | Source |\n|---|---|\n"
    "| lem:live | SRC |\n",
    encoding="utf-8")
prov = cp.parse_provenance(prov_file)
check("a duplicate source-registry key is surfaced (not silently dropped)",
      has(prov["parse_warnings"], "defined twice"))
check("both rows of a reused key are retained for hashing", len(prov["source_rows"]) == 2)


# -------------------------------------------------------------------------------------------------
# 4. ANCHOR WHITELIST (report/UNWIRED.md) — unanchored+whitelisted=WARN; unanchored+not=ERROR.
# -------------------------------------------------------------------------------------------------
UNW = prov_dir / "UNWIRED.md"
UNW.write_text(
    "# UNWIRED\nSome prose that mentions conj-not-an-id and must be ignored.\n\n"
    "## Frontier\n```\nconj-whitelisted\n# a comment line, ignored\n\nlem-also-ok\n```\n"
    "more prose\n```\nlem-temp-t0\n```\n",
    encoding="utf-8")
wl = cp.load_unwired(UNW)
check("load_unwired harvests only fenced ids (prose/comments ignored)",
      wl == {"conj-whitelisted", "lem-also-ok", "lem-temp-t0"})

anchored = {"id": "lem-anchored", "provenance": "report lem:anchored"}
white = {"id": "conj-whitelisted", "provenance": ""}      # no report label, but whitelisted
naked = {"id": "lem-orphan", "provenance": ""}             # no report label, NOT whitelisted
texset = {"lem:anchored"}

# GREEN: an anchored shard produces neither warn nor error.
e, w = cp.check_anchor([anchored], texset, wl)
check("an anchored shard: no anchor error/warn", e == [] and w == [])

# WARN: unanchored but whitelisted.
e, w = cp.check_anchor([white], texset, wl)
check("unanchored + whitelisted -> WARN, not error", e == [] and has(w, "conj-whitelisted"))

# RED->GREEN target: unanchored + NOT whitelisted -> ERROR.
e, w = cp.check_anchor([naked], texset, wl)
check("unanchored + NOT whitelisted -> ERROR", has(e, "lem-orphan"))

# With an EMPTY whitelist, every unanchored id errors (proves the whitelist is load-bearing).
e, w = cp.check_anchor([white, naked], texset, frozenset())
check("empty whitelist -> all unanchored ids error", has(e, "conj-whitelisted") and has(e, "lem-orphan"))


# -------------------------------------------------------------------------------------------------
# 5. INTEGRATION SMOKE: the real repo's UNWIRED.md whitelists ALL currently-unanchored ids, so the
#    live check_anchor yields ZERO errors (check-all stays green today).
# -------------------------------------------------------------------------------------------------
shards = cp.parse_registry()
texlabels = cp.tex_labels()
live_wl = cp.load_unwired(cp.UNWIRED)
e, w = cp.check_anchor(shards, texlabels, live_wl)
check("LIVE repo: every unanchored registry id is whitelisted (zero anchor errors)", e == [])


print(f"\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
