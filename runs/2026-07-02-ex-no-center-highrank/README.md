# Run bundle: high-rank no-center (EX) decider - 2026-07-02

**Status: L3 numerical evidence. NEVER rigorous.** All certified quantities are
computed over exact rationals; decimal fields in the CSV are display-only.

## Hypothesis

For the inherited no-center path family from `w40_ndg`, decide whether
`min_{U in M_{1/2}} max_s Phi_s(U)/delta(P)` keeps growing with rank or
plateaus. The stress record is numerical/L3 evidence for `(EX)`, not a proof of
`(EX)`.

## Command

```bash
python3 runs/2026-07-02-ex-no-center-highrank/scripts/certify_no_center_highrank.py
```

The command writes:

```text
runs/2026-07-02-ex-no-center-highrank/data/no_center_highrank.csv
```

## Finding

The no-center path at `a=1/100` follows the exact pattern
`Phi/delta = 2 - 2/(k-2)` through the certified rows `k=6,8,10,12,14,16,20,30`.
Thus this family plateaus toward `2` from below rather than growing without
bound. The k=6 and k=8 rows reproduce the inherited exact invariants
`3/2` and `5/3`; k=10,12,14 give `7/4`, `9/5`, `11/6`.

Certification scope:

- k=6,8: full exact enumeration of all actual-row bases, with theta-half filter.
- k>=10: certified determinant reduction to the theta-half class consisting of
  all foreign unit rows plus one signed row; every reduced chart is then checked
  exactly.
- delta-scale variants at `a=1/200` and `a=1/20` show the same normalized
  ratios under the same determinant reduction. The copied repo files did not
  include a separate repeated-shear constructor, so no new repeated-shear family
  is certified here.

## Invariant / certificate

The script must reproduce the inherited no-center records exactly:

```text
k=6, delta=1/100, BL=True, P2=True, rowsum=True, Phi/delta=3/2
k=8, delta=1/100, BL=True, P2=True, rowsum=True, Phi/delta=5/3
```

It also checks `BL=I`, `P^2=P`, row sums, exact `delta`, harmonic deficit
identities in every checked theta-half chart, and the exact formula
`Phi/delta = 2 - 2/(k-2)` for every emitted data row.

**Orchestrator independent recomputation (2026-07-02):** the k=10 row was
recomputed with fresh, bundle-independent code over `fractions.Fraction`
(same construction conventions read off `w40_ndg/verify_part_a.py`):
`BL=I`, `P^2=P`, row sums, `delta=1/100` all confirmed; min over the
16-chart theta-class of `max_s Phi_s/delta` = `7/4` exactly, matching this
bundle's row and the `2 - 2/(k-2)` pattern.

## Next

Use `C0 ~= 2` as the working Arm-A target for this family. A future growth
claim needs a genuinely new high-rank variant plus either full theta-half chart
enumeration or a comparable exact chart-coverage reduction.
