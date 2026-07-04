<!--
ROLE: independent exploration wave for arm G wave 9: per-branch exact
realizability of the (PRT) blocker branches (V)/(P)/(G).
STATUS: exploration/decision note. Nothing below proves (EX), conj-kernel,
conj-degenerate-transport, or op-classical under repo L0.
worker: codex
arm: G wave 9
answers: bd aism-qkv
Tier legend: T0 = exact repo-file fact or exact python3 fractions.Fraction
arithmetic in this wave; T1 = elementary derivation from T0/validated inputs;
T2 = plausible proof target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch checker: /tmp/aism_g9_branch.py, pure fractions.Fraction arithmetic;
no checker output file was written to the repo.
Verdict: (V) is REALIZED by an exact high-self lambda-positive orphan with
ratio 624/4427, but its old argmin score is M=0. (P) is REALIZED by an exact
high-self active orphan with ratio 240/451 and genuine Psi blocking. (G) was
not certified and is not proved empty; local Gamma-pattern candidates failed
either delta<=1/4 or complete argmin certification. Thus (PRT) remains OPEN;
(SC)/(RH) remain OPEN.
-->

# Arm G Wave 9: Per-Branch Exact Realizability

No `fr` or `bd` command was run. No existing repo file was edited. The scratch
checker rebuilt `P=L B`, asserted `B L=I_3`, `P^2=P`, `P1=1`, enumerated all
theta-half actual-row charts, and computed every displayed fraction below.
[T0]

Rows are ordered `(c0,c1,c2,o)`, with chart `U=(c0,c1,c2)`, pivot
`s=c2`, and tested B-row `j=o`.

## (V) Volume-Inadmissible Branch: REALIZED

This is a lambda-positive orphan: `a(o)=(2/3,-1/10,13/30)`, legal through
the positive transverse coordinate `2/3>1/2`, with negative coordinate
`-1/10` sub-threshold. Hence it is non-fan in the G3/G6 sense. [T1]

```text
L =
[ 1    0      0     ]
[ 0    1      0     ]
[ 0    0      1     ]
[ 2/3 -1/10  13/30 ]

B =
[  8/13   3/52  -1/4    15/26 ]
[  1/6   39/40  13/120  -1/4  ]
[ -1/4    3/80  67/80    3/8  ]

P = L B =
[  8/13    3/52    -1/4    15/26 ]
[  1/6    39/40    13/120  -1/4  ]
[ -1/4     3/80    67/80    3/8  ]
[ 89/312  -89/2080 89/480 119/208]
```

Exact checks:

```text
delta(P) = 1/4,          rank(P)=3,
Phi(U) = (0,0,0),        M=0,
beta_o = 3/8,            P_oo=119/208,
kappa_o = 89/208 < 1/2, W_o=1/10,
nu_o = 89/2080.
```

Complete theta-half enumeration:

| chart | volume | Phi vector | max Phi |
|---|---:|---:|---:|
| `(c0,c1,c2)` | `1` | `(0,0,0)` | `0` |
| `(c1,c2,o)` | `2/3` | `(0,0,2047/6240)` | `2047/6240` |

The pivot-removing chart is `(c0,c1,o)`. Since `vol_max=1` and `m_U=1`,

```text
|a_s(o)| m_U = 13/30 < 1/2,
```

so the branch is exactly (V). This is a score-degenerate realization because
`M=0`; it decides realizability of the volume branch, not stress of the
blocker inequality. [T0]

Budget and ratio:

```text
G_class^- = 1/4
S_-^mu    = 0
SIGMA     = beta_o nu_o = 267/16640
FanRes    = 0
denom     = 4427/16640

beta_o W_o = 3/80
ratio      = (3/80)/(4427/16640) = 624/4427.
```

## (P) Psi-Blocked Branch: REALIZED

This is an active orphan: `a(o)=(3/5,-2/5,4/5)`, legal through
`3/5>1/2`, with negative coordinate `-2/5` sub-threshold and
`E_s(o)=1/5>0`. It is non-fan. [T1]

