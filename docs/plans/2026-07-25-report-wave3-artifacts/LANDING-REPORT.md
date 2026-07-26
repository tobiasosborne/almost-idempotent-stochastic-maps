# LANDING REPORT — report waves 3 + 3b + 3c

Date: 2026-07-26

## Outcome

Landing completed within the requested write allowlist. The 12 new shards are byte-identical to the
scratchpad sources, the report builds to a 77-page `main.pdf`, the Bash shard gate passes, and the
provenance gate reports 0 errors.

No git command was run. No file under `argument/`, `definitions/`, `proofs/`, `docs/`, `scripts/`,
`.frontier/`, or `.beads/` was written.

## Files copied / edited

### Copied: 12 new/revised shards

1. `report/sections/25_hcb3_offdiagonal_inverse.tex`
2. `report/sections/26_hcb4_canonical_gram.tex`
3. `report/sections/27_hcb4_canonical_closeness.tex`
4. `report/sections/28_hcb4_canonical_inverse.tex`
5. `report/sections/29_hcb.tex`
6. `report/sections/30_extcb_one_dimensional_corners.tex`
7. `report/sections/31_extcb_corner_dimension_additivity.tex`
8. `report/sections/32_extcb1_dimension_selection.tex`
9. `report/sections/33_extcb_four_corner_norm.tex`
10. `report/sections/34_extcb_four_corner_merge.tex`
11. `report/sections/35_extcb.tex`
12. `report/sections/36_status_outlook.tex`

Copy verification: `12/12` compare byte-identically with the scratchpad originals.

### Existing report prose edited under §G1: 9 files / 10 replacement items

1. `report/sections/00_overview.tex` — 2 replacement items
2. `report/sections/10_hcb2_amplified_adjointness.tex`
3. `report/sections/15_hcb_column_hilbert_squared.tex`
4. `report/sections/18_hcb1_column_action.tex`
5. `report/sections/19_hcb2_product_defect.tex`
6. `report/sections/20_hcb3_diagonal_unit.tex`
7. `report/sections/21_hcb3_diagonal_upper_norm.tex`
8. `report/sections/23_hcb3_diagonal_lower_modulus.tex`
9. `report/sections/24_hcb3_diagonal_inverse.tex`

### Wiring files edited: 5

1. `report/README.md`
2. `report/SHARD_CATALOG.md`
3. `report/PROVENANCE.md`
4. `report/main.tex`
5. `report/UNWIRED.md`

### Removed / build outputs

- Removed replaced source shard: `report/sections/25_status_outlook.tex` (1 file).
- Removed 26 stale pre-build `report/sections/*.aux` files as required by §A.
- `make` regenerated normal build outputs under `report/`, including `main.pdf` and per-section aux
  files.

Source-level count: 12 copied shards + 9 existing prose shards + 5 wiring files = 26 written source
files, plus 1 replaced source shard removed.

## §G replacements

### §G1 — existing repo shards

| File | Replacement | Applied |
|---|---|---|
| `00_overview.tex` | H-CB range extended through `sec:hcb4-canonical-inverse`; fifth H-CB-parent/EXT item added | yes |
| `00_overview.tex` | stale open status for `conj-hcb`/EXT replaced by validated H-CB and EXT parents; assembly remains open | yes |
| `10_hcb2_amplified_adjointness.tex` | two pending dependencies replaced by validated, section-linked dependencies | yes |
| `15_hcb_column_hilbert_squared.tex` | `lem-hcb4-canonical-closeness` pending status replaced by validated consumer wording | yes |
| `18_hcb1_column_action.tex` | `lem-hcb4-canonical-closeness` pending status replaced by validated, section-linked wording | yes |
| `19_hcb2_product_defect.tex` | `lem-hcb3-offdiagonal-inverse` pending status replaced by validated, section-linked wording | yes |
| `20_hcb3_diagonal_unit.tex` | stale no-consumer/open-parent wording replaced by validated parent-consumer wording | yes |
| `21_hcb3_diagonal_upper_norm.tex` | stale off-diagonal/canonical/parent statuses replaced by validated section references | yes |
| `23_hcb3_diagonal_lower_modulus.tex` | stale off-diagonal/parent statuses replaced by validated anchor/parent wording | yes |
| `24_hcb3_diagonal_inverse.tex` | stale off-diagonal/canonical/parent statuses replaced by proved/validated wording | yes |

