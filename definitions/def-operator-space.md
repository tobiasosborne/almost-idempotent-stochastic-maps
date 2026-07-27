---
id: def-operator-space
term: operator space
aliases: self-adjoint operator space
kind: cited
status: locked
source: kitaev-2405.02434
locus: approximate_algebras.tex:1453-1464 (Definition def:opspace)
sha256: e7eb512a2ec2438d
consensus: user-ratified 2026-07-27 (W79 decision D2, docs/plans/2026-07-27-W78-ratification-package.md; byte-verified this date)
---

**Statement (byte-matched; harmonised notation $\mathcal L$, $M_{n,k}$).** A complex
vector space $\mathcal L$ is called an *operator space* if each space
$M_n\otimes\mathcal L$ (for $n=1,2,\ldots$) is equipped with a norm
$\lVert\cdot\rVert_n$ satisfying the following axioms:

$$\lVert AXB\rVert_n \le \lVert A\rVert\,\lVert X\rVert_k\,\lVert B\rVert
\qquad (A\in M_{n,k},\; B\in M_{k,n},\; X\in M_k\otimes\mathcal L),$$

$$\left\lVert\begin{pmatrix}X&0\\ 0&Y\end{pmatrix}\right\rVert_{k+n}
= \max\bigl\{\lVert X\rVert_k,\lVert Y\rVert_n\bigr\}
\qquad (X\in M_k\otimes\mathcal L,\; Y\in M_n\otimes\mathcal L).$$

The norm on $\mathcal L$ itself is defined by identifying $\mathcal L$ with
$M_1\otimes\mathcal L$. An operator space is called *self-adjoint* if it is
equipped with a conjugate-linear involution $\dagger$ that preserves all norms
$\lVert\cdot\rVert_n$.

**Notes / provenance.** Byte-verbatim from the local source Definition block at
`approximate_algebras.tex:1453-1464` ONLY (per `AUDIT-MAIN-STRUCTURE-v3.md` §2:
the rectangular norms/inclusions constructed at `approximate_algebras.tex:1467-1475`
are DERIVED notation/consequences, referenced in later result-row provenance but
deliberately NOT primitive fields of this cited definition). Provisioned as the
P0 vocabulary gate of the MAIN-CB structural design
(`DESIGN-MAIN-STRUCTURE-v5.md` §1.1). Related: [[def-epsilon-cstar-algebra]],
[[def-extended-epsilon-cstar-algebra]], [[def-compressed-corner]].
