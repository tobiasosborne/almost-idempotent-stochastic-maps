---
id: lem-ihorn-width-payer-extraction
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, k_b = c_m*b/64, and delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt and Omega(omega) >= b*tau satisfies: for any affine 1-Lipschitz scalar ell attaining Omega(omega), the sign split of the normalized omega at ell(r_omega) (zero values assigned to the plus class) has conditional masses s_+, s_- > 0 with s_+ + s_- = 1 and conditional barycenters q_+, q_- with s_+*s_-*||q_+ - q_-||_1 >= Omega(omega)/2; and with L = ||q_+ - q_-||_1, chi the recentered norming functional (chi(q_-) = 0, chi(q_+) = 1, l1-Lipschitz constant 1/L), ell_chi = sum over full row-point fibers R of |sum_{j in R} ((q_+)_j - (q_-)_j)| > 0, A_lev = 1/(2*ell_chi) > 0, and F_chi = {R : |chi(p_R)| > A_lev}, every fiber R has |chi(p_R)| <= (2 + 4*delta(P))/L and P_v^+(F_chi) >= k_b*tau.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-height
deps: lem-hx-transverse-moment-identity; lem-hx-financing-floor; lem-l5-positive-flow-foldback; lem-negpart-subadditive
status: proved
af: none
provenance: W63 wave (docs/waves/2026-07-10-W63-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) DECOMPOSITION-W63-I.md node EW + Appendix A.3; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W63-I-BATCH.md line 'EW: VALID' (exact sign-split chord identity; s_+s_- weights in (A.4) recomputed; c_m*b*tau/64 = k_b*tau). Reviewer != author.
owner: B
---

**Role (W63 I-horn batch, 6/10 — natural-scale width payer extraction).** When
the selected co-top web has scalar width at the natural scale
(\(\Omega\ge b\tau\)), an exact affine sign split constructs a quantitatively
separated synthetic pair (the weighted chord \(s_+s_-\|q_+-q_-\|_1\ge\Omega/2\))
and one fixed top-owned payer of \(P_v^+\)-mass \(\ge k_b\tau\) — the engine
package for the creative width leaf (node W); the legitimate core of the
second-moment/width-amplification idea.

**Mechanism (one line).** Exact affine centering gives the chord identity;
[[lem-hx-transverse-moment-identity]] + the corrected
[[lem-hx-financing-floor]] on \((q_+,q_-)\); multiply by \(Ms_+s_-\), dominate
both conditional positive parts by the actual \(\omega\)-actor flow
([[lem-negpart-subadditive]] sign-reversed), fold once by
[[lem-l5-positive-flow-foldback]].

**Honest scope.** The scalar optimizer is chosen only for its attained value —
no coordinate frame, no atom selector, not Jensen (an exact sign-split
identity). Small conditional masses are harmless only because separation is
retained in the PRODUCT \(s_+s_-\|q_+-q_-\|_1\); no mass floor for either
endpoint is inferred (recorded fallback).

**Rigour tier.** L5 (fresh hostile batched codex verdict, W63). NOT af-validated.
