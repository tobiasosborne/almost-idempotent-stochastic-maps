---
id: lem-stage1-polar-path-admissibility
kind: lemma
contract: Joint projected-straight-path admissibility: there exist universal C_path, C_pol >= 1, kappa_pol in (0, 1/2] such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_pol*(epsilon_r + delta) <= kappa_pol, and U_0, U_1 in calU, if 0 <= q <= 1, ||U_1 - U_0|| <= q, C_path*q <= 1/4, and C_path*(q + epsilon_r*q + q^2) < delta - C_pol*(epsilon_r*delta + delta^2), then for Z_t = (1-t)*U_0 + t*U_1 every L_{Z_t} is invertible, every Z_t in calUbar_{C_path*(q + epsilon_r*q + q^2)}, and H(t, U_0, U_1) = u_delta(Z_t) is jointly continuous in all displayed variables, joins U_0 to U_1, and obeys H(t, cU_0, cU_1) = c*H(t, U_0, U_1) for c in U(1).
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction; lem-stage1-polar-coherence-naturality
status: proved
af: validated
workspace: proofs/lem-stage1-polar-path-admissibility
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 7, landed verbatim (LaTeX flattened to registry ASCII; incl. the v6 finite-dimensional domain restriction, audit-v5 sect-6 option 1); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). Source loci TeX 895-912 plus derivation from 655-661, 699-725; exact identity Z_t^dagger bold-dot Z_t - J = t*(t-1)*(U_1 - U_0)^dagger bold-dot (U_1 - U_0).
owner: A
---

**Status.** af-VALIDATED 2026-07-27 (96th rigorous result): first-pass —
root validated, 12/12 nodes, taint clean (tier routine: prover high /
verifiers high, zero challenges). Export in the workspace; oracle
`af-lem-stage1-polar-path-admissibility` + `fr verify` PASS. Landed
VERBATIM from the audited `DESIGN-S1-POLAR-v6.md` §3 row 7 (final verdict
LAND; carries the v6 finite-dimensional insertion).

**Derivation obligation (design §4).** Use the exact quadratic identity and
L_{Z_t} = L_{U_0} + t*L_{U_1 - U_0} with one Neumann comparison. Joint
continuity and scalar equivariance use one open polar domain.