Sweep for the old G1 phrases (`not-yet-validated`, `is not validated`, stale canonical-tier
`af: none`, and stale `conj-hcb` `proved-mod-audit`/`af: none`) returned no matches in the nine G1
files.

### §G2 — already present in copied scratchpad shards

| File | Replacement | Present after landing |
|---|---|---|
| `29_hcb.tex` | canonical-tier section range added | yes |
| `29_hcb.tex` | all sixteen results stated as reproduced in the document | yes |
| `36_status_outlook.tex` | canonical layer inserted in reproduced inventory | yes |
| `36_status_outlook.tex` | queued-canonical prose replaced by scoped supplied-registry statement | yes |

### §G3 — already present in copied scratchpad shards; no extra landing edit

| File | Replacement | Present after landing |
|---|---|---|
| `29_hcb.tex` | `conj-extcb` recorded as proved/validated and section-linked | yes |
| `32_extcb1_dimension_selection.tex` | `conj-extcb` consumer recorded as proved/validated | yes |
| `34_extcb_four_corner_merge.tex` | `conj-extcb` consumer recorded as proved/validated | yes |
| `36_status_outlook.tex` | inventory updated to 37 reproduced / 70 total / 33 off-route; assembly carrier named | yes |
| `36_status_outlook.tex` | conditional-clause qualification, shard summary, and closing status updated | yes |
| `28_hcb4_canonical_inverse.tex` | five live registry definitions recorded, including the two completeness-branch definitions | yes |

## Hash recomputation

All 26 §E paths were recomputed against the live repository immediately before landing. The ledger
uses these computed SHA256-16 values.

| Source key | Live SHA256-16 | §E match |
|---|---:|---|
| `ARG-LEM-HCB3-OFFDIAGONAL-INVERSE` | `ae44e4c30e481156` | yes |
| `AF-LEM-HCB3-OFFDIAGONAL-INVERSE` | `8e0654cec4ce118f` | yes |
| `ARG-LEM-HCB4-CANONICAL-GRAM` | `789fbbaefd0d1fbc` | yes |
| `AF-LEM-HCB4-CANONICAL-GRAM` | `a12f20742b28bdee` | yes |
| `ARG-LEM-HCB4-CANONICAL-CLOSENESS` | `a3d2e9ddded6f79a` | yes |
| `AF-LEM-HCB4-CANONICAL-CLOSENESS` | `336ce36ecd5bbfb5` | yes |
| `ARG-LEM-HCB4-CANONICAL-INVERSE` | `0e61a08b0d6157ff` | yes |
| `AF-LEM-HCB4-CANONICAL-INVERSE` | `0a3da88fbf702f9a` | yes |
| `ARG-CONJ-HCB` | `de52bbad964e45ef` | yes |
| `AF-CONJ-HCB` | `8818e7d0952d7343` | yes |
| `ARG-LEM-EXTCB-ONE-DIMENSIONAL-PRODUCT` | `ce1cfccd673787c4` | yes |
| `AF-LEM-EXTCB-ONE-DIMENSIONAL-PRODUCT` | `e154fae299637b1d` | yes |
| `ARG-LEM-EXTCB-ONE-DIMENSIONAL-CORNER-DIMENSION` | `5764c43280c08261` | yes |
| `AF-LEM-EXTCB-ONE-DIMENSIONAL-CORNER-DIMENSION` | `0e4440d7635b5943` | yes |
| `ARG-LEM-EXTCB-CORNER-DIMENSION-ADDITIVITY` | `517d59f6fd2b3f05` | yes |
| `AF-LEM-EXTCB-CORNER-DIMENSION-ADDITIVITY` | `83aaabfed5dfb04b` | yes |
| `ARG-LEM-EXTCB1-CLOSE-CORNER-DIMENSION` | `a6c30bde11080b1c` | yes |
| `AF-LEM-EXTCB1-CLOSE-CORNER-DIMENSION` | `3a26c1b3f960edc8` | yes |
| `ARG-LEM-EXTCB1-CROSS-CORNER-DIMENSION` | `f9a6aa8b2fbb4791` | yes |
| `AF-LEM-EXTCB1-CROSS-CORNER-DIMENSION` | `59ce65ddb29e6f75` | yes |
| `ARG-LEM-EXTCB-FOUR-CORNER-NORM` | `b7c4ab7ce44519b0` | yes |
| `AF-LEM-EXTCB-FOUR-CORNER-NORM` | `670ead004d58b5bf` | yes |
| `ARG-LEM-EXTCB-FOUR-CORNER-MERGE` | `3a2724066e5735e0` | yes |
| `AF-LEM-EXTCB-FOUR-CORNER-MERGE` | `35c643ae943968aa` | yes |
| `ARG-CONJ-EXTCB` | `80bd2795d2be2fd8` | **no** |
| `AF-CONJ-EXTCB` | `00494481438b5a79` | yes |

