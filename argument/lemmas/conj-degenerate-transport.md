---
id: conj-degenerate-transport
kind: lemma
contract: Degenerate transverse transport: there is a universal constant C_tr (independent of dimension, rank, and instance) such that for every exact signed idempotent P (square real matrix with P^2 = P and all row sums equal to 1) with 0 < delta(P) <= 1/4 where delta(P) = max_i sum_j max(-P_ij, 0), every actual-row basis U = (u_1, ..., u_k) minimizing Phi(U) = max_s Phi_s(U) over all actual-row bases with Gram volume Vol(U) >= (1/2) * Vol_max(P) (coordinates a_t(j) defined by p_j = sum_t a_t(j) p_{u_t}, beta_s(j) = P_{u_s j}, mu_s(j) = sum_{t != s} max(-a_t(j), 0), E_s(j) = max(mu_s(j) - (1 - a_s(j)), 0), Phi_s(U) = sum_j max(beta_s(j), 0) * E_s(j)), and every pivot s, writing D_s for the set of rows j with beta_s(j) > 0, E_s(j) > 0, and every block swap keeping u_s in the chart and bringing row j into one or two transverse pivot positions having Schur volume factor |det C| <= 1/2, one has sum_{j in D_s} beta_s(j) * mu_s(j) <= C_tr * delta(P).
defs: def-signed-idempotent; def-negative-mass
deps: 
status: conjecture
af: none
provenance: docs/waves/2026-07-03-A12-lift.md (arm A wave 12, codex; statement (TT) of §T2 — the payment-horn gap after the lift analysis); exact zoo evidence in the A12 transport table (all restricted ratios <= 5/3, incl. the nonzero-lambda balanced staircase at ~1.000002 and sigma-cap B at 0)
owner: D
workspace: proofs/conj-degenerate-transport
---

**THE remaining payment-horn gap (A12).** This is arm D's transverse coefficient tax
(`RESEARCH_NOTES.md` arm D; the w25–w31 line's single named open) RESTRICTED to the Schur-degenerate
set `D_s` at a theta-1/2 Phi-argmin. With (TT), the payment horn [[conj-degenerate-payment]] follows
at constant `2*C_tr` via the crude pointwise `E <= 2*mu` on `D_s`, or at
`f*(2+sqrt(2))*C_tr` via the rigorous [[lem-fan-payment-restricted]] through the A12
perturbed-DRF lift (whose barycenter and lambda source terms are controlled by the same transport
mechanism). Composed: `C0 = max(C_pay, C_legal)`, `C_sf = 2*C0 + 6` through the rigorous
[[lem-factorization]].

**Wall status (A12 §T3):** the ALL-row version of this tax is the old wall-shaped arm-D target. The
`D_s` restriction + argmin hypothesis plausibly dodges it (the degenerate set is a max-based,
pivot-local object; repeated anchors amplify sums, not this restricted quantity) — but any proof
summing per coordinate, per class, or per near-degenerate block re-imports the class-count wall
(Rule 13, dead routes c10/c20). Proof resources: row reproduction `a_t(j) = sum_l P_jl a_t(l)`,
beta stationarity `beta_s(l) = sum_j beta_s(j) P_jl`, the harmonic identities, the Schur slab
(`|a_t(j)| <= 1/2` on tested degenerate coordinates — NOT usable via coordinate counting), row
negativity `nu_j <= delta`, and the H-M Thm 1.12 signed structure (arm D's anchor,
`refs/hognas-mukherjea`).

**Do NOT af-elevate** until a proof sketch exists (genuine-gap abort predicted).
