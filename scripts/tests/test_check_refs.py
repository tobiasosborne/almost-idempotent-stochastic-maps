#!/usr/bin/env python3
"""
Red-green tests for scripts/check-refs.py — prove the provenance matcher CATCHES a fabricated
"VERBATIM" quote (a paraphrase mis-attributed to a refs/ locus) while PASSING a real verbatim
quote, tolerating markdown noise, and preferring the VERBATIM-tagged run.

"Runs without errors is never a passing test" — these assert verdicts against known-correct values.

Day-1 subset: pure-helper unit tests only (no filesystem, no live proofs/ workspaces). The
integration tests over real af workspaces and a real refs/ file are DEFERRED until this repo has
its first proofs/<id>/externals and an ingested refs/ source (tracked in RESEARCH_NOTES / beads).
No external deps; run: python3 scripts/tests/test_check_refs.py
"""
import importlib.util
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent

# import the hyphenated gate module by path
_spec = importlib.util.spec_from_file_location("check_refs", ROOT / "scripts" / "check-refs.py")
cr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cr)

passed = failed = 0


def check(name, cond):
    global passed, failed
    if cond:
        passed += 1
        print(f"PASS  {name}")
    else:
        failed += 1
        print(f"FAIL  {name}")


# -------------------------------------------------------------------------------------------------
# Unit tests on the pure helpers (no filesystem) — normalization + the matcher.
# -------------------------------------------------------------------------------------------------

REAL = ('Let H be a complex Hilbert space and B(H) the algebra of all bounded linear operators on H. '
        'By a JC algebra we shall mean any norm-closed Jordan subalgebra of $B(H)_{\\rm sa}$.')
FABRICATION = ('If A is a $C^*$ algebra then $A_{sa}$ with the Jordan product '
               '$a \\circ b = \\frac{1}{2}(ab+ba)$ is a JB algebra.')

tn_real = cr.normalize("intro words. " + REAL + " more text after.")

ok, chunk = cr.longest_run_match(cr.normalize(REAL), tn_real)
check("real verbatim quote matches its source text", ok and len(chunk) >= cr.MIN_RUN)

ok, _ = cr.longest_run_match(cr.normalize(FABRICATION), tn_real)
check("fabricated quote does NOT match a source that lacks those words", not ok)

# markdown noise (emphasis * and dollar-escaping \$) must NOT break a real match
ok, _ = cr.longest_run_match(
    cr.normalize("T is called positive, if for all $A \\ge 0$, $T(A) \\ge 0$."),
    cr.normalize("*T* is called *positive*, if for all  $A \\ge 0$ ,  $T(A) \\ge 0$ . Then"))
check("markdown emphasis/whitespace noise tolerated (formatting, not words)", ok)

# A WHOLESALE fabrication (a paraphrase of a true fact) leaves NO distinctive >=40-char run intact.
ok, _ = cr.longest_run_match(
    cr.normalize("If A is a $C^*$ algebra then $A_{sa}$ with the Jordan product is a JB algebra."),
    cr.normalize("*T* is called *positive*, if for all  $A \\ge 0$ ,  $T(A) \\ge 0$ . Then"))
check("a wholesale paraphrase (no distinctive run survives) is caught", not ok)

# A word swap inside a SHORT quote (whose only distinctive content IS that run) is caught.
short_src = "$T(A) \\le 0$ for all positive A, a definition."   # source says \\ge, quote claims \\le
ok, _ = cr.longest_run_match(
    cr.normalize(short_src),
    cr.normalize("Recall $T(A) \\ge 0$ for all positive A, a definition. Next..."))
check("a word swap in a short quote (no surviving long run) is caught", not ok)

# extraction prefers the VERBATIM-tagged quote
q = cr.extract_quote('HOS, refs/x.md:1, VERBATIM: "the real claim". NOTE: "a longer aside not the quote"')
check("extract_quote prefers the VERBATIM run", q == "the real claim")

