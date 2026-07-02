<!--
ROLE: proof-scoping theory wave for fr arm A, wave 4: aggregate charge route for (EX).
STATUS: L0 exploration report only. Nothing below is rigorous or promoted.
Tier legend: T0 = exact repo-file computation/provenance or exact scratch recomputation;
T1 = elementary derivation or conservative synthesis from T0; T2 = plausible proof skeleton;
T3 = speculation. Worker: codex. Arm A wave 4. Answers bd aism-oia.
Scope discipline: repo files only; no prior conversation trusted. Created only this file.
Note: the mission explicitly forbade `fr` and `bd`; those commands were not run.
-->

# Arm A · Wave 4 · Aggregate Charge Proof Skeleton

## 0. Skeleton Overview

The target is the existential `(EX)` form: every rank-`>=3` exact signed idempotent
`P` with `delta(P)<=1/4` has a theta-`1/2` actual-row chart `U0` with
`max_s Phi_s(U0) <= C0 delta(P)` for some universal constant. [T0:
`argument/lemmas/conj-ex.md`; `docs/ingest/report/kernel-conjecture-v2.tex:219-231`]

The clean proof interface is variational: choose a `Phi`-argmin `U*` over the finite
class `M_{1/2}(P)` and prove `max_s Phi_s(U*) <= C0 delta(P)`. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:328-346`; A1]

The strongest honest skeleton I can isolate is:

1. PROVED-inline: the argmin interface is lossless for `(EX)`. [T1]
2. PROVED-inline: fixed-chart harmonicity gives a useful moment system, but a
   beta-row-only LP certificate is impossible. [T1]
3. PROVED-inline: argmin comparison against volume-permitted Schur swaps is valid,
   but it is a stationarity inequality, not a single-swap descent theorem. [T1]
4. GAP: a realizable aggregate charge lemma is still needed; it must use either
   chart optimality through all volume-permitted swaps or the full `P=LB`, `BL=I`
   row-negativity geometry. [T2]

The irreducible gap is not pointwise high `E`, not zero overshoot, and not a
per-class count. It is a global weighted charge:

`sum_j (P_{u_s j})_+ E_s(j) <= C delta(P)` at a theta-half `Phi`-argmin. [T2]

## 1. Step-By-Step Derivations

### Step 1. Argmin Interface

For fixed `P`, the set of actual-row bases is finite, and `M_{1/2}(P)` is nonempty
because it contains every max-volume actual-row basis. [PROVED-inline, T1]

Therefore the function `Phi(U)=max_s Phi_s(U)` has a minimizer `U*` over
`M_{1/2}(P)`. [PROVED-inline, T1]

If `(EX)` supplies any chart `U0 in M_{1/2}(P)` with `Phi(U0)<=C0 delta(P)`, then
minimality gives `Phi(U*)<=Phi(U0)<=C0 delta(P)`. [PROVED-inline, T1]

Conversely, a universal bound on every such `Phi`-argmin immediately gives the
existential `(EX)` chart by taking `U0=U*`. [PROVED-inline, T1]

Thus the proof target can be stated as the single argmin lemma:

**GAP A.** There is a universal constant `C` such that for every rank-`>=3` exact
signed idempotent `P` with `0<delta(P)<=1/4`, every theta-`1/2` `Phi`-argmin
`U*` satisfies `max_s Phi_s(U*) <= C delta(P)`. [GAP, T2]

This statement is af-elevatable as written: it is single, finite-dimensional,
and has no selector algorithm. [T1]

### Step 2. Fixed-Chart Harmonic System

Fix a chart `U=(u_1,...,u_k)` and pivot `s`. The coordinates satisfy
`p_j=sum_t a_t(j) r_t`, `sum_t a_t(j)=1`, and the full harmonic identities
`sum_j beta_s(j) a_t(j)=delta_st`, where `beta_s(j)=P_{u_sj}`. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:115-129`]

For the pivot,
`lambda_s(j)=1-a_s(j)`, `mu_s(j)=sum_{t!=s}(-a_t(j))_+`,
`sigma_s(j)=sum_{t!=s}(a_t(j))_+`, and
`E_s(j)=(mu_s(j)-lambda_s(j))_+`. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:130-149`]

Since `lambda_s=sigma_s-mu_s`, the identities
`E_s=(sigma_s-2 lambda_s)_+=(2 mu_s-sigma_s)_+` hold pointwise. [PROVED-inline,
T1]

The scalar deficit identity
`sum_j beta_s(j) lambda_s(j)=0` is the sum of the off-pivot harmonic equations.
[T0: `docs/ingest/report/kernel-conjecture-v2.tex:260-270`]

Splitting signs gives
`Dpos_s - V_s = Dneg_s`, with
`Dpos_s=sum beta_s^+ lambda_s^+`,
`V_s=sum beta_s^+ (-lambda_s)_+`, and
`Dneg_s=sum beta_s^- lambda_s`. [PROVED-inline, T1]

The known factorization uses the theta-half box `|a_t(j)|<=2`, hence
`lambda_s(j)<=3`, to get `Dneg_s<=3 delta(P)` and then
`S*_s<=2 Phi_s+6 delta(P)`. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:272-293`]

