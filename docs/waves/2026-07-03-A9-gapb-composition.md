<!--
ROLE: independent proof wave for arm A wave 9: GAP B composition after A8.
STATUS: L3/T-tier exploration report only. Nothing below proves (EX), conj-kernel, or op-classical
under repo L0; inline derivations are proof sketches unless later af/Lean/byte-verified.
Tier legend: T0 = exact repo-file fact or exact fractions.Fraction scratch recomputation;
T1 = elementary derivation / conservative synthesis from T0;
T2 = plausible proof candidate with a live gap;
T3 = speculation.
Worker: codex. Arm A wave 9. Answers bd aism-yqo.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd were not run.
Scratch checker: /tmp/aism_a9_gapb.py, pure fractions.Fraction arithmetic.
-->

# Arm A Wave 9: GAP B Composition

## T1. Payment Horn Proof Attempt

I read A8 first and used the registry contract in
`argument/lemmas/conj-degenerate-payment.md` verbatim as the target. The target is the pivot-local
weighted statement

```text
sum_{j in D_s} beta_s(j) E_s(j) <= 2 delta(P),
```

where `D_s` contains positive-beta, positive-`E_s` rows whose active-preserving 1- or 2-block covering
swaps all have Schur volume factor `<=1/2`. Boundary `|det C|=1/2` is therefore paid by this horn in the
registry. [T0]

### Exact payment table

The exact zoo check from A8 remains the best evidence. I recomputed the displayed rational comparisons in
`/tmp/aism_a9_gapb.py` using `fractions.Fraction`; each ratio below is the degenerate payment divided by
`delta(P)`. [T0]

| instance | degenerate payment / `delta` | passes `<=2` |
|---|---:|---|
| transverse `a=1/8` | `1` | yes |
| transverse `a=1/4`, boundary paid | `1` | yes |
| no-center path `k=6` | `3/2` | yes |
| no-center path `k=8` | `5/3` | yes |
| one-anchor star `foreign=9` | `23/16` | yes |
| repeated star `anchors=3` | `11/8` | yes |
| A7 shared-midpoint path `f=5` | `3/2` | yes |
| sigma-cap refuter B | `0` | yes |
| balanced staircase `m=5,a=1/16` | `20000121/20000000` | yes |

The table supports the conjectural constant `2`; it does not prove it. [T0/T1]

### What the row-negative route gives

Let `nu_j=sum_l max(-P_jl,0)`. The only unconditional weighted negative-mass estimate I found is the
trivial one

```text
sum_{j in D_s} beta_s(j) nu_j
  <= delta(P) sum_{j in D_s} beta_s(j)
  <= delta(P) sum_j beta_s(j)_+
  = delta(P) (1 + nu_{u_s})
  <= (5/4) delta(P),
```

using `delta(P)<=1/4`. Thus any proof of

```text
sum_{j in D_s} beta_s(j) E_s(j) <= C sum_{j in D_s} beta_s(j) nu_j
```

would immediately give a universal payment bound `(5C/4) delta(P)`. This would be enough for (EX) with a
worse constant. [T1]

The pointwise version is false at useful constants and probably the wrong object. Exact row diagnostics:

| row | `E_s(j)/nu_j` |
|---|---:|
| transverse `a=1/8` carrier | `17/8` |
| transverse `a=1/4` carrier | `5/2` |
| balanced staircase `e0` | `314000/999` |
| balanced staircase `x-` | `151250000/59999879` |

The `x-` row matches the guide: it has large `E/delta=121/48` and is paid by almost full row negative mass.
But `e0` kills any pointwise own-negativity proof: its beta is tiny, so its weighted contribution is small,
while `E_s(e0)` is huge relative to its own `nu_e0`. [T0/T1]

For the balanced staircase, the weighted own-negativity diagnostic is still favorable:

```text
sum beta E / delta       = 20000121/20000000,
sum beta nu / delta      = 5752786904077/14520000000000,
(sum beta E)/(sum beta nu) = 14520087846000/5752786904077.
```

The last ratio is about `2.52`, so a weighted constant `3` survives this witness. I did not find a proof of
that weighted inequality. [T0/T2]

### Attempted proof mechanism and gap

