---
id: lem-topology-hopf-structure
kind: lemma
contract: Hopf structure theorem in the form consumed by Stage 1: a finite-dimensional connected graded-commutative bialgebra over a characteristic-zero field is an exterior algebra on odd-degree homogeneous generators.
defs: def-h-space-left-inversion
deps:
status: stated
af: none
provenance: hatcher-algebraic-topology AT.txt:17798-17800 (Theorem 3C.4 — the consumed row is a finite-dimensional COROLLARY of the printed exterior-tensor-polynomial statement, not its verbatim form; Hopf-algebra definition/connectedness at txt:17654-17677; loci pinned 2026-07-26); DESIGN-FUDW-DECOMP-v4.1.md §2.3
owner: A
workspace: proofs/lem-topology-hopf-structure
---

**Status.** Local source-result transcription at `stated`; to be af-elevated
as a small tree with the byte-matched external. Not `cited`, not
af-validated, not L0-rigorous yet.

**Source locus (pinned).** Hatcher, Theorem 3C.4 (txt:17798-17800): "If A is
a commutative, associative Hopf algebra over a field F of characteristic 0,
and A_n is finite-dimensional over F for each n, then A is isomorphic as an
algebra to the tensor product of an exterior algebra on odd-dimensional
generators and a polynomial algebra on even-dimensional generators." Hatcher's
"Hopf algebra" is connected by definition and does NOT require
coassociativity/counit/antipode (txt:17654-17677) — the row's bialgebra
hypotheses are STRONGER than the source needs (safe direction).

**Derivation to close at elevation (one step).** Under the row's TOTAL
finite-dimensionality (strictly stronger than the source's graded-piecewise
hypothesis), any nontrivial polynomial factor would be infinite-dimensional;
hence no even polynomial generators occur and A is exterior on odd-degree
generators. The row is a corollary, not the verbatim theorem (honest scope).

**Consumers.** Stage-1 trace rows (`lem-stage1-left-inversion-trace` chain,
per §3.3).
