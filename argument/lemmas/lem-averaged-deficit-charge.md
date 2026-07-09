---
id: lem-averaged-deficit-charge
kind: lemma
contract: Averaged deficit charge: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), a hidden top vertex v of height H, any c_m > 0, and any phi that is a top support functional at v (affine, phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1) or a finite convex average of top support functionals at v: if sum over {j : H - phi(p_j) >= tau} of max(P_vj, 0) >= c_m then c_m*tau <= delta*(2+4*delta); in particular no such configuration exists for 0 < delta < min(1/4, (c_m/3)^2).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-top-deficit-price
status: proved
af: none
provenance: W54 wave (docs/waves/2026-07-09-W54-huddle-charge-decomposition.md): codex prover L1 (PROVED) + fresh hostile codex verifier V-L1 (VALID) — leaf L1 of the W54 case tree
owner: A
---

**Role (the tree's Branch-II charge; the averaging licence).** Leaf L1 of the W54
decomposition: any c_m of the top row's positive mass at top-deficit >= tau forces
tau >= c_m/3 — the charge closing the Q2/Q3 branches. The load-bearing sub-claim proved
here (V-L1-checked) is the AVERAGING LICENCE: a finite convex average of top support
functionals at v is again one (affinity, value H at p_v, and phi <= 0 on C_W are affine
constraints; a convex combination of 1-Lipschitz functions is 1-Lipschitz) — so
[[lem-top-deficit-price]]'s m-L clause applies verbatim to averaged functionals. This is
what legalizes the averaged-phi split (Q3-v2) and the L2 mechanism's two-functional
spread argument. Thresholds closed (>= throughout); dimension-free; clone-invariant.

**Rigour tier.** L5 (reviewer != author: fresh hostile codex V-L1, VALID). NOT af-validated.
