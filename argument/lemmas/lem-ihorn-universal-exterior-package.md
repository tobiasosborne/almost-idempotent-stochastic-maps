---
id: lem-ihorn-universal-exterior-package
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128 and delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt satisfies, for every point c of the row polytope K(P), P_v^+({R : ||p_R - c||_1 > 1/2}) >= tau*S/8.
defs: def-signed-idempotent; def-negative-mass
deps: lem-l5-universal-exterior-payer
status: proved
af: none
provenance: W63 wave (docs/waves/2026-07-10-W63-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) DECOMPOSITION-W63-I.md node E + Appendix A.1; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W63-I-BATCH.md line 'E: VALID' (ceiling arithmetic delta_rt <= min(1/16, (c_m/8)^2) checked). Reviewer != author.
owner: B
---

**Role (W63 I-horn batch, 4/10 — the universal exterior package on the I class).**
[[lem-l5-universal-exterior-payer]] instantiated on the I-base datum under the
batch ceiling \(\delta_{\rm rt}\): row \(v\) itself pays \(\tau S/8\) positive
mass outside EVERY half-ball. Together with the I-base all-center floor on
\(G_v\) these are two per-center facts that are NOT ordered.

**Mechanism (one line).** The selected \(m\le P_v^+\) has mass \(S\ge c_m\) on
the closed \(4\tau\)-far set, and
\(\delta_{\rm rt}\le\min\{1/16,(c_m/8)^2\}\), so the payer shard applies
verbatim.

**Honest scope.** Per-center uniform only: no common exterior fiber, no disjoint
family of payer sets, no centerwise sum. Creative leaves may rerun it at one
actual center or use one common bounded receiver statistic only. Fallback: R3's
exact precursor inequality.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W63). NOT af-validated.
