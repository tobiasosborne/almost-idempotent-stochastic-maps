<!--
ROLE: independent exploration wave for arm G wave 10: decide the (G)
collateral branch of (PRT) — construct or prove empty.
STATUS: exploration/decision note. Nothing below proves (EX), conj-kernel,
conj-degenerate-transport, or op-classical under repo L0.
worker: codex
arm: G wave 10
answers: bd aism-93m
Tier legend: T0 = exact repo-file fact or exact Fraction arithmetic in this
wave; T1 = elementary derivation from T0/validated inputs; T2 = plausible
target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch checker: /tmp/aism_g10_prt.py, pure fractions.Fraction arithmetic;
no checker output file was written to the repo.
Verdict: (G) remains OPEN. No delta<=1/4 certified instance was found.
An exact local Gamma-blocked pattern was found with full argmin enumeration,
but it has delta(P)=49/60 and is therefore tooling only, not a decider.
A T1 collateral-import inequality was derived; it charges Gamma rise to a
transverse import term, but that term is not yet bounded by the PRT budget.
(PRT), (SC), and (RH) therefore remain OPEN.
-->

# Arm G Wave 10: Gamma-Collateral Branch

No `fr` or `bd` command was run. No existing repo file was edited. The scratch
checker rebuilt `P=L B`, asserted `B L=I_3`, `P^2=P`, row sums `1`, computed
`delta(P)`, enumerated all theta-half actual-row charts, and computed every
displayed fraction below. [T0]

Rows are indexed as `(c0,c1,c2,j,k,...)`, with base chart
`U=(c0,c1,c2)` and pivot `s=c2`.

## Task 1: Construction Attempts

### Certified capped `(G)` instance

None found. This is not an emptiness theorem. [T0/T2]

The exact search used two targeted templates:

```text
two-B-row template:
  j=(1/2+h, -(1/2-h), 1-2h)
  k=(-a, 1+a-z, z)

three-B-row template:
  same j,k plus one high-pivot financier l, e.g. (0,-eps,1+eps)
  or (-eps,0,1+eps)
```

The search forced `P_jj=1-kappa` by solving one left-inverse entry exactly,
then sampled rational columns for the collateral and financier rows. Every
candidate that survived the preliminary filters was checked by complete
Fraction enumeration. No sampled candidate satisfied all of:

```text
delta(P) <= 1/4,
U theta-half Phi-argmin,
j beta-positive non-fan high-self,
V_j theta-half admissible,
Psi_j < M <= Gamma_j.
```

This finite randomized rational sweep is evidence only, not infeasibility.
[T0/T2]

### Exact local `(G)` tooling witness, rejected by `delta`

The following exact instance has the desired local branch pattern and complete
theta-half argmin certification, but it violates the row-negative cap. It is
therefore not a certified `(G)` instance. [T0]

```text
L =
[ 1    0     0   ]
[ 0    1     0   ]
[ 0    0     1   ]
[ 3/5 -2/5   4/5 ]
[-1/5  4/5   2/5 ]

B =
[  2/5    13/30  -23/30   59/60  -1/20 ]
[ 23/100  12/25   -3/50   -1/5   11/20 ]
[ -3/20   -1/5     1/2     2/5    9/20 ]
```

Thus `P=L B` is:

```text
[  2/5    13/30  -23/30   59/60  -1/20 ]
[ 23/100  12/25   -3/50   -1/5   11/20 ]
[ -3/20   -1/5     1/2     2/5    9/20 ]
[  7/250 -23/250  -9/250  99/100 11/100]
[ 11/250 163/750 229/750 -59/300 63/100]
```

Exact checks:

```text
P^2=P,            P*1=1,          rank(P)=3,
delta(P)=49/60 > 1/4.
```

The tested row is

```text
j=(3/5,-2/5,4/5),       beta_j=2/5,
P_jj=99/100,            kappa_j=1/100 < 1/2,
W_j=2/5,                nu_j=16/125.
```

It is an active non-fan orphan in the G5/G6 taxonomy: the positive transverse
coordinate `3/5` is strict legal, the negative coordinate `-2/5` is
sub-threshold, and

```text
E_s(j)=1/5>0.
```

Complete theta-half enumeration:

| chart | volume | Phi vector | max Phi |
|---|---:|---:|---:|
| `(c0,c1,c2)` | `1` | `(0,0,2/25)` | `2/25` |
| `(c0,j,k)` | `4/5` | `(0,0,163/1500)` | `163/1500` |
| `(c0,c2,k)` | `4/5` | `(0,1/5,163/1000)` | `1/5` |
| `(c1,c2,j)` | `3/5` | `(23/100,0,7/125)` | `23/100` |
| `(c0,c1,j)` | `4/5` | `(0,11/40,0)` | `11/40` |

