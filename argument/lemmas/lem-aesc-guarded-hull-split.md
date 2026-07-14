---
id: lem-aesc-guarded-hull-split
kind: lemma
contract: For c_m = 1/4, with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta < tau/D_0, and with an exhibited selected-corner certificate C* = (phi,h,f*,eta*) obtained from the lem-ihorn-selected-corner-extraction construction and satisfying M_X(C*) <= 1/8, M_I(C*) < 1/16, and M_D(C*) > 1/16 — define eta_D*(u) = eta*({(x,u) : p_x = p_u and u is type D}), and for every u in supp(eta_D*) fix an arbitrary reduced optimal display k_T,u + sum_z a_u,z*(p_z-p_u) = k_O,u, with A_u = sum_z a_u,z, q_u = A_u^(-1)*sum_z a_u,z*p_z, ell_u = ||q_u-p_u||_1, and g_u = dist_1(K_T(u),K_O(u)); whenever g_u >= tau, A_u >= 4, and ell_u >= tau/2, set (q_tilde_u,A_tilde_u) = (q_u,A_u) if ell_u <= 2*tau and (p_u+(2*tau/ell_u)*(q_u-p_u), A_u*ell_u/(2*tau)) if ell_u > 2*tau, and set A_esc = {u in supp(eta_D*) : g_u >= tau, A_u >= 4, ell_u >= tau/2, and for every row f, ||p_f-p_u+A_tilde_u*(q_tilde_u-p_u)||_1 > 3*delta(P)}; with h_u = dist_1(p_u-A_tilde_u*(q_tilde_u-p_u), K(P)), H_out = {u in A_esc : h_u > 3*delta(P)}, and D_tail = {u in A_esc : h_u <= 3*delta(P)}, if eta_D*(A_esc) >= 1/80 and eta_D*(H_out) < 1/160, then eta_D*(D_tail) > 1/160.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top; def-actor-hull
deps: lem-dcap-five-way-completion-split
status: proved
af: none
provenance: W67 wave (docs/waves/2026-07-14-W67-artifacts/): codex strategist (gpt-5.6-sol, xhigh) AESC-ATTACK-W67.md §1.3; fresh routine prover (gpt-5.6-sol, high) APPENDIX-W67-aesc-proofs.md; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W67-AESC-BATCH.md line HS: VALID. Reviewer != author.
owner: B
---

**Role (W67 A-esc routine, HS — guarded hull split).** Partitions the substantial A-esc mass into hull-exterior and hull-near carriers with the declared boundary ownership.

**Mechanism (one line).** The disjoint predicates \(h_u>3\delta\) and \(h_u\le3\delta\) partition A-esc, so the strict failure guard leaves more than \(1/160\) mass in \(D_{\rm tail}\).

**Honest scope.** This is a bookkeeping node on the A-esc window; it does NOT prove the creative residual HES ([[conj-w67-aesc-hull-exterior-separator-synchronization]]) or DTR ([[conj-w67-aesc-diffuse-tail-ray-conversion]]), and no leaf exclusion or (EC) bound is claimed.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W67). NOT af-validated.
