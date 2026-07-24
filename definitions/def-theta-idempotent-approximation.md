---
id: def-theta-idempotent-approximation
term: theta idempotent-approximation map
aliases: theta map; functional-calculus idempotent approximation
kind: cited
status: draft
source: kitaev-2405.02434
locus: approximate_algebras.tex:505-528 (displays Taylor_simple, Taylor_simple_bound, abs_sgn, and the theta display inside Proposition prop_P — ONLY the definitional displays are cited; the Proposition's claims are NOT citable and must be re-proved)
sha256: e7eb512a2ec2438d
---

**Byte-verbatim source text.**

Power-series functional calculus (tex:505-510):
```tex
f(X)=a_0I+\sum_{n=1}^{\infty}a_n(X-x_0I)^n\quad\:
\text{if }\, \|X-x_0I\|<r,\\
\|f(X)-f(x_0I)\|\le \sum_{n=1}^{\infty}|a_n|\ts\|X-x_0I\|^n.
```

Absolute value and sign (tex:517-520):
```tex
|X|=(X^2)^{1/2},\qquad \sgn(X)=X(X^2)^{-1/2}\qquad\quad
\bigl(\|X^2-x_0^2I\|<x_0^2\bigr).
```

The theta map (tex:527-528, the definitional display of Proposition `prop_P`):
```tex
\wt{P}=\theta(2P-I),\qquad
\text{where}\quad \theta(X)=\frac{1}{2}\bigl(I+\sgn(X)\bigr).
```

**Scope note.** This is the map `theta` referenced by the compression-map
display `Co_{P,Q}=\theta(\La_P\Ra_Q+\Ra_Q\La_P-1)` in
[[def-compressed-corner]] (tex:1057). The neighbouring Proposition's
conclusions (idempotence of `wtP`, commutation, distance bound) are claims,
not definitions — they enter the registry only as re-proved results.

**Ratification.** Draft pending recorded sign-off; expected to lock under the
user's recorded byte-match criterion (2026-07-24: "if they match the source
then they are valid").
