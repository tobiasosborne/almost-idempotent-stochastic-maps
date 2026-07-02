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

## `AISM-11-STATUS-LEDGER`
- **File:** `report/sections/11-discussion.tex`
- **Title:** Status ledger for non-validated registry results
- **Summary:** Anchors every registry result not already reproduced as an af-validated section.
- **Summary:** Preserves each remaining result's honest status without promoting inherited or numerical claims.
- **Keywords:** status ledger, provenance, proved-mod-audit, conjecture, numerical, open
