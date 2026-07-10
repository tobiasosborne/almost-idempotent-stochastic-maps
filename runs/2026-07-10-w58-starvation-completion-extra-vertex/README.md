# Run bundle: W58 extra-vertex completion family — INFEASIBLE, certificate extends K-parametrically (2026-07-10, session 14)

## Hypothesis

bd `aism-hjm` / sketch v21 item 0a: does the FIRST EXTRA-VERTEX completion family (one
added vertex of completion freedom beyond the W57 minimal actor-hull) complete the W55
starvation gadget to a counterexample in `P = L*B`, `B*L = I` coordinates? The W57
residual and the gadget's only remaining refuter route at rank 3. (Rigour tag:
`numerical` — exact rational computation, L3 evidence, never proof. Parent campaign:
`runs/2026-07-10-w57-starvation-completion-lp`.)

## Finding

Worker (verbatim first line): `RESULT: INFEASIBLE-CERTIFICATE — All three
first-extra-vertex support cases are exactly infeasible, with independent raw
verification passing.` Cases `xv_literal_r3_vertex6`, `xv_hx_near_r3_vertex6`,
`xv_hx_far_r3_vertex6_nonvertex7` all INFEASIBLE (exact Fractions, no floating point
in the decision path). STABILITY: uniform over rational `A0 in [4,6]`,
`0 < tau <= 1/256`, exposer coordinate `Y in [0,1]`; exact reduction
`1/tau - A0 <= X <= 2/tau + 4*tau`; contradiction margin
`186482464633099560555/565148976676864 > 0`. The parent five-entry multiplier pattern
does NOT extend unchanged; a column-local seven-entry pattern does — to `K <= 124`
exterior zero-top support fibers at the parent ceiling, and to EVERY fixed `K` for
`tau <= min(1/256, 1/(12(K+1)))`. HONEST SCOPE: rank-3 only; fixed-K families only
(the ceiling degrades with K — this does NOT decide unbounded-K or rank > 3); refutes
nothing and proves nothing about H-X/L6.5. Updated candidate lemma (CERTIFICATE.md):
for every fixed K >= 1, no rank-three W55 completion with ||p_z - p_v||_1 = tau, row
negativity <= tau^2, at most K exterior zero-top support fibers with canonical exposer
coordinate in [0,1], and remaining added zero-top fibers inside the actor hull, exists
below the stated K-dependent ceiling.

## Command

```bash
cd runs/2026-07-10-w58-starvation-completion-extra-vertex/scripts
python3 decide_xv.py       # decides the three xv cases, writes ../data/xv/*.json (exact rationals; deterministic)
python3 check_xv.py        # INDEPENDENT recomputation from ../data/xv alone -> per-case PASS + "OVERALL PASS"
```

## Invariant (checkable)

`check_xv.py` re-verifies from the raw JSON alone, in exact rationals: `B*L = I`,
`P^2 = P`, the gadget + exterior-vertex constraints, the exact X-reduction, the Farkas
combination (margin above), the stability probes (81 per case), and the K-extension
pattern. Expected output: three `PASS ...` lines then `OVERALL PASS` (the two
`FAIL(expected-relaxation)` sub-fields per line are deliberate relaxation probes).
Reproduced independently by the orchestrator on 2026-07-10: OVERALL PASS.

## Next

1. Paper-proof wave on the K-parametric completion-obstruction candidate lemma
   (bd `aism-cq2`) — the column-local multiplier pattern is the guide; the K-dependent
   ceiling is the honest weakness a paper proof must either accept or remove.
2. Rank > 3 and unbounded-K remain the undecided directions if the paper proof stalls.
3. Fold the blocking-constraint anatomy into the `conj-sl1a-off-diagonal-cell` (H-X)
   attack.
