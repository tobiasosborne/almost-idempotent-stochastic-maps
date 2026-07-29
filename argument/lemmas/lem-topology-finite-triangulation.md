---
id: lem-topology-finite-triangulation
kind: lemma
contract: Finite triangulation of compact smooth manifolds: every compact smooth manifold without boundary is homeomorphic to a finite simplicial complex.
defs:
deps:
status: proved
af: validated
provenance: munkres-elementary-differential-topology munkres-elementary-differential-topology.txt:4356-4358 (Theorem 10.6, p.103: every non-bounded C^r manifold has a C^r triangulation; scanned-typewriter OCR superscript garbling visually reconciled against the p.108 page image 2026-07-26); compactness => finite complex derived in-tree; DESIGN-FUDW-DECOMP-v4.1.md §2.3
owner: A
workspace: proofs/lem-topology-finite-triangulation
---

**Status.** af-VALIDATED in-repo (2026-07-29, run 3 on the second clean
re-seed): 6-node tree, root `validated`, taint clean 6/6, ZERO
challenges (`proofs/lem-topology-finite-triangulation/export.md`;
oracle `af-lem-topology-finite-triangulation` pass). History:
RE-SOURCED and RE-PINNED (user-directed in-session, 2026-07-26):
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

**Re-seed 2026-07-29 (bead aism-j5t9 executed).** The 2026-07-26 Munkres
re-run BALLOONED (39 nodes, 37 live > cap 26) because the prover
re-derived the "C^r triangulation => homeomorphic to a finite simplicial
complex" unpacking from scratch. Per the bead's fix: Munkres's
DEFINITIONS are now provisioned as byte-matched externals
`GT-munkres-edt-def-8.1` (class C^r relative to K; non-degenerate;
txt:3332-3336, printed p.79) and `GT-munkres-edt-def-8.3` (immersion;
imbedding; "if it is also a homeomorphism onto, it is called a C^r
triangulation of M"; txt:3384-3392, printed pp.80-81) — both visually
reconciled against the page images (same scan-OCR pattern as Thm 10.6).
The 16 ballooned pending nodes (the 1.6-1.10 subtree) were archived at
re-seed. A first re-run aborted round-0 on the balloon tripwire (the 21
retired-Cairns validated nodes count live; validated->archived is an
invalid af transition; live=27 > cap 26 structurally) -> first clean
re-seed. That re-seed's Def 8.1/8.3 externals were CORRUPTED by a
line-counting defect (python splitlines() counts the OCR txt's 117
form-feed page separators as line breaks; sed/grep -n do not; the
quotes came from ~82 lines earlier in the file) — check-refs still
passed because it verifies the quote exists verbatim SOMEWHERE, not at
the claimed locus. The resulting STUCK run's 5 validated nodes are
DISCARDED (node 1.2 cited both corrupted externals; its acceptance is
a recorded verification near-miss). See FINDINGS.md 2026-07-29. Second
clean re-seed (2026-07-29): fresh `af init`, byte-unchanged contract;
FOUR authorized externals, all re-extracted in sed-space (\n-only) and
verified quote-at-claimed-locus + against the page images:
`GT-munkres-edt-thm-10.6` (txt:4356-4358), `GT-munkres-edt-def-8.1`
(txt:3332-3336), `GT-munkres-edt-def-8.3` (txt:3384-3392), and
`GT-munkres-edt-def-1.1-non-bounded` (txt:241-242; bridges the
contract's "without boundary" to Thm 10.6's "non-bounded" — the
authorization the previous run's verifier correctly demanded). The
Cairns external stays dropped (retired route). Old ledgers preserved in
git history. Cap stays 26 (R12: provision, don't bump).

**Build-granularity discipline (BINDING on the re-run tree).** With the
def externals provisioned the remaining route is ~5 steps: (i) ONE node
for the hypothesis bridge (smooth = C^infinity => C^r; without boundary
= non-bounded) and the Thm 10.6 application giving a C^r triangulation
f: K -> M; (ii) ONE node reading off from GT-munkres-edt-def-8.1/8.3
that a C^r triangulation is in particular a homeomorphism of |K| onto
M; (iii) ONE node for compactness of |K| (homeomorphic transfer) and
the finite-subcover step (the validated compactness nodes may be
cited); (iv) ONE node for compact realization => finitely many
vertices => finite complex; (v) ONE assembly node. Do NOT sub-split
routine steps; do NOT re-derive what the def externals state.
