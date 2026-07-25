---
id: lem-hcb3-uniform-square-lower
kind: lemma
contract: Uniform square lower estimate: there are universal K_sq < infinity and e_sq > 0 such that every H-CB datum with e <= e_sq, every n >= 1, and every Z in M_n tensor S_P satisfy ||Z^dagger dot Z|| >= (1-K_sq*e)||Z||^2.
defs: def-hcb-datum; def-extended-epsilon-cstar-algebra
deps: lem-compcb-corner-algebra
status: stated
af: seeded
provenance: factored out of proofs/lem-hcb3-diagonal-lower-modulus per the balloon tripwire (2026-07-25, node 1.1 / challenges ch-f39f17d9fb40be92, ch-f6597fc7968c250c — statement extracted mechanically from the tree text); UNPROVED here pending its own af pass
owner: A
workspace: proofs/lem-hcb3-uniform-square-lower
---

**Status.** `stated` — the exact all-amplification square lower estimate whose
in-tree re-derivation ballooned the `lem-hcb3-diagonal-lower-modulus` run past
its node cap (dyadic block machinery). Factored per the tripwire so it can be
established once, on the extended-corner structure supplied by
`lem-compcb-corner-algebra`, and imported first-class by the diagonal
estimates. Not af-validated and not L0-rigorous until its own pass clears.

**Provenance.** Balloon-abort classification of the 2026-07-25
`lem-hcb3-diagonal-lower-modulus` run; the statement is node 1.1's claim,
transcribed mechanically (workspace-relative phrasing replaced by the
registry's own def references).
