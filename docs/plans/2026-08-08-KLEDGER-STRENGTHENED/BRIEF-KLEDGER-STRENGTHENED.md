# BRIEF — design the strengthened `lem-routef-k-ledger` replacement + `lem-routef-f0-assembly` landing package

You are a fresh design worker (independent context). You must re-derive the
package from the sources below; trust NOTHING from any conversation summary.

## Situation

The LEDGER-DOMAINS queue is complete: the formation row, ledger rows 1–14,
D2, D3, and the two ROW8-FACTOR sub-lemmas are all af-validated (T0). The
F0 seam rows `lem-routef-f0-ucp-lift` and `lem-routef-f0-defect-identity`
are T0. `lem-routef-f2-positive-unital-compression`,
`lem-routef-f3-retract-defect`, and `lem-routef-prh-finish` are T0.

What remains on Route F above the root rewire (W78 §5 step 6):

1. **Replace** the landed `argument/lemmas/lem-routef-k-ledger.md` contract
   (currently `proved-mod-audit`, `af: none`, OLD deps line) with the
   **strengthened replacement**: a fully-quantified ∀n ∀Q ∀η parent that
   binds the seam to `op-classical` explicitly. This REPLACES a landed
   contract — it is a new proof obligation, NOT a binder edit
   (AUDIT-F0-ASSEMBLY correction 3).
2. **Land** the new row `lem-routef-f0-assembly` (DESIGN-F0-ASSEMBLY §1.4).
3. Elevation follows after user ratification (not your job; you design the
   workspaces and budgets).

## Task

Produce the complete landing package. Its mathematical core is already
designed and audited — your job is to instantiate it against the CURRENT
byte-frozen T0 registry contracts and produce land-ready shard text, af
skeletons, and seeding packages.

## Hard constraints (violating any of these makes the design REJECTED)

1. **The strengthened parent contract** starts from
   `DESIGN-F0-ASSEMBLY.md` §1.3 and MUST fold in, verbatim where they
   apply, the AUDIT-F0-ASSEMBLY corrections: the canonical complexification
   typing (`Q_C`, `Phi := J Q_C D` — match the byte-frozen phrasing of the
   two landed lift rows, "canonical complex-linear extension Q_C"), and the
   strengthened-replacement classification. The conclusion constants are
   `K` (row 13) and `eta_K := min{rho_fac, (24*K)^(-1), 1}` (row 14) and
   the final bound `||Q - E||_{infinity->infinity} <= (K + 4*sqrt(2K))*sqrt(eta)`.
   Every named quantity must resolve to a T0 dep's contract, a `definitions/`
   shard, or be defined inside the contract; NO symbol may rest on a design
   document's ambient prose (that failure killed this family once — see
   FINDINGS.md 2026-08-05).
2. **The deps line** is the BINDING block of
   `DESIGN-LEDGER-SETTING-RESCOPE-V2.md` §6.2 (15 ids: the two F0 lift
   rows, the formation row, rows 5/6/8/9, the three telescopes, K-finiteness,
   threshold-minimum, F2, F3, PRH). Per the ROW8-FACTOR delta (sketch v48
   map change 2): row 8 now factors through
   `lem-routef-upsilon-prime-component-construction` (T0) and
   `lem-routef-upsilon-prime-left-inverse` (T0). Determine from the
   byte-frozen contracts whether the parent needs the componentwise
   construction data directly; if yes, ADD
   `lem-routef-upsilon-prime-component-construction` as a direct dep and
   justify; if no, justify why row 8's frozen contract suffices. Deps may
   ONLY be af-validated (T0) rows.
3. **Application order** inside the parent proof (rescope-v2 §6.2):
   F0 lift + defect identity -> check `eta <= eta_K <= rho_fac <= rho_T <= rho_id^corr`
   -> formation (same `Phi`, same `eta`) -> row 5 -> row 6 -> row 8 -> row 9
   (packet construction) -> rows 10/11/12 -> row 13 -> row 14 -> F2 -> F3 -> PRH.
   Verify each seam byte-against the frozen contracts (the F0-ASSEMBLY §2
   seam table is your template; re-run it against the CURRENT registry text,
   which post-dates that audit).
4. **`lem-routef-f0-assembly`**: contract per DESIGN-F0-ASSEMBLY §1.4 with
   the same Q_C typing correction; `deps: lem-routef-k-ledger` ONLY (no
   F2/F3/PRH duplication — §3 double-counting rule).
5. **Budgets (BINDING):** strengthened parent target 17 nodes / 4 rounds /
   hard cap 22 (rescope-v2 §6.2; re-audit this projection against your
   skeleton and say honestly whether it holds under the observed 1.5–3x
   fresh-build expansion of this family; if it cannot fit under cap 22,
   propose a factoring — do NOT inflate the cap). `lem-routef-f0-assembly`
   target 2 nodes / depth 2 / cap 6.
