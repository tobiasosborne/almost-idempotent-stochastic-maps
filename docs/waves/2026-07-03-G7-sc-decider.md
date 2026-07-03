<!--
ROLE: independent exploration wave for arm G wave 7: pivot-removing
self-support/cancellation decider for (SC).
STATUS: exploration/decision note. Nothing below proves (EX), conj-kernel,
conj-degenerate-transport, or op-classical under repo L0.
worker: codex
arm: G wave 7
answers: bd aism-d23
Tier legend: T0 = exact repo-file fact or exact python3 fractions.Fraction
arithmetic in this wave; T1 = elementary derivation from T0/validated inputs;
T2 = plausible proof target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch checker: /tmp/aism_g7_sc.py, pure fractions.Fraction arithmetic;
no checker output file was written to the repo.
Verdict: the pivot-REMOVING chart move has an exact Schur formula and an
exact max-stationarity disjunction, derived below. This explains the G6
silent amplifier: the move has volume factor 5/4 and kills Phi. However,
(SC) is NOT proved and NOT refuted in this wave. The live gap is a
pivot-removing collateral/import bound: when the move is theta-half
admissible but the new chart's max Phi stays high, charge that obstruction
to G_class^- + S_-^mu + SIGMA + FanRes. The rank-3 (RH) assembly is blocked
exactly on this (SC) gap.
-->

# Arm G Wave 7: SC Decider

Read inputs in the requested order: G6; G5; G4, G3, G2, G1; A9, A8; D5,
D4, D6; and the 2026-07-03 orphan/legal-leak sections of `FINDINGS.md`.
I did not run `fr` or `bd`, and I edited no existing file. [T0]

Target:

```text
(SC)  sum_{j in NF} beta_j * (sum_{t != s} a_t(j)^-)
      <= C_SC * (G_class^- + S_-^mu + SIGMA) + C_fan' * FanRes,

SIGMA = sum_{beta_j>0} beta_j nu_j.
```

Here `NF` is the non-fan beta-positive H-M `B` rows: active orphans,
lambda-positive orphans, and silent rows. [T0]

## T1. Pivot-Removing Schur Move

Fix a rank-3 chart `U=(u_0,u_1,u_2)`, old chart coordinates `a(i)`, and
pivot `s`. Let a non-chart row `j` enter by replacing the old pivot row
`u_s`. Put

```text
c = a_s(j),       d_t = a_t(j),       lambda_s(j)=sum_{t != s} d_t=1-c.
```

The chart volume changes by the exact factor

```text
vol(U - u_s + j) / vol(U) = |c| = |1-lambda_s(j)|.       (1)
```

If `m_U=vol(U)/vol_max`, then the pivot-removing chart is theta-half
admissible exactly when

```text
|c| m_U >= 1/2,       equivalently       |c| >= 1/(2 m_U).       (2)
```

Since `m_U>=1/2`, the easy sufficient condition is `|c|>=1`. The determinant
factor is **not** `P_jj`. The self coefficient enters through row
reproduction:

```text
(1-P_jj) a_r(j) = sum_{i != j} P_ji a_r(i)       for r=0,1,2.   (3)
```

Thus high self-support means the residual moment in (3) is small; it does not
by itself decide chart volume. [T1]

For any row `i`, the new coordinates are

```text
a_s^j(i) = a_s(i)/c,
a_t^j(i) = a_t(i) - a_s(i)d_t/c             (t != s).            (4)
```

In particular `a^j(j)=e_s`, and the old pivot row has coordinates

```text
a_s^j(u_s)=1/c,       a_t^j(u_s)=-d_t/c       (t != s).          (5)
```

Let `B_r` be the old left-inverse rows, so the old pivot `s` beta row is
`beta_i=B_s(i)`. In the new chart,

```text
B_s^j = P_j = sum_r a_r(j) B_r,       B_t^j = B_t  (t != s).     (6)
```

So the row `j` is removed from the new pivot score because

```text
E_s^j(j)=0.
```

Equations (1), (4), and (6) are the pivot-removing analogue of A8/A9's
active-preserving Schur accounting. [T1]

## T1. Exact Phi Disjunction

