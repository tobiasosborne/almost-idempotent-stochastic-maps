# Hostile audit — `cor-classical-sharpness` tightened skeleton

Date: 2026-08-09  
Role: fresh hostile auditor; finding a defect is a success  
Scope: design audit only; no claim is promoted

## Numbered findings, highest severity first

1. **HIGH — the final “equivalently” clause is not definitionally discharged.**
   **Exact locus:** `ADDENDUM-CORSHARP-SKELETON.md:97-124`, especially
   lines 118-124; repeated at lines 203-211.  The byte-frozen root at
   `argument/lemmas/cor-classical-sharpness.md:4` asserts both the explicit
   counterexample statement and “equivalently, no uniform exponent
   `beta>1/2` can replace `1/2` in `op-classical`.”  None of the three
   registered definitions, and no statement in the sole theorem external,
   defines the English phrase “can replace.”  Moreover `op-classical` is not
   an imported external.  Thus declaring the phrase to be “read here,
   definitionally” does not perform a definitional reduction available to an
   af verifier.  A verifier may correctly demand the content of aborted nodes
   1.5.1-1.5.2: an explicit expansion of the proposed uniform estimate and a
   quantifier-negation step.

   **Exact minimal correction:** keep the work inside node 1.4, but replace
   the asserted definitional reading by an explicit local expansion: for each
   fixed `beta>1/2`, “`beta` can replace `1/2`” means that there exist
   `C>0,eta_0>0`, independent of the dimension, such that for every dimension,
   every admissible `eta<=eta_0`, and every row-stochastic `Q` of defect at
   most `eta`, some stochastic idempotent `E` satisfies
   `||Q-E||<=C*eta^beta`.  Then state in the same node that the already
   constructed dimension-four witness, for arbitrary proposed `C,eta_0`, is
   the literal logical negation of that formula.  Do not cite or import
   `op-classical`, and do not create a separate wrapper branch.

2. **HIGH — the addendum records user ratification before the repository says
   that ratification has occurred.**  **Exact locus:**
   `ADDENDUM-CORSHARP-SKELETON.md:1`, the provenance append at lines 135-142,
   and the proposed Status block at lines 149-153.  The canonical
   `HANDOFF.md:34-45` says remedy (b) still requires “Fresh hostile audit +
   user ratification,” and its ranked next step is for the user to ratify the
   remedy.  A separate proof-strategy designer cannot supply that
   authorization.  Consequently `USER-RATIFIED`, the provenance text
   “user-ratified skeleton-tightening remedy,” and “This user-ratified ...
   addendum” are unsupported provenance claims at audit time.  The mathematical
   status remains honestly `stated`, and the 26-over-20 abort is honestly
   disclosed; the defect is the authorization claim.

   **Exact minimal correction:** until an explicit user ratification is
   recorded, replace those three ratification assertions by `PROPOSED /
   HOSTILE-AUDITED / PENDING USER RATIFICATION`, “hostile-audited proposed
   skeleton-tightening remedy (b), pending user ratification,” and “This
   hostile-audited proposed skeleton-tightening addendum,” respectively.
   After the user ratifies, those exact phrases may be mechanically changed to
   the dated user-ratified forms.

3. **MEDIUM — the designed-node budget omits the final-clause discharge
   obligation.**  **Exact locus:** `ADDENDUM-CORSHARP-SKELETON.md:126-128`.
   Under the attack-list rule that an implicit verifier-forced obligation
   counts, the English-to-formula/quantifier-negation discharge in finding 1
   is a sixth designed obligation even if its proof text is kept physically
   inside node 1.4.  The honest count is therefore root + nodes 1.1-1.4 + the
   final-clause discharge = **6**, not 5.  This does not break the cap:
   `6 x 3 = 18 <= 20`, but it leaves two slots, not five.

   **Exact minimal correction:** replace the budget paragraph by the count
   above and describe the final-clause discharge as an in-node designed
   obligation that must not become a separate af branch.

4. **MEDIUM — the MUST-NOT list does not forbid all of the run-1 quantifier
   branch expansion it claims to cure.**  **Exact locus:**
   `ADDENDUM-CORSHARP-SKELETON.md:32-35` permits internal refinement, while
   lines 207-226 forbid a separate equivalence wrapper but do not forbid
   separate children for cutoff positivity/minimum existence, the two strict
   `eta` endpoint checks, positive-real-power monotonicity, or counterexample
   packaging.  Those are precisely the nodes at
   `TREE-CORSHARP-ABORTED.md:21-31`; together with the wrapper they formed the
   recorded wide branch.  The current MUST-NOTs therefore leave most of that
   failure mode available.

   **Exact minimal correction:** add one MUST-NOT bullet requiring node 1.4's
   cutoff positivity and nonempty interval, `eta` endpoint checks, strict
   power inequality, reuse of nodes 1.2-1.3, counterexample packaging, and the
   explicit logical-negation sentence from finding 1 to appear as one linear
   justification with no child branches.  State that if a verifier will not
   accept that linear node, the run must abort and move to remedy (c), rather
   than regrow the run-1 branch.

## Checks producing no finding

- **Contract clauses before the final English equivalence:** nodes 1.1-1.4
  provide the required positive unital witnesses, row-stochastic
  `Q_lambda`, weak defect bound, per-`F` lower bound, and the strict
  per-`(C,eta_0,beta)` counterexample in the root's quantifier order.
- **Import fidelity:** the root statement of
  `proofs/lem-prh-sharpness/export.md:5` states exactly the existence and types
  of the positive unital maps, the equality
  `||M_lambda A_lambda-I_2||=2*lambda^2`, and the lower bound against every
  stochastic idempotent.  The addendum attributes no absent family fact to
  that external.
- **Weak/strict discipline and arithmetic:** all norm steps stay weak.  For
  `r=2*beta-1>0`, the strict choice
  `lambda<(C*2^beta)^(-1/r)` gives
  `C*2^beta*lambda^r<1`, hence
  `C*eta^beta=C*2^beta*lambda^(2*beta)<lambda`; combining this with the weak
  imported lower bound gives the required strict distance inequality.  The
  other cutoffs give `2*lambda^2<eta_0` and `2*lambda^2<1/4`.
  For every allowed `C,eta_0,beta`, all three cutoff terms are positive and
  finite, including as `beta` approaches `1/2` from above, so their minimum
  contains a positive `lambda`; large `C` and tiny `eta_0` cause no endpoint
  failure.
- **Replacement exactness apart from finding 2:** the proposed provenance
  line is the current line plus one appended clause, all other frontmatter is
  instructed to remain unchanged, `status: stated` remains honest, and the
  run-1 balloon is disclosed.

VERDICT: LAND-WITH-EXACT-CORRECTIONS
