<!--
ROLE: proof-scoping structure wave for arm D wave 1: H-M 1.12 coordinates
for the restricted degenerate transverse transport conjecture.
STATUS: exploration/scoping note. Nothing below proves (EX), conj-kernel,
conj-degenerate-transport, or op-classical.
Worker: codex. Arm D wave 1. Answers bd aism-d9j.
Tier legend: T0 = exact repo-file fact or exact python3 fractions.Fraction
arithmetic in this wave; T1 = elementary derivation from T0/validated inputs;
T2 = plausible proof target with a live gap; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd
were not run. This intentionally skips the repo's usual fr-board startup step.
Scratch arithmetic: temporary python3 fractions.Fraction one-off; no repo
output was written by the checker.
Quote discipline: H-M 1.12 is line-located and paraphrased, with a short
byte-verbatim excerpt only.
-->

# Arm D Wave 1: H-M Coordinates For Degenerate Transport

Target read verbatim from `argument/lemmas/conj-degenerate-transport.md`:
at a theta-`1/2` `Phi`-argmin actual-row basis `U`, for every pivot `s`,
the Schur-degenerate rows `D_s` should satisfy

```text
sum_{j in D_s} beta_s(j) * mu_s(j) <= C_tr * delta(P).
```

This wave attacks that statement from H-M Theorem 1.12 coordinates and
keeps every proof-status label below explicit.

## T1. H-M 1.12 Coordinates

Local source: `refs/hognas-mukherjea/hognas-mukherjea-2011.txt:2246-2277`.
Short byte-verbatim excerpt from line 2246:

```text
idempotent matrix of rank k
```

The theorem statement at lines 2246-2277 gives a partition
`{T, B, C_1, ..., C_k}` of the index set for a real rank-`k` idempotent
matrix. `T` consists of zero-row and zero-column indices. Each `C_t` is a
rank-one proportional-row class. For representatives `u_t in C_t`, every
`B` row is an exact linear combination

```text
P_{ij} = sum_t a_t(i) P_{u_t j},      i in B,
```

and the idempotence constraints are the coefficient sum rules (1.2)/(1.3):

```text
sum_{i in C_s} eps(i,u_s) P_{u_s i}
  + sum_{i in B} a_s(i) P_{u_s i} = 1,

sum_{i in C_t} eps(i,u_t) P_{u_s i}
  + sum_{i in B} a_t(i) P_{u_s i} = 0,     s != t.
```

The theorem also includes a converse and a formula for rows indexed by `T_c`.
[T0, local cited source + paraphrase]

For this repo's exact signed idempotents, all row sums equal `1`. Therefore a
nonzero proportional-row scalar satisfies `eps(i,u_t)=1`: proportional
nonzero rows are identical-row clones. Hence in an H-M chart whose
representatives are the actual-row basis `U`,

```text
a(h)=e_t        for h in C_t,
mu_s(h)=0       for every class row h,
```

because no transverse coordinate of a class row is negative. Thus every row
with positive transverse tax is either an H-M `B` row or a `T_c` row. But a
`T_c` index has zero column, so `beta_s(j)=P_{u_s j}=0` for every pivot and
cannot contribute to `sum beta_s(j) mu_s(j)`. The TT tax is therefore exactly
an H-M `B`-row tax in these coordinates. [T1]

For pivot `s`, write `beta(j)=P_{u_s j}` and
`Gamma_{s,t}=sum_{i in C_t} beta(i)`. The sum rules become

```text
Gamma_{s,s} + sum_{i in B} beta(i) a_s(i) = 1,
Gamma_{s,t} + sum_{i in B} beta(i) a_t(i) = 0,     t != s.
```

These are the harmonic coordinate identities with clone-class aggregation
built in. They are clone-invariant: cloning a class only changes the class
aggregate `Gamma_{s,t}`, not the formula. [T1]

