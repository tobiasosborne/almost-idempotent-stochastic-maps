---
id: conj-low-slab-cap
kind: lemma
contract: (CONJECTURE) Low-slab coefficient cap: there exist universal a > 0, theta in (0,1), and delta_0 > 0 such that every exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set W(P), and height H > ((5a/4 + 3/2)/theta)*tau (tau = sqrt(delta)) has some hidden top vertex v whose optimal exposer h_v* satisfies: sum over {j in G_a : h_v*(p_j) < tau/4} of max(P_vj, 0) <= 1 - theta - 4*tau, where G_a = {j : dist_1(p_j, conv{p_w : w in W}) > a*tau}.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-invisible-mass; def-height; def-slab; def-near-cluster
deps: lem-absorption-implies-low-slab-cap
status: conjecture
af: none
provenance: W32 wave (docs/waves/2026-07-07-W32-cs-pincer.md): the successor statement named by worker Z's gap analysis (VZ confirmed the gap honesty: CS alone cannot cap the low slab); the theta-flexible re-scoping of the session-11 orchestrator (any universal (a, theta) suffices)
owner: A
workspace: proofs/conj-low-slab-cap
---

**Role (THE frontier statement, theta-flexible form).** Composition with
[[lem-cs-low-slab-pincer]] at s = κ (ν_v/κ ≤ 4τ) gives σ_a(v) ≤ 1 − θ at that hidden top;
[[lem-parametric-halo-collapse]] (af-validated) then forces H ≤ ((5a/4+3/2)/θ)τ —
contradiction with the tallness hypothesis, i.e. the height bound H ≤ (K_a/θ)τ holds
UNCONDITIONALLY once this conjecture does. At (a, θ) = (4, 1/2) this implies
[[conj-min-a-w4]] (whose 1/2 is the historical calibration, not load-bearing); ANY universal
(a, θ) closes the Kernel height clause at B = K_a/θ, and with W-nonemptiness (open at
rank ≥ 3) the full [[conj-kernel]].

**Why this is the right split (W29/W32 pincer evidence).** Hiddenness forces > 94% of the
witness mass into the deep low-exposer slab ([[lem-hiddenness-depth-markov]]); the pincer
forbids row mass in the HIGH slab; a counterexample must therefore make the top's row mass
and its witness mass cohabit the deep low slab. Empirically (certified W29 frontier) true
hidden tops have σ_4 = 0 — the conjecture asks only that the cohabitation cannot be total.

**Attack surfaces (aism-2fi):** the harmonic-affine bridge (W33 — the (ψ, g) pencil as an
exposer family); the two-exposer pairing across the deep-carrier web; the quadratic-slab
upgrade at rank 3 ([[lem-rank3-maxchart-hidden-tangent]] side).

**Status discipline.** A conjecture — promotes nothing; consumers must carry it as a dep.
