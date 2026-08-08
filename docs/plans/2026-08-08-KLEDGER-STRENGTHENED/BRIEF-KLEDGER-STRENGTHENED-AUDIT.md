# BRIEF — fresh hostile audit of DESIGN-KLEDGER-STRENGTHENED.md

You are a fresh hostile auditor. You did NOT write
`docs/plans/2026-08-08-KLEDGER-STRENGTHENED/DESIGN-KLEDGER-STRENGTHENED.md`
and your job is to find the error that gets a wrong or undischargeable
contract into the registry. Finding a fatal flaw is a BIG SUCCESS, not a
failure of the process. Assume the design is wrong until it survives your
attack.

## What is at stake

The design REPLACES the landed `lem-routef-k-ledger` contract (the parent of
the entire 19-row T0 ledger family) with a strengthened fully-quantified
∀n ∀Q ∀eta form, and lands the new `lem-routef-f0-assembly` row — the
penultimate node before the `op-classical` root rewire. If ratified, both
shards land VERBATIM and are af-elevated. An error here is the single most
consequential contract error left on Route F: it becomes the statement the
root discharge rests on.

## Mandatory attack list (do all of these, then anything else you find)

1. **Authorization fidelity.** The replacement contract must implement
   `DESIGN-F0-ASSEMBLY.md` §1.3 with the AUDIT-F0-ASSEMBLY corrections
   (strengthened-replacement classification; canonical complexification
   `Q_C` typing matching the two landed lift rows byte-for-byte at the
   seam), and the deps block of `DESIGN-LEDGER-SETTING-RESCOPE-V2.md` §6.2.
   Any silent deviation from the ratification trail = finding.
2. **Seam-table re-verification (do not trust the design's table).**
   Re-derive every row of the seam table yourself against the CURRENT
   byte-frozen contracts under `argument/lemmas/`: the F0 lift pair
   (`Phi := J Q_C D`, the cb/inf-norm defect identity), formation's
   hypothesis `0 <= eta <= rho_id^corr` and `||Phi^2-Phi||_cb <= eta`, the
   packet chain rows 5 -> 6 -> 8 -> 9 ("supplied by" clauses — check the
   existential export direction, not just the estimates), telescopes,
   row 13's K, row 14's eta_K and scalar consequences, F2's exact
   hypotheses (incl. its threshold form), F3's, PRH's conclusion
   `(K+4*sqrt(2K))*sqrt(eta)` for the SAME Q. Any conversion, re-binding,
   or constant re-enlargement the design missed = finding.
3. **The eta-domain chain.** Verify from the frozen contracts (not the
   design prose) that `eta <= eta_K` implies every threshold hypothesis
   used downstream: `eta_K <= rho_fac`, the chain to `rho_T` and
   `rho_id^corr` needed by formation, F2's `min{(24K)^{-1},1}`, F3's
   denominator guard. A single gap makes the parent vacuous or
   undischargeable.
4. **Packet existence vs telescope import (rescope audit risk 11).** Delete
   formation or any of rows 5/6/8/9 from the deps line: does packet
   construction fail? Conversely: does the design consume any object that
   rows 5/6/8/9's CONTRACTS do not export (interface-projection failure,
   FINDINGS.md 2026-08-05)? Specifically adjudicate the design's 15-vs-16
   deps decision: does row 8's frozen contract REALLY export the Upsilon'
   the parent needs, or is the componentwise package of
   `lem-routef-upsilon-prime-component-construction` consumed anywhere?
5. **Same-datum drift.** One W_RF, one S, one (B, Phi, Delta, Upsilon, eta)
   through all fifteen applications; the E repairs the SAME Q that entered
   at F0. Attempt to re-select witnesses mid-proof; the contract must
   forbid it.
6. **Dimension-freeness.** K and eta_K must be exactly the T0 rows'
   universal scalars; no n, amplification level, block count, block
   dimension, or Choi multiplicity may leak into the parent's constants.
7. **F0-assembly minimality.** `lem-routef-f0-assembly` must consume ONLY
   `lem-routef-k-ledger` (no F2/F3/PRH duplication) and must NOT touch
   sharpness or `op-classical`. Its `eta_0 = eta_K`, `C = K+4*sqrt(2K)`
   specialization must follow from the parent contract alone.
8. **Status honesty / no laundering.** Both shards must land `status:
   stated`, `af: none`; the superseded W74F paper ledger must be recorded
   as history only. Any inherited `proved-mod-audit`, any prose implying
   the strengthened form was already hostile-verified, any promotion = REJECT.
9. **Budget honesty.** The parent budget is target 17 nodes / 4 rounds /
   HARD CAP 22. With this family's observed 1.5–3x fresh-build expansion
   (row 8 ballooned 11 -> 29), is 15 external applications + assembly
   honestly under 22? If not, the design must propose factoring — check it
   does, and that its factoring (if any) is itself sound. Never accept a
   cap inflation.
10. **Seeding-package exactness.** The add-external list must carry all 15
    dep contracts byte-verbatim at literal `proofs/<dep-id>` paths, plus
    every definition consumed; enumerate the TEXTBOOK THEOREMS the skeleton
    silently invokes (the Wedderburn/Stinespring omission cost a 37-node
    balloon — FINDINGS.md 2026-08-08). A missing external that forces a
    prover re-derive = finding.
11. **Guard-release scope.** Landing releases ONLY the K-ledger
    DO-NOT-REWIRE guard (W78 D4). Any edit to `op-classical`, any root
    route change, any claim beyond the guard release = REJECT.
12. **Landing-manifest completeness (Rule 9; the rescope-v2 audit's finding
    4 is the cautionary precedent).** UNWIRED.md additions, provenance
    honesty on the replaced shard, generated projections, sketch/HANDOFF/
    worklog — anything stale = finding.

## Verdict format

Write EXACTLY ONE file:
`docs/plans/2026-08-08-KLEDGER-STRENGTHENED/AUDIT-KLEDGER-STRENGTHENED.md`,
headed by one of:
- `VERDICT: LAND` (no corrections),
- `VERDICT: LAND-WITH-EXACT-CORRECTIONS` (list each correction as an exact
  old-string/new-string pair; only corrections you have VERIFIED restore
  soundness),
- `VERDICT: REJECT` (state the fatal flaw first, then all other findings).

Then a numbered findings list, most severe first, each with the exact locus
(file + section/line) and a one-sentence consequence. Explicitly dispose
EVERY item of the design's own ranked-risk list AND every attack above.

## Discipline (non-negotiable)

Write ONLY the verdict file. Do NOT edit the design, the registry,
`definitions/`, `proofs/`, or anything else. Do NOT run git commit or git
push. Do NOT run `af` mutations. Your final message: the verdict line plus
your top three findings in <=6 lines.
