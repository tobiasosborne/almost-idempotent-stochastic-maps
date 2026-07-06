---
id: lem-single-heavy-recipient-rho-shadow
kind: lemma
contract: Single-heavy-recipient rho-shadow: for an exact signed idempotent P with 0 < delta(P) <= 1/16 (tau = sqrt(delta)), if some row index j has P_vj^+ >= 1 - tau at a row index v, then ||p_v - p_j||_1 < 4*tau.
defs: def-signed-idempotent; def-negative-mass; def-exposed
deps: lem-received-mass-proximity
status: proved
af: none
provenance: W35 wave (docs/waves/2026-07-07-W35-absorption.md): fresh-codex prover (worker AC) + SEPARATE fresh-codex hostile verifier (VAC, VALID-WITH-CORRECTIONS — 0 < delta added for strictness (at delta = 0 the strict form degenerates, the distance is 0); the constant chain (1+2tau)(1+2tau^2) <= 27/16 < 2 at tau <= 1/4 verified symbolically)
owner: A
workspace: proofs/lem-single-heavy-recipient-rho-shadow
---

**Role (no lone mule: a single recipient of nearly all of v's mass sits INSIDE v's
exposedness-exempt ball).** Via [[lem-received-mass-proximity]] (singleton form,
ε = τ, ν ≤ τ²): ‖p_v − p_j‖₁ ≤ 2τ(1+2τ)(1+2τ²) ≤ 27τ/8 < ρ = 4τ. So a hidden vertex cannot
outsource its mass to ONE far row — the ρ-far set never sees a (1−τ)-heavy recipient. Any cap
counterexample must SPREAD its deep mass across several far recipients; combined with the
witness constraints this is the absorption question's surviving shape.

**Body addenda (VAC).** If W(P) is nonempty: d_j ≥ d_v − 4τ (1-Lipschitzness of dist₁(·, C_W));
if v is a height-attaining top, d_j ≥ H − 4τ — the heavy recipient inherits near-top depth.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
