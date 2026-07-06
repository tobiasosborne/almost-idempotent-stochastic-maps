# Run bundle: W35 refuter side — the absorption threshold, measured exactly (2026-07-07, session 11)

## Hypothesis

bd `aism-2fi` / wave W35 (docs/waves/2026-07-07-W35-absorption.md): how much received deep
mass R = sum over surviving-deep recipients of P_vj^+ is sustainable at a truly hidden vertex
(exact rational certificates, canonical geometry)? The absorption theorem's empirical target.

## Finding

Worker AD (verbatim first line): `NOT-SUSTAINED (frontier: R_4 = 0 in these certified
constructions; binding constraint: true-hidden rows stay below 4τ, while coefficient pushes
are absorbed into W)`. Frontier table (all exact):
- width 4: best sustained R = 0 (W29 true-hidden, δ = 99/8000, H/τ = √(5/99));
- width 1: best sustained R = 0 (rank-5 scaled record, δ = 5588149/96000000, H/τ ≈ 0.351);
- width 1/4: R = 8405373/80000000 ≈ 0.105 at scale s = 1403/1000 — and **the SAME direction
  at s = 351/250 ABSORBS the hidden row into W (t*₅ = 51/569, H = 0): the absorption
  transition captured exactly in a 1-parameter family.**
- LP comparison at δ = 1/4: a 5/4 positive coefficient exists with EVERYTHING visible —
  coefficient capacity is NOT the blocker; exact geometry is.

## Command

```bash
PYTHONDONTWRITEBYTECODE=1 python3 runs/2026-07-07-w35-absorption-threshold/scripts/w35_worker_ad_verify.py
```

(Worker AD's self-contained exact verifier, recovered verbatim from /tmp; orchestrator rerun:
PASS.)

## Invariant / checkable

The script hard-verifies in exact rationals: all printed matrices are exact signed idempotents
(P² = P, row sums 1); canonical W/hidden classification via exact exposedness LPs; the R
ledgers; the s = 1403/1000 vs s = 351/250 transition (hidden → visible with exact t* values).
Exit prints `PASS`.

## Next

W36: the transition wave — hand the prover THIS 1-parameter family and ask what quantity
crosses zero at the absorption transition; extract and generalize the exposer that appears at
s = 351/250. The cluster-to-exposedness statement (the cap's true content, W35 round 1) is the
target; the transition is its Rosetta stone.

## Honest scope (L3)

Bounded constructions — NO emptiness/threshold-universality claim; each certificate is a [T0]
fact about itself. The prover-side lemmas live in the registry (L5 reviewed).
