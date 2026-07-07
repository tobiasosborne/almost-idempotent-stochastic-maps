---
id: lem-affine-exposer-row-capacity
kind: lemma
contract: Affine-exposer row capacity: for an exact signed idempotent P, a row index i, an affine functional h with h(p_i) = 0 and 0 <= h(p_j) <= 1 for all rows j, any threshold eta >= 0, and any set F contained in {j : h(p_j) >= eta}: eta * sum over f in F of max(P_if, 0) <= nu_i, where nu_i is the row-i negative mass.
defs: def-signed-idempotent; def-negative-mass
deps: lem-row-zero-capacity; lem-harmonic-affine-bridge
status: proved
af: none
provenance: W47 wave (docs/waves/2026-07-07-W47-mechanism.md): fresh-codex prover (worker AY — direct composition: affine-in-position row values are P-fixed by the af-validated bridge, then the af-validated row-zero capacity applies with the generic threshold) + SEPARATE fresh-codex hostile verifier (VAY, VALID-WITH-CORRECTIONS — exact-signed-idempotent hypothesis made explicit; the capacity lemma's kappa is a generic threshold so the eta-renaming is legal for eta >= 0; box constraints consumed by capacity, not by the bridge)
owner: A
---

**Role (the L0-composition charging tool).** Both deps are af-validated; this corollary is
the form in which the capacity primitive meets the exposedness LP: any admissible exposer
h centered at row i charges i's positive mass on the eta-high slab against nu_i <= delta.
Instantiated at a zero-face row z of an optimal exposer h* (h*(p_z) = 0), it is the upper
half of the (T2) contradiction in [[lem-blocker-capacity-bridge]].

**Rigour tier.** Reviewed composition of two L0 lemmas (L5 as a shard; both deps validated —
near-mechanical af-elevation candidate).
