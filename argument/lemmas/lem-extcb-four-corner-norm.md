---
id: lem-extcb-four-corner-norm
kind: lemma
contract: Four-corner assembled norm estimate: there are universal K_norm < infinity and e_norm > 0 such that, for every four-corner merging datum with e = rho+epsilon <= e_norm, every n >= 1, and every X in M_n tensor B, the assembled map gamma_n = alpha_n Gamma_n mu_n (where mu_n(X) = ((I_n tensor Pi_j) X (I_n tensor Pi_k))_{j,k}, Gamma_n is the direct sum of the four fixed amplifications gamma_{jk,n}, and alpha_n((Y_jk)) = sum_{jk} Y_jk) satisfies (1-K_norm*e)||X|| <= ||gamma_n(X)|| <= (1+K_norm*e)||X||.
defs: def-four-corner-merging-datum; def-extended-epsilon-cstar-algebra; def-compressed-corner
deps: lem-compcb-corner-algebra; lem-hcb3-uniform-square-lower
status: stated
af: seeded
provenance: factored out of proofs/lem-extcb-four-corner-merge per the 3rd-stall tripwire (2026-07-25, node 1.3 / challenges ch-d3060d3ae953118f, ch-d809d25e1f7853a7, ch-0fda8a3c0b65233a — statement extracted mechanically from the tree text, assembly notation from validated node 1.1); UNPROVED here pending its own af pass
owner: A
workspace: proofs/lem-extcb-four-corner-norm
---

**Status.** `stated` — the uniform two-sided norm estimate for the
assembled four-corner map, whose in-tree derivation stalled the
`lem-extcb-four-corner-merge` run three times (the 1.3.x cluster:
target-corner separation + per-block defect propagation). Factored per the
tripwire so it can be established once and imported first-class by the
merge. Not af-validated and not L0-rigorous until its own pass clears.

**Provenance.** Third-stall classification of the 2026-07-25
`lem-extcb-four-corner-merge` runs; the statement is node 1.3's claim with
the assembly maps written out from validated node 1.1 (registry-self-
contained phrasing; no other change).
