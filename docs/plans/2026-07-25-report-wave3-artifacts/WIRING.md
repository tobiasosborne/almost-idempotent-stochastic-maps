# WIRING — landing instructions for report waves 3 + 3b + 3c

Author-side artifact. Nothing in this directory has been written into the repo. Everything below is
mechanical except the prose repairs in §G, which are content edits and need the usual reviewer.

**Wave 3b (2026-07-25, second author).** The three `af: validated` `lem-hcb4-canonical-*` results that
wave 3 found sitting unwritten under `conj-hcb` were written up and the §I renumbering plan was
executed inside this scratchpad.

**Wave 3c (2026-07-26, third author).** `conj-extcb` was `af`-VALIDATED and banked between wave 3b and
this wave (registry `status: proved`, `af: validated`; T0 is now 70). Three jobs were done:
(1) the EXT parent is now **written up** as a new shard `35_extcb.tex`, with status/outlook renumbered
`35 -> 36`; (2) every "pending"/"seeded"/"proved-mod-audit" reference to `conj-extcb` across the
existing shards was flipped to the recorded `proved` / `af: validated` state, with the forward
references turned into real `\S\ref{sec:extcb}` references; (3) shard `36`'s status inventory was
recounted against the CURRENT generated index (`repo-inputs/argument-INDEX.md`, 70 `proved`/`validated`
rows). **The file names and `SHARD-ID`s below are the current ones.**

Shards produced (verified by a real `pdflatex` build and by the real `check-report-shards.sh` run
against a simulated tree, §H):

| new file | SHARD-ID | registry ids reproduced | lines | wave |
|---|---|---|---|---|
| `report/sections/25_hcb3_offdiagonal_inverse.tex` | `AISM-25-HCB3-OFFDIAGONAL-INVERSE` | `lem-hcb3-offdiagonal-inverse` | 116 | 3 |
| `report/sections/26_hcb4_canonical_gram.tex` | `AISM-26-HCB4-CANONICAL-GRAM` | `lem-hcb4-canonical-gram` | 121 | 3b |
| `report/sections/27_hcb4_canonical_closeness.tex` | `AISM-27-HCB4-CANONICAL-CLOSENESS` | `lem-hcb4-canonical-closeness` | 122 | 3b |
| `report/sections/28_hcb4_canonical_inverse.tex` | `AISM-28-HCB4-CANONICAL-INVERSE` | `lem-hcb4-canonical-inverse` | 122 | 3b (+3c fix) |
| `report/sections/29_hcb.tex` | `AISM-29-HCB` | `conj-hcb` | 130 | 3 (+3c) |
| `report/sections/30_extcb_one_dimensional_corners.tex` | `AISM-30-EXTCB-ONE-DIMENSIONAL-CORNERS` | `lem-extcb-one-dimensional-product`, `lem-extcb-one-dimensional-corner-dimension` | 132 | 3 |
| `report/sections/31_extcb_corner_dimension_additivity.tex` | `AISM-31-EXTCB-CORNER-DIMENSION-ADDITIVITY` | `lem-extcb-corner-dimension-additivity` | 108 | 3 |
| `report/sections/32_extcb1_dimension_selection.tex` | `AISM-32-EXTCB1-DIMENSION-SELECTION` | `lem-extcb1-close-corner-dimension`, `lem-extcb1-cross-corner-dimension` | 167 | 3 (+3c) |
| `report/sections/33_extcb_four_corner_norm.tex` | `AISM-33-EXTCB-FOUR-CORNER-NORM` | `lem-extcb-four-corner-norm` | 119 | 3 |
| `report/sections/34_extcb_four_corner_merge.tex` | `AISM-34-EXTCB-FOUR-CORNER-MERGE` | `lem-extcb-four-corner-merge` | 132 | 3 (+3c) |
| `report/sections/35_extcb.tex` | `AISM-35-EXTCB` | `conj-extcb` | 204 | **3c (new)** |
| `report/sections/36_status_outlook.tex` | `AISM-36-STATUS-OUTLOOK` | (no lemma; revised ledger section) | 149 | 3 (renumbered 3b, 3c) |

