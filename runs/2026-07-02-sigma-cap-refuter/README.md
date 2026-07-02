# Run bundle: σ̃-cap refuter sweep (arm F, wave 2) — 2026-07-02

**Status: L3 numerical evidence. NEVER rigorous.** Exact ℚ certificates; floats only for search.
Shares the exact pipeline of `runs/2026-07-02-web-regime-hunt/` (exact_lp/pipeline/gen — import from there
or from the scratchpad copies).

## Hypothesis

Can the σ̃-cap (`1−σ̃_v ≥ cτ` for hidden top vertices) be KILLED by an exact construction with
`1−σ̃ = o(τ)` — especially the low-height halo-straddling configs flagged by arm B wave 3 (Step D)?

## Command (re-run)

```bash
cd runs/2026-07-02-sigma-cap-refuter/scripts
python3 certify.py            # exact certification of instances A (max genuine σ̃_g) and C (σ̃>1 self-mass)
python3 certify_best.py       # instance B (max H/τ with a genuine distinct recipient)
python3 halo_bound_check.py   # the [check] halo-robust collapse bound on all three instances, exact
python3 search4f.py 7 4000    # the randomized frontier sweep (seed, nsamp)
```

## Finding (headline + honest scope)

1. **NOT a kill — the halo-robust cap survives with margin**: over ~25k float-searched hidden top
   vertices, genuine invisible mass (recipients at dist ≥ τ/4) never exceeded ≈0.37τ, i.e.
   `1−σ̃_g ≥ 0.92` everywhere; max H/τ = 0.462 (< corner 0.536); the dangerous joint regime
   remains un-entered.
2. **The ε=0 cap is FALSE as literally written**: exact certificate (instance C) with
   δ = 252559/1280000, hidden top vertex with σ̃ = 5343/5000 > 1 — entirely SELF-mass (P_vv > 1)
   at recipient distance 0.02τ; σ̃ restricted to dist ≥ τ/4 is exactly 0. Pure halo effect.
3. **[check] halo-robust collapse bound** `H(1−σ̃_g) ≤ (σ̃−σ̃_g)·τ/4 + ν(2+4δ)`: holds exactly and
   non-vacuously on all three certified instances (gives H ≤ 0.45–0.70τ). Elevation candidate.
   **Scope limits**: family-limited search; the "no-free-frontier" wall mechanism is a [check]
   heuristic, not a theorem; kill ⟺ dangerous-regime equivalence uses the af-validated collapse bound.

## Invariant / certificate (checkable)

- `certify.py` must reproduce instance C exactly: P²=P over ℚ, δ = 252559/1280000,
  σ̃ = 5343/5000, halo-restricted σ̃ (≥τ/4) = 0, clone-invariance under row-split.
- **Independent cross-check (orchestrator, 2026-07-02, fresh code)**: rebuilt instance C from its
  generator parameters, verified P²=P exactly, row sums, δ = 252559/1280000, and the self-mass
  entry P_vv = 5343/5000 — all confirmed.
- `halo_bound_check.py`: the halo-robust bound must hold exactly on instances A/B/C.
- Calibration: pipeline must still reproduce s5 and the wave-1 headline (H/δ = 100/49) exactly.

## Next

- af-elevate the halo-robust collapse bound (registry: conj-halo-collapse).
- Attack the no-free-frontier exposedness-absorption mechanism (registry: conj-no-free-frontier).
- Never state the σ̃-cap at ε=0 (see FINDINGS 2026-07-02; registry obs-sigma-halo-nonrobust).
