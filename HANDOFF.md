<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read **`docs/plans/2026-07-07-top-down-proof-sketch-v10.md`** — THE canonical strategic map
   (v10, session-11 round-7; v9 and earlier superseded in place, kept for line citations).
   **STEWARDSHIP (user mandate, 2026-07-06, binding): reconciling the sketch with newly banked
   evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. **PHASE DISCIPLINE (user, 2026-07-05, binding): no progress theatre** — progress =
   unscoped/unpriced surface shrinking.
4. Run `fr board` and `bd ready`. Session-11 wave artifacts: `docs/waves/2026-07-06-W26/27/28/30`
   + `2026-07-07-W29/31/32/33`; bundles `runs/2026-07-06-w26-hiddenness/`,
   `runs/2026-07-06-w29-witness-coupling/`, `runs/2026-07-06-w30-w-nonemptiness/`.
   Wave prompts + raw answers: session-11 scratchpad (`W26/`–`W34/`).
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-07, session 11 round-5 CHECKPOINT — VAG + af #4 IN FLIGHT)

**Rigorous (af-validated, T0): 19** — this session elevated `lem-parametric-halo-collapse`
(#17, 915891a), `lem-genuine-disintegration` (#18, 072c97f), `lem-top-concentration` (#19,
2a01032) — three of the four g-bootstrap steps are L0. **Registry: 77 results** (+22 this
session). All new lemmas `proved`/`af: none` with SEPARATE fresh hostile codex verifiers (L5);
L0 claimed ONLY for the af-validated 19.

**THE TERMINAL PICTURE (sketch v9): THE FIVE-ROUTE CONVERGENCE.** Waves W26–W38 attacked the
cap through five independent mechanism families (witness coupling; CS/pincer; collapse family;
absorption/proximity; dual certificates + residual cancellation) — every one bottoms out on
ONE conjecture: **near-cluster absorption** (a tall hidden top cannot keep ≥ 1−θ₀ of its mass
on its ρ-near deep cluster without a cluster-side vertex turning exposed). Five priced levers
(sketch v9): the value-vs-Lipschitz conditioning lemma; the W36 exact transition family;
the deepest-vertex extremal choice; the W30/W31 anchor tension inside the cluster; the
quotient self-loop object. The Route-A chain is otherwise fully reviewed/rigorous
(cap ⇒ pincer ⇒ collapse[RIGOROUS] ⇒ height ⇒ HLC ⇒ exposed-hull), with W-nonemptiness
rank ≥ 3 sharing the mechanism and trunk <2>7 the only unreviewed link.

**Session 11 in one paragraph (user directive: full-proof orchestration, breadth-first,
codex/opus delegation).** Nine waves + two af orchestrations so far. W26 (relaunch): hiddenness
CONSUMED — `lem-hiddenness-dual-witness` + `lem-top-slab-companion`; W25's certificate died
under canonical geometry. W27: trunk <2>6 PAID (`lem-hlc-implies-exposed-hull`, pinned-delta;
loose-delta contract mismatch + Q-not-stochastic interface = named findings). W28: the
assembly codified (`lem-min-a-implies-height` B=13 + `lem-delta-zero-endpoint`). W30+W31:
W-nonemptiness strata (`lem-simplex-visibility`, `lem-sharp-vertex-visibility`,
`cor-rank-two-visible`, `lem-rank3-maxchart-hidden-tangent`). W29+W32+W33: the coupling
toolkit (`lem-hiddenness-depth-markov` >94% witness mass deep+far;
`lem-hiddenness-alpha-slab-leakage`; `lem-cs-low-slab-pincer` SHARP;
`lem-harmonic-affine-bridge` {g:Pg=g}=affine-in-position; `lem-conditional-g-near-exposer`;
`lem-two-observable-pencil-bound`) + THE frontier statement **`conj-low-slab-cap`
(theta-flexible: ANY universal (a,theta) closes the Kernel height clause at B = K_a/theta)**.
**THE CENTRAL DISCOVERY: ONE mechanism (charge slab/witness geometry to row coefficients, or
square the slab defect) now sits under BOTH open ledger items** (FINDINGS 2026-07-07;
bd aism-2fi P0). The certified pincer (W29-X): true-hidden folds back before depth 4τ
(best frontier H/τ = √(5/99)); tall attempts die by absorption.

