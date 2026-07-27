---
id: lem-stage1-smooth-polar-inverse
kind: lemma
contract: Smooth polar-inverse upgrade: for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0, if lem-stage1-smooth-unitary-atlas gives the smooth embedded atlas and Pi_delta: calU x B^{calH}_delta(J) -> S_delta is the bijective C^1 local diffeomorphism of lem-stage1-polar-retraction onto an open set, then the same ambient-bilinear Pi_delta is a smooth diffeomorphism and its same set-theoretic inverse (u_delta, h_delta) is smooth; no point or first derivative is changed.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction; lem-stage1-smooth-unitary-atlas
status: proved
af: validated
workspace: proofs/lem-stage1-smooth-polar-inverse
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 10, landed verbatim (LaTeX flattened to registry ASCII); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). Source loci TeX 809-855; Lee C.34 at lee-smooth-manifolds-2ed.txt:31134-31137 and C.36 at 31286-31298, applied chartwise after the smooth-atlas row.
owner: A
---

**Status.** af-VALIDATED 2026-07-27 (99th rigorous result): first-pass —
root validated, 21/21 nodes, taint clean (tier routine, zero challenges).
Export in the workspace; oracle `af-lem-stage1-smooth-polar-inverse` +
`fr verify` PASS. Lee C.34/C.36 imported as the byte-matched externals
GT-lee-2ed-thm-C.34 / GT-lee-2ed-cor-C.36. Landed VERBATIM from the
audited `DESIGN-S1-POLAR-v6.md` §3 row 10 (final verdict LAND).

**Derivation obligation (design §4).** The polar map is a smooth
ambient-bilinear map after `lem-stage1-smooth-unitary-atlas`. The
C^1-diffeomorphism property of `lem-stage1-polar-retraction` gives
derivative invertibility. Apply Lee C.34/C.36 chartwise; global injectivity
glues the inverse.
