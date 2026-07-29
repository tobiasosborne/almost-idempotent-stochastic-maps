<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The governing plan is the RATIFIED W78 package as executed through the
   endorsed W97 rebuild design
   (`docs/plans/2026-07-28-13E-BINDER-design/`, v3 + v3.1 + v3.2) and the
   S1-POLAR-v6 serial order. The Stage-1 tracker bead is **`aism-e1qs`**.
   The proof sketch is `docs/plans/CURRENT.md` → v38 (v39 fold-in still
   pending, see Next steps 4).
3. **Rigorous (af-validated, T0): 113.** Registry: 299. `op-classical`
   OPEN.
4. **SESSION-35 HEADLINE (2026-07-29): ELEVEN elevations banked
   (108th→119th, T0 102→113).**
   - **The W98 elevation queue is COMPLETE (8/8)** and **all six
     2026-07-28 retractions are remedied**: rows 2–8 banked
     (explicit-group-closeness 109th; explicit-smooth-unitary-operations
     110th; inversion-derivative-control re-validated 111th; 13e
     FIRST-EVER validation 112th; 13c via the repo's FIRST IN-LEDGER
     REPAIR 113th; 13f 114th; 13g 115th). The two retired parents stay
     retired (their content lives in the bridges + 13e).
   - **Row 13 `lem-stage1-polar-constant-ledger` (the Stage-1 KEYSTONE)
     af-VALIDATED (116th)** — one universal witness tuple W for all
     eight clauses; consumer re-check byte-verified (A_5)/(A_6)/(A_7)
     against 13e/13f/13g before seeding; 11/11 first-pass, zero
     challenges.
   - Serial order continued: `lem-finite-polyhedron-maximal-simplex-
     placement` (117th; its run-1 STUCK abort was a genuine verifier
     CONTRACT-AMBIGUITY catch — the user RATIFIED the pointwise
     disambiguation in-session, bead `aism-iw4w` closed, contract now
     ends "; therefore every point of every finite fixed set does."),
     `lem-stage1-uniform-inversion-isolation` (118th),
     `lem-stage1-quotient-manifold-package` (119th).
   - **Report paper-track SYNCED** (two Opus worktree subagents, merged
     centrally, commit `f89bc195`): shards 47–51 restored (re-validated
     rows conjecture→lemma envs with fresh prose accounts of the NEW
     trees; retired parents honest) + NEW shards 49b (explicit bridges)
     and 51b (ledger keystone). PROVENANCE/UNWIRED fully reconciled;
     stale surface banner refreshed; PDF builds clean.
5. **Two BINDING process laws (LEARNINGS 2026-07-28) + one BINDING
   discipline (validated 11× this session):** (i) every definite
   description a proof root binds must have a provider external that
   supplies the TYPED WITNESS; (ii) a parameterized proof fixes provider
   witnesses FIRST and transports receiving fields by monotonicity;
   (iii) every elevation seeds with a per-shard BINDING
   build-granularity note (one node per design-skeleton step, no
   sub-splitting routine estimates) — 7 of 11 runs this session landed
   first-pass under it, none ballooned.
6. **NEXT SESSION STARTS HERE:**
   1. **Launch `lem-stage1-quotient-left-inversion`** (downstream row 4
      of S1-POLAR-v6 §5; design budget 8/3). The workspace is FULLY
      SEEDED and committed (3 defs incl. def-h-space-left-inversion + 5
      T0 dep externals, byte-verbatim; discipline note in the shard;
      round-trip OK) — launch was deferred at the user's graceful-stop
      request. Command:
      `AF=~/go/bin/af python3 scripts/af-orchestrate.py lem-stage1-quotient-left-inversion --tier routine --workers 5 --max-rounds 10 --node-cap 12`
      (background, single call). Bank per the verified sequence (item 7).
   2. Then, strictly serial: `lem-stage1-quotient-inversion-index-data`
      (needs the left inversion; all other deps already T0) →
      `lem-stage1-quotient-finite-cw` (BLOCKED on
      `lem-topology-finite-triangulation`, still stated/seeded — elevate
      that leaf first; Munkres Thm 10.6 external, see `aism-j5t9`) →
      G-S1 → MAIN → the 14-row ledger → k-ledger → f0-assembly → root
      rewire LAST (v36-sketch serial order).
