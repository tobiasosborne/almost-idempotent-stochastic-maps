---
id: lem-stage1-polar-scalar-arithmetic
kind: lemma
contract: Universal Stage-1 polar arithmetic: for every C_rect, C_ch, C_pol, C_grp, C_path, C_der >= 1, e_rect in (0, 1/C_rect], and kappa_ch, kappa_pol, kappa_der in (0, 1/2], setting delta_* = min{1/4, kappa_ch/(4*C_ch), kappa_pol/(4*C_pol)}, epsilon_*^r = min{1/4, kappa_ch/(4*C_ch), kappa_pol/(4*C_pol), kappa_der/(8*C_der), 1/C_grp, delta_*/(12*C_path*C_grp)}, e_S1 = min{e_rect, epsilon_*^r/C_rect}, r_iso = min{delta_*/4, kappa_der/(8*C_der)}, epsilon_r = C_rect*epsilon_X, q = C_grp*epsilon_r, r_- = delta_* - C_pol*(epsilon_r*delta_* + delta_*^2), and eta = C_path*(q + epsilon_r*q + q^2), every 0 <= epsilon_X <= e_S1 satisfies C_ch*(epsilon_r + delta_*) <= kappa_ch, C_pol*(epsilon_r + delta_*) <= kappa_pol, q < r_-, C_path*q <= 1/4, eta < r_-, C_der*(epsilon_r + r_iso) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta_*))*r_iso + q < 2*delta_*; moreover r_- >= 3*delta_*/4, eta <= delta_*/4, and C_der*(r_iso + epsilon_r) <= kappa_der/4 < 1.
defs: def-stage1-polar-witness-data
deps:
status: stated
af: none
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 12, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). AUDIT-S1-POLAR-v2.md sect-3 recomputes all eight guards exactly; pure scalar derivation.
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 12 (final verdict LAND; audit §4:
SUPPORTED — audit-v2 §3 proves all displayed inequalities for every tuple
with the stated sign/range hypotheses). Not proved in-repo; af elevation
per the design's projected budget 5/2. Universal over every already
selected tuple; it proves scalar implications only and has no analytic
dependency.
