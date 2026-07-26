---
id: lem-topology-local-index-sign
kind: lemma
contract: Nondegenerate local fixed-point index: if x is an isolated fixed point of a smooth self-map f of a compact orientable manifold with det(I-Df_x) != 0, then its local fixed-point index is sgn det(I-Df_x).
defs: def-lefschetz-fixed-point-data
deps:
status: proved
af: validated
provenance: granas-dugundji granas-dugundji-fixed-point-theory.txt:14700-14708 (Thm (8.5), Leray-Schauder formula, Ch. IV §12.8, pp.328-329) + granas-dugundji-fixed-point-theory.txt:12089-12094 (Thm (8.4), Brouwer degree sgn det, Ch. IV §10.8, p.267) — two-theorem composition, loci pinned 2026-07-26; DESIGN-FUDW-DECOMP-v4.1.md §2.3
owner: A
workspace: proofs/lem-topology-local-index-sign
---

**SCOPE NARROWING (user-ratified in-session, 2026-07-26).** The original
transcription quantified over an unqualified C^1 self-map; the af verifier
(node 1.5 challenge) correctly refused the closure because
`def-lefschetz-fixed-point-data` defines the local index only for smooth
self-maps of compact orientable manifolds. The contract is narrowed to that
scope (option (a)); the Granas-Dugundji two-theorem composition covers it.
CONSUMER OBLIGATION: `lem-stage1-extra-fixed-class` must supply smoothness,
compactness, and orientability at its application site (same pattern as the
Lefschetz-Hopf maximal-simplex obligation).

**Status.** af-VALIDATED in-repo (2026-07-26, session 28): 23-node tree under
the user-ratified narrowed contract (smooth self-map of a compact orientable
manifold — root amended in-place, 21 previously validated nodes retained),
taint clean 23/23. Export at `proofs/lem-topology-local-index-sign/export.md`.

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