7. **Banking sequence (verified ~29×):** af export (md+tex) → per-id
   oracle appended to `.frontier/portfolio.json` (absolute paths) →
   `fr verify proofs/<rid>/export.md --oracle af-<rid>` → mechanical
   shard flip → regenerate (`argument.py --generate`,
   `gen-report-dag.py`, `gen-report-stats.py --extract`) → check-all →
   `fr log FH banked --artifact <export> --tier T0` → commit → push →
   next seed. If a PROVENANCE row pins the shard/export hash, refresh it
   mechanically (sha256[:16]) — the pre-commit gate catches staleness.
8. **Orchestration laws (BINDING):** af runs strictly sequential; no
   design/audit codex job while an af run is live; non-`.frontier/` repo
   writes abort live runs as PROVER-OVERREACH (subagents during a live
   run → ISOLATED WORKTREES, merge in a zero-live-run window — the
   validated session-35 pattern); fr/bd writes FIRST, commit, launch
   LAST; commits only in zero-live-run windows; `git push` allowed while
   a run is live. Codex = `gpt-5.6-sol`, xhigh cap (prover xhigh ONLY
   after a STUCK). A hard-cap hit is a factoring stop; a verifier
   finding that needs a CONTRACT change stops the campaign and returns
   to design/user (validated live: the maximal-simplex catch).
9. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at
   close). All work committed AND pushed. NOTHING is in flight.

## Next steps (ranked)

1. Item 6.1: launch + bank quotient-left-inversion, then item 6.2's
   serial chain (elevate `lem-topology-finite-triangulation` before
   quotient-finite-cw).
2. Literature follow-up (user question, 2026-07-29): Gonzalez–Hartfiel,
   *On the structure of the stochastic idempotent matrix space*, LAA 145
   (1991) 141–158 is NOT in the lit DB (only the unrelated
   Hartfiel–Meyer 1998 trace in FINDINGS.md) — directly about
   op-classical's target set; decide whether to queue it in
   RESEARCH_NOTES.md (acquisition needs institutional access;
   ScienceDirect 403s direct fetch). Flor 1969 is refs-staging Item 5,
   acquired + hash-verified, never promoted (uncited).
3. Report polish carried from the sync: upgrade shard 51's
   `\texttt{...}` bridge mentions to `\ref`s (labels now exist in 49b);
   registry-side wording refresh for the two retired-parent shards
   (they still say "pending the design audit"; the report states
   retirement as fact per the endorsed design).
4. Sketch v39 fold-in: the queue + row 13 + downstream banks change the
   map materially (supersede by dated file, re-run
   `scripts/gen-current-pointer.py`).
5. Carried housekeeping: `aism-j5t9` (Munkres def external);
   polar-retraction 29-node REFACTOR warning (cosmetic);
   `def-stage1-polar-witness-data` `\rm` typeset flag (still flagged by
   gen-report-defs, non-blocking); report/*.aux policy; repo-root-
   relative oracle paths; 12 dormant signed-trunk draft defs;
   `aism-ur9` (dormant); two stale pre-session-33 agent worktrees under
   `.claude/worktrees/` (agent-a745…, agent-ad79… — verify merged/stale
   before removing; the two session-35 report worktrees were removed
   after merge).

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 113 covers the Route-F
  row chain and the entire rebuilt Stage-1 block through
  quotient-manifold-package; everything downstream of the seeded
  quotient-left-inversion remains non-rigorous until validated.
- Any claim the remaining serial rows WILL validate — each is tested
  only by its own elevation.
- The two retired parents (`lem-stage1-approximate-group-laws`,
  `lem-stage1-smooth-unitary-operations`) re-elevating — retired in
  place per the endorsed design; their live content is the explicit
  bridges + 13e.
- Route X / XE decider work (fallback only). Signed trunk PAUSED.
