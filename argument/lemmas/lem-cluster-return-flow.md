---
id: lem-cluster-return-flow
kind: lemma
contract: Cluster return-flow: for an exact signed idempotent P, any row-index subset C, and s = P*1_C: P s = s and s_i = <p_i, 1_C> (affine-in-position); -delta <= s_i <= 1 + delta for every i; |s_u - s_v| <= (1/2)*||p_u - p_v||_1 for all rows u, v (the constant 1/2 is sharp); and if C is contained in the l1-ball of radius r around p_v, then sum over {k not in C} of max(P_vk, 0)*max(s_k, 0) >= s_v*(1 - s_v) - (r/2)*(1 + delta) - delta*(1 + 3*delta).
defs: def-signed-idempotent; def-negative-mass
deps: lem-harmonic-affine-bridge
status: proved
af: none
provenance: W48 wave (docs/waves/2026-07-07-W48-mechanism-bricks.md; ideation candidate 3, re-derived independently): fresh-codex prover (worker BA — corrected the ideation slack to r(1+delta) + delta(1+3delta) and the honest interpretive corollary A/M >= (m(1-m) - E)/(m + delta)) + SEPARATE fresh-codex joint hostile verifier (VBW, VALID-WITH-CORRECTIONS — uniformity constant sharpened from 1 to 1/2 via (p_u - p_v)*1 = 0, sharpness on I_2; return-flow slack improves accordingly to (r/2)(1+delta) + delta(1+3delta))
owner: A
---

**Role (heaviness propagates; return-flow is quantitative).** Cluster-mass uniformity
converts v-only heaviness into cluster-uniform heaviness for free (the W42 wall, mass
side); the return-flow inequality lower-bounds out-of-cluster positive mass weighted by
return fractions — a LOWER-bound-producing tool of exactly (F2)'s output type.
