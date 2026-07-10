---
id: lem-ihorn-priced-ray-package
kind: lemma
contract: For every c_m in (0,1) and every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — the barycenter q_A = (1/S)*sum_Q m_Q*p_Q and every attained minimizer (Lambda, c') of the lem-l5-top-face-ray-formula minimum for Z_v(q_A) (c' omitted when Lambda = 0) satisfy 0 <= ||p_v - q_A + Lambda*(p_v - c')||_1 - Lambda*H = Z_v(q_A) <= nu_v*(2 + 4*delta(P))/S <= delta(P)*(2 + 4*delta(P))/S, where nu_v is the negative mass of row v.
defs: def-signed-idempotent; def-visible-set; def-height; def-negative-mass
deps: lem-l5-mass-barycenter-dualization; lem-l5-top-face-ray-formula; lem-top-deficit-price
status: proved
af: none
provenance: W63 wave (docs/waves/2026-07-10-W63-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) DECOMPOSITION-W63-I.md node P + Appendix A.1; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W63-I-BATCH.md line 'P: VALID'. Reviewer != author.
owner: B
---

**Role (W63 I-horn batch, 1/10 — the priced ray package).** The constant-complexity
certificate every I-horn creative leaf receives: on the I-base class the true dual
value \(Z_v(q_A)\) is squeezed between \(0\) and \(\nu_vD_0/S\le\delta D_0/S\).
Hence any creative \(\gamma\tau\) lower bound makes the I antecedent EMPTY below a
ceiling — node I is asymptotically an emptiness theorem, and its hard core is a
tall completion obstruction (DECOMPOSITION-W63-I.md §0).

**Mechanism (one line).** [[lem-l5-mass-barycenter-dualization]] converts the mass
objective to \(SZ_v(q_A)\); [[lem-top-deficit-price]] caps it above by
\(\nu_vD_0\); [[lem-l5-top-face-ray-formula]] supplies the attained ray value.

**Honest scope.** The minimizer is arbitrary among attained ones — no tie
property, favorable center, or selected coordinate. The top-deficit price is used
only in its proved upper direction (no W53 reversal). Signed picture;
clone-invariant; frame-free.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W63). NOT af-validated.
