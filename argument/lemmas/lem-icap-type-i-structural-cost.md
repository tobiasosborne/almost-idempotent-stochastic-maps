---
id: lem-icap-type-i-structural-cost
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta < tau/D_0, and with an exhibited selected-corner certificate C* = (phi,h,f*,eta*) obtained from the lem-ihorn-selected-corner-extraction construction and satisfying M_X(C*) <= 1/8 and M_I(C*) >= 1/16 — every type-I carrier u in the exhibited certificate or the closed diagonal flow satisfies rho_T(u) = dist_1(0,K_T(u)) <= t*(u)*D_0 < (1/2+delta(P))*tau; moreover, for the far-tight probability lambda_u in an alpha-free display and bar(p)_{T,u} = integral p_t d lambda_u(t), integral ||p_t-bar(p)_{T,u}||_1 d lambda_u(t) > (7/2-delta(P))*tau, so the T(u)-hull is not geometrically singleton.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top
deps: lem-optimal-face-conic-reduction
status: proved
af: none
provenance: W64 wave (docs/waves/2026-07-11-W64-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) ICAP-ATTACK-W64.md §1.8 + appendix; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W64-ICAP-BATCH.md line A: VALID. Reviewer != author.
owner: B
---

**Role (W64 I-cap tree, A — type-I structural cost).** Records the alpha-free cancellation geometry carried by every type-I vertex in B0 or IC, without claiming an exclusion.

**Mechanism (one line).** [[lem-optimal-face-conic-reduction]] supplies \(\bar p_{T,u}-p_u=t^*(u)(\bar p_{O,u}-p_u)\), and the diameter and far-tight distance bounds give the cancellation radius and dispersion estimates.

**Honest scope.** Alpha-free displays are used one carrier at a time as geography, never averaged against \(\beta_I\), identified with flow coefficients, or divided by \(t^*(u)\). Fallback: retain only the clone-safe convex-hull radius bound; a singleton or separating halfspace at radius at least \((1/2+\delta)\tau\) forces type D.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W64). NOT af-validated.
