---
id: lem-icap-common-receiver-ownership
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta < tau/D_0, and with an exhibited selected-corner certificate C* = (phi,h,f*,eta*) obtained from the lem-ihorn-selected-corner-extraction construction and satisfying M_X(C*) <= 1/8 and M_I(C*) >= 1/16 — in the routed bulk cell J in {X,I,D} from lem-icap-kernel-bulk-census, define C = {(x,u) : H-phi(p_x) < 4*tau, h(p_x) < 4*tau, H-phi(p_u) < 4*tau, h(p_u) < 4*tau} and g_J(x) = sum_u xi_x(u)*1_C(x,u)*1_{type J}(x,u); then for every f in F_X, P_f^+(g_X) > 1/8 and P_v^+(g_X) > c_m/512; for every f in F_I, P_f^+(g_I) >= 1/16 and P_v^+(g_I) > c_m/1536; for every f in F_D, P_f^+(g_D) > 1/16 and P_v^+(g_D) > c_m/1536; and for J in {I,D}, g_J = 1_{U_J}, where U_J = {u : u is a row vertex, H-phi(p_u) < 4*tau, h(p_u) < 4*tau, and u has type J}.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top
deps: lem-icap-kernel-bulk-census; lem-ihorn-cotop-sl1a-package; lem-l5-positive-flow-foldback
status: proved
af: none
provenance: W64 wave (docs/waves/2026-07-11-W64-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) ICAP-ATTACK-W64.md §1.5 + appendix; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W64-ICAP-BATCH.md line G: VALID. Reviewer != author.
owner: B
---

**Role (W64 I-cap tree, G — common receiver ownership).** Turns the routed census cell into constant top-owned mass and supplies the X coupling or intrinsic I/D vertex set used downstream.

**Mechanism (one line).** Each selected block lies in the common corner, so one root-independent \(g_J\) captures its cell mass and one [[lem-l5-positive-flow-foldback]] transfers the owned source floor to row \(v\).

**Honest scope.** Exactly one common nonnegative statistic is folded in the realized case, with no actor-dependent test sum or kernel optimization; I/D become intrinsic by diagonal Diracness, while X retains barycentric provenance and is not a transition law. Fallback: retain the sharper pre-error floors \(c_m/384\) in X and \(c_m/768\) in I/D.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W64). NOT af-validated.
