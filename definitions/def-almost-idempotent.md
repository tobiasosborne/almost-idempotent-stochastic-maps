---
id: def-almost-idempotent
term: almost idempotent
aliases: η-idempotent; eta-idempotent; almost-idempotent stochastic matrix
kind: consensus
status: locked
source: internal
locus: adopted from ../almost-idempotent-positive-maps/definitions/def-almost-idempotent.md (stochastic specialization)
sha256: -
consensus: adopted from ../almost-idempotent-positive-maps definitions/def-almost-idempotent.md (operator-norm formulation, report rem:cb-norm); ∞→∞ specialization per kernel-conjecture.tex thm:chain(c)
---

**Statement (commutative / stochastic specialization).** A [[def-stochastic|row-stochastic matrix]] $Q$
on $\ell^\infty_n$ is *almost idempotent* (with defect $\eta$) if
$$\lVert Q^2-Q\rVert_{\infty\to\infty}\le\eta,\qquad \eta\in[0,\tfrac14),$$
where $\lVert\cdot\rVert_{\infty\to\infty}$ is the operator norm induced by $\ell^\infty_n$ — i.e. the
maximum over rows of the $\ell^1$-norm of the corresponding row of $Q^2-Q$. The range $\eta<\tfrac14$ is
what makes the binomial series producing the exact idempotent converge.

**Notes / provenance.** Adopted from `../almost-idempotent-positive-maps/definitions/def-almost-idempotent.md`
(the operator-norm — *not* cb-norm — formulation, report rem:cb-norm), specialized to the
$\lVert\cdot\rVert_{\infty\to\infty}$ map norm on stochastic matrices as in
`classical-portfolio/report/kernel-conjecture.tex` Theorem (chain)(c). Measuring non-idempotence in the
map operator norm (rather than the cb-norm) is why the bridge exponent is $\sqrt\eta$ rather than $\eta$.
The classical stability question (`op-classical`) asks whether every such $Q$ lies within $C\sqrt\eta$
(max-row-$\ell^1$) of an exactly idempotent row-stochastic matrix; its parent object is
[[def-near-positive-projection]]. Distinguish $\eta$ (this defect) from the
[[def-negative-mass|negative mass]] $\delta$ of the associated [[def-signed-idempotent]], with
$\delta=O(\eta)$.
