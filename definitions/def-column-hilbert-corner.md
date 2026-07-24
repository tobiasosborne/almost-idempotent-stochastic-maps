---
id: def-column-hilbert-corner
term: level-one and amplified column-Hilbert corner
aliases: column-Hilbert corner; amplified column space
kind: cited
status: draft
source: kitaev-2405.02434
locus: approximate_algebras.tex:1123-1128,1546-1550
sha256: e7eb512a2ec2438d
---

**Byte-verbatim source text.**

```tex
\begin{Lemma}\label{lem_PQ_Hilb}
Let $P$ and $Q$ be $\delta$-projections in an $\eps$-$C^*$ algebra. If $Q$ is one-dimensional, then $\calS_{P,Q}$ is a Hilbert space with the inner product $\braket{\cdot}{\cdot}$ defined by the equation
\begin{equation}\label{1dQ_ip}
Y^\dag\cdot X=\braket{Y}{X}\,\wt{Q}\qquad (X,Y\in\calS_{P,Q}),
\end{equation}
where $Y^\dag\cdot X=\Co_{Q}(Y^{\dag}X)$ and $\wt{Q}=\Co_Q(Q)$.
```

```tex
\noindent\textbf{One-dimensional projections and the corresponding Hilbert spaces.} Lemma~\ref{lem_PQ_Hilb} says that if $P,Q\in\calA$ are $\delta$-projections and $Q$ is one-dimensional, then the space $\calS_{P,Q}$ is equipped with the Hermitian inner product given by \eqref{1dQ_ip}. The extended version of this space, $\CC^n\otimes\calS_{P,Q}=\Ma{n,1}\otimes\calS_{P,Q}$, satisfies essentially the same equation:
\begin{equation}\label{1dQ_ip_ext}
Y^\dag\cdot X=\braket{Y}{X}\,\wt{Q}\qquad (X,Y\in\Ma{n,1}\otimes\calS_{P,Q}),
\end{equation}
where $\braket{Y}{X}=\sum_{l}\braket{[Y]_{l1}}{[X]_{l1}}$.
```

**Status.** Draft transcription; ratification is required before locking. The
known false unsquared display at source lines 1551-1555 is deliberately not
part of this definition.

**Provenance.** Byte-verbatim from the pinned source at the recorded loci
and SHA256 prefix; the exclusion is required by `DESIGN-FUDW-DECOMP-v3.md`
§4.1 and is consistent with `VERDICT-W74F-H-STAGE1.md`.
