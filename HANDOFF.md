<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read **`docs/plans/2026-07-10-top-down-proof-sketch-v22.md`** — THE canonical strategic
   map (v22, W58 extra-vertex delta; v21 and earlier superseded in place, kept for line
   citations). Then `docs/waves/2026-07-10-W56-sl1a-decomposition-close.md` (the W56
   close: the wall, the harvest, the new three-cell SL1a surface).
   **STEWARDSHIP (user mandate, 2026-07-06, binding): reconciling the sketch with newly
   banked evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. **STANDING DIRECTIVES (user, binding):** (i) TIER-1 FOCUS; (ii) the objective function
   of every Tier-1 attack is DECOMPOSITION into lower-complexity pieces — BUT NOTE the
   W56 wall: for SL1a-shaped targets, "one hard leaf on a smaller class" after free
   preprocessing is a certified dead objective; decompose by MECHANISM SEPARATION
   (the three-cell shape) instead; (iii) creativity mandate (2026-07-09): proof-strategy
   subagents are prompted to think outside the box while respecting FINDINGS dead routes;
   (iv) work mostly SERIALLY; Fable-grade agents (serial) for truly demanding creative
   author steps — verification stays fresh-codex-only (§6); (v) no progress theatre.
4. Run `fr board` and `bd ready`. This checkout HAS the local beads DB. NOTE: beads has
   NO Dolt remote configured anywhere (`bd dolt push/pull` cannot work; the DB is
   local-only to this machine — cross-device sync is a pending user decision).
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-10, W56 close)

**Rigorous (af-validated, T0): 28** (unchanged — no af runs). **Registry: 150** (+7
proved L5 lemmas, +3 conjectures this wave; EVERY banked proof passed a SEPARATE fresh
hostile codex verifier; L0 claimed ONLY for the af-validated 28).

**THE STATE OF THE PROOF (sketch v20): SL1a = three quantified sigma-cells on a proved
interface.** W56 ran resumed-architect (codex ultra) -> hostile r1 (INVALID) -> Fable
repair -> hostile r2 (INVALID) -> extraction -> per-shard verification (4 VALID +
6 VALID-WITH-CORRECTIONS, 0 INVALID) -> corrections -> BANK. The two INVALIDs converged
on a structural wall (now a FINDINGS certificate): after the free routine pipeline, any
retained-class hard leaf restates SL1a. The honest deliverable is mechanism separation:

- **Proved (L5):** `lem-sl1a-score-selector`, `lem-sl1a-corner-ledger` (Gamma_f(C_f) >
  1/2, universal over legal kernels), `lem-radial-horn-partition`,
  `lem-zero-face-one-sixteenth-capacity-kill`, `lem-affine-barycenter-identity`,
  `lem-clone-invariant-row-complexity`, and **`lem-sl1a-three-cell-reduction`**
  (three cells => SL1a, delta_0 = min(delta_D, delta_I, delta_X, 2^-16)).
- **The new SL1a surface (OPEN):** `conj-sl1a-deep-diagonal-cell` (H-D),
  `conj-sl1a-intersection-diagonal-cell` (H-I), `conj-sl1a-off-diagonal-cell` (H-X).
  SL1a is EQUIVALENT to their conjunction — sharper windows, not strict progress.

**New dead routes (FINDINGS 2026-07-10):** one-hard-leaf-after-free-preprocessing;
lex-(V,R) minimal-counterexample stratification; freight censoring without a norm gap;
second-generation L-C recursion; max-principle far-side return (= W55
carrier-coincidence). The W55 dead routes and walls are unchanged.

**The huddle-charge surface after W56:** {H-D + H-I + H-X} (== SL1a) +
`conj-shallow-counterweight-exclusion` (SL1b) / `conj-cotop-web-coupling` + the L5
dual-face mass minimax (aism-vuc). Four Tier-1 windows became six sharper ones.

## Next steps (ranked) — W57

