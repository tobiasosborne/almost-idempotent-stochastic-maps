# W25 worker N report -- step-4 obstruction certificate

Verdict: **INSUFFICIENT** relative to the scalar step-4 fact surface.  The exact checker
`runs/2026-07-06-w25-step4-decider/scripts/w25_worker_n.py` gives a rational model satisfying the
listed conclusions with a one-point self-sustaining web `{g >= 1/2}` and `H > 13*tau`.

## Model

[T1] Constants:

- `delta = 1/100`, `tau = 1/10`, `rho = 4*tau = 2/5`, `kappa = tau/4 = 1/40`.
- `delta < delta_1 = (17 - 12*sqrt(2))/2` is checked exactly by squaring
  `12*sqrt(2) < 17 - 2*delta`.
- `H = 2`, so `H = 20*tau > 13*tau`.

[T1] Coefficient matrix:

```text
P =
  w: [1,       0,      0]
  v: [0,       1,      0]
  s: [101/100, -1/100, 0]
```

This is an exact signed idempotent coefficient matrix: `P*1=1` and `P^2=P`.  The row negative
masses are `nu_w=0`, `nu_v=0`, `nu_s=1/100`, hence `delta(P)=1/100`.

[T1] Abstract labels:

- visible label `W={w}`;
- hidden vertices `{v,s}`;
- hidden top `{v}`;
- depths to the abstract visible hull `C_W={p_w}`:
  `d_w=0`, `d_v=H=2`, `d_s=1/50`.

These depths agree with the literal `ell^1` distances to `conv{p_w}` for this chosen abstract
`W`, but this `W` is intentionally not the canonical visible set of the row geometry.

## Facts Certified

[T1] Generic row facts:

- row sums are `1`;
- `P^2=P`, so `P*(P*1_S)=P*1_S` for every fixed column set `S` (the script checks all `2^3`
  subsets);
- `nu_i <= delta` for every row;
- mass split `sum_j P_ij^+ = 1 + nu_i` for every row;
- all row-pair `ell^1` distances are at most `2+4*delta`;
- the sandwich `sigma_S(i)-nu_i <= (P*1_S)_i <= sigma_S(i)` is checked for every column subset
  `S`, hence for every halo width.

[T1] Step-4 surface at width `a=4`:

- `G_4={j:d_j>4*tau}={v}`.
- `g=P*1_{G_4}=(0,1,-1/100)` and `P*g=g`.
- The visible row is small: `-nu_w=0 <= g_w=0 <= 4*tau=2/5`.
- The hidden top is high: `g_v=1 > 1/2-delta = 49/100`.
- Parametric-collapse conclusion is satisfied at the top: `sigma_4(v)=1`, `sigma(v)=1`, so
  `H*(1-sigma_4)=0`.
- Genuine disintegration is satisfied with identity vertex representations.  For the only web
  row `v`, all mass is `v -> v` with `M_v=1` and slack `(H-d_v)/(H-4*tau)=0`.

Thus the imported conclusions permit the stable web `v -> v` at level `g=1`, while the abstract
visible row remains at `g=0`.

## Missing True Input

[T1] The certificate is **not** a counterexample to the Kernel conjecture or to the reviewed
lemmas, because it violates the actual `def-visible-set` / `def-exposed` geometry.  In the real
row geometry, the supposed hidden top `v` is visibly exposed:

- `v` is a row vertex; any convex combination of `w` and `s` has first coordinate at least `1`,
  while `p_v` has first coordinate `0`.
- The affine function `h(x)=(100/101)x_0` has `h(p_v)=0` and values
  `h(p_w)=100/101`, `h(p_s)=1`, all in `[0,1]`.
- Both `w` and `s` are `rho`-far from `v`, and the far-row margin is `100/101 >= kappa=1/40`.

So canonical exposedness would put `v` in `W(P)`, erasing the advertised hidden top.  The step-4
facts are therefore blind to the essential extra geometric assertion: a high, deep, self-sustaining
`g` state cannot remain hidden once the full exposedness/W-hull geometry is enforced.

## Consequence For The Prover

[T1] Any proof of step 4 from only harmonicity, visible smallness, top forced mass, generic
row-signed facts, and the step-3 disintegration inequality is impossible: those facts have the
model above.  A successful proof must import additional geometric structure, most likely one of:

- full canonical exposedness of hidden tops, not merely Lemma A's consequence on already-visible rows;
- convex relations imposed by the true `W(P)` hull;
- a depth ledger such as a re-established `obs-deep-leakage`;
- another true-for-idempotents anti-self-loop principle excluding the `v -> v` web.

[T1] The sharp obstruction mode is self-support: the disintegration slack is zero at the top, but
the mass disintegrates entirely onto the same hidden top.  No count-free contradiction appears until
some external geometric input forbids that top from being hidden.
