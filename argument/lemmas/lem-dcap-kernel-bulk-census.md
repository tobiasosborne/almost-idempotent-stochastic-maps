---
id: lem-dcap-kernel-bulk-census
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta < tau/D_0, and with an exhibited selected-corner certificate C* = (phi,h,f*,eta*) obtained from the lem-ihorn-selected-corner-extraction construction and satisfying M_X(C*) <= 1/8, M_I(C*) < 1/16, and M_D(C*) > 1/16 — letting lambda_A be the lem-ihorn-cotop-sl1a-package probability, z = H-phi, s(x) = 2*z(p_x)/D_0+h(p_x), and F = {x in supp(lambda_A) : s(x) <= 12*tau/13}, for every legal row-point vertex kernel xi fixed before any cell is inspected use the same (phi,h,xi) at every f in F, set Gamma_f(x,u) = P_f^+({x})*xi_x(u), C = {(x,u) : H-phi(p_x) < 4*tau, h(p_x) < 4*tau, H-phi(p_u) < 4*tau, h(p_u) < 4*tau}, B_F = C cap {||p_u-p_v||_1 >= 4*tau}, B_N = C cap {||p_u-p_v||_1 < 4*tau}, choose B(f)=B_F when Gamma_f(B_F) >= 1/4 and B(f)=B_N otherwise, and partition F as F_X, F_I, F_D by X: M_X(B(f)) > 1/8; I: M_X(B(f)) <= 1/8 and M_I(B(f)) >= 1/16; D: M_X(B(f)) <= 1/8 and M_I(B(f)) < 1/16; then exactly one priority alternative holds: BI: lambda_A(F_I) >= 1/42; BX: lambda_A(F_I) < 1/42 and lambda_A(F_X) >= 1/42; BD: lambda_A(F_I) < 1/42, lambda_A(F_X) < 1/42, and lambda_A(F_D) > 1/42.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top
deps: lem-sl1a-corner-ledger; lem-radial-horn-partition; lem-dcap-score-bulk-transfer
status: proved
af: none
provenance: W65 wave (docs/waves/2026-07-13-W65-artifacts/): codex strategist-prover (gpt-5.6-sol, xhigh) DCAP-ATTACK-W65.md §1.4; fresh routine prover (gpt-5.6-sol, high) APPENDIX-W65-dcap-proofs.md; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W65-DCAP-BATCH.md line B2: VALID. Reviewer != author.
owner: B
---

**Role (W65 D-cap tree, B2 — arbitrary-kernel bulk census).** Partitions the score-good bulk into the priority-routed I, X, or D branch surrounding the fixed local D root.

**Mechanism (one line).** The common corner ledger and radial partition classify every score-good root for the already fixed kernel, and \(\lambda_A(F)>3/42\) forces the guarded three-way census.

**Honest scope.** The kernel is arbitrary and fixed before inspection; it may classify \(f^*\) differently and need not route bulk to D, while radial equality belongs to \(B_F\), \(M_X=1/8\) stays diagonal, \(M_I=1/16\) belongs to I, and priority equality belongs first to BI and then BX. Fallback: retain all three cell weights rather than declaring a priority cell.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W65). NOT af-validated.
