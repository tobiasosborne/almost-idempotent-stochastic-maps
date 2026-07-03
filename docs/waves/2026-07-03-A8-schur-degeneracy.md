<!--
ROLE: proof-scoping theory wave for arm A, wave 8: Schur degeneracy payment for GAP B.
STATUS: L3 numerical/exploration report only. Nothing below proves (EX), conj-kernel, or op-classical.
Tier legend: T0 = exact repo-file fact or exact Fraction scratch recomputation;
T1 = elementary derivation / conservative synthesis from T0;
T2 = plausible proof candidate with a live gap;
T3 = speculation.
Worker: codex. Arm A wave 8. Answers bd aism-f3r.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd were not run.
Scratch checker: /tmp/aism_a8_schur.py, pure fractions.Fraction arithmetic.
-->

# Arm A Wave 8: Schur Degeneracy Payment

## T1. Swap Landscape

Source horn, verbatim from `docs/ingest/report/kernel-conjecture-v2.tex:448-454`: "when the multi-row
swap block is not volume-permitted, one needs a theorem that near-degeneracy of the transverse determinant
forces". The rest of that local passage says the forced mass should be `O(delta)`. [T0]

I used the block-swap convention from `kernel-conjecture-v2.tex:500-518` and
`docs/ingest/experiments/out/w40_ndg/proof.md:195-239`: for a chart-coordinate matrix `A`, replacing pivot
positions `I` by rows `J` has Schur block `C=A[J,I]`, volume factor `|det C|`, and transformed coordinates
`x'_I=x_I C^{-1}`, `x'_K=x_K-x_I C^{-1}D`. [T0]

Convention for this wave: a covering swap for active pivot `s` keeps pivot `s` in the chart and brings an
`E_s`-carrying row into one or two transverse pivot positions. This is the only version that can compare
the same pivot functional `Phi_s` before and after the swap. [T1]

Exact coverage: full theta-half enumeration for the two transverse pairs, no-center `k=6,8`, sigma-cap B,
and the balanced staircase; certified reduced theta classes for the fan/multiblock rows; A7 C1 rebuilt
from its description as two pure path fans plus midpoint rows with shared aggregate `t=0`. All checks
`BL=I`, `P^2=P`, and row sums passed exactly. [T0]

| instance | `delta` | `Phi_s(U*)/delta` | `#E_s` rows | max `|det C|` over covering swaps | best covering swap legal? | `Phi_s(V)/delta` after best legal cover | `Phi(V)/delta` after best legal cover |
|---|---:|---:|---:|---:|---|---:|---:|
| transverse `a=1/8` | `2/17` | `1` | `1` | `1/4` | no | `NA` | `NA` |
| transverse `a=1/4` | `1/5` | `1` | `1` | `1/2` | yes | `0` | `3` |
| no-center path `k=6` | `1/100` | `3/2` | `7` | `1/50` | no | `NA` | `NA` |
| no-center path `k=8` | `1/100` | `5/3` | `11` | `1/50` | no | `NA` | `NA` |
| one-anchor star `foreign=9` | `1/100` | `23/16` | `15` | `1/50` | no | `NA` | `NA` |
| repeated star `anchors=3` | `1/100` | `11/8` | `7` per active anchor | `1/50` | no | `NA` | `NA` |
| A7 shared-midpoint path `f=5` | `1/100` | `3/2` | `7` | `1/50` | no | `NA` | `NA` |
| sigma-cap refuter B | `74551/1600000` | `0` | `0` | `0` | no | `NA` | `NA` |
| balanced staircase `m=5,a=1/16` | `30/121` | `20000121/20000000` | `2` | `1/8` | no | `NA` | `NA` |

All legal active-preserving swaps, not only covering swaps, were also enumerated up to block size `2`. The
minimum legal `Phi(V)` equalled `Phi(U*)` in every nonzero case except legal covering swaps for transverse
`a=1/4`: there the same-pivot score drops to `0`, but the chart maximum for covering swaps is `3 delta`.
[T0]

Row support at the active pivot:

- Transverse `a=1/8`: row `p(-1/8)` carries all mass; `beta=8/17`, `E/delta=17/8`, contribution `q/delta=1`,
  row negative mass `=delta`, max covering determinant `1/4`. [T0]
