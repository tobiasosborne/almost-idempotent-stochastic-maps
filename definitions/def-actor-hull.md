---
id: def-actor-hull
term: always-tight hull
aliases: actor hull; K_T; K_O; K_T(u); K_O(u); always-tight hulls; disjoint always-tight hulls; displacement hull
kind: original
status: draft
source: internal
locus: internal; first pinned in argument/lemmas/lem-downhill-cotop-conic-mass.md and lem-always-tight-dual-support.md
sha256: -
consensus: project-original; sign-off pending (Rule 7 lock). First pinned by lem-always-tight-dual-support (the T/O families) + lem-downhill-cotop-conic-mass (the hulls K_T, K_O)
---

**Statement.** Fix an [[def-signed-idempotent|exact signed idempotent]] $P$ and a
[[def-exposed|hidden]] geometrically distinct row vertex $u$ with $t^*(u)>0$. Let $T(u)$, $O(u)$,
$Z(u)$ be the always-tight $\rho$-far / upper-box / [[def-zero-face|zero-face]] constraint families of
the exposedness LP at $u$ ([[lem-always-tight-dual-support]]). The **always-tight hulls** (or *actor
hulls*) are the displacement convex bodies
$$K_T(u):=\operatorname{conv}\{p_f-p_u:f\in T(u)\},\qquad
  K_O(u):=t^*(u)\cdot\operatorname{conv}\{p_i-p_u:i\in O(u)\}.$$
They are **disjoint** when $g:=\operatorname{dist}_1(K_T(u),K_O(u))>0$ (the huddle / Branch-I
predicate), and **intersect** otherwise (Branch II, the alpha-free optimal display of
[[lem-optimal-face-conic-reduction]]). Boundary ownership: tangency / any common point counts as
intersecting.

**Notes / provenance.** Project-original; "actor hull" and "always-tight hull(s)" name the same
displacement bodies $K_T,K_O$ built from the actors (far / upper-box rows) the
[[def-dual-witness|dual witness]] charges. The disjoint-vs-intersect dichotomy on $K_T,K_O$ is the
root split $S1$ of the W54 huddle-charge tree. `status: draft` — A+B sign-off pending (Rule 7).
Related: [[def-zero-face]], [[def-dual-witness]], [[def-co-top]].
