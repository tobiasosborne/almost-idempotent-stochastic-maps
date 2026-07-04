# Rank-4 Exact-Rational Numerics Decider

**Status:** L3 numerical evidence only.  All certified arithmetic in `decider_rank4.py` uses `fractions.Fraction`; decimal displays are non-certified readability only.

## Headline Verdicts

- **Pivot-removing disjunction:** no rank-4 violation found.  Exact asserts checked 48 theta-half pivot-removing moves at certified Phi-argmins.
- **Collateral import (CI):** no rank-4 violation found under the natural `c>0` transcription.  Exact asserts checked 144 transverse CI inequalities; smallest slack was `0`.
- **Max rank-4 Phi/delta observed:** `5/4` on `no_center_rank4_a1_100`.  The no-center rank-4 edge case gives Phi/delta `5/4`; the cheap rank-5 no-center probe gives `4/3`, matching `2 - 2/(5-2)`.
- **Max rank-4 B/delta observed:** `27031/82920` on `cycle_coupling_rank4_a1_30_w1_2`.  Max `(B+C)/delta` observed: `157/460` on `cycle_coupling_rank4_a1_12_w1_2`.
- **Blow-up trend:** none seen in this bounded exact search.  Rank-5 cheap probes reproduced the no-center law at `4/3 = 2 - 2/(5-2)` and produced no transfer violation.

## Rank-4 Transcription Used

For a chart `U=(u_0,...,u_{k-1})`, coordinates are `p_i = sum_t a_t(i) p_{u_t}`, `beta_r(i)=P_{u_r i}`, and

`E_r(i)=max(sum_{q != r} max(-a_q(i),0) - (1-a_r(i)), 0)`,  `Phi_r(U)=sum_i max(beta_r(i),0) E_r(i)`.

For rank 4 CI, with pivot `s`, transverse beta row `r`, and the two remaining transverse indices `T={q: q notin {r,s}}`, I used

`R_{r,j}^{(4)}(i) = (1/c-1) a_s(i)^- + sum_{q in T} max(a_s(i) d_q/c,0) - a_s(i)d_r/c`,

where `c=a_s(j)>0` and `d_q=a_q(j)`.  The checked inequality is

`Phi_r(V_j) <= Phi_r(U) + sum_i beta_r(i)^+ max(R_{r,j}^{(4)}(i),0)`.

For cross-pivot mass I kept the validated pairwise split for every ordered pair `r != s`:

`B_{r,s}=sum_i beta_r(i)^+ a_s(i)^-`, `C_{r,s}=sum_i beta_r(i)^- a_s(i)^+`, with `A=B+C-D` asserted exactly.  In rank 4 the reported value is the maximum over the three transverse choices `r` for each maximal pivot `s`.

## Certified Points

| instance | rank | n | delta | theta charts | Phi/delta | max B/delta | max (B+C)/delta | moves | CI pairs |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `CALIBRATION_no_center_rank3_a1_100` | 3 | 4 | `1/100` | 2 | `1` | `0` | `0` | 2 | 4 |
| `no_center_rank4_a1_100` | 4 | 7 | `1/100` | 4 | `5/4` | `0` | `0` | 12 | 36 |
| `no_center_rank4_a1_20` | 4 | 7 | `1/20` | 4 | `5/4` | `0` | `0` | 12 | 36 |
| `no_center_rank4_a1_4` | 4 | 7 | `1/4` | 10 | `5/4` | `0` | `0` | 12 | 36 |
| `cycle_coupling_rank4_a1_5_w15_16` | 4 | 12 | `467/2160` | 81 | `131/2335` | `131/2335` | `31/467` | 4 | 12 |
| `cycle_coupling_rank4_a1_12_w1_2` | 4 | 12 | `115/876` | 81 | `1741/5520` | `1741/5520` | `157/460` | 4 | 12 |
| `cycle_coupling_rank4_a1_30_w1_2` | 4 | 12 | `691/13530` | 81 | `27031/82920` | `27031/82920` | `931/2764` | 4 | 12 |
| `rank5_probe_no_center_a1_100` | 5 | 10 | `1/100` | 6 | `4/3` | `0` | `0` | 10 | 40 |
| `rank5_probe_no_center_a1_20` | 5 | 10 | `1/20` | 6 | `4/3` | `0` | `0` | 10 | 40 |
| `cycle_coupling_rank5_a1_8_w15_16` | 5 | 15 | `72323/530048` | 243 | `4113/72323` | `4113/72323` | `4616/72323` | 10 | 40 |

## Calibration And Hard Asserts

- The script first reproduces the known rank-3 no-center value: `delta=1/100`, `Phi/delta=1`.
- Every emitted instance asserts `BL=I`, `P^2=P`, row sums equal `1`, `delta<=1/4`, exact chart volumes, exact pivot-removing volume identity `Vol(V_j)=|a_s(j)| Vol(U)`, the disjunction, CI for `c>0`, and cross-pivot cancellation.
- Re-run command: `python3 runs/2026-07-04-rank4-transfer-decider/scripts/decider_rank4.py`.

## Honest Scope

- Rank 4 coverage is explicit and finite: three no-center scales and three cyclic coupling mixtures.
- Rank 5 was only a cheap probe: two no-center scales and one cyclic coupling mixture.
- CI was checked only in its stated `c>0` regime.  Negative-pivot moves were included for the disjunction but skipped for CI because the registered CI statement does not cover them.
- This is not a proof and does not search all rank-4 signed idempotents.  It rules out only violations in the deterministic families enumerated here.

## Rank-5 Probe Notes

- `rank5_probe_no_center_a1_100`: Phi/delta `4/3`, max B/delta `0`, moves `10`.
- `rank5_probe_no_center_a1_20`: Phi/delta `4/3`, max B/delta `0`, moves `10`.
- `cycle_coupling_rank5_a1_8_w15_16`: Phi/delta `4113/72323`, max B/delta `4113/72323`, moves `10`.
