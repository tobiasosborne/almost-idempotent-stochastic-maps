# PROVENANCE — report audit ledger

**Policy.** Every Definition and Theorem reproduced in the report (`sections/*.tex`) must have an
entry in the per-claim ledger. An entry records: (1) the report label; (2) the ground-truth source
(a source-registry key with path + SHA256-16); (3) the source/internal-proof locus the
statement is matched to; (4) any harmonisation applied. "Provenanced" = a faithful
transcription/derivation of registered source material, or an internal project statement tied to a
hashed proof/consensus file. Results original to this project are marked `ORIGINAL`.

Verify a hash with: `sha256sum "<path>" | cut -c1-16`.

> **Current report surface.** The first shards reproduce twelve `af`-validated results and anchor every
> remaining registry result in the status ledger. Non-rigorous registry statuses are copied honestly;
> the ledger rows below are anchors, not promotions.

## Ground-truth source registry

| Key | Path | SHA256 (16) | What it is |
|-----|------|-------------|------------|
| `ARG-CONJ-DEGENERATE-PAYMENT` | `argument/lemmas/conj-degenerate-payment.md` | `3b7cd00d33cbf5fa` | Registry shard for `conj-degenerate-payment` |
| `ARG-CONJ-DEGENERATE-TRANSPORT` | `argument/lemmas/conj-degenerate-transport.md` | `25dcf1d0d6e1e977` | Registry shard for `conj-degenerate-transport` |
| `ARG-CONJ-EX` | `argument/lemmas/conj-ex.md` | `02d459033dc90a3c` | Registry shard for `conj-ex` |
| `ARG-CONJ-HALO-COLLAPSE` | `argument/lemmas/conj-halo-collapse.md` | `34f4de8d0861573d` | Registry shard for `conj-halo-collapse` |
| `ARG-CONJ-KERNEL` | `argument/lemmas/conj-kernel.md` | `9c1f2f250cf211a6` | Registry shard for `conj-kernel` |
| `ARG-CONJ-NO-FREE-FRONTIER` | `argument/lemmas/conj-no-free-frontier.md` | `070ea358dbc4c1b9` | Registry shard for `conj-no-free-frontier` |
| `ARG-CONJ-RH` | `argument/lemmas/conj-rh.md` | `32d9183c905dfe31` | Registry shard for `conj-rh` |
| `ARG-CONJ-SC` | `argument/lemmas/conj-sc.md` | `97a6fac2e65508ed` | Registry shard for `conj-sc` |
| `ARG-CONJ-SKINNY-SHADOW-CAP` | `argument/lemmas/conj-skinny-shadow-cap.md` | `c44aa05083b9e8c6` | Registry shard for `conj-skinny-shadow-cap` |
| `ARG-OBS-ORPHAN-AMPLIFIER` | `argument/lemmas/obs-orphan-amplifier.md` | `7472032fae335d9e` | Registry shard for `obs-orphan-amplifier` |
| `ARG-LEM-PIVOT-REMOVING-MOVE` | `argument/lemmas/lem-pivot-removing-move.md` | `0f636ca712959b57` | Registry shard for `lem-pivot-removing-move` |
| `ARG-EX-HUME` | `argument/lemmas/ex-hume.md` | `db5fb7b80f69be6a` | Registry shard for `ex-hume` |
| `ARG-LEM-CANONICAL-SEPARATOR` | `argument/lemmas/lem-canonical-separator.md` | `10d34ab7f83bfd0c` | Registry shard for `lem-canonical-separator` |
| `ARG-LEM-CLASSICAL-EQUIV` | `argument/lemmas/lem-classical-equiv.md` | `2f3a5574f2dfbbde` | Registry shard for `lem-classical-equiv` |
| `ARG-LEM-DUAL-LOCALIZATION` | `argument/lemmas/lem-dual-localization.md` | `ea1434019e41f90f` | Registry shard for `lem-dual-localization` (retired/superseded 2026-07-04) |
| `ARG-LEM-EXPOSED-CIRCUIT` | `argument/lemmas/lem-exposed-circuit.md` | `17f0f840a3bf79e8` | Registry shard for `lem-exposed-circuit` |
| `ARG-LEM-FAN-PAYMENT` | `argument/lemmas/lem-fan-payment.md` | `e1ddc5ff382fa777` | Registry shard for `lem-fan-payment` |
| `ARG-LEM-FACTORIZATION` | `argument/lemmas/lem-factorization.md` | `206a89c203319e6f` | Registry shard for `lem-factorization` |
| `ARG-LEM-WEIGHTED-MIN` | `argument/lemmas/lem-weighted-min.md` | `027c9e9d2177675c` | Registry shard for `lem-weighted-min` |
| `ARG-LEM-ZEROSUM-TRIANGLE` | `argument/lemmas/lem-zerosum-triangle.md` | `faf9bf0f9ebbde07` | Registry shard for `lem-zerosum-triangle` |
| `ARG-LEM-FAN-PAYMENT-RESTRICTED` | `argument/lemmas/lem-fan-payment-restricted.md` | `5cea17b1c6fd6722` | Registry shard for `lem-fan-payment-restricted` |
| `ARG-LEM-NEGPART-SUBADDITIVE` | `argument/lemmas/lem-negpart-subadditive.md` | `ef75f5da237ac853` | Registry shard for `lem-negpart-subadditive` |
| `ARG-LEM-LEAKAGE` | `argument/lemmas/lem-leakage.md` | `ebedf751f8a1d2ab` | Registry shard for `lem-leakage` |
| `ARG-LEM-MASS-SPLIT` | `argument/lemmas/lem-mass-split.md` | `634fdf3556b8f4ea` | Registry shard for `lem-mass-split` |
| `ARG-LEM-RESIDUAL-LOWER` | `argument/lemmas/lem-residual-lower.md` | `3d4604e0725be091` | Registry shard for `lem-residual-lower` |
| `ARG-LEM-RESIDUAL-UPPER` | `argument/lemmas/lem-residual-upper.md` | `dc6328ea2b22dd3e` | Registry shard for `lem-residual-upper` |
| `ARG-LEM-WIGGLE-RIGIDITY` | `argument/lemmas/lem-wiggle-rigidity.md` | `8a2455f1281f7c41` | Registry shard for `lem-wiggle-rigidity` |
| `ARG-OBS-DEEP-LEAKAGE` | `argument/lemmas/obs-deep-leakage.md` | `5824fd1d4ef9d890` | Registry shard for `obs-deep-leakage` |
| `ARG-OBS-FWR-GAP` | `argument/lemmas/obs-fwr-gap.md` | `577a9461bf982794` | Registry shard for `obs-fwr-gap` |
| `ARG-OBS-HEIGHT-COLLAPSE` | `argument/lemmas/obs-height-collapse.md` | `d7eb2ff172935af3` | Registry shard for `obs-height-collapse` |
| `ARG-OBS-LINEAR-LAW-FINITE-DELTA` | `argument/lemmas/obs-linear-law-finite-delta.md` | `e42a723d8f9a40b5` | Registry shard for `obs-linear-law-finite-delta` |
| `ARG-OBS-SIGMA-HALO-NONROBUST` | `argument/lemmas/obs-sigma-halo-nonrobust.md` | `cc2f80fb9fc80e45` | Registry shard for `obs-sigma-halo-nonrobust` |
| `ARG-OP-CLASSICAL` | `argument/lemmas/op-classical.md` | `2ef7e965c5db0146` | Registry shard for `op-classical` |
| `ARG-OP-EXPOSED-HULL` | `argument/lemmas/op-exposed-hull.md` | `d988f94acd0e06b7` | Registry shard for `op-exposed-hull` |
| `ARG-PROP-APPROX-SIMPLEX` | `argument/lemmas/prop-approx-simplex.md` | `36bc314b5637c753` | Registry shard for `prop-approx-simplex` |
| `ARG-THM-CLASSICAL-FACTORIZATION` | `argument/lemmas/thm-classical-factorization.md` | `5aef19d51a9dea22` | Registry shard for `thm-classical-factorization` |
| `ARG-THM-CLUSTER` | `argument/lemmas/thm-cluster.md` | `822ae1100d053594` | Registry shard for `thm-cluster` |
| `ARG-THM-CORNER-CONSTANTS` | `argument/lemmas/thm-corner-constants.md` | `5511fbf48c7a35db` | Registry shard for `thm-corner-constants` |
| `ARG-THM-RANK-ONE` | `argument/lemmas/thm-rank-one.md` | `2934d0541289281a` | Registry shard for `thm-rank-one` |
| `ARG-THM-SIMPLEX` | `argument/lemmas/thm-simplex.md` | `68e40372042d2d7c` | Registry shard for `thm-simplex` |
| `ARG-THM-WELL-EXPOSED` | `argument/lemmas/thm-well-exposed.md` | `87b83d58733411c7` | Registry shard for `thm-well-exposed` |
| `AF-LEM-CLASSICAL-EQUIV` | `proofs/lem-classical-equiv/export.md` | `35b46507291c6cb0` | `af` proof export for `lem-classical-equiv` |
| `AF-OBS-HEIGHT-COLLAPSE` | `proofs/obs-height-collapse/export.md` | `09189b50445991e8` | `af` proof export for `obs-height-collapse` |
| `AF-LEM-MASS-SPLIT` | `proofs/lem-mass-split/export.md` | `67002d8da8acec01` | `af` proof export for `lem-mass-split` |
| `AF-LEM-RESIDUAL-LOWER` | `proofs/lem-residual-lower/export.md` | `e8fbf760d4954dad` | `af` proof export for `lem-residual-lower` |
| `AF-LEM-RESIDUAL-UPPER` | `proofs/lem-residual-upper/export.md` | `05e247da7eb8db25` | `af` proof export for `lem-residual-upper` |
| `AF-CONJ-HALO-COLLAPSE` | `proofs/conj-halo-collapse/export.md` | `216304dc1141dd42` | `af` proof export for `conj-halo-collapse` |
| `AF-LEM-FAN-PAYMENT-RESTRICTED` | `proofs/lem-fan-payment-restricted/export.md` | `7391a277652ba34b` | `af` proof export for `lem-fan-payment-restricted` |
| `AF-LEM-NEGPART-SUBADDITIVE` | `proofs/lem-negpart-subadditive/export.md` | `fe2ceedc496256f6` | `af` proof export for `lem-negpart-subadditive` |
| `AF-LEM-FAN-PAYMENT` | `proofs/lem-fan-payment/export.md` | `e5b82f20f763b68a` | `af` proof export for `lem-fan-payment` |
| `AF-LEM-WEIGHTED-MIN` | `proofs/lem-weighted-min/export.md` | `2b0bc678481aa4cc` | `af` proof export for `lem-weighted-min` |
| `AF-LEM-ZEROSUM-TRIANGLE` | `proofs/lem-zerosum-triangle/export.md` | `10c4fc62e9ad5714` | `af` proof export for `lem-zerosum-triangle` |
| `AF-LEM-FACTORIZATION` | `proofs/lem-factorization/export.md` | `c755b58b9c2a2fe9` | `af` proof export for `lem-factorization` |

