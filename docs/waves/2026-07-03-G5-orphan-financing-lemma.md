<!--
ROLE: independent exploration wave for arm G wave 5: aggregate
active-orphan-financing lemma, rank-3 cancellation decider.
STATUS: exploration/decision note. Nothing below proves (EX), conj-kernel,
conj-degenerate-transport, or op-classical under repo L0.
worker: codex
arm: G wave 5
answers: bd aism-whs
Tier legend: T0 = exact repo-file fact or exact python3 fractions.Fraction
arithmetic in this wave; T1 = elementary derivation from T0/validated inputs;
T2 = plausible proof target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch checker: /tmp/aism_g5_family.py, pure fractions.Fraction arithmetic;
no checker output file was written to the repo.
Verdict: cancellation AMPLIFIES. The rank-3 aggregate active-orphan-financing
lemma with right side G_class^- + S_-^mu + R_D^nu is REFUTED by an exact
two-B-row family with delta(P)<1/4, unique theta-half Phi-argmin base chart,
two active strict-legal orphans, no fan rows, and
OD/(G_class^-+S_-^mu+R_D^nu)=1/(2h)-2 -> infinity. This does not refute
(EX): the same family has Phi_s(U)/delta(P) -> 1.
-->

# Arm G Wave 5: Orphan Financing Lemma

Read inputs in the requested order: G4, G3, G2, G1, D6, D5, D4, A9, A8, and
the 2026-07-03 entries of `FINDINGS.md`. I did not run `fr` or `bd`, and I
did not edit any existing file. [T0]

## T1. Multi-B-Row Harmonic Identity

Work at the rank-3 chart

```text
c0=(1,0,0),       c1=(0,1,0),       c2=(0,0,1),
```

with pivot `s=c2`. Let the H-M `B` rows be

```text
a(j)=(x_j,y_j,z_j),       x_j+y_j+z_j=1,       j=1,...,k.
```

Writing `L=[I_3; A]`, every left inverse is obtained by choosing a `3 x k`
matrix `D=(d_{rj})` and setting

```text
B_{r,c_t}=1_{r=t} - sum_j d_{rj} a_t(j),
B_{r,j}=d_{rj}.                                      (1)
```

For the pivot beta row

```text
beta_j=d_{2j},       Gamma_t=B_{2,c_t},
```

the exact harmonic sum rules are

```text
Gamma_0 = - sum_j beta_j x_j,
Gamma_1 = - sum_j beta_j y_j,
Gamma_2 = 1 - sum_j beta_j z_j.                       (2)
```

Equivalently, for each transverse coordinate `r=0,1`,

```text
Gamma_r + sum_j beta_j a_r(j) = 0.                    (3)
```

Thus a beta-positive row with positive transverse coordinate pushes the
corresponding `Gamma_r` negative, while a beta-positive row with negative
coordinate pushes it back up and can cancel that financier. This is exact
left-inverse algebra, independent of theta-half selection. [T1]

For an orphan set `O`, put

```text
P_r^O = sum_{j in O} beta_j a_r(j)^+,
N_r^O = sum_{j in O} beta_j a_r(j)^-,
H_r   = sum_{j notin O} beta_j a_r(j).
```

Then (3) is the exact cancellation ledger

```text
P_r^O = N_r^O - H_r - Gamma_r.                         (4)
```

Consequently

```text
P_r^O <= Gamma_r^- + N_r^O + (-H_r)_+.                 (5)
```

Equation (5) is the bookkeeping wall: own orphan negative mass `N_r^O` cancels
class financing before the positive part `Gamma_r^-` is taken. Nothing in
(2)-(5) prevents both transverse financiers from being nearly canceled. [T1]

## T0/T1. Exact Amplifying Family

For `0<h<1/6`, define

```text
p=1/2+h,       e=1/2-h,       q=1-2h,
o0=( p,-e,q),       o1=(-e, p,q).
```

Take `beta_0=beta_1=1/4` and the left inverse (row order
`c0,c1,c2,o0,o1`)

```text
B0 = [ 1 - p/4 - e^2/(4p),  e/2,        -h q/(2p),  1/4,      -e/(4p) ],
B1 = [ e/2,                 1 - p/4 - e^2/(4p), -h q/(2p),
       -e/(4p),             1/4 ],
B2 = [ -h/2,                -h/2,        p,          1/4,       1/4 ].
```

The scratch checker asserted exactly

```text
B L = I_3,       P = L B,       P^2=P,       P 1=1.      (6)
```

The projection rows simplify to

```text
P_c0 = B0,
P_c1 = B1,
P_c2 = [ -h/2, -h/2, p, 1/4, 1/4 ],
P_o0 = [ 1/4+h, -delta, 2 delta, 1/(4p), 0 ],
P_o1 = [ -delta, 1/4+h, 2 delta, 0, 1/(4p) ],
```

where

```text
delta = e(1/4+h)/p.
```

Since

```text
1/4 - delta = h^2/p > 0,
```

the whole family is under the row-negative cap:

```text
delta(P)=delta < 1/4.                                  (7)
```

The class aggregates are

```text
Gamma_0 = Gamma_1 = -h/2,       Gamma_2=p,
G_class^- = h.
```

There are no beta-negative rows and no degenerate rows in this family, so

```text
S_-^mu = 0,       R_D^nu = 0.                           (8)
```

## T0. Theta-Half Argmin Enumeration

The maximum chart volume is `1`, attained by `(c0,c1,c2)`. For `0<h<1/6`,
the theta-half chart family is exactly the following seven charts:

