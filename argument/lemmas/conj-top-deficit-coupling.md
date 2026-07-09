---
id: conj-top-deficit-coupling
kind: lemma
contract: (CONJECTURE) Top-deficit coupling: there exist universal c_def > 0, a >= 4, theta_0 in (0,1), delta_0 > 0 such that for every exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set, and hidden top vertex v of height H > a*tau carrying >= 1 - theta_0 of its positive row mass on the cluster {j : ||p_j - p_v||_1 < 4*tau, dist_1(p_j, conv{p_w : w in W}) > a*tau}: some top support functional phi (phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1) has Z_v(phi) = sum_j max(P_vj, 0)*(H - phi(p_j)) >= c_def*H.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: 
status: conjecture
af: none
provenance: W53 wave (docs/waves/2026-07-09-W53-binding-constraint-lemmaization.md): prover B1's GAP-1 in VB1-corrected form (the delta_0 range made part of the exclusion arithmetic) — the (i) handle of THE HUDDLE CHARGE (sketch v17)
owner: A
---

**Role (the (i) huddle-charge handle — the sharpest single closer).** With
[[lem-top-deficit-price]] this forces H <= 3*delta/c_def, hence H <= 4*tau for all
delta <= min(delta_0, 1/4, (4*c_def/3)^2) — tall-emptiness in the heavy class, rank-free,
i.e. the (M2) target and the Kernel height clause. The difficulty is exact: rows in v's
rho-ball have top-deficit z_j < 4*tau, so heavy huddle configurations concentrate positive
mass where the pairing is blind — c_def*H must come from hiddenness/zero-face structure
forcing mass OUT of the low-deficit slab ([[lem-top-witness-third-actor]] is the forced
counter-structure; [[lem-disjointness-huddle-reduction]] the anatomy).

**Refuter target.** A tall heavy exact signed idempotent with Z_v(phi) = o(H) for EVERY
top support functional — necessarily a huddle with all positive mass at depth within
o(H) of H (never realized: W52 BLOCKED, evidence only).

**Status discipline.** A conjecture — promotes nothing; consumers carry it as a dep.
