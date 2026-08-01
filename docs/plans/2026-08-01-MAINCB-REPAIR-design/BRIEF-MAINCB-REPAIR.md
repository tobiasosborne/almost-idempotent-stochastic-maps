# BRIEF — the MAIN two-defect interface repair (unit-clause thread + maincb witness ledger)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation; everything you produce is escalated for verbatim landing after a
fresh hostile audit and user ratification. Write your design to
`docs/plans/2026-08-01-MAINCB-REPAIR-design/DESIGN-MAINCB-REPAIR.md`.

## Context

The MAIN campaign (`docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md`,
user-ratified; 30 rows M01–M28) is 18/31 rows banked af-validated T0. Two
independent contract-level interface defects were established by fresh af
verifier cohorts during session 38 (bead `aism-jl4g`); both block the
remainder of the campaign. Two workspaces are PARKED on exactly these
defects: **M12** `proofs/lem-maincb-cross-class-merging-datum` at 9/10
(ONLY the unit clause open; runs 1–3 ledgers in git history) and **M19-S1**
`proofs/lem-maincb-stage1-call-envelope` at 15/17 (ONLY the
anaphoric-constant ledger nodes open; stuck ×3 on the same class). Your job
is the complete repair package for BOTH defects, ready for hostile audit and
user ratification, after which the parked trees are RE-SEEDED (never
patched) under the repaired contracts.

## Defect (a) — the unit-clause thread

`def-four-corner-merging-datum` REQUIRES a diagonal-unit approximation
field, but `def-extended-delta-inclusion` carries NO unit clause: an
extended \(C_{\rm out}t\)-isomorphism therefore cannot furnish the datum's
unit field, so M12's ratified contract
(`DESIGN-MAIN-STRUCTURE-v5.md` row M12, `argument/lemmas/lem-maincb-cross-class-merging-datum.md`)
is under-hypothesized. Two independent M12 verifier cohorts confirmed this.

The unit data must thread from the reset states: the repair supplies
\(\|v_W(I_{B_W}) - u_{A_W}\| \le t\) for \(W\in\{U,V\}\) (with \(u_{A_W}\)
the corner unit of \(A_W\)) as an explicit hypothesis/output field, threaded
through every `def-maincb-reset-state` producer/consumer:

- **M12** `lem-maincb-cross-class-merging-datum` — amend hypotheses to
  supply the two unit estimates; conclusion unchanged.
- **M19-S3** `lem-maincb-stage3-call-envelope` — supplies the two reset
  states to M12; must carry/forward the unit estimates.
- **M26** `lem-maincb-binary-block-merge` — produces the merged reset state
  \(v_{U\cup V}\); must OUTPUT its unit estimate so merges compose.
- **M25** `lem-maincb-one-class-extension` — produces per-class reset
  states with unit estimates from the M16/EXT outputs (conj-extcb's
  \(v_+\) construction — read `proofs/conj-extcb/` exports and the extcb
  block contracts for what unit control the construction actually gives).
