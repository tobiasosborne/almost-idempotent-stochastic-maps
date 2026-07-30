<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v39** (NOT yet folded
   for this session's banks — see item 7.3). The live campaign is the
   **S1-ENDGAME elevation queue** (bead `aism-8dsp`, claimed):
   **10 of 13 rows BANKED**; rows 11–13 (C1–C3) remain.
3. **Rigorous (af-validated, T0): 127.** Registry: 311. `op-classical`
   OPEN.
4. **SESSION-37 RECORD (2026-07-30), the S1-ENDGAME session:**
   - **Design cycle CONVERGED (rounds 2–5 run this session):** audit v2
     (REDESIGN, Hatcher ground truth VERIFIED locally) → v3 (REDESIGN,
     3 fatals) → v4 (REDESIGN, 2 fatals; the r_bidx=r_iso ambient
     bridge PASSED) → **v5 LAND, zero corrections**
     (`docs/plans/2026-07-29-S1-ENDGAME-design/DESIGN-S1-ENDGAME-v5.md`
     + `AUDIT-S1-ENDGAME-v5.md`). Fatals per round: 6→3→2→0.
   - **USER RATIFIED the full package** (13 contracts + 3 externals,
     2026-07-30). 13 shards landed VERBATIM by script (registry
     298→311), all 13 workspaces seeded (round-trip verified),
     UNWIRED whitelist updated.
   - **TEN ROWS ELEVATED AND BANKED (124th–133rd rigorous results, T0
     117→127):** A0 `hspace-coproduct-tail` (14 nodes, 1 challenge) →
     A1 `exterior-cohomology` (8, clean; the two Hatcher externals
     consumed exactly as registered) → A2 `associated-graded` (9,
     first-pass) → A3 `left-inversion-trace` (6, first-pass; A-CHAIN
     COMPLETE) → B0a `bound-quotient-left-inversion` (13 live == cap,
     3 challenges repaired; the typed epsilon_B^r architecture
     validated) → B0i `bound-quotient-local-index` (19 nodes, FIVE
     challenges repaired incl. a false-as-displayed quotient-norm
     equality; **user-ratified one-row cap amendment 15→20**, commit
     bc3ca739, after a balloon stop at 17 — transparent repair growth,
     precedent scoped) → B0s `bound-inversion-isolation` (10, 1
     challenge) → B0b `bound-quotient-index-data` (7, first-pass;
     B0 CHAIN COMPLETE) → **B1 `extra-fixed-class` (15 == cap, 3
     challenges repaired — THE KEYSTONE: one ledger elimination, the
     extra fixed class via Lefschetz–Hopf)** → C0
     `fixed-unitary-projection-bridge` (10, 2 unbound-Q challenges
     repaired; architecture (b) validated).
   - Every bank: export md+tex → register-oracle → `fr verify` pass →
     mechanical flip → regenerate → check-all OK → fr log banked →
     commit → push (the verified sequence, now ~43×).
5. **NEXT SESSION STARTS HERE — resume the queue at row 11/13:**
   1. **C1 `lem-stage1-rectified-nontrivial-projection`** (budget
      6/3/10). Provision: defs `def-extended-epsilon-cstar-algebra`,
      `def-epsilon-cstar-algebra`, `def-delta-projection`; dep
      externals `lem-stage1-rectified-cstar-control` (W-free provider)
      + `lem-stage1-fixed-unitary-projection-bridge` (C0) — BOTH T0.
      Then launch (tier routine, workers 4).
   2. **C2 `lem-stage1-original-complementary-pair`** (6/2/10; defs
      extended-epsilon-cstar-algebra + delta-projection; dep C1).
   3. **C3 `lem-stage1-fresh-two-point-inclusion`** (9/3/14; defs
      extended-epsilon-cstar-algebra, delta-projection,
      extended-delta-inclusion, operator-space, projection-basis; dep
      C2; PLUS the ONE Kitaev GT external
      `GT-kitaev-prop-delta-hominc` at
      `approximate_algebras.tex:1194-1196` — register with the
      locus-trap rule: `\n`-only awk extraction + programmatic
      quote-at-locus assertion, as done for the Hatcher externals in
      commit bae06f82's pattern).
   4. On C3's bank the **G-S1 GATE IS DISCHARGED** (all three
      producers T0). Then: fold the 10–13 banks into a new
      top-down-proof-sketch version (supersede v39 by dated file +
      re-run `python3 scripts/gen-current-pointer.py`), close
      `aism-8dsp`, and the MAIN campaign still needs `aism-dm8n`
      (P0 defs, USER) + M01–M18 before M19-S1..M28.
6. **Per-row worked pattern (verified 10×; follow verbatim):**
   provision (def-add --file per def; add-external per dep with
   "imports validated registry lemma proofs/<dep> — <contract>") →
   commit provisioning → launch
   `python3 scripts/af-orchestrate.py <id> --workers 4 --max-rounds
   <rounds> --node-cap <cap> --tier routine` in background → on
   "converging but hit --max-rounds" with all challenges resolved,
   resume `--phase verify --max-rounds 6`; with OPEN challenges,
   resume full phase → on root=validated, bank per item 4's sequence.
   A BALLOON abort is a factoring STOP → classify (transparent repair
   growth vs concealed obligations) → user decision (precedent:
   bc3ca739 allows a scoped cap amendment for the former).
7. **Parallel P2 / carried items:**
   1. `aism-9kmt` report sync — now covers banks 120–133 (14 results
      incl. the ten S1-ENDGAME rows); UNWIRED delisting on anchoring.
   2. Parallel-af proposal (user "still thinking"): worktree-per-run
      on DAG antichains; unblocker = `aism-2kyc` (repo-root-relative
      oracle paths; MERGE-NOTES §4.2). Not yet filed as a bead.
   3. `docs/plans/CURRENT.md` (v39) does NOT yet reflect this
      session's 10 banks — the sketch fold-in is Rule-9 work for the
      session that discharges G-S1 (item 5.4).
   4. Carried housekeeping: polar-retraction 29-node REFACTOR warning
      (cosmetic); `def-stage1-polar-witness-data` `\rm` typeset flag;
      report/*.aux policy; 12 dormant signed-trunk draft defs;
      `aism-ur9` (dormant); two stale pre-session-33 agent worktrees
      under `.claude/worktrees/`; Gonzalez–Hartfiel 1991 not in lit
      DB; Flor 1969 acquired, never promoted.
8. **Orchestration laws (BINDING, unchanged):** af runs strictly
   sequential; no design/audit codex while an af run is live; fr/bd
   writes FIRST, commit, launch LAST; commits only in zero-live-run
   windows. Codex = `gpt-5.6-sol`, xhigh cap (elevations run tier
   routine). A hard-cap hit is a factoring stop (see item 6 for the
   ratified transparent-repair exception path). A verifier finding
   needing a CONTRACT change returns to design/user.
9. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at
   close). All work committed AND pushed. **NOTHING is in flight.**

## Next steps (ranked)

1. Item 5.1–5.3: elevate C1 → C2 → C3 (the last ~21 target nodes).
2. Item 5.4: G-S1 gate close-out + sketch fold-in + `aism-8dsp` close.
3. `aism-dm8n` (MAIN P0 defs, USER decision) — independent, any time.
4. `aism-9kmt` report sync (P2, now larger).
5. Parallel-af decision (user pending) + `aism-2kyc` unblocker.

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 127.
- Any claim the G-S1 gate is discharged — rows 11–13 (C1–C3) are
  seeded but NOT elevated; the three producers are not yet T0.
- Any registry content beyond the ratified 13 rows — zero new defs,
  zero new contracts; the B0i cap amendment (15→20) is the only
  ratified budget deviation, scoped to that row.
- The v39 sketch fold-in for this session's banks (deliberately
  deferred to the G-S1-discharge session, item 7.3).
- Route X / XE decider work (fallback only); signed trunk PAUSED.
