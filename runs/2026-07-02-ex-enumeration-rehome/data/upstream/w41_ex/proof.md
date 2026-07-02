# w41_ex proof log

## Verdict

**FACTORIZATION VERIFIED.**  In every theta `1/2` chart and for every pivot `s`,

```text
S*_s(U) <= 2 Phi_s(U) + 6 delta(P).
```

The sketch's `a ~ 3` loses one `Phi`: the sharpened pointwise inequality is

```text
sigma_s(j) + 2(-lambda_s(j))_+ <= E_s(j) + 2(lambda_s(j))_+.
```

Thus `(a,b)=(2,6)` for the factorization used here.  I did not prove that no
different argument can improve the `6`; this is the exact constant pair from
the repaired `(DEF)`/theta-box factorization.

**(EX) at rank 3: HOLDS EMPIRICALLY, not proved.**  Exhaustive theta-half chart
enumeration on the required exact rank-3 suite found

```text
min_U max_s Phi_s(U) / delta(P) <= 1
```

in every `delta <= 1/4` instance.  The sharp observed ratio is exactly `1`,
attained by the transverse pair and by the rank-3 no-center path for many exact
parameters.  No counterexample or growing family was found.

The best empirical construction is:

```text
choose a max-volume actual-row triangle with minimum Phi among max-volume ties.
```

This matched the full theta-half `Phi`-argmin in all sharp cases and had worst
observed ratio `1`.  Arbitrary max-volume tie choice is not enough for the
sharp `C0=1`: the transverse pair at `a=1/4` has a max-volume tie with
`Phi/delta=5/4`.

## Part 1. Factorization

Fix a theta-half actual-row basis `U=(u_s)`.  Let `A=L L_U^{-1}` and write
`a_t(j)=A[j,t]`.  For a fixed pivot `s`,

```text
lambda(j) = 1 - a_s(j)
mu(j)     = sum_{t != s} (-a_t(j))_+
sigma(j) = sum_{t != s} ( a_t(j))_+
E(j)      = (mu(j) - lambda(j))_+.
```

Since the coordinates sum to `1`,

```text
lambda = sigma - mu,
E      = (sigma - 2 lambda)_+.
```

Put

```text
g(j) = sigma(j) + 2(-lambda(j))_+,
S*_s = sum_j (P_{u_s j})_+ g(j),
Phi_s = sum_j (P_{u_s j})_+ E(j).
```

The key pointwise estimate is stronger than the w40 sketch:

```text
g(j) <= E(j) + 2(lambda(j))_+.
```

Proof by signs:

If `lambda < 0`, then `E=sigma+2(-lambda)=g`.

If `lambda >= 0`, then `g=sigma`.  When `sigma >= 2 lambda`,
`E=sigma-2 lambda`, so `g=E+2 lambda`; when `sigma < 2 lambda`, `E=0` and
`g=sigma < 2 lambda`.

Therefore

```text
S*_s <= Phi_s + 2 Dpos_s,
Dpos_s := sum_j (P_{u_s j})_+ lambda(j)_+.
```

The deficit identity is exact:

```text
0 = sum_j P_{u_s j} lambda(j)
  = Dpos_s - V_s - Dneg_s,

V_s    := sum_j (P_{u_s j})_+ (-lambda(j))_+,
Dneg_s := sum_j (P_{u_s j})_- lambda(j).
```

On positive-beta overshoot rows, `lambda<0` and
`E=sigma+2(-lambda) >= 2(-lambda)`, hence

```text
V_s <= Phi_s/2.
```

In the theta-half class, Cramer gives `|a_t(j)| <= 2`, hence
`lambda(j) <= 3`.  The negative mass of row `u_s` is at most `delta(P)`, so

```text
Dneg_s <= 3 delta(P).
```

Combining,

```text
Dpos_s = V_s + Dneg_s <= Phi_s/2 + 3 delta(P),
S*_s   <= Phi_s + 2 Dpos_s <= 2 Phi_s + 6 delta(P).
```

This is chartwise and does not use minimality.

### Composition with (EX)

Assume `(EX)` with constant `C0`: for every rank-3 `P` with
`delta(P)<=1/4`, there exists a theta-half actual-row chart `U0` with

```text
max_s Phi_s(U0) <= C0 delta(P).
```

Let `U*` be a selected theta-half `Phi`-argmin.  Then

```text
max_s Phi_s(U*) <= max_s Phi_s(U0) <= C0 delta(P).
```

The factorization gives

```text
max_s S*_s(U*) <= (2 C0 + 6) delta(P).
```

Since the repaired pointwise reduction gives `SF_s <= S*_s`, the registry
contract follows with

