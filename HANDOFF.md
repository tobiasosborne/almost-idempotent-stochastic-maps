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
2. Read **`docs/plans/2026-07-06-top-down-proof-sketch-v5.md`** — THE canonical strategic map
   (v5, session-10 round-2 delta of v4; v4/v3/v2 superseded in place, kept for line citations).
   Every wave names its node there. The OPEN LEDGER + UNSCOPED-SURFACE list at its end IS the
   progress metric. **STEWARDSHIP (user mandate, 2026-07-06, binding): the sketch is the
   project's most dynamic artifact — keeping it reconciled with newly banked evidence is a
   FIRST-CLASS DELIVERABLE of every session; a wave that changes the map without updating the
   sketch is incomplete work (Rule 9).**
3. **THE PHASE DISCIPLINE (user, 2026-07-05, binding): no progress theatre.** Progress =
   unscoped/unpriced surface shrinking — never commit/seeding/elevation counts. (bd memory
   `bfs-phase-discipline`; agent memory `no-progress-theatre`.)
4. Run `fr board` and `bd ready`. Newest wave artifacts: `docs/waves/2026-07-06-W20-*` through
   `2026-07-06-W24-*`; newest bundles: `runs/2026-07-06-w20-g-zoo-measurement/`,
   `runs/2026-07-06-w21-lemma-a-decider/`, `runs/2026-07-06-w23-a-gap/`. `FINDINGS.md` has five
   new dated entries (07-06 W20/W21/W22/W23/W24). Wave prompts + raw worker answers:
   session-10 scratchpad (`W20/`–`W24/`).
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-06, session 10 round-2 CLOSE) — the g-bootstrap is ONE open step from MIN-A; trunk <2>5 paid; REGISTRY +5 (all reviewed or wiring)

**Rigorous (af-validated, T0): 16** — unchanged. **Registry deltas this session: +4 REVIEWED
lemmas + 1 open-problem node + 1 rewire** — `lem-visible-g-small` (W21), `lem-kernel-implies-hlc`
(W22), `lem-parametric-halo-collapse` (W23), `lem-genuine-disintegration` (W24), `op-hlc`
(registered + `op-exposed-hull` rewired through it). All four lemmas: `status: proved`,
`af: none` — L5 reviewer-gate satisfied (each by a SEPARATE fresh hostile codex verifier), L0
"rigorous" NOT claimed. The linker's ready frontier = the three g-bootstrap lemmas.

**Session 10 in one paragraph.** Eleven fresh codex workers across five waves, all on the
user-directed kernel-conjecture strategy (the g-bootstrap) plus the trunk debt. Round 1
(W20+W21): Lemma A proved (C = 4, a ≥ 4; `−ν_w ≤ g_w ≤ 4τ`), verified, refuter-converged; the
zoo measured (`G_a` empty zoo-wide for a ≥ 1 — zoo measurement retired as a step-4 decider);
THE A-GAP named. Round 2 (W22+W23+W24): trunk <2>5 (Kernel ⇒ HLC, C₁ = max{B,3}) re-derived
independent of the ingest and hostile-verified — staleness debt PAID, `op-hlc` wired;
**THE A-GAP CLOSED mod-review** — the parametric halo collapse `H(1−σ_a) ≤ (σ−σ_a)·aτ +
ν(2+4δ)` (validated contract = the a = 1/4 case, exact calibration) gives the forced-mass curve
**T(a) = 5a/2 + 3** and MIN-A at width 4: `H > 13τ` ⇒ every hidden top has `g^{(4)} > 1/2 − δ`,
against Lemma A's `4τ` visible cap, numerical gap iff `δ < (17−12√2)/2 ≈ 0.0147` (route (ii)
open-both-sides and moot; L3 bundle); step 3 (disintegration) proved + verified —
`g_i ≤ M_i^a + Σ P_ij⁺(H−d_j)/(H−aτ)` with `M_i^a` on hidden vertices at depth (aτ, H].
**Net: the g-bootstrap's remaining mathematical content is exactly ONE open step — step 4**,
posed precisely in sketch v5 (M1 block): for `δ < 0.0147`, `H > 13τ`, the P-harmonic `g^{(4)}`
has hidden tops > 1/2 − δ, visible rows ≤ 4τ, deep mass disintegrating onto hidden vertices —
derive the contradiction (once-applied max principle; anti-splitting, analytic form).
obs-deep-leakage DEMOTED from standing blocker to a step-4 design question (the width-4 surface
was derived without it). Orchestrator recomputed headline arithmetic throughout; all worker
scripts rerun exit 0; every prover was checked by a separate hostile verifier.

## Next steps (ranked) — RESUME HERE

0. **THE STEP-4 WAVE (the bootstrap finisher attempt).** Design per sketch v5 M1 step 4:
   prove-or-refute pair + hostile verifier on the once-applied maximum principle over the
   width-4 surface. The wave brief must (a) hand workers the three reviewed lemmas + the two
   af-validated collapse contracts as the ONLY imports, (b) pre-register kill criteria (a
   certified band-web sustaining g^{(4)} ≥ 1/2 under the constraints = a Kernel-counterexample
   hint), (c) decide explicitly whether obs-deep-leakage is consumed (if yes, aism-tq3
   re-blocks).
