---
id: lem-icap-single-root-receiver-cap
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta < tau/D_0, and with an exhibited selected-corner certificate C* = (phi,h,f*,eta*) obtained from the lem-ihorn-selected-corner-extraction construction and satisfying M_X(C*) <= 1/8 and M_I(C*) >= 1/16 — defining eta_I*(u) = eta*{(x,u) : p_x = p_u and u is type I}, m_I* = eta_I*(1), Pi_f*(R) = sum_u eta_I*(u)*P_u^+(R), and e_delta = 2*delta(P)*(1+delta(P)), one has m_I* >= 1/16, eta_I* <= P_f*^+ as full-fiber measures, and sup_{0 <= g <= 1}(Pi_f*(g)-P_f*^+(g)) <= e_delta, with the supremum attained by 1_{Pi_f* > P_f*^+}; moreover the receiverwise overlap Pi_f*^o({R}) = min(Pi_f*({R}),P_f*^+({R})) has mass at least m_I* - e_delta.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top
deps: lem-l5-positive-flow-foldback
status: proved
af: none
provenance: W64 wave (docs/waves/2026-07-11-W64-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) ICAP-ATTACK-W64.md §1.2 + appendix; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W64-ICAP-BATCH.md line B0: VALID. Reviewer != author.
owner: B
---

**Role (W64 I-cap tree, B0 — single-root diagnostic).** Closes the original exhibited type-I root under one positive-flow foldback before the score-bulk branch, but does not complete I-cap.

**Mechanism (one line).** Diagonal vertex Diracness makes \(\eta_I^*\) a full-fiber submeasure of \(P_{f^*}^+\), and [[lem-l5-positive-flow-foldback]] applied once at \(f^*\) gives the \(e_\delta\) receiver cap.

**Honest scope.** One common receiver test is used on full fibers, with no witness display, atom selection, or second corner extraction; the cap gives no top-owned lower mass and does not spend tallness. Fallback: retain the canonical receiverwise overlap of mass at least \(m_I^*-e_\delta\).

**Rigour tier.** L5 (fresh hostile batched codex verdict, W64). NOT af-validated.
