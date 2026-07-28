# Hostile audit of `DESIGN-13E-BINDER-v3.1.md`

1. **Location:** §1, contract line 6, in the graph-family clause and the
   characterization of the polar inverse; §1 line 19, which claims that every
   former anaphor has a contract-local typed referent.
   **Defect:** the redrafted
   `lem-stage1-explicit-smooth-unitary-operations` contract is still not fully
   binder-closed under the two 2026-07-28 typed-witness laws.  In
   “such that `g_V(A^par)` is the unique `A^perp` ...,” neither `V` nor
   `A^par` is explicitly quantified in that pointwise predicate.  The family
   notation `(g_V)_{V in calU}` types the family, but it does not syntactically
   quantify the later free occurrence of `A^par`; compare the repository's
   binder-closed transport contracts, which say “for every `U` ... and
   `A^par` ...”.  Likewise the two displayed inverse identities use `X` and
   `(U,H)` without stating `X in S_delta` and
   `(U,H) in calU x B_delta^{calH}(J)`.  These readings are recoverable by
   conventional implicit universal closure, but that is precisely the
   convention this repair is required not to rely on.  The rest of the noun
   and symbol walk succeeds: the algebra binds its reserved notation;
   `A^perp` is bound by the unique-element description; `f_V`, `chi_V`,
   `calA_delta`, `calM_delta`, `Pi_delta`, `S_delta`, `(u_delta,h_delta)`,
   the three `C1` maps, and the three smooth maps all receive local formulas,
   types, or defining properties; and every noun phrase using “displayed,”
   “same,” or “resulting” has a preceding local referent.
   **Severity: MAJOR.**
   **Prescribed repair:** replace the graph predicate by “such that, for every
   `V in calU` and every
   `A^par in B_{2delta}^{icalH}(0)`, `g_V(A^par)` is the unique ...”, and
   state the inverse identities for every `X in S_delta` and every
   `(U,H) in calU x B_delta^{calH}(J)` (or as two typed composition identities).
   Submit that exact contract to another fresh binder audit before landing or
   seeding.

No further defect was found in the requested focused checks.  After the
quantifier repair, the statement is a physical one-line house-style contract
and the old 15-node smooth-operations tree shows that its simpler,
already-typed restriction/corestriction, composition, scalar-preservation,
inverse-uniqueness, covariance, and derivative-identification proof is
realistic at the stated 12/18 cap.  The hypotheses are jointly satisfiable:
for an exact finite-dimensional C*-algebra (`epsilon_r = 0`), choose positive
`delta` below the finitely many graph, polar, and group-domain thresholds;
then `lem-stage1-unitary-graph-control`,
`lem-stage1-smooth-unitary-atlas`, `lem-stage1-polar-retraction`,
`lem-stage1-smooth-polar-inverse`, and the explicit domain bridge supply one
model of every premise.  The covariance identities are not among those
premises, so the conclusion is non-vacuous.

The intended downstream instantiations are also typed.  The v3 13e and 13g
proofs do not consume this smooth bridge: they produce row-13 clauses `(A_5)`
and `(A_7)`.  At the ledger's admissible `delta_*`, `(A_2)` supplies the
displayed graph family and atlas input, `(A_4)` supplies the displayed polar
map and inverse, `(A_5)` supplies domain membership and the identical `C1`
operations, and the two smooth-upgrade externals supply the smooth structure
and the smooth polar inverse.  Thus uniform isolation, quotient left
inversion, and quotient inversion-index data possess the typed inputs needed
to apply the repaired bridge; quotient manifold deliberately proves only the
binder-free scalar action locally.  The v3.1 external-registration list is
exactly its two `defs:` entries followed by its five `deps:` entries.
Finally, the MINOR-5 row is factually accurate: the actual
`lem-finite-polyhedron-maximal-simplex-placement` shard has empty `defs:` and
`deps:`, no workspace, an algebra-independent finite-poset contract, and no
Stage-1 definite description, so it needs no repair action and does not alter
the touched-shard count.

VERDICT: REJECT (the redrafted contract still relies on implicit universal closure for its graph predicate and inverse identities)
