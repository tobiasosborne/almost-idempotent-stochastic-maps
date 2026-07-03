<!--
ROLE: independent decision wave for arm A wave 10: weighted own-negativity payment.
STATUS: L3/T-tier exploration report only. Nothing below proves (EX), conj-kernel, or op-classical
under repo L0; inline derivations are proof sketches unless later af/Lean/byte-verified.
Tier legend: T0 = exact repo-file fact or exact fractions.Fraction scratch recomputation;
T1 = elementary derivation / conservative synthesis from T0;
T2 = plausible proof candidate with a live gap;
T3 = speculation.
Worker: codex. Arm A wave 10. Answers bd aism-85b.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd were not run.
Scratch checker: /tmp/aism_a10_wop.py, pure fractions.Fraction arithmetic.
-->

# Arm A Wave 10: Weighted Own-Negativity Payment

## T1. Refutation Hunt

The target was the weighted own-negativity payment

```text
sum_{j in D_s} beta_s(j) E_s(j)
  <= C sum_{j in D_s} beta_s(j) nu_j
```

at a theta-`1/2` `Phi`-argmin, where `D_s` is the A8 degenerate set. A9 already
gave the trivial composition

```text
sum_{j in D_s} beta_s(j) nu_j <= delta(P) * (1 + nu_{u_s}) <= (5/4) delta(P).
```

Thus any universal `C` would decide the payment horn with a worse constant.
[T0/T1]

### The raw zero-average inequality is false

The broad discrete statement "for every zero-average finite set and every
chosen `w0`, average `neg_l1(w-w0)` is at most twice average `neg_l1(w)`" is
false. Exact scalar certificate:

```text
G = {1, -1/4, -1/4, -1/4, -1/4},  w0 = 1.
```

The average is zero,

```text
avg neg(w-w0) = 1,       avg neg(w) = 1/5,
```

so the ratio is `5`, not `<=2`. This is not a valid shear fan because the
individual vectors do not have zero coordinate-sum; it only kills the
over-broad formulation. [T0]

### Exact lopsided fan sanity checks

I then tested realizable reduced fans, where every shear vector has coordinate
sum zero and the selected pivot is a chart argmin. The exact `LB` construction
uses two foreign unit rows, one anchor row in `B`, shear scale `a=1/100`, and
`P=LB`. In both rows below the checker verifies `BL=I`, `P^2=P`, row sums, and
`delta(P)=1/100`. [T0]

Uniform lopsided fan:

```text
vectors: (1,-1), four copies of (-1/4,1/4)
weights: 1/5 each
theta argmins: 4
argmin basis: (0,1,3), pivot row 3
D row: row 2, beta=1/5, E=1/80, nu=1/100, max cover det=1/80
sum_D beta E / delta = 1/4
sum_D beta nu / delta = 1/5
WOP ratio = 5/4
```

Non-uniform two-row fan:

```text
vectors: (1,-1), (-1/9,1/9)
weights: 1/10, 9/10
theta argmin: unique
argmin basis: (0,1,3), pivot row 3
D row: row 2, beta=1/10, E=1/90, nu=1/100, max cover det=1/90
sum_D beta E / delta = 1/9
sum_D beta nu / delta = 1/10
WOP ratio = 10/9
```

These are not refuters. They show the argmin condition blocks the cheap
"large spike pivot" attack: the dangerous spike chart is not a `Phi`-argmin.
[T0/T1]

### Staircase near-misses

The best exact D-filtered ratio I found in this wave is a small balanced
staircase, sharper than the A9 `m=5` row but still below `3`. Parameters:

```text
m=2, a=1/6, eps=1/20, u=3/16
delta(P)=1/4
theta-half charts: 3
Phi-argmins: 2
min Phi/delta = 203/200
argmin basis: (1,2,3,4,5), pivot row 5
```

The degenerate rows for the reported pivot are:

| row | `beta` | `E` | `nu` | max cover det |
|---:|---:|---:|---:|---:|
| `0` | `19/400` | `49/114` | `1/20` | `43/228` |
| `6` | `7/20` | `2/3` | `199/800` | `1/3` |

Hence

```text
sum_D beta E / delta  = 203/200
sum_D beta nu / delta = 1431/4000
WOP ratio             = 4060/1431
```

The A9 balanced staircase row was also reproduced:

```text
m=5, a=1/16, eps=1/1000, u=20/121, delta=30/121
WOP ratio = 14520087846000/5752786904077.
```

No exact row tested in this wave exceeded `3`. The search was not exhaustive,
so this is evidence only, not a bound. [T0/T1]

