VERDICT: **FACTORIZATION VERIFIED** with constants `(a,b) = (2,6)`:

`S*_s(U) <= 2 Phi_s(U) + 6 delta(P)` for any theta-`1/2` chart.

`(EX)` at rank 3: **HOLDS EMPIRICALLY**, not proved. Exact enumeration found no counterexample; worst observed `min_U max_s Phi_s(U) / delta(P)` is exactly `1`, attained by transverse/no-center rank-3 families. This would compose to `C_sf = 2*C0 + 6`, so the empirical `C0=1` would give `C_sf=8`.

Long form is in [proof.md](/tmp/codex-sigma-wall/w41_ex/proof.md). Artifacts saved:

- [rank3_explorer.py](/tmp/codex-sigma-wall/w41_ex/rank3_explorer.py)
- [rank3_results.txt](/tmp/codex-sigma-wall/w41_ex/rank3_results.txt)
- [rank3_results.json](/tmp/codex-sigma-wall/w41_ex/rank3_results.json)
- [rank3_param_scan.json](/tmp/codex-sigma-wall/w41_ex/rank3_param_scan.json)
- [progress.md](/tmp/codex-sigma-wall/w41_ex/progress.md)

Exact coverage: `278` rank-3 records with `delta <= 1/4`, including `220` random and `53` structured adversarial; `2947` theta-half charts checked in those records, `7573` total valid charts. Factorization violations: `0`. No `answer.md` was created.