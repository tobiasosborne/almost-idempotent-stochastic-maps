# BRIEF — the Stage-1 nontrivial-projection ENDGAME (trace rows + extra-fixed-class + the three G-S1 producers)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation; everything you produce is escalated for verbatim landing after a
fresh hostile audit. Write your design to
`docs/plans/2026-07-29-S1-ENDGAME-design/DESIGN-S1-ENDGAME.md`.

## The objective

Produce registry-ready contracts, dependency lists, def-layer requirements,
provenance loci, and per-row af budgets for the ENTIRE remaining chain from
the (now fully af-validated) Stage-1 polar substrate to the three **G-S1
split producers** that gate the MAIN campaign:

**Block A — the trace rows (`DESIGN-S1-POLAR-v6.md` §9 step 28, "separately
designed", never designed):**
1. `lem-stage1-exterior-cohomology`
2. `lem-stage1-left-inversion-associated-graded`
3. `lem-stage1-left-inversion-trace`

These carry Kitaev's Proposition `prop_H-group`
(`refs/kitaev-2405.02434/approximate_algebras.tex:971-972`, proof at
`:1023-1040`): for a connected CW complex M with finite-dimensional real
cohomology that is an H-space with a left inversion map sigma,
`Tr sigma^{*k} = (-1)^k dim H^k(M;R)`. You choose the factoring into the
three named rows (the names are ratified; their CONTENT split is yours to
design — e.g. Hopf-algebra exterior structure / associated-graded argument /
the trace identity). The already-T0 topology rows
`lem-topology-hopf-structure`, `lem-topology-kunneth-cross-product`,
`lem-topology-orientable-top-cohomology` were landed for exactly this
purpose — read their contracts and consume them rather than re-deriving.

**Block B — the corrected `lem-stage1-extra-fixed-class`
(`DESIGN-S1-POLAR-v6.md` §9 step 29):** the Lefschetz–Hopf contradiction
producing a second fixed class `breve-U != breve-e` of `breve-sigma`
(source: the proof of `lem_nontriv_projection`,
`approximate_algebras.tex:936-969`). Its ten-item dependency list is
ALREADY FIXED by the audited `DESIGN-S1-POLAR-v6.md` §6 (read it verbatim);
NINE of the ten are now af-validated T0 — the only missing one is
`lem-stage1-left-inversion-trace` from Block A. Your job here is the
one-line contract, the proof-skeleton, and the budget; do NOT change the
§6 dependency list. Note the audits' placement decisions: the square-root
phase-lift is a contract clause of `lem-stage1-quotient-inversion-index-data`
(T0, banked 2026-07-29) and is CONSUMED here, not re-proved; finiteness +
maximal-simplex placement of the fixed set under the only-fixed-class
hypothesis comes from `lem-finite-polyhedron-maximal-simplex-placement` (T0)
plus `lem-topology-lefschetz-hopf` (T0).

**Block C — the three G-S1 producers (`DESIGN-MAIN-STRUCTURE-v5.md` §5;
ids ratified, contracts never designed):**
1. `lem-stage1-rectified-nontrivial-projection` — the registry form of
   Kitaev's Lemma `lem_nontriv_projection`
   (`approximate_algebras.tex:917-935`): every (suitably rectified /
   exact-unit) epsilon-C*-algebra with `1 < dim < infinity` has a
   NONTRIVIAL O(epsilon)-projection (both P and I-P nonvanishing). It
   consumes Block B's extra fixed class, the phase-lift (via the
   quotient-index row), the isolation balls
   (`lem-stage1-uniform-inversion-isolation`, T0), and the bridge
   `P = (2I + U + U^dagger)/4` turning a near-Hermitian unitary fixed
   point into an O(delta+epsilon)-projection (`:929-935`). Decide and
   state precisely how the exact-unit rectification layer
   (`lem-stage1-exact-unit-rectification`,
   `lem-stage1-rectified-cstar-control`/`-transport`, all T0) enters —
   the MAIN consumer calls this on compressed corners `S_{P_j}` which are
   extended epsilon-C*-algebras, NOT exact-unit ones. This
   hypothesis-interface decision (what exactly the contract assumes:
   extended vs exact-unit vs rectified) is THE central design risk;
   the audits of MAIN-v5 already fixed the consumer-side wording of
   M19-S1 — read it and match it.
