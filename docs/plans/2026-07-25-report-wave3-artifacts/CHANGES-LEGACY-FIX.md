# Legacy-review corrections applied

| Verdict finding | File | Description |
|---|---|---|
| F1 — MAJOR | `report/sections/00_overview.tex` | Corrected the overview summary and block count from four to five, added the H-CB-parent/EXT tier to the summary, and described the assembly as remaining below the af-validated rung rather than open. |
| F2 — MAJOR | `report/sections/03_compcb_amplification_naturality.tex` | Corrected the closing proof sentence to name isometry, unitality, and multiplicativity as the properties used. |
| F3 — MINOR | `report/sections/06_compcb_entrywise_compression_naturality.tex` | Replaced the “strictly sharper” claim with the supplied single-slot-specialization description. |
| F4 — MINOR | `report/sections/14_compcb_corner_algebra.tex` | Made the displayed registry-consumer list explicitly non-exhaustive. |
| F5 — MAJOR | `report/sections/16_compcb_single_compression_transfer.tex` | Replaced the stale role paragraph with the supplied current EXT-parent and broader-assembly statuses. |
| F6 — MINOR | `report/sections/17_hcb1_variational_identity.tex` | Replaced the single-consumer claim with the supplied two-consumer account naming `lem-hcb1-column-action` and `conj-hcb`. |
| F7 — MAJOR | `report/sections/21_hcb3_diagonal_upper_norm.tex` | Corrected the lower-modulus discussion to say the hypothesis is supplied only inside the EXT section. |
| F8 — MINOR | `report/sections/22_hcb3_uniform_square_lower.tex` | Replaced the stale single-consumer claim with the supplied non-exhaustive wording. |
| F9 — MINOR | `report/sections/24_hcb3_diagonal_inverse.tex` | Removed the reversed ordinal labels and named the bijectivity and level-one lower-modulus hypotheses directly. |

## AMBIGUOUS

## Gate tails

`cd report && make` — exit 0:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
Rc files read:
  /etc/LatexMk
Latexmk: This is Latexmk, John Collins, 31 Jan. 2024. Version 4.83.
Latexmk: Nothing to do for 'main.tex'.
Latexmk: All targets (main.pdf) are up-to-date
```

`bash scripts/check-report-shards.sh` — exit 1:

```text
report shard check: report/SHARD_CATALOG.md does not mirror summary from report/sections/00_overview.tex: Describes the five af-validated blocks reproduced here: the bridge, PRH, the COMP tier, the H-CB tier, and the H-CB-parent/EXT tier.
```

The shard gate's sole failure requires mirroring F1's mandated summary correction into
`report/SHARD_CATALOG.md`. That file is outside the nine-file write scope, so it was not
modified.
