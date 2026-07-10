---
id: lem-ihorn-dual-cotop-geography
kind: lemma
contract: For every c_m in (0,1) and every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — the exposedness margin satisfies t*(v) > 0, reduced optimal witness displays at v exist, and every reduced optimal witness display (lambda, a, gamma) at v (as in lem-optimal-face-conic-reduction) has pushforward lambda-mass on full row-point fibers in G_v strictly greater than 13/16, i.e. sum over {f : Q(f) in G_v} of lambda_f > 13/16.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass
deps: lem-positive-exposedness-margin; lem-always-tight-dual-support; lem-optimal-face-conic-reduction; lem-cotop-witness-pinning
status: proved
af: none
provenance: W63 wave (docs/waves/2026-07-10-W63-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) DECOMPOSITION-W63-I.md node V + Appendix A.1; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W63-I-BATCH.md line 'V: VALID'. Reviewer != author.
owner: B
---

**Role (W63 I-horn batch, 3/10 — dual-required co-top geography).** The second,
dual-required far co-top measure: independently of the selected \(\omega\), the
hiddenness dual FORCES more than \(13/16\) of its witness mass into the same far
co-top band \(G_v\). Creative leaves use this as geography only.

**Mechanism (one line).** \(S>0\) makes the \(4\tau\)-far set nonempty, so
[[lem-positive-exposedness-margin]] gives \(t^*(v)>0\); reduced optimal displays
exist by [[lem-always-tight-dual-support]] + [[lem-optimal-face-conic-reduction]];
the \(c=4\), \(\delta\le1/4\) case of [[lem-cotop-witness-pinning]] gives
\(\lambda(G_v)>1-(1/2+\delta)/4\ge13/16\).

**Honest scope.** The witness \(\lambda\) is geography only: it is NEVER
identified with \(\omega\), \(\mu_A\), or any \(P_v^+\)-submeasure (no
coefficient overlap is implied; \(\lambda P\ne p_v\)), and no reciprocal of
\(t^*(v)\) appears in any constant. Fallback: keep the exact pinning moment
instead of the 13/16 geography.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W63). NOT af-validated.
