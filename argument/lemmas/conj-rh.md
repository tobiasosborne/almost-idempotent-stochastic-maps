---
id: conj-rh
kind: lemma
contract: Repaired orphan horn: there are universal constants C_RH and C_RH_fan such that for every rank-3 exact signed idempotent P (square real matrix with P^2 = P and all row sums equal to 1) with 0 < delta(P) <= 1/4 where delta(P) = max_i sum_l max(-P_il, 0), every actual-row chart U = (u_0, u_1, u_2) whose rows p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space and whose Gram volume Vol(U) >= (1/2)Vol_max(P) minimizes Phi(U) = max_r Phi_r(U) among such charts, with coordinates a_t(i) defined by p_i = sum_t a_t(i)p_{u_t}, beta_r(i) = P_{u_r i}, lambda_r(i) = 1 - a_r(i), mu_r(i) = sum_{t != r} max(-a_t(i), 0), E_r(i) = max(mu_r(i) - lambda_r(i), 0), Phi_r(U) = sum_i max(beta_r(i), 0)E_r(i), every maximal pivot s with Phi_s(U) = Phi(U), B(U) = {j : j is not one of u_0,u_1,u_2}, active orphan set O_act(s,U) = {j in B(U) : beta_s(j) > 0, E_s(j) > 0, j has a strict legal active-preserving cover keeping u_s with Schur volume factor |det C| > 1/2, and j has no volume-permitted negative active-preserving cover keeping u_s}, L_mu^orph = sum_{j in O_act(s,U)} beta_s(j)mu_s(j), F_L^orph = sum_{l in B(U)} mu_s(l)max(-sum_{j in O_act(s,U)} beta_s(j)P_jl, 0), OD_s^orph(U) = L_mu^orph + F_L^orph + sum_{j in O_act(s,U)} beta_s(j)E_s(j), G_class^-(s,U) = sum_{r=0}^2 max(-P_{u_s u_r}, 0), S_-^mu(s,U) = sum_{j in B(U)} max(-beta_s(j), 0)mu_s(j), nu_j = sum_l max(-P_jl, 0), SIGMA_s(U) = sum_{j in B(U): beta_s(j) > 0} beta_s(j)nu_j, and FanRes_s(U) = sum_{j in B(U), t != s, beta_s(j) > 0, a_t(j) < -1/2} (max(-a_t(j),0)/mu_s(j))*(Phi_s(U-u_t+j) - (Phi_s(U) - beta_s(j)E_s(j))) over the G1/G2 one-row volume-permitted negative fan covers, one has OD_s^orph(U) <= C_RH*(G_class^-(s,U) + S_-^mu(s,U) + SIGMA_s(U)) + C_RH_fan*FanRes_s(U).
defs: def-signed-idempotent; def-negative-mass
deps: 
status: conjecture
af: seeded
provenance: docs/waves/2026-07-03-G6-repaired-horn.md §Target display (RH), §T1/T2 "What Would Prove RH" eq. (6), and §Verdict; docs/waves/2026-07-03-G5-orphan-financing-lemma.md eqs. (8)-(10); docs/waves/2026-07-03-G7-sc-decider.md §T2 "(RH) Assembly Status"
owner: A
workspace: proofs/conj-rh
---

**Budget convention.** This uses the G5/G6 `G_class^-` pivot-class aggregate, not any broader `G^-`. `SIGMA` is the G6 repair term over all beta-positive non-chart rows, including silent rows.

**Floor.** [[obs-orphan-amplifier]] forces the budget coefficient in front of `G_class^- + S_-^mu + SIGMA` to be at least `4`: in that family `FanRes_s(U)=0`, `OD -> 1/2`, and the repaired denominator tends to `1/8`.

**Assembly interfaces.** G5 supplies the harmonic ledger with cancellations taken before positive parts. G6 supplies the rank-3 active-orphan overhead `E_s(j) <= mu_s(j)` on the rows entering `OD`. The fan contribution is deliberately left as `FanRes_s(U)` rather than silently absorbed.

**Reduction status.** This is the repaired horn left open after G6 and G7. It is expected to assemble from [[conj-sc]] plus the fan horn, but no proof is recorded here.
