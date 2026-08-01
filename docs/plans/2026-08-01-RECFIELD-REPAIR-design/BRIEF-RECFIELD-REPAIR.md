# BRIEF — recorded-field identification repair (aism-4kof; the M19-S2 countermodel)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation. Write your design to
`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md`.
It will be hostile-audited by a separate fresh agent and then user-ratified.

## The established defect (verifier-validated, run of 2026-08-01)

The amended M19-S2 contract (`argument/lemmas/lem-maincb-stage2-call-envelope.md`,
from `DESIGN-MAINCB-REPAIR-v2.md` sect-4) was REFUTED as worded by a fresh af
verifier cohort with an exact M_2 countermodel (evidence:
`proofs/lem-maincb-stage2-call-envelope/ledger/`, nodes 1.1.2 and 1.1.5.1
both VALIDATED as countermodels; root left pending). The three findings:

1. **ch-5db0cccd95d6fcc7 (the core defect).** The contract's conclusion
   asserts "M04 gives epsilon_U, epsilon_R <= W.L*epsilon", but the
   RECORDED field epsilon_U of the already-supplied reset state is a free
   datum: `lem-maincb-direct-corner-envelope` (M04, frozen T0) proves the
   corner A_U ADMITS an extended L^0*epsilon-C*-algebra bound; NO
   hypothesis identifies or rebinds the recorded field to that bound.
   Countermodel: exact ambient/map/reset data at epsilon=0 (d_U=0, unit
   error 0) with any recorded epsilon_U>0 — every displayed reset
   inequality holds while epsilon_U <= W.L*0 fails. Moreover epsilon_R is
   not even a field of the supplied U-reset state.
2. **ch-dfa6b07f88648996.** The scalar chain in the parked tree circularly
   assumed those bounds as antecedents.
3. **ch-70457b235e07bbb1 (in-tree repairable; context only).** A node
   refused to infer the unit clause of an extended t_2-inclusion, but the
   locked `def-extended-delta-inclusion` DOES carry it (consistent with
   AUDIT-MAINCB-REPAIR F1). Not a contract defect.

## Your task

Produce the MINIMAL contract-repair package that makes the affected rows
true and provable while keeping every downstream consumer derivable:

1. **Decide the repair shape** (state the trade-off, recommend one):
   (a) identification HYPOTHESES — e.g. "the supplied reset state's
   recorded epsilon_W is at most W.L*epsilon" (or "equals the corner's
   inherited defect witness") added where consumed; or (b) restate the
   conclusions over the ACTUAL corner defects M04 exports, dropping claims
   about recorded fields; or (c) a semantics clarification confined to how
   `def-maincb-reset-state` / `def-maincb-partition-state` recorded fields
   are BOUND at supply time (careful: def changes ripple — both defs are
   locked and consumed by banked T0 rows; a def amendment is a LAST
   resort and an explicit escalation).
   Read `definitions/def-maincb-reset-state.md`,
   `def-maincb-partition-state.md` and the v5 design's intent
   (`DESIGN-MAIN-STRUCTURE-v5.md` M19-S2/S3 rows and audit-v4 §3.1 "tied
   to the displayed A,w") before deciding.
2. **Survey the same pattern** in every not-yet-banked amended row and
   report a per-row verdict (defective as worded / sound):
   M19-S2, M19-S3 (identical "M04 gives ..." conclusion over recorded
   fields), M25 ("moreover epsilon_C <= W.K_call*epsilon"), M20 ("every
   atomic corner defect is at most W.L*epsilon"), M12 (its
   epsilon_U,epsilon_V <= t are HYPOTHESES — verify that reading), M21-M24,
   M26-M28, M18. The BANKED rows (now incl. M16
   `lem-maincb-stage2-raw-extension` and M19-R
   `lem-maincb-reset-invariant-preservation`, both T0 2026-08-01) are
   FROZEN — verify none of your repairs forces a change to them; if one
   would, STOP that route and flag it.
3. **Verbatim repaired contracts** for every row you find defective — one
   physical ASCII line each, typed-witness laws i/ii
   (`docs/LEARNINGS.md` 2026-07-28), no numerical constants, every
   consumer/producer interface re-checked clause-by-clause (esp.
   M19-S3 -> M12 unit forwarding, M25 -> M28, M20's comparison role).
4. **Budgets + re-seed guidance** for the repaired rows (M19-S2's parked
   evidence tree: which validated nodes survive; the countermodel nodes
   are archived-by-design in a re-seed).
5. **Dimension-freeness re-check** of the induction arithmetic under your
   repair (the RI/UI invariants and the W-ledger interfaces are already
   T0-anchored via M19-R — do not disturb them).
6. **Honest risk register**: per repaired row, what a hostile verifier
   attacks first; top three ways this design could be wrong.

## Hard constraints

- No registry mutation; design doc only. One physical line per contract.
- No T0 invalidation (the frozen set now includes the three new bridge
  rows, M16, and M19-R — list what you checked).
- Ground truth: exact `refs/` loci only
  (`refs/kitaev-2405.02434/approximate_algebras.tex`; the induction is at
  `:1414-1444`). If a needed fact is not there, flag it — do not design
  around it (L1).
- Minimality: the smallest change that makes the rows true AND their
  consumers derivable. Say explicitly per row why no smaller change works.
