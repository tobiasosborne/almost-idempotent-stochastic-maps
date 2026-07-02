<!--
ROLE: adversarial construction wave artifact for fr arm A.
STATUS: L3 numerical/exploration report only. Nothing below proves (EX), conj-kernel, or op-classical.
Worker: codex. Arm A wave 7. Answers bd aism-xrr.
Tier legend: T0 = exact repo-file computation or exact rational recomputation in this wave;
T1 = elementary derivation / conservative synthesis from T0;
T2 = plausible heuristic; T3 = speculation.
Scope discipline: repo files only; no prior conversation trusted.
Mission override: the user explicitly forbade fr/bd commands, so fr and bd were not run.
No L3 bundle was created because no certified row had min-max Phi/delta > 2.
-->

# Arm A Wave 7: Coupled Anchors

## Target

The attempted refuter is an exact signed idempotent under the cap
`delta(P) <= 1/4` with certified

`min_{theta-1/2 actual-row charts U} max_s Phi_s(U)/delta(P) > 2`.

The prior strongest certified record remains below 2:
`27/14` in `runs/2026-07-02-ex-no-center-highrank/`, with multiblock and
under-cap active-pivot rows also below 2. [T0]

## Method

All certified rows use exact rational arithmetic. For each instance I checked
`BL=I`, row sums, `P=LB`, `P^2=P` via `BL=I`, and direct row negative mass
`delta(P) <= 1/4`. [T0]

Full-enumeration rows enumerate every actual-row basis, compute exact row
volumes, retain the theta-half class, and then evaluate the exact chart
coefficients `A=L L_U^{-1}` and the pivot scores `Phi_s`. [T0]

Reduced rows use the same determinant discipline as A2/A3: all foreign unit
rows are present and the remaining pivots are signed rows whose anchor block
has determinant at least half the maximum. Any basis omitting a foreign unit
has at least one determinant column scaled by the shear amplitude `a=1/100`,
and the checked Hadamard bound keeps it below the theta-half threshold. For
the anchor-mixing star rows, permutation/sign symmetry reduces the reduced
chart scan to eight exact representatives. [T0/T1]

## Design Rationale

**C1, shared signed rows.** I added midpoint signed rows with anchor part
`(e_0+e_1)/2`, alongside pure anchor rows. The `B` aggregate on shared rows was
swept in both signs for the small path case. Positive or negative shared
aggregate raised `delta` faster than it raised the selected `Phi`; the best
certified value in the sweep was at zero shared aggregate. The midpoint rows
are still in the theta-half class, so this tests whether charts can use one row
to serve two anchors. [T0/T1]

**C2, non-paired zero-average shear sets.** I replaced paired edge fans by
zero-average but non-symmetric shear sets, including the simplex-like triple
`(2,-1,-1),(-1,2,-1),(-1,-1,2)` and a lopsided four-row set. This attacks the
closed forms that rely on plus/minus pairing. [T0/T1]

**C3, anchor-mixing shears.** Signed rows for anchor 0 contain shear mass on
anchor 1 and a foreign coordinate, and conversely. Thus exchanging one
anchor's signed pivot changes the coordinates seen by the other anchor's rows.
Increasing the mixing amplitude up to `a=1/4` only lowered the normalized
score; the best rows used `a=1/100`. [T0/T1]

**C4, non-uniform anchor B-weights.** I used exact non-uniform weights
`(1/2,1/3,1/6)` on shears
`(1,-1,0),(0,1,-1),(-3,1,2)`, whose weighted average is zero. The same weighted
fan was tested with one anchor and with two anchors. [T0]

**C5, no-pure shared anchors.** I removed pure anchor rows and used two
near-anchor shared types `(1-eps,eps)` and `(eps,1-eps)`, so every signed row
carries mass on both anchor coordinates. Full enumeration at `eps=1/10`
matched the small shared-row score rather than increasing it. [T0/T1]

## Exact Results

All `Phi/delta` entries are exact rationals. Decimal comparisons are not used
as certified evidence. [T0]

