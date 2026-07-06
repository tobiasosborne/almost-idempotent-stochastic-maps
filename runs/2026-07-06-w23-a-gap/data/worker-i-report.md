OPEN-BOTH-SIDES (prove blocked at: shell S_w inside rho where the visible exposer has no lower bound; refute frontier: no exact family here enters G_{15/4}, and the shallow-corner ansatz is blocked by delta-inflation/exposedness absorption)

# W23 Worker I - A-GAP Route (ii)

Tier legend: [T0] repo definition or established shard; [T1] exact computation by this script; [T2] proof-analysis consequence; [T3] heuristic frontier read.

## Established imports

- [T0] `def-visible-set`: tau = sqrt(delta), rho = 4 tau, kappa = tau/4; W is the set of (rho,kappa)-exposed row vertices.
- [T0] `def-exposed`: an admissible exposer only has a guaranteed lower margin on rows with l1-distance at least rho from the vertex; rows inside the rho-ball are exempt.
- [T0] `lem-visible-g-small`: for a >= 4, visible rows satisfy `-nu_w <= g_w <= 4*tau`; the only use of a >= 4 is `G_a subset {||p_j-p_w||_1 >= rho}`.
- [T0] `obs-height-collapse` and `conj-halo-collapse` are af-validated hidden-top outgoing-mass inequalities; their hypotheses are about a hidden top vertex v and the row v, not incoming mass `P_wj` from a visible row.

## Prove-side attempt

- [T2] For a in (29/8,4), any uncontrolled index for a visible w lies in the annulus `a*tau < ||p_j-p_w||_1 < 4*tau`. The first inequality is just `p_w in C_W`; the second is the definition of the below-rho shell.
- [T2] The original exposer pairing cannot price this annulus. Visibility gives an affine h with `h(p_j) >= kappa` only for rows at distance at least `rho = 4*tau`; the definition gives no positive lower bound for shell rows.
- [T2] Pairing the exposer of w against the reproduction identity of a shell row j controls, at best, how row j sends mass to rho-far rows. It gives no reciprocal or column estimate for the incoming coefficient `P_wj`.
- [T2] The af-validated height-collapse tools do not apply to an arbitrary shell index. If the shell row is non-vertex, it is outside their hypotheses; if it is a hidden vertex but not top, it is still outside their hypotheses; if a hidden top exists, the conclusions concern that top row's own positive mass split, not visible-row load on the shell.
- [T2] The generic convex-distance residual bound is one-sided in the wrong direction for this task: signed reproduction can make the positive barycenter close to `C_W` while individual positive recipients lie outside `C_W`. Without a common separator for the whole shell, it does not yield `sum_{j in S_w} P_wj^+ = O(tau)`.

Conclusion of the proof attempt: I do not have a valid below-4 proof. The missing estimate is exactly an incoming shell-mass cap
`sum_{j: dist(p_j,C_W)>a*tau, ||p_j-p_w||_1<4*tau} P_wj^+ <= C(a)*tau` for visible w.

## Refute-side exact checks

Rerun:

```bash
python3 runs/2026-07-06-w23-a-gap/scripts/w23_worker_i.py
```

### sharp Hume family s=1/100

- [T1] delta = `1/10000`; W = `[1, 2]`; H^2/delta = `0`.
- [T1] G_15/4 = `[]`; visible-row g-values = `{1: '0', 2: '0'}`.
- [T1] row negative masses = `['0', '1/10000', '0']`.
- [T1] dist(row,C_W)^2/delta = `['0', '0', '0']`.

Matrix:

```python
[
  ["99/10000", "980199/1000000", "9901/1000000"],
  ["1/100", "9901/10000", "-1/10000"],
  ["0", "0", "1"]
]
```

### W19 rank-3 genuine-partner anchor

- [T1] delta = `74551/1600000`; W = `[0, 1, 2]`; H^2/delta = `6644487865272110569/31166444486118384000`.
- [T1] G_15/4 = `[]`; visible-row g-values = `{0: '0', 1: '0', 2: '0'}`.
- [T1] row negative masses = `['949/32000', '417/40000', '51/1250', '74551/1600000', '20353/640000']`.
- [T1] dist(row,C_W)^2/delta = `['0', '0', '0', '6644487865272110569/31166444486118384000', '325579905398333417881/3116644448611838400000']`.

Matrix:

```python
[
  ["31023/32000", "43/16000", "-949/32000", "9/200", "1/80"],
  ["-457/80000", "40017/40000", "-377/80000", "1/200", "1/200"],
  ["-51/1250", "303/80000", "76661/80000", "11/160", "1/100"],
  ["23129/50000", "-74551/1600000", "819923/1600000", "961/16000", "23/2000"],
  ["7770491/12800000", "-20353/640000", "4572529/12800000", "17831/320000", "377/32000"]
]
```

### W19 rank-5 genuine-self anchor

