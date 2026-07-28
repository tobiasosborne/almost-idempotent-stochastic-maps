<!--
ROLE: search catalog for the sharded lab-book — one entry per report/sections/NN_<slug>.tex shard,
  mirroring its SHARD-ID / filename / SHARD-TITLE / SHARD-KEYWORDS and every SHARD-SUMMARY line.
  scripts/check-report-shards.sh verifies (per included shard) that its id, file path, title, keywords,
  and each summary line appear verbatim here and in report/README.md. Distinct from report/README.md
  (which is the ORDER map). Add an entry in the same commit that adds the shard.
UPDATE POLICY: append/curate in lockstep with report/sections/ (CLAUDE.md Rule 9). Not generated.
-->

# Report shard catalog (search index)

One block per shard: the stable `AISM-NN-LABEL` id, its file, title, the 2–3 summary lines (mirrored
verbatim), and keywords.

<!-- template for a new entry (copy, fill, keep the summary lines byte-identical to the shard header):

## `AISM-00-ROADMAP`
- **File:** `report/sections/00_roadmap.tex`
- **Title:** Roadmap and rigour status
- **Summary:** <SHARD-SUMMARY line 1, verbatim from the shard header>
- **Summary:** <SHARD-SUMMARY line 2, verbatim>
- **Keywords:** <SHARD-KEYWORDS, verbatim>

-->

## `AISM-00-OVERVIEW`
- **File:** `report/sections/00_overview.tex`
- **Title:** Orientation and rigour boundary
- **Summary:** States the open target op-classical and fixes the two equivalent pictures bridged by lem-classical-equiv.
- **Summary:** Describes the five af-validated blocks reproduced here: the bridge, PRH, the COMP tier, the H-CB tier, and the H-CB-parent/EXT tier.
- **Summary:** Records the honesty boundary: only af-validated results appear as lemmas; everything else stays outside this document.
- **Keywords:** overview, op-classical, rigour ladder, signed picture, stochastic picture, COMP tier, H-CB tier

## `AISM-00A-DEFINITIONS`
- **File:** `report/sections/00a_definitions.tex`
- **Title:** The vocabulary
- **Summary:** Frames the generated definitions layer: every term the current proof strategy needs is stated once, typeset from its canonical definitions/ shard by scripts/gen-report-defs.py.
- **Summary:** Explains the two rules that govern the layer -- typeset statement first with the byte-verbatim source demoted to a second check, and scope restricted to the Route-F dependency closure -- plus the macro-translation table that makes a quoted source compile.
- **Summary:** Gives the rigour-ladder legend for definition kinds and statuses, the signed/stochastic reading guidance and the def:<slug> crosslink scheme, and records the honesty boundary: a locked cited definition certifies provenance, never truth, and a definition is never proved.
- **Keywords:** definitions, vocabulary, generated projection, macro-translation table, source check, proof-strategy scope, rigour ladder, cited, consensus, original, crosslinks, signed picture, stochastic picture

## `AISM-01-CLASSICAL-EQUIV`
- **File:** `report/sections/01_classical_equiv.tex`
- **Title:** The signed-stochastic bridge
- **Summary:** Reproduces lem-classical-equiv, the af-validated equivalence of the signed and stochastic formulations up to universal constants.
- **Summary:** Gives a prose account of the binomial-series construction forward and the positive-part renormalisation backward, with the explicit constants of the tree.
- **Keywords:** lem-classical-equiv, af validated, signed picture, stochastic picture, bridge, binomial series

## `AISM-02-PRH`
- **File:** `report/sections/02_prh.tex`
- **Title:** Positive-retract hardening
- **Summary:** Reproduces lem-prh, the af-validated hardening of a positive approximate retract into an exact stochastic idempotent.
- **Summary:** Explains the disjoint-core construction, the conditioning and core-replacement error terms, and the optimisation giving the sharp 2*sqrt(2*epsilon) rate.
- **Keywords:** lem-prh, af validated, positive approximate retract, stochastic idempotent, disjoint cores, square-root rate

## `AISM-03-COMPCB-AMPLIFICATION-NATURALITY`
- **File:** `report/sections/03_compcb_amplification_naturality.tex`
- **Title:** Amplification naturality of the functional calculus
- **Summary:** Reproduces lem-compcb-amplification-naturality, the af-validated commutation of a power-series functional calculus with the unital amplification.
- **Summary:** Explains the partial-sum transport argument and the binomial identification of the inverse-square-root branch used for the theta specialization.
- **Keywords:** lem-compcb-amplification-naturality, af validated, functional calculus, amplification, theta map, binomial series

## `AISM-04-COMPCB-AMPLIFIED-COMPRESSION`
- **File:** `report/sections/04_compcb_amplified_compression.tex`
- **Title:** The amplified compression identity
- **Summary:** Reproduces lem-compcb-amplified-compression, the af-validated identification of the amplified compression map and corner with their entrywise amplifications.
- **Summary:** Explains the uniform theta-domain threshold, the entrywise operator amplification that replaces the diagonal embedding, and the range identification.
- **Keywords:** lem-compcb-amplified-compression, af validated, compression map, amplification, compressed corner, theta domain

