<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md` — esp. L0 rigour ladder, Rule 13 dead routes).
2. Run `fr board` and `bd ready`. Skim `argument/DAG.md` (2 green nodes now) + `FINDINGS.md` (three new
   dated entries from 2026-07-02 — constants pinned, linear-law correction, halo non-robustness).
3. The wave artifacts live in `docs/waves/` (B1, B2, B3, F1, F2 — verbatim harvests with orchestrator
   verification notes); the L3 bundles in `runs/` (2 bundles, both gate-green).
4. Gate before committing: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-02, session 2 close) — TWO rigorous results; finisher route staged

- **Rigorous (af-validated in-repo, banked via fr verify, T0):**
  1. `lem-classical-equiv` — the signed↔stochastic bridge (29-node tree, clean).
  2. `obs-height-collapse` — the collapse bound `H(1−σ̃) ≤ ν(2+4δ)` (19-node tree, clean) — the first
     NEW (non-inherited) rigorous result.
- **Registry: 26 nodes** (9 defs; statuses honest: 2 proved/validated, inherited proved-mod-audit,
  wave-derived heuristic/numerical/conjecture). Mirror: `bd ready` == frontier (sync-beads implemented,
  reviewer-hardened). Two L3 run bundles. `fr`: arms A–F + R; 8 pulls logged (R:▣▣✗ B:✗✗✗ F:△△).
- **Codex quota: ~exhausted; refreshes 16:00 today. NO codex/af dispatches before then.**
- **Known WARNs (accepted, tracked):** two validated trees >12 nodes trip the brittleness gate every
  run (aism-6ec; AF-FEEDBACK item 10); 26 "maps to NO report label" provenance warnings (report shards
  don't exist yet — step 5 below).

## The frontier (after 5 waves + 2 elevations, 2026-07-02)

The reduction chain now runs: **`conj-no-free-frontier` ⇒ halo-robust σ̃-cap ⇒ (via `conj-halo-collapse`)
`H = O(√δ)` ⇒ Kernel Conjecture ⇒ HLC ⇒ op-exposed-hull ⇒ op-classical.** Status of each new link:

- `obs-height-collapse` **RIGOROUS** — but its ε=0 σ̃ is self-mass-vulnerable (`obs-sigma-halo-nonrobust`:
  exact instance with σ̃=5343/5000>1, pure halo; NEVER state σ̃-statements at ε=0).
- `conj-halo-collapse` (the self-mass-immune bridge, exact on 3 certified instances) — elevation run 1
  BALLOONED (49>40, structural not mathematical); **factor + re-seed + re-run = aism-q7e** (quota-gated).
- Halo-robust cap `σ̃_g ≤ 1−c`: survives F2's kill attempt with margin (σ̃_g ≤ 0.37τ over ~25k; killing
  it ⟺ entering the never-entered dangerous regime). Mechanism candidate `conj-no-free-frontier`
  (exposedness absorption) — **must pass the walls-check first = aism-5yk** (B3's one-sided ledger
  blocks coefficient-mass lower bounds at v; anti-splitting blocks class-counting; the mechanism is a
  different species but this is unverified).
- Closed families (do not re-walk; artifact-backed): v-local (`obs-deep-leakage`), web-rigidity
  (`obs-fwr-gap`), ε=0 cap (`obs-sigma-halo-nonrobust`), plus all inherited dead routes.

## Next steps (ranked) — RESUME HERE

1. **After 16:00: execute aism-q7e** — factor `conj-halo-collapse` into 2–3 minimal sub-lemma shards
   (lem-mass-split bookkeeping; lem-residual-distance estimates), re-seed, re-orchestrate
   (`--workers 8 --max-rounds 12`; each contract = ONE statement, per the banked lesson).
2. **Walls-check wave (aism-5yk, opus, no codex needed)** — can run before 16:00: does
   `conj-no-free-frontier` dodge the one-sided-ledger + anti-splitting obstructions? Attack plan or
   death certificate.
3. `aism-136`: verify wave-1's claim that `lem-dual-localization`'s contract is trivially true as
   stated; propose a corrected contract TO THE USER (do not edit unilaterally).
4. `aism-4el`: re-home the inherited 67k record as a runs/ bundle. `aism-6ec`: factoring decision for
   the two >12-node validated trees.
5. Report shards (`AISM-NN`) for the two rigorous results + PROVENANCE rows — clears the 26 anchor
   warnings and starts the lab-book.
6. Tooling: hand `docs/tooling-feedback/{FR,AF}-FEEDBACK.md` to the fr/af maintainer agents (af item 1
   already fixed in af 0.1.4 per the updated file).

## Standing role/process rules (user-mandated 2026-07-02)

- Orchestrator = knowledge/strategy overview + proof-direction evaluation; NEVER verifies proofs
  (codex/af does). No Fable subagents without explicit permission — codex / opus / sonnet only.
- af contracts: SINGLE minimal statement (bd memory `af-elevation-contracts-must-be-a-single-minimal`).
- Numerics: exact-ℚ certificates, L3 bundles, orchestrator independently recomputes headline claims.
- Waves: verbatim harvest artifact in `docs/waves/`, honest-status codification, fr log per pull.

## Recipes / commands

```bash
sh scripts/check-all.sh                          # the gate
python3 scripts/argument.py --sync-beads          # idempotent DAG→beads mirror
fr board ; fr status                              # the portfolio
python3 scripts/seed-af-workspaces.py <id>        # seed one af workspace (contract verbatim)
python3 scripts/af-orchestrate.py <id> --workers 8 --max-rounds 12   # background; NEVER judge
python3 scripts/af-orchestrate.py <id> --phase verify --max-rounds 16  # RESUME existing tree
fr verify proofs/<id>/export.md --oracle af-<id>  # bank gate (register oracle in portfolio.json)
cd runs/<bundle>/scripts && python3 <script>      # re-run any numerical certificate
```

## What is intentionally NOT here

- Any claim that more than TWO results are rigorous (everything else: honest lower rungs).
- σ̃-statements at ε=0 (refuted — halo-robust σ̃_g only).
- The linear law quoted as "δ ≥ H/2, zero exceptions" (finite-δ exceedance H/δ=100/49 certified;
  asymptotic constant 2 stands).
- A git remote / remote CI (local-only by decision). `cited` defs with pinned refs/ sources (deferred).
- Codex dispatches before 16:00 (quota).
