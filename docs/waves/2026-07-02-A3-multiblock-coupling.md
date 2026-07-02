<!--
ROLE: harvest artifact for an adversarial construction wave on fr arm A.
STATUS: L3 numerical evidence only; not a proof of (EX), conj-kernel, or op-classical.
Tier legend: T0 = exact repo-file computation/provenance; T1 = conservative synthesis from T0;
T2 = plausible heuristic; T3 = speculation. Worker: codex. Arm A wave 3. Answers bd aism-azi.
Scope discipline: repo files only; no prior conversation trusted.
-->

# Arm A · Wave 3 · Multiblock Coupling Stress Test

## Target

The refutation target is the universal-constant form of `(EX)`: find a rank-growing exact signed idempotent
family with `delta(P)<=1/4` where
`min_{U in M_{1/2}(P)} max_s Phi_s(U)/delta(P)` grows without bound. [T0 from
`argument/lemmas/conj-ex.md` and the chart definitions in `docs/ingest/report/kernel-conjecture-v2.tex`]

A2 certified that the no-center path family follows `2-2/(k-2)` through the checked ranks and therefore
plateaus toward `2`, not infinity. [T0: `runs/2026-07-02-ex-no-center-highrank/`]

## Method

The script `runs/2026-07-02-ex-multiblock-coupling/scripts/certify_multiblock_coupling.py` uses the same
exact `LB` template as A2: foreign unit rows, signed shear rows attached to one or more anchors, uniform
anchor rows in `B`, unit selectors for foreign coordinates, and `P=LB`. It checks `BL=I`, row sums, exact
`delta`, and `P^2=P` via `P^2=L(BL)B=LB`. [T0]

All rows use shear scale `a=1/100`. For each family, the determinant reduction is certified by the bound
`4*R2*a^2 < 1/4`, where `R2` is the maximum squared shear norm. Thus any basis with more than one signed
row per anchor has volume below half the max-volume class. The entire theta-half class is exactly: all
foreign unit rows plus one signed row per anchor. [T0]

In that reduced class, the anchor-pivot score has the exact closed form
`Phi = a/|G| * sum_{w in G} neg_l1(w-w0)`, normalized by the global shear negative mass. Multi-anchor
families minimize independently per anchor and then take the maximum anchor score. [T0 for the script
calculation; T1 as structural interpretation]

## Design Rationale

D1 star/complete/complete-bipartite edge fans replace the path's consecutive edges by richer edge graphs on
the same foreign coordinates. This directly attacks the possibility that the A2 plateau is a one-dimensional
path artifact. [T1]

D2 multi-anchor overlapping fans use two anchor coordinates with overlapping foreign star or complete-vs-star
fans. This tests whether one chart must favor one anchor's fan at the expense of another. [T1]

D3 higher-arity ternary shears use all signed vectors of the form `e_u+e_v-2e_t`. These have three nonzero
foreign entries and larger shear norm/negative mass than edge shears, so they test whether wider supports
increase the average chart wedge cost. [T1]

D4 cycle-plus-skip edges add a non-path sparse graph: cycle edges plus skip-2 chords. This is a small
expander-like perturbation of the path without the complete graph's high symmetry. [T2]

## Exact Results

All rows are `certified_reduction`; no `upper_bound_only` row is used. [T0]

| family | parameters | k | n_rows | delta | Phi/delta | charts |
|---|---|---:|---:|---:|---:|---:|
| calibration_no_center_path | rank_k=10 | 10 | 25 | 1/100 | 7/4 | 16 |
| one_anchor_star_edges | foreign=5 | 6 | 13 | 1/100 | 11/8 | 8 |
| one_anchor_star_edges | foreign=9 | 10 | 25 | 1/100 | 23/16 | 16 |
| one_anchor_star_edges | foreign=13 | 14 | 37 | 1/100 | 35/24 | 24 |
| one_anchor_star_edges | foreign=19 | 20 | 55 | 1/100 | 53/36 | 36 |
| one_anchor_complete_edges | foreign=4 | 5 | 16 | 1/100 | 3/2 | 12 |
| one_anchor_complete_edges | foreign=6 | 7 | 36 | 1/100 | 5/3 | 30 |
| one_anchor_complete_edges | foreign=8 | 9 | 64 | 1/100 | 7/4 | 56 |
| one_anchor_complete_edges | foreign=10 | 11 | 100 | 1/100 | 9/5 | 90 |
| one_anchor_complete_bipartite_edges | K_{3,3} | 7 | 24 | 1/100 | 5/3 | 18 |
| one_anchor_complete_bipartite_edges | K_{4,4} | 9 | 40 | 1/100 | 7/4 | 32 |
| one_anchor_complete_bipartite_edges | K_{5,5} | 11 | 60 | 1/100 | 9/5 | 50 |
| two_anchor_overlapping_stars | foreign=5 | 7 | 21 | 1/100 | 11/8 | 64 |
| two_anchor_overlapping_stars | foreign=8 | 10 | 36 | 1/100 | 10/7 | 196 |
| two_anchor_overlapping_stars | foreign=12 | 14 | 56 | 1/100 | 16/11 | 484 |
| two_anchor_complete_vs_star | foreign=4 | 6 | 22 | 1/100 | 3/2 | 72 |
| two_anchor_complete_vs_star | foreign=6 | 8 | 46 | 1/100 | 5/3 | 300 |
| two_anchor_complete_vs_star | foreign=8 | 10 | 78 | 1/100 | 7/4 | 784 |
| one_anchor_ternary_all | foreign=4 | 5 | 28 | 1/50 | 11/8 | 24 |
| one_anchor_ternary_all | foreign=6 | 7 | 126 | 1/50 | 19/12 | 120 |
| one_anchor_ternary_all | foreign=8 | 9 | 344 | 1/50 | 27/16 | 336 |
| one_anchor_ternary_all | foreign=10 | 11 | 730 | 1/50 | 7/4 | 720 |
| one_anchor_cycle_skip_edges | foreign=7 | 8 | 35 | 1/100 | 12/7 | 28 |
| one_anchor_cycle_skip_edges | foreign=11 | 12 | 55 | 1/100 | 20/11 | 44 |
| one_anchor_cycle_skip_edges | foreign=15 | 16 | 75 | 1/100 | 28/15 | 60 |

## Verdict

**Plateau persists in these natural multiblock couplings.** [T1] No certified row exceeds `2`; the closest
large sparse cycle-skip row is `28/15`, while complete, bipartite, ternary, and calibration rows sit on
sub-2 trends. This is evidence for a universal `(EX)` constant at the chart level, not a proof of `(EX)`.

The attempted class-count amplification does not materialize here because the certified theta-half class
collapses to one signed pivot per anchor. The score becomes an average pairwise shear-distance problem inside
each fan, and multi-anchor rows take a max of independent per-anchor minima rather than a sum over anchors.
[T1]

No growth refuter was found. A refutation now needs a construction that breaks this decoupling, for example
non-uniform anchor weights, unpaired shear sets whose average is still exactly zero, or anchor rows that mix
anchor coordinates so that theta-half charts cannot choose one independent pivot per fan. [T2]

## Next-Wave Recommendation

Do not spend another wave on paired uniform one-anchor edge fans, complete/bipartite variants, or decoupled
multi-anchor copies unless a new mechanism is added. The next adversarial construction should force coupling
between anchor choices in the actual theta-half determinant class; otherwise the average-distance plateau
seen here will likely recur. [T1/T2]