## T2. Proof Attempt

### A fan all-mass inequality is proved inline

Let `(w_i,p_i)` be a finite weighted shear fan in `R^d` with `p_i>0`,
`sum_i p_i=1`, each `sum_l w_i(l)=0`, and weighted barycenter
`sum_i p_i w_i=0`. Put

```text
n(w) = sum_l max(-w(l),0).
```

Because each `w_i` has coordinate sum zero, `n(w_i)=||w_i||_1/2`. Let
`w_*` be a support point minimizing

```text
F(v) = sum_i p_i n(w_i-v)
```

over the support. Then

```text
F(w_*) <= 2 sum_i p_i n(w_i).
```

Proof. Let `N=sum_i p_i n(w_i)`. Some support point `v` has `n(v)<=N`,
otherwise the weighted average of the `n(w_i)` would exceed `N`. For zero-sum
vectors,

```text
n(w_i-v) <= n(w_i) + n(v)
```

coordinatewise, since the negative part of `w_i-v` is bounded by the negative
part of `w_i` plus the positive part of `v`, and the positive and negative
masses of `v` are equal. Therefore

```text
F(w_*) <= F(v)
       <= sum_i p_i n(w_i) + n(v)
       <= 2N.
```

This proves the all-mass fan template with constant `2`. Draft af contract:

```text
For a finite weighted family of zero-coordinate-sum vectors with weighted
barycenter zero, a support minimizer of the weighted average negative
distance has average negative distance at most twice the weighted average
negative mass.
```

[T1-PROVED-INLINE for this discrete lemma only]

### Why this does not prove WOP

The WOP denominator is not the all-mass denominator. It is restricted to
`D_s`, equivalently to rows with positive `E_s` and degenerate covering swaps.
In a reduced fan with duplicate selected shears, the all-mass denominator
counts the selected duplicates' own negative mass, while WOP drops them
because `E_s=0`. The lopsided uniform fan above shows the gap exactly:

```text
all-mass fan ratio at the argmin = 5/8
D-restricted WOP ratio           = 5/4
```

The missing fan-level statement is therefore a D-restricted version:

```text
sum_{i: n(w_i-w_*)>0} p_i n(w_i-w_*)
  <= C sum_{i: n(w_i-w_*)>0} p_i n(w_i).
```

I did not prove this in general. It remains plausible with `C=2` for genuine
reduced fans, but the proof must control the selected pivot's own negative mass
that disappears from the restricted denominator. [T1/T2]

### General sourcing attempt and live gap

For a general exact signed idempotent, row reproduction gives

```text
a_t(j) = sum_l P_jl a_t(l).
```

The desired pointwise intuition is: if row `j` has large negative transverse
coordinate mass, then either row `j` pays through its own negative entries
`nu_j`, or that negative coordinate mass was inherited through positive
`P_jl` from other rows. The second case is the hard one. A positive
inheritance chain can move negative coordinates around without charging
`nu_j` pointwise; the balanced staircase `e0` row is the exact warning.

The Schur degeneracy slab gives useful local geometry (`|a_t(j)|<=1/2` in
tested transverse positions and small two-block determinants), but I could not
turn it into a dimension-free beta-weighted source inequality. The needed
statement should look like a transport/cancellation lemma: beta-weighted
negative transverse mass inherited inside `D_s` either cancels by the harmonic
identities or exits through `sum_{D_s} beta_s(j) nu_j`. I do not have that
lemma. [T2]

## T3. Verdict

**UNDECIDED.** I found no decision-grade refuter of WOP and no complete proof.
Because there is no exact counterexample, I did not create an L3 run bundle.
[T1]

What is solid from this wave:

- The raw "any chosen `w0`" zero-average inequality is false, exactly. [T0]
- The reduced-fan all-mass inequality is proved inline with constant `2`. [T1]
- Non-uniform and lopsided fan attacks did not refute WOP once the pivot is a
  `Phi`-argmin. [T0/T1]
- The sharpest exact near-miss found here is the `m=2` staircase ratio
  `4060/1431`, still below `3`. [T0]

What wave 11 should do:

1. Prove or refute the D-restricted fan inequality above. This is the cleanest
   standalone subproblem exposed by the all-mass proof.
2. Search non-fan `LB` templates where a selected pivot has substantial own
   negative mass excluded from the WOP denominator while other degenerate rows
   have large `E/nu`.
3. If the D-restricted fan lemma is true, lift it into the general proof as the
   model transport inequality for the reproduction identity.

Honest status: WOP with `C=3` remains unbroken by this wave, but it is not
proved. [T2]
