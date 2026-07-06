NOT-REALIZED-HERE. Best certified strict-halo `sigma_g` in this worker report is `5991/80000` (rank 5, self-recipient), and the best rank-3 distinct-partner point is `229/3200`; both are far below `1/2`.
This is not an emptiness claim: the exact row-negativity LP relaxation easily puts `5/4` mass on designated outside recipients, but exact geometry then makes those recipients visible (`H=0`), so the named binding constraint is exposedness/absorption rather than row-sum capacity.

# W19 Worker A — Exact Feasibility Attack

Tier legend: [T0] repo definition or banked exact pipeline; [T1] exact computation/assertion from printed rational matrices; [T2] structured non-realization read from these designs; [T3] heuristic interpretation.

## Rerun

```bash
python3 runs/2026-07-06-w19-sigma-frontier/scripts/w19_worker_a.py
```

## Pipeline Calibration

- [T1] `calibration_sigma_halo_nonrobust`: delta=252559/1280000; W=[1, 2, 3, 4]; H=962906/108276325; hidden=[0]; tops=[0]; halo=[]; sigma_g={0: '0'}; dists=['962906/108276325', '0', '0', '0', '0']; tstars={0: '1/25', 1: '224/225', 2: '1', 3: '8/9', 4: '1'}.
- [T1] `rank3_genuine_partner`: delta=74551/1600000; W=[0, 1, 2]; H=2577690413/25862880000; hidden=[3]; tops=[3]; halo=[3, 4]; sigma_g={3: '229/3200'}; dists=['0', '0', '0', '2577690413/25862880000', '18043832891/258628800000']; tstars={0: '11/21', 1: '20/21', 2: '10/21', 3: '1/21'}.

The first calibration is the banked F2 halo-nonrobust witness: raw invisible self-mass `5343/5000` but strict-halo `sigma_g=0`. The second is the banked rank-3 genuine-partner point, recomputed from its exact matrix.

### Calibration matrix: sigma-halo nonrobust anchor

- [T1] Exact certificate: `delta=252559/1280000; W=[1, 2, 3, 4]; H=962906/108276325; hidden=[0]; tops=[0]; halo=[]; sigma_g={0: '0'}; dists=['962906/108276325', '0', '0', '0', '0']; tstars={0: '1/25', 1: '224/225', 2: '1', 3: '8/9', 4: '1'}`.
- [T2] Binding constraint read: raw self-mass can be huge, but here the strict-halo recipient set is empty.

Full exact matrix `P`:

```python
[
  ["5343/5000", "49/160000", "0", "-49/6400", "-49/800"],
  ["14/75", "1201/1200", "0", "-1/48", "-1/6"],
  ["7/50", "1/1600", "1", "-1/64", "-1/8"],
  ["231/5000", "33/160000", "0", "6367/6400", "-33/800"],
  ["3575971/3000000", "510853/96000000", "0", "-510853/3840000", "-30853/480000"]
]
```

## Design 1 — Rank-3 Mass Splitting With Duplicate Outside Recipients

Definition: `C_a=(1/2, 1/2+1/20, -1/20)` for all hidden recipients, `R2` has every hidden column equal to `rho`, and `q=m*rho` is the total hidden-column mass. For every hidden top row in the certified side, `sigma_g=q` because all hidden duplicate recipient columns lie at strict distance `> tau/4` from `conv W`.

| m | rho | q=sigma_g | delta | H | W | hidden tops | binding |
|---:|---:|---:|---:|---:|---|---|---|
| 2 | 5/168 | 5/84 | 1/16 | 1/10 | [0, 1, 2] | [3, 4] | row-negativity scales with total `q`; splitting does not increase total hostable mass |
| 4 | 5/336 | 5/84 | 1/16 | 1/10 | [0, 1, 2] | [3, 4, 5, 6] | row-negativity scales with total `q`; splitting does not increase total hostable mass |
| 8 | 5/672 | 5/84 | 1/16 | 1/10 | [0, 1, 2] | [3, 4, 5, 6, 7, 8, 9, 10] | row-negativity scales with total `q`; splitting does not increase total hostable mass |
| 2 | 1/32 | attempted `1/16` | 21/320 | 0 | [0, 1, 2, 3, 4] | [] | exposedness absorption: recipients enter W |

