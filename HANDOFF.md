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
   **`docs/plans/2026-07-27-W78-ratification-package.md`** (D1–D4 ratified
   in-chat 2026-07-27, recorded on closed bead `aism-gzp9`). The live
   campaign bead is **`aism-kqeb` (W80)**; the immediate resume bead is
   **`aism-686b`**. The proof sketch is `docs/plans/CURRENT.md` → v35
   (session-31 T0 gains not yet folded into a v36 — SMALL Rule-9 debt: the
   map shape is unchanged, only the T0 counts moved; fold when the polar
   queue finishes).
3. **Rigorous (af-validated, T0): 95.** Registry: 295. Definitions: 45.
   `op-classical` OPEN.
4. **HARD BLOCK: the codex usage limit is exhausted (reset 2026-08-01
   21:18).** ALL codex work — af elevations, design jobs, hostile checks —
   is blocked until then. Nothing was half-consumed; every workspace is in
   a clean state.
5. **Session-31 arc (T0 85 → 95, registry 267 → 295):**
   (a) **Package §5 step 1 COMPLETE:** F2 typing cycle ran end-to-end
   (design `DESIGN-F2-TYPING.md` → hostile `AUDIT-F2-TYPING.md`
   LAND-WITH-CORRECTIONS → verbatim landing → re-seed with the
   projection-basis byte external → elevation).
   `lem-routef-f2-positive-unital-compression` af-VALIDATED (86th; 22/22;
   one genuine η=0 endpoint challenge repaired in-run);
   `lem-routef-f3-retract-defect` af-VALIDATED (87th; 11/11 first-pass,
   zero challenges). **The Route-F row chain F0 seam → F2 → F3 → PRH is
   af-validated end-to-end at row level.**
   (b) **Package §5 step 2 (polar front): LANDING COMPLETE, ELEVATION 6/21
   + 2 bonus rows.** All 26 rows of `DESIGN-S1-POLAR-v6.md` §9 steps 2–27
   landed verbatim (12 analytic + 7 transports 13a–g + row-13 constant
   ledger + maximal-simplex + 5 downstream); a fresh hostile
   flattening-equivalence check (`CHECK-POLAR-FLATTENING.md`) returned
   CLEAN 26/26. Elevated T0: rows 1–5 (88th–92nd: rectified-cstar-control
   17/17 after a max-rounds resume; unitary-graph-control 15/15;
   maurer-cartan-trivialization 15/15; polar-retraction 29/29 — the
   central row, over the 26 soft cap so it carries a linker REFACTOR
   warning; coherence-naturality 10/10), then **the row-6 balloon cycle**:
   `lem-stage1-approximate-group-laws` ballooned (60 nodes) → factoring
   design `DESIGN-S1-GROUP-FACTORING.md` → hostile audit
   LAND-WITH-CORRECTIONS (one proof-body correction, applied) → two
   children landed verbatim + parent deps rewired (contract
   BYTE-UNCHANGED) → `lem-stage1-group-domain-membership` af-VALIDATED
   (93rd; run 2 after a STUCK on prover discipline, repaired by relaying
   the AUDIT's guard-derived smallness fact epsilon_r < 1/6 into the shard
   body) → `lem-stage1-group-closeness` af-VALIDATED (94th; 12/12
   first-pass) → parent af-VALIDATED (95th; 14/14).
   (c) Sketch v35 written (sessions 28-addendum–30 reconciliation);
   def-projection-basis stale-body drift fixed (lock is genuine,
   ratified 2026-07-24, commit b9270ef4).
