---
id: lem-icap-tallness-spend
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta < tau/D_0, and with an exhibited selected-corner certificate C* = (phi,h,f*,eta*) obtained from the lem-ihorn-selected-corner-extraction construction and satisfying M_X(C*) <= 1/8 and M_I(C*) >= 1/16 — for L_v = {Q : d_Q <= tau/4}, H_v^out = {Q : d_Q > tau/4}, and every routed statistic g_J from lem-icap-common-receiver-ownership, P_v^+(L_v) < ell_T = delta(P)+(4*tau/63)*(D_0+tau/4) < 2*tau/15, and every receiver on which g_J > 0 lies in H_v^out; the sharper fallback is (H-tau/4)*(1-sigma_g) <= nu_v*(D_0+tau/4).
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top; def-invisible-mass
deps: lem-icap-common-receiver-ownership; lem-ihorn-tall-halo-saturation
status: proved
af: none
provenance: W64 wave (docs/waves/2026-07-11-W64-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) ICAP-ATTACK-W64.md §1.6 + appendix; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W64-ICAP-BATCH.md line T+: VALID. Reviewer != author.
owner: B
---

**Role (W64 I-cap tree, T+ — tallness spend).** Prices shallow receiver leakage for every routed cell and locates the common cell support in the outer halo before diagonal closure.

**Mechanism (one line).** [[lem-ihorn-tall-halo-saturation]] and \(P_v^+(1)=1+\nu_v\) give the exact shallow-mass bound, while corner deficit \(H-\phi(p_x)<4\tau\) forces \(d_x>H-4\tau>\tau/4\).

**Honest scope.** Only the permitted halo height budget is consumed; equality \(d_Q=\tau/4\) belongs to the shallow set, and tallness alone does not align top mass, corner coefficients, and alpha-free witnesses. Fallback: retain the sharper undivided parent inequality.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W64). NOT af-validated.
