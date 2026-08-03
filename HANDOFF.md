<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v45** (current).
3. **Rigorous (af-validated, T0): 168.** Registry: **364** (was 348).
   `op-classical` OPEN.
4. **SESSION-42 RECORD (2026-08-03) — one blocker LOCATED, one front LANDED.
   T0 did not move, and that is the honest result: no mathematics was
   proved this session.**

   **(a) The thmainext elevation is BLOCKED — a contract-level finding.**
   `lem-thmainext-conditional` looked elevation-ready (all 7 deps and all
   120 ancestors T0, workspace an unseeded scaffold). A fresh-codex design
   round produced a nine-node skeleton; a SEPARATE fresh hostile audit
   returned **DESIGN-REJECTED**
   (`docs/plans/2026-08-03-THMAINEXT-ELEVATION-design/`).
   - **Settled affirmatively (Q-A):** there is NO hidden eighth premise.
     M28 consumed as one validated `af` external DOES close the
     ledger-datum existential (its contract binds `W` as "supplied by" the
     ledger theorem and closes by asserting its projections are finite
     positive universal witnesses; `af` externals are usable without
     re-deriving their proof deps). A search of every
     `proofs/*/externals/*.json` carrying the `"Fix ... W supplied by ..."`
     phrase found no contrary precedent. So
     `lem-maincb-reset-constant-ledger` does NOT belong on the deps line,
     the ratified `C_E := W.c0_cb*W.K_call` / `epsilon_E := W.epsilon_MAIN`
     choice stands, and the `DESIGN-THMAINEXT-REWIRE` §3 flag is
     discharged.
   - **The blocker:** the frozen contract's clause *"the assembly USES the
     corrected squared COL-HILB estimate and the hostile-verified H-CB,
     EXT-CB, and Stage-1 reset packets"* is **not dischargeable from the
     seven frozen T0 deps**. M28 exports only `W.epsilon_MAIN`, the final
     `B,v` and their estimates — **no trace of its own construction** — and
     no frozen contract supplies `W.epsilon_MAIN <= e_H` or `<= e_ext`. So
     every packet branch can prove only a conditional interface, and all
     six fail the semantic deletion test. Secondary: the M03 branch never
     identifies its output with M19-R's `v_R`. Mechanical: the seed omitted
     base `def-epsilon-cstar-algebra`.
   - Attacks that PASSED: one `W` bound before the receiving constants; the
     final `v` is M28's own typed witness; squared COL estimate and
     conditional H-CB inverse clauses intact; `rho+epsilon <= a_merge`;
     constants exactly M28's field expressions, un-shrunk. **That last pass
     forecloses the illicit repair** of hiding the missing threshold
     compatibility inside a smaller `epsilon_E`.
   - **USER DECISION PENDING — bead `aism-g83q`.** Options: **(A)** a new
     packet-trace bridge lemma + ratify adding it to the frozen deps line,
     then redesign (cost risk: may need MAIN to export construction data it
     does not, which `DESIGN-MAINCB-REPAIR-v2`'s hand-off clause forbids);
     **(B)** re-scope the frozen contract to its existential content, which
     M28 already discharges, treating the method clause as documentary
     provenance (the auditor judged this "would weaken the target" but
     could not determine whether a verifier reads it as prose or as a
     proposition); **(C)** park it. **User chose (C) in-session on
     2026-08-03**; A-vs-B remains open.

   **(b) The LEDGER-DOMAINS front LANDED — 16 rows, registry 348 → 364.**
   The LAND-14 package had been hostile-audited (`AUDIT-LEDGER-DOMAINS-v2.md`)
   and W78-ratified since July but never transcribed. Landed by script
   (`scripts/land-ledger-domains-rows.py`, retained) with contracts
   flattened LaTeX → registry ASCII per the `a7ab84c7` precedent: 14
   reserved rows + the D2/D3 degree-row reconnections (dep lists from
   design §6.1). **Both audit corrections folded in verbatim** —
   `rho_id^corr := min{rho_theta, rho_AI, epsilon_E/C_A}` (the `rho_theta`
   entry exposes the `eta < 1/4` domain of `lem-kitaev-almost-idemp-audit`),
   and the unit-defect wording. **All 16 rows are `status: stated` /
   `af: none` — NOTHING promoted.**
   - **Independently verified:** a fresh transcription auditor returned
     **TRANSCRIPTION-CONFIRMED-WITH-CORRECTIONS with ZERO substantive
     findings** (`AUDIT-LEDGER-LANDING-TRANSCRIPTION.md`) — no symbol drift
     in any of the 16 contracts, defs/deps matching in membership AND
     order, correction scoping right, bodies inventing nothing. Its 8
     prescribed fixes were editorial provenance-locus typos **inherited
     from the ratified design's own table**; applied verbatim to both the
     shards and the generating script.
   - The `lem-routef-k-ledger` parent rewire (design §6.2) was deliberately
     NOT done; its **DO-NOT-REWIRE guard stays on** (W78 §5 step 6).

5. **NEXT SESSION STARTS HERE:**
   1. **The ledger elevation queue** (bead `aism-3fjg`) — serial, design
      §D-order, per-row node budgets in the design §2 "projected af"
      column. **Split by the status cap:** rows 6, D2, 7, D3, 8–13 do NOT
      import `lem-thmainext-conditional` and are **elevatable now**; rows
      1–5 and 14 DO import it and cannot reach `af: validated` until it is
      T0 (linker status propagation), so they wait on `aism-g83q`.
   2. **The F0-assembly landing** — `DESIGN-F0-ASSEMBLY.md` (audit **LAND**,
      four corrections, W78-ratified D4) is still untranscribed:
      `lem-routef-f0-assembly` and the **strengthened `lem-routef-k-ledger`
      replacement contract**. Note this REPLACES a landed contract and
      releases the DO-NOT-REWIRE guard — W78 §5 step 6 sequences it here,
      and it needs its own fresh prover + fresh hostile verifier.
   3. `aism-g83q` — the thmainext A-vs-B decision, whenever you want it.
   4. `aism-9kmt` report sync (P2, LARGE — unanchored banks ~120–177, plus
      the 16 new ledger ids now whitelisted in `report/UNWIRED.md`).

6. **Worked patterns (BINDING; follow verbatim):**
   - **Pre-launch checks:** workspace root string == the RATIFIED design
     contract text (not merely == the shard); def_added names UNIQUE in
     the ledger (`af def-add` does NOT reject duplicates — it assigns fresh
     ids and pollutes the seed; wipe + re-seed if polluted).
   - **Provision the PROOF's vocabulary, not the contract's** (M19-S3 and
     M28, demonstrated twice; the thmainext design also omitted base
     `def-epsilon-cstar-algebra`): add the per-node import lists from the
     design skeleton at seeding time. Reuse the byte-verbatim
     `GT-kitaev-def-delta-homomorphism` registration from
     `proofs/lem-maincb-extended-inclusion-monotone/externals/` wherever
     δ-homomorphism arithmetic appears.
   - Elevation guidance that produced 8 first-pass banks: constant-choice /
     binder FIRST child; one fixed W threaded (same-map law); NO
     pending-sibling citations; explicit typing citations at point of use;
     NO reset provider unless the row genuinely resets.
   - **Design rounds:** commission with an explicit brief; ALWAYS follow
     with a SEPARATE fresh hostile audit told that finding a gap is a BIG
     SUCCESS. The orchestrator judges neither. Give the auditor a
     deletion test for decorative dep branches — that is what caught the
     thmainext method clause.
   - **Landings the orchestrator transcribes** get a fresh independent
     transcription audit (reviewer ≠ author, Rule 3 / L5). Retain the
     generating script and apply corrections to it too, so a re-run
     reproduces the corrected state.
   - Launch: worktree per run (`git worktree add --detach
     .claude/worktrees/af-<row> HEAD`), orchestrator from INSIDE the
     worktree, ONE backgrounded call, tier routine, workers 4, node-cap =
     the row's (amended) hard cap.
   - Balloon/stuck: read the orchestrator's classification; missing
     vocabulary ⇒ provision + clean re-seed; transparent repair growth ⇒
     scoped cap amendment (flag it; ceiling 26); "converging, hit
     max-rounds" ⇒ resume `--phase verify` on the SAME tree (no rebuild);
     contract-level finding ⇒ STOP, escalate.
   - Bank: serial in main (rsync back → export → oracle → `fr verify`
     export.md → flip → regenerate → check-all → fr log → commit → push).
     **`fr log banked` REQUIRES an oracle-verified artifact** — it
     correctly refused a registry landing this session; landings and
     design/audit harvests log as `progress`.

7. **A NEW CLASS OF OBSTRUCTION is now on the map (sketch v45 §2).**
   A **contract that asserts its own provenance**. The thmainext method
   clause names hostile-verified packets and reads like a W74F
   transcription artifact, but once frozen into a `contract:` the linker's
   contract-match law makes it a proof obligation like any other —
   invisible until an elevation is attempted. **Worth a sweep of the
   remaining un-elevated rows before their design rounds are
   commissioned.**

8. **Open beads:** `aism-g83q` (P1, the thmainext A-vs-B decision;
   `aism-ixtc` is blocked on it), `aism-3fjg` (P1, ledger elevation queue),
   `aism-wazy` (P1, duplicate-contract tripwire suggestion), `aism-9kmt`
   (P2, report sync), `aism-xjnc` (P3, `docs/plans/CHANGELOG.md` stale
   since v31 — decide backfill vs explicit retirement). Carried P1 items
   unchanged (typeset flags, polar-retraction REFACTOR warning, dormant
   signed-trunk defs, lit-DB).

9. **Orchestration laws (BINDING):** parallel worktree orchestrations ≤5
   concurrent, serial banking; no design/audit codex while ANY af run is
   live; fr/bd writes FIRST, commit, launch LAST; codex = `gpt-5.6-sol`,
   xhigh cap (designs/audits xhigh or high; elevations tier routine). A
   verifier finding needing a CONTRACT/DEF change returns to design/user.

10. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at close).
    All work committed AND pushed. **NOTHING is in flight.**

## Next steps (ranked)

1. The ledger elevation queue, thmainext-free subtree first (rows 6, D2, 7,
   D3, 8–13) — `aism-3fjg`.
2. The F0-assembly landing + the strengthened `lem-routef-k-ledger`
   replacement (W78 §5 step 6; releases the DO-NOT-REWIRE guard).
3. `aism-g83q` — the thmainext A-vs-B decision, then its redesign.
4. `aism-9kmt` report sync (P2, large).
5. The `aism-wazy` tripwire: a linker check that no two registry rows share
   a byte-identical contract.

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. **T0 = 168, unchanged this
  session.** The 16 landed ledger rows are `stated`: transcriptions, not
  proofs. The MAIN subtree being complete is a STRUCTURAL milestone inside
  Route F, not the theorem.
- Any rigour claim for the ledger landing. It was verified as a faithful
  *transcription* by an independent agent — that is a provenance fact, not
  a mathematical one.
- Any resolution of the thmainext method-clause blocker: options A and B
  are both open and both need user ratification.
- The `lem-routef-k-ledger` parent rewire (guard still on).
- The report anchoring of banks ~120–177 and the 16 new ledger ids
  (carried as `aism-9kmt`).
- Route X / XE decider work (fallback only); signed trunk PAUSED.
