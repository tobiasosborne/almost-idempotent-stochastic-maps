---
id: conj-no-free-frontier
kind: lemma
contract: No free frontier (exposedness absorption): for an exact signed idempotent P with 0 < delta(P) <= 1/4 and nonempty W(P), every row vertex that is extremal in some C_W-separating direction (a 1-Lipschitz affine functional nonpositive on conv W) and whose strictly nearer rows in that direction all lie within ell-1 distance rho = 4*sqrt(delta) of it is (rho,kappa)-well-exposed with kappa = sqrt(delta)/4.
defs: def-signed-idempotent; def-visible-set; def-exposed; def-negative-mass
deps: 
status: conjecture
af: none
provenance: docs/waves/2026-07-02-F2-sigma-cap-refuter.md (arm F wave 2, opus worker, [check] wall mechanism "no-free-frontier / exposedness-absorption", transcribed to a single statement by the orchestrator 2026-07-02)
owner: A
workspace: proofs/conj-no-free-frontier
---

**Arm F wave-2 wall mechanism (status CONJECTURE).** The reason the refuter sweep could never host
genuine invisible mass beyond `≈0.37τ`: rows genuinely outside `C_W` occupy separating directions, and
the extremal one in each direction gets exposed (its supporting functional has margin; only within-ρ
rows sit behind it) — so it joins `W` and `C_W` extends to absorb the near-outside rows. Only
mutually-shielding near-coincident twins persist hidden, and their hostable mass is bounded by the poke
depth `∝ ν = O(τ)` (`t* = ν/(1+ν) < κ`).

**Role:** the mechanism candidate for the halo-robust cap `σ̃_g ≤ 1−c` (indeed the empirics suggest
`σ̃_g = O(τ)`). NOTE the strategist caution: arm B wave 3's one-sided-ledger obstruction applies to
COEFFICIENT-mass lower bounds at v; this statement is about EXPOSEDNESS of extremal rows — a different
species, plausibly outside that obstruction — but whether its quantitative form dodges the
anti-splitting class-count is exactly what the next wave must determine before any af elevation.
