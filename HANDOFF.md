<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v49** (current).
3. **Rigorous (af-validated, T0): 190.** Registry: **371**. `op-classical` OPEN.
4. **SESSION-45 STATE (2026-08-08, W138, IN PROGRESS): the KLEDGER-STRENGTHENED
   v2 package is LANDED (user-ratified) and the five-stage elevation queue is
   the live work.**
   - Full discipline this session: fresh design → hostile audit **REJECT**
     (1 FATAL cap-budget + 3 HIGH) → fresh v2 design (three first-class
     helper rows; option-(a) pre-forall scalar positivity; 30-item census;
     complete stale-prose manifest) → fresh hostile re-audit **LAND, zero
     corrections** → user ratification (land + elevate) → landing executed,
     gates green. Artifacts: `docs/plans/2026-08-08-KLEDGER-STRENGTHENED/`.
   - Landed rows (all `stated`/`af: none`): the strengthened
     `lem-routef-k-ledger` replacement (18 deps = ratified 15 + 3 helpers;
     W74F paper ledger recorded as superseded history),
     `lem-routef-scalar-header-positivity`, `lem-routef-factor-map-packet`,
     `lem-routef-factor-estimate-packet`, `lem-routef-f0-assembly`.
   - The DO-NOT-REWIRE guard on `lem-routef-k-ledger` is RELEASED. The
     `op-classical` root rewire remains a separate LAST user-ratified step.
   - Eleven stale report loci repaired per the v2 manifest §7.2; UNWIRED
     updated; all generators re-run; `check-all` OK incl. report build.

5. **THE ELEVATION QUEUE (v2 design §8 — BINDING budgets; fresh prover +
   separate fresh verifiers per node; bottom-up; NEVER resume across a
   registry ratification; seed each consumer only at a checkout where its
   producers are banked):**
   1. `lem-routef-scalar-header-positivity` — 4 designed / 3 rounds / cap 14;
      def-adds §5.1 (setting + ucp + extended-epsilon + extended-delta);
      externals: E3 only.
   2. `lem-routef-factor-map-packet` — 5 / 4 rounds / cap 18; externals
      H1, E1–E7 (exact §5.4 order).
   3. `lem-routef-factor-estimate-packet` — 5 / 4 rounds / cap 18; externals
      H1, H2, E8–E12.
   4. strengthened `lem-routef-k-ledger` — 6 / 4 rounds / cap 21; ALL 18
      externals (E1–E15, H1–H3); direct the prover to use the helper
      interfaces without reopening their internals.
   5. `lem-routef-f0-assembly` — 2 / 2 rounds / cap 8; external P.
   External strings: byte-exact dictionary in
   `DESIGN-KLEDGER-STRENGTHENED-V2.md` §§5.2–5.4 (H-strings only after the
   helper is banked). Cap hit ⇒ STOP (balloon/stuck taxonomy per FINDINGS
   2026-08-08); never inflate a cap.

6. **Also in flight (USER P0, bead `aism-aywn`):** the standalone 3–5pp
   paper (`paper/main.tex`, Kitaev-on-faith audience, novel stochastic
   steps). Draft dispatched to fresh codex; needs a separate fresh
   faithfulness audit BEFORE the user sees it. Honest formalisation-status
   remark is mandatory in the draft.

7. **After the queue:** root rewire LAST (separate user ratification; the
   W78 D1 sharpness-split decision governs the root contract). Then
   `aism-9kmt` report sync.

8. **Open beads:** `aism-e30g` (W138, in progress — this campaign),
   `aism-aywn` (P0 paper), `aism-wazy` (P1 tripwire), `aism-9kmt` (P2
   report sync), `aism-xjnc` (P3 CHANGELOG). Carried P1 items unchanged.

9. Gate at last check: `sh scripts/check-all.sh` → `[check-all] OK`.

## Next steps (ranked)

1. Run the five-stage elevation queue (item 5) to T0, banking each stage
   (oracle insert, `fr verify`, mechanical flip, regenerate, gate, commit).
2. Harvest + faithfulness-audit the P0 paper draft; deliver to user.
3. Root rewire LAST (separate user-ratified package).
4. `aism-9kmt` report sync.

## What is intentionally NOT here

- Any claim `op-classical` is proved — **OPEN**. T0 = 190.
- Any promotion by the landing: all five new/replaced rows are
  `stated`/`af: none` until their af trees validate.
- Any `op-classical` root edit (guard released ONLY on the K-ledger row).
