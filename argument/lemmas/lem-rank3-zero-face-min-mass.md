---
id: lem-rank3-zero-face-min-mass
kind: lemma
contract: Rank-3 zero-face minimum mass: in the disjoint edge case of lem-rank3-zero-face-anatomy with reach R = max over Z of chi_2(p_z - p_u) > 0, the minimum zero-face conic mass over all reduced optimal displays is EXACTLY A_min = gap_2/R; with the l1-normalized chi_2 (||chi|| = sup{|chi(x)| : x in D_u, ||x||_1 = 1}, so dist_1(x, ker chi) = |chi-hat(x)|) and u hidden (t*(u) < kappa): gap-hat_2 < (1/2 + delta)*tau and reach-hat < 4*tau; hence reach-hat >= (1/2 + delta)*tau/A_0 implies A_min < A_0.
defs: def-signed-idempotent; def-exposed; def-negative-mass
deps: lem-rank3-zero-face-anatomy
status: proved
af: none
provenance: W49-fable wave (docs/waves/2026-07-07-W49F-fable-deep-proofs.md): Fable author FP1 (Theorem 2) + VFP1 (VALID — chi_1-balance automatic, chi_2 the one scalar equation, attainment checked; the quotient-distance normalization made explicit; CROSS-CHECK: A_min = 100 on obs-realized-alpha-blowup matches the independently banked minimum reduced alpha mass EXACTLY; new exact values 12400000/292059 and 589861/141 verified)
owner: A
---

**Role (the bounded-horn trigger).** A_min = gap/reach converts the reach conjecture
([[conj-rank3-cluster-zero-face-reach]]) DIRECTLY into the bounded horn of
[[conj-zero-face-elimination]] at rank 3. The formula reproducing the banked 100 is the
strongest internal consistency check in the record.