## `AISM-05-COMPCB-AMPLIFIED-COMPRESSION-IDENTITIES`
- **File:** `report/sections/05_compcb_amplified_compression_identities.tex`
- **Title:** Idempotence and adjoint symmetry of amplified compressions
- **Summary:** Reproduces lem-compcb-amplified-compression-identities, the af-validated amplified idempotence and dagger-symmetry of the compression maps.
- **Summary:** Explains the transfer of two exact level-one identities through the entrywise amplification, and records the verdict-driven contract amendment binding the ambient algebra.
- **Keywords:** lem-compcb-amplified-compression-identities, af validated, idempotence, involution, amplification, contract amendment

## `AISM-06-COMPCB-ENTRYWISE-COMPRESSION-NATURALITY`
- **File:** `report/sections/06_compcb_entrywise_compression_naturality.tex`
- **Title:** Entrywise compression naturality at a matrix unit
- **Summary:** Reproduces lem-compcb-entrywise-compression-naturality, the af-validated slotwise action of an amplified compression on an E11-supported element.
- **Summary:** Explains the specialization of the amplification identity to a square corner and the elementary-tensor evaluation that finishes it.
- **Keywords:** lem-compcb-entrywise-compression-naturality, af validated, matrix unit, elementary tensor, compression, slotwise action

## `AISM-07-COMPCB-RECTANGULAR-PRODUCT`
- **File:** `report/sections/07_compcb_rectangular_product.tex`
- **Title:** The uniform rectangular compressed-product estimate
- **Summary:** Reproduces lem-compcb-rectangular-product, the af-validated bound comparing the compressed and ambient products uniformly in the amplification level.
- **Summary:** Explains the unpacking of the level-one big-O constant and the amplified verification of its hypotheses, and records the tree's explicit definition of a compatible amplified rectangular pair.
- **Keywords:** lem-compcb-rectangular-product, af validated, compressed product, rectangular pair, uniform constant, amplification

## `AISM-08-COMPCB-AMPLIFIED-ALMOST-CONTAINMENT`
- **File:** `report/sections/08_compcb_amplified_almost_containment.tex`
- **Title:** Amplified almost-containment of corners
- **Summary:** Reproduces lem-compcb-amplified-almost-containment, the af-validated statement that an inner corner is almost fixed by an outer compression.
- **Summary:** Explains the uniform norm ledger, the fixed-point step in the source corner, and the transfer of almost-invariance to the outer projections.
- **Keywords:** lem-compcb-amplified-almost-containment, af validated, almost containment, corner inclusion, approximate associativity, uniform constants

## `AISM-09-COMPCB-COMPRESSED-UNIT-NORM`
- **File:** `report/sections/09_compcb_compressed_unit_norm.tex`
- **Title:** The compressed-unit norm estimate
- **Summary:** Reproduces lem-compcb-compressed-unit-norm, the af-validated one-sided bound for every delta-projection and two-sided bound for nonvanishing ones.
- **Summary:** Explains the vanishing/nonvanishing dichotomy, the direct comparison of the compressed unit with the projection, and the audit that forced the byte-matched norm axioms to be provisioned.
- **Keywords:** lem-compcb-compressed-unit-norm, af validated, compressed unit, nonvanishing projection, dichotomy, missing-axiom audit

## `AISM-10-HCB2-AMPLIFIED-ADJOINTNESS`
- **File:** `report/sections/10_hcb2_amplified_adjointness.tex`
- **Title:** Exact adjointness of the amplified Ha map
- **Summary:** Reproduces lem-hcb2-amplified-adjointness, the af-validated exact identity relating the operator adjoint of an amplified Ha map to the involution of its argument.
- **Summary:** Explains the exact product-reversal identity, the level-one uniqueness argument in the Ha defining relation, and the blockwise transport to amplifications.
- **Keywords:** lem-hcb2-amplified-adjointness, af validated, Ha map, adjointness, involution, product reversal

## `AISM-11-COMPCB-COMPRESSED-UNIT-ACTION`
- **File:** `report/sections/11_compcb_compressed_unit_action.tex`
- **Title:** The uniform compressed-unit action
- **Summary:** Reproduces lem-compcb-compressed-unit-action, the af-validated statement that compressed units act as approximate two-sided identities on rectangular corners.
- **Summary:** Explains the comparison of the compressed unit with its projection, the ambient action estimate, and the final passage to the compressed product.
- **Keywords:** lem-compcb-compressed-unit-action, af validated, compressed unit, approximate identity, rectangular corner, uniform constants

## `AISM-12-COMPCB-ROW-COLUMN-PRODUCT`
- **File:** `report/sections/12_compcb_row_column_product.tex`
- **Title:** The row-column compressed-product estimate
- **Summary:** Reproduces lem-compcb-row-column-product, the af-validated compressed-versus-ambient comparison for a row times a column.
- **Summary:** Explains the square embedding into one extra block, the isometry of zero-padding, and the reduction to the validated rectangular-product estimate.
- **Keywords:** lem-compcb-row-column-product, af validated, row-column product, zero padding, square embedding, compressed product

## `AISM-13-HCB0-COMPRESSED-ASSOCIATOR`
- **File:** `report/sections/13_hcb0_compressed_associator.tex`
- **Title:** The uniform compressed associator estimate
- **Summary:** Reproduces lem-hcb0-compressed-associator, the af-validated bound on the failure of associativity of the compressed product.
- **Summary:** Explains the five-term telescope through the ambient product, the role of the epsilon-associator axiom, and the endpoint-safe constant bookkeeping.
- **Keywords:** lem-hcb0-compressed-associator, af validated, associator, compressed product, telescope, uniform constants

