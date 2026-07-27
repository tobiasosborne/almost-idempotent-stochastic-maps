<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read **`docs/plans/2026-07-27-W78-ratification-package.md`** — the
   consolidated USER RATIFICATION package that now gates ALL further
   critical-path work (bead `aism-gzp9`, W79). The risk register
   (`docs/plans/2026-07-26-critical-path-risk-register.md`) carries the
   dated session-30 close state. The proof sketch remains
   `docs/plans/CURRENT.md` → v34 (sessions 29–30 produced design/audit
   artifacts only; no registry or sketch change — reconciliation debt: none).
3. **Rigorous (af-validated, T0): 83.** Registry: 265. UNCHANGED across
   sessions 29–30. NOTHING was landed, seeded, rewired, or promoted.
   `op-classical` is OPEN.
4. **Session-30 headline: the de-risk campaign is COMPLETE — all four
   risk-register fronts are designed and fresh-hostile-audited to a
   landable state.** 19 codex jobs this session (11 hostile audits, 7
   prescribed repairs, 1 design; gpt-5.6-sol, xhigh for audits/designs,
   high for prescribed repairs), on top of session 29's 8. **ZERO
   route-level findings across the entire campaign** — no
   dimension-dependent constant, no error in Kitaev's theorems, no
   unclosable gap. Every defect found was in OUR contract factoring and
   every one has an audited repair. The landable designs:
   - **Front 1 — S1-POLAR:** `DESIGN-S1-POLAR-v6.md` (13 core rows + 7
     parameterized transport helpers 13a–g + 6 downstream repairs + 2
     datum-only defs). `AUDIT-S1-POLAR-v6.md` = **LAND** (one documentary
     correction). Seven hostile stages; notable: the v5 audit caught a
     PRE-EXISTING producer-domain quantifier defect (rows 6–8 quantified
     over every exact-unit algebra while their graph/polar producers are
     finite-dimensional) that four earlier audits had accepted — repaired
     by coherent finite-dimensional closure (audit-v5 §6 option 1; all
     Route-F consumers live on ℂⁿ).
   - **Front 2 — MAIN-STRUCTURE:** `DESIGN-MAIN-STRUCTURE-v5.md` (P0
     definition gate with 4 schema-complete datum shards; M01–M18; G-S1;
     call envelopes M19-S1/S2/S3 + invariant row M19-R; M20–M28).
     `AUDIT-MAIN-STRUCTURE-v5.md` = **REPAIR-CONFIRMED**. Six hostile
     stages; includes an auditor-constructed M₄ counterexample that
     killed the non-unital Stage-1 hypothesis (now excluded by the
     restored unit clause — verified).
   - **Front 3 — LEDGER-DOMAINS:** `DESIGN-LEDGER-DOMAINS-v2.md`
     unchanged; fresh re-audit `AUDIT-LEDGER-DOMAINS-v2.md` = **LAND-14**
     with two exact corrections (ρ_id^corr adds the ρ_θ entry; one
     wording fix). Black-box `lem-thmainext-conditional` consumption
     survived independent attack (no reset-package hypothesis; K
     non-circular).
   - **Front 4 — F0 assembly:** `DESIGN-F0-ASSEMBLY.md` +
     `AUDIT-F0-ASSEMBLY.md` = **LAND** with four corrections. Every seam
     K-ledger → F2 → F3 → PRH → op-classical recomputed as EXACT MATCH
     (single K; single η_K = min{ρ_fac,(24K)⁻¹,1}; C = K+4√(2K);
     dimension-free; both directions of ‖Φ²−Φ‖_cb = ‖Q²−Q‖_∞→∞ verified).
     Key honest catches: the corrected `lem-routef-k-ledger` is a
     STRENGTHENED REPLACEMENT (new parent proof obligation, not a binder
     edit); the `op-classical` sharpness parenthetical forces a root
     decision (D1); F2/F3 are proved-mod-audit (af: none), an elevation
     gate; OR-route root wiring confirmed representable in the schema.
5. **The ONE remaining design gap on the critical path:** the three
   Stage-1 split producers (G-S1 contents:
   `lem-stage1-rectified-nontrivial-projection`,
   `lem-stage1-original-complementary-pair`,
   `lem-stage1-fresh-two-point-inclusion`) — deliberately sequenced
   behind the polar landing (package §5 step 3); their polar
   prerequisites now exist in v6.
6. **fr state:** FH heavily exploited this session (all harvests logged,
   T1 audit artifacts); breaker healthy — every wave produced a genuine
   frontier reduction. User override stands: critical-path work only;
   Route X/XE fallback untouched; signed trunk PAUSED.
7. Standing mandates (unchanged): codex = `gpt-5.6-sol`, effort capped
   `xhigh` (high for routine/prescribed repairs); batched verification
   default; ratification-queue delegation verbatim-only; NOTHING lands
   without the user.
8. Orchestration laws (unchanged + session-30 confirmations): af runs
   strictly sequential per checkout; pre-create dirs for codex writers;
   commits only in zero-live-run windows; parallel NON-af codex jobs 3-wide
   is safe; prescribed narrow repairs at effort `high` are fast and
   reliable (4 of 4 executed exactly this session).
9. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at close).

## Next steps (ranked)

1. **W79 (`aism-gzp9`) — USER DECISIONS D1–D4** from the ratification
   package §3: D1 the `op-classical` sharpness split (option A
   upper-bound-only + OR-routes, audit-recommended, vs option B compound +
   `ex-hume` unconditional dep + its elevation); D2 ratify the six
   datum-only def shards; D3 UCP definition vs L2 textbook exemption;
   D4 authorize the strengthened `lem-routef-k-ledger` replacement and
   its guard-release point. NOTHING proceeds without these.
2. **W80 (`aism-kqeb`, blocked on W79) — the landing/elevation campaign**
   per package §5: corrections folded verbatim → quick wins (two F0 lift
   rows + F2/F3 elevations) → polar front → the Stage-1 split-producer
   design round → MAIN front → ledger front (decoupled, parallelizable) →
   strengthened k-ledger (fresh prover + verifier) → f0-assembly →
   root rewire LAST.
3. Carried housekeeping: `aism-j5t9` (Munkres C^r-triangulation definition
   external, then finite-triangulation re-run); report/*.aux policy;
   repo-root-relative oracle paths; 12 dormant signed-trunk draft defs;
   `aism-ur9` (W60 route fork, dormant while Route F leads).

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN; T0 = 83; nothing moved in
  sessions 29–30 (design/audit artifacts only, all NON-RIGOROUS by their
  own headers).
- Any promise the landing/elevation campaign is mechanical — the
  strengthened k-ledger is a genuine new proof obligation; the Stage-1
  split producers still need their design round; af elevation can balloon
  (see the parked finite-triangulation run).
- Route X / XE decider work (user-voided; fallback only). Signed trunk
  stays PAUSED.
