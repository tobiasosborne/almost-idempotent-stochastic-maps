---
id: lem-topology-lefschetz-hopf
kind: lemma
contract: Lefschetz-Hopf formula (maximal-simplex form): if f:X->X is a map of a finite polyhedron with a finite set of fixed points, each of which lies in a maximal simplex of X, then the Lefschetz number L(f) is the sum of the indices of all the fixed points of f.
defs: def-lefschetz-fixed-point-data
deps:
status: proved
af: validated
provenance: arkowitz-brown-2004 arkowitz-brown-lefschetz-hopf-2004.txt:124-126 (Theorem 1.2, Lefschetz-Hopf — contract pinned to the EXACT source statement 2026-07-26; the v4.1 register's broader isolated-fixed-point wording was a hypothesis MISMATCH and is NOT claimed); DESIGN-FUDW-DECOMP-v4.1.md §2.3
owner: A
workspace: proofs/lem-topology-lefschetz-hopf
---

**Status.** af-VALIDATED in-repo (2026-07-26, session 28): 2-node tree (root +
one direct application of the byte-matched external), taint clean 2/2,
first-pass, zero challenges. Export at `proofs/lem-topology-lefschetz-hopf/export.md`.

**Source locus (pinned).** Arkowitz–Brown, *The Lefschetz–Hopf theorem and
axioms for the Lefschetz number* (2004), Theorem 1.2
(`refs/arkowitz-brown-2004/arkowitz-brown-lefschetz-hopf-2004.txt:124-126`):
"If f : X → X is a map of a finite polyhedron with a finite set of fixed
points, each of which lies in a maximal simplex of X, then L(f) is the sum of
the indices of all the fixed points of f."

**FAITHFULNESS CALLOUT (hypothesis narrowing, 2026-07-26).** The design
register's provisional wording ("finitely many isolated fixed points") was
STRONGER than this source theorem: the source additionally requires every
fixed point to lie in a MAXIMAL simplex. The register said "exact theorem
required"; this shard carries the exact restricted statement. Any consumer
(`lem-stage1-extra-fixed-class` per §3.3) must DISCHARGE the maximal-simplex
positioning for its fixed points, or a different source giving the general
isolated-fixed-point form must be acquired and byte-matched. Flagged as a
consumer-side obligation in the phase-4 assembly.

**Consumers.** `lem-stage1-extra-fixed-class` (per §3.3) — with the
maximal-simplex obligation above.
