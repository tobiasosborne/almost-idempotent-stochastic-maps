<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md` — esp. L0 rigour ladder, Rule 13 dead routes).
2. Run `fr board` and `bd ready`. Skim `argument/DAG.md` (**14 green nodes**) + `FINDINGS.md`
   (2026-07-03 orphan section + the 2026-07-04 frame-free callout update) + `docs/LEARNINGS.md`
   (**first entry landed**: the lem-dual-localization tautology) + `report/main.pdf` (15 shards;
   results 1–13 have sections, the 14th is ledger-row-only pending AISM-15, `aism-*` open issue).
3. Wave artifacts in `docs/waves/` (B1–B4, F1–F2, A1–A12, D1–D6, G1–G8, **G9–G11**); L3 bundles in `runs/` (6).
4. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-04, session 6 CLOSE + continuation) — FOURTEEN rigorous results

**Rigorous (af-validated in-repo, banked, T0):** results 1–12 unchanged (see `argument/INDEX.md`) plus
**13. `lem-pivot-removing-move`** — the G7 pivot-removing chart move (exact volume factor `|a_s(j)|`,
coordinate transform, and the max-stationarity disjunction `Phi_s(U) <= max(Psi_j, Gamma_j)` at a θ-½
Φ-argmin). Run 1 clean: 9-node tree, 3 rounds, ZERO challenges, taint 9/9; `fr verify` pass
(oracle `af-lem-pivot-removing-move`). **The (SC)/(PRT) minimality tool is now rigorous.** And
**14. `lem-collateral-import`** — the (CI) import bound `Phi_r(V_j) <= Phi_r(U) + I_{r,j}` (run 1
clean: 32-node tree, 6 rounds, zero open challenges, taint 32/32; imports result 13 as external;
`fr verify` pass). **The collateral branch is bracketed by rigorous statements.**

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

*(2026-07-04 continuation, part 2: `lem-collateral-import` is the **FOURTEENTH rigorous result**
(af-validated run 1, 32 nodes, zero open challenges; `fr verify` pass). Wave 11 RAN — see
`docs/waves/2026-07-04-G11-capped-charge.md`: (CHARGE) PARTIAL; the dominant import reduces via the
exact B-L cancellation `Σ_i β_r(i)a_s(i)=0` to the cross-pivot masses `B_{r,s}+C_{r,s}`, which are
NOT in the pivot-s budget — **the (PRT) residual is now the cross-pivot charge question**. No capped
clean (G) in 360k sweeps; certified capped near miss only (δ=¼, Ψ=69/250 and Γ=21/80 both > M=1/10).)*

1. **Codify + af-elevate the G11 tools (`aism-cw8`)** — TWO separate minimal shards:
   `lem-cross-pivot-cancellation` (the B-L identity, tiny near-definitional tree) and
   `lem-import-reduction` (bound (4), deps on the VALIDATED `lem-collateral-import`).
2. **Arm G wave 12 (`aism-4uh`): the cross-pivot charge decider** — (i) pay `B_{r,s}+C_{r,s}` from
   the pivot-s budget using argmin minimality; or (ii) propose the budget reshape (a transverse-pivot
   term in (SC)/(RH) — the G5→G6 SIGMA-repair pattern one level up; test against ALL certified
   instances); or (iii) capped (G) construction seeded from the G11 near miss (push Ψ below M while
   keeping Γ up). Exact ℚ + complete argmin certification + orchestrator recomputation.
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
fr verify proofs/<id>/export.md --oracle af-<id>   # 14 oracles registered
# wave dispatch:
codex exec --skip-git-repo-check -C <repo> -s workspace-write -o <answer> - < <prompt>
# af export (run INSIDE proofs/<id>/; af export prints to stdout):
cd proofs/<id> && "$AF" export -f markdown > export.md && "$AF" export -f latex > export.tex
```

## What is intentionally NOT here

- Any claim that more than FIFTEEN results are rigorous (all other arm-G output is honest
  conjecture / proved-mod-audit / wave-tier material).
- Any claim (EX)/Kernel/op-classical is closed — open inputs: (PRT)'s (G) collateral branch ⇒ (SC) ⇒
  (RH) on the A-side engine, (BN), the B-side sigma-cap. ((SI), both orphan exclusions, the
  class/signed-only orphan budget, pointwise silent domination: all REFUTED — see FINDINGS.)
- `C_legal = 0` or any orphan budget without the `Σβν` own-negativity term.
- The old `lem-dual-localization` "open problem" — it was a tautology; the successor is
  `conj-skinny-shadow-cap` (see `docs/LEARNINGS.md` 2026-07-04).
- A git remote (local-only by decision).
