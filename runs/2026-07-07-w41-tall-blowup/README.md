# Run bundle: W41 refuter side — the tall alpha-blowup frontier (2026-07-07, session 11)

## Hypothesis

bd `aism-2fi` / wave W41 (docs/waves/2026-07-07-W41-tall-blowup-decider.md): can the realized
alpha blow-up (obs-realized-alpha-blowup) coexist with the tall heavy near-cluster hypotheses
of conj-near-cluster-absorption?

## Finding

Worker AM (verbatim first line): `NOT-SUSTAINED (frontier: v-top H/tau = sqrt(5/49), S4 = 0,
A_min = 0, delta = 49/2000; alpha-preserved record has H_global/tau =
sqrt(101183481/985900000), A_min = 100, but v is not top; binding constraint: the thin alpha
row becomes visible/taller, and forcing v top collapses A_min to 0)`. Four exact certificate
families (OBS4 baseline / HEIGHT+A / TOP-preserving / SELF-heavy): in EVERY one, the alpha
blow-up and the hidden-TOP condition are mutually exclusive; S4 = 0 throughout. Instance
facts, NOT a general no-go — but exact-certificate support for
conj-tall-zero-face-radial-thickness at tops. Verifier VAN independently reran the script.

## Command

```bash
PYTHONDONTWRITEBYTECODE=1 python3 runs/2026-07-07-w41-tall-blowup/scripts/w41_am_verify.py
```

(Worker AM's self-contained exact verifier, recovered verbatim from /tmp; orchestrator rerun:
PASS; VAN rerun: PASS.)

## Invariant / checkable

The script hard-verifies in exact rationals: P² = P and row sums for all four families;
canonical W/hidden/top classification via exact LPs; per-instance t*, A_min (exact witness
LPs), S4 ledgers; the frontier table values incl. A_min = 100 (HEIGHT+A, v non-top),
A_min = 0 (TOP-preserving), A_min = 25625/256 (SELF-heavy, P_vv = 1). Exit prints PASS.

## Next

Attack conj-tall-zero-face-radial-thickness directly (why does TOPNESS fatten the zero face?
— the certified dichotomy suggests a real mechanism: at a top, the residual direction points
"downhill" where the cluster/near rows provide hull thickness), or route (ii) of the W40 fork
(the capacity + cancellation finisher).

## Honest scope (L3)

Bounded constructions — no universality claim; each certificate is a [T0] fact about itself.
The prover-side lemmas live in the registry (L5 reviewed).