Interpretation for `mu_s(j)`: for an H-M `B` row, `a(j)` is an affine
coordinate vector because all representative rows have row sum `1`, so
`sum_t a_t(j)=1`. Then

```text
mu_s(j) = sum_{t != s} max(-a_t(j), 0)
```

is exactly the negative transverse coefficient mass, i.e. the failure of that
row to be a convex combination of the representative classes in the transverse
directions. H-M 1.12 itself does not bound this deviation by `delta(P)`.
The balanced staircase below gives the warning: row `e0` has
`rowneg(e0)/delta = 121/30000` but `mu(e0)/delta = 37873/29970`. Thus the
needed statement cannot be pointwise "row negativity pays row coefficient
negativity"; it has to be beta-weighted and aggregate. [T1/T2]

### Exact Zoo Partitions

All rows below were recomputed with exact `fractions.Fraction` arithmetic.
For each case the checker verified `B L = I`, `P^2=P`, and row sums `1`.
[T0]

#### Transverse pair `a=1/4`

Use chart `U=(e1,e2,x+)`, pivot `s=x+`; `delta=1/5`.

```text
T_c = {e0};       C_1={e1}, C_2={e2}, C_3={x+};       B={x-}.
```

The `T_c` row has chart coordinates `(-1/4, 1/4, 1)` but `beta(e0)=0`.
The only tax row is

```text
x-: a=(-1/2, 1/2, 1), beta=2/5, lambda=0, mu=1/2, E=1/2,
    rowneg/delta=1.
```

Hence `D_s={x-}` and

```text
M_D/delta = beta*mu/delta = 1.
```

The H-M sum rules for this pivot are visibly the harmonic identities:

```text
e1-coordinate:  1/5 + (-1/5) = 0
e2-coordinate: -1/5 +  1/5  = 0
x+-coordinate:  3/5 +  2/5  = 1.
```

[T0/T1]

#### No-center path `k=6`, `a=1/100`

Use chart `U=(e1,e2,e3,e4,e5,+23)`, pivot `s=+23`; `delta=1/100`.
There are no zero rows or zero columns. The H-M classes are singletons

```text
C_t={U_t},       B={+12,-12,-23,+34,-34,+45,-45}.
```

Every `B` row is Schur-degenerate and lies in `D_s`; every one has
`beta=1/8` and `lambda=0`.

| row | H-M coordinates in `U` | `mu/delta` | contribution to `M_D/delta` |
|---|---:|---:|---:|
| `+12` | `(1/100,-1/50,1/100,0,0,1)` | `2` | `1/4` |
| `-12` | `(-1/100,0,1/100,0,0,1)` | `1` | `1/8` |
| `-23` | `(0,-1/50,1/50,0,0,1)` | `2` | `1/4` |
| `+34` | `(0,-1/100,1/50,-1/100,0,1)` | `2` | `1/4` |
| `-34` | `(0,-1/100,0,1/100,0,1)` | `1` | `1/8` |
| `+45` | `(0,-1/100,1/100,1/100,-1/100,1)` | `2` | `1/4` |
| `-45` | `(0,-1/100,1/100,-1/100,1/100,1)` | `2` | `1/4` |

Therefore

```text
M_D/delta = 3/2.
```

The class-aggregate sum rules are

```text
e1: 0+0=0,   e2: 1/100-1/100=0,   e3: -1/100+1/100=0,
e4: 0+0=0,   e5: 0+0=0,           +23: 1/8+7/8=1.
```

[T0/T1]

#### Balanced staircase `m=5`, `a=1/16`, `eps=1/1000`

The balanced dual scale is `u=20/121`. Use chart
`U=(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,x+)`, pivot `s=x+`;
`delta=30/121`. There are no zero rows or zero columns. The H-M classes are
singletons

```text
C_t={U_t},       B={e0,x-}.
```

Both `B` rows lie in `D_s`.

