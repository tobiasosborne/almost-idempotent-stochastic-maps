# BRIEF — the M24 corner-nontriviality gap (dim S_{P_j} >= 1)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation; everything you produce is escalated for verbatim landing after a
fresh hostile audit and user ratification. Write your design to
`docs/plans/2026-08-02-M24-NONTRIVIALITY-design/DESIGN-M24-NONTRIVIALITY.md`.

## Context

The MAIN campaign (`docs/plans/2026-08-01-MAINCB-REPAIR-design/DESIGN-MAINCB-REPAIR-v2.md`,
user-ratified 2026-08-01) is banked af-validated T0 through M27; the sole
remaining rows are **M24** `lem-maincb-stage1-maximality` (PARKED, this
brief) and the capstone **M28** `lem-maincb-structural-assembly` (blocked
ONLY on M24; its workspace is seeded and its oracle registered). M24's
first elevation (2026-08-02, W122) aborted STUCK on a CONTRACT-LEVEL
finding (bead `aism-twpa`, P0): the ratified contract concludes
`dim S_{P_j} = 1`, but the verifier cohort established that NO allowed
input yields `dim S_{P_j} >= 1`. The workspace
`proofs/lem-maincb-stage1-maximality/` was restored to the clean ratified
seed (8 ledger entries, linker green). Your job is the complete repair
design for this single gap, ready for hostile audit and user ratification.

## The defect record (verbatim verifier challenges)

From the aborted 45-entry tree (preserved read-only at
`/tmp/claude-1000/-home-tobiasosborne-Projects-almost-idempotent-stochastic-maps/3dd18513-bf41-437f-80f3-7515872b1529/scratchpad/stuck-lem-maincb-stage1-maximality/`;
3 of 4 nodes had validated before the abort):

- **ch-94ae993f6abc0f5b** (node 1.2, dependencies, major): "The inference
  P_j != 0 implies S_{P_j} is a nonzero vector space is unsupported by
  every allowed input. def-maincb-partition-state only declares, for a
  supplied partition state and U subseteq J, A_U = S^A_{P_U} as a
  compressed corner; it states no nontriviality theorem for S^A_P when
  P != 0. The three imported lemmas supply maximal existence and positive
  lower norm, strict refinement conditional on dim S_{P_j}>1, and
  constants; none supplies dim S_{P_j}>=1. Moreover, the root contract
  supplies no MAIN-CB partition state tied to the displayed A,w. Since w
  is only an approximate inclusion, P_j=w(e_j) is merely known nonzero
  here, not an exact nonzero projection from which corner nontriviality
  could be taken definitionally."
- **ch-7411a0325c917f52** (node 1, dependencies, major): "The validated
  children establish only that P_j=w(e_j) is nonzero (node 1.2) and that
  dim S_{P_j}<=1 (node 1.3). They do not establish dim S_{P_j}>=1. No
  allowed external supplies the missing implication P_j nonzero =>
  S_{P_j} nonzero ... Hence dim S_{P_j}=0 is not excluded by the
  permitted dependencies."
- **ch-37eff8dcb9a3b5d1** (node 1, scope, major): the prover's root
  weakening to `dim S_{P_j} <= 1` "is an impermissible scope drift rather
  than a proof of node 1 as commissioned" (correctly rejected; discarded).

## Ground truth (the paper's own route — read these loci, never a paraphrase)

All in `refs/kitaev-2405.02434/approximate_algebras.tex`:

- `:920-929` — the projection alternatives `\eqref{P_alternatives}`:
  `||P|| <= O(delta)` OR `| ||P|| - 1 | <= O(delta+eps)`; a
  delta-projection is *nonvanishing* iff the second alternative holds.
- `:1066` — "It is clear that S_P = 0 if and only if P is sufficiently
  close to 0 as described by the first alternative in
  \eqref{P_alternatives}. (Recall that in the opposite case, we call P
  'nonvanishing'.)" — i.e. the paper's missing-step is exactly
  **nonvanishing => S_P != 0**, stated as "clear" and never proved there.