## `AISM-14-COMPCB-CORNER-ALGEBRA`
- **File:** `report/sections/14_compcb_corner_algebra.tex`
- **Title:** The compressed corner as an extended approximate C*-algebra
- **Summary:** Reproduces lem-compcb-corner-algebra, the af-validated statement that a nonvanishing compressed corner is an extended C_ca*e-C*-algebra.
- **Summary:** Explains the obligation-by-obligation verification of the axioms at every matrix level and the constant ledger that unifies them.
- **Keywords:** lem-compcb-corner-algebra, af validated, compressed corner, extended C*-algebra, operator space, axiom verification

## `AISM-15-HCB-COLUMN-HILBERT-SQUARED`
- **File:** `report/sections/15_hcb_column_hilbert_squared.tex`
- **Title:** The corrected amplified column-Hilbert estimate
- **Summary:** Reproduces lem-hcb-column-hilbert-squared, the af-validated comparison of the amplified column inner product with the squared column norm.
- **Summary:** Explains the three scalar estimates and their synthesis, and records the withdrawn zero-padding route that forced two new dependencies.
- **Keywords:** lem-hcb-column-hilbert-squared, af validated, column Hilbert, squared estimate, withdrawn route, nonvanishing bridge

## `AISM-16-COMPCB-SINGLE-COMPRESSION-TRANSFER`
- **File:** `report/sections/16_compcb_single_compression_transfer.tex`
- **Title:** Single-compression transfer of an extended inclusion
- **Summary:** Reproduces lem-compcb-single-compression-transfer, the af-validated statement that restricting an extended inclusion to an ideal and compressing once yields an extended inclusion.
- **Summary:** Explains the ideal-unit projection, the exact dagger and unit clauses, the compression-closeness estimate, and the four-term multiplicativity telescope.
- **Keywords:** lem-compcb-single-compression-transfer, af validated, extended inclusion, ideal, compression, multiplicativity telescope

## `AISM-17-HCB1-VARIATIONAL-IDENTITY`
- **File:** `report/sections/17_hcb1_variational_identity.tex`
- **Title:** The amplified Ha variational identity
- **Summary:** Reproduces lem-hcb1-variational-identity, the af-validated exact identity expressing the Ha defect as a compressed associator.
- **Summary:** Explains the entrywise expansion, the summation of the level-one defining relation, and the cancellation against the amplified column display.
- **Keywords:** lem-hcb1-variational-identity, af validated, Ha map, variational identity, associator, contract amendment

## `AISM-18-HCB1-COLUMN-ACTION`
- **File:** `report/sections/18_hcb1_column_action.tex`
- **Title:** The uniform Ha column action
- **Summary:** Reproduces lem-hcb1-column-action, the af-validated estimate that the amplified Ha map acts on columns like left multiplication up to O(e).
- **Summary:** Explains the compressed-unit nondegeneracy proved inside the operator algebra, the defect pairing, and the self-pairing cancellation that avoids Riesz duality.
- **Keywords:** lem-hcb1-column-action, af validated, Ha map, column action, nondegeneracy, self-pairing

## `AISM-19-HCB2-PRODUCT-DEFECT`
- **File:** `report/sections/19_hcb2_product_defect.tex`
- **Title:** The uniform amplified Ha product defect
- **Summary:** Reproduces lem-hcb2-product-defect, the af-validated bound on the failure of the amplified Ha map to be multiplicative.
- **Summary:** Explains the amplified column-norm calibration, the uniform Ha operator bound, and the four-term telescope evaluated on columns.
- **Keywords:** lem-hcb2-product-defect, af validated, Ha map, product defect, telescope, operator norm

## `AISM-20-HCB3-DIAGONAL-UNIT`
- **File:** `report/sections/20_hcb3_diagonal_unit.tex`
- **Title:** The uniform diagonal Ha unit estimate
- **Summary:** Reproduces lem-hcb3-diagonal-unit, the af-validated statement that the amplified Ha map sends the amplified compressed unit to an approximate identity operator.
- **Summary:** Explains the direct level-n bound on the amplified unit, the two-term split into a column-action defect and a unit-action defect, and the coordinate-sum conversion.
- **Keywords:** lem-hcb3-diagonal-unit, af validated, Ha map, compressed unit, approximate identity, coordinate sum

## `AISM-21-HCB3-DIAGONAL-UPPER-NORM`
- **File:** `report/sections/21_hcb3_diagonal_upper_norm.tex`
- **Title:** The uniform diagonal Ha upper norm
- **Summary:** Reproduces lem-hcb3-diagonal-upper-norm, the af-validated bound making the amplified diagonal Ha map a contraction up to 1+O(e).
- **Summary:** Explains the matrix-uniform square estimate, the quadratic recurrence for the operator norm, and the scalar root argument that closes it.
- **Keywords:** lem-hcb3-diagonal-upper-norm, af validated, Ha map, operator norm, quadratic recurrence, corner algebra

