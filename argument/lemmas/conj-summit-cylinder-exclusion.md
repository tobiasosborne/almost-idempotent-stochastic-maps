---
id: conj-summit-cylinder-exclusion
kind: lemma
contract: (CONJECTURE) Summit-cylinder exclusion: there exist universal c_3 > 0 and delta_0 > 0 such that for every exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set W(P), hidden top vertex v of height H > 16*tau, and every row f with ||p_f - p_v||_1 >= 4*tau and dist_1(p_f, conv{p_w : w in W}) > H - 8*tau: p_f is not in Cyl_v(c_3*tau), where Cyl_v(eps) = {x : sup over y in Y_v of y.(p_v - x) < eps} and Y_v is the dual face of lem-top-support-dual-face; equivalently Z_v(f) >= c_3*tau.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: 
status: conjecture
af: none
provenance: W54 wave (docs/waves/2026-07-09-W54-huddle-charge-decomposition.md): prover L3's GAP-1 in the V-L3-corrected standalone form (finding 6: "with that correction, GAP-1 genuinely restores original L3") — leaf L3 of the W54 case tree
owner: A
---

**Role (the corrected L3 leaf).** With the proved dichotomy of
[[lem-top-support-dual-face]], this exclusion IS leaf L3 (far-actor deficit visibility):
every rho-far row in the 8*tau top band is Z-visible at scale c_3*tau. The W54 tree's B2
step consumes exactly this (V-L3 finding 8). The known obstruction it must beat: bare
l1 geometry canNOT exclude the cylinder (V-L3 finding 3 audited the prover's explicit
4-point witness) — the exclusion must use exact idempotence and/or the visible-set
structure, not metric geometry alone. The weaker axis-form (Z_v(f) >= c_3*tau OR
dist_1(p_f, Ax_v) <= r*tau) does NOT restore L3 and is only a residual refinement
(V-L3 finding 7).

**Status discipline.** A conjecture — promotes nothing; consumers carry it as a dep.
