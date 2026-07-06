---
id: conj-near-cluster-absorption
kind: lemma
contract: (CONJECTURE) Near-cluster absorption: there exist universal a >= 4, theta_0 in (0,1), and delta_0 > 0 such that for every exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set W(P), and hidden top vertex v of height H > ((5a/4 + 3/2)/theta_0)*tau (tau = sqrt(delta)): the positive mass v places on its rho-near deep cluster satisfies sum over {j : ||p_j - p_v||_1 < 4*tau, dist_1(p_j, conv W) > a*tau} of max(P_vj, 0) <= 1 - theta_0.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-invisible-mass; def-height
deps: 
status: conjecture
af: none
provenance: W38 wave (docs/waves/2026-07-07-W38-self-cluster.md): the residual content of conj-low-slab-cap after the session-11 five-route convergence (FINDINGS 2026-07-07; sketch v9) — named by worker AG's gap analysis, VAG-confirmed consistency of the S = 1 - O(tau) pure cluster with all banked identities
owner: A
workspace: proofs/conj-near-cluster-absorption
---

**Role (THE remaining Route-A conjecture — the five-route convergence point).** Every
session-11 mechanism family bottoms out here: witness coupling (no λ↔P⁺ comparison), CS/pincer
(h = 0 mass invisible), the collapse family (one-directional), absorption/proximity (sub-scale),
dual certificates (wrong direction) — see sketch v9. Together with the far-mass machinery
(pincer + witness at a θ-split) this implies [[conj-low-slab-cap]], hence the full reviewed/
rigorous chain to the Kernel height clause and op-classical (modulo Kernel(i) rank ≥ 3 — which
shares this mechanism via the anchor tension — and trunk <2>7).

**Why it should be true (certified evidence, L3):** every certified true-hidden construction
has the cluster EMPTY (σ₄ ≡ 0, G₄ = ∅ — W29-X, W35-AD); the exact W36 transition family shows
absorption firing precisely when a heavy circuit partner enters the ρ-ball; no construction
with depth > 1τ has ever been realized (W20).

**Priced levers (sketch v9, none tried):** (a) the value-vs-Lipschitz conditioning lemma
(near-row LP comparability); (b) the W36 transition family as local model; (c) the
deepest-vertex extremal choice (kills the C_a^> escape); (d) the anchorless-witness tension
inside the cluster ([[lem-hiddenness-dual-witness]] at cluster vertices needs far barycenters
with anchors); (e) the quotient self-loop object ([[lem-self-defect-shadow]] is the first
brick).

**Status discipline.** A conjecture — promotes nothing; consumers carry it as a dep.
