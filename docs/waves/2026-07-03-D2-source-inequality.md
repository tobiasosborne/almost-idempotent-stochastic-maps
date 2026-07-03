<!--
ROLE: decision wave for arm D wave 2: H-M quotient source inequality,
the step-4 core of (TT).
STATUS: exploration/decision note. Nothing below proves (EX),
conj-kernel, conj-degenerate-transport, or op-classical.
Worker: codex. Arm D wave 2. Answers bd aism-9tb.
Tier legend: T0 = exact repo-file fact or exact python3 fractions.Fraction
arithmetic in this wave; T1 = elementary derivation from T0/validated inputs;
T2 = plausible proof target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch arithmetic: temporary python3 fractions.Fraction one-off; no repo
output was written by the checker.
Verdict: UNDECIDED. The exact source split is useful, but the remaining
dimension-free beta-negative transverse term is not closed.
-->

# Arm D Wave 2: H-M Source Inequality

Read inputs, in the requested order: D1 (`docs/waves/2026-07-03-D1-hm-transport.md`),
the registry target (`argument/lemmas/conj-degenerate-transport.md`), and A12
T2 (`docs/waves/2026-07-03-A12-lift.md`). I use D1's H-M notation throughout:
`beta(j)=P_{u_s j}`, `Gamma_t=Gamma_{s,t}`, and `T={t:t != s}`. For a scalar
`x`, write `x^+=max(x,0)` and `x^-=max(-x,0)`.

## T1. Exact Source Split

For every transverse coordinate `t in T`, H-M quotient harmonicity is

```text
Gamma_t + sum_{j in B} beta(j) a_t(j) = 0.                 (H_t)
```

Split the H-M `B` rows by the sign of `beta`. Define

```text
L_t       = sum_{j in B, beta>0} beta(j) a_t(j)^-,
P_t       = sum_{j in B, beta>0} beta(j) a_t(j)^+,
N_t^-     = sum_{j in B, beta<0} |beta(j)| a_t(j)^-,
N_t^+     = sum_{j in B, beta<0} |beta(j)| a_t(j)^+.
```

Then (H_t) gives the exact identity

```text
L_t = P_t + N_t^- - N_t^+ + Gamma_t.                       (1)
```

This is the requested split. The sign is important: with D1's convention
`Gamma_t + sum_B beta a_t = 0`, a positive transverse class aggregate
`Gamma_t>0` is the coordinate source for positive-beta negative coordinate
mass. The directly controlled aggregate

```text
sum_r Gamma_r^- <= sum_i beta(i)^- <= delta(P)              (2)
```

is still true, but it is not the per-coordinate source in (1). It becomes useful
only after an aggregate/fan argument transfers positive class source in one
coordinate to negative class source elsewhere, as in the no-center fan rows.
[T1]

For the degenerate target, let

```text
D = D_s,
R = {j in B : beta(j)>0 and j not in D}.
```

The coordinate identity restricted to the target rows is

```text
L_{D,t}
 = P_{D,t} + P_{R,t} - L_{R,t} + N_t^- - N_t^+ + Gamma_t,   (3)
```

where `L_{D,t}=sum_{j in D} beta(j)a_t(j)^-` and similarly for `P_{D,t}`.
Summing `L_{D,t}` over `t in T` gives

```text
M_D = sum_{j in D} beta(j) mu_s(j).                         (4)
```

Equation (3) is exact, but it is not yet an upper bound: `P_{D,t}` is same-row
positive coordinate mass and causes a cyclic estimate if simply kept on the
right side. The no-center rows are the red test: all positive-beta `B` rows are
in `D`, there are no beta-negative rows, and the mass is transported internally
among the degenerate fan rows. [T1]

The precise source inequality that would close this wave is therefore the
aggregate, all-class version

```text
(SI)  M_D <= C_src * ( G_class^- + S_-^mu ),

G_class^- = sum_{r=1}^k Gamma_r^-,
S_-^mu    = sum_{j in B, beta(j)<0} |beta(j)| mu_s(j).
```

Because of (2), `(SI)` plus a dimension-free estimate
`S_-^mu <= C_- delta(P)` implies (TT). The statement is deliberately not
coordinatewise: a coordinatewise proof would use `Gamma_t^+`, while the
dimension-free budget is `G_class^-`. The missing content of `(SI)` is exactly
the aggregate degenerate-row transport that prevents the positive-beta rows in
`D` from self-sourcing without cost. [T2]

