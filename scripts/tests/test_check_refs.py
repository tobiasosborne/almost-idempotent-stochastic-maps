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

print(f"\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
