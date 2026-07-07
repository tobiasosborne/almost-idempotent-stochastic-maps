---
id: lem-rank3-optimal-face-interval-reduction
kind: lemma
contract: Rank-3 optimal-face interval reduction: for a rank-3 exact signed idempotent P, a geometrically distinct hidden row vertex u with 0 < t*(u) < inf, and always-tight families T, O (tight on the whole optimal face), for any optimal exposer h both conv{p_f - p_u : f in T} and t*(u)*conv{p_i - p_u : i in O} lie in the level line L_h = {x in D_u : hbar(x) = t*(u)} (D_u the 2-dimensional displacement space, hbar the linear part of h), so the alpha-free condition is exactly overlap of the two intervals in any affine coordinate on L_h; if the intervals are disjoint, the separator lemma yields a separator-dependent nonclone zero-face blocker on the psi-negative half of the kernel line of hbar.
defs: def-signed-idempotent; def-visible-set; def-exposed
deps: lem-optimal-face-alpha-free-characterization; lem-always-tight-dual-support; lem-separator-zero-face-obstruction
status: proved
af: none
provenance: W47 wave (docs/waves/2026-07-07-W47-mechanism.md): fresh-codex prover (worker AX) + SEPARATE fresh-codex hostile verifier (VAX, VALID-WITH-CORRECTIONS — four corrections adopted verbatim: the one-optimal-h quantifier (fixed generators lie in every level line, degenerating to a point if lines differ); dim D_u = rank(P) - 1 = 2 from P1 = 1 (clones do not change the affine dimension); the O hull is the t*-SCALED hull (unscaled O points sit at level 1); the "across the gap" ray claim DEMOTED to separator-dependent. VAX recomputed exact interval endpoints on all three census instances by independent vertex enumeration: disjoint exactly at HEIGHT+A (u=3: I_T = {-59/120} vs I_O = {-59/12000}), overlap at TOP-preserving and the W29 frontier)
owner: A
---

**Role (the rank-3 terminal question is one-dimensional).** At rank 3 the conic terminal
node [[conj-zero-face-elimination]] collapses to SCALAR ORDERING: the two always-tight hulls
are intervals on the exposer level line, alpha-free == interval overlap, and the census
pattern (|T| <= 2, |O| = 1) is literal betweenness. The remaining rank-3 gap (the named
candidate lem-rank3-cluster-uniform-optimal-face-interlacing) is: force the interval overlap
from the tall/heavy/near-cluster hypotheses — none of which the proved reduction consumes.

**Honest limits.** Pure reduction — proves nothing about tall regimes; the blocker
half-line clause is separator-dependent (no canonical ray).

**Rigour tier.** In-repo paper proof with fresh hostile review (L5). NOT af-validated.