- `:1417-1426` — Stage 1 of th_main (M24's locus): the paper only rules
  out `dim S_{P_m} > 1` (via lem_nontriv_projection + strict refinement +
  maximality) and treats `>= 1` as implicit.
- `:931-945` — lem_nontriv_projection (the `dim > 1` splitting tool; its
  in-repo counterpart `lem-stage1-rectified-nontrivial-projection` is
  banked T0).

Note what the chain requires: `P_j = w(e_j)` must first be shown
**nonvanishing** (second alternative), not merely nonzero — the verifiers
explicitly flagged that "merely known nonzero" is insufficient. Survey
what lower-norm control the extended-inclusion hypotheses on `w` provide
(M22's contract cites "the lower norm is positive"; check
`def-extended-delta-inclusion` and the banked M22/M23 exports for what is
actually available as an import).

## The three candidate resolution routes (options on bead aism-twpa — UNJUDGED; you judge)

- **(a) Provision a nontriviality provider row** (new registry lemma,
  e.g. `lem-maincb-corner-nontriviality`): universal constants such that
  a nonvanishing delta-projection P has S_P != 0 (equivalently
  dim S_P >= 1), typed in the extended/compressed-corner vocabulary M24
  already imports; plus whatever bridge shows each `P_j = w(e_j)` under
  M24's hypotheses IS nonvanishing at the ledger scale. Candidate
  existing material to assess (applicability UNJUDGED): banked T0
  `lem-compcb-corner-algebra` ("whenever ... P is a nonvanishing
  delta-projection, S_P with the compressed product ... is an extended
  C_ca*e-C*-algebra" — does an extended C*-algebra structure on S_P
  already force S_P != 0 via its unit u_P = Co_P(P)? check
  `def-extended-epsilon-cstar-algebra` and banked
  `lem-compcb-compressed-unit-norm`); banked
  `lem-stage1-rectified-nontrivial-projection` (NOTE: different shape —
  it produces a nontrivial projection inside an algebra of dim > 1; the
  bead's candidate pointer, likely the wrong tool for dim >= 1); the
  compcb/extcb corner-dimension rows.
- **(b) Amend the M24 contract to the provable `dim S_{P_j} <= 1` form**
  — admissible ONLY IF the consumer survey shows every consumer needs
  only `<=`. M24's sole registry dependent is M28. But survey the FULL
  discharge chain inside M28's design skeleton
  (`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M28, budget 9/3/13): M28 must
  discharge the hypothesis "all atomic images are one-dimensional" of
  banked T0 rows M25 `lem-maincb-one-class-extension` and M19-S3
  `lem-maincb-stage3-call-envelope` ("with one-dimensional atomic
  images"), and the class structure of `def-maincb-partition-state`
  (j ~ k iff dim S^A_{P_j,P_k} = 1, "when this relation is an
  equivalence" — check reflexivity) consumed by M27
  `lem-maincb-stage3-finite-recombination` ("has classes C_1,...,C_q").
  Those T0 contracts are FROZEN: if M28 cannot discharge them from
  `dim <= 1` alone, option (b) is DEAD — say so with the exact blocking
  clause quoted.
- **(c) Strengthen a dep contract to export nontriviality.** M24's deps
  are M22 `lem-maincb-maximal-reset-selection`, M23
  `lem-maincb-stage1-strict-refinement`, M18
  `lem-maincb-reset-constant-ledger` — ALL banked af-validated T0 as of
  2026-08-02, hence FROZEN (no-T0-invalidation, constraint 2). If (c)
  survives at all it must do so without amending any banked contract
  (e.g. as an additional NEW dep row — which structurally collapses into
  (a)); establish this honestly.

Judge all three; produce ONE recommended design with explicit rejection
reasons for the others. If two are viable, recommend the one with the
smaller ratification surface (fewer new/amended shards), then the smaller
elevation budget.

## Hard constraints (all BINDING)

1. **Contracts:** one physical line each, flattened registry ASCII in the
   shard style, no numerical value of any universal constant (named
   existential witnesses are correct form). Every definite description a
   contract binds must have a TYPED-WITNESS provider among its deps/defs
   (`docs/LEARNINGS.md` 2026-07-28 law i); parameterized rows fix
   provider witnesses FIRST and transport receiving fields by
   monotonicity (law ii). Ledger-bound rows bind constants through the
   `def-maincb-witness-ledger` datum W supplied by
   `lem-maincb-reset-constant-ledger`, exactly as the banked M21-M27 do.
2. **No T0 invalidation.** No proposed wording may force an amendment of
   any af-validated T0 row's contract, any locked definition, or any
   byte-matched external registered in an existing VALIDATED workspace.
   As of 2026-08-02 the banked MAIN set includes M01-M23 and M25-M27
   (verify the exact set from `argument/lemmas/` `status`/`af` fields).
   The M28 contract is ratified-but-unbanked: prefer leaving it
   byte-unchanged; if your design amends it, flag that as an explicit
   ratification item with the precise reason.
3. **Def layer:** REUSE existing shards (`def-compressed-corner`,
   `def-delta-projection`, `def-one-dimensional-delta-projection`,
   `def-near-positive-projection`, `def-maincb-partition-state` (note its
   2026-07-30 amendment), `def-maincb-witness-ledger`,
   `def-extended-epsilon-cstar-algebra`, `def-extended-delta-inclusion`,
   `def-projection-basis`, ...; read `definitions/INDEX.md`). Each
   genuinely new def shard is a USER ratification item — expected ZERO;
   justify any exception.
4. **Dimension-freeness:** every constant universal — independent of
   dim A, amplification, block data, class count, and stage index. If a
   new row's smallness threshold must sit inside the ledger's
   `W.epsilon_MAIN` window, state the required inequality explicitly and
   check it against the banked M18/M20 arithmetic (their contracts are
   frozen — the new row must FIT, not force).
5. **Budgets:** per-row prover-build budget target/rounds/hard-cap; hard
   ceiling 26; if a row cannot plausibly land under ~12 nodes given the
   T0 imports, FACTOR it and say so. Give RE-SEED guidance for M24
   (which of the aborted tree's validated node statements survive
   verbatim — budget calibration only; the tree is re-seeded fresh) and
   state the impact on M28's ratified budget (9/3/13), which must NOT
   change unless you flag it.
6. **Source discipline:** every external carries an exact `refs/` locus
   (file:line-range) into `refs/kitaev-2405.02434/approximate_algebras.tex`.
   If a step needs ground truth not in `refs/`, STOP that route and flag
   it as a reference-acquisition item (L1). The aborted-tree ledger and
   the three challenges above are evidence — cite them by challenge id.
7. **No registry mutation, no proofs.** Design document only.

## Materials (read these; never design against a paraphrase)

- `argument/lemmas/lem-maincb-stage1-maximality.md` — the parked shard
  (ratified contract + binding elevation guidance).
- `argument/lemmas/lem-maincb-structural-assembly.md` (M28) and the
  banked `lem-maincb-*.md` rows, esp. M22, M23, M25, M26, M27, M18, M20
  — frozen contracts you must fit.
- `docs/plans/2026-08-01-MAINCB-REPAIR-design/DESIGN-MAINCB-REPAIR-v2.md`
  sect-4 (the ratified row table incl. M24/M28 skeletons and budgets)
  + `AUDIT-MAINCB-REPAIR.md`.
- `definitions/def-compressed-corner.md`, `def-delta-projection.md`,
  `def-one-dimensional-delta-projection.md`,
  `def-extended-epsilon-cstar-algebra.md`,
  `def-extended-delta-inclusion.md`, `def-maincb-partition-state.md`,
  `def-maincb-witness-ledger.md`, `def-projection-basis.md`.
- Banked corner tooling: `lem-compcb-corner-algebra`,
  `lem-compcb-compressed-unit-norm`, `lem-compcb-compressed-unit-action`,
  `lem-extcb-one-dimensional-corner-dimension`,
  `lem-extcb-corner-dimension-additivity`,
  `lem-maincb-compressed-corner-unit-comparison` (read their contracts
  and exports under `proofs/<id>/export.md`).
- `refs/kitaev-2405.02434/approximate_algebras.tex` loci above.
- `docs/LEARNINGS.md` (2026-07-28 typed-witness laws; 2026-08-02 entries
  if present).

## Deliverables (in DESIGN-M24-NONTRIVIALITY.md)

1. **The option verdicts**: (a)/(b)/(c) each judged with the decisive
   argument; ONE recommendation. For (b): the consumer-survey table
   (M28 skeleton step by step; M25, M19-S3, M27, def-maincb-partition-state
   class structure) with the exact clause that survives or blocks. For
   (c): the frozen-dep analysis.
2. **The final contract package** (for the recommended route): every new
   or amended row — id | one-line ASCII contract verbatim | defs | deps |
   provenance loci | budget target/rounds/hard-cap | new/amended flag.
   Expected shape if (a): one provider row + the M24 contract byte-UNCHANGED
   with the provider added to deps; state explicitly whether M24's
   contract text changes.
3. **The def-layer table**: reused defs; zero new defs or a justification.
4. **The no-T0-invalidation check**: every banked row/locked def/external
   your design touches or neighbours, verdict per item.
5. **The dimension-freeness + ledger-fit audit** (constraint 4).
6. **Proof-plan skeletons** for each new/amended row: numbered node plan
   within budget, per-node import list, the exact tex locus each analytic
   step leans on; plus updated ELEVATION GUIDANCE bullets for the M24
   re-seed (the session-39 binding patterns: constant-choice first child,
   typed-reset provider alone, no pending-sibling citations, explicit
   typing citations).
7. **Re-seed + serial-order guidance**: M24 re-seed steps, then the M28
   launch precondition check (deps all T0 + oracle registered), any
   change to the ratified M28 budget flagged.
8. **An honest risk register**: what a hostile verifier attacks first in
   each new/amended row; the top three ways THIS design could be wrong.