That factorization is one-way for downstream use; it does not upper-bound
`Phi_s`. [T1]

#### Where Pure Fixed-Chart LP Fails

A beta-row-only dual certificate cannot exist if it uses only the harmonic
moments and the negative mass of the pivot beta row. [PROVED-inline, T1]

Exact coefficient witness: take pivot `s=0` and two coordinate atoms
`a^+=(1,M,-M)` and `a^-=(1,-M,M)` with beta weights `1/2,1/2`. Then
`sum beta=1`, `sum beta a=e_0`, and the pivot beta row has negative mass `0`,
but each atom has `lambda=0`, `mu=M`, `E=M`, so `Phi_0=M`. [PROVED-inline, T1]

This is not an actual small-delta idempotent witness; it is a certificate that
the coefficient-only LP relaxation is too weak. [T1]

Therefore Step 2 must keep the missing realizability constraints: all rows of
`P=LB` have negative mass at most `delta(P)`, `BL=I`, and chart choices are
actual rows. [T1]

The full harmonic system suggests the right charge: high `E_s` means large
aggregate off-pivot negative coordinate mass, and each off-pivot coordinate
has zero beta moment. [T2]

The obstruction is cancellation among positive-beta rows: negative coordinate
mass on one high-`E` row can be balanced by positive coordinate mass on other
positive-beta rows without using beta-negative mass. [T1]

Summing coordinate-by-coordinate risks a factor depending on the number of
transverse coordinates, which is the chart analogue of the class-count wall.
[T1]

### Step 3. Argmin Exchange Interface

For a block swap replacing pivot set `I` by actual rows `J`, write old
coordinates in block form
`C=A[J,I]`, `D=A[J,K]`. The new coordinates are
`x'_I=x_I C^{-1}` and `x'_K=x_K-x_I C^{-1}D`, and the volume factor is
`|det C|`. [T0: `docs/ingest/report/kernel-conjecture-v2.tex:500-518`;
`docs/ingest/experiments/out/w40_ndg/proof.md`]

If the swapped chart `V` remains in `M_{1/2}(P)`, then argmin minimality gives
`Phi(U*)<=Phi(V)`. [PROVED-inline, T1]

This is not the dead single-swap contraction claim. It does not assert that a
one-row swap improves `Phi`, only that every legal comparison chart has score
at least the global minimum. [T1]

The live exchange skeleton is:

`Phi_s(U*)` on high-excess rows either can be tested by a volume-permitted Schur
swap, in which case stationarity gives an inequality, or the relevant Schur
blocks are near-degenerate, in which case degeneracy itself must force an
`O(delta)` payment. [T2]

