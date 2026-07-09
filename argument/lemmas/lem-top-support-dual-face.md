---
id: lem-top-support-dual-face
kind: lemma
contract: Top-support dual face: for an exact signed idempotent P with delta(P) > 0, nonempty visible set W(P), and hidden top vertex v of height H, writing Phi_v = {phi affine, phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1}, h_C(y) = sup{y.c : c in conv{p_w : w in W}}, and Y_v = {y : ||y||_inf <= 1, y.p_v - h_C(y) = H}: Y_v is nonempty, on the row set Phi_v is exactly {phi_y(x) = y.x - h_C(y) : y in Y_v}, and for every row f the top-deficit supremum Z_v(f) := sup over phi in Phi_v of (H - phi(p_f)) equals sup over y in Y_v of y.(p_v - p_f) and is finite; hence for every eps > 0 exactly one of Z_v(f) >= eps (visible horn, owning equality) or p_f in Cyl_v(eps) := {x : sup over y in Y_v of y.(p_v - x) < eps} (summit-cylinder horn) holds.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-top-deficit-price
status: proved
af: none
provenance: W54 wave (docs/waves/2026-07-09-W54-huddle-charge-decomposition.md): codex prover L3 (Statements A+B of its PARTIAL) + fresh hostile codex verifier V-L3 (VALID-WITH-CORRECTIONS; the proved disjunction confirmed valid, l1/l-infinity duality and Phi_v-membership checked, clone-invariance via the fiber-weighted average)
owner: A
---

**Role (legal tilts ARE the dual face).** The exact characterization of the top support
functional class: a tilt stays in Phi_v iff its linear part stays in the exposed face Y_v
of the l-infinity ball realizing the height (V-L3 finding 4 — this kills naive tilt
constructions and replaces them with face geometry). Z_v(f) is the canonical "how visible
is row f from the summit" functional; the summit cylinder Cyl_v(eps) and summit axis
Ax_v = {x : y.x = y.p_v for all y in Y_v} are the canonical blind objects. Existence
mechanics from [[lem-top-deficit-price]]; the rest is first-principles l1/l-infinity
support duality. Dimension-free; clone-invariant.

**Consumer note.** [[conj-summit-cylinder-exclusion]] (the corrected L3 leaf) is stated in
this vocabulary; the W54 tree's B2 step consumes it. CAUTION (V-L3 finding 5): pointwise
cylinder exclusion does NOT upgrade to a simultaneous one-phi-for-a-set statement by
averaging — the per-row bounds are not preserved (the L5 minimax step is a genuinely
separate question).

**Rigour tier.** L5 (reviewer != author: fresh hostile codex V-L3). NOT af-validated.
