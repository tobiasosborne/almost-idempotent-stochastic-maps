---
id: lem-dtr-poti-assembly
kind: lemma
contract: Assume conj-dtr-zero-oriented-surplus-exclusion and conj-dtr-positive-oriented-surplus-gap-exclusion hold. Then the following holds. For c_m = 1/4, with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta < tau/D_0, and with an exhibited selected-corner certificate C* = (phi,h,f*,eta*) obtained from the lem-ihorn-selected-corner-extraction construction and satisfying M_X(C*) <= 1/8, M_I(C*) < 1/16, and M_D(C*) > 1/16 — define eta_D*(u) = eta*({(x,u) : p_x = p_u and u is type D}), and for every u in supp(eta_D*) fix an arbitrary reduced optimal display k_T,u + sum_z a_u,z*(p_z-p_u) = k_O,u, with A_u = sum_z a_u,z, q_u = A_u^(-1)*sum_z a_u,z*p_z, ell_u = ||q_u-p_u||_1, and g_u = dist_1(K_T(u),K_O(u)); whenever g_u >= tau, A_u >= 4, and ell_u >= tau/2, set (q_tilde_u,A_tilde_u) = (q_u,A_u) if ell_u <= 2*tau and (p_u+(2*tau/ell_u)*(q_u-p_u), A_u*ell_u/(2*tau)) if ell_u > 2*tau, define chi_u(x) = sgn(q_tilde_u-p_u) dot (x-p_u)/||q_tilde_u-p_u||_1, c_u,Q = sum_{j in Q} P_uj, and Tail_1(u) = sum_{Q : |chi_u(p_Q)| > 1} max(c_u,Q,0), and set A_esc = {u in supp(eta_D*) : g_u >= tau, A_u >= 4, ell_u >= tau/2, and for every row f, ||p_f-p_u+A_tilde_u*(q_tilde_u-p_u)||_1 > 3*delta(P)}; with h_u = dist_1(p_u-A_tilde_u*(q_tilde_u-p_u), K(P)) and D_tail = {u in A_esc : h_u <= 3*delta(P)}, for every full-fiber carrier set B subset D_tail with eta_D*(B) > 1/160, Tail_1(u) > tau/8, min_f ||p_f-x_u||_1 > 3*delta(P), and h_u <= 3*delta(P) for every u in B, where x_u = p_u-A_tilde_u*(q_tilde_u-p_u), and with P_i^+(F) = sum_{R in F} sum_{k in R} max(P_ik,0) for every row i, define U_B = {full fibers R : there exists u in B with c_u,R > 0 and |chi_u(p_R)| > 1} and require P_f*^+(U_B) > tau/2560; with I the finite index set of P, on the finite row-point quotient mathcal_Q = I/~, where i ~ j if and only if p_i = p_j, define the ORIGINAL top-selected measure m_A(Q) = sum_{j in A cap Q} max(P_vj,0), not a normalized variant, with m_A(E) = sum_{Q in E} m_A(Q), S = m_A(1), and q_A = S^(-1)*sum_Q m_A(Q)*p_Q, define rho(Q) = min{m_A(Q), eta_D*(B cap Q)} and rho(E) = sum_{Q in E} rho(Q), define z(p) = H-phi(p), T_u = {R : |chi_u(p_R)| > 1}, t_phi(u) = sum_{R in T_u} max(c_u,R,0)*z(p_R), and G_phi = sum_{u in B} rho(u)*max(t_phi(u)-D_0*delta(P),0), where rho(u) is the rho-mass of the full row-point fiber containing u; with C_W = conv{p_w : w in W}, h_C_W(y) = sup{y dot c : c in C_W}, Y_v = {y : ||y||_infinity <= 1 and y dot p_v-h_C_W(y) = H}, and Z_v(q_A) = sup_{y in Y_v} y dot (p_v-q_A), define d_Q = dist_1(p_Q,C_W), L_v = {Q : d_Q <= tau/4}, and E_* = {R : ||p_R-p_f*||_1 > 1/2}; every such datum satisfies Z_v(q_A) >= (1/8)*P_v^+(E_*) - (c_m/16)*P_v^+(L_v).
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top; def-actor-hull; def-invisible-mass
deps: conj-dtr-zero-oriented-surplus-exclusion; conj-dtr-positive-oriented-surplus-gap-exclusion; lem-dtr-canonical-overlap; lem-dtr-oriented-tail-ray-conversion; lem-dtr-tail-coherent-conversion; lem-dcap-tall-same-center-packet
status: proved
af: none
provenance: W70 wave (docs/waves/2026-07-16-W70-artifacts/): codex strategist (gpt-5.6-sol, xhigh) DTR-ATTACK-W69.md §2.1 (banked docs/waves/2026-07-14-W69-artifacts/); fresh routine prover (gpt-5.6-sol, high) APPENDIX-W70-dtr-proofs.md §4; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W70-DTR-BATCH.md line ASM: VALID. Reviewer != author.
owner: B
---

**Role (W69/W70 ASM — conditional exact POTI assembly).** Assuming the two registered creative residuals, the exhaustive POTI split yields exact (EC).

**Mechanism (one line).** Zero surplus uses POTI-0, strict positive shortfall uses POTI+, and nonnegative diagnostic uses POTI-R.

**Displayed consequence (B4.2 then B4.1).** After exact (EC), the one public exterior spend and last shallow spend give
\[
Z_v(q_A)>\frac{7c_m}{960}\tau.
\]

**Displayed weakened variant.** Independently, under the hypotheses of [[lem-dtr-tail-coherent-conversion]],
\[
Z_v(q_A)>\frac{r_0\alpha\lambda}{16S}\tau\ge\gamma_{\rm coh}\tau,
\]
without either creative residual.

**Honest scope.** This is a PROVED CONDITIONAL implication: [[conj-dtr-zero-oriented-surplus-exclusion]] and [[conj-dtr-positive-oriented-surplus-gap-exclusion]] remain open, no leaf exclusion is proved unconditionally, and this shard's contract conclusion is not consumable unconditionally.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W70). NOT af-validated.
