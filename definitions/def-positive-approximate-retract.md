---
id: def-positive-approximate-retract
term: positive approximate retract
aliases: positive retract pair; PRH datum
kind: original
status: draft
source: internal
locus: project formulation transcribed from docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md §§1,4
sha256: -
consensus: W74F transcription draft; user ratification pending
---

**Statement.** A *positive approximate retract* between finite commutative
$C^*$-algebras is a pair of positive unital maps
\[
A:\ell^\infty(k)\longrightarrow\ell^\infty(n),
\qquad
M:\ell^\infty(n)\longrightarrow\ell^\infty(k)
\]
for which $MA$ is close to $I_k$ in the
$\ell^\infty\!\to\!\ell^\infty$ operator norm.  Its retract defect is
\[
\varepsilon_{\mathrm{ret}}:=\lVert MA-I_k\rVert_{\infty\to\infty}.
\]
Equivalently, the matrices of $A$ and $M$ have probability-vector rows.

**Scope.** This project term packages the datum hardened by `lem-prh`; it
does not assert that such a pair exists for any particular almost-idempotent
map.

**Provenance.** Project formulation extracted from the W74F-A PRH artifact.
This is an `original` definition at `status: draft`; it is not ratified.
