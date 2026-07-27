<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The governing plan is the RATIFIED
   **`docs/plans/2026-07-27-W78-ratification-package.md`** (D1–D4). The live
   campaign bead is **`aism-kqeb` (W80)**. The proof sketch is
   `docs/plans/CURRENT.md` → v35 (sessions 31–32 T0 gains NOT yet folded
   into a v36 — Rule-9 debt, now medium-sized: 12 new T0 results this
   session; fold when the transport block closes).
3. **Rigorous (af-validated, T0): 106.** Registry: 295. Definitions: 45.
   `op-classical` OPEN.
4. **Session-32 arc (T0 95 → 106):** codex usage was reset EARLY by the
   user (2026-07-27), and the serial polar §9 elevation queue ran:
   - Row 7 `lem-stage1-polar-path-admissibility` (96th; 12/12 first-pass).
   - Row 8 `lem-stage1-inversion-derivative-control` (97th; 10/10
     first-pass).
   - Row 9 `lem-stage1-smooth-unitary-atlas` (98th; 14/14; one
     pending-sibling challenge repaired in-run; Lee C.40 byte-matched as
     `GT-lee-2ed-thm-C.40`).
   - Row 10 `lem-stage1-smooth-polar-inverse` (99th; 21/21 first-pass;
     Lee C.34 + C.36 byte-matched as `GT-lee-2ed-thm-C.34` /
     `GT-lee-2ed-cor-C.36`).
   - Row 11 `lem-stage1-smooth-unitary-operations` (100th; 15/15; run 2 —
     run 1 was a FALSE-POSITIVE PROVER-OVERREACH abort on the
     orchestrator's own `.frontier/` Stop-hook writes; the guard now
     exempts `.frontier/`, see item 7).
   - Row 12 `lem-stage1-polar-scalar-arithmetic` (101st; 15/15
     first-pass). **All analytic rows 1–12 are T0.**
   - Transports: 13a `rectified-cstar-transport` (102nd; 7/7), 13b
     `unitary-graph-transport` (103rd; 9/9), 13c `maurer-cartan-transport`
     (104th; 13/13; two conditional-uniqueness challenges repaired
     in-run), 13d `polar-retraction-transport` (105th; 5/5), 13f
     `polar-path-transport` (106th; 9/9).
5. **13e `lem-stage1-approximate-group-laws-transport` is PAUSED — USER
   DECISION `aism-b5hz`.** Three STUCK runs (last with prover xhigh)
   converged on a genuine **ratified-contract interface defect**: the
   group-laws family (`lem-stage1-approximate-group-laws` + two children)
   binds u_delta by the ELLIPTICAL definite description "the inverse
   u_delta of the polar map", while the ratified 13e transport contract
   binds (u_delta, h_delta) EXPLICITLY as the unique inverse of
   Pi_delta(U,H) = U bold-dot H. The identification u_grp = u_pol needs a
   typed polar datum the parent contract never exposes — formally
   underivable from ANY validated externals (coherence-naturality needs
   two typed polar data; the group-laws side supplies none). Two dep
   widenings (polar-retraction, coherence-naturality) were landed
   (contract BYTE-UNCHANGED, harmless, keep them). Workspace intact,
   28/37 nodes validated. Options in the bead: (A) mini design/audit
   cycle restating 13e's binder anaphorically (deviates from the ratified
   design text — needs ratification; check what row 13 needs first);
   (B) explicit-binder amendment of the group-laws family + re-elevation
   (3 af-validated contracts touched); (C) fresh codex design round.
   13f validating cleanly (bare-u_delta parent anaphor resolved against
   the explicit polar-retraction import) proves the defect is
   13e-SPECIFIC, not transport-family-wide.
