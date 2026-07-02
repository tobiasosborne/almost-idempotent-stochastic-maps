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
| _(none yet)_ | | | | |