## `AISM-22-HCB3-UNIFORM-SQUARE-LOWER`
- **File:** `report/sections/22_hcb3_uniform_square_lower.tex`
- **Title:** The uniform square lower estimate
- **Summary:** Reproduces lem-hcb3-uniform-square-lower, the af-validated matrix-uniform lower bound for the compressed square of a corner element.
- **Summary:** Explains the two-branch argument: a vanishing projection collapses the corner to zero via the theta calculus, and a nonvanishing one inherits the lower C*-axiom at every level.
- **Keywords:** lem-hcb3-uniform-square-lower, af validated, lower C* axiom, vanishing corner, theta calculus, corner algebra

## `AISM-23-HCB3-DIAGONAL-LOWER-MODULUS`
- **File:** `report/sections/23_hcb3_diagonal_lower_modulus.tex`
- **Title:** Diagonal Ha lower-modulus propagation
- **Summary:** Reproduces lem-hcb3-diagonal-lower-modulus, the af-validated propagation of a level-one lower-modulus hypothesis to every amplification.
- **Summary:** Explains the quadratic root gap, the dichotomy for the level-n lower moduli, and the Ruan halving plus dyadic bootstrap that carries the level-one bound upward.
- **Keywords:** lem-hcb3-diagonal-lower-modulus, af validated, lower modulus, quadratic recurrence, Ruan axioms, dyadic bootstrap

## `AISM-24-HCB3-DIAGONAL-INVERSE`
- **File:** `report/sections/24_hcb3_diagonal_inverse.tex`
- **Title:** Diagonal Ha inverse propagation
- **Summary:** Reproduces lem-hcb3-diagonal-inverse, the af-validated propagation of level-one bijectivity and lower modulus to bijectivity of every amplification.
- **Summary:** Explains the exact entrywise inversion, the imported lower-modulus bound, and the elementary reciprocal estimate that produces the 1+C_inv*e inverse norm.
- **Keywords:** lem-hcb3-diagonal-inverse, af validated, Ha map, bijectivity, inverse norm, entrywise amplification

## `AISM-25-HCB3-OFFDIAGONAL-INVERSE`
- **File:** `report/sections/25_hcb3_offdiagonal_inverse.tex`
- **Title:** Off-diagonal Ha inverse propagation
- **Summary:** Reproduces lem-hcb3-offdiagonal-inverse, the af-validated rectangular counterpart of the diagonal inverse estimate.
- **Summary:** Explains the rectangular square estimate, the adjoint-product route to an amplified lower modulus anchored at the diagonal index, and the reciprocal bound.
- **Keywords:** lem-hcb3-offdiagonal-inverse, af validated, Ha map, rectangular corner, lower modulus, inverse norm

## `AISM-26-HCB4-CANONICAL-GRAM`
- **File:** `report/sections/26_hcb4_canonical_gram.tex`
- **Title:** The canonical corner Gram estimate
- **Summary:** Reproduces lem-hcb4-canonical-gram, the af-validated two-sided comparison of the ambient corner norm with the norm of the canonical identification.
- **Summary:** Explains the exact Gram scalarisation, the two uniform inputs it is fed, the scalar square-root passage, and the adjoint transfer to the row corner.
- **Keywords:** lem-hcb4-canonical-gram, af validated, canonical corner identification, Gram scalarisation, compressed unit, row transfer

## `AISM-27-HCB4-CANONICAL-CLOSENESS`
- **File:** `report/sections/27_hcb4_canonical_closeness.tex`
- **Title:** Canonical Ha closeness
- **Summary:** Reproduces lem-hcb4-canonical-closeness, the af-validated O(e) closeness of the two special Ha maps to the canonical corner identifications, uniformly in the amplification level.
- **Summary:** Explains the normalised compressed-unit scalar that carries the whole defect, the adjoint reduction to the column action, and the exact scalarisation of the comparison term.
- **Keywords:** lem-hcb4-canonical-closeness, af validated, Ha map, canonical identification, compressed unit normalisation, adjoint reduction

## `AISM-28-HCB4-CANONICAL-INVERSE`
- **File:** `report/sections/28_hcb4_canonical_inverse.tex`
- **Title:** The canonical Ha inverse estimate
- **Summary:** Reproduces lem-hcb4-canonical-inverse, the af-validated complete bijectivity of the two special Ha maps with amplified inverses within O(e) of the canonical ones.
- **Summary:** Explains the canonical inverse bound, the quantitative Neumann step, and the closed-corner completeness branch required for the Banach target.
- **Keywords:** lem-hcb4-canonical-inverse, af validated, Neumann series, complete bijectivity, Banach target, closed corner

## `AISM-29-HCB`
- **File:** `report/sections/29_hcb.tex`
- **Title:** The H-CB parent contract
- **Summary:** Reproduces conj-hcb, the af-validated parent statement of the H-CB tier, assembled from the validated tier lemmas with one universal constant pair.
- **Summary:** Explains the aggregation of thresholds and coefficients, the clause-by-clause discharge, and the refuted unconditional inverse clause that forced the conditional wording.
- **Keywords:** conj-hcb, af validated, H-CB tier, constant aggregation, conditional inverse, contract amendment

