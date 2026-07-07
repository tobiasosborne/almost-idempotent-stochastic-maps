# Run bundle: W44 rank-3 boundary census — the T/O hull intersection at the tall-heavy class boundary (2026-07-07, session 12)

## Hypothesis

bd `aism-2fi` / wave W44 (docs/waves/2026-07-07-W44-t1-intersection.md), worker AU: decide
(T1) at rank 3 — prove the cluster-uniform always-tight T/O hull intersection where hulls
are computable, or refute it with an exact certificate.

## Finding

Worker AU (verbatim first line): `PARTIAL (proved: exact rank-3 boundary certificates for
the T/O intersection, including failure outside the tall-heavy hypotheses and success on the
banked top-preserving/frontier tops; gap: no rank-3 theorem forcing optimal-face T/O
interlacing from tall heavy near-cluster hypotheses)`. Three exact instances:

1. **W41 HEIGHT+A** (delta = 9859/400000, H = 10059/200000): BOTH positive-mass near hidden
   rows u = 3, 4 of the top have EMPTY W43 intersections (u=3: t* = 1/100, T = {1}, O = {2};
   u=4: t* = 5339/292059, T = {0}, O = {2}) — and the instance is OUTSIDE the tall-heavy
   class (H^2/delta = 101183481/985900000 < 16, i.e. H < 4*tau; G_4 empty). NOT a (T1)
   refuter; the sharpest boundary datum.
2. **W41 TOP-preserving** (delta = 49/2000): the intersection HOLDS at every positive-mass
   near hidden row of each hidden top, with exact convex certificates
   (59/123)d_0 + (64/123)d_1 = (1/41)d_2 and (61/123)d_0 + (62/123)d_1 = (1/41)d_2.
3. **W29 frontier** (delta = 99/8000): both hidden tops satisfy the intersection
   (t* = 1/81; weights [119/243, 124/243] and [121/243, 122/243] vs [1]).

Instance facts, NOT a general theorem: empty intersections are realized only OUTSIDE the
tall-heavy hypotheses; every banked in-class instance satisfies (T1). Bounded census (three
instances), no universality claim.

## Command

```bash
PYTHONDONTWRITEBYTECODE=1 python3 runs/2026-07-07-w44-rank3-boundary/scripts/rank3_t1_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 runs/2026-07-07-w44-rank3-boundary/scripts/hostile_rank3_verify.py
```

## Invariant / checkable

TWO independent exact-rational verifiers (prover AU's checker + hostile verifier VAU's
independent implementation — VAU hardcodes only the matrices and solves the exposedness LPs
by exact vertex enumeration in h-value space via P h = h, checking whole-face tightness by
min/max of each h_k over the forced optimal face t = t*). Both hard-assert: P^2 = P, row
sums, delta, W/hidden/top classification, t*, whole-face T/O sets, hull
intersection/emptiness with exact weights, and the class arithmetic (H^2/delta values, G_4
emptiness). VAU's script exits printing `ALL ASSERTIONS PASSED`; orchestrator reruns of both:
PASS. Registry consumer: obs-rank3-t1-boundary (VAU-approved contract).

## Next

- Route (a) of sketch v12: the rank-3 interlacing lemma (lem-rank3-cluster-uniform-optimal-face-interlacing candidate) — prove the in-class intersection from planar hull geometry, with HEIGHT+A as the boundary stress instance.
- Extend the census toward the class boundary (perturb HEIGHT+A INTO the tall-heavy class while tracking the intersection) if the proof wave stalls.
