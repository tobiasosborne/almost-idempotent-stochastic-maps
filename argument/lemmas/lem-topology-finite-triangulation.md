---
id: lem-topology-finite-triangulation
kind: lemma
contract: Finite triangulation of compact C^1 manifolds: every compact C^1 manifold is homeomorphic to a finite simplicial complex.
defs:
deps:
status: stated
af: seeded
provenance: cairns-1935 cairns-triangulation-1935.txt:47-50 (unnumbered THEOREM, p.549 — MATCH via compactness/finite subcover, loci pinned 2026-07-26); DESIGN-FUDW-DECOMP-v4.1.md §2.3
owner: A
workspace: proofs/lem-topology-finite-triangulation
---

**Status.** Local source-result transcription at `stated`; to be af-elevated as
a 1-node tree with the byte-matched external. Not `cited`, not af-validated,
not L0-rigorous yet.

**Source locus (pinned).** Cairns, *Triangulation of the manifold of class
one*, Bull. AMS 41(8) (1935) 549–552, the (unnumbered) THEOREM at p. 549
(`refs/cairns-1935/cairns-triangulation-1935.txt:47-50`): "If an r-manifold,
M^r, of class one is covered by the domains of a finite set of allowable
coordinate systems, it can be triangulated into the cells of a finite
complex." ("Class one" = C^1 in Veblen–Whitehead terminology, per the paper's
own footnotes.)

**Derivation gap to close at elevation (one step).** The contract's "compact"
hypothesis yields the source's "finite set of allowable coordinate systems"
hypothesis by extracting a finite subcover from the cover by coordinate
domains; "triangulated into the cells of a finite complex" gives the
homeomorphism with a finite simplicial complex. This glue is the 1-node af
content.

**Consumers.** Stage-1 quotient-finite-CW row, per
`DESIGN-FUDW-DECOMP-v4.1.md` §2.3/§3.3.