Define, at the pivot-removing chart `V_j=U-u_s+j`,

```text
Psi_j   = Phi_s(V_j)
        = sum_i (P_ji)^+ E_s^j(i)
        = sum_{i != j} (P_ji)^+ E_s^j(i),

Gamma_j = max_{r != s} Phi_r(V_j)
        = max_{r != s} sum_i B_r(i)^+ E_r^j(i).
```

Let `M=Phi(U)=Phi_s(U)`, with `s` chosen maximal at the old chart. If
`V_j` is theta-half admissible, argmin minimality gives the exact inequality

```text
M <= max(Psi_j, Gamma_j).                                (7)
```

Equivalently, for an admissible row `j`, at least one of the following holds:

```text
new-pivot branch:     Psi_j >= M,
collateral branch:    Gamma_j >= M.                      (8)
```

This is weaker than A9's same-pivot identity because the pivot row changes
from `B_s` to `P_j`. If the new-pivot branch is used, the exact surplus over
the old non-`j` pivot contribution is

```text
C_PR(j) = Psi_j - sum_{i != j} beta_i^+ E_s(i).
```

Then `C_PR(j) >= beta_j E_s(j)` follows from `Psi_j>=M`, but only in that
branch. In the collateral branch, no same-pivot payment is forced. [T1]

Thus a proof of (SC) cannot only say "pivot onto `j`"; it must charge every
reason why (7) does not contradict old-chart minimality. The exact blockers
are volume loss `|a_s(j)| m_U < 1/2`, high new-pivot score `Psi_j`, or high
collateral score `Gamma_j`.                                      (9)

These are structural alternatives, not error terms. [T1]

## T0. Checks On G6 And G5

The scratch checker rebuilt the G6 and G5 families, asserted

```text
B L = I,       P = L B,       P^2=P,       P 1=1,
```

and compared (4),(6) against direct chart enumeration. [T0]

For the G6 silent amplifier at `e=1/4`, `kappa=1/100`, old chart
`(c0,c1,c2)` and pivot `s=c2`:

```text
old Phi       = (0, 0, 99/250),
a_s(o)        = 5/4,
P_oo          = 99/100,
nu_o          = 1/400,
new chart     = (c0,c1,o),
new Phi       = (0, 0, 0).
```

So the silent row has tiny ambient own-negativity but the pivot-removing move
is theta-half admissible and strictly improves the chart. This is why the
G6 amplifier is not an (RH) refuter. [T0/T1]

For the G5 two-orphan family at `h=1/10`, old chart `(c0,c1,c2)`:

```text
old Phi = (0, 0, 1/10).
```

Each orphan has

```text
a_s(o_i)=4/5,       P_{o_i o_i}=5/12,       nu_{o_i}=7/30.
```

The two pivot-removing charts are admissible, but blocked:

```text
(c0,c1,o0): Phi = (0, 1/4, 7/15),
(c0,c1,o1): Phi = (1/4, 0, 7/15).
```

Here the blocker is not dangerous for (SC): the self coefficient is not close
to `1`, and the ambient term `SIGMA` is already of the right size, matching
G6's repaired-horn replay and the exact floor `C_RH>=4`. [T0/T1]

## T2. Attempted (SC) Split

The natural split is by self-support. Fix `tau in (0,1)` and write

```text
Low_tau  = {j in NF : 1-P_jj >= tau},
High_tau = {j in NF : 1-P_jj <  tau}.
```

For `j in Low_tau`, G6's exact inequality gives, for every transverse
coordinate `r`,

```text
tau * a_r(j)^-
 <= P_jj^- a_r(j)^+
    + sum_{i != j} P_ji^- a_r(i)^+
    + sum_{i != j} P_ji^+ a_r(i)^-.                    (10)
```

The theta-half Cramer box gives `|a_r(i)|<=2` for every actual row. Thus the
negative-coefficient part of (10), after summing the two transverse
coordinates, is bounded by a universal multiple of `nu_j`. What remains is
the positive-import term

```text
I_+(j) =
  sum_{r != s} sum_{i != j} P_ji^+ a_r(i)^-.             (11)
```

