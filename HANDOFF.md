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
   **`docs/plans/2026-07-27-W78-ratification-package.md`** — the user
   ratified ALL FOUR decisions D1–D4 in-chat 2026-07-27 ("proceed as you
   recommend on all decisions D1-4"), recorded on closed bead `aism-gzp9`.
   The live campaign bead is **`aism-kqeb` (W80)** — the landing/elevation
   campaign per the package's §5 serial order. The proof sketch is
   `docs/plans/CURRENT.md` → v34; NOTE: the W80 landings (7 defs, 2 new T0
   rows, the op-classical contract split) are not yet reconciled into a
   v35 — that is OPEN Rule-9 debt for the next session (small: the map
   changed by exactly the §D-seam items below).
3. **Rigorous (af-validated, T0): 85.** Registry: 267 (two new F0 seam
   rows). Definitions: 45 (seven landed this session). `op-classical` OPEN.
4. **Session-30 arc (one session, three phases):**
   (a) **De-risk campaign COMPLETE** — all four risk-register fronts
   designed + fresh-hostile-audited to landable: polar
   `DESIGN-S1-POLAR-v6.md` (LAND), MAIN `DESIGN-MAIN-STRUCTURE-v5.md`
   (REPAIR-CONFIRMED), ledger `DESIGN-LEDGER-DOMAINS-v2.md` (LAND-14 + 2
   corrections), F0 `DESIGN-F0-ASSEMBLY.md` (LAND + 4 corrections). Zero
   route-level findings in ~13 hostile audits.
   (b) **D1–D4 executed:** op-classical contract split to upper-bound-only
   (option A; sharpness via ex-hume; future OR-route wiring recorded in the
   shard body, applied only at the campaign's LAST step); 7 def shards
   landed (def-operator-space CITED byte-verified; def-maincb-{reset-state,
   raw-call,partition-state}; def-approximate-unitary-space;
   def-stage1-polar-witness-data; def-ucp-map); both F0 seam rows landed
   with audit corrections.
   (c) **Elevation campaign started: 2 banked, 1 in design-repair.**
   `lem-routef-f0-ucp-lift` af-VALIDATED (84th; 9/9; incl. a GENUINE
   real-vs-complex typing challenge caught by the af verifier — survived
   two hostile audits of the design — repaired by recorded contract
   amendment on both seam rows). `lem-routef-f0-defect-identity`
   af-VALIDATED (85th; 12/12 first-pass, zero challenges). Both
   oracle-registered + fr-verified + banked. **The stochastic↔Kitaev
   interface of Route F is rigorous in-repo.**
5. **F2 = the live workfront (NEXT SESSION STARTS HERE).**
   `lem-routef-f2-positive-unital-compression` elevation ABORTED [STUCK]
   with a clean tripwire classification (read the abort block in the last
   run log via `proofs/lem-routef-f2-positive-unital-compression/ledger/`
   challenges): (i) the SAME real-vs-complex typing defect family as F0,
   in F2's LANDED hostile-endorsed contract (ch-2163ee19860aa3d7); (ii)
   MISSING provisionable facts — fd-commutative-C*-classification
   (byte-matchable anchor: projection basis,
   `approximate_algebras.tex:1361-1363`; `def-projection-basis` locked) and
   UCP complete contractivity; (iii) two cross-sibling DAG defects + an
   ε-scoping leak. 11/30 nodes validated; workspace retained. A fresh
   design job per **`docs/plans/2026-07-27-F2-TYPING-design/BRIEF-F2-TYPING.md`**
   was dispatched and then STOPPED for the session wind-up (no deliverable
   yet). **Next agent: re-dispatch that brief verbatim** (one codex exec at
   effort high, deliverable DESIGN-F2-TYPING.md), then a fresh hostile
   check, then land the corrected contract verbatim, re-seed, re-elevate.
   PROCESS GUARD (recorded in the fr log and a commit): do NOT hand-edit
   the F2 contract — an attempt was self-caught as an author-role
   violation and reverted; the design→audit→verbatim-landing path is
   mandatory.
6. **After F2:** F3 elevation (contract is real-space only, no typing
   issue expected), then the polar front per `DESIGN-S1-POLAR-v6.md` §9
   (defs are already landed; rows 1–12 → helpers 13a–g → ledger row 13 →
   6 downstream), then the Stage-1 split-producer design round (the ONE
   remaining critical-path design gap), then MAIN per
   `DESIGN-MAIN-STRUCTURE-v5.md` §10, then the ledger 14-row campaign
   (decoupled), then the strengthened k-ledger (D4: a NEW proof
   obligation, fresh prover + fresh hostile verifier; DO-NOT-REWIRE guard
   released ONLY at package §5 step 6), then f0-assembly, then the root
   rewire LAST.
7. **Orchestration laws (BINDING; session-30 additions in bold):**
   af runs strictly sequential; pre-create dirs; commits only in
   zero-live-run windows; **no fr/bd writes in a turn AFTER an af launch —
   log + commit FIRST, launch as the turn's LAST action** (a mid-run
   fr-log append aborts the run as PROVER-OVERREACH false positive; banked
   to bd memory); **the banking sequence that works: af export (md+tex) →
   register per-id oracle in .frontier/portfolio.json → fr verify with the
   export PATH as the claim → flip shard (mechanical) → regenerate
   (argument.py --generate + gen-report-dag + gen-report-stats --extract)
   → check-all → fr log banked --artifact <export path> --tier T0 →
   commit.** Routine tier sufficed for both F0 rows.
8. Standing mandates: codex = `gpt-5.6-sol`, xhigh cap (high for
   routine/prescribed); batched verification default; NOTHING lands
   without ratification (D1–D4 are the ratified envelope; anything beyond
   escalates); Route X/XE fallback only; signed trunk PAUSED.
9. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at close).

## Next steps (ranked)

1. **Re-dispatch the F2 typing design job** (brief committed at
   `docs/plans/2026-07-27-F2-TYPING-design/BRIEF-F2-TYPING.md`) → fresh
   hostile check → land corrected contract verbatim → re-seed → re-elevate
   (provision the projection-basis byte-matched external per the design's
   §2 verdict; consider the registry-factoring split if the design
   recommends it).
2. **F3 elevation** (seed + routine tier), completing package §5 step 1.
3. **Sketch v35** (Rule-9 debt: reconcile the D1 contract split, 7 defs,
   2 new T0 rows into the top-down sketch; small delta).
4. **Polar front landing/elevation** per `DESIGN-S1-POLAR-v6.md` §9.
5. Carried housekeeping: `aism-j5t9` (Munkres C^r-triangulation def
   external); report/*.aux policy; repo-root-relative oracle paths; 12
   dormant signed-trunk draft defs; `aism-ur9` (dormant).

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 85 covers the F0 seam
  only; F2/F3, the polar/MAIN/ledger fronts, the strengthened k-ledger,
  and the root assembly all remain non-rigorous.
- Any promise F2's typing correction is trivial — the real/complex
  interface at the A, M output end must keep F3/PRH consumption verbatim;
  that is exactly what the design job must get right and the hostile check
  must verify.
- Route X / XE decider work (fallback only). Signed trunk PAUSED.
