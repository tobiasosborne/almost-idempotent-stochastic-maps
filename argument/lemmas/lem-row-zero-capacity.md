---
id: lem-row-zero-capacity
kind: lemma
contract: Row-zero capacity: for an exact signed idempotent P, a row index i, and any vector y with P y = y, 0 <= y_j <= 1 for all j, y_i = 0, and y_f >= kappa for all f in a set F, one has kappa * sum over f in F of max(P_if, 0) <= nu_i, where nu_i is the row-i negative mass.
defs: def-signed-idempotent; def-negative-mass
deps: lem-harmonic-affine-bridge
status: proved
af: seeded
provenance: W40 wave (docs/waves/2026-07-07-W40-two-primitives.md): fresh-codex prover (worker AK) + SEPARATE fresh-codex hostile verifier (VAL, VALID-WITH-CORRECTIONS — the hypothesis y_i = 0 made explicit; the converse row-local balancing construction kept as a body note with its free-anchor caveat; nu_i = 0 edge forces the F-mass to vanish)
owner: A
workspace: proofs/lem-row-zero-capacity
---

**Role (the general circuit-capacity threshold — the W36 mechanism as an inequality).** Any
harmonic (= affine-in-position, [[lem-harmonic-affine-bridge]]) candidate exposer vanishing at
row i pays for its kappa-margin on F out of row i's negative mass: 0 = (Py)_i splits into
kappa * (positive F-mass) <= nu_i. This is the necessary half of the W36 anatomy
(t* = anchors/far-mass) in general position; the row-local sufficient half (balancing row i
alone with anchor values kappa*B/nu_i in [0,1]) holds under free-anchor compatibility but is
NOT a full exposer construction (full margin-kappa feasibility is exactly non-hiddenness, by
LP duality of the exposedness program — the dual-direction wall, FINDINGS 2026-07-07).

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
