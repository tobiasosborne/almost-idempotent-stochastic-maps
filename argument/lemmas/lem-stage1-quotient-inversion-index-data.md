---
id: lem-stage1-quotient-inversion-index-data
kind: lemma
contract: There is a universal e_idx^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_idx^r and 1 < N = dim_C calX < infinity, the scalar class breve-e = [J] is an isolated fixed point of the smooth breve-sigma, the vertical line iR*J is D-sigma_J-invariant, ||D-breve-sigma_{breve-e} + I|| < 1 in the quotient norm, and det(I - D-breve-sigma_{breve-e}) > 0, so its local index is +1; more precisely, there is a quotient neighborhood calN of [J] such that if [U] in calN is fixed, choose a representative U_0 close to J and c in U(1) with sigma(U_0) = c*U_0, choose a in U(1) with a^2 = c, and use sigma(a*U_0) = conj(a)*sigma(U_0) = a*U_0: the two actual fixed lifts +-a*U_0 lie in the J- and -J-isolation balls, hence equal J and -J, so [U] = [J].
defs: def-approximate-unitary-space; def-lefschetz-fixed-point-data; def-epsilon-cstar-algebra
deps: lem-stage1-uniform-inversion-isolation; lem-stage1-explicit-smooth-unitary-operations; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse; lem-stage1-polar-constant-ledger; lem-stage1-quotient-manifold-package; lem-stage1-quotient-left-inversion; lem-topology-local-index-sign
status: proved
af: validated
workspace: proofs/lem-stage1-quotient-inversion-index-data
provenance: DESIGN-S1-POLAR-v6.md sect-5 downstream row 5, landed verbatim (LaTeX flattened to registry ASCII; incl. the explicit square-root phase-lift clause required by the audits); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80).
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-29): 12-node tree, root
`validated`, taint clean 12/12 (`proofs/lem-stage1-quotient-inversion-
index-data/export.md`; oracle `af-lem-stage1-quotient-inversion-index-
data` pass). Run: tier routine, 8/9 leaves first-pass; two major
challenges on the derivative branch — 1.2 (dependency guard: e_idx^r
had to be locally proved <= e_H^r, e_quot^r before applying the
quotient externals) and 1.2.2 (the tangent-quotient identification /
differentiated intertwining needed explicit local slice charts) — both
repaired in-ledger and freshly verified. Contract transcribed VERBATIM
from the audited `DESIGN-S1-POLAR-v6.md` §5 (final verdict LAND;
projected budget 9/3, actual 12 nodes <= cap 13), incl. the explicit
square-root phase-lift clause.

**Phase-lift obligation (design §5, binding on the proof).** The proof must
include the neighborhood estimate suppressed by the one-line contract:
quotient closeness selects U_0 close to J; continuity and sigma(J) = J make
the quotient phase c close to 1; its two square roots can be labelled so
that a*U_0 is in the J-ball and -a*U_0 is in the -J-ball. This is a
qualitative neighborhood shrink inside the already fixed isolation radius,
not a new analytic coefficient. The contract records the lift because
actual isolation alone does NOT imply quotient isolation (design §6: this
row, not `lem-stage1-extra-fixed-class`, carries the phase-lift).

**W97 amendment (2026-07-28, deps-only).** Deps replaced per the endorsed
rebuild design (`DESIGN-13E-BINDER-v3.md` §1.11; audit chain v3/v3.2,
final VERDICT LAND): the explicit derivative data come from row 13 (A_7)
and phase covariance + the vertical derivative from
`lem-stage1-explicit-smooth-unitary-operations` (+ atlas and smooth polar
inverse); the anaphoric control lemma, the retired smooth-operations
parent, and coherence-naturality are dropped. Contract and defs
BYTE-UNCHANGED.

**Build-granularity discipline (BINDING on the af tree; extends the
user-ratified W98 row-1 discipline of 2026-07-28).** The target is the
design's 9-node skeleton (budget 9/3; hard cap 13). Tree discipline:
(i) ONE early node fixing the ledger tuple W (e_idx^r from its fields,
with e_idx^r <= the isolation/H-space radii already banked) and reading
off the (A_5)/(A_7) operations and derivative data at those fields;
(ii) ONE node for the smooth breve-sigma and the quotient structure at
breve-e (from quotient-left-inversion + quotient-manifold-package);
(iii) ONE node for D-sigma_J: the vertical line iR*J is invariant and
the (A_7) explicit derivative data give the stated form; (iv) ONE node
for the quotient-norm bound ||D-breve-sigma_{breve-e} + I|| < 1;
(v) ONE node for det(I - D-breve-sigma_{breve-e}) > 0; (vi) ONE node
for the square-root phase-lift (quotient-fixed [U] -> actual fixed
lifts +-a*U_0 via sigma(a*U_0) = conj(a)*sigma(U_0), c near 1,
labelled roots); (vii) ONE node for quotient isolation ([U] = [J] via
the J-/-J-isolation balls of uniform-inversion-isolation); (viii) ONE
node for the local index +1 via lem-topology-local-index-sign; (ix) at
most ONE assembly node. Do NOT sub-split routine continuity/norm
estimates. Constants live in the proof body, never the contract.
