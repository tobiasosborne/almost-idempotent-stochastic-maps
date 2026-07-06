---
id: lem-self-defect-shadow
kind: lemma
contract: Self-defect shadow: for an exact signed idempotent P and a row index v with P_vv < 1, writing nu_out = sum over {j != v} of max(-P_vj, 0), one has dist_1(p_v, conv{p_j : j != v}) <= (2 + 4*delta(P)) * nu_out / (1 - P_vv).
defs: def-signed-idempotent; def-negative-mass
deps: 
status: proved
af: none
provenance: W38 wave (docs/waves/2026-07-07-W38-self-cluster.md): fresh-codex prover (worker AG) + SEPARATE fresh-codex hostile verifier (VAG, VALID-WITH-CORRECTIONS — SHARPENED the numerator from nu_v to nu_out (the off-diagonal negative mass); the P_vv < 0 edge case checked (formula weakens gracefully); exact fixture: W29 row 3, dist = 1/2420 <= 405801/15920000)
owner: A
workspace: proofs/lem-self-defect-shadow
---

**Role (heavy self-loops shadow the vertex).** Renormalizing row reproduction off the diagonal:
(1−P_vv)(p_v − q) = Σ_{j≠v} P_vj⁻(q − p_j) with q the off-diagonal positive barycenter — the
distance from v to the other rows' hull is priced by the AMPLIFIED off-diagonal negative
budget ν_out/(1−P_vv). Honest limit (the W38 diagnosis): the amplification permits
1 − P_vv = O(τ) at ν = O(τ²), i.e. heavy self-loops at O(τ) distance — no standalone cap.
Composes with [[lem-sharp-vertex-visibility]] (a vertex FAR from the others' hull is visible):
a hidden vertex with 1 − P_vv small must have its shadow distance BELOW ρ — quantifying
exactly how self-loops hide. Brick for [[conj-near-cluster-absorption]].

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