## `AISM-30-EXTCB-ONE-DIMENSIONAL-CORNERS`
- **File:** `report/sections/30_extcb_one_dimensional_corners.tex`
- **Title:** One-dimensional corner calculus
- **Summary:** Reproduces lem-extcb-one-dimensional-product and lem-extcb-one-dimensional-corner-dimension, the af-validated multiplicativity of the compressed product through a one-dimensional middle projection and its dimension corollary.
- **Summary:** Explains the scalarisation of the compressed square, the three-term squared-norm comparison and the square-root passage, then the injective-transport argument bounding the corner dimension.
- **Keywords:** lem-extcb-one-dimensional-product, lem-extcb-one-dimensional-corner-dimension, af validated, one-dimensional projection, compressed product, corner dimension

## `AISM-31-EXTCB-CORNER-DIMENSION-ADDITIVITY`
- **File:** `report/sections/31_extcb_corner_dimension_additivity.tex`
- **Title:** Corner-dimension additivity
- **Summary:** Reproduces lem-extcb-corner-dimension-additivity, the af-validated splitting of a compressed corner over two projection bases into the direct sum of its blocks.
- **Summary:** Explains the binary splitting lemma and its Neumann inversion, the transport of the second index by the involution, and the two finite inductions that assemble the double sum.
- **Keywords:** lem-extcb-corner-dimension-additivity, af validated, projection basis, binary splitting, Neumann series, direct sum

## `AISM-32-EXTCB1-DIMENSION-SELECTION`
- **File:** `report/sections/32_extcb1_dimension_selection.tex`
- **Title:** Dimension selection in an EXT-CB datum
- **Summary:** Reproduces lem-extcb1-close-corner-dimension and lem-extcb1-cross-corner-dimension, the af-validated identification of the cross-corner dimensions of an EXT-CB datum as (r,1).
- **Summary:** Explains the close-idempotent range transport, the matrix-unit normalisation of the transported diagonal, and the dichotomy that additivity converts into the count r.
- **Keywords:** lem-extcb1-close-corner-dimension, lem-extcb1-cross-corner-dimension, af validated, close idempotents, matrix units, corner dimension, EXT-CB datum

## `AISM-33-EXTCB-FOUR-CORNER-NORM`
- **File:** `report/sections/33_extcb_four_corner_norm.tex`
- **Title:** The four-corner assembled norm estimate
- **Summary:** Reproduces lem-extcb-four-corner-norm, the af-validated two-sided norm control of the map assembled from four corner maps, uniform in the amplification level.
- **Summary:** Explains the coarse block conditioning, the sixteen-term square defect, and the scalar C*-bootstrap that upgrades crude constants to 1 plus or minus O(e).
- **Keywords:** lem-extcb-four-corner-norm, af validated, four-corner merging datum, block conditioning, square defect, C* bootstrap

## `AISM-34-EXTCB-FOUR-CORNER-MERGE`
- **File:** `report/sections/34_extcb_four_corner_merge.tex`
- **Title:** The complete four-corner merge
- **Summary:** Reproduces lem-extcb-four-corner-merge, the af-validated assembly of four fixed bijective level-one corner maps into a single extended isomorphism.
- **Summary:** Explains the single-level-one-map assembly, the multiplicative defect, the Neumann coverage argument for surjectivity, and the counterexample that forced the total-defect smallness hypothesis.
- **Keywords:** lem-extcb-four-corner-merge, af validated, merge, extended isomorphism, Neumann coverage, contract amendment, counterexample

## `AISM-35-EXTCB`
- **File:** `report/sections/35_extcb.tex`
- **Title:** The EXT-CB parent contract
- **Summary:** Reproduces conj-extcb, the af-validated parent statement of the EXT tier: one map on M_{r+1} extending a level-one datum, carried at every amplification by one unitary and four fixed corner maps.
- **Summary:** Explains the dimension-free exact-target correction, the spatial four-corner system transported through the level-one Ha inverses, the ordered use of the conditional H-CB clauses, and the merge that closes the tier.
- **Keywords:** conj-extcb, af validated, EXT tier, exact-target correction, Newton iteration, spatial four-corner system, merge

## `AISM-36-ROUTEF-PRH-FINISH`
- **File:** `report/sections/36_routef_prh_finish.tex`
- **Title:** The Route F finish edge
- **Summary:** Reproduces lem-routef-prh-finish, the af-validated conditional PRH finish edge within Route F: retract data for a row-stochastic Q at defect eta yields a stochastic idempotent within (K+4*sqrt(2K))*sqrt(eta).
- **Summary:** Explains the scalar preparation that converts the hypothesis eta-window into the PRH window, the exhaustive dimension split guarding the import of lem-prh, and the two-term triangle finish.
- **Summary:** States plainly that this is an implication whose antecedent is supplied by no result reproduced here, so no unconditional square-root bound follows and op-classical stays open.
- **Keywords:** lem-routef-prh-finish, af validated, Route F, positive approximate retract, stochastic idempotent, square-root rate, conditional finish

