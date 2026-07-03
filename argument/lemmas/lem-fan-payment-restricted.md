---
id: lem-fan-payment-restricted
kind: lemma
contract: D-restricted zero-sum fan payment: let (w_1, p_1), ..., (w_m, p_m) be a finite family with vectors w_i in R^d and weights p_i > 0 satisfying sum_i p_i = 1, such that every w_i has coordinate sum zero and the weighted barycenter is zero (sum_i p_i w_i = 0); write n(w) = sum_l max(-w(l), 0); let w_* be a minimizer of v -> sum_i p_i n(w_i - v) over {w_1, ..., w_m} and let A = { i : n(w_i - w_*) > 0 }; then sum_{i in A} p_i n(w_i - w_*) <= (2 + sqrt(2)) * sum_{i in A} p_i n(w_i).
defs: 
deps: lem-zerosum-triangle; lem-negpart-subadditive
status: proved
af: validated
provenance: docs/waves/2026-07-03-A11-drestricted-fan.md (arm A wave 11, codex; T2 complete inline proof — horn (i): zero-sum triangle + barycenter subadditivity give N <= D/q where q is the duplicate-pivot-cluster mass; horn (ii): averaging the minimizer comparison over nonpivot support points gives N <= 2(1-q)/(1-2q) * D for q < 1/2; the bounds cross at q0 = 1 - 1/sqrt(2) with common value 2 + sqrt(2))
owner: A
workspace: proofs/lem-fan-payment-restricted
---

**The D-restricted refinement of the af-validated [[lem-fan-payment]]** — the denominator keeps only
the rows with positive distance to the selected pivot (the fan shadow of the WOP/degenerate-set
restriction behind [[conj-degenerate-payment]]).

**The constant is SHARP and 2 is exactly refuted (A11 T1, T0 certificates):** a d=3 triple attains
ratio `9/4`; a d=4 paired direct sum attains `5/2`; the direct-sum certificate sequence (k blocks,
pivot mass q -> 1 - 1/sqrt(2) from above) attains `2 + sqrt(2)` in the limit, matching the proof's
crossing value. Do not quote constant 2 for the D-restricted variant.

**af-VALIDATED IN-REPO 2026-07-03** (run 1 clean, 10 rounds): 27-node adversarial tree, root
`validated`, taint 27/27 clean; imports the af-validated deps [[lem-zerosum-triangle]] and
[[lem-negpart-subadditive]] as externals; fresh codex provers/verifiers per node, Claude
orchestrated only (§6). Export: `proofs/lem-fan-payment-restricted/export.md`. Status flip is the
mechanical reflection of the codex ledger.

**Proof shape (A11):** with q = duplicate-pivot mass, r = 1 - q: (i)
`N <= D + r*n(w_*)` ([[lem-zerosum-triangle]]) and `D >= q*n(w_*)` (barycenter +
[[lem-negpart-subadditive]] + n(-v) = n(v) for zero-sum v) give `N <= D/q`; (ii) `N = F(w_*) <=
F(w_j)` averaged over j in A with the triangle bound gives `N <= 2(1-q)/(1-2q)*D` when `q < 1/2`;
min of the two bounds is maximized at the crossing `q0 = 1 - 1/sqrt(2)`, value `2 + sqrt(2)`.

**Role:** with this, the discrete inequality behind the payment horn is closed at constant
`2 + sqrt(2)`; the remaining obstruction to [[conj-degenerate-payment]] is the LIFT: showing the
rows of an exact signed idempotent at a theta-1/2 Phi-argmin reduce to this fan model with the
Schur-degenerate set as A (A11 T3).