2. `lem-stage1-original-complementary-pair` — producing universal
   `C_np, e_np`: inside the relevant corner, the nontrivial projection
   P' and its complement `P'' = tilde-P_m - P'` form a quantitatively
   controlled complementary pair (`approximate_algebras.tex:1419-1424`;
   `tilde-P_m = Co_{P_m}(P_m)` is the corner unit). The corner-algebra
   layer is T0 (`lem-compcb-corner-algebra` and the compcb block).
3. `lem-stage1-fresh-two-point-inclusion` — producing universal
   `C_pair, e_pair`: the two-point commutative C*-algebra
   O(epsilon)-includes into the corner via
   `v^(2)(Pi') = P'`, `v^(2)(Pi'') = P''` (`:1419-1424`), with the
   unit/defect clauses M19-S1 needs.

**The consumer interface you must match:** M19-S1
`lem-maincb-stage1-call-envelope` in `DESIGN-MAIN-STRUCTURE-v5.md` §6
depends on exactly these three producer ids and states that "the three
G-S1 producers and the literal old-side compression furnish an explicit
Stage-1 raw-call datum satisfying M15 with base scale t_1 = K_1*epsilon".
Your producer contracts must make that derivation SUPPORTED — quote the
M19-S1 contract in your interface-match section and verify clause-by-clause.

## Hard constraints (all BINDING)

1. **Contracts:** one physical line each, flattened registry ASCII (no
   LaTeX), no numerical value of any universal constant (named existential
   witnesses like `C_np, e_np` are correct form). Every definite
   description a contract binds must have a TYPED-WITNESS provider among
   its deps/defs (LEARNINGS 2026-07-28 law i); parameterized rows fix
   provider witnesses FIRST and transport receiving fields by monotonicity
   (law ii).
2. **Imports:** every new row's deps must be af-validated T0 rows, `cited`
   leaves, or rows earlier in YOUR serial order. No new row may import the
   retired parents (`lem-stage1-approximate-group-laws`,
   `lem-stage1-smooth-unitary-operations`) or any stated/none row.
3. **Dimension-freeness:** every constant universal, independent of
   `dim calX`, amplification, and block data. Kitaev's `O(...)` claims
   must be priced into named constants with explicit provider rows or
   in-proof derivations; flag any step where dimension could leak.
4. **Budgets:** per-row prover-build budget (nodes / rounds) with hard cap
   26; if any single row cannot plausibly land under ~12 nodes given the
   T0 imports, FACTOR it and say so. Include a per-row
   build-granularity note (one node per design-skeleton step) in the W98
   discipline style.
5. **Def layer:** enumerate every definition each contract uses; REUSE the
   existing shards (`def-approximate-unitary-space`,
   `def-epsilon-cstar-algebra`, `def-h-space-left-inversion`,
   `def-lefschetz-fixed-point-data`, `def-delta-projection`,
   `def-compressed-corner`, `def-projection-basis`,
   `def-extended-epsilon-cstar-algebra`, `def-extended-delta-inclusion`,
   ...; read `definitions/INDEX.md`). If a genuinely new def shard is
   unavoidable (e.g. for the cohomology/CW vocabulary of Block A or the
   two-point commutative algebra), give its full proposed content,
   provenance locus, and `consensus`/`cited` tag — each new def is a USER
   ratification item, so minimize their number and say why each is
   unavoidable. BSc/MSc common knowledge (singular cohomology, CW complex,
   graded algebra, cup product) needs NO def shard — do not shard it.
6. **Source discipline:** every external you propose must carry an exact
   `refs/` locus (file:line-range). The Kitaev tex is
   `refs/kitaev-2405.02434/approximate_algebras.tex` (clean LaTeX, no OCR
   issues). If a step needs a published theorem NOT in `refs/` (e.g. Hopf's
   theorem on H-space cohomology beyond what
   `lem-topology-hopf-structure` already carries, Leray–Hirsch, Borel's
   structure theorem), STOP that route and either re-route through the
   existing T0 topology rows or flag it as a reference-acquisition item —
   do NOT design around an unavailable ground truth (L1).
7. **No registry mutation, no proofs.** Design document only. The failed
   ledger of any prior related run and all audited designs are evidence;
   cite them by path:line.

## The available T0 inventory (verified 2026-07-29)

Stage-1 polar block (ALL af-validated): rows 1-13 incl.
`lem-stage1-polar-constant-ledger` (the keystone; clauses (A_1)-(A_8)),
`lem-stage1-explicit-group-operations`-family, atlas/smooth-polar-inverse,
transports, `lem-stage1-uniform-inversion-isolation`,
`lem-stage1-quotient-manifold-package`, `lem-stage1-quotient-left-inversion`
(H-space + left inversion on breve-calU),
`lem-stage1-quotient-inversion-index-data` (isolated index +1 + the
square-root phase-lift), `lem-stage1-quotient-finite-cw` (finite polyhedron
/ finite CW), `lem-finite-polyhedron-maximal-simplex-placement`,
`lem-stage1-exact-unit-rectification`, `lem-stage1-rectified-cstar-control`,
`lem-stage1-rectified-cstar-transport`.
Topology leaves (ALL af-validated): `lem-topology-quotient-manifold`,
`lem-topology-finite-triangulation`, `lem-topology-lefschetz-hopf`,
`lem-topology-local-index-sign`, `lem-topology-orientable-top-cohomology`,
`lem-topology-hopf-structure`, `lem-topology-kunneth-cross-product`.
Corner/compression layer (af-validated): the compcb block incl.
`lem-compcb-corner-algebra`; the extcb block (except the side row
`lem-extcb-exact-target-approximation`, stated — do not import it).
Read the exact contracts in `argument/lemmas/` — never design against a
paraphrase.

## Known risks to address explicitly

- **R1 (interface):** extended vs exact-unit hypothesis on
  `lem-stage1-rectified-nontrivial-projection` (see Block C item 1).
  Kitaev reduces WLOG to exact unit (`:922`); our rectification layer is
  quantitative — price the reduction.
- **R2 (Block A ground truth):** `prop_H-group`'s proof uses the Hopf
  structure of `H^*(M;R)` for a connected H-space with finitely generated
  cohomology. Verify what `lem-topology-hopf-structure` +
  `lem-topology-kunneth-cross-product` already give (read their contracts
  and exports under `proofs/`) and design Block A to close the REMAINING
  gap only. If the remaining gap needs a source not in `refs/`, flag it
  (constraint 6).
- **R3 (N=1 / dim=1 edges):** the producers require `1 < dim`; the
  quotient rows have N=1 special cases; make every dimension hypothesis
  explicit in the contracts.
- **R4 (cascade):** confirm no proposed contract wording forces an
  amendment of any T0 row or any byte-matched external registered in an
  existing validated workspace (list the workspaces you checked).

## Deliverables (in DESIGN-S1-ENDGAME.md)

1. A row table per block: proposed id | one-line contract | defs | exact
   deps | provenance loci | budget (nodes/rounds) | feasibility verdict.
2. The serial landing + elevation order across all seven rows, merged with
   nothing else (G-S1 unblocks M19-S1..M28 upon completion — state this
   hand-off explicitly).
3. A per-row proof skeleton (numbered steps, one af node each).
4. The def-layer table (reused defs; any proposed new defs in full).
5. The dimension-freeness audit.
6. The interface-match check against M19-S1 (clause-by-clause).
7. An honest risk register: for each row, what a hostile verifier will
   attack first.
