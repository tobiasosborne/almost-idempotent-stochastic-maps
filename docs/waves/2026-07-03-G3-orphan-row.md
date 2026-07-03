<!--
ROLE: adversarial exploration wave for arm G wave 3: orphan-row decider
against the negative-side legal circulation candidate.
STATUS: exploration/decision note. Nothing below proves (EX), conj-kernel,
conj-degenerate-transport, or op-classical under repo L0.
worker: codex
arm: G wave 3
answers: bd aism-2fh
Tier legend: T0 = exact repo-file fact or exact python3 fractions.Fraction
arithmetic in this wave; T1 = elementary derivation from T0/validated inputs;
T2 = plausible proof target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch checker: /tmp/aism_g3_orphan.py, pure fractions.Fraction arithmetic;
no checker output file was written to the repo.
Verdict: orphan rows REALIZED by an exact rank-3 theta-half Phi-argmin
certificate, refuting the literal G2 implication with hypothesis mu_j>0.
The same certificate REFUTES the rank-3 pure-legal fan-matched inequality with
C_legal=0; its residual is 257/57600 and the standard boundary budget is
G_class^- = 7/240, so this instance forces C_legal >= 257/1680 if that budget
is the repair. It does not refute the strengthened active-row statement with
E_s(j)>0 (equivalently lambda_s(j)<mu_j), which remains OPEN.
-->

# Arm G Wave 3: Orphan Row Decider

Read inputs, in the requested order: G2, G1, D6, A9, A8, D5, D4, and the
2026-07-03 entries of `FINDINGS.md`. I also checked the local factorization
contract for the general definition

```text
E_s(j) = max(mu_s(j) - lambda_s(j), 0).
```

No discrepancy with the displayed D6/G1/G2 arithmetic was found. [T0]

## T0. Minimal One-B-Row Constraint System

Work in rank `3` coordinates with chart representatives

```text
c0=(1,0,0),   c1=(0,1,0),   c2=(0,0,1),
```

and one H-M `B` row

```text
o=(p,-e,1-p+e),       p>1/2,       0<e<=1/2.
```

The relation among the four actual rows is

```text
v=(-p, e, -1+p-e, 1),        sum_i v_i row_i = 0.
```

Thus every left inverse of `L=[c0;c1;c2;o]` has rows

```text
B_r = e_r + alpha_r v,       r=0,1,2.
```

This solves `B L=I_3` identically; hence `P=L B` is an exact idempotent and
row sums are `1` because every coordinate row is affine. The pivot beta at
`s=c2` is `beta_o=alpha_2`. [T1]

The certificate below is the exact specialization

```text
p=7/12,       e=1/12,       alpha=(-1/5,-1/4,1/20).
```

## T0. Exact Certificate

With row order `(c0,c1,c2,o)`,

```text
L =
[ 1      0      0   ]
[ 0      1      0   ]
[ 0      0      1   ]
[ 7/12  -1/12   1/2 ]

B =
[ 67/60   -1/60    1/10   -1/5  ]
[  7/48   47/48    1/8    -1/4  ]
[ -7/240   1/240  39/40    1/20 ]
```

The scratch checker asserted exactly

```text
B L = I_3,       P = L B,       P^2 = P,       P 1 = 1.
```

The resulting projection is

```text
P =
[  67/60    -1/60    1/10    -1/5   ]
[   7/48    47/48    1/8     -1/4   ]
[  -7/240    1/240  39/40     1/20  ]
[ 1799/2880 -257/2880 257/480 -17/240]
```

Row negative masses are

```text
13/60,       1/4,       7/240,       461/2880,
```

so

```text
delta(P)=1/4.
```

There are no zero rows or zero columns, and the three chart rows are singleton
H-M classes. Thus `o` is the unique H-M `B` row in the D1 sense. [T0/T1]

For pivot `s=c2`, the H-M class aggregates are the beta entries of row `c2`:

```text
Gamma_{s,0}=-7/240,     Gamma_{s,1}=1/240,     Gamma_{s,2}=39/40,
beta_o=1/20.
```

They satisfy the H-M harmonic sum rules exactly:

```text
Gamma_{s,0} + beta_o*(7/12)  = 0,
Gamma_{s,1} + beta_o*(-1/12) = 0,
Gamma_{s,2} + beta_o*(1/2)   = 1.
```

## T0. Full Theta-Half Argmin Certificate

The actual-row basis volumes are

```text
(c0,c1,c2): 1,
(c0,c1,o): 1/2,
(c1,c2,o): 7/12,
(c0,c2,o): 1/12.
```

Thus the theta-`1/2` chart family is exactly

```text
(c0,c1,c2),       (c0,c1,o),       (c1,c2,o).
```

Using the repo factorization definition of `Phi`, the exact pivot-score
vectors are

```text
chart (c0,c1,c2):  (0, 0, 0),                  max = 0,
chart (c0,c1,o):   (0, 1/24, 3341/2880),       max = 3341/2880,
chart (c1,c2,o):   (0, 0, 2827/2880),          max = 2827/2880.
```

