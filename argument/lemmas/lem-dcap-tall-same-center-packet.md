---
id: lem-dcap-tall-same-center-packet
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta < tau/D_0, and with an exhibited selected-corner certificate C* = (phi,h,f*,eta*) obtained from the lem-ihorn-selected-corner-extraction construction and satisfying M_X(C*) <= 1/8, M_I(C*) < 1/16, and M_D(C*) > 1/16 — define L_v = {Q : d_Q <= tau/4}, H_v^out = {Q : d_Q > tau/4}, E_* = {R : ||p_R-p_f*||_1 > 1/2}, C = {(x,u) : H-phi(p_x) < 4*tau, h(p_x) < 4*tau, H-phi(p_u) < 4*tau, h(p_u) < 4*tau}, and each routed statistic g_J(x) = sum_u xi_x(u)*1_C(x,u)*1_J(x,u); then P_v^+(L_v) < ell_T = delta(P)+(4*tau/63)*(D_0+tau/4) < 2*tau/15, every receiver on which the routed g_J is positive lies in H_v^out, P_v^+(E_*) >= tau*S/8 >= c_m*tau/8, and the exact undivided fallback is (H-tau/4)*(1-sigma_g) <= nu_v*(D_0+tau/4).
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top; def-invisible-mass
deps: lem-ihorn-tall-halo-saturation; lem-ihorn-universal-exterior-package
status: proved
af: none
provenance: W65 wave (docs/waves/2026-07-13-W65-artifacts/): codex strategist-prover (gpt-5.6-sol, xhigh) DCAP-ATTACK-W65.md §1.6; fresh routine prover (gpt-5.6-sol, high) APPENDIX-W65-dcap-proofs.md; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W65-DCAP-BATCH.md line B4: VALID. Reviewer != author.
owner: B
---

**Role (W65 D-cap tree, B4 — tall same-center packet).** Prices shallow receiver leakage for every routed cell and supplies the universal exterior mass at the same public center used by the original D-root closure.

**Mechanism (one line).** [[lem-ihorn-tall-halo-saturation]] gives the exact shallow bound, corner deficit puts routed support in the outer halo, and [[lem-ihorn-universal-exterior-package]] supplies \(\tau S/8\) outside the half-ball centered at \(p_{f^*}\).

**Honest scope.** Equality \(d_Q=\tau/4\) is shallow and the half-ball exterior is strict; only one receiver center is used, and the crude intersection lower bound need not be positive, so tallness and exterior mass are common-test inputs rather than a decorative set difference. Fallback: retain the undivided parent inequality and the unweakened \(\tau S/8\) exterior floor.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W65). NOT af-validated.