- [T1] Certified side: `q=5/84`, `delta=1/16`, `H=1/10`, strict-halo recipients are exactly the hidden columns, and each hidden top has `sigma_g=5/84`.
- [T2] Frontier read: increasing `q` from `5/84` to `1/16` does not hit the `delta<=1/4` cap; it flips the hidden recipients into `W`, making `H=0`. The active constraint is exposedness/absorption.
### Best duplicate split point (m=4, q=5/84)

- [T1] Exact certificate: `delta=1/16; W=[0, 1, 2]; H=1/10; hidden=[3, 4, 5, 6]; tops=[3, 4, 5, 6]; halo=[3, 4, 5, 6]; sigma_g={3: '5/84', 4: '5/84', 5: '5/84', 6: '5/84'}; dists=['0', '0', '0', '1/10', '1/10', '1/10', '1/10']; tstars={0: '11/21', 1: '10/21', 2: '20/21', 3: '1/21', 4: '1/21', 5: '1/21', 6: '1/21'}`.
- [T2] Binding constraint read: mass splitting across more recipient indices leaves total `sigma_g=q=5/84`; row negativity and exposedness depend on total q, not m.

Full exact matrix `P`:

```python
[
  ["163/168", "-11/336", "1/336", "5/336", "5/336", "5/336", "5/336"],
  ["-5/168", "325/336", "1/336", "5/336", "5/336", "5/336", "5/336"],
  ["-5/168", "-11/336", "337/336", "5/336", "5/336", "5/336", "5/336"],
  ["79/168", "869/1680", "-79/1680", "5/336", "5/336", "5/336", "5/336"],
  ["79/168", "869/1680", "-79/1680", "5/336", "5/336", "5/336", "5/336"],
  ["79/168", "869/1680", "-79/1680", "5/336", "5/336", "5/336", "5/336"],
  ["79/168", "869/1680", "-79/1680", "5/336", "5/336", "5/336", "5/336"]
]
```

### Duplicate split absorption comparison (m=2, q=1/16)

- [T1] Exact certificate: `delta=21/320; W=[0, 1, 2, 3, 4]; H=0; hidden=[]; tops=[]; halo=[]; sigma_g={}; dists=['0', '0', '0', '0', '0']; tstars={0: '11/21', 1: '1', 2: '20/21', 3: '1/10', 4: '1/10'}`.
- [T2] Binding constraint read: raising total mass slightly makes the outside recipients visible, so there is no hidden top to count.

Full exact matrix `P`:

```python
[
  ["31/32", "-11/320", "1/320", "1/32", "1/32"],
  ["-1/32", "309/320", "1/320", "1/32", "1/32"],
  ["-1/32", "-11/320", "321/320", "1/32", "1/32"],
  ["15/32", "33/64", "-3/64", "1/32", "1/32"],
  ["15/32", "33/64", "-3/64", "1/32", "1/32"]
]
```

## Design 2 — Rank-3 Distinct Genuine Partner Anchor

- [T1] This banked exact point has two strict-halo recipients for the hidden top: self row 3 and distinct partner row 4. It is the best rank-3 distinct-recipient certificate in this report.
### Rank-3 genuine-partner point

- [T1] Exact certificate: `delta=74551/1600000; W=[0, 1, 2]; H=2577690413/25862880000; hidden=[3]; tops=[3]; halo=[3, 4]; sigma_g={3: '229/3200'}; dists=['0', '0', '0', '2577690413/25862880000', '18043832891/258628800000']; tstars={0: '11/21', 1: '20/21', 2: '10/21', 3: '1/21'}`.
- [T2] Binding constraint read: the distinct partner carries only `23/2000`; total `sigma_g=229/3200`, with row 3 negativity already close to the controlling budget.

Full exact matrix `P`:

```python
[
  ["31023/32000", "43/16000", "-949/32000", "9/200", "1/80"],
  ["-457/80000", "40017/40000", "-377/80000", "1/200", "1/200"],
  ["-51/1250", "303/80000", "76661/80000", "11/160", "1/100"],
  ["23129/50000", "-74551/1600000", "819923/1600000", "961/16000", "23/2000"],
  ["7770491/12800000", "-20353/640000", "4572529/12800000", "17831/320000", "377/32000"]
]
```

## Design 3 — Rank-5 One-Hidden Genuine Self Anchor

- [T1] This is the largest certified strict-halo `sigma_g` in this worker report: `5991/80000`. The only strict-halo recipient is the hidden top itself.
### Rank-5 genuine-self point

- [T1] Exact certificate: `delta=3983/96000; W=[0, 1, 2, 3, 4]; H=4131459/48713900; hidden=[5]; tops=[5]; halo=[5]; sigma_g={5: '5991/80000'}; dists=['0', '0', '0', '0', '0', '4131459/48713900']; tstars={0: '134/139', 1: '394/417', 2: '751/1251', 3: '415/417', 4: '569/1251', 5: '17/417'}`.
- [T2] Binding constraint read: self-mass can become genuine, but its amount is small once the row is kept hidden and outside the tau/4 halo.

Full exact matrix `P`:

```python
[
  ["6409/6400", "-69/32000", "-1/64", "3/16000", "-341/16000", "3/80"],
  ["3/8000", "39977/40000", "-1/240", "1/20000", "-341/60000", "1/100"],
  ["3/1280", "-23/6400", "187/192", "1/3200", "-341/9600", "1/16"],
  ["1/2560", "-23/38400", "-5/1152", "19201/19200", "-341/57600", "1/96"],
  ["21/6400", "-161/32000", "-7/192", "7/16000", "45613/48000", "7/80"],
  ["-222027/6400000", "1702207/32000000", "74009/192000", "-74009/16000000", "25237069/48000000", "5991/80000"]
]
```

## Design 4 — Exact LP Relaxation Showing Why Optimization Alone Is Not Enough

- [T1] Fixed rank-3 cycle design with three designated hidden recipients. Exact LP over free `R2` entries, with row negative masses constrained by `delta<=1/4` and designated coefficients constrained nonnegative, maximizes designated mass at `5/4`.
- [T1] Exact geometry of the LP optimizer: delta=1/4; W=[3, 4, 5]; H=0; hidden=[]; tops=[]; halo=[]; sigma_g={}; dists=['0', '0', '0', '0', '0', '0']; tstars={3: '26/31', 4: '26/31', 5: '26/31'}.
- [T2] Binding constraint: the optimizer's recipients become visible (`W=[3,4,5]`, `H=0`). Thus the missing condition is not coefficient capacity; it is keeping high-mass genuine recipients hidden/outside the exposed hull.

Full exact LP optimizer matrix `P`:

```python
[
  ["-495/3224", "0", "5/124", "92325/99944", "18465/99944", "469/99944"],
  ["749/3224", "0", "25/124", "-18751/99944", "76205/99944", "-879/99944"],
  ["-99/3224", "0", "125/124", "2345/99944", "469/99944", "-551/99944"],
  ["-1/4", "0", "0", "149/124", "5/124", "1/124"],
  ["31/104", "0", "0", "-25/104", "99/104", "-1/104"],
  ["0", "0", "5/4", "-25/124", "-5/124", "-1/124"]
]
```

## Assert List

