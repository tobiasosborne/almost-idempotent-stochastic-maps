---
id: def-pivot
term: pivot (chart)
aliases: pivot; maximal pivot; pivot-removing move; pivot-removing chart; theta-half chart; theta-half admissible; Phi-argmin chart; actual-row chart; Phi_r; Psi_j; Gamma_j
kind: original
status: draft
source: internal
locus: internal; first pinned in argument/lemmas/lem-pivot-removing-move.md (and inlined verbatim in conj-b-restricted / conj-gamma-emptiness)
sha256: -
consensus: project-original; sign-off pending (Rule 7 lock). First pinned by lem-pivot-removing-move
---

**Statement.** Fix a rank-$3$ [[def-signed-idempotent|exact signed idempotent]] $P$ with rows $p_i$.

- **Actual-row chart.** $U=(u_0,u_1,u_2)$, a triple of row indices whose rows $p_{u_0},p_{u_1},p_{u_2}$
  form a basis of the row space. Old coordinates: $a_q(i)$ with $p_i=\sum_q a_q(i)\,p_{u_q}$.
- **Charge functionals.** $E_r(i)=\max\!\big(\sum_{q\ne r}\max(-a_q(i),0)-(1-a_r(i)),\,0\big)$,
  $\Phi_r(U)=\sum_i\max(P_{u_r i},0)\,E_r(i)$, and $\Phi(U)=\max_r\Phi_r(U)$.
- **Volume gauge.** $\operatorname{Vol}(U)$ the Gram volume of the chart, $\operatorname{Vol}_{\max}(P)$
  the maximum Gram volume over actual-row charts, $m_U=\operatorname{Vol}(U)/\operatorname{Vol}_{\max}(P)$.
  $U$ is **theta-half** if $m_U\ge\tfrac12$; a **theta-half $\Phi$-argmin chart** is a theta-half $U$
  minimizing $\Phi$ among theta-half actual-row charts.
- **Pivot.** A **pivot** is a chart index $s$; a **maximal pivot** has $\Phi_s(U)=\Phi(U)$.
- **Pivot-removing move.** For a non-chart row $j$ with $c=a_s(j)\ne0$, the **pivot-removing chart**
  is $V_j=U-u_s+j$; it is **theta-half admissible** when $|a_s(j)|\,m_U\ge\tfrac12$ (volume factor
  $\operatorname{Vol}(V_j)/\operatorname{Vol}(U)=|a_s(j)|$). New coordinates on $V_j$:
  $a_s^{\,j}(i)=a_s(i)/c$ and $a_q^{\,j}(i)=a_q(i)-a_s(i)a_q(j)/c$ for $q\ne s$. The
  **transferred charges** are
  $\Psi_j=\sum_i\max(P_{ji},0)\,\max\!\big(\sum_{q\ne s}\max(-a_q^{\,j}(i),0)-(1-a_s^{\,j}(i)),0\big)$
  and $\Gamma_j=\max_{r\ne s}\sum_i\max(P_{u_r i},0)\,\max\!\big(\sum_{q\ne r}\max(-a_q^{\,j}(i),0)-(1-a_r^{\,j}(i)),0\big)$.

Pivot-removing max-stationarity ([[lem-pivot-removing-move]]) is the bound $\Phi_s(U)\le\max(\Psi_j,\Gamma_j)$.

**Notes / provenance.** Project-original; the "pivot" here is the chart-swap sense (a basis row
exchanged for an external row), NOT the generic linear-algebra pivot. This shard is the single home of
the rank-$3$ chart/volume vocabulary that was inlined verbatim in the contracts of
[[lem-pivot-removing-move]], [[conj-b-restricted]] and [[conj-gamma-emptiness]] (the latter two had
their notation preambles moved here 2026-07-10). `status: draft` — A+B sign-off pending (Rule 7).
Related: [[def-signed-idempotent]], [[def-negative-mass]].
