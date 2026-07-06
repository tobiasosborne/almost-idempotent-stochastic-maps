FORCED-STRUCTURE (statement: true hiddenness is exactly a dual/gauge witness: for a hidden vertex v, a convex combination of rho-far rows lies within kappa*(2+4*delta) in ell-1 of p_v; the W25 self-loop model has no such witness and becomes visible)

# W26 Worker Q report -- hiddenness obstruction audit

## Scope and verdict

[T1] I did **not** find a second insufficiency certificate satisfying F0-F10 with a sustained
`G_4` web and `H > 13*tau`.

[T0/T1] The useful output is the exact hiddenness dual form.  It is not a full proof of
`conj-min-a-w4`, but it is the first forced structure that the W25 scalar model did not satisfy:
hiddenness forces a near barycenter of rho-far rows around every labeled-hidden vertex.

[T3] The search component is bounded evidence only: Lambda-C generated exact signed idempotents,
`n <= 10`, `1000` samples, exact rational LPs for row-vertex, exposedness, and distance checks.
No emptiness claim is made.

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 runs/2026-07-06-w26-hiddenness/scripts/w26_worker_q.py --samples 1000
```

## Forced hiddenness dual

[T0] For a row vertex `v`, let

`F_v = {j : ||p_j - p_v||_1 >= rho}`.

The primal exposedness LP is

```text
t*(v) = max t
subject to h affine, h(p_v)=0,
           0 <= h(p_i) <= 1 for every row i,
           h(p_j) >= t for every j in F_v.
```

By finite LP duality/minimax, this equals the gauge LP

```text
min alpha = sum_i beta_i
subject to mu in Delta(F_v), beta_i >= 0,
           sum_{j in F_v} mu_j p_j - p_v
             = sum_i beta_i (p_i - p_v).
```

Thus `t*(v) < kappa` forces an exact witness:

```text
q_far = sum_{j in F_v} mu_j p_j in conv{rho-far rows from v},
||q_far - p_v||_1 <= alpha * D < kappa * (2 + 4*delta),
```

where `D` is the row diameter.  Since each row in `F_v` is individually at distance at least
`rho = 4*tau`, hiddenness says the far rows must convexly fold back near `p_v`.  This is precisely
what the W25 one-point self-loop model lacks.

## W25 re-audit under canonical geometry

[T1] Matrix:

```text
w: [1, 0, 0]              nu=0
v: [0, 1, 0]              nu=0
s: [101/100, -1/100, 0]   nu=1/100
```

[T1] Exact audit:

```text
delta = 1/100
canonical W = [v, s]
hidden vertices = []
H = 0
G_4 = []
g = [0, 0, 0]
t*(v) = 100/101  (VISIBLE)
t*(s) = 1        (VISIBLE)
```

So W25's old abstract label `W={w}`, hidden top `v`, is not geometrically honest once F9/F10
are imposed.  Hiddenness closes exactly that loophole.

## True-hidden calibration

[T1] The script also audited a known exact true-hidden rank-5 calibration from the pipeline.
It shows the dual witness in action, but it is not tall and it is outside the current delta
window.

```text
delta = 49/2000
W = [r0, r1, r2]
hidden = [r3, r4]
H = 1/20
H^2/delta = 5/49
G_4 = []
t*(r3) = t*(r4) = 1/41  (HIDDEN)
```

Matrix:

```text
r0: [99/100, -21/2000, 1/2000, 1/100, 1/100]
r1: [-1/100, 1979/2000, 1/2000, 1/100, 1/100]
r2: [-1/100, -21/2000, 2001/2000, 1/100, 1/100]
r3: [289/600, 3137/6000, -49/2000, 1/100, 1/100]
r4: [299/600, 3037/6000, -49/2000, 1/100, 1/100]
```

Exact dual witnesses:

```text
r3:
  alpha = 1/41 = t*(r3)
  far rows = [r0, r1, r2]
  mu = {r0: 59/123, r1: 64/123}
  beta = {r2: 1/41}
  ||p_r3 - q_far||_1 = 1/20 = alpha*D

r4:
  alpha = 1/41 = t*(r4)
  far rows = [r0, r1, r2]
  mu = {r0: 61/123, r1: 62/123}
  beta = {r2: 1/41}
  ||p_r4 - q_far||_1 = 1/20 = alpha*D
```

This is the geometric pattern a valid F0-F10 obstruction must have: every hidden carrier needs
rho-far rows whose convex hull comes back within the kappa-scale cone of that carrier.

## Small exact search

[T3] Search summary:

```text
seed = 26017
samples = 1000
audited exact idempotents with 0 < delta <= 1/4 = 115
hidden vertex records = 5
tall13 records = 0
delta-window audited = 2
hidden vertex records in delta-window = 1
tall13 records in delta-window = 0
F0-F10 sustained tall web found = no
```

[T3] Best `H/tau` record in the bounded search:

```text
n = 6, k = 4, m = 2
delta = 1/160
H = 1/80
H^2/delta = 1/40
H/tau ~= 0.158114
W = [x0, x1, x2, x3, x4]
hidden = [x5]
G_4 = []
sustained top = []
```

Matrix:

```text
x0: [1, 0, 0, 0, 0, 0]
x1: [0, 1, 0, 0, 0, 0]
x2: [0, 0, 1, 0, 0, 0]
x3: [0, 0, 0, 1, 0, 0]
x4: [0, 0, 0, 1, 0, 0]
x5: [1189/1600, -1/160, 1/4, 21/1600, 0, 0]
```

## What remains relaxed / open

[T1] The scripted audits did not relax exact idempotence, row sums, negative mass, canonical
visible/hidden classification, or real distances to `conv W`.

[T3] The generator search is not an exhaustive feasibility proof.  It only says that this
bounded exact search found no geometrically honest replacement for W25's self-loop certificate.

[T1] The next obstruction/prover interface should consume the dual witnesses for **all deep
carrier vertices**, not just the top label.  A future insufficiency certificate must build a
sustained `G_4` carrier web while every hidden carrier has a rho-far barycenter returning within
`kappa*(2+4*delta)` of that carrier.  That is the named geometric constraint missing from W25.
