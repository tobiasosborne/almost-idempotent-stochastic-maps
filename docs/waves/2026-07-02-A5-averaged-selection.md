<!--
ROLE: proof-scoping theory wave for arm A, wave 5: averaged chart selection route to (EX).
STATUS: L0 exploration report only. Nothing below is rigorous or promoted.
Tier legend: T0 = exact repo-file fact or exact Fraction scratch recomputation;
T1 = elementary derivation / conservative synthesis from T0;
T2 = plausible proof skeleton with a live gap;
T3 = speculation.
Worker: codex. Arm A wave 5. Answers bd aism-fpq.
Scope discipline: repo files only; no prior conversation trusted. Created only this file.
Mission override: the user explicitly forbade fr/bd commands, so fr board was not run.
Scratch checker: /tmp/aism_a5_check.py, pure fractions.Fraction arithmetic.
-->

# Arm A Wave 5: Averaged Chart Selection

## Q1. The General Randomization

The fan calculation is real but special. In the certified reduced fan class, a chart is determined by
choosing one signed shear row `w0` from a finite shear set `G`; unit pivots have zero excess, and the anchor
pivot has

`Phi(w0) = a/|G| * sum_{w in G} neg_l1(w-w0)`. [T0:
`runs/2026-07-02-ex-multiblock-coupling/scripts/certify_multiblock_coupling.py:237-241`]

Averaging over `w0 in G` gives

`E Phi = a/|G|^2 * sum_{w,w0 in G} neg_l1(w-w0)`. [T1]

The pointwise triangle estimate is

`neg_l1(w-w0) <= neg_l1(w) + pos_l1(w0)`. [T1]

For the signed edge fan groups tested here, the exact pair averages are:

```text
no_center_k6: |G|=8  pair_avg_neg=25/16
no_center_k8: |G|=12 pair_avg_neg=61/36
star_f9:      |G|=16 pair_avg_neg=23/16
```

Thus `E Phi <= 2a = 2 delta` on those fans, and the exact averages are strictly below `2 delta`. [T0]

For a general exact signed idempotent, I find five candidate randomizations.

1. **Fiber / Schur-swap randomization.** Pick a base chart and swap one pivot inside a candidate fiber, with
   weights from positive beta mass or from chart-row mass. This is canonical on the reduced fans because the
   certified theta class is exactly "all unit rows plus one signed row per anchor". Outside that model it is
   not canonical: fibers depend on the chosen chart and pivot, legal swaps can be empty, and beta-weighted
   swaps are pivot-specific rather than a joint chart distribution. Preservation of `M_{1/2}` holds only
   after conditioning on legal swaps or by rejection. [T1]

2. **Uniform measure on `M_{1/2}`.** This is preserved by definition and is finite, but it is raw-index
   sensitive under cloning unless passed to a quotient first. It also fails the seed constant `2` on small
   examples: transverse `a=1/4` has `E_M[sum_s Phi_s]/delta = 9/4`, and the non-fan sigma-cap instance B
   has `E_M[sum_s Phi_s]/delta = 23268201023/1686045416`. [T0]

3. **Volume-squared measure conditioned on `M_{1/2}`.** This is the clean determinantal candidate. If `X`
   is any full-rank row-coordinate matrix for the actual rows, then
   `Pr(S) proportional det(X_S)^2` is fixed-size volume sampling. By Cauchy-Binet the normalizing constant
   is `det(X^T X)`, and the inclusion kernel is the orthogonal projection
   `K = X (X^T X)^{-1} X^T`; hence row inclusions have the usual projection-DPP negative correlations. [T1]

   This gives closed forms for inclusion probabilities and pair probabilities, but not for `E[Phi_s]`:
   `Phi_s` depends on the inverse basis matrix and on the pivot row of the oblique projection `P=LB`, not
   only on whether a row is included. I found no kernel-only formula for `E[Phi_s]`. [T1]

   Conditioned volume-squared averaging also fails the seed constant `2` in the non-fan instance:
   `E[sum_s Phi_s]/delta = 412090939625/46884974798`. [T0]

4. **Unconditioned volume-squared basis sampling.** This is the honest projection-DPP measure on all actual
   bases, but it does not preserve `M_{1/2}` with probability `1`. Exact conditioning masses computed here:
   transverse `a=1/8`: `Pr(M)=16/17`; transverse `a=1/4`: `Pr(M)=14/15`; perturbed staircase:
   `Pr(M)=154770121/179760132`; no-center `k=6`: `Pr(M)=125000000000000/125200105020001`;
   sigma-cap B: `Pr(M)=2373200/2593799`. [T0] These are benign on the bench but give no dimension-free
   conditioning theorem.

