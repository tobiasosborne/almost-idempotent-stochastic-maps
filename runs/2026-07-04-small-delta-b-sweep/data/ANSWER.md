# Exact-rational small/mid-delta B-decider

Status: L3 numerical evidence only; not a proof.

## Headline

Max certified `B/delta` observed with `delta < 3/20` is `8400000/10897843` at `delta=55319/1000000` (compensated-insert).

The maximizing mass is on `U=(0, 2, 4)`, `s=2`, `r=1` with `B=42/985` and `C=0`.

Calibration assert: the G12 instance recomputes `delta=1/4`, `B=2/57`, `B/delta=8/57`.

## Full Maximizing Instance

Family: `compensated-insert`

`L`:

```text
[1  0  0]
[0  1  0]
[0  0  1]
[2/25  -3/50  49/50]
[1/25  197/200  -1/40]
[-1/100  51/100  1/2]
```

`B`:

```text
[1  0  0  0  0  0]
[-1/50  203/400  1/80  0  1/2  0]
[-55319/1000000  7269/1000000  5599/20000  7/10  0  681/10000]
```

`P=L B`:

```text
[1  0  0  0  0  0]
[-1/50  203/400  1/80  0  1/2  0]
[-55319/1000000  7269/1000000  5599/20000  7/10  0  681/10000]
[1349369/50000000  -1166319/50000000  273601/1000000  343/500  -3/100  33369/500000]
[867319/40000000  19988231/40000000  4251/800000  -7/400  197/400  -681/400000]
[-95719/2000000  524919/2000000  2927/20000  7/20  51/200  681/20000]
```

## Certified Argmins and Branches

- `insert-y=681/10000`: delta `55319/1000000`, best B/delta `8400000/10897843`, clean Gamma `True`.
  Argmin `U=(0, 2, 4)`, volume `197/200`, m `197/200`, phi `('0', '679/24625', '219870541/7880000000')`.
  Branch row `1`: type `Gamma`, clean `True`, self `203/400`, beta_s `19988231/40000000`, E_s `11/197`, Psi `1/200`, Gamma `7/250`.
- `insert-y=17/250`: delta `1383/25000`, best B/delta `70000/90817`, clean Gamma `True`.
  Argmin `U=(0, 2, 4)`, volume `197/200`, m `197/200`, phi `('0', '679/24625', '10993499/394000000')`.
  Branch row `1`: type `Gamma`, clean `True`, self `203/400`, beta_s `999409/2000000`, E_s `11/197`, Psi `1/200`, Gamma `7/250`.
- `insert-y=1/20`: delta `111/2000`, best B/delta `5600/7289`, clean Gamma `True`.
  Argmin `U=(0, 2, 4)`, volume `197/200`, m `197/200`, phi `('0', '679/24625', '219769/7880000')`.
  Branch row `1`: type `Gamma`, clean `True`, self `203/400`, beta_s `19979/40000`, E_s `11/197`, Psi `1/200`, Gamma `7/250`.
- `insert-y=3/100`: delta `557/10000`, best B/delta `84000/109729`, clean Gamma `True`.
  Argmin `U=(0, 2, 4)`, volume `197/200`, m `197/200`, phi `('0', '679/24625', '274571/9850000')`.
  Branch row `1`: type `Gamma`, clean `True`, self `203/400`, beta_s `24961/50000`, E_s `11/197`, Psi `1/200`, Gamma `7/250`.
- `insert-y=1/100`: delta `559/10000`, best B/delta `84000/110123`, clean Gamma `True`.
  Argmin `U=(0, 2, 4)`, volume `197/200`, m `197/200`, phi `('0', '679/24625', '1097723/39400000')`.
  Branch row `1`: type `Gamma`, clean `True`, self `203/400`, beta_s `99793/200000`, E_s `11/197`, Psi `1/200`, Gamma `7/250`.
