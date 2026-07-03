<!--
ROLE: independent exploration wave for arm G wave 4: orphan-financing
optimizer and active-orphan adversary.
STATUS: exploration/decision note. Nothing below proves (EX), conj-kernel,
conj-degenerate-transport, or op-classical under repo L0.
worker: codex
arm: G wave 4
answers: bd aism-5ua
Tier legend: T0 = exact repo-file fact or exact python3 fractions.Fraction
arithmetic in this wave; T1 = elementary derivation from T0/validated inputs;
T2 = plausible proof target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch checker: temporary inline python3 fractions.Fraction checkers; no
checker output file was written to the repo.
Verdict: the rank-3 one-B-row orphan ratio is bounded with supremum 1,
not attained; G3's 257/1680 point is far from sharp. The cap is the
theta-half legal/orphan volume boundary, with delta active on the extremal
trend, not an argmin switch. The strengthened ACTIVE-row orphan exclusion is
REFUTED by an exact certificate. If active A9 payment is charged to the
orphan horn, the same boundary trend forces C_orph >= 2. No admissible
two-B-row or rank-4 amplification was certified in this wave.
-->

# Arm G Wave 4: Orphan Financing

Read inputs in the requested order: G3, G2, G1, D6, D5, D4, A9, A8, and the
2026-07-03 entries of `FINDINGS.md`. I did not run `fr` or `bd`. [T0]

## T1. One-B-Row Formula

Use G3's chart

```text
c0=(1,0,0), c1=(0,1,0), c2=(0,0,1),
o=(p,-e,q),       q=1-p+e,
```

and write

```text
v=(-p,e,-q,1),       B_r=e_r+alpha_r v.
```

Let

```text
a=alpha_0,       c=alpha_1,       b=alpha_2>0,
x=P_oo=p a - e c + q b.
```

Then

```text
B_2=(-bp, be, 1-bq, b),
P_o=(p(1-x), -e(1-x), q(1-x), x).
```

For pivot `s=c2`, the H-M orphan data are

```text
beta_o=b,      mu_o=e,      lambda_o=p-e,
E_s(o)=(2e-p)_+.
```

The class aggregates are

```text
Gamma_0=-bp,      Gamma_1=be,      Gamma_2=1-bq.
```

Since `delta<=1/4` gives `bp<=1/4`, the active region relevant to the
optimizer has `Gamma_2>0`, hence

```text
G_class^- + S_-^mu + R_D^nu = bp.
```

With one legal B row,

```text
L_mu = be,
F_L  = e(-b x)_+,
rho  = (L_mu+F_L)/(G_class^-+S_-^mu+R_D^nu)
     = (e/p)(1+(-x)_+).                              (1)
```

The row `o` supplies the cap. If `x>=0`, then `rho=e/p<1` because orphan
legality has `p>1/2` and the negative coordinate is not volume-permitted,
`e<=1/2`. If `x<0`, the row-negative cap includes

```text
e(1-x)-x <= 1/4
```

when `q>=0`; if `q<0`, the extra negative `q(1-x)` only strengthens the
bound. Thus `x<0` forces `e<1/4` and (1) is bounded away from `1`. Therefore

```text
rho < 1
```

on every admissible strict one-B-row orphan, and any supremum can only be
approached at the volume boundary `p downarrow 1/2`, `e uparrow 1/2` with
`x>=0`. [T1]

## T0/T1. Supremum Trend

For `0<h<=1/10`, put

```text
p=1/2+h,       e=1/2-h,       q=1-2h,
alpha_0=1/(4q),       alpha_1=-1/4,
alpha_2=(-q^2+9q-6)/(8q^2).
```

Then

```text
x=P_oo=1-1/(4e)=(2q-1)/(2q).
```

The exact checker asserted `B L=I`, `P=L B`, `P^2=P`, row sums `1`, and
`delta(P)=1/4`. The negative-mass cap is active on rows `c0`, `c1`, and `o`;
the beta row is below the cap. The theta-half charts are

```text
(c0,c1,c2),       (c0,c1,o),       (c1,c2,o),
```

and the symbolic sign split on this interval gives the base chart as a
theta-half `Phi`-argmin with slack. Exact checkpoints:

| `h` | `rho=e/p` | `(L_mu+F_L+beta E_s)/(G_class^-)` | base `max Phi` |
|---:|---:|---:|---:|
| `1/10` | `2/3` | `1` | `7/320` |
| `1/20` | `9/11` | `16/11` | `301/4320` |
| `1/100` | `49/51` | `32/17` | `218503/1920800` |
| `1/1000` | `499/501` | `332/167` | `246760003/1992008000` |

Consequently

```text
sup rho = 1,
```

not attained because strict legality requires `p>1/2` while orphan status
requires the negative coordinate not to cross the same threshold. If active
A9 same-pivot payment is added to the orphan demand, the same family has

```text
(L_mu+F_L+beta_o E_s(o))/G_class^-
  = (e + (2e-p))/p
  = 2(1-4h)/(1+2h)  -> 2.
```

Thus the orphan horn constant forced by one-B-row instances is at least `1`
for `L_mu+F_L`, and at least `2` if active A9 payment is charged to the same
class-aggregate horn. [T0/T1]

