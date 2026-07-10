---
id: lem-ihorn-ultra-compression
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128 and delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, and Omega(omega) < b*tau satisfies ||q_A - p_v||_1 < tau/32 and h(q_A) <= delta(P)/S for every admissible exposer h at v, where q_A = (1/S)*sum_Q m_Q*p_Q.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass
deps: lem-affine-barycenter-identity
status: proved
af: none
provenance: W63 wave (docs/waves/2026-07-10-W63-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) DECOMPOSITION-W63-I.md node U + Appendix A.4; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W63-I-BATCH.md line 'U: VALID' (constant recomputed as (4*c_m+5)*tau/512 < tau/32; partial-fiber domination checked). Reviewer != author.
owner: B
---

**Role (W63 I-horn batch, 7/10 — ultra-isotropic compression).** In the
ultra-isotropic regime (both statistics below \(b\tau\)) the selected barycenter
\(q_A\) is pinned within \(\tau/32\) of \(p_v\) AND universally shadowed by every
admissible exposer. This is the opposite of promoting atom separation to
barycenter separation: it PROVES the small upper radius that makes the remaining
web a genuine SL1a-shaped object.

**Mechanism (one line).** Domination \(m\le\omega\) of the partially selected
full-fiber measure gives \(\|q_A-r_\omega\|_1\le(M/S)\Omega\)
([[lem-affine-barycenter-identity]] for the affine integrals); affine row
reproduction of the exact idempotent (\(\sum_jP_{vj}h(p_j)=h(p_v)=0\)) gives
\(\sum_jP^+_{vj}h(p_j)=\sum_jP^-_{vj}h(p_j)\le\nu_v\), then restrict to \(m\)
and divide by \(S\).

**Honest scope.** The supremum is over admissible exposers, not top support
functionals, and no exposers are averaged. All inequalities are on the selected
full-fiber measure. Fallback: retain the exact bounds
\(\|q_A-r_\omega\|_1\le M\Omega/S\) and \(h(q_A)\le\nu_v/S\).

**Rigour tier.** L5 (fresh hostile batched codex verdict, W63). NOT af-validated.
