---
id: lem-stage1-maurer-cartan-trivialization
kind: lemma
contract: Uniform global tangent/Maurer-Cartan control: there are universal C_ch >= 1, kappa_ch in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0 with C_ch*(epsilon_r + delta) <= kappa_ch, the graph maps supplied by lem-stage1-unitary-graph-control satisfy: every tangent space T_U calU is the image of L_U(I + Dg_U(0)): icalH -> calX, and omega_U(Z) = (L_U^{-1} Z)^par : T_U calU -> icalH is a global C^1 bundle trivialization with distortion at most 1 + C_ch*epsilon_r, satisfying omega_{cU}(cZ) = omega_U(Z) and omega_U(iU) = iJ for every c in U(1).
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-unitary-graph-control
status: stated
af: none
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 3, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). Source loci TeX 795-807; the two equivariance identities are direct from the displayed formula and scalar bilinearity.
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 3 (final verdict LAND). Not proved in-repo;
af elevation per the design's projected budget 4/2.

**Derivation obligation (design §4).** Invert the graph tangent map from
`lem-stage1-unitary-graph-control` to obtain TeX 795–807 globally. Derive
omega_{cU}(cZ) = omega_U(Z) and omega_U(iU) = iJ directly; no
graph-existence work is repeated.
