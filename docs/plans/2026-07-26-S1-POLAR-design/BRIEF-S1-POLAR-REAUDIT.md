# BRIEF — fresh hostile RE-AUDIT of DESIGN-S1-POLAR-v2.md (third stage)

You are a fresh, independent, HOSTILE auditor. You did NOT write
`DESIGN-S1-POLAR-v2.md` and you did NOT write the first audit. Assume the v2
design is wrong until proven otherwise. The v1 design also claimed to be
closable and the first audit still returned REDESIGN — expect v2 to hide
defects too. Finding one — a wrong formula, an unproved smoothness claim, an
unclosable guard, a circular dependency, a hidden dimension-dependence, a
misread locus, theorem content smuggled into a definition — is a BIG SUCCESS.

## Your target

`docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v2.md` — a nine-row
formula-level replacement for the `gap-stage1-polar-chart-contract`
reservation (§3), six corrected downstream rows (§5), an obligation ledger
for `lem-stage1-extra-fixed-class` (§6), a dimension-freeness audit (§7), two
definition shards (§8), and a claimed disposition of EVERY first-audit
finding (§9–10).

## Audit against (read all)

1. `docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR.md` — the binding
   first audit. For EVERY finding there, verify v2 §9 genuinely dispositions
   it (repairs it or refutes it with a proof), not merely claims to. A
   finding silently dropped or paraphrased away is itself a finding.
2. `docs/plans/2026-07-26-S1-POLAR-design/BRIEF-S1-POLAR.md` and
   `DESIGN-S1-POLAR.md` (what was asked; what v1 proposed) — check v2 did not
   silently narrow the deliverable.
3. `refs/kitaev-2405.02434/approximate_algebras.tex` — CHECK EVERY CITED
   LOCUS (TeX 407–440, 458, 560, 655–912, 943–955, esp. 758–807, 809–855,
   857–893, 895–912) against what each v2 contract claims it supports.
4. The smoothing sources v2 pins by SHA and txt-line (§1): Lee's smooth
   inverse/implicit function theorems C.34 (txt:31134–31299) and C.40
   (txt:31330–31380); Munkres Cor. 4.9 (txt:2055–2056), Thm 4.2
   (txt:1833–1905), Thm 5.11, Thm 3.10. Verify each locus exists, says what
   is claimed, and — critically — that its HYPOTHESES are actually delivered
   by the v2 rows that invoke it.
5. `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md`
   §2.4, §2.6, §4.1, R14/R35 — compound contracts, theorem-content-free
   definitions, no guessed radii, ≤12 nodes / depth ≤3.
6. Landed shards: `argument/lemmas/lem-stage1-exact-unit-rectification.md`,
   `lem-stage1-quantitative-inverse-function.md`,
   `lem-topology-quotient-manifold.md` — do the v2 deps use only what these
   contracts actually provide?

## Specific attack surface (check each, then hunt beyond)

- **The direct-smoothness claim (the load-bearing repair; §1 route +
  row `lem-stage1-smooth-unitary-polar-package`).** Attack hardest here:
  (a) Is f_V genuinely a polynomial map of finite-dimensional REAL vector
  spaces when the product is the RECTIFIED product ⋅ and the involution is
  only real-linear? (b) Does Lee C.40 apply as stated — is the implicit
  function equation in the exact form C.40 requires, with the invertibility
  hypothesis supplied by an earlier row (which one, and does its contract
  literally supply it at the needed points)? (c) Does Lee C.34 apply to the
  polar map — where is bijectivity + invertible derivative at EVERY point of
  the domain proved? (d) Is "no point or first derivative of any map is
  changed" a theorem or an assertion? (e) Does the U(1)-action smoothness
  follow, or is it asserted? (f) Do the DOWNSTREAM consumers (quotient
  manifold, H-space, Lefschetz rows) need smoothness of anything v2's row 8
  does not deliver (e.g. smoothness of μ, σ as maps INTO the manifold 𝒰 with
  its new smooth structure, vs into the ambient space)?
- **Ledger arithmetic (`lem-stage1-polar-constant-ledger`).** Recompute every
  displayed implication from the displayed minima: r_− ≥ 3δ*/4; η ≤ δ*/4;
  q < r_−; C_path·q ≤ 1/4; C_der(ε_r + r_iso) ≤ κ_der; the final
  C_der(r_iso+ε_r) ≤ κ_der/4 < 1; and the compatibility of ε*^r with ALL
  eight guard inequalities simultaneously. An arithmetic slip here poisons
  every downstream row.
- **Self-containment.** The first audit's compound/non-closed complaint: is
  every v2 `contract:` cell truly closed — no reliance on §2 notation, no
  "where clauses" that live outside the cell, no constant used before it is
  quantified inside the same contract?
- **Dependency structure.** Is the 9-row DAG acyclic and well-founded? Does
  row 8 (smooth upgrade) secretly need the ledger row (row 9) or vice versa?
  Does any row exceed the 12-node/depth-3 projection honestly?
- **The six downstream contract repairs (§5) + obligation ledger (§6).**
  Check `lem-stage1-extra-fixed-class`'s needs item by item against what the
  corrected contracts deliver. A silent shortfall here is the most dangerous
  possible defect. Also: do the six repairs touch any af-VALIDATED shard's
  contract (that would be a re-validation obligation v2 must declare)?
- **Definition hygiene (§8).** Does `def-stage1-polar-witness-data` or
  `def-approximate-unitary-space` assert any existence/inequality/map
  (R35)? Is the "existential witness by source convention TeX 458" move
  legitimate for ALL six constants, or does any constant require a specific
  value for the arithmetic in the ledger row to close?
- **Dimension-freeness (§7).** Hunt for dimension smuggled through: norm
  equivalence on finite-dimensional spaces, compactness, the direct-sum norm
  comparison (TeX 560), or Lee/Munkres theorems whose constants are
  manifold-dependent.

## Deliverable — write `docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR-v2.md`

- Verdict per proposed row (all 9), per downstream repair (all 6), per
  definition shard, and per §9 disposition claim: VALID /
  VALID-WITH-CORRECTIONS (state them exactly) / REFUTED (show the defect
  concretely).
- A final disposition: LAND (with any corrections) / REDESIGN (what must
  change) / ROUTE-ALARM (a genuine obstruction — describe it).
- Cite every check you performed with exact loci (file:line / TeX line /
  txt line).

## Hard constraints

- Write ONLY `docs/plans/2026-07-26-S1-POLAR-design/AUDIT-S1-POLAR-v2.md`.
  Touch nothing else.
- Do not repair the design beyond stating corrections; do not promote any
  status; nothing here is rigorous.
- If a needed fact is not in the local sources, say NOT IN LOCAL REFS — do
  not fill from memory.
