---
id: def-near-positive-projection
term: near-positive projection
aliases: δ-positive unital idempotent; delta-positive unital idempotent; near-idempotent stochastic map; near-positive idempotent
kind: original
status: locked
source: internal
locus: adopted from ../almost-idempotent-positive-maps/definitions/def-near-positive-projection.md (commutative shadow)
sha256: -
consensus: adopted from ../almost-idempotent-positive-maps definitions/def-near-positive-projection.md (B's factorization program, op:npps); commutative shadow agreed for this repo
---

**Statement (commutative shadow).** A *near-positive projection* is a linear map
$R\colon\ell^\infty_n\to\ell^\infty_n$ that is an exact unital idempotent, $R^2=R$ and
$R(\mathbf 1)=\mathbf 1$, and is *$\delta$-positive*: for every $0\le x$ (entrywise) with
$\lVert x\rVert_\infty\le1$ one has $Rx\ge-\delta\,\mathbf 1$, for a small parameter
$\delta\in[0,\delta_0)$. As a matrix this is exactly an [[def-signed-idempotent|exact signed idempotent]]
whose [[def-negative-mass|negative mass]] satisfies $\delta(R)\le\delta$ (and $\lVert R\rVert\le1+O(\delta)$).

The motivating operator-algebra example is the spectral idempotent $P=\theta(2\Phi-\mathbf 1)$ built from
an [[def-almost-idempotent]] $\Phi$, with $\delta=O(\eta)$; such a $P$ need **not** be a genuinely
positive map. *Near-positive-projection stability* (the open hypothesis parenting `op-classical`) asks
whether every near-positive projection is within $C\sqrt\delta$ (operator norm) of a genuine *positive*
unital idempotent — a [[def-stochastic|stochastic idempotent]] $E$; the $\sqrt{}$ exponent is sharp
(Hume's $3\times3$ family).

**Notes / provenance.** Adopted from `../almost-idempotent-positive-maps/definitions/def-near-positive-projection.md`
(B's factorization program, `op:npps`), taken here as the commutative shadow / general parent of the
classical object. This is the map/positivity framing of the same object as [[def-signed-idempotent]]
(matrix/geometry framing): $R$ is $\delta$-positive iff $\delta(R)\le\delta$. The *stability* statement is
an open registry problem, not part of this definition.
