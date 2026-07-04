# Proof Export

## Node 1

**Statement:** Pivot-removing max-stationarity: let P be a rank-3 exact signed idempotent (square real matrix with P^2 = P and all row sums equal to 1), let U = (u_0,u_1,u_2) be an actual-row chart whose rows p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space, let Vol_max(P) be the maximum Gram volume over actual-row charts, m_U = Vol(U)/Vol_max(P), define old coordinates a_t(i) by p_i = sum_t a_t(i)p_{u_t}, beta_r(i) = P_{u_r i}, lambda_r(i) = 1-a_r(i), mu_r(i) = sum_{t != r} max(-a_t(i),0), E_r(i) = max(mu_r(i)-lambda_r(i),0), Phi_r(U) = sum_i max(beta_r(i),0)E_r(i), and Phi(U) = max_r Phi_r(U), assume U is a theta-half Phi-argmin meaning m_U >= 1/2 and Phi(U) is minimal among actual-row charts W with Vol(W)/Vol_max(P) >= 1/2, fix a maximal pivot s with Phi_s(U)=Phi(U), and let j notin {u_0,u_1,u_2} have c = a_s(j) != 0 such that the pivot-removing chart V_j = U-u_s+j is theta-half admissible, equivalently |a_s(j)|*m_U >= 1/2 with volume factor Vol(V_j)/Vol(U)=|a_s(j)|; defining new coordinates on V_j by a_s^j(i)=a_s(i)/c and a_t^j(i)=a_t(i)-a_s(i)a_t(j)/c for t != s, E_r^j(i)=max(sum_{q != r} max(-a_q^j(i),0)-(1-a_r^j(i)),0), Psi_j=Phi_s(V_j)=sum_i max(P_{ji},0)E_s^j(i), and Gamma_j=max_{r != s} Phi_r(V_j)=max_{r != s} sum_i max(P_{u_r i},0)E_r^j(i), one has Phi_s(U) <= max(Psi_j, Gamma_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Because V_j is theta-half admissible, V_j lies among the actual-row charts W with Vol(W)/Vol_max(P) >= 1/2 to which the theta-half Phi-argmin property of U applies; hence Phi(U) <= Phi(V_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** The root hypothesis defines U being a theta-half Phi-argmin to mean: among actual-row charts W satisfying Vol(W)/Vol_max(P) >= 1/2, the value Phi(U) is minimal.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** The root hypothesis also says V_j is theta-half admissible; equivalently Vol(V_j)/Vol_max(P)=|a_s(j)| m_U >= 1/2 via Vol(V_j)/Vol(U)=|a_s(j)| and m_U=Vol(U)/Vol_max(P), so V_j is one of those comparison charts and minimality gives Phi(U) <= Phi(V_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** The root hypothesis fixes a maximal pivot s with Phi_s(U)=Phi(U).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For the pivot-removing chart V_j, the definitions of Psi_j, Gamma_j, and Phi give Phi(V_j)=max(Psi_j,Gamma_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For any rank-3 chart, Phi(chart) is the maximum of its three component values Phi_r(chart); separating the index r=s from the two indices r != s gives Phi(V_j)=max(Phi_s(V_j), max_{r != s} Phi_r(V_j)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** The root definitions for the pivot-removing chart give Psi_j=Phi_s(V_j) and Gamma_j=max_{r != s} Phi_r(V_j); substituting these two equalities into the preceding displayed maximum gives Phi(V_j)=max(Psi_j,Gamma_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Assuming the earlier subclaims Phi(U) <= Phi(V_j), Phi_s(U)=Phi(U), and Phi(V_j)=max(Psi_j,Gamma_j), elementary substitution and transitivity give Phi_s(U) <= max(Psi_j,Gamma_j), which is exactly the root conclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

