# BRIEF — S1-POLAR fourth repair (prescribed; audit-v3 binding; NARROW)

You are a fresh, independent design mathematician executing a PRESCRIBED
narrow repair. `AUDIT-S1-POLAR-v3.md` is BINDING. It found exactly ONE
substantive defect and ONE transcription defect in `DESIGN-S1-POLAR-v3.md`;
everything else was VALID (all locus checks, the 13-row factoring, the
dependency DAG, the dimension-freeness audit, the phase-lift, the
downstream architecture, both definition shards, the serial order shape).

## Defect 1 (fatal) — row 13 is meta-level

`lem-stage1-polar-constant-ledger` in v3 quantifies over contract TEXT
("after replacing the leading existential constants in the contracts
of..."). The registry contract line must be an object-level mathematical
statement (`argument/README.md:9-16,24-28,42-46,73-76`).

Apply the audit's repair option 1 (`AUDIT-S1-POLAR-v3.md` §0.1, its
preferred option — it preserves the architecture):

- Keep row 12 (`lem-stage1-polar-scalar-arithmetic`) EXACTLY as in v3.
- Replace row 13's contract by an object-level root of the form
  ∃W [A₁(W) ∧ A₂(W) ∧ A₃(W) ∧ A₄(W) ∧ A₆(W) ∧ A₇(W) ∧ A₈(W) ∧ R(W)]
  where A₁,…,A₈ are the SEVEN fully restated parameterized conclusions of
  v3 rows 1 (rectified C*-control), 2 (graph control), 3 (Maurer–Cartan),
  4 (polar retraction), 6 (group laws), 7 (path admissibility), and 8
  (inversion derivative) — restated INLINE as mathematical predicates of
  the tuple W's fields (the same algebras, graph maps g_V, polar inverse
  (u_δ, h_δ), group maps μ, σ, scales), NOT by reference to any contract —
  and R(W) explicitly states the four finite-minimum equations (δ*, ε*^r,
  e_S1, r_iso as the exact minima of row 12) and all scalar conclusions of
  row 12's conclusion list. No phrase may refer to "the contract of",
  "replacing constants", "the full conclusion of", or any row id inside
  the mathematical statement. The contract will be LONG — that is
  acceptable; meta-language is not. Deps stay: rows 1,2,3,4,6,7,8,12.
- Re-project row 13's af budget honestly against the ≤12-node/depth-3 cap
  for the ACTUAL object-level root you write. If the honest projection
  exceeds the cap, split the conjunction into two witness rows (e.g.
  analytic-witness join A₁–A₈ and a final row adding R) and say so.

## Defect 2 (transcription) — six downstream rows lack `defs`

Add exactly the definition imports the audit prescribed
(`AUDIT-S1-POLAR-v3.md` §0.2):

- `lem-stage1-uniform-inversion-isolation`: `def-epsilon-cstar-algebra`;
  `def-approximate-unitary-space`.
- `lem-stage1-quotient-manifold-package` and
  `lem-stage1-quotient-finite-cw`: `def-approximate-unitary-space` (+
  `def-epsilon-cstar-algebra` where the contract names the algebra).
- `lem-stage1-quotient-left-inversion`: `def-approximate-unitary-space`;
  `def-h-space-left-inversion`; `def-epsilon-cstar-algebra`.
- `lem-stage1-quotient-inversion-index-data`: `def-approximate-unitary-space`;
  `def-lefschetz-fixed-point-data`; `def-epsilon-cstar-algebra`.
- `lem-finite-polyhedron-maximal-simplex-placement`: none.

## What NOT to change

EVERYTHING ELSE. Copy `DESIGN-S1-POLAR-v3.md` forward verbatim: rows 1–12,
the six downstream contracts (adding only `defs`), the obligation ledger,
§1 sources, §2 (rewrite only its description of the row-13 architecture to
match the object-level form), §7 dimension-freeness, §8 definitions, §9
serial order (unchanged order; row 13's step now executable), §10 →
becomes a disposition of AUDIT-S1-POLAR-v3.md's findings instead. Mark the
two changes against the audit items that forced them.

## Deliverable — write `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v4.md`

Full standalone document (same structure as v3), with a §0 stating exactly
the two changes, and a disposition table covering EVERY finding of
`AUDIT-S1-POLAR-v3.md` (CLEARED-BY / unchanged-VALID).

## Hard constraints

Design only; write ONLY inside `docs/plans/2026-07-26-S1-POLAR-design/`;
no registry/definitions mutation; no status promotion; no guessed
constants; the row-13 contract must be readable as a single self-contained
mathematical sentence-complex with every symbol quantified inside it.
