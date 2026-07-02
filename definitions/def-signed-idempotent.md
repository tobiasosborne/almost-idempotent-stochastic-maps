---
id: def-signed-idempotent
term: exact signed idempotent
aliases: signed idempotent; signed affine retraction; signed stochastic retraction
kind: original
status: locked
source: internal
locus: quoted from classical-portfolio/report/kernel-conjecture.tex §Setting (Definition, exact signed idempotent)
sha256: -
consensus: adapted from ../almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex §Setting (def:esi); exact-idempotence form adopted for this repo
---

**Statement (exact signed idempotent).** Let $n\in\mathbb N$. A matrix $P\in\mathbb R^{n\times n}$ is an
*exact signed idempotent* if
$$P\mathbf 1=\mathbf 1\qquad\text{and}\qquad P^2=P,$$
where $\mathbf 1=(1,\dots,1)^{\mathsf T}$. Equivalently, $P$ is a linear self-map of $\mathbb R^n$ fixing
the all-ones vector with $P^2=P$ *exactly*, whose rows are signed measures of total mass $1$
($\sum_j P_{ij}=1$ for each $i$). A row-stochastic idempotent — a [[def-stochastic|stochastic idempotent]]
— is exactly an exact signed idempotent whose [[def-negative-mass|negative mass]] $\delta(P)=0$.

*Row geometry.* Writing $p_i\in\mathbb R^n$ for the $i$-th row with the $\ell^1$ metric, each row
satisfies $\sum_j p_{ij}=1$ and $\sum_j|p_{ij}|\le1+2\delta$; hence all rows lie in a common affine
hyperplane and pairwise $\ell^1$ distances are at most $2+4\delta$ (with $\delta=\delta(P)$).

**Notes / provenance.** Quoted from `classical-portfolio/report/kernel-conjecture.tex` §Setting
(Definition: *Exact signed idempotent*, and the row-geometry remark). The exact-idempotence form is the
working object: $P^2=P$ holds exactly while non-positivity is quarantined into the scalar
[[def-negative-mass|negative mass]] $\delta(P)$. This is the matrix/geometry framing of
[[def-near-positive-projection]] (map/positivity framing). Its exposed row vertices, visible set, height
and invisible mass are [[def-exposed]], [[def-visible-set]], [[def-height]], [[def-invisible-mass]].
