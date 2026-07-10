---
id: lem-ihorn-cotop-sl1a-package
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta < tau/D_0, admits the probability measure lambda_A = (mu_A restricted to {Q : dist_1(p_Q, conv{p_w : w in W}) > H - 4*tau})/(1 - theta) with support contained in {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 4*tau}, S*(1-theta)*lambda_A <= P_v^+ as full-fiber measures, barycenter r satisfying ||r - p_v||_1 < 33*tau/28, and integral of h(p_Q) d lambda_A(Q) < 2*tau/7 for every admissible exposer h at v.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass
deps: lem-ihorn-ultra-compression
status: proved
af: none
provenance: W63 wave (docs/waves/2026-07-10-W63-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) DECOMPOSITION-W63-I.md node L0 + Appendix A.5; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W63-I-BATCH.md line 'L0: VALID' (both 1-theta denominators and the strict 33*tau/28, 2*tau/7 bounds recomputed via tau/D_0 <= 1/8 and tau/c_m <= 1/4). Reviewer != author.
owner: B
---

**Role (W63 I-horn batch, 9/10 — the co-top SL1a package; THE decisive
compression).** In the ultra-isotropic thin-rim regime, a completely arbitrary
selected set \(A\) becomes ONE scaled-top-owned SL1a probability web whose
constants (\(33\tau/28\), \(2\tau/7\)) are STRONGER than the registered SL1a
thresholds (\(11\tau/5\), \(4\tau/13\)). This is what routes the isotropic core
of the L5 minimax into the W56 SL1a corner machinery.

**Mechanism (one line).** Delete rim mass \(\theta\) (barycenter displacement
\(\le\theta D_0<\tau\)), renormalize by \(1-\theta\);
[[lem-ihorn-ultra-compression]] pays the original radius and exposer moment.

**Honest scope.** The exact relation is \(S(1-\theta)\lambda_A\le P_v^+\); the
normalized \(\lambda_A\) itself need NOT be a \(P_v^+\)-submeasure. It is not a
hiddenness witness and not \(\lambda P\). Fallback: retain the exact conditional
bounds \((\|q_A-p_v\|_1+\theta D_0)/(1-\theta)\) and \(\delta/(S(1-\theta))\).

**Rigour tier.** L5 (fresh hostile batched codex verdict, W63). NOT af-validated.