```text
L =
[ 1    0     0   ]
[ 0    1     0   ]
[ 0    0     1   ]
[ 3/5 -2/5  4/5 ]

B =
[ 13/16  1/8  -1/4  5/16 ]
[  3/20  9/10  1/5 -1/4  ]
[ -1/4   1/6   2/3  5/12 ]

P = L B =
[ 13/16   1/8    -1/4   5/16 ]
[  3/20   9/10    1/5  -1/4  ]
[ -1/4    1/6     2/3   5/12 ]
[ 91/400 -91/600 91/300 149/240]
```

Exact checks:

```text
delta(P) = 1/4,          rank(P)=3,
Phi(U) = (0,0,1/12),     M=1/12,
beta_o = 5/12,           P_oo=149/240,
kappa_o = 91/240 < 1/2, W_o=2/5,
nu_o = 91/600.
```

Complete theta-half enumeration:

| chart | volume | Phi vector | max Phi |
|---|---:|---:|---:|
| `(c0,c1,c2)` | `1` | `(0,0,1/12)` | `1/12` |
| `(c0,c1,o)` | `4/5` | `(0,1/20,91/300)` | `91/300` |
| `(c1,c2,o)` | `3/5` | `(3/20,0,91/200)` | `91/200` |

The pivot-removing chart `(c0,c1,o)` is theta-half admissible. Its branch
values are

```text
Psi_o   = 91/300 >= M=1/12,
Gamma_o = 1/20  <  M.
```

So this is a genuine (P) realization. [T0]

Budget and ratio:

```text
G_class^- = 1/4
S_-^mu    = 0
SIGMA     = beta_o nu_o = 91/1440
FanRes    = 0
denom     = 451/1440

beta_o W_o = 1/6
ratio      = (1/6)/(451/1440) = 240/451.
```

## (G) Gamma-Blocked Branch: OPEN

No certified (G) instance was found. This is not an emptiness theorem. [T0/T2]

Two exact search directions were tested in the scratch checker:

```text
1. one-row active-orphan cap families;
2. G6-style high-self silent rows plus one collateral blocker row.
```

The one-row active-orphan family either stayed (P)-blocked or lost the
argmin when `Psi` was pushed below `M`. The silent-plus-blocker template
produced local Gamma branch patterns, but the candidates failed certification:
either `delta(P)>1/4`, or a different theta-half chart had strictly smaller
max Phi. Failed designs are not infeasibility results. [T0/T2]

No T1 standalone inequality proving (G) empty was obtained.

## Amplification Probe

For the realized (V) family, the tested exact checkpoints used

```text
o_e=(2/3,-e,1/3+e),       0<e<1/6,
alpha=(1/(4(1/3+e)), -1/4, 3/8).
```

Each listed row has complete argmin certification with `Phi(U)=(0,0,0)` and
branch (V). [T0]

| `e` | ratio |
|---:|---:|
| `1/100` | `49440/3314951` |
| `1/20` | `2208/30343` |
| `1/10` | `624/4427` |
| `3/20` | `8352/40765` |

For the realized (P) family, the tested exact checkpoints used

```text
p=1/2+h,       e=1/2-h,       o=(p,-e,1-p+e),
alpha=(1/(4(1-p+e)), -1/4, 1/(4p)).
```

Each listed row has complete argmin certification and branch (P). [T0]

| `h` | ratio |
|---:|---:|
| `1/20` | `7920/12259` |
| `1/16` | `576/937` |
| `1/12` | `1680/2963` |
| `1/10` | `240/451` |
| `1/8` | `480/991` |

No certified ratio-growth family was found. These probes are bounded evidence
only; they do not prove a universal branch constant. [T0/T2]

## Verdict

```text
(V) branch:  REALIZED (ratio 624/4427; score-degenerate M=0)
(P) branch:  REALIZED (ratio 240/451; genuine Psi blocker)
(G) branch:  OPEN (no certified instance; no emptiness proof)
(PRT):       OPEN (narrowed: V/P are real, G remains undecided)
(SC)/(RH):   OPEN / blocked exactly as in G7-G8
```

Nothing here proves or refutes `(EX)`, `conj-kernel`, `(SC)`, `(RH)`,
or `op-classical`.