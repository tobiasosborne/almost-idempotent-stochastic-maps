<!--
ROLE: independent decision wave for arm A, wave 11: D-restricted fan inequality.
STATUS: L3/T-tier exploration report. The DRF proof below is an elementary T1 proof candidate until
banked through the repo's review/af process; it does not by itself prove (EX), conj-kernel, or op-classical.
Tier legend: T0 = exact repo-file fact or exact fractions.Fraction arithmetic;
T1 = elementary derivation from T0 / already validated lemmas;
T2 = plausible lift or downstream synthesis with remaining hypotheses to check;
T3 = speculation.
Worker: codex. Arm A wave 11. Answers bd aism-8w8.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd were not run.
Scratch: exact python3 fractions.Fraction one-offs only; no repo outputs and no persistent scratch file.
-->

# Arm A Wave 11: D-Restricted Fan Payment

## T1. Sharp Search

I write

```text
n(x) = sum_l max(-x_l, 0).
```

On the zero-coordinate-sum hyperplane this is a norm: `n(x)=n(-x)=||x||_1/2`, and
`n(x)=0` iff `x=0`. Thus the restricted set

```text
A = {i : n(w_i-w_*) > 0}
```

is exactly the set of non-duplicate rows away from the chosen support minimizer. Let
`q=sum_{i notin A} p_i` be the total mass of the duplicate pivot cluster and let
`r=1-q`. [T0/T1]

### Baseline families

Two-point and one-dimensional lopsided stars do not break constant `2`. If the pivot has mass
`q` and the other point is forced by the zero barycenter, then the restricted ratio is

```text
R = 1/q,
```

but the pivot is a support minimizer only for `q >= 1/2`; hence `R <= 2`. In the heavy-pivot
regime `q -> 1`, the ratio tends to `1`, because the other rows become large enough to pay the
barycenter. The A10 lopsided uniform fan is the same phenomenon with the small cluster selected:

```text
G = {(1,-1), 4 copies of (-1/4,1/4)},  p_i=1/5.
```

The selected cluster has `q=4/5`, all-mass ratio `5/8`, and D-restricted ratio `5/4`. [T0]

### Exact small refuters to C=2

The constant `2` is already false in `d=3`. Take weights

```text
p = (2/9, 4/9, 1/3)
```

and zero-sum vectors

```text
w_0 = (-4, 0, 4),
w_* = (2, 6, -8),
w_2 = (0, -8, 8).
```

The weighted barycenter is zero. The support scores are

```text
F(w_0)=8,   F(w_*)=8,   F(w_2)=80/9,
```

so `w_*` is a minimizer. The restricted numerator and denominator are

```text
N = sum_{i in A} p_i n(w_i-w_*) = 8,
D = sum_{i in A} p_i n(w_i)     = 32/9,
R = N/D                         = 9/4.
```

Thus `C=2` is not a D-restricted fan theorem. [T0]

A cleaner `d=4` certificate gives ratio `5/2`. Let

```text
p_* = 2/5,     p_1=p_2=3/10,
w_* = (1/2,-1/2, 1/2,-1/2),
w_1 = (-2/3, 2/3, 0, 0),
w_2 = (0, 0, -2/3, 2/3).
```

Again every vector has coordinate sum zero and the weighted barycenter is zero. The scores are

```text
F(w_*) = 1,
F(w_1) = F(w_2) = 16/15,
```

so the pivot is the unique minimizer among these three support points. Since

```text
n(w_1)=n(w_2)=2/3,
n(w_1-w_*)=n(w_2-w_*)=5/3,
```

the D-restricted ratio is

```text
N = 1,       D = 2/5,       R = 5/2.
```

This is the first genuinely dangerous shape: the pivot has substantial excluded own mass, but the
nonpivot rows are separated from each other enough that moving the pivot to either one is not cheaper.
[T0/T1]

### Sharp certificate sequence

The preceding example is the `k=2`, `q=2/5` member of a family that approaches the exact supremum.
Fix an integer `k>=2`, a rational `0<q<1/2`, put `r=1-q` and `t=q/r`, and work in `R^{2k}` with
coordinate pairs `(a_j,b_j)`. Define

```text
w_* has pair j equal to (1/k, -1/k),
w_j has pair j equal to (-t, t) and all other pairs equal to (0,0),
p_* = q,        p_j = r/k   (1 <= j <= k).
```

Then the weighted barycenter is zero because `r t = q`. Also

```text
n(w_*) = 1,
n(w_j) = t,
n(w_j-w_*) = 1+t = 1/r,
```

so

```text
N = 1,      D = q,      R = 1/q.
```

For every nonpivot `w_j`,

```text
F(w_j)
  = q(1+t) + sum_{l != j} (r/k) n(w_l-w_j)
  = q/(1-q) + 2q(1-1/k).
```