## ⛔ BLOCKER AT SESSION HALT (2026-07-07 ~01:00): CODEX USAGE QUOTA EXHAUSTED (resets 4:00 AM)

All codex workers died on `ERROR: You've hit your usage limit ... try again at 4:00 AM`.
W38 WAS fully banked before the halt (4b1a654). Killed mid-run with NO output (relaunch
fresh — briefs preserved in the session scratchpad AND summarized in sketch v9):

- **W39-AH** (levers a+c: conditioning lemma + deepest vertex): brief
  `scratchpad/W39/PROMPT-AH.md`. **W39-AI** (lever d: anchor tension / aggregated-witness
  circuit): brief `scratchpad/W39/PROMPT-AI.md`. If the scratchpad is gone, re-derive both
  briefs from conj-near-cluster-absorption's shard body (the five levers) + sketch v9.
- **af orchestration #4: `lem-hiddenness-dual-witness`** — prover build IS in the ledger;
  a plain relaunch resumes: `python3 scripts/af-orchestrate.py lem-hiddenness-dual-witness
  --workers 6 --max-rounds 14 --node-cap 40` (background). On root=validated: mechanical
  banking (the 2a01032 commit is the model).

## Next steps (ranked; resume AFTER the quota reset)

0. Relaunch the three killed workers (above). On W39 harvest: hostile verifier per house
   pattern → bank → sketch v10 if the map moves.
1. af elevation queue (aism-88r) after the witness: lem-cs-low-slab-pincer,
   lem-harmonic-affine-bridge, lem-row-far-dual-certificate (all deps-none, few-line proofs).
2. Trunk <2>7 audit (aism-23b) with the W27 interface findings as explicit audit questions.
3. The loose-delta robustness lemma (small).
4. Standing queue: aism-pld, aism-j3j, alpha->1 (Route B gate), aism-5an, refs (aism-5de,
   aism-1nh), aism-z98 USER DECISION, report labels (aism-av0 — 35+ shards warn-level).

## Standing rules (session-11 additions to the CLAUDE.md/bd-memory set)

Codex workers only (no Fable subagents); ONE af orchestration at a time; **argument//definitions
edits during a live orchestration ONLY as fast atomic edit+commit windows (two guard-abort
lessons this session — resume works from the intact ledger via a plain relaunch)**; hostile
verifier BEFORE codifying any worker proof; verifier corrections that WEAKEN hypotheses are
upgrades — codify the corrected form; theta-flexibility: never treat a calibration constant
as load-bearing without checking; fr: `fr orient` on no-bank turns, one `fr log` pull per
banked wave, ▣ banked ONLY via `fr verify` against the af oracle (claim = the export.md path).

## Recipes

```bash
sh scripts/check-all.sh
python3 scripts/seed-af-workspaces.py <id>                    # then COMMIT before orchestrating
python3 scripts/af-orchestrate.py <id> --workers 6 --max-rounds 14 --node-cap 40   # background
codex exec --skip-git-repo-check -C <repo> -s workspace-write -o <answer> - < <prompt>  # one bg call per worker
# banking an af validation: af export -d proofs/<id> > proofs/<id>/export.md (+ --format latex);
#   sed shard af: seeded->validated; argument.py --generate; register oracle in
#   .frontier/portfolio.json; fr verify proofs/<id>/export.md --oracle af-<id>; fr log ▣; commit.
PYTHONDONTWRITEBYTECODE=1 python3 runs/2026-07-06-w26-hiddenness/scripts/w26_worker_q.py --samples 1000
PYTHONDONTWRITEBYTECODE=1 python3 -u runs/2026-07-06-w29-witness-coupling/scripts/w29_verify.py
PYTHONDONTWRITEBYTECODE=1 python3 -u runs/2026-07-06-w30-w-nonemptiness/scripts/w30_worker_u_audit.py --samples 2000 --seed 30031
```

## What is intentionally NOT here

- Any claim more than NINETEEN results are af-validated. The session-11 reviewed lemmas
  (17 of them) are L5, NOT L0-rigorous.
- Any claim conj-low-slab-cap, conj-near-cluster-absorption, conj-min-a-w4, Kernel(i) at
  rank>=3, or the Kernel Conjecture is proved. The trunk still has <2>7 mod-audit + the loose-delta lemma open.
- Any claim the bootstrap works outside small delta_0 (the theta-flexible form trades B for
  delta_0; state the pair).
- A git remote (local-only by decision) — close = commits + bd close-out, no push.
