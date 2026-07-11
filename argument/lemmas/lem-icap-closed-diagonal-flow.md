---
id: lem-icap-closed-diagonal-flow
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta < tau/D_0, and with an exhibited selected-corner certificate C* = (phi,h,f*,eta*) obtained from the lem-ihorn-selected-corner-extraction construction and satisfying M_X(C*) <= 1/8 and M_I(C*) >= 1/16 — in BI let alpha_I = a_A restricted to F_I, a_I = alpha_I(1), eta_f^I = Gamma_f restricted to B(f) cap I, beta_I(u) = sum_f alpha_I(f)*eta_f^I(u), Pi_I(R) = sum_u beta_I(u)*P_u^+(R), e_delta = 2*delta(P)*(1+delta(P)), and hat(Pi)_I({R}) = min(Pi_I({R}),P_v^+({R})); then a_I > c_m/48, beta_I(1) > c_m/768, sup_{0 <= g <= 1}(Pi_I(g)-P_v^+(g)) <= (1+a_I)*e_delta <= (2+delta(P))*e_delta, and hat(Pi)_I(H_v^out) > c_m/1024; the identical conclusions hold in BD with I replaced by D.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top; def-invisible-mass
deps: lem-icap-kernel-bulk-census; lem-icap-tallness-spend; lem-l5-positive-flow-foldback
status: proved
af: none
provenance: W64 wave (docs/waves/2026-07-11-W64-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) ICAP-ATTACK-W64.md §1.7 + appendix; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W64-ICAP-BATCH.md line IC: VALID. Reviewer != author.
owner: B
---

**Role (W64 I-cap tree, IC — closed diagonal flow).** Closes the routed BI sign-cube packet, and identically the BD diagonal packet, into constant coefficient mass, controlled two-fold overflow, and constant covered outer-halo return.

**Mechanism (one line).** Two [[lem-l5-positive-flow-foldback]] applications with the same arbitrary \(g\), first at each root and then at \(v\), combine with the T+ shallow bound and canonical receiverwise truncation.

**Honest scope.** Errors scale with total source mass rather than root count; no hiddenness witnesses are averaged, no carrier becomes a new top, no receiver reruns score/corner extraction, and no atom is selected. Fallback: retain \(\Pi_I\), \(P_v^+\), and their canonical overlap (with B0 as the original one-root check).

**Rigour tier.** L5 (fresh hostile batched codex verdict, W64). NOT af-validated.
