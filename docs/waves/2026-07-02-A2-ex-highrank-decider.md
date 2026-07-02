<!--
ROLE: verbatim harvest artifact for a certified numerics wave on fr arm A.
STATUS: L3 numerical evidence only; not a proof of (EX), conj-kernel, or op-classical.
Tier legend: T0 = exact repo-file computation/provenance; T1 = conservative synthesis from T0;
T2 = plausible heuristic; T3 = speculation. Worker: codex. Arm A wave 2. Answers bd aism-e4q.
-->

# Arm A · Wave 2 · High-Rank No-Center Decider

## Method

The source vocabulary is the actual-row chart setup in
`docs/ingest/report/kernel-conjecture-v2.tex`: `M_{1/2}`, coordinates `a_s(j)`,
`beta_s(j)=P_{u_sj}`, `E_s(j)`, and `Phi_s(U)`. [T0]

The construction is the `w40_ndg` no-center path: for rank `k`, take the
`k-1` foreign unit rows and the `2(k-2)` signed adjacent rows
`e_0 +/- a(e_i-e_{i+1})`. The left inverse `B` is the same constrained one:
`B_0` has mass `1/(2(k-2))` on every signed row and the other `B_i` select the
corresponding foreign unit row. The script checks `BL=I`, `P=LB`, `P^2=P`,
row sums, and `delta(P)=a` exactly. [T0]

Chart coverage uses determinant pruning. Row-volume ratios for `P_U=L_U B`
equal `|det L_U|` ratios up to the fixed factor `det(BB^T)^{1/2}`. A basis with
no signed row is singular. A basis with exactly one signed row contains all
foreign unit rows and has determinant `1`; these are the max-volume charts.
If a basis has `r>=2` signed rows, subtract one signed row from the other
signed rows and expand along the selected unit rows. The determinant is
`a^{r-1} det M`, where each row of `M` is a difference of signed edge vectors,
so its squared row norm is at most `8`; Hadamard gives
`det^2 <= (8a^2)^{r-1}`. For `a=1/100` and the variants `a<=1/20`, this is
`<1/4`, hence outside `M_{1/2}`. [T0]

The script nevertheless fully enumerates all actual-row bases for k=6 and k=8
as calibration, using the same exact determinant formula. [T0]

## Exact Values

| k | a | delta | Phi/delta | S*/delta | certification | charts checked | notes |
|---:|---:|---:|---:|---:|---|---:|---|
| 6 | 1/100 | 1/100 | 3/2 | 5/2 | full_enumeration | 8 | 1716 bases, 916 nonsingular, theta=8 |
| 8 | 1/100 | 1/100 | 5/3 | 8/3 | full_enumeration | 12 | 75582 bases, 21408 nonsingular, theta=12 |
| 10 | 1/100 | 1/100 | 7/4 | 11/4 | certified_reduction | 16 | theta class = all units + one signed row |
| 12 | 1/100 | 1/100 | 9/5 | 14/5 | certified_reduction | 20 | theta class = all units + one signed row |
| 14 | 1/100 | 1/100 | 11/6 | 17/6 | certified_reduction | 24 | theta class = all units + one signed row |
| 16 | 1/100 | 1/100 | 13/7 | 20/7 | certified_reduction | 28 | theta class = all units + one signed row |
| 20 | 1/100 | 1/100 | 17/9 | 26/9 | certified_reduction | 36 | theta class = all units + one signed row |
| 30 | 1/100 | 1/100 | 27/14 | 41/14 | certified_reduction | 56 | theta class = all units + one signed row |
| 14 | 1/200 | 1/200 | 11/6 | 17/6 | certified_reduction | 24 | delta-scale variant |
| 14 | 1/20 | 1/20 | 11/6 | 17/6 | certified_reduction | 24 | delta-scale variant |
| 20 | 1/200 | 1/200 | 17/9 | 26/9 | certified_reduction | 36 | delta-scale variant |

The k=6 and k=8 rows reproduce the inherited `w40_ndg` invariants
`Phi/delta=3/2` and `5/3` with `BL=True`, `P2=True`, and `rowsum=True`. [T0]

Every emitted row matches `Phi/delta = 2 - 2/(k-2)` exactly. This is certified
for the finite rows above; I do not promote the closed form to a theorem for
all k. [T0/T1]

The copied repo files contain the no-center constructor and notes pointing to
omitted repeated-shear discussions, but no separate repeated-shear constructor
was present under `docs/ingest/` or `runs/`. This wave therefore certifies only
the no-center path and its delta-scale variants. [T0]

## Verdict

Plateau for the certified no-center path: the selected min-chart ratio rises
monotonically through the checked ranks but stays below `2`, fitting convergence
to `2` rather than unbounded growth. [T1]

This supports using `C0 ~= 2` as the next Arm-A proof target for this family,
with composed `C_sf = 2*C0 + 6 ~= 10`. It is still L3 evidence, not a proof of
`(EX)` and not a proof that all natural variants plateau. [T1]

There are no `upper_bound_only` rows in this bundle. To upgrade a future
heuristic repeated-shear row to a certified minimum, it needs either full
theta-half enumeration or a determinant/symmetry reduction proving that every
omitted theta-half chart is either absent from `M_{1/2}` or has no smaller
`max_s Phi_s/delta`. [T1]

## Next-Wave Recommendation

Bank this as evidence that the original no-center stress family is not a
counterexample program against all universal constants. The next useful Arm-A
wave should either formalize the aggregate charge suggested by the plateau, or
construct a genuinely new repeated-shear/multi-block family with exact `L,B`
and chart coverage from the start. [T1]
