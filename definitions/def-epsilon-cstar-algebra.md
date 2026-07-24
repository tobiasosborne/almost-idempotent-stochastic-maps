---
id: def-epsilon-cstar-algebra
term: ε-C*-algebra
aliases: epsilon-C*-algebra; approximate C*-algebra
kind: cited
status: locked
consensus: user-ratified 2026-07-24 (tobiasosborne, in-session sign-off: byte-match-to-source criterion for cited; delegated ratification for consensus/original)
source: kitaev-2405.02434
locus: approximate_algebras.tex:407-440
sha256: e7eb512a2ec2438d
---

**Byte-verbatim source text.**

```tex
\begin{Definition}
An \emph{$\eps$-Banach algebra} is a Banach space $\calA$ endowed with a bilinear multiplication map $\calA\times \calA\to \calA$ such that
\begin{alignat}{2}
\label{ax_prodnorm}
\|XY\| &\le (1+\eps)\ts\|X\|\ts\|Y\|\qquad &&(X,Y\in \calA),\\[2pt]
\label{ax_assoc}
\|(XY)Z-X(YZ)\| &\le \eps\ts\|X\|\ts\|Y\|\ts\|Z\|\qquad &&(X,Y,Z\in \calA).
\end{alignat}
Such an algebra is called \emph{$\eps'$-commutative} if
\begin{equation}
\label{ax_comm}
\|XY-YX\|\le \eps'\ts\|X\|\ts\|Y\|\qquad (X,Y\in \calA).
\end{equation}
A \emph{$*\eps$-Banach algebra} is a complex $\eps$-Banach algebra with a conjugate linear involution $X\mapsto X^\dag$ satisfying the equations
\begin{equation}
\label{ax_*}
\|X^\dag\|=\|X\|,\qquad (XY)^\dag=Y^\dag X^\dag\qquad (X,Y\in \calA).
\end{equation}
An \emph{$\eps$-$C^*$ algebra} is one with this additional property:
\begin{equation}
\label{ax_C*}
\|X^{\dag}X\|\ge (1-\eps)\ts\|X\|^{2}\qquad (X\in \calA).
\end{equation}
(A bound from the other side, $\|X^{\dag}X\|\le (1+\eps)\ts\|X\|^{2}$, follows from \eqref{ax_prodnorm} and \eqref{ax_*}.) We assume that all algebras are unital. The unit element $I\in\calA$ should satisfy the approximate or exact conditions
\begin{alignat}{4}
\label{ax_eps_unit}
\|XI&-X\|\le\eps\ts\|X\|,\qquad &\|IX&-X\|\le\eps\ts\|X\|,\qquad
&\bigl|\|I\|&-1\bigr|\le\eps\qquad &&\text{(by default)},\quad \text{or}\\[2pt]
\label{ax_exact_unit}
XI&=X,\qquad &IX&=X,\qquad
&\|I\|&=1\qquad &&\text{(if specified)}.
\end{alignat}
If the involution is defined, one also requires that $I^\dag=I$.
\end{Definition}
```

**Status.** Draft transcription; ratification is required before locking.

**Provenance.** Byte-verbatim from the pinned source at the recorded locus
and SHA256 prefix; provisioned by `DESIGN-FUDW-DECOMP-v3.md` §4.1 and admitted
only for the safe subset by `VERDICT-FUDW-DECOMP-V3.md` §D.
