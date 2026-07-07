# Run bundle: W52 pre-registered tall-entry experiment — BLOCKED with named binding constraints (2026-07-07, session 12)

## Hypothesis

bd `aism-2fi` / sketch v15 mode-decider (the FP1-pre-registered experiment): can ANY exact
rational perturbation of the banked rank-3 record enter the tall heavy near-cluster class
(H^2/delta > 16 with a hidden top and nonempty width-4 cluster), and if so does
disjointness survive entry (the reach-conjecture data)?

## Finding

Worker BH (verbatim first line): `BLOCKED (binding constraints: no tried exact perturbation
reached H^2/delta > 16; C4 stayed empty; when top/top-cluster behavior was restored, the
always-tight hulls intersected)`. Four exact families (HA_t, HA_eps, HA_base scaling, the
HEIGHT+A -> TOP-preserving interpolation) + a 1296-record exact grid over six append
directions (1270 with 0 < delta <= 1/4): ZERO tall, ZERO nonempty C4. Binding anatomy:
before H^2/delta approaches 16, either delta inflates, or the deep append row turns
VISIBLE, or the top reverts to the base rows and the hulls INTERSECT. Best disjoint
frontier ever recorded: delta = 4239/80000, H = 4399/40000, H^2/delta = 19351201/84780000
(~0.228 vs threshold 16), gap-hat = 1/1939, reach-hat = 3/58000, A_min = 58000/5817.
Bounded search over named families — NOT an emptiness proof; the (M2) scaffolding.

## Command

```bash
PYTHONDONTWRITEBYTECODE=1 python3 runs/2026-07-07-w52-tall-entry/scripts/w52_exact.py
```

## Invariant / checkable

Exact Fraction arithmetic throughout (no floats); whole-face T/O by min/max over the forced
optimal face (the VAU method); the script re-verifies P^2 = P and row sums per instance;
both W44 bundle scripts rerun PASS alongside (hostile_rank3_verify.py: ALL ASSERTIONS
PASSED); the frontier instances print as full exact matrices for independent recomputation.

## Next

- (M2) tall-emptiness proof wave: turn the three named binding constraints (delta
  inflation / forced visibility / top reversion-with-intersection) into lemmas — the
  huddle-exclusion anatomy (lem-zero-face-vertex-support) is the target statement.
- If a genuinely different construction family is proposed, extend the grid before any
  emptiness claim strengthens.
