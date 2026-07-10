---
id: lem-ihorn-drift-payer-extraction
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, k_b = c_m*b/64, and delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt and L = ||r_omega - p_v||_1 >= b*tau satisfies: for chi(x) = s.(x - p_v)/L with s an l1-norming sign vector of r_omega - p_v, ell_chi = sum over full row-point fibers R of |sum_{j in R} ((r_omega)_j - (p_v)_j)| > 0, A_lev = 1/(2*ell_chi) > 0, and F_chi = {R : |chi(p_R)| > A_lev}, every fiber R has |chi(p_R)| <= (2 + 4*delta(P))/L, and P_v^+(F_chi) >= k_b*tau.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-height
deps: lem-hx-transverse-moment-identity; lem-hx-financing-floor; lem-l5-positive-flow-foldback; lem-negpart-subadditive
status: proved
af: none
provenance: W63 wave (docs/waves/2026-07-10-W63-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) DECOMPOSITION-W63-I.md node ED + Appendix A.2; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W63-I-BATCH.md line 'ED: VALID' (corrected financing-floor call with distinct endpoints and A_lev > 0; foldback arithmetic (A.3) recomputed, V >= c_m*b*tau/18 > k_b*tau). Reviewer != author.
owner: B
---

**Role (W63 I-horn batch, 5/10 — natural-scale drift payer extraction).** When the
selected co-top web drifts at the natural scale (\(L\ge b\tau\)), one fixed
top-owned high-lever receiver set \(F_\chi\) with \(P_v^+\)-mass \(\ge k_b\tau\)
is CONSTRUCTED — the engine package the creative drift leaf (node D) must couple
to the priced ray.

**Mechanism (one line).** [[lem-hx-transverse-moment-identity]] makes
\(\ell_\chi>0\); the corrected [[lem-hx-financing-floor]] on the distinct pair
\((r_\omega,p_v)\) with lever \(\Lambda=D_0/L\) gives
\(r_\omega^+(F_\chi)+P_v^+(F_\chi)\ge L/(2D_0)-2\delta\); positive-part
subadditivity ([[lem-negpart-subadditive]], sign-reversed) dominates
\(Mr_\omega^+(F_\chi)\) by the actual \(\omega\)-actor flow; one
[[lem-l5-positive-flow-foldback]] application closes
\((1+M)V\ge M(L/(2D_0)-2\delta)-2\delta(1+\delta)\).

**Honest scope.** NOT the forbidden vanished-endpoint call: \(L\ge b\tau>0\) at
the call site and \(A_{\rm lev}>0\) explicit. One fixed receiver set folded once;
no pairwise floors summed. Fallback: retain the exact precursor inequality
instead of the clean \(k_b\tau\) floor.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W63). NOT af-validated.
