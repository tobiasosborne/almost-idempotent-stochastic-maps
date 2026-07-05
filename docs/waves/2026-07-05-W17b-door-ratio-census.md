<!--
WAVE: wave 17b (sigma-door ratio decider) — 2026-07-05, session 8.
WORKER: fresh codex exec (prompt: session scratchpad PROMPT-w17b-door-ratio.md). Answer VERBATIM
  below (worker's full report incl. all assert lines: runs/2026-07-05-door-ratio-census/data/
  full-report.md).
ORCHESTRATOR: script rerun clean from waves-scratch AND from the banked bundle (exit 0; stdout
  captured to data/census-stdout.txt; one mechanical re-home patch parents[2]->parents[3],
  precedent = the wave-13 amplifier bundle); 19 hard asserts incl.
  the three calibrations against banked exact witnesses (the sigma-halo witness reproduces
  sigma_g = 0 exactly). Verdict REGIME-EMPTY-SO-FAR — honest: NOT an emptiness claim.
STRATEGIC READING (orchestrator): with wave-17's D1 (constant cap sigma_g <= 1/2 => Kernel with
  B = 29/8 via the af-validated halo-collapse), the census's max sigma_g = 1/25 shows >= 12x
  empirical slack on the Route-A constant-cap target — consistent with the upstream ~25k census
  (sigma_g <~ 0.37*tau). The B4 walls targeted the TIGHTER sigma_g <= 1 - c*tau cap and a
  specific mechanism; the wall re-read against the constant cap is session 9's top item.
TIER: T0 census + calibrations; the strategic reading is T2.
-->

# Wave 17b Door-Ratio Decider Report

Full banked report, including every hard assert line, is at [ANSWER.md](/home/tobias/Projects/almost-idempotent-stochastic-maps/waves-scratch/w17b-door-ratio/ANSWER.md). Script is [door_ratio_decider.py](/home/tobias/Projects/almost-idempotent-stochastic-maps/waves-scratch/w17b-door-ratio/door_ratio_decider.py).

## Rerun

```bash
python3 waves-scratch/w17b-door-ratio/door_ratio_decider.py
```

## Verdict

**REGIME-EMPTY-SO-FAR.** I certified 514 rank-3 exact instances with exact rational arithmetic and found **0** hidden top vertices with `sigma_g > 1/2` under `delta <= 1/4`.

This is not an emptiness claim. It says the D1 door regime is still hard to realize in the tested banked and fresh families, so the door ratio is **undecided** in its intended high-halo branch.

## Key Census

- Candidate rank-3 instances loaded: `514`
- Exact analyses completed: `514`
- Errors/skips: `0`
- Certified with `0 < delta <= 1/4`: `298`
- Certified with nonempty `W`: `298`
- Instances with hidden top vertices: `74`
- Hidden top vertices measured: `138`
- Hidden tops with `sigma_g > 0`: `50`
- Hidden tops with `sigma_g > 1/2`: `0`
- D3 argmin-chart contains hidden top: `0`
- D5 zero-pivot halo-mass examples: `0`

## Best Certified Halo Case

Best halo mass found:

```text
label      fresh-web-p1/20-x0-rho1/50
delta      6/125
W          [0, 1, 2]
H          1/10
v          3 and 4
sigma_raw  1/25
sigma_g    1/25
max S*     21/500
R_door     21/2
argmin     [(0, 1, 2)]
```

This is far below the required `sigma_g > 1/2`.

## Calibrations Hard-Asserted

- s5: `delta=1841/1600000`, `W=[0,1,2]`, `H=1/1000`, `sigma_raw(row3)=1/2000`, `sigma_g(row3)=0`.
- web headline: `delta=49/2000`, `W=[0,1,2]`, `H=1/20`, hidden tops `[3,4]`.
- sigma-halo witness: `delta=252559/1280000`, hidden top with `sigma_raw=5343/5000`, `sigma_g=0`.

## Next Experiment

Use an exact feasibility/optimization loop for `sigma_g > 1/2` instead of broader brute-force family search: fix rank-3 `Lambda=[I;C]`, impose a candidate hidden-top/visible-set combinatorial type and tau/4 halo membership, then solve for `R2` with exact branch-and-bound over the quadratic threshold comparisons.