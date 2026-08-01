# BRIEF — hostile audit of DESIGN-MAINCB-REPAIR.md (fresh verifier)

You are a fresh, independent, HOSTILE auditor. You did NOT write
`DESIGN-MAINCB-REPAIR.md` and must assume it is wrong until proven
otherwise. It repairs two verifier-established interface defects in the
MAIN campaign with: (a) contract-level unit clauses threaded through
M12/M19-S3/M25/M26/M19-R plus TWO new unit-helper bridge rows, and (b) one
new data-only `def-maincb-witness-ledger` plus 17 amended and 3 new result
contracts. Both directions need attack: an under-repaired contract re-parks
the trees after an expensive re-seed; an over-strong hypothesis makes a row
unusable by its consumers or vacuous. Finding an error in EITHER direction
is a BIG SUCCESS. The design's own §10 lists its three most likely failure
modes — attack those FIRST, then everything else.

## Your target

`docs/plans/2026-08-01-MAINCB-REPAIR-design/DESIGN-MAINCB-REPAIR.md`.

## Audit against (read all)

1. `docs/plans/2026-08-01-MAINCB-REPAIR-design/BRIEF-MAINCB-REPAIR.md`
   (what was asked — check every deliverable and every hard constraint).
2. `docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md`
   (the ratified design being amended) and its audits v3/v4/v5.
3. `refs/kitaev-2405.02434/approximate_algebras.tex` — CHECK EVERY CITED
   LOCUS (esp. 1194–1196 prop_delta_hominc's third clause and its PROOF;
   1317–1319; 1325–1359; 1414–1444; 1557) against what the design claims.
4. The frozen T0 shards (`argument/lemmas/lem-maincb-*.md` with
   `af: validated` — 14 rows) and the parked workspaces
   `proofs/lem-maincb-cross-class-merging-datum/`,
   `proofs/lem-maincb-stage1-call-envelope/` (do the amended contracts
   actually answer the verifier findings recorded in those ledgers?).
5. The W93 precedent: `definitions/def-stage1-polar-witness-data.md`,
   `lem-stage1-polar-scalar-arithmetic` / `lem-stage1-polar-constant-ledger`
   contracts, `docs/LEARNINGS.md` 2026-07-28 laws i/ii.
6. `definitions/def-maincb-*.md`, `def-four-corner-merging-datum.md`,
   `def-extended-delta-inclusion.md`, `def-extcb-datum.md`; the extcb/compcb
   block contracts for what M25's claimed v_+ unit control actually is.

## Specific attack surface

- **The two new unit-helper bridge rows (§1.3):** is the isomorphism-unit
  theorem TRUE at a universal scale with the design's proposed proof route
  (bijectivity transferring approximate left-unit action)? Is the
  compressed-corner comparison strong enough for BOTH consumers it claims
  (the Stage-1 old-side unit and M09's two-compression map)? These are the
  design's own top-two risks — try to produce a counterexample or a
  dimension leak.
- **M19-R same-witness identity (§10.3):** the design applies
  prop_delta_hominc's third clause to a specific M02 iterate and claims
  bijectivity of THAT iterate. Check against the actual M02/M03 landed
  contracts (frozen): does the quantified output of M03 let the contract
  name the same witness, or is the anaphor defect merely relocated?
- **The witness ledger (§2):** is it genuinely DATA-ONLY (no smuggled
  positivity/inequality/existence assertion — the R35 test that
  def-stage1-polar-witness-data passed)? Is the field list COMPLETE (every
  anaphoric constant in every amended contract resolved through it — grep
  each of the 17+3 contracts for any residual unquantified anaphor)? Is any
  field secretly analytic (a derived scale asserted positive)?
- **The binder/arithmetic rows (§3):** DAG-check the claimed acyclicity
  (M19 rows not depending on M18; transports not cyclic). Verify law ii
  compliance: providers fix witnesses FIRST; receivers transport by
  monotonicity.
- **The 17 amended contracts (§4):** clause-by-clause against their
  DESIGN-MAIN-STRUCTURE-v5 ratified forms — is every change necessary
  (minimality) and sufficient (the parked verifier findings actually
  discharged)? Do consumer/producer interfaces still match clause-by-clause
  (esp. M19-S3 -> M12, M16 -> M25, M26 -> M27, M25/M27 -> M28)?
- **No-T0-invalidation (§6):** independently verify that NO amended
  contract or new row forces any change to a validated row's contract or a
  byte-matched external in a validated workspace. Any violation is a
  ROUTE-LEVEL ALARM.
- **Dimension-freeness + induction arithmetic (§7):** attack the constants
  table under the rebinding; any entry not universal, or any class-count /
  stage-index / amplification dependence, is a ROUTE-LEVEL ALARM. Recheck
  the RI invariant arithmetic line by line.
- **Re-seed budgets (§8) and landing order (§9):** is the order
  well-founded (every row's deps exist by the time it runs, incl. the two
  bridge rows landing BEFORE any re-seed)? Are the node budgets plausible
  against the cap 26?

## Deliverable — write `docs/plans/2026-08-01-MAINCB-REPAIR-design/AUDIT-MAINCB-REPAIR.md`

- Verdict per section: VALID / VALID-WITH-CORRECTIONS (state the exact
  corrected text) / REFUTED (show why).
- Verdict per amended/new contract (all 20 + the def + the 2 bridge rows):
  same scale.
- Final disposition: DESIGN-CONFIRMED (ready for user ratification, with
  any exact corrections listed) / DESIGN-REFUTED (which defect remains
  open and why) / ROUTE-ALARM.
- Cite every check with exact loci (file:line).

## Hard constraints

- Write ONLY `docs/plans/2026-08-01-MAINCB-REPAIR-design/AUDIT-MAINCB-REPAIR.md`.
- No repairs beyond stating exact corrections; no status promotion; nothing
  here is rigorous. NOT-IN-LOCAL-REFS discipline applies (L1): if a claimed
  ground truth is not at the cited locus, that is a FINDING, not something
  to patch around.