Therefore `U=(c0,c1,c2)` is the unique theta-half `Phi`-argmin. At this chart
every pivot is maximal because all three pivot scores are `0`; choose
`s=c2`. [T0]

## T1. The Orphan Row Is Real

In the argmin chart `U=(c0,c1,c2)`, the H-M row has coordinates

```text
a(o) = (7/12, -1/12, 1/2).
```

For pivot `s=c2`,

```text
beta_o  = 1/20 > 0,
lambda_o = 1 - a_s(o) = 1/2,
mu_o     = 1/12 > 0,
E_s(o)   = max(mu_o-lambda_o,0) = 0.
```

The row is strict legal in the literal G2/D6 covering sense: replacing the
transverse pivot `c0` by `o` has one-row Schur volume

```text
|a_0(o)| = 7/12 > 1/2.
```

But the only negative transverse coordinate is

```text
a_1(o) = -1/12,
```

whose Schur volume is below the theta-half threshold. Hence there is no
volume-permitted transverse coordinate with `a_t(o)<0`. This is exactly an
orphan row:

```text
beta_o>0,     o notin D_s,     mu_o>0,
```

but no volume-permitted negative coordinate. The target implication from G2 is
therefore false as written. [T1]

Scope caveat: this certificate exploits the lambda-positive regime
`lambda_o>mu_o`, so `E_s(o)=0`. It does **not** refute the strengthened
statement obtained by adding `E_s(j)>0` or `lambda_s(j)=0`. That active-row
or lambda-zero orphan exclusion remains open. [T1/T2]

## T0. Circulation Ledger On The Certificate

For the legal set `L={o}` and H-M `B` block `{o}`,

```text
L_mu = beta_o * mu_o = 1/240.
```

The self-entry of the orphan row is

```text
P_oo = -17/240,
```

so the legal import term is

```text
F_L = mu_o * (- beta_o P_oo)_+
    = (1/12) * (17/4800)
    = 17/57600.
```

Thus the pure legal demand is

```text
L_mu + F_L = 257/57600.
```

The fan-matched negative-coordinate family has no volume-permitted member:
the only negative coordinate is `-1/12`. Therefore

```text
sum_{legal negative (j,t)} w_{j,t} C_s(j,t) = 0.
```

Consequently the rank-3 pure-legal inequality with `C_legal=0`,

```text
L_mu + F_L <= sum w C_s,
```

is refuted by this exact certificate. [T0/T1]

The leak does not amplify without any visible financier. It is paid by the
negative class aggregate forced by the positive legal coordinate:

```text
G_class^- = 7/240,       S_-^mu = 0,       R_D^nu = 0.
```

Relative to the standard boundary budget, this one instance requires

```text
(L_mu+F_L)/(G_class^- + S_-^mu + R_D^nu)
  = (257/57600)/(7/240)
  = 257/1680.
```

The mechanism is therefore a class-aggregate orphan financier, not the
negative-coordinate fan. In this one-row quotient it is transparent:
`Gamma_{s,0}=-beta_o a_0(o)` is negative exactly because the orphan is legal
through the positive coordinate `a_0(o)>1/2`. [T1]

## T2. What Remains Open

The certificate settles the literal orphan implication in the refutation
direction, but it also shows that the original question was slightly too broad
for the intended legal-collateral horn. The row has `mu>0` but no `Phi`
contribution, so no A9 same-pivot `q_j=beta_j E_s(j)` has to be paid.

The smallest surviving active-row variant is:

```text
At a theta-half Phi-argmin with maximal pivot s, if a strict legal H-M B row
j has beta_j>0 and E_s(j)>0, then j has a volume-permitted negative
transverse coordinate.
```

I did not prove or refute this strengthened statement. It is the natural
replacement if arm G wants an orphan-exclusion lemma rather than an
orphan-financing lemma. [T2]

For the circulation route, the smaller missing statement is now an
orphan-financing horn:

```text
sum_{orphan legal j} beta_j mu_j + orphan legal imports
  <= C_orph * (negative class aggregate plus the existing signed-ledger
               boundary terms),
```

with cancellations handled before taking positive parts. The certificate says
such a horn must see positive-coordinate class financing; the negative
fan-matched weights alone cannot see it. [T2]

## Verdict

Task-C bits:

```text
orphan rows:                    REALIZED (exact rank-3 certificate, T0/T1)
literal G2 implication:          REFUTED as written
active E_s>0 orphan exclusion:   OPEN (displayed strengthened statement)
rank-3 pure-legal inequality:    REFUTED for C_legal=0 by same certificate
implied C_legal on certificate:  >= 257/1680 against the standard boundary budget
```

Arm-G headline: the single smallest missing statement is no longer "orphan
rows do not exist." They do. The circulation candidate needs either the
strengthened active-row orphan exclusion above, or more directly an
orphan-financing lemma charging lambda-positive orphan leakage to
class-aggregate/signed-ledger budget before the fan-matched negative-coordinate
collateral is applied. [T1/T2]
