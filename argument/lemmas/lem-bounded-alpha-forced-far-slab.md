---
id: lem-bounded-alpha-forced-far-slab
kind: lemma
contract: Bounded-alpha forced far slab: for an exact signed idempotent P with 0 < delta(P) <= delta_0 <= 1/4 and nonempty visible set, a hidden top vertex v of height H with top support functional phi (phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1), a geometrically distinct row vertex u with ||p_u - p_v||_1 < 4*tau, any A_0 >= 0, and any c > 1/2 + delta_0 + 4*(1 + A_0): if F_u cap {j : dist_1(p_j, conv{p_w : w in W}) >= H - c*tau} is empty (F_u = {j : ||p_j - p_u||_1 >= 4*tau}), then u is (rho,kappa)-exposed or every hiddenness dual witness of u with sum_i beta_i < tau/4 has sum_i alpha_i > A_0; equivalently a hidden near-top vertex with a small-beta witness of alpha-mass <= A_0 forces a rho-far row from u at depth >= H - c*tau.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-bounded-alpha-top-slab-reduction; lem-hiddenness-dual-witness
status: proved
af: none
provenance: W53 wave (docs/waves/2026-07-09-W53-binding-constraint-lemmaization.md): codex prover B2 (Proposition B) + fresh hostile codex verifier VB2 (VALID-WITH-CORRECTIONS; corrections applied — small-beta witness reading explicit; A_0 >= 0 and c > K(A_0, delta_0) pinned; Markov normalization imported from lem-hiddenness-dual-witness)
owner: A
---

**Role (the huddle partner drags its own web).** The forced-visibility alternative in
static, universal form: the huddle partner u either turns exposed, or its every canonical
witness has alpha-mass > A_0 (the zero-face blow-up channel — realized OUTSIDE tall-heavy
by [[obs-realized-alpha-blowup]], openness of the tall case = [[conj-tall-bounded-alpha]]),
or u forces its OWN rho-far top-slab actor. Proof: the Markov clause of
[[lem-bounded-alpha-top-slab-reduction]] leaves lambda-mass < 1 on {z_f > c*tau} for
c > K(A_0, delta_0) := 1/2 + delta_0 + 4*(1 + A_0); some far row has z_f <= c*tau, and
phi(p_f) <= d_f lifts it into the depth slab; the exposed/hidden dichotomy plus
[[lem-hiddenness-dual-witness]] normalization close the trichotomy (VB2-checked).
Dimension-free; clone-invariant.

**Rigour tier.** L5 (reviewer != author: fresh hostile codex VB2). NOT af-validated.
