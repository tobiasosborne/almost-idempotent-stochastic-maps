---
id: def-negative-mass
term: negative mass
aliases: negativity; row polytope; row polytope K
kind: original
status: locked
source: internal
locus: quoted from classical-portfolio/report/kernel-conjecture.tex §Setting (def:esi, δ(P)); row polytope from ../almost-idempotent-positive-maps/definitions/def-stochastic.md
sha256: -
consensus: adapted from kernel-conjecture.tex §Setting (negativity δ(P)) and ../almost-idempotent-positive-maps definitions/def-stochastic.md (row polytope K)
---

**Statement.** For an [[def-signed-idempotent|exact signed idempotent]] $P\in\mathbb R^{n\times n}$ (or any
signed matrix), the *negative mass* (equivalently *negativity*) is
$$\delta(P):=\max_{1\le i\le n}\ \sum_{j=1}^{n}\max\{-P_{ij},\,0\},$$
the largest total negative mass in any single row. The *row polytope* is
$$K:=\operatorname{conv}\{p_1,\dots,p_n\},$$
the convex hull of the rows $p_i\in\mathbb R^n$. A [[def-stochastic|stochastic idempotent]] is exactly a
signed idempotent with $\delta(P)=0$.

**Notes / provenance.** $\delta(P)$ quoted from `classical-portfolio/report/kernel-conjecture.tex`
§Setting (Definition: *Exact signed idempotent*); the row polytope $K$ adopted from
`../almost-idempotent-positive-maps/definitions/def-stochastic.md`. This scalar is the single knob that
controls the geometry: the three derived scales $\tau=\sqrt\delta$, $\rho=4\tau$, $\kappa=\tau/4$ live in
[[def-visible-set]]. The $\delta$-positivity of [[def-near-positive-projection]] is the same quantity: a
unital idempotent $R$ is $\delta$-positive iff $\delta(R)\le\delta$.
