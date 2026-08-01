<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v42** (current).
3. **Rigorous (af-validated, T0): 156.** Registry: 347. `op-classical` OPEN.
4. **SESSION-39 RECORD (2026-08-01, the aism-jl4g dissolution session):**
   - **FIVE user ratifications** executed the whole design→hostile-audit→
     ratify→land→elevate loop end-to-end five times: (1) the witness-ledger
     + unit-thread package (1 new def, 3 new rows, 17 amended contracts);
     (2) the recorded-field ENV repair (6 contracts; a validated M_2
     countermodel had refuted the pre-ENV M19-S2); (3) the bijectivity
     bridge + typed M17; (4) the monotonicity micro-row; (5) the
     consumer-chain repair (M26/M27 hypothesis restore + the typed-reset
     provider + three demotions).
   - **SIXTEEN bank events, TWELVE net new T0 rows (152nd–168th; 144→156):**
     both session-38 parked blockers (M12, M19-S1) closed; the full M19
     family reached T0 (S3 later demoted, see below); M16, M17, M18, M20
     banked (M18/M20 currently suspended, see below); 6 new bridge/ledger
     rows all T0 (isomorphism-unit, corner-unit-comparison,
     witness-arithmetic, cross-datum-bijectivity, inclusion-monotone,
     reset-output-typing).
   - **THREE latent certificate gaps RETRACTED (docs/LEARNINGS.md
     2026-08-01):** M25, M19-S2, M19-S3 banked certificates used
     inferences underivable from registered premises (audit F1/F5 of
     `AUDIT-CONSUMER-REPAIR.md`); demoted honestly; M19-S2 RE-VALIDATED
     same-day (10/10 first-pass with the explicit monotonicity import).
     The linker's L0 propagation then SUSPENDED M18/M20 — their
     certificates are INTACT, workspaces preserved; they re-flip
     mechanically (flip + fr re-verify) once S2✓(done)+S3 re-bank.
   - Every bank: export → register-oracle → `fr verify` PASS → mechanical
     flip → regenerate → check-all OK → fr log → commit → push.
5. **NEXT SESSION STARTS HERE — finish the re-validations, then the chain:**
   1. **M19-S3 re-validation** (parked ~15-19/24 in
      `proofs/lem-maincb-stage3-call-envelope`, preserved): RE-SEED FRESH
      (the parked tree churned on the corner-envelope export-scope and the
      monotonicity-typing application — architect around: (a) M04 exports
      projections at c0*eps and subordination/complementarity at L0*eps —
      keep the two scales separated from the start; (b) the monotonicity
      row's typing is v:B->A with B a plain fd C*-algebra — apply it only
      to such maps, or derive corner-level monotonicity from the def
      directly; (c) the raw-call record stores the derived output map and
      scale, never the datum). Its re-bank re-flips M18 AND M20
      (mechanical: status/af flip + fr re-verify; both trees untouched).
   2. **M25 re-validation** (parked in
      `proofs/lem-maincb-one-class-extension`): RE-SEED FRESH using the
      typed-reset provider `lem-maincb-reset-output-typing` ALONE for
      every reset step (its conclusion subsumes M19-R's — the
      dual-provider distinct-witness challenge was the killer), with
      explicit induction dependencies (no floating 'inductively
      constructed state' nodes).
   3. **M21 + M23 re-seeds** (deps already wired: witness-arithmetic +
      typed-reset for M21; typed-reset for M23). Then M22, M24.
   4. **M26** (contract now has the restored one-dimensional-images
      hypothesis + the bridge import), then M27, then **M28** — the MAIN
      structural assembly. All contracts ratified and audit-stable.
   5. Then the escalated `lem-thmainext-conditional` rewire (design
      sect-10 step 15), the decoupled campaigns (14-row ledger, k-ledger,
      f0-assembly), root rewire LAST.
6. **Worked patterns (BINDING; follow verbatim):**
   - Provision: `python3 scripts/provision-af-row.py <rid>` + base
     `def-epsilon-cstar-algebra` + vocabulary defs (M25 needed
     `def-extcb-datum`; M21 and the micro-row needed the byte-verbatim
     `GT-kitaev-def-delta-homomorphism` external, tex:443-456 — reuse the
     registration pattern in `proofs/lem-maincb-extended-inclusion-monotone/externals/`).
   - Launch: worktree per run (`git worktree add --detach
     .claude/worktrees/af-<row> HEAD`), orchestrator from INSIDE the
     worktree, ONE backgrounded call, tier routine, workers 4.
   - Balloon/stuck: transparent repair growth ⇒ scoped cap amendment
     (flag it; ceiling = repo cap 26); tangled/stale-premise tree ⇒ clean
     RE-SEED; contract-level finding ⇒ STOP, escalate (exercised FIVE
     times this session; it works).
   - Bank: serial in main (rsync back → export → oracle → verify → flip →
     regenerate → check-all → fr log → commit → push).
   - **Session-39 additions:** deps must list every lemma a contract
     NAMES (the F3-class wiring rule — two waves were lost to it);
     consumers of existential providers must fix ONE witness explicitly
     (the same-map law); design/audit worker prompts carry an explicit
     no-git/no-fr/no-bd prohibition (a designer self-committed once,
     benign, f8920d0a).
7. **Open beads:** `aism-mc54` (P0, claimed) — the re-validation
   completions above are its remaining scope; close it when M19-S3 + M25
   re-bank and M18/M20 re-flip. `aism-jl4g`, `aism-4kof`, `aism-73ur`
   closed this session. Carried P2 items unchanged (aism-9kmt report sync
   — now ~47 unanchored banks; the \rm typeset flags; polar-retraction
   REFACTOR warning; dormant signed-trunk defs; lit-DB items).
8. **Orchestration laws (BINDING):** parallel worktree orchestrations ≤5
   concurrent, serial banking; no design/audit codex while ANY af run is
   live; fr/bd writes FIRST, commit, launch LAST; codex = `gpt-5.6-sol`,
   xhigh cap (designs/audits xhigh or high; elevations tier routine). A
   verifier finding needing a CONTRACT/DEF change returns to design/user.
9. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at close).
   All work committed AND pushed. **NOTHING is in flight.**

## Next steps (ranked)

1. M19-S3 re-seed/re-validate → mechanical M18/M20 re-flips (T0 156→159).
2. M25 re-seed/re-validate (typed-reset provider only, explicit induction).
3. M21, M23 (wired), then M22, M24, M26, M27, M28 — the MAIN capstone.
4. `lem-thmainext-conditional` rewire; then the decoupled campaigns.
5. `aism-9kmt` report sync (P2, large — banks 120–168 unanchored).

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 156 (peak 160 today;
  the delta is honest demotions/suspensions, not lost mathematics: the
  suspended M18/M20 certificates are intact and the retracted-certificate
  CONTRACTS were never refuted).
- Any claim the retracted M25/M19-S2/M19-S3 certificates count — see
  docs/LEARNINGS.md 2026-08-01 (M19-S2 already re-validated cleanly).
- The report anchoring of banks 120–168 (carried as `aism-9kmt`).
- Route X / XE decider work (fallback only); signed trunk PAUSED.
