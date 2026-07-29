# BRIEF v2 — S1-ENDGAME repair round (fix the audit's REDESIGN findings)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation. Read, in this order:
1. `docs/plans/2026-07-29-S1-ENDGAME-design/BRIEF-S1-ENDGAME.md` (the
   original constraints — ALL still binding);
2. `docs/plans/2026-07-29-S1-ENDGAME-design/DESIGN-S1-ENDGAME.md` (v1 —
   your starting point; keep everything the audit did not attack);
3. `docs/plans/2026-07-29-S1-ENDGAME-design/AUDIT-S1-ENDGAME.md` (VERDICT
   REDESIGN — Blocks A, B, C1; every finding must be repaired or refuted
   with a line-cited argument).

Write the complete repaired design to
`docs/plans/2026-07-29-S1-ENDGAME-design/DESIGN-S1-ENDGAME-v2.md` — a
SELF-CONTAINED replacement (same deliverables list as the original brief),
not a diff.

## Mandatory repairs

**R-A1 (the bialgebra antecedent).** The audit found A1 cannot supply the
standard bialgebra antecedent that the ACTUAL T0 contract of
`lem-topology-hopf-structure` requires: for a merely homotopy-associative —
or in our case NOT-EVEN-homotopy-associative — H-space, the coproduct need
not be coassociative. Kitaev's own proof (`approximate_algebras.tex:971-1040`)
deliberately AVOIDS full Hopf-algebra structure: read what `prop_H-group`'s
proof actually uses (the multiplication-induced coproduct on cohomology, the
primitive-element/associated-graded argument, and ONLY the first homotopy of
`homo_inverse` — tex:912). Redesign Block A so that every consumed T0
contract is consumed WITH ITS ACTUAL ANTECEDENTS (read
`argument/lemmas/lem-topology-hopf-structure.md`,
`lem-topology-kunneth-cross-product.md` again, byte-for-byte). If the T0
Hopf row genuinely cannot serve a non-coassociative coproduct, Block A must
either (a) derive the weaker structure it actually needs in its own rows
from Kunneth + the H-space axioms (price the extra nodes), or (b) propose a
NEW leaf `lem-topology-*` row with an honest contract and a `refs/` locus —
subject to the original brief's constraint 6 (no unavailable ground truth).
State explicitly which option you take and why.

**R-B1 (the typed same-map witness).** B1 combined the H-space, isolation,
index, and finite-CW results without a contract-level typed witness that
they all concern the SAME `breve-sigma` on the SAME `breve-calU`. This is
the exact defect family that sank the first 13e transport (see
`docs/plans/2026-07-28-13E-BINDER-design/BRIEF-13E-BINDER.md` for the
history and `argument/lemmas/lem-stage1-polar-constant-ledger.md` (A_5)-(A_8)
for the validated repair pattern: ONE explicit binder — "writing
(u_delta, h_delta) for the unique inverse of Pi_delta ..." — fixed in an
early clause, all later clauses referring to THAT object). Repair B1 the
same way: the contract must bind `breve-calU`, `breve-mu`, `breve-sigma`
ONCE via the explicit provider chain (the row-13 ledger tuple W and the
descent clauses of `lem-stage1-quotient-left-inversion` /
`lem-stage1-quotient-manifold-package` /
`lem-stage1-quotient-inversion-index-data` — read their ACTUAL contract
texts and check they export the same explicitly-bound object; where they
do, SAY so with the exact binding phrase; where they do not, add the
identification clause to B1's contract itself as a proved conjunct).

**R-C1 (the inversion-witness identity + budget).** Same repair pattern as
R-B1: C1 must consume B1's fixed class through the SAME explicitly-bound
inversion it uses for the A5-closeness step — no independently selected
inversion. Additionally the audit found C1's 11-node budget implausible:
FACTOR C1 (e.g. a separate row for the phase-lift-to-projection bridge
`P = (2I + U + U^dagger)/4` with its O(delta+eps) estimate, tex:929-935,
vs the rectification-transport wrapper) or reprice with a per-node
skeleton that a routine prover can land.

**R-C3 (locus).** Add `approximate_algebras.tex:458` (data-independent
big-O constants) to C3's provenance as the audit requires.

**R-M04 (the hand-off honesty).** The audit is right that G-S1 alone does
not make M19-S1..M28 eligible (M04 and the other MAIN pre-gate rows are
absent). Correct the hand-off section: completing these seven rows
discharges the G-S1 GATE only; the MAIN campaign additionally needs P0 +
M01-M18 per `DESIGN-MAIN-STRUCTURE-v5.md`. Do not overclaim.

**R-form.** Fix the two contract-form violations: A1's ambiguous
`bialgebra` term (use the precise structure actually proved/consumed) and
B1's untyped definite description (per R-B1).

## Unchanged from v1 (keep unless a repair forces a change)

The audit found: all cited Kitaev loci match (incl. `prop_delta_hominc`
at tex:1194-1196); all direct deps exist at proved/validated; the
rectification layer's product/unit transport claim is genuine; the
producer shapes match M19-S1/M15 clause-by-clause; zero new defs and zero
reference acquisitions — preserve these properties. Every original-brief
constraint (one-line ASCII contracts, typed-witness law, T0-only imports,
dimension-freeness, budgets vs cap 26, def-layer minimization, L1 source
discipline) remains binding.

Your final answer: a <=15-line executive summary — per-repair disposition
(fixed how / refuted why), any budget changes, and whether any NEW row or
def was added relative to v1.
