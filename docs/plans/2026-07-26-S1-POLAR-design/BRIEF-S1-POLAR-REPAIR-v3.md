# BRIEF — S1-POLAR third repair (fresh designer; re-audit binding)

You are a fresh, independent design mathematician. Prior state:

- `DESIGN-S1-POLAR-v2.md` was sent to a fresh hostile re-audit,
  `AUDIT-S1-POLAR-v2.md`, which returned **REDESIGN** — but confirmed the
  route: the direct-smoothness repair is VALID (the graph equation is a
  degree-two polynomial of finite-dimensional real vector spaces; Lee C.40
  applies pointwise and local smooth graphs glue by uniqueness; the polar
  inverse becomes smooth via chartwise Lee C.34/C.36; no fallback
  approximation and no source acquisition needed), the ENTIRE row-9 constant
  arithmetic recomputes exactly (its §3), dimension-freeness is VALID with
  NO ROUTE-LEVEL ALARM (its §8), and `def-approximate-unitary-space` is
  VALID as specified.
- Exactly four defects killed v2 (its §0), all architectural/contract-
  logical, none mathematical.

`AUDIT-S1-POLAR-v2.md` is BINDING. Its §10 redesign list is your
specification:

1. **Factor the compound rows.** Split row 2
   (`lem-stage1-unitary-chart-control`) into (a) graph
   existence/quantitative-estimate/normal-derivative-invertibility control
   and (b) global Maurer–Cartan/tangent trivialization control. Split row 8
   (`lem-stage1-smooth-unitary-polar-package`) into at least three separate
   producers: smooth-atlas, smooth-polar-inverse, and
   smooth-action/operations (smooth scalar action + smooth μ, σ as maps into
   the embedded manifold). Do the splits NOW — a projected node count with a
   promise to split after measurement was explicitly refuted.
2. **Export a genuine common-witness relation.** The v2 ledger row asserts
   "simultaneously selectable" but its formal conclusion is only scalar
   arithmetic; a consumer sees ∃W·Arithmetic(W) plus separate existential
   analytic theorems, NOT one W satisfying both. Repair per the audit §3:
   EITHER (a) a closed witness-unification row that explicitly identifies
   the common monotone maxima/minima with the witnesses of the analytic
   rows, PLUS a universal scalar lemma quantified over every already
   selected tuple (C_• ≥ 1, 0 < κ_• ≤ 1/2, 0 < e_rect ≤ 1/C_rect); OR (b)
   have every consumer select the analytic witnesses and repeat the
   universal scalar lemma locally. State which option you take and why. The
   data-only `def-stage1-polar-witness-data` stays data-only (it was VALID
   as data, REFUTED as the threading repair — the result DAG, not the
   definition, must export the relation).
3. **Add the quotient fixed-class phase-lift.** Isolation of the actual
   fixed points J, −J does not by itself isolate [J] for the quotient map.
   Add to the quotient-index row (and the `lem-stage1-extra-fixed-class`
   obligation ledger) the explicit step: a quotient fixed class close to [J]
   yields, via σ(cU) = c̄·σ(U), a square root of the quotient phase, and
   scalar naturality, an ACTUAL fixed lift inside the J- or −J-isolation
   ball. The audit confirms the dependencies can support this derivation —
   it must be stated as a proof obligation, not assumed.
4. **Correct the two provenance items.** (a) The two closeness estimates
   ‖μ(U,V) − U·V‖ and ‖σ(U) − U†‖ derive from TeX 845–868 + the polar
   retraction; only the three group defects are literal at TeX 872–874 —
   fix the group-laws row's provenance cell and the §9 disposition line.
   (b) State explicitly that `lem-stage1-rectified-cstar-control`'s proof
   RECONSTRUCTS TeX 672–687 (including exact dagger compatibility and every
   C*-axiom + ‖J‖ = 1) inside its own tree — the landed
   `lem-stage1-exact-unit-rectification` contract exports only exact unit +
   product/unit closeness, and importing stronger content from its proof
   export through the weaker registry contract is forbidden.

Also carry the audit's per-row and per-repair VALID-WITH-CORRECTIONS items
(its §4–§6): the six downstream repairs must depend on the FACTORED rows
(not the compound row 8, not an unthreaded ledger); the corrected
`lem-stage1-extra-fixed-class` dependency list adds the quotient-index and
maximal-simplex rows AND records the phase-lift inside the quotient-index
proof.

## What NOT to redo

Do NOT change: the direct-smoothness route selection (confirmed; Munkres
stays checked-fallback-only), rows 3/4/6/7 (`lem-stage1-polar-retraction`,
`-polar-coherence-naturality`, `-polar-path-admissibility`,
`-inversion-derivative-control` — all VALID as written), the row-9
arithmetic content (VALID; only its logical packaging changes), the two
definition shards' content (both VALID as data), or the dimension-freeness
§7 analysis. Keep every retained contract verbatim unless a named audit
correction touches it, and mark each change against the audit item that
forced it.

## Read (all binding)

`AUDIT-S1-POLAR-v2.md` (the binding re-audit), `AUDIT-S1-POLAR.md`,
`BRIEF-S1-POLAR.md` (original constraints), `DESIGN-S1-POLAR-v2.md` (the
base you are repairing), the landed shards
(`lem-stage1-exact-unit-rectification.md`,
`lem-stage1-quantitative-inverse-function.md`,
`lem-topology-quotient-manifold.md`, `lem-topology-lefschetz-hopf.md`,
`lem-topology-local-index-sign.md`, `lem-topology-finite-triangulation.md`,
`lem-topology-orientable-top-cohomology.md`),
`DESIGN-FUDW-DECOMP-v4.1.md` §2.4/§2.6/§4.1/R14/R35,
`refs/kitaev-2405.02434/approximate_algebras.tex` (407–440, 458, 560,
655–912, 943–955), and the Lee/Munkres loci the audit pinned. Cite exact
loci for every claim.

## Deliverable — write `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v3.md`

Same discipline as v2, plus:

- a §0 verdict stating exactly what changed vs v2 and which audit item
  forced each change;
- the factored proposal table (expect ~12–13 analytic rows after the
  mandatory splits), per-row one-line self-contained contracts, exact deps
  by id (acyclic; existing shards or earlier rows only), provenance loci,
  node budgets (≤12 / depth ≤3) — budgets must now be honest per FACTORED
  row;
- the witness-unification architecture (option (a) or (b) above), stated as
  closed contracts;
- the corrected six downstream repairs and the corrected
  `lem-stage1-extra-fixed-class` obligation ledger including the
  phase-lift;
- dimension-freeness audit (carry v2 §7 forward; note anything the
  factoring changes);
- a serial landing order that is a genuine topological sort;
- a disposition table covering EVERY finding of `AUDIT-S1-POLAR-v2.md`
  (CLEARED-BY / REFUTED-WITH-LOCUS / ESCALATED).

## Hard constraints

Design only; write ONLY inside `docs/plans/2026-07-26-S1-POLAR-design/`;
no registry or definitions/ mutation; no status promotion; no guessed radii
or numerical constants (TeX 458 named-witness discipline stands); NOT IN
LOCAL REFS discipline; an honestly escalated gap beats a papered-over one.
