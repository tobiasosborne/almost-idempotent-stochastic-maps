# BRIEF — aism-fudw decomposition v2: FRESH HOSTILE RE-REVIEW

You are a FRESH HOSTILE REVIEWER (codex, independent context — you are not the v1
architect, not the v1 reviewer, not the repair architect; you have seen none of
their reasoning beyond the written artifacts). Finding a flaw is a BIG SUCCESS.

## Object under review

`docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v2.md` —
the REPAIRED decomposition of the Route F chain into af-sized registry
sub-lemmas, produced in response to the INVALID verdict on v1.

## Read first

Everything listed in
`docs/plans/2026-07-24-fudw-decomposition-artifacts/BRIEF-FUDW-VERIFY.md`
§Read-first (which governed the v1 review and applies verbatim), PLUS:

- `VERDICT-FUDW-DECOMP.md` (the v1 rejection — your predecessor's findings),
- `DESIGN-FUDW-DECOMP.md` (v1, for diffing what changed),
- `BRIEF-FUDW-REPAIR.md` (the repair work order).

## Attack surface

The full eight-item attack surface of `BRIEF-FUDW-VERIFY.md` applies verbatim to
v2 as a standalone object (coverage, faithfulness, contract hygiene, DAG
soundness, envelope realism, def provisioning, status law, gap honesty). In
ADDITION:

9. **Disposition completeness**: does v2's disposition table actually resolve
   every BLOCKER/MAJOR/MINOR/GAP of the v1 verdict, or does any repair merely
   rename or relocate a defect? Re-attack each of the five v1 blockers directly
   against the v2 text.
10. **Repair-introduced regressions**: did the repair break something v1 had
    right (new cycles via the COMP-CB subtree, new compound contracts in the
    MAIN factoring, status inflation among the 12 `stated` rows, GAP contracts
    that smuggle in unproved strength)?

## Output

Write `VERDICT-FUDW-DECOMP-V2.md` and `ANSWER-VERIFY-V2.md` in the same
directory, with exactly the format rules of `BRIEF-FUDW-VERIFY.md` §Output
(VERDICT line first; per-attack-surface findings with severity and ready-to-paste
corrections; registry-impact section; ≤10-line summary).

## Hard boundaries

Identical to `BRIEF-FUDW-VERIFY.md`: you create ONLY your two output files; no
registry/proofs/refs edits; no git; do not soften findings.
