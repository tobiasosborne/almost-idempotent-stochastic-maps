<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md` — esp. L0 rigour ladder, Rule 13 dead routes).
2. Run `fr board` and `bd ready`. Skim `argument/DAG.md` (**6 green nodes**) + `FINDINGS.md` (four dated
   2026-07-02 entries) + `report/main.pdf` (the lab-book now exists: 7 shards, all 29 results anchored).
3. Wave artifacts in `docs/waves/` (B1–B4, F1, F2); L3 bundles in `runs/` (3, gate-green).
4. Gate before committing: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-02, session 3 close) — SIX rigorous results; the finisher BRIDGE is rigorous

**Rigorous (af-validated in-repo, banked via fr verify, T0):**

1. `lem-classical-equiv` — signed↔stochastic bridge (29-node tree).
2. `obs-height-collapse` — ε=0 collapse bound `H(1−σ̃) ≤ ν(2+4δ)` (19 nodes).
3. `lem-mass-split` — `Σ a_j⁺ = 1+ν_v` (9 nodes).
4. `lem-residual-lower` — frame-free convex outsourcing `dist₁(p,C) ≤ dist₁(q,C)` (32 live nodes).
5. `lem-residual-upper` — frame-free residual bound `m·dist₁(q,C) ≤ Σb_j·dist₁(p_j,C)+Σc_k·D_k` (49).
6. **`conj-halo-collapse` — the halo-robust height-collapse BRIDGE
   `H(1−σ̃_g) ≤ (σ̃−σ̃_g)·τ/4 + ν_v(2+4δ)` (20-node tree, clean; run 2 on the factored workspace).**

**The chain now reads: cap (OPEN) ⇒ [bridge, RIGOROUS] ⇒ `H = O(√δ)` at hidden top vertices ⇒ Kernel
Conjecture ⇒ HLC ⇒ op-exposed-hull ⇒ op-classical.** One input missing: the halo-robust cap
`σ̃_g ≤ 1−c`.

- Registry: 29 results; lab-book: 7 report shards, provenance 0 errors/0 warnings; `bd` mirror synced.
- Process wins recorded: the balloon/factoring discipline WORKS (run 1: 49>40 abort → factor →
  run 2: 20 nodes clean). Two bd memories: single-minimal contracts; no argument/definitions edits
  while any orchestration is live (git-porcelain overreach guard).
- Known WARNs (accepted, tracked aism-6ec): five >12-node REFACTOR warnings on validated trees.

## The frontier (2026-07-02 close)

**THE open question: the halo-robust cap `σ̃_g ≤ 1−c` for hidden top vertices (0<δ≤¼, W≠∅).**

- Mechanism `conj-no-free-frontier` is **wall-blocked — DO NOT ELEVATE** (B4: dodges the one-sided
  ledger but re-imports the dimension-free class count = dead route c10/c20; plus FAIL-1: uniform
  κ=τ/4 plausibly false as written). Artifact `docs/waves/2026-07-02-B4-walls-check.md` §6 records
  two deciders: (i) FAIL-1 exact-instance hunt (arm F work); (ii) the class-count question (open
  signed quantitative Baake–Sumner — dead-route territory without a new idea).
- Arm B is 4×✗ (stalled). **Arm A ((EX) chart bound) is the untried PRIMARY** and composes to
  `C_sf = 8` without needing the cap — the natural next EXPLORE (issue aism-vip).
- Empirics: cap holds with margin (`σ̃_g ≤ 0.37τ` over ~25k, F2) — low-dimension evidence, silent on
  the class-count wall.

## Next steps (ranked) — RESUME HERE

1. **aism-vip: EXPLORE arm A** — first scoping wave on the (EX) chart bound
   `max_s Φ_s(U₀) ≤ C₀·δ` (codex worker; read the dead routes FIRST: 12.8–128× blowup,
   exists-exact-max-volume selectors). Deliverable: attack plan or reduction.
2. Alternative/parallel: **arm F hunt for the B4 FAIL-1 decider** — an exact instance with an
   extremal row failing (ρ,κ)-exposedness at uniform κ=τ/4 (refutes `conj-no-free-frontier` as
   written; sharpens what any future cap mechanism must assume).
3. **USER DECISION pending (aism-136, `bd human`):** `lem-dual-localization` contract is trivially
   true as stated (codex-verified). Candidate corrected contracts in the bd notes.
4. Hygiene queue: `aism-6ec` (REFACTOR-warning policy for big validated trees); refs/ pinning for
   `cited` defs (deferred); report shard for the bridge proof narrative (the ledger row exists;
   a full section like the other five would be natural next lab-book work).

## Standing role/process rules (user-mandated 2026-07-02)

- Orchestrator = knowledge/strategy overview + proof-direction evaluation; NEVER verifies proofs
  (codex/af does). No Fable subagents without explicit permission — **prefer codex** workers.
- af contracts: SINGLE minimal statement (bd memory). Balloon abort → FACTOR, re-seed, re-run —
  proven effective this session.
- No argument/definitions edits while ANY orchestration is live (bd memory; guard is git-porcelain).
- Numerics: exact-ℚ certificates, L3 bundles, orchestrator independently recomputes headlines.
- Waves: verbatim harvest artifact in `docs/waves/`, honest-status codification, fr log per pull.

## Recipes / commands

```bash
sh scripts/check-all.sh                          # the gate
fr board ; fr status                              # the portfolio
python3 scripts/seed-af-workspaces.py <id>        # seed one af workspace (contract verbatim)
python3 scripts/af-orchestrate.py <id> --workers 8 --max-rounds 12 --node-cap 40   # background
python3 scripts/af-orchestrate.py <id> --phase verify --max-rounds 16 --node-cap 40 # RESUME a tree
fr verify proofs/<id>/export.md --oracle af-<id>  # bank gate (6 oracles registered)
python3 scripts/argument.py --sync-beads          # idempotent DAG→beads mirror
```

## What is intentionally NOT here

- Any claim that more than SIX results are rigorous (everything else: honest lower rungs).
- Any claim the Kernel Conjecture / (EX) / op-classical is closed — the CAP IS OPEN.
- σ̃-statements at ε=0 (refuted); the cap via exposedness absorption (B4, wall-blocked).
- The linear law as "δ ≥ H/2, zero exceptions" (H/δ=100/49 certified; asymptotic constant 2 stands).
- A git remote / remote CI (local-only by decision).