| row | H-M coordinates in `U` | `beta` | `lambda` | `mu` | `E` | `rowneg/delta` |
|---|---:|---:|---:|---:|---:|---:|
| `e0` | five `-313/4995`, five `104/1665`, pivot `1000/999` | `999/1000000` | `-1/999` | `313/999` | `314/999` | `121/30000` |
| `x-` | five `-1/8`, five `1/8`, pivot `1` | `95879/242000` | `0` | `5/8` | `5/8` | `59999879/60000000` |

The weighted transport contributions are

```text
e0:  beta*mu/delta = 37873/30000000,
x-:  beta*mu/delta = 95879/96000,
M_D/delta = 60000121/60000000.
```

The H-M class aggregates exactly cancel the `B` row aggregates. For each of
the first five transverse coordinates,

```text
Gamma = 60000121/1210000000,      B-sum = -60000121/1210000000.
```

For each of the next five,

```text
Gamma = -59999879/1210000000,     B-sum = 59999879/1210000000.
```

For the pivot coordinate,

```text
Gamma = 145879/242000,            B-sum = 96121/242000,
Gamma+B-sum = 1.
```

[T0/T1]

## T2. Restricted Tax Attempt

### (a) Class-quotient aggregation

H-M 1.12 gives the correct clone-invariant quotient: class rows have no
`mu`, zero-column rows have no `beta`, and all tax lives on `B`. The sum rules
replace raw index counting by class aggregates `Gamma_{s,t}`. This is exactly
the shape a proof needs. [T1]

What it does not yet give is positivity. In the balanced staircase, some
`Gamma_{s,t}` are negative because the pivot row itself is signed on those
classes. Thus the quotient equations are signed balance laws, not a positive
transport estimate. A viable lemma would have to say:

```text
positive beta-weighted negative transverse B-mass
is controlled by pivot-row negative class aggregates plus B-row negativity,
without summing over coordinates or classes.
```

I do not see that lemma from H-M alone. [GAP, T2]

### (b) Barycenter/source mechanism

A12's centered variables `w_j` turn the harmonic identities into

```text
sum_j beta_s(j) w_j = 0.
```

In H-M coordinates, the same identity decomposes into class source
`Gamma_{s,t}` plus `B`-row source. Negative transverse coordinate mass on
`beta>0` rows must be balanced by positive transverse mass, by `beta<0` mass,
or by signed class aggregates. The Schur-degenerate slab caps tested
coordinates, but only pointwise; summing those caps over coordinates is the
forbidden class-count route. [T1]

The aggregate version I would elevate only after more work is:

```text
For the positive-beta measure restricted to H-M B rows in D_s, the
negative-part functional n(a_{\perp}) is sourced by the negative part of the
pivot row and by beta-negative B rows, with a dimension-free constant.
```

This is close to TT but has a clearer H-M source package. The live difficulty
is that `n` is convex in the wrong direction for upper-bounding the average
negative part from a barycenter identity. The validated fan lemmas solve the
discrete payment once transport is known; they do not supply this source
bound. [GAP, T2]

### (c) Clustered-conditioning route

The inherited H-M campaign says the clustered-conditioning lemma was
proved-and-audited upstream: `eta=sqrt(delta)` clustering and a max-volume
actual-row basis with coefficient bound `A=1`. That is useful structure, but
it is still only `proved-mod-audit` here and it naturally gives
`sqrt(delta)`-scale geometry. TT needs an `O(delta)` weighted tax. [T1/T2]

The restriction to `D_s` might upgrade the scale if near-degenerate rows have
total positive beta mass `O(delta/eta)` or if the H-M class source cancels at
the quotient level. I found no derivation. Used naively, clustering reimports
either coordinate counting or near-cluster counting, both recorded walls. [GAP,
T2]

## T3. Wall Question

The inherited line stalled as follows, per `docs/ingest/OVERVIEW.md:288-324`
and `docs/ingest/ORCHESTRATION.md:195-203`: H-M coordinates led to a
representative displacement lemma; the general-row displacement version was
refuted already at `delta=0`; the max-volume form was only numerically
bounded; the reductions then converged on the all-row transverse coefficient
tax

