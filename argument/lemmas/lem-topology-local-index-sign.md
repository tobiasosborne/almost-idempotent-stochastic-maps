---
id: lem-topology-local-index-sign
kind: lemma
contract: Nondegenerate local fixed-point index: if x is an isolated fixed point of a C^1 self-map f with det(I-Df_x) != 0, then its local fixed-point index is sgn det(I-Df_x).
defs: def-lefschetz-fixed-point-data
deps:
status: stated
af: seeded
provenance: granas-dugundji granas-dugundji-fixed-point-theory.txt:14700-14708 (Thm (8.5), Leray-Schauder formula, Ch. IV §12.8, pp.328-329) + granas-dugundji-fixed-point-theory.txt:12089-12094 (Thm (8.4), Brouwer degree sgn det, Ch. IV §10.8, p.267) — two-theorem composition, loci pinned 2026-07-26; DESIGN-FUDW-DECOMP-v4.1.md §2.3
owner: A
workspace: proofs/lem-topology-local-index-sign
---

**Status.** Local source-result transcription at `stated`; to be af-elevated
with the two byte-matched externals. Not `cited`, not af-validated, not
L0-rigorous yet.

**Source loci (pinned).** Granas–Dugundji, *Fixed Point Theory* (2003):
(i) Theorem (8.4) (Ch. IV §10.8, p. 267, txt:12089-12094): for f:U->R^n
differentiable with a regular zero a (f'(a) nonsingular), the local Brouwer
degree is d(f,V) = sgn det f'(a); (ii) Theorem (8.5) (Leray–Schauder formula,
Ch. IV §12.8, pp. 328–329, txt:14700-14708): if F is differentiable at a fixed
point x_0 and 1 is not an eigenvalue of F'(x_0), then x_0 is an ISOLATED fixed
point and J(F,x_0) = J(F'(x_0),0). The book defines the fixed-point index via
the degree of id−f (txt:13756-13760, 14589-14594).

**Derivation to close at elevation (small).** In local coordinates set
g = id − f; det(I−Df_x) ≠ 0 says x is a regular zero of g, so (8.4)(b) gives
sgn det(I−Df_x); (8.5) supplies isolation and reduction to the linearization.
NOTE (honest scope): the literal one-line finite-dimensional statements in the
source at txt:14613-14632 are labelled EXAMPLES, not theorems — the citation
rests only on the two genuine theorems above.

**Consumers.** `lem-stage1-extra-fixed-class` (per §3.3).
