# INDEX — script / output / run manifest

The evidence-layer manifest: the reverse-lookup that ties producing scripts → run bundles → CSV outputs →
report shards. Distinct from `argument/INDEX.md` (the rigorous DAG) and `definitions/INDEX.md` (the
vocabulary). Hand-maintained in lockstep with content (CLAUDE.md Rule 9); `check-runs.py` verifies every
`runs/` bundle appears here.

## Run bundles

| Run bundle | Question | Producing script | Rigour |
|------------|----------|------------------|--------|
| `runs/2026-07-02-web-regime-hunt/` | Can an exact idempotent enter the dangerous web regime (σ̃>τ ∧ H>Bτ)? → NO in ~48k instances; collapse bound 0/500 violations; certified H/δ=100/49>2 (hull-dip, kernel-safe) | `scripts/` inside the bundle (`verify_instance.py` = headline certificate) | numerical (L3) |
| `runs/2026-07-02-sigma-cap-refuter/` | Can the σ̃-cap be killed (1−σ̃=o(τ))? → NOT genuinely: halo-robust σ̃_g ≤ 0.37τ over ~25k; but ε=0 cap FALSE exactly (σ̃=5343/5000>1 self-mass, instance C); halo-robust collapse bound holds exactly on A/B/C | `scripts/` inside the bundle (`certify.py`, `halo_bound_check.py`) | numerical (L3) |
| _(pending — the ingested 67k-instance record, re-home as a `runs/` bundle: bd aism-4el)_ | | | numerical (L3) |

## Script → output manifest

| Script | Tool | Run bundle | CSV outputs | Figures | Report shard |
|--------|------|------------|-------------|---------|--------------|
| _(none yet)_ | | | | | |

## Planning / reference documents

| Document | Role |
|----------|------|
| `PRD.md` | scope + success criteria (rigour ladder) |
| `RESEARCH_NOTES.md` | open directions (fr arms) + reference-acquisition queue |
| `argument/DAG.md` | the rigorous knowledge DAG (generated) |
| `docs/ingest/` | the ingested classical-portfolio (object of re-establishment; re-tag map in its README) |
