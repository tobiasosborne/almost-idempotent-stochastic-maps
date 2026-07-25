# PROVENANCE — report audit ledger

**Policy.** Every Definition and Theorem reproduced in the report (`sections/*.tex`) must have an
entry in the per-claim ledger. An entry records: (1) the report label; (2) the ground-truth source
(a source-registry key with path + SHA256-16); (3) the source/internal-proof locus the
statement is matched to; (4) any harmonisation applied. "Provenanced" = a faithful
transcription/derivation of registered source material, or an internal project statement tied to a
hashed proof/consensus file. Results original to this project are marked `ORIGINAL`.

Verify a hash with: `sha256sum "<path>" | cut -c1-16`.

> **Current report surface.** The section shards reproduce twenty-six of the twenty-nine `af`-validated
> registry results (the paper-track T0 spine) and anchor every remaining registry result in the status
> ledger. Non-rigorous registry statuses are copied honestly; the ledger rows below are anchors, not
> promotions.

> **Current report surface (2026-07-25 rescope).** The section shards reproduce the af-validated
> lemmas of the live Route F chain (bridge, PRH, COMP tier, H-CB tier). Results off the live route
> keep their registry records and statuses; they are whitelisted in `UNWIRED.md`, not reproduced here.

<!-- PROVENANCE.md rows for the fresh report (21 af-validated lemmas).
     Two blocks: (A) ground-truth source-registry rows, (B) per-claim ledger rows.
     Row formats copied from report/PROVENANCE.md. SHA256-16 computed
     2026-07-25; verify with: sha256sum "<path>" | cut -c1-16 -->

## Ground-truth source registry