# -------------------------------------------------------------------------------------------------
# UN-VACUUM (aism-dbq): classify_and_check verdicts on the ABSENT-payload path.
#
# RED->GREEN evidence (documented per Rule 1): flip the absent-refs branch in check-refs.py back to
#   `return {"verdict": "skip_noquote", ...}` and the "absent refs payload -> hard fail" assertion
#   below goes RED (verdict skip_noquote != fail); restore the `"verdict": "fail"` and it goes GREEN.
#   The skip_import assertion stays GREEN either way (proves the fix does NOT break dep-imports).
# -------------------------------------------------------------------------------------------------

# An external CLAIMING a refs/ verbatim quote whose payload is ABSENT must be a hard FAIL (not a skip):
# refs/does-not-exist/... is guaranteed absent in the repo, so this exercises the real absent branch.
r = cr.classify_and_check(
    "GT-ghost",
    'GHOST, refs/does-not-exist-xyz/none.md:1, VERBATIM: "some claimed verbatim words here"',
    {})
check("absent refs payload -> hard fail (un-vacuumed, no silent skip)", r["verdict"] == "fail")

# A dep-IMPORT (proofs/<dep-id> path, NO refs locus) must STILL skip — the fix must not break the
# 19 legitimate skip_import cases that are satisfied by the registry, not by a refs payload.
r = cr.classify_and_check(
    "lem-foo",
    "imports proofs/lem-some-validated-dep (a prior validated lemma)",
    {})
check("dep-import (proofs/ path, no refs locus) still skip_import", r["verdict"] == "skip_import")

# -------------------------------------------------------------------------------------------------
# ACKNOWLEDGED-ABSENT (device provisioning, 2026-08-04; hostile-review round 1 corrections folded
# in): the narrow escape hatch over the aism-dbq un-vacuum. A rescue is DIGEST-BOUND — it requires
# the exact (path, workspace, name) triple AND the external's JSON filename AND sha256(source).
# Entries are validated at load against checksums.sha256 (fail-closed). Verdict counting below uses
# LISTS, never name-keyed dicts, so duplicate-name impersonators cannot hide from the assertions.
#
# RED->GREEN evidence (Rule 1): comment out the digest-bound rescue block in check_refs() and
#   "acknowledged absent external ..." goes RED (verdict stays fail); restore it -> GREEN. Weaken
#   the rescue (drop the file or source_sha256 comparison, or the loader validation) and the
#   corresponding attack test below goes RED.
# -------------------------------------------------------------------------------------------------
import hashlib as _hashlib
import json as _json
import subprocess as _subprocess
import tempfile

ABSENT = "refs/does-not-exist-xyz/none.md"
SRC = f'GHOST, {ABSENT}:1, VERBATIM: "some claimed verbatim words here that were once verified"'
SRC_SHA = _hashlib.sha256(SRC.encode("utf-8")).hexdigest()
PAYLOAD_SHA = "1" * 64  # what the (temp) manifest pins for ABSENT


def verdicts(rows, name):
    """ALL verdicts recorded for an external name — duplicates must stay visible."""
    return sorted(r["verdict"] for r in rows if r["external"] == name)


