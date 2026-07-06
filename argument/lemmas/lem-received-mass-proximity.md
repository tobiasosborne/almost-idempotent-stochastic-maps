---
id: lem-received-mass-proximity
kind: lemma
contract: Received-mass proximity: for an exact signed idempotent P, any row index i with nu_i = sum_j max(-P_ij, 0), and any nonempty index set A with sigma_A = sum over j in A of max(P_ij, 0) > 0, one has dist_1(p_i, conv{p_j : j in A}) <= (2 + 4*delta(P))*(1 + 2*nu_i - sigma_A).
defs: def-signed-idempotent; def-negative-mass
deps: lem-mass-split
status: proved
af: none
provenance: W35 wave (docs/waves/2026-07-07-W35-absorption.md): fresh-codex prover (worker AC) + SEPARATE fresh-codex hostile verifier (VAC, VALID — the balance identity sum_{j in A} P_ij^+ (p_j - q_A) = 0 expanded, coefficient bookkeeping 1 + 2*nu_i - sigma_A checked, sigma_A <= 1 + nu_i edge behavior checked; exact fixture on the W29 rank-5 frontier at three (i, A) pairs)
owner: A
workspace: proofs/lem-received-mass-proximity
---

**Role (receiving mass = proximity — the first absorption-family fact).** A row is close to
the convex hull of any set carrying most of its positive mass: subtract the A-barycenter q_A
from row reproduction; what remains has coefficient mass (1 + nu_i − sigma_A) + nu_i, each term
priced by the row diameter D = 2 + 4δ. Singleton form (body): P_ij⁺ ≥ 1 − ε gives
‖p_i − p_j‖₁ ≤ D(ε + 2ν_i). Feeds [[lem-single-heavy-recipient-rho-shadow]].

**Honest limit (the W35 gap, VAC-confirmed arithmetic).** At the cap-relevant scale
(sigma_A > 1 − θ − 4τ) the bound is ~ D(θ + 4τ + 2δ) > ρ even at θ = 0 — proximity alone
cannot reach the exposedness-exempt scale once the CS pincer has spent 4τ. The missing
absorption step is cluster-to-EXPOSEDNESS, not cluster-to-proximity (FINDINGS 2026-07-07 W35).

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
