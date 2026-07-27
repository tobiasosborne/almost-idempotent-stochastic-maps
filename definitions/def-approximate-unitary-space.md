---
id: def-approximate-unitary-space
term: approximate unitary space
aliases: approximate unitaries; unitary set of an epsilon-C*-algebra
kind: consensus
status: locked
source: internal
locus: adopted from refs/kitaev-2405.02434 approximate_algebras.tex:692-706 (sets), 845-859 (u,h and group maps), 945 (U_e and the scalar quotient)
sha256: -
consensus: user-ratified 2026-07-27 (W79 decision D2, docs/plans/2026-07-27-W78-ratification-package.md; content per DESIGN-S1-POLAR-v6.md sect 8, audited AUDIT-S1-POLAR-v4/v5/v6)
---

**Statement (vocabulary and reserved notation only).** Let
$(\mathcal X,J,\boldsymbol\cdot,\dagger)$ be an exact-unit
$\varepsilon$-$C^*$-algebra ([[def-epsilon-cstar-algebra]]). Define:

- $\mathcal H=\{X\in\mathcal X: X^\dagger=X\}$ (Hermitian) and
  $i\mathcal H=\{X\in\mathcal X: X^\dagger=-X\}$ (anti-Hermitian);
- $\overline{\mathcal U}_\delta=\{X\in\mathcal X:\ \lVert X^\dagger\boldsymbol\cdot X-J\rVert\le 2\delta$
  and $X$ has a right inverse$\}$, and $\mathcal U_\delta$ the analogous set
  with the strict inequality $\lVert X^\dagger\boldsymbol\cdot X-J\rVert<2\delta$;
- the *unitaries* $\mathcal U=\overline{\mathcal U}_0$;
- $\mathcal U_e$ = the connected component of $\mathcal U$ containing $J$,
  and the scalar action $U\equiv cU$ for $c\in U(1)$ on it.

For a point $V$ for which the left-multiplier $L_V$ is invertible, reserve
the *coordinate notation* $\phi_V(X)=L_V^{-1}\boldsymbol\cdot(X-V)$ and its
components $\phi_V^{\parallel}$ (anti-Hermitian part) and $\phi_V^{\perp}$
(Hermitian part). Reserve the symbols $u,h$ (polar inverse components) and
$\mu,\sigma$ (group operations) ONLY as partial notation on domains supplied
by result rows.

**Notes / provenance.** Vocabulary/typing only — this shard asserts NO
chart, inverse, estimate, smoothness, compactness, orientation, or isolation
theorem (all of those are the contracts of the Stage-1 polar result rows,
`DESIGN-S1-POLAR-v6.md` §3). Adopted from the local source's approximate-
unitary discussion with harmonised notation; the source loci are recorded
above for orientation, but this is a `consensus` adoption, not a byte-cited
definition. Related: [[def-epsilon-cstar-algebra]],
[[def-stage1-polar-witness-data]], [[def-h-space-left-inversion]],
[[def-lefschetz-fixed-point-data]].
