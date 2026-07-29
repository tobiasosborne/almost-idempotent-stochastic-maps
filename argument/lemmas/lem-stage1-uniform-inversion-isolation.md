---
id: lem-stage1-uniform-inversion-isolation
kind: lemma
contract: There are universal e_iso^r > 0, r_iso > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_iso^r, J and -J are the only fixed points of the smooth sigma in their respective ambient r_iso-balls.
defs: def-epsilon-cstar-algebra; def-approximate-unitary-space
deps: lem-stage1-quantitative-inverse-function; lem-stage1-explicit-smooth-unitary-operations; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse; lem-stage1-polar-constant-ledger
status: proved
af: validated
workspace: proofs/lem-stage1-uniform-inversion-isolation
provenance: DESIGN-S1-POLAR-v6.md sect-5 downstream row 1, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80).
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §5 (final verdict LAND). Not proved in-repo;
af elevation per the design's projected budget 6/3. Discharges the
"actual inversion isolation near J, -J" obligation of the corrected
`lem-stage1-extra-fixed-class` ledger (design §6).

**W97 amendment (2026-07-28, deps-only).** Deps replaced per the endorsed
rebuild design (`DESIGN-13E-BINDER-v3.md` §1.11; audit chain v3/v3.2,
final VERDICT LAND): derivative information comes from row 13 (A_7) and
smoothness/regularity of the explicit sigma from
`lem-stage1-explicit-smooth-unitary-operations` (+ atlas and smooth polar
inverse, its antecedents); the retracted control lemma and the retired
smooth-operations parent are dropped. Contract and defs BYTE-UNCHANGED.

**Build-granularity discipline (BINDING on the af tree; extends the
user-ratified W98 row-1 discipline of 2026-07-28).** The target is the
design's 6-node skeleton (budget 6/3; hard cap 10). Tree discipline:
(i) ONE early node fixing the row-13 witness tuple W and reading off
the (A_7) derivative bound at s = +1/-1 with r = r_iso and the (R)
guards (e_iso^r and r_iso are defined from the tuple's e_S1/r_iso
fields); (ii) ONE node for the smooth/regularity inputs of the explicit
sigma from the smooth-operations bridge (+ atlas/smooth-polar-inverse
antecedents); (iii) ONE node applying the quantitative inverse function
external to F_s - id (derivative within C_der*(epsilon_r + r_iso) of
-2*I, hence invertible with a quantitative radius); (iv) ONE node per
sign concluding the fixed-point isolation in the ambient r_iso-ball —
do NOT sub-split routine norm estimates. Constants live in the proof
body, never the contract; every smallness inference cites its guard
node explicitly.

**af-VALIDATED 2026-07-29 (downstream row 1, post-row-13 serial
order).** First-pass run under the binding build-granularity discipline
above (tier routine, fresh codex verifier per node): root validated,
7/7 live nodes (design budget 6; hard cap 10), taint clean, 5 rounds,
one in-run challenge repaired (an undeclared dependency at node 1.5,
fixed by a dependency-backed bridge node) and re-verified fresh. Export
in the workspace; oracle `af-lem-stage1-uniform-inversion-isolation` +
`fr verify` PASS. This status flip is a mechanical reflection of the
codex ledger.