```text
C_sf = 2 C0 + 6.
```

For the empirical rank-3 value `C0=1`, this would give `C_sf=8`.

## Part 2. Rank-3 exact checks

Artifacts:

```text
rank3_explorer.py
rank3_results.json
rank3_results.txt
rank3_param_scan.json
progress.md
```

No `answer.md` was created.

The harness constructs exact `L,B` with `B L=I`, forms `P=L B`, checks
`P^2=P` and row sums, enumerates every theta-half actual-row triangle, and
computes `Phi`, `S*`, total negative coordinate mass, and the candidate
selectors.

Exact coverage:

```text
valid delta<=1/4 rank-3 instances: 278
  random exact instances:          220
  structured adversarial:           53
  known/restricted families:         5
theta-half charts checked:        2947 in delta<=1/4 records
theta-half charts checked total:  7573 over all valid records
factorization violations:            0
```

Candidate selector maxima over the `278` `delta<=1/4` records:

| selector | worst Phi/delta | count > 1 |
|---|---:|---:|
| full theta-half `Phi`-argmin | `1` | `0` |
| best `Phi` among max-volume ties | `1` | `0` |
| worst max-volume tie | `5/4` | `3` |
| peeled / most-convex chart | `5/4` | `4` |
| min total negative coefficient mass | `5/4` | `4` |

The sharp tie-failure witness is the transverse pair at `a=1/4`:

```text
delta = 1/5
Phi-argmin / best max-volume tie: basis [1,2,3], Phi = 1/5, Phi/delta = 1
bad max-volume / peeled / min-neg: basis [0,1,2], Phi = 1/4, Phi/delta = 5/4
```

Mandatory family restrictions/adaptations:

| family | delta | status | Phi_min/delta |
|---|---:|---|---:|
| transverse pair `a=1/8` | `2/17` | rank 3, inside `delta0` | `1` |
| transverse pair `a=1/4` | `1/5` | rank 3, inside `delta0` | `1` |
| dense pair `k=7` restriction | `1/5` | restricted to rank-3 transverse analog | `1` |
| staircase `m=1` | `1/2` | rank 3 but outside `delta0=1/4` | `1` |
| perturbed staircase `m=1, eps=1/1000` | `1/2` | rank 3 but outside `delta0=1/4` | `997/1000` |
| no-center path `a=1/100` | `1/100` | rank 3, inside `delta0` | `1` |
| no-center path `a=1/4` | `1/4` | rank 3, boundary of `delta0` | `1` |

The staircase rank-3 analog `m=1` is not singular, but it remains pinned at
`delta=1/2`, so it does not test `(EX)` at `delta0=1/4`.

Parametric sharp-family scan:

```text
40 exact transverse/no-center records with delta<=1/4
all have Phi_min/delta = 1
```

Structured adversarial records with `delta<=1/4`:

```text
adversarial_no_center:              15 records, worst Phi/delta = 1
adversarial_balanced_cyclic:         8 records, worst Phi/delta = 0
adversarial_balanced_cyclic_mix:    28 records, worst Phi/delta = 1/17
adversarial_basis windmills:         2 records, worst Phi/delta = 0
```

The windmill and balanced cyclic configurations did not stress `(EX)` once the
left inverse was constrained to keep `delta<=1/4`; either the standard simplex
chart stayed in the theta-half class with `Phi=0`, or a max-volume tie had very
small `Phi`.

## Current obstruction

The computations point to the rank-3 lemma

```text
there exists a max-volume actual-row triangle U with max_s Phi_s(U) <= delta(P).
```

If proved, `(EX)` holds at rank 3 with `C0=1`, and the factorization gives the
selected-chart registry constant `C_sf=8`.

I do not have that proof.  The missing step is a geometric tie-selection
argument for max-area triangles: exact max-volume gives the coordinate box
`|a_t(j)|<=1`, but the proof still has to charge the two rank-3 bad wedges at
each vertex to the negative mass of the pivot row without losing to positive
beta cancellations inside the same wedge.  The transverse and no-center
families show that `C0<1` is false.

## Calibrated probabilities

```text
P(factorization S* <= 2 Phi + 6 delta is correct)        = 0.995
P(the composition C_sf = 2 C0 + 6 is correct)             = 0.99
P(rank-3 EX is true with C0 = 1)                           = 0.78
P(rank-3 EX is false via an unbounded min-chart family)    = 0.08
P(best-max-volume-tie is the right rank-3 construction)    = 0.72
P(arbitrary max-volume / peeled / min-neg selectors suffice with C0=1) = 0.00
```
