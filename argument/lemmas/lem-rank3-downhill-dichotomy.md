---
id: lem-rank3-downhill-dichotomy
kind: lemma
contract: Rank-3 downhill dichotomy: in the disjoint edge case of lem-rank3-zero-face-anatomy, for every affine psi with psi >= 0 on all rows and eps = psi(p_u) >= 0: either some always-tight zero-face row z has psi(p_z) < eps (a downhill zero-face row), or min over f in T of (psi(p_f) - eps) <= t*(u)*max over i in O of (psi(p_i) - eps); quantitatively min_T(psi - eps) <= t*(u)*max_O(psi - eps) + A_min*max(eps - psi(p_z*), 0), z* the psi-minimal zero-face row.
defs: def-signed-idempotent; def-exposed
deps: lem-rank3-zero-face-min-mass
status: proved
af: none
provenance: W49-fable wave (docs/waves/2026-07-07-W49F-fable-deep-proofs.md): Fable author FP1 (Theorem 4 + Corollary 4.1) + VFP1 (VALID — the proof honestly controls only min_T, so "some f in T" is the right non-top quantifier)
owner: A
---

**Role.** The only escape from the pinning at non-tops is a strictly deeper zero-face row —
priced by A_min. Feeds the reach conjecture's belief case (the downhill row as reach witness).
