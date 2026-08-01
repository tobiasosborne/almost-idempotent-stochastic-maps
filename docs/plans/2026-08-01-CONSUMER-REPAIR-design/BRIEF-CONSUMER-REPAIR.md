# BRIEF — the consumer-chain repair round (aism-mc54): M26/M27 hypothesis restore + M19-R output typing

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation; do NOT run git commit, git push, fr, or bd. Write to
`docs/plans/2026-08-01-CONSUMER-REPAIR-design/DESIGN-CONSUMER-REPAIR.md`.
A fresh hostile audit and user ratification follow.

## The two verifier-established findings (2026-08-01)

**F-A (M26/M27 missing hypothesis).** The ratified ENV-form M26
`lem-maincb-binary-block-merge` omits "with one-dimensional atomic images"
from its w-hypothesis, but its deps require it: M19-S3's contract
hypothesizes it and `lem-maincb-cross-datum-bijectivity` requires "w:C^m->A
with one-dimensional images P_j" (M26 evidence:
`proofs/lem-maincb-binary-block-merge/ledger/`, ch-c393331c4b1ad7da,
ch-bc46dcefe4c24c51). The pre-ENV v5-era M26 HAD the clause; the RECFIELD
rewrite (`DESIGN-RECFIELD-REPAIR.md` sect-3) dropped it. M27
`lem-maincb-stage3-finite-recombination` (same rewrite) also omits it and
consumes M26.

**F-B (M19-R output typing).** `def-maincb-reset-state` types d_R as a
recorded NUMBER plus a hypothesis tag (data-only, R35). So M19-R
`lem-maincb-reset-invariant-preservation` (T0, banked 2026-08-01), whose
conclusion reads "...produces an error-improved map v_R:B_R->A_R satisfying
d_R <= W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}|| <= W.c0_cb*epsilon_R,
preserving bijectivity...", does NOT export the analytic fact its consumers
need: that v_R IS an extended (W.c0_cb*epsilon_R)-inclusion (resp. extended
isomorphism when u_R is bijective). M21 and M23 both parked on exactly this
(M21: ch-badf51f17e1eba66, ch-3252308f0b77411e; M23: ch-0c8c4a8212a96fab,
ch-03d8796a2b6adab2 — read all four in the parked ledgers).

## Your task

1. **F-A repair:** the corrected M26 and M27 contracts (one physical ASCII
   line each) restoring the one-dimensional-atomic-images hypothesis —
   minimal change, everything else byte-identical to the ratified ENV
   forms. Verify M27->M28 and M26->M27 interfaces still match.
2. **F-B repair decision + contracts.** The default expectation
   (state the trade-off, recommend explicitly): **strengthen M19-R's
   conclusion** to add "...and v_R is an extended
   W.c0_cb*epsilon_R-inclusion, and an extended isomorphism when u_R is
   bijective" (or your better wording), then RE-VALIDATE M19-R — the
   M02-STRENGTHENED precedent. Evidence it is provable: M19-R's own
   validated tree derives v_R as M02's literal iterate typed as an
   extended K_floor*epsilon_R-inclusion (read
   `proofs/lem-maincb-reset-invariant-preservation/export.md`), the
   monotonicity micro-row `lem-maincb-extended-inclusion-monotone` (T0)
   lifts K_floor <= W.c0_cb, and M25's banked tree derived the same
   typing in-line (`proofs/lem-maincb-one-class-extension/export.md`).
   CASCADE CHECK: M19-R currently has NO banked consumer (M25 used it but
   derived the typing itself — verify M25's validated tree does not
   byte-import the old M19-R contract string in a way the strengthening
   would invalidate; dep externals quote the dep contract, so check
   whether a dep-contract change stales M25's registered external and
   state the consequence honestly — if M25 would need re-validation,
   count that cost in your recommendation vs option (b) a same-witness
   bridge row).
3. **Survey:** M21, M22, M23, M24, M28 — per-row verdict: does the
   ratified contract stand as-is once F-A + F-B land (expected yes for
   all five; the M21/M23 issues were F-B + in-tree)? Note M21's in-tree
   hygiene items (t-binding ch-497c658458dedf3a, the u_0 producer
   hypotheses ch-2ba51f6789c8a046) as re-seed guidance, not contract
   changes — unless you find otherwise.
4. **Budgets + re-seed guidance** for: M19-R re-validation, M26, M27,
   M21, M23 (which parked nodes survive).
5. **Risk register**: per repaired row; top two ways this could be wrong.

## Hard constraints

- Contract changes ONLY to: M26, M27 (F-A) and M19-R (F-B, if you
  recommend strengthening). NO def changes. The other 18 banked
  T0 MAIN rows are FROZEN (M19-R's own re-validation is the sanctioned
  exception under the M02 precedent — it is currently T0; flag its
  temporary demotion honestly).
- Typed-witness laws i/ii; dimension-free; exact refs/ loci (L1);
  one physical ASCII line per contract.
