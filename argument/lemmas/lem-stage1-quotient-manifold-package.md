---
id: lem-stage1-quotient-manifold-package
kind: lemma
contract: There is a universal e_quot^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_quot^r and 1 < N = dim_C calX < infinity, breve-calU = calU_e/U(1) is a connected compact orientable smooth manifold without boundary of real dimension N - 1.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-maurer-cartan-trivialization; lem-stage1-smooth-unitary-atlas; lem-stage1-polar-constant-ledger; lem-topology-quotient-manifold
status: stated
af: none
provenance: DESIGN-S1-POLAR-v6.md sect-5 downstream row 2, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80).
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §5 (final verdict LAND). Not proved in-repo;
af elevation per the design's projected budget 8/3. Discharges the
"connected compact orientable positive-dimensional smooth quotient"
obligation (design §6): smooth embedded atlas/action, free proper scalar
action, quotient dimension, closedness, and Maurer-Cartan orientation,
via rows 3, 9, 11 and the T0 `lem-topology-quotient-manifold`.

**W97 amendment (2026-07-28, deps-only).** Deps replaced per the endorsed
rebuild design (`DESIGN-13E-BINDER-v3.md` §1.11; audit chain v3/v3.2,
final VERDICT LAND): the retired smooth-operations parent is dropped in
favour of the LOCAL binder-free scalar-action proof (ambient scalar
multiplication is smooth, preserves calU by the exact unitary equations
and an explicit right inverse, and restricts/corestricts through the
sound embedded atlas) — depending on the new smooth bridge here would
needlessly couple the quotient construction to a chosen delta and its
polar antecedents. Contract and defs BYTE-UNCHANGED.
