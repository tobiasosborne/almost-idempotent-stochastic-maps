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
   **`docs/plans/2026-07-27-W78-ratification-package.md`** (D1–D4). The
   live campaign bead is **`aism-kqeb` (W80)**; the Stage-1 rebuild
   tracker is **`aism-e1qs`**. The proof sketch is
   `docs/plans/CURRENT.md` → **v38**.
3. **Rigorous (af-validated, T0): 101.** Registry: 295. Definitions: 45.
   `op-classical` OPEN.
4. **SESSION-33 HEADLINE — the binder-defect arc, start to finish:**
   - Banked 13g (107th) in the morning; by evening SIX Stage-1 af
     validations were RETRACTED (the repo's first retractions): the
     group-laws parent (95th), smooth-unitary-operations (100th),
     inversion-derivative-control (97th), and transports 13c (104th),
     13f (106th), 13g (107th). One defect class throughout: attaching an
     anaphorically-bound map from an opaque contract to a typed datum
     without a typed preimage witness. ALL SIX CONTRACTS UNDISPUTED.
   - Chain of custody: 13e repair design (user delegated `aism-b5hz`,
     option C) → hostile audit raised the first allegation → per-locus
     adjudication confirmed (control + 13g) → second allegation wave →
     **comprehensive sweep over all 18 remaining Stage-1 T0 exports**
     (`SWEEP-ADJUDICATION-STAGE1.md`): 4 more DEFECTIVE, **FOURTEEN
     CERTIFIED SOUND (the entire typed backbone survives)**, cascade
     CLOSED (linker-verified). Both LEARNINGS entries of 2026-07-28 carry
     the loci and root cause; report shards 47–51 demote the six
     statements to conjecture envs with the defects marked in-text;
     workspaces/ledgers retained.
   - **The W97 rebuild design is COMPLETE and hostile-endorsed
     (final audit VERDICT: LAND).** Package =
     `DESIGN-13E-BINDER-v3.md` as amended by `DESIGN-13E-BINDER-v3.1.md`
     §2 (MINOR-5 row) and `DESIGN-13E-BINDER-v3.2.md` (the binder-closed
     smooth-bridge contract, token-diff-verified). Audits: v3 (ZERO
     mathematical findings — bridges, control, 13e, 13f, 13g all
     endorsed; 298-node linker simulation green), v3.1 (satisfiability
     model at eps_r=0; one quantifier-closure finding), v3.2 (LAND, no
     findings). All in `docs/plans/2026-07-28-13E-BINDER-design/`.
5. **Two BINDING process laws (LEARNINGS 2026-07-28, apply to ALL future
   elevations incl. MAIN/ledger/f0-assembly):** (i) every definite
   description a proof root binds must have a provider external that
   supplies the TYPED WITNESS (displayed source/formula/target +
   inverse/preimage identity), never a same-named conclusion; (ii) a
   parameterized proof fixes provider witnesses FIRST and transports
   receiving fields by monotonicity — never treat an unbounded receiving
   coefficient as a universal constant.
6. **NEXT SESSION STARTS HERE — execute the endorsed rebuild:**
   1. ~~Land the registry package~~ **DONE 2026-07-28 (session 34,
      wave W98):** the 11-shard package landed in 3 atomic gated
      commits (`e6648a55` 3 NEW bridges + UNWIRED whitelist;
      `58f38c8c` control/13e/13f/13g deps-only; `feb0efd9` rows-14+
      deps-only). Contracts/defs byte-diff-verified against the design
      at landing (v3.2 text for the smooth bridge); PROVENANCE hashes
      refreshed; `check-all` OK after each stage. All touched shards
      remain `stated` — no rigour claim.
   2. **Serial elevation queue — START HERE** (design §2 order; caps < 26; per-target
      external lists as tabulated; the two retired parents do NOT
      re-elevate): bridges → smooth bridge → control → 13e → **13c
      in-ledger repair** (verifier revokes 1.3.3 + the closure chain,
      orchestrator archives 1.3.3 only after revocation, DISTINCT fresh
      codex per re-accepted node per audit-v3 finding 4) → 13f → 13g.
      Honest budget ~107 codex jobs (fresh-per-node); tier routine;
      bank each per the verified sequence (item 7).
   3. Then **row 13** (`lem-stage1-polar-constant-ledger`, consumes all
      seven transports), maximal-simplex, the 5 downstream rows, G-S1,
      MAIN, the 14-row ledger, k-ledger, f0-assembly, root rewire LAST.
7. **Banking sequence (verified ~18×):** af export (md+tex) → per-id
   oracle appended to `.frontier/portfolio.json` (absolute paths; the
   oracle reads the claim on STDIN) → `fr verify proofs/<rid>/export.md
   --oracle af-<rid>` → mechanical shard flip → regenerate
   (`argument.py --generate`, `gen-report-dag.py`,
   `gen-report-stats.py --extract`) → check-all → `fr log FH banked
   --artifact <export> --tier T0` (bank gate accepts `banked` ONLY for
   oracle-verified artifacts) → commit → next seed in the same window.
8. **Orchestration laws (BINDING):** af runs strictly sequential; no
   design/audit codex job while an af run is live; non-`.frontier/` repo
   writes abort live runs as PROVER-OVERREACH (`.frontier/` exempt);
   fr/bd writes FIRST, commit, launch LAST; commits only in
   zero-live-run windows; `git push` allowed while a run is live.
   Codex = `gpt-5.6-sol`, xhigh cap (prover xhigh ONLY after a STUCK).
9. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at
   close). All work committed AND pushed. NOTHING is in flight (the user
   requested a graceful stop; the final audit was harvested before
   close).

## Next steps (ranked)

1. Execute the endorsed rebuild per item 6 (landing, then the 8-step
   elevation queue) — everything needed is in
   `docs/plans/2026-07-28-13E-BINDER-design/` and bead `aism-e1qs`.
2. After the queue: row 13 and the v36-sketch serial order.
3. Report follow-ups tied to the queue: on each re-validation, restore
   the demoted conjecture envs in shards 47–51 to lemma envs (mechanical
   reversal of the retraction edits) and re-anchor the 3 NEW bridge rows
   (delete their UNWIRED lines).
4. Sketch v39 fold-in after the queue lands (v38 already carries the
   full retraction map; the design-LAND is recorded in fr/worklog).
5. Carried housekeeping: `aism-j5t9` (Munkres def external);
   polar-retraction 29-node REFACTOR warning (cosmetic);
   `def-stage1-polar-witness-data` `\rm` typeset flag; report/*.aux
   policy; repo-root-relative oracle paths; 12 dormant signed-trunk
   draft defs; `aism-ur9` (dormant); two stale pre-session-33 agent
   worktrees under `.claude/worktrees/` (agent-a745…, agent-ad79… —
   verify merged/stale before removing).

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 101 covers the Route-F
  row chain, the fourteen sweep-certified Stage-1 trees (incl.
  transports 13a/13b/13d), and everything outside Stage-1. The six
  retracted results, 13e, row 13 and everything downstream remain
  non-rigorous until the endorsed queue validates them.
- Any claim the rebuild WILL validate — the design is hostile-endorsed,
  but "the derivations replay against the typed binder" is tested only
  by the elevation queue itself.
- The two retired parents (`lem-stage1-approximate-group-laws`,
  `lem-stage1-smooth-unitary-operations`) re-elevating — the endorsed
  design leaves them as honest stated conjectures; their live content
  re-enters via 13e and the explicit smooth bridge.
- Route X / XE decider work (fallback only). Signed trunk PAUSED.
