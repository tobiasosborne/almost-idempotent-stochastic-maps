<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md` — esp. L0 rigour ladder, Rule 13 dead routes).
2. Run `fr board` and `bd ready`. Skim `argument/DAG.md` (**12 green nodes**) + `FINDINGS.md` +
   `report/main.pdf` (9 shards; NOTE: sections for results 8–12 not yet written — ledger rows only).
3. Wave artifacts in `docs/waves/` (B1–B4, F1–F2, A1–A12, D1–D2); L3 bundles in `runs/` (6).
4. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-03, session 4 checkpoint) — TWELVE rigorous results

**Rigorous (af-validated in-repo, banked, T0):** 1. `lem-classical-equiv` · 2. `obs-height-collapse` ·
3. `lem-mass-split` · 4. `lem-residual-lower` · 5. `lem-residual-upper` · 6. `conj-halo-collapse`
(B-side bridge) · 7. `lem-factorization` (A-side composition link) · 8. `lem-zerosum-triangle` ·
9. `lem-weighted-min` · 10. **`lem-fan-payment`** (all-mass zero-sum fan payment, constant 2 — NEW
mathematics, explains the certified plateau-2) · 11. `lem-negpart-subadditive` ·
12. **`lem-fan-payment-restricted`** (D-restricted fan payment, SHARP constant `2+√2`; C=2 exactly
refuted — never quote 2 for the restricted variant).

**The A-side reduction cascade (waves A8–A12, D1–D2 — the session's main product):**
(EX) argmin charge = GAP B = [payment horn] + [legal-collateral horn].
Payment horn (`conj-degenerate-payment`) ⇐ discrete side CLOSED (results 10+12) + THE LIFT (A12):
coordinate half EXACT (λ-correction; barycenter defect identically sourced by pivot-row negativity;
perturbed-DRF derived) ⇒ remaining gap = **`conj-degenerate-transport` (TT)**:
`Σ_{D_s} β⁺μ ≤ C_tr·δ` at a θ-½ Φ-argmin. D1 (H–M Thm 1.12): (TT) is exactly an H-M B-row
inequality; quotient harmonicity proved; δ=0 refuter EXCLUDED from D_s. D2: exact source split +
class-negative budget `ΣΓ⁻ ≤ δ` proved inline; remaining = **(SI)** aggregate degenerate source +
**(BN)** β-negative transverse bound (4-piece factoring in the D2 artifact §T4;
`C_tr = C_src(1+C_-)`; then payment horn at `2C_tr` crude).

**Chain summary:** [(SI)+(BN) OPEN] ⇒ (TT) ⇒ payment horn ⇒ (+ legal-collateral horn OPEN) ⇒ (EX)
⇒ [rigorous lem-factorization] ⇒ C_sf ⇒ … op-classical. B-side (cap) unchanged/parked.

## Next steps (ranked) — RESUME HERE

1. **D3 (in flight or next): decide (SI)** — the aggregate degenerate source; the no-center
   internal-transport is the crux; the rigorous fan lemmas may BE the aggregate transport. And hunt
   instances with β-negative B rows ((BN) is untested — the whole zoo has none).
2. **Codify D2's two provable pieces** as registry shards + af-elevate (small trees):
   `lem-hm-coordinate-source-split` (D2 eq. (1)) and `lem-class-negative-budget` (`ΣΓ⁻ ≤ δ`).
3. **Legal-collateral horn** (A9 has the exact disjunction; crude Lipschitz is circular) — needs a
   new idea; no candidate mechanism yet.
4. **Lab-book shards AISM-08..12** for results 8–12 (ledger rows exist; full sections pending).
5. **USER DECISION pending (aism-136):** lem-dual-localization trivially-true contract.
6. B-side deciders (arm F FAIL-1 hunt; signed Baake–Sumner) when diversifying.

## Standing rules (unchanged; see CLAUDE.md + bd memories)

Codex workers only (no Fable subagents); ONE af orchestration at a time; single-minimal af
contracts; pre-factor linear-chain proofs (fan-payment ballooned 39/47 → factored trio validated
15+10+8 clean); node-cap 40 (not 30); no argument//definitions edits while an orchestration runs;
numerics = exact-ℚ L3 bundles with orchestrator recomputation; waves = verbatim docs/waves/
artifacts, honest T0–T3 tiers, fr log per pull, workers told no fr/bd.

## Recipes

```bash
sh scripts/check-all.sh
python3 scripts/seed-af-workspaces.py <id>
python3 scripts/af-orchestrate.py <id> --workers 8 --max-rounds 14 --node-cap 40   # background
fr verify proofs/<id>/export.md --oracle af-<id>   # 12 oracles registered
```

## What is intentionally NOT here

- Any claim that more than TWELVE results are rigorous.
- Any claim (EX)/Kernel/op-classical is closed — open inputs: (SI), (BN), legal-collateral horn,
  B-side cap.
- Constant 2 for the D-RESTRICTED fan payment (sharp is 2+√2; exact refuters in A11).
- Plateau-2 as a theorem for general (EX) (L3 evidence + the rigorous fan-template cases only).
- A git remote (local-only by decision).