| Key | Path | SHA256 (16) | What it is |
|-----|------|-------------|------------|
| `ARG-LEM-CLASSICAL-EQUIV` | `argument/lemmas/lem-classical-equiv.md` | `b9e615e904722f43` | Registry shard for `lem-classical-equiv` |
| `AF-LEM-CLASSICAL-EQUIV` | `proofs/lem-classical-equiv/export.md` | `35b46507291c6cb0` | `af` proof export for `lem-classical-equiv` |
| `ARG-LEM-PRH` | `argument/lemmas/lem-prh.md` | `eb601e5d7a251273` | Registry shard for `lem-prh` |
| `AF-LEM-PRH` | `proofs/lem-prh/export.md` | `884892b1bbdd26cc` | `af` proof export for `lem-prh` |
| `ARG-LEM-COMPCB-AMPLIFICATION-NATURALITY` | `argument/lemmas/lem-compcb-amplification-naturality.md` | `47736086b0a61108` | Registry shard for `lem-compcb-amplification-naturality` |
| `AF-LEM-COMPCB-AMPLIFICATION-NATURALITY` | `proofs/lem-compcb-amplification-naturality/export.md` | `79cb34f616111726` | `af` proof export for `lem-compcb-amplification-naturality` |
| `ARG-LEM-COMPCB-AMPLIFIED-COMPRESSION` | `argument/lemmas/lem-compcb-amplified-compression.md` | `1d94d5f84a4db275` | Registry shard for `lem-compcb-amplified-compression` |
| `AF-LEM-COMPCB-AMPLIFIED-COMPRESSION` | `proofs/lem-compcb-amplified-compression/export.md` | `8f46c0b3816499e3` | `af` proof export for `lem-compcb-amplified-compression` |
| `ARG-LEM-COMPCB-AMPLIFIED-COMPRESSION-IDENTITIES` | `argument/lemmas/lem-compcb-amplified-compression-identities.md` | `ebad8b76d7193d86` | Registry shard for `lem-compcb-amplified-compression-identities` |
| `AF-LEM-COMPCB-AMPLIFIED-COMPRESSION-IDENTITIES` | `proofs/lem-compcb-amplified-compression-identities/export.md` | `2c2b75330b4a62c5` | `af` proof export for `lem-compcb-amplified-compression-identities` |
| `ARG-LEM-COMPCB-ENTRYWISE-COMPRESSION-NATURALITY` | `argument/lemmas/lem-compcb-entrywise-compression-naturality.md` | `752e424e4ae37830` | Registry shard for `lem-compcb-entrywise-compression-naturality` |
| `AF-LEM-COMPCB-ENTRYWISE-COMPRESSION-NATURALITY` | `proofs/lem-compcb-entrywise-compression-naturality/export.md` | `d71c997e217170fd` | `af` proof export for `lem-compcb-entrywise-compression-naturality` |
| `ARG-LEM-COMPCB-RECTANGULAR-PRODUCT` | `argument/lemmas/lem-compcb-rectangular-product.md` | `37a0237e07ba7f23` | Registry shard for `lem-compcb-rectangular-product` |
| `AF-LEM-COMPCB-RECTANGULAR-PRODUCT` | `proofs/lem-compcb-rectangular-product/export.md` | `d872eb78fc625cdd` | `af` proof export for `lem-compcb-rectangular-product` |
| `ARG-LEM-COMPCB-AMPLIFIED-ALMOST-CONTAINMENT` | `argument/lemmas/lem-compcb-amplified-almost-containment.md` | `b5ce34855a8fcffa` | Registry shard for `lem-compcb-amplified-almost-containment` |
| `AF-LEM-COMPCB-AMPLIFIED-ALMOST-CONTAINMENT` | `proofs/lem-compcb-amplified-almost-containment/export.md` | `af4a250b8562a8c6` | `af` proof export for `lem-compcb-amplified-almost-containment` |
| `ARG-LEM-COMPCB-COMPRESSED-UNIT-NORM` | `argument/lemmas/lem-compcb-compressed-unit-norm.md` | `d960c40240a278f8` | Registry shard for `lem-compcb-compressed-unit-norm` |
| `AF-LEM-COMPCB-COMPRESSED-UNIT-NORM` | `proofs/lem-compcb-compressed-unit-norm/export.md` | `7f66addd94ee3360` | `af` proof export for `lem-compcb-compressed-unit-norm` |
| `ARG-LEM-HCB2-AMPLIFIED-ADJOINTNESS` | `argument/lemmas/lem-hcb2-amplified-adjointness.md` | `3385d205f630ea76` | Registry shard for `lem-hcb2-amplified-adjointness` |
| `AF-LEM-HCB2-AMPLIFIED-ADJOINTNESS` | `proofs/lem-hcb2-amplified-adjointness/export.md` | `b33bcb729f46baa0` | `af` proof export for `lem-hcb2-amplified-adjointness` |
| `ARG-LEM-COMPCB-COMPRESSED-UNIT-ACTION` | `argument/lemmas/lem-compcb-compressed-unit-action.md` | `e997fdb53fe01b87` | Registry shard for `lem-compcb-compressed-unit-action` |
| `AF-LEM-COMPCB-COMPRESSED-UNIT-ACTION` | `proofs/lem-compcb-compressed-unit-action/export.md` | `f23fbe2fc5941cd9` | `af` proof export for `lem-compcb-compressed-unit-action` |
| `ARG-LEM-COMPCB-ROW-COLUMN-PRODUCT` | `argument/lemmas/lem-compcb-row-column-product.md` | `c53ad9be702469ca` | Registry shard for `lem-compcb-row-column-product` |
| `AF-LEM-COMPCB-ROW-COLUMN-PRODUCT` | `proofs/lem-compcb-row-column-product/export.md` | `19f19cfe2cffc458` | `af` proof export for `lem-compcb-row-column-product` |
| `ARG-LEM-HCB0-COMPRESSED-ASSOCIATOR` | `argument/lemmas/lem-hcb0-compressed-associator.md` | `3ce16393dfd1caea` | Registry shard for `lem-hcb0-compressed-associator` |
| `AF-LEM-HCB0-COMPRESSED-ASSOCIATOR` | `proofs/lem-hcb0-compressed-associator/export.md` | `ccf4d86b642db648` | `af` proof export for `lem-hcb0-compressed-associator` |
| `ARG-LEM-COMPCB-CORNER-ALGEBRA` | `argument/lemmas/lem-compcb-corner-algebra.md` | `90f855050dd789d6` | Registry shard for `lem-compcb-corner-algebra` |
| `AF-LEM-COMPCB-CORNER-ALGEBRA` | `proofs/lem-compcb-corner-algebra/export.md` | `d6260f028148f47a` | `af` proof export for `lem-compcb-corner-algebra` |
| `ARG-LEM-HCB-COLUMN-HILBERT-SQUARED` | `argument/lemmas/lem-hcb-column-hilbert-squared.md` | `4771c7efd751805a` | Registry shard for `lem-hcb-column-hilbert-squared` |
| `AF-LEM-HCB-COLUMN-HILBERT-SQUARED` | `proofs/lem-hcb-column-hilbert-squared/export.md` | `cb17b123df8cd31b` | `af` proof export for `lem-hcb-column-hilbert-squared` |
| `ARG-LEM-COMPCB-SINGLE-COMPRESSION-TRANSFER` | `argument/lemmas/lem-compcb-single-compression-transfer.md` | `d4748e06ec3ee630` | Registry shard for `lem-compcb-single-compression-transfer` |
| `AF-LEM-COMPCB-SINGLE-COMPRESSION-TRANSFER` | `proofs/lem-compcb-single-compression-transfer/export.md` | `83ffbac62450f69f` | `af` proof export for `lem-compcb-single-compression-transfer` |
| `ARG-LEM-HCB1-VARIATIONAL-IDENTITY` | `argument/lemmas/lem-hcb1-variational-identity.md` | `99631ed35861cd77` | Registry shard for `lem-hcb1-variational-identity` |
| `AF-LEM-HCB1-VARIATIONAL-IDENTITY` | `proofs/lem-hcb1-variational-identity/export.md` | `39b33095ed4a6da7` | `af` proof export for `lem-hcb1-variational-identity` |
| `ARG-LEM-HCB1-COLUMN-ACTION` | `argument/lemmas/lem-hcb1-column-action.md` | `51cc06d87845d169` | Registry shard for `lem-hcb1-column-action` |
| `AF-LEM-HCB1-COLUMN-ACTION` | `proofs/lem-hcb1-column-action/export.md` | `177412ec15b272d5` | `af` proof export for `lem-hcb1-column-action` |
| `ARG-LEM-HCB2-PRODUCT-DEFECT` | `argument/lemmas/lem-hcb2-product-defect.md` | `ced2d9fc9beeaa6d` | Registry shard for `lem-hcb2-product-defect` |
| `AF-LEM-HCB2-PRODUCT-DEFECT` | `proofs/lem-hcb2-product-defect/export.md` | `7bb9fdd2e3feb8ae` | `af` proof export for `lem-hcb2-product-defect` |
| `ARG-LEM-HCB3-DIAGONAL-UNIT` | `argument/lemmas/lem-hcb3-diagonal-unit.md` | `dbfb330643439d5c` | Registry shard for `lem-hcb3-diagonal-unit` |
| `AF-LEM-HCB3-DIAGONAL-UNIT` | `proofs/lem-hcb3-diagonal-unit/export.md` | `caeb9b93fb761bd8` | `af` proof export for `lem-hcb3-diagonal-unit` |
| `ARG-LEM-HCB3-DIAGONAL-UPPER-NORM` | `argument/lemmas/lem-hcb3-diagonal-upper-norm.md` | `ecb0f4c046f5fc21` | Registry shard for `lem-hcb3-diagonal-upper-norm` |
| `AF-LEM-HCB3-DIAGONAL-UPPER-NORM` | `proofs/lem-hcb3-diagonal-upper-norm/export.md` | `c34e1710967eaf2b` | `af` proof export for `lem-hcb3-diagonal-upper-norm` |
| `ARG-LEM-HCB3-UNIFORM-SQUARE-LOWER` | `argument/lemmas/lem-hcb3-uniform-square-lower.md` | `c9dbdb7f834c999e` | Registry shard for `lem-hcb3-uniform-square-lower` |
| `AF-LEM-HCB3-UNIFORM-SQUARE-LOWER` | `proofs/lem-hcb3-uniform-square-lower/export.md` | `dabba7ee13e6be01` | `af` proof export for `lem-hcb3-uniform-square-lower` |
| `ARG-LEM-HCB3-DIAGONAL-LOWER-MODULUS` | `argument/lemmas/lem-hcb3-diagonal-lower-modulus.md` | `1691acf1207ee77e` | Registry shard for `lem-hcb3-diagonal-lower-modulus` |
| `AF-LEM-HCB3-DIAGONAL-LOWER-MODULUS` | `proofs/lem-hcb3-diagonal-lower-modulus/export.md` | `4b0a3aa54c13ce2d` | `af` proof export for `lem-hcb3-diagonal-lower-modulus` |
| `ARG-LEM-HCB3-DIAGONAL-INVERSE` | `argument/lemmas/lem-hcb3-diagonal-inverse.md` | `bd9f655e16d64392` | Registry shard for `lem-hcb3-diagonal-inverse` |
| `AF-LEM-HCB3-DIAGONAL-INVERSE` | `proofs/lem-hcb3-diagonal-inverse/export.md` | `7bf03119e8aa18a6` | `af` proof export for `lem-hcb3-diagonal-inverse` |

