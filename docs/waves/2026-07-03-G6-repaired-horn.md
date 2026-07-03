<!--
ROLE: independent exploration wave for arm G wave 6: repaired orphan horn,
silent-row hole, and ambient-vs-chart own-negativity audit.
STATUS: exploration/decision note. Nothing below proves (EX), conj-kernel,
conj-degenerate-transport, or op-classical under repo L0.
worker: codex
arm: G wave 6
answers: bd aism-sw7
Tier legend: T0 = exact repo-file fact or exact python3 fractions.Fraction
arithmetic in this wave; T1 = elementary derivation from T0/validated inputs;
T2 = plausible proof target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch checker: /tmp/aism_g6_repaired.py, pure fractions.Fraction arithmetic;
no checker output file was written to the repo.
Verdict: silent-row domination by ambient own negativity is FALSE as a
pointwise statement: chart negative coordinates can be carried by positive
self/import mass, with beta*a^- over beta*nu = 1/kappa in an exact family.
That family is NOT an (RH) refuter because the theta-half Phi-argmin pivots
onto the self-supported row. The repaired horn (RH) remains OPEN. It survives
all prior certified instances checked here; G5's exact family gives the floor
C_RH >= 4. The single missing statement is an argmin self-support/cancellation
control turning non-fan chart-negative mass into SIGMA plus the existing
class/signed and fan-collateral budgets.
-->

# Arm G Wave 6: Repaired Horn

Read inputs in the requested order: G5; G4; G3, G2, G1; D4, D3, D5, D6,
A9, A8; and `FINDINGS.md` through the 2026-07-03 orphan section. I did not
run `fr` or `bd`, and I edited no existing file. [T0]

Target at a rank-3 theta-half `Phi`-argmin chart `U`, maximal pivot `s`,
and H-M `B` rows:

```text
OD := L_mu^orph + F_L^orph + sum_{active orphan j} beta_j E_s(j)

(RH)  OD <= C_RH * (G_class^- + S_-^mu + SIGMA),
SIGMA := sum_{j in B : beta_j > 0} beta_j nu_j.
```

All orphan imports are aggregated before positive parts, as in G5. Silent
rows are not in `OD`, but they are counted in `SIGMA`. [T0]

## T1. Silent Rows

I use the D6/A8 covering convention. A row is strict legal for pivot `s` if
some active-preserving covering swap keeping `s` in the chart has Schur
volume factor `>1/2`. In rank 3, a one-row transverse swap has factor
`|a_t(j)|` for `t != s`; two-row covers are tested by the corresponding
transverse Schur determinant.

For this wave, a **silent** beta-positive H-M `B` row means:

```text
beta_j > 0,
and every active-preserving covering block containing j has |det C| <= 1/2.
```

In particular all one-row transverse coordinates obey `|a_t(j)|<=1/2`, and
the pivot-complement coordinate

```text
lambda_s(j) = sum_{t != s} a_t(j) = 1 - a_s(j)
```

is also sub-threshold in the one-dimensional complement sense used by the
rank-3 covering tests below. Silent rows can participate in the harmonic
sum rules and cancel a class financier, but they create no legal/orphan
demand term in `OD`. [T1]

## T1. Ambient Negativity Is Not Chart Negativity

Let `p_j=P_{j,*}` be row `j` of the ambient idempotent and

```text
nu_j = sum_i p_j(i)^-.
```

For every chart coordinate `r`, row reproduction gives the exact identity

```text
a_r(j) = sum_i p_j(i) a_r(i).                            (1)
```

Splitting off the self coefficient,

```text
(1 - P_jj) a_r(j) = sum_{i != j} P_ji a_r(i).             (2)
```

Thus a negative chart coordinate of row `j` can be carried by a positive
self coefficient `P_jj`. It costs no ambient negative mass until one asks how
the small residual `(1-P_jj)a_r(j)` is represented. The exact subadditive
negative-part inequality is