## Per-claim ledger

Status column: **V** = byte-verified against the registered local source; **I** = inline-provenanced
(source+locus in a `% PROV:` comment), awaiting byte-check; **O** = ORIGINAL/internal result tied to a
hashed file; **OPEN** = project target/conjectural, not a proved theorem; **HEURISTIC** = perturbative/
field-theory argument (NON-rigorous); **NUMERICAL** = supported only by a `runs/` bundle (NON-rigorous);
**EXTRACT** = supported by a hashed extraction, not yet byte-matched; **PDF** = PDF not yet text-verified;
**SUPERSEDED** = the registry contract was retired and superseded by a successor shard (see the row note).

| Report label | Source | Loc. | Status | Note |
|--------------|--------|------|--------|------|
| lem:classical-equiv | ARG-LEM-CLASSICAL-EQUIV AF-LEM-CLASSICAL-EQUIV | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`. |
| obs:height-collapse | ARG-OBS-HEIGHT-COLLAPSE AF-OBS-HEIGHT-COLLAPSE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`. |
| lem:mass-split | ARG-LEM-MASS-SPLIT AF-LEM-MASS-SPLIT | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`. |
| lem:residual-lower | ARG-LEM-RESIDUAL-LOWER AF-LEM-RESIDUAL-LOWER | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`. |
| lem:residual-upper | ARG-LEM-RESIDUAL-UPPER AF-LEM-RESIDUAL-UPPER | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; large tree warning retained. |
| conj:degenerate-payment | ARG-CONJ-DEGENERATE-PAYMENT | registry contract | OPEN | Status ledger anchor only; registry status `conjecture` (A8 payment horn). |
| conj:degenerate-transport | ARG-CONJ-DEGENERATE-TRANSPORT | registry contract | OPEN | Status ledger anchor only; registry status `conjecture` (A12 transport gap). |
| conj:ex | ARG-CONJ-EX | registry contract | OPEN | Status ledger anchor only; registry status `conjecture`. |
| conj:halo-collapse | ARG-CONJ-HALO-COLLAPSE AF-CONJ-HALO-COLLAPSE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; run-2 tree on the factored workspace. |
| conj:kernel | ARG-CONJ-KERNEL | registry contract | OPEN | Status ledger anchor only; registry status `conjecture`. |
| conj:no-free-frontier | ARG-CONJ-NO-FREE-FRONTIER | registry contract | OPEN | Status ledger anchor only; registry status `conjecture`. |
| conj:rh | ARG-CONJ-RH | registry contract | OPEN | Status ledger anchor only; registry status `conjecture` (repaired orphan horn; exact coefficient floor 4 from obs-orphan-amplifier). |
| conj:sc | ARG-CONJ-SC | registry contract | OPEN | Status ledger anchor only; registry status `conjecture` ((SC) control; reduced to (PRT), collateral branch open after G9). |
| conj:skinny-shadow-cap | ARG-CONJ-SKINNY-SHADOW-CAP | registry contract | OPEN | Status ledger anchor only; registry status `conjecture` (corrected Route-B skinny cap; supersedes lem-dual-localization). |
| obs:orphan-amplifier | ARG-OBS-ORPHAN-AMPLIFIER | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit` (exact G5 two-orphan family; identities orchestrator-recomputed 2026-07-04). |
| lem:pivot-removing-move | ARG-LEM-PIVOT-REMOVING-MOVE | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit` (G7 pivot-removing tool; wave paper-proof, unreviewed). |
| ex:hume | ARG-EX-HUME | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit`, not rigorous here. |
| lem:canonical-separator | ARG-LEM-CANONICAL-SEPARATOR | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit`. |
| lem:dual-localization | ARG-LEM-DUAL-LOCALIZATION | registry contract | SUPERSEDED | Retired 2026-07-04 (contract trivially true as stated); superseded by conj-skinny-shadow-cap; registry status `obstruction`. |
| lem:exposed-circuit | ARG-LEM-EXPOSED-CIRCUIT | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit`. |
| lem:factorization | ARG-LEM-FACTORIZATION AF-LEM-FACTORIZATION | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; run-1 tree, tightness claim not elevated. |
| lem:fan-payment | ARG-LEM-FAN-PAYMENT AF-LEM-FAN-PAYMENT | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; run-3 tree on the factored workspace, runs 1-2 ballooned. |
| lem:weighted-min | ARG-LEM-WEIGHTED-MIN AF-LEM-WEIGHTED-MIN | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; verify phase resumed after a network outage. |
| lem:zerosum-triangle | ARG-LEM-ZEROSUM-TRIANGLE AF-LEM-ZEROSUM-TRIANGLE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; run-1 tree, factored out of lem-fan-payment. |
| lem:fan-payment-restricted | ARG-LEM-FAN-PAYMENT-RESTRICTED AF-LEM-FAN-PAYMENT-RESTRICTED | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; run-1 tree; sharpness certificates not elevated. |
| lem:negpart-subadditive | ARG-LEM-NEGPART-SUBADDITIVE AF-LEM-NEGPART-SUBADDITIVE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; run-1 tree, pre-factored before elevation. |
| lem:leakage | ARG-LEM-LEAKAGE | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit`. |
| lem:wiggle-rigidity | ARG-LEM-WIGGLE-RIGIDITY | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit`. |
| obs:deep-leakage | ARG-OBS-DEEP-LEAKAGE | registry contract | HEURISTIC | Status ledger anchor only; registry status `heuristic`. |
| obs:fwr-gap | ARG-OBS-FWR-GAP | registry contract | HEURISTIC | Status ledger anchor only; registry status `heuristic`. |
| obs:linear-law-finite-delta | ARG-OBS-LINEAR-LAW-FINITE-DELTA | registry contract | NUMERICAL | Status ledger anchor only; registry status `numerical`. |
| obs:sigma-halo-nonrobust | ARG-OBS-SIGMA-HALO-NONROBUST | registry contract | NUMERICAL | Status ledger anchor only; registry status `numerical`. |
| op:classical | ARG-OP-CLASSICAL | registry contract | OPEN | Status ledger anchor only; registry status `open`. |
| op:exposed-hull | ARG-OP-EXPOSED-HULL | registry contract | OPEN | Status ledger anchor only; registry status `open`. |
| prop:approx-simplex | ARG-PROP-APPROX-SIMPLEX | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit`. |
| thm:classical-factorization | ARG-THM-CLASSICAL-FACTORIZATION | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit`. |
| thm:cluster | ARG-THM-CLUSTER | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit`. |
| thm:corner-constants | ARG-THM-CORNER-CONSTANTS | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit`; numerical component not promoted. |
| thm:rank-one | ARG-THM-RANK-ONE | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit`. |
| thm:simplex | ARG-THM-SIMPLEX | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit`. |
| thm:well-exposed | ARG-THM-WELL-EXPOSED | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit`. |
