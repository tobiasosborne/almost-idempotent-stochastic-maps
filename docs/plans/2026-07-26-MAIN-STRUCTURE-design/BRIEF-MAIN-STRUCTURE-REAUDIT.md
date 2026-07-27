# BRIEF — fresh hostile RE-AUDIT of DESIGN-MAIN-STRUCTURE-v2.md (third stage)

You are a fresh, independent, HOSTILE auditor. You did NOT write
`DESIGN-MAIN-STRUCTURE-v2.md` and you did NOT write the first audit. Assume
v2 is wrong until proven otherwise. The first audit killed the v4.1 MAIN
factoring AND the first repair's central assumption — expect the second
repair to hide defects too. Finding one in EITHER direction (a falsely-sound
repair row, or a first-audit failure that v2 claims to clear but does not) is
a BIG SUCCESS.

## Your target

`docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v2.md` —
an acyclic repair: helper rows (§3.1), the nested-corner comparison M07
(§3.2 with its derivation obligation), conditional structural producers
(§3.3), raw calls + corrected reset package + the G-S1 gate (§3.4), the
eight MAIN structural targets (§3.5), well-founded measures for R19/R21
(§4), a dimension-freeness audit (§5), a serial landing order (§6), a
disposition of first-audit findings (§7), and an escalation ledger (§8).

## Audit against (read all)

1. `docs/plans/2026-07-26-MAIN-STRUCTURE-design/AUDIT-MAIN-STRUCTURE.md` —
   the binding first audit. For EVERY failure/finding there, verify v2 §7
   genuinely clears it at the contract level, not by relabeling. A failure
   silently surviving inside a reworded row is the highest-value find.
2. `BRIEF-MAIN-STRUCTURE.md`, `DESIGN-MAIN-STRUCTURE.md` (same dir) — what
   was asked; what the first repair proposed; check v2 did not silently drop
   deliverables (per-row proof plans, hazard adjudications, IMPROVE-CB).
3. `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md`
   §2.4 rows 221–228, §3.3, §4.1, R17–R23, R36.
4. `refs/kitaev-2405.02434/approximate_algebras.tex` — CHECK EVERY CITED
   LOCUS (esp. 1325–1359, 1414–1450, 1542–1557) against what each M-row
   claims it supports.
5. The landed shards v2 lists as its only available leaves (§2): verify each
   IS landed, and that its contract says what v2 uses — most critically
   `lem-compcb-single-compression-transfer` (v2 claims its formula is the
   IDEAL-UNIT compression and therefore a DIFFERENT outer-compression
   transfer row is needed — verify both halves), `conj-extcb`,
   `lem-extcb-four-corner-merge`, `lem-extcb-exact-target-correction`,
   `lem-thmainext-conditional`, and the narrowed
   `lem-maincb-error-improvement` (lines 13–31: approximate codomain A, not
   B(H) — v2 §2 makes a load-bearing claim about exactly this).

## Specific attack surface (check each, then hunt beyond)

- **The nested-corner comparison (M07, §3.2).** This is the row the whole
  repair leans on (it replaces the four-corner bijectivity misuse). Work
  through the derivation obligation line by line: is the two-sided
  comparison actually derivable from the landed compression/corner rows at
  the stated loci, with universal constants? Is the comparison genuinely
  two-sided (both inclusions/estimates), and is it strong enough for every
  close-range argument that later rows run through it?
- **The outer-compression transfer (§3.1).** Is the Stage-2/3 compression
  formula (a) actually distinct from the landed ideal-unit form, (b)
  derivable from local sources at the cited loci, (c) consumed consistently
  by the rows that need it? If it is secretly the same formula, the row is
  dead weight; if it is underivable, the repair collapses — test both.
- **Conditional producers before the reset ledger (§3.3).** The first
  audit's circularity finding: verify the conditional corner-equivalence and
  cross-union rows really consume NO reset-ledger output (trace every
  hypothesis to an earlier M-row or a landed leaf). Any hypothesis of the
  form "a reset map with defect ≤ c₀t exists" hidden in a side condition is
  a REFUTATION.
- **The G-S1 gate (§3.4).** Verify NO M-row imports a constant, map, or
  existence statement from the three unlanded Stage-1 split producers
  (`lem-stage1-rectified-nontrivial-projection`,
  `lem-stage1-original-complementary-pair`,
  `lem-stage1-fresh-two-point-inclusion`) anywhere except after the declared
  gate in the landing order. A leaked import before the gate makes the plan
  non-executable.
- **The eight MAIN targets (§3.5).** For each: does its corrected contract
  close (all constants quantified, no "sufficiently small"), and does its
  proof plan use only earlier rows/landed leaves? Attack the recombination
  row's conditionality on the complete one-class family (v_C)_C — is
  "complete family" well-defined and produced by an earlier row, and does
  the induction terminate (R21)?
- **Well-founded measures (§4).** R19: is the strict refinement measure
  genuinely strictly decreasing at every recursive call (exhibit the call
  sites)? R21: are the one-class and cross-class inductions actually
  separated in the row structure, or only narratively?
- **Zero-corner transport (first-audit defect 3).** Where exactly does the
  zero/off-diagonal datum get produced in v2, and is it consumed everywhere
  the first audit said it was missing?
- **Dimension-freeness (§5).** Every entry of the corrected threshold
  package universal; any n-, block-count-, or stage-index-dependence is a
  ROUTE-LEVEL ALARM.
- **Serial landing order (§6).** Well-founded (every step's inputs exist by
  the time it runs), and consistent with G-S1.
- **Escalation ledger (§8).** v2 escalates contract corrections to the user.
  Check the list is COMPLETE: every landed-shard contract v2's rows need to
  read differently than currently landed must appear here. A missing
  escalation is a finding.

## Deliverable — write `docs/plans/2026-07-26-MAIN-STRUCTURE-design/AUDIT-MAIN-STRUCTURE-v2.md`

- Verdict per M-row, per hazard adjudication (R19/R21/R22), per first-audit
  disposition claim (§7), and for the landing order: VALID /
  VALID-WITH-CORRECTIONS (state them exactly) / REFUTED (show the defect
  concretely).
- Final disposition: REPAIR-CONFIRMED (land v2 with any corrections, gated
  on G-S1) / DESIGN-REFUTED (what fails; what a third repair must change) /
  ROUTE-ALARM (a genuine obstruction — describe it).
- Cite every check with exact loci.

## Hard constraints

- Write ONLY `docs/plans/2026-07-26-MAIN-STRUCTURE-design/AUDIT-MAIN-STRUCTURE-v2.md`.
  Touch nothing else.
- No repairs beyond stating corrections; no status promotion; nothing here
  is rigorous. NOT IN LOCAL REFS discipline applies.
