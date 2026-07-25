---
id: conj-hcb
kind: lemma
contract: H-CB: there are universal C_H < infinity and e_H > 0 such that, whenever e=delta+epsilon <= e_H, Q is a level-one one-dimensional delta-projection in an extended epsilon-C*-algebra A, and P,R,S are delta-projections, the maps 1_{M_n} tensor Ha^Q_{P,R}, under the COL-HILB identification with operators on C^n tensor S_{R,Q} and C^n tensor S_{P,Q}, satisfy for every n the adjoint equality, product defect at most C_H*e*||Z||||W||, and the uniform unit, upper-norm, homomorphism, and canonical-identity closeness estimates required by lem_extension; moreover, if the level-one lower modulus of Ha^Q_{P,P} is at least 1/4, then every amplification has lower modulus at least 1-C_H*e, and if Ha^Q_{P,P} is also bijective at level one then every amplification is bijective with inverse norm at most 1+C_H*e; the analogous off-diagonal inverse bound for Ha^Q_{P,R} is asserted only when Ha^Q_{P,R} is bijective at level one and Ha^Q_{R,R} satisfies that diagonal lower-modulus hypothesis; all constants independent of n, dim A, block count, and block dimensions.
defs: def-extended-epsilon-cstar-algebra; def-ha-map; def-delta-projection; def-one-dimensional-delta-projection; def-canonical-corner-identifications
deps: lem-hcb0-compressed-associator; lem-hcb1-column-action; lem-hcb1-variational-identity; lem-hcb-column-hilbert-squared; lem-hcb2-amplified-adjointness; lem-hcb2-product-defect; lem-hcb3-diagonal-unit; lem-hcb3-diagonal-upper-norm; lem-hcb3-diagonal-lower-modulus; lem-hcb3-diagonal-inverse; lem-hcb3-offdiagonal-inverse; lem-hcb3-uniform-square-lower; lem-hcb4-canonical-gram; lem-hcb4-canonical-closeness; lem-hcb4-canonical-inverse; lem-compcb-corner-algebra
status: proved-mod-audit
af: seeded
provenance: docs/plans/2026-07-24-W74F-wave2-artifacts/PROOF-W74F-E-HCB.md (prover); hostile verdict VERDICT-W74F-E-HCB.md (VALID-WITH-CORRECTIONS, contract amended to the verifier's exact clause); decomposition DECOMP-W74F-C-THMAINEXT.md §3 H-CB
owner: A
workspace: proofs/conj-hcb
---

**Status.** Hostile-verified paper proof (fresh codex prover, separate fresh
hostile codex verifier, VALID-WITH-CORRECTIONS), hence `proved-mod-audit`;
not `af`-validated and not L0-rigorous.  The id keeps its historical
`conj-` slug; ids are stable.

**Contract amendment (2026-07-24).** The original conjecture asserted an
unconditional inverse estimate; that clause is FALSE (exact
\(\mathbb C\oplus\mathbb C\) counterexample, PROOF §2.1, verifier-confirmed
genuine).  The contract now carries the verifier's exact conditional
replacement clause.  The verifier confirms this does not weaken what
EXT-CB / `lem_extension` consume: at `tex:1391` the particular \(h_{11}\)
is first proved a level-one \(O(e)\)-isomorphism, meeting both conditional
hypotheses at a universal smallness threshold.

**What is proved.** \(C_H=4000c\) and \(e_H=1/(10000c)\), where \(c\) is
the maximum of the sanctioned COMP-CB / corrected-COL-HILB universal
constants and inverse threshold (explicit relative constants, not absolute
decimals — those inputs carry unnamed universal big-O constants in the
source).  No entrywise \(n\)-sums; no ledger entry depends on \(n\),
\(\dim\mathcal A\), block count, or block dimensions.  The verifier found
no \(n\)-growth family and re-derived corrected COL-HILB independently.

**Verifier corrections (recorded, all wording-level).** (i) the
compressed-unit input splits into a general upper bound and a
nonvanishing-only two-sided bound (no coefficient changes); (ii)
"established separately" means a universal \(1-O(e)\) lower bound then
threshold-shrunk to \(1/4\), not bare bijectivity; (iii) bijectivity of the
canonical corners follows from the Neumann condition, not from two-sided
norm bounds alone.