0. DONE: W57 minimal family AND W58 extra-vertex family both INFEASIBLE (exact, stable
   Farkas; bundles runs/2026-07-10-w57-* and runs/2026-07-10-w58-*; L3; the obstruction
   is K-parametric per the W58 CERTIFICATE). LIVE: 0b paper-proof the K-parametric
   completion-obstruction candidate lemma (aism-cq2, W59 in flight at session close).
   Original item for reference: **H-X first** (`conj-sl1a-off-diagonal-cell`): it shares the completion-obstruction
   shape with the W55 large-gauge wall, so ONE exact `P=L*B, B*L=I`
   completion/refutation LP wave (v19 item 3 == v20 item 0) serves both fronts. A
   rational feasible tau->0 family refutes; a stable dual infeasibility certificate is
   the intended dimension-free mechanism.
1. **Codify W55 E1-E5** after a fresh standalone prover/verifier pass (HANDOFF-v19
   item 0, still pending).
2. **The small-gauge bridge** `A0<=3/32 => SL1a(cells)+SL1b` — carry the conditioning
   constants verbatim (484/223, 256/223).
3. **H-D / H-I**: far-horn v-in-F_u coupling (H-D) and the intersecting-hull anatomy
   via `lem-intersection-witness-confinement` (H-I); prompt for out-of-the-box
   mechanisms, constraints = the W56 dead routes.
4. **SL1b** (easiest sibling, unchanged) and the **L5 minimax** (aism-vuc, independent).
5. Parked: af-elevation queue (the W56 proved 7 are prime single-contract shapes; also
   the W53/W54 families), L7 gaps (aism-2ii), trunk <2>7 (aism-ik6), refs ingest
   (aism-5de). USER DECISIONS pending: `aism-nlg`, `aism-z98`, beads Dolt remote.

## Standing rules (updated 2026-07-10)

Codex = gpt-5.6-sol (smoke-tested this session: model+effort verbatim-verified in
session logs); effort ULTRA for creative/demanding, xhigh for hostile verification,
high for routine — `af-orchestrate.py --tier` encodes this. Fable-grade agents: AUTHOR
role only, serial, for the genuinely creative steps; ALWAYS hostile-verified by fresh
codex before codification; instruct INCREMENTAL file writes (<~10k tokens per call).
ONE af orchestration at a time; wave docs carry verbatim verdict first-lines;
`fr orient` on no-wave turns; ▣ banked only via `fr verify` against the af oracle.
`codex exec -o FILE` overwrites with the final MESSAGE — point -o at a scratch
FINAL.md. Codex usage limits can interrupt long waves: bridge with a delayed
dispatcher (sleep-until-reset + retry loop, see the W56 close Process notes).

## Recipes

```bash
sh scripts/check-all.sh
python3 scripts/seed-af-workspaces.py <id>       # then COMMIT before orchestrating
python3 scripts/af-orchestrate.py <id> --workers 6 --max-rounds 14 --node-cap 40   # background
codex exec --skip-git-repo-check -C <scratch-workdir> -m gpt-5.6-sol \
  -c 'model_reasoning_effort="ultra"' -s workspace-write -o <scratch>/FINAL.md - < <prompt>
```

## What is intentionally NOT here

- Any claim more than TWENTY-EIGHT results are af-validated. The W56 banked 7 are L5
  (fresh-hostile-verified), NOT L0.
- Any claim SL1a, any sigma-cell, SL1b, L6.5, the L5 minimax, tall-emptiness, the
  huddle charge, or the Kernel Conjecture is proved. `lem-sl1a-three-cell-reduction`
  is a CONDITIONAL derivation; its three deps are conjectures.
- Any claim the three-cell surface is strict progress: SL1a is EQUIVALENT to the
  conjunction. The gain is mechanism separation + proved interface + named refuter
  targets, honestly stated.
- Any claim the W55 E1-E5 or small-gauge bridge are codified (still pending, W57 items
  1-2).