```text
a_r(j)^-
 <= P_jj^+ a_r(j)^- + P_jj^- a_r(j)^+
    + sum_{i != j} (P_ji^+ a_r(i)^- + P_ji^- a_r(i)^+).   (3)
```

If `P_jj^+` is close to `1`, (3) gives no lower bound of `a_r(j)^-` by
`nu_j`. Therefore the tempting domination

```text
beta_j nu_j >= beta_j a_r(j)^-
```

is false without an additional argmin/self-support statement. [T1]

## T0. Exact Silent Algebra Amplifier

For `0<e<=1/2` and `0<kappa<1`, take rows

```text
c0=(1,0,0), c1=(0,1,0), c2=(0,0,1),
o=(0,-e,1+e),
```

and

```text
B0 = [1,0,0,0],
B1 = [0,1,0,0],
B2 = [0, e(1-kappa)/(1+e), kappa, (1-kappa)/(1+e)].
```

The checker asserted exactly

```text
B L = I_3,       P = L B,       P^2=P,       P 1=1.
```

At the base chart `U=(c0,c1,c2)`, pivot `s=c2`, row `o` has coordinates

```text
a(o)=(0,-e,1+e).
```

It is silent in the one-row rank-3 covering tests: the transverse coordinates
are `0` and `-e`, and the pivot complement is `lambda_s(o)=-e`, all
sub-threshold. Its beta and ambient negative mass are

```text
beta_o = (1-kappa)/(1+e),       nu_o = e kappa.
```

Consequently

```text
beta_o a_1(o)^- = e(1-kappa)/(1+e),
beta_o nu_o     = e kappa(1-kappa)/(1+e),
(beta_o a_1(o)^-) / (beta_o nu_o) = 1/kappa.             (4)
```

For the checkpoint `e=1/4`, `kappa=1/100`, the checker printed

```text
delta(P)=1/400,       beta*a^- = 99/500,
beta*nu = 99/50000,   ratio = 100.
```

So silent rows can carry macroscopic chart cancellation with arbitrarily
small ambient own negative mass. [T0/T1]

This is not an (RH) refuter. The same checker enumerated the theta-half
charts and found

```text
chart (c0,c1,o):  volume 5/4,  Phi=(0,0,0),       max Phi=0,
chart (c0,c1,c2): volume 1,    max Phi=99/250.
```

The Phi-argmin pivots onto the self-supported row, where it is no longer a
silent `B` row. This is the exact obstruction left open: prove that every
argmin-compatible self-supported silent cancellation can be eliminated this
way, or build a family where collateral rows prevent that pivot. [T0/T2]

## T0. Repaired-Horn Replay

The checker replayed the mandatory instances with

```text
denominator = G_class^- + S_-^mu + SIGMA.
```

### G5 two-orphan family

For `p=1/2+h`, `e=1/2-h`,

```text
OD = 1/2 - 2h,
delta = e(1/4+h)/p,
SIGMA = delta/2,
denominator = h + delta/2.
```

Checkpoints:

| `h` | `OD` | `SIGMA` | denominator | ratio |
|---:|---:|---:|---:|---:|
| `1/10` | `3/10` | `7/60` | `13/60` | `18/13` |
| `1/20` | `2/5` | `27/220` | `19/110` | `44/19` |
| `1/100` | `12/25` | `637/5100` | `172/1275` | `153/43` |
| `1/1000` | `249/500` | `125249/1002000` | `126251/1002000` | `498996/126251` |

Thus the exact family forces

```text
sup OD/(G_class^-+S_-^mu+SIGMA) = 4.                    (5)
```

[T0/T1]

### G4 active-orphan certificate and boundary family

For the displayed active-orphan certificate,

```text
OD = 21/320,
denominator = 21/320 + (7/64)(1/4) = 119/1280,
ratio = 12/17.
```

For the G4 boundary trend, the repaired ratio is

```text
OD/(G_class^-+SIGMA) = (1-4h)/(3/4+h) -> 4/3.
```

