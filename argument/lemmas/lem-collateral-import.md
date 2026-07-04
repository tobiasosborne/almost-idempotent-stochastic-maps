---
id: lem-collateral-import
kind: lemma
contract: Collateral import bound: let P be a rank-3 exact signed idempotent (square real matrix with P^2 = P and all row sums equal to 1), let U = (u_0,u_1,u_2) be an actual-row chart whose rows p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space, define coordinates a_q(i) by p_i = sum_q a_q(i)p_{u_q}, beta_r(i) = P_{u_r i}, E_r(i) = max(sum_{q != r} max(-a_q(i),0) - (1 - a_r(i)), 0), and Phi_r(U) = sum_i max(beta_r(i),0)E_r(i); fix a pivot index s, a non-chart row j with c = a_s(j) > 0, a transverse index r != s, and let t be the remaining index, writing d_r = a_r(j) and d_t = a_t(j); on the pivot-removing chart V_j = U - u_s + j define new coordinates a_s^j(i) = a_s(i)/c and a_q^j(i) = a_q(i) - a_s(i)a_q(j)/c for q != s, E_r^j(i) = max(sum_{q != r} max(-a_q^j(i),0) - (1 - a_r^j(i)), 0), and Phi_r(V_j) = sum_i max(beta_r(i),0)E_r^j(i) (the transverse left-inverse row at r is unchanged by the move); define R_{r,j}(i) = (1/c - 1)*max(-a_s(i),0) + max(a_s(i)*d_t/c, 0) - a_s(i)*d_r/c and I_{r,j}(U) = sum_i max(beta_r(i),0)*max(R_{r,j}(i),0); then Phi_r(V_j) <= Phi_r(U) + I_{r,j}(U).
defs: def-signed-idempotent
deps: lem-pivot-removing-move
status: proved-mod-audit
af: seeded
provenance: docs/waves/2026-07-04-G10-collateral-branch.md §Task 3 "Emptiness-Lemma Attempt" (the per-row expansion E_r^j(i) <= E_r(i) + R_{r,j}(i)_+ via (-x+y)^+ <= x^- + y^+ and (X+Y)^+ <= X^+ + Y^+, summed against the unchanged transverse beta row); new-coordinate and unchanged-left-inverse formulas per the af-VALIDATED lem-pivot-removing-move contract
owner: A
workspace: proofs/lem-collateral-import
---

**The (CI) inequality** — G10's T1 tool for the (G) collateral branch of (PRT). The per-row step is
```text
E_r^j(i) <= E_r(i) + max(R_{r,j}(i), 0),
```
proved by expanding `E_r^j` with the [[lem-pivot-removing-move]] transform and applying the
elementary positive-part inequalities `(-x+y)^+ <= x^- + y^+` and `(X+Y)^+ <= X^+ + Y^+`; summing
against `max(beta_r(i),0)` (the transverse left-inverse row is unchanged by the move) gives the
contract inequality.

**Sharpness (T0, orchestrator-recomputed 2026-07-04).** On the G10 local witness (rank-3, 5 rows,
`delta = 49/60`, certified theta-half argmin, `M = 2/25`) the bound is EXACT:
`I_{1,j} = 11/40 = Phi_1(V_j)` with `Phi_1(U) = 0` — zero slack. The witness violates the
`delta <= 1/4` cap, so it stresses (CI), not (PRT).

**Role.** Combined with the af-validated disjunction of [[lem-pivot-removing-move]], a clean
Gamma-blocked branch (`Psi_j < M <= Gamma_j`) at a theta-half Phi-argmin forces
`M - Phi_r(U) <= I_{r,j}(U)` for some transverse `r`. The (PRT) collateral question is exactly
whether `I_{r,j}` is charged to `G_class^- + S_-^mu + SIGMA + FanRes` at `delta <= 1/4` for
high-self non-fan rows `j` ([[conj-sc]]), or whether the cap makes a clean Gamma branch
unrealizable. The `c > 0` restriction is inherited from the G10 derivation; the `c < 0` case is
not covered by this statement.
