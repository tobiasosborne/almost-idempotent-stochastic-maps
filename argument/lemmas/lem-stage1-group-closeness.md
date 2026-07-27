---
id: lem-stage1-group-closeness
kind: lemma
contract: Group-input polar closeness: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), the inverse u_delta:S_delta -> calU of the polar map satisfies ||u_delta(U bold-dot V) - U bold-dot V|| <= C_grp*epsilon_r and ||u_delta(U^dagger) - U^dagger|| <= C_grp*epsilon_r for every U, V in calU.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
status: stated
af: none
provenance: DESIGN-S1-GROUP-FACTORING.md sect-2.2, landed verbatim (row-6 balloon repair; AUDIT-S1-GROUP-FACTORING.md LAND-WITH-CORRECTIONS, contract clause PASS); derivation from lem-stage1-polar-retraction + the two registered definitions; orientation Kitaev TeX 845-868 (qualitative — NOT byte-citable for this quantitative contract).
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-GROUP-FACTORING.md` §2.2 (hostile verdict LAND-WITH-CORRECTIONS;
the correction was proof-body-only). Not proved in-repo; af elevation per
the design's §5.2 skeleton (15-node target and hard cap).

**Sibling independence (binding).** This row deliberately does NOT import
`lem-stage1-group-domain-membership`: the displayed expressions assert both
inputs are in the domain of u_delta, and the proof must establish that
typing INTERNALLY (repeat the raw input-domain calculation C3–C8) rather
than appeal to the sibling — the small duplication is the price of
eliminating every cross-sibling edge (the balloon cause). Route: polar
decomposition X = u bold-dot h, two associator comparisons giving
X^dagger bold-dot X = h bold-dot h + O(epsilon_r), h = J + a with
h bold-dot h - J = 2a + a bold-dot a, absorb the quadratic term
(||a|| < delta <= 1/2), solve for ||a|| <= K*epsilon_r, conclude
||u - X|| <= K*epsilon_r. All estimates <=, meaningful at epsilon_r = 0;
the endpoint discipline of the membership shard applies verbatim.
