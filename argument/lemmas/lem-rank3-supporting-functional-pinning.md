---
id: lem-rank3-supporting-functional-pinning
kind: lemma
contract: Rank-3 supporting-functional pinning: in the disjoint edge case of lem-rank3-zero-face-anatomy, every affine psi with psi >= 0 on all rows and psi(p_u) = 0 satisfies psi(p_f) <= t*(u)*psi(p_i) for every f in T and i in O, with strict inequality exactly when the linear part of psi has positive transverse component (equality only for nonnegative scalar multiples of the optimal exposer, including zero); contrapositively, ONE supporting functional with psi(p_f) > t*(u)*psi(p_i) certifies hull intersection; at a hidden top u with t*(u) < kappa and H >= (1/2 + delta)*tau, disjointness forces every always-tight far row to be co-top (depth d_f > H - (1/2 + delta)*tau) and any visible row in T certifies intersection.
defs: def-signed-idempotent; def-exposed; def-visible-set; def-height
deps: lem-rank3-zero-face-anatomy
status: proved
af: none
provenance: W49-fable wave (docs/waves/2026-07-07-W49F-fable-deep-proofs.md): Fable author FP1 (Theorem 3 + Corollary 3.1) + VFP1 (VALID — the a-part cancels EXACTLY on T x O; the strictness wording corrected to the positive-transverse-component form; co-top forcing and visible-row exclusion sound)
owner: A
---

**Role.** Disjointness is pinned against EVERY supporting functional at once — the overlap
certificate is one functional beating the t* ratio. At tall tops, disjointness forces the
whole tight-far family into the summit slab.