| chart type | volume | max `Phi` |
|---|---:|---:|
| `(c0,c1,c2)` | `1` | `1/4 - 3h/2` |
| `(c0,c1,o0)`, `(c0,c1,o1)` | `q` | `(1/4+h)(1/2+3h)/(1/2+h)` |
| `(c0,c2,o1)`, `(c1,c2,o0)` | `p` | `3 delta` |
| `(c0,o0,o1)`, `(c1,o0,o1)` | `q` | `1/4+h` |

The remaining actual-row charts have volume `<1/2` and are not in
`M_{1/2}`. Since the base-chart maximum is strictly below `1/4`, while every
listed competitor has maximum at least `1/4`, the base chart is the unique
theta-half `Phi`-argmin. Its pivot vector is

```text
Phi(c0,c1,c2) = (0, 0, 1/4 - 3h/2),
```

so `s=c2` is the unique maximal pivot for `0<h<1/6`. [T0/T1]

Exact checkpoints from the checker:

| `h` | `delta(P)` | base max `Phi` | next max `Phi` | `G_class^-` |
|---:|---:|---:|---:|---:|
| `1/10` | `7/30` | `1/10` | `7/20` | `1/10` |
| `1/20` | `27/110` | `7/40` | `3/10` | `1/20` |
| `1/100` | `637/2550` | `47/200` | `13/50` | `1/100` |
| `1/1000` | `125249/501000` | `497/2000` | `251/1000` | `1/1000` |

## T1. Orphan Classification And OD

At the base chart and pivot `s=c2`, the two H-M rows have transverse
coordinates

```text
o0: ( p,-e ),       o1: ( -e,p ).
```

Each row is strict legal through its positive coordinate `p>1/2`, and neither
has a volume-permitted negative coordinate because `e<1/2`. Hence both rows
are active strict-legal orphans; the fan family is empty. [T1]

For each orphan,

```text
mu=e,       E_s = 2e-p = 1/2-3h > 0.
```

The orphan imports cancel before positive parts but here add nothing:

```text
F_L^orph = 0,
```

because the aggregate orphan imports into the two B columns are nonnegative.
Therefore

```text
OD = L_mu^orph + F_L^orph + sum beta_j E_s(j)
   = 2*(1/4)*e + 2*(1/4)*(1/2-3h)
   = 1/2 - 2h.                                         (9)
```

Combining (8) and (9),

```text
OD / (G_class^- + S_-^mu + R_D^nu)
  = (1/2 - 2h)/h
  = 1/(2h) - 2  -> infinity.                           (10)
```

This is an exact amplifying family, not a finite grid. The proposed universal
rank-3 active-orphan-financing lemma is false. [T0/T1]

## T1. Cancellation Mechanism

The two orphans form the exact starving pattern that G4 left open:

```text
sum_j beta_j a_0(j) = (1/4)(p-e) = h/2,
sum_j beta_j a_1(j) = (1/4)(p-e) = h/2.
```

Thus each positive legal coordinate is almost canceled by the other orphan's
sub-threshold negative coordinate, leaving only `Gamma_0=Gamma_1=-h/2`.
The canceling negative coordinate is not fan-financed, because it is
sub-threshold, and its own leak is part of `OD`, not the right-hand budget.
The row-negative cap does not prevent this: the actual row-negative mass is
`delta=1/4-h^2/p`, just below the cap. [T1]

So the structural hope suggested by the killed G4 design is false in the
aggregate: cancellation is not conserved by
`G_class^-+S_-^mu+R_D^nu`. It is paid only by row-negative mass sitting in the
orphan rows themselves, a quantity absent from the proposed orphan budget.
[T1]

## T1/T2. Consequences For The Two-Horn Candidate

The G4 reshaped horn

```text
L_mu + F_L + sum_{active legal orphan j} beta_j E_s(j)
  <= C_fan * sum_{volume-permitted negative (j,t)} w_{j,t} C_s(j,t)
     + C_orph * (G_class^- + S_-^mu + R_D^nu)
```

is false for every finite `C_orph`: in this family the fan term is empty and
the second budget is `h`, while `OD -> 1/2`. [T1]

This is not an (EX) refuter seed. On the same family,

```text
Phi_s(c0,c1,c2) / delta(P)
  = (1/4 - 3h/2) / (1/4 - h^2/p)  -> 1,
```

so the instance lives well inside the plateau-2 evidence. It refutes only the
attempt to pay active orphan leakage from class/signed boundary budget after
fan rows are removed. [T1]

The updated two-horn candidate must add a cancellation-resilient orphan
budget. The smallest visible repair from this family is a row-negative or
global-cap term, for example schematically

```text
OD <= C_orph' * (G_class^- + S_-^mu + R_D^nu
                 + sum_{active orphan j} beta_j nu_j)
```

or a cruder `+ C_delta delta(P)` term. This family forces

```text
C_delta >= 2
```

if `delta(P)` is the added orphan budget, because `OD/delta(P) -> 2`. For the
weighted own-row term `sum beta_j nu_j`, it forces a coefficient at least `4`.
These are lower bounds only, not proofs of either repaired statement. [T2]

## Verdict

Task bits:

```text
cancellation crux:        AMPLIFIES (exact two-orphan family)
rank-3 orphan lemma:      REFUTED for every finite C_orph
fan horn in the family:   empty
budget used by target:    G_class^-+S_-^mu+R_D^nu = h
orphan demand:            OD = 1/2 - 2h
amplification ratio:      1/(2h)-2 -> infinity
EX status:                not refuted; Phi_s/delta -> 1
```

The single smallest missing statement is no longer the G4 aggregate
active-orphan-financing lemma. It is a repaired orphan horn that includes the
row-negative mass created by sub-threshold cancellation, or an equivalent
delta-scale cancellation budget. Nothing here proves (EX), `conj-kernel`,
`conj-degenerate-transport`, or `op-classical` under repo L0. [T1/T2]
