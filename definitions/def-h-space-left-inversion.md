---
id: def-h-space-left-inversion
term: H-space and left inversion
aliases: H-space; associative H-space; inversion map; left inversion map
kind: cited
status: locked
consensus: byte-match lock per definitions/README.md (cited criterion); provisioned by DESIGN-FUDW-DECOMP-v4.1.md §4.1 (kind "cited / lock after byte-match")
source: kitaev-2405.02434
locus: approximate_algebras.tex:895-912
sha256: e7eb512a2ec2438d
---

**Byte-verbatim source text.**

```tex
By definition, an \emph{H-space} is a topological space $M$ with a basepoint $e$ and a continuous multiplication map $\mu\colon M\to M$ such that $\mu(e,e)=e$ and
\begin{equation}\label{H-unit}
\bigl(x\mapsto \mu(x,e)\bigr)
\,\sim\,\bigl(x\mapsto x\bigr)
\,\sim\,\bigl(x\mapsto \mu(e,x)\bigr),
\end{equation}
where ``$f\sim g$'' means that $f$ and $g$ are homotopic through basepoint-preserving maps. [...] An H-space $M$ is called \emph{associative} if
\begin{equation}
\bigl((x,y,z)\mapsto \mu(\mu(x,y),z)\bigr)
\,\sim\,\bigl((x,y,z)\mapsto \mu(x,\mu(y,z))\bigr).
\end{equation}
[...] An \emph{inversion map} is a continuous basepoint-preserving map $\sigma\colon M\to M$ such that
\begin{equation}\label{homo_inverse}
\bigl(x\mapsto \mu(\sigma(x),x)\bigr)
\,\sim\,\bigl(x\mapsto e\bigr)
\,\sim\,\bigl(x\mapsto \mu(x,\sigma(x))\bigr).
\end{equation}
[...] When only the existence of that homotopy is required, $\sigma$ is called a \emph{left inversion map}.
```

**Statement (harmonised).** An *H-space* is a topological space $M$ with basepoint
$e$ and a continuous multiplication $\mu\colon M\times M\to M$ with $\mu(e,e)=e$
such that $x\mapsto\mu(x,e)$ and $x\mapsto\mu(e,x)$ are each basepoint-preserving
homotopic to the identity. It is *associative* if the two triple-product maps are
homotopic. An *inversion map* is a continuous basepoint-preserving
$\sigma\colon M\to M$ with both $x\mapsto\mu(\sigma(x),x)$ and
$x\mapsto\mu(x,\sigma(x))$ homotopic to the constant map $e$; when only the first
homotopy is required, $\sigma$ is a *left inversion map*.

**Notes / provenance.** Definition only (per the DESIGN-FUDW-DECOMP-v4.1 §4.1
register row: "pinned TeX 895–912, definition only") — no claim about $\mathcal U$
or any Stage-1 object is carried by this shard. Source typo note: the source
writes $\mu\colon M\to M$ for the multiplication map's type where
$\mu\colon M\times M\to M$ is meant (its uses $\mu(x,y)$ are two-argument
throughout); the harmonised statement records the corrected type. Elisions
`[...]` in the verbatim block skip source sentences about the specific space
$\mathcal U$ (claims, not definition content). Used by the Stage-1 topology rows
`lem-topology-hopf-structure` and (via fixed-point data) the Lefschetz rows; see
[[def-lefschetz-fixed-point-data]].
