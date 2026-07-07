---
id: lem-harmonic-line-coordinate-row-balance
kind: lemma
contract: Harmonic line-coordinate row balance: for an exact signed idempotent P and any affine-in-position row coordinate r with r_u = 0 at a row index u, one has 0 = sum_j P_uj r_j, and with M_+ = sum over {j : P_uj > 0, r_j > 0} of P_uj*r_j and M_- = -sum over {j : P_uj > 0, r_j < 0} of P_uj*r_j and R = max_j |r_j|: M_+ <= M_- + nu_u*R and M_- <= M_+ + nu_u*R.
defs: def-signed-idempotent; def-negative-mass
deps: lem-harmonic-affine-bridge
status: proved
af: none
provenance: W49 wave (docs/waves/2026-07-07-W49-face-deciders.md): fresh-codex prover (worker BF) + SEPARATE fresh-codex hostile verifier (VBD, VALID — exact sign split re-derived; HEIGHT+A fixture recomputed independently: r = (6400/59, -100, 0, 0, 205/59, 1), P r = r, M_+ = M_- = 3137/60 at row 3, nu_3 = 49/2000)
owner: A
---

**Role.** Every row balances exactly across any harmonic line coordinate centered at it —
the elementary two-sidedness engine for the (F1) T-spread question. Alone it is NOT enough:
the balancing far rows need not be always-tight ([[obs-rank3-t1-boundary]]'s HEIGHT+A
carries the missing side on a NON-tight far row — the tightness-promotion wall).