## `AISM-37-STAGE1-QUANTITATIVE-IFT`
- **File:** `report/sections/37_stage1_quantitative_ift.tex`
- **Title:** Quantitative inverse-function control
- **Summary:** Reproduces lem-stage1-quantitative-inverse-function, the af-validated statement that a C1 map whose derivative stays uniformly close to a fixed Banach-space isomorphism is injective, two-sidedly controlled on secants, and covers a definite ball.
- **Summary:** Explains the normalisation to a perturbation of the identity, the segment plus Banach-valued fundamental-theorem estimate for the secant error, and the centred covering by a contraction on a closed ball.
- **Summary:** Records the three hostile challenges the tree survived, including the counterexample that forced the covering step to be specialised to the map it is applied to.
- **Keywords:** lem-stage1-quantitative-inverse-function, af validated, inverse function theorem, secant estimate, Banach fixed point, covering, Stage 1

## `AISM-38-STAGE1-EXACT-UNIT`
- **File:** `report/sections/38_stage1_exact_unit.tex`
- **Title:** Dimension-free exact-unit rectification
- **Summary:** Reproduces lem-stage1-exact-unit-rectification, the af-validated replacement of an approximate unit by an exact one: every epsilon-C*-algebra with small enough defect carries, on the same involutive normed space, an exact unit and a product at distance O(epsilon) from the original.
- **Summary:** Explains the norm-one self-adjoint rescaling of the unit, the Hermitian norming functional obtained by Hahn-Banach and symmetrisation, and the rank-one correction of the product that makes the new unit exactly two-sided.
- **Summary:** Records the hostile challenge and its counterexample, the explicit universal witnesses, and the two hypotheses the exported tree carries but never uses.
- **Keywords:** lem-stage1-exact-unit-rectification, af validated, epsilon-C*-algebra, exact unit, Hahn-Banach, Hermitian functional, rank-one correction, Stage 1

## `AISM-42-ROUTEF-F0-SEAM`
- **File:** `report/sections/42_routef_f0_seam.tex`
- **Title:** The F0 seam: a stochastic matrix as a unital completely positive map
- **Summary:** Reproduces the two af-validated F0 seam rows lem-routef-f0-ucp-lift and lem-routef-f0-defect-identity, which carry a row-stochastic Q into the matrix algebra M_n as the UCP map Phi = J Q_C D.
- **Summary:** Explains the real-versus-complex typing the seam turns on, the diagonal-compression argument that makes extraction and inclusion completely positive, and the two-sided matrix-level computation giving the defect identity with constant exactly one.
- **Summary:** Records that the seam consumes no smallness hypothesis and performs no conversion of the defect, and that neither row on its own bears on op-classical, which is open.
- **Keywords:** lem-routef-f0-ucp-lift, lem-routef-f0-defect-identity, af validated, Route F, F0 seam, diagonal inclusion, diagonal extraction, complete positivity, cb norm, defect identity

## `AISM-43-ROUTEF-AI-LEDGER`
- **File:** `report/sections/43_routef_ai_ledger.tex`
- **Title:** The approximate-algebra ledger for an almost-idempotent UCP map
- **Summary:** Reproduces three af-validated rows: lem-kitaev-almost-idemp-audit, the corrected audit turning an almost-idempotent UCP map into an extended epsilon-C*-algebra; lem-routef-functional-calculus-closeness, the C_theta*eta bound on the functional-calculus projector; and lem-routef-ai-defect-linearization, which linearises the resulting defect.
- **Summary:** Explains the spectral correction package built from the binomial series, the internally constructed iterated Stinespring stack that carries the two amplified associativity estimates, and the telescoping that converts them into the epsilon-C*-algebra axioms at every amplification.
- **Summary:** Records the local source type and index corrections the audit had to apply, and the banking-time contract reconciliation of the linearization row, and states that the ledger is an implication whose consumer is not af-validated.
- **Keywords:** lem-kitaev-almost-idemp-audit, lem-routef-functional-calculus-closeness, lem-routef-ai-defect-linearization, af validated, Route F, extended epsilon-C*-algebra, functional calculus, Stinespring stack, associativity defect, defect linearization

## `AISM-44-ROUTEF-F2-F3`
- **File:** `report/sections/44_routef_f2_f3.tex`
- **Title:** The F2/F3 block: manufacturing the positive unital retract pair
- **Summary:** Reproduces the two af-validated rows lem-routef-f2-positive-unital-compression and lem-routef-f3-retract-defect, which convert an approximate UCP factorization of the F0 lift through a finite-dimensional C*-algebra into a positive unital pair A, M with the three estimates the Route F finish edge consumes.
- **Summary:** Explains the commutator argument that forces commutativity of the intermediate algebra, the in-tree norm-two Pauli witness that replaces the unavailable finite-dimensional classification, the coordinate isomorphism built from the byte-matched projection basis, and the exact identity behind the retract-defect bound.
- **Summary:** States that the factorization hypotheses are supplied by a registry row that is not af-validated, so the Route F chain is not closed here and op-classical stays open.
- **Keywords:** lem-routef-f2-positive-unital-compression, lem-routef-f3-retract-defect, af validated, Route F, positive unital compression, commutativity forcing, projection basis, retract defect, lower modulus
## `AISM-45-STAGE1-POLAR-CHARTS`
- **File:** `report/sections/45_stage1_polar_charts.tex`
- **Title:** Rectified algebras and graph charts on the approximate unitaries
- **Summary:** Reproduces lem-stage1-rectified-cstar-control, lem-stage1-unitary-graph-control and lem-stage1-maurer-cartan-trivialization, the three af-validated results that turn an epsilon-C*-algebra into an exactly unital one satisfying every axiom and then coordinatise its unitary set by C1 graph charts.
- **Summary:** Explains the rescaled unit and rank-one product correction that transfer every axiom at epsilon_r = 100*epsilon_X, the normal-derivative Neumann step that solves the graph equation by the quantitative inverse-function lemma, and the differentiated defining equation that makes the Maurer-Cartan trivialization C1.
- **Summary:** Records the explicit universal witnesses, the archived nodes of the graph tree, and the challenge that forced the trivialization inverse to be derived from an implicit-function formula rather than from mere chart regularity.
- **Keywords:** lem-stage1-rectified-cstar-control, lem-stage1-unitary-graph-control, lem-stage1-maurer-cartan-trivialization, af validated, epsilon-C*-algebra, graph chart, Maurer-Cartan trivialization, Stage 1

