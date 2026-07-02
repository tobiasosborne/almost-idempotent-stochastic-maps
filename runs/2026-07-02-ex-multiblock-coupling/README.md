# Run bundle: multiblock (EX) coupling stress test - 2026-07-02

**Status: L3 numerical evidence. NEVER rigorous.** All certified quantities are
computed over exact rationals; decimal fields in the CSV are display-only.

## Hypothesis

Richer signed-shear coupling graphs might force
`min_{U in M_{1/2}} max_s Phi_s(U)/delta(P)` to grow with rank, unlike the
no-center path family from `runs/2026-07-02-ex-no-center-highrank/`, which
plateaus toward `2`.

This bundle attacks that possibility with one-anchor star/complete/complete
bipartite edge fans, two-anchor overlapping fans, higher-arity ternary shears,
and a cycle-plus-skip chord family.

## Command

```bash
python3 runs/2026-07-02-ex-multiblock-coupling/scripts/certify_multiblock_coupling.py
```

The command writes:

```text
runs/2026-07-02-ex-multiblock-coupling/data/multiblock_coupling.csv
```

## Finding

No growth refuter was found. Every emitted row is `certified_reduction`: the
Hadamard determinant bound proves that the whole theta-half class consists of
all foreign unit rows plus one signed row per anchor, and the script checks that
entire class exactly.

The richest certified ratios remain below `2`: complete and complete-bipartite
edge fans follow `2-2/f` through the checked rows, ternary all-triple shears
reach `7/4` at foreign dimension `10`, and cycle-plus-skip edges reach `28/15`
at foreign dimension `15`. Two-anchor overlapping fans decouple under the
certified chart class and do not amplify the one-anchor ratios.

## Invariant / certificate

- Calibration: the first CSV data row reproduces the A2 no-center path value
  `k=10`, `delta=1/100`, `Phi/delta=7/4` exactly.
- Every row checks `BL=I`, row sums, `delta` by direct row negative mass, and
  `P^2=P` via the exact identity `P^2 = L(BL)B = LB`.
- For every family, `4*R2*a^2 < 1/4` at `a=1/100`, where `R2` is the maximum
  squared shear norm. Hence any basis with an extra signed row has volume
  below half the max-volume class; omitted bases are outside `M_{1/2}`.


- **Orchestrator independent recomputation (2026-07-02):** the row
  `one_anchor_star_edges, foreign=9` (k=10, 16 signed rows) was recomputed
  with fresh, bundle-independent code over `fractions.Fraction`: `BL=I`,
  `P^2=P`, row sums, `delta=1/100` confirmed; min over the 16-chart
  theta-class of `max_s Phi_s/delta` = `23/16` exactly, matching the CSV row.

## Next

The natural multiblock variants tested here plateau below `2`, so the next
useful adversarial wave should target genuinely non-uniform anchor weights or
non-paired shear sets where the reduced theta class no longer decouples into
independent per-anchor average-distance minimizers.