The source names exactly this near-degenerate horn as the open higher-rank gap:
near-degeneracy of the transverse determinant must force carried `S*` or `Phi`
mass to be `O(delta)`. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:448-454`]

The single useful reduction I can state without hiding a class-count assumption is:

**GAP B.** There is a universal constant `C` such that for every rank-`>=3` exact
signed idempotent `P` with `0<delta(P)<=1/4`, every theta-`1/2` `Phi`-argmin
`U*`, and every pivot `s` of `U*`, the Schur-swap stationarity inequalities for
all volume-permitted block swaps imply `Phi_s(U*)<=C delta(P)`. [GAP, T2]

GAP B is slightly less clean than GAP A because it refers to a family of
stationarity inequalities, but it marks where chart optimality has to enter.
[T2]

### Step 4. Reduced-Fan Structural Hint

In the certified reduced theta class of the multiblock runs, the anchor-pivot
score has the exact form
`Phi = a/|G| * sum_{w in G} neg_l1(w-w0)`. [T0:
`runs/2026-07-02-ex-multiblock-coupling/scripts/certify_multiblock_coupling.py`;
`runs/2026-07-02-ex-multiblock-coupling/README.md`]

For multiple anchors in those runs, the minimization decouples per anchor and
the chart score is the maximum of the per-anchor minima, not a sum over anchors.
[T0/T1: A3]

This is the best structural hint: a successful proof should look like a
weighted average-distance minimization in a clone-quotient coordinate measure,
not like a count of bad rows or bad classes. [T2]

The no-center path data follows `Phi/delta = 2 - 2/(k-2)` through the certified
rows and plateaus toward `2`. [T0:
`runs/2026-07-02-ex-no-center-highrank/README.md`;
`runs/2026-07-02-ex-no-center-highrank/data/no_center_highrank.csv`]

Thus the honest working constant is `C0` around `2`, not the rank-3 aesthetic
constant `1`. [T1]

## 2. Test-Bench Table

Exact scratch recomputation used only repo constructors from `w40_ndg`,
`w41_ex`, and the two 2026-07-02 run scripts; no repo file was written by the
scratch checker. [T0]

| witness | delta | selected `Phi/delta` | selected `S*/delta` | selected max `E/delta` | selected max `S+/delta` | selected max `V/delta` | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| transverse pair `a=1/8` | `2/17` | `1` | `2` | `17/8` | `2` | `0` | target `C0=2` passes; pointwise `E<=2delta` fails |
| transverse pair `a=1/4` | `1/5` | `1` | `2` | `5/2` | `2` | `0` | target passes; bad selectors reach `5/4` |
| perturbed staircase `m=5, eps=1/1000` | `1/2` | `1` | `2` | `10` | `2` | `1/500000` | outside cap; kills pointwise and `V=0` |
| no-center path `k=6` | `1/100` | `3/2` | `5/2` | `2` | `5/2` | `0` | `C0=1` false in high rank; `C0=2` passes |
| no-center path `k=8` | `1/100` | `5/3` | `8/3` | `2` | `8/3` | `0` | plateau trend; sharp sigma-`2delta` fails |
| multiblock star, foreign `9` | `1/100` | `23/16` | `39/16` | `2` | `39/16` | `0` | reduced-fan average-distance formula passes |

Candidate inequalities tested:

- `Phi(U*) <= 2 delta(P)`: PASSES all mandatory witnesses above. [TESTED, T0]
- `max_j E_s(j) <= 2 delta(P)` at the selected chart: FAILS on both transverse
  pairs and the perturbed staircase. [TESTED, T0]
- `max_s S^+_s(U*) <= 2 delta(P)`: FAILS on no-center `k=6`, no-center `k=8`,
  and the multiblock star row. [TESTED, T0]
- `V_s(U*)=0` for every selected pivot: FAILS on perturbed staircase
  `m=5, eps=1/1000`. [TESTED, T0]
- Reduced one-anchor average-distance bound `Phi/delta<2`: PASSES the no-center
  and multiblock rows tested here and matches A2/A3. [TESTED, T0]

The perturbed staircase line is outside the `(EX)` delta cap, but it is mandatory
because it kills proof mechanisms that would otherwise be tempting. [T0/T1]

## 3. Honest Verdict

The skeleton is one real lemma away from closing `(EX)` with some universal
constant. [T2]

The one real lemma is an aggregate, chart-optimality-sensitive charge of
positive beta mass on high-`E` rows to `delta(P)`. [T2]

The gap is genuinely new relative to the B4 one-sided ledger wall: `(EX)` asks
for a weighted chart excess, not a lower bound on visible mass. [T1]

The gap becomes wall-shaped if the proof decomposes into bad transverse classes
or near-degenerate blocks and then sums a per-class estimate. That would import
the class-count wall in chart coordinates. [T1]

The fixed-chart beta LP route alone is dead: the exact two-atom moment witness
has zero pivot negative mass and arbitrarily large `Phi`. [T1]

The single-swap descent route is dead, but argmin comparison is not dead. The
difference is that comparison may use all legal swaps as stationarity
constraints and may be non-strict. [T1]

The reduced-fan evidence points to a clone-quotient average-distance principle:
the chart should choose a center minimizing an average negative `l1` distance,
and multi-anchor copies should combine by max rather than by sum. [T2]

I do not see a proof of that principle for arbitrary realizable charts. [T1]

## 4. Ranked Recommendation

1. Elevate GAP A only if the goal is to attack `(EX)` directly with af:
   "There is a universal constant `C` such that for every rank-`>=3` exact
   signed idempotent `P` with `0<delta(P)<=1/4`, every theta-`1/2` `Phi`-argmin
   `U*` satisfies `max_s Phi_s(U*) <= C delta(P)`." [T1]

2. Prefer one proof-scoping wave before af elevation to sharpen GAP B into a
   statement with an explicit Schur-block degeneracy functional. GAP B is the
   mathematically smaller route, but it is not yet clean enough as an af
   contract. [T1]

3. Do not elevate pointwise `E`, zero-overshoot, sigma-`2delta`, single-swap
   contraction, or coefficient-only LP lemmas. They are refuted by the mandatory
   witnesses or by the fixed-chart LP relaxation above. [T0/T1]

4. If pivoting, pivot toward clone-quotient average-distance minimization for
   realizable chart measures. The exact reduced-fan formula is the strongest
   structural hint now in the repo. [T2]