The old payment-included class-only ratio tended to `2`; adding `SIGMA`
absorbs part of that stress. [T0/T1]

### G3 orphan certificate

Using G3's displayed row negative mass `nu_o=461/2880`,

```text
OD = 257/57600,
denominator = 7/240 + (1/20)(461/2880) = 2141/57600,
ratio = 257/2141.
```

[T0]

### D6 certificates

D6-A and D6-B have strict legal rows with volume-permitted negative
coordinates, hence they belong to the fan side, not `OD`. After fan separation
the repaired-horn orphan demand is

```text
OD = 0
```

for both certificates. [T0/T1]

The worst certified finite checkpoint is G5 at `h=1/1000`,
`498996/126251`; the exact family floor is the supremum `4`. [T0/T1]

## T1/T2. What Would Prove RH

G5's exact cancellation ledger says, for each transverse coordinate `r`,

```text
P_r^O = N_r^O - H_r - Gamma_r,
P_r^O <= Gamma_r^- + N_r^O + (-H_r)_+.                  (6)
```

The repaired budget correctly names two missing sources:

- `N_r^O`, the active orphans' own sub-threshold negative coordinates;
- the silent part of `(-H_r)_+`, coming from beta-positive non-OD rows.

The fan part of `(-H_r)_+` should remain an interface to the G1/A9 legal
collateral horn. The class part is paid by `G_class^-`, and beta-negative
rows by `S_-^mu`. The surviving proof target is therefore the following
argmin self-support/cancellation control:

```text
(SC)  At a rank-3 theta-half Phi-argmin with maximal pivot s,
      the beta-weighted transverse negative chart mass of all non-fan
      beta-positive H-M B rows, after the legal fan rows are removed, is
      bounded by a universal constant times

      G_class^- + S_-^mu + SIGMA

      plus the explicit fan-collateral residual.
```

This statement is strictly stronger than the false pointwise domination
`nu_j >= a_r(j)^-`, because (SC) must also exclude or charge the positive
self-support mechanism in (2)-(4). I did not prove (SC), and I did not find
an argmin-compatible amplifier refuting it. [T2]

For the payment term, the prompt's inequality `E_s(j)<=mu_j` needs a
condition. It is false for arbitrary silent rows with `lambda_s(j)<0`; in the
silent algebra family, `E_s(o)=2e>mu_o=e`. But for rank-3 active strict
legal orphans, legality is through a positive transverse coordinate
`p>1/2` and orphan status gives the negative coordinate magnitude
`e<=1/2`, hence

```text
lambda_s = p-e >= 0,
E_s = (mu_s-lambda_s)_+ <= mu_s.
```

Thus, on the active orphan rows that actually enter `OD`,

```text
sum beta_j E_s(j) <= L_mu^orph,
```

so the payment term is at most a factor-two overhead on the `L_mu` part.
This part is closed in rank 3; it does not control `F_L^orph` or the silent
cancellation term in (SC). [T1/T2]

## Verdict

Task bits:

```text
silent-row hole:        OPEN for RH; CLOSED-BY-DOMINATION is false.
ambient-vs-chart fact:  beta*chart-negative / beta*nu = 1/kappa in an
                        exact silent algebra family; the Phi-argmin pivots
                        onto the row, so no RH refuter is certified.
(RH):                   OPEN. No prior certified instance violates it.
C_RH floor:             4, forced by the exact G5 two-orphan family.
worst finite replay:    498996/126251 at G5 h=1/1000.
single missing step:    (SC), the argmin self-support/cancellation control.
```

Arm-G headline: the unified `SIGMA` repair is the right budget on all
registered tests and exactly fixes the G5 amplifier up to constant `4`, but
it is not proved. The next wave should attack (SC) directly: either prove
that a Phi-argmin cannot leave self-supported silent cancellation in the
non-fan residual, or build an exact theta-half argmin family where collateral
prevents pivoting onto the silent row and the (RH) ratio grows without bound.
[T1/T2]
