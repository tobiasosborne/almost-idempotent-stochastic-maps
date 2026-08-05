<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v47** (current).
3. **Rigorous (af-validated, T0): 176.** Registry: **365**. `op-classical` OPEN.
4. **SESSION-43 RECORD (2026-08-05, W136).** One arc, start to finish: the
   LEDGER-DOMAINS elevation queue was opened, its contracts were found
   undischargeable AS WRITTEN by fresh af verifiers, the family was re-scoped
   onto a formation backbone through a full design→audit→ratify→land→
   transcription-audit loop, and SEVEN rows were banked (T0 169 → 176):

   - **`lem-routef-raw-factor-setting-formation`** (T0 170, NEW row,
     registry 365, first pass 10/10) — the family's existence backbone:
     one global witness header `W_RF` first, then per-input datum `S`.
   - **Rows 1–4** (T0 171/172/173/174): `raw-factor-norms` 23/23 (a false
     strict `dim(A)<d^2` claim refuted with an exact counterexample and
     repaired in-tree), `raw-factor-identities` 11/11 first pass,
     `raw-product-estimate` 6/6, `raw-factor-units` 8/8 (unit clause grounded
     in the byte-verbatim `GT-kitaev-def-delta-homomorphism`, tex:443–456 —
     `hom_unit` is definitional).
   - **The Kitaev pair** (T0 175/176): `lem-kitaev-diagonal-repair` 20/20
     (refutes the printed direct-sum diagonal against PROVENANCE-ONLY
     externals tex:1254/2780–2783 AND constructs the phase-balanced diagonal
     with exact projective norm 1) and `cor-kitaev-diagonal-cpization` 22/22
     (centrality-only CP, no multiplicativity).

   **Every bank:** fresh codex prover, separate fresh verifier per node,
   oracle registered (hand-inserted into `.frontier/portfolio.json` — the
   register-oracle.py format guard refuses the current file format; entries
   go before the `af-lem-thmainext-conditional` anchor), external `fr verify`
   PASS, mechanical flip, gates green, committed, pushed.

5. **THE HEADLINE FOR NEXT SESSION: the rows 5–14 status cap is DISSOLVED.**
   With the Kitaev pair T0, every remaining LEDGER-DOMAINS row (5, 6, D2, 7,
   D3, 8–13, revised 14) has a fully rigorous dep cone. Elevate serially in
   the design's §D order under the RE-SCOPED contracts (bead `aism-3fjg`).

6. **The rescope (what changed in the registry, all USER-RATIFIED):**
   - `definitions/def-routef-raw-factor-setting.md` — theorem-free witness
     package (locked; consensus line records two sign-offs: the landing and
     the `I_B` = identity-map type fix).
   - `argument/lemmas/lem-routef-raw-factor-setting-formation.md` — the
     formation row (now T0).
   - All 16 family rows: ambient-binding prefix; suffixes byte-identical to
     the 2026-08-03 landing EXCEPT row 14 (sole revision: scalar threshold
     interface; F2/F3/PRH + def-stochastic + def-positive-approximate-retract
     + thmainext left its imports — their application moves to the future
     strengthened K-ledger). defs: lines drop `def-almost-idempotent`
     (row-stochastic picture), import the setting def (+ `def-ucp-map` where
     CP/UCP is produced); deps: add formation + the audit's direct edges.
   - `scripts/land-ledger-domains-rows.py` v2: re-run reproduces the landed
     17 shards byte-for-byte (verified by the transcription re-audit in a
     clean clone). `cor-kitaev-diagonal-cpization` defs line += def-ucp-map.
   - Full artifact trail: `docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/`
     (v1 design REJECTED — deletion test caught definition-as-theorem
     laundering; v2 LAND-WITH-EXACT-CORRECTIONS; landing transcription
     REJECTED on 5 editorial deviations then CONFIRMED after exact fixes)
     and `docs/plans/2026-08-05-KITAEV-PAIR-ELEVATION/`.

