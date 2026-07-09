---
id: lem-positive-exposedness-margin
kind: lemma
contract: Positive exposedness margin: for an exact signed idempotent P with rho = 4*tau > 0 (i.e. delta(P) > 0) and a geometrically distinct row vertex v with nonempty far set F_v = {j : ||p_j - p_v||_1 >= rho}: t*(v) > 0; in particular every HIDDEN geometrically distinct row vertex with F_v nonempty has 0 < t*(v) < kappa (hiddenness forces delta(P) > 0, hence rho > 0, and no row vertex is hidden at delta = 0).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: 
status: proved
af: none
provenance: W54 wave (docs/waves/2026-07-09-W54-huddle-charge-decomposition.md): R4 shard auditor's positive-margin proof + fresh hostile codex verifier V-R4 (VALID-WITH-CORRECTIONS; corrections applied — the rho > 0 qualifier is in the hypotheses, no LP-attainment clause is cited, the min over other distinct row points is taken only after nonemptiness is established)
owner: A
---

**Statement mechanics (V-R4-checked).** v a row vertex means p_v lies outside the compact
convex hull of the OTHER geometrically distinct row points ([[def-exposed]]); F_v nonempty
and rho > 0 guarantee that set is nonempty. Strict finite-dimensional separation gives an
affine a with a(p_v) = 0 and a > 0 on every other distinct row point; with M = max_j
a(p_j) > 0 the normalization h = a/M is an admissible exposer, and finiteness gives
min over the other distinct row points m = min a(p_j) > 0, so every far row (not a clone
of v since rho > 0) has h(p_f) >= m/M > 0, hence t*(v) >= m/M > 0. Dimension-free;
clone-invariant (clones inherit a-values).

**Role (the t* = 0 boundary is vacuous).** Discharges the W54 assembly pinhole AG-1: the
exposedness LP at a hidden geometrically distinct vertex never sits at t* = 0, so
[[lem-zero-face-localization]]'s far-constraint mechanism (far rows have h* >= t*) always
has a positive threshold. R4's boundary analysis (V-R4-confirmed): WITHOUT the vertex
hypothesis, t* = 0 with F nonempty would make localization false (h = 0 optimal, far
zero-face rows) — this lemma is exactly what excludes that case, and should be read as
the missing first step of the localization proof note.

**Rigour tier.** L5 (reviewer != author: fresh hostile codex V-R4). NOT af-validated.