To finish the low-self side one needs a weighted import statement of the
form

```text
sum_{j in Low_tau} beta_j I_+(j)
 <= C * (G_class^- + S_-^mu + SIGMA) + C_fan * FanRes.   (12)
```

I do not have (12). It is the same obstruction pattern as D5's legal-aware
financier import: positive imports can move chart negativity without being
seen by the importing row's own ambient negative mass. [T2]

For `j in High_tau`, equation (3) says chart negativity is genuinely
self-supported. If the pivot-removing chart is admissible, (7) says the move
is blocked only by `Psi_j` or `Gamma_j`. A complete proof of (SC) would need
an aggregate theorem:

```text
(PRC)  high-self pivot-removing blockers for non-fan rows are paid by
       G_class^- + S_-^mu + SIGMA + FanRes.              (13)
```

I do not have (13). G6 is the good case (`Psi=Gamma=0`); G5 is the budgeted
case (`P_jj=5/12`, `SIGMA` large). The missing case is a high-self row whose
pivot-removing chart is admissible but whose max Phi is kept high by
new-pivot or collateral imports that are not already in `SIGMA` or the fan
residual. [T2]

If the pivot-removing chart is not admissible, then

```text
|1-lambda_s(j)| < 1/(2m_U).
```

This is again not a budget by itself. In the positive-`lambda` orphan regime,
`E_s(j)` may be much smaller than `mu_j` or even zero, so old `Phi_s`
does not directly pay the negative transverse mass. The harmonic ledger
must still control cancellation before positive parts are taken. [T2]

## T2. Status Of (SC)

No complete proof of (SC) was obtained. The exact disjunction is strong
enough to explain the G6 silent amplifier, but it does not by itself bound
the obstruction terms in (9). [T2]

No exact refuting family was certified either. In particular, I did not find
a family with

```text
delta(P)<=1/4,
complete theta-half argmin enumeration,
unbounded beta-weighted silent/orphan cancellation over
G_class^- + S_-^mu + SIGMA + FanRes,
and every pivot-removing move blocked by volume loss or collateral Phi.
```

Failed designs are not infeasibility results. [T0/T2]

The honest verdict is therefore:

```text
(SC): OPEN.
displayed gap: prove (12)+(13), or replace them by one direct
               pivot-removing collateral/import theorem.
```

## T2. (RH) Assembly Status

Because (SC) is open, the full rank-3 repaired horn is not assembled. If
(SC) were proved with constant `C_SC`, the G5/G6 bookkeeping would combine as
follows:

```text
OD = L_mu^orph + F_L^orph + sum_{active orphan j} beta_j E_s(j),

E_s(j) <= mu_s(j)        on active orphan rows,
```

so the G5 ledger (cancellations before positive parts), the fan interface
`FanRes`, and the closed rank-3 overhead `E_s<=mu_s` would reduce (RH) to
the (SC) bound plus the existing class/signed terms. The resulting constant
would have to satisfy

```text
C_RH >= 4
```

because the G5 two-orphan family has exact repaired ratio tending to `4`.
Any assembled constant below `4` would contradict that T0 family. [T1/T2]

Interfaces needed for a future assembly: G5 harmonic sum rules and ledger
(2)-(5), G1/G2 `FanRes`, G6 ambient/chart identity and `SIGMA`, the
pivot-removing formulas (1),(4),(6),(7), and a proof of (SC) or equivalent
PRC/import control.

## Verdict

Task bits:

```text
pivot-removing tool:    DONE, exact formulas (1),(4),(6), disjunction (7)
(SC):                   OPEN, blocked on PRC/import control
C_SC:                   none
refuter family:          none certified
(RH) assembly:           blocked on (SC)
C_RH:                   none; any future value must be >= 4
```

Arm-G headline: the smallest remaining statement is not another orphan
exclusion and not pointwise `nu_j >= a_t(j)^-`. It is a pivot-removing
collateral/import theorem: at a theta-half `Phi`-argmin, every beta-positive
non-fan row whose chart negativity is self-supported must either pivot into
the chart or create a blocker paid by `G_class^- + S_-^mu + SIGMA + FanRes`.
[T2]
