NO-KILL-FRONTIER. In the exact matrices and duplicate-family scan certified here, every workable deep halo `a in {4,5,6}` has `G_a` empty, so visible `sup g_w/tau = 0` and band `sup g = 0`. This is a frontier report, not an emptiness theorem.

# W20 Worker B — adversarial g-bootstrap kill attempt

Tier legend: [T0] repo definition/banked construction pattern; [T1] exact Fraction computation hard-asserted by this script; [T2] structured read from the checked constructions; [T3] heuristic.

## Rerun

```bash
python3 runs/2026-07-06-w20-g-zoo-measurement/scripts/w20_worker_b.py
```

## Verdict

- [T1] K1 was not realized: for all certified records in this worker artifact and all `a in {4,5,6}`, `G_a` is empty, hence every visible row has signed `g_w=0`.
- [T1] K2 was not realized at workable widths: the same empty `G_a` gives no non-W level set with `g>=1/2`.
- [T1] Low-halo stress only (`a=1/4`): best visible value is `7/80` on `rank5 genuine self`, with `(g/tau)^2=105/569` and `g/tau~0.429575`.
- [T1] Low-halo band frontier (`a=1/4`): best non-W signed `g` is `5991/80000` on `rank5 genuine self`; this is far below `1/2`.
- [T2] Binding constraint: coefficient capacity is not the wall. The exact row-negativity LP places `5/4` designated positive mass, but exact geometry absorbs those rows into `W` (`H=0`). In the under-cap exact geometries that keep hidden rows, depth stays inside even the `a=1` halo, let alone `a=4`.

## Workable-width frontier table

| a | visible frontier | visible g | (g/tau)^2 | band frontier | band g | level(g>=1/2) |
|---:|---|---:|---:|---|---:|---|
| 4 | calibration sigma-halo-nonrobust | 0 | 0 | calibration sigma-halo-nonrobust | 0 | [] |
| 5 | calibration sigma-halo-nonrobust | 0 | 0 | calibration sigma-halo-nonrobust | 0 | [] |
| 6 | calibration sigma-halo-nonrobust | 0 | 0 | calibration sigma-halo-nonrobust | 0 | [] |

## Low-halo diagnostics

- [T1] These are not K1/K2 kills because `a=1/4` is the old sigma-halo scale, not the workable `a>=4` Lemma-A scale.
- [T1] Best visible low-halo row: `rank5 genuine self`; a=1/4: G=[5]; max_W g=7/80 (g/tau~0.429575, (g/tau)^2=105/569); max_nonW g=5991/80000; level(g>=1/2)=[].
- [T1] Best non-W low-halo row: `rank5 genuine self`; a=1/4: G=[5]; max_W g=7/80 (g/tau~0.429575, (g/tau)^2=105/569); max_nonW g=5991/80000; level(g>=1/2)=[].
- [T1] Weighted row-cloning row 4 of the rank-3 partner by weights 1/3,2/3 transports `G_{1/4}` from `(3,4)` to `(3,4,5)` and preserves all old-row `g` values exactly.

## LP relaxation vs exact geometry

- [T1] The relaxed cycle LP optimizes only coefficient/negative-mass constraints and reaches designated positive mass `5/4`.
- [T1] After exact visible-set geometry is recomputed, that optimizer has `W=[3,4,5]`, `H=0`, no hidden row, and all `G_a` empty. This repeats the W19 absorption wall in the signed `g` language.

## Full exact matrices for frontier/certificate instances

### rank3 genuine partner

- [T1] delta=74551/1600000; W=[0, 1, 2]; H=2577690413/25862880000; H/tau~0.461729; hidden=[3]; tops=[3]; dists=['0', '0', '0', '2577690413/25862880000', '18043832891/258628800000']; tstars={0: '11/21', 1: '20/21', 2: '10/21', 3: '1/21'}.
- [T1] a=1/4: G=[3, 4]; max_W g=63/800 (g/tau~0.364824, (g/tau)^2=19845/149102); max_nonW g=229/3200; level(g>=1/2)=[].
- [T1] a=4: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=5: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=6: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].

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

