# Run bundle: W29 — witness-constrained tall-web hunt (refuter side) (2026-07-06/07, session 11)

## Hypothesis

Sketch v7 ledger item 5 / bd `aism-hhf`: can an exact signed idempotent satisfy ALL reviewed
constraints (canonical geometry, hiddenness dual witnesses at every hidden carrier, top-slab
companion, top concentration) while refuting conj-min-a-w4 (tall, every hidden top σ₄ > 1/2)?

## Finding

NOT-REFUTED. Best certified TRUE-hidden frontier instance: δ = 99/8000, H = 1/40,
H²/δ = 5/99 (H/τ = √(5/99) ≈ 0.225 ≪ 13), W = {r0,r1,r2}, hidden tops {r3,r4} with exact
witnesses (t* = 1/81 each), G₄ = ∅, σ₄ ≡ 0. Two-sided pincer diagnosis: (i) true hiddenness
folds back before depth 4τ — max d_j = H < 4τ in every certified construction, so G₄ never
turns on; (ii) tall/high-mass attempts die by exposedness absorption (the would-be hidden top
becomes canonically visible, W expands, H collapses). Full frontier table in
`docs/waves/2026-07-06-W29-witness-coupling.md` and the worker answer (session scratchpad).

## Command

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -u runs/2026-07-06-w29-witness-coupling/scripts/w29_verify.py
```

(Worker X's self-contained exact verifier, recovered verbatim from its /tmp scratch;
orchestrator rerun: PASS.)

## Invariant / checkable

The script hard-verifies, in exact rationals: P² = P, row sums, δ = 99/8000; canonical
W = {0,1,2} and hidden = {3,4} via exact exposedness LPs; t*(r3) = t*(r4) = 1/81 < κ; the
printed dual witnesses' balance equations; G₄ emptiness (max d_j = H = 1/40 < 4τ). Exit
prints `PASS`.

## Next

W32 (coupling attempt #2): the untouched complementary-slackness channel — the OPTIMAL exposer
h* paired with row reproduction at v gives positive-mass control ≤ ν_v/s on {h* ≥ s}; combine
with lem-hiddenness-depth-markov (94% of witness mass deep+far) and lem-top-concentration.

## Honest scope (L3)

Bounded refuter search: NO emptiness claim; the certified instances are exact [T0] facts about
themselves. The prover-side lemmas of this wave live in the registry (L5 reviewed), not here.