| family | params | k | n | delta | min-max Phi/delta | certification | charts |
|---|---|---:|---:|---:|---:|---|---:|
| C1 shared midpoint path | `f=3`, `a=1/100`, shared aggregate `t=0` | 5 | 15 | `1/100` | `5/4` | full_enumeration | 48 theta / 3003 bases |
| C1 shared midpoint path | `f=5`, `a=1/100`, best swept aggregate `t=0` | 7 | 29 | `1/100` | `3/2` | certified_reduction | 192 |
| C2 non-paired simplex triple | two anchors, uniform weights | 5 | 9 | `1/50` | `1` | full_enumeration | 9 theta / 126 bases |
| C2 lopsided zero-average four-set | two anchors, uniform weights | 5 | 11 | `3/100` | `5/12` | full_enumeration | 16 theta / 462 bases |
| C3 anchor-mixing star | `f=3`, `a=1/100` | 5 | 15 | `1/100` | `39701/30003` | full_enumeration | 36 theta / 3003 bases |
| C3 anchor-mixing star | `f=29`, `a=1/100` | 31 | 145 | `1/100` | `427114/290029` | certified_reduction + symmetry | 3364 |
| C3 anchor-mixing star | `f=119`, `a=1/100` | 121 | 595 | `1/100` | `1768159/1190119` | certified_reduction + symmetry | 56644 |
| C4 non-uniform weighted fan | one anchor, weights `(1/2,1/3,1/6)` | 4 | 6 | `3/100` | `4/9` | full_enumeration | 3 theta / 15 bases |
| C4 non-uniform weighted fan | two anchors, same weighted fan | 5 | 9 | `3/100` | `4/9` | full_enumeration | 9 theta / 126 bases |
| C5 no-pure near-shared anchors | `eps=1/10`, `f=3`, `a=1/100` | 5 | 11 | `1/100` | `5/4` | full_enumeration | 16 theta / 462 bases |

The maximum certified value achieved by this wave is `3/2`, in the C1
midpoint-shared path with `f=5`. The best genuinely anchor-mixing high-rank row
is `1768159/1190119 < 2`. [T0]

## Near-Miss Notes

C1 did not break the product fallback. Midpoint rows enter the theta-half
class, but the selected chart can still use the pure-pure anchor pair. Signed
shared aggregate is not helpful in the checked sweep: it increases the direct
negative mass denominator and lowers `Phi/delta`. [T1]

C2 and C4 move the shear barycenter, but the argmin chart chooses the cheap
central or heavy-weight row. The lopsided examples lower the ratio rather than
raising it. [T1]

C3 is the strongest genuinely non-product geometry tested here. It does
couple the anchor coordinates in the chart inverse, but the exact high-rank
trend remains far below 2 and increases only slowly with `f`. Raising the
mixing amplitude from `1/100` through `1/4` lowered the normalized score in
the checked rows. [T0/T1]

## Verdict

**Plateau survives this coupled-anchor wave.** No certified under-cap instance
with min-max `Phi/delta > 2` was found. The cheap coupling mechanisms tested
here either retain a decoupled fallback chart or reduce the normalized score by
raising `delta`. [T1]

This does not prove (EX), and it does not prove a universal plateau-2 theorem.
It does close the last obvious cheap adversaries from the A3/A6 diagnosis:
shared signed rows, non-paired zero-average fans, anchor-mixing shears,
non-uniform anchor weights, and no-pure shared anchors all stayed below 2 in
the certified exact rows above. [T1]

## Next-Step Recommendation

Do not spend another wave on small LB templates whose reduced theta class is
all foreign units plus a bounded number of signed pivots. The next plausible
plateau breaker would need a chart class where every theta-half basis is
globally coupled and where the coupling does not enter primarily by increasing
direct negative mass. A proof wave should instead target a max-based plateau-2
exchange/charge lemma, with explicit handling of the pure-pivot fallback
exposed by C1. [T2]
