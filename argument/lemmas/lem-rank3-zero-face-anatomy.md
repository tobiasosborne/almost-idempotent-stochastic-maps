---
id: lem-rank3-zero-face-anatomy
kind: lemma
contract: Rank-3 zero-face anatomy: for a rank-3 exact signed idempotent P with delta(P) > 0 and nonempty visible set, and a hidden geometrically distinct row vertex u with 0 < t*(u) < inf whose always-tight hulls are disjoint: every optimal exposer has the SAME linear part chi_1/M, where chi_1 is the edge functional of one extreme ray R_1 of the planar displacement cone at u and M = max_j chi_1(p_j - p_u) is attained on O; t*(u) = (min over far rows of chi_1)/M; T = argmin_far chi_1; O = argmax chi_1; the always-tight zero face Z is exactly the set of nonclone rows on R_1, each with ||p_z - p_u||_1 < 4*tau; and the hulls intersect if and only if gap_2 := t*(u)*(min over O of chi_2) - (max over T of chi_2) <= 0, chi_2 the opposite edge functional; whereas if some optimal exposer has both cone coefficients positive, Z contains no row with p_z distinct from p_u and the hulls INTERSECT.
defs: def-signed-idempotent; def-exposed; def-visible-set; def-negative-mass
deps: lem-rank3-optimal-face-interval-reduction; lem-always-tight-dual-support; lem-optimal-face-conic-reduction
status: proved
af: none
provenance: W49-fable wave (docs/waves/2026-07-07-W49F-fable-deep-proofs.md): Fable author FP1 (Theorem 1 + the planar cone toolkit) + SEPARATE fresh-codex hostile verifier (VFP1, VALID-WITH-CORRECTIONS — W(P) nonempty added to the setting; dim D_u = 2 survives clone-collapse; strict separation from geometric distinctness; Z rho-near because far rows have h >= t* > 0; the (star) inequality rules out T above scaled O; all 9 fixture vertices recomputed independently with whole-face tightness)
owner: A
---

**Role (disjointness has ONE shape at rank 3).** Failure of the terminal intersection forces
a completely rigid picture: unique edge exposer, zero face on one short extreme ray, T pinned
below scaled O. Everything about the (T1) horn at rank 3 reduces to the geometry of this
picture ([[lem-rank3-zero-face-min-mass]], [[conj-rank3-cluster-zero-face-reach]]).
