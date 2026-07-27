---
id: lem-stage1-smooth-unitary-atlas
kind: lemma
contract: Smooth graph-atlas upgrade: for every finite-dimensional exact-unit epsilon_r-C*-algebra, if calU is covered by the unique C^1 graph functions g_V of lem-stage1-unitary-graph-control and D_{A^perp} f_V is invertible at every graph point, then those same g_V are C^infinity, and the same graph charts make calU a smooth embedded manifold; no point or first derivative of a graph or chart is changed.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-rectified-cstar-control; lem-stage1-unitary-graph-control
status: stated
af: seeded
workspace: proofs/lem-stage1-smooth-unitary-atlas
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 9, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). Polynomiality from TeX 420-429, 692-793; Lee C.40 at lee-smooth-manifolds-2ed.txt:31330-31344, 31374-31385; overlap gluing is by graph uniqueness.
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 9 (final verdict LAND). Not proved in-repo;
af elevation per the design's projected budget 3/2. Qualitative: introduces
no smoothness threshold or coefficient.

**Derivation obligation (design §4).** The graph equation is a degree-two
polynomial of real finite-dimensional spaces. Apply Lee C.40 pointwise and
use `lem-stage1-unitary-graph-control` uniqueness on overlaps.