- **M19-R** `lem-maincb-reset-invariant-preservation` — unit-estimate
  preservation under M03 error improvement. Ground truth: the THIRD clause
  of `prop_delta_hominc`, `refs/kitaev-2405.02434/approximate_algebras.tex:1194-1196`
  ("if \(\|v(I_{\calA'})-I_{\calA''}\|\) is less than a certain positive
  constant, then \(\|v(I_{\calA'})-I_{\calA''}\|\le O(\delta+\eps)\)") —
  ALREADY a registered byte-matched GT external in the S1-ENDGAME C3
  workspace (grep `proofs/*/externals/` for `prop_delta_hominc` and reuse
  the registration verbatim).

Decide precisely: whether the unit estimate enters `def-maincb-reset-state`
itself (a def amendment — ratification item, ripples through ALL its
consumers including banked T0 rows: check the cascade!) or as explicit
contract clauses on the affected rows only (the audit-v3/v4 style). State
the trade-off and recommend one; the default expectation from the session-38
discussion is CONTRACT CLAUSES ONLY unless you find that leaves a
consumer unable to discharge its obligation.

## Defect (b) — the maincb witness ledger (the W93 anaphoric-constant pattern)

M19-S1 is stuck ×3 on the same verifier class: its contract binds
\(c_0^{\rm cb}\) as an unquantified anaphor (M03's external binds
\(c_0^{\rm cb}\) existentially within its own statement; af verifiers
refuse the cross-shard identification without a typed datum — EXACTLY the
W93 Stage-1 lesson, `docs/LEARNINGS.md` 2026-07-28 laws i/ii). ALL of
M19-S1/S2/S3/R (as not-yet-banked or to-be-re-seeded), M20–M28 use
anaphoric constants: \(c_0^{\rm cb}, L, e_{\rm env}, e_1, e_{\rm s2},
e_{\rm cross}, K_1, K_2, K_3, K_{\rm call}, \varepsilon_{\rm MAIN},
r_{\rm reset}\).

The repair pattern is PROVEN in-repo: `def-stage1-polar-witness-data`
(pure data tuple, NO analytic assertions) + the result rows
`lem-stage1-polar-scalar-arithmetic` / `lem-stage1-polar-constant-ledger`
+ parameterized transport/explicit-binder rows (read the Stage-1 B-chain
shards and `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v6.md`
§§2–3, 8). Produce:

1. **`def-maincb-witness-ledger`** — a typed, data-only tuple of named
   scalar fields covering the anaphoric constants above (decide the exact
   field list: which constants are ledger fields vs derived scales; follow
   the fourteen-field polar precedent's coefficient/margin/derived-scale
   typing). Full proposed shard content, provenance locus,
   `original`/`consensus` tag. This is a USER ratification item.
2. **The binder/arithmetic result row(s)** — decide whether the existing
   M18 `lem-maincb-reset-constant-ledger` (already designed; NOT yet
   banked — check its current status in `argument/lemmas/`) is rebound to
   export the analytic-witness relation over the new datum, or whether a
   separate `lem-maincb-witness-arithmetic` row is needed (the polar
   precedent used two rows). Contracts verbatim.
3. **Rebound contracts** for every affected row — M19-S1, M19-S2, M19-S3,
   M19-R, M20, M21, M22, M23, M24, M25, M26, M27, M28 — each one physical
   line, binding its constants THROUGH the ledger datum (typed-witness law
   i; provider witnesses fixed FIRST, receiving fields transported by
   monotonicity, law ii). Rows whose current contracts do NOT mention any
   anaphoric constant may be left unchanged — say so explicitly per row.

Defects (a) and (b) interact: the amended M12/M19-S3/M25/M26/M19-R
contracts from (a) must ALREADY be written in the ledger-bound form of (b).
Produce ONE coherent final contract per affected row, not two layers of
amendment.

## Hard constraints (all BINDING)

1. **Contracts:** one physical line each, flattened registry ASCII in the
   shard style (the design doc may use LaTeX; the registry lines must be
   ASCII), no numerical value of any universal constant (named existential
   witnesses are correct form). Every definite description a contract binds
   must have a TYPED-WITNESS provider among its deps/defs
   (`docs/LEARNINGS.md` 2026-07-28 law i); parameterized rows fix provider
   witnesses FIRST and transport receiving fields by monotonicity (law ii).
2. **No T0 invalidation.** No proposed wording may force an amendment of
   any af-validated T0 row's contract or any byte-matched external
   registered in an existing VALIDATED workspace. The banked MAIN rows
   (M01–M11, M13–M15 — verify the exact set from `argument/lemmas/`
   `status`/`af` fields) are FROZEN. If a repair genuinely cannot avoid
   touching a T0 contract, STOP that route and flag it as an escalation
   item with the precise reason. List the workspaces/rows you checked.
3. **Def layer:** REUSE existing shards (`def-maincb-partition-state` — note
   its 2026-07-30 user-ratified amendment ('nonempty subset of J') —,
   `def-maincb-reset-state`, `def-maincb-raw-call`,
   `def-four-corner-merging-datum`, `def-extended-delta-inclusion`,
   `def-extcb-datum`, `def-epsilon-cstar-algebra`, ...; read
   `definitions/INDEX.md`). Each genuinely new def shard is a USER
   ratification item — minimize their number and justify each. Expected:
   exactly ONE new def (`def-maincb-witness-ledger`) unless you show a
   second is unavoidable.
4. **Dimension-freeness:** every constant universal — independent of
   \(\dim\calX\), amplification, block data, class count, and stage index.
   The M20 comparison row and the RI invariant
   (`DESIGN-MAIN-STRUCTURE-v5.md` §§7–8, the constants table) must survive
   your rebinding — check the induction-invariant arithmetic explicitly.
5. **Budgets:** per-row prover-build budget (nodes/rounds), hard cap 26; if
   a rebound row cannot plausibly land under ~12 nodes given the T0
   imports, FACTOR it and say so. Give explicit RE-SEED guidance for the
   parked M12 (9/10) and M19-S1 (15/17) trees: which validated nodes'
   statements survive verbatim under the repaired contracts (the trees are
   re-seeded fresh; this guidance only calibrates the budget).
6. **Source discipline:** every external carries an exact `refs/` locus
   (file:line-range) into `refs/kitaev-2405.02434/approximate_algebras.tex`.
   If a step needs ground truth not in `refs/`, STOP that route and flag it
   as a reference-acquisition item (L1). The failed-run ledgers (M12 runs
   1–3, M19-S1 runs 1–3, in git history and the parked `proofs/`
   workspaces) are evidence — cite verifier findings by path.
7. **No registry mutation, no proofs.** Design document only.

## Materials (read these; never design against a paraphrase)

- `docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md`
  (the ratified design: row table §6, M25 proof plan, induction invariant,
  constants table) + its audit files (AUDIT-…-v3/v4/v5).
- `argument/lemmas/lem-maincb-*.md` — the CURRENT contracts and statuses
  (banked rows are frozen; the ratified-but-unbanked rows are what you
  rebind).
- `proofs/lem-maincb-cross-class-merging-datum/` and
  `proofs/lem-maincb-stage1-call-envelope/` — the parked trees and their
  ledgers (verifier findings = the defect record).
- `definitions/def-maincb-*.md`, `def-four-corner-merging-datum.md`,
  `def-extended-delta-inclusion.md`, `def-stage1-polar-witness-data.md`
  (the pattern precedent).
- `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v6.md` §§2–3, 8
  (the W93 repair pattern) and `docs/LEARNINGS.md` (2026-07-28 laws).
- `refs/kitaev-2405.02434/approximate_algebras.tex` — esp. `:1194-1196`
  (prop_delta_hominc, the near-unitality clause), `:1317-1319`
  (cor_improvement), `:1325-1345` (four-corner merge), `:1352-1359`,
  `:1414-1444` (the main induction), `:1557`.
- `docs/plans/2026-07-30-top-down-proof-sketch-v41.md` (the live sketch;
  map change 3 records these defects).

## Deliverables (in DESIGN-MAINCB-REPAIR.md)

1. **The unit-clause thread design** (defect a): the decision
   (def amendment vs contract clauses) with the trade-off argument; the
   thread map (which row supplies/forwards/consumes which unit estimate,
   as a small table over M12/M19-S3/M25/M26/M19-R + any row you find is
   also affected — check M16, M17, M22, M24, M28 explicitly).
2. **`def-maincb-witness-ledger`** — full proposed shard content
   (data-only, W93 pattern), field table with types/roles, provenance,
   tag.
3. **The binder/arithmetic row decision** (rebind M18 vs new row), with
   contracts verbatim.
4. **The final contract table**: every affected row — id | one-line
   contract (the ONE coherent final form) | defs | deps | provenance loci |
   budget | changed/unchanged flag with one-line reason.
5. **The def-layer table** (reused defs; the new def in full; zero other
   new defs or a justification).
6. **The cascade/no-T0-invalidation check** (constraint 2): rows and
   workspaces checked, verdict per banked row.
7. **The dimension-freeness audit** incl. the induction-invariant
   arithmetic under the rebinding.
8. **Re-seed guidance** for M12 and M19-S1 (constraint 5).
9. **The serial landing + elevation order** for the remainder of the
   campaign under the repaired contracts (which rows re-seed first, what
   unblocks what; M16, M17 and the M19 family, M20–M28, then the escalated
   `lem-thmainext-conditional` rewire is OUT of your scope — note the
   hand-off only).
10. **An honest risk register**: per affected row, what a hostile verifier
    will attack first; plus the top three ways THIS design could be wrong.
