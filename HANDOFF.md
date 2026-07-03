<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md` — esp. L0 rigour ladder, Rule 13 dead routes).
2. Run `fr board` and `bd ready`. Skim `argument/DAG.md` (**12 green nodes**) + `FINDINGS.md`
   (esp. the 2026-07-03 orphan section — FIVE new death certificates this session) +
   `report/main.pdf` (9 shards; sections for results 8–12 still ledger-rows-only).
3. Wave artifacts in `docs/waves/` (B1–B4, F1–F2, A1–A12, D1–D6, **G1–G8**); L3 bundles in `runs/` (6).
4. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-03, session 5 CLOSE) — still TWELVE rigorous results

**Rigorous (af-validated in-repo, banked, T0):** unchanged from session 4 — 1. `lem-classical-equiv` ·
2. `obs-height-collapse` · 3. `lem-mass-split` · 4. `lem-residual-lower` · 5. `lem-residual-upper` ·
6. `conj-halo-collapse` · 7. `lem-factorization` · 8. `lem-zerosum-triangle` · 9. `lem-weighted-min` ·
10. `lem-fan-payment` · 11. `lem-negpart-subadditive` · 12. `lem-fan-payment-restricted`.
**Nothing was promoted this session** (all session-5 output is wave-artifact T0/T1/T2, honestly tagged).

**Session 5 = arm G (flow-conservation), waves G1–G8.** The conjectured circulation engine SURVIVED
adversarial contact and is now a concrete three-part architecture with ONE isolated sub-gap:

- **Fan horn (G1/G2):** fan-matched weights `w_{j,t}=a_t(j)⁻/μ_j` telescope every certified legal leak
  (incl. exact `F_L`) with tested residual constant 0; unoriented weightings FAIL (signed orientation
  forced). Survived adversarial stress (worst certified ratio 814/2149).
- **Repaired orphan horn (RH) (G3–G6):** `OD ≤ C_RH·(G_class⁻ + S⁻^μ + Σ_{β>0} β_jν_j)` — the unified
  own-negativity budget. Exact floor `C_RH ≥ 4` (G5 family, sup exactly 4); survives ALL certified
  instances; D6 certificates have OD=0 after fan separation.
- **(SC) → (PRT), the single open sub-gap (G6–G8):** the argmin self-support/cancellation control,
  reduced to the **high-self pivot-removing blocker/import theorem**: every non-fan β-positive
  high-self row either admits an unblocked admissible pivot-removing move (contradicting argmin) or its
  blocker branch — volume-inadmissible / Ψ-blocked / Γ-blocked — is charged to
  `G⁻+S⁻^μ+SIGMA+FanRes`. Waves G7+G8 both went OPEN on it (tool-building progress, target undecided)
  ⇒ arm yielded per the breaker (fr decision: EXPLORE R).

**Toolkit banked at T1 (worker paper-proofs, unreviewed — NOT rigorous):** G5 harmonic sum rules +
cancellation ledger `P_r^O = N_r^O − H_r − Γ_r`; G6 ambient/chart identity
`(1−P_jj)a_r(j) = Σ_{i≠j}P_ji a_r(i)` + payment overhead `E_s ≤ μ_s` (rank-3 active orphans); G7
pivot-removing disjunction `M ≤ max(Ψ_j,Γ_j)` (volume factor `|a_s(j)|`, NOT `P_jj`) — the first
statement that genuinely uses Φ-minimality; G8 B-block transfer system (`κ_jW_j ≤ S_j⁻+ΣP_ji⁺W_i`,
`S_j⁻ ≤ 4ν_j`) + β-weighted financed-excess identity (reproduces D5's financing on the D4 refuter
exactly).

**Dead this session (FINDINGS death certificates — do NOT re-walk):** literal orphan exclusion (G3);
ACTIVE-row orphan exclusion (G4); rank-3 pure-legal `C_legal=0` (G3); the class/signed-only orphan
budget for EVERY finite constant (G5 exact two-orphan amplifier — NOT an (EX) refuter, `Φ_s/δ → 1`);
pointwise silent domination `ν_j ≥ a_r(j)⁻` (G6 — ambient ν vs chart negativity are different objects).

**Evidence pattern (8 waves):** every exact leak has an exactly identifiable financier; every kill was a
too-small budget, never an (EX)-threatening amplifier. Credence (EX) ~80/20 unchanged; the refutation
program now shares (PRT) (an unpayable blocker family = the reshaped kill criterion).

## Next steps (ranked) — RESUME HERE

1. **(PRT) direct attack (arm G wave 9, `aism-qkv`)** — with a FRESH angle: per-branch exact
   realizability first (construct or exclude each blocker type — volume-inadmissible / Ψ-blocked /
   Γ-blocked high-self non-fan row at a certified argmin), NOT another aggregate pass (G7/G8 both went
   OPEN on aggregate attacks). The branch that resists realization is the one to prove impossible.
2. **Registry codification of arm G outputs (`aism-l70`) — needs a USER decision:** register `conj-rh`,
   `conj-sc`/(PRT), `obs-orphan-amplifier` (G5 family), `lem-pivot-removing-move` (G7 tool). Blocker:
   contract vocabulary (H-M class aggregates beyond singleton classes, θ-½ argmin chart, orphan row) —
   either (a) add def shards or (b) fully-inline contracts in the `conj-degenerate-transport` style.
3. **af-elevate the provable infrastructure** (unchanged queue from session 4, now larger): the D5
   ledger lemma, D2 source split, `ΣΓ⁻ ≤ δ` budget, A12 λ-correction/perturbed-DRF; NEW candidates
   once codified: the G5 ledger, G6 ambient/chart identity, G7 pivot-removing formulas (small trees,
   pre-factored — remember the fan-payment 39/47-node lesson).
4. **(BN)** `S⁻^μ ≤ C₋δ`: alive (worst 3/32); one more adversarial hunt then elevate or codify.
5. **Lab-book shards AISM-08..12** for results 8–12 (ledger rows exist; sections pending).
6. **USER DECISION pending (aism-136):** lem-dual-localization trivially-true contract.
7. B-side deciders (arm F FAIL-1 hunt; signed Baake–Sumner) when diversifying.

## Standing rules (unchanged; see CLAUDE.md + bd memories)

Codex workers only (no Fable subagents); ONE af orchestration at a time; single-minimal af contracts;
pre-factor linear-chain proofs; node-cap 40; no argument//definitions edits while an orchestration runs;
numerics = exact-ℚ L3 bundles with orchestrator recomputation; waves = verbatim docs/waves/ artifacts,
honest T0–T3 tiers, fr log per pull, workers told no fr/bd. Session-5 addition: wave prompts live in the
session scratchpad (g1–g8-prompt.md pattern); worker answers + transcripts likewise.

## Recipes

```bash
sh scripts/check-all.sh
python3 scripts/seed-af-workspaces.py <id>
python3 scripts/af-orchestrate.py <id> --workers 8 --max-rounds 14 --node-cap 40   # background
fr verify proofs/<id>/export.md --oracle af-<id>   # 12 oracles registered
# wave dispatch (session-5 pattern):
codex exec --skip-git-repo-check -C <repo> -s workspace-write -o <answer> - < <prompt>
```

## What is intentionally NOT here

- Any claim that more than TWELVE results are rigorous (ALL arm-G output is T0/T1/T2 wave material).
- Any claim (EX)/Kernel/op-classical is closed — open inputs: (PRT)⇒(SC)⇒(RH) on the A-side engine,
  (BN), B-side cap. ((SI), both orphan exclusions, the class/signed orphan budget, pointwise silent
  domination: all REFUTED — see FINDINGS.)
- `C_legal = 0` or any orphan budget without the `Σβν` own-negativity term.
- A git remote (local-only by decision).
