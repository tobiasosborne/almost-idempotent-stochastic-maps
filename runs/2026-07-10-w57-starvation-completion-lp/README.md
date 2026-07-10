# Run bundle: W57 exact starvation-gadget completion LP — minimal rank-3 family INFEASIBLE with stable Farkas certificates (2026-07-10, session 14)

## Hypothesis

bd `aism-oxu` / sketch v20 item 0: does the W55 exact starvation gadget (`A0 = 5`,
`g = 5*tau`, exact top-row reproduction, zero far positive inflow) extend to a genuine
counterexample completion in `P = L*B`, `B*L = I` coordinates — the decisive
prove-or-refute instrument for `conj-sl1a-off-diagonal-cell` (H-X) and the L6.5
large-gauge completion wall? (Rigour tag: `numerical` — exact rational computation,
L3 evidence, never proof.)

## Finding

Worker (verbatim first line): `RESULT: INFEASIBLE-CERTIFICATE — The minimal rank-three
actor-hull family is exactly infeasible, while the first extra-vertex completion family
remains open.` Three cases decided in EXACT rational arithmetic (stdlib Fractions, no
floating point in the decision path): `literal_r3_actor5`, `hx_near_r3_actor5`,
`hx_far_r3_nonvertex6` — all INFEASIBLE with exact Farkas certificates. Certificate
STABILITY: survives rational `A0 in [4,6]` and `0 < tau <= 1/256`; the consistent
singleton locus is `g = A0*tau`. HONEST SCOPE: rank-3 minimal actor-hull completions
only; the first EXTRA-VERTEX completion family is UNDECIDED and is the live residual.
The two H-X cases are formal horn relaxations; the canonical actor hull cannot realize
genuine co-top/tall geometry. This REFUTES NOTHING and PROVES NOTHING about H-X/L6.5;
it kills the literal gadget's minimal completions and seeds a candidate mechanism.
Candidate lemma contract extracted by the worker (CERTIFICATE.md; status if ever
codified: conjecture until paper-proved): "after clone aggregation and deletion of
zero-top actor-hull nonvertices, no rank-three projection with row negativity at most
s^2 realizes the pinned starvation tableau for A in [4,6] and sufficiently small s > 0."

## Command

```bash
cd runs/2026-07-10-w57-starvation-completion-lp/scripts
python3 decide.py          # decides the three cases, writes ../data/*.json (exact rationals; deterministic, no seed)
python3 check.py           # INDEPENDENT recomputation from ../data alone -> per-case PASS + "OVERALL PASS"
```

## Invariant (checkable)

`check.py` re-verifies every certificate from the raw JSON alone in exact rationals:
`B*L = I`, `P^2 = P`, the affine gadget constraints, the metric obstruction, the Farkas
combination (nonnegative multipliers summing to a strictly negative combination;
common margin `555569345906618009855/18446744073709551616 > 0`), and the stability
bounds. Expected output: three `PASS ...` lines then `OVERALL PASS` (the two
`FAIL(expected-relaxation)` sub-fields per line are deliberate relaxation probes and
are expected). Reproduced independently by the orchestrator on 2026-07-10: OVERALL PASS.

## Next

1. Decide the extra-vertex completion family (the honest residual) — same exact-LP
   harness, one more vertex of completion freedom.
2. Paper-proof wave on the candidate completion-obstruction lemma from the stable
   multipliers (codex prover + fresh hostile verifier; then af elevation).
3. Fold into the H-X attack: the blocking constraint anatomy in CERTIFICATE.md is the
   candidate mechanism for `conj-sl1a-off-diagonal-cell`.