- `two-carrier-A`: delta `7/125`, best B/delta `150/197`, clean Gamma `True`.
  Argmin `U=(0, 2, 4)`, volume `197/200`, m `197/200`, phi `('0', '679/24625', '438977/15760000')`.
  Branch row `1`: type `Gamma`, clean `True`, self `203/400`, beta_s `39907/80000`, E_s `11/197`, Psi `1/200`, Gamma `7/250`.
- `two-carrier-B`: delta `99/1250`, best B/delta `25/33`, clean Gamma `True`.
  Argmin `U=(0, 2, 4)`, volume `99/100`, m `99/100`, phi `('0', '24/625', '1951/50000')`.
  Branch row `1`: type `Gamma`, clean `True`, self `3911/5000`, beta_s `193149/250000`, E_s `5/99`, Psi `11/2500`, Gamma `99/2500`.
- `two-carrier-C`: delta `21/250`, best B/delta `2000/2779`, clean Gamma `True`.
  Argmin `U=(0, 2, 4)`, volume `397/400`, m `397/400`, phi `('0', '3423/99250', '111634177/3176000000')`.
  Branch row `1`: type `Gamma`, clean `True`, self `14839/20000`, beta_s `5875483/8000000`, E_s `19/397`, Psi `13/2000`, Gamma `9/250`.
- `two-carrier-D`: delta `71/625`, best B/delta `25/36`, clean Gamma `True`.
  Argmin `U=(0, 2, 4)`, volume `99/100`, m `99/100`, phi `('0', '923/22500', '12737/300000')`.
  Branch row `1`: type `Gamma`, clean `True`, self `1703/2000`, beta_s `420321/500000`, E_s `5/99`, Psi `3/1000`, Gamma `213/5000`.

The complete machine-readable list is in `certified_points.json`; row-level masses are in `certified_points.csv`.

## Amplification Attempts and Obstructions

- Non-argmin amplifier eps `1/100`: base-chart delta `99/14900`, B/delta `50`, but theta-half argmin switches to `U=(0, 2, 3)` with Phi `0` while base Phi is `9801/14900`.
- Non-argmin amplifier eps `1/50`: base-chart delta `49/3700`, B/delta `25`, but theta-half argmin switches to `U=(0, 2, 3)` with Phi `0` while base Phi is `2401/3700`.
- Non-argmin amplifier eps `1/20`: base-chart delta `19/580`, B/delta `10`, but theta-half argmin switches to `U=(0, 2, 3)` with Phi `0` while base Phi is `361/580`.
- `insert-y=685/10000` (compensated-insert): delta `11063/200000`, argmins `[(0, 1, 3)]`; obstruction: argmin `(0, 1, 3)` branch row `2` is `Psi`, high-self `False`.
- `two-carrier-more-v` (two-carrier): delta `9/125`, argmins `[(0, 1, 3)]`; obstruction: argmin `(0, 1, 3)` branch row `2` is `Psi`, high-self `False`.
- `two-carrier-small-p` (two-carrier): delta `3/100`, argmins `[(0, 1, 3)]`; obstruction: argmin `(0, 1, 3)` branch row `2` is `Psi`, high-self `False`.

- Grid amplification inside the two certified families was obstructed by either the theta-half argmin switching away from the designed chart, the branch becoming Psi/mixed instead of Gamma, loss of high-self (`P_jj <= 1/2`), or delta leaving `[1/100,3/20]`.

## Honest Scope

Covered exactly two construction families: a 5-row two-carrier sparse-left-inverse family and a 6-row compensated-insertion family that adds one actual row and preserves `BL=I` by identity-column compensation. Both enumerate all actual-row charts for each retained instance; the maximizing 6-row records enumerate 20 charts.

The retained points and obstruction probes are the finite rational parameter list encoded in `decider_small_delta.py` (including the inserted-weight boundary near `681/10000`). This is not an exhaustive search over rank-3 idempotents or over all support patterns.
