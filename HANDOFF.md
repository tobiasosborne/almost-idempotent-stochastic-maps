<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (now **v32** — *PHASE 2
   IS CLOSED: the whole H-CB subtree incl. the `conj-hcb` parent is
   af-validated; phase 3 (EXT-CB) is the live runway*) +
   `docs/plans/CHANGELOG.md` (newest entry = v32). **STEWARDSHIP mandate
   binding (Rule 9).**
3. **Rigorous (af-validated, T0): 62.** Registry: 254. The `conj-hcb` closure
   is ▣ banked (passing external `fr verify` via oracle `af-conj-hcb`).
4. **STANDING DIRECTIVES (user, binding):** (i) capacity on the open leaves;
   (ii) decomposition as objective function; (iii) FINDINGS dead routes
   absolute; (iv) mostly serial; verification fresh-codex-only; af per §6
   (Claude orchestrates, never judges); (v) no progress theatre; (vi) codex
   capped at xhigh; (vii) Route F L0 closure is P0; (viii) RDSE/LDHR-48
   PAUSED. Session-24 addition: sonnet subagents for queries; general work
   delegated to codex `gpt-5.6-sol`; Claude monitors.
5. `fr board` + `bd ready`; beads sync via **bash** `scripts/beads-sync.sh export`.
6. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-25, session 25 close)

**PHASE 2 (aism-niwk) CLOSED.** T0 34 → 62 across sessions 24–25. The full
H-CB subtree is L0-rigorous: 11 COMP + 15 hcb0–4 lemmas + the `conj-hcb`
parent (11/11 first-pass — every clause of the hostile-amended compound
contract discharged against a first-class validated import). The conditional
clauses (level-one lower modulus ≥ 1/4; level-one bijectivity) remain
load-bearing hypotheses; EXT meets them at `tex:1391` (recorded verifier
finding).

**Report rescoped (user mandate, session 25):** `report/` now reproduces the
live chain only — 26 shards, 24 af-validated prose lemma write-ups
(statement + byte-verbatim contract anchor + prose account of the validated
tree), kernel-route surface deprecated (UNWIRED-whitelisted). `main.pdf`
53pp, pushed. Next report wave: `conj-hcb` + `offdiagonal-inverse` write-ups.
**Hostile prose-vs-export review PENDING (bead filed; reviewer ≠ author).**

## BINDING process laws (learned phase 2; apply to every phase-3 seeding)

1. **Dep alignment:** registry `deps:` line ≡ the workspace first-class
   externals at seeding (mismatch caused every stall; alignment produced 7
   consecutive first-pass validations). Battery = all other validated
   contracts as `-CONTRACT` context externals.
2. **Default first-class set:** `lem-compcb-corner-algebra` +
   `lem-hcb3-uniform-square-lower` in every H-CB/EXT-adjacent seeding.
3. **Cumulative 15-def kit** replayed byte-identical from the previous
   workspace's ledger (`def_added` events; `def-ha-map`/`def-hcb-datum`-style
   frontmatter bodies need `af def-add --file`).
4. **Tripwire factoring:** on BALLOON/3rd-stall, extract the blocking node's
   statement into a `stated` registry micro-lemma (uniform-square-lower
   template), validate it in its own small run, re-seed the parent on it.
5. **Orchestrator hygiene:** porcelain-wide overreach guard — ANY uncommitted
   repo edit aborts a live run; commit `fr` appends atomically in the same
   turn; no repo edits while any orchestration is live.
6. **Banking flips are mechanical:** export → flip frontmatter AND the body
   Status paragraph → regenerate → gate → commit. `fr log` ▣ banked needs
   `fr verify proofs/<id>/export.md --oracle af-<id>` (artifact-path claim;
   register via scripts/register-oracle.py — NOTE portfolio.json format
   drift: if the registrar refuses, insert the entry by text surgery
   preserving formatting).

## Next steps (ranked)

1. **Phase 3 (aism-fgr7): af-elevate the EXT-CB subtree.** Bottom-up queue:
   `lem-extcb-one-dimensional-product` →
   `lem-extcb-corner-dimension-additivity` → `lem-extcb-four-corner-merge` →
   `lem-extcb-one-dimensional-corner-dimension` →
   `lem-extcb1-close-corner-dimension` →
   `lem-extcb1-cross-corner-dimension` → parent `conj-extcb` (deps:
   `conj-hcb` ✓). Three leaves are `stated` (af builds the proof; fine at
   this size). Seed per the process laws above; one backgrounded
   `af-orchestrate.py` at a time (workers 3, rounds 20, cap 45, tier
   routine).
2. **Report wave 3:** `conj-hcb` + `offdiagonal-inverse` prose shards (same
   author pattern), rebuild pdf, push. Then run the batched hostile
   prose-vs-export review (one fresh codex over all shards, per-shard
   verdict lines — W56 pattern).
3. **aism-0163 (blocks phase 4):** focused repair of the quarantined
   MAIN/ledger rows per the v3 verdict + fresh hostile review; F2/F3
   contracts now exist (`lem-routef-f2-positive-unital-compression`,
   `lem-routef-f3-retract-defect`, proved-mod-audit). Also acquire the 7
   Stage-1 external topology sources into `refs/`.
4. Route X deciders (aism-ea2f) — unchanged fallback pricing.

## What is intentionally NOT here

- Any claim `op-classical` is proved/rigorous. It is OPEN. T0 is exactly
  **62** (each a root-validated taint-clean af tree; everything else in the
  chain remains `proved-mod-audit`/`stated`).
- Any movement on the quarantined MAIN/ledger rows, the 4 GAP interfaces, or
  Stage-1 topology provisioning (aism-0163, phase-4 blockers).
- Any movement on RDSE/LDHR-48, the signed trunk, or numerical `K`/`η_K`.
