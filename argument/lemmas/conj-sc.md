---
id: conj-sc
kind: lemma
contract: Self-support/cancellation control: there are universal constants C_SC and C_fan_prime such that for every rank-3 exact signed idempotent P (square real matrix with P^2 = P and all row sums equal to 1) with 0 < delta(P) <= 1/4 where delta(P) = max_i sum_l max(-P_il, 0), every actual-row chart U = (u_0, u_1, u_2) whose rows p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space and whose Gram volume Vol(U) >= (1/2)Vol_max(P) minimizes Phi(U) = max_r Phi_r(U) among such charts, with coordinates a_t(i) defined by p_i = sum_t a_t(i)p_{u_t}, beta_r(i) = P_{u_r i}, lambda_r(i) = 1 - a_r(i), mu_r(i) = sum_{t != r} max(-a_t(i), 0), E_r(i) = max(mu_r(i) - lambda_r(i), 0), Phi_r(U) = sum_i max(beta_r(i), 0)E_r(i), every maximal pivot s with Phi_s(U) = Phi(U), B(U) = {j : j is not one of u_0,u_1,u_2}, NF_s(U) = {j in B(U) : beta_s(j) > 0 and j is non-fan, meaning j is an active orphan with E_s(j) > 0 and a strict legal active-preserving cover but no volume-permitted negative active-preserving cover keeping u_s, or a lambda-positive orphan with mu_s(j) > 0, E_s(j) = 0, a strict legal active-preserving cover keeping u_s with Schur volume factor > 1/2, and the same no-negative-cover property, or a silent row such that every active-preserving covering block containing j and keeping u_s has Schur volume factor |det C| <= 1/2}, W_s(j) = sum_{t != s} max(-a_t(j), 0), G_class^-(s,U) = sum_{r=0}^2 max(-P_{u_s u_r}, 0), S_-^mu(s,U) = sum_{j in B(U)} max(-beta_s(j), 0)mu_s(j), nu_j = sum_l max(-P_jl, 0), SIGMA_s(U) = sum_{j in B(U): beta_s(j) > 0} beta_s(j)nu_j, and FanRes_s(U) = sum_{j in B(U), t != s, beta_s(j) > 0, a_t(j) < -1/2} (max(-a_t(j),0)/mu_s(j))*(Phi_s(U-u_t+j) - (Phi_s(U) - beta_s(j)E_s(j))) over the G1/G2 one-row volume-permitted negative fan covers, one has sum_{j in NF_s(U)} beta_s(j)W_s(j) <= C_SC*(G_class^-(s,U) + S_-^mu(s,U) + SIGMA_s(U)) + C_fan_prime*FanRes_s(U).
defs: def-signed-idempotent; def-negative-mass
deps: 
status: conjecture
af: none
provenance: docs/waves/2026-07-03-G7-sc-decider.md §Target display (SC) and §T2 "Status Of (SC)"; docs/waves/2026-07-03-G6-repaired-horn.md §T1/T2 "What Would Prove RH"; docs/waves/2026-07-03-G8-transfer-financing.md display (PRT); docs/waves/2026-07-04-G9-prt-realizability.md §Verdict
owner: A
workspace: proofs/conj-sc
---

**Budget convention.** `G_class^-`, `S_-^mu`, and `SIGMA` are in the G5/G6 sense. In particular, `SIGMA` counts all beta-positive non-chart rows, not only rows contributing directly to `OD`.

**Role.** This is the isolated missing step for [[conj-rh]] after G6: it must turn non-fan chart-negative mass into class/signed, own-negativity, and fan-collateral budgets.

**Reduction.** G8 reduces the remaining high-self part to the pivot-removing transfer target `(PRT)`. The low-self side is governed by the transfer-financing identity `(FE)`, but `(FE)` alone controls only `kappa_j W_j`.

**G9 narrowing.** G9 realizes the volume-inadmissible `(V)` branch and the Psi-blocked `(P)` branch by exact certified instances; the Gamma-blocked `(G)` collateral branch remains the sole undecided branch.

**Minimality requirement.** Any proof must use Phi-minimality through [[lem-pivot-removing-move]]. G6 explicitly refutes the pointwise shortcut `nu_j >= a_t(j)^-`.