- Transverse `a=1/4`: row `p(-1/4)` carries all mass; `beta=2/5`, `E/delta=5/2`, contribution `1`, row
  negative mass `=delta`, max determinant `1/2`. [T0]
- No-center, star, repeated-star, and A7 fan rows: the carrying rows are exactly the non-selected signed
  rows in the active fan; their `E/delta` values are `1` or `2`, their row negative mass is `delta`, and
  their weighted sums are the table values. [T0]
- Balanced staircase: the carrying rows are `e0` and `x-`. For `e0`,
  `beta=999/1000000`, `E/delta=18997/14985`, contribution `18997/15000000`, row negative mass
  `(121/30000)delta`, max determinant `313/4995`. For `x-`, `beta=95879/242000`, `E/delta=121/48`,
  contribution `95879/96000`, row negative mass `(59999879/60000000)delta`, max determinant `1/8`. [T0]

## T2. Structural Dichotomy

For a one-row active-preserving swap bringing row `j` into transverse position `t`, write
`c=a_t(j)` and `d_l=a_l(j)` for the other old coordinates of `j`. The coordinate transform is

```text
a'_t(i)=a_t(i)/c,
a'_l(i)=a_l(i)-a_t(i)d_l/c  (l != t).
```

In particular `E'_s(j)=0`, because row `j` becomes a non-`s` pivot. [T1]

If one incorrectly had a pivotwise stationarity inequality `Phi_s(U*) <= Phi'_s(V)`, then

```text
beta_s(j)_+ E_s(j)
  <= sum_{i != j} beta_s(i)_+ (E'_s(i)-E_s(i)).
```

This is the exact accounting identity: the removed row must be paid by collateral increases on other rows.
[T1]

But the available variational inequality is only `Phi(U*) <= Phi(V)`, not pivotwise stationarity. The
transverse `a=1/4` row is the red test: a legal covering swap has `Phi'_s(V)=0` while `Phi_s(U*)=delta`;
the max comparison survives only because another pivot rises and `Phi(V)=3delta`. Therefore GAP B cannot be
"single legal swap lowers the active pivot"; it needs a max/collateral horn. [T0/T1]

The proof dichotomy should be:

1. **Legal-collateral horn.** A covering swap with `|det C|>1/2` is available. Stationarity compares the
   chart maxima, so the proof must control the collateral pivots/rows created by the Schur transform. [T1]
2. **Near-degenerate payment horn.** Every active-preserving covering block has `|det C|<=1/2`. Then the
   one-row minors give `|a_t(j)|<=1/2` for every transverse position tested, and the two-row minors say
   that no partner creates a large transverse area with `j`. This is the slab/degeneracy regime needing a
   direct `delta` payment. [T1]

In the fan families the slab is explicit. A reduced chart chooses a signed row `w0` from a zero-average fan
`G`; every signed row `w` has active-coordinate `1` and transverse coordinates `a(w-w0)`. Thus

```text
lambda_s(w)=0,
E_s(w)=a * neg_l1(w-w0),
beta_s(w)=1/|G|.
```

For edge fans `delta=a`, so `Phi_s/delta` is just the average of `neg_l1(w-w0)` over the active fan. This
gives exactly `3/2` for no-center `k=6`, `5/3` for `k=8`, `23/16` for star `foreign=9`, `11/8` for each
active repeated-star anchor, and `3/2` for A7. What pays is not determinant geometry alone; it is the
realized `P=LB`, `BL=I` structure: signed rows have row negative mass `<=delta`, and the active beta row
averages the zero-mean fan. [T0/T1]

The balanced staircase shows why a pointwise slab payment is false-looking. The `x-` row is genuinely
near-degenerate (`max |det C|=1/8`) and has `E/delta=121/48>2`, but its weighted contribution is
`95879/96000 delta`, and its own row negative mass is almost exactly `delta`. The payment must be weighted
and realized; `E_s(j)` alone is the wrong object. [T0/T1]

## T3. Payment Lemma Candidates

**Candidate 1: degenerate row cap with constant `2`.** Statement: if every active-preserving `1`- or
`2`-block covering swap for row `j` has volume factor `<1/2`, then `E_s(j)<=2delta(P)`. [T2]

