---
id: lem-ihorn-tall-halo-saturation
kind: lemma
contract: For every c_m in (0,1) and every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — the halo-robust invisible mass sigma_g of v (the positive coefficient mass v places on rows at l1-distance > tau/4 from conv{p_w : w in W}) satisfies 1 - sigma_g < (4*tau/63)*(2 + 4*delta(P) + tau/4).
defs: def-signed-idempotent; def-visible-set; def-height; def-invisible-mass; def-negative-mass
deps: lem-halo-collapse
status: proved
af: none
provenance: W63 wave (docs/waves/2026-07-10-W63-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) DECOMPOSITION-W63-I.md node T + Appendix A.1; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W63-I-BATCH.md line 'T: VALID' (incl. the 1 - sigma_g <= 0 case and the exact 4*tau/63 factor). Reviewer != author.
owner: B
---

**Role (W63 I-horn batch, 2/10 — tall halo saturation).** The quantitative gate
that ejects every known short fixture: on the tall I-base class, almost ALL of
row \(v\)'s positive mass lies beyond the \(\tau/4\) visible-hull halo
(\(1-\sigma_g=O(\tau)\)). Every creative I-horn leaf must consume this
saturation or one of the two exact height budgets that yield it; a proof that
ignores tallness has not explained the four consecutive refuter failures.

**Mechanism (one line).** Combine exactly [[lem-halo-collapse]]
(\(H(1-\sigma_g)\le(\sigma_v-\sigma_g)\tau/4+\nu_vD_0\)) with
\(\sigma_v-\sigma_g\le\nu_v+(1-\sigma_g)\), \(\nu_v\le\delta=\tau^2\), and strict
\(H>16\tau\), giving \((H-\tau/4)(1-\sigma_g)\le\nu_v(D_0+\tau/4)\).

**Honest scope.** Uses one of the two permitted tallness budgets and no surrogate
height estimate. If \(1-\sigma_g\le0\) the conclusion is automatic; otherwise the
division is by \(H-\tau/4>0\). The sharper un-divided form
\((H-\tau/4)(1-\sigma_g)\le\nu_v(D_0+\tau/4)\) is the recorded fallback.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W63). NOT af-validated.
