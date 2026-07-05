<!--
WAVE: decision-check DC1 (fusion check, D/G coupling hypothesis) — 2026-07-05, session 8.
WORKER: fresh codex exec (prompt: session scratchpad PROMPT-dc1-fusion.md). Worker answer VERBATIM below.
ORCHESTRATOR: worker script rerun clean (exit 0, all hard asserts). Headline: FUSION SUPPORTED on
  the finite certificate set (T0 recomputations; T2 interpretation) — every D-line demand (M_D,
  L_mu, F_L, FIN_lhs) financed by the G-line contract budget, no demand-positive/budget-zero
  escape; worst ratio M_D/budget = 1 exactly (D3, financed entirely by SIGMA). NOTE: no instance
  here has B_{r,s} > 0 at the certified pivot — no NSC coupling data (that was DC2's job).
TIER: T0 per-instance certificates; T2 fusion verdict (finite evidence, not proof).
-->

# DC1 Fusion Check: exact recomputation report

Rerun command:

```bash
python3 waves-scratch/dc1-fusion/verify_fusion.py
```

All arithmetic in the script uses `fractions.Fraction`; decimal values below are display-only. Scratch artifacts written: `waves-scratch/dc1-fusion/verify_fusion.py` and `waves-scratch/dc1-fusion/REPORT.md`. No `fr`, `bd`, or `git` command was run.

## Tiered Verdict

- **T0:** The requested D3, D4, D6A, and D6B certificates reconstruct exactly and pass the hard asserts listed below.
- **T0:** In every reconstructed certificate, each D-line demand tested here has positive combined G-contract budget; no demand-positive/budget-zero escape occurs.
- **T0:** The largest exact requested-demand ratio among `M_D`, `L_mu`, `F_L`, and `FIN_lhs` is `1` for `M_D` at `D3 centered fan`.
- **T0:** The largest exact `FIN_lhs / (G_class^- + S_-^mu + SIGMA_s + FanRes_s)` ratio alone is `131750/471329` at `D6 legal leak B / FIN stress`.
- **T2 VERDICT: FUSION SUPPORTED on this finite certificate set.** The D-line residuals are financed by the G-line combined budget at bounded exact ratios. This is evidence only, not a proof.
- **T2:** These finite ratios do **not** predict a value of the universal `(FIN)` constant.

## Per-instance Exact Data

| instance | `delta` | D rows | legal rows | `M_D` | `L_mu` | `F_L` | `FIN_lhs` | G-contract budget | `FIN_lhs/budget` |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| D3 centered fan | `1/10` | p, m | none | `1/20` | `0` | `0` | `0` | `1/20` | `0` |
| D4 B-block contraction refuter | `1/5` | p, m | none | `21/200` | `0` | `0` | `21/4000` | `21/100` | `1/40` |
| D6 legal leak A eps=`1/10000` | `10/41` | pB | mA, mB | `1/100000` | `999959/4100000` | `0` | `999959/4100000` | `1051002583/1176700000` | `286988233/1051002583` |
| D6 legal leak B / FIN stress | `1217/5000` | pB | mA | `87/20000` | `1143/5000` | `21717/20000000` | `4743/20000` | `4241961/5000000` | `131750/471329` |

## Budget Anatomy

- **D3, D4:** financed entirely by `SIGMA_s`; `G_class^- = S_-^mu = FanRes_s = 0`.
- **D6A:** `G_class^- = 10/41` alone exceeds `FIN_lhs = 999959/4100000`; `SIGMA_s` covers the tiny `M_D`; `FanRes_s` is extra slack.
- **D6B:** `G_class^-` covers most legal leak; `S_-^mu + SIGMA_s` cover the remaining `(FIN)` gap; `FanRes_s` is extra slack.
- **NSC:** no requested instance has `B_{r,s}>0` at the certified pivot, so there are no nontrivial NSC ratios to report.

## Demand Ratios

| instance | `M_D/budget` | `L_mu/budget` | `F_L/budget` | `FIN_lhs/budget` |
|---|---:|---:|---:|---:|
| D3 centered fan | `1` | `0` | `0` | `0` |
| D4 B-block contraction refuter | `1/2` | `0` | `0` | `1/40` |
| D6 legal leak A eps=`1/10000` | `11767/1051002583` | `286988233/1051002583` | `0` | `286988233/1051002583` |
| D6 legal leak B / FIN stress | `7250/1413987` | `127000/471329` | `2413/1885316` | `131750/471329` |

## Hard Asserts

- `B*L=I_3`, `P^2=P`, row sums `1`, positive `delta`: all four instances.
- certified theta-half `Phi`-argmin chart and maximal pivot: all four instances.
- D3: `delta=1/10`, `M_D=delta/2`, H-M `G_class^-=0`, `S_-^mu=0`, quoted chart scores.
- D4: `delta=1/5`, `rho_B=21/20`, `M_D/delta=21/40`, H-M `G_class^-/delta=1/4`, `R_D^nu/delta=21/20`, quoted chart scores.
- D6A: `delta=10/41`, `L_mu/delta=999959/1000000`, `M_D/delta=41/1000000`, `F_L=0`, `FIN_lhs/delta=999959/1000000`.
- D6B: `delta=1217/5000`, `L_mu/delta=1143/1217`, `F_L/delta=21717/4868000`, `M_D/delta=87/4868`, `FIN_lhs/delta=4743/4868`, `FIN_right/delta=591017/608500`, `(FIN_lhs)/(FIN_right)=592875/591017`.
- D5 stationarity identity asserted column-by-column on every non-chart column.
- `FanRes` residual nonnegativity asserted on every included legal negative cover.
- basis determinant nonzero asserted during exact chart-coordinate solves.
