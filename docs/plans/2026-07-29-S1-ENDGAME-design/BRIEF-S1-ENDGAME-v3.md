# BRIEF v3 — S1-ENDGAME repair round 2 (fix audit v2's REDESIGN findings)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation. Read, in this order:
1. `docs/plans/2026-07-29-S1-ENDGAME-design/BRIEF-S1-ENDGAME.md` (the
   original constraints — ALL still binding);
2. `docs/plans/2026-07-29-S1-ENDGAME-design/BRIEF-S1-ENDGAME-v2.md` (the
   round-1 repairs — their intent still binding);
3. `docs/plans/2026-07-29-S1-ENDGAME-design/DESIGN-S1-ENDGAME-v2.md` (v2 —
   your starting point; keep everything audit v2 did not attack);
4. `docs/plans/2026-07-29-S1-ENDGAME-design/AUDIT-S1-ENDGAME-v2.md` (VERDICT
   REDESIGN — findings F1-F8 fatal/correctable; every finding must be
   repaired or refuted with a line-cited argument).

Write the complete repaired design to
`docs/plans/2026-07-29-S1-ENDGAME-design/DESIGN-S1-ENDGAME-v3.md` — a
SELF-CONTAINED replacement (same deliverables list as the original brief),
not a diff.

## What audit v2 SETTLED (preserve; do not re-litigate)

- The Hatcher ground truth is LOCAL and VERIFIED: weak-Hopf conditions at
  `refs/hatcher-algebraic-topology/AT.txt:17654-17677`, Theorem 3C.4 at
  `:17798-17800` (F9/§1). Block A's mathematical strategy (R-A1) is REPAIRED —
  keep it, subject to R-F6/R-F7/R-F8 below.
- R-C3 (tex:458 provenance) and R-M04 (G-S1-only hand-off) are REPAIRED — keep.
- Deps are all T0 and acyclic; no dimension leak; zero new defs achievable
  (F11/F12/F13) — preserve these properties.

## Mandatory repairs (the audit-v2 §4 surface, expanded)