## `AISM-46-STAGE1-POLAR-RETRACTION`
- **File:** `report/sections/46_stage1_polar_retraction.tex`
- **Title:** The closed polar retraction and its coherence
- **Summary:** Reproduces lem-stage1-polar-retraction, the af-validated statement that (U,H) maps to U bold-dot H is a C1 diffeomorphism from calU times a delta-ball of Hermitians onto an open set sandwiched between two defect sublevel sets, with a normalised inverse (u_delta, h_delta).
- **Summary:** Reproduces lem-stage1-polar-coherence-naturality, the af-validated conditional statement that any two polar data agree on the overlap of their images and that both components are natural for the circle action.
- **Summary:** Explains the coordinate map p_V and its near-identity derivative, the contraction that produces the polar zero, the global injectivity argument in a chart centred at the point itself, and the two-sided radius sandwich; records that the coherence row asserts no existence.
- **Keywords:** lem-stage1-polar-retraction, lem-stage1-polar-coherence-naturality, af validated, polar decomposition, C1 diffeomorphism, radius sandwich, scalar naturality, Stage 1

## `AISM-47-STAGE1-GROUP-LAWS`
- **File:** `report/sections/47_stage1_group_laws.tex`
- **Title:** Quantitative approximate group laws on the unitaries
- **Summary:** Reproduces lem-stage1-group-domain-membership and lem-stage1-group-closeness, the two af-validated sub-lemmas showing that a product U bold-dot V and an adjoint U^dagger of unitaries lie in the polar domain with right inverses, and that the polar projection moves them by at most C_grp*epsilon_r.
- **Summary:** Reproduces lem-stage1-approximate-group-laws, the af-validated parent: the polar projection of the product and of the adjoint are globally defined C1 maps mu and sigma with exact basepoint identities and five defect estimates of size C_grp*epsilon_r.
- **Summary:** Records the balloon abort that forced the parent proof to be factored into these two deliberately sibling-independent children, the binding in-scope smallness discipline, and the endpoint discipline that keeps every estimate meaningful at epsilon_r = 0.
- **Keywords:** lem-stage1-group-domain-membership, lem-stage1-group-closeness, lem-stage1-approximate-group-laws, af validated, approximate group, associator defect, balloon repair, endpoint discipline, Stage 1

## `AISM-48-STAGE1-SMOOTH-POLAR`
- **File:** `report/sections/48_stage1_smooth_polar.tex`
- **Title:** Paths, the inversion derivative, and the smooth atlas
- **Summary:** Reproduces lem-stage1-polar-path-admissibility, the af-validated statement that the straight segment between two nearby unitaries stays in the polar domain and projects to a jointly continuous, circle-equivariant path joining them.
- **Summary:** States lem-stage1-inversion-derivative-control (af validation RETRACTED 2026-07-28, now a stated candidate): the polar inversion sigma retains the sJ graph chart on a small ball and its coordinate representative has derivative within C_der*(epsilon_r+r) of minus the identity.
- **Summary:** Reproduces lem-stage1-smooth-unitary-atlas, the af-validated conditional upgrade of the C1 graph functions to C-infinity by Lee's implicit function theorem, leaving every point, chart and first derivative unchanged.
- **Keywords:** lem-stage1-polar-path-admissibility, lem-stage1-inversion-derivative-control, lem-stage1-smooth-unitary-atlas, af validated, projected straight path, chart retention, implicit function theorem, smooth embedded manifold, Stage 1