### duplicate split m=4 q=5/84

- [T1] delta=1/16; W=[0, 1, 2]; H=1/10; H/tau~0.400000; hidden=[3, 4, 5, 6]; tops=[3, 4, 5, 6]; dists=['0', '0', '0', '1/10', '1/10', '1/10', '1/10']; tstars={0: '11/21', 1: '10/21', 2: '20/21', 3: '1/21', 4: '1/21', 5: '1/21', 6: '1/21'}.
- [T1] a=1/4: G=[3, 4, 5, 6]; max_W g=5/84 (g/tau~0.238095, (g/tau)^2=25/441); max_nonW g=5/84; level(g>=1/2)=[].
- [T1] a=4: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=5: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=6: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].

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

### duplicate split m=2 q=1/16

- [T1] delta=21/320; W=[0, 1, 2, 3, 4]; H=0; H/tau~0.000000; hidden=[]; tops=[]; dists=['0', '0', '0', '0', '0']; tstars={0: '11/21', 1: '1', 2: '20/21', 3: '1/10', 4: '1/10'}.
- [T1] a=1/4: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=4: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=5: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=6: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].

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

### rank5 genuine self

- [T1] delta=3983/96000; W=[0, 1, 2, 3, 4]; H=4131459/48713900; H/tau~0.416372; hidden=[5]; tops=[5]; dists=['0', '0', '0', '0', '0', '4131459/48713900']; tstars={0: '134/139', 1: '394/417', 2: '751/1251', 3: '415/417', 4: '569/1251', 5: '17/417'}.
- [T1] a=1/4: G=[5]; max_W g=7/80 (g/tau~0.429575, (g/tau)^2=105/569); max_nonW g=5991/80000; level(g>=1/2)=[].
- [T1] a=4: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=5: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=6: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].

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

### web-regime headline H/delta witness

- [T1] delta=49/2000; W=[0, 1, 2]; H=1/20; H/tau~0.319438; hidden=[3, 4]; tops=[3, 4]; dists=['0', '0', '0', '1/20', '1/20']; tstars={0: '62/123', 1: '59/123', 2: '40/41', 3: '1/41', 4: '1/41'}.
- [T1] a=1/4: G=[3, 4]; max_W g=1/50 (g/tau~0.127775, (g/tau)^2=4/245); max_nonW g=1/50; level(g>=1/2)=[].
- [T1] a=4: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=5: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=6: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].

Full exact matrix `P`:

```python
[
  ["99/100", "-21/2000", "1/2000", "1/100", "1/100"],
  ["-1/100", "1979/2000", "1/2000", "1/100", "1/100"],
  ["-1/100", "-21/2000", "2001/2000", "1/100", "1/100"],
  ["289/600", "3137/6000", "-49/2000", "1/100", "1/100"],
  ["299/600", "3037/6000", "-49/2000", "1/100", "1/100"]
]
```

### relaxed cycle LP absorption

- [T1] delta=1/4; W=[3, 4, 5]; H=0; H/tau~0.000000; hidden=[]; tops=[]; dists=['0', '0', '0', '0', '0', '0']; tstars={3: '26/31', 4: '26/31', 5: '26/31'}.
- [T1] a=1/4: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=4: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=5: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].
- [T1] a=6: G=[]; max_W g=0 (g/tau~0.000000, (g/tau)^2=0); max_nonW g=0; level(g>=1/2)=[].

Full exact matrix `P`:

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

## Duplicate-family scan

- [T1] Checked `98` under-cap exact duplicate-family candidates over rational `p,q`; every candidate hard-asserted idempotence, row sums, `0<delta<=1/4`, visible-set nonemptiness, exact distances, and `Pg=g` for every listed halo width.
- [T2] No checked scan candidate had positive `G_a` for `a in {4,5,6}`. This is a bounded construction-family frontier, not a proof of impossibility.

## Assert list

- [T1] calibration sigma-halo-nonrobust: P^2=P and P1=1
- [T1] calibration sigma-halo-nonrobust: 0 < delta <= 1/4
- [T1] calibration sigma-halo-nonrobust: W(P) is nonempty
- [T1] calibration sigma-halo-nonrobust: exact dist_1 to conv(W) for every row
- [T1] calibration sigma-halo-nonrobust: Pg=g exactly for a=1/4
- [T1] calibration sigma-halo-nonrobust: Pg=g exactly for a=1
- [T1] calibration sigma-halo-nonrobust: Pg=g exactly for a=2
- [T1] calibration sigma-halo-nonrobust: Pg=g exactly for a=4
- [T1] calibration sigma-halo-nonrobust: Pg=g exactly for a=5
- [T1] calibration sigma-halo-nonrobust: Pg=g exactly for a=6
- [T1] calibration sigma-halo-nonrobust: delta matches banked value
- [T1] calibration sigma-halo-nonrobust: strict tau/4 halo G is empty
- [T1] rank3 genuine partner: P^2=P and P1=1
- [T1] rank3 genuine partner: 0 < delta <= 1/4
- [T1] rank3 genuine partner: W(P) is nonempty
- [T1] rank3 genuine partner: exact dist_1 to conv(W) for every row
- [T1] rank3 genuine partner: Pg=g exactly for a=1/4
- [T1] rank3 genuine partner: Pg=g exactly for a=1
- [T1] rank3 genuine partner: Pg=g exactly for a=2
- [T1] rank3 genuine partner: Pg=g exactly for a=4
- [T1] rank3 genuine partner: Pg=g exactly for a=5
- [T1] rank3 genuine partner: Pg=g exactly for a=6
- [T1] rank3 genuine partner: delta matches banked value
- [T1] rank3 genuine partner: W=(0,1,2)
- [T1] rank3 genuine partner: G_{1/4}=(3,4)
- [T1] rank3 genuine partner: G_4 is empty
- [T1] duplicate split m=4 q=5/84: P^2=P and P1=1
- [T1] duplicate split m=4 q=5/84: 0 < delta <= 1/4
- [T1] duplicate split m=4 q=5/84: W(P) is nonempty
- [T1] duplicate split m=4 q=5/84: exact dist_1 to conv(W) for every row
- [T1] duplicate split m=4 q=5/84: Pg=g exactly for a=1/4
- [T1] duplicate split m=4 q=5/84: Pg=g exactly for a=1
- [T1] duplicate split m=4 q=5/84: Pg=g exactly for a=2
- [T1] duplicate split m=4 q=5/84: Pg=g exactly for a=4
- [T1] duplicate split m=4 q=5/84: Pg=g exactly for a=5
- [T1] duplicate split m=4 q=5/84: Pg=g exactly for a=6
- [T1] duplicate split m=2 q=1/16: P^2=P and P1=1
- [T1] duplicate split m=2 q=1/16: 0 < delta <= 1/4
- [T1] duplicate split m=2 q=1/16: W(P) is nonempty
- [T1] duplicate split m=2 q=1/16: exact dist_1 to conv(W) for every row
- [T1] duplicate split m=2 q=1/16: Pg=g exactly for a=1/4
- [T1] duplicate split m=2 q=1/16: Pg=g exactly for a=1
- [T1] duplicate split m=2 q=1/16: Pg=g exactly for a=2
- [T1] duplicate split m=2 q=1/16: Pg=g exactly for a=4
- [T1] duplicate split m=2 q=1/16: Pg=g exactly for a=5
- [T1] duplicate split m=2 q=1/16: Pg=g exactly for a=6
- [T1] rank5 genuine self: P^2=P and P1=1
- [T1] rank5 genuine self: 0 < delta <= 1/4
- [T1] rank5 genuine self: W(P) is nonempty
- [T1] rank5 genuine self: exact dist_1 to conv(W) for every row
- [T1] rank5 genuine self: Pg=g exactly for a=1/4
- [T1] rank5 genuine self: Pg=g exactly for a=1
- [T1] rank5 genuine self: Pg=g exactly for a=2
- [T1] rank5 genuine self: Pg=g exactly for a=4
- [T1] rank5 genuine self: Pg=g exactly for a=5
- [T1] rank5 genuine self: Pg=g exactly for a=6
- [T1] rank5 genuine self: delta matches banked value
- [T1] rank5 genuine self: W=(0,1,2,3,4)
- [T1] rank5 genuine self: G_{1/4}=(5)
- [T1] rank5 genuine self: hidden self g=5991/80000 at a=1/4
- [T1] web-regime headline H/delta witness: P^2=P and P1=1
- [T1] web-regime headline H/delta witness: 0 < delta <= 1/4
- [T1] web-regime headline H/delta witness: W(P) is nonempty
- [T1] web-regime headline H/delta witness: exact dist_1 to conv(W) for every row
- [T1] web-regime headline H/delta witness: Pg=g exactly for a=1/4
- [T1] web-regime headline H/delta witness: Pg=g exactly for a=1
- [T1] web-regime headline H/delta witness: Pg=g exactly for a=2
- [T1] web-regime headline H/delta witness: Pg=g exactly for a=4
- [T1] web-regime headline H/delta witness: Pg=g exactly for a=5
- [T1] web-regime headline H/delta witness: Pg=g exactly for a=6
- [T1] web-regime headline: delta=49/2000
- [T1] web-regime headline: H=1/20
- [T1] relaxed cycle LP: exact optimum exists
- [T1] relaxed cycle LP: designated positive mass is 5/4
- [T1] relaxed cycle LP absorption: P^2=P and P1=1
- [T1] relaxed cycle LP absorption: 0 < delta <= 1/4
- [T1] relaxed cycle LP absorption: W(P) is nonempty
- [T1] relaxed cycle LP absorption: exact dist_1 to conv(W) for every row
- [T1] relaxed cycle LP absorption: Pg=g exactly for a=1/4
- [T1] relaxed cycle LP absorption: Pg=g exactly for a=1
- [T1] relaxed cycle LP absorption: Pg=g exactly for a=2
- [T1] relaxed cycle LP absorption: Pg=g exactly for a=4
- [T1] relaxed cycle LP absorption: Pg=g exactly for a=5
- [T1] relaxed cycle LP absorption: Pg=g exactly for a=6
- [T1] relaxed cycle LP absorption: exact geometry has no hidden vertices
- [T1] duplicate scan p=1/200 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/200 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/200 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/200 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/200 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/200 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/200 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/200 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/200 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/200 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/200 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/200 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/200 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/200 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/200 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/200 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/200 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/200 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/200 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/200 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/200 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/200 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/200 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/200 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/200 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/200 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/200 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/200 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/200 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/200 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/200 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/200 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/200 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/200 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/200 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/200 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/200 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/200 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/200 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/200 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/200 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/200 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/200 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/200 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/200 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/200 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/200 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/200 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/200 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/200 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/200 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/200 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/200 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/200 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/200 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/200 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/200 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/200 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/200 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/200 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/200 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/200 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/200 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/200 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/200 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/200 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/200 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/200 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/200 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/200 q=1/10: Pg=g exactly for a=6
- [T1] duplicate scan p=1/100 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/100 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/100 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/100 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/100 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/100 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/100 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/100 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/100 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/100 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/100 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/100 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/100 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/100 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/100 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/100 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/100 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/100 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/100 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/100 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/100 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/100 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/100 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/100 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/100 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/100 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/100 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/100 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/100 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/100 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/100 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/100 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/100 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/100 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/100 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/100 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/100 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/100 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/100 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/100 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/100 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/100 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/100 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/100 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/100 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/100 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/100 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/100 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/100 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/100 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/100 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/100 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/100 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/100 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/100 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/100 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/100 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/100 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/100 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/100 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/100 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/100 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/100 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/100 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/100 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/100 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/100 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/100 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/100 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/100 q=1/10: Pg=g exactly for a=6
- [T1] duplicate scan p=1/80 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/80 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/80 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/80 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/80 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/80 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/80 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/80 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/80 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/80 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/80 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/80 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/80 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/80 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/80 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/80 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/80 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/80 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/80 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/80 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/80 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/80 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/80 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/80 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/80 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/80 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/80 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/80 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/80 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/80 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/80 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/80 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/80 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/80 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/80 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/80 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/80 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/80 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/80 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/80 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/80 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/80 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/80 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/80 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/80 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/80 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/80 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/80 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/80 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/80 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/80 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/80 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/80 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/80 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/80 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/80 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/80 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/80 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/80 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/80 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/80 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/80 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/80 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/80 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/80 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/80 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/80 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/80 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/80 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/80 q=1/10: Pg=g exactly for a=6
- [T1] duplicate scan p=1/60 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/60 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/60 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/60 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/60 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/60 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/60 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/60 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/60 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/60 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/60 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/60 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/60 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/60 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/60 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/60 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/60 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/60 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/60 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/60 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/60 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/60 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/60 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/60 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/60 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/60 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/60 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/60 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/60 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/60 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/60 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/60 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/60 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/60 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/60 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/60 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/60 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/60 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/60 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/60 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/60 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/60 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/60 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/60 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/60 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/60 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/60 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/60 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/60 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/60 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/60 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/60 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/60 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/60 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/60 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/60 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/60 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/60 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/60 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/60 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/60 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/60 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/60 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/60 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/60 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/60 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/60 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/60 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/60 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/60 q=1/10: Pg=g exactly for a=6
- [T1] duplicate scan p=1/40 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/40 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/40 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/40 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/40 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/40 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/40 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/40 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/40 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/40 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/40 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/40 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/40 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/40 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/40 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/40 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/40 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/40 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/40 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/40 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/40 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/40 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/40 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/40 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/40 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/40 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/40 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/40 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/40 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/40 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/40 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/40 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/40 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/40 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/40 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/40 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/40 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/40 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/40 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/40 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/40 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/40 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/40 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/40 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/40 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/40 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/40 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/40 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/40 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/40 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/40 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/40 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/40 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/40 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/40 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/40 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/40 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/40 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/40 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/40 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/40 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/40 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/40 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/40 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/40 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/40 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/40 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/40 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/40 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/40 q=1/10: Pg=g exactly for a=6
- [T1] duplicate scan p=1/30 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/30 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/30 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/30 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/30 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/30 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/30 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/30 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/30 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/30 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/30 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/30 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/30 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/30 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/30 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/30 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/30 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/30 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/30 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/30 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/30 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/30 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/30 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/30 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/30 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/30 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/30 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/30 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/30 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/30 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/30 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/30 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/30 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/30 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/30 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/30 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/30 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/30 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/30 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/30 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/30 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/30 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/30 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/30 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/30 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/30 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/30 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/30 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/30 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/30 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/30 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/30 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/30 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/30 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/30 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/30 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/30 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/30 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/30 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/30 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/30 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/30 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/30 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/30 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/30 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/30 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/30 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/30 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/30 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/30 q=1/10: Pg=g exactly for a=6
- [T1] duplicate scan p=1/20 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/20 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/20 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/20 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/20 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/20 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/20 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/20 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/20 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/20 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/20 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/20 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/20 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/20 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/20 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/20 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/20 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/20 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/20 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/20 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/20 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/20 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/20 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/20 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/20 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/20 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/20 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/20 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/20 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/20 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/20 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/20 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/20 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/20 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/20 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/20 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/20 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/20 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/20 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/20 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/20 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/20 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/20 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/20 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/20 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/20 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/20 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/20 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/20 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/20 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/20 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/20 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/20 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/20 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/20 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/20 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/20 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/20 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/20 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/20 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/20 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/20 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/20 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/20 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/20 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/20 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/20 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/20 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/20 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/20 q=1/10: Pg=g exactly for a=6
- [T1] duplicate scan p=1/16 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/16 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/16 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/16 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/16 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/16 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/16 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/16 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/16 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/16 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/16 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/16 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/16 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/16 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/16 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/16 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/16 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/16 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/16 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/16 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/16 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/16 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/16 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/16 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/16 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/16 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/16 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/16 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/16 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/16 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/16 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/16 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/16 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/16 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/16 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/16 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/16 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/16 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/16 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/16 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/16 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/16 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/16 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/16 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/16 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/16 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/16 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/16 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/16 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/16 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/16 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/16 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/16 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/16 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/16 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/16 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/16 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/16 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/16 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/16 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/16 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/16 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/16 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/16 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/16 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/16 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/16 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/16 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/16 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/16 q=1/10: Pg=g exactly for a=6
- [T1] duplicate scan p=1/12 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/12 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/12 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/12 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/12 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/12 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/12 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/12 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/12 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/12 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/12 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/12 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/12 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/12 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/12 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/12 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/12 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/12 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/12 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/12 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/12 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/12 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/12 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/12 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/12 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/12 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/12 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/12 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/12 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/12 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/12 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/12 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/12 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/12 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/12 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/12 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/12 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/12 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/12 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/12 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/12 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/12 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/12 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/12 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/12 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/12 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/12 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/12 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/12 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/12 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/12 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/12 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/12 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/12 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/12 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/12 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/12 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/12 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/12 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/12 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/12 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/12 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/12 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/12 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/12 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/12 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/12 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/12 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/12 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/12 q=1/10: Pg=g exactly for a=6
- [T1] duplicate scan p=1/10 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/10 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/10 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/10 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/10 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/10 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/10 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/10 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/10 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/10 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/10 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/10 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/10 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/10 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/10 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/10 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/10 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/10 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/10 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/10 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/10 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/10 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/10 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/10 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/10 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/10 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/10 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/10 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/10 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/10 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/10 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/10 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/10 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/10 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/10 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/10 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/10 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/10 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/10 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/10 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/10 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/10 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/10 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/10 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/10 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/10 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/10 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/10 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/10 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/10 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/10 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/10 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/10 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/10 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/10 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/10 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/10 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/10 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/10 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/10 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/10 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/10 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/10 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/10 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/10 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/10 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/10 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/10 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/10 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/10 q=1/10: Pg=g exactly for a=6
- [T1] duplicate scan p=1/8 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/8 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/8 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/8 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/8 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/8 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/8 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/8 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/8 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/8 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/8 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/8 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/8 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/8 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/8 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/8 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/8 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/8 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/8 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/8 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/8 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/8 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/8 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/8 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/8 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/8 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/8 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/8 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/8 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/8 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/8 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/8 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/8 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/8 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/8 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/8 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/8 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/8 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/8 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/8 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/8 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/8 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/8 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/8 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/8 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/8 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/8 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/8 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/8 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/8 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/8 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/8 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/8 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/8 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/8 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/8 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/8 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/8 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/8 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/8 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/8 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/8 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/8 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/8 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/8 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/8 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/8 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/8 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/8 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/8 q=1/10: Pg=g exactly for a=6
- [T1] duplicate scan p=1/6 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/6 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/6 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/6 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/6 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/6 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/6 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/6 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/6 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/6 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/6 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/6 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/6 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/6 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/6 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/6 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/6 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/6 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/6 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/6 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/6 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/6 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/6 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/6 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/6 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/6 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/6 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/6 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/6 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/6 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/6 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/6 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/6 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/6 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/6 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/6 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/6 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/6 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/6 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/6 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/6 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/6 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/6 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/6 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/6 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/6 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/6 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/6 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/6 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/6 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/6 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/6 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/6 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/6 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/6 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/6 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/6 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/6 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/6 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/6 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/6 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/6 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/6 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/6 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/6 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/6 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/6 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/6 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/6 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/6 q=1/10: Pg=g exactly for a=6
- [T1] duplicate scan p=1/5 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/5 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/5 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/5 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/5 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/5 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/5 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/5 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/5 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/5 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/5 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/5 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/5 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/5 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/5 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/5 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/5 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/5 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/5 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/5 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/5 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/5 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/5 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/5 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/5 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/5 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/5 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/5 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/5 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/5 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/5 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/5 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/5 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/5 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/5 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/5 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/5 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/5 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/5 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/5 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/5 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/5 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/5 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/5 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/5 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/5 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/5 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/5 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/5 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/5 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/5 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/5 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/5 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/5 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/5 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/5 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/5 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/5 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/5 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/5 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/5 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/5 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/5 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/5 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/5 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/5 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/5 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/5 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/5 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/5 q=1/10: Pg=g exactly for a=6
- [T1] duplicate scan p=1/4 q=1/1000: P^2=P and P1=1
- [T1] duplicate scan p=1/4 q=1/1000: 0 < delta <= 1/4
- [T1] duplicate scan p=1/4 q=1/1000: W(P) is nonempty
- [T1] duplicate scan p=1/4 q=1/1000: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/4 q=1/1000: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/4 q=1/1000: Pg=g exactly for a=1
- [T1] duplicate scan p=1/4 q=1/1000: Pg=g exactly for a=2
- [T1] duplicate scan p=1/4 q=1/1000: Pg=g exactly for a=4
- [T1] duplicate scan p=1/4 q=1/1000: Pg=g exactly for a=5
- [T1] duplicate scan p=1/4 q=1/1000: Pg=g exactly for a=6
- [T1] duplicate scan p=1/4 q=1/500: P^2=P and P1=1
- [T1] duplicate scan p=1/4 q=1/500: 0 < delta <= 1/4
- [T1] duplicate scan p=1/4 q=1/500: W(P) is nonempty
- [T1] duplicate scan p=1/4 q=1/500: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/4 q=1/500: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/4 q=1/500: Pg=g exactly for a=1
- [T1] duplicate scan p=1/4 q=1/500: Pg=g exactly for a=2
- [T1] duplicate scan p=1/4 q=1/500: Pg=g exactly for a=4
- [T1] duplicate scan p=1/4 q=1/500: Pg=g exactly for a=5
- [T1] duplicate scan p=1/4 q=1/500: Pg=g exactly for a=6
- [T1] duplicate scan p=1/4 q=1/200: P^2=P and P1=1
- [T1] duplicate scan p=1/4 q=1/200: 0 < delta <= 1/4
- [T1] duplicate scan p=1/4 q=1/200: W(P) is nonempty
- [T1] duplicate scan p=1/4 q=1/200: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/4 q=1/200: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/4 q=1/200: Pg=g exactly for a=1
- [T1] duplicate scan p=1/4 q=1/200: Pg=g exactly for a=2
- [T1] duplicate scan p=1/4 q=1/200: Pg=g exactly for a=4
- [T1] duplicate scan p=1/4 q=1/200: Pg=g exactly for a=5
- [T1] duplicate scan p=1/4 q=1/200: Pg=g exactly for a=6
- [T1] duplicate scan p=1/4 q=1/100: P^2=P and P1=1
- [T1] duplicate scan p=1/4 q=1/100: 0 < delta <= 1/4
- [T1] duplicate scan p=1/4 q=1/100: W(P) is nonempty
- [T1] duplicate scan p=1/4 q=1/100: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/4 q=1/100: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/4 q=1/100: Pg=g exactly for a=1
- [T1] duplicate scan p=1/4 q=1/100: Pg=g exactly for a=2
- [T1] duplicate scan p=1/4 q=1/100: Pg=g exactly for a=4
- [T1] duplicate scan p=1/4 q=1/100: Pg=g exactly for a=5
- [T1] duplicate scan p=1/4 q=1/100: Pg=g exactly for a=6
- [T1] duplicate scan p=1/4 q=1/50: P^2=P and P1=1
- [T1] duplicate scan p=1/4 q=1/50: 0 < delta <= 1/4
- [T1] duplicate scan p=1/4 q=1/50: W(P) is nonempty
- [T1] duplicate scan p=1/4 q=1/50: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/4 q=1/50: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/4 q=1/50: Pg=g exactly for a=1
- [T1] duplicate scan p=1/4 q=1/50: Pg=g exactly for a=2
- [T1] duplicate scan p=1/4 q=1/50: Pg=g exactly for a=4
- [T1] duplicate scan p=1/4 q=1/50: Pg=g exactly for a=5
- [T1] duplicate scan p=1/4 q=1/50: Pg=g exactly for a=6
- [T1] duplicate scan p=1/4 q=1/25: P^2=P and P1=1
- [T1] duplicate scan p=1/4 q=1/25: 0 < delta <= 1/4
- [T1] duplicate scan p=1/4 q=1/25: W(P) is nonempty
- [T1] duplicate scan p=1/4 q=1/25: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/4 q=1/25: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/4 q=1/25: Pg=g exactly for a=1
- [T1] duplicate scan p=1/4 q=1/25: Pg=g exactly for a=2
- [T1] duplicate scan p=1/4 q=1/25: Pg=g exactly for a=4
- [T1] duplicate scan p=1/4 q=1/25: Pg=g exactly for a=5
- [T1] duplicate scan p=1/4 q=1/25: Pg=g exactly for a=6
- [T1] duplicate scan p=1/4 q=1/10: P^2=P and P1=1
- [T1] duplicate scan p=1/4 q=1/10: 0 < delta <= 1/4
- [T1] duplicate scan p=1/4 q=1/10: W(P) is nonempty
- [T1] duplicate scan p=1/4 q=1/10: exact dist_1 to conv(W) for every row
- [T1] duplicate scan p=1/4 q=1/10: Pg=g exactly for a=1/4
- [T1] duplicate scan p=1/4 q=1/10: Pg=g exactly for a=1
- [T1] duplicate scan p=1/4 q=1/10: Pg=g exactly for a=2
- [T1] duplicate scan p=1/4 q=1/10: Pg=g exactly for a=4
- [T1] duplicate scan p=1/4 q=1/10: Pg=g exactly for a=5
- [T1] duplicate scan p=1/4 q=1/10: Pg=g exactly for a=6
- [T1] duplicate family scan: at least one under-cap exact candidate checked
- [T1] duplicate split m=4 q=5/84: delta=1/16
- [T1] duplicate split m=4 q=5/84: band g=5/84 at a=1/4
- [T1] duplicate split q=1/16: recipients absorbed into W
- [T1] clone-consistency rank3 partner row4 split 1:2: P^2=P and P1=1
- [T1] clone-consistency rank3 partner row4 split 1:2: 0 < delta <= 1/4
- [T1] clone-consistency rank3 partner row4 split 1:2: W(P) is nonempty
- [T1] clone-consistency rank3 partner row4 split 1:2: exact dist_1 to conv(W) for every row
- [T1] clone-consistency rank3 partner row4 split 1:2: Pg=g exactly for a=1/4
- [T1] clone-consistency rank3 partner row4 split 1:2: Pg=g exactly for a=1
- [T1] clone-consistency rank3 partner row4 split 1:2: Pg=g exactly for a=2
- [T1] clone-consistency rank3 partner row4 split 1:2: Pg=g exactly for a=4
- [T1] clone-consistency rank3 partner row4 split 1:2: Pg=g exactly for a=5
- [T1] clone-consistency rank3 partner row4 split 1:2: Pg=g exactly for a=6
- [T1] clone consistency: cloned strict-halo fiber is transported
- [T1] clone consistency: old rows 0..3 keep the same g values
- [T1] clone consistency: cloned rows inherit old g
- [T1] clone consistency: delta unchanged
- [T1] frontier: no tested a in {4,5,6} has positive visible g
- [T1] frontier: no tested a in {4,5,6} has positive non-W band g

