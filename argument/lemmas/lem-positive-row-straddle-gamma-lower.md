---
id: lem-positive-row-straddle-gamma-lower
kind: lemma
contract: Positive-row straddle Gamma lower bound: for an exact signed idempotent P, a vector g with P g = g and 0 <= g_j <= 1, and a row j with positive row-mass A on {k : g_k <= a} and C on {k : g_k >= a + s}: Gamma_j >= (A*C/(1 + nu_j))*s^2 - nu_j (sharp local form), and uniformly Gamma_j >= (A*C/(1 + delta))*s^2 - delta.
defs: def-signed-idempotent; def-negative-mass
deps: lem-signed-carre-du-champ
status: proved
af: none
provenance: W51 wave (docs/waves/2026-07-07-W51-splitting-decider.md): fresh-codex prover (worker BG — positive/negative row decomposition, variance minimization over the centering constant, cross-pair contribution A*C*s^2/(1 + nu_j), negative part subtracts at most nu_j) + SEPARATE fresh-codex hostile verifier (VBG, VALID-WITH-CORRECTIONS — the nu_j form is the sharp local statement; the delta form is the usable uniform corollary)
owner: A
---

**Role (the straddle-to-budget converter, with its honest limit).** Converts level-straddling
row structure into Gamma cost — but at the (F2) scale (s = kappa, C = 4*tau) the positive
term (<= tau^3/4) is dominated by the negative slack (tau^2), so this alone CANNOT produce
the blocker mass floor ([[obs-gamma-two-level-class-count-wall]]). Usable where s and the
masses are constant-scale (level-structure arguments away from the kappa threshold).
