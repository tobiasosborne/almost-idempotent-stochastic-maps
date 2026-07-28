---
id: lem-stage1-polar-path-transport
kind: lemma
contract: Parameterized polar-path transport: there exist C_path^0, C_pol^0 >= 1 and kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_path >= C_path^0, C_pol >= C_pol^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_pol*(epsilon_r + delta) <= kappa_pol, every U_0, U_1 in calU, and every q in [0, 1] satisfying ||U_1 - U_0|| <= q, C_path*q <= 1/4, and C_path*(q + epsilon_r*q + q^2) < delta - C_pol*(epsilon_r*delta + delta^2), every L_{Z_t} is invertible and every Z_t = (1-t)*U_0 + t*U_1 lies in calUbar_{C_path*(q + epsilon_r*q + q^2)} for t in [0, 1], and, writing u_delta for the unique first component of the inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the map H(t, U_0, U_1) = u_delta(Z_t) is jointly continuous in (t, U_0, U_1), joins U_0 to U_1, and satisfies H(t, cU_0, cU_1) = c*H(t, U_0, U_1) for every c in U(1).
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-path-admissibility
status: stated
af: seeded
workspace: proofs/lem-stage1-polar-path-transport
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 13f, landed verbatim (LaTeX flattened to registry ASCII; incl. the v6 finite-dimensional domain restriction, audit-v5 sect-6 option 1); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). TeX 895-912; parameterized path/loss/guard monotonicity; AUDIT-S1-POLAR-v4.md sect-1.6, sect-3.
owner: A
---

**Status.** **RETRACTED from the rigorous record 2026-07-28 (sweep)** — the af validation (then the 106th rigorous result) was found DEFECTIVE by the independent Stage-1 sweep adjudication (`docs/plans/2026-07-28-13E-BINDER-design/SWEEP-ADJUDICATION-STAGE1.md`; second LEARNINGS entry of 2026-07-28; bead `aism-e1qs`): export node 1.3.1: attaches the parent path-admissibility conclusion to the root-bound explicit u_delta by sameness of notation; the parent contract exports only the anaphoric path formula (no h_delta, no displayed Pi_delta, no typed preimage identity). Status mechanically demoted proved->stated, af validated->seeded; workspace and ledger retained as the re-elevation base; repair folded into the W97 explicit-binder campaign (design v3). The CONTRACT is not in dispute, only the proof.

**Superseded status record (pre-retraction).** af-VALIDATED 2026-07-27 (106th rigorous result): first-pass —
root validated, 9/9 nodes, taint clean (tier routine, zero challenges;
the bare-u_delta parent anaphor resolved cleanly against the explicit
polar-retraction import, unlike the paused 13e). Export in the workspace;
oracle `af-lem-stage1-polar-path-transport` + `fr verify` PASS. Landed
VERBATIM from the audited `DESIGN-S1-POLAR-v6.md` §3 row 13f.