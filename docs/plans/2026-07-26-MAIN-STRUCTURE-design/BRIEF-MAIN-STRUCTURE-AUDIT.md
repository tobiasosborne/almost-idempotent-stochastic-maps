# BRIEF — hostile audit of DESIGN-MAIN-STRUCTURE.md (second stage, fresh verifier)

You are a fresh, independent, HOSTILE auditor. You did NOT write
`DESIGN-MAIN-STRUCTURE.md` and must assume it is wrong until proven otherwise.
It makes five strong DEFECT claims against the v4.1 proposed factoring and
proposes seven helper rows to repair them. Both directions need attack:
a falsely-claimed defect wastes a redesign; a falsely-sound repair wastes an
elevation campaign. Finding an error in EITHER direction is a BIG SUCCESS.

## Your target

`docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE.md`.

## Audit against (read all)

1. `docs/plans/2026-07-26-MAIN-STRUCTURE-design/BRIEF-MAIN-STRUCTURE.md`
   (what was asked).
2. `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md`
   §2.4 rows 221–228, §3.3, §4.1, R17–R23, R36.
3. `refs/kitaev-2405.02434/approximate_algebras.tex` — CHECK EVERY CITED LOCUS
   (esp. 1325–1359, 1414–1450, 1542–1557) against what the design claims.
4. The landed shards it cites as authoritative:
   `argument/lemmas/lem-extcb-four-corner-merge.md`,
   `lem-extcb1-close-corner-dimension.md`, `lem-extcb-corner-dimension-additivity.md`,
   `lem-maincb-error-improvement.md`, `conj-extcb.md`,
   `lem-extcb-exact-target-correction.md`.

## Specific attack surface

- **Defect claim 1 (four-corner bijectivity):** does
  `lem-extcb-four-corner-merge`'s landed contract really require four
  bijective corner maps, and is the design right that a direct-sum source
  cannot supply them? Or does some reading of the v4.1 row avoid the defect?
- **Defect claim 2 (binary merge non-iterability):** is the v4.1 recombination
  really inapplicable at ≥3 classes, or does an implicit union-class reading
  rescue it?
- **Defect claim 3 (zero-corner transport):** is the compressed-target
  transport genuinely missing from the proposed dependencies?
- **Defect claims 4–5 (threshold omissions; assembly producers):** verify
  against the landed IMPROVE-CB contract and the v4.1 reset rows.
- **The seven helper rows:** for each, is the claimed source locus sufficient
  (esp. the direct-sum inclusion merge from TeX 1325–1359 + 1542–1557, the
  generic close-corner transport claimed NOT-IN-LOCAL-REFS-as-contract but
  elementary)? Is any helper secretly circular (forward-referencing a
  threshold its consumer produces — the design itself states this rule)?
- **Hazard adjudications (R19/R21/R22)** in §4: recheck the claimed strict
  measure, the induction separation, and the zero-datum production.
- **Dimension-freeness (§5):** attack the corrected threshold package; any
  entry of the finite minimum that is not universal is a ROUTE-LEVEL ALARM.
- **Landing order (§6):** is it well-founded (every step's inputs exist by
  the time it runs)?

## Deliverable — write `docs/plans/2026-07-26-MAIN-STRUCTURE-design/AUDIT-MAIN-STRUCTURE.md`

- Verdict per defect claim: CONFIRMED / REFUTED (show why) / OVERSTATED
  (state the correct weaker form).
- Verdict per helper row and per hazard adjudication: VALID /
  VALID-WITH-CORRECTIONS (exact) / REFUTED.
- Final disposition: REPAIR-CONFIRMED (v4.1 MAIN factoring must be replaced
  per this design, with any corrections) / DESIGN-REFUTED (v4.1 stands or a
  different repair is needed) / ROUTE-ALARM.
- Cite every check with exact loci.

## Hard constraints

- Write ONLY `docs/plans/2026-07-26-MAIN-STRUCTURE-design/AUDIT-MAIN-STRUCTURE.md`.
- No repairs beyond stating corrections; no status promotion; nothing here is
  rigorous. NOT IN LOCAL REFS discipline applies.
