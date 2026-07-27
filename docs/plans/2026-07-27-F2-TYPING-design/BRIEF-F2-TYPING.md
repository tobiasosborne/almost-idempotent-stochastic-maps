# BRIEF — F2 contract typing correction + elevation-provisioning design (small, surgical)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation; everything you produce is escalated for verbatim landing after a
fresh hostile check.

## The problem

The landed contract of `argument/lemmas/lem-routef-f2-positive-unital-compression.md`
(hostile-endorsed exact text, VERDICT-F2F3-BRIDGE.md §7) types
D: M_n → l_inf^n, J: l_inf^n → M_n, Φ = J Q D, ι: l_inf^k → B,
A := D Δ ι, M := ι⁻¹ Υ J — but `definitions/def-stochastic.md` fixes
l_inf^n = ℝⁿ, while the diagonal of a complex matrix lies in ℂⁿ and B is a
complex C*-algebra. An af elevation attempt STUCK on exactly this
(challenge ch-2163ee19860aa3d7 in
`proofs/lem-routef-f2-positive-unital-compression/ledger/` — read it), the
same defect family already REPAIRED at T0 in the two F0 seam rows
(`lem-routef-f0-ucp-lift`, `lem-routef-f0-defect-identity`: D: M_n → ℂⁿ,
J: ℂⁿ → M_n, Q_ℂ the canonical complex-linear extension, Φ = J Q_ℂ D —
both now af-validated with this typing).

## Your deliverables — write `docs/plans/2026-07-27-F2-TYPING-design/DESIGN-F2-TYPING.md`

1. **The corrected one-line F2 contract.** Requirements: (a) the Φ end must
   match the T0 F0 seam typing EXACTLY (Φ = J Q_ℂ D through ℂⁿ) so the
   future k-ledger parent composes both; (b) the OUTPUT end must still
   deliver A: l_inf^k → l_inf^n and M: l_inf^n → l_inf^k as REAL positive
   unital maps with the three EXACT estimates unchanged (F3 and PRH consume
   them literally on the real spaces — read
   `lem-routef-f3-retract-defect.md:4` and `lem-routef-prh-finish.md:4`;
   their hypothesis lists must stay satisfied verbatim); (c) state the
   real/complex interface explicitly and minimally (e.g. how ι and the
   compositions restrict/corestrict to the real subspaces — YOU design the
   clean formulation; candidates include routing through l_inf^k(ℂ) with a
   restriction clause, or asserting the composed maps preserve the real
   subalgebras — pick the one that keeps the proof (PROOF-F2F3-BRIDGE.md §1)
   valid as written and JUSTIFY it); (d) constants, thresholds, and the
   quantifier structure unchanged — this is a TYPING correction, not new
   mathematics. Also state whether `defs:` should gain `def-ucp-map` (the
   contract says "UCP maps"; that def now exists).
2. **Elevation provisioning plan** for the re-seed, addressing the STUCK
   run's remaining challenge classes (read the abort classification in the
   run log and the challenges in the ledger): (i) the classification of
   finite-dimensional commutative C*-algebras — the local byte-matchable
   anchor is the projection-basis sentence at
   `refs/kitaev-2405.02434/approximate_algebras.tex:1361-1363` (and
   `definitions/def-projection-basis.md` is a locked cited def); decide:
   provision as a byte-matched af external + prove the ℂᵏ-isomorphism
   in-tree (finite-dimensional simultaneous diagonalization is elementary),
   OR factor a registry sub-lemma — recommend one with a budget estimate;
   (ii) UCP complete contractivity ‖Δ‖_cb ≤ 1 — provable in-tree from
   unitality + complete positivity in finite dimensions? Give the 2–3 step
   argument or declare NOT-DERIVABLE-LOCALLY; (iii) the ε := K·η scoping
   (the prover's shorthand leaked across siblings) — a prover-discipline
   note, not a contract item. Estimate the total node budget; if an honest
   estimate exceeds ~25 nodes, recommend the registry factoring split
   instead (name the sub-lemma contracts).
3. **Consumer re-check.** One paragraph each: F3's and PRH's hypothesis
   lists still satisfied verbatim by the corrected conclusion; the
   future strengthened k-ledger parent (docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md
   §1.3) still types through the same Φ.

## Hard constraints

Read the af run log at the ledger and the challenge texts before designing.
No guessed constants; no estimate changes; no new hypotheses beyond typing;
NOT IN LOCAL REFS discipline; write ONLY inside
`docs/plans/2026-07-27-F2-TYPING-design/`.
