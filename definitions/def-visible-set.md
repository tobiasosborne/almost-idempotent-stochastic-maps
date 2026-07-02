---
id: def-visible-set
term: visible set
aliases: visible set W; W(P); (ρ,κ)-exposed set; three scales
kind: original
status: locked
source: internal
locus: quoted from classical-portfolio/report/kernel-conjecture.tex §Setting (def:scales, def:exposed)
sha256: -
consensus: adapted from kernel-conjecture.tex §Setting (Definition: three scales; Definition: (ρ,κ)-exposedness and the visible set W)
---

**Statement.** Given an [[def-signed-idempotent|exact signed idempotent]] $P$ with
$\delta=\delta(P)$ (the [[def-negative-mass|negative mass]]), the *three scales* are
$$\tau:=\sqrt\delta,\qquad \rho:=4\tau,\qquad \kappa:=\tau/4.$$
The *visible set* is
$$\mathcal W=\mathcal W(P):=\{\,v:\ p_v\text{ is a }(\rho,\kappa)\text{-exposed row vertex of }P\,\},$$
the set of row vertices that are [[def-exposed|$(\rho,\kappa)$-exposed]] at these scales; all other row
vertices are *hidden*. At $\delta=0$ the visible vertices are exactly the distinct rows of the recurrent
(equal-input) blocks of a stochastic idempotent.

**Notes / provenance.** Adapted from `classical-portfolio/report/kernel-conjecture.tex` §Setting
(Definition: *The three scales*; Definition: *$(\rho,\kappa)$-exposedness and the visible set $\mathcal W$*).
The scales couple exposedness ([[def-exposed]]) to the negative mass ([[def-negative-mass]]). The convex
hull $C_{\mathcal W}:=\operatorname{conv}\{p_w:w\in\mathcal W\}$ is consumed by [[def-height]] (max
$\ell^1$-distance of a row from $C_{\mathcal W}$) and [[def-invisible-mass]] (positive mass a row places
outside $C_{\mathcal W}$).