**Grouping rationale.** One shard per registry result, except two deliberate pairs.
(i) `30` groups `lem-extcb-one-dimensional-product` with `lem-extcb-one-dimensional-corner-dimension`:
the second is an 8-node corollary of the first and would be a 35-line shard alone, while the pair reads
as one statement about one-dimensional middle indices.
(ii) `32` groups `lem-extcb1-close-corner-dimension` with `lem-extcb1-cross-corner-dimension`: both
live on the same EXT-CB datum, the first exists only to serve the second (it is its sole registry
consumer), and separating them would duplicate the datum set-up twice. The hcb4 trio is deliberately
**not** grouped (9/11/19-node trees, consumed at different places, and 1:1 preserves the hostile
reviewer's diff against `proofs/<id>/export.md`). Everything else is 1:1.

**Placement and size of `35_extcb.tex` (wave 3c decision).** `conj-extcb` goes *after* all seven of its
EXT front-end suppliers and after `conj-hcb`, i.e. last before status/outlook, exactly as `29_hcb.tex`
sits after the H-CB tier it aggregates. Status/outlook therefore renumbers `35 -> 36`; it has stayed
last through every wave (`README.md` already records the earlier `22 -> 25` renumber of the same
section). The shard is **204 lines** — the largest in the report, above the ~200 soft target and well
under the 280 hard guard. It was **not** split, deliberately: the only natural cut is the in-workspace
dimension-free exact-target correction (export nodes 1.2, 1.2.1–1.2.3, 1.2.3.1, 1.2.3.1.1), and that is
*not* a registry result — giving it its own `\section` would either invent a report-only lemma label
with no registry backref (a `check-provenance` reverse-label WARN) or break the 1:1 shard ↔ registry
result correspondence the whole report and the reviewer's export diff rest on. A 4-line overage is the
cheaper cost. The tree was compressed from 46 nodes by narrating the redundant dependency-gate bridges
once (see AUTHOR-NOTES §wave-3c).

---

## A. File placement

```bash
cp <scratch>/25_hcb3_offdiagonal_inverse.tex          report/sections/
cp <scratch>/26_hcb4_canonical_gram.tex               report/sections/
cp <scratch>/27_hcb4_canonical_closeness.tex          report/sections/
cp <scratch>/28_hcb4_canonical_inverse.tex            report/sections/
cp <scratch>/29_hcb.tex                               report/sections/
cp <scratch>/30_extcb_one_dimensional_corners.tex     report/sections/
cp <scratch>/31_extcb_corner_dimension_additivity.tex report/sections/
cp <scratch>/32_extcb1_dimension_selection.tex        report/sections/
cp <scratch>/33_extcb_four_corner_norm.tex            report/sections/
cp <scratch>/34_extcb_four_corner_merge.tex           report/sections/
cp <scratch>/35_extcb.tex                             report/sections/
git rm -f report/sections/25_status_outlook.tex        # replaced by the renumbered revision
cp <scratch>/36_status_outlook.tex                     report/sections/
rm -f report/sections/*.aux                            # stale per-shard aux from earlier builds
```

## B. `report/main.tex` — include list

Replace the current include block tail (`... \include{sections/24_hcb3_diagonal_inverse}` followed by
`\include{sections/25_status_outlook}`) with:

```latex
\include{sections/24_hcb3_diagonal_inverse}
\include{sections/25_hcb3_offdiagonal_inverse}
\include{sections/26_hcb4_canonical_gram}
\include{sections/27_hcb4_canonical_closeness}
\include{sections/28_hcb4_canonical_inverse}
\include{sections/29_hcb}
\include{sections/30_extcb_one_dimensional_corners}
\include{sections/31_extcb_corner_dimension_additivity}
\include{sections/32_extcb1_dimension_selection}
\include{sections/33_extcb_four_corner_norm}
\include{sections/34_extcb_four_corner_merge}
\include{sections/35_extcb}
\include{sections/36_status_outlook}
```

No preamble change is required: every shard uses only macros already defined in `main.tex`
(`\comb \dproj \ecs \nrm \dg \cpr \Co \Cos \Cnr \Cnrs \cunit \colq \colnrm \ipo \ipa \Ha \Han \Amp
\Mat \Matr \ampl \ampel \contractquote \Img \Ker \sgn`) plus stock `amsmath`/`amssymb`. See
AUTHOR-NOTES §macros for the notations written out longhand rather than macro-ised; `35_extcb.tex`
writes $\nrm{\cdot}_{\mathrm{cb}}$, $B(H)$ and $\int U\dg\otimes U\,dU$ longhand too, on purpose, so
that the landing needs no preamble edit.

## C. `report/README.md` — shard-order table

Replace the `| 25 | \`AISM-25-STATUS-OUTLOOK\` | ... |` row with:

```markdown
| 25 | `AISM-25-HCB3-OFFDIAGONAL-INVERSE` | `report/sections/25_hcb3_offdiagonal_inverse.tex` |
| 26 | `AISM-26-HCB4-CANONICAL-GRAM` | `report/sections/26_hcb4_canonical_gram.tex` |
| 27 | `AISM-27-HCB4-CANONICAL-CLOSENESS` | `report/sections/27_hcb4_canonical_closeness.tex` |
| 28 | `AISM-28-HCB4-CANONICAL-INVERSE` | `report/sections/28_hcb4_canonical_inverse.tex` |
| 29 | `AISM-29-HCB` | `report/sections/29_hcb.tex` |
| 30 | `AISM-30-EXTCB-ONE-DIMENSIONAL-CORNERS` | `report/sections/30_extcb_one_dimensional_corners.tex` |
| 31 | `AISM-31-EXTCB-CORNER-DIMENSION-ADDITIVITY` | `report/sections/31_extcb_corner_dimension_additivity.tex` |
| 32 | `AISM-32-EXTCB1-DIMENSION-SELECTION` | `report/sections/32_extcb1_dimension_selection.tex` |
| 33 | `AISM-33-EXTCB-FOUR-CORNER-NORM` | `report/sections/33_extcb_four_corner_norm.tex` |
| 34 | `AISM-34-EXTCB-FOUR-CORNER-MERGE` | `report/sections/34_extcb_four_corner_merge.tex` |
| 35 | `AISM-35-EXTCB` | `report/sections/35_extcb.tex` |
| 36 | `AISM-36-STATUS-OUTLOOK` | `report/sections/36_status_outlook.tex` |
```

Also add an addendum comment above the table, matching the existing house pattern:

```
<!-- ADDENDUM (waves 3 + 3b + 3c): 25 hcb3-offdiagonal-inverse, 26-28 the hcb4 canonical layer,
     29 hcb (H-CB parent), 30-34 the EXT front end, 35 extcb (EXT parent);
     status/outlook renumbered 25 -> 36. -->
```

## D. `report/SHARD_CATALOG.md` — new entries

Delete the existing `` ## `AISM-25-STATUS-OUTLOOK` `` block (it is regenerated below as
`AISM-36-STATUS-OUTLOOK`, at the end where it belongs) and append these twelve blocks after the
`AISM-24-...` block. Summary lines are byte-identical to the shard headers — `check-report-shards.sh`
`grep -F`s each one, so do not reflow them. (These blocks were **generated from the shard headers**,
so they already carry the wave-3b/3c header corrections to `AISM-28` and `AISM-36`.)