```text
sum_j (P_{u_s j})_+ * sum_{t != s} (-a_t(j))_+ <= C_mu * delta.
```

The tax prover never landed. The repo does not contain the upstream worker
files for the exact `delta=0` refuter, so I did not cite or reconstruct a
missing note. [T0/T1]

What can be tested exactly from the accessible repo instances:

- The `delta=0` obstruction does not automatically enter TT in H-M
  representative coordinates. At `delta=0`, class rows have `mu=0`; zero-column
  rows have `beta=0`; convex H-M `B` rows have `mu=0`. Thus `D_s` is empty in
  the exact H-M/nonnegative normal form. [T1]
- The `D_s` restriction does not make the problem easy. In no-center `k=6`,
  all seven nonselected H-M `B` rows enter `D_s`, and `M_D/delta=3/2`. Any
  proof by per-row or per-class counting would already see the high-rank wall.
  [T0/T1]
- The argmin/D restriction also does not justify pointwise own-row negativity:
  in the balanced staircase, `e0 in D_s` has `rowneg(e0)/delta=121/30000` but
  `mu(e0)/delta=37873/29970`. Its beta is tiny, so the aggregate remains
  harmless, but the row itself is a death certificate for pointwise payment.
  [T0/T1]

Verdict: `D_s` plus `Phi`-argmin plausibly dodges the old all-row wall only in
an aggregate sense. It excludes the literal `delta=0` convex/H-M refuter and
avoids unnormalized all-pivot amplification, but it still admits the
high-rank fan rows and the balanced low-own-negativity row. The additional
hypothesis that matters is not merely "row is degenerate"; it is the full
package

```text
beta-weighted, pivot-local, Phi-argmin, Schur-degenerate H-M B-row
aggregation through the signed sum rules.
```

Any proof omitting one of those words falls back into an already tested wall.
[T1/T2]

## T4. Verdict And Skeleton

Proof skeleton for TT:

1. **H-M reduction.** In a chart whose representatives are the H-M classes,
   class rows have `mu=0` and `T_c` rows have `beta=0`; TT is an H-M `B`-row
   inequality. **PROVED-inline** from H-M 1.12 plus row sums. [T1]
2. **Quotient harmonicity.** The H-M sum rules give
   `Gamma_{s,t}+sum_B beta a_t=0` for `t != s` and the pivot version with
   right side `1`. **PROVED-inline.** [T1]
3. **Schur restriction.** For rows in `D_s`, one- and two-block covering swaps
   are volume-degenerate; tested zoo rows satisfy the slab behavior recorded
   in A8. **TESTED / partly definitional from the `D_s` contract.** [T0/T1]
4. **Source inequality.** Convert the signed quotient harmonicity and Schur
   slab into
   `sum_{D_s cap B} beta_+ mu <= C delta`, without coordinate, class, or
   near-block counting. **GAP; this is the af-elevatable core.** [T2]
5. **Payment composition.** Once TT holds, A12's pointwise `E<=2 mu` on `D_s`
   gives the payment horn at constant `2 C_tr`; the validated fan lemmas give
   sharper support infrastructure but are not the transport source. **PROVED
   conditional on TT.** [T1]

Recommendation:

- Do not af-elevate `conj-degenerate-transport` yet as a monolith. The
  current proof would abort at step 4.
- Next arm D wave should isolate the step-4 source inequality in H-M quotient
  language, with variables only `(Gamma_{s,t})`, H-M `B` coefficients, beta
  signs, and row negative masses. The exact red tests are no-center `k=6`
  for class-count pressure and balanced staircase `e0` for pointwise
  own-negativity failure.
- A death certificate exists for easy versions: pointwise `mu <= C nu_j`,
  per-coordinate slab summation, per-class counting, and unrestricted all-row
  tax proofs are all blocked by the computations above and the recorded
  dead-route ledger. TT itself remains alive. [T2]