## T2. The Remaining Hard Term

The beta-negative sigma source is

```text
S_-^sigma = sum_{j in B, beta(j)<0} |beta(j)| sigma_s(j),
sigma_s(j)=sum_{t in T} a_t(j)^+.
```

Since `sigma_s(j)=lambda_s(j)+mu_s(j)` and the theta-half Cramer box used in
the factorization gives `lambda_s(j)<=3` on the relevant rows, one gets only

```text
S_-^sigma <= 3 * sum_{beta<0} |beta(j)| + S_-^mu
           <= 3 delta(P) + S_-^mu.                         (5)
```

Thus the sigma term is harmless only after `S_-^mu` is bounded. The harmonic
identities do not close this by themselves. From (1),

```text
N_t^- <= L_t + N_t^+ + Gamma_t^-,
```

and summing over `t` gives

```text
S_-^mu <= M_+ + S_-^sigma + sum_{t in T} Gamma_t^-,
M_+ = sum_{j in B, beta>0} beta(j) mu_s(j).                 (6)
```

Substituting (5) into (6) leaves `S_-^mu` on both sides with the wrong sign.
This is a tautology-level coupled system, not a bound. [T1]

The pivot coordinate gives a second exact relation. Let
`A_s^+=sum_{j in B, beta>0} beta(j) a_s(j)` and
`B_- = sum_{beta<0}|beta(j)|`. From
`Gamma_s + sum_B beta a_s = 1`,

```text
S_-^sigma
 = B_- + S_-^mu + 1 - Gamma_s - A_s^+.                     (7)
```

This confirms the intuition: a beta-negative row with large positive
transverse sigma must either also have large beta-negative `mu`, or create a
pivot-coordinate deficit paid by class/pivot bookkeeping. But (7) is not a
dimension-free estimate, because `1-Gamma_s-A_s^+` is a signed transport
quantity, not known to be `O(delta)`. [T1/T2]

The current red instances do not exercise this hard term. In transverse,
no-center, and balanced-staircase D1 tests, every H-M `B` row carrying the
target has `beta>0`, so

```text
S_-^sigma = S_-^mu = 0.
```

Therefore the beta-negative term remains a genuine open subproblem rather than
a tested theorem. The most useful coupled target is:

```text
(BN)  sum_{j in B, beta(j)<0} |beta(j)| mu_s(j) <= C_- delta(P)
```

under the same theta-half argmin and H-M realization hypotheses. I do not have
a proof of `(BN)`. [T2]

## T3. Exact Witness Tables And Refutation Hunt

All table entries below were recomputed by an exact `fractions.Fraction`
scratch checker from the D1 displayed data. The checker asserted (1) in every
listed coordinate. [T0]

### Per-coordinate identity checks

For transverse `a=1/4`, `delta=1/5`, `D={x-}`:

| coord | `L_{D,t}` | `P_t` | `N_t^-` | `N_t^+` | `Gamma_t` |
|---|---:|---:|---:|---:|---:|
| `e1` | `1/5` | `0` | `0` | `0` | `1/5` |
| `e2` | `0` | `1/5` | `0` | `0` | `-1/5` |

For no-center `k=6`, `delta=1/100`, all seven `B` rows lie in `D` and
`beta=1/8`:

| coord | `L_{D,t}` | `P_t` | `N_t^-` | `N_t^+` | `Gamma_t` |
|---|---:|---:|---:|---:|---:|
| `e1` | `1/800` | `1/800` | `0` | `0` | `0` |
| `e2` | `1/100` | `0` | `0` | `0` | `1/100` |
| `e3` | `0` | `1/100` | `0` | `0` | `-1/100` |
| `e4` | `1/400` | `1/400` | `0` | `0` | `0` |
| `e5` | `1/800` | `1/800` | `0` | `0` | `0` |

This is the internal-transport warning: three coordinates are sourced by
positive degenerate-row coordinates, not by beta-negative rows. Any proof that
turns `P_{D,t}` into a free source is circular. [T0/T1]

For balanced staircase `m=5,a=1/16,eps=1/1000`, `delta=30/121`, both `B` rows
lie in `D`:

| coord group | multiplicity | `L_{D,t}` | `P_t` | `Gamma_t` |
|---|---:|---:|---:|---:|
| first five | `5` | `60000121/1210000000` | `0` | `60000121/1210000000` |
| next five | `5` | `0` | `59999879/1210000000` | `-59999879/1210000000` |

