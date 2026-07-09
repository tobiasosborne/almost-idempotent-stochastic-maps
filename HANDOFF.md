<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read **`docs/plans/2026-07-09-top-down-proof-sketch-v18.md`** — THE canonical strategic map
   (v18, session-13 close; v17 and earlier superseded in place, kept for line citations).
   Then **`docs/plans/2026-07-09-w54-huddle-charge-decomposition-tree.md`** — the VERIFIED
   decomposition of the terminal node (read PART A through PART B).
   **STEWARDSHIP (user mandate, 2026-07-06, binding): reconciling the sketch with newly
   banked evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. **STANDING DIRECTIVES (user, binding):** (i) TIER-1 FOCUS; (ii) Fable-grade agents
   liberally for deep proof/strategy while Tier-1 nodes remain (verification stays
   fresh-codex-only, §6); (iii) once Tier 1 falls, farm out the parked queue; (iv) no
   progress theatre; **(v) NEW 2026-07-09: the objective function of every Tier-1 attack
   is DECOMPOSITION into lower-complexity pieces** (case trees, small-lemma systems with
   checkable assemblies) — W53/W54 are the template.
4. Run `fr board` and `bd ready`. Session-13 artifacts: waves
   `docs/waves/2026-07-09-W53-binding-constraint-lemmaization.md` +
   `2026-07-09-W54-huddle-charge-decomposition.md` (+ `2026-07-09-W54-artifacts/` — the
   Fable proof docs backing the banked shards, the tree, all verifier verdicts).
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-09, session 13 close)

**Rigorous (af-validated, T0): 28** (unchanged — no af runs this session).
**Registry: 140** (+21 this session; EVERY codified proof passed a SEPARATE fresh hostile
codex verifier, L5; L0 claimed ONLY for the af-validated 28).

**THE STATE OF THE PROOF (sketch v18): the terminal node is a VERIFIED four-leaf system.**
Session 13 executed the decomposition mandate end-to-end: W53 collapsed the three W52
binding constraints into THE HUDDLE CHARGE (sketch v17); W54's Fable-architect case tree
was hostile-verified (INVALID -> prescribed repairs -> VALID-WITH-CORRECTIONS, all
applied), its easy/medium leaves proved or reduced, and both creative branches collapsed:

- **Branch II == {`conj-straddling-web-exclusion` (SL1a) + `conj-shallow-counterweight-
  exclusion` (SL1b)}** via `lem-l2-core-collapse` + `lem-intersection-witness-confinement`
  (the identity-level averaging cap). Alternative: Theorem-C route via
  `conj-summit-cylinder-exclusion` + narrow dual face (wave doc).
- **Branch I == {`conj-cotop-web-coupling` (L6.5) + the L5 dual-face mass minimax
  (aism-vuc)}** via `lem-cotop-witness-pinning`, `lem-downhill-cotop-conic-mass`,
  `lem-psi-corner-trap` (the t*-FREE toolkit — the t*-division death trap is closed).
- Consumption above the node: `lem-absorption-implies-low-slab-cap` wires tall-emptiness
  (+ `conj-far-low-slab-cap`) => `conj-low-slab-cap` => the Kernel height clause.

SL1a and conj-cotop-web-coupling are two windows on ONE object (the confined co-top web);
the honest open count is FOUR sharply-scoped conjectures, each with proved toolkits,
named refuter targets, and preserved proof context.

**Dead by certificate this session (FINDINGS 2026-07-09, do not re-walk):** witness-
averaging for Branch II (identity cap); the averaging axis (degenerate via Y_v);
pointwise-to-simultaneous by averaging; pure co-top rigidity (shallow-counterweight
escape); any starvation constant dividing by t*(u); plus the W53 entries (affine-pairing
blind spot; B2-as-stated subsumed; small-beta witness reading binding).

## Next steps (ranked) — W55

0. **SL1b first** (`conj-shallow-counterweight-exclusion`, graded most attackable):
   codex prover — shallow rows live near the visible hull where exposers have room;
   universal shadowing below kappa should contradict the visible-side machinery
   (lem-row-far-dual-certificate, lem-visible-g-small, the margin lemma).
1. **The confined co-top web as ONE joint Fable wave**: SL1a + conj-cotop-web-coupling
   together (aism-zm8), consuming lem-cotop-witness-pinning + lem-intersection-witness-
   confinement + lem-psi-corner-trap; decomposition-first.
2. **L5 dual-face mass minimax** (aism-vuc): codex geometry problem on Y_v (linear in y;
   the simplex obstruction is sharp — the proof must use Y_v structure + idempotence).
3. conj-far-low-slab-cap + conj-summit-cylinder-exclusion: siblings; may fall to the same
   web mechanisms — check after 0/1.
4. Parked: L7 gaps (aism-2ii), elevation queue (the W53/W54 proved families are prime
   af-elevation shapes — single minimal contracts), trunk <2>7 (aism-ik6), Kernel(i)
   rank >= 3, refs ingest (aism-5de).
5. USER DECISIONS pending: `aism-nlg`, `aism-z98` (standing).

## Standing rules (unchanged from session 12 + the new decomposition directive)

Codex workers for all proving/verifying; Fable-grade for deep proof/strategy (AUTHOR
output — always hostile-verified by fresh codex before codification); ONE af
orchestration at a time; wave docs carry verbatim verdict first-lines; `fr orient` on
no-bank turns; ▣ banked only via `fr verify` against the af oracle. Worker-prompt
patterns + verifier-prompt patterns for decomposition waves: see the W53/W54 scratchpad
prompts quoted in the wave docs (self-contained workspaces: definitions + argument +
CONVENTIONS + the target artifact; verdict-first-line discipline; status discipline
stated in every prompt). NOTE: `codex exec -o FILE` overwrites with the final MESSAGE —
point -o at a scratch FINAL.md, never at the worker's ANSWER.md; recover answers from
the session log if clobbered. Fable agents: instruct INCREMENTAL file writes (<~10k
tokens per call) — one died on the 64k output ceiling and was resumed via SendMessage.

## Recipes

```bash
sh scripts/check-all.sh
python3 scripts/seed-af-workspaces.py <id>       # then COMMIT before orchestrating
python3 scripts/af-orchestrate.py <id> --workers 6 --max-rounds 14 --node-cap 40   # background
codex exec --skip-git-repo-check -C <scratch-workdir> -s workspace-write -o <scratch>/FINAL.md - < <prompt>
```

## What is intentionally NOT here

- Any claim more than TWENTY-EIGHT results are af-validated. All session-13 codified
  proofs are L5 (fresh-hostile-verified), NOT L0.
- Any claim the huddle charge, tall-emptiness, any of the four leaves, or the Kernel
  Conjecture is proved. The W54 tree is a VERIFIED CONDITIONAL derivation — its leaves
  are conjectures.
- Any claim the W52 BLOCKED search or any numerical evidence is a proof (L3).
