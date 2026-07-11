---
id: lem-icap-score-bulk-production
kind: lemma
contract: For every c_m in (0,1), with b = c_m/128, delta_rt = min(2^(-16), (c_m/4)^2, (c_m*b/120)^2), and D_0 = 2 + 4*delta(P), every I-base datum (P,v,A) — P a finite exact signed idempotent with 0 < delta(P) <= 1/4 and nonempty visible set W, v a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), every j in A with ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau, full-fiber submeasure m_Q = sum_{j in A cap Q} max(P_vj, 0) of mass S = sum_Q m_Q >= c_m, omega the restriction of P_v^+ to G_v = {Q : ||p_Q - p_v||_1 >= 4*tau, dist_1(p_Q, conv{p_w : w in W}) > H - 8*tau}, for every c in K(P) with ||c - p_v||_1 <= 1/4 both P_v^+({Q in Sh_v : ||p_Q - c||_1 > 1/2}) < tau*S/16 and P_v^+({Q in G_v : ||p_Q - c||_1 > 1/2}) >= tau*S/16 with Sh_v = {Q : dist_1(p_Q, conv{p_w : w in W}) <= H - 8*tau} and P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0), ||r_omega - p_v||_1 < 1/8, and Omega(omega) < 1/16 (r_omega the normalized omega-barycenter; Omega the affine 1-Lipschitz scalar width) — with delta(P) <= delta_rt, ||r_omega - p_v||_1 < b*tau, Omega(omega) < b*tau, and theta = mu_A({Q : H - 8*tau < dist_1(p_Q, conv{p_w : w in W}) <= H - 4*tau}), where mu_A = m/S, satisfying theta < tau/D_0, and with an exhibited selected-corner certificate C* = (phi,h,f*,eta*) obtained from the lem-ihorn-selected-corner-extraction construction and satisfying M_X(C*) <= 1/8 and M_I(C*) >= 1/16 — letting lambda_A be the lem-ihorn-cotop-sl1a-package probability, a_A = S*(1-theta)*lambda_A <= P_v^+, z = H-phi, s(x) = 2*z(p_x)/D_0+h(p_x), and F = {x in supp(lambda_A) : s(x) <= 12*tau/13}, one has lambda_A(F) > 1/14 and a_A(F) > c_m/16; more generally lambda_A({s <= L*tau}) > 1-6/(7*L) for every L > 6/7.
defs: def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top
deps: lem-ihorn-cotop-sl1a-package; lem-sl1a-score-selector
status: proved
af: none
provenance: W64 wave (docs/waves/2026-07-11-W64-artifacts/): codex strategist-prover (gpt-5.6-sol, ultra) ICAP-ATTACK-W64.md §1.3 + appendix; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W64-ICAP-BATCH.md line S: VALID. Reviewer != author.
owner: B
---

**Role (W64 I-cap tree, S — score-bulk production).** Converts the fixed target certificate and co-top web into a score-good root set of constant normalized and top-owned mass before the X/I/D census.

**Mechanism (one line).** The admissible score components have \(\lambda_A\)-mean below \(6\tau/7\), so Markov at \(12\tau/13\), followed by \(a_A=S(1-\theta)\lambda_A\), gives the two mass floors.

**Honest scope.** The normalized \(\lambda_A\) is not confused with the owned measure \(a_A\); score equality belongs to \(F\), and the given \((\phi,h)\) is retained without a cover, averaging, or Jensen step. Fallback: retain \(\lambda_A\{s\le L\tau\}>1-6/(7L)\).

**Rigour tier.** L5 (fresh hostile batched codex verdict, W64). NOT af-validated.
