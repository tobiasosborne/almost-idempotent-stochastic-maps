<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md` — esp. L0 rigour ladder, Rule 13 dead routes).
2. Run `fr board` and `bd ready`. Skim `argument/DAG.md` (**13 green nodes**) + `FINDINGS.md`
   (2026-07-03 orphan section + the 2026-07-04 frame-free callout update) + `docs/LEARNINGS.md`
   (**first entry landed**: the lem-dual-localization tautology) + `report/main.pdf` (14 shards;
   results 1–12 have sections, the 13th is ledger-row-only pending AISM-14).
3. Wave artifacts in `docs/waves/` (B1–B4, F1–F2, A1–A12, D1–D6, G1–G8, **G9**); L3 bundles in `runs/` (6).
4. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-04, session 6 CLOSE) — THIRTEEN rigorous results

**Rigorous (af-validated in-repo, banked, T0):** results 1–12 unchanged (see `argument/INDEX.md`) plus
**13. `lem-pivot-removing-move`** — the G7 pivot-removing chart move (exact volume factor `|a_s(j)|`,
coordinate transform, and the max-stationarity disjunction `Phi_s(U) <= max(Psi_j, Gamma_j)` at a θ-½
Φ-argmin). Run 1 clean: 9-node tree, 3 rounds, ZERO challenges, taint 9/9; `fr verify` pass
(oracle `af-lem-pivot-removing-move`). **The (SC)/(PRT) minimality tool is now rigorous.**

**Session 6 headlines:**

- **Wave G9 (arm G): (PRT) narrowed to ONE branch.** The three pivot-removing blocker branches were
  attacked by per-branch exact realizability: **(V)** volume-inadmissible REALIZED (exact certified
  argmin, score-degenerate `M=0`, charge ratio `624/4427`); **(P)** Ψ-blocked REALIZED (genuine blocker
  `91/300 ≥ M=1/12`, ratio `240/451`); amplification probes bounded on both families. **(G)**
  Γ/collateral: neither realized nor proved empty ⇒ **THE isolated open piece of (PRT) is the collateral
  branch.** Both certificates orchestrator-recomputed exactly. Artifact `docs/waves/2026-07-04-G9-*`.
- **Two USER decisions executed:** (a) arm-G codification uses **fully-inline contracts** (no def shards
  while the vocabulary moves; revisit after (PRT)); (b) **`lem-dual-localization` superseded by
  `conj-skinny-shadow-cap`** — the transcribed contract was a distance tautology (B1 + independent codex
  verifier; upstream DELIVERABLE2:86 mislabelled it). Retired to `obstruction`; first
  `docs/LEARNINGS.md` entry; all callouts updated in lockstep.
- **Arm-G outputs codified (registry now 41 results):** `conj-rh` (repaired orphan horn; body records
  the exact floor `C_RH ≥ 4`), `conj-sc` (the (SC) control; body records the (PRT) reduction + G9
  narrowing), `obs-orphan-amplifier` (proved-mod-audit; contract identities orchestrator-recomputed at
  four parameter values), `lem-pivot-removing-move` (now proved/validated). deps left EMPTY per
  conjecture precedent — assembly expectations live in bodies, NOT as DAG edges.
- **Lab-book:** shards AISM-08..12 landed (results 8–12, contracts verbatim); status ledger renumbered
  to `13_discussion.tex`; **gate fix**: `check-provenance.py` hard-coded the ledger filename — after the
  rename the status-drift check silently parsed zero rows (false green); fixed + red/green probed.

**Review discipline this session (worked):** codex drafted the codification → independent codex review
returned REQUEST-CHANGES (4 real transcription fixes: Schur volume factor `|det C|` wording, λ-positive
strict-legal cover clause, silent-row universal quantifier, Φ/δ→1 transcription — plus it caught a body
truncation from the orchestrator's extraction script) → fixes applied verbatim → a third fresh codex
confirm-pass CONFIRMed. Reviewer ≠ author throughout; three distinct codex reviewers used.

## Next steps (ranked) — RESUME HERE

1. **Arm G wave 10 (`aism-93m`): decide the (G) collateral branch** — (i) targeted construction:
   two-blocker-row designs where `V_j` is admissible, `Psi_j < M`, but some other pivot `r` has
   `Phi_r(V_j) ≥ M` (build on the NOW-RIGOROUS `lem-pivot-removing-move` disjunction + transform
   formulas); (ii) if construction resists, the emptiness lemma: bound `Gamma_j` by old-chart scores +
   imports via the G8 transfer ledger, pre-factored for af. Either output decides the (PRT) assembly
   shape. δ ≤ ¼ + complete argmin certification + exact ℚ mandatory; orchestrator recomputation of any
   headline certificate.
2. **AISM-14 section shard (`aism-t5c`)** for the 13th rigorous result (ledger row + PROVENANCE say
   "section pending").
3. **af-elevation backlog** (codify-then-elevate, per the session-5 queue): the D5 ledger lemma, D2
   source split, `ΣΓ⁻ ≤ δ` budget, A12 λ-correction/perturbed-DRF; G5 harmonic/cancellation ledger, G6
   ambient/chart identity + payment overhead `E_s ≤ μ_s`. All still need registry codification first
   (same inline-contract convention). Remember: single-minimal contracts; pre-factor linear chains.
4. **(BN)** `S⁻^μ ≤ C₋δ`: alive (worst 3/32); one more adversarial hunt then elevate or codify.
5. **B-side** when diversifying: the sigma-cap is the live target; `conj-skinny-shadow-cap` is the
   corrected Route-B statement (arm F FAIL-1 hunt; signed Baake–Sumner as deciders).

## Standing rules (unchanged; see CLAUDE.md + bd memories)

Codex workers only (no Fable subagents); ONE af orchestration at a time; single-minimal af contracts;
pre-factor linear-chain proofs; node-cap 40; no argument//definitions edits while an orchestration runs
(commit BEFORE launching — the overreach guard is git-porcelain-based); numerics = exact-ℚ with
orchestrator recomputation; waves = verbatim docs/waves/ artifacts, honest T0–T3 tiers, fr log per pull,
workers told no fr/bd; wave prompts + answers + transcripts live in the session scratchpad.

## Recipes

```bash
sh scripts/check-all.sh
python3 scripts/seed-af-workspaces.py <id>       # then COMMIT before orchestrating
python3 scripts/af-orchestrate.py <id> --workers 8 --max-rounds 14 --node-cap 40   # background
fr verify proofs/<id>/export.md --oracle af-<id>   # 13 oracles registered
# wave dispatch:
codex exec --skip-git-repo-check -C <repo> -s workspace-write -o <answer> - < <prompt>
# af export (run INSIDE proofs/<id>/; af export prints to stdout):
cd proofs/<id> && "$AF" export -f markdown > export.md && "$AF" export -f latex > export.tex
```

## What is intentionally NOT here

- Any claim that more than THIRTEEN results are rigorous (all other arm-G output is honest
  conjecture / proved-mod-audit / wave-tier material).
- Any claim (EX)/Kernel/op-classical is closed — open inputs: (PRT)'s (G) collateral branch ⇒ (SC) ⇒
  (RH) on the A-side engine, (BN), the B-side sigma-cap. ((SI), both orphan exclusions, the
  class/signed-only orphan budget, pointwise silent domination: all REFUTED — see FINDINGS.)
- `C_legal = 0` or any orphan budget without the `Σβν` own-negativity term.
- The old `lem-dual-localization` "open problem" — it was a tautology; the successor is
  `conj-skinny-shadow-cap` (see `docs/LEARNINGS.md` 2026-07-04).
- A git remote (local-only by decision).