- [T1] calibration sigma-halo-nonrobust: P^2=P and P1=1 from the printed matrix
- [T1] calibration sigma-halo-nonrobust: 0 < delta <= 1/4
- [T1] calibration sigma-halo-nonrobust: W(P) is nonempty
- [T1] calibration sigma-halo-nonrobust: all row distances to conv W computed exactly
- [T1] calibration: delta=252559/1280000
- [T1] calibration: raw sigma=5343/5000 and strict-halo sigma_g=0
- [T1] calibration rank3 genuine partner: P^2=P and P1=1 from the printed matrix
- [T1] calibration rank3 genuine partner: 0 < delta <= 1/4
- [T1] calibration rank3 genuine partner: W(P) is nonempty
- [T1] calibration rank3 genuine partner: all row distances to conv W computed exactly
- [T1] rank3 partner: delta=74551/1600000
- [T1] rank3 partner: hidden top is row 3
- [T1] rank3 partner: strict-halo recipients are rows 3 and 4
- [T1] rank3 partner: sigma_g(row3)=229/3200
- [T1] duplicate split m=2 q=5/84: P^2=P and P1=1 from the printed matrix
- [T1] duplicate split m=2 q=5/84: 0 < delta <= 1/4
- [T1] duplicate split m=2 q=5/84: W(P) is nonempty
- [T1] duplicate split m=2 q=5/84: all row distances to conv W computed exactly
- [T1] duplicate split m=4 q=5/84: P^2=P and P1=1 from the printed matrix
- [T1] duplicate split m=4 q=5/84: 0 < delta <= 1/4
- [T1] duplicate split m=4 q=5/84: W(P) is nonempty
- [T1] duplicate split m=4 q=5/84: all row distances to conv W computed exactly
- [T1] duplicate split m=8 q=5/84: P^2=P and P1=1 from the printed matrix
- [T1] duplicate split m=8 q=5/84: 0 < delta <= 1/4
- [T1] duplicate split m=8 q=5/84: W(P) is nonempty
- [T1] duplicate split m=8 q=5/84: all row distances to conv W computed exactly
- [T1] duplicate split m=2: delta=1/16
- [T1] duplicate split m=2: W=(0,1,2)
- [T1] duplicate split m=2: H=1/10
- [T1] duplicate split m=2: sigma_g=5/84
- [T1] duplicate split m=4: delta=1/16
- [T1] duplicate split m=4: W=(0,1,2)
- [T1] duplicate split m=4: H=1/10
- [T1] duplicate split m=4: sigma_g=5/84
- [T1] duplicate split m=8: delta=1/16
- [T1] duplicate split m=8: W=(0,1,2)
- [T1] duplicate split m=8: H=1/10
- [T1] duplicate split m=8: sigma_g=5/84
- [T1] duplicate split m=2 q=1/16: P^2=P and P1=1 from the printed matrix
- [T1] duplicate split m=2 q=1/16: 0 < delta <= 1/4
- [T1] duplicate split m=2 q=1/16: W(P) is nonempty
- [T1] duplicate split m=2 q=1/16: all row distances to conv W computed exactly
- [T1] duplicate split q=1/16: recipients become visible; no hidden top
- [T1] rank5 genuine self: P^2=P and P1=1 from the printed matrix
- [T1] rank5 genuine self: 0 < delta <= 1/4
- [T1] rank5 genuine self: W(P) is nonempty
- [T1] rank5 genuine self: all row distances to conv W computed exactly
- [T1] rank5 genuine self: delta=3983/96000
- [T1] rank5 genuine self: hidden top is row 5
- [T1] rank5 genuine self: strict-halo recipient is row 5
- [T1] rank5 genuine self: sigma_g(row5)=5991/80000
- [T1] rank3 relaxed cycle LP: exact LP optimum exists
- [T1] rank3 relaxed cycle LP: designated positive mass is 5/4
- [T1] rank3 relaxed cycle LP optimum: P^2=P and P1=1 from the printed matrix
- [T1] rank3 relaxed cycle LP optimum: 0 < delta <= 1/4
- [T1] rank3 relaxed cycle LP optimum: W(P) is nonempty
- [T1] rank3 relaxed cycle LP optimum: all row distances to conv W computed exactly
- [T1] rank3 relaxed cycle LP optimum: no hidden vertices after exact geometry
- [T1] best certified sigma_g in this worker report is 5991/80000
- [T1] best certified sigma_g is below 1/2

## Verdict

- [T2] `sigma_g > 1/2` was not realized here.
- [T2] This is not an emptiness claim. The useful non-realization insight is that coefficient optimization has ample mass, but exact exposedness absorbs the high-mass recipients; in the certified hidden-top families, the frontier is instead controlled by exposedness/halo absorption and row-negativity scaling with total recipient mass.
