# w40_ndg proof log

## Verdicts

**Part A verdict: REPAIR CONFIRMED, with the literal `V=0 at every tested argmin` claim REFUTED.**

The repaired pointwise reduction

```text
E_s(j) <= sigma_s(j) + 2(-lambda_s(j))_+
```

is correct and was reverified exactly over the theta `1/2` class of the mandatory
families by an independent script, `verify_part_a.py`.  The selected-chart
`SB*` numerics also reproduce with `S*/delta <= 3`.

However, `V=0 at every tested argmin` is false as stated: the mandatory
perturbed staircase `m=5, eps=1/1000` has a selected argmin row with
`V/delta = 1/500000`.  The repair does not collapse back to `(SB)` by a
zero-overshoot theorem.

**Part B verdict: RANK-2 THEOREM, both horns closed in rank 2 with explicit
`C=2`; full NDG in higher rank remains open.**

For rank `k=2`, every theta-half `Phi`-argmin satisfies

```text
S*_s <= 2 delta(P)       for s=1,2,
V_s = 0,
Phi = 0.
```

The proof is direct and bypasses the higher-rank determinant horn: the
max-diameter chart has `Phi=0`, so all argmins have `Phi=0`; this forbids
positive-beta overshoot rows.  Then `(DEF)` charges `S*` to the negative mass of
the pivot row.  Exact random and adversarial rank-2 `LB/BL=I` checks are in
`rank2_explorer.py`, `rank2_results.json`, and `rank2_results.txt`.

Calibration:

```text
P(Part A P1 repair survives audit)                 = 0.98
P(literal V=0-at-argmin is false)                  = 0.995
P(DEF-coupling/no-free-overshoot interpretation)   = 0.90
P(rank-2 theorem below is correct)                 = 0.94
P(rank-2 C=2 is an artifact of the proof)           = 0.20
P(full higher-rank NDG is closed here)              = 0.00
```

## Part A. Repair Audit

### A1. Pointwise proof of `(P1)`

Definitions:

```text
lambda_s(j) = 1 - a_s(j)
mu_s(j)     = sum_{t != s} (-a_t(j))_+
sigma_s(j)  = sum_{t != s} ( a_t(j))_+
E_s(j)      = (mu_s(j) - lambda_s(j))_+.
```

Since `sum_t a_t(j)=1`, the off-pivot sum gives

```text
lambda_s(j) = sigma_s(j) - mu_s(j),
mu_s(j) = sigma_s(j) - lambda_s(j),
E_s(j) = (sigma_s(j) - 2 lambda_s(j))_+.
```

Now split by the sign of `lambda=lambda_s(j)`.

If `lambda >= 0`, then

```text
E = (sigma - 2 lambda)_+ <= sigma
  = sigma + 2(-lambda)_+.
```

If `lambda < 0`, then `sigma - 2 lambda = sigma + 2(-lambda) > 0`, so

```text
E = sigma + 2(-lambda)
  = sigma + 2(-lambda)_+.
```

Thus `(P1)` holds pointwise, with equality on overshoot rows.

Summing against `(beta_s(j))_+ >= 0` gives

```text
SF_s <= S*_s := S+_s + 2 V_s,
V_s := sum_j (beta_s(j))_+ (-lambda_s(j))_+.
```

### A1 exact re-verification

`verify_part_a.py` recomputes `P=L B`, enumerates the theta-half chart class,
selects the minimum-`Phi` chart, and checks `(R)`, `(P1)`, `(DEF)`, and
`V = Dpos - Dneg`.

Summary from `part_a_results.txt`:

```text
transverse_pair_a1_4:           Phi/d=1   S*/d_max=2    V/d_max=0
dense_pair_k7:                  Phi/d=1   S*/d_max=2    V/d_max=0
staircase_m2:                   Phi/d=1   S*/d_max=2    V/d_max=0
staircase_m3:                   Phi/d=1   S*/d_max=2    V/d_max=0
perturbed_staircase_m5_eps:     Phi/d=1   S*/d_max=2    V/d_max=1/500000
no_center_path_k6:              Phi/d=3/2 S*/d_max=5/2  V/d_max=0
no_center_path_k8:              Phi/d=5/3 S*/d_max=8/3  V/d_max=0
```

Every line has:

```text
P1_all=True, DEF_star=True, VID_all=True, BL=True, P2=True, rowsum=True.
```

For the no-center path cases I used the exact determinant structure instead of
brute-force determinant enumeration: with `a=1/100`, a theta-half basis must
contain all foreign unit rows and exactly one signed row; two signed rows force
an `a`-factor below `1/2`.

### A2. `V=0 at argmin` is refuted

The selected argmin of the perturbed staircase `m=5, eps=1/1000` is

```text
[1,2,3,4,5,6,7,8,9,10,11].
```

At `s=10`, `u=11`, `j=0`, the independent verifier finds

```text
beta   = 999/1000000 > 0
lambda = -1/999
V contribution = beta * (-lambda) = 1/1000000
delta = 1/2
V/delta = 1/500000
E = 5003/1998
sigma = 4999/1998
```

So a positive-beta overshoot row exists at a tested selected argmin.  The
statement "V=0 at every tested argmin" cannot be promoted to a theorem; it is
already false in the mandatory family.  What remains true is weaker: the
overshoot is tiny here and the repaired selected envelope still has
`S*/delta = 2`.

### A3. `(DEF)` coupling and no-free-overshoot

Let

```text
Dpos_s := sum_j (beta_s(j))_+ lambda_s(j)_+
V_s    := sum_j (beta_s(j))_+ (-lambda_s(j))_+
Dneg_s := sum_j (beta_s(j))_- lambda_s(j),
```

where `beta_- = (-beta)_+`.  The harmonic deficit identity is

```text
sum_j beta_s(j) lambda_s(j) = 0.
```

Splitting signs gives

```text
Dpos_s - V_s = Dneg_s.
```

In the theta-half class, `|lambda_s(j)| <= 3`, hence

```text
|Dneg_s| <= 3 delta.
```

This confirms the w39 coupling algebra, but it is not an independent bound on
`V_s`: it is one equation in `Dpos_s` and `V_s`.  A large positive deficit can
carry a large overshoot without violating `(DEF)`.  The prior class-wide w39
overshoot scan is consistent with this interpretation: off the argmin,
`V/delta` reaches `1` on the transverse and staircase families and
`1663/1667` on the perturbed staircase.

The clean pointwise handle remains

```text
(-lambda)_+ = (mu - sigma)_+ <= mu,
V_s <= M_s := sum_j (beta_s(j))_+ mu_s(j),
```

but `M_s` is itself a selection-level object in higher rank.

## Multi-Row Swap Formula

Let `U` be a chart, and write row coordinates in that chart as row vectors
`a(i)`.  Swap pivot index set `I` with actual row set `J`, with `|I|=|J|=m`.
Let `K` be the unswapped pivot indices.  In the old coordinates, after ordering
`I` before `K`, write

```text
C = A[J,I]       (m x m)
D = A[J,K]       (m x (k-m)).
```

The new basis matrix in old coordinates is

```text
M = [ C  D ]
    [ 0  I ].
```

The swap is nonsingular iff `det C != 0`, and the volume factor is `|det C|`.
For any old coordinate row split as `(x_I, x_K)`,

```text
x'_I = x_I C^{-1}
x'_K = x_K - x_I C^{-1} D.
```

For beta rows, the new pivot rows corresponding to the swapped-in actual rows
are the same affine combinations of old pivot beta rows:

```text
beta'_I = C beta_I + D beta_K,
beta'_K = beta_K.
```

This is the block/Schur version of the single-shear formula.  In higher rank it
is exactly the formula needed for the volume-permitted horn:

```text
Vol(V) = |det C| Vol(U).
```

The missing higher-rank step is not the formula; it is a usable bound on
`Phi(V)` after the shear, or a direct estimate when every relevant `det C` is
below the theta threshold.

## Part B. Rank-2 Theorem

### Statement

Let `rank(P)=2`, and let `U*` be any theta-half `Phi`-argmin over actual-row
bases.  Then, for both pivot rows,

```text
Phi(U*) = 0,
V_s(U*) = 0,
S*_s(U*) <= 2 delta(P).
```

Thus rank 2 satisfies `(SB*)` with explicit constant `C=2`.

### Proof

Represent each actual row by a scalar `x_i`, so

```text
L_i = (1 - x_i, x_i).
```

For a basis formed by rows `p<q`, use normalized coordinate

