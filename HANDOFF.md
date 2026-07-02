<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md` (scope + the north-star theorem + reduction chain), then `CLAUDE.md` (== `AGENTS.md`, how
   to work — esp. the L0 rigour ladder and Rule 13 dead routes).
2. Run `fr board` (the live portfolio + FRONTIER) and `bd ready` (available work).
3. Skim `argument/DAG.md` (first green node is live) and `argument/INDEX.md`; read `FINDINGS.md` before
   touching anything flagged or a dead route; read `docs/ingest/README.md` for the honest re-tag map of the
   inherited work.
4. Gate before committing: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-02, session 2) — first rigorous result BANKED

- **`lem-classical-equiv` is af-VALIDATED IN-REPO** (commit `e68d1b6`) — the signed↔stochastic bridge, the
  repo's first genuinely rigorous result (L0 rung b). 29-node adversarial tree, root `validated`, taint
  29/29 clean; fresh codex prover/verifiers per node, Claude orchestrated only. Ledger + human-readable
  `export.md` in `proofs/lem-classical-equiv/`. Banked: claim-specific oracle `af-lem-classical-equiv`
  registered, `fr verify … export.md` → PASS, `fr log R banked` (tier T0). Its 3 registry dependents
  (`thm-rank-one`, `thm-simplex`, `prop-approx-simplex`) now have their dep available (blocked 9→6).
  KNOWN WARN (accepted for now): 29 nodes > 12 trips the linker brittleness signal every gate run —
  factoring decision filed as `aism-6ec` (P3).
- **`bd ready` == the proof frontier.** `argument.py --sync-beads` is implemented (idempotent mirror:
  issue-per-result, `blocks` edges = DAG deps, available results auto-closed) and reviewer-hardened
  (`--limit 0`, `--type blocks`; commits `17c9293`, `a2d78ce`). The op-classical chain is fully wired:
  `deps: thm-classical-factorization; prop-approx-simplex` — ONE COMPOSED route, AND not OR (commit
  `c2d828f`, ingest-cited in the shard body); the north star closes over all 8 ancestors down to
  `conj-kernel`.
- **`fr` campaign live**: arms A–F seeded + new support arm **R** (re-establish the inherited chain via af).
  First ▣ banked on R; standing decision: **EXPLORE B** next. All of A–F still untried.
- **Roles (user-mandated 2026-07-02):** the orchestrator keeps the knowledge/strategy overview and
  evaluates proof DIRECTIONS but NEVER verifies proofs (codex/af does); no Fable subagents without
  explicit user permission — prefer codex / opus / sonnet workers.
- **Git:** local-only, clean at `e68d1b6`+. **beads:** 17 DAG mirrors + work issues; `aism-rha`/`aism-22r`
  closed this session.

## The frontier (re-scoped 2026-07-02 by arm B waves 1-2 + arm F wave 1)

Still the Kernel / (EX) conjecture — but three waves sharpened WHERE it lives:
- **v-local and web-rigidity proof families are CLOSED** (obs-deep-leakage: exactness pushes the hidden
  vertex's mass into the shallow band, O(δ)/H cap on deep-side mass; obs-fwr-gap: F-WR is a
  coincidence-or-antipodality dichotomy, cannot count classes). Both heuristic-tagged, artifact-backed
  (`docs/waves/2026-07-02-B{1,2}-*.md`).
- **The collapse bound is af-VALIDATED** (`obs-height-collapse`, 19/19 clean): `H(1−σ̃) ≤ ν(2+4δ)`.
  Waves B3 + F2 then sharpened the finisher question two ways: (i) **B3's one-sided ledger** — the
  σ̃-cap asks for a lower bound on the exact quantity the collapse caps from above; its only lower-bound
  route is the anti-splitting wall; the cap may be strictly stronger than the kernel. (ii) **F2's
  refuter sweep** — the ε=0 cap is EXACTLY FALSE (self-mass certificate `σ̃=5343/5000>1`,
  `obs-sigma-halo-nonrobust`; never state the cap at ε=0), but the **halo-robust cap survives with
  margin** (`σ̃_g ≤ 0.37τ` over ~25k; killing it ⟺ entering the dangerous regime). **Current finisher
  plan: af-validate `conj-halo-collapse` (the self-mass-immune bridge, orchestration RUNNING) + establish
  the halo-robust cap via `conj-no-free-frontier` (exposedness absorption) — after first checking that
  mechanism dodges the one-sided-ledger/anti-splitting walls.**
- **Constants pinned + a certified correction**: existential C₀=1 tight (5/4 = selector floor);
  `H/δ = 100/49 > 2` at finite δ (hull-dip, `runs/2026-07-02-web-regime-hunt/`, kernel-safe, asymptotic
  constant still 2) — do NOT quote "δ ≥ H/2, zero exceptions" (FINDINGS 2026-07-02 correction).
- Contract-precision flag: `aism-136` (lem-dual-localization's stated inequality may be trivially true —
  proposed restatement goes to the user, not edited unilaterally).

## Strategy assessment (2026-07-02, orchestrator)

- **Arm B first** (standing `fr` decision): `lem-dual-localization` is a SINGLE well-isolated inequality
  (`‖Ē‖₁ ≥ H` from `P²=P`, skinny μ→1 regime). Recorded deaths say the proof must NOT be convexity-based
  (pure convex shadow composition is vacuous as μ→1) — the mechanism must come from the idempotence
  algebra. Yields the LINEAR law, strictly stronger than the H² envelope HLC needs.
- **Arm F early and cheap, redesigned**: the record's biggest evidential hole — below corner scale
  δ≈0.233 the dangerous antecedent (hidden vertex with σ̃_v>√δ) has NEVER been entered. Construct
  instances that force the antecedent; also resolves the C₀ tension (`aism-8bi`).
- **Arm A after F pins C₀** (don't prove toward a false constant); any chart invariant must be
  CLONE-INVARIANT (Rule 13); the selector graveyard is long — a new structural idea is required.
- **C, D are feeders** (to B and A respectively); **E stays a literature probe** (generic Hoffman/
  Łojasiewicz constants are n-dependent; op-classical needs n-free).

## Next steps (ranked) — RESUME HERE

1. **Open Arm B** with a real `fr` wave (opus/sonnet subagents; log with `fr log B …`): target the
   frame-free `δ ≥ H/2` (or `H ≤ C·δ`) in the skinny regime. Brief the wave with: DELIVERABLE2/3 +
   `kernel-conjecture*.tex` loci, the frame-specific proof (`dist₁(λ,Δ)=2·neg(λ)`), and the
   no-convexity death certificates.
2. **Pin the two constants** (`aism-8bi`, `aism-z48`) from the ingest docs — cheap reads, high strategy
   value; correct FRONTIER/HANDOFF text if confirmed.
3. **Re-home the 67k record** as `runs/<date>-ex-enumeration/` (`aism-4el`, L3 discipline) — and design
   the Arm-F antecedent-forcing probe on top of it.
4. **Next af elevations** (arm R): `thm-rank-one` / `thm-simplex` / `prop-approx-simplex` now have their
   dep validated; same protocol (`seed-af-workspaces.py <id>` → `af-orchestrate.py <id>` in background;
   provision missing defs YOURSELF on the shard's `defs:` line if the classification says MISSING fact —
   see `a2d78ce` for the pattern). Register a claim-specific oracle per banked result.
5. **Report shards** as rigorous results land (`AISM-NN` headers, `PROVENANCE.md` row, catalog sync) —
   the 17 "maps to NO report label" provenance warnings become real work once shard 1 exists.

## Recipes / commands

```bash
sh scripts/check-all.sh                          # the gate
python3 scripts/argument.py                       # linker: check + regen + ready/blocked frontier
python3 scripts/argument.py --sync-beads          # idempotent DAG→beads mirror (implemented this session)
python3 scripts/argument.py --show <id>           # one result's neighbourhood
fr board ; fr status                              # the portfolio
python3 scripts/seed-af-workspaces.py <id>        # seed one af workspace from a registry contract
python3 scripts/af-orchestrate.py <id> --workers 8 --max-rounds 8    # background; NEVER judge
python3 scripts/af-orchestrate.py <id> --phase verify --max-rounds 16  # RESUME an existing tree (no rebuild)
fr verify proofs/<id>/export.md --oracle af-<id>  # bank gate (register oracle in portfolio.json first)
```

## What is intentionally NOT here

- Any claim that more than ONE result is rigorous (only `lem-classical-equiv`; everything else is
  `proved-mod-audit`/`conjecture`/`numerical`/`open`).
- The general positive-maps / Jordan (JB) Layer-1 structure theorem (stays in
  `../almost-idempotent-positive-maps`).
- A git remote / remote CI (local-only by decision).
- `cited` definitions whose `refs/` source isn't pinned (deferred; seed defs are `consensus`/`original`).
- Resolution of the C₀ (1 vs ≥5/4) and H/δ (2+1.3e-11) tensions — flagged, filed, NOT yet pinned.
