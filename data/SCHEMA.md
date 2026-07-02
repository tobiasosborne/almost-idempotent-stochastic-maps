# data/SCHEMA.md — CSV column contracts for run outputs

Every CSV produced under `runs/<bundle>/data/` is listed here with its column contract, and reverse-
listed in the top-level `INDEX.md`. This is the third leg of the provenance triangle
(INDEX reverse-lookup ↔ this SCHEMA ↔ producing script). `data/` at the repo top level holds **no
generated data** — it holds only this schema (aqm discipline).

## Common rules

- **Sentinel rows.** A row whose first column begins with `#` is a comment/caveat line, not data;
  parsers must skip it. Use it for supersession, negative-control, or missing-tool status.
- **Exact vs float.** Column suffix `_exact` = string of the exact value in the producing tool;
  `_float` = floating approximation; `_residual` = declared normed error (document the norm +
  denominator + precision here). Finite precision is not exact evidence — prefer exact/finite-field
  arithmetic and boolean certificate columns (e.g. `dual_feasible`, `sos_certificate`).

## Per-CSV registry

| CSV | Produced by | Run bundle | Report shard | Columns |
|-----|-------------|------------|--------------|---------|
| `runs/2026-07-02-ex-enumeration-rehome/data/campaign_summary.csv` | manual re-home manifest from archived upstream outputs | `runs/2026-07-02-ex-enumeration-rehome/` | none | see contract below |

### `runs/2026-07-02-ex-enumeration-rehome/data/campaign_summary.csv`

Column contract:

- `artifact_id`: stable row id for this re-home manifest.
- `campaign`: upstream campaign or enumeration label.
- `upstream_path`: read-only source path used for the re-home.
- `local_path`: path inside the run bundle, or `not_copied` for a report-only inventory row.
- `instance_count`: archived instance count when the source gives one; `NA` if not applicable.
- `delta_cap_count`: count inside the stated `delta` cap, when applicable.
- `chart_count`: chart/enumeration count, when applicable.
- `violation_count`: empirical violation count in the archived source's own terminology.
- `key_metric`: compact headline metric; parse as descriptive text, not a theorem.
- `status`: rigour tag; all rows here are `numerical_L3`.
- `sha256`: SHA-256 of the local copied artifact when one exists; `NA` otherwise.
