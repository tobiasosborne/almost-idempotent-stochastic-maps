<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read **`docs/plans/2026-07-07-top-down-proof-sketch-v8.md`** — THE canonical strategic map
   (v8, session-11 round-3; v7 and earlier superseded in place, kept for line citations).
   **STEWARDSHIP (user mandate, 2026-07-06, binding): reconciling the sketch with newly banked
   evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. **PHASE DISCIPLINE (user, 2026-07-05, binding): no progress theatre** — progress =
   unscoped/unpriced surface shrinking.
4. Run `fr board` and `bd ready`. Session-11 wave artifacts: `docs/waves/2026-07-06-W26/27/28/30`
   + `2026-07-07-W29/31/32/33`; bundles `runs/2026-07-06-w26-hiddenness/`,
   `runs/2026-07-06-w29-witness-coupling/`, `runs/2026-07-06-w30-w-nonemptiness/`.
   Wave prompts + raw answers: session-11 scratchpad (`W26/`–`W34/`).
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-07, session 11 MID-SESSION CHECKPOINT — waves W34 + af #2 IN FLIGHT)

**Rigorous (af-validated, T0): 17** — `lem-parametric-halo-collapse` elevated this session
(915891a; 14/14 nodes, taint clean, fr-oracle ▣). **Registry: 71 results** (+16 this session:
12 reviewed lemmas + 1 corollary + 1 conjecture + op-hlc wiring done earlier). All new lemmas
`proved`/`af: none` with SEPARATE fresh hostile codex verifiers (L5); L0 claimed ONLY for the
af-validated 17.

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

## IN FLIGHT (resume these FIRST if interrupted)

- **W34 (`aism-2fi`/`aism-n7i`): the g-max self-consistency attack** on conj-low-slab-cap —
  codex worker AB, brief `scratchpad/W34/PROMPT-AB.md` (sub-target: the DEPTH-d parametric
  collapse). On harvest: hostile verifier, orchestrator recompute, bank per session pattern.
- **af orchestration #2: `lem-genuine-disintegration`** (elevation queue aism-88r item 2) —
  running in background; round-1 DAG-hygiene churn is normal. On root=validated: af export,
  flip af: seeded→validated, register fr oracle, fr verify (claim = export.md path), fr log
  ▣ banked, commit (all mechanical — see the 915891a commit as the model).
  **While it runs: argument//definitions edits ONLY as fast atomic edit+commit windows.**
- If a wave brief is lost with the scratchpad: re-derive from the wave docs + this file; the
  W34 brief's content is summarized in sketch v8 (attack channel 1).

## Next steps (ranked)

0. Harvest W34 → verify → bank; then the next coupling wave iterates on its named gap
   (the depth-d collapse, if delivered, is a shard on its own).
1. af elevation queue (aism-88r, one at a time): after genuine-disintegration →
   lem-top-concentration (deps none) → lem-hiddenness-dual-witness → lem-cs-low-slab-pincer +
   lem-harmonic-affine-bridge (both deps-none, few-line proofs — cheap validations).
2. Trunk <2>7 audit (aism-23b): thm-classical-factorization classification pass — now with
   the W27 interface findings (Q not stochastic; loose-delta) as explicit audit questions.
3. The loose-delta robustness lemma (small; closes op-exposed-hull's literal wording).
4. W-nonemptiness rank>=3 next wave: rides the unified mechanism (aism-2fi); do not fund
   separately from the coupling unless W34 dies.
5. Standing queue: aism-pld, aism-j3j, alpha->1 (Route B gate), aism-5an, refs (aism-5de,
   aism-1nh), aism-z98 USER DECISION, report labels (aism-av0 — 20+ shards now warn-level).

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

- Any claim more than SEVENTEEN results are af-validated. The 12 new session-11 lemmas are
  REVIEWED (L5), NOT L0-rigorous.
- Any claim conj-low-slab-cap, conj-min-a-w4, Kernel(i) at rank>=3, or the Kernel Conjecture
  is proved. The trunk still has <2>7 mod-audit + the loose-delta lemma open.
- Any claim the bootstrap works outside small delta_0 (the theta-flexible form trades B for
  delta_0; state the pair).
- A git remote (local-only by decision) — close = commits + bd close-out, no push.
