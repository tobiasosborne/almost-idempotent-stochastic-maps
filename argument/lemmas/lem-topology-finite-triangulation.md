---
id: lem-topology-finite-triangulation
kind: lemma
contract: Finite triangulation of compact smooth manifolds: every compact smooth manifold without boundary is homeomorphic to a finite simplicial complex.
defs:
deps:
status: stated
af: seeded
provenance: munkres-elementary-differential-topology munkres-elementary-differential-topology.txt:4356-4358 (Theorem 10.6, p.103: every non-bounded C^r manifold has a C^r triangulation; scanned-typewriter OCR superscript garbling visually reconciled against the p.108 page image 2026-07-26); compactness => finite complex derived in-tree; DESIGN-FUDW-DECOMP-v4.1.md §2.3
owner: A
workspace: proofs/lem-topology-finite-triangulation
---

**Status.** RE-SOURCED and RE-PINNED (user-directed in-session, 2026-07-26):
the Cairns 1935 route is RETIRED — Cairns states his theorem for "class one"
manifolds with "allowable coordinate systems" but delegates both definitions
to Veblen–Whitehead 1932 (not in `refs/`), so the modern-manifold bridge was
an unprovable input from local ground truth (the af verifier's root
challenge was correct; the L1 stop condition fired). The row now pins to
Munkres, *Elementary Differential Topology* (user-supplied copy, promoted
2026-07-26 with manifest rows), Theorem 10.6: every non-bounded C^r manifold
has a C^r triangulation. The contract takes the compact smooth (C^∞, empty
boundary) special case — exactly what the Stage-1 consumer applies — with
the compactness ⇒ finite-complex step derived in-tree.

**Scope note.** "Smooth" = C^∞ ⊆ C^r for every r, so Munkres's C^r statement
covers the contract's hypothesis class; the previous contract's C^1
generality is NOT claimed (the Stage-1 manifold is smooth). "Without
boundary" matches the "non-bounded" hypothesis of Thm 10.6's first sentence.

**OCR-encoding callout (L1 honesty).** The source payload is a
typewriter-era scan; the per-page tesseract extraction garbles superscripts
(`c™`, `cr`, `C*™` all render C^r on the page image). The registered
external quotes the txt VERBATIM (that is what byte-matches); the p.108 page
image was visually confirmed 2026-07-26. Same pattern as the Lee
`lee-smooth-manifolds` OCR glyphs reconciled in the validated
`lem-topology-quotient-manifold` tree.

**Consumers.** Stage-1 quotient-finite-CW row / the Lefschetz–Hopf
application (needs: the compact smooth Stage-1 manifold is a finite
polyhedron), per `DESIGN-FUDW-DECOMP-v4.1.md` §2.3/§3.3.