## `AISM-49-STAGE1-SMOOTH-UPGRADES`
- **File:** `report/sections/49_stage1_smooth_upgrades.tex`
- **Title:** The smooth polar inverse, smooth operations, and the polar arithmetic
- **Summary:** Reproduces lem-stage1-smooth-polar-inverse, the af-validated conditional upgrade of the bijective C1 polar map Pi_delta to a smooth diffeomorphism whose same set-theoretic inverse (u_delta, h_delta) is smooth, obtained chartwise from Lee's inverse function theorem with no point or first derivative changed.
- **Summary:** Reproduces lem-stage1-smooth-unitary-operations, the af-validated statement that the circle action and the polar-projected product and inversion mu and sigma are smooth maps into the embedded manifold calU and obey the exact covariance identities mu(cU,dV) = cd mu(U,V) and sigma(cU) = conj(c) sigma(U).
- **Summary:** Reproduces lem-stage1-polar-scalar-arithmetic, the af-validated universal scalar row: the derived scales delta_*, epsilon_*^r, e_S1, r_iso built from any admissible coefficients and margins make every epsilon_X below e_S1 satisfy all seven Stage-1 polar guards, with the quantitative slack r_- >= 3 delta_*/4 and eta <= delta_*/4.
- **Keywords:** lem-stage1-smooth-polar-inverse, lem-stage1-smooth-unitary-operations, lem-stage1-polar-scalar-arithmetic, af validated, smooth diffeomorphism, inverse function theorem, circle equivariance, guard arithmetic, witness tuple, Stage 1
## `AISM-50-STAGE1-POLAR-TRANSPORTS`
- **File:** `report/sections/50_stage1_polar_transports.tex`
- **Title:** Parameterized transports of the Stage-1 polar layer
- **Summary:** Reproduces four af-validated Stage-1 polar transport rows, lem-stage1-rectified-cstar-transport, lem-stage1-unitary-graph-transport, lem-stage1-maurer-cartan-transport and lem-stage1-polar-retraction-transport, which re-state four fixed-constant polar lemmas at the named fields of an arbitrary Stage-1 polar witness datum.
- **Summary:** States the common transport skeleton once: instantiate the parent's universal witnesses as thresholds, derive epsilon_r >= 0 from the product-norm axiom at the unit, transport every scalar guard by coefficient/margin monotonicity, apply the parent, and weaken the conclusion coefficients back to the fields of the tuple.
- **Summary:** Records the Maurer-Cartan challenges that forced an arbitrary-family tangent argument independent of the distinguished graph family, with the conditional uniqueness bridge kept explicitly conditional.
- **Keywords:** lem-stage1-rectified-cstar-transport, lem-stage1-unitary-graph-transport, lem-stage1-maurer-cartan-transport, lem-stage1-polar-retraction-transport, af validated, witness data, transport, guard monotonicity, Stage 1

## `AISM-51-STAGE1-POLAR-TRANSPORTS-II`
- **File:** `report/sections/51_stage1_polar_transports_ii.tex`
- **Title:** Parameterized transports of the Stage-1 polar layer, II: paths and the inversion derivative
- **Summary:** Reproduces the af-validated transport lem-stage1-polar-path-transport and states lem-stage1-inversion-derivative-transport (af validation RETRACTED 2026-07-28, now a stated candidate); both carry projected-path / inversion-derivative content to the parameterized witness-data form with explicit definite descriptions for the polar and graph binders.
- **Summary:** Explains the joint-threshold construction that transports five scalar guards to four fixed-constant parents simultaneously, and the three binder identifications that discharge the explicit u_delta, g_sJ and sigma descriptions from af-validated imports.
- **Summary:** Records the inversion-derivative run-1 STUCK abort on bare-anaphor binders in the sole allowed external, repaired by widening the deps line with six T0 imports while leaving the contract byte-unchanged.
- **Keywords:** lem-stage1-polar-path-transport, lem-stage1-inversion-derivative-transport, af validated, witness data, transport, definite description, deps widening, Stage 1

## `AISM-39-ARGUMENT-DAG`
- **File:** `report/sections/39_argument_dag.tex`
- **Title:** Argument-DAG atlas: the Route-F proof chain for op-classical
- **Summary:** Generated atlas of the sub-DAG that carries the argument landing op-classical: the transitive deps/routes closure of the root together with the Route-F families, drawn layered and landscape, one detail page per phase.
- **Summary:** Nodes are colour- and glyph-coded by rigour rung (af-validated / cited / proved / seeded / proved-mod-audit-or-conjecture / stated / open) using the same proof_class function that colours the Mermaid twin argument/DAG.md, so the two views cannot disagree.
- **Summary:** Every node carries the anchor dag:<id> and links back to its report statement; the design-pending GAP compositions are drawn dashed and are explicitly NOT registry edges.
- **Keywords:** argument DAG, atlas, Route F, op-classical, dependency graph, rigour ladder, generated figure, crosslink anchors, GAP composition

## `AISM-40-CAMPAIGN-STATISTICS`
- **File:** `report/sections/40_campaign_statistics.tex`
- **Title:** The campaign in numbers
- **Summary:** Machine-generated census of the whole proof campaign across this repository and its progenitor: calendar, rigour ladder over time, arm allocation, adversarial elevations, worker jobs, evidence and dead routes.
- **Summary:** Carries no mathematical claim and promotes nothing up the rigour ladder; every figure is a count of an artifact in the repositories, with the unrecoverable quantities (token and cost figures) named as gaps rather than estimated.
- **Summary:** The body is generated by scripts/gen-report-stats.py from a committed data snapshot, so the freshness gate is stable across ordinary commits; the staleness semantics are stated in the colophon.
- **Keywords:** campaign statistics, metrics, fr controller, af elevations, rigour ladder, dead routes, progenitor comparison, generated layer

## `AISM-41-STATUS-OUTLOOK`
- **File:** `report/sections/41_status_outlook.tex`
- **Title:** Status and outlook
- **Summary:** Records what this report validates, where the live route now stops, and the quarantined assembly interface.
- **Summary:** Tabulates the validated registry results not reproduced on the live route, with every row traced to the generated argument index.
- **Keywords:** status, outlook, conj-hcb, conj-extcb, registry index, live route, off-route table
