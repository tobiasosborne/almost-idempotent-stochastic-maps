VERDICT: 4/10 VALID
conj-sl1a-deep-diagonal-cell.md — VALID-WITH-CORRECTIONS — overlaps earlier cells and leaves essential vocabulary implicit
conj-sl1a-intersection-diagonal-cell.md — VALID-WITH-CORRECTIONS — overlaps the off-diagonal cell and leaves essential vocabulary implicit
conj-sl1a-off-diagonal-cell.md — VALID-WITH-CORRECTIONS — canonical contract uses undefined shorthand
lem-affine-barycenter-identity.md — VALID — exact affine identity with no nonlinear overclaim
lem-clone-invariant-row-complexity.md — VALID — geometric counts and lexicographic attainment are correct
lem-radial-horn-partition.md — VALID — exhaustive boundary-owned partition with corrected Proposition-E wording
lem-sl1a-corner-ledger.md — VALID-WITH-CORRECTIONS — exact ledger proof but non-standalone canonical contract
lem-sl1a-score-selector.md — VALID-WITH-CORRECTIONS — exact selector proof but dangling SL1a shorthand
lem-sl1a-three-cell-reduction.md — VALID-WITH-CORRECTIONS — sound conditional reduction but false transient-extension note and contract defects
lem-zero-face-one-sixteenth-capacity-kill.md — VALID — proved dependency and one-sixteenth arithmetic check exactly

conj-sl1a-deep-diagonal-cell.md

1. Add guards \(M_X(B)\le1/8\) and \(M_I(B)<1/16\).
2. Define top support functionals and the optimal-face sets \(T(u),O(u)\) explicitly.
3. Expand all body-local shorthand in the canonical contract.

conj-sl1a-intersection-diagonal-cell.md

1. Add the guard \(M_X(B)\le1/8\).
2. Define top support functionals and the optimal-face sets \(T(u),O(u)\) explicitly.
3. Expand all body-local shorthand in the canonical contract.

conj-sl1a-off-diagonal-cell.md

1. Define “top support functional” explicitly.
2. Replace canonical-contract shorthand with the displayed kernel, corner, radial-cell, far, and co-top definitions.

lem-sl1a-corner-ledger.md

1. Replace `SL1a top datum` in the canonical contract with the body’s explicit hypotheses and definitions.

lem-sl1a-score-selector.md

1. Replace `putative SL1a counterexample datum` in the canonical contract with the fully quantified body hypotheses.

lem-sl1a-three-cell-reduction.md

1. Explicitly push the row-index measure forward to geometrically distinct row points.
2. Delete or appropriately qualify the unsupported claim that transient extension preserves \(W\) and \(H\).
3. Replace `\delta_0,qquad` with `\delta_0,\qquad`.
4. Expand the canonical conditional contract and synchronize line 48 with the new I/D branch guards.