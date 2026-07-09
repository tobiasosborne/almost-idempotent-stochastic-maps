---
id: lem-downhill-cotop-conic-mass
kind: lemma
contract: Downhill co-top conic mass: in the setting of lem-cotop-witness-pinning with additionally disjoint always-tight hulls at v (g = dist_1(K_T(v), K_O(v)) > 0, K_T = conv{p_f - p_v : f in T}, K_O = t*(v)*conv{p_i - p_v : i in O}): every reduced optimal display has sum over Z of a_z > g/(4*tau); for every l1-optimal separator ell (||ell||_inf <= 1, min over K_T of ell - max over K_O of ell >= g) the a-weighted displacement is downhill, sum over z in Z of a_z*ell(p_z - p_v) <= -g; and for every c > 0, at least g/(4*tau) - (1/2+delta)/c of the conic mass sits on rows z simultaneously nonclone (p_z != p_v), rho-near v, h*-zero, and co-top (dist_1(p_z, conv W) > H - c*tau).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-cotop-witness-pinning; lem-disjoint-hulls-forced-alpha; lem-zero-face-localization; lem-optimal-face-conic-reduction
status: proved
af: none
provenance: W54 wave (docs/waves/2026-07-09-W54-huddle-charge-decomposition.md): Fable author L6 (sub-leaf L6.3) + fresh hostile codex verifier V-L6 (VALID-WITH-CORRECTIONS; the nonclone clause repaired per V-L6 finding 3 — proof order changed to derive the downhill inequality FIRST, then locate the mass: all zero-face carriers are rho-near by lem-zero-face-localization, clones of v have ell(p_z - p_v) = 0, so the downhill total forces > g/(4*tau) of mass onto nonclone negative-displacement carriers; the unsupported centered-zero-deletion reading is NOT used)
owner: A
---

**Role (disjointness pays in nonclone co-top zero-face mass, quantitatively downhill).**
The Branch-I anatomy in coefficient form: a disjointness gap g at the top forces
> g/(4*tau) of reduced conic mass onto genuinely distinct rho-near co-top h*-zero rows
whose separator displacement aggregates to <= -g. Combined with
[[lem-cotop-witness-pinning]] this is the primal-side skeleton of the huddle that
[[conj-cotop-web-coupling]] must starve. Dimension-free; clone-invariant (the repaired
proof charges clones zero displacement).

**Rigour tier.** L5 (reviewer != author: fresh hostile codex V-L6; correction applied).
NOT af-validated.