**R-F1 (B0b's manifold antecedent).** B0b concludes `breve-calU` is a
connected compact orientable smooth boundaryless manifold of dimension N-1,
but NO listed dep's root contract supplies that package: quotient-finite-cw
and finite-triangulation are CONDITIONAL on it, and local-index-sign requires
it (audit F1, with the five per-dep citations). The only existing root that
provides the package is `lem-stage1-quotient-manifold-package`. Repair: add
it as a DIRECT B0b dependency (preferred), or enlarge B0a's root contract to
export exactly those conjuncts — then RE-CHECK that the finite-CW and
local-index antecedents are now discharged clause-by-clause. Remember the
import law: a consumer may use a dep's ROOT CONTRACT only, never its
explanatory body or dependency closure.

**R-F2 (the estimate lost at the B0b→B1 boundary).** B0a's near-adjoint
estimate `||sigma(U)-U^dagger|| <= C_grp*epsilon_r` is consumed by B1 but
crosses B0b without being re-exported (audit F2). Repair: B0b's root
conclusion must contractually RE-EXPORT every B0a field/property that B1
consumes (the displayed map, its covariance, the near-adjoint estimate), OR
B1 must receive a genuinely parameterized package whose required conjuncts
are spelled in B1's own root. Follow the validated ledger policy: all
analytic predicates expanded in the root itself
(`argument/lemmas/lem-stage1-polar-constant-ledger.md:21-31`).

**R-F3 (free `r_bidx`).** B1 concludes `||U-J|| >= r_bidx` and
`||U+J|| >= r_bidx` with `r_bidx` neither existentially introduced in B1,
nor quantified as an input, nor destructured from B0b (audit F3 — a literal
naked symbol). Repair: B1's "writing" clause must explicitly bind the SAME
`r_bidx` supplied by B0b's package (name it as a destructured field), or B1
introduces its own existential radius. No free symbols in any contract.

**R-F4 (binder order + the anaphor purge).** B0b pre-uses the representative
`U_0` to name the quantified class (audit F4). Correct binder shape: "for
every fixed class `breve-U`, there exist a representative `U_0` and phases
`c,a` ... with `[U_0]=breve-U`." Globally: REPLACE every occurrence of "the
exact (displayed) witnesses supplied by [lemma]" — in B0b, B1, AND C0 — with
explicit quantification over ONE displayed package and the exact conjuncts
that package satisfies (the row-13 pattern: bind one universal tuple first,
then the unique/chosen objects of displayed maps). Non-unique existential
packages must NEVER be consumed by definite description.

**R-F5 (one C0/C1 architecture).** C1 currently selects a B1 package and
then "applies C0 to that exact package", but C0's root quantifies only an
exact-unit algebra — it has no package parameter (audit F5). Choose ONE
honest architecture and state it explicitly:
  (a) C0 is a PARAMETERIZED bridge: its root contract is conditional on a
      fully displayed B1-package (all conjuncts spelled), and C1 passes that
      package; or
  (b) C0 applies B1 exactly ONCE internally, exports only the resulting
      projection (+ its estimates), and C1 consumes C0 alone, never
      selecting B1 itself.
Either way, no dep is applied twice to select possibly-different witnesses.
Note: the explicit bridge formula `P=(2I+U+U^dagger)/4` with its
`O(delta+epsilon)` conclusion is at `approximate_algebras.tex:939` — fix any
`:929-935` shorthand to a range containing 939.

**R-F6 (Hatcher externals: exact printed statements).** Register the two
externals with EXACTLY what is printed at the loci (audit F6/§1.2):
- `GT-hatcher-weak-hopf-conditions` (`AT.txt:17654-17677`): connectedness
  plus the positive-positive coproduct-tail formula — NOT a `Delta(1)=...`
  clause;
- `GT-hatcher-hopf-structure-3C4` (`AT.txt:17798-17800`): exterior TENSOR
  POLYNOMIAL conclusion — NOT exterior-only.
A1's own contract/skeleton keeps the separately DERIVED `Delta(1)` clause,
the polynomial-factor exclusion (via finite total dimension), and the
finite-odd-generator argument as explicit A1 obligations (nodes already
exist for the first two; ADD the finite-generator node if missing). The
design prose must not describe the externals as stronger than their text.

**R-F7 (quantifier nits).** In A1's contract: state explicitly that a FINITE
family of positive-degree tails `a'_j, a''_j` exists; state once that the
coefficient field is the reals (write `reals` or declare `R = the real
field` inside the contract line). Mechanical; do not change content.

**R-F8 (honest budgets for A1 and B0b).** Benchmarks: the validated
hopf-structure row took 13 nodes FROM THE STRONGER standard-bialgebra
antecedent; quotient-index took 12; isolation took 7 (audit F8). A1 at 8/12
and B0b at 9/14 are NOT credible. Repair by FACTORING (preferred — e.g.
split A1 into a coproduct-construction row + an exterior-structure row;
split B0b's manifold/CW attachment from its phase-lift/index branches) or by
an honestly justified per-node plan a ROUTINE-tier prover can land, with
target ~<=12 per row (the original factoring rule; do not just raise hard
caps to conceal multi-obligation nodes). Repriced/factored rows must keep
the serial order consistent (audit F11's topological order) and update the
budget table.

## Unchanged constraints (binding as ever)

One-line ASCII contracts; typed-witness law (NO free symbols, NO untyped
definite descriptions); T0-only imports consumed with their ACTUAL root
antecedents; dimension-free constants; budgets vs cap 26 with the ~12
factoring rule; def-layer minimization (zero new defs unless forced — F13
says achievable); L1 source discipline (`\n`-only loci); the M19-S1
producer shapes and the G-S1-only hand-off exactly as v2 has them.

Your final answer: a <=15-line executive summary — per-finding disposition
(F1-F8: fixed how / refuted why), the new row count and budget table if
factoring changed it, and whether any NEW row, external, or def was added
relative to v2.
