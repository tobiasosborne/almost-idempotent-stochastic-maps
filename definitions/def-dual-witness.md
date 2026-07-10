---
id: def-dual-witness
term: hiddenness dual witness
aliases: dual witness; dual certificate; small-beta witness; reduced optimal witness; witness balance; (lambda, alpha, beta)
kind: original
status: draft
source: internal
locus: internal; first pinned in argument/lemmas/lem-hiddenness-dual-witness.md
sha256: -
consensus: project-original; sign-off pending (Rule 7 lock). First pinned by lem-hiddenness-dual-witness (the LP-dual object) + lem-always-tight-dual-support (support localization)
---

**Statement.** Fix an [[def-signed-idempotent|exact signed idempotent]] $P$ and a
[[def-exposed|hidden]] row vertex $v$ ($\rho=4\tau$, $\kappa=\tau/4$, $\tau=\sqrt{\delta(P)}$), with
$F_v=\{j:\lVert p_j-p_v\rVert_1\ge\rho\}$ the (nonempty) $\rho$-far row set.

A **hiddenness dual witness** of $v$ is a triple $(\lambda,\alpha,\beta)$ of nonnegative
coefficients — $\lambda_f\ (f\in F_v)$ with $\sum_f\lambda_f=1$ (a probability on the far rows), and
$\alpha_i,\beta_i\ge0$ over all rows with $\sum_i\beta_i=t^*(v)<\kappa$ — satisfying the *witness
balance*
$$\sum_{f\in F_v}\lambda_f\,(p_f-p_v)\;+\;\sum_i\alpha_i\,(p_i-p_v)\;=\;\sum_i\beta_i\,(p_i-p_v).$$
It is the LP dual of the exposedness program (see [[def-exposed]]); the *small-beta* property is
$\sum_i\beta_i=t^*(v)<\kappa$. A witness is **reduced** when redundant centered-zero constraints are
deleted; by [[lem-always-tight-dual-support]] a reduced optimal witness has
$\operatorname{supp}(\lambda)\subseteq T$, $\operatorname{supp}(\beta)\subseteq O$, and
$\operatorname{supp}(\alpha)\subseteq Z$ (the [[def-actor-hull|always-tight]] far / upper-box /
[[def-zero-face|zero-face]] families).

**Notes / provenance.** Project-original; from [[lem-hiddenness-dual-witness]] (existence via finite
LP duality). The witness converts the scalar hiddenness fact $t^*(v)<\kappa$ into a geometric object:
a convex combination of $\rho$-far rows reproducing $p_v$ up to controlled signed slack. "dual
certificate" is used interchangeably in the shards. `status: draft` — A+B sign-off pending (Rule 7).
Related: [[def-zero-face]], [[def-actor-hull]], [[def-co-top]].