5. **Markov chain on legal volume-permitted Schur swaps.** Rejection at the `M_{1/2}` boundary preserves the
   class. Its stationary law can be made uniform or volume-biased on connected components, so this is not a
   new averaging measure unless one proves connectedness, mixing, and an aggregate drift inequality. It is a
   possible proof language for stationarity, not a finished selector. [T2]

Verdict for Q1: the fan average generalizes only as a conditional scheme: find a clone-quotient chart
distribution supported on `M_{1/2}` whose expected total excess is `O(delta)`. The obvious global choices
do not give the fan constant `2`, and no projection-kernel identity currently evaluates `E[Phi_s]`. [T1]

## Q2. The Simultaneity Crux

The probabilistic-method reduction should target `sum_s Phi_s`, not `max_s Phi_s`, because
`max_s Phi_s <= sum_s Phi_s` eliminates simultaneity if the expected sum is small. [T1]

On the fan families this works exactly: only the anchor pivot carries nonzero excess, so `sum_s Phi_s =
max_s Phi_s`. [T0]

At best charts, the exact bench values are:

| case | delta | best `max Phi/delta` | best `sum Phi/delta` | active pivots `Phi_s>delta/10` | best `Phi_s/delta` |
|---|---:|---:|---:|---:|---|
| transverse `a=1/8` | `2/17` | `1` | `1` | `1` | `[0, 0, 1]` |
| transverse `a=1/4` | `1/5` | `1` | `1` | `1` | `[0, 0, 1]` |
| perturbed staircase `m=5, eps=1/1000` | `1/2` | `1` | `5005003/1000000` | `5` | `[0,0,0,0,0,1,1,1,1,1,5003/1000000]` |
| no-center `k=6` | `1/100` | `3/2` | `3/2` | `1` | `[0,0,0,0,0,3/2]` |
| no-center `k=8` | `1/100` | `5/3` | `5/3` | `1` | `[0,0,0,0,0,0,0,5/3]` |
| multiblock star `foreign=9` | `1/100` | `23/16` | `23/16` | `1` | `[0,0,0,0,0,0,0,0,0,23/16]` |
| sigma-cap refuter B, non-fan | `74551/1600000` | `0` | `0` | `0` | `[0,0,0]` |

The outside-cap perturbed staircase is the warning: even at a selected chart, many pivots can carry
`~delta` excess. I do not see a theorem that only `O(1)` pivots are active under the `(EX)` cap; the bench
inside `delta<=1/4` is consistent with one active pivot, but that is evidence only. [T1]

For averages, `E[sum_s Phi_s]` is small on the reduced fans but not for naive global averaging. Exact ratios:

| case | `M` uniform `E sum/delta` | `M` vol2 `E sum/delta` | all-basis vol2 `E sum/delta` |
|---|---:|---:|---:|
| transverse `a=1/8` | `49/48` | `49/48` | `83/51` |
| transverse `a=1/4` | `9/4` | `3/2` | `21/10` |
| perturbed staircase `m=5, eps=1/1000` | `372450088103/57511500000` | `4444013073500993/773850605000000` | `1361000745195229/224700165000000` |
| no-center `k=6`, reduced `M` | `25/16` | `25/16` | `17608303504847597/10016008401600080` |
| no-center `k=8`, reduced `M` | `61/36` | `61/36` | not computed in this wave |
| multiblock star `foreign=9`, reduced `M` | `23/16` | `23/16` | not computed in this wave |
| sigma-cap B, non-fan | `23268201023/1686045416` | `412090939625/46884974798` | `468117246369933/40994505560788` |

The sum route is therefore the right simultaneity interface, but it needs a special aggregate measure. It is
not enough to average over all theta charts or over volume-squared theta charts. [T1]

## Q3. Realizability Input

The fan proof uses realizability in three places.

First, `P=LB` and `BL=I` make the signed rows harmonic: the positive beta mass on the fan is uniform and the
shear set has zero average. Without this, the formula
`Phi = a/|G| * sum_w neg_l1(w-w0)` is not available. [T1]

Second, `delta(P)` is not an abstract coordinate scale. In the fans it is exactly `a * max_w neg_l1(w)`,
and the tested edge fans have `max_w neg_l1(w)=1`, so `delta=a`. That is where the bound
`E Phi <= 2 delta` enters. [T0/T1]