For any row `j`, idempotence gives the coordinate reproduction identities

```text
a_t(j) = sum_l P_jl a_t(l).
```

A signed measure with negative mass `nu_j` can force an expectation outside the convex hull of the positive
part only by paying with `nu_j`. The natural plan is therefore:

1. choose a transverse test functional built from the negative coordinates of `a(j)`;
2. use the Schur slab and 2-block area bounds to show row `j` is separated from the other actual rows in
   that functional by a gap comparable to `E_s(j)`;
3. convert that separation to `nu_j >= c E_s(j)`;
4. average with weights `beta_s(j)`.

Step 2 is the live failure. The one-block slab gives `|a_t(j)|<=1/2` at transverse positions, and the
two-block minors bound pairwise transverse areas with `j`, but I could not turn those pairwise area
constraints into a dimension-free separating functional. Coefficient-only examples can place many rows on
the same near-degenerate slab line; the missing ingredient must use full realizability, not only the
moments. [T1/T2]

I can still prove the fan-template payment, as in A8. In a reduced edge-fan chart with active fan `G`,
selected row `w0`, and shear scale `a`,

```text
lambda_s(w)=0,
E_s(w)=a * neg_l1(w-w0),
beta_s(w)=1/|G|,
delta(P)=a.
```

Hence the payment divided by `delta` is exactly the finite average
`|G|^{-1} sum_w neg_l1(w-w0)`. Direct exact averaging gives `3/2`, `5/3`, `23/16`, `11/8`, and `3/2` for
the fan rows in the table. This is a template proof only, not a proof of
`conj-degenerate-payment`. [T1]

Verdict for T1: no general payment proof, not even with a worse universal constant. The best next target is
the weighted own-row negative-mass inequality above; the pointwise route is dead. [T1/T2]

## T2. Legal-Collateral Horn

For a one-row active-preserving swap replacing transverse pivot `t` by row `j`, write
`c=a_t(j)` and `d_l=a_l(j)` for `l != t`. The Schur coordinate transform is

```text
a'_t(i) = a_t(i)/c,
a'_l(i) = a_l(i) - a_t(i) d_l/c        (l != t).
```

If pivot `s` is kept, the beta row for pivot `s` is unchanged. Row `j` becomes a non-`s` pivot, so
`E'_s(j)=0`. Define `q_j=beta_s(j) E_s(j)` and

```text
C_s(V) = sum_{i != j} beta_s(i)_+ (E'_s(i)-E_s(i)).
```

Then the same-pivot accounting identity is exact:

```text
Phi'_s(V) = Phi_s(U) - q_j + C_s(V).
```

If `s` attains `M=Phi(U)=Phi_s(U)` and `V` is a legal comparison chart, argmin minimality gives only

```text
M <= max( M - q_j + C_s(V),  Gamma(V) ),
Gamma(V) := max_{r != s} Phi'_r(V).
```

Thus either the same pivot pays the removed row through `C_s(V) >= q_j`, or some collateral pivot has
`Gamma(V) >= M`. This is the exact legal-collateral inequality. It is not an upper bound on `M`. [T1]

The exact transverse `a=1/4` witness shows why this distinction is necessary. In the argmin chart
`U=(1,2,3)`, `delta=1/5`, the active pivot is row `3`, and row `4` contributes exactly `delta`:

```text
a(4)=(-1/2, 1/2, 1), beta_s(4)=2/5, E_s(4)=1/2.
```

The covering swap replacing pivot `2` by row `4` has `|c|=1/2` and new chart `V=(1,4,3)`. The same active
pivot drops to `0`, but the new pivot row `4` has a single collateral contribution from row `2`:

```text
a'_V(2)=(1,2,-2), beta_4(2)=1/5=delta, E'_4(2)=3,
Phi'_4(V)=3 delta.
```

The full new pivot vector is `Phi(V)/delta=(1,3,0)`. This is the exact source of the `3 delta` collateral
jump. [T0]

For comparison, the transverse `a=1/8` row has `|c|=1/4`, so it is not legal under the `1/2` threshold; the
same formal swap would produce `Phi(V)/delta=7`, confirming that Schur distortion alone is too large when
the volume threshold fails. [T0/T1]

