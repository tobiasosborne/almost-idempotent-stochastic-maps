---
id: conj-rank3-cluster-zero-face-reach
kind: lemma
contract: (CONJECTURE) Rank-3 cluster zero-face reach (width-4 form): there exist universal theta_0 in (0,1), A_0 < inf, delta_0 > 0 such that for every rank-3 exact signed idempotent P with 0 < delta(P) <= delta_0 and nonempty visible set, every hidden top v of height H > 13*tau carrying >= 1 - theta_0 of its positive row mass on its width-4 top-slab cluster C_4, and every mass-carrying cluster vertex u in C_4 with 0 < t*(u) < kappa whose always-tight hulls are disjoint: some always-tight zero-face row z at u satisfies dist_1(p_z - p_u, span(R_2)) >= (1/2 + delta)*tau/A_0, R_2 the non-kernel extreme ray of the displacement cone at u.
defs: def-signed-idempotent; def-exposed; def-visible-set; def-height; def-negative-mass
deps: 
status: conjecture
af: none
provenance: W49-fable wave (docs/waves/2026-07-07-W49F-fable-deep-proofs.md): FP1's single missing statement, VFP1-approved in the width-4 corrected form (well-formed; Theorem 2 converts it into the bounded horn)
owner: A
---

**Role (THE rank-3 closer).** By [[lem-rank3-zero-face-min-mass]] this ALONE closes
[[conj-zero-face-elimination]] at rank 3 (bounded horn; theta-flexible). For: heaviness +
the pincer push cluster mass onto the kernel ray whose reach is in question; the downhill
dichotomy independently supplies a deeper near zero-face candidate; total reach collapse
flips into the generic case = forced overlap. Against: no tool lower-bounds near-row
displacements. Decisive data: the W52-BH pre-registered tall-entry experiment. NOTE: the
whole quantified domain is UNREALIZED (FINDINGS 2026-07-07 W49F) — tall-emptiness would
make this vacuous and close the node anyway.
