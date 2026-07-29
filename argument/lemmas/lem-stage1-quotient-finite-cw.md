---
id: lem-stage1-quotient-finite-cw
kind: lemma
contract: For every finite-dimensional exact-unit epsilon_r-C*-algebra, if breve-calU = calU_e/U(1) is a compact smooth manifold without boundary, then breve-calU is homeomorphic to a finite simplicial complex and hence has finite CW type.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-quotient-manifold-package; lem-topology-finite-triangulation
status: proved
af: validated
workspace: proofs/lem-stage1-quotient-finite-cw
provenance: DESIGN-S1-POLAR-v6.md sect-5 downstream row 3, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80).
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-29): 4-node tree, root
`validated`, taint clean 4/4, ZERO challenges first-pass
(`proofs/lem-stage1-quotient-finite-cw/export.md`; oracle
`af-lem-stage1-quotient-finite-cw` pass; run tier routine, actual 4
nodes <= cap 6, design budget 3/2). Contract transcribed VERBATIM from
the audited `DESIGN-S1-POLAR-v6.md` §5 (final verdict LAND). The former
honest cap was lifted in-session: `lem-topology-finite-triangulation`
af-VALIDATED (122nd rigorous result; bead `aism-j5t9` closed), so both
deps were T0 at elevation.

**Build-granularity discipline (BINDING on the af tree; extends the
user-ratified W98 row-1 discipline of 2026-07-28).** The target is the
design's 3-node skeleton (budget 3/2; hard cap 6). Tree discipline:
(i) ONE node instantiating the hypothesis: under the stated antecedent,
breve-calU is a compact smooth manifold without boundary (the N>1
structure from lem-stage1-quotient-manifold-package; the N=1 one-point
case directly); (ii) ONE node applying lem-topology-finite-triangulation
to conclude breve-calU is homeomorphic to a finite simplicial complex;
(iii) ONE node for "hence finite CW type" (a finite simplicial complex
is a finite CW complex; homeomorphism transfers CW type) + assembly.
Do NOT sub-split routine steps. Constants live in the proof body,
never the contract.
