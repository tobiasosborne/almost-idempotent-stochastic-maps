---
id: lem-icap-priority-residual-split
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta < tau/D_0, and with an exhibited selected-corner certificate C* = (phi,h,f*,eta*) obtained from the lem-ihorn-selected-corner-extraction construction and satisfying M_X(C*) <= 1/8 and M_I(C*) >= 1/16 — the routed bulk package lies in exactly one of these priority-guarded cells, with equality owned by the first line of each pair: in BX, for Xi_X(x,u) = P_v^+(x)*xi_x(u)*1_C(x,u)*1_X(x,u), either X_gap: Xi_X({||p_x-p_u||_1 >= b*tau}) >= c_m/1024, or X_near: Xi_X({||p_x-p_u||_1 >= b*tau}) < c_m/1024 and Xi_X({||p_x-p_u||_1 < b*tau}) > c_m/1024; in BI, for n_I = P_v^+ restricted to U_I, either I_far: n_I({||p_u-p_v||_1 >= 4*tau}) >= c_m/3072, or I_near: n_I({||p_u-p_v||_1 >= 4*tau}) < c_m/3072 and n_I({||p_u-p_v||_1 < 4*tau}) > c_m/3072; in BD, for n_D = P_v^+ restricted to U_D and g_u = dist_1(K_T(u),K_O(u)), either D_gap: n_D({g_u >= tau}) >= c_m/3072, or D_near: n_D({g_u >= tau}) < c_m/3072 and n_D({g_u < tau}) > c_m/3072.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top
deps: lem-icap-common-receiver-ownership
status: proved
af: none
provenance: W64 wave (docs/waves/2026-07-11-W64-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) ICAP-ATTACK-W64.md §1.9 + appendix; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W64-ICAP-BATCH.md line R: VALID-WITH-CORRECTION. Contract restated per the verifier-mandated priority-guard correction. Reviewer != author.
owner: B
---

**Role (W64 I-cap tree, R — corrected six-way residual split).** Routes the realized X, I, or D bulk into exactly one of six strictly smaller geometric leaves after G supplies constant public mass.

**Mechanism (one line).** Split the routed mass into two measurable bins and take the first line when its half-floor holds; otherwise the verifier-mandated negation guards force the strict second line.

**Honest scope.** This body and contract apply the W64 verifier correction: X-near includes failure of X-gap, I-near includes failure of I-far, and D-near includes failure of D-gap; equality belongs to X-gap, I-far, and D-gap. The split proves no exclusion, selects no atom or favorable carrier, and never discards the near branch. Fallback: retain each full distance distribution rather than its priority two-bin summary.

**Rigour tier.** L5 (fresh hostile batched codex verdict with mandated correction applied, W64). NOT af-validated.
