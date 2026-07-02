---
id: lem-residual-lower
kind: lemma
contract: Convex outsourcing: let C be the convex hull of finitely many points of R^n, and suppose p = sum_{j=1}^m c_j p_j + (1 - s) q with points p_j, q in R^n, coefficients c_j >= 0, s = sum_{j=1}^m c_j < 1, and dist_1(p_j, C) <= dist_1(p, C) for every j; then dist_1(p, C) <= dist_1(q, C).
defs: 
deps: 
status: stated
af: none
provenance: factored out of proofs/conj-halo-collapse elevation run 1 (node 1.4.2, all four children codex-validated there); stated frame-free (pure l1 convex geometry, no idempotent structure)
owner: A
workspace: proofs/lem-residual-lower
---

**Purpose (factoring, aism-q7e).** The lower residual-distance bound of the halo-collapse argument,
stated as a standalone frame-free convexity fact: if a point `p` is written as a sub-convex
combination of points no farther from `C` than `p` itself plus a residual `(1-s) q`, then the residual
point `q` must be at least as far from `C` as `p`. Proof shape (run-1 nodes 1.4.2.1–1.4.2.4): project
each `p_j` and `q` onto `C`, form the matching convex combination `c` in `C`, and apply the triangle
inequality to `dist_1(p, C) <= ||p - c||_1`; subtract `s * dist_1(p, C)`.

Only BSc-level notions are used (`l1` distance to a set, convex hull — common knowledge per L2), so
`defs` is empty by design.

**Role:** dep of [[conj-halo-collapse]] — applied with `p = p_v` (a hidden top vertex, so
`dist_1(p_j, C_W) <= H = dist_1(p_v, C_W)` for all rows), the `c_j` the genuine-pot masses `a_j^+`
(`j` with `d_j > tau/4`), and `s = sigma_g < 1`.