6. **Statuses at landing:** strengthened parent `status: stated`, `af: none`
   (the old proved-mod-audit W74F paper ledger stays recorded in the body
   and provenance as history, honestly marked superseded — the strengthened
   form was never hostile-verified as a paper proof and must NOT inherit
   `proved-mod-audit`; if you believe it should, argue it explicitly for
   the auditor to attack). `lem-routef-f0-assembly` `status: stated`,
   `af: none`. NOTHING is promoted by this design.
7. **Guard semantics:** the DO-NOT-REWIRE guard on `lem-routef-k-ledger` is
   released by THIS landing and only this landing (W78 D4). The
   `op-classical` root wiring is NOT touched — root rewire is a separate
   LAST step. Your package must not propose any edit to `op-classical`.
8. **No new definitions** unless truly unavoidable (theorem-free data/typing
   only; deletion test). `def-ucp-map` exists. Note the reusable T0 GT
   externals `GT-kitaev-fd-cstar-structure` and
   `GT-kitaev-canonical-stinespring` exist if a workspace needs them.

## Inputs you MUST read

- `argument/lemmas/lem-routef-k-ledger.md` (the row being replaced)
- `docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md` + `AUDIT-F0-ASSEMBLY.md`
- `docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/DESIGN-LEDGER-SETTING-RESCOPE-V2.md` §§2, 6 + `AUDIT-LEDGER-SETTING-RESCOPE-V2.md`
- `docs/plans/2026-08-08-ROW8-FACTOR/DESIGN-ROW8-FACTOR.md` (the factored row-8 interface)
- The CURRENT byte-frozen contracts of ALL 15+2 candidate deps under
  `argument/lemmas/` (the two lift rows; `lem-routef-raw-factor-setting-formation`;
  `lem-routef-delta-prime-closeness`; `lem-routef-delta-normalization-closeness`;
  `lem-routef-upsilon-prime-closeness`; `lem-routef-upsilon-normalization-closeness`;
  `lem-routef-delta-upsilon-telescope`; `lem-routef-multiplicative-telescope`;
  `lem-routef-upsilon-delta-telescope`; `lem-routef-k-finiteness`;
  `lem-routef-threshold-minimum`; `lem-routef-f2-positive-unital-compression`;
  `lem-routef-f3-retract-defect`; `lem-routef-prh-finish`;
  `lem-routef-upsilon-prime-component-construction`;
  `lem-routef-upsilon-prime-left-inverse`)
- `definitions/def-routef-raw-factor-setting.md`, `definitions/def-ucp-map.md`,
  `definitions/def-stochastic.md`, `definitions/def-almost-idempotent.md`
- `CLAUDE.md` §§1, 6; `FINDINGS.md` entries dated 2026-08-05 and 2026-08-08
- `scripts/af_constants.py` (NODE_SOFT_CAP)

## Deliverable

Write EXACTLY ONE file:
`docs/plans/2026-08-08-KLEDGER-STRENGTHENED/DESIGN-KLEDGER-STRENGTHENED.md`
containing:

(a) the complete replacement text of `lem-routef-k-ledger.md` (full
    frontmatter + body, ready to land verbatim; honest provenance recording
    the replacement, its authorization trail, and the superseded W74F
    paper-ledger history);
(b) the complete text of the new `lem-routef-f0-assembly.md` shard;
(c) the re-run seam table (every consumed estimate/constant vs the CURRENT
    frozen contract text, with EXACT-MATCH / MATCH-STRONGER / MISMATCH
    verdicts; any MISMATCH is a stop-the-line finding);
(d) a complete af tree skeleton per target (node ids + exact statements)
    demonstrating the budgets, with the honest 1.5–3x expansion assessment;
(e) the seeding package per target: def-add list + exact add-external list
    (dep externals use the literal `proofs/<dep-id>` path + byte-verbatim
    contract convention);
(f) the landing manifest: every file the landing session must touch
    (shards, `report/UNWIRED.md` additions, generated
    definitions/argument/report projections, HANDOFF/sketch/worklog updates)
    — nothing may be left stale (Rule 9; rescope-v2 audit finding 4 is the
    cautionary precedent);
(g) the elevation order and per-target budgets;
(h) a ranked list of the risks a fresh hostile auditor should attack
    (include at minimum: packet-existence vs telescope-import confusion;
    same-datum drift across the 15 deps; the eta-domain chain
    `eta_K <= rho_fac <= rho_T <= rho_id^corr`; complexification seam
    `Q <-> Q_C <-> Phi`; sharpness overclaim; status laundering of the
    superseded paper ledger; guard-release scope).

Head the file with: `Status: DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD,
SEED, OR PROMOTE — pending fresh hostile audit and user ratification.`

## Discipline (non-negotiable)

Write ONLY the deliverable file. Do NOT edit `argument/`, `definitions/`,
`proofs/`, or any other file. Do NOT run git commit or git push. Do NOT run
`af` mutations. Your final message: a 10-line summary — the deps-line
decision (16 vs 15), the seam-table verdict, and the two budgets.
