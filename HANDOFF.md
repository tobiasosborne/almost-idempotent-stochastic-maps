<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (v32; the CHANGELOG's
   newest delta entry carries the phase-3 state below). **STEWARDSHIP mandate
   binding (Rule 9).**
3. **Rigorous (af-validated, T0): 69.** Registry: 256. Phase 2 (H-CB) is
   CLOSED and ▣ banked (oracle `af-conj-hcb`). Phase 3 (EXT-CB) is ONE
   RESUMABLE RUN from closing (see next).
4. **FIRST TASK — resume the conj-extcb parent (user-stopped mid-run,
   2026-07-25, ZERO loss: the af ledger is append-only).** Tree state at
   stop: 29 nodes, 9 validated, 19 pending, 1 archived, tree intact.
   Resume with exactly:
   `python3 scripts/af-orchestrate.py conj-extcb --workers 3 --max-rounds 24 --node-cap 45 --tier routine --phase verify`
   (backgrounded, one at a time, NO repo edits while live). Its 10
   first-class imports (conj-hcb + the 7 EXT lemmas + default pair) and
   22-def kit are fully provisioned. On validation: export -> flip ->
   regenerate -> gate -> commit -> register oracle
   (scripts/register-oracle.py conj-extcb; if the registrar refuses on
   portfolio.json format drift, insert the entry by text surgery) ->
   `fr verify proofs/conj-extcb/export.md --oracle af-conj-extcb` ->
   `fr log FH banked ... --artifact ... --class af --tier T0` -> close
   bead aism-fgr7. That closes PHASE 3.
5. **STANDING DIRECTIVES (user, binding):** (i) capacity on the open leaves;
   (ii) decomposition as objective function; (iii) FINDINGS dead routes
   absolute; (iv) mostly serial; verification fresh-codex-only; af per §6
   (Claude orchestrates, never judges); (v) no progress theatre; (vi) codex
   capped at xhigh; (vii) Route F L0 closure is P0; (viii) RDSE/LDHR-48
   PAUSED.
6. `fr board` + `bd ready`; beads sync via `bash scripts/beads-sync.sh export`.
7. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-25, session 25 close — user-directed stop)

T0 34 → **69** across sessions 24–25. **Phase 2 (H-CB) CLOSED**: COMP
prerequisites + hcb0–4 tiers + `conj-hcb` parent all af-validated
(conj-hcb ▣ banked via external oracle). **Phase 3 (EXT-CB) effectively
done modulo the parent**: all 7 EXT lemmas af-validated
(one-dimensional-product 25/25, corner-dimension-additivity 39/39,
four-corner-norm 18/18 [tripwire-factored from the merge], four-corner-merge
22+4arch, one-dimensional-corner-dimension 8/8, close-corner-dimension
16/16, cross-corner-dimension 30/30); `conj-extcb` mid-elevation 9/29,
resumable (item 4).

**Two ratified content changes this session (both loud, both pushed):**
- `def-four-corner-merging-datum`: quantitative-complementarity amendment
  (transcription-fidelity to its cited locus tex:1326; USER-RATIFIED
  2026-07-25; af challenge ch-4dd98c4d identified it).
- `lem-extcb-four-corner-merge` contract: smallness hypothesis amended to
  the validated root (`rho+epsilon <= a_merge` — the linker's
  contract-match gate caught the prover's mid-run root amendment;
  verdict-driven precedent; body note records it).

**Report:** rescoped to the live chain (user mandate) — 26 shards, 24
af-validated prose lemma write-ups, 53pp pdf, pushed. Report wave 3 pending:
conj-hcb + offdiagonal-inverse (+ the phase-3 EXT set) write-ups; hostile
prose-vs-export review bead open (reviewer != author).

## BINDING process laws (phases 2–3 distillate; apply to every seeding)

1. **Dep alignment:** registry `deps:` line ≡ workspace first-class
   externals at seeding; battery = all other validated contracts as
   `-CONTRACT` externals. (Mismatch caused every early stall.)
2. **Default first-class pair:** `lem-compcb-corner-algebra` +
   `lem-hcb3-uniform-square-lower` in every seeding.
3. **Cumulative def kit (22)** replayed byte-identical from the previous
   workspace's ledger `def_added` events (`--file` for frontmatter bodies);
   registry defs added per the shard's `defs:` line.
4. **Tripwire factoring:** BALLOON or 3rd stall on one cluster => extract
   the blocking node's statement into a `stated` registry micro-lemma,
   validate it in its own run, re-seed/resume the parent on it
   (uniform-square-lower and four-corner-norm precedents).
5. **Orchestrator hygiene:** porcelain-wide overreach guard — any
   uncommitted repo edit aborts a live run; commit `fr` appends atomically;
   NO repo edits while an orchestration is live. Workspace re-seeds must
   `rm -rf` the WHOLE dir (git rm leaves gitignored caches -> af init
   sequence-gap error; bd memory recorded).
6. **Mid-run root amendments happen:** the linker's contract-match gate
   catches them at the banking flip — when it fires, amend the registry
   contract to the VALIDATED root verbatim (verdict-driven precedent),
   never the other way.
7. **Banked (▣) logging** needs the artifact-path claim form:
   `fr verify proofs/<id>/export.md --oracle af-<id>`.

## Next steps (ranked)

1. Resume + close `conj-extcb` (item 4 above) => PHASE 3 CLOSED; close
   bead aism-fgr7; sketch v33 + CHANGELOG + HANDOFF reconciliation at that
   boundary (Rule 9).
2. **aism-0163 (blocks phase 4):** focused repair of the quarantined
   MAIN/ledger rows per the v3 verdict + fresh hostile review; F2/F3
   contracts exist (proved-mod-audit). Acquire the 7 Stage-1 external
   topology sources into `refs/`.
3. **Report wave 3:** conj-hcb + offdiagonal-inverse + EXT-tier prose
   shards (opus author pattern; scratchpad-only while runs are live);
   then the batched hostile prose-vs-export review (open bead).
4. Route X deciders (aism-ea2f) — unchanged fallback pricing.

## What is intentionally NOT here

- Any claim `op-classical` is proved/rigorous. It is OPEN. T0 is exactly
  **69**; `conj-extcb` is NOT yet validated (9/29 mid-run); everything else
  in the chain above EXT remains `proved-mod-audit`/`stated`/quarantined.
- Any movement on the quarantined MAIN/ledger rows, the GAP interfaces, or
  Stage-1 topology provisioning (aism-0163).
- Any movement on RDSE/LDHR-48, the signed trunk, or numerical `K`/`η_K`.