Hence `w_*` is a support minimizer whenever

```text
q/(1-q) + 2q(1-1/k) >= 1.                         (1)
```

For every rational

```text
q > q_0 := 1 - 1/sqrt(2),
```

the left side of (1) tends to `q/(1-q)+2q > 1` as `k -> infinity`, so some finite `k`
gives an exact rational admissible family with ratio `1/q`. Taking rational `q downarrow q_0`
therefore gives

```text
sup R >= 1/q_0 = 2 + sqrt(2).
```

The upper bound in T2 matches this, so the supremum trend is bounded and sharp:

```text
sup R = 2 + sqrt(2).
```

[T0/T1]

## T2. Decision Proof

Let `w_*` be a support minimizer for

```text
F(v) = sum_i p_i n(w_i-v).
```

Let `A={i:n(w_i-w_*)>0}`, `q=sum_{i notin A}p_i`, `r=sum_{i in A}p_i=1-q`, and set

```text
N = sum_{i in A} p_i n(w_i-w_*),
D = sum_{i in A} p_i n(w_i).
```

If `A` is empty then `N=D=0`, so assume `A` is nonempty. Since `w_*` itself has positive
weight, `q>0`. All indices outside `A` are duplicate copies of `w_*`. [T1]

First, the zero-sum triangle bound gives

```text
n(w_i-w_*) <= n(w_i) + n(w_*),
```

so

```text
N <= D + r n(w_*).                                  (2)
```

The barycenter identity gives

```text
sum_{i in A} p_i w_i = -q w_*.
```

By subadditivity of `n`, and because `w_*` has coordinate sum zero,

```text
D >= n(sum_{i in A} p_i w_i) = n(-q w_*) = q n(w_*).
```

Combining with (2),

```text
N <= (1/q) D.                                       (3)
```

Second, average the minimizer comparison over nonpivot support points. For each `j in A`,
`N=F(w_*) <= F(w_j)`. Therefore

```text
N <= (1/r) sum_{j in A} p_j F(w_j)
   = (q/r) N
     + (1/r) sum_{i,j in A} p_i p_j n(w_i-w_j).
```

Again by the zero-sum triangle bound,

```text
n(w_i-w_j) <= n(w_i) + n(w_j),
```

hence

```text
sum_{i,j in A} p_i p_j n(w_i-w_j) <= 2rD.
```

If `q<1/2`, this yields

```text
N <= [2(1-q)/(1-2q)] D.                             (4)
```

If `q>=1/2`, (3) already gives `N<=2D`. If `q<1/2`, combine (3) and (4):

```text
N/D <= min( 1/q,  2(1-q)/(1-2q) ).
```

The first function is decreasing in `q`; the second is increasing on `(0,1/2)`. They cross at

```text
q_0 = 1 - 1/sqrt(2),
```

and the common value is

```text
1/q_0 = 2 + sqrt(2).
```

Therefore the D-restricted fan inequality holds with the sharp universal constant

```text
sum_{i in A} p_i n(w_i-w_*)
  <= (2 + sqrt(2)) sum_{i in A} p_i n(w_i).
```

[T1-PROVED-INLINE]

Draft single-sentence af contract:

```text
D-restricted zero-sum fan payment: under the hypotheses of lem-fan-payment, if w_* is a support
minimizer of v -> sum_i p_i n(w_i-v) and A={i:n(w_i-w_*)>0}, then
sum_{i in A} p_i n(w_i-w_*) <= (2+sqrt(2)) sum_{i in A} p_i n(w_i).
```

The sharpness sequence above shows that the constant cannot be improved below `2+sqrt(2)` for this
abstract D-restricted fan statement. [T1]

## T3. Verdict

**DRF PROVED-INLINE, with sharp constant `2+sqrt(2)`.** Constant `2` is exactly refuted; it fails already
for three vectors in `d=3` with ratio `9/4`, and the `d=4` direct-sum certificate gives `5/2`. The exact
direct-sum sequence approaches `2+sqrt(2)`, matching the proof. [T0/T1]

Composed fan-template consequence: in any reduced fan-template payment where the numerator is a shear
scale times `sum_{i in A} p_i n(w_i-w_*)` and the restricted own-negativity denominator is the same shear
scale times `sum_{i in A} p_i n(w_i)`, the payment horn holds with constant `2+sqrt(2)`. This upgrades the
A10 all-mass fan mechanism to the D-restricted denominator, but with a necessary constant loss beyond `2`.
[T1/T2]

This does not by itself prove `conj-degenerate-payment`: the lift still has to verify that the actual
idempotent rows at a theta-`1/2` `Phi`-argmin reduce to this fan model with the same numerator and
denominator and that the Schur-degenerate set is exactly the D-restricted set being paid. The discrete
inequality is no longer the obstruction; the remaining obstruction is the lift/realizability interface.
[T2]