## T0. Active Orphan Certificate

The `h=1/10` member is the clean refuter of the strengthened active-orphan
exclusion. It has

```text
p=3/5,       e=2/5,       q=4/5,
alpha=(5/16,-1/4,7/64).
```

The exact matrices are

```text
L =
[ 1    0    0 ]
[ 0    1    0 ]
[ 0    0    1 ]
[ 3/5 -2/5  4/5 ]

B =
[ 13/16   1/8    -1/4    5/16 ]
[  3/20   9/10    1/5   -1/4  ]
[ -21/320 7/160  73/80   7/64 ]

P =
[ 13/16   1/8    -1/4    5/16 ]
[  3/20   9/10    1/5   -1/4  ]
[ -21/320 7/160  73/80   7/64 ]
[  3/8   -1/4     1/2    3/8  ]
```

The checker asserted exactly

```text
B L = I_3,       P^2=P,       P 1=1,       delta(P)=1/4.
```

The theta-half family and scores are

| chart | volume | `Phi` vector | max |
|---|---:|---:|---:|
| `(c0,c1,c2)` | `1` | `(0,0,7/320)` | `7/320` |
| `(c0,c1,o)` | `4/5` | `(0,1/20,1/2)` | `1/2` |
| `(c1,c2,o)` | `3/5` | `(3/20,0,3/4)` | `3/4` |

Thus `(c0,c1,c2)` is a theta-half `Phi`-argmin. At pivot `s=c2`,

```text
beta_o=7/64>0,
mu_o=2/5,
lambda_o=1/5,
E_s(o)=1/5>0.
```

The row is strict legal through the positive coordinate `3/5>1/2`, while its
only negative transverse coordinate is `-2/5`, below the strict
volume-permitted threshold. Therefore the strengthened statement

```text
E_s(j)>0  =>  some negative transverse coordinate is volume-permitted
```

is false. [T0/T1]

The full ledger on this certificate is

```text
G_class^- = 21/320,
L_mu      = 7/160,
F_L       = 0,
beta_o E_s(o) = 7/320.
```

So

```text
(L_mu+F_L)/G_class^- = 2/3,
(L_mu+F_L+beta_o E_s(o))/G_class^- = 1.
```

This is an unpaid active orphan only for the negative-coordinate fan; it is
not unfinanced. Its exact financier is the negative class aggregate
`Gamma_0=-21/320`. [T0/T1]

## T0/T2. Beyond One B Row

I probed the obvious amplification attempt: add a second legal row

```text
y=(-3/5,3/5,1)
```

with positive beta chosen to cancel the orphan's negative `Gamma_0`. In the
rank-3 two-B-row left-inverse parameterization, with `gamma_0=gamma_1=0` and
`gamma_2=alpha_2`, the checker still has

```text
B L=I,       P^2=P,       P 1=1,
```

and the base chart remains a theta-half argmin, but the candidate is rejected:

```text
delta(P)=1001/1600 > 1/4.
```

With smaller beta the same template was still rejected before producing an
admissible cancellation. This is only a killed design, not an infeasibility
proof. I did not certify a two-B-row or rank-4 orphan whose residual jumps
above the one-B-row boundary trend. [T0/T2]

## T2. Reshaped Two-Horn Candidate

The active exclusion is dead, so the legal side cannot be only the G1
negative-coordinate fan. The surviving shape is:

```text
L_mu + F_L + sum_{active legal orphan j} beta_j E_s(j)
  <= C_fan * sum_{volume-permitted negative (j,t)} w_{j,t} C_s(j,t)
     + C_orph * (G_class^- + S_-^mu + R_D^nu).
```

Rows with volume-permitted negative coordinates belong to the fan horn. Rows
with no such coordinate, including active orphans, belong to the class/signed
orphan horn. This wave implies

```text
C_orph >= 1        if the orphan horn pays only L_mu+F_L,
C_orph >= 2        if it also pays active A9 terms beta E_s.
```

No new lower bound on `C_fan` was produced here; the G1/G2 certified fan
instances still telescope with constant `1` in the tested cases, but that is
not a theorem. [T0/T2]

The smallest missing statement is therefore an aggregate
**active-orphan-financing lemma**: after fan-matched negative legal rows are
charged to same-pivot Schur collateral, all remaining strict legal orphan
demand, including active `beta E_s` payment and legal imports with
cancellations taken before positive parts, is bounded by a universal constant
times

```text
G_class^- + S_-^mu + R_D^nu.
```

This is strictly smaller than proving (EX) or `conj-degenerate-payment`, and
it is now necessary because active orphans are realized. [T2]

## Verdict

Task bits:

```text
one-B-row orphan ratio:          bounded; sup = 1; not attained
cap mechanism:                   theta-half volume boundary, with delta active
G3 point:                        257/1680, far below the boundary trend
active-orphan exclusion:          REFUTED by exact rank-3 certificate
active orphan has financier:      yes, Gamma_0^- exactly
two-B/rank-4 amplification:       no admissible jump certified; OPEN
reshaped horn lower constants:    C_orph >= 1, or >= 2 with active A9 payment
```

Nothing here proves (EX), `conj-kernel`, `conj-degenerate-transport`, or
`op-classical` under repo L0. [T0/T2]