```markdown
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

## `AISM-36-STATUS-OUTLOOK`
- **File:** `report/sections/36_status_outlook.tex`
- **Title:** Status and outlook
- **Summary:** Records what this report validates, where the live route now stops, and the quarantined assembly interface.
- **Summary:** Tabulates the validated registry results not reproduced on the live route, with every row traced to the generated argument index.
- **Keywords:** status, outlook, conj-hcb, conj-extcb, registry index, live route, off-route table
```

## E. `report/PROVENANCE.md` — ledger rows

Append to the **Ground-truth source registry** table. Hashes recomputed **2026-07-26 against the live
repo**; `check_source_hashes` hard-errors on tracked files (both `argument/lemmas/*.md` and
`proofs/*/export.md` are tracked), so **recompute again at landing** with
`sha256sum "<path>" | cut -c1-16` if any registry shard or export changes in between. Two rows changed
since the wave-3b snapshot because commit `8d0a5061` edited those shards (see §I).

```markdown
| `ARG-LEM-HCB3-OFFDIAGONAL-INVERSE` | `argument/lemmas/lem-hcb3-offdiagonal-inverse.md` | `ae44e4c30e481156` | Registry shard for `lem-hcb3-offdiagonal-inverse` |
| `AF-LEM-HCB3-OFFDIAGONAL-INVERSE` | `proofs/lem-hcb3-offdiagonal-inverse/export.md` | `8e0654cec4ce118f` | `af` proof export for `lem-hcb3-offdiagonal-inverse` |
| `ARG-LEM-HCB4-CANONICAL-GRAM` | `argument/lemmas/lem-hcb4-canonical-gram.md` | `789fbbaefd0d1fbc` | Registry shard for `lem-hcb4-canonical-gram` |
| `AF-LEM-HCB4-CANONICAL-GRAM` | `proofs/lem-hcb4-canonical-gram/export.md` | `a12f20742b28bdee` | `af` proof export for `lem-hcb4-canonical-gram` |
| `ARG-LEM-HCB4-CANONICAL-CLOSENESS` | `argument/lemmas/lem-hcb4-canonical-closeness.md` | `a3d2e9ddded6f79a` | Registry shard for `lem-hcb4-canonical-closeness` |
| `AF-LEM-HCB4-CANONICAL-CLOSENESS` | `proofs/lem-hcb4-canonical-closeness/export.md` | `336ce36ecd5bbfb5` | `af` proof export for `lem-hcb4-canonical-closeness` |
| `ARG-LEM-HCB4-CANONICAL-INVERSE` | `argument/lemmas/lem-hcb4-canonical-inverse.md` | `0e61a08b0d6157ff` | Registry shard for `lem-hcb4-canonical-inverse` |
| `AF-LEM-HCB4-CANONICAL-INVERSE` | `proofs/lem-hcb4-canonical-inverse/export.md` | `0a3da88fbf702f9a` | `af` proof export for `lem-hcb4-canonical-inverse` |
| `ARG-CONJ-HCB` | `argument/lemmas/conj-hcb.md` | `de52bbad964e45ef` | Registry shard for `conj-hcb` |
| `AF-CONJ-HCB` | `proofs/conj-hcb/export.md` | `8818e7d0952d7343` | `af` proof export for `conj-hcb` |
| `ARG-LEM-EXTCB-ONE-DIMENSIONAL-PRODUCT` | `argument/lemmas/lem-extcb-one-dimensional-product.md` | `ce1cfccd673787c4` | Registry shard for `lem-extcb-one-dimensional-product` |
| `AF-LEM-EXTCB-ONE-DIMENSIONAL-PRODUCT` | `proofs/lem-extcb-one-dimensional-product/export.md` | `e154fae299637b1d` | `af` proof export for `lem-extcb-one-dimensional-product` |
| `ARG-LEM-EXTCB-ONE-DIMENSIONAL-CORNER-DIMENSION` | `argument/lemmas/lem-extcb-one-dimensional-corner-dimension.md` | `5764c43280c08261` | Registry shard for `lem-extcb-one-dimensional-corner-dimension` |
| `AF-LEM-EXTCB-ONE-DIMENSIONAL-CORNER-DIMENSION` | `proofs/lem-extcb-one-dimensional-corner-dimension/export.md` | `0e4440d7635b5943` | `af` proof export for `lem-extcb-one-dimensional-corner-dimension` |
| `ARG-LEM-EXTCB-CORNER-DIMENSION-ADDITIVITY` | `argument/lemmas/lem-extcb-corner-dimension-additivity.md` | `517d59f6fd2b3f05` | Registry shard for `lem-extcb-corner-dimension-additivity` |
| `AF-LEM-EXTCB-CORNER-DIMENSION-ADDITIVITY` | `proofs/lem-extcb-corner-dimension-additivity/export.md` | `83aaabfed5dfb04b` | `af` proof export for `lem-extcb-corner-dimension-additivity` |
| `ARG-LEM-EXTCB1-CLOSE-CORNER-DIMENSION` | `argument/lemmas/lem-extcb1-close-corner-dimension.md` | `a6c30bde11080b1c` | Registry shard for `lem-extcb1-close-corner-dimension` |
| `AF-LEM-EXTCB1-CLOSE-CORNER-DIMENSION` | `proofs/lem-extcb1-close-corner-dimension/export.md` | `3a26c1b3f960edc8` | `af` proof export for `lem-extcb1-close-corner-dimension` |
| `ARG-LEM-EXTCB1-CROSS-CORNER-DIMENSION` | `argument/lemmas/lem-extcb1-cross-corner-dimension.md` | `f9a6aa8b2fbb4791` | Registry shard for `lem-extcb1-cross-corner-dimension` |
| `AF-LEM-EXTCB1-CROSS-CORNER-DIMENSION` | `proofs/lem-extcb1-cross-corner-dimension/export.md` | `59ce65ddb29e6f75` | `af` proof export for `lem-extcb1-cross-corner-dimension` |
| `ARG-LEM-EXTCB-FOUR-CORNER-NORM` | `argument/lemmas/lem-extcb-four-corner-norm.md` | `b7c4ab7ce44519b0` | Registry shard for `lem-extcb-four-corner-norm` |
| `AF-LEM-EXTCB-FOUR-CORNER-NORM` | `proofs/lem-extcb-four-corner-norm/export.md` | `670ead004d58b5bf` | `af` proof export for `lem-extcb-four-corner-norm` |
| `ARG-LEM-EXTCB-FOUR-CORNER-MERGE` | `argument/lemmas/lem-extcb-four-corner-merge.md` | `3a2724066e5735e0` | Registry shard for `lem-extcb-four-corner-merge` |
| `AF-LEM-EXTCB-FOUR-CORNER-MERGE` | `proofs/lem-extcb-four-corner-merge/export.md` | `35c643ae943968aa` | `af` proof export for `lem-extcb-four-corner-merge` |
| `ARG-CONJ-EXTCB` | `argument/lemmas/conj-extcb.md` | `a8529323f4410a6a` | Registry shard for `conj-extcb` |
| `AF-CONJ-EXTCB` | `proofs/conj-extcb/export.md` | `00494481438b5a79` | `af` proof export for `conj-extcb` |
```

