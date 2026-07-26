# Prose review corrections (waves 3+3b)

| Verdict locus | File/lines | Applied correction |
|---|---|---|
| F1 — shard 28 header | `28_hcb4_canonical_inverse.tex:4-5` | Replaced the challenge-history summary and keyword with the ready-to-paste closed-corner completeness summary and keywords. |
| F1 — shard 28 unsupported block | `28_hcb4_canonical_inverse.tex:103-107` | Deleted the entire “Corrections of record” block, including both reproduced `c_{00}` counterexamples and the challenge/repair narrative; nothing from the block was softened, summarized, or relocated. |
| F1 — shard 28 status | `28_hcb4_canonical_inverse.tex:104-107` | Replaced the unsupported definition/challenge/amendment ledger with the ready-to-paste 19-node validated status and six-node completeness-branch statement. |
| F2 — shard 26 status | `26_hcb4_canonical_gram.tex:104-106` | Replaced the unsupported definition/amendment/challenge history with the ready-to-paste 9-node validated status. |
| F3 — shard 27 status | `27_hcb4_canonical_closeness.tex:107-109` | Replaced the unsupported definition/amendment/challenge history and shard-28 comparison with the ready-to-paste 11-node validated status. |
| F4 — shard 35 status inventory | `35_status_outlook.tex:10-55` | Recomputed the inventory from `repo-inputs/argument-INDEX.md`: 36 explicitly listed reproduced `proved`/`validated` ids, 69 total `proved`/`validated` rows, and a 33-row complement. Added a LaTeX derivation comment immediately above every count. |
| F4 — shard 35 off-route table | `35_status_outlook.tex:91-142` | Rebuilt the table as the exact index-ordered complement of the reproduced ids. It has 33 rows: the former 30 rows plus `lem-collateral-import`, `lem-cross-pivot-cancellation`, and `lem-import-reduction`, all recorded as `proved`/`validated` by the supplied index and individual registry shards. Removed claims about an unsupported previous-edition ledger and `UNWIRED.md`. |
| WIRING §G2 | `WIRING.md:337` | Replaced the unsupported global-total/off-route-split claim with the verdict’s ready-to-paste two-sentence supplied-registry qualification. |

## AMBIGUOUS

None.

## Self-check

- `36`: the number of ids explicitly listed in shard 35’s reproduced inventory. All 36 have `status = proved` and `af = validated` in `repo-inputs/argument-INDEX.md`.
- `69`: the number of rows in `repo-inputs/argument-INDEX.md` whose status/AF pair is `proved`/`validated`.
- `33`: `69 - 36`; it is also the number of table rows. An exact sequence comparison confirms that the table is the generated-index-order complement, with no missing, extra, or duplicated id.
- Every table row’s id and `proved`/`validated` status pair matches its row in `repo-inputs/argument-INDEX.md`. The three newly provisioned rows also match their individual supplied registry shards.
- `conj-extcb` is not included in either validated count: the supplied index records `proved-mod-audit`/`seeded`, which is the pending status stated in the forward-reference text.
- The only other digits in shard 35 occur in shard/registry identifiers or unchanged LaTeX column-width parameters; they are not numerical status claims. Thus every quantitative claim in the shard has a named supplied-file derivation comment.
- Mechanics check: each edited `.tex` shard has one `\section`, complete SHARD-ID/TITLE/SUMMARY/KEYWORDS headers, unchanged labels, and no more than 280 lines.
