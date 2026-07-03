---
id: conj-degenerate-payment
kind: lemma
contract: Degenerate payment: let P be an exact signed idempotent (square real matrix with P^2 = P and all row sums equal to 1) with 0 < delta(P) <= 1/4 where delta(P) = max_i sum_j max(-P_ij, 0), let U = (u_1, ..., u_k) be an actual-row basis of P (k = rank(P)) minimizing Phi(U) = max_s Phi_s(U) over all actual-row bases with Gram volume Vol(U) >= (1/2) * Vol_max(P), with coordinates a_t(j) defined by p_j = sum_t a_t(j) p_{u_t}, beta_s(j) = P_{u_s j}, lambda_s(j) = 1 - a_s(j), mu_s(j) = sum_{t != s} max(-a_t(j), 0), E_s(j) = max(mu_s(j) - lambda_s(j), 0), and Phi_s(U) = sum_j max(beta_s(j), 0) * E_s(j); fix a pivot s and let D_s be the set of rows j such that beta_s(j) > 0, E_s(j) > 0, and every block swap that keeps u_s in the chart and brings row j into one or two transverse pivot positions has Schur volume factor |det C| <= 1/2; then sum_{j in D_s} beta_s(j) * E_s(j) <= 2 * delta(P).
defs: def-signed-idempotent; def-negative-mass
deps: 
status: conjecture
af: none
provenance: docs/waves/2026-07-03-A8-schur-degeneracy.md (arm A wave 8, codex; Candidate 3 of the GAP-B split — the payment horn); exact zoo test: passes all A2-A7 instances with worst value (5/3)*delta (table in the wave artifact §T3)
owner: A
workspace: proofs/conj-degenerate-payment
---

**The payment horn of GAP B** (the [[conj-ex]] argmin charge). A8 split GAP B into (i) this
pivot-local weighted near-degenerate payment and (ii) the legal-collateral horn (rows with a
volume-permitted covering swap must be handled through the MAX-comparison `Phi(U*) <= Phi(V)` without
the `3*delta` collateral jump of the transverse `a=1/4` witness breaking the constant). Together the
two horns would give `max_s Phi_s(U*) <= C*delta` at a theta-1/2 Phi-argmin, i.e. (EX), which
composes through the af-validated [[lem-factorization]] to `C_sf = 2*C0 + 6`.

**Why this shape (A8 §T3/T4):** pointwise variants are dead exactly — `E_s(j) <= 2*delta` fails at
transverse `a=1/8` (`E/delta = 17/8`, max covering det `1/4`) and at the under-cap balanced staircase
(`E/delta = 121/48`, max det `1/8`); the determinant-discounted cap `(1-m_j)*E_s(j) <= 2*delta` fails
at the same staircase row (`847/384 > 2`). The surviving statement is the WEIGHTED pivot total over
the degenerate set only: max-based (no sum over pivots — the A6 repeated-anchor witness kills that),
not class-count-shaped (no per-row counting; the beta-weighted fan average is what stays bounded as
the number of carrying rows grows), and realizability-dependent (the zoo payments all use the row
negative budget and the harmonic beta identities; A4's two-atom witness kills coefficient-only
readings).

**Evidence status:** exact pass on the full A2-A7 zoo (worst `5/3`); provable inline on the reduced
fan templates (where `Phi_s/delta` is the fan average of `neg_l1(w - w0)`); NO general proof — the
balanced-staircase row shows the general argument must combine the Schur slab with the row-negative
budget and the harmonic identities, not determinant geometry alone. Boundary convention: `|det C| =
1/2` is assigned to the payment horn (A8: with the boundary in the legal horn, the composed zoo
constant degrades via the `a=1/4` collateral).

**Do NOT af-elevate yet** (genuine-gap abort predicted); wave 9 first: general proof attempt +
legal-collateral horn composition.