The tiny `e0` lambda defect is visible in the aggregate:

```text
M_D/delta          = 60000121/60000000,
G_class^-/delta   = 59999879/60000000,
M_D-G_class^-     = delta * 121/30000000.
```

This is exactly the A12 warning: pointwise own-row negativity does not pay the
`e0` coordinate, but the weighted aggregate remains close to the class-negative
source. [T0/T1]

### Aggregate source tests

| witness | `M_D/delta` | `G_class^-/delta` | `S_-^mu/delta` | `sum_T Gamma_t^+/delta` | comment |
|---|---:|---:|---:|---:|---|
| transverse `a=1/4` | `1` | `1` | `0` | `1` | sign-correct split |
| no-center `k=6` | `3/2` | `1` | `0` | `1` | internal fan transport |
| balanced staircase | `60000121/60000000` | `59999879/60000000` | `0` | `60000121/60000000` | nonzero lambda |
| H-M `delta=0` normal form | `0` | `0` | `0` | `0` | `D_s` empty by D1 |

Existing exact L3 no-center data in
`runs/2026-07-02-ex-no-center-highrank/data/no_center_highrank.csv` pushes the
same beta-negative-free reduced fan family to the following value. In the
reduced fan interpretation `lambda=0` on the carrying rows, so the recorded
`Phi/delta` is the corresponding `mu`-transport ratio; D2 did not re-enumerate
the Schur-degenerate status at `k=30`.

```text
k=30: reduced-fan mu-transport / delta = 27/14.
```

The certified pattern in that bundle is `2 - 2/(k-2)`, so this family presses
the source constant toward `2` but does not refute a universal constant. [T0
as repo-recorded exact L3 evidence; not rerun by this wave]

### Refutation hunt

I also checked the proposed class-aggregate bookkeeping. If the `Gamma_r`
classes partition the index set on which class aggregates are taken, then

```text
sum_r Gamma_r^- <= sum_{i in union C_r} beta(i)^- <= sum_i beta(i)^- <= delta(P).
```

So `G_class^-` cannot exceed `delta(P)`. This part is proved bookkeeping. The
catch is the sign: (1) uses `Gamma_t` with positive sign in each transverse
coordinate. The all-class negative aggregate can be the right source only after
a nontrivial aggregate transport argument, not by coordinatewise comparison.
[T1]

I did not find an exact realizable theta-half argmin refuting (TT). The easy
coefficient-only attacks are not certificates: they can satisfy the quotient
balance while ignoring the full `P=LB`, `BL=I`, row-negativity, and argmin
constraints. The many-D-row no-center family is the strongest exact stress
available here; it raises the necessary constant to nearly `2`, not to
dimension growth. [T1/T2]

## T4. Verdict

Verdict: **UNDECIDED**. The wave produces a sharper target, not a proof and not
a refutation.

What is proved inline:

- The exact coordinate split (1).
- The restricted split (3), showing precisely where same-D positive coordinate
  mass becomes cyclic.
- The class-negative budget `G_class^- <= delta(P)`.
- The beta-negative sigma reduction
  `S_-^sigma <= 3 delta(P) + S_-^mu`, assuming the same theta-half Cramer box
  used by the factorization.

What remains open:

- `(SI)`: the aggregate Schur-degenerate source inequality
  `M_D <= C_src (G_class^- + S_-^mu)`.
- `(BN)`: the beta-negative transverse estimate
  `S_-^mu <= C_- delta(P)`.
- The legal-row absorption if one instead proves a version of `(SI)` with
  explicit nondegenerate positive-coordinate source terms.

Suggested factoring before any af elevation:

1. `lem-hm-coordinate-source-split`: equation (1), purely algebraic.
2. `lem-class-negative-budget`: `sum_r Gamma_r^- <= delta(P)`, purely
   bookkeeping on the pivot row.
3. `conj-degenerate-source-aggregate`: `(SI)` under the exact TT hypotheses.
4. `conj-beta-negative-transverse`: `(BN)` under the exact TT hypotheses.

Together, items 2-4 imply `M_D <= C_tr delta(P)` with
`C_tr=C_src*(1+C_-)`. At present, items 3 and 4 are live gaps. Do not
af-elevate `conj-degenerate-transport` as a monolith from this wave; it would
abort exactly at those two statements. [T2]
