VERDICT: 7-VALID/11-total

25_hcb3_offdiagonal_inverse.tex: VALID — contract byte-match, proof trace, status, and mechanics all pass.
26_hcb4_canonical_gram.tex: VALID-WITH-CORRECTIONS — the proof is faithful, but the status paragraph adds unsupported amendment/challenge metadata.
27_hcb4_canonical_closeness.tex: VALID-WITH-CORRECTIONS — the proof is faithful, but the status paragraph adds unsupported amendment/challenge metadata.
28_hcb4_canonical_inverse.tex: INVALID — the “Corrections of record” inserts mathematical counterexamples and challenge history absent from both admissible ground-truth files.
29_hcb.tex: VALID — the amended conditional contract and the clause-by-clause aggregation match the registry and export.
30_extcb_one_dimensional_corners.tex: VALID — both contracts byte-match and both proofs follow their exports without added mathematics.
31_extcb_corner_dimension_additivity.tex: VALID — the binary splitting, adjoint transport, and finite inductions faithfully compress the export.
32_extcb1_dimension_selection.tex: VALID — both contracts and the close-range/rank/additivity arguments are traceable to validated nodes.
33_extcb_four_corner_norm.tex: VALID — block conditioning, the sixteen-term square defect, and the scalar bootstrap match the export.
34_extcb_four_corner_merge.tex: VALID — the total-defect amendment, coverage argument, and counterexample are all present in the validated export.
35_status_outlook.tex: INVALID — its global counts and off-route status table are not supported by the registry files supplied as ground truth.

## Batch-wide checks

- Statement fidelity: all 12 `\contractquote` payloads are literal byte-matches to their respective registry `contract:` lines.
- Mechanics: every shard has exactly one `\section`, a complete SHARD-ID/TITLE/SUMMARY/KEYWORDS header, no more than 280 lines, and the required first-hyphen-to-colon claim labels. The 11 shards also compile against the supplied `main.tex` preamble without an undefined command.
- Status containment: `conj-extcb` appears only as an explicitly pending `proved-mod-audit`/`af: seeded` consumer and is never rendered as a theorem.

## Findings and ready-to-paste corrections

### F1 — MAJOR — shard 28 contains proof-like mathematics outside the validated export

Lines 104–120 give two explicit `c_{00}` counterexamples and a three-challenge repair narrative. Neither counterexample, the three-challenge count, nor that history occurs in `lem-hcb4-canonical-inverse-export.md` or its registry shard. The export validates the closed-corner completeness branch itself, not these editorial demonstrations. Lines 126–127 repeat unsupported counts of definitions, challenges, resolutions, and amendments. The header summary/keywords also advertise that unsupported history.

Ready-to-paste correction:

```latex
% SHARD-SUMMARY: Explains the canonical inverse bound, the quantitative Neumann step, and the closed-corner completeness branch required for the Banach target.
% SHARD-KEYWORDS: lem-hcb4-canonical-inverse, af validated, Neumann series, complete bijectivity, Banach target, closed corner
```

Delete the entire `\textbf{Corrections of record.}` block. Replace the status paragraph by:

```latex
\noindent\textbf{Status.} \texttt{proved}; \texttt{af: validated} (T0). Workspace
\texttt{proofs/lem-hcb4-canonical-inverse}: 19 nodes, all \texttt{validated}, root
\texttt{validated}, taint clean. Six of the nineteen exported nodes form the completeness
branch.
```

### F2 — MINOR — shard 26 asserts unevidenced workspace history

The export and registry support 9/9 validated nodes, a validated root, and clean taint. They do not state “twelve registered definitions,” “four prover amendments,” or “no challenge.” Those author-side ledger claims are inadmissible here.

Replace lines 104–108 by:

```latex
\noindent\textbf{Status.} \texttt{proved}; \texttt{af: validated} (T0). Workspace
\texttt{proofs/lem-hcb4-canonical-gram}: 9 nodes, all \texttt{validated}, root
\texttt{validated}, taint clean.
```

### F3 — MINOR — shard 27 asserts unevidenced workspace history

The export and registry support 11/11 validated nodes, a validated root, and clean taint. They do not support the definition count, “no node amendment,” “no challenge,” or the comparison with three challenges in shard 28.

Replace lines 107–111 by:

```latex
\noindent\textbf{Status.} \texttt{proved}; \texttt{af: validated} (T0). Workspace
\texttt{proofs/lem-hcb4-canonical-closeness}: 11 nodes, all \texttt{validated}, root
\texttt{validated}, taint clean.
```

### F4 — MAJOR — shard 35 presents an unprovisioned global status ledger as fact

The supplied ground truth contains 12 registry shards, all `proved`/`af: validated`. It contains no registry shards for most of the claimed 36 reproduced results, the asserted total of 69, the 30 rows in the deprecation table, or the three additional off-route results invoked by WIRING to close the arithmetic. The arithmetic `36+30+3=69` is internally consistent but is not registry evidence. Because AUTHOR-NOTES and WIRING are author claims, they cannot validate this status section.

Replace the opening status inventory with this scoped paragraph:

```latex
The eleven prose shards in this verification batch reproduce twelve supplied registry
results, each \texttt{proved} with \texttt{af: validated}:
\texttt{lem-hcb3-offdiagonal-inverse},
\texttt{lem-hcb4-canonical-gram},
\texttt{lem-hcb4-canonical-closeness},
\texttt{lem-hcb4-canonical-inverse},
\texttt{conj-hcb},
\texttt{lem-extcb-one-dimensional-product},
\texttt{lem-extcb-one-dimensional-corner-dimension},
\texttt{lem-extcb-corner-dimension-additivity},
\texttt{lem-extcb1-close-corner-dimension},
\texttt{lem-extcb1-cross-corner-dimension},
\texttt{lem-extcb-four-corner-norm}, and
\texttt{lem-extcb-four-corner-merge}.
No global registry total or status for off-route results is asserted here because the
corresponding registry shards were not included in the supplied ground truth.
```

Replace the entire “Results removed from the previous report” body, including the 30-row table and its trailing status paragraph, by:

```latex
The route-pivot inventory is not reproduced in this reviewed shard because the
corresponding registry shards were not included in the verification bundle. No status
claim about those omitted rows is made here.
```

Alternatively, provision all 57 omitted registry shards and rerun the status audit; author inventory alone is not a correction.

## WIRING §G1/§G2 adjudication

### §G1 — VALID

All ten replacement rows across the nine existing files are factually aligned with the supplied registries/exports and the brief’s pending-only rule for `conj-extcb`:

- `conj-hcb`, `lem-hcb3-offdiagonal-inverse`, and the hcb4 trio are `proved`/`af: validated`.
- The dependency claims in shards 10, 15, 18, 19, 20, 23, and 24 agree with the relevant `deps:` lines and export uses.
- The repaired text preserves the unsupplied hypotheses on the conditional lower-modulus/inverse clauses and does not promote `conj-extcb`.

### §G2 — VALID-WITH-CORRECTIONS

The two shard-29 changes are correct: the canonical-tier target is now present, and `conj-hcb`’s registry records sixteen validated dependencies. Adding the three supplied hcb4 results makes the local enumerated report count rise from 33 to 36. The final shard-35 replacement is not admissible as written, however: “the balance” of a global total of 69 being validated off-route material relies on 33 registry shards absent from `repo-inputs/`.

Ready-to-paste replacement for that G2 row:

```text
Every supplied live H-CB registry result introduced in waves 3/3b is reproduced here.
No global registry total or off-route status split is asserted without the corresponding
registry shards in the verification bundle.
```