## Per-claim ledger

| Report label | Source | Loc. | Status | Note |
|--------------|--------|------|--------|------|
| lem:classical-equiv | ARG-LEM-CLASSICAL-EQUIV AF-LEM-CLASSICAL-EQUIV | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-classical-equiv`. |
| lem:prh | ARG-LEM-PRH AF-LEM-PRH | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-prh`. |
| lem:compcb-amplification-naturality | ARG-LEM-COMPCB-AMPLIFICATION-NATURALITY AF-LEM-COMPCB-AMPLIFICATION-NATURALITY | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-compcb-amplification-naturality`. |
| lem:compcb-amplified-compression | ARG-LEM-COMPCB-AMPLIFIED-COMPRESSION AF-LEM-COMPCB-AMPLIFIED-COMPRESSION | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-compcb-amplified-compression`. |
| lem:compcb-amplified-compression-identities | ARG-LEM-COMPCB-AMPLIFIED-COMPRESSION-IDENTITIES AF-LEM-COMPCB-AMPLIFIED-COMPRESSION-IDENTITIES | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-compcb-amplified-compression-identities`. |
| lem:compcb-entrywise-compression-naturality | ARG-LEM-COMPCB-ENTRYWISE-COMPRESSION-NATURALITY AF-LEM-COMPCB-ENTRYWISE-COMPRESSION-NATURALITY | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-compcb-entrywise-compression-naturality`. |
| lem:compcb-rectangular-product | ARG-LEM-COMPCB-RECTANGULAR-PRODUCT AF-LEM-COMPCB-RECTANGULAR-PRODUCT | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-compcb-rectangular-product`. |
| lem:compcb-amplified-almost-containment | ARG-LEM-COMPCB-AMPLIFIED-ALMOST-CONTAINMENT AF-LEM-COMPCB-AMPLIFIED-ALMOST-CONTAINMENT | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-compcb-amplified-almost-containment`. |
| lem:compcb-compressed-unit-norm | ARG-LEM-COMPCB-COMPRESSED-UNIT-NORM AF-LEM-COMPCB-COMPRESSED-UNIT-NORM | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-compcb-compressed-unit-norm`. |
| lem:hcb2-amplified-adjointness | ARG-LEM-HCB2-AMPLIFIED-ADJOINTNESS AF-LEM-HCB2-AMPLIFIED-ADJOINTNESS | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb2-amplified-adjointness`. |
| lem:compcb-compressed-unit-action | ARG-LEM-COMPCB-COMPRESSED-UNIT-ACTION AF-LEM-COMPCB-COMPRESSED-UNIT-ACTION | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-compcb-compressed-unit-action`. |
| lem:compcb-row-column-product | ARG-LEM-COMPCB-ROW-COLUMN-PRODUCT AF-LEM-COMPCB-ROW-COLUMN-PRODUCT | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-compcb-row-column-product`. |
| lem:hcb0-compressed-associator | ARG-LEM-HCB0-COMPRESSED-ASSOCIATOR AF-LEM-HCB0-COMPRESSED-ASSOCIATOR | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb0-compressed-associator`. |
| lem:compcb-corner-algebra | ARG-LEM-COMPCB-CORNER-ALGEBRA AF-LEM-COMPCB-CORNER-ALGEBRA | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-compcb-corner-algebra`. |
| lem:hcb-column-hilbert-squared | ARG-LEM-HCB-COLUMN-HILBERT-SQUARED AF-LEM-HCB-COLUMN-HILBERT-SQUARED | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb-column-hilbert-squared`. |
| lem:compcb-single-compression-transfer | ARG-LEM-COMPCB-SINGLE-COMPRESSION-TRANSFER AF-LEM-COMPCB-SINGLE-COMPRESSION-TRANSFER | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-compcb-single-compression-transfer`. |
| lem:hcb1-variational-identity | ARG-LEM-HCB1-VARIATIONAL-IDENTITY AF-LEM-HCB1-VARIATIONAL-IDENTITY | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb1-variational-identity`. |
| lem:hcb1-column-action | ARG-LEM-HCB1-COLUMN-ACTION AF-LEM-HCB1-COLUMN-ACTION | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb1-column-action`. |
| lem:hcb2-product-defect | ARG-LEM-HCB2-PRODUCT-DEFECT AF-LEM-HCB2-PRODUCT-DEFECT | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb2-product-defect`. |
| lem:hcb3-diagonal-unit | ARG-LEM-HCB3-DIAGONAL-UNIT AF-LEM-HCB3-DIAGONAL-UNIT | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb3-diagonal-unit`. |
| lem:hcb3-diagonal-upper-norm | ARG-LEM-HCB3-DIAGONAL-UPPER-NORM AF-LEM-HCB3-DIAGONAL-UPPER-NORM | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb3-diagonal-upper-norm`. |
| lem:hcb3-uniform-square-lower | ARG-LEM-HCB3-UNIFORM-SQUARE-LOWER AF-LEM-HCB3-UNIFORM-SQUARE-LOWER | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb3-uniform-square-lower`. |
| lem:hcb3-diagonal-lower-modulus | ARG-LEM-HCB3-DIAGONAL-LOWER-MODULUS AF-LEM-HCB3-DIAGONAL-LOWER-MODULUS | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb3-diagonal-lower-modulus`. |
| lem:hcb3-diagonal-inverse | ARG-LEM-HCB3-DIAGONAL-INVERSE AF-LEM-HCB3-DIAGONAL-INVERSE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; workspace `proofs/lem-hcb3-diagonal-inverse`. |
