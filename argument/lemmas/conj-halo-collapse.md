---
id: conj-halo-collapse
kind: lemma
contract: Halo-robust height collapse: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), and hidden top vertex v of height H, let sigma be the invisible mass of v, sigma_g the halo-robust invisible mass (the positive coefficient mass v places on rows at ell-1 distance > tau/4 from conv W, tau = sqrt(delta)), and nu_v the row negative mass; then H * (1 - sigma_g) <= (sigma - sigma_g) * tau/4 + nu_v * (2 + 4*delta).
defs: def-signed-idempotent; def-height; def-visible-set; def-invisible-mass; def-negative-mass
deps: 
status: conjecture
af: seeded
provenance: docs/waves/2026-07-02-F2-sigma-cap-refuter.md (arm F wave 2, opus worker, [check] mechanism: split the row reproduction with halo recipients priced at tau/4 instead of H); verified exact and non-vacuous on the three certified instances of runs/2026-07-02-sigma-cap-refuter/ (halo_bound_check.py)
owner: A
workspace: proofs/conj-halo-collapse
---

**Arm F wave-2 candidate (status CONJECTURE).** The self-mass-immune refinement of the af-validated
[[obs-height-collapse]]: recipients inside the `τ/4`-halo of `C_W` are priced at their actual distance
(`≤ τ/4`) rather than the worst case `H`, so the bound stays non-vacuous even when raw `σ̃ ≥ 1` via
self/halo mass (see [[obs-sigma-halo-nonrobust]]). Same proof shape as the validated bound plus one
extra split of the positive mass into halo vs genuine pots.

**Role:** if af-validated, this replaces obs-height-collapse as the finisher bridge: together with a
halo-robust cap `σ̃_g ≤ 1 − c` (mechanism candidate: [[conj-no-free-frontier]]) it yields
`H = O(τ)` — the Kernel Conjecture's height cap. Elevation candidate NOW (small tree; the anti-splitting
gap is not inside this statement).
