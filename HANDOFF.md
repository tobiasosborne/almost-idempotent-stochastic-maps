<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md` (Kernel is THE theorem-facing input; (EX) is a separate attack route), then
   `CLAUDE.md` (== `AGENTS.md`).
2. Read **`docs/plans/2026-07-06-top-down-proof-sketch-v4.md`** — THE canonical strategic map
   (v4, session-10 surgical delta of v3; v3/v2 superseded in place, kept for line citations).
   Every wave names its node there. The OPEN LEDGER + UNSCOPED-SURFACE list at its end IS the
   progress metric. **STEWARDSHIP (user mandate, 2026-07-06, binding): the sketch is the
   project's most dynamic artifact — keeping it reconciled with newly banked evidence is a
   FIRST-CLASS DELIVERABLE of every session; a wave that changes the map without updating the
   sketch is incomplete work (Rule 9).**
3. **THE PHASE DISCIPLINE (user, 2026-07-05, binding): no progress theatre.** Progress =
   unscoped/unpriced surface shrinking — never commit/seeding/elevation counts. (bd memory
   `bfs-phase-discipline`; agent memory `no-progress-theatre`.)
4. Run `fr board` and `bd ready`. Newest wave artifacts: `docs/waves/2026-07-06-W20-*`,
   `2026-07-06-W21-*`; newest bundles: `runs/2026-07-06-w20-g-zoo-measurement/`,
   `runs/2026-07-06-w21-lemma-a-decider/`. `FINDINGS.md` has two new dated entries (07-06
   W20/W21). Wave prompts + raw worker answers: session-10 scratchpad (`W20/`, `W21/`).
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-06, session 10 CLOSE) — the g-bootstrap survived its deciders; REGISTRY +1

**Rigorous (af-validated, T0): 16** (`argument/INDEX.md`) — unchanged. **Registry delta: +1
REVIEWED (not af): `lem-visible-g-small`** — LEMMA A, the g-bootstrap's load-bearing step 2,
`status: proved`, `af: none`; it is now the linker's ready frontier (af-elevation proposal
`aism-88r`, user opt-in required).

**Session 10 in one paragraph.** Two waves on the user-directed target (the g-bootstrap =
sketch M1, the kernel-conjecture strategy of record), five fresh codex workers in two
mutually-blind adversarial pairs + one separate adversarial verifier. **W21 (Lemma A
prove-or-refute, aism-0b1):** PROVED at exact constants — for every visible row `w` and halo
width `a ≥ 4`, `−ν_w ≤ g_w ≤ 4τ` (exposer-pairing against row reproduction; `a ≥ 4` used
exactly once); the SEPARATE fresh verifier returned VALID on all 7 hostile checklist items
(incl. a 20k-instance exact sanity sweep); the mutually-blind refuter converged NOT-REFUTED
and independently derived the prover's key inclusion from the opposite mandate — its output
is a new frontier certificate: visible-row `g = √(147/569)·τ ≈ 0.508τ` at `a = 1/4`
(harmless to the lemma; largest certified visible g/τ to date). **W20 (zoo g-measurement,
aism-vmt):** LEMMA-A-SUPPORTED / NO-KILL-FRONTIER — full exact sweep (307 unique certified
matrices, 1842 (matrix,a) cases, 1842 harmonicity + 9564 sandwich checks, 4 banked
calibrations) plus an adversarial constructor; both pre-registered kills UNREALIZED; the
structural headline is that **`G_a` is EMPTY zoo-wide for every `a ≥ 1`** — no known
construction realizes depth > 1τ, so the step-4 kill zone is unreachable and zoo measurement
is RETIRED as a step-4 decider (sketch v4 RETIRED #8). Binding constraint everywhere:
exposedness absorption (third independent confirmation). **The new named front is THE A-GAP
`(29τ/8, 4τ]`** (aism-sg6): Lemma A needs `a ≥ 4`; MIN-A's tall antecedent guarantees depth
only `> 3.625τ`. Orchestrator recomputed the load-bearing algebra of every headline from the
printed matrices alone (8/8 + 11/11 checks, both scripts banked in the bundles); all worker
scripts rerun exit 0. **Trunk staleness rule VIOLATED this session** (user-directed focus);
debt explicit in sketch v4 — trunk item FIRST next session.

## Next steps (ranked) — RESUME HERE

0. **Trunk debt (staleness rule, sketch v4):** promote ONE trunk item into the next wave mix —
   `<2>5` transcription+audit (`aism-pu0`) is the cheapest. Non-negotiable per the standing
   rule; three sessions stale.
1. **`aism-sg6` — THE A-GAP `(29τ/8, 4τ]`** (sketch v4 M1 step 2): design wave pricing the
   three closure routes — (i) collapse-constant improvement, (ii) a small-`a` Lemma-A
   mechanism (the ρ-far inclusion fails below 4 — needs a genuinely new idea), (iii) deep-mass
   routing via step 3/4. Adversarial pair on (i) vs (ii) is the natural shape.
2. **g-bootstrap step 3 (disintegration)** — expected-short T1 derivation, still underived
   (sketch v4 M1 step 3): genuine mass lands on hidden vertices in the depth band via
   lem-residual-upper [validated] + exposed-vertices-are-in-W. Cheap; pairs well with 1.
3. **`aism-tq3` — obs-deep-leakage re-establishment/elevation.** Blocking dep of step 4's deep
   side AND a-gap route (iii); status HEURISTIC while every Route-A depth-ledger step consumes
   it.
4. **`aism-88r` — af-elevate `lem-visible-g-small` (USER DECISION).** It is the linker's ready
   frontier; single-minimal contract, deps: none, 5-step proof — a small tree. Opt-in per
   Rule 6; do not start without the go-ahead.
5. **`aism-pld` (P1) — poke-charge codification + distinct-multi-class σ_g optimization** (M2
   fallback + the only step-4 stress left with teeth — but note: to matter for step 4 its
   constructions must first realize depth > 1τ, which nothing banked does).
6. Standing queue: `aism-yxa` (D1 codification + review); `aism-j3j` (E2 survivors); α→1
   continuation (Route B's kill/rescue gate); arm E wave 3 (`aism-5an`); refs ingest
   (`aism-5de`, `aism-1nh`); `aism-z98` USER DECISION; report sections 14–15 (`aism-av0`).

## Standing rules (see CLAUDE.md + bd memories; session-10 additions in bold)

Codex workers only (no Fable subagents); ONE af orchestration at a time; single-minimal af
contracts; no argument//definitions edits while an orchestration runs; numerics = exact-ℚ with
orchestrator recomputation; waves = verbatim docs/waves/ artifacts, honest tiers, fr log per
pull, workers told no fr/bd; wave prompts/answers in the session scratchpad; independent codex
review before codifying worker proofs; literature enters as `stated` until byte-matched.
Session-9 additions all held (mutually-blind adversarial pairs; orchestrator recomputes
printed-matrix arithmetic; name missing charges; LP-vs-exact-geometry as binding-constraint
identifier; explicit self-mass conventions; orchestrator hypotheses marked as
hypotheses-to-refute). **Session-10 additions: (i) the prove/refute/verify TRIPLE (blind
prover + blind refuter + separate hostile verifier on the prover's text) is the house shape
for codifying a new lemma in one wave — W21 ran it end-to-end for one wave's cost; (ii) a
`status: proved, af: none` registry shard must carry its reviewer provenance in the shard
frontmatter AND the commit `Review:` line; (iii) measurement waves must report which zoo
members were skipped and why (W20's 216-entry skip table) — silent subsampling is banned;
(iv) when a decider's battleground is empirically unreachable (G_a empty zoo-wide), RETIRE
the measurement channel in the sketch rather than re-running it bigger.**

## Recipes

```bash
sh scripts/check-all.sh
python3 scripts/seed-af-workspaces.py <id>       # then COMMIT before orchestrating
python3 scripts/af-orchestrate.py <id> --workers 8 --max-rounds 14 --node-cap 40   # background
codex exec --skip-git-repo-check -C <repo> -s workspace-write -o <answer> - < <prompt>
python3 runs/2026-07-06-w20-g-zoo-measurement/scripts/w20_worker_a.py              # W20 sweep rerun
python3 runs/2026-07-06-w20-g-zoo-measurement/scripts/orchestrator_recompute.py    # W20 orch check
python3 runs/2026-07-06-w21-lemma-a-decider/scripts/w21_worker_d.py                # W21 refuter rerun
python3 runs/2026-07-06-w21-lemma-a-decider/scripts/orchestrator_recompute.py      # W21 orch check
# session-10 wave pattern (works): falsifiable target -> TWO mutually-blind adversarial codex
#   workers (+ for a new lemma: a SEPARATE hostile verifier on the prover's text) -> orchestrator
#   recomputes printed-matrix arithmetic + reruns scripts -> bank verbatim wave doc (+ L3 bundle)
#   -> FINDINGS/sketch in lockstep -> fr log one pull per wave -> registry/bd follow-ups.
```

## What is intentionally NOT here

- Any claim more than SIXTEEN results are af-validated (~6 substantive). `lem-visible-g-small`
  is REVIEWED (`proved`/`af: none`) — L5 satisfied, L0 "rigorous" NOT claimed.
- Any claim the a ≥ 4 restriction of Lemma A is removable — the ρ-far inclusion genuinely
  fails below 4; the a-gap is OPEN (aism-sg6).
- Any claim the step-4 band-web residual moved: it is analytically untouched; W20 only showed
  the empirical channel is dead (G_a empty zoo-wide ≠ emptiness theorem).
- Any claim CAP-1/2 or MIN-A is decided: the visible-row frontier is 0.508τ at a = 1/4 and
  0.075 in σ_g — evidence with margin, three-times-stamped not-an-emptiness.
- A git remote (local-only by decision) — session close = commits + bd close-out, no push.
