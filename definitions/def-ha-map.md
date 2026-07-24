---
id: def-ha-map
term: Ha-map
aliases: Ha map; Kitaev Ha-map
kind: cited
status: locked
source: kitaev-2405.02434
locus: approximate_algebras.tex:1146-1149
sha256: e7eb512a2ec2438d
---

**Byte-verbatim source text.**

```tex
Let $Q$ be a one-dimensional $\delta$-projection in an $\eps$-$C^*$ algebra $\calA$. For any $\delta$-projections $P,R\in\calA$, we define a map $\Ha^{Q}_{P,R}\colon\calS_{P,R}\to\Bo(\calS_{R,Q},\calS_{P,Q})$. (Here $\Bo(\calS_{R,Q},\calS_{P,Q})$ is the space of bounded linear maps from $\calS_{R,Q}$ to $\calS_{P,Q}$ with the norm induced by the Euclidean norm $\|X\|_\Euc=\sqrt{\braket{X}{X}}$. Due to inequality \eqref{1dQ_ip_norm}, the latter is equal to $\|X\|$ up to a $1\pm O(\eps+\delta)$ factor.) For each $Z\in\calS_{P,R}$ and $X\in\calS_{R,Q}$, the element $\Ha^{Q}_{P,R}(Z)(X)\in\calS_{P,Q}$ is defined by the condition
\begin{equation}\label{Ha_def}
(Y^\dag\cdot Z)\cdot X+Y^\dag\cdot(Z\cdot X)
=2\,\bbraket{Y}{\Ha^{Q}_{P,R}(Z)(X)}\,\wt{Q}\quad \text{for all }\,Y\in\calS_{P,Q}.
\end{equation}
```

**Notation.** Registry contracts use `Ha` for the source macro `\(\Ha\)`.

**Provenance.** Byte-verbatim from the pinned source at the recorded locus and
SHA256 prefix.  User-ratified and locked 2026-07-24 (tobiasosborne, in-session sign-off).
