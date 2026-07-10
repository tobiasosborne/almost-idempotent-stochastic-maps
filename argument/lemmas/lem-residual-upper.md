---
id: lem-residual-upper
kind: lemma
contract: Residual distance bound: let C be the convex hull of finitely many points of R^n, let b_1..b_M, c_1..c_N >= 0 with m = sum_j b_j - sum_k c_k > 0, let p_j, r_k be points of R^n with q = (sum_j b_j p_j - sum_k c_k r_k) / m, and let D_k >= 0 satisfy ||x - r_k||_1 <= D_k for all x in C and each k; then m * dist_1(q, C) <= sum_j b_j * dist_1(p_j, C) + sum_k c_k * D_k.
defs: 
deps: 
status: proved
af: validated
provenance: factored out of proofs/conj-halo-collapse elevation run 1 (node 1.4.3 and its algebra children 1.4.3.1–1.4.3.5, several codex-validated there); stated frame-free (pure l1 convex geometry, no idempotent structure)
owner: A
workspace: proofs/lem-residual-upper
---

**Purpose (factoring, aism-q7e).** The upper residual-distance bound of the halo-collapse argument,
stated as a standalone frame-free convexity fact: a signed combination `q` with positive part near `C`
and negative part uniformly `D_k`-close to `C` is itself close to `C`, at the pot-weighted price.
Proof shape (run-1 nodes 1.4.3.1–1.4.3.5): project each `p_j` onto `C` (projections `beta_j`,
`||p_j - beta_j||_1 = dist_1(p_j, C)`); note `m_B := sum_j b_j >= m > 0`, so
`b := (1/m_B) sum_j b_j beta_j` lies in `C`; the algebra identity
`m (q - b) = sum_j b_j (p_j - beta_j) + sum_k c_k (b - r_k)` plus the triangle inequality and
`||b - r_k||_1 <= D_k` gives the bound via `m * dist_1(q, C) <= ||m (q - b)||_1`.

Only BSc-level notions are used (`l1` distance to a set, convex hull — common knowledge per L2), so
`defs` is empty by design.

**Role:** dep of [[lem-halo-collapse]] — applied with the `b_j` the halo-pot masses (`a_j^+`, `j` in
`B`: `0 <= d_j <= tau/4`, so `dist_1(p_j, C_W) <= tau/4` prices the first sum at
`(sigma - sigma_g) * tau/4`), the `r_k` the negative-pot rows (`c_k = a_k^-`, `D_k = 2 + 4*delta` from
the row-geometry clause of def-signed-idempotent), and `m = 1 - sigma_g` via [[lem-mass-split]].

**af-VALIDATED IN-REPO 2026-07-02** (run 1 + verify resumes, clean): 49 validated live nodes (52
total incl. 3 archived), root `validated`, taint 52/52 clean; fresh codex prover/verifiers per node,
Claude orchestrated only (§6). Ledger: `proofs/lem-residual-upper/ledger/`; export:
`proofs/lem-residual-upper/export.md`. Status flip is the mechanical reflection of the codex ledger.
Tree size (49>12) trips the tracked REFACTOR warn (aism-6ec) — growth was af dependency-scoping
bridge nodes, not mathematical content.