1. **Trunk <2>6 re-audit** (HLC ⇒ op-exposed-hull) — the staleness rule's next mandatory
   debtor; now one of only two unreviewed links behind a proved Kernel (with <2>7).
2. **`aism-88r` (USER DECISION) — af elevation of the reviewed quartet**, prioritizing
   `lem-parametric-halo-collapse` + `lem-genuine-disintegration` (their deps are ALL
   af-validated; single-minimal contracts; small trees expected). Opt-in per Rule 6.
3. **`aism-yxa` re-aimed** — codify the D1/cap⇒Kernel assembly targeting the parametric form
   (B = 13 at width 4; W-nonemptiness and δ=0 endpoint are the remaining assembly gaps).
4. **`aism-tq3`** — obs-deep-leakage: HOLD until the step-4 design decides whether it is
   consumed; if yes, it re-blocks and jumps the queue.
5. Standing queue: `aism-pld` (poke-charge + multi-class; gated on realizing depth > 1τ);
   `aism-j3j` (E2 survivors); α→1 continuation (Route B gate); arm E (`aism-5an`); refs ingest
   (`aism-5de`, `aism-1nh`); `aism-z98` USER DECISION; report sections 14–15 (`aism-av0` — note
   five new reviewed/registered shards now lack report labels, warn-level).

## Standing rules (see CLAUDE.md + bd memories; session-10 additions in bold)

Codex workers only (no Fable subagents); ONE af orchestration at a time; single-minimal af
contracts; no argument//definitions edits while an orchestration runs; numerics = exact-ℚ with
orchestrator recomputation; waves = verbatim docs/waves/ artifacts, honest tiers, fr log per
pull, workers told no fr/bd; wave prompts/answers in the session scratchpad; independent codex
review before codifying worker proofs; literature enters as `stated` until byte-matched.
**Session-10 additions: (i) the prove/refute/verify TRIPLE (blind prover + blind refuter +
separate hostile verifier) is the house shape for codifying a new lemma in one wave; for pure
derivations a prover + hostile verifier PAIR suffices (W22/W24); (ii) a `status: proved,
af: none` shard carries its reviewer provenance in frontmatter AND the commit `Review:` line;
(iii) measurement waves report skips explicitly; (iv) when a decider's battleground is
empirically unreachable, RETIRE the measurement channel in the sketch; (v) verifier briefs
should demand the verifier EXPAND compressed prover steps itself (W23-L reproved the
residual-split from scratch — that is what made the parametric collapse trustworthy); (vi)
calibration anchors in derivation waves (recover a known validated constant as a special case)
catch conventions drift — T(1/4) = 29/8 was the load-bearing check.**

## Recipes

```bash
sh scripts/check-all.sh
python3 scripts/seed-af-workspaces.py <id>       # then COMMIT before orchestrating
python3 scripts/af-orchestrate.py <id> --workers 8 --max-rounds 14 --node-cap 40   # background
codex exec --skip-git-repo-check -C <repo> -s workspace-write -o <answer> - < <prompt>
python3 runs/2026-07-06-w20-g-zoo-measurement/scripts/w20_worker_a.py              # W20 sweep rerun
python3 runs/2026-07-06-w21-lemma-a-decider/scripts/orchestrator_recompute.py      # W21 orch check
python3 runs/2026-07-06-w23-a-gap/scripts/w23_worker_i.py                          # W23 route-ii rerun
# session-10 wave pattern: falsifiable target -> blind adversarial workers (+ separate hostile
#   verifier on any claimed proof; verifier EXPANDS compressed steps + checks a known-constant
#   calibration) -> orchestrator recomputes printed arithmetic + reruns scripts -> bank verbatim
#   wave doc (+ L3 bundle) -> FINDINGS/sketch in lockstep -> fr log per wave -> registry/bd.
```

## What is intentionally NOT here

- Any claim more than SIXTEEN results are af-validated (~6 substantive). The four new lemmas
  are REVIEWED (`proved`/`af: none`) — L5 satisfied, L0 "rigorous" NOT claimed; op-hlc is OPEN.
- Any claim MIN-A or the Kernel Conjecture is proved: step 4 is OPEN; W-nonemptiness and the
  δ=0 endpoint are unassembled; and the whole chain above HLC (<2>6, <2>7) is mod-audit.
- Any claim the bootstrap works at δ ≥ (17−12√2)/2 — the width-4 numerical gap needs small δ₀;
  that is a universal-constant restriction, not a defect, but never elide it.
- Any claim about step 4's difficulty: the anti-splitting residual has killed every previous
  local/count-based approach (obs-deep-leakage, obs-fwr-gap walls); the width-4 surface is
  sharper but the mechanism is genuinely unknown.
- A git remote (local-only by decision) — session close = commits + bd close-out, no push.
