---
id: lem-ihorn-rim-sl1b-package
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta >= tau/D_0, admits the subprobability measure mu_sh = mu_A restricted to {Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau} with total mass mu_sh(1) = theta >= tau/D_0, support contained in {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}, S*mu_sh <= P_v^+ as full-fiber measures, and integral of h(p_Q) d mu_sh(Q) <= tau/4 for every admissible exposer h at v.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass
deps: lem-ihorn-ultra-compression
status: proved
af: none
provenance: W63 wave (docs/waves/2026-07-10-W63-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) DECOMPOSITION-W63-I.md node S0 + Appendix A.5; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W63-I-BATCH.md line 'S0: VALID' (scaled ownership and the all-exposer moment bound via tau <= c_m/4 checked). Reviewer != author.
owner: B
---

**Role (W63 I-horn batch, 8/10 — the rim-to-SL1b package).** In the
ultra-isotropic regime with heavy depth rim (\(\theta\ge\tau/D_0\)), restricting
the selected measure to the rim produces EXACTLY the registered SL1b
shallow-payer package with its true scaled ownership retained — the reduction
interface for the creative shallow-rim leaf (node Sh) and the bridge to the
registered SL1b surface (conj-shallow-counterweight-exclusion fallback).

**Mechanism (one line).** Restrict \(\mu_A\); exactly
\(S\mu_{\rm sh}=m|_{\mathcal R_{48}}\le P_v^+\); [[lem-ihorn-ultra-compression]]'s
universal shadow bound gives
\(\int h\,d\mu_{\rm sh}\le h(q_A)\le\delta/S\le\tau^2/c_m\le\tau/4\) using
\(\tau\le c_m/4\).

**Honest scope.** The submeasure is not normalized and no row is selected;
universal quantification in \(h\) precedes every later use. Equality
\(d_Q=H-4\tau\) and \(\theta=\tau/D_0\) are both intentionally owned here.
Fallback: keep the stronger values \(\theta\) and \(\delta/S\).

**Rigour tier.** L5 (fresh hostile batched codex verdict, W63). NOT af-validated.
