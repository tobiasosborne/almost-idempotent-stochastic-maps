---
id: lem-simplex-visibility
kind: lemma
contract: Simplex visibility: for an exact signed idempotent P with delta(P) <= 1/4 whose row polytope conv{p_i} is a simplex whose vertices are row vertices, every geometrically distinct row vertex is (4*sqrt(delta), sqrt(delta)/4)-exposed; in particular W(P) is nonempty.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: 
status: proved
af: none
provenance: W30 wave (docs/waves/2026-07-06-W30-w-nonemptiness.md): fresh-codex prover (worker T) + SEPARATE fresh-codex hostile verifier (VT, VALID — confirmed the ambient affine extension of barycentric coordinates is harmless since admissibility tests row values only; duplicates handled; exact rank-2 and delta=0 fixtures); first-principles, no imports
owner: A
workspace: proofs/lem-simplex-visibility
---

**Role (the first W-nonemptiness brick, Kernel(i)).** The visible set cannot be empty when the
row polytope is a simplex on row vertices: the barycentric exposer h = 1 − λ_v is admissible
and every ρ-far row pays margin ≥ ρ/D = 4τ/(2+4δ) ≥ κ at δ ≤ 1/4. Feeds
[[cor-rank-two-visible]]; the general (non-simplex) case is the named OPEN production theorem
(sketch v7 unscoped list; the W30-U obstruction "hiddenness needs visible anchors" is the
candidate mechanism).

**Proof shape (worker T, T1; VT).** For a simplex vertex p_v write any row as
p_j = (1−t)p_v + t·y_j with y_j in the opposite face and t = h(p_j); the opposite face is a
convex hull of row vertices and row-pair distances are ≤ D = 2+4δ (row norms ≤ 1+2δ), so
‖p_j − p_v‖₁ ≤ t·D and every ρ-far row has h ≥ ρ/D ≥ κ. Duplicates: coincident rows share
barycentric values; at δ > 0 they are not ρ-far, at δ = 0 the required margin is 0.

**Honest limits.** The simplex hypothesis is genuinely restrictive (the banked rank-5 W19
matrix has 6 vertices at affine rank 4 — not a simplex — though its W is nonempty anyway, VT
fixture). Says nothing about non-simplex polytopes — that is exactly the remaining gap.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous; af-elevation candidate
(deps: none).