with tempfile.TemporaryDirectory() as td:
    tdp = pathlib.Path(td)
    exdir = tdp / "proofs" / "lem-ack-test" / "externals"
    exdir.mkdir(parents=True)
    (exdir / "a1.json").write_text(_json.dumps({"name": "GT-acknowledged", "source": SRC}))
    (exdir / "a2.json").write_text(_json.dumps({"name": "GT-not-listed", "source": SRC}))
    maniff = tdp / "checksums.sha256"
    maniff.write_text(f"{PAYLOAD_SHA}  ./does-not-exist-xyz/none.md\n")
    ack = {"entries": [{"path": ABSENT, "sha256": PAYLOAD_SHA, "restore_bead": "aism-l4uw",
                        "externals": [{"workspace": "lem-ack-test", "name": "GT-acknowledged",
                                       "file": "a1.json", "source_sha256": SRC_SHA}]}]}
    ackf = tdp / "ack.json"
    ackf.write_text(_json.dumps(ack))

    rows, fail_count, _ = cr.check_refs(proofs_dir=tdp / "proofs", ack_file=ackf,
                                        manifest_file=maniff)
    check("acknowledged absent external (file+digest bound) -> skip_absent_ack, not FAIL",
          verdicts(rows, "GT-acknowledged") == ["skip_absent_ack"])
    check("UNLISTED external over the same absent payload still hard-FAILs (vacuum stays closed)",
          verdicts(rows, "GT-not-listed") == ["fail"] and fail_count == 1)

    # ATTACK: a brand-new external file IMPERSONATES the listed name (same name, same source, a
    # different filename). The file binding must reject it — and the listed one still rescues.
    (exdir / "zz-impersonator.json").write_text(
        _json.dumps({"name": "GT-acknowledged", "source": SRC}))
    rows, fail_count, _ = cr.check_refs(proofs_dir=tdp / "proofs", ack_file=ackf,
                                        manifest_file=maniff)
    check("impersonating duplicate (same name+source, new file) hard-FAILs; exit stays non-zero",
          verdicts(rows, "GT-acknowledged") == ["fail", "skip_absent_ack"] and fail_count == 2)
    (exdir / "zz-impersonator.json").unlink()

    # ATTACK: the listed external's QUOTE is altered in place (same tuple, same filename). The
    # source digest must reject it — an acknowledgment never covers modified words.
    (exdir / "a1.json").write_text(_json.dumps({
        "name": "GT-acknowledged",
        "source": f'GHOST, {ABSENT}:1, VERBATIM: "subtly altered fabricated words, same length-ish"'}))
    rows, fail_count, _ = cr.check_refs(proofs_dir=tdp / "proofs", ack_file=ackf,
                                        manifest_file=maniff)
    check("altered quote under an acknowledged tuple hard-FAILs (source digest binds the words)",
          verdicts(rows, "GT-acknowledged") == ["fail"])
    (exdir / "a1.json").write_text(_json.dumps({"name": "GT-acknowledged", "source": SRC}))

    # ATTACK: same name+file+source but a DIFFERENT workspace directory.
    exdir2 = tdp / "proofs" / "lem-other-ws" / "externals"
    exdir2.mkdir(parents=True)
    (exdir2 / "a1.json").write_text(_json.dumps({"name": "GT-acknowledged", "source": SRC}))
    rows, _, _ = cr.check_refs(proofs_dir=tdp / "proofs", ack_file=ackf, manifest_file=maniff)
    check("same external replayed from a DIFFERENT workspace hard-FAILs (workspace binds)",
          [r["verdict"] for r in rows if r["workspace"] == "lem-other-ws"] == ["fail"])
    (exdir2 / "a1.json").unlink()

    # ATTACK: the NAME must bind independently — same file, same source, renamed external.
    # (Goes RED if the rescue key ever drops the name component.)
    (exdir / "a1.json").write_text(_json.dumps({"name": "GT-renamed", "source": SRC}))
    rows, _, _ = cr.check_refs(proofs_dir=tdp / "proofs", ack_file=ackf, manifest_file=maniff)
    check("renamed external (same file+source, different name) hard-FAILs (name binds)",
          verdicts(rows, "GT-renamed") == ["fail"])
    (exdir / "a1.json").write_text(_json.dumps({"name": "GT-acknowledged", "source": SRC}))

    # LOADER fail-closed: an entry whose path is not pinned / pinned under a different sha /
    # non-canonical must ABORT the gate, never load partially.
    def raises(entries):
        ackf.write_text(_json.dumps({"entries": entries}))
        try:
            cr.load_absent_acks(ack_file=ackf, manifest_file=maniff)
            return False
        except ValueError:
            return True

    base_ext = [{"workspace": "w", "name": "n", "file": "f.json", "source_sha256": "0" * 64}]
    check("loader REJECTS an entry whose path is not pinned in checksums.sha256",
          raises([{"path": "refs/never-pinned/x.txt", "sha256": PAYLOAD_SHA, "externals": base_ext}]))
    check("loader REJECTS an entry whose sha256 mismatches the pinned manifest hash",
          raises([{"path": ABSENT, "sha256": "2" * 64, "externals": base_ext}]))
    # ISOLATED traversal test (review round 2): pin the traversal SPELLING in the manifest too, so
    # the manifest-membership check passes and ONLY the canonicalization guard can reject it.
    maniff.write_text(f"{PAYLOAD_SHA}  ./does-not-exist-xyz/none.md\n"
                      f"{PAYLOAD_SHA}  ./../does-not-exist-xyz/none.md\n")
    check("loader REJECTS a traversal path even when the manifest pins that exact spelling",
          raises([{"path": "refs/../does-not-exist-xyz/none.md", "sha256": PAYLOAD_SHA,
                   "externals": base_ext}]))
    maniff.write_text(f"{PAYLOAD_SHA}  ./does-not-exist-xyz/none.md\n"
                      f"{PAYLOAD_SHA}  ./does-not-exist-xyz//none.md\n")
    check("loader REJECTS an empty path segment ('//') even when pinned verbatim",
          raises([{"path": "refs/does-not-exist-xyz//none.md", "sha256": PAYLOAD_SHA,
                   "externals": base_ext}]))
    # MUTATION-KILLING canonical test (review round 3): this spelling RESOLVES INSIDE refs/, so the
    # symlink-confinement check alone would accept it — only the segment guard rejects it. Deleting
    # the segment guard turns this test RED.
    maniff.write_text(
        f"{PAYLOAD_SHA}  ./does-not-exist-xyz/none.md\n"
        f"{PAYLOAD_SHA}  ./does-not-exist-xyz/../does-not-exist-xyz/none.md\n")
    check("loader REJECTS an in-refs '..' spelling that resolves INSIDE refs/ (segment guard, "
          "not confinement, must catch it)",
          raises([{"path": "refs/does-not-exist-xyz/../does-not-exist-xyz/none.md",
                   "sha256": PAYLOAD_SHA, "externals": base_ext}]))
    maniff.write_text(f"{PAYLOAD_SHA}  ./does-not-exist-xyz/none.md\n")

    # SYMLINK-ESCAPE regression (review round 3): a canonical-looking path whose parent dir is a
    # symlink out of refs/. Segments pass; only resolved-path confinement can reject. Transient,
    # gitignored payload area; always cleaned up.
    _link = ROOT / "refs" / "tmp-acktest-symlink"
    try:
        _link.symlink_to(tdp)
        maniff.write_text(f"{PAYLOAD_SHA}  ./does-not-exist-xyz/none.md\n"
                          f"{PAYLOAD_SHA}  ./tmp-acktest-symlink/evil.txt\n")
        check("loader REJECTS a pinned, canonical-looking path that RESOLVES outside refs/ "
              "through a symlink",
              raises([{"path": "refs/tmp-acktest-symlink/evil.txt", "sha256": PAYLOAD_SHA,
                       "externals": base_ext}]))
    finally:
        _link.unlink(missing_ok=True)
        maniff.write_text(f"{PAYLOAD_SHA}  ./does-not-exist-xyz/none.md\n")
    check("loader REJECTS an external lacking the digest binding fields",
          raises([{"path": ABSENT, "sha256": PAYLOAD_SHA,
                   "externals": [{"workspace": "w", "name": "n"}]}]))

    # STRICT manifest parsing (review round 2): the old whitespace-split parser could be spoofed by
    # filenames with spaces and silently took the last of duplicate lines.
    spaced = tdp / "spaced.sha256"
    spaced.write_text(f"{PAYLOAD_SHA}  ./actual-dir/file with-space-tail.txt\n")
    pinned_sp = cr._parse_manifest(spaced)
    check("manifest filename containing spaces is parsed VERBATIM (no whitespace-split spoof)",
          pinned_sp == {"refs/actual-dir/file with-space-tail.txt": PAYLOAD_SHA})
    spaced.write_text("not a manifest line\n")
    try:
        cr._parse_manifest(spaced)
        check("malformed manifest line ABORTS the parse (trust input, fail-closed)", False)
    except ValueError:
        check("malformed manifest line ABORTS the parse (trust input, fail-closed)", True)
    spaced.write_text(f"{PAYLOAD_SHA}  ./x.txt\n{'2' * 64}  ./x.txt\n")
    try:
        cr._parse_manifest(spaced)
        check("duplicate manifest path ABORTS the parse (no silent last-wins)", False)
    except ValueError:
        check("duplicate manifest path ABORTS the parse (no silent last-wins)", True)

    # STALE entry, HERMETIC (review round 3): create a transient PRESENT payload under the real
    # refs/ (gitignored area, always cleaned up), pin its true sha in the temp manifest, and assert
    # AT LOADER LEVEL that the entry is excluded — deleting the stale guard turns this RED directly,
    # independent of how check_refs consults acknowledgments.
    _pdir = ROOT / "refs" / "tmp-acktest-present"
    _pfile = _pdir / "payload.txt"
    try:
        _pdir.mkdir(exist_ok=True)
        _pfile.write_text("transient present payload for the stale-entry test\n")
        _psha = _hashlib.sha256(_pfile.read_bytes()).hexdigest()
        maniff.write_text(f"{PAYLOAD_SHA}  ./does-not-exist-xyz/none.md\n"
                          f"{_psha}  ./tmp-acktest-present/payload.txt\n")
        fab = ('X, refs/tmp-acktest-present/payload.txt:1, '
               'VERBATIM: "words that certainly do not appear in that payload file"')
        good_ext = {"workspace": "lem-ack-test", "name": "GT-stale-ack", "file": "a3.json",
                    "source_sha256": _hashlib.sha256(fab.encode()).hexdigest()}
        ackf.write_text(_json.dumps({"entries": [
            {"path": "refs/tmp-acktest-present/payload.txt", "sha256": _psha,
             "externals": [good_ext]}]}))
        acks_stale = cr.load_absent_acks(ack_file=ackf, manifest_file=maniff)
        check("loader EXCLUDES an entry whose payload is PRESENT (stale guard, asserted directly)",
              acks_stale == {})
        # ...and end-to-end: the fabricated quote against the present payload is byte-checked: FAIL.
        (exdir / "a3.json").write_text(_json.dumps({"name": "GT-stale-ack", "source": fab}))
        rows, _, _ = cr.check_refs(proofs_dir=tdp / "proofs", ack_file=ackf,
                                   manifest_file=maniff)
        check("ack entry for a PRESENT payload is stale/ignored — mismatched quote still FAILs",
              verdicts(rows, "GT-stale-ack") == ["fail"])
        (exdir / "a3.json").unlink()
        # Schema validation runs BEFORE the staleness continue — a malformed external cannot hide
        # behind a present payload (review round 2).
        ackf.write_text(_json.dumps({"entries": [
            {"path": "refs/tmp-acktest-present/payload.txt", "sha256": _psha,
             "externals": [{"workspace": "w", "name": "n"}]}]}))
        try:
            cr.load_absent_acks(ack_file=ackf, manifest_file=maniff)
            check("schema violation on a STALE (present-payload) entry still ABORTS", False)
        except ValueError:
            check("schema violation on a STALE (present-payload) entry still ABORTS", True)
    finally:
        if _pfile.exists():
            _pfile.unlink()
        if _pdir.exists():
            _pdir.rmdir()

# The policy file must be genuinely TRACKED — an ignored trust input is invisible to review and to
# the af prover-overreach guard (review rounds 1+2): (a) it is in the git index, AND (b) the
# .gitignore RULES exempt it (--no-index evaluates rules even for already-tracked files).
_ls = _subprocess.run(["git", "ls-files", "--error-unmatch",
                       "refs/manifest/absent-acknowledged.json"],
                      cwd=ROOT, capture_output=True)
check("refs/manifest/absent-acknowledged.json is in the git index (tracked trust input)",
      _ls.returncode == 0)
_ci = _subprocess.run(["git", "check-ignore", "-q", "--no-index",
                       "refs/manifest/absent-acknowledged.json"], cwd=ROOT)
check("the .gitignore RULES exempt absent-acknowledged.json (no ignore regression possible)",
      _ci.returncode != 0)

print(f"\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
