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

## Ground-truth source registry

| Key | Path | SHA256 (16) | What it is |
|-----|------|-------------|------------|
| `ARG-CONJ-DEGENERATE-PAYMENT` | `argument/lemmas/conj-degenerate-payment.md` | `3b7cd00d33cbf5fa` | Registry shard for `conj-degenerate-payment` |
| `ARG-CONJ-DEGENERATE-TRANSPORT` | `argument/lemmas/conj-degenerate-transport.md` | `b68de13aaa480a15` | Registry shard for `conj-degenerate-transport` |
| `ARG-CONJ-EX` | `argument/lemmas/conj-ex.md` | `150f2cf7b1925372` | Registry shard for `conj-ex` |
| `ARG-LEM-HALO-COLLAPSE` | `argument/lemmas/lem-halo-collapse.md` | `297e462fa69d03c7` | Registry shard for `lem-halo-collapse` (renamed from `conj-halo-collapse` 2026-07-10) |
| `ARG-CONJ-KERNEL` | `argument/lemmas/conj-kernel.md` | `f010524f7cf199f0` | Registry shard for `conj-kernel` |
| `ARG-CONJ-NO-FREE-FRONTIER` | `argument/lemmas/conj-no-free-frontier.md` | `ae2798814ac899f5` | Registry shard for `conj-no-free-frontier` |
| `ARG-CONJ-RH` | `argument/lemmas/conj-rh.md` | `c4b4885f2a17b4d7` | Registry shard for `conj-rh` |
| `ARG-CONJ-SC` | `argument/lemmas/conj-sc.md` | `618c7511457521d6` | Registry shard for `conj-sc` |
| `ARG-CONJ-SKINNY-SHADOW-CAP` | `argument/lemmas/conj-skinny-shadow-cap.md` | `c44aa05083b9e8c6` | Registry shard for `conj-skinny-shadow-cap` |
| `ARG-OBS-ORPHAN-AMPLIFIER` | `argument/lemmas/obs-orphan-amplifier.md` | `7472032fae335d9e` | Registry shard for `obs-orphan-amplifier` |
| `ARG-LEM-PIVOT-REMOVING-MOVE` | `argument/lemmas/lem-pivot-removing-move.md` | `69fa5db24c4aefbf` | Registry shard for `lem-pivot-removing-move` |
| `ARG-LEM-CROSS-PIVOT-CANCELLATION` | `argument/lemmas/lem-cross-pivot-cancellation.md` | `0ee1d3933b8df1df` | Registry shard for `lem-cross-pivot-cancellation` |
| `ARG-LEM-IMPORT-REDUCTION` | `argument/lemmas/lem-import-reduction.md` | `b228e6b2c93470ce` | Registry shard for `lem-import-reduction` |
| `ARG-LEM-COLLATERAL-IMPORT` | `argument/lemmas/lem-collateral-import.md` | `84d102f0f6623af1` | Registry shard for `lem-collateral-import` |
| `ARG-EX-HUME` | `argument/lemmas/ex-hume.md` | `5c9bdc59fc0e4413` | Registry shard for `ex-hume` |
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
| `ARG-LEM-MASS-SPLIT` | `argument/lemmas/lem-mass-split.md` | `7fe0b0de4b392d5c` | Registry shard for `lem-mass-split` |
| `ARG-LEM-RESIDUAL-LOWER` | `argument/lemmas/lem-residual-lower.md` | `368090f8f6e2b61a` | Registry shard for `lem-residual-lower` |
| `ARG-LEM-RESIDUAL-UPPER` | `argument/lemmas/lem-residual-upper.md` | `c062d9f2e84df296` | Registry shard for `lem-residual-upper` |
| `ARG-LEM-WIGGLE-RIGIDITY` | `argument/lemmas/lem-wiggle-rigidity.md` | `8a2455f1281f7c41` | Registry shard for `lem-wiggle-rigidity` |
| `ARG-OBS-DEEP-LEAKAGE` | `argument/lemmas/obs-deep-leakage.md` | `5824fd1d4ef9d890` | Registry shard for `obs-deep-leakage` |
| `ARG-OBS-FWR-GAP` | `argument/lemmas/obs-fwr-gap.md` | `577a9461bf982794` | Registry shard for `obs-fwr-gap` |
| `ARG-OBS-HEIGHT-COLLAPSE` | `argument/lemmas/obs-height-collapse.md` | `d7eb2ff172935af3` | Registry shard for `obs-height-collapse` |
| `ARG-OBS-LINEAR-LAW-FINITE-DELTA` | `argument/lemmas/obs-linear-law-finite-delta.md` | `e42a723d8f9a40b5` | Registry shard for `obs-linear-law-finite-delta` |
| `ARG-OBS-SIGMA-HALO-NONROBUST` | `argument/lemmas/obs-sigma-halo-nonrobust.md` | `2149abf651bb54fa` | Registry shard for `obs-sigma-halo-nonrobust` |
| `ARG-OP-CLASSICAL` | `argument/lemmas/op-classical.md` | `2ef7e965c5db0146` | Registry shard for `op-classical` |
| `ARG-OP-EXPOSED-HULL` | `argument/lemmas/op-exposed-hull.md` | `32e37b1a400c883d` | Registry shard for `op-exposed-hull` |
| `ARG-PROP-APPROX-SIMPLEX` | `argument/lemmas/prop-approx-simplex.md` | `9f82860ad220c83c` | Registry shard for `prop-approx-simplex` |
| `ARG-THM-CLASSICAL-FACTORIZATION` | `argument/lemmas/thm-classical-factorization.md` | `d8141d320ce37791` | Registry shard for `thm-classical-factorization` |
| `ARG-THM-CLUSTER` | `argument/lemmas/thm-cluster.md` | `a0b07d18715d720e` | Registry shard for `thm-cluster` |
| `ARG-THM-CORNER-CONSTANTS` | `argument/lemmas/thm-corner-constants.md` | `5511fbf48c7a35db` | Registry shard for `thm-corner-constants` |
| `ARG-THM-RANK-ONE` | `argument/lemmas/thm-rank-one.md` | `2934d0541289281a` | Registry shard for `thm-rank-one` |
| `ARG-THM-SIMPLEX` | `argument/lemmas/thm-simplex.md` | `68e40372042d2d7c` | Registry shard for `thm-simplex` |
| `ARG-THM-WELL-EXPOSED` | `argument/lemmas/thm-well-exposed.md` | `87b83d58733411c7` | Registry shard for `thm-well-exposed` |
| `AF-LEM-CLASSICAL-EQUIV` | `proofs/lem-classical-equiv/export.md` | `35b46507291c6cb0` | `af` proof export for `lem-classical-equiv` |
| `AF-OBS-HEIGHT-COLLAPSE` | `proofs/obs-height-collapse/export.md` | `09189b50445991e8` | `af` proof export for `obs-height-collapse` |
| `AF-LEM-MASS-SPLIT` | `proofs/lem-mass-split/export.md` | `67002d8da8acec01` | `af` proof export for `lem-mass-split` |
| `AF-LEM-RESIDUAL-LOWER` | `proofs/lem-residual-lower/export.md` | `e8fbf760d4954dad` | `af` proof export for `lem-residual-lower` |
| `AF-LEM-RESIDUAL-UPPER` | `proofs/lem-residual-upper/export.md` | `05e247da7eb8db25` | `af` proof export for `lem-residual-upper` |
| `AF-LEM-HALO-COLLAPSE` | `proofs/conj-halo-collapse/export.md` | `216304dc1141dd42` | `af` proof export for `lem-halo-collapse` (workspace dir kept at `proofs/conj-halo-collapse/`) |
| `AF-LEM-FAN-PAYMENT-RESTRICTED` | `proofs/lem-fan-payment-restricted/export.md` | `7391a277652ba34b` | `af` proof export for `lem-fan-payment-restricted` |
| `AF-LEM-NEGPART-SUBADDITIVE` | `proofs/lem-negpart-subadditive/export.md` | `fe2ceedc496256f6` | `af` proof export for `lem-negpart-subadditive` |
| `AF-LEM-FAN-PAYMENT` | `proofs/lem-fan-payment/export.md` | `e5b82f20f763b68a` | `af` proof export for `lem-fan-payment` |
| `AF-LEM-WEIGHTED-MIN` | `proofs/lem-weighted-min/export.md` | `2b0bc678481aa4cc` | `af` proof export for `lem-weighted-min` |
| `AF-LEM-ZEROSUM-TRIANGLE` | `proofs/lem-zerosum-triangle/export.md` | `10c4fc62e9ad5714` | `af` proof export for `lem-zerosum-triangle` |
| `AF-LEM-FACTORIZATION` | `proofs/lem-factorization/export.md` | `c755b58b9c2a2fe9` | `af` proof export for `lem-factorization` |
| `AF-LEM-COLLATERAL-IMPORT` | `proofs/lem-collateral-import/export.md` | `c2d35f80dc8b12c6` | `af` proof export for `lem-collateral-import` |
| `AF-LEM-CROSS-PIVOT-CANCELLATION` | `proofs/lem-cross-pivot-cancellation/export.md` | `942b216f2a64b6bd` | `af` proof export for `lem-cross-pivot-cancellation` |
| `AF-LEM-PIVOT-REMOVING-MOVE` | `proofs/lem-pivot-removing-move/export.md` | `276e02185cab5cc3` | `af` proof export for `lem-pivot-removing-move` |
| `ARG-LEM-HIDDENNESS-DUAL-WITNESS` | `argument/lemmas/lem-hiddenness-dual-witness.md` | `a89129996a8d06a7` | Registry shard for `lem-hiddenness-dual-witness` |
| `AF-LEM-HIDDENNESS-DUAL-WITNESS` | `proofs/lem-hiddenness-dual-witness/export.md` | `d71d6c8842a42fd7` | `af` proof export for `lem-hiddenness-dual-witness` |
| `ARG-LEM-ALWAYS-TIGHT-DUAL-SUPPORT` | `argument/lemmas/lem-always-tight-dual-support.md` | `f277cfd1cf557222` | Registry shard for `lem-always-tight-dual-support` |
| `AF-LEM-ALWAYS-TIGHT-DUAL-SUPPORT` | `proofs/lem-always-tight-dual-support/export.md` | `5627d564d97b0ce7` | `af` proof export for `lem-always-tight-dual-support` |
| `ARG-LEM-HIDDENNESS-DEPTH-MARKOV` | `argument/lemmas/lem-hiddenness-depth-markov.md` | `1b9fba36bbd9e28c` | Registry shard for `lem-hiddenness-depth-markov` |
| `AF-LEM-HIDDENNESS-DEPTH-MARKOV` | `proofs/lem-hiddenness-depth-markov/export.md` | `e47f169b3bd440ce` | `af` proof export for `lem-hiddenness-depth-markov` |
| `ARG-LEM-ROW-FAR-DUAL-CERTIFICATE` | `argument/lemmas/lem-row-far-dual-certificate.md` | `c9de63ba0422ab59` | Registry shard for `lem-row-far-dual-certificate` |
| `AF-LEM-ROW-FAR-DUAL-CERTIFICATE` | `proofs/lem-row-far-dual-certificate/export.md` | `b4214c77f3e8c43c` | `af` proof export for `lem-row-far-dual-certificate` |
| `ARG-LEM-TOP-SLAB-COMPANION` | `argument/lemmas/lem-top-slab-companion.md` | `2ba54119151a63c2` | Registry shard for `lem-top-slab-companion` |
| `AF-LEM-TOP-SLAB-COMPANION` | `proofs/lem-top-slab-companion/export.md` | `0bd9a544b579944a` | `af` proof export for `lem-top-slab-companion` |
| `ARG-LEM-CS-LOW-SLAB-PINCER` | `argument/lemmas/lem-cs-low-slab-pincer.md` | `7115bf723810e0aa` | Registry shard for `lem-cs-low-slab-pincer` |
| `AF-LEM-CS-LOW-SLAB-PINCER` | `proofs/lem-cs-low-slab-pincer/export.md` | `e40f769ec5cd533a` | `af` proof export for `lem-cs-low-slab-pincer` |
| `ARG-LEM-ROW-ZERO-CAPACITY` | `argument/lemmas/lem-row-zero-capacity.md` | `fd6eacae12969ebd` | Registry shard for `lem-row-zero-capacity` |
| `AF-LEM-ROW-ZERO-CAPACITY` | `proofs/lem-row-zero-capacity/export.md` | `58a4acc9f72797ca` | `af` proof export for `lem-row-zero-capacity` |
| `ARG-LEM-HARMONIC-AFFINE-BRIDGE` | `argument/lemmas/lem-harmonic-affine-bridge.md` | `2b3d9266b79e3a35` | Registry shard for `lem-harmonic-affine-bridge` |
| `AF-LEM-HARMONIC-AFFINE-BRIDGE` | `proofs/lem-harmonic-affine-bridge/export.md` | `fe417c19b4d62333` | `af` proof export for `lem-harmonic-affine-bridge` |
| `ARG-LEM-PARAMETRIC-HALO-COLLAPSE` | `argument/lemmas/lem-parametric-halo-collapse.md` | `8c67fd4310b7725d` | Registry shard for `lem-parametric-halo-collapse` |
| `AF-LEM-PARAMETRIC-HALO-COLLAPSE` | `proofs/lem-parametric-halo-collapse/export.md` | `12a8d1452a51a257` | `af` proof export for `lem-parametric-halo-collapse` |
| `ARG-LEM-DEPTH-D-HALO-COLLAPSE` | `argument/lemmas/lem-depth-d-halo-collapse.md` | `35ce052128fc18a9` | Registry shard for `lem-depth-d-halo-collapse` |
| `AF-LEM-DEPTH-D-HALO-COLLAPSE` | `proofs/lem-depth-d-halo-collapse/export.md` | `c22fed932acf9cb7` | `af` proof export for `lem-depth-d-halo-collapse` |
| `ARG-LEM-GENUINE-DISINTEGRATION` | `argument/lemmas/lem-genuine-disintegration.md` | `e68f022493e5e777` | Registry shard for `lem-genuine-disintegration` |
| `AF-LEM-GENUINE-DISINTEGRATION` | `proofs/lem-genuine-disintegration/export.md` | `926f1e024670b0e2` | `af` proof export for `lem-genuine-disintegration` |
| `ARG-LEM-TOP-CONCENTRATION` | `argument/lemmas/lem-top-concentration.md` | `9a94c19f6bbd5a1e` | Registry shard for `lem-top-concentration` |
| `AF-LEM-TOP-CONCENTRATION` | `proofs/lem-top-concentration/export.md` | `835cacb8312e2d83` | `af` proof export for `lem-top-concentration` |
| `ARG-LEM-STARVATION-COMPLETION-OBSTRUCTION` | `argument/lemmas/lem-starvation-completion-obstruction.md` | `a7ae8563e5777a18` | Registry shard for `lem-starvation-completion-obstruction` |
| `AF-LEM-STARVATION-COMPLETION-OBSTRUCTION` | `proofs/lem-starvation-completion-obstruction/export.md` | `ed573c49836f7273` | `af` proof export for `lem-starvation-completion-obstruction` |

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
| lem:halo-collapse | ARG-LEM-HALO-COLLAPSE AF-LEM-HALO-COLLAPSE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; run-2 tree on the factored workspace. |
| conj:kernel | ARG-CONJ-KERNEL | registry contract | OPEN | Status ledger anchor only; registry status `conjecture`. |
| conj:no-free-frontier | ARG-CONJ-NO-FREE-FRONTIER | registry contract | OPEN | Status ledger anchor only; registry status `conjecture`. |
| conj:rh | ARG-CONJ-RH | registry contract | OPEN | Status ledger anchor only; registry status `conjecture` (repaired orphan horn; exact coefficient floor 4 from obs-orphan-amplifier). |
| conj:sc | ARG-CONJ-SC | registry contract | OPEN | Status ledger anchor only; registry status `conjecture` ((SC) control; reduced to (PRT), collateral branch open after G9). |
| conj:skinny-shadow-cap | ARG-CONJ-SKINNY-SHADOW-CAP | registry contract | OPEN | Status ledger anchor only; registry status `conjecture` (corrected Route-B skinny cap; supersedes lem-dual-localization). |
| obs:orphan-amplifier | ARG-OBS-ORPHAN-AMPLIFIER | registry contract | EXTRACT | Status ledger anchor only; registry status `proved-mod-audit` (exact G5 two-orphan family; identities orchestrator-recomputed 2026-07-04). |
| lem:pivot-removing-move | ARG-LEM-PIVOT-REMOVING-MOVE AF-LEM-PIVOT-REMOVING-MOVE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; run-1 tree, zero challenges, pre-factored elevation. |
| lem:hiddenness-dual-witness | ARG-LEM-HIDDENNESS-DUAL-WITNESS AF-LEM-HIDDENNESS-DUAL-WITNESS | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; first-principles finite LP duality, no imports. |
| lem:always-tight-dual-support | ARG-LEM-ALWAYS-TIGHT-DUAL-SUPPORT AF-LEM-ALWAYS-TIGHT-DUAL-SUPPORT | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; imports lem-hiddenness-dual-witness as validated external. |
| lem:hiddenness-depth-markov | ARG-LEM-HIDDENNESS-DEPTH-MARKOV AF-LEM-HIDDENNESS-DEPTH-MARKOV | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; verifier weakened hypotheses to any witness with sum beta < kappa. |
| lem:row-far-dual-certificate | ARG-LEM-ROW-FAR-DUAL-CERTIFICATE AF-LEM-ROW-FAR-DUAL-CERTIFICATE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; weak-duality certificate, sharp on the W29 frontier. |
| lem:top-slab-companion | ARG-LEM-TOP-SLAB-COMPANION AF-LEM-TOP-SLAB-COMPANION | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; exact symbolic constant chain checked. |
| lem:cs-low-slab-pincer | ARG-LEM-CS-LOW-SLAB-PINCER AF-LEM-CS-LOW-SLAB-PINCER | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; minimal hypotheses, sharp at s = t*. |
| lem:row-zero-capacity | ARG-LEM-ROW-ZERO-CAPACITY AF-LEM-ROW-ZERO-CAPACITY | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; rests on lem-harmonic-affine-bridge in the registry. |
| lem:harmonic-affine-bridge | ARG-LEM-HARMONIC-AFFINE-BRIDGE AF-LEM-HARMONIC-AFFINE-BRIDGE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; two lines each direction. |
| lem:parametric-halo-collapse | ARG-LEM-PARAMETRIC-HALO-COLLAPSE AF-LEM-PARAMETRIC-HALO-COLLAPSE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; imports mass-split, residual-lower, residual-upper; recovers lem-halo-collapse at a = 1/4. |
| lem:depth-d-halo-collapse | ARG-LEM-DEPTH-D-HALO-COLLAPSE AF-LEM-DEPTH-D-HALO-COLLAPSE | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; imports mass-split, residual-upper; calibrates against parametric-halo-collapse. |
| lem:genuine-disintegration | ARG-LEM-GENUINE-DISINTEGRATION AF-LEM-GENUINE-DISINTEGRATION | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; imports residual-upper; g-bootstrap step 3. |
| lem:top-concentration | ARG-LEM-TOP-CONCENTRATION AF-LEM-TOP-CONCENTRATION | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; first-principles support functional, no imports. |
| lem:starvation-completion-obstruction | ARG-LEM-STARVATION-COMPLETION-OBSTRUCTION AF-LEM-STARVATION-COMPLETION-OBSTRUCTION | registry contract and proof export node 1 | O | Contract quoted verbatim; status `proved`, `af: validated`; W59 paper-proof, fresh hostile verifier VALID-WITH-CORRECTIONS, reviewer != author. |
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
| lem:collateral-import | ARG-LEM-COLLATERAL-IMPORT AF-LEM-COLLATERAL-IMPORT | registry contract | PROVED | Status ledger row; af-validated in-repo 2026-07-04 (32-node tree, taint clean; run 1, zero open challenges); section shard pending. |
| lem:cross-pivot-cancellation | ARG-LEM-CROSS-PIVOT-CANCELLATION AF-LEM-CROSS-PIVOT-CANCELLATION | registry contract | PROVED | Status ledger row; af-validated in-repo 2026-07-04 (23-node tree, taint clean; run 1); near-definitional — weight discounted per session audit; section shard pending. |
| lem:import-reduction | ARG-LEM-IMPORT-REDUCTION | registry contract | PROVED | Status ledger row; registry status `proved`, `af: validated` (G11 reduction (4)); section shard pending. |
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
