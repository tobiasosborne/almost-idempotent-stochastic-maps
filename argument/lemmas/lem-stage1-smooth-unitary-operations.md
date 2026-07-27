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

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 11 (final verdict LAND). Not proved in-repo;
af elevation per the design's projected budget 4/2. Qualitative: no new
coefficient.

**Derivation obligation (design §4).** The scalar action is a smooth
ambient restriction/corestriction. `lem-stage1-approximate-group-laws` puts
product and adjoint inputs in the polar domain; compose those smooth
ambient maps with `lem-stage1-smooth-polar-inverse` and corestrict to the
embedded manifold.
