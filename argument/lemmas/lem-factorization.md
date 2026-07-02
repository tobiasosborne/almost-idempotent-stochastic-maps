---
id: lem-factorization
kind: lemma
contract: Factorization bound: let P be an exact signed idempotent (square real matrix with P^2 = P and all row sums equal to 1), let delta(P) = max_i sum_j max(-P_ij, 0), let k = rank(P), and let U = (u_1, ..., u_k) be an actual-row basis of P (the rows p_{u_1}, ..., p_{u_k} of P form a basis of the row space of P) whose Gram volume satisfies Vol(U) >= (1/2) * Vol_max(P), where Vol_max(P) is the maximum Gram volume over all actual-row bases of P; define coordinates a_t(j) by p_j = sum_t a_t(j) p_{u_t}, and for each pivot index s in {1, ..., k} set beta_s(j) = P_{u_s j}, lambda_s(j) = 1 - a_s(j), mu_s(j) = sum_{t != s} max(-a_t(j), 0), sigma_s(j) = sum_{t != s} max(a_t(j), 0), E_s(j) = max(mu_s(j) - lambda_s(j), 0), Phi_s(U) = sum_j max(beta_s(j), 0) * E_s(j), and S*_s(U) = sum_j max(beta_s(j), 0) * (sigma_s(j) + 2 * max(-lambda_s(j), 0)); then for every pivot s, S*_s(U) <= 2 * Phi_s(U) + 6 * delta(P).
defs: def-signed-idempotent; def-negative-mass
deps: 
status: proved-mod-audit
af: seeded
provenance: docs/ingest (classical-portfolio; statement (F) and its audited proof at docs/ingest/report/kernel-conjecture-v2.tex lines ~272-293; chart vocabulary lines ~79-165)
owner: A
workspace: proofs/lem-factorization
---

The proved-mod-audit engine that composes with [[conj-ex]]: an (EX) bound `max_s Phi_s <= C0*delta`
turns (F) into the registry constant `C_sf = 2*C0 + 6` (8 at C0=1; 10 at the A2/A3-supported C0=2).
The inherited audit (w41 codex proof, w42 independent Opus audit) also records the constants `(2,6)`
as tight for this argument and class-wide, with no hidden `delta <= 1/4` dependence — the tightness
claim is NOT part of the contract above and is not being elevated.

**Proof shape (inherited, mod-audit):** the pointwise sign split
`sigma_s(j) + 2*max(-lambda_s(j),0) <= E_s(j) + 2*max(lambda_s(j),0)` ((P1) repaired domination),
the harmonic deficit identity `sum_j beta_s(j) lambda_s(j) = 0` ((DEF), from coordinate harmonicity
`sum_j beta_s(j) a_t(j) = delta_st`), the split `D+_s = V_s + D-_s` with
`D-_s = sum_j max(-beta_s(j),0)*lambda_s(j) <= 3*delta(P)` (Cramer box: the theta = 1/2 volume
hypothesis gives `|a_t(j)| <= 2`, hence `lambda_s(j) <= 3`; pivot-row negative mass `<= delta`),
and `V_s <= Phi_s/2` (on overshoot rows `lambda_s(j) < 0`, `E_s(j) >= 2*(-lambda_s(j))`).

**Elevation (2026-07-03, aism-kia):** contract narrowed from the inherited compound form (tightness
+ composition gloss moved to this body) to the single inequality, per the single-minimal-contract
discipline (bd memory; the obs-height-collapse run-1 lesson). Awaiting af run.

Finer vocabulary (def-actual-row-chart, def-phi-excess) still deferred; the contract is
self-contained.
