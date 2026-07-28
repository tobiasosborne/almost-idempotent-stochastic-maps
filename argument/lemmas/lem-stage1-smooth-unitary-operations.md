---
id: lem-stage1-smooth-unitary-operations
kind: lemma
contract: Smooth action/operations upgrade: under lem-stage1-approximate-group-laws, lem-stage1-smooth-unitary-atlas, and lem-stage1-smooth-polar-inverse, the scalar action U(1) x calU -> calU, (c, U) |-> cU, and the same maps mu: calU x calU -> calU, mu(U, V) = u_delta(U bold-dot V), and sigma: calU -> calU, sigma(U) = u_delta(U^dagger), are smooth as maps into the embedded manifold calU; they obey mu(cU, dV) = c*d*mu(U, V) and sigma(cU) = conj(c)*sigma(U), and no point or first derivative is changed.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-coherence-naturality; lem-stage1-approximate-group-laws; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse
status: stated
af: seeded
workspace: proofs/lem-stage1-smooth-unitary-operations
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 11, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). TeX 857-868 for the domains; smoothness by restriction/corestriction of the ambient scalar, bilinear, and real-linear maps followed by the smooth polar inverse; scalar identities use polar coherence/naturality.
owner: A
---

**Status.** **RETRACTED from the rigorous record 2026-07-28 (sweep)** — the af validation (then the 100th rigorous result) was found DEFECTIVE by the independent Stage-1 sweep adjudication (`docs/plans/2026-07-28-13E-BINDER-design/SWEEP-ADJUDICATION-STAGE1.md`; second LEARNINGS entry of 2026-07-28; bead `aism-e1qs`): export nodes 1.2.1-1.2.2, 1.3.1.2, 1.3.2: the typed smooth-polar-inverse u_delta is attached to the anaphoric group-laws u_delta with no typed witness; the scalar-action subargument alone is sound but does not certify the compound root. Status mechanically demoted proved->stated, af validated->seeded; workspace and ledger retained for the historical record; whether this row re-elevates or is RETIRED in place (its live content re-entering via the W97 explicit-binder bridges) is a W97 campaign-design decision pending the design audit. The CONTRACT is not in dispute, only the proof.

**Superseded status record (pre-retraction).** af-VALIDATED 2026-07-27 (100th rigorous result): root
validated, 15/15 nodes, taint clean (tier routine; two genuine
cross-sibling challenges — scalar preservation of calU leaning on a
pending sibling — repaired in-run by local membership derivations; run 2
after a spurious PROVER-OVERREACH abort on the orchestrator's own
.frontier/ writes, guard exempted). Export in the workspace; oracle
`af-lem-stage1-smooth-unitary-operations` + `fr verify` PASS. Landed
VERBATIM from the audited `DESIGN-S1-POLAR-v6.md` §3 row 11 (final
verdict LAND).

**Derivation obligation (design §4).** The scalar action is a smooth
ambient restriction/corestriction. `lem-stage1-approximate-group-laws` puts
product and adjoint inputs in the polar domain; compose those smooth
ambient maps with `lem-stage1-smooth-polar-inverse` and corestrict to the
embedded manifold.
