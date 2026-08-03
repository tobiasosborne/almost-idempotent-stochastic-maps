<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v46** (current).
3. **Rigorous (af-validated, T0): 169.** Registry: **364**. `op-classical` OPEN.
4. **SESSION-42 RECORD (2026-08-03).** Three things landed: a contract-level
   blocker was located and then dissolved by user decision, the LEDGER-DOMAINS
   front was transcribed, and `lem-thmainext-conditional` was banked.

   **(a) `lem-thmainext-conditional` af-VALIDATED — T0 168 → 169.**
   4-node tree, root validated, taint clean, **FIRST PASS, zero challenges**
   (fresh codex prover, separate fresh verifier per node; one verifier
   correctly *blocked* node 1.3 until its children validated). Oracle
   `af-lem-thmainext-conditional` registered, `fr verify` PASS, shard flipped
   mechanically from the codex ledger. Tree: fix M28's ledger datum `W` and
   define `C_E := W.c0_cb*W.K_call`, `epsilon_E := W.epsilon_MAIN` (1.1);
   apply M28 to arbitrary `A, epsilon` and substitute (1.2); unfold
   `def-extended-delta-inclusion` for the all-amplification reading and
   universality (1.3).
   - **HONEST SCOPE — do not let the counter speak for itself.** This proves
     **no mathematics absent from `lem-maincb-structural-assembly`**. The
     hostile auditor was asked outright and answered: mathematically the row
     is *redundant* relative to M28 — a strict weakening with no new analytic
     information; structurally it is a meaningful *interface*, hiding `W`, the
     block form `⊕_C M_{|C|}` and the unit estimate while exposing exactly the
     two constants `lem-routef-k-ledger` consumes. Value = validated interface
     projection + DAG decoupling. What genuinely improved: the Route-F chain
     above MAIN now rests on a **T0** carrier, and blocked count fell 117 → 115.

   **(b) How it got unblocked — the method-clause re-scope (option B,
   USER-RATIFIED).** A design round + separate hostile audit returned
   **DESIGN-REJECTED**: the contract's clause "the assembly *uses* the
   corrected squared COL-HILB estimate and the hostile-verified H-CB, EXT-CB,
   and Stage-1 reset packets" is a claim about a *proof*, not about `A,B,v`,
   and is not dischargeable from the frozen deps (M28 exports no trace of its
   own construction; no frozen contract supplies `W.epsilon_MAIN <= e_H` or
   `<= e_ext`). The user ratified removing it (commit `7b044403`); the
   mathematical content is **byte-unchanged**.
   - **The `deps:` line was deliberately NOT reduced.** Those seven edges are
     the *linker-enforced* form of the same "uses" statement — above all the
     edge to `lem-hcb-column-hilbert-squared`, the corrected squared estimate
     replacing the paper's unsquared display. Prose in a contract enforces
     nothing; a dep edge is checked every gate run. Shard body + provenance
     forbid "simplifying" them to the transitive reduction.
   - The same audit **settled Q-A affirmatively**: no hidden eighth premise —
     M28 as one validated external closes the ledger-datum existential, so
     `lem-maincb-reset-constant-ledger` stays off the deps line.

   **(c) The LEDGER-DOMAINS front LANDED — 16 rows, registry 348 → 364.**
   The LAND-14 package (hostile-audited `AUDIT-LEDGER-DOMAINS-v2.md`,
   W78-ratified since July) transcribed at last, by retained script
   `scripts/land-ledger-domains-rows.py`, contracts flattened LaTeX → registry
   ASCII per the `a7ab84c7` precedent: 14 reserved rows + D2/D3 reconnections
   (dep lists from design §6.1). Both audit corrections folded in verbatim —
   `rho_id^corr := min{rho_theta, rho_AI, epsilon_E/C_A}` (the `rho_theta`
   entry exposes the `eta < 1/4` domain of `lem-kitaev-almost-idemp-audit`)
   and the unit-defect wording. All 16 rows `status: stated` / `af: none`.
   - **Independently verified:** fresh transcription auditor returned
     **TRANSCRIPTION-CONFIRMED-WITH-CORRECTIONS, ZERO substantive findings** —
     no symbol drift, defs/deps matching in membership AND order, correction
     scoping right, bodies inventing nothing. Its 8 fixes were editorial
     provenance-locus typos **inherited from the ratified design's own table**,
     applied to both the shards and the generating script.
   - The `lem-routef-k-ledger` parent rewire was deliberately NOT done; its
     **DO-NOT-REWIRE guard stays on** (W78 §5 step 6).

5. **NEXT SESSION STARTS HERE:**
   1. **The ledger elevation queue** — bead `aism-3fjg`. 16 rows, serial, in
      the design's §D order; per-row node budgets in
      `DESIGN-LEDGER-DOMAINS-v2.md` §2 ("projected af" column: 8/3, 4/2, 3/2,
      4/2, 6/3, 5/3, 5/3 D2, 4/2, 7/3 D3, 11/3, 5/3, 4/2, 4/2, 3/2, 4/2, 5/2).
      **The v45 status cap is GONE** — rows 1–5 and 14 import
      `lem-thmainext-conditional`, which is now T0, so the WHOLE queue is
      elevatable.
   2. **The F0-assembly landing** — `DESIGN-F0-ASSEMBLY.md` (audit **LAND**,
      four corrections, W78-ratified D4) is still untranscribed:
      `lem-routef-f0-assembly` + the **strengthened `lem-routef-k-ledger`
      replacement contract**. This REPLACES a landed contract and releases the
      DO-NOT-REWIRE guard (W78 §5 step 6); needs its own fresh prover + fresh
      hostile verifier.
   3. Then the **root rewire LAST** — unchanged from v41–v46.
   4. `aism-9kmt` report sync (P2, LARGE — unanchored banks ~120–177, plus the
      16 ledger ids and `lem-thmainext-conditional`, all whitelisted in
      `report/UNWIRED.md`).

6. **Worked patterns (BINDING; follow verbatim):**
   - **Pre-launch checks (all four, every launch):** af root node 1 == the
     shard contract under the linker's normalisation **AND** byte-present in
     the RATIFIED design (root == ratified text, not merely == shard);
     registered def names UNIQUE in the ledger (`af def-add` does NOT reject
     duplicates — it assigns fresh ids and pollutes the seed); externals carry
     the literal `proofs/<dep-id>` path.
   - **Provision the PROOF's vocabulary at SEEDING time, not the contract's**
     (M19-S3, M28, and again thmainext v1 which omitted base
     `def-epsilon-cstar-algebra`). Take the per-node import lists from the
     design skeleton. The prover prompt skips already-registered names, so
     pre-provisioning also dodges the duplicate-pollution gotcha.
   - **Registered-but-uncited externals are safe** (verified against the
     scripts: `check-refs` has no citation/use test; `argument.py` never reads
     the workspace external set; `af-orchestrate` directs registration of every
     dep but citation only where used) — **but operationally visible**: they
     tempt tree reinflation. Register all deps, cite only what is used, and
     **prune a revived branch rather than raise the cap**.
   - **Design rounds:** commission with an explicit brief; ALWAYS follow with a
     SEPARATE fresh hostile audit told that finding a gap is a BIG SUCCESS.
     Arm it with a **deletion test** for decorative dep branches (that caught
     the thmainext method clause) and, when a design comes back *small*, aim it
     at **under**-specification instead.
   - **Landings the orchestrator transcribes** get their own fresh independent
     transcription audit (Rule 3 / L5). Retain the generating script and apply
     corrections to it too, so a re-run reproduces the corrected state.
   - Elevation guidance that produced 9 first-pass banks: constant-choice /
     binder FIRST child; one fixed W threaded (same-map law); NO
     pending-sibling citations; explicit typing citations at point of use; NO
     reset provider unless the row genuinely resets.
   - Launch: worktree per run (`git worktree add --detach
     .claude/worktrees/af-<row> HEAD`), orchestrator from INSIDE the worktree,
     ONE backgrounded call, tier routine, workers 4, node-cap = the row's
     (amended) hard cap. Remove the worktree after banking.
   - Balloon/stuck: read the orchestrator's classification; missing vocabulary
     ⇒ provision + clean re-seed; transparent repair growth ⇒ scoped cap
     amendment (flag it; ceiling 26); "converging, hit max-rounds" ⇒ resume
     `--phase verify` on the SAME tree; contract-level finding ⇒ STOP, escalate.
   - Bank: rsync back → export → register oracle → `fr verify` export.md →
     mechanical flip → regenerate (argument INDEX/DAG + report defs/dag/stats)
     → check-all → `fr log banked` → commit → push → remove worktree.
     **`fr log banked` REQUIRES an oracle-verified artifact** — it correctly
     refused a registry landing this session; landings and design/audit
     harvests log as `progress`.
   - **A newly validated row STAYS in `report/UNWIRED.md`** until the paper
     track anchors it; removing the line fails `check-provenance` (tested).

7. **The obstruction class, and its worked remedy (sketch v45 §2, v46 §4).**
   *A contract that asserts its own provenance* — invisible until an elevation
   is attempted, because the linker's contract-match law turns the annotation
   into a proof obligation. **Remedy, now demonstrated end to end:** check
   whether any consumer depends on the narrative clause; if none does, re-scope
   it to `provenance:` and let the `deps:` edges carry it. **A sweep of the
   remaining un-elevated rows for this pattern is still recommended**, and now
   has a cheap disposition for whatever it finds.

8. **Open beads:** `aism-3fjg` (P1, ledger elevation queue), `aism-wazy` (P1,
   duplicate-contract tripwire), `aism-9kmt` (P2, report sync), `aism-xjnc`
   (P3, `docs/plans/CHANGELOG.md` stale since v31 — backfill or retire).
   Carried P1 items unchanged (typeset flags, polar-retraction REFACTOR
   warning, dormant signed-trunk defs, lit-DB). `aism-g83q` and `aism-ixtc`
   CLOSED this session.

9. **Orchestration laws (BINDING):** parallel worktree orchestrations ≤5
   concurrent, serial banking; no design/audit codex while ANY af run is live;
   fr/bd writes FIRST, commit, launch LAST; codex = `gpt-5.6-sol`, xhigh cap
   (designs/audits xhigh or high; elevations tier routine). A verifier finding
   needing a CONTRACT/DEF change returns to design/user.

10. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at close).
    All work committed AND pushed. **NOTHING is in flight.**

## Next steps (ranked)

1. The ledger elevation queue, 16 rows, serial — `aism-3fjg`. No status cap
   remains.
2. The F0-assembly landing + the strengthened `lem-routef-k-ledger` replacement
   (W78 §5 step 6; releases the DO-NOT-REWIRE guard).
3. The root rewire — LAST.
4. `aism-9kmt` report sync (P2, large).
5. The provenance-clause sweep of remaining un-elevated rows (§7).
6. The `aism-wazy` tripwire: a linker check that no two registry rows share a
   byte-identical contract.

## What is intentionally NOT here

- Any claim `op-classical` is proved — **OPEN**. T0 = 169.
- Any claim that T0 168 → 169 was new mathematics. It was not: the row is a
  validated *interface projection* over `lem-maincb-structural-assembly`, and
  it was reachable only because the user ratified re-scoping the contract's
  method clause out.
- Any rigour claim for the 16 landed ledger rows: they are `stated`
  transcriptions, verified as faithful *transcriptions* by an independent
  agent — a provenance fact, not a mathematical one.
- The `lem-routef-k-ledger` parent rewire (guard still on).
- The report anchoring of banks ~120–177, the 16 ledger ids, and
  `lem-thmainext-conditional` (carried as `aism-9kmt`).
- Route X / XE decider work (fallback only); signed trunk PAUSED.
