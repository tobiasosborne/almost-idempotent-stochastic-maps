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
- **Title:** Roadmap and rigour status
- **Summary:** Orients the lab-book around the open target op-classical and the report's strict rigour boundary.
- **Summary:** Records the linear-law versus sqrt-envelope headline as orientation, not as a promoted theorem.
- **Keywords:** overview, op-classical, rigour ladder, linear law, sharp exponent

## `AISM-01-CLASSICAL-EQUIV`
- **File:** `report/sections/01_classical_equiv.tex`
- **Title:** The signed-stochastic bridge
- **Summary:** Reproduces the registry contract for lem-classical-equiv, one of the af-validated rigorous results.
- **Summary:** Summarizes the clean 29-node proof tree and records its role as the signed-to-stochastic bridge.
- **Keywords:** lem-classical-equiv, af validated, signed picture, stochastic picture, bridge

## `AISM-02-HEIGHT-COLLAPSE`
- **File:** `report/sections/02_height_collapse.tex`
- **Title:** Height collapse
- **Summary:** Reproduces the registry contract for obs-height-collapse as an af-validated rigorous obstruction.
- **Summary:** Summarizes the clean 19-node proof tree and its role in isolating the remaining sigma-cap input.
- **Keywords:** obs-height-collapse, af validated, height, invisible mass, sigma cap

## `AISM-03-MASS-SPLIT`
- **File:** `report/sections/03_mass_split.tex`
- **Title:** Mass split bookkeeping
- **Summary:** Reproduces the registry contract for lem-mass-split, an af-validated row-sum identity.
- **Summary:** Summarizes the clean 9-node proof tree and its role as a factored dependency of halo collapse.
- **Keywords:** lem-mass-split, af validated, negative mass, row sum, halo collapse

## `AISM-04-RESIDUAL-LOWER`
- **File:** `report/sections/04_residual_lower.tex`
- **Title:** Convex outsourcing
- **Summary:** Reproduces the registry contract for lem-residual-lower, an af-validated frame-free convexity fact.
- **Summary:** Summarizes the clean 32-live-node proof tree and its lower-bound role in halo collapse.
- **Keywords:** lem-residual-lower, af validated, convex outsourcing, l1 distance, halo collapse

## `AISM-05-RESIDUAL-UPPER`
- **File:** `report/sections/05_residual_upper.tex`
- **Title:** Residual distance bound
- **Summary:** Reproduces the registry contract for lem-residual-upper, an af-validated frame-free convexity fact.
- **Summary:** Summarizes the clean 49-live-node proof tree and records the tracked refactor warning honestly.
- **Keywords:** lem-residual-upper, af validated, residual distance, l1 distance, halo collapse

## `AISM-06-HALO-COLLAPSE`
- **File:** `report/sections/06_halo_collapse.tex`
- **Title:** Halo-robust height collapse
- **Summary:** Reproduces the registry contract for lem-halo-collapse, the af-validated halo-robust bridge.
- **Summary:** Records the run-1 balloon, the factoring into three sub-lemmas, and the clean 20-node run-2 tree.
- **Keywords:** lem-halo-collapse, af validated, height collapse, halo-robust, invisible mass, bridge

## `AISM-07-FACTORIZATION`
- **File:** `report/sections/07_factorization.tex`
- **Title:** Factorization bound
- **Summary:** Reproduces the registry contract for lem-factorization, the af-validated (EX) composition link.
- **Summary:** Summarizes the clean 11-live-node run-1 tree and notes the tightness claim was not elevated.
- **Keywords:** lem-factorization, af validated, factorization, chart scores, (EX) composition

## `AISM-08-ZEROSUM-TRIANGLE`
- **File:** `report/sections/08_zerosum_triangle.tex`
- **Title:** Zero-sum triangle bound
- **Summary:** Reproduces the registry contract for lem-zerosum-triangle, an af-validated negative-part triangle inequality.
- **Summary:** Summarizes the clean 10-node run-1 tree and its role as the first factored dependency of the fan payment lemma.
- **Keywords:** lem-zerosum-triangle, af validated, negative part, zero coordinate sum, triangle inequality

## `AISM-09-WEIGHTED-MIN`
- **File:** `report/sections/09_weighted_min.tex`
- **Title:** Weighted minimum bound
- **Summary:** Reproduces the registry contract for lem-weighted-min, an af-validated averaging selection bound.
- **Summary:** Summarizes the clean 8-node tree and its role as the support-averaging step of the fan payment proof.
- **Keywords:** lem-weighted-min, af validated, weighted average, support averaging, index selection

