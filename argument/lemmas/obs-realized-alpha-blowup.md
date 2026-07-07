---
id: obs-realized-alpha-blowup
kind: obstruction
contract: Realized alpha blow-up: for every eps in (0, 1/4] and t in (0, 1) there is an exact signed idempotent (an explicit 4x4: rows e1; (1 + eps*(1-t), 0, t*eps, -eps); e3; e4) with delta = eps and a hidden row vertex v = e1 such that EVERY optimal hiddenness dual witness of v has total alpha mass sum_i alpha_i = 1/eps.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: lem-zero-face-alpha-gauge
status: proved
af: none
provenance: W40 wave (docs/waves/2026-07-07-W40-two-primitives.md): worker AJ produced the LP-structural blow-up family; the hostile verifier VAL STRENGTHENED it by exhibiting the exact signed-idempotent realization (P^2 = P, row sums 1, delta = eps; exact recomputation at eps = t = 1/100: v hidden, t*(v) = 1/100, A_min = 100)
owner: A
workspace: proofs/obs-realized-alpha-blowup
---

**Role (a wall: LP alpha mass is unbounded inside exact idempotents).** The witness's free ray
cannot be gauge-fixed in general: a thin zero-face row (a near-clone of v INSIDE the optimal
exposer's zero face, displaced by eps along a direction the far rows must cancel) forces
alpha = 1/eps. Any aggregation/alpha-control argument for [[conj-near-cluster-absorption]]
must therefore consume EXTRA structure of the tall heavy-cluster mode (candidates: the
alpha-slab leakage bound controls alpha OFF the top slab in tall regimes; the blow-up row here
sits ON the zero face — the open question is whether blow-up survives the tall-cluster
hypotheses) — or avoid witness aggregation altogether. Do not attempt LP-only alpha bounds
(this instance is the death certificate).

**Rigour tier.** Exact realized instance ([T0] facts about itself), independently recomputed
by the hostile verifier; the shard's universal statement quantifies over the explicit family
only. NOT af-validated.
