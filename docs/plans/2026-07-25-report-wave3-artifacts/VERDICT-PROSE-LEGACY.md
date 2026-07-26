VERDICT: 16-VALID/25-reviewed

## Per-shard verdicts

00_overview.tex — VALID-WITH-CORRECTIONS — Counts five listed af-validated blocks as four and calls the `proved-mod-audit` assembly “open.”

01_bridge.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

02_compcb_radial_defect.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

03_compcb_amplification_naturality.tex — VALID-WITH-CORRECTIONS — The proof uses isometry, contrary to its closing claim that continuity suffices.

04_compcb_block_diagonal.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

05_compcb_corner_preservation.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

06_compcb_entrywise_compression_naturality.tex — VALID-WITH-CORRECTIONS — Calls a single-input specialization “strictly sharper” than the equality of maps from which it follows.

07_compcb_defect_transfer.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

08_compcb_inverse_amplification.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

09_compcb_inverse_naturality.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

10_compcb_inverse_compatibility.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

11_compcb_defect_uniformization.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

12_compcb_subspace_inverse_defect.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

13_compcb_matrix_amplification.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

14_compcb_corner_algebra.tex — VALID-WITH-CORRECTIONS — Introduces a non-exhaustive four-item consumer list as exhaustive.

15_compcb_compressed_inverse_identity.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

16_compcb_single_compression_transfer.tex — VALID-WITH-CORRECTIONS — Calls EXT “still-open” although `conj-extcb` is now `proved` with `af: validated`.

17_hcb1_variational_identity.tex — VALID-WITH-CORRECTIONS — Claims a single registry consumer but omits the validated parent `conj-hcb`.

18_hcb1_column_action.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

19_hcb1_row_column.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

20_hcb2_offdiagonal_bound.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

21_hcb3_diagonal_upper_norm.tex — VALID-WITH-CORRECTIONS — Says no result in the document supplies a hypothesis that its own role paragraph later locates in the EXT parent.

22_hcb3_uniform_square_lower.tex — VALID-WITH-CORRECTIONS — Claims a single registry consumer although the current registry has several.

23_hcb3_diagonal_lower_modulus.tex — VALID — Contract, export-derived proof, validated status, and mechanics all agree with ground truth.

24_hcb3_diagonal_inverse.tex — VALID-WITH-CORRECTIONS — Reverses “first” and “second” when identifying its two hypotheses.

## Findings and ready-to-paste corrections

### F1 — MAJOR — `00_overview.tex`

The summary and body say “four” blocks, but the immediately following list has five. Later, “What is open beyond them is the assembly” assigns the inadmissible status “open” to `lem-thmainext-conditional`, whose registry front matter is `status: proved-mod-audit` and `af: none`.

Replace the summary with:

```tex
% SHARD-SUMMARY: Describes the five af-validated blocks reproduced here: the bridge, PRH, the COMP tier, the H-CB tier, and the H-CB-parent/EXT tier.
```

Replace `Four blocks, in dependency order.` with:

```tex
Five blocks, in dependency order.
```

Replace `What is open beyond them is the assembly, whose registry carrier` with:

```tex
What remains below the af-validated rung beyond them is the assembly, whose registry carrier
```

### F2 — MAJOR — `03_compcb_amplification_naturality.tex`

The proof transports the radius condition through `\iota_n` using isometry. Its final sentence instead says that continuity, unitality, and multiplicativity are sufficient; continuity does not preserve the required norm bound.

Replace that sentence with:

```tex
No property of $\iota_n$ beyond isometry, unitality and multiplicativity is used.
```

### F3 — MINOR — `06_compcb_entrywise_compression_naturality.tex`

The role note calls the pointwise identity “strictly sharper” than an equality of maps. It is a specialization of that stronger map equality.

Replace the affected sentence with:

```tex
It is an explicit single-slot specialization of the $\ampl{n}$-clause: that clause identifies two maps, while \eqref{eq:ecn-main} records its value on the single-slot element needed downstream.
```

### F4 — MINOR — `14_compcb_corner_algebra.tex`

“Its registry consumers are” makes the four-item list exhaustive, but current reverse dependencies include additional validated consumers, including both parent results.

Replace:

```tex
Its registry consumers are
```

with:

```tex
Among its registry consumers are
```

### F5 — MAJOR — `16_compcb_single_compression_transfer.tex`

The role paragraph's “still-open EXT” is stale: `conj-extcb` is `proved` with `af: validated`. The broader assembly carrier is instead `proved-mod-audit` with `af: none`.

Replace the final role paragraph with:

```tex
This is the single-compression transfer primitive aimed at compression-based
EXT and Stage-1 assembly, where inclusions have to be pushed through
compressions repeatedly.  The EXT parent \texttt{conj-extcb} is now
\texttt{proved} with \texttt{af: validated}; the broader assembly carrier
\texttt{lem-thmainext-conditional} remains \texttt{proved-mod-audit} with
\texttt{af: none}.  This lemma has no registry consumers.
```

### F6 — MINOR — `17_hcb1_variational_identity.tex`

The role paragraph says there is one consumer. Current registry reverse dependencies also include the validated parent `conj-hcb`.

Replace the consumer sentence with:

```tex
Its registry consumers are \texttt{lem-hcb1-column-action}
(\S\ref{sec:hcb1-column-action}), where it is combined with
\texttt{lem-hcb1-combo-bound}, and the parent \texttt{conj-hcb}
(\S\ref{sec:hcb}).
```

### F7 — MAJOR — `21_hcb3_diagonal_upper_norm.tex`

The role paragraph first says that nothing in the document supplies the level-one lower-modulus hypothesis, then says that the conditional hypotheses are supplied inside `\S\ref{sec:extcb}`. Those assertions cannot both stand.

Replace:

```tex
a hypothesis nothing in this document supplies,
```

with:

```tex
a hypothesis supplied only inside \S\ref{sec:extcb},
```

### F8 — MINOR — `22_hcb3_uniform_square_lower.tex`

“Its single registry consumer” is stale; the current registry records multiple consumers, including parent and downstream H-CB/EXT results.

Replace:

```tex
Its single registry consumer is
```

with:

```tex
Its registry consumers include
```

### F9 — MINOR — `24_hcb3_diagonal_inverse.tex`

The theorem lists the lower-modulus premise first and bijectivity second, but the proof calls bijectivity the “first hypothesis” and lower modulus the “second hypothesis.” The proof mathematics itself matches the export.

Replace:

```tex
This step uses the \emph{first hypothesis}---bijectivity---and nothing else.
```

with:

```tex
This step uses the \emph{bijectivity} hypothesis and nothing else.
```

Replace:

```tex
and the second hypothesis is at least
```

with:

```tex
and the level-one lower-modulus hypothesis is at least
```

## Batch-wide checks

All 24 result-bearing shards reproduce their registry `contract:` line byte-for-byte. All 24 are `status: proved` with `af: validated`, and their result-status prose agrees. Every shard has one section, the required header fields, no more than 280 lines, correct transformed labels, and only macros defined by `main.tex` or standard LaTeX. A compilation check of all 25 supplied shards found no undefined control sequences; cross-references to the explicitly out-of-scope shards 25–36 remain unresolved only because those files are absent from this review batch.
