# BRIEF — LEDGER-SETTING-RESCOPE v2 repair design

Date: 2026-08-05. Author: orchestrator (Claude). You are a FRESH codex repair
designer with NO prior context and no authorship stake in the v1 design.

## Inputs (read in this order)

1. `docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/BRIEF-LEDGER-SETTING-RESCOPE.md`
   — the original problem (verifier-caught family-wide contract
   under-specification; the three decisive challenge texts verbatim).
2. `docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/DESIGN-LEDGER-SETTING-RESCOPE.md`
   — the v1 design (REJECTED; parts survive: the 16 byte-suffix prefixes
   passed, the radius ordering passed, the af-amend mechanics passed).
3. `docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/AUDIT-LEDGER-SETTING-RESCOPE.md`
   — the BINDING hostile audit: 8 numbered findings (3 BLOCKER, 2 HIGH) and
   the **§3 exact redesign gate**. Your design must satisfy every item of that
   gate; treat its findings table as corrections to apply verbatim where exact,
   and as requirements where structural.
4. The worked exemplars the audit itself points to:
   `definitions/def-maincb-witness-ledger.md` and
   `definitions/def-stage1-polar-witness-data.md` (data-and-typing-only witness
   packages) and their producer rows (e.g. `lem-maincb-reset-constant-ledger`,
   the M28 chain) — this repository has already solved the
   definition-vs-formation split once; REUSE that shape.
5. `DESIGN-LEDGER-DOMAINS-v2.md` (the ratified mathematics), the 16 landed
   shards, and the two live af ledgers.

## Deliverables

One file: `docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/DESIGN-LEDGER-SETTING-RESCOPE-V2.md`,
a complete auditable package containing:

1. **Theorem-free setting definition** (revised
   `def-routef-raw-factor-setting`): raw-input data and typing/notation ONLY.
   No "supplies/furnishes/therefore", no existence assertions, no analytic
   estimates. Full shard text in `definitions/` schema.
2. **A formation lemma** (new registry row, full shard text): quantifier order
   `there exists ONE universal witness package W_RF (eta_A, C_A, C_E,
   epsilon_E, ...) such that for every admissible (H, Phi, eta) [0 <= eta <=
   rho_id^corr] there is a setting datum S (with its (B, v))` — with the
   correct direct deps (`lem-routef-ai-defect-linearization`,
   `lem-kitaev-almost-idemp-audit`, `lem-thmainext-conditional`, whatever else
   is genuinely used). This row is what the re-scoped family and the future
   strengthened K-ledger instantiate from. Give its projected af budget.
3. **The 16 re-scoped contracts** over the formation lemma's global-W-first
   scoping: keep the v1 byte-suffix discipline wherever possible (prefix-only,
   suffix byte-identical to landed) EXCEPT row 14, which per audit finding 5
   must be revised to an explicit scalar-arithmetic interface (state the exact
   new contract; the F2/F3/PRH application moves to the strengthened K-ledger).
   Bind every displayed matrix variable universally (finding 6). Canonicalize
   "furnished/successive" either as typed serial-packet data or by adding the
   audit's listed direct dep edges (finding 4 lists them row by row); state the
   full corrected `deps:` line per row.
4. **Corrected `defs:` lines** per row (drop `def-almost-idempotent`; add the
   setting def; anything else needed — audit finding 7 notes `def-ucp-map`
   provisioning for the workspaces).
5. **Revised af continuation plans + budgets** for the two live trees against
   the corrected contracts (the amend mechanics themselves are already
   audit-cleared).
6. **Blast radius** incl. the strengthened-K-ledger dependency on the
   formation lemma; DO-NOT-REWIRE guard untouched.
7. **Ranked hostile-audit risks** for the v2 re-audit.

## Constraints (binding)

- Design ONLY: write nothing outside `docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/`.
- The scalar ledger and all landed mathematics byte-unchanged except row 14's
  contract revision (which must be conservative: the scalar inequalities it
  proves are exactly those the v2 LEDGER-DOMAINS design §3.5 derives).
- L2: one canonical definition; no restatement; no naked symbols.
- Registry ASCII conventions; linker contract-match compatibility.
- This design promotes nothing; all 16 rows stay `stated`.