6. **NEXT SESSION STARTS HERE (after the codex reset): resume the serial
   polar elevation queue at row 7.** `lem-stage1-polar-path-admissibility`
   is SEEDED (round-trip verified, defs registered). Launch:
   `python3 scripts/af-orchestrate.py lem-stage1-polar-path-admissibility
   --tier routine --max-rounds 15` (fr dispatch FIRST, launch as the
   turn's LAST action). Then serially: row 8
   (inversion-derivative-control), rows 9–11 (smooth upgrades), row 12
   (scalar arithmetic), transports 13a–g, row 13 (constant ledger),
   maximal-simplex, the 5 downstream rows. Per-row design budgets are in
   each shard body. Escalate prover to xhigh ONLY after a STUCK; factor
   per a fresh design cycle ONLY after a BALLOON classification (both
   playbooks were exercised this session and work).
7. **Banking sequence (unchanged, verified 10× this session):** af export
   (md+tex) → append per-id oracle to `.frontier/portfolio.json`
   (`af-<rid>` / `scripts/oracles/af-validated.py <rid>` / ledger+shard
   inputs, absolute paths) → `fr verify proofs/<rid>/export.md --oracle
   af-<rid>` → flip shard mechanically (status: proved / af: validated +
   body Status update) → regenerate (`argument.py --generate`,
   `gen-report-dag.py`, `gen-report-stats.py --extract`; also
   `gen-report-defs.py --dag-anchors` if a def body changed) → check-all →
   `fr log FH banked --artifact <export> --tier T0` → commit → seed the
   next row in the same commit window.
8. **Orchestration laws (BINDING):** af runs strictly sequential; no
   design/audit codex job while an af run is live (any repo write aborts
   it as PROVER-OVERREACH); fr/bd writes FIRST, commit, af launch as the
   turn's LAST action; commits only in zero-live-run windows; `git push`
   only (no pull --rebase) while a run is live.
9. **After the polar queue:** package §5 step 3 = the Stage-1
   split-producer design round (G-S1: rectified-nontrivial-projection,
   original-complementary-pair, fresh-two-point-inclusion — the ONE
   remaining critical-path design gap; small; polar prerequisites now T0),
   then MAIN per `DESIGN-MAIN-STRUCTURE-v5.md` §10, then the ledger
   14-row campaign (decoupled), then the strengthened k-ledger (D4 guard
   releases at §5 step 6), then f0-assembly, then the root rewire LAST.
10. Standing mandates: codex = `gpt-5.6-sol`, xhigh cap; batched
    verification default; NOTHING lands without ratification (D1–D4 is
    the envelope); Route X/XE fallback only; signed trunk PAUSED.
10b. **Mathlib/Lean advisory (post-close, user-requested, 2026-07-27;
    Opus subagent, checked vs loogle + mathlib4 docs).** Verdict MAYBE:
    a Lean formalisation is realistic today ONLY for the analytic lower
    half (the T0 F0 seam + rectification / defect-linearization /
    functional-calculus rows — weeks-scale on existing mathlib:
    Matrix.rowStochastic, linfty_opNorm, ApproximatesLinearOn, CFC,
    gcongr/positivity). NOT realistic for the whole campaign: mathlib has
    NO cb-norm/UCP theory (CompletelyBounded = 0 hits), no submanifold /
    quotient-manifold / oriented-manifold API, and the Stage-1 topology
    cluster is entirely absent (no Lefschetz–Hopf, no cup product, no
    triangulability — not even Brouwer). Split ~15–25% reuse / 75–85% new
    library. CONFIRMS the standing policy: af is the rigour rung for this
    campaign; Lean reserved for the stable analytic seam or after mathlib
    grows the missing stacks. Full table in the worklog session-31
    addendum; fr log cycle W82.
11. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at
    close). All work committed AND pushed.

## Next steps (ranked)

1. **`aism-686b`: resume the polar queue at row 7** (blocked until the
   codex reset 2026-08-01 21:18; see item 6 for the exact command and
   discipline).
2. Sketch v36 fold-in of the session-31 T0 gains (small Rule-9 debt; can
   ride with the next landing commit).
3. Polar §9 steps 28–29 (the three separately-designed trace rows +
   corrected `lem-stage1-extra-fixed-class`) — blocked on their own
   audited campaign designs; check `docs/plans/` for the Stage-1
   left-inversion-trace design set before starting.
4. Package §5 step 3 (G-S1 split producers) once rows 1–12 are T0.
5. Carried housekeeping: `aism-j5t9` (Munkres C^r-triangulation def
   external; unblocks lem-topology-finite-triangulation and hence
   lem-stage1-quotient-finite-cw's cap); the 12-node vs NODE_SOFT_CAP=26
   brittleness-prose drift (AUDIT-F2-TYPING correction 2 flagged it for
   separate reconciliation: AGENTS.md:90-91, argument/README.md:80-81);
   polar-retraction 29-node REFACTOR warning (cosmetic; tree is clean);
   report/*.aux policy; repo-root-relative oracle paths; 12 dormant
   signed-trunk draft defs; `aism-ur9` (dormant).

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 95 covers the Route-F
  row chain and polar rows 1–6; polar rows 7–27, G-S1, MAIN, the 14-row
  ledger, the strengthened k-ledger, f0-assembly, and the root rewire all
  remain non-rigorous.
- Any promise the remaining polar rows elevate as smoothly — rows 9/10
  consume Lee externals (byte-match them at seeding, pattern
  GT-lee-2ed-*), and row 13 is an 8-way conjunction assembly.
- Route X / XE decider work (fallback only). Signed trunk PAUSED.
