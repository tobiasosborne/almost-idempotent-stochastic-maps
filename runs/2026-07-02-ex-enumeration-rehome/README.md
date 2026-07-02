# Run bundle: inherited (EX) enumeration re-home - 2026-07-02

**Status: L3 numerical evidence. NEVER rigorous (CLAUDE.md L0/L3).** This is a REHOME of the inherited
classical-portfolio numerical record, not a new theorem and not a proof of `(EX)`, HLC, the linear law, or
`op-classical`. The archived scripts/data are evidence only.

## Hypothesis

Can the inherited exact signed-idempotent enumeration record be quarantined as a reproducible L3 bundle:
exact signed row-stochastic idempotents `P` with `P^2=P`, `delta=max_i neg(p_i)`, `tau=sqrt(delta)`,
`rho=4tau`, `kappa=tau/4`, exposed set `W`, and height `H=dist_1(row, conv W)`; plus the rank-3
theta-`1/2` `(EX)` chart enumeration with `delta<=1/4`?

## Command (re-run)

The small local invariant is the intended cheap check:

```bash
cd runs/2026-07-02-ex-enumeration-rehome
python3 check_invariant.py
```

Recorded output, 2026-07-02:

```text
PASS exact invariant
sha256_checked=4
rank3_records=444
delta_ok_records=278
random_delta_ok=220
adversarial_delta_ok=53
ex_violations_C0_1=0
factorization_violations=0
worst_phi_min_over_delta=1
spot_checks=transverse_pair_a1_8:delta=2/17:phi=2/17:ratio=1;transverse_pair_a1_4:delta=1/5:phi=1/5:ratio=1;no_center_rank3_a1_100:delta=1/100:phi=1/100:ratio=1
```

Archival full reruns require the upstream scientific environment (`scipy`, `sympy`, and for several
campaigns `gurobipy` with presolve discipline). The copied producers live in `scripts/` and may write
outputs relative to the current directory:

```bash
cd runs/2026-07-02-ex-enumeration-rehome/scripts
python3 d8_decision.py
python3 d8_controls.py
python3 d8_sweep.py
python3 d9_duals.py
python3 d10_certmine.py
python3 d11_scalesweep.py
python3 d12_dmfprobe.py
python3 d13_smalldelta.py
python3 d14_leakage.py
python3 rank3_explorer.py
```

Upstream source map: all 58 top-level `*.py` files from
`../almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/` were copied
verbatim to `scripts/`; `scripts/rank3_explorer.py` was copied verbatim from
`../almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/out/w41_ex/rank3_explorer.py`.
Core archived outputs are under `data/upstream/`; `data/campaign_summary.csv` is the local manifest.

## Finding (headline + honest scope)

1. **Broad inherited spine:** the upstream ledger records `67,000+` exact verified instances across
   independent d8-d14 campaigns, with no exact counterexample found. This is numerical evidence only.
2. **Linear-law finding:** within the inherited generators, the record fits the linear pattern
   `H ~= 2 delta` (equivalently `delta ~= H/2`) rather than a small-delta square-root floor. The d13
   small-delta probe found no hidden-top-vertex floor entry for `delta<=1e-2`.
3. **Finite-delta correction:** do not quote a global finite-delta constant `2`. The certified 5x5
   obstruction in `argument/lemmas/obs-linear-law-finite-delta.md` has `delta=49/2000`, `H=1/20`, hence
   `H/delta=100/49>2`; its mechanism is hull-dip, and the scaling has `H/delta -> 2` and `H/tau -> 0`.
4. **Rank-3 `(EX)` enumeration:** `444` exact rank-3 records were archived, `278` with `delta<=1/4`
   (`220` random, `53` adversarial, `5` known/restricted). The enumeration checked `2947` theta-half
   charts in the cap (`7573` charts total), found `0` empirical `(EX)` violations for `C0=1`, and found
   `0` factorization violations. This is rank-3 evidence, not a proof of `(EX)`.
5. **Known caveat:** below the corner scale `delta~0.233`, the dangerous antecedent was never entered:
   no verified record had the joint regime `sigma_tilde>tau` and `H>Btau`. That absence is evidence, not
   a theorem or emptiness proof.

## Invariant / certificate (checkable)

`check_invariant.py` performs an independent exact-rational consistency check on the stored rank-3 `(EX)`
records using Python `Fraction`: it recomputes `phi_min/delta` for three named exact records, confirms the
expected `444/278/220/53` counts, confirms `0` `C0=1` empirical `(EX)` violations, confirms `0`
factorization violations, and checks SHA-256 for four archived artifacts:

- `data/upstream/d8_decision.json`
- `data/upstream/d13_smalldelta.json`
- `data/upstream/d14_leakage.json`
- `data/upstream/w41_ex/rank3_results.json`

The invariant does not rerun the 67k campaign and does not certify truth of the mathematical claims.

## Next

- Keep this record tagged `numerical (L3)` wherever cited.
- Any rigorous upgrade must be a separate byte-matched reference, `af` validation, Lean proof, or reviewed
  proof shard; this bundle alone cannot promote a claim.
- If a future worker needs full rerun reproducibility, pin the exact Python package/Gurobi environment and
  write a fresh run bundle rather than editing this inherited re-home.