## `AISM-10-FAN-PAYMENT`
- **File:** `report/sections/10_fan_payment.tex`
- **Title:** Zero-sum fan payment
- **Summary:** Reproduces the registry contract for lem-fan-payment, the af-validated all-mass fan payment inequality.
- **Summary:** Summarizes the factored 15-node run-3 tree after two balloon aborts and its role behind the plateau-2 constant.
- **Keywords:** lem-fan-payment, af validated, fan payment, plateau 2, payment horn

## `AISM-11-NEGPART-SUBADDITIVE`
- **File:** `report/sections/11_negpart_subadditive.tex`
- **Title:** Negative-part subadditivity
- **Summary:** Reproduces the registry contract for lem-negpart-subadditive, an af-validated pointwise subadditivity bound.
- **Summary:** Summarizes the clean 16-node run-1 tree and its role as the pre-factored barycenter step of the D-restricted fan proof.
- **Keywords:** lem-negpart-subadditive, af validated, negative part, subadditivity, barycenter step

## `AISM-12-FAN-PAYMENT-RESTRICTED`
- **File:** `report/sections/12_fan_payment_restricted.tex`
- **Title:** D-restricted zero-sum fan payment
- **Summary:** Reproduces the registry contract for lem-fan-payment-restricted, af-validated with sharp constant two plus root two.
- **Summary:** Summarizes the clean 27-node run-1 tree and records that constant two is exactly refuted for this variant.
- **Keywords:** lem-fan-payment-restricted, af validated, D-restricted, sharp constant, payment horn

## `AISM-14-PIVOT-REMOVING-MOVE`
- **File:** `report/sections/14_pivot_removing_move.tex`
- **Title:** Pivot-removing max-stationarity
- **Summary:** Reproduces the registry contract for lem-pivot-removing-move, the af-validated pivot-removing chart move.
- **Summary:** Summarizes the clean 9-node zero-challenge run-1 tree and its role as the minimality tool of the argmin engine.
- **Keywords:** lem-pivot-removing-move, af validated, pivot removing, max stationarity, argmin, collateral

## `AISM-15-HIDDENNESS-DUAL-WITNESS`
- **File:** `report/sections/15_hiddenness_dual_witness.tex`
- **Title:** The hiddenness dual witness and its always-tight support
- **Summary:** Reproduces lem-hiddenness-dual-witness, the af-validated LP-dual witness attached to a hidden row vertex.
- **Summary:** Reproduces lem-always-tight-dual-support, the af-validated complementary-slackness localisation of that witness.
- **Summary:** Typesets the exposedness LP, its dual, and the complementarity identity that both proofs turn on.
- **Keywords:** lem-hiddenness-dual-witness, lem-always-tight-dual-support, af validated, exposedness LP, LP duality, complementary slackness

## `AISM-16-WITNESS-CONSEQUENCES`
- **File:** `report/sections/16_witness_consequences.tex`
- **Title:** Consequences of the hiddenness witness: depth-Markov, far-row certificate, top-slab companion
- **Summary:** Reproduces lem-hiddenness-depth-markov, the af-validated Markov bound concentrating the witness mass near the top depth.
- **Summary:** Reproduces lem-row-far-dual-certificate and lem-top-slab-companion, the af-validated margin bound and far-row existence statement.
- **Summary:** Typesets the l1 support-functional deficit and the weighted-average arguments the three proofs share.
- **Keywords:** lem-hiddenness-depth-markov, lem-row-far-dual-certificate, lem-top-slab-companion, af validated, support functional, Markov inequality, exposedness margin

## `AISM-17-SLAB-CAPACITY-PRIMITIVES`
- **File:** `report/sections/17_slab_capacity_primitives.tex`
- **Title:** Slab and capacity primitives for harmonic test functions
- **Summary:** Reproduces lem-cs-low-slab-pincer and lem-row-zero-capacity, the af-validated Chebyshev-slab and row-zero capacity bounds.
- **Summary:** Reproduces lem-harmonic-affine-bridge, the af-validated equivalence between P-harmonic vectors and affine functions of the rows.
- **Summary:** Typesets the single row-reproduction identity that all three elementary primitives share.
- **Keywords:** lem-cs-low-slab-pincer, lem-row-zero-capacity, lem-harmonic-affine-bridge, af validated, row reproduction, negative mass, harmonic vector

