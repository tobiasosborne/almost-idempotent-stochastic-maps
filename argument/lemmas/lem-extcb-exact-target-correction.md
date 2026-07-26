---
id: lem-extcb-exact-target-correction
kind: lemma
contract: There are universal a_corr>0 and C_corr<infinity with the following property: if B is a finite-dimensional C*-algebra, H a finite-dimensional Hilbert space, and T:B->B(H) is linear, dagger-preserving, has ||T_n(XY)-T_n(X)T_n(Y)||<=a||X||||Y|| and ||T_n(I)-I||<=a at every n, where 0<=a<=a_corr, then one unital dagger-homomorphism mu:B->B(H) satisfies ||mu_n-T_n||<=C_corr*a at every n.
defs: def-fd-cstar-diagonal; def-extended-epsilon-cstar-algebra
deps:
status: proved
af: none
provenance: proofs/conj-extcb ledger node 1.2 (af-validated 2026-07-25, taint clean; children 1.2.1-1.2.3 + endpoint repairs 1.2.3.1, 1.2.3.1.1) — contract adopted VERBATIM per the banking precedent; DESIGN-GAP-EA.md §2.1 (aism-fbh8, design codex job 2026-07-26)
owner: A
---

**Status.** GAP-EA discharge row (DESIGN-GAP-EA.md option (a)): the central
theorem sentence of af-validated `conj-extcb` node 1.2, adopted verbatim. The
mathematical assertion is validated inside `proofs/conj-extcb` (taint clean),
but no standalone workspace exists yet — hence `proved` / `af: none`. Only a
standalone af run moves this row to `af: validated`.

**Content.** Dimension-free exact-target correction: a linear dagger-preserving
map with amplification-uniform multiplicative and unit defects at most
`a <= a_corr` is `C_corr*a`-close, uniformly at every amplification level, to a
single level-one unital dagger-homomorphism. The validated proof runs through
the norm-one Haar diagonal, exact unitalization, and a normalized Newton
correction, with no external theorem. The validated subtree establishes the
usable value `C_corr = 57`, which stays OUT of this contract (the validated
root asserts existence only — over-banking guard, DESIGN-GAP-EA.md §4.6).

**Seeding plan (when elevated).** Six-node transcription of the ACTIVE
`conj-extcb` subtree — 1.2, 1.2.1, 1.2.2, 1.2.3 AND the load-bearing endpoint
repairs 1.2.3.1, 1.2.3.1.1 (a four-node transcription is NOT faithful,
DESIGN-GAP-EA.md §4.1). def-adds: `def-fd-cstar-diagonal`,
`def-epsilon-cstar-algebra`, `def-extended-epsilon-cstar-algebra`, plus the
byte-matched operator-space matrix-norm axioms used in `conj-extcb`. No
externals. Budget 6-8 nodes; R12 applies (balloon => factor, never cap-raise).

**Consumers.** `lem-extcb-exact-target-approximation` (the M_r bridge);
`lem-maincb-error-improvement` (IMPROVE-CB — consumes THIS general-B form
directly, not the bridge; its own contract narrowing escalates to the user).
