# INDEX — script / output / run manifest

The evidence-layer manifest: the reverse-lookup that ties producing scripts → run bundles → CSV outputs →
report shards. Distinct from `argument/INDEX.md` (the rigorous DAG) and `definitions/INDEX.md` (the
vocabulary). Hand-maintained in lockstep with content (CLAUDE.md Rule 9); `check-runs.py` verifies every
`runs/` bundle appears here.

## Run bundles

| Run bundle | Question | Producing script | Rigour |
|------------|----------|------------------|--------|
| `runs/2026-07-02-undercap-killers/` | Which mechanism-killing witnesses survive the `(EX)` cap? → active-pivot simplification is killed under the cap: certified multiblock charts have `delta=1/100`, up to five pivots with `Phi_s>delta/2`, and `max Phi/delta` up to `7/4`; tiny selected `V>0` also occurs in balanced staircase rows; no row in this bundle reaches `max Phi/delta>2` or `max E/delta>3` under the cap | `runs/2026-07-02-undercap-killers/scripts/certify_undercap_killers.py` | numerical (L3) |
| `runs/2026-07-02-ex-multiblock-coupling/` | Can richer one-anchor, multi-anchor, higher-arity, and cycle/chord shear couplings push the `(EX)` selected ratio past the no-center plateau? → NO in the certified rows: all natural multiblock families checked stay below `2`; calibration reproduces A2 `k=10 -> 7/4` | `runs/2026-07-02-ex-multiblock-coupling/scripts/certify_multiblock_coupling.py` | numerical (L3) |
| `runs/2026-07-02-ex-no-center-highrank/` | Does the no-center path `(EX)` stress ratio plateau or grow with rank? Exact k=6/8 reproduce `3/2`, `5/3`; certified k=10,12,14,16,20,30 follow `2-2/(k-2)` and plateau toward `2`; delta-scale variants do not grow | `runs/2026-07-02-ex-no-center-highrank/scripts/certify_no_center_highrank.py` | numerical (L3) |
| `runs/2026-07-02-web-regime-hunt/` | Can an exact idempotent enter the dangerous web regime (σ̃>τ ∧ H>Bτ)? → NO in ~48k instances; collapse bound 0/500 violations; certified H/δ=100/49>2 (hull-dip, kernel-safe) | `scripts/` inside the bundle (`verify_instance.py` = headline certificate) | numerical (L3) |
| `runs/2026-07-02-sigma-cap-refuter/` | Can the σ̃-cap be killed (1−σ̃=o(τ))? → NOT genuinely: halo-robust σ̃_g ≤ 0.37τ over ~25k; but ε=0 cap FALSE exactly (σ̃=5343/5000>1 self-mass, instance C); halo-robust collapse bound holds exactly on A/B/C | `scripts/` inside the bundle (`certify.py`, `halo_bound_check.py`) | numerical (L3) |
| `runs/2026-07-02-ex-enumeration-rehome/` | Re-home the inherited 67k+ exact-instance d8-d14 linear-law spine plus rank-3 `(EX)` enumeration: `H~=2delta` within inherited generators; rank-3 `(EX)` has 278 `delta<=1/4` records, 2947 in-cap theta-half charts, 0 empirical `C0=1` violations; all evidence only | copied upstream producers in `scripts/`; local invariant `check_invariant.py`; manifest `data/campaign_summary.csv` | numerical (L3) |
| `runs/2026-07-04-cross-pivot-kill-test/` | Do the G11 cross-pivot masses dwarf the pivot-s budget? → NO on all six certified instances: `B_{r,s}=0` everywhere (12 pairs), `C_{r,s}<=2delta` trivially via the Cramer box, worst `(B+C)/budget = 2499/1376 ~ 1.82`; residual localizes to the B-question | `runs/2026-07-04-cross-pivot-kill-test/scripts/cross_pivot_masses.py` (deterministic, known-value asserts) | numerical (L3) |
| `runs/2026-07-04-rank4-transfer-decider/` | Does the (PRT) skeleton transfer beyond rank 3 (session-7 de-risk decider #1)? → PASSES in this search: no rank-4/5 violation of the pivot-removing disjunction (48 theta-half moves) or of the natural `c>0` rank-4 (CI) transcription (144 pairs, worst slack exactly 0); `Phi/delta` plateau intact (`5/4` rank 4, `4/3` rank 5); first nonzero-B instances beyond rank 3, all sub-delta (max `B/delta = 27031/82920`) | `runs/2026-07-04-rank4-transfer-decider/scripts/decider_rank4.py` (deterministic, known-value asserts; orchestrator-recomputed) | numerical (L3) |
| `runs/2026-07-04-small-delta-b-sweep/` | Does `B/delta` amplify at small delta at certified argmins (session-7 de-risk decider #2, the wave-13 gate)? → BOUNDED but LARGE: max certified `B/delta = 8400000/10897843 ~ 0.771` at `delta ~ 0.055` on a clean high-self non-fan Gamma branch (unique certified theta-half argmin); ten points in `[0.69, 0.771]` across two families; every amplification attempt obstructed by argmin switching / branch turning Psi / high-self loss — minimality binds; B-lemma needs `K >= 0.771`, wave 13 GO | `runs/2026-07-04-small-delta-b-sweep/scripts/decider_small_delta.py` (deterministic, G12 calibration assert; orchestrator-recomputed incl. full chart enumeration) | numerical (L3) |
| `runs/2026-07-04-b-amplifier-hunt/` | Wave-13 amplifier: push `sup B/delta` at certified argmins → new record `~0.77764` with an ALGEBRAIC family-limit law (irrational row-loss balance; certified rationals approach from both sides); crossing 1: NO; cloning does not amplify; `B` exceeds the literal (CI)-financed total and the G12 pivot-s budget x4.24 (B needs its OWN delta-financing — NSC/aism-z98 shape; NOT a skeleton kill, see README orchestrator correction) | `runs/2026-07-04-b-amplifier-hunt/scripts/amplifier_wave13.py` (deterministic, dual calibration asserts; orchestrator-recomputed incl. the argmin tie) | numerical (L3) |

## Script → output manifest

| Script | Tool | Run bundle | CSV outputs | Figures | Report shard |
|--------|------|------------|-------------|---------|--------------|
| `runs/2026-07-02-undercap-killers/scripts/certify_undercap_killers.py` | `python3` exact rational arithmetic (`sympy`) | `runs/2026-07-02-undercap-killers/` | `runs/2026-07-02-undercap-killers/data/undercap_killers.csv` | none | none |
| `runs/2026-07-02-ex-multiblock-coupling/scripts/certify_multiblock_coupling.py` | `python3` exact rational arithmetic (`sympy`) | `runs/2026-07-02-ex-multiblock-coupling/` | `runs/2026-07-02-ex-multiblock-coupling/data/multiblock_coupling.csv` | none | none |
| `runs/2026-07-02-ex-no-center-highrank/scripts/certify_no_center_highrank.py` | `python3` exact rational arithmetic (`sympy`) | `runs/2026-07-02-ex-no-center-highrank/` | `runs/2026-07-02-ex-no-center-highrank/data/no_center_highrank.csv` | none | none |
| `runs/2026-07-02-ex-enumeration-rehome/check_invariant.py` + manual re-home manifest | `python3` / manual archival copy | `runs/2026-07-02-ex-enumeration-rehome/` | `runs/2026-07-02-ex-enumeration-rehome/data/campaign_summary.csv` | none | none |
| `runs/2026-07-04-cross-pivot-kill-test/scripts/cross_pivot_masses.py` | `python3` exact rational arithmetic (`fractions`) | `runs/2026-07-04-cross-pivot-kill-test/` | none (stdout table; known-value asserts are the contract) | none | none |
| `runs/2026-07-04-rank4-transfer-decider/scripts/decider_rank4.py` | `python3` exact rational arithmetic (`fractions`) | `runs/2026-07-04-rank4-transfer-decider/` | `runs/2026-07-04-rank4-transfer-decider/data/certified_points.csv` (+ `.json`, `ANSWER.md`) | none | none |
| `runs/2026-07-04-small-delta-b-sweep/scripts/decider_small_delta.py` | `python3` exact rational arithmetic (`fractions`) | `runs/2026-07-04-small-delta-b-sweep/` | `runs/2026-07-04-small-delta-b-sweep/data/certified_points.csv` (+ `.json`, `ANSWER.md`) | none | none |
| `runs/2026-07-04-b-amplifier-hunt/scripts/amplifier_wave13.py` | `python3` exact rational arithmetic (`fractions`) | `runs/2026-07-04-b-amplifier-hunt/` | `runs/2026-07-04-b-amplifier-hunt/data/certified_points.csv` (+ `.json`, `ANSWER.md`) | none | none |

## Planning / reference documents

| Document | Role |
|----------|------|
| `PRD.md` | scope + success criteria (rigour ladder) |
| `RESEARCH_NOTES.md` | open directions (fr arms) + reference-acquisition queue |
| `argument/DAG.md` | the rigorous knowledge DAG (generated) |
| `docs/ingest/` | the ingested classical-portfolio (object of re-establishment; re-tag map in its README) |
