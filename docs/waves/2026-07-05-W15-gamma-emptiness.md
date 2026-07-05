<!--
WAVE: arm G wave 15 (conj-gamma-emptiness prove-or-refute) — 2026-07-05, session 8, bd aism-3x7.
WORKER: fresh codex exec (prompt: session scratchpad PROMPT-w15-gamma-emptiness.md). Answer VERBATIM below.
ORCHESTRATOR: worker script rerun clean (exit 0); **headline refutation independently recomputed
  with orchestrator-authored code** (runs/2026-07-05-gamma-emptiness-refuter/scripts/
  orch_verify_refuter.py — rebuilds P from L,B and re-derives everything): CONFIRMED.
  conj-gamma-emptiness is DISPROVED; shard flipped; the run bundle is the death certificate.
KEY SCOPING GAINS (orchestrator): (1) G11's 0/352 was search coverage, NOT emptiness evidence;
  (2) the branch-restricted B-lemma's hypothesis class is NONEMPTY for the first time (this
  instance: B/delta ~ 0.7708, and the refuting row is high-self P_11 = 203/400 — a high-self
  clause would not have saved the conjecture); (3) the worker's T1 residual makes the (PRT)
  collateral conclusion an EXPLICIT corollary of B <= K*delta (K_G = 17K + 20 under the box).
  Successor codified per the user-adopted fallback: conj-b-restricted.
TIER: T0 refutation certificate (orchestrator-confirmed); T1 residual inequalities; T0 calibrations.
-->

# Wave 15 Gamma-emptiness Report

Verdict: **REFUTED**. The unqualified capped Gamma-emptiness contract is false by an exact T0 certificate.

Rerun command:

```bash
python3 waves-scratch/w15-gamma-emptiness/gamma_emptiness_cert.py
```

Scratch artifacts:

- `waves-scratch/w15-gamma-emptiness/gamma_emptiness_cert.py`
- `waves-scratch/w15-gamma-emptiness/certificate.json`
- `waves-scratch/w15-gamma-emptiness/REPORT.md`

(Banked copies: `runs/2026-07-05-gamma-emptiness-refuter/`.)

No `fr`, `bd`, or `git` commands were run.

## T0 Refuter

Use coordinate rows `L` and left inverse `B`:

```text
L =
[1, 0, 0]
[0, 1, 0]
[0, 0, 1]
[2/25, -3/50, 49/50]
[1/25, 197/200, -1/40]
[-1/100, 51/100, 1/2]

B =
[1, 0, 0, 0, 0, 0]
[-1/50, 203/400, 1/80, 0, 1/2, 0]
[-55319/1000000, 7269/1000000, 5599/20000, 7/10, 0, 681/10000]
```

The script hard-asserts `B L = I_3`, `P=L B`, `P^2=P`, row sums `1`, and `trace(P)=3`. Thus this is a rank-3 exact signed idempotent.

```text
delta(P) = 55319/1000000 <= 1/4
```

The unique theta-half Phi-argmin is:

```text
U = (0, 2, 4),  m_U = 197/200
Phi(U) = (0, 679/24625, 219870541/7880000000)
M = Phi_2(U) = 219870541/7880000000
```

For non-chart row `j=1` and maximal pivot `s=2`:

```text
a(j) = (-8/197, 5/197, 200/197)
|a_s(j)| m_U = 1
V_j = (0, 2, 1)
Phi(V_j) = (0, 7/250, 1/200)
Psi_j = 1/200
Gamma_j = 7/250
```

Therefore:

```text
Psi_j = 1/200 < 219870541/7880000000 = Phi_s(U) <= 7/250 = Gamma_j
```

Exact margins:

```text
Phi_s(U) - Psi_j = 180470541/7880000000
Gamma_j - Phi_s(U) = 769459/7880000000
```

This is exactly the forbidden clean Gamma-block under `delta <= 1/4`.

## T0 Theta-half Enumeration

The script enumerates all actual-row triples; the complete theta-half list is:

| chart | volume | m | Phi vector | max Phi |
|---|---:|---:|---:|---:|
| `(0, 2, 4)` | `197/200` | `197/200` | `(0, 679/24625, 219870541/7880000000)` | `219870541/7880000000` |
| `(0, 1, 3)` | `49/50` | `49/50` | `(0, 11/2450, 273601/9800000)` | `273601/9800000` |
| `(0, 1, 2)` | `1` | `1` | `(0, 1/200, 7/250)` | `7/250` |
| `(0, 3, 4)` | `4819/5000` | `4819/5000` | `(0, 2188808/75296875, 5736622297/192760000000)` | `5736622297/192760000000` |
| `(0, 3, 5)` | `2649/5000` | `2649/5000` | `(0, 4651217/441500000, 1629659223/1766000000)` | `1629659223/1766000000` |
| `(0, 4, 5)` | `2021/4000` | `2021/4000` | `(0, 579658699/40420000000, 39261793/40420000)` | `39261793/40420000` |
| `(0, 2, 5)` | `51/100` | `51/100` | `(0, 931/8500, 33986577/34000000)` | `33986577/34000000` |
| `(0, 1, 5)` | `1/2` | `1/2` | `(0, 121/4000, 1002487/1000000)` | `1002487/1000000` |

## T1 Proof-side Residual

The proof attempt does not close. For `c>0`, the validated import route gives only:

```text
M - Phi_r(U) <= I_{r,j}
I_{r,j} <= alpha_B B_{r,s} + alpha_A A_{r,s}
A = B + C - D,   C <= 2 delta
```

So the exact residual is:

```text
M - Phi_r(U) <= (alpha_B + alpha_A) B_{r,s} + 2 alpha_A delta
```

Under the theta-half Cramer box, this becomes only:

```text
M - Phi_r(U) <= 17 B_{r,s} + 16 delta
```

For `c<0`, the reviewed equality-form split gives the analogous residual:

```text
M - Phi_r(U) <= (gamma_A + gamma_B) B_{r,s} + 2 gamma_A delta
```

with worst box bound:

```text
M - Phi_r(U) <= 17 B_{r,s} + 20 delta
```

The missing ingredient is still a real bound on `B_{r,s}` or a stronger Gamma-specific obstruction.

On the refuter itself:

```text
r=1, c=200/197, d_r=5/197, d_t=-8/197
alpha_B=13/200, alpha_A=0
B_{1,2}=42/985, C=0, A=42/985, D=0
I=21/9850
M - Phi_r(U)=2590541/7880000000
```

No contradiction is possible from the current inequalities.

## T0 Calibration

The script also reconstructs the requested seed cases:

```text
G10 clean Gamma witness: delta = 49/60 > 1/4
G11 capped near miss: delta = 1/4, but Psi-M = 22/125 > 0
```

## Hard Asserts

- `B L = I_3`
- `P = L B`
- `P^2 = P`
- all row sums equal `1`
- `trace(P)=3`
- exact `delta(P)`
- complete theta-half chart enumeration
- unique argmin and maximal pivot
- pivot-removing coordinates and chart values
- `Psi_j < Phi_s(U) <= Gamma_j`
- cross-pivot cancellation `A=B+C-D`
- `C <= 2 delta`
- literal CI import values
