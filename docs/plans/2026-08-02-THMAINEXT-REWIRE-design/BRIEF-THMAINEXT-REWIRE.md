# BRIEF — the lem-thmainext-conditional dependency rewire (design v5 sect-10 step 15, post-MAINCB-repair re-validation)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation; everything you produce is escalated for verbatim landing after a
fresh hostile audit. Write your design to
`docs/plans/2026-08-02-THMAINEXT-REWIRE-design/DESIGN-THMAINEXT-REWIRE.md`.

## Context

The MAIN campaign is COMPLETE: every row M01-M28 is af-validated T0
(2026-08-02; capstone `lem-maincb-structural-assembly` banked 20/20).
The user-ratified `DESIGN-MAIN-STRUCTURE-v5.md` sect-10 step 15
prescribed, "only after M28 and M19-R validate" (both now T0), this EXACT
dependency rewire for `lem-thmainext-conditional`, leaving its contract
verbatim:

```yaml
deps: conj-hcb; conj-extcb; lem-hcb-column-hilbert-squared; lem-maincb-error-improvement; lem-maincb-reset-invariant-preservation; lem-maincb-structural-assembly; lem-extcb-four-corner-merge
```

That step was marked **ESCALATED, not applied**. Since it was written,
the `aism-jl4g` two-defect repair (`DESIGN-MAINCB-REPAIR-v2.md`,
user-ratified 2026-08-01) AMENDED the contracts of M12, M16-M18,
M19-S1/S2/S3/R, and M20-M28 — including M19-R
(`lem-maincb-reset-invariant-preservation`) and M28
(`lem-maincb-structural-assembly`), two of the seven proposed deps — by
rebinding all constants through the `def-maincb-witness-ledger` datum W
and threading explicit unit clauses. The repair design's hand-off clause
(`DESIGN-MAINCB-REPAIR-v2.md` sect "later lem-thmainext-conditional
rewire") states the rewire "must consume M28's final unit-controlled
isomorphism without reopening this package."

Your job: re-validate (or minimally amend) the v5 sect-10 rewire against
the CURRENT banked T0 contracts, producing the ONE final deps line ready
for hostile audit and landing. The `lem-thmainext-conditional` contract
itself stays byte-UNCHANGED (it is `proved-mod-audit`, af: none; the
rewire does not elevate it and does not change its status).

## What to check (all against current shard/export bytes, never a paraphrase)

1. **Coverage:** does each analytic input the `lem-thmainext-conditional`
   proof record actually uses (the W74F artifact chain in its provenance:
   DECOMP-W74F-C-THMAINEXT.md sect 3-5 assembly + corrected COL-HILB;
   PROOF-W74F-H-STAGE1.md Stage-1 reset packet) have a T0 (or
   proved-mod-audit conj-*) provider in the proposed seven-dep line, AS
   THOSE PROVIDERS ARE NOW WORDED (the repaired W-ledger forms)? In
   particular: M28 now delivers the isomorphism WITH the unit estimate
   `||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon` and witnesses
   C_struct/e_struct — does the thmainext assembly consume exactly this
   (the hand-off clause), or does it need anything M28's repaired
   contract no longer (or never) exported?
2. **The W-ledger binding mismatch:** the thmainext contract binds its
   own universal constants (C_E, epsilon_E) WITHOUT the ledger datum. The
   proposed deps now export ledger-bound statements ("Fix the datum W
   supplied by lem-maincb-reset-constant-ledger; ..."). Is the deps line
   still coherent for a future af elevation (typed-witness laws i/ii,
   docs/LEARNINGS.md 2026-07-28) — i.e. can C_E, epsilon_E be chosen from
   the W-ledger witnesses without a contract change? State this
   explicitly; if the contract WOULD need rewording for af elevation,
   FLAG it as a separate future escalation item — do NOT propose a
   contract change now (out of scope, per the hand-off clause).
3. **Transitive availability:** v5 claimed the reset constant ledger is
   available transitively through M19-R and the complete MAIN subtree
   through M28. Verify against the current DAG (argument/INDEX.md;
   `python3 scripts/argument.py --show <id>`); the linker forbids
   cycles — check none is introduced.
4. **Dep-set minimality/sufficiency:** is any of the seven now redundant
   (available transitively) or insufficient (a repaired contract dropped
   something v5 assumed)? Deviations from the ratified v5 line must be
   individually justified — default is the v5 line verbatim.
5. **No-T0-invalidation:** the rewire touches ONLY the
   `lem-thmainext-conditional` shard's deps field (+ provenance note).
   Confirm no other shard, no locked def, no validated workspace is
   touched. Note `proofs/lem-thmainext-conditional` exists as a workspace
   — check what state it is in and whether the deps change requires any
   workspace action now (expected: none, af: none means no seed to
   preserve — verify).

## Materials

- `argument/lemmas/lem-thmainext-conditional.md` (current shard: contract,
  provenance, body).
- `docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md`
  sect-10 (the ratified step 15 + the 8-node/depth-2 projection) and
  sect-11 (the escalation ledger).
- `docs/plans/2026-08-01-MAINCB-REPAIR-design/DESIGN-MAINCB-REPAIR-v2.md`
  (the repaired contracts, esp. rows M19-R and M28; the hand-off clause).
- Current shards/exports: `argument/lemmas/lem-maincb-structural-assembly.md`,
  `lem-maincb-reset-invariant-preservation.md`,
  `lem-maincb-error-improvement.md`, `lem-hcb-column-hilbert-squared.md`,
  `lem-extcb-four-corner-merge.md`, `conj-hcb.md`, `conj-extcb.md`
  (+ their `proofs/<id>/export.md` where af: validated).
- The W74F artifacts named in the thmainext provenance
  (`docs/plans/2026-07-23-W74F-artifacts/`).
- `docs/LEARNINGS.md` 2026-07-28 typed-witness laws.

## Deliverables (in DESIGN-THMAINEXT-REWIRE.md)

1. **The final deps line** (one line, semicolon-separated ids): v5
   verbatim, or amended with a per-id justification.
2. **The coverage table:** each analytic input of the thmainext proof
   record -> its provider id -> the provider's CURRENT contract clause
   that supplies it (quote the clause).
3. **The W-ledger coherence statement** (check 2): elevation-readiness
   verdict + any flagged future escalation (no contract change proposed).
4. **The DAG check:** no cycle; transitive-availability claims verified;
   linker-facing notes (status propagation: the row stays
   proved-mod-audit and may import T0 + conj rows — confirm the linker
   accepts a proved-mod-audit row with mixed deps).
5. **The no-T0-invalidation table** + the workspace disposition note.
6. **The exact landing package:** the new deps line + the provenance
   sentence to append to the shard (naming design v5 sect-10 step 15,
   this design, and the audit), flagged as a deps-only amendment with
   contract byte-UNCHANGED.
7. **Risk register:** the top ways this rewire could be wrong, and what a
   hostile auditor should attack first.

## Hard constraints

- Design document only; no registry mutation, no proofs, no status
  changes; `lem-thmainext-conditional` remains `proved-mod-audit` and
  `op-classical` remains OPEN.
- Never quote a contract from memory — read the current shard bytes.
- NOT-IN-LOCAL-REFS discipline (L1) applies to any new ground-truth claim.