A crude legal-swap Lipschitz estimate is circular. From `|c|>1/2` and the theta-half Cramer box one can
bound new coordinates by old coordinates with universal factors, and then bound `Phi'_r(V)` by a universal
multiple of old `S^*_r(U)`. The af-validated factorization gives `S^*_r(U)<=2 Phi_r(U)+6 delta`, so this
has the shape

```text
Phi'_r(V) <= A Phi(U) + B delta
```

with `A>=1` in the available estimates. Minimality then yields `M<=A M+B delta`, which is vacuous. A legal
horn must instead prove a direct collateral cap, for example: if a maximal pivot has a strict legal covering
row, then every collateral pivot created by a chosen legal cover is `O(delta)` for structural reasons not
captured by the crude Schur norm. [T1/T2]

Verdict for T2: exact inequality derived; no general legal-collateral bound. The boundary witness forces
any collateral constant to allow at least `3` if boundary swaps are put in the legal horn. [T1]

## T3. Composition Skeleton

Fix a theta-half `Phi`-argmin `U*` and a pivot `s` attaining `M=Phi(U*)`. Rows with
`beta_s(j)>0` and `E_s(j)>0` split as follows. If every active-preserving 1- or 2-block cover has
`|det C|<=1/2`, put `j in D_s`; otherwise `j` is in the strict legal side. With the registry boundary
convention, there is no third horn: if all transverse coordinates were zero then `E_s(j)=0`. [T1]

The composition would be:

1. **Payment horn**: `sum_{j in D_s} beta_s(j) E_s(j) <= C_p delta(P)`. Current registry conjecture has
   `C_p=2`; this wave did not prove it. [GAP]
2. **Legal-collateral horn**: if the maximal pivot has any strict legal contributor, max-stationarity plus
   collateral control gives `M <= C_l delta(P)`. This wave derived only the exact disjunction
   `M <= max(M-q_j+C_s, Gamma)`, not the needed cap. [GAP]
3. If there is no strict legal contributor, all positive `E_s` mass is in `D_s`, so `M<=C_p delta(P)`.
   [PROVED-INLINE conditional on 1]
4. If there is a strict legal contributor, `M<=C_l delta(P)`. [PROVED-INLINE conditional on 2]
5. Therefore `max_s Phi_s(U*) <= max(C_p,C_l) delta(P)`. Through `lem-factorization`, this would give
   `C_sf=2 max(C_p,C_l)+6`. [T1 conditional]

An alternate row-sum composition, bounding legal row contributions one by one and adding them to the
payment horn, risks the dead unnormalized-sum wall. The max-pivot dichotomy above is the safer skeleton:
payment handles the all-degenerate case; legal-collateral must bound the whole maximal pivot, not count
legal rows. [T1]

## T4. Verdict And Recommendation

No statement from this wave is ready for af elevation as a proof of GAP B. In particular,
`conj-degenerate-payment` should remain `conjecture`; a genuine-gap abort is still likely if elevated now.
[T1]

Af-ready after cleanup: the exact Schur accounting identity for one-row active-preserving swaps is a small
single statement, but it is only bookkeeping and does not close (EX). Draft contract:

```text
For a one-row active-preserving Schur swap replacing transverse pivot t by row j,
Phi'_s = Phi_s - beta_s(j)_+ E_s(j) + sum_{i != j} beta_s(i)_+(E'_s(i)-E_s(i)).
```

This may be worth formalising only as support infrastructure for a later legal horn. [T1]

Next wave recommendation: attack the weighted own-row negative-mass payment

```text
sum_{j in D_s} beta_s(j) E_s(j) <= C sum_{j in D_s} beta_s(j) nu_j
```

or find a counterexample. It composes immediately with the trivial
`sum beta_s nu_j <= (5/4)delta` bound and is exactly where the balanced staircase says the payment lives.
The legal-collateral horn also needs a new idea: crude Schur distortion plus existing factorization is
circular. [T2]

Honest final verdict: GAP B is not solved. The payment horn survived all exact tests but remains open; the
legal horn has a precise max-stationarity disjunction and a sharp `3 delta` boundary stress test, but no
general collateral cap. [T1]