## `AISM-18-PARAMETRIC-HALO-COLLAPSE`
- **File:** `report/sections/18_parametric_halo_collapse.tex`
- **Title:** Parametric and depth-d halo collapse
- **Summary:** Reproduces lem-parametric-halo-collapse, the af-validated width-parametric generalisation of the halo-collapse bridge.
- **Summary:** Reproduces lem-depth-d-halo-collapse, the af-validated non-top-row version with an explicit deeper-row correction term.
- **Summary:** Typesets the residual-split convexity argument that reduces both bounds to the frame-free residual estimates.
- **Keywords:** lem-parametric-halo-collapse, lem-depth-d-halo-collapse, af validated, halo collapse, residual split, invisible mass, height

## `AISM-19-GENUINE-DISINTEGRATION`
- **File:** `report/sections/19_genuine_disintegration.tex`
- **Title:** Genuine-mass disintegration and top concentration
- **Summary:** Reproduces lem-genuine-disintegration, the af-validated bound splitting halo mass into hidden-vertex mass and a shallow remainder.
- **Summary:** Reproduces lem-top-concentration, the af-validated bound on the positive mass a hidden top vertex places outside the genuine set.
- **Summary:** Typesets the depth-convexity and support-functional deficit arguments driving the g-bootstrap.
- **Keywords:** lem-genuine-disintegration, lem-top-concentration, af validated, genuine mass, g-bootstrap, depth convexity, support functional

## `AISM-20-STARVATION-OBSTRUCTION`
- **File:** `report/sections/20_starvation_obstruction.tex`
- **Title:** The bounded-slab starvation completion obstruction
- **Summary:** Reproduces lem-starvation-completion-obstruction, the af-validated K-free non-existence result for a rank-three starvation configuration.
- **Summary:** Typesets the unit-moment identity and the fiber-budget bound whose contradiction drives the proof.
- **Summary:** Records the paper-proof provenance and the role of the obstruction in closing the exchange-starvation leaf.
- **Keywords:** lem-starvation-completion-obstruction, af validated, starvation, rank three, unit moment, exterior budget, K-free

## `AISM-21-HX-FINANCING-ENGINE`
- **File:** `report/sections/21_hx_financing_engine.tex`
- **Title:** The H-X financing engine: unit moment, sign-union ledger, financing floor
- **Summary:** Reproduces the three af-validated W60/W61 engine lemmas lem-hx-transverse-moment-identity, lem-hx-signed-variation-ledger, and lem-hx-financing-floor.
- **Summary:** Typesets the basis-free unit transverse moment, the two-sign-union budget converter, and their arithmetic assembly into the high-lever financing floor.
- **Summary:** Records the W61 quantifier correction on the floor (all reals A restated to A > 0) and the af provenance of all three results.
- **Keywords:** lem-hx-transverse-moment-identity, lem-hx-signed-variation-ledger, lem-hx-financing-floor, af validated, unit moment, sign union, financing floor, H-X engine

## `AISM-22-HX-STARVATION-COUPLING`
- **File:** `report/sections/22_hx_starvation_coupling.tex`
- **Title:** Robust scalar starvation and forced exterior coupling
- **Summary:** Reproduces the af-validated lem-hx-robust-scalar-starvation, the rank-free slab-free generalization of the starvation obstruction with an explicit universal ceiling.
- **Summary:** Reproduces the af-validated lem-hx-forced-exterior-coupling, the first forced long-range positive-financing lower bound.
- **Summary:** Records the exact T0 calibration, the verifier's tail-cap near-counterexample, and the af provenance of both results.
- **Keywords:** lem-hx-robust-scalar-starvation, lem-hx-forced-exterior-coupling, af validated, starvation, top-tail cap, tableau window, forced coupling, H-X engine

## `AISM-13-STATUS-LEDGER`
- **File:** `report/sections/13_discussion.tex`
- **Title:** Status ledger for non-validated registry results
- **Summary:** Anchors every registry result not already reproduced as an af-validated section.
- **Summary:** Preserves each remaining result's honest status without promoting inherited or numerical claims.
- **Keywords:** status ledger, provenance, proved-mod-audit, conjecture, numerical, open