Append to the **per-claim ledger**:

```markdown
| lem:hcb3-offdiagonal-inverse | ARG-LEM-HCB3-OFFDIAGONAL-INVERSE AF-LEM-HCB3-OFFDIAGONAL-INVERSE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb3-offdiagonal-inverse`. |
| lem:hcb4-canonical-gram | ARG-LEM-HCB4-CANONICAL-GRAM AF-LEM-HCB4-CANONICAL-GRAM | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb4-canonical-gram`. |
| lem:hcb4-canonical-closeness | ARG-LEM-HCB4-CANONICAL-CLOSENESS AF-LEM-HCB4-CANONICAL-CLOSENESS | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb4-canonical-closeness`. |
| lem:hcb4-canonical-inverse | ARG-LEM-HCB4-CANONICAL-INVERSE AF-LEM-HCB4-CANONICAL-INVERSE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb4-canonical-inverse`. |
| conj:hcb | ARG-CONJ-HCB AF-CONJ-HCB | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/conj-hcb`; conditional inverse clauses reproduced as amended. |
| lem:extcb-one-dimensional-product | ARG-LEM-EXTCB-ONE-DIMENSIONAL-PRODUCT AF-LEM-EXTCB-ONE-DIMENSIONAL-PRODUCT | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-extcb-one-dimensional-product`. |
| lem:extcb-one-dimensional-corner-dimension | ARG-LEM-EXTCB-ONE-DIMENSIONAL-CORNER-DIMENSION AF-LEM-EXTCB-ONE-DIMENSIONAL-CORNER-DIMENSION | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-extcb-one-dimensional-corner-dimension`. |
| lem:extcb-corner-dimension-additivity | ARG-LEM-EXTCB-CORNER-DIMENSION-ADDITIVITY AF-LEM-EXTCB-CORNER-DIMENSION-ADDITIVITY | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-extcb-corner-dimension-additivity`. |
| lem:extcb1-close-corner-dimension | ARG-LEM-EXTCB1-CLOSE-CORNER-DIMENSION AF-LEM-EXTCB1-CLOSE-CORNER-DIMENSION | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-extcb1-close-corner-dimension`. |
| lem:extcb1-cross-corner-dimension | ARG-LEM-EXTCB1-CROSS-CORNER-DIMENSION AF-LEM-EXTCB1-CROSS-CORNER-DIMENSION | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-extcb1-cross-corner-dimension`. |
| lem:extcb-four-corner-norm | ARG-LEM-EXTCB-FOUR-CORNER-NORM AF-LEM-EXTCB-FOUR-CORNER-NORM | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-extcb-four-corner-norm`. |
| lem:extcb-four-corner-merge | ARG-LEM-EXTCB-FOUR-CORNER-MERGE AF-LEM-EXTCB-FOUR-CORNER-MERGE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-extcb-four-corner-merge`; smallness hypothesis reproduced in its amended (total-defect) form. |
| conj:extcb | ARG-CONJ-EXTCB AF-CONJ-EXTCB | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/conj-extcb` (40 validated + 6 archived); the recorded correction is proof-level, not a contract amendment. |
```

Also refresh the "Current report surface" note: the shards now reproduce **thirty-seven** af-validated
registry results (the wave-2 note says twenty-six/twenty-nine and is stale).

**Label discipline (do not change).** `check-provenance.py:labels_of` anchors a registry id by the
first-hyphen-to-colon transform, so the report labels must be exactly
`lem:hcb3-offdiagonal-inverse`, `lem:hcb4-canonical-gram`, `lem:hcb4-canonical-closeness`,
`lem:hcb4-canonical-inverse`, `conj:hcb`, `lem:extcb-...`, and — new in wave 3c — **`conj:extcb`**.
Labelling the EXT parent `lem:extcb` would leave `conj-extcb` unanchored and, once removed from
`UNWIRED.md`, would hard-fail `check-all`. `35_extcb.tex` uses `\label{conj:extcb}`.

## F. `report/UNWIRED.md` — removals

Delete exactly these thirteen lines from the fenced block (line numbers as of the 2026-07-26 snapshot):

```
26:  conj-extcb          <- NEW in wave 3c: now written up in 35_extcb.tex
27:  conj-hcb
101: lem-extcb-four-corner-norm
229: lem-hcb3-offdiagonal-inverse
230: lem-hcb4-canonical-gram
231: lem-hcb4-canonical-closeness
232: lem-hcb4-canonical-inverse
233: lem-extcb-one-dimensional-product
234: lem-extcb-one-dimensional-corner-dimension
235: lem-extcb-corner-dimension-additivity
236: lem-extcb-four-corner-merge
237: lem-extcb1-close-corner-dimension
238: lem-extcb1-cross-corner-dimension
```

**Keep** `lem-collateral-import` (37), `lem-cross-pivot-cancellation` (38) and `lem-import-reduction`
(56): they are `af: validated` signed-geometry results off the live route, reproduced by no wave.
They appear in §36's off-route table like the other thirty. The arithmetic now closes exactly:
**37 reproduced + 33 off-route table rows = 70** `proved`/`validated` index rows.

## G. Prose repairs forced by these waves (content edits — need the reviewer)

### G1. Repairs to shards already in the repo

**Nine existing shards assert statuses that these waves make false** (found with
`grep -rn "conj-hcb\|conj-extcb\|offdiagonal\|hcb4\|af: none\|not-yet-validated" report/sections/`).
Rule 9 makes these part of the same landing, not follow-ups. Each is a one- or two-sentence repair; the
mathematics is untouched. Wave 3c revised the two `00_overview.tex` rows, which wave 3b had written
while `conj-extcb` was still open.

| file | line(s) | stale text | repair |
|---|---|---|---|
| `00_overview.tex` | 108-110 | "The H-CB tier feeds the parent contract \texttt{conj-hcb}, which is \textbf{open} (\texttt{proved-mod-audit}, \texttt{af: none}); beyond it lie the EXT tier and a quarantined assembly interface." | "The H-CB tier feeds the parent contract \texttt{conj-hcb} (\S\ref{sec:hcb}), and that in turn feeds the EXT parent \texttt{conj-extcb} (\S\ref{sec:extcb}); both are \texttt{proved} with \texttt{af: validated}. What is open beyond them is the assembly, whose registry carrier \texttt{lem-thmainext-conditional} is \texttt{proved-mod-audit} with \texttt{af: none}, together with the quarantined assembly interface." |
| `00_overview.tex` | 68-75 | item 4 of "What this report contains" ends the H-CB range at `\ref{sec:hcb3-diagonal-inverse}` and lists four blocks | extend the range to `\ref{sec:hcb4-canonical-inverse}` (the H-CB tier now runs through its canonical layer); add a fifth item — the H-CB parent contract (`\S\ref{sec:hcb}`) and the whole EXT tier (`\S\S\ref{sec:extcb-one-dimensional-corners}--\ref{sec:extcb}`): corner arithmetic through a one-dimensional index, the dimension selection $(r,1)$ of an EXT-CB datum, the four-corner merge, and the EXT parent that adds one dimension to a level-one datum |
| `10_hcb2_amplified_adjointness.tex` | 99-100 | "a declared dependency of the not-yet-validated \texttt{lem-hcb3-offdiagonal-inverse} and \texttt{lem-hcb4-canonical-closeness}" | "a declared dependency of \texttt{lem-hcb3-offdiagonal-inverse} (\S\ref{sec:hcb3-offdiagonal-inverse}) and \texttt{lem-hcb4-canonical-closeness} (\S\ref{sec:hcb4-canonical-closeness}), both now \texttt{af: validated}" |
| `15_hcb_column_hilbert_squared.tex` | 106-107 | "and the not-yet-validated \texttt{lem-hcb4-canonical-closeness}" | "and \texttt{lem-hcb4-canonical-closeness} (\S\ref{sec:hcb4-canonical-closeness}), now \texttt{af: validated}, which consumes it at $n=1$ to normalise the compressed unit" |
| `18_hcb1_column_action.tex` | 107-108 | "a declared dependency of the not-yet-validated \texttt{lem-hcb4-canonical-closeness}" | "a declared dependency of \texttt{lem-hcb4-canonical-closeness} (\S\ref{sec:hcb4-canonical-closeness}), now \texttt{af: validated}" |
| `19_hcb2_product_defect.tex` | 100-101 | "a declared dependency of the not-yet-validated \texttt{lem-hcb3-offdiagonal-inverse}" | "a declared dependency of \texttt{lem-hcb3-offdiagonal-inverse} (\S\ref{sec:hcb3-offdiagonal-inverse}), now \texttt{af: validated}" |
| `20_hcb3_diagonal_unit.tex` | 89-93 | "it has no validated registry consumers of its own. \texttt{conj-hcb} is \texttt{proved-mod-audit} and \texttt{af: none}: it is not rigorous here, and neither it nor this lemma bears on the status of \texttt{op-classical}" | "its registry consumer is the parent contract itself (\S\ref{sec:hcb}), now \texttt{proved} with \texttt{af: validated}; neither it nor this lemma bears on the status of \texttt{op-classical}" |
| `21_hcb3_diagonal_upper_norm.tex` | 112-115 | "The off-diagonal inverse and the canonical tier beyond them are \texttt{af: none}, and \texttt{conj-hcb} itself is \texttt{proved-mod-audit}, i.e. open at this repository's rigour ladder" | "The off-diagonal inverse (\S\ref{sec:hcb3-offdiagonal-inverse}), the canonical tier (\S\S\ref{sec:hcb4-canonical-gram}--\ref{sec:hcb4-canonical-inverse}) and \texttt{conj-hcb} itself (\S\ref{sec:hcb}) are now all \texttt{af: validated}; the conditional hypotheses named above are supplied only inside \S\ref{sec:extcb}, and nowhere else here" |
| `23_hcb3_diagonal_lower_modulus.tex` | 137-139 | "and to the not-yet-validated \texttt{lem-hcb3-offdiagonal-inverse}. The parent \texttt{conj-hcb} remains \texttt{proved-mod-audit} with \texttt{af: none}" | "and to \texttt{lem-hcb3-offdiagonal-inverse} (\S\ref{sec:hcb3-offdiagonal-inverse}), which consumes it as its diagonal anchor. The parent \texttt{conj-hcb} (\S\ref{sec:hcb}) is now \texttt{proved} with \texttt{af: validated}" |
| `24_hcb3_diagonal_inverse.tex` | 107-109 | "The matching off-diagonal statement \texttt{lem-hcb3-offdiagonal-inverse} is not validated, the hcb4 canonical tier is \texttt{af: none}, and the parent \texttt{conj-hcb} remains \texttt{proved-mod-audit}." | "The matching off-diagonal statement \texttt{lem-hcb3-offdiagonal-inverse} (\S\ref{sec:hcb3-offdiagonal-inverse}), the hcb4 canonical tier (\S\S\ref{sec:hcb4-canonical-gram}--\ref{sec:hcb4-canonical-inverse}) and the parent \texttt{conj-hcb} (\S\ref{sec:hcb}) are now all \texttt{proved} with \texttt{af: validated}." |

Line numbers are as of the 2026-07-26 snapshot. None of these repairs promotes anything: each replaces
a statement of the form "X is not validated" with the recorded fact that X now is, and every
conditional hypothesis stays flagged.

### G2. Repairs wave 3b made inside the scratchpad (already applied — listed for the reviewer)

| file (new name) | was | now |
|---|---|---|
| `29_hcb.tex` | "…and in the canonical tier, so the parent's only work is…" | adds the target `(\S\S\ref{sec:hcb4-canonical-gram}--\ref{sec:hcb4-canonical-inverse})` |
| `29_hcb.tex` | "All sixteen are `proved` with `af: validated`; the canonical tier is reproduced in the registry but not yet in this document." | "All sixteen are `proved` with `af: validated`, and all sixteen are now reproduced in this document." |
| `36_status_outlook.tex` | H-CB tier list ends at `lem-hcb3-offdiagonal-inverse` | inserts the canonical layer — gram, closeness, inverse — before the parent |
| `36_status_outlook.tex` | "…together with three live-route results whose prose write-ups are queued rather than absent: the canonical tier …" | replaced by the scoped supplied-registry statement (see the wave-3 verdict F4/G2 adjudication) |

`25_hcb3_offdiagonal_inverse.tex` needed **no** repair.

### G3. Repairs wave 3c made inside the scratchpad (already applied — listed for the reviewer)

`conj-extcb`'s validation makes four sentences in the wave-3/3b shards false, and one sentence in
`28_hcb4_canonical_inverse.tex` was overtaken by repo commit `8d0a5061`. All are already applied here;
**nothing further is needed at landing**.

| file | was | now |
|---|---|---|
| `29_hcb.tex` | "Downstream, `conj-hcb` is the principal input to `conj-extcb`, which remains `proved-mod-audit` with `af: seeded` — **open** at this document's rigour bar, and referred to below only as a pending consumer, never as a theorem." | "Downstream, `conj-hcb` is the principal input to `conj-extcb` (`\S\ref{sec:extcb}`), itself `proved` with `af: validated` and reproduced below; the conditional clauses above are consumed there, after their level-one hypotheses have been established." |
| `32_extcb1_dimension_selection.tex` | "Its consumer is `conj-extcb`, which is `proved-mod-audit` with `af: seeded` — **open** at this document's rigour bar." | "Its consumer is `conj-extcb` (`\S\ref{sec:extcb}`), now `proved` with `af: validated`; the close-corner lemma is there because a hostile verdict on that parent demanded it." |
| `34_extcb_four_corner_merge.tex` | "Its consumer is `conj-extcb`, which is `proved-mod-audit` with `af: seeded` — a hostile-verified paper proof, one rung below rigorous here, and **not** reproduced as a theorem in this document." | "Its consumer is `conj-extcb` (`\S\ref{sec:extcb}`), now `proved` with `af: validated`: this merge is the last step of that proof." |
| `36_status_outlook.tex` | reproduced inventory "thirty-six" / index total "69" / complement "33 = 69 − 36"; "The immediate queue is the EXT parent `conj-extcb` … its elevation is in progress"; the closing "the parent of the next tier is in elevation" | inventory **thirty-seven** (adds `conj-extcb` with a `\S\ref{sec:extcb}` pointer) / index total **70** / complement **33 = 70 − 37** (the same 33 rows — `conj-extcb` was never in the table); "With `\S\ref{sec:hcb}` the H-CB tier is closed, and with `\S\ref{sec:extcb}` so is the EXT tier"; the open item is now named as `lem-thmainext-conditional` (`proved-mod-audit`, `af: none`) with a status-derivation comment; closing line "the base, the middle and both tier parents … are rigorous here, and the assembly above them is quarantined" |
| `36_status_outlook.tex` | qualifications paragraph: the conditional inverse/lower-modulus clauses have "hypotheses that nothing in this document establishes for any particular datum" | now false — `\S\ref{sec:extcb}` establishes them for the EXT-CB datum. Rewritten to say exactly that, and that nothing else here supplies them for any datum. |
| `36_status_outlook.tex` | SHARD-SUMMARY 1 "what remains on the live H-CB and EXT queue" | "where the live route now stops" (catalog block in §D regenerated to match) |
| `28_hcb4_canonical_inverse.tex` | "Two definitions the validated tree consumes essentially … are provisioned in the workspace but are **not listed** on the registry shard's `defs` line, which records only …" | overtaken by repo commit `8d0a5061`: the `defs:` line now lists all five. Rewritten to record the five and to state that the last two are consumed essentially in the validated closed-corner completeness branch (per the W3C verdict F1 correction; no challenge-history metadata). **This is out of wave 3c's stated scope but was a demonstrably false statement about the current repo; flagged here for the reviewer.** |

The count derivation comments the wave-3 corrections pass introduced are **kept**, with their
derivations updated (`37`, `70`, `33 = 70 − 37`), plus one new status-derivation comment for
`lem-thmainext-conditional`. Challenge-history metadata briefly reintroduced by the first G3 rewrite of shard 28 was removed per the W3C verdict (F1); none remains.

## H. Gates

```bash
bash scripts/check-report-shards.sh    # ids/prefixes/README/CATALOG/size + no orphan shards
python3 scripts/check-provenance.py --check
cd report && make                      # latexmk -pdf; must be warning-free
sh scripts/check-all.sh                # the single gate
```

Author-side evidence (all run in the scratchpad or on a throwaway copy; the repo was never written to):

1. **Full build.** The 25 repo shards `00-24` plus all 12 shards of this directory were compiled twice
   with `pdflatex` against the **real** `report/main.tex` preamble and the §B include list — 37
   includes, exit 0, **77 pages, 0 LaTeX warnings, 0 undefined references, no rerun requested**.
   (Overfull-hbox density is unchanged from the repo baseline: the `\contractquote` blocks overflow by
   design, worst 188.6 pt here vs 223.1 pt in the current repo build.)
2. **Contract byte-match.** A script extracted the balanced-brace argument of every `\contractquote`
   in this directory and compared it against the `contract:` line of every LIVE
   `argument/lemmas/*.md`: **13/13 quotes are byte-identical to exactly one registry contract**
   (`25`→`lem-hcb3-offdiagonal-inverse`, `26`/`27`/`28`→the hcb4 trio, `29`→`conj-hcb`, `30`→two ids,
   `31`, `32`→two ids, `33`, `34`, **`35`→`conj-extcb`**; `36` has none, as expected).
3. **Shard gate simulated.** The **real** `scripts/check-report-shards.sh` was run unmodified against a
   simulated `report/` tree (this directory's shards + the §C README table + the §D catalog blocks):
   `37 shards included, labeled, cataloged, all <= 280 lines`, exit 0. Red→green was confirmed three
   times — a wrong `SHARD-ID` prefix on `35`, a deleted `SHARD-SUMMARY` on `36`, and a padded 294-line
   `35` each made it exit 1 with the expected message, and restoring returned it to exit 0.
4. **Provenance gate simulated (new in wave 3c).** A throwaway copy of `argument/`, `definitions/`,
   `scripts/`, `report/` and every tracked `proofs/*/export.md` was landed with §A–§F applied, and the
   **real** `scripts/check-provenance.py --check` was run on it: **0 errors** — `forward labels`,
   `claim labels`, `claim sources`, `hash freshness`, `status drift`, `reverse labels`, `coverage` and
   `parse integrity` all `[OK]`. In particular `coverage` is clean only *because* the §E per-claim rows
   are applied, and `conj:extcb` resolves as the anchor for `conj-extcb` once its `UNWIRED.md` line is
   deleted. The remaining warnings are the pre-existing whitelisted-unanchored ones.
5. **Status arithmetic.** A script re-derived §36's three counts from `repo-inputs/argument-INDEX.md`:
   70 rows with `proved`/`validated`; 37 ids listed in the reproduced inventory, every one of them a
   `proved`/`validated` index row; the off-route table is exactly the 33-row index-ordered complement,
   with no missing, extra or duplicated id, and `37 + 33 = 70`.

That exercises M (mechanical) and I (idempotent) for the LaTeX, shard-metadata and report↔registry
wiring layers, plus C (cross-reference) for the contract quotes. D and R remain for the landing session
and the hostile review; the author is not the reviewer.

## I. Caveats to carry into the landing commit

- **Hashes.** The §E SHA256-16 values are as of 2026-07-26 and were verified by an actual
  `check-provenance --check` run (hash freshness `[OK]`). Recompute if anything moves before the commit.
- **`conj-extcb` is written up, not promoted.** It was already `proved`/`af: validated` in the registry
  before this wave; `35_extcb.tex` is a write-up of the banked tree, and every status word in it is a
  mechanical reflection of the registry front matter and the export ledger, not a judgment.
- **The `conj-extcb` registry BODY is stale.** `argument/lemmas/conj-extcb.md` front matter says
  `status: proved` / `af: validated`, but its body still opens "…hence `proved-mod-audit`; not
  `af`-validated and not L0-rigorous." The shard follows the front matter and the export (which agree
  with `argument/INDEX.md`). **Registry-hygiene fix for the landing session**; it does not affect the
  report text. The body's *Verifier correction* paragraph is still current and is what
  `35_extcb.tex`'s "Correction of record" reproduces.
- **Two earlier hygiene caveats are CLOSED.** Repo commit `8d0a5061` ("registry hygiene: two
  review-caught fixes on af-validated shards") added `def-compressed-corner` and
  `def-extended-epsilon-cstar-algebra` to `lem-hcb4-canonical-inverse`'s `defs:` line and removed the
  "UNPROVED here pending its own af pass" tail from `lem-extcb-four-corner-norm`'s `provenance:`. Both
  changed those files' hashes (§E) and one of them made a sentence in `28_hcb4_canonical_inverse.tex`
  false (§G3).
- **`35_extcb.tex` is 204 lines**, above the ~200 soft target, under the 280 guard. Rationale in the
  placement note above; the alternative (splitting the correction lemma into its own `\section`) was
  rejected on 1:1-correspondence grounds.
- **The `conj-extcb` export has 6 archived nodes.** They are dependency-gated duplicates superseded by
  siblings; the shard says so and narrates none of them as mathematics.