Deviation: §E prints `a8529323f4410a6a` for `argument/lemmas/conj-extcb.md`; the live file computes
to `80bd2795d2be2fd8`. The live value was used. No other deviation was found.

## Gate outputs

### `cd report && make`

Exit: 0. Produced `report/main.pdf`, 77 pages, 618895 bytes.

Tail from the full rebuilding invocation:

```text
Output written on main.pdf (77 pages, 618895 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Log file says output to 'main.pdf'
Latexmk: All targets (main.pdf) are up-to-date
```

Full output of the final clean rerun:

```text
make: Entering directory '/home/tobias/Projects/almost-idempotent-stochastic-maps/report'
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
Rc files read:
  /etc/LatexMk
Latexmk: This is Latexmk, John Collins, 31 Jan. 2024. Version 4.83.
Latexmk: Nothing to do for 'main.tex'.
Latexmk: All targets (main.pdf) are up-to-date

make: Leaving directory '/home/tobias/Projects/almost-idempotent-stochastic-maps/report'
```

### `sh scripts/check-report-shards.sh`

The literal brief command exits 2 before running the check because `/bin/sh` is `dash`, while the
script uses Bash-only `set -o pipefail`:

```text
scripts/check-report-shards.sh: 7: set: Illegal option -o pipefail
```

WIRING §H gives the executable form as `bash scripts/check-report-shards.sh`. That operative gate
exits 0 with full output:

```text
report shard check: 37 shards included, labeled, cataloged, all <= 280 lines
```

### `python3 scripts/check-provenance.py --check`

Exit: 0. Tail:

```text
        (warn) prop-f2-t1-equivalence: unanchored but whitelisted in report/UNWIRED.md (off paper-track)
        (warn) thm-classical-factorization: unanchored but whitelisted in report/UNWIRED.md (off paper-track)
        (warn) thm-cluster: unanchored but whitelisted in report/UNWIRED.md (off paper-track)
        (warn) thm-corner-constants: unanchored but whitelisted in report/UNWIRED.md (off paper-track)
        (warn) thm-rank-one: unanchored but whitelisted in report/UNWIRED.md (off paper-track)
        (warn) thm-simplex: unanchored but whitelisted in report/UNWIRED.md (off paper-track)
        (warn) thm-well-exposed: unanchored but whitelisted in report/UNWIRED.md (off paper-track)
[OK  ] reverse labels
[OK  ] coverage
[OK  ] parse integrity

check-provenance: 255 registry results, 37 claim rows, 182 tex labels — 0 errors, 218 warnings
```

The 218 warnings are the expected whitelisted off-paper-track anchors; there are 0 errors.

## AMBIGUOUS

- The brief requests `sh scripts/check-report-shards.sh`, but the script is Bash-specific
  (`set -o pipefail`) and WIRING §H explicitly specifies `bash scripts/check-report-shards.sh`.
  The literal `sh` invocation cannot execute the gate; the Bash invocation passes. No script was
  changed because `scripts/` is outside the write allowlist.

## BLOCKED

Empty.
