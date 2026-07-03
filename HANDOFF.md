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

## Current state (2026-07-03, session 4 CLOSE) — TWELVE rigorous results

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

**D3–D6 (post-checkpoint):** (SI) REFUTED exactly (D3 centered-fan argmin certificate — external
sources alone cannot pay; own-negativity R_D^ν is the missing source; FINDINGS entry) ⇒ survivor
(RSI) `M_D ≤ C_src(G⁻+S⁻^μ+R_D^ν)` — UNBROKEN, C_src=1 sharp at the D3 fan. (BN) got its first
exact β-negative instances: alive, worst 3/32. D4: import decomposition PROVED-inline (class rows
import-safe; imports chain only through B rows); B-block contraction KILLED exactly (ρ_B=21/20
argmin certificate). D5: the exact β-stationarity financing ledger PROVED-inline (D4 refuter
financed to the penny by the negative pivot-class aggregate); but the WIE→RSI composition is
TAUTOLOGICAL — the legal baseline L_μ leaks in ⇒ **the payment and legal horns are COUPLED**;
resisting statement (FIN). D6: the leak is REALIZED — exact argmin certificates (L_μ/δ ≈ 1 with
M_D>0; F_L>0; (FIN) at C=1 stressed); the argmin-mechanism impossibility lemma is FALSE (FINDINGS).

**Chain summary at close:** [(FIN) with C_fin>1 + legal collateral theorem — the two COUPLED open
mechanisms] ⇒ (RSI)+(BN) ⇒ (TT) ⇒ payment horn ⇒ (EX) ⇒ [rigorous lem-factorization] ⇒ C_sf ⇒ …
op-classical. B-side (cap) unchanged/parked.

## Next steps (ranked) — RESUME HERE

1. **The legal collateral theorem** — `strict legal contributor at a maximal pivot ⇒ Φ ≤
   C_legal·δ` (D6 rec 3): the legal horn's real open mechanism; must use more than Schur norms
   (A9: crude Lipschitz circular; D6: no useful collateral lower bound). THE hard open on the
   A/D-side, now explicitly coupled to the payment side via (FIN).
2. **(FIN) with C_fin > 1** — the joint legal-aware financier statement (D5 §T2, stressed but
   unbroken by D6 certificate B). Decide or reduce it.
3. **Codify + af-elevate the provable infrastructure** (small trees, quota-cheap):
   `lem-beta-stationarity-excess-ledger` (D5 (1)/(2)), `lem-hm-coordinate-source-split` (D2 (1)),
   `lem-class-negative-budget` (`ΣΓ⁻ ≤ δ`, trivial grouped-negative-part bound), the A12
   λ-correction + perturbed-DRF lemmas. Each is proved in a wave artifact, awaiting elevation.
4. **(BN)** `S⁻^μ ≤ C₋δ`: alive with margin (worst 3/32); one more adversarial hunt then elevate
   or codify as conjecture.
5. **Lab-book shards AISM-08..12** for results 8–12 (ledger rows exist; full sections pending).
6. **USER DECISION pending (aism-136):** lem-dual-localization trivially-true contract.
7. B-side deciders (arm F FAIL-1 hunt; signed Baake–Sumner) when diversifying.

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