7. **NEXT SESSION, ranked:**
   1. **Ledger rows 5–14, serial, §D order** (`aism-3fjg`). Worked-pattern
      deltas learned this session (BINDING):
      - Fresh builds under the re-scoped contracts run **1.5–3× the old
        projections** (formation-instantiation scaffolding). Pre-amend caps
        and FLAG it (this session: 8→20→24 [row 1 incl. repair], 3→14
        [row 3], 4→10 [rows 2/4]); ceiling 26; a cap hit is stop-and-classify.
      - Provision per workspace: the setting def + `def-ucp-map` + extended
        defs + base vocabulary + `GT-kitaev-def-delta-homomorphism`
        (tex:443–456, the established source-string format) + the validated
        dep externals with literal `proofs/<dep-id>` paths.
      - Rows 5 and D3 also need `cor-kitaev-diagonal-cpization` /
        `lem-kitaev-almost-idemp-audit` externals per their deps lines.
      - NEVER `af def-add` an existing name to update it — duplicates
        pollute and the lookup returns the STALE copy; the remedy is a clean
        re-seed (worked twice this session).
   2. **F0-assembly landing + strengthened `lem-routef-k-ledger`** (releases
      the DO-NOT-REWIRE guard). The rescope audit's blast-radius section is
      BINDING here: the strengthened parent must add
      `lem-routef-raw-factor-setting-formation` AND rows 5/6/8/9 as direct
      deps (the telescopes don't export packet existence); honest budget
      ~17 nodes / 4 rounds / cap 22.
   3. **Root rewire LAST** (unchanged).
   4. `aism-9kmt` report sync (larger now: banks ~120–177 + 7 session banks
      + the formation id; all whitelisted in `report/UNWIRED.md`).

8. **Gotchas recorded this session (FINDINGS.md 2026-08-05):** the sandbox
   path-remap illusion (main paths can resolve to a worktree dir INSIDE the
   sandbox — verify isolation unsandboxed before "fixing" it); the
   ambient-binding under-specification obstruction class + its worked remedy;
   interface projections hiding load-bearing clauses (thmainext hides M28's
   unit estimate — Kitaev's `hom_unit` supplied it definitionally); worker
   discipline (the pair auditor committed AND pushed its own audit file,
   66a9f657 — content verified benign; check `git log` after every codex
   round).

9. **Cross-device note (from session start):** beads `aism-l4uw` (Munkres
   payload restore) and `aism-ccso` (P1 `_REFS_RE` laundering vector) exist
   ONLY on the Hannover device's beads DB (no dolt remote here; the tracked
   `.beads/issues.jsonl` export is stale since session 30). The substance is
   in FINDINGS.md. Decide: recreate locally or wire a dolt remote.

10. **Open beads:** `aism-3fjg` (P1, rows 5–14 — updated), `aism-abca`
    (Kitaev pair — CLOSED this session), `aism-wazy` (P1 tripwire),
    `aism-9kmt` (P2 report sync), `aism-xjnc` (P3 CHANGELOG stale). Carried
    P1 items unchanged.

11. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at close).
    All work committed AND pushed. **NOTHING is in flight** (no af runs, no
    codex, no worktrees; all six elevation worktrees removed after banking).

## Next steps (ranked)

1. Ledger rows 5–14 serial elevation (`aism-3fjg`) — all deps T0 now.
2. F0-assembly landing + strengthened K-ledger replacement (guard release).
3. Root rewire LAST.
4. `aism-9kmt` report sync.
5. Cross-device beads decision (§9).

## What is intentionally NOT here

- Any claim `op-classical` is proved — **OPEN**. T0 = 176.
- Any claim the seven banks are new mathematics beyond the designed ledger:
  rows 170–174 re-establish the audited LEDGER-DOMAINS design at T0 under
  honestly re-scoped contracts; 175–176 re-establish inherited
  proved-mod-audit Kitaev-repair material (with a genuine refutation clause
  discharged against the printed source).
- Any weakening of row 14's mathematics: its revision to the scalar
  interface was audit-prescribed (the old contract asserted an F2/F3/PRH
  interface those rows do not export) and user-ratified; the application
  moves to the strengthened K-ledger where the map data are bound.
- The `lem-routef-k-ledger` parent rewire (guard still on).
- Report anchoring of the new banks (carried in `aism-9kmt`).
- Route X / XE decider work (fallback only); signed trunk PAUSED.
