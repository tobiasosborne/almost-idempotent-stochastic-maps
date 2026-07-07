---
id: lem-harmonic-affine-bridge
kind: lemma
contract: Harmonic-affine bridge: for an exact signed idempotent P with rows p_i = (P_ij)_j, a vector g satisfies Pg = g if and only if there exists u with g_i = u . p_i for every row index i; in the forward direction u = g works (g_i = p_i . g), and the constant term of any affine representation is absorbable into u since all row sums equal 1.
defs: def-signed-idempotent
deps: 
status: proved
af: validated
provenance: W33 wave (docs/waves/2026-07-07-W33-harmonic-affine-bridge.md): fresh-codex prover (worker AA) + SEPARATE fresh-codex hostile verifier (VAA, VALID — index conventions checked against the def shard; exact fixture on the banked W19 rank-5: Pg = g and g_i = p_i . g verified entrywise); first-principles, two lines each direction
owner: A
workspace: proofs/lem-harmonic-affine-bridge
---

**Role (the structural fusion of the g-machinery with the exposer machinery).** Every
P-harmonic observable IS a linear functional of position: g_i = (Pg)_i = Σ_j P_ij g_j = p_i·g;
conversely affine-in-position vectors are harmonic by row reproduction + row sums. Clone-robust
automatically (coincident rows share values). Consequences: the g-bootstrap observable
g = P·1_{G_a} and the affine deficit ψ = H − φ live in ONE function class — the admissible-
exposer candidates — so hiddenness (t* < κ) constrains the exact functionals that define the
deep web. Consumed by [[lem-conditional-g-near-exposer]], [[lem-two-observable-pencil-bound]];
the W34 g-max self-consistency channel is built on it.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous; PRIME af-elevation candidate
(deps: none, two-line proof).
