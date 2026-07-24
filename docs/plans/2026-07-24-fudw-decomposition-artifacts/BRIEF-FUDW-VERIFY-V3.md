# BRIEF — aism-fudw decomposition v3: FRESH HOSTILE RE-REVIEW

You are a FRESH HOSTILE REVIEWER (codex, independent context — none of the five
prior workers; their written artifacts are your only inputs). Finding a flaw is a
BIG SUCCESS.

## Object under review

`docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v3.md`.

## Read first

Everything in `BRIEF-FUDW-VERIFY.md` §Read-first (governs verbatim), PLUS the
full verdict/design lineage in this directory: `VERDICT-FUDW-DECOMP.md` (v1),
`DESIGN-FUDW-DECOMP-v2.md`, `VERDICT-FUDW-DECOMP-V2.md`, `BRIEF-FUDW-REPAIR-V3.md`,
and the v3 design itself.

## Attack surface

Items 1–8 of `BRIEF-FUDW-VERIFY.md` applied to v3 as a standalone object, plus
items 9–10 of `BRIEF-FUDW-VERIFY-V2.md` (disposition completeness against BOTH
prior verdicts; repair-introduced regressions). Pay particular hostile attention
to: the 3 new COMP producers, the closed H-datum proposal, the 8-row MAIN
factoring, the common-split and degree-two producers, the expanded degree-three
formula, and whether the named GAPs (GAP-EA, GAP-S1-POLAR-CONTRACT,
GAP-MAIN-STRUCTURE, GAP-LEDGER-DOMAINS, uncontracted F2/F3) are honestly scoped
rather than quietly load-bearing inside any `proved-mod-audit` contract.

## Verdict semantics (IMPORTANT)

The v3 design self-declares "repaired architecture only; not globally seedable"
because of its named GAPs. Judge it against THAT claim: a design whose
`proved-mod-audit` rows are faithful, acyclic, envelope-realistic, and
def-complete, and whose GAPs are honestly quarantined, is VALID (or
VALID-WITH-CORRECTIONS) AS A DECOMPOSITION even though the GAP ids block
end-to-end seeding. INVALID is for defects in what the design DOES claim.
State explicitly in your verdict which subset of rows (if any) is safe to
transcribe into the registry and seed first.

## Output

`VERDICT-FUDW-DECOMP-V3.md` + `ANSWER-VERIFY-V3.md` in this directory, exactly
per `BRIEF-FUDW-VERIFY.md` §Output (VERDICT line first; per-surface findings
with severity + ready-to-paste corrections; registry-impact section including
the safe-to-transcribe subset; ≤10-line summary).

## Hard boundaries

Identical to `BRIEF-FUDW-VERIFY.md`: ONLY your two output files; no registry/
proofs/refs edits; no git; do not soften findings.
