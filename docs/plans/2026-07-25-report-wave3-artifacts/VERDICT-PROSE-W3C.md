VERDICT: 5-VALID/7-reviewed

35_extcb.tex: VALID — the contract quote byte-matches `conj-extcb`; the prose follows the validated correction/spatialisation/inverse-trigger/merge spine, does not rely on archived nodes, and keeps the two constant ledgers distinct.
26_hcb4_canonical_gram.tex: VALID — the unsupported definition/amendment/challenge ledger is gone and the replacement 9-node status is supported.
27_hcb4_canonical_closeness.tex: VALID — the unsupported definition/amendment/challenge ledger and shard-28 comparison are gone and the replacement 11-node status is supported.
28_hcb4_canonical_inverse.tex: VALID-WITH-CORRECTIONS — the counterexamples, correction block, counts, and old defs-line claim are gone, but the new defs sentence reintroduces unsupported challenge-history metadata.
36_status_outlook.tex: VALID — independent recomputation gives 70 `proved`/`validated` index rows, 37 distinct reproduced ids, and the displayed 33-row exact index-ordered complement.
propagation-set (29/32/34 and all 12 shards): VALID — every `conj-extcb` reference now reflects `proved` / `af: validated`; no stale pending, seeded, elevation, or one-rung-below description remains.
WIRING.md: INVALID — one §E hash and the corresponding §I post-hygiene assertion contradict the supplied ground truth; §G3 also repeats the shard-28 challenge-history regression.

## Findings and ready-to-paste corrections

### F1 — MINOR — shard 28 reintroduces challenge-history metadata

`28_hcb4_canonical_inverse.tex:114-118` correctly reflects the post-fix five-entry `defs:` line until its final clause, “one of them only after a hostile challenge said so.” Neither the supplied post-fix registry nor its export states that history. It also directly contradicts the brief's requirement that the corrected shard contain no challenge-history metadata. WIRING §G3 repeats the clause and then falsely says that no such metadata was reintroduced.

Replace shard 28 lines 114-118 by:

```latex
Its \texttt{defs} line records \texttt{def-ha-map}, \texttt{def-hcb-datum},
\texttt{def-canonical-corner-identifications}, \texttt{def-compressed-corner} and
\texttt{def-extended-epsilon-cstar-algebra}; the last two are consumed essentially in
the validated closed-corner completeness branch. Downstream, this lemma is one of
```

In WIRING §G3, replace the shard-28 row's “now” cell by:

```text
Overtaken by repo commit 8d0a5061: the defs: line now lists all five. Rewritten to
record those five and to state that the last two are consumed essentially in the
validated closed-corner completeness branch.
```

After those two deletions, §G3's final “No challenge-history metadata was reintroduced anywhere” sentence becomes accurate.

### F2 — MAJOR — WIRING's post-hygiene hash claim does not match the supplied registry

WIRING §E records `b7c4ab7ce44519b0` for
`argument/lemmas/lem-extcb-four-corner-norm.md`. The SHA256-16 of the supplied
`repo-inputs/lem-extcb-four-corner-norm-registry.md` is
`6d5efa199a10a464`. The other 25 §E hashes match their supplied files.

The byte mismatch is substantive, not formatting: supplied registry line 9 still ends
“UNPROVED here pending its own af pass,” while WIRING §I says commit `8d0a5061`
removed that exact tail and that both changed hashes are already recorded. Thus the
claimed post-commit source snapshot and hash-freshness evidence cannot both be true
against this review bundle. A provenance freshness gate would hard-error if §E were
landed with the supplied bytes.

If this supplied bundle is the landing authority, replace the §E row by:

```markdown
| `ARG-LEM-EXTCB-FOUR-CORNER-NORM` | `argument/lemmas/lem-extcb-four-corner-norm.md` | `6d5efa199a10a464` | Registry shard for `lem-extcb-four-corner-norm` |
```

and replace WIRING §I's “Two earlier hygiene caveats are CLOSED” bullet by:

```markdown
- **One earlier hygiene caveat remains OPEN in the supplied registry.** The
  `lem-hcb4-canonical-inverse` `defs:` line contains all five definitions, but
  `lem-extcb-four-corner-norm`'s `provenance:` still ends “UNPROVED here pending its
  own af pass,” contradicting its `proved` / `af: validated` front matter and export.
  Remove that stale tail at landing and then recompute the §E SHA256-16 value; until
  those bytes are supplied, do not claim the post-`8d0a5061` hash-freshness check.
```

If `b7c4ab7ce44519b0` is intended to be the real post-`8d0a5061` hash, provision the
actual post-fix registry shard and rerun the hash check instead; the recorded hash must
not be retained merely on author assertion.

## Passed re-verifications

- `35_extcb.tex` has one section, the complete header, 204 lines, and
  `\label{conj:extcb}`. Its lone `\contractquote` is an exact match. The export contains
  40 validated and 6 archived nodes, all taint clean; the prose follows validated
  replacements for the duplicated archived branches. It reports
  `C_{\mathrm{merge}}(D_0+1)` as the tree's witness and separately attributes the
  expanded `C_{\mathrm{ext}}` expression to the registry body without equating them.
- Shards 26 and 27 contain none of the history metadata rejected by the wave-3 verdict.
  Shard 28 contains no reproduced counterexample or old challenge-count/status block;
  F1 is the sole remaining correction defect in those three shards.
- The 37 reproduced ids in shard 36 are unique and all occur among the 70
  `proved`/`validated` rows. Its 33 table ids are unique and sequence-equal to the
  index-ordered complement. `conj-extcb` is correctly in the reproduced list and not
  the table; `lem-thmainext-conditional` is correctly recorded
  `proved-mod-audit` / `af: none`.
- WIRING §F lists exactly 13 distinct removals, including `conj-extcb`; it retains
  `lem-collateral-import`, `lem-cross-pivot-cancellation`, and
  `lem-import-reduction`. G1 and G2 are factually supported. G3's status/count
  propagation is supported; only F1's extra challenge-history clause fails.
