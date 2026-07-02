# Run bundle: web-regime construction hunt (arm F, wave 1) — 2026-07-02

**Status: L3 numerical evidence. NEVER rigorous (CLAUDE.md L0/L3).** Exact-arithmetic (ℚ) throughout;
floats only for ranking/printing. Produced by an opus subagent (arm F wave 1), re-homed from the session
scratchpad; the orchestrator independently recomputed the headline instance (see Invariant).

## Hypothesis

Can an exact signed idempotent (P²=P, rows sum 1, δ ≤ 1/4) ENTER the kernel conjecture's dangerous web
regime — a hidden row vertex with invisible mass σ̃ > τ = √δ AND height H > Bτ (B = 0.536)? The
inherited 67k-instance record never entered it (FINDINGS.md).

## Command (re-run)

```bash
cd runs/2026-07-02-web-regime-hunt/scripts
python3 exact_lp.py            # simplex self-test (validated vs scipy: 300 LPs, 0 fails)
python3 calibrate_s5.py        # pipeline calibration: must reproduce s5 exactly
python3 verify_instance.py     # THE headline certificate (see Invariant below)
python3 exp3.py                # budget family: H=2δ, t*=δ/(1+δ), corner transition — exact
python3 search.py 1 1200 ; python3 search2.py 11 3000 ; python3 exp6_maxHd.py 1 1200
```
Deterministic seeds are the first CLI arg of the search scripts (out_hd_*.txt / out_s2_*.txt are the
retained sweep outputs; ~48,000 exact idempotents, ~500 certified hidden vertices total).

## Finding (headline + honest scope)

1. **The dangerous regime was NOT entered: 0 of ~500 certified hidden vertices had H > Bτ; the joint
   (σ̃ > τ) ∧ (H > Bτ) never occurred** (σ̃/τ up to ≈4 alone; H/τ up to 0.502 alone, at the corner cap).
2. **The s8-style collapse bound `H·(1−σ̃) ≤ ν·(2+4δ)` held with 0/500 violations** — the quantitative
   form of "height cannot be bootstrapped from a shallow web"; the only open door is σ̃ → 1.
3. **Certified finite-δ exceedance of the empirical linear law**: the exact 5×5 instance in
   `verify_instance.py` (generator `build_from_LambdaC`, C = [[1/2−x,1/2+x+p,−p],[1/2+x,1/2−x+p,−p]],
   x = p/3, p = 1/40, R2 = ρ·ones, ρ = 1/100) has δ = 49/2000, hidden rows {3,4}, H = 1/20, hence
   **H/δ = 100/49 ≈ 2.0408 > 2** (hull-dip: the visible archetypes carry their own negativity).
   Scaling the family: H/δ → 2, H/τ → 0 — an O(δ) finite-size effect, kernel-safe.
   **Scope limits:** family-limited search (7 construction families, n ≤ 9); "hidden/exposed" is the
   operational (ρ,κ)-pipeline of the record (t* LP), reimplemented exactly; absence of the regime here
   is evidence of difficulty, not of emptiness.

## Invariant / certificate (what makes this checkable)

- `calibrate_s5.py` must reproduce the s5 known values EXACTLY: δ = 1841/1600000, H = 1/1000,
  σ̃ = 1/2000, W = {0,1,2}, ‖p₄−p₅‖₁ = 2003/2000; cloning row 0 ×3 must leave δ, H, σ̃ invariant.
- `verify_instance.py` must certify the headline instance with a MATCHING primal/dual pair:
  P² = P over ℚ; δ = 49/2000; primal ‖p₃ − (7/15·p₀ + 8/15·p₁)‖₁ = 1/20; dual affine φ with
  ‖a‖∞ = 1, φ(p_w) = {0, 0, −2} ≤ 0 on W, φ(p₃) = 1/20; LP optimum = primal = dual = 1/20.
- **Independent cross-check (done 2026-07-02 by the orchestrator, fresh code, Fractions only):**
  P² = P, row sums, δ = 49/2000, both hidden rows within exactly 1/20 of conv W — all confirmed.
- `exact_lp.py` self-test: exact simplex vs scipy on 300 random LPs, 0 disagreements.

## Next

- af-elevate the collapse-bound candidate (`obs-height-collapse`, registry) — if validated, the kernel
  antecedent formally re-scopes to σ̃ → 1.
- Arm F wave 2 (if pulled): rank-growing shielded constructions targeting 1−σ̃ = O(τ) at small δ; or
  attack `σ̃ ≤ 1−cτ` for hidden vertices analytically (would CLOSE the kernel conjecture via the
  collapse bound).
- Do not re-quote "δ ≥ H/2 with zero exceptions" — see FINDINGS 2026-07-02 correction.
