---
id: def-exposed
term: exposed vertex
aliases: (ρ,κ)-exposed; (rho,kappa)-exposed; exposedness margin; admissible exposer; hidden row vertex; well-exposed vertex
kind: consensus
status: locked
source: internal
locus: adapted from classical-portfolio/report/kernel-conjecture.tex §Setting (def:vertex, def:exposed); ../almost-idempotent-positive-maps/definitions/def-exposed.md
sha256: -
consensus: adopted from ../almost-idempotent-positive-maps definitions/def-exposed.md (B's exposed-circuit machinery, report sec:classical); reconciled with kernel-conjecture.tex def:exposed
---

**Statement.** Fix an [[def-signed-idempotent|exact signed idempotent]] $P\in\mathbb R^{n\times n}$ and
write $p_i\in\mathbb R^n$ for its $i$-th row, with the $\ell^1$ metric $\lVert x-y\rVert_1=\sum_j|x_j-y_j|$.

A row $p_v$ is a *row vertex* of $P$ if $p_v\notin\operatorname{conv}\{\,p_j:p_j\neq p_v\text{ as vectors of }\mathbb R^n\,\}$
(geometrically coincident duplicate rows count as a single point; a repeated point is still a vertex if it
lies outside the hull of the *other* points).

An *admissible exposer* for a row vertex $v$ is an affine function $h:\mathbb R^n\to\mathbb R$ with
$$h(p_v)=0\qquad\text{and}\qquad 0\le h(p_j)\le 1\quad\text{for every row }p_j.$$
The *exposedness margin* of $v$ is
$$t^*(v):=\sup_{h\text{ admissible}}\ \min\{\,h(p_j):\lVert p_j-p_v\rVert_1\ge\rho\,\},$$
with the convention $t^*(v)=+\infty$ when no row is at $\ell^1$-distance $\ge\rho$ from $p_v$. The vertex
$v$ is *$(\rho,\kappa)$-exposed* if $t^*(v)\ge\kappa$, and *hidden* otherwise. The scales $\rho=4\tau$,
$\kappa=\tau/4$ (with $\tau=\sqrt\delta$) and the resulting *visible set* $\mathcal W(P)$ of exposed
vertices are recorded in [[def-visible-set]].

Informally: an exposed vertex can be linearly separated, with margin $\ge\kappa$, from every row that is
genuinely far ($\ge\rho$) from it; rows inside the $\rho$-ball are exempt.

**Notes / provenance.** Adapted from `classical-portfolio/report/kernel-conjecture.tex` §Setting
(def:vertex, def:exposed) and `../almost-idempotent-positive-maps/definitions/def-exposed.md`. The latter
states the equivalent *exposedness modulus* $e_v(\rho)=\sup_h\min_{\lVert p_i-v\rVert_1\ge\rho}h(p_i)$ and
calls a vertex *well-exposed* at $\sqrt{}$-scale if $e_v(\rho)\ge c\sqrt\delta$ for some
$\rho=O(\sqrt\delta)$, where $\delta$ is the [[def-negative-mass|negative mass]]. Central to the proved
classical special cases (well-exposed $\Rightarrow$ simplex) and to the open global exposed-hull lemma
(`op-exposed-hull`). A pointwise exposed-or-redundant dichotomy is provably *insufficient* (dense regular
polygons) — the gap must be stated globally (see [[def-height]]).
