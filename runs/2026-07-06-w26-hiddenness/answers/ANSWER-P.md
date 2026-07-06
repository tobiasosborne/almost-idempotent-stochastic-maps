PARTIAL (proved: hiddenness LP-dual witness and top-slab far-row consequence; gap: no inequality couples that witness to row-v positive mass `sigma_4`)

[T0] Let `v` be hidden and set `F_v={j: ||p_j-p_v||_1 >= rho}`. The exposedness LP is

```text
maximize t
over affine h with h(p_v)=0
subject to 0 <= h(p_i) <= 1 for all i,
           t <= h(p_f) for all f in F_v.
```

Writing `h(x)=u.(x-p_v)`, its dual is:

```text
minimize sum_i beta_i
subject to lambda_f, alpha_i, beta_i >= 0,
           sum_{f in F_v} lambda_f = 1,
           sum_f lambda_f (p_f-p_v) + sum_i alpha_i (p_i-p_v)
             = sum_i beta_i (p_i-p_v).
```

Strong LP duality applies. Since `v` is hidden, `t*(v)<kappa`, so there are witnesses with
`B:=sum_i beta_i < kappa`.

Equivalently,

```text
sum_f lambda_f p_f + sum_i alpha_i p_i - sum_i beta_i p_i
  = (1 + A - B) p_v,    A=sum_i alpha_i.
```

Thus hiddenness gives a signed “surrounding” certificate: one unit of positive mass is forced onto `rho`-far rows, balanced by arbitrary positive slack and by negative slack of total `< kappa`.

[T0] Pairing this witness with any affine `psi` satisfying `psi(p_v)=0` and `0<=psi(p_i)<=E` gives

```text
sum_f lambda_f psi(p_f) + sum_i alpha_i psi(p_i)
  = sum_i beta_i psi(p_i) <= B E < kappa E.
```

So the `lambda`-average of `psi` over `rho`-far rows is `< kappa E`.

[T1] For a hidden top `v`, use the support functional from `lem-top-concentration`: affine `phi` with
`phi(p_v)=H`, `phi<=0` on `C_W`, `||phi||_Lip(l1)<=1`, and `0 <= H-phi(p_i) <= D:=2+4delta`.

Set `psi=H-phi` and `E<=D`. The hiddenness witness gives a `rho`-far row `f` with

```text
H - phi(p_f) < kappa D = (tau/4)(2+4delta) = (1/2 + delta) tau.
```

Since `phi(p_f) <= d_f := dist_1(p_f,C_W) <= H`,

```text
d_f > H - (1/2 + delta)tau.
```

Under the target constants `delta <= (17-12sqrt(2))/2` and `H>13tau`, this is

```text
d_f > (13 - (1/2 + delta))tau
    >= (4 + 6sqrt(2))tau
    > 4tau.
```

So every hidden top has a `rho`-far row in `G_4` lying within `(1/2+delta)tau` of the top height.

[T2 gap] This does consume hiddenness, but it still does not cap `sigma_4(v)`. The dual certificate has two missing controls:

1. The positive slack `alpha` is unbounded, so the far-row unit `lambda` need not represent a controlled fraction of any row-reproduction mass.

2. The witness is geometric; it is not tied to the actual coefficients `P_vj^+` whose sum defines `sigma_4(v)`. In particular, it can prove existence of far top-slab rows, but not that the top row places small positive mass on `G_4`.

So I cannot honestly derive the MIN-A contradiction. The codifiable partial is the hiddenness dual-witness lemma plus the top-slab consequence above; the remaining missing lemma must couple this witness to the row coefficients, or separately cap the self/near-top contribution to `sigma_4`.