---
id: def-invisible-mass
term: invisible mass
aliases: invisible positive mass; σ̃_v; invisible mass σ̃_v
kind: original
status: locked
source: internal
locus: quoted from classical-portfolio/report/kernel-conjecture.tex §Setting (Definition: Invisible mass σ̃_v; Remark: Halo robustness)
sha256: -
consensus: adapted from kernel-conjecture.tex §Setting (Definition: Invisible mass σ̃_v, def:sigt)
---

**Statement.** Let $C_{\mathcal W}:=\operatorname{conv}\{p_w:w\in\mathcal W\}$ ([[def-visible-set]]) and let
$p_v$ be a row vertex. The *invisible (positive) mass* of $v$ is
$$\widetilde\sigma_v:=\sum_{j\,:\,\operatorname{dist}_1(p_j,\,C_{\mathcal W})>0}\ \max\{P_{vj},\,0\},$$
the total positive coefficient mass that row $v$ places on rows lying strictly outside $C_{\mathcal W}$ —
*including* the index $j=v$ itself when $p_v\notin C_{\mathcal W}$ and $P_{vv}>0$.

*Halo robustness.* Replacing the condition $\operatorname{dist}_1(p_j,C_{\mathcal W})>0$ by
$\operatorname{dist}_1(p_j,C_{\mathcal W})>\varepsilon$ changes $\widetilde\sigma_v$ only by mass sitting
in the $\varepsilon$-halo of $C_{\mathcal W}$, which is absorbable as an $\varepsilon$-loss in the
[[def-height|height]]; the $\varepsilon=0$ form is used throughout.

**Notes / provenance.** Quoted from `classical-portfolio/report/kernel-conjecture.tex` §Setting
(Definition: *Invisible mass $\widetilde\sigma_v$*) with the *Halo robustness* remark. $\widetilde\sigma_v$
is the hypothesis quantity of the Kernel Conjecture: a hidden top vertex ([[def-height]]) with
$\widetilde\sigma_v>\tau=\sqrt\delta$ is the missing branch, while the $\widetilde\sigma_v\le\tau$ branch is
the proved height cap. Uses [[def-visible-set]], [[def-negative-mass]].