So `U` is the theta-half Phi-argmin, with

```text
M = Phi_s(U)=2/25.
```

The pivot-removing chart is `V_j=(c0,c1,j)`, volume `4/5`, hence
theta-half admissible. Its branch values are

```text
Psi_j   = 0       < M=2/25,
Gamma_j = 11/40  > M=2/25.
```

This is exactly the requested `(G)` sign pattern, but only outside the cap.
The cap failure is severe: row `c0` alone has negative mass

```text
23/30 + 1/20 = 49/60.
```

Budget terms for this rejected witness:

```text
G_class^- = 7/20
S_-^mu    = 0
SIGMA     = 1397/10000
FanRes    = 0
denom     = 4897/10000

beta_j W_j = 4/25
ratio      = (4/25)/(4897/10000) = 1600/4897.
```

### Other failed exact designs

The direct “G9 active orphan plus collateral row” template with

```text
j=(3/5,-2/5,4/5),       k=(-2/5,1,2/5)
```

does create transverse collateral. For example one checkpoint has

```text
delta(P)=133/300,
M=1/12,
Psi_j=479/1500 > M,
Gamma_j=13/100 > M.
```

It fails both the cap and the clean `(G)` sign, since the new-pivot score
remains high. [T0]

Forcing `j` to be very high-self can make `Psi_j` small, but in the tested
two-B-row grids the same move pushed large negative mass into chart columns.
The exact local witness above is the cleanest endpoint of that mechanism:
`Psi_j=0` and `Gamma_j>M`, but `delta(P)>1/4`. [T0/T2]

## Task 2: Amplification Probe

No capped `(G)` instance was realized, so no certified amplification family
was probed. The rejected local witness has ratio `1600/4897`, but because
`delta(P)=49/60`, it is tooling only and gives no `(PRT)` stress value. [T0]

## Task 3: Emptiness-Lemma Attempt

No T1 proof of emptiness was obtained. The useful T1 output is a precise
collateral-import inequality. [T1]

Fix a pivot-removing move with `c=a_s(j)>0`, transverse collateral pivot
`r != s`, and let `t` be the other transverse coordinate. Write
`d_q=a_q(j)`. From the validated Schur formulas,

```text
a_s^j(i)=a_s(i)/c,
a_t^j(i)=a_t(i)-a_s(i)d_t/c,
a_r^j(i)=a_r(i)-a_s(i)d_r/c.
```

For every actual row `i`,

```text
E_r^j(i)
 <= E_r(i) + R_{r,j}(i)_+,
```

where

```text
R_{r,j}(i)
 = (1/c - 1) a_s(i)^-
   + (a_s(i)d_t/c)^+
   - a_s(i)d_r/c.
```

Proof: expand the definition of `E_r^j`; use
`(-x+y)^+ <= x^- + y^+`; then use `(X+Y)^+ <= X^+ + Y^+`.
This uses only the validated transform and elementary positive-part
inequalities. [T1]

Multiplying by the unchanged transverse beta row gives

```text
Phi_r(V_j)
 <= Phi_r(U) + I_{r,j},

I_{r,j} := sum_i P_{u_r i}^+ R_{r,j}(i)_+.
```

Therefore any clean Gamma branch on pivot `r` forces

```text
M - Phi_r(U) <= I_{r,j}.                         (CI)
```

This is the exact import that must be charged to
`G_class^- + S_-^mu + SIGMA + FanRes` to close `(G)`. I could not prove that
charge. [T1/T2]

In the rejected local witness, the collateral pivot is `r=1`, the other
transverse coordinate is `t=0`, and

```text
c=4/5,       d_t=3/5,       d_r=-2/5.
```

The only effective import is the collateral row `k`, and

```text
I_{1,j} = (11/20) * (5/4) * (2/5) = 11/40.
```

This equals the observed collateral score:

```text
Phi_1(V_j)=11/40.
```

So the inequality is sharp on the local model, but sharpness occurs outside
the cap. The live gap is exactly whether a capped argmin can carry such an
import without paying it through the existing budget terms. [T1/T2]

## Verdict

```text
(G) branch:  OPEN (narrowed: local Gamma-only blockers exist exactly, but
             the found one has delta(P)=49/60; no capped certified instance)
(PRT):       OPEN (needs a budget charge for the collateral import I_{r,j},
             or a cap-level emptiness proof)
(SC)/(RH):   OPEN / still blocked on PRT
```

Nothing here proves or refutes `(EX)`, `conj-kernel`,
`conj-degenerate-transport`, or `op-classical`.