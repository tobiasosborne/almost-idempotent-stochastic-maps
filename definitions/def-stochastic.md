---
id: def-stochastic
term: stochastic idempotent
aliases: row-stochastic idempotent; stochastic retraction; unital positive map on ℓ∞_n
kind: consensus
status: locked
source: internal
locus: adopted from ../almost-idempotent-positive-maps/definitions/def-stochastic.md
sha256: -
consensus: adopted from ../almost-idempotent-positive-maps definitions/def-stochastic.md (B's classical formulation, report sec:classical def:stochastic)
---

**Statement (commutative vocabulary).** A *unital positive map* of $\ell^\infty_n=\mathbb R^n$ is a
*row-stochastic matrix* $Q$ ($Q\ge0$ entrywise, $Q\mathbf 1=\mathbf 1$) — an affine self-map of the
probability simplex $\Delta_n$. A *stochastic idempotent* $E$ is a row-stochastic $E$ with $E^2=E$: an
affine retraction of $\Delta_n$ onto a sub-polytope.

Dropping positivity but keeping *exact* idempotence gives the *signed* generalization — a
[[def-signed-idempotent|signed affine retraction]] $P$ with $P\mathbf 1=\mathbf 1$ and $P^2=P$ exactly,
whose rows are signed measures of total mass $1$. Its failure of positivity is quantified by the
[[def-negative-mass|negative mass]] $\delta(P)$; a stochastic idempotent is exactly a signed idempotent
with $\delta(P)=0$.

**Notes / provenance.** Adopted from `../almost-idempotent-positive-maps/definitions/def-stochastic.md`
(B's classical formulation, report sec:classical `def:stochastic`); re-tagged `consensus` /
`source: internal` for this repo. The signed form is the working object because $P^2=P$ holds *exactly*
(non-positivity quarantined in $\delta$, see [[def-negative-mass]]). This is the commutative
specialization of [[def-near-positive-projection]]; the approximate-idempotence sibling is
[[def-almost-idempotent]] (a genuinely positive $Q$ with $\lVert Q^2-Q\rVert$ small). Exposed row
vertices and the visible set are [[def-exposed]] / [[def-visible-set]].
