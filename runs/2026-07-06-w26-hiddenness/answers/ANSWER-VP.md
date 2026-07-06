VALID-WITH-CORRECTIONS (both claims survive; Claim 1’s strict `psi` inequality needs `E>0`, otherwise only `<=`)

**Dual Derivation**

[T0] Let `a_i = p_i - p_v` and `F = F_v`. Since admissible exposers are affine with `h(p_v)=0`, write `h(p_i)=u.a_i`. The primal is exactly:

```text
maximize t
subject to t - u.a_f <= 0        f in F
          -u.a_i <= 0            all rows i
           u.a_i <= 1            all rows i
```

with `u,t` free. This matches the shards: box constraints are over all row indices, `F` is all rows with `||p_f-p_v||_1 >= rho`, and duplicates remain row indices though zero differences vanish.

The dual is:

```text
minimize sum_i beta_i
subject to sum_f lambda_f = 1
          sum_f lambda_f a_f + sum_i alpha_i a_i = sum_i beta_i a_i
          lambda, alpha, beta >= 0
```

This is the prover’s dual. Feasibility: `u=0,t=0`. Boundedness: hidden implies `F` is nonempty, because the shard sets `t*=+infty` when no far row exists; then `t <= h(p_f) <= 1`. Closed finite LP gives attainment and strong duality. Since hidden means `t*(v)<kappa`, an optimal dual witness has `B=sum beta_i=t*(v)<kappa`.

[T1] Pairing is valid. For affine `psi` with `psi(p_v)=0`, its linear part applied to the balance gives

```text
sum_f lambda_f psi(p_f) + sum_i alpha_i psi(p_i)
= sum_i beta_i psi(p_i).
```

If `0 <= psi(p_i) <= E`, then `sum lambda psi(p_f) <= B E`. This is strictly `< kappa E` only when `E>0`. If `E=0`, take `psi=0`: the left side is `0`, so the strict statement `0 < 0` is false. That is the only correction I found.

**Claim 2**

[T1] The support functional use is sound. From `ell^1/ell^infty` separation, there is affine `phi` with `phi(p_v)=H`, `phi<=0` on `C_W`, and `||phi||_Lip<=1`. Hence for every row,

```text
phi(p_i) <= d_i := dist_1(p_i,C_W) <= H
0 <= H - phi(p_i) <= D := 2 + 4 delta.
```

Apply Claim 1 with `psi=H-phi` and `E=D>0`. Then some `f in F_v` has

```text
H - phi(p_f) < kappa D = (tau/4)(2+4 delta) = (1/2 + delta) tau.
```

Since `phi(p_f) <= d_f`, this gives

```text
d_f > H - (1/2 + delta) tau.
```

The constants check exactly:

```text
13 - (1/2 + (17 - 12 sqrt(2))/2)
= 4 + 6 sqrt(2) > 4.
```

So under `H>13 tau`, `d_f > 4 tau`; and because `f in F_v`, also `||p_f-p_v||_1 >= 4 tau`. Thus `f in G_4`.

**Exact Fixture**

[T1] I used the exact W19 duplicate-split fixture from [worker-report.md](/home/tobias/Projects/almost-idempotent-stochastic-maps/runs/2026-07-06-w19-sigma-frontier/data/worker-report.md): the `m=4, q=5/84` 7x7 matrix.

Exact recomputation over `Fraction`s:

```text
delta = 1/16, tau = 1/4, rho = 1, kappa = 1/16
W = {0,1,2}, hidden vertices = {3,4,5,6}
v = 3
F_v = {0,1,2}
distances from v = [11/10, 1, 21/10, 0, 0, 0, 0]
t*(v) = 1/21 < 1/16
```

Optimal primal exposer:

```text
u = (-20/21, -20/21, 0, 0, 0, 0, 0)
h-values = [1/21, 1/21, 1, 0, 0, 0, 0]
```

Dual witness:

```text
lambda_0 = 10/21, lambda_1 = 11/21
beta_2 = 1/21
all alpha_i = 0, all other beta_i = 0
B = 1/21 < 1/16
```

The balance equation holds exactly, and with `psi=h`, `E=1`:

```text
sum_f lambda_f psi(p_f) = 1/21 < 1/16 = kappa E.
```

**Minimal Hypotheses**

Claim 1 needs: finite row set from `P`; `v` a hidden row vertex under the shard definitions; `F_v` as the `rho`-far row-index set; and `E>0` for the strict consequence. With `E=0`, replace strict `<` by `<=`.

Claim 2 needs: exact signed idempotent `P`; `0 < delta(P) <= (17-12*sqrt(2))/2`; nonempty `W(P)`; `v` a hidden top vertex with height `H`; and `H>13 tau`. No invisible-mass or coefficient-mass hypothesis is used.