<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md` — esp. L0 rigour ladder, Rule 13 dead routes).
2. Run `fr board` and `bd ready`. Skim `argument/DAG.md` (3 green nodes now) + `FINDINGS.md` (four dated
   2026-07-02 entries — constants pinned, linear-law correction, halo non-robustness, B4 walls-check).
3. Wave artifacts in `docs/waves/` (B1–B4, F1, F2 — verbatim harvests); L3 bundles in `runs/` (3, all
   gate-green, incl. the re-homed 67k record).
4. Gate before committing: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-02, session 3, mid-flight) — THREE rigorous results; bridge validation underway

- **Rigorous (af-validated in-repo, banked via fr verify, T0):**
  1. `lem-classical-equiv` — signed↔stochastic bridge (29-node tree).
  2. `obs-height-collapse` — collapse bound `H(1−σ̃) ≤ ν(2+4δ)` (19-node tree).
  3. `lem-mass-split` — `Σ a_j⁺ = 1+ν_v` (9-node tree, clean) — 1st of the aism-q7e factoring.
- **In flight (af trees built, verify stalled at 16:00 quota; resume on refresh ~16:16):**
  - `lem-residual-lower` (33 nodes, 12 validated, ALL challenges resolved, 18 awaiting verifiers) —
    resume `--phase verify --node-cap 40`.
  - `lem-residual-upper` (38 nodes, 17 validated, 4 OPEN dependency-scoping challenges) — resume
    `--phase verify --node-cap 48`; if it balloons AGAIN, factor the recombination algebra identity
    `m(q−b) = Σ b_j(p_j−β_j) + Σ c_k(b−r_k)` into a registry sub-lemma (drafted in session notes).
- **Registry: 29 nodes.** `conj-halo-collapse` now imports the three sub-lemmas (deps registered,
  codex-reviewed PASS). Root contract UNCHANGED; partial run-1 tree retained.
- **Known WARNs (accepted, tracked aism-6ec):** five >12-node REFACTOR warnings; 26 report-anchor
  provenance warnings (report shards still don't exist — ranked step 4 below).

## The frontier (after B4, 2026-07-02)

**The cap mechanism is wall-blocked; the bridge is the live elevation.** Chain status:

- `conj-halo-collapse` (bridge, `H(1−σ̃_g) ≤ (σ̃−σ̃_g)τ/4 + ν(2+4δ)`): factored per aism-q7e into
  `lem-mass-split` (BANKED), `lem-residual-lower`/`-upper` (in verify flight). When all three are
  `af: validated` → wipe + re-seed the bridge workspace (contract unchanged, deps as externals) →
  re-orchestrate (`--workers 8 --max-rounds 12 --node-cap 40`).
- `conj-no-free-frontier` (cap mechanism): **DO NOT af-ELEVATE** — B4 walls-check verdict CONDITIONAL:
  dodges the one-sided ledger (genuinely: positional, no P-coefficient) but the composed σ̃_g bound
  re-imports the dimension-free class count (dead route c10/c20), and uniform κ=τ/4 is plausibly FALSE
  as written (FAIL-1, dense-regular-polygon). Artifact: `docs/waves/2026-07-02-B4-walls-check.md`.
- **The cap itself (`σ̃_g ≤ 1−c`) is still THE open finisher input**, now needing a NEW ledger-immune,
  class-count-free mechanism, or the class-count decider (open signed quantitative Baake–Sumner), or
  the FAIL-1 exact-instance decider (both recorded in B4 §6).
- Closed families (do not re-walk): v-local (`obs-deep-leakage`), web-rigidity (`obs-fwr-gap`), ε=0 cap
  (`obs-sigma-halo-nonrobust`), cap-via-exposedness-absorption (B4), + all inherited dead routes.

## Next steps (ranked) — RESUME HERE

1. **On quota refresh (~16:16): resume the two residual verify runs** (commands above; timer armed).
   Bank each on clean validation: `af export` → status flip (mechanical) → linker regen → gate →
   commit → `fr verify` (oracles `af-lem-residual-lower/-upper` already registered) → `fr log R`.
   ⚠ Process gotcha (bd memory): NO argument/ or definitions/ edits while ANY orchestration is live —
   the overreach guard is git-porcelain-based and aborts every live run.
2. **Then the bridge re-run (aism-q7e finish):** `rm -rf proofs/conj-halo-collapse` (tree is committed;
   set shard `af: seeded→none` first), re-seed via `seed-af-workspaces.py conj-halo-collapse`,
   re-orchestrate `--workers 8 --max-rounds 12 --node-cap 40`. On validation: bank + close aism-q7e.
   NOTE the linker: bridge can be `af: validated` only when all three deps are.
3. **USER DECISION pending (aism-136, flagged `bd human`):** `lem-dual-localization` contract confirmed
   trivially-true-as-stated (codex verification, notes in the issue). Candidate corrected contracts in
   the bd notes; do not edit unilaterally.
4. Report shards (`AISM-NN`) for the three rigorous results + PROVENANCE rows — clears the 26 anchor
   warnings, starts the lab-book. Then `aism-6ec` (factoring decision for >12-node validated trees).
5. **Cap strategy (the real open question):** arm B is 4×✗ and wall-blocked; arm A ((EX) chart bound)
   is the untried PRIMARY — a first scoping wave is the natural next EXPLORE once the bridge is banked.
   The B4 deciders (FAIL-1 instance hunt = arm F work; class-count = dead-route territory, do not
   re-walk without a new idea) are recorded in the artifact.

## Standing role/process rules (user-mandated 2026-07-02)

- Orchestrator = knowledge/strategy overview + proof-direction evaluation; NEVER verifies proofs
  (codex/af does). No Fable subagents without explicit permission — **prefer codex over opus/sonnet**
  (user 2026-07-02).
- af contracts: SINGLE minimal statement (bd memory `af-elevation-contracts-must-be-a-single-minimal`).
- Numerics: exact-ℚ certificates, L3 bundles, orchestrator independently recomputes headline claims.
- Waves: verbatim harvest artifact in `docs/waves/`, honest-status codification, fr log per pull.
- No argument/definitions edits while orchestrations run (bd memory, overreach guard).

## Recipes / commands

```bash
sh scripts/check-all.sh                          # the gate
python3 scripts/argument.py --sync-beads          # idempotent DAG→beads mirror
fr board ; fr status                              # the portfolio
python3 scripts/seed-af-workspaces.py <id>        # seed one af workspace (contract verbatim)
python3 scripts/af-orchestrate.py <id> --workers 8 --max-rounds 12   # background; NEVER judge
python3 scripts/af-orchestrate.py <id> --phase verify --max-rounds 12 --node-cap 40  # RESUME a tree
fr verify proofs/<id>/export.md --oracle af-<id>  # bank gate (oracle in portfolio.json config)
cd runs/<bundle>/scripts && python3 <script>      # re-run any numerical certificate
```

## What is intentionally NOT here

- Any claim that more than THREE results are rigorous (everything else: honest lower rungs).
- σ̃-statements at ε=0 (refuted — halo-robust σ̃_g only), or the cap via exposedness absorption (B4).
- The linear law quoted as "δ ≥ H/2, zero exceptions" (H/δ=100/49 certified; asymptotic constant 2 stands).
- A git remote / remote CI (local-only by decision). `cited` defs with pinned refs/ sources (deferred).
