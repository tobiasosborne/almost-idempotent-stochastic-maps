---
id: lem-topology-kunneth-cross-product
kind: lemma
contract: Cohomological Kunneth isomorphism over R: for CW complexes X and Y with each H^k(Y;R) a finitely generated free R-module, the cross product H*(X;R) (x)_R H*(Y;R) -> H*(X x Y;R) is an isomorphism of rings; in particular this holds over the field R = reals for finite-CW spaces with finite-dimensional cohomology.
defs:
deps:
status: stated
af: none
provenance: hatcher-algebraic-topology AT.txt:13505-13506 (Theorem 3.15 in THIS printing — NOT 3.16; the v4.1 register's "Thm 3.16" locus is off by one, flagged to the design owner in the ACQUIRED log 2026-07-25 and confirmed 2026-07-26); DESIGN-FUDW-DECOMP-v4.1.md §2.3
owner: A
workspace: proofs/lem-topology-kunneth-cross-product
---

**Status.** Local source-result transcription at `stated`; to be af-elevated
as a 1-node tree with the byte-matched external. Not `cited`, not
af-validated, not L0-rigorous yet.

**Source locus (pinned).** Hatcher, Theorem 3.15 (txt:13505-13506): "The
cross product H∗(X;R) ⊗_R H∗(Y;R) → H∗(X×Y;R) is an isomorphism of rings if X
and Y are CW complexes and H^k(Y;R) is a finitely generated free R-module for
all k." Locus note: in this printing the result is Theorem 3.15; "Theorem
3.16" does not exist as a theorem label (what follows 3.15 is Example 3.16).

**Derivation note (field triviality).** Over a field (R = ℝ),
finite-dimensional H^k(Y;ℝ) is automatically finitely generated free, so the
consuming finite-CW/finite-dimensional form follows directly from the printed
hypotheses; finite-CW is stronger than CW. The source hypotheses (CW + f.g.
free) must NOT be dropped in any consumer.

**Consumers.** Stage-1 trace/cohomology rows (per §3.3).
