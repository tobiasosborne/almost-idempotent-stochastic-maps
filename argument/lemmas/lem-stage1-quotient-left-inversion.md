---
id: lem-stage1-quotient-left-inversion
kind: lemma
contract: There is a universal e_H^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_H^r, the scalar-equivariant mu, sigma and the jointly continuous projected straight paths descend to breve-calU; the descended multiplication makes it a connected H-space, and the descended smooth map breve-sigma is a left inversion.
defs: def-approximate-unitary-space; def-h-space-left-inversion; def-epsilon-cstar-algebra
deps: lem-stage1-explicit-smooth-unitary-operations; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse; lem-stage1-polar-constant-ledger; lem-stage1-quotient-manifold-package
status: proved
af: validated
workspace: proofs/lem-stage1-quotient-left-inversion
provenance: DESIGN-S1-POLAR-v6.md sect-5 downstream row 4, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80).
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-29): 10-node tree, root
`validated`, taint clean 10/10 (`proofs/lem-stage1-quotient-left-inversion/
export.md`; oracle `af-lem-stage1-quotient-left-inversion` pass). Run:
tier routine, 6/7 leaves first-pass; node 1.6 (smoothness of the
descended inversion) drew one major challenge (quotient-submersion/
local-section properties outside the allowed externals) and was repaired
in-ledger with two bridging substeps, both freshly verified. Contract
transcribed VERBATIM from the audited `DESIGN-S1-POLAR-v6.md` §5 (final
verdict LAND; projected budget 8/3, actual 10 nodes ≤ cap 12).
Discharges the "continuous H-space and left inversion; smooth
breve-sigma" obligation (design §6) from rows 5-7 and 11.

**W97 amendment (2026-07-28, deps-only).** Deps replaced per the endorsed
rebuild design (`DESIGN-13E-BINDER-v3.md` §1.11; audit chain v3/v3.2,
final VERDICT LAND): the explicit group operations and paths come from
row 13 (A_5)-(A_6); smoothness and covariance for those same maps from
`lem-stage1-explicit-smooth-unitary-operations` (+ atlas and smooth polar
inverse); coherence-naturality, the retired group-laws parent, the
path-admissibility dep, and the retired smooth-operations parent are
dropped. Contract and defs BYTE-UNCHANGED.

**Build-granularity discipline (BINDING on the af tree; extends the
user-ratified W98 row-1 discipline of 2026-07-28).** The target is the
design's 8-node skeleton (budget 8/3; hard cap 12). Tree discipline:
(i) ONE early node fixing the ledger tuple W (e_H^r from its fields)
and reading off the (A_5) group operations and (A_6) projected paths at
those fields; (ii) ONE node for smoothness/scalar-covariance of the
same mu/sigma from the explicit smooth bridge (+ atlas/smooth-polar-
inverse antecedents); (iii) ONE node for descent of mu/sigma/paths to
breve-calU by the covariance identities (mu(cU,dV)=cd*mu(U,V),
sigma(cU)=conj(c)*sigma(U), H(t,cU_0,cU_1)=c*H(t,U_0,U_1)) through the
quotient-manifold-package structure; (iv) ONE node each for: the
descended multiplication making breve-calU an H-space (units from
mu(J,U)=mu(U,J)=U), connectedness (paths), smoothness of breve-sigma,
and the left-inversion identity (mu(sigma(U),U) approx J descends to
the H-space left inversion per def-h-space-left-inversion) — one node
per design-skeleton step, do NOT sub-split routine
quotient-topology/continuity steps. Constants live in the proof body,
never the contract.
