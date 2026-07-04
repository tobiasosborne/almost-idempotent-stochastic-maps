---
id: lem-pivot-removing-move
kind: lemma
contract: Pivot-removing max-stationarity: let P be a rank-3 exact signed idempotent (square real matrix with P^2 = P and all row sums equal to 1), let U = (u_0,u_1,u_2) be an actual-row chart whose rows p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space, let Vol_max(P) be the maximum Gram volume over actual-row charts, m_U = Vol(U)/Vol_max(P), define old coordinates a_t(i) by p_i = sum_t a_t(i)p_{u_t}, beta_r(i) = P_{u_r i}, lambda_r(i) = 1-a_r(i), mu_r(i) = sum_{t != r} max(-a_t(i),0), E_r(i) = max(mu_r(i)-lambda_r(i),0), Phi_r(U) = sum_i max(beta_r(i),0)E_r(i), and Phi(U) = max_r Phi_r(U), assume U is a theta-half Phi-argmin meaning m_U >= 1/2 and Phi(U) is minimal among actual-row charts W with Vol(W)/Vol_max(P) >= 1/2, fix a maximal pivot s with Phi_s(U)=Phi(U), and let j notin {u_0,u_1,u_2} have c = a_s(j) != 0 such that the pivot-removing chart V_j = U-u_s+j is theta-half admissible, equivalently |a_s(j)|*m_U >= 1/2 with volume factor Vol(V_j)/Vol(U)=|a_s(j)|; defining new coordinates on V_j by a_s^j(i)=a_s(i)/c and a_t^j(i)=a_t(i)-a_s(i)a_t(j)/c for t != s, E_r^j(i)=max(sum_{q != r} max(-a_q^j(i),0)-(1-a_r^j(i)),0), Psi_j=Phi_s(V_j)=sum_i max(P_{ji},0)E_s^j(i), and Gamma_j=max_{r != s} Phi_r(V_j)=max_{r != s} sum_i max(P_{u_r i},0)E_r^j(i), one has Phi_s(U) <= max(Psi_j, Gamma_j).
defs: def-signed-idempotent
deps: 
status: proved
af: validated
provenance: docs/waves/2026-07-03-G7-sc-decider.md §T1 "Pivot-Removing Schur Move" eqs. (1),(2),(4),(5),(6) and §T1 "Exact Phi Disjunction" eq. (7)
owner: A
workspace: proofs/lem-pivot-removing-move
---

**Transcribed formulas.** G7 gives the pivot-removing volume identity
```text
Vol(U-u_s+j)/Vol(U) = |a_s(j)|.
```

For `c=a_s(j)` and `d_t=a_t(j)`, the new coordinates are
```text
a_s^j(i) = a_s(i)/c,
a_t^j(i) = a_t(i) - a_s(i)d_t/c  (t != s),
```
and the old pivot row has
```text
a_s^j(u_s)=1/c,       a_t^j(u_s)=-d_t/c.
```

The new left-inverse rows are
```text
B_s^j = P_j = sum_r a_r(j)B_r,       B_t^j = B_t  (t != s).
```

**Where minimality enters.** Since `V_j` is theta-half admissible and `U` is a theta-half `Phi`-argmin,
```text
Phi_s(U) = Phi(U) <= Phi(V_j) = max(Psi_j, Gamma_j).
```

This is the first arm-G statement that genuinely uses `Phi`-minimality. The formulas alone do not prove [[conj-sc]]; they only name the pivot-removing alternatives.

**af-VALIDATED IN-REPO 2026-07-04** (run 1 clean, 3 rounds, zero challenges): 9-node adversarial
tree, root `validated`, taint 9/9 clean; fresh codex provers/verifiers per node, Claude orchestrated
only (§6). Export: `proofs/lem-pivot-removing-move/export.md`. Status flip is the mechanical
reflection of the codex ledger.
