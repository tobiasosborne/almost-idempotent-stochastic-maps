# BRIEF — S1-POLAR fifth repair (prescribed; audit-v4 binding; ROW 13 ONLY)

You are a fresh, independent design mathematician executing a PRESCRIBED
repair of EXACTLY ONE row. `AUDIT-S1-POLAR-v4.md` is BINDING. Its verdicts:
row-13 clauses A₁ (rectification), A₂ (graph), A₄ (polar), and R
(arithmetic) are VALID as written in v4; clauses A₃ (Maurer–Cartan), A₅
(group laws, v4 label (A_6)), A₆ (path, v4 (A_7)), and A₇ (derivative, v4
(A_8)) are REFUTED on binder/domain defects; the budget projection is
REFUTED pending the repair; everything else in v4 (rows 1–12, downstream
rows + defs, obligation ledger, dimension-freeness, definitions, serial
order, sources) is VALID and byte-verified — DO NOT TOUCH ANY OF IT.

## The four defects to fix (audit §§1.3, 1.5–1.7, 2.2, 3 — read them)

1. **Silent domain weakening:** v4's group, path, and derivative clauses
   quantify over "finite-dimensional" exact-unit ε_r-C*-algebras; the
   producers (rows 6, 7, 8) quantify over EVERY exact-unit
   ε_r-C*-algebra. Restore the literal producer domains — do not insert
   `finite-dimensional` anywhere the producer lacks it.
2. **Conditionalized conclusions:** the group and derivative clauses turned
   affirmative producer conclusions into `if`-conditionals. Restate them
   affirmatively, exactly as the producers conclude (with W's constants
   substituted).
3. **Unbound maps:** A₃ asserts "the family" without quantification and
   imports graph-producer content into the Maurer–Cartan conclusion; A₇
   places the polar inverse and graph package in an antecedent. Bound
   variables in one conjunct do NOT scope over later conjuncts. Repair per
   audit §6.2: give each clause explicit object-level binders/definitions
   for the maps it constrains — introduce the unique maps by their defining
   properties inside the clause (e.g. "for every V and A∥ in the displayed
   domains, the unique g_V(A∥) with f_V(A∥+g_V(A∥))=0 — whose existence
   and uniqueness clause A₂ asserts — satisfies …"), or use antecedents
   that encode EXACTLY the dependency data already guaranteed by earlier
   conjuncts, adding no new guard and no new conclusion. The datum-only
   tuple W still carries only scalars, never maps.
4. **Budget honesty:** after the repair, re-project row 13's af budget
   under ONE declared counting convention. If the seven producer
   applications + monotonicity do not each close in one atomic node and
   the honest projection exceeds 12 nodes / depth 3, factor parameterized
   monotonicity/transport HELPER ROWS that receive the same W — do NOT
   split into unrelated existential tuples and do NOT raise the cap. If
   you add helper rows, give them the full row discipline (contract, defs,
   deps, provenance, budget) and insert them in the serial order.

Clause content discipline: preserve every already-correct estimate and
identity in A₁, A₂, A₄, R verbatim; in the four repaired clauses preserve
every listed producer conclusion (all seven group estimates/identities;
joint continuity + equivariance for the path; chart retention + the −2I
derivative bound; MC distortion + both equivariance identities) — nothing
dropped, nothing added.

## Deliverable — write `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v5.md`

Full standalone document: copy v4 forward byte-stable EXCEPT (a) the
repaired row-13 contract (and any new helper rows), (b) the re-projected
budget, (c) §0 = exact delta vs v4 citing the audit item per change, and
(d) the disposition table now covering EVERY finding of
`AUDIT-S1-POLAR-v4.md` (CLEARED-BY / unchanged-VALID).

## Hard constraints

Design only; write ONLY inside `docs/plans/2026-07-26-S1-POLAR-design/`;
no registry/definitions mutation; no status promotion; no meta-language
("the contract of", "the conclusion of", row ids inside math); no guessed
constants; NOT IN LOCAL REFS discipline.
