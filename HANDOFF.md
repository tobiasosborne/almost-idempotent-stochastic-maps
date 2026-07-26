<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read **`docs/plans/2026-07-26-critical-path-risk-register.md`** — the ranked
   de-risk ledger that now GOVERNS all work (user mandate 2026-07-26, session
   29: "only one priority: de-risk the critical path, riskiest first"; the
   XE/Route-X decider wave W74 was VOIDED by the user — Route X is fallback
   ONLY, touched only if a critical-path front returns a route-killing gap).
   The proof sketch remains `docs/plans/CURRENT.md` → v34 (unchanged this
   session; session 29 produced design artifacts, no registry/sketch change).
3. **Rigorous (af-validated, T0): 83.** Registry: 265. UNCHANGED this session
   — session 29 was a pure design/audit de-risk campaign; NOTHING was landed,
   seeded, or promoted. All artifacts live in three new dirs under
   `docs/plans/2026-07-26-{S1-POLAR,MAIN-STRUCTURE,LEDGER-DOMAINS}-design/`.
4. **Session-29 headline: one full design→hostile-audit→repair cycle on the
   three riskiest fronts; 8 fresh hostile codex jobs; ZERO route-level
   findings.** No dimension-dependent constant, no error in Kitaev's
   theorems, no unclosable gap. Every defect found was in OUR factoring or in
   Kitaev's unwritten prose steps, and each now has a designed repair:
   - **Front 1 — S1-POLAR** (`aism-cxza`): `DESIGN-S1-POLAR-v2.md` =
     DESIGNED-CLOSABLE. 9 analytic rows + 6 downstream contract repairs. The
     audit's C¹→smooth blocker closes WITHOUT approximation machinery — the
     chart/polar/inversion maps are smooth outright (smooth IFT); no
     fixed-point/index datum changes. Munkres EDT SHA-pinned but not needed.
   - **Front 2 — MAIN-STRUCTURE** (`aism-qum7`): v4.1's eight MAIN rows are
     DEFINITIVELY DEAD AS WRITTEN (five defects confirmed by two independent
     hostile agents — four-corner bijectivity misuse, non-iterable binary
     merge, missing zero-corner transport, threshold omissions, missing
     assembly producers). `DESIGN-MAIN-STRUCTURE-v2.md` = acyclic repair
     (nested-corner comparison, outer-compression transfer, conditional
     equivalence/cross-union, recombination on the complete one-class
     family), with ONE escalated sequencing gate **G-S1**: three Stage-1
     split producers land only after the polar round.
   - **Front 3 — LEDGER-DOMAINS** (`aism-2ehu`): `DESIGN-LEDGER-DOMAINS-v2.md`
     = all 14 withdrawn K-ledger rows close with derived local radii. The
     front is DECOUPLED from the MAIN reset repair: terminal
     η_K = min{ρ_fac, (24K)⁻¹, 1} via the landed `lem-thmainext-conditional`
     contract as black box (audit finding: the originally-claimed terminal
     GAP was overstated).
5. **Three genuine Kitaev prose gaps found, all repaired-by-design** (support
   the L0 re-establishment decision): TeX 906 (straight-path projection lacks
   the right-inverse argument → new path-admissibility row), TeX 883–888
   (printed derivative erratum; corrected form NOT byte-present; unconsumed
   by our rows), TeX 795–807 vs 947–954 (the C¹→smooth jump). Also: the
   audits confirmed Kitaev prints dimension-freeness in his theorem
   statements (TeX 458, th_main/th_main_ext) — our audits verify it survives
   full quantification (so far: everywhere yes).
6. **Strategy truths banked in-chat this session (cite these, do not re-derive):**
   (a) The honest uncharitable framing: op-classical = a corollary of a
   fully-quantified Kitaev + a compact stochastic bridge; ~60-70% of the
   campaign is closing his O(·)s, ~25-35% is proving steps he asserted but
   never wrote, ~10% is genuinely ours and mostly already T0 (PRH, F2/F3,
   equivalence, sharpness). (b) Kitaev NEVER claims almost-implies-near for
   his idempotents — only encoding+decoding (th_almost_idemp gives an
   approximate ALGEBRA; the functional-calculus Φ̃ is exactly idempotent but
   NOT positive; th_main/th_main_ext give an O(ε)-isomorphism). The passage
   to a stochastic almost⇒near is OUR mathematics (F2→F3→PRH), provably not
   a free corollary: ex-hume forces the exponent drop η → √η in the
   stochastic category. (c) vs Salzmann–Bergh–Datta (local ref): no
   implication either way; on the almost-idempotent subclass ours is strictly
   stronger (one E repairs ALL approximate fixed points, evading their
   two-point no-go); their optimality remark is our external √-sharpness
   anchor.
7. **fr breaker state:** FH un-stalled via genuine frontier reductions (the
   design harvests). The frontier now reads the de-risk state. The user
   OVERRIDE stands: critical-path work only.
8. Standing user mandates (unchanged): codex = `gpt-5.6-sol`, effort capped
   `xhigh` (use `high` for routine/prescribed repairs); batched verification
   default; banking precedent; ratification-queue delegation (verbatim only,
   modifications escalate); signed trunk PAUSED.
9. Session-28 orchestration laws still binding (sequential af runs; pre-create
   dirs; commits only in zero-live-run windows). Session-29 addendum: codex
   DESIGN jobs (non-af) ran 3-wide in parallel without incident in
   pre-created dirs; TaskStop after the deliverable write is safe (ANSWER
   summary files are expendable).
10. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at close).

## Next steps (ranked — the W78 plan, bead filed)

1. **Three fresh hostile re-audits** of the v2 designs (GAP-EA two-stage
   pattern; briefs/patterns in the three design dirs — reuse the
   BRIEF-*-AUDIT.md shape against the v2 files). Attack surfaces named in
   `aism-` bead notes: polar = the direct-smoothness claim + self-containment
   fixes; MAIN = nested-corner comparison + outer-compression rows; ledger =
   corrected Υ′ radius composition + the black-box thmainext consumption.
2. **Consolidated USER RATIFICATION package** after audits pass: all new
   rows, the 6 polar downstream contract repairs, MAIN contract corrections
   (v2 explicitly escalates them), def shards (incl.
   `def-approximate-unitary-space`, `def-maincb-reset-state`,
   `def-maincb-raw-call`, `def-operator-space`), and the serial landing
   order. NOTHING lands without the user.
3. **F0 assembly design job** (front #4, the last undesigned risk): the
   op-classical root composition from F2/F3 + K-ledger + PRH; consumes the
   ledger v2 parent wiring proposal; keep `lem-routef-k-ledger`
   DO-NOT-REWIRE guard until ratified.
4. **Landing/elevation campaign** per the ratified order (ledger front is
   decoupled and can run first; MAIN gates on polar via G-S1).
5. Carried housekeeping: `aism-j5t9` (Munkres C^r-triangulation definition
   external, then finite-triangulation re-run); report/*.aux policy;
   repo-root-relative oracle paths; 12 dormant signed-trunk draft defs.

## What is intentionally NOT here

- Any claim `op-classical` is proved — it is OPEN; T0 = 83; nothing moved
  this session (design artifacts only, all NON-RIGOROUS by their own
  headers).
- Any promise the v2 designs survive re-audit — the polar v1 design looked
  CLOSABLE and the audit still returned REDESIGN; expect corrections.
- Route X / XE decider work (VOIDED by user, `aism-ea2f` deferred; fallback
  only). Signed trunk stays PAUSED.
