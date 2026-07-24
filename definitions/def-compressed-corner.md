---
id: def-compressed-corner
term: compressed corner
aliases: compression map; compressed product; compressed unit
kind: cited
status: locked
consensus: user-ratified 2026-07-24 (tobiasosborne, in-session sign-off: byte-match-to-source criterion for cited; delegated ratification for consensus/original)
source: kitaev-2405.02434
locus: approximate_algebras.tex:1054-1066,1077-1082
sha256: e7eb512a2ec2438d
---

**Byte-verbatim source text.**

```tex
To each pair of projections $(P,Q)$ in a $C^*$ algebra $\calB$, one assigns the vector space $\calS_{P,Q}=\{PXQ:\,X\in\calB\}$. In this section, we discuss an approximate version of this construction. Recall that a $\delta$-projection in an $\eps$-$C^*$ algebra $\calA$ is a Hermitian element $P$ such that $\|P^2-P\|\le\delta$. For each pair $(P,Q)$ of $\delta$-projections, there are two slightly different maps that could be called ``compressions'': $\La_P\Ra_Q\colon X\mapsto P(XQ)$ and $\Ra_Q\La_P\colon X\mapsto (PX)Q$. We will use their symmetric combination, $\frac{1}{2}(\La_P\Ra_Q+\Ra_Q\La_P)$. It is an $O(\delta+\eps)$-idempotent element of the algebra of operators acting on $\calA$, and therefore, can be approximated by an idempotent using Proposition~\ref{prop_P}. The \emph{compression map} thus defined,
\begin{equation}
\Co_{P,Q}\colon\calA\to\calA,\qquad
\Co_{P,Q}=\theta(\La_P\Ra_Q+\Ra_Q\La_P-1),
\end{equation}
satisfies the equations
\begin{equation}
\Co_{P,Q}^2=\Co_{P,Q},\qquad\:
\Co_{P,Q}(X)^\dag=\Co_{Q,P}(X^\dag)\quad\: (X\in\calA),
\end{equation}
and both $\|\La_P\Ra_Q-\Co_{P,Q}\|$ and $\|\Ra_Q\La_P-\Co_{P,Q}\|$ are bounded by $O(\delta+\eps)$. The image of this map, $\calS_{P,Q}=\Img\Co_{P,Q}=\Ker(1-\Co_{P,Q})$, is a closed linear subspace of $\calA$. There is a variant of this construction where only $\La_P$ or only $\Ra_Q$ is applied, and one writes $\Co_{P,1},\calS_{P,1}$ or $\Co_{1,Q},\calS_{1,Q}$, respectively. (This is the same as $\Co_{P,I}$, etc.\ if the unit is exact.)

When $P=Q$, the abbreviations $\Co_{P}$, $\calS_P$ are used.
```

```tex
For any triple $(P,Q,R)$ of $\delta$-projections, one defines the \emph{compressed product} between elements of the corresponding subspaces:
\begin{equation}\label{compr_prod}
(X,Y)\mapsto X\cdot Y\,\colon\,
\calS_{P,Q}\times\calS_{Q,R}\to \calS_{P,R},\qquad X\cdot Y=\Co_{P,R}(XY).
\end{equation}
It is close to the ambient product in $\calA$, namely, $\|X\cdot Y-XY\|\le O(\delta+\eps)\|X\|\ts\|Y\|$. If $P$ is a nonvanishing projection, the compressed product turns the Banach space $\calS_P$ (which is closed under the involution $X\mapsto X^\dag$) into an $O(\delta+\eps)$-$C^*$ algebra with unit $\wt{P}=\Co_{P}(P)$.\medskip
```

**Status.** Draft transcription; ratification is required before locking.

**Provenance.** Byte-verbatim from the pinned source at the recorded loci
and SHA256 prefix; provisioned by `DESIGN-FUDW-DECOMP-v3.md` §4.1 and admitted
only for the safe subset by `VERDICT-FUDW-DECOMP-V3.md` §D.