6. **NEXT SESSION STARTS HERE: launch transport 13g.**
   `lem-stage1-inversion-derivative-transport` is SEEDED (round-trip
   verified) and its wave W95 is ALREADY DISPATCHED in the fr log (the
   user stopped the session between dispatch and launch). First action:
   `python3 scripts/af-orchestrate.py lem-stage1-inversion-derivative-transport
   --tier routine --max-rounds 15` (background, turn's LAST action), then
   bank per item 8 and harvest under W95. After 13g: **row 13
   (`lem-stage1-polar-constant-ledger`, the 8-way conjunction assembly)
   consumes ALL SEVEN transports and is therefore BLOCKED on the 13e
   decision `aism-b5hz` — resolve that first.** Then maximal-simplex +
   the 5 downstream rows, then package §5 step 3 (G-S1 split producers),
   then MAIN (`DESIGN-MAIN-STRUCTURE-v5.md` §10), the 14-row ledger, the
   strengthened k-ledger, f0-assembly, root rewire LAST.
7. **Tooling changes this session (all committed):**
   - `scripts/af-orchestrate.py`: the prover-overreach guard now EXEMPTS
     `.frontier/` — the fr Stop hook forces orchestrator log writes every
     turn, which false-positived a live run. `definitions/`, `argument/`,
     `report/`, `scripts/` stay protected.
   - `scripts/tests/test_register_oracle.py`: the real-portfolio case now
     SKIPs on a foreign-root portfolio (portfolio.json records absolute
     paths of the main checkout), so the pre-commit gate passes in git
     worktrees. Red→green verified in the main checkout (17 passed).
   - Two stale `argument/` shard bodies reconciled with their
     af-validated frontmatter (`lem-kitaev-almost-idemp-audit`,
     `lem-routef-functional-calculus-closeness`).
8. **Banking sequence (verified ~17× total):** af export (md+tex) →
   append per-id oracle to `.frontier/portfolio.json` (`af-<rid>` /
   `scripts/oracles/af-validated.py <rid>` / ledger+shard inputs,
   absolute paths) → `fr verify proofs/<rid>/export.md --oracle af-<rid>`
   → flip shard mechanically (status: proved / af: validated + body
   Status update) → regenerate (`argument.py --generate`,
   `gen-report-dag.py`, `gen-report-stats.py --extract`) → check-all →
   `fr log FH banked --artifact <export> --tier T0 --decide EXPLOIT FH`
   → commit → seed the next row in the same commit window.
9. **Orchestration laws (BINDING, one amendment):** af runs strictly
   sequential; no design/audit codex job while an af run is live; any
   non-`.frontier/` repo write aborts a live run as PROVER-OVERREACH
   (the `.frontier/` exemption is new — fr logging mid-run is now safe);
   fr/bd writes FIRST, commit, af launch as the turn's LAST action;
   commits only in zero-live-run windows; `git push` only while a run is
   live.
10. **REPORT IS CAUGHT UP (user mandate this session).** All 18
    previously unanchored T0 results are now reproduced in the lab-book:
    shards `42_routef_f0_seam` / `43_routef_ai_ledger` /
    `44_routef_f2_f3` (Route-F chain) and `45_stage1_polar_charts` /
    `46_stage1_polar_retraction` / `47_stage1_group_laws` /
    `48_stage1_smooth_polar` (Stage-1 polar rows 1–9), written by two
    Opus worktree agents, merged with genuine full gates in the main
    checkout; UNWIRED.md shrunk by 18; 36 PROVENANCE source rows + 18
    claim rows added. **Results 99–106 (smooth-polar-inverse through
    polar-path-transport) are NOT yet in the report** — next report
    catch-up wave should add them (same worktree-agent pattern works;
    note for agents: symlink the gitignored `refs/<source-id>/` payloads
    into the worktree or `check-refs` fails, and keep new shard numbers
    disjoint).
11. Standing mandates: codex = `gpt-5.6-sol`, xhigh cap (escalate prover
    to xhigh ONLY after a STUCK; factor per a fresh design cycle ONLY
    after a BALLOON); batched verification default; NOTHING lands without
    ratification (D1–D4 envelope); Route X/XE fallback only; signed trunk
    PAUSED.
12. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at
    close). All work committed AND pushed.

## Next steps (ranked)

1. **Launch 13g** (`lem-stage1-inversion-derivative-transport`; seeded,
   W95 dispatched — see item 6) and bank it.
2. **`aism-b5hz`: USER DECISION on the 13e interface defect** — blocks
   row 13 (constant ledger) and hence the rest of the polar queue.
3. Report catch-up wave for results 99–106 (item 10).
4. Sketch v36 fold-in of the session-31+32 T0 gains (Rule-9 debt, now 23
   results behind v35).
5. Polar §9 steps 28–29 (three separately-designed trace rows +
   corrected `lem-stage1-extra-fixed-class`) — blocked on their own
   audited campaign designs.
6. Package §5 step 3 (G-S1 split producers) once rows 1–13 are T0.
7. Carried housekeeping: `aism-j5t9` (Munkres C^r-triangulation def
   external); NODE_SOFT_CAP brittleness-prose drift (AGENTS.md:90-91,
   argument/README.md:80-81); polar-retraction 29-node REFACTOR warning
   (cosmetic); `def-stage1-polar-witness-data` body uses `\rm` which the
   defs generator cannot typeset (warning-level flag on every
   gen-report-defs run); report/*.aux policy; repo-root-relative oracle
   paths (would also let the worktree test-skip retire); 12 dormant
   signed-trunk draft defs; `aism-ur9` (dormant).

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 106 covers the Route-F
  row chain, polar analytic rows 1–12, and transports 13a–d, f. Transport
  13e (paused), 13g (seeded), row 13, maximal-simplex, the 5 downstream
  rows, G-S1, MAIN, the 14-row ledger, the strengthened k-ledger,
  f0-assembly, and the root rewire all remain non-rigorous.
- Any promise 13e resolves without a ratified contract change — three
  independent verifier cohorts established the underivability; do not
  re-run it unchanged (it will STUCK again).
- Route X / XE decider work (fallback only). Signed trunk PAUSED.
