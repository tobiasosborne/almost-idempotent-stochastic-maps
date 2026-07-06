NOT-REFUTED-FRONTIER (sup g_w/tau = 0 on the certified a>=4 frontier; small-a frontier: a=1/4, K^2=147/569, K=0.508279)

# W21 Worker D -- Lemma A REFUTE-side exact report

Tier legend: [T0] repo definition or banked exact pipeline; [T1] exact computation hard-asserted by this script; [T2] structured read from these certificates; [T3] heuristic/search intuition.

## Verdict

- [T1] No certified refutation was realized for Lemma A at `a in {4,5,6}`: the certified frontier has `G_a=empty` and hence `sup_{w in W} g_w/tau=0` for those widths.
- [T1] The best small-halo certificate is `a=1/4`, `w=4`, `G={5}`, `g=49/400`, `delta=27881/480000`, so `K^2=147/569` and `K=0.508279`.
- [T2] Binding constraint named: exposedness absorption. In the same one-parameter rank-5 geometry, increasing the tail scale from `lambda=7/5` to `lambda=29/20` makes row 5 visible, so `C_W` absorbs it and every halo set becomes empty.
- [T2] This is not an emptiness theorem. It is a deterministic exact frontier for the constructions certified here, plus an absorption comparison explaining why the attempted high-mass continuation fails.

## Exact Frontier Table

| a | certificate | G_a | best visible w | g_w | K^2=g_w^2/delta | K=g_w/tau | positive far-mass |
|---:|---|---|---:|---:|---:|---:|---:|
| 1/4 | `scaled-rank5-lambda-7/5` | [5] | 4 | 49/400 | 147/569 | 0.508279 | 49/400 |
| 1 | `scaled-rank5-lambda-7/5` | [] | - | 0 | 0 | 0.000000 | 0 |
| 2 | `scaled-rank5-lambda-7/5` | [] | - | 0 | 0 | 0.000000 | 0 |
| 4 | `scaled-rank5-lambda-7/5` | [] | - | 0 | 0 | 0.000000 | 0 |
| 5 | `scaled-rank5-lambda-7/5` | [] | - | 0 | 0 | 0.000000 | 0 |
| 6 | `scaled-rank5-lambda-7/5` | [] | - | 0 | 0 | 0.000000 | 0 |

## Certified Instances

### scaled-rank5-lambda-7/5

- [T1] `delta=27881/480000; W=[0, 1, 2, 3, 4]; H=20760213/244997300; dists=['0', '0', '0', '0', '0', '20760213/244997300']; negs=['8757/160000', '1379/100000', '5257/96000', '973/64000', '27881/480000', '6087071/160000000']; tstars={0: '134/139', 1: '394/417', 2: '751/1251', 3: '415/417', 4: '569/1251', 5: '17/417'}`.
- [T1] `a=1/4`: `G_a=[5]`, best visible row `w=4`, `g=49/400`, `K^2=147/569`, `K=0.508279`, positive far-mass `49/400`.
- [T1] `a=1`: `G_a=[]`, best visible `g=0`.
- [T1] `a=2`: `G_a=[]`, best visible `g=0`.
- [T1] `a=4`: `G_a=[]`, best visible `g=0`.
- [T1] `a=5`: `G_a=[]`, best visible `g=0`.
- [T1] `a=6`: `G_a=[]`, best visible `g=0`.

Full exact matrix `P`:

```python
[
  ["32063/32000", "-483/160000", "-7/320", "21/80000", "-2387/80000", "21/400"],
  ["21/40000", "199839/200000", "-7/1200", "7/100000", "-2387/300000", "7/500"],
  ["21/6400", "-161/32000", "185/192", "7/16000", "-2387/48000", "7/80"],
  ["7/12800", "-161/192000", "-7/1152", "96007/96000", "-2387/288000", "7/480"],
  ["147/32000", "-1127/160000", "-49/960", "49/80000", "223291/240000", "49/400"],
  ["-1074189/32000000", "8235449/160000000", "358063/960000", "-358063/80000000", "122099483/240000000", "41937/400000"]
]
```

### scaled-rank5-lambda-29/20-absorption

- [T1] `delta=115507/1920000; W=[0, 1, 2, 3, 4, 5]; H=0; dists=['0', '0', '0', '0', '0', '0']; negs=['36279/640000', '5713/400000', '21779/384000', '4031/256000', '115507/1920000', '24246437/640000000']; tstars={0: '134/139', 1: '394/417', 2: '751/1251', 3: '415/417', 4: '1', 5: '51/569'}`.
- [T1] `a=1/4`: `G_a=[]`, best visible `g=0`.
- [T1] `a=1`: `G_a=[]`, best visible `g=0`.
- [T1] `a=2`: `G_a=[]`, best visible `g=0`.
- [T1] `a=4`: `G_a=[]`, best visible `g=0`.
- [T1] `a=5`: `G_a=[]`, best visible `g=0`.
- [T1] `a=6`: `G_a=[]`, best visible `g=0`.

Full exact matrix `P`:

