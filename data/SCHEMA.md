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
| `runs/2026-07-02-undercap-killers/data/undercap_killers.csv` | `runs/2026-07-02-undercap-killers/scripts/certify_undercap_killers.py` | `runs/2026-07-02-undercap-killers/` | none | see contract below |
| `runs/2026-07-02-ex-multiblock-coupling/data/multiblock_coupling.csv` | `runs/2026-07-02-ex-multiblock-coupling/scripts/certify_multiblock_coupling.py` | `runs/2026-07-02-ex-multiblock-coupling/` | none | see contract below |
| `runs/2026-07-02-ex-no-center-highrank/data/no_center_highrank.csv` | `runs/2026-07-02-ex-no-center-highrank/scripts/certify_no_center_highrank.py` | `runs/2026-07-02-ex-no-center-highrank/` | none | see contract below |
| `runs/2026-07-02-ex-enumeration-rehome/data/campaign_summary.csv` | manual re-home manifest from archived upstream outputs | `runs/2026-07-02-ex-enumeration-rehome/` | none | see contract below |

### `runs/2026-07-02-undercap-killers/data/undercap_killers.csv`

Column contract:

- `family`: construction family label, or a sentinel comment beginning with `#`.
- `params`: exact parameter description: shear scale, foreign count, staircase scale, and left-inverse scale when applicable.
- `k`: rank parameter, equal to the number of columns in the coordinate matrix `L`.
- `n_rows`: number of actual rows in `L` and hence the size of `P=LB`.
- `delta_exact`: exact negative-mass value as a rational string.
- `under_cap`: boolean string recording whether `delta_exact <= 1/4`.
- `phi_over_delta_exact`: exact selected-chart value `min_U max_s Phi_s(U)/delta(P)` over the certified theta-half chart class.
- `sum_phi_over_delta_exact`: exact selected-chart value `sum_s Phi_s(U)/delta(P)` at the same argmin chart.
- `active_pivots_gt_delta_half`: count of pivots at the selected chart with `Phi_s > delta(P)/2`.
- `max_E_over_delta_exact`: exact selected-chart maximum of rowwise `E_s(j)/delta(P)`.
- `V_over_delta_exact`: exact selected-chart maximum of `V_s(U)/delta(P)`.
- `certification`: one of `full_enumeration`, `certified_reduction`, `upper_bound_only`.
- `charts_checked`: number of theta-half charts covered after the stated certification step.
- `notes`: compact exact checks/caveats, including selected basis, nonzero pivot scores or per-anchor minima, determinant reduction when used, and `BL`/`P2`/row-sum/`DEF` checks.

### `runs/2026-07-02-ex-multiblock-coupling/data/multiblock_coupling.csv`

Column contract:

- `family`: construction family label, or a sentinel comment beginning with `#`.
- `params`: exact parameter description: shear scale, foreign coordinate count, graph/fan choice, and any calibration note.
- `k`: rank parameter, equal to anchors plus foreign coordinates.
- `n_rows`: number of actual rows in `L` and hence the size of `P=LB`.
- `delta_exact`: exact negative-mass value as a rational string.
- `phi_over_delta_exact`: exact selected-chart value `min_U max_s Phi_s(U)/delta(P)` over the certified theta-half chart class.
- `phi_over_delta_float`: decimal display of `phi_over_delta_exact`; not certified evidence.
- `certification`: one of `full_enumeration`, `certified_reduction`, `upper_bound_only`.
- `charts_checked`: number of theta-half charts covered after the stated certification step.
- `notes`: compact exact checks/caveats, including determinant-reduction bound, selected chart, `Sstar/delta`, per-anchor minima, `BL`, `P2`, row-sum, and direct-delta checks.

### `runs/2026-07-02-ex-no-center-highrank/data/no_center_highrank.csv`

Column contract:

- `k`: rank parameter of the no-center path instance, or a sentinel comment beginning with `#`.
- `family`: no-center path scale label; sentinel rows carry caveats.
- `delta_exact`: exact negative-mass value as a rational string.
- `phi_over_delta_exact`: exact selected-chart value `min_U max_s Phi_s(U)/delta(P)` as a rational string.
- `phi_over_delta_float`: decimal display of `phi_over_delta_exact`; not certified evidence.
- `certification`: one of `full_enumeration`, `certified_reduction`, `upper_bound_only`.
- `charts_checked`: number of theta-half charts evaluated after the stated certification step.
- `notes`: compact exact checks/caveats, including `BL`, `P2`, `rowsum`, selected chart, and `Sstar/delta`.

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

### `runs/2026-07-04-rank4-transfer-decider/data/certified_points.csv`

Column contract (all exact values are rational strings; one row per certified instance):

- `name`: stable instance id (`CALIBRATION_*` = known rank-3 reproduction; `*rank5*` = cheap probe).
- `family`: construction family (`calibration`, `no-center`, `cycle-coupling`).
- `rank` / `n`: rank of `P` and ambient dimension.
- `delta`: exact negative mass `delta(P)`.
- `theta_charts` / `argmin_count` / `argmin_basis`: theta-half chart census at the certified argmin
  (complete enumeration over actual-row charts; basis = row indices, space-separated).
- `phi` / `phi_over_delta` / `max_phi_s_over_delta`: exact argmin `Phi` values and ratios.
- `max_B_over_delta` / `max_BC_over_delta`: cross-pivot masses under the G12 convention (`s` = maximal
  pivot, `r` transverse) — NOT the all-ordered-pairs maximum (see bundle README finding 3).
- `pivot_moves_checked` / `positive_c_moves`: pivot-removing disjunction checks (all theta-half moves;
  disjunction asserted exactly on each).
- `ci_pairs_checked` / `worst_ci_slack`: rank-4 `c>0` (CI) transcription checks; slack `0` = sharp.
- `rank5_probe`: `True` for the cheap rank-5 probes (reduced coverage — see bundle README scope).

### `runs/2026-07-04-small-delta-b-sweep/data/certified_points.csv`

Column contract (exact values are rational strings; one row per certified (instance, s, r) mass):

- `name` / `family`: instance id and construction family (`compensated-insert`, `two-carrier`).
- `delta`: exact negative mass `delta(P)`.
- `U`: certified theta-half Phi-argmin chart (row indices, space-separated; complete actual-row chart
  enumeration per instance).
- `s` / `r`: maximal pivot and transverse index for the reported masses (G12 convention).
- `B` / `C` / `A` / `D`: exact cross-pivot masses; cancellation `A = B + C - D` hard-asserted.
- `B_over_delta`: the decider quantity (headline max `8400000/10897843` at `delta = 55319/1000000`).
- `clean_gamma_js` / `gamma_js`: count of branch rows classified clean-high-self-non-fan-Gamma / Gamma
  at this argmin (worker's implementation of the G12 branch conventions).
