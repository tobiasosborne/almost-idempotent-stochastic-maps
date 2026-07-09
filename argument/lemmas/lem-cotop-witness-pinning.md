---
id: lem-cotop-witness-pinning
kind: lemma
contract: Co-top witness pinning: for an exact signed idempotent P with 0 < delta(P) <= 1/4 and nonempty visible set, a hidden top vertex v of height H with t*(v) > 0, every reduced optimal witness display (lambda, a, gamma) of the exposedness LP at v (lambda, gamma probability vectors on T(v), O(v), coefficients a_z >= 0 on Z(v), as in lem-optimal-face-conic-reduction), and every top support functional phi at v with z_j = H - phi(p_j) >= 0: sum over f in T of lambda_f*z_f + sum over z in Z of a_z*z_z = t*(v)*sum over i in O of gamma_i*z_i <= t*(v)*(2+4*delta) < (1/2+delta)*tau, every left summand nonnegative; consequently for every c > 0, lambda{f in T : ||p_f - p_v||_1 >= 4*tau, dist_1(p_f, conv W) > H - c*tau} > 1 - (1/2+delta)/c and sum over {z in Z : dist_1(p_z, conv W) > H - c*tau} of a_z > (sum over Z of a_z) - (1/2+delta)/c; at c = 4 and delta <= 1/4 more than 13/16 of the lambda-mass sits in the starved set {j : ||p_j - p_v||_1 >= 4*tau, dist_1(p_j, conv W) > H - 8*tau}.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-hiddenness-dual-witness; lem-always-tight-dual-support; lem-optimal-face-conic-reduction; lem-top-deficit-price
status: proved
af: none
provenance: W54 wave (docs/waves/2026-07-09-W54-huddle-charge-decomposition.md): Fable author L6 (sub-leaves L6.1 + L6.2) + fresh hostile codex verifier V-L6 (VALID-WITH-CORRECTIONS; L6.1/L6.2 confirmed valid as written — exact display pairing, sign conventions, Markov steps for probability AND nonnegative conic mass all checked)
owner: A
---

**Role (the exact pairing: dual witness AND zero-face mass are both co-top).** Applying a
top support functional's linear part to the reduced display of
[[lem-optimal-face-conic-reduction]] pins the ENTIRE dual side of hiddenness at a top into
the top slab: the lambda-clause recovers tight-far geography restricted to reduced
witnesses; the a-clause (zero-face conic mass is co-top) is NEW. The witness's far mass is
forced into the starved set of the W54 tree's NOT-Q5 — the object
[[conj-cotop-web-coupling]] must couple to the top's own coefficients. No disjointness,
tallness, or heaviness needed. Dimension-free; clone-invariant.

**Rigour tier.** L5 (reviewer != author: fresh hostile codex V-L6). NOT af-validated.
