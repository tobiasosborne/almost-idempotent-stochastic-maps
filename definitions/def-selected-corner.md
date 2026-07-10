---
id: def-selected-corner
term: selected-corner configuration
aliases: selected corner; corner configuration; disintegration kernel xi; Gamma_f; M_X; M_I; M_D; B_F; B_N; C_f
kind: original
status: draft
source: internal
locus: internal; first pinned (inlined verbatim) in argument/lemmas/lem-sl1a-three-cell-reduction.md and the three conj-sl1a-*-cell shards
sha256: -
consensus: project-original; sign-off pending (Rule 7 lock). First pinned by lem-sl1a-three-cell-reduction (the SL1a three-cell surface)
---

**Statement.** Fix a finite [[def-signed-idempotent|exact signed idempotent]] $P$ with $0<\delta(P)$,
$\tau=\sqrt{\delta(P)}$, $D=2+4\delta(P)$, nonempty [[def-visible-set|visible set]] $\mathcal W$,
$C_{\mathcal W}=\operatorname{conv}\{p_w:w\in\mathcal W\}$, and a [[def-height|hidden top]] $v$ of
height $H>16\tau$. A **selected-corner configuration** is such $(P,v)$ together with:

- an affine $\phi$ with $\phi(p_v)=H$, $\phi\le0$ on $C_{\mathcal W}$, and $|\phi(a)-\phi(b)|\le\lVert a-b\rVert_1$
  (a [[def-top-support-functional|top support functional]]), an [[def-exposed|admissible exposer]] $h$ at
  $v$, and a **selected corner row** $f$ with $\lVert p_f-p_v\rVert_1\ge4\tau$,
  $\operatorname{dist}_1(p_f,C_{\mathcal W})>H-4\tau$ ([[def-co-top|co-top]] and $\rho$-far) satisfying
  the corner inequality $2(H-\phi(p_f))/D+h(p_f)\le 12\tau/13$;
- a **disintegration kernel** $\xi_x(u)$ from row points to geometrically distinct row vertices,
  constant on clone fibers, with $p_x=\sum_u\xi_x(u)p_u$ and Dirac at vertex points.

Write $P^+_{fx}=\sum_{j:p_j=p_x}\max(P_{fj},0)$, $\Gamma_f(x,u)=P^+_{fx}\,\xi_x(u)$,
$C_f=\{(x,u):H-\phi(p_x)<4\tau,\ h(p_x)<4\tau,\ H-\phi(p_u)<4\tau,\ h(p_u)<4\tau\}$,
$B_F=C_f\cap\{\lVert p_u-p_v\rVert_1\ge4\tau\}$, $B_N=C_f\cap\{\lVert p_u-p_v\rVert_1<4\tau\}$. For a
block $B\in\{B_F,B_N\}$ the three **corner masses** are
$$M_X(B)=\Gamma_f\{(x,u)\in B:p_x\ne p_u\},\quad
  M_I(B)=\Gamma_f\{(x,u)\in B:p_x=p_u,\ K_T(u)\cap K_O(u)\ne\emptyset\},$$
$$M_D(B)=\Gamma_f\{(x,u)\in B:p_x=p_u,\ K_T(u)\cap K_O(u)=\emptyset\},$$
with $K_T(u),K_O(u)$ the [[def-actor-hull|always-tight hulls]] at $u$ (off-diagonal $X$ = distinct
$p_x\ne p_u$; intersection $I$ = diagonal with intersecting hulls; deep $D$ = diagonal with disjoint
hulls).

**Notes / provenance.** Project-original; the single home of the SL1a "corner" machinery inlined
verbatim in [[lem-sl1a-three-cell-reduction]] and the three cell conjectures. The three cells partition
the selected corner's mass into the $X/I/D$ diagonal cells. `status: draft` — A+B sign-off pending
(Rule 7). Related: [[def-actor-hull]], [[def-co-top]], [[def-top-support-functional]], [[def-top-deficit]].