Verdict: FAIL. Transverse `a=1/8` has `maxdet=1/4` and `E/delta=17/8`; balanced staircase has
`maxdet=1/8` and `E/delta=121/48`. This is the pointwise-`E` dead route in a new coordinate. [T0/T1]

**Candidate 2: determinant-discounted row cap.** Statement: with `m_j` the largest active-preserving
covering determinant for row `j`, `(1-m_j)E_s(j)<=2delta(P)`. [T2]

Verdict: FAIL. The balanced staircase `x-` row gives exact ratio
`(1-1/8)E/delta=847/384>2`. The determinant slab by itself is not the payment. [T0/T1]

**Candidate 3: pivot-total near-degenerate payment.** Statement: for an exact signed idempotent with
`delta<=1/4`, a theta-half `Phi`-argmin `U`, and pivot `s`, let `D_s` be the rows with
`beta_s(j)>0`, `E_s(j)>0`, and no active-preserving `1`- or `2`-block covering swap of volume factor
`>1/2`. Then

```text
sum_{j in D_s} beta_s(j)_+ E_s(j) <= 2 delta(P).
```

This is a single pivot-local statement; it does not sum over pivots or classes. [T2]

Exact zoo test for Candidate 3:

| instance | degenerate rows | degenerate weighted mass / `delta` |
|---|---:|---:|
| transverse `a=1/8` | `1` | `1` |
| transverse `a=1/4` | `0` with strict `>1/2` legality; `1` if the boundary `=1/2` is paid | `0` or `1` |
| no-center path `k=6` | `7` | `3/2` |
| no-center path `k=8` | `11` | `5/3` |
| star `foreign=9` | `15` | `23/16` |
| repeated star `anchors=3` | `7` per active anchor | `11/8` |
| A7 shared-midpoint path `f=5` | `7` | `3/2` |
| sigma-cap B | `0` | `0` |
| balanced staircase `m=5,a=1/16` | `2` | `20000121/20000000` |

Candidate 3 passes the requested zoo with constant `2`; the worst exact value in this zoo is `5/3`.
If the boundary case `|det C|=1/2` is assigned to the payment horn, the composed zoo constant is `2`.
If the boundary is assigned to the legal horn and the legal horn only uses max-stationarity, transverse
`a=1/4` already forces a collateral constant `3`. [T0/T1]

## T4. Wall Check And Verdict

The surviving candidate is not class-count-shaped as stated: it controls one pivot's weighted
near-degenerate mass directly. It becomes wall-shaped if proved by first showing a per-row bound such as
`beta_s(j)E_s(j)<=delta` and then counting rows. The no-center and star rows have growing numbers of
carrying rows; only the beta-weighted fan average keeps the total bounded. [T1]

The candidate is also not coefficient-only. A4's two-atom relaxation would allow large `E` with no row
negative budget. Every successful zoo payment used realizability: either a zero-average fan in `BL=I`, or
an actual row whose negative mass is almost the full `delta` budget. [T1]

I can prove Candidate 3 inline only for the reduced fan templates: the displayed formula gives
`Phi_s/delta = |G|^{-1} sum_w neg_l1(w-w0)`, and the exact finite averages above are `<2`. I do not see an
elementary proof for arbitrary realizable charts. The balanced staircase suggests the general proof must
combine the Schur slab with row-negative budget and harmonic beta identities, not determinant estimates
alone. [T1]

Ranked recommendation:

1. Elevate Candidate 3, preferably with the boundary `|det C|<=1/2` included in the payment horn. This is
   the smallest max-based, non-class-count statement that survived the zoo. [T1/T2]
2. Run wave 9 on the legal-collateral horn: prove or refute that rows with a covering determinant `>1/2`
   can be handled without the transverse `a=1/4` collateral jump breaking `C=2`. [T1]
3. Do not pursue rowwise `E` caps or determinant-discounted row caps; both have exact deaths above. [T0]

Honest verdict: GAP B sharpened, not solved. The open object is now a pivot-local weighted payment plus a
separate legal-collateral comparison, not a pointwise Schur determinant lemma. [T1]