- [T1] delta = `3983/96000`; W = `[0, 1, 2, 3, 4]`; H^2/delta = `819309766496688/4725917231967715`.
- [T1] G_15/4 = `[]`; visible-row g-values = `{0: '0', 1: '0', 2: '0', 3: '0', 4: '0'}`.
- [T1] row negative masses = `['1251/32000', '197/20000', '751/19200', '139/12800', '3983/96000', '1258153/32000000']`.
- [T1] dist(row,C_W)^2/delta = `['0', '0', '0', '0', '0', '819309766496688/4725917231967715']`.

Matrix:

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

### W19 duplicate-split m=4, q=5/84

- [T1] delta = `1/16`; W = `[0, 1, 2]`; H^2/delta = `4/25`.
- [T1] G_15/4 = `[]`; visible-row g-values = `{0: '0', 1: '0', 2: '0'}`.
- [T1] row negative masses = `['11/336', '5/168', '1/16', '79/1680', '79/1680', '79/1680', '79/1680']`.
- [T1] dist(row,C_W)^2/delta = `['0', '0', '0', '4/25', '4/25', '4/25', '4/25']`.

Matrix:

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

### failed shallow-corner constant-mass ansatz

- [T1] delta = `1903/1000000`; W = `[1, 2, 3, 4]`; H^2/delta = `0`.
- [T1] G_15/4 = `[]`; visible-row g-values = `{1: '0', 2: '0', 3: '0', 4: '0'}`.
- [T1] row negative masses = `['1/1000000', '0', '0', '1901/1000000', '1903/1000000']`.
- [T1] dist(row,C_W)^2/delta = `['0', '0', '0', '0', '0']`.

Matrix:

```python
[
  ["1/2", "-1/1000000", "1/1000000", "1/4", "1/4"],
  ["0", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["1/2", "-1901/1000000", "1901/1000000", "1/4", "1/4"],
  ["1/2", "1903/1000000", "-1903/1000000", "1/4", "1/4"]
]
```

## Refute-side read

- [T1] The sharp rank-one family, the W19 rank-3/rank-5 anchors, and the duplicate-split family all have `G_{15/4} = empty` under exact visibility and exact l1-distance predicates.
- [T1] The shallow-corner ansatz realizes the desired formal row-0 pattern (constant mass on two near outside coordinate points with only a formal O(delta) correction), but exact row negativity inflates from the target `1/1000000` to `1903/1000000`, and exact visibility makes `G_{15/4}` empty.
- [T2] This identifies the binding refuter constraints: keep actual negative mass at O(epsilon^2), keep row distances to `C_W` at O(epsilon) in the band `(15/4,4)*tau`, and keep the recipient rows out of W while row w places non-O(tau) mass on them.
- [T3] I did not obtain a counterexample or a degradation certificate. This is not an emptiness claim.

## Assert list

- [T1] sharp Hume family s=1/100: P^2=P and P1=1 exactly
- [T1] sharp Hume family s=1/100: 0 < delta <= 1/4
- [T1] sharp Hume family s=1/100: W(P) is nonempty
- [T1] sharp Hume family s=1/100: all distances to C_W computed exactly
- [T1] W19 rank-3 genuine-partner anchor: P^2=P and P1=1 exactly
- [T1] W19 rank-3 genuine-partner anchor: 0 < delta <= 1/4
- [T1] W19 rank-3 genuine-partner anchor: W(P) is nonempty
- [T1] W19 rank-3 genuine-partner anchor: all distances to C_W computed exactly
- [T1] W19 rank-5 genuine-self anchor: P^2=P and P1=1 exactly
- [T1] W19 rank-5 genuine-self anchor: 0 < delta <= 1/4
- [T1] W19 rank-5 genuine-self anchor: W(P) is nonempty
- [T1] W19 rank-5 genuine-self anchor: all distances to C_W computed exactly
- [T1] W19 duplicate-split m=4, q=5/84: P^2=P and P1=1 exactly
- [T1] W19 duplicate-split m=4, q=5/84: 0 < delta <= 1/4
- [T1] W19 duplicate-split m=4, q=5/84: W(P) is nonempty
- [T1] W19 duplicate-split m=4, q=5/84: all distances to C_W computed exactly
- [T1] shallow-corner ansatz: R Lambda = I_3 exactly
- [T1] failed shallow-corner constant-mass ansatz: P^2=P and P1=1 exactly
- [T1] failed shallow-corner constant-mass ansatz: 0 < delta <= 1/4
- [T1] failed shallow-corner constant-mass ansatz: W(P) is nonempty
- [T1] failed shallow-corner constant-mass ansatz: all distances to C_W computed exactly
- [T1] banked exact families tested here have empty G_15/4
- [T1] shallow-corner ansatz: actual delta inflates by more than 100x over the formal target
- [T1] shallow-corner ansatz: G_15/4 is empty after exact visibility analysis

