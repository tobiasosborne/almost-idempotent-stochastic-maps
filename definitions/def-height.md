---
id: def-height
term: height
aliases: height H; H(P); hidden top vertex
kind: original
status: locked
source: internal
locus: quoted from classical-portfolio/report/kernel-conjecture.tex §Setting (Definition: Height)
sha256: -
consensus: adapted from kernel-conjecture.tex §Setting (Definition: Height, def:height)
---

**Statement.** Let $C_{\mathcal W}:=\operatorname{conv}\{p_w:w\in\mathcal W\}$, where $\mathcal W=\mathcal W(P)$
is the [[def-visible-set]], and let $\operatorname{dist}_1(x,S)=\inf_{s\in\operatorname{conv}S}\lVert x-s\rVert_1$.
If $\mathcal W\neq\emptyset$, the *height* of a row $p_i$ is $\operatorname{dist}_1(p_i,C_{\mathcal W})$, and
the *height of $P$* is
$$H=H(P):=\max_{1\le i\le n}\ \operatorname{dist}_1\!\big(p_i,\ \operatorname{conv}\{p_w:w\in\mathcal W\}\big).$$
Because $\operatorname{dist}_1(\cdot,C_{\mathcal W})$ is convex and every row is a convex combination of the
geometrically distinct row vertices, the maximum is attained at a row vertex; if $H>0$, any maximizing
vertex is necessarily [[def-exposed|hidden]]. Such a vertex is called a *hidden top vertex*.

**Notes / provenance.** Quoted from `classical-portfolio/report/kernel-conjecture.tex` §Setting
(Definition: *Height*). $H$ measures how far the rows spill outside the hull of the visible
([[def-visible-set]], [[def-exposed]]) vertices; the linear hull bound / HLC target is
$H(P)\le C\sqrt\delta$ in the [[def-negative-mass|negative mass]] $\delta$. The invisible mass
[[def-invisible-mass]] of a hidden top vertex is the hypothesis quantity that governs whether $H$ can be
large.