Third, all row-negativity bounds are row bounds for the actual oblique projection `P=LB`, not for arbitrary
chart coefficients. A coefficient-only relaxation is dead: A4's two-atom moment witness has zero pivot
negative mass and arbitrarily large `Phi`. [T0/T1: `docs/waves/2026-07-02-A4-aggregate-charge.md`]

This is the essential obstruction to a general proof. The DPP kernel sees the geometry of actual rows; the
fan formula also needs how positive beta mass is placed on coordinate-excess rows by the oblique projection.
`delta` enters through `P` row negativity and the exact harmonic identities, not through volume geometry
alone. [T1]

## Q4. Bench

All entries below were recomputed by `/tmp/aism_a5_check.py` using `fractions.Fraction`. The checker rebuilds
`L,B`, verifies `BL=I`, `P^2=P`, row sums, exact `delta`, enumerates or uses the certified reduced
theta-half class, and computes the chart excess definitions from
`docs/ingest/report/kernel-conjecture-v2.tex:81-151`. [T0]

Key scratch excerpt:

```text
CASE transverse_pair_a1_8 n=5 k=3 delta=2/17 theta=3 checks={BL: True, P2: True, rowsum: True}
  best max/d=1 sum/d=1 phi_s/d=[0, 0, 1]
  M_unif: Emax/d=49/48 Esum/d=49/48 Ephi_s/d=[17/48, 0, 2/3]
  M_vol2: Emax/d=49/48 Esum/d=49/48 Ephi_s/d=[17/48, 0, 2/3]
  All_vol2: Emax/d=299/204 Esum/d=83/51 Ephi_s/d=[55/102, 3/17, 31/34] Pr(M)=16/17

CASE transverse_pair_a1_4 n=5 k=3 delta=1/5 theta=5 checks={BL: True, P2: True, rowsum: True}
  best max/d=1 sum/d=1 phi_s/d=[0, 0, 1]
  M_unif: Emax/d=37/20 Esum/d=9/4 Ephi_s/d=[13/20, 3/5, 1]
  M_vol2: Emax/d=19/14 Esum/d=3/2 Ephi_s/d=[1/2, 3/14, 11/14]
  All_vol2: Emax/d=5/3 Esum/d=21/10 Ephi_s/d=[4/5, 1/3, 29/30] Pr(M)=14/15

CASE no_center_path_k6 n=13 k=6 delta=1/100 theta=8 checks={BL: True, P2: True, rowsum: True}
  best max/d=3/2 sum/d=3/2 phi_s/d=[0, 0, 0, 0, 0, 3/2]
  M_unif: Emax/d=25/16 Esum/d=25/16 Ephi_s/d=[0, 0, 0, 0, 0, 25/16]

CASE no_center_path_k8 n=19 k=8 delta=1/100 theta=12 checks={BL: True, P2: True, rowsum: True}
  best max/d=5/3 sum/d=5/3 phi_s/d=[0, 0, 0, 0, 0, 0, 0, 5/3]
  M_unif/M_vol2: Emax/d=61/36 Esum/d=61/36 Ephi_s/d=[0,0,0,0,0,0,0,61/36]

CASE multiblock_star_foreign9 n=25 k=10 delta=1/100 theta=16 checks={BL: True, P2: True, rowsum: True}
  best max/d=23/16 sum/d=23/16 phi_s/d=[0,0,0,0,0,0,0,0,0,23/16]
  M_unif/M_vol2: Emax/d=23/16 Esum/d=23/16 Ephi_s/d=[0,0,0,0,0,0,0,0,0,23/16]

CASE sigma_cap_refuter_B_nonfan n=5 k=3 delta=74551/1600000 theta=4 checks={BL: True, P2: True, rowsum: True}
  best basis=(0, 1, 2) max/d=0 sum/d=0 phi_s/d=[0, 0, 0]
  M_unif: Emax/d=23268201023/1686045416 Esum/d=23268201023/1686045416
  M_vol2: Emax/d=412090939625/46884974798 Esum/d=412090939625/46884974798
  All_vol2: Emax/d=109308589266698/10248626390197 Esum/d=468117246369933/40994505560788 Pr(M)=2373200/2593799
```

The long outside-cap perturbed staircase vector is:

```text
best phi_s/d=[0,0,0,0,0,1,1,1,1,1,5003/1000000], sum/d=5005003/1000000
M_unif Esum/d=372450088103/57511500000
M_vol2 Esum/d=4444013073500993/773850605000000
All_vol2 Esum/d=1361000745195229/224700165000000, Pr(M)=154770121/179760132
```

The non-fan sigma-cap B theta charts explain the failure of naive averaging:

```text
delta 74551/1600000, theta_count 4
(0,1,2) vol=1       max/d=0
(1,2,4) vol=257/400 max/d=582786825/38319214
(0,1,3) vol=11/20   max/d=15578537/820061
(1,2,3) vol=1/2     max/d=1565295/74551
```

Thus the best chart can be perfect while most theta charts are bad. This is a precise death certificate for
"average over the whole theta class" as a `C0=2` proof. [T0/T1]

## Q5. Verdict

There is an elementary averaged-selection lemma:

**Conditional averaged-selection lemma.** Let `P` be an exact signed idempotent and let `m_P` be a probability
measure supported on `M_{1/2}(P)`. If

`E_{U~m_P} sum_s Phi_s(U) <= C delta(P)`,

then there exists `U0 in M_{1/2}(P)` with `max_s Phi_s(U0) <= C delta(P)`. [T1]

This is af-elevatable but nearly tautological: it packages the probabilistic method and moves all difficulty
to the expected-sum hypothesis. [T1]

The sharpest non-tautological version I can defend is:

**Proposed aggregate-measure hypothesis.** For every rank-`>=3` exact signed idempotent `P` with
`0<delta(P)<=1/4`, there exists a clone-quotient probability measure `m_P` on `M_{1/2}(P)`, constructed
from `P=LB`, `BL=I`, row positive/negative mass, and volume-permitted Schur exchanges, such that
`E_{m_P} sum_s Phi_s <= C delta(P)` for a universal `C`. [T2]

Unproved hypotheses, each single-statement:

1. **Support hypothesis:** the constructed measure is supported on `M_{1/2}(P)` without a dimension-dependent
   conditioning loss. [T2]
2. **Aggregate charge hypothesis:** under that measure,
   `E sum_s Phi_s <= C delta(P)`. [T2]
3. **Clone-quotient invariance:** splitting identical actual rows refines the measure but does not change the
   induced weighted chart-excess law. [T2]
4. **Realizability charge:** the aggregate bound uses `P=LB`, `BL=I`, and all-row negativity
   `nu_i(P)<=delta(P)`; no coefficient-only relaxation is sufficient. [T1]

Wall/dead-route check:

- Uniform theta averaging is clone-sensitive and fails `C0=2`. [T0/T1]
- Conditioned volume-squared averaging is canonical and clone-friendlier, but fails `C0=2` on the non-fan
  sigma instance and has no kernel-only `Phi` formula. [T0/T1]
- A proof that decomposes by bad fibers/classes and sums per-class estimates re-imports the B4 class-count
  wall. [T1]
- This is not the recorded Jensen death by itself. The valid step here is
  `E[f(U)] <= C delta => exists U with f(U)<=C delta`; it does not replace `f(U)` by
  `f(E[U])` or use convexity of a chart functional. The Jensen refuter applies only if one tries to pass to
  a chart of averaged rows or to an upper bound from a convex function of averages. [T1]

Final verdict: the fan selection-by-averaging is a strong structural hint, not a general proof. It survives
as a probabilistic-method interface for `sum_s Phi_s`, but the natural global chart measures tested here do
not give the desired aggregate estimate. The next live object is the aggregate-measure hypothesis above; the
current naive averaged-selection route is killed as a `C0=2` theorem. [T1]

## Ranked Recommendation

1. **Elevate only the conditional probabilistic-method lemma if a small af target is wanted.** It is clean
   and true-looking, but it will not close `(EX)` without the aggregate hypothesis. [T1]
2. **Next wave:** build the clone-quotient aggregate measure explicitly. It must be neither uniform over raw
   charts nor plain volume-squared over theta charts. Test first on sigma-cap B, where bad theta charts expose
   the failure mode. [T1]
3. **Pivot if the measure decomposes per class.** Any per-fiber/per-wedge proof that needs a dimension-free
   count is wall-shaped and should be stopped early. [T1]
4. **Do not pursue a projection-kernel-only proof of `E[Phi]`.** Volume DPP kernels give row inclusion
   identities, but `Phi_s` is inverse-chart and oblique-beta nonlinear; the bench already shows volume alone
   is not enough. [T1]