```python
[
  ["128261/128000", "-2001/640000", "-29/1280", "87/320000", "-9889/320000", "87/1600"],
  ["87/160000", "799333/800000", "-29/4800", "29/400000", "-9889/1200000", "29/2000"],
  ["87/25600", "-667/128000", "739/768", "29/64000", "-9889/192000", "29/320"],
  ["29/51200", "-667/768000", "-29/4608", "384029/384000", "-9889/1152000", "29/1920"],
  ["609/128000", "-4669/640000", "-203/3840", "203/320000", "890777/960000", "203/1600"],
  ["-4278783/128000000", "32804003/640000000", "1426261/3840000", "-1426261/320000000", "486355001/960000000", "173739/1600000"]
]
```

## Large-Halo Obstruction Read

- [T2] For `a>=4`, any `j in G_a` is `rho`-far from every visible `w`, because `p_w in C_W` and `dist_1(p_j,p_w) >= dist_1(p_j,C_W) > a*tau >= 4*tau = rho`.
- [T2] Thus the intended `delta/kappa=4*tau` exposedness cancellation barrier is exactly the active mechanism to beat. The certified constructions here did not even enter that large-halo regime; before the tail can be enlarged, the recipient is absorbed into `W`.
- [T1] Hard-asserted large-width certified value: `max_{a in {4,5,6}, w in W} g_w = 0` on these matrices.

## Hard Assert List

- [T1] scaled-rank5-lambda-7/5: P^2=P and every row sum is 1
- [T1] scaled-rank5-lambda-7/5: delta(P)>0
- [T1] scaled-rank5-lambda-7/5: delta(P)<=1/4
- [T1] scaled-rank5-lambda-7/5: W(P) is nonempty
- [T1] scaled-rank5-lambda-7/5: row 0 is visible
- [T1] scaled-rank5-lambda-7/5: row 1 is visible
- [T1] scaled-rank5-lambda-7/5: row 2 is visible
- [T1] scaled-rank5-lambda-7/5: row 3 is visible
- [T1] scaled-rank5-lambda-7/5: row 4 is visible
- [T1] scaled-rank5-lambda-7/5: dist_1(row 0, conv W) is LP-certified
- [T1] scaled-rank5-lambda-7/5: dist_1(row 1, conv W) is LP-certified
- [T1] scaled-rank5-lambda-7/5: dist_1(row 2, conv W) is LP-certified
- [T1] scaled-rank5-lambda-7/5: dist_1(row 3, conv W) is LP-certified
- [T1] scaled-rank5-lambda-7/5: dist_1(row 4, conv W) is LP-certified
- [T1] scaled-rank5-lambda-7/5: dist_1(row 5, conv W) is LP-certified
- [T1] scaled-rank5-lambda-29/20-absorption: P^2=P and every row sum is 1
- [T1] scaled-rank5-lambda-29/20-absorption: delta(P)>0
- [T1] scaled-rank5-lambda-29/20-absorption: delta(P)<=1/4
- [T1] scaled-rank5-lambda-29/20-absorption: W(P) is nonempty
- [T1] scaled-rank5-lambda-29/20-absorption: row 0 is visible
- [T1] scaled-rank5-lambda-29/20-absorption: row 1 is visible
- [T1] scaled-rank5-lambda-29/20-absorption: row 2 is visible
- [T1] scaled-rank5-lambda-29/20-absorption: row 3 is visible
- [T1] scaled-rank5-lambda-29/20-absorption: row 4 is visible
- [T1] scaled-rank5-lambda-29/20-absorption: row 5 is visible
- [T1] scaled-rank5-lambda-29/20-absorption: dist_1(row 0, conv W) is LP-certified
- [T1] scaled-rank5-lambda-29/20-absorption: dist_1(row 1, conv W) is LP-certified
- [T1] scaled-rank5-lambda-29/20-absorption: dist_1(row 2, conv W) is LP-certified
- [T1] scaled-rank5-lambda-29/20-absorption: dist_1(row 3, conv W) is LP-certified
- [T1] scaled-rank5-lambda-29/20-absorption: dist_1(row 4, conv W) is LP-certified
- [T1] scaled-rank5-lambda-29/20-absorption: dist_1(row 5, conv W) is LP-certified
- [T1] frontier: delta=27881/480000
- [T1] frontier: W=(0,1,2,3,4)
- [T1] frontier: exact d_5 value
- [T1] frontier: G_{1/4}={5}
- [T1] frontier: best visible row at a=1/4 is w=4
- [T1] frontier: g^{(1/4)}_4=49/400
- [T1] frontier: positive far-mass equals 49/400
- [T1] frontier: d_5<=tau, so G_a is empty for a>=1
- [T1] frontier: G_1 is empty
- [T1] frontier: G_2 is empty
- [T1] frontier: G_4 is empty
- [T1] frontier: G_5 is empty
- [T1] frontier: G_6 is empty
- [T1] absorption: delta=115507/1920000
- [T1] absorption: row 5 is absorbed into W
- [T1] absorption: H=0 after row 5 becomes visible
- [T1] absorption: G_1/4 is empty
- [T1] absorption: G_1 is empty
- [T1] absorption: G_2 is empty
- [T1] absorption: G_4 is empty
- [T1] absorption: G_5 is empty
- [T1] absorption: G_6 is empty
