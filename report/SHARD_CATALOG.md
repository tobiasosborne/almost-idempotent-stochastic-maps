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
- **Summary:** Describes the four af-validated blocks reproduced here: the bridge, PRH, the COMP tier, and the H-CB tier.
- **Summary:** Records the honesty boundary: only af-validated results appear as lemmas; everything else stays outside this document.
- **Keywords:** overview, op-classical, rigour ladder, signed picture, stochastic picture, COMP tier, H-CB tier

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

## `AISM-22-STATUS-OUTLOOK`
- **File:** `report/sections/22_status_outlook.tex`
- **Title:** Status and outlook
- **Summary:** Records what this report validates, what remains on the live H-CB and EXT queue, and the quarantined assembly interface.
- **Summary:** Tabulates the results removed from the previous report as a route-pivot record, each with its retained registry status.
- **Keywords:** status, outlook, conj-hcb, EXT tier, quarantine, route pivot, deprecation table
