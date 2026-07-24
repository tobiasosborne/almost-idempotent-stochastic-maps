---
id: def-delta-projection
term: δ-projection and nonvanishing alternative
aliases: delta-projection; nonvanishing delta-projection
kind: cited
status: locked
consensus: user-ratified 2026-07-24 (tobiasosborne, in-session sign-off: byte-match-to-source criterion for cited; delegated ratification for consensus/original)
source: kitaev-2405.02434
locus: approximate_algebras.tex:917-920,926-929
sha256: e7eb512a2ec2438d
---

**Byte-verbatim source text.**

```tex
A \emph{projection} in an $\eps$-$C^*$ algebra $\calA$ is a Hermitian element $P$ such that $P^2=P$. Such elements are generally hard to come by, see Remark~\ref{rem_X2}, so will content ourselves with \emph{$\delta$-projections} for sufficiently small $\delta$. They are defined by the conditions
\begin{equation}\label{delta_P}
P^\dag=P,\qquad \|P^2-P\|\le\delta.
\end{equation}
```

```tex
\begin{equation}\label{P_alternatives}
\|P\|\le O(\delta)\quad \text{or}\quad \bigl|\|P\|-1\bigr|\le O(\delta+\eps).
\end{equation}
A $\delta$-projection is called \emph{nonvanishing} if the second alternative holds. If $P$ is a $\delta$-projection, then $I-P$ is a $\delta'$-projection, where $\delta'=\delta$ if $\calA$ has exact unit and $\delta'=\delta+O(\eps)$ in general. A $\delta$-projection $P$ is called \emph{nontrivial} if both $P$ and $I-P$ are nonvanishing.
```

**Status.** Draft transcription; ratification is required before locking.

**Provenance.** Byte-verbatim from the pinned source at the recorded loci
and SHA256 prefix; provisioned by `DESIGN-FUDW-DECOMP-v3.md` §4.1 and admitted
only for the safe subset by `VERDICT-FUDW-DECOMP-V3.md` §D.
