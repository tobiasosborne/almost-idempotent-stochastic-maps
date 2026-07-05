# Run bundle: sigma-door ratio census (wave 17b decider) — 2026-07-05

**Status: L3 numerical evidence — a census, i.e. evidence-of-absence; NEVER an emptiness claim
(the wave-15 lesson is stamped on this bundle: a failed search is never emptiness evidence).**
Exact ℚ throughout. Codex-worker-authored (prompt in the session scratchpad); worker script
rerun by the orchestrator (exit 0); the three calibration hard-asserts anchor the implementation
to previously banked exact witnesses. Companion wave artifact:
`docs/waves/2026-07-05-W17b-door-ratio-census.md`.

## Hypothesis / adversarial question

First-ever measurement of the wave-17 "door ratio" `R_door = max_s S*_s(U0) / (σ_g·H)` in the
D1-reduced regime (hidden top vertices with halo-robust `σ_g > 1/2`, `δ ≤ 1/4`): drive it to 0
(kills the ⟨3⟩3 dictionary door), find a floor (supports it), or report the regime unrealized.

## Headline finding

**REGIME-EMPTY-SO-FAR.** 514 rank-3 exact instances analyzed (0 errors/skips), 298 certified
with `0 < δ ≤ 1/4` and nonempty `W`; 74 instances carried hidden top vertices (138 vertices
measured); 50 hidden tops had `σ_g > 0`; **0 had `σ_g > 1/2`**. Best realized halo mass:
`σ_g = 1/25` (`δ = 6/125`, `H = 1/10`, `R_door = 21/2` there). Also 0 realizations of the D3
mode (argmin chart containing a hidden top) and 0 D5 zero-pivot-visibility examples.

## Honest scope + strategic reading (orchestrator)

The door ratio is UNDECIDED in its intended high-halo branch — the regime was not realized in
these families. The strategic content is the SLACK: the D1 reduction (wave 17, worker T1) shows
a constant cap `σ_g ≤ 1/2` for hidden tops under the cap yields Kernel outright with `B = 29/8`
(via the af-validated halo-collapse), and this census realizes at most `σ_g = 1/25` — a ≥12×
empirical margin, consistent with the upstream ~25k-instance census (`σ_g ≲ 0.37τ`,
`runs/2026-07-02-sigma-cap-refuter/`). The B4 walls were built against the TIGHTER target
`σ_g ≤ 1 − c·τ` and a specific mechanism (exposedness absorption); whether they bind the
slack-rich constant-cap target is the Route-A re-read question (next session's top item).

## Command (re-run)

```bash
python3 runs/2026-07-05-door-ratio-census/scripts/door_ratio_decider.py   # full census + asserts
```

`data/full-report.md` is the worker's complete report (all hard-assert lines);
`data/census-stdout.txt` is the orchestrator's captured rerun output.

## Invariant / known-value check

The script hard-asserts three calibrations against previously banked exact witnesses before any
hunting: (i) the s5 instance (`δ = 1841/1600000`, `W = [0,1,2]`, `H = 1/1000`,
`σ_raw(row3) = 1/2000`, `σ_g(row3) = 0`); (ii) the web headline (`δ = 49/2000`, `W = [0,1,2]`,
`H = 1/20`, hidden tops `[3,4]`); (iii) the sigma-halo non-robustness witness
(`δ = 252559/1280000`, `σ_raw = 5343/5000`, **`σ_g = 0`** — the implementation reproduces the
known raw-vs-halo-robust divergence exactly). 19 hard asserts total; rerun exit 0.

## Next

Worker-named follow-up: replace family search by an exact feasibility/branch-and-bound
optimization for `σ_g > 1/2` (fix rank-3 `Λ = [I; C]`, impose a candidate hidden-top/visible-set
combinatorial type + τ/4 halo membership, solve for the remaining block exactly). Orchestrator
addition: the Route-A wall re-read (do the B4 death certificates even apply to the constant-cap
target?) now outranks it — both queued for session 9.
