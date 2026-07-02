<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md` — esp. L0 rigour ladder, Rule 13 dead routes).
2. Run `fr board` and `bd ready`. Skim `argument/DAG.md` (**7 green nodes**) + `FINDINGS.md` (the
   2026-07-03 arm-A roll-up + the 2026-07-02 entries) + `report/main.pdf` (9 shards, all 29 results
   anchored).
3. Wave artifacts in `docs/waves/` (B1–B4, F1–F2, **A1–A7 new**); L3 bundles in `runs/` (6, gate-green).
4. Gate before committing: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-03, session 4 close) — SEVEN rigorous results; arm A is the live program

**Rigorous (af-validated in-repo, banked via fr verify, T0):**

1. `lem-classical-equiv` — signed↔stochastic bridge (29 nodes).
2. `obs-height-collapse` — ε=0 collapse bound (19 nodes).
3. `lem-mass-split` — `Σ a_j⁺ = 1+ν_v` (9 nodes).
4. `lem-residual-lower` — frame-free convex outsourcing (32 live).
5. `lem-residual-upper` — frame-free residual bound (49 live).
6. `conj-halo-collapse` — the halo-robust height-collapse BRIDGE (20 nodes).
7. **`lem-factorization` — the (EX) composition link `S*_s ≤ 2Φ_s + 6δ` (11 live nodes, run 1 clean,
   5 rounds; contract narrowed to the single inequality first; tightness (2,6) NOT elevated).**

**Two live chains to `op-classical`:**
- **A-side (this session's program):** (EX) `max_s Φ_s(U₀) ≤ C₀δ` (OPEN, conjecture) ⇒ [rigorous
  `lem-factorization`] ⇒ `C_sf = 2C₀+6` ⇒ … `op-classical`.
- **B-side (unchanged):** halo-robust cap `σ̃_g ≤ 1−c` (OPEN, wall-blocked mechanisms) ⇒ [rigorous
  bridge `conj-halo-collapse`] ⇒ `H=O(τ)` ⇒ Kernel ⇒ … `op-classical`.

## Session-4 arm-A campaign (7 codex waves, A1–A7 in docs/waves/)

- **A1 scoping:** existential (EX) suffices downstream (no selector needed; w42 audit — no quantifier
  slip); walls-check: aggregate proofs dodge the B-walls, per-class proofs re-import class-count.
  **"C₀=1 empirically" is rank-3-only** (FINDINGS).
- **A2+A3+A6+A7 certified adversarial program (4 L3 bundles, headlines orchestrator-recomputed):**
  min-max `Φ/δ` PLATEAUS below 2 across 7 independent design families (path `2−2/(k−2)` k≤30;
  5 decoupled couplings; staircase rescales; repeated anchors; 5 coupled designs to rank 121 —
  coupling *reduces* the ratio). **Cheap-adversary program CLOSED; plateau-2 argmin lemma unbroken.**
- **A4+A5 proof scoping (mechanism kills, exact certificates):** beta-LP-only dead (two-atom witness);
  naive chart averaging dead (uniform/vol²/DPP — sigma-cap-B certificate); unnormalized `Σ_s Φ_s`
  dead (repeated-anchor witness, A6). Survivors: argmin interface; Schur-swap comparison;
  max-based probabilistic interface; `V_s ≤ Φ_s/2` (elementary).
- **The δ=1/2 killers (B6, perturbed staircase) do NOT port under the cap** — the cap is
  load-bearing (A6 rescale tradeoff). Working constant `C₀ ≈ 2` ⇒ `C_sf = 10`.

## The frontier (2026-07-03 close)

**Arm A's sole open input: the max-based argmin charge** — GAP A/GAP B in
`docs/waves/2026-07-02-A4-aggregate-charge.md`: prove `max_s Φ_s(U*) ≤ Cδ` at a θ-½ Φ-argmin, either
via Schur-swap stationarity + a near-degeneracy payment (the source's named open horn,
kernel-conjecture-v2.tex ~448–454) or a genuinely new aggregate/max-based mechanism. Do NOT
af-elevate GAP A as-is (it is (EX) restated — genuine-gap abort predicted).

**B-side unchanged:** the halo-robust cap needs a NEW ledger-immune, class-count-free mechanism, or
the B4 deciders (FAIL-1 exact instance hunt = arm F work; signed quantitative Baake–Sumner count).

## Next steps (ranked) — RESUME HERE

1. **Arm A wave 8 (theory):** sharpen GAP B — an explicit Schur-block degeneracy functional with the
   payment inequality, exact-tested on the A2–A7 instance zoo (A4 §4 rec 2). Kill criteria as before
   (per-class counting; dead selectors).
2. **Alternative:** arm F FAIL-1 decider hunt (exact instance refuting `conj-no-free-frontier` at
   uniform κ=τ/4) — sharpens any future B-side cap mechanism; independent of arm A.
3. **USER DECISION still pending (aism-136, `bd human`):** `lem-dual-localization` contract is
   trivially true as stated (codex-verified); candidate corrected contracts in the bd notes.
4. Hygiene: aism-6ec (accept-and-defer recommendation recorded on the REFACTOR WARNs); refs/ pinning
   for `cited` defs (deferred); consider a def-actual-row-chart / def-phi-excess definitions pass if
   arm A keeps producing chart-language registry results (contracts currently self-contained).

## Standing role/process rules (user-mandated 2026-07-02/03)

- Orchestrator = strategy/overview; NEVER verifies proofs (codex/af does). No Fable subagents —
  prefer codex workers. ONE af orchestration at a time; codex scouting waves serial-ish.
- af contracts: SINGLE minimal statement (bd memory; lem-factorization narrowing worked first-run).
- No argument/definitions edits while ANY orchestration is live (git-porcelain overreach guard).
- Numerics: exact-ℚ, L3 bundles, orchestrator independently recomputes one headline per bundle
  (done for A2/A3/A6: 7/4, 23/16, and the 512-chart repeated-star row).
- Waves: verbatim harvest artifact in `docs/waves/`, honest tiering (T0–T3), fr log per pull;
  workers told: no fr/bd, no registry/report edits.

## Recipes / commands

```bash
sh scripts/check-all.sh                          # the gate
fr board ; fr status                              # the portfolio
python3 scripts/seed-af-workspaces.py <id>        # seed one af workspace (contract verbatim)
python3 scripts/af-orchestrate.py <id> --workers 8 --max-rounds 12 --node-cap 40   # background
fr verify proofs/<id>/export.md --oracle af-<id>  # bank gate (7 oracles registered)
python3 scripts/argument.py --sync-beads          # idempotent DAG→beads mirror
```

## What is intentionally NOT here

- Any claim that more than SEVEN results are rigorous (everything else: honest lower rungs).
- Any claim (EX) / the Kernel Conjecture / op-classical is closed — BOTH chain inputs are OPEN.
- Plateau-2 as a theorem (it is L3 evidence + an unbroken candidate lemma, across 7 design families).
- The tightness of (2,6) in lem-factorization as rigorous (deliberately not elevated; body note).
- A git remote / remote CI (local-only by decision; bd hook confirms no remote — do not "push").