```text
y_i = (x_i - p)/(q - p).
```

For the left pivot, `lambda=y_i`; for the right pivot, `lambda=1-y_i`.  In rank
2 there is only one transverse coordinate.  Therefore

```text
sigma = lambda_+,
mu    = (-lambda)_+,
E     = (mu - lambda)_+ = 2(-lambda)_+,
S* integrand = lambda_+ + 2(-lambda)_+.
```

Now choose a max-diameter basis: `p=min_i x_i`, `q=max_i x_i`.  Every row has
`0 <= y_i <= 1`.  Hence both pivot rows have `E=0` for every column, so

```text
Phi(max-diameter chart) = 0.
```

Since `Phi` is nonnegative, every `Phi`-argmin has `Phi=0`.

Fix any argmin chart and any pivot `s`.  Because `Phi=0`, every row with
`(beta_s(j))_+ > 0` has `E_s(j)=0`.  In rank 2 this means

```text
lambda_s(j) >= 0
```

on all positive-beta rows.  Therefore

```text
V_s = sum_j (beta_s(j))_+ (-lambda_s(j))_+ = 0
```

and

```text
S*_s = sum_j (beta_s(j))_+ lambda_s(j).
```

Use `(DEF)`:

```text
0 = sum_j beta_s(j) lambda_s(j)
  = sum_j (beta_s(j))_+ lambda_s(j)
    - sum_j (beta_s(j))_- lambda_s(j).
```

So

```text
S*_s = sum_j (beta_s(j))_- lambda_s(j)
     <= sum_j (beta_s(j))_- (lambda_s(j))_+.
```

In the theta-half class, Cramer gives `|a_t(j)| <= 2`; in rank 2 the transverse
coordinate is exactly `lambda_s(j)`, so `(lambda_s(j))_+ <= 2`.  Also

```text
sum_j (beta_s(j))_- <= nu_{u_s}(P) <= delta(P).
```

Therefore

```text
S*_s <= 2 delta(P).
```

This proves the rank-2 selected-chart bound for every `Phi`-argmin, not merely
for a tie-broken selection.

### Horn interpretation in rank 2

The volume-permitted overshoot horn closes because positive-beta overshoot is
impossible at an argmin: such a row has `lambda<0`, hence `E=2(-lambda)>0` and
would force `Phi>0`, contradicting the max-diameter comparison chart with
`Phi=0`.

The near-degenerate horn closes by the `(DEF)` charge above.  Once overshoot is
absent, all `S*` carriers have nonnegative transverse coordinate, and their
positive mass is paid by the negative beta mass of the same pivot row.  The
theta-half box gives the explicit factor `2`.

### Exact rank-2 checks

`rank2_explorer.py` constructs exact rank-2 idempotents from rational supports
using the `LB/BL=I` converse, enumerates every theta-half basis pair, and checks
all `Phi` argmins, not only the lexicographic first one.

Summary from `rank2_results.txt`:

```text
fixed adversarial cases: phi_min=0, maxV/d=0, maxS*/d in {0,1}
12 deterministic random exact cases: phi_min=0, maxV/d=0, maxS*/d <= 2
sharp observed cases: random_04 and random_11 have maxS*/d=2
```

Every generated instance has

```text
BL=True, P2=True, rowsum=True.
```

The sharp examples are useful: the proof's `C=2` is not just slack from a bad
estimate over the theta-half box.  In those examples, an argmin tie has a
carrier exactly at the theta boundary and the negative beta mass saturates the
charge.

## What remains open

The higher-rank NDG horn is not closed here.  The rank-2 proof uses a special
fact with no direct higher-rank analogue: a max-diameter chart puts all rows in
the interval `[0,1]`, forcing `Phi=0`.  In rank `k>=3`, a max-volume simplex
does not put all actual rows in the nonnegative simplex; transverse signs can
remain, and the block determinant horn is real.

The next missing display is therefore:

```text
If every relevant multi-row swap block C has |det C| below the theta threshold,
then the S*_s mass carried by those rows is O(delta) from (DEF), the sum-rule
identities, and row negativity.
```

The Schur formula above gives the exact comparison chart for the
volume-permitted side, but I did not obtain the higher-rank sheared `Phi(V)`
bound or the determinant-to-charge inequality.
