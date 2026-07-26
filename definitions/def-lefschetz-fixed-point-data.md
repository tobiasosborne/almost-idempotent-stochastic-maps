---
id: def-lefschetz-fixed-point-data
term: Lefschetz number and local fixed-point index
aliases: Lefschetz number; fixed point index; fixed-point index; ind(f,x); Lambda(f)
kind: cited
status: locked
consensus: byte-match lock per definitions/README.md (cited criterion); provisioned by DESIGN-FUDW-DECOMP-v4.1.md §4.1 (kind "cited / lock after byte-match")
source: kitaev-2405.02434
locus: approximate_algebras.tex:961-967
sha256: e7eb512a2ec2438d
---

**Byte-verbatim source text.**

```tex
The \emph{fixed point index} $\ind(f,x)$ and the \emph{Lefschetz number} $\Lambda(f)$ are defined as follows:
\begin{alignat}{2}
\ind(f,x)&=\sgn\det(1-f'(x)),\qquad
& f'(x)\colon \Ta_xM&\to\Ta_xM,\\[2pt]
\Lambda(f)&=\sum_{k}(-1)^k\Tr f^{*k},\qquad
& f^{*k}\colon H^k(M;\RR)&\to H^k(M;\RR),
\end{alignat}
```

**Statement (harmonised).** For a smooth self-map $f$ of a compact orientable
manifold $M$: at a fixed point $x$ with $\det(1-f'(x))\ne0$ (where
$f'(x)\colon T_xM\to T_xM$ is the differential), the *fixed point index* is
$\operatorname{ind}(f,x)=\operatorname{sgn}\det(1-f'(x))$; the *Lefschetz number*
is $\Lambda(f)=\sum_k(-1)^k\operatorname{Tr}f^{*k}$, where
$f^{*k}\colon H^k(M;\mathbb R)\to H^k(M;\mathbb R)$ is the induced map on real
cohomology.

**Notes / provenance.** Definitions only (per the DESIGN-FUDW-DECOMP-v4.1 §4.1
register row: "pinned TeX 957–967, definitions only"): this shard carries the two
displayed definitions and NO theorem content — in particular it does not assert
the Lefschetz–Hopf identity $\sum_{x\in\operatorname{Fix}(f)}\operatorname{ind}(f,x)=\Lambda(f)$
(that is the separate result row `lem-topology-lefschetz-hopf`, to be `cited`
from Arkowitz–Brown), nor the index-sign theorem (`lem-topology-local-index-sign`,
Granas–Dugundji). The source's index formula is stated in the nondegenerate
($\det\ne0$) smooth case; the general topological index the theorem rows use is
the standard one in their own sources. See [[def-h-space-left-inversion]].
