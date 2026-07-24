<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (now **v30** — *Route F is
   proved-mod-audit COMPLETE; the open work is L0 closure*) + `docs/plans/CHANGELOG.md`
   (newest entry = v30). **STEWARDSHIP mandate binding (Rule 9).**
3. Read **`docs/plans/2026-07-24-af-elevation-campaign.md`** — the L0 campaign ground
   plan (epic **aism-xuvw**). The full W74F evidence base is in
   `docs/plans/2026-07-24-W74F-wave2-artifacts/` (proofs + hostile verdicts).
4. **PRH af-elevation is DONE**: `proofs/lem-prh` root validated (14/14, taint
   clean), `lem-prh` = `proved` / `af: validated`, export banked, aism-h9qc closed.
   No orchestration is live at handoff. **Campaign process lesson (hard-won, honor
   it): the af overreach guard is porcelain-WIDE — ANY dirty/untracked file outside
   the live workspace aborts the run; make NO repo edits at all while an
   orchestration is live** (run #1 aborted on the orchestrator's own mid-run docs
   write; relaunch over the intact tree then validated cleanly).
5. **STANDING DIRECTIVES (user, binding):** (i) capacity on the open leaves;
   (ii) decomposition as objective function; (iii) FINDINGS dead routes absolute;
   (iv) mostly serial; verification fresh-codex-only; af per §6 (Claude orchestrates,
   never judges); (v) no progress theatre; (vi) codex capped at xhigh; (vii) Route F
   / its L0 closure is P0; (viii) RDSE/LDHR-48 attacks PAUSED.
6. `fr board` + `bd ready`; beads sync via **bash** `scripts/beads-sync.sh`.
7. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-24, session 23 FINAL — W74F waves 2/3/3b + W72 + campaign launch)

**Rigorous (af-validated, T0): 35 — `lem-prh` VALIDATED at session close (14/14
nodes, taint clean; campaign phase 0 COMPLETE). Registry: 215. Definitions: 23, the
four W74F defs LOCKED on recorded user ratification (2026-07-24).**

### Route F is `proved-mod-audit` COMPLETE (sketch v30)

`op-classical ⇐ F0 cb-lift ⇐ th_factorization (⇐ th_main_ext ⇐ H-CB + EXT-CB +
Stage-1 packet; + th_almost_idemp interface; + repaired diagonal) ⇐ F2/F3 ⇐ PRH`,
finish `‖Q−E‖_{∞→∞} ≤ (K+4√(2K))√η` for `η ≤ η_K`, all constants relative and
dimension-free, every node fresh-codex hostile-verified and codified. Key shards:
`lem-prh`(+sharpness), `conj-hcb` (amended conditional-inverse contract),
`conj-extcb`, `lem-thmainext-conditional` (restated), `lem-routef-k-ledger`,
`lem-kitaev-diagonal-repair`(+CP-ization), `lem-kitaev-almost-idemp-audit`.
The wave-3 ledger was REJECTED once by its hostile verifier (missing Stage-1 packet)
and closed only after the wave-3b repair — the pipeline demonstrably catches
plausible-but-incomplete closure claims.

**NOT rigorous by L0.** `proved-mod-audit` = one rung below T0; nothing in the chain
is af-validated or byte-citable (the source's printed proof was invalid; ours is a
repair). W72 side-theatre: POTI-0 debt discharged and codified (POTI-0 == RDSE +
LDHR-48 at proved-mod-audit; residuals PAUSED).

### The L0 af-elevation campaign is LAUNCHED (epic aism-xuvw)

- **Phase 0 — COMPLETE:** `lem-prh` af-validated (see START-HERE #4); T0 = 35.
- **Phase 1 — aism-fudw (unblocked, do BETWEEN orchestrations):** factor H-CB /
  EXT-CB / Stage-1 / assembly / ledger proofs into af-sized registry sub-lemmas.
- **Phases 2–5 (dep-chained):** aism-niwk (H-CB) → aism-fgr7 (EXT-CB) → aism-5byv
  (Stage-1 + assembly + ledger) → aism-y81y (F0/F2/F3 codification + the
  `op-classical` root tree).
- Ordering law, workflow loop, and failure surface: the campaign plan doc.

## Next steps (ranked)

0. **Run the decomposition pass** (aism-fudw) — no orchestration is live. Its
   output gates phases 2–5. Surface the Stage-1 topological-input provisioning
   (Lefschetz–Hopf refs/defs) early.
1. **Phase 2 (aism-niwk)** once 1 lands: Ha/COL-HILB def layer + HCB-0..4 workspaces.
2. Route X deciders (aism-ea2f) — unchanged fallback pricing.
3. af-elevation queue (aism-88r) for non-Route-F debt; signed trunk stays parked;
   pauses stand.

## Standing rules (delta from session 22)

- **Verdict-driven contract amendment/restatement** (new precedent): exact contract
  text from a hostile verdict's registry-impact note is applied as a mechanical
  reflection, recorded in body + commit.
- **A hostile REJECTION is a normal cycle** (wave 3 → 3b): bank INVALID, repair the
  named gap, re-verify fresh. No third state for banked work (upheld twice).
- af campaign rules: strictly serial; clean registry tree while live; single minimal
  elevation contracts; banking flips after landing.

## What is intentionally NOT here

- Any claim op-classical is proved/rigorous, or that a hostile verdict equals
  af-validation.
- Any numerical `K`/`η_K` (relative expressions only).
- Any claim beyond exactly **35** af-validated results (`lem-prh` is the sole new
  one; `lem-prh-sharpness` remains proved-mod-audit — elevate separately if wanted).
- Any movement on RDSE/LDHR-48, the signed trunk, or the strategists' altitude
  diagnosis (banked interpretation only).
- Any emptiness claim from the tallness-bound deciders: L3 evidence only.
