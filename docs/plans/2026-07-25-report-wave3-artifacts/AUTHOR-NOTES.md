# AUTHOR-NOTES — report wave 3

Written by the author, for the hostile reviewer (bead `aism-h0mp`) and the landing session. Every
statement below is a fact about the sources (`argument/lemmas/<id>.md`, `proofs/<id>/export.md`) or a
declared authoring decision. Nothing here is mathematics of mine.

**Method.** Statement = the registry `contract`, typeset, with the ASCII original reproduced verbatim
underneath via `\contractquote`. Proof = a narrative compression of the validated tree, in tree order,
citing validated children by registry id where the export cites them and inlining them where the export
proves them in-workspace. No step was re-derived independently and no constant was improved.

**Skips.** `conj-extcb` — `proofs/conj-extcb/export.md` does not exist (workspace `af: seeded`,
registry `proved-mod-audit`, elevation live). It is **not** written up; it appears in four shards
(`26`, `29`, `31`, `32`) only as the pending consumer, always tagged. No other target was skipped:
all nine remaining targets have exports.
> **SUPERSEDED by wave 3c (2026-07-26).** `conj-extcb` was `af`-validated and banked after wave 3b;
> the export now exists and the parent is written up as `35_extcb.tex`. Shard numbers in this wave-3
> section are the pre-3b ones; the current map is the table at the top of `WIRING.md`.

---

## Per target

### `lem-hcb3-offdiagonal-inverse` → `25_hcb3_offdiagonal_inverse.tex`
- **Tree:** 16 nodes (root; 1.1+1 child; 1.2+2; 1.3+2 with 4 grandchildren; 1.4+2). Depth 4.
- **Cited children:** `lem-hcb2-product-defect` (1.3.1), `lem-hcb2-amplified-adjointness` (1.3.1),
  `lem-hcb3-diagonal-lower-modulus` (1.3.2, 1.3.2.1). Workspace externals named as such: the
  compressed-product display, the $\ecs$-Banach/$C^*$ norm axioms.
- **Inlined:** node 1.2.1's amplified compression identification $\Co{p}{q}=\ampl{n}\Co{P}{Q}$ (the tree
  re-derives it from the $\theta$ power series rather than citing
  `lem-compcb-amplified-compression`), and the whole constant ledger 1.1/1.1.1.
- **FLAG (deps vs tree).** The registry `deps` list six lemmas; the exported tree visibly consumes
  three. `lem-compcb-corner-algebra`, `lem-hcb3-uniform-square-lower` and `lem-hcb3-diagonal-inverse`
  do not appear in the export text. I said so in the shard's *Role in the chain* (house style
  elsewhere lists all registry imports silently; here the mismatch is large enough to state).
- **FLAG (near-miss citation).** Node 1.2 proves a *rectangular* square estimate
  $\nrm{Z\dg\cpr Z}\ge(1-B\comb)\nrm{Z}^{2}$ that looks like `lem-hcb3-uniform-square-lower` but is not
  it (that lemma is diagonal). The prose says this explicitly so the reviewer does not read a
  mis-citation.

### `conj-hcb` → `26_hcb.tex`
- **Tree:** 11 nodes, all depth 1 (root + 1.1 ledger + 1.2-1.9 one clause each + 1.10 uniformity).
  Pure aggregation; no analysis.
- **Cited children:** the eight suppliers named in node 1.1
  (`lem-hcb2-amplified-adjointness`, `lem-hcb2-product-defect`, `lem-hcb3-diagonal-unit`,
  `lem-hcb3-diagonal-upper-norm`, `lem-hcb3-diagonal-lower-modulus`, `lem-hcb3-diagonal-inverse`,
  `lem-hcb3-offdiagonal-inverse`, `lem-hcb4-canonical-closeness`). **Inlined:** nothing.
- **FLAG (16 deps, 8 citations).** The registry lists sixteen dependencies; the tree cites eight. The
  shard says "the exported tree cites eight of them directly, the others entering through those eight",
  which is a description of the two documents, not an inference of mine.
- **FLAG (two constant ledgers).** The registry *body* records the paper-proof witnesses $C_H=4000c$,
  $\comb_H=1/(10000c)$; the *tree* derives $C_H=\max\{\dots\}$, $\comb_H=\min\{\dots\}$. The prose
  follows the tree and attributes the other pair explicitly to the registry body. If the reviewer
  prefers, the sentence can be dropped without touching the proof.
- **Environment choice.** `kind: lemma` in the registry, so `\begin{lemma}`, matching all 24 existing
  shards, even though this is a tier parent. Promoting it to `theorem` is cosmetic; the amsthm counter
  is shared.
- **Label.** `\label{conj:hcb}`, **not** `lem:hcb` — `check-provenance.py:labels_of` anchors an id by
  its first-hyphen-to-colon transform. See WIRING §E.
- **Compression friction.** The contract is one 200-word sentence with three trailing conditionals. I
  typeset it as a lead clause plus a three-item `enumerate`; the byte-verbatim ASCII sits underneath, so
  the reviewer can check the split without reconstructing it.

### `lem-extcb-one-dimensional-product` → `27_extcb_one_dimensional_corners.tex` (Lemma, first)
- **Tree:** 25 nodes, depth 4 (1.1 ledger with 4 children and 3 grandchildren; 1.2 scalarisation +3;
  1.3 squared comparison +4 with 3 grandchildren; 1.4 assembly +2 +1 qed).
- **Cited children:** `lem-compcb-corner-algebra` (unit axiom on $\Cnrs{Q}$); the registered
  one-dimensional$\Rightarrow$nonvanishing bridge; the compressed-product display and $\ecs$-$C^*$
  axioms as workspace externals.
- **Inlined:** all of 1.1 (one paragraph), all three sub-estimates of 1.3 (one paragraph, three
  sentences), the degenerate case 1.4.2.
- **Constant map for the reviewer:** my $C_0$ = the export's `C0` (= $\max\{C_{ca},C_{dot},C_L,1\}$),
  $C_1$ = `C1`, $C_h$ = `C_h`, $C_2=C_3+C_4+C_5$ = `C2` = $C_{PQR}$. Intermediate constants
  `B`, `t0`, `C_uQ`, `C_QY`, `C_as`, `C_a`, `C_u` are absorbed into $O(\comb)$ statements; none carries
  information the statement uses.

### `lem-extcb-one-dimensional-corner-dimension` → same shard (Lemma, second)
- **Tree:** 8 nodes, depth 3. Narrated essentially 1:1; nothing was dropped.
- **Cited:** the product lemma above (node 1.1.2) and `def-one-dimensional-delta-projection`.
- **Index subtlety made explicit.** The product lemma needs its *middle* index one-dimensional; node
  1.1.2 applies it to the triple $(Q,P,Q)$, i.e. with middle $P$. The prose states this, because the
  root hypothesis ("$P$ **and** $Q$ one-dimensional") is otherwise easy to read as redundant.

### `lem-extcb-corner-dimension-additivity` → `28_extcb_corner_dimension_additivity.tex`
- **Tree:** 39 nodes, depth 6 — the largest in the set.
- **Cited:** `def-projection-basis`, `def-extended-delta-inclusion`, `def-compressed-corner`. The two
  registry deps (`lem-compcb-corner-algebra`, `lem-hcb3-uniform-square-lower`) are declared but not
  visibly consumed in the export text.
- **FLAG (the tree proves the same calculus twice).** Nodes 1.2.1-1.2.4 prove the abstract binary
  splitting lemma; nodes 1.5.1.1-1.5.1.4 prove it *again*, inline, for the specific first-index split
  $R_0=P_{[1,j-1]},R_1=P_j$. My prose states it once, abstractly, and then instantiates. This is the one
  place where a 1:1 diff against the export will not line up, and it is deliberate.
- **FLAG (repair children).** 1.4.2.2.1, 1.5.1.5.1/2, and the "direct discharge" pattern generally, are
  re-derivations that avoid a then-pending sibling. I record their existence in the Status paragraph
  and do not narrate them as mathematics.
- **FLAG (what is *not* claimed).** The conclusion is a linear bijection with bounded inverse; the tree
  does **not** track a bound uniform in the number of blocks (the inductions compose $p+q$ bijections).
  The universal *threshold* is uniform; the composite *norms* are not asserted to be. I put this in the
  transcription note rather than letting "linearly bijective" be read as "uniformly bounded".

### `lem-extcb1-close-corner-dimension` → `29_extcb1_dimension_selection.tex` (Lemma, first)
- **Tree:** 16 nodes, depth 4.
- **Cited:** `lem-compcb-corner-algebra` (unit of $\Cnrs{P}$),
  `lem-compcb-amplified-compression-identities` at $n=1$ (idempotence of both compressions),
  `def-compressed-corner`, `def-delta-projection`.
- **Inlined:** the close-idempotent range lemma (1.3, 1.3.1, 1.3.2) — stated and proved in prose, since
  it is three lines and is used again in the second lemma in a weaker form; and the "explicit
  prerequisite assembly" children 1.2.2.1/1.2.2.2, which re-derive node 1.1's constants without
  invoking it.
- **Note.** Two *different* close-idempotent lemmas appear in this wave: the strong one here
  ($\nrm{E-F}(2M+1)<1$, transports ranges by an invertible $W$) and the weak one in the cross-corner
  tree ($\nrm{E-F}<1$, equal ranks). I kept both, in their own places, rather than unifying them.

### `lem-extcb1-cross-corner-dimension` → same shard (Lemma, second)
- **Tree:** 30 nodes, depth 5.
- **Cited:** `lem-extcb-one-dimensional-corner-dimension`, `lem-extcb-corner-dimension-additivity`,
  `lem-extcb1-close-corner-dimension`, `lem-compcb-corner-algebra`, `def-projection-basis`,
  `def-extcb-datum`, `def-one-dimensional-delta-projection`.
- **Inlined:** the four sub-estimates of node 1.2.2 (Hermitian projection control, subordination,
  transported-source comparison, compression-vs-multiplication), compressed to one sentence each.
- **FLAG (four redundant discharges).** Nodes 1.3.3.1, 1.3.3.2, 1.3.3.3 and 1.3.3.3.1 all prove
  $\dim\Cnr{v(I_r)}{Q}=r\,d$, differing only in which pending sibling they route around. The prose
  proves it once.
- **FLAG (a definition carrying a fact).** The step "equivalence of one-dimensional
  $\dproj$-projections is transitive" is consumed from `def-one-dimensional-delta-projection`, whose
  byte-verbatim source text asserts it and attributes it to the source's `lem_PQR` — i.e. to
  `lem-extcb-one-dimensional-product` (§27). The prose names that route explicitly instead of treating
  transitivity as a bare definitional given.

### `lem-extcb-four-corner-norm` → `30_extcb_four_corner_norm.tex`
- **Tree:** 18 nodes, depth 5.
- **Cited:** `def-four-corner-merging-datum`, `def-compressed-corner`,
  `def-extended-epsilon-cstar-algebra` and the operator-space (Ruan) axioms. The two registry deps are
  declared but not visibly consumed.
- **Inlined:** amplification naturality (1.1.2.1) — again re-proved in-workspace rather than cited from
  the COMP tier; the mismatched-corner kill estimate (1.1.2.2) with its explicit associator count; the
  sixteen-term expansion (1.2.2/1.2.2.1).
- **Numeric constants kept:** $\nrm{p_j}\le2$, $\nrm{p_jp_l}\le4\comb$, $\nrm{\beta\alpha-I}\le3L_c\comb$,
  $c_{\mathrm{blk}}=1/(16M_c)$, $B_{\mathrm{blk}}=5$, $D_{\mathrm{sq}}=8(4+2c_c+2K_{\mathrm{inc}})$,
  $K_{\mathrm{norm}}=\max\{25+D_{\mathrm{sq}},(25+D_{\mathrm{sq}})/c_{\mathrm{blk}}\}$. Dropped:
  $q=1+\ecs\le5/4$ and the per-associator $16q^{3}\ecs$ bookkeeping of 1.2.1.1.
- **Registry hygiene FLAG (not fixed here).** `argument/lemmas/lem-extcb-four-corner-norm.md` carries
  `status: proved` / `af: validated`, but its `provenance:` field still ends "UNPROVED here pending its
  own af pass". The shard body is correct; the field is stale. Landing-session fix, not a report issue.

### `lem-extcb-four-corner-merge` → `31_extcb_four_corner_merge.tex`
- **Tree:** 26 statements = 22 `validated` + 4 `archived` (1.1.2.1, 1.2.3.1, 1.5.2.1, 1.7.1 — all
  dependency-gated duplicates superseded by children that discharge the same step from validated
  material). Depth 4.
- **Cited:** `lem-extcb-four-corner-norm` (node 1.4/1.4.1), `def-four-corner-merging-datum`,
  `def-extended-delta-inclusion`, `def-compressed-corner`.
- **Inlined:** the corner-product separation (1.2.x), the sixteen-term multiplicative expansion (1.3.1),
  the coverage estimate (1.5.1/1.5.1.1) and the Neumann discharge (1.5.2).
- **Reproduced nearly in full:** the counterexample of node 1.7.2 ($\mathcal A=\mathbb C^{3}$ with
  $(a,b,c)(a',b',c')=(aa',bb',0)$, $\rho=0$, $\ecs=1$). It is a refutation of record and the reason the
  contract was amended, so it gets its own paragraph rather than a mention — the same treatment
  §24 gives the $\mathbb C\oplus\mathbb C$ counterexample.
- **FLAG (workspace definition alias).** Nodes 1.1.2.2, 1.2.2.1 and 1.5.1.1 cite
  `def-four-corner-merging-datum-2026-07-25-amended`, described there as "an exact workspace snapshot of
  the current canonical `def-four-corner-merging-datum`". The prose cites only the canonical registry
  definition, since the alias is a provisioning artifact of the run. Declared here so the reviewer sees
  the substitution was deliberate.

---

## Macros

Every shard uses only commands already defined in `report/main.tex`. Two notations were written
longhand; I propose, but did **not** add, the following (a preamble change is a separate, reviewed act):

- `\Jcan{P}{Q}{n}` for the canonical corner identification $J_{P,Q,n}$
  (`def-canonical-corner-identifications`), used in `26_hcb.tex` and needed by any future hcb4 shard,
  which will use it heavily. Suggested: `\newcommand{\Jcan}[3]{J_{#1,#2,#3}}`.
- A semantic name for the four-corner datum's common defect, currently plain `\rho`. `CONVENTIONS.md`
  §(c) already uses $\rho$ for the signed-geometry scale $4\tsq$; the two are unrelated. I added a
  transcription note in `30` and used $\rho$ only inside the EXT shards, but a macro (e.g.
  `\newcommand{\mdefect}{\rho}`) would remove the collision permanently if more EXT material is written.

No other macro was wanted. `\bigoplus`, `\dim`, `\rank`, `\Img`, `\Ker`, `\sgn` are all available
(the last four via `main.tex`'s `\DeclareMathOperator` block).

## Build evidence

`pdflatex` twice, in the scratchpad, against the real `main.tex` preamble plus the 25 existing shards
and all 8 new ones: 33 includes, exit 0, **0 warnings, 0 undefined references**. Isolated build of the
7 new lemma shards alone: exit 0, the only undefined references being the deliberate `\S\ref`s into
existing sections (`sec:hcb2-amplified-adjointness`, `sec:hcb3-diagonal-unit`,
`sec:hcb3-diagonal-inverse`), all of which exist in `report/sections/`.

---

# AUTHOR-NOTES — report wave 3b (the hcb4 canonical layer)

Second author, same session, same read-only constraint (a live `af` orchestration; no repo path was
created, edited or deleted). Same method as wave 3: statement = the registry `contract`, typeset, with
the ASCII original byte-verbatim underneath via `\contractquote`; proof = a narrative compression of
the validated tree in tree order, citing validated children where the export cites them and inlining
them where the export proves them in-workspace. **No step was re-derived independently, no constant was
improved, no status was promoted.** The three targets were already `proved`/`af: validated` before this
wave; writing them up changes nothing on the rigour ladder. `conj-extcb` is not mentioned in any of the
three new shards.

**Renumbering.** Wave 3's §I plan was executed: `26/27/28 = hcb4-{gram,closeness,inverse}`,
`29 = hcb`, `30-34 = EXT`, `35 = status-outlook`. Seven of the predecessor's files were renamed and
their `% SHARD-ID:` lines retargeted; two of them (`29_hcb.tex`, `35_status_outlook.tex`) also needed
prose repairs, because they described the trio as validated-but-not-reproduced. Those repairs are
already applied here and are itemised in WIRING §G2.

**Skips.** None. All three targets have exports (110/134/230 lines).

---

## Per target

### `lem-hcb4-canonical-gram` → `26_hcb4_canonical_gram.tex`
- **Tree:** 9 nodes, depth 4 (root; 1.1 column case with 1.1.1, 1.1.2 + two children, 1.1.3;
  1.2 row transfer + 1.2.1). Ledger: 12 registered definitions, 4 prover amendments before
  validation, **0 challenges**.
- **Cited children:** `lem-compcb-rectangular-product` (1.1.2.1),
  `lem-compcb-compressed-unit-norm` (1.1.2.2). Named as workspace externals rather than lemmas: the
  column-Hilbert inner-product displays, the compressed-product display, the operator-space
  matrix-norm axioms (Ruan scalar-tensor invariance), the $\varepsilon$-Banach $C^*$ norm axioms, and
  the one-dimensional$\Rightarrow$nonvanishing bridge.
- **Inlined:** node 1.1.3 in full (one paragraph), and node 1.2.1 folded into 1.2 — the row case is
  three sentences and separating it would have produced a two-sentence display.
- **Constant map for the reviewer:** my $A$ = the export's `A` = $C_r+1$; $B$ = `B` = $C_u$;
  $C_{\mathrm{col}}=A+B$ = `C_col`, and $C_J=C_{\mathrm{col}}$, $\comb_J=\comb_{\mathrm{col}}$.
- **FLAG (deps vs tree).** Four registry `deps`; the exported tree visibly consumes two.
  `lem-compcb-corner-algebra` and `lem-hcb3-uniform-square-lower` do not appear in the export text. I
  said so in *Role in the chain*, following the wave-3 precedent for large mismatches.
- **Compression-resistant point.** The scalar passage is asymmetric: the thresholds give
  $x^{2}\ge1-(A+B)\comb$ but only $x^{2}\le1+2(A+B)\comb$, and the factor $2$ is absorbed by using
  $\sqrt{1-t}\ge1-t$ on one side and $\sqrt{1+t}\le1+t/2$ on the other. Dropping either inequality
  makes the symmetric conclusion look unmotivated, so both are stated and the asymmetry is named.
- **Norm-collision point.** The two sides of the conclusion carry *different* norms (ambient
  operator-space vs Euclidean operator norm). The contract writes both as `||.||`. I put this in the
  transcription note, because a reader who reads them as the same norm will read the lemma as a
  triviality about a bijection rather than as the statement that the canonical identification is a
  $1\pm O(\comb)$ isometry.

### `lem-hcb4-canonical-closeness` → `27_hcb4_canonical_closeness.tex`
- **Tree:** 11 nodes, depth 3 (1.1 + three children; 1.2 + three children; 1.3 + one). Ledger: 12
  registered definitions, **0 amendments and 0 challenges** — a clean first pass, and the only one of
  the three.
- **Cited children:** `lem-compcb-corner-algebra` (1.1.1),
  `lem-hcb-column-hilbert-squared` at $n=1$ (1.1.2), `lem-hcb2-amplified-adjointness` (1.2.1 and
  1.3.1), `lem-hcb1-column-action` (1.2.1), `lem-hcb4-canonical-gram` (1.2.2). Workspace externals:
  the column-Hilbert inner-product displays, the $\varepsilon$-Banach $C^*$ norm axioms, the
  nonvanishing bridge.
- **Inlined:** node 1.1.3 folded into the normalisation paragraph; node 1.3.1 folded into 1.3.
- **Constant map:** $A=2C_{\mathrm{col}}+C_{\mathrm{ca}}$ = the export's `A`;
  $C_{*}=C_{\mathrm{act}}+2A$ = `C_*` = $C_{\mathrm{sp}}$.
- **FLAG (deps vs tree).** Six registry `deps`, five visibly consumed;
  `lem-hcb3-uniform-square-lower` is declared and does not appear in the export text.
- **A step I refused to paraphrase.** Node 1.2.2's "under the canonical identification by $q_0$ this
  vector is $\alpha d$, whereas $J_{P,Q,n}(Z)\dg X$ is $d$" is reproduced almost verbatim. It is a
  change of coordinates, not an estimate, and a looser paraphrase would let the reader take
  $\lvert\alpha-1\rvert$ for an approximation error introduced here rather than the single scalar the
  whole lemma is about.
- **One threshold made explicit.** The export writes $C_{*}=C_{\mathrm{act}}+2A$ without saying where
  the $2$ comes from; it is the bound $A\comb(1+C_J\comb)\le2A\comb$, valid once
  $\comb\le1/\max\{C_J,1\}$ — a threshold the export does list. I stated the implication rather than
  leaving the coefficient unexplained.

### `lem-hcb4-canonical-inverse` → `28_hcb4_canonical_inverse.tex`
- **Tree:** 19 nodes, depth 6 (the deepest are 1.2.2.1.1.1 and 1.2.2.1.1.2). Ledger: 13 registered
  definitions, **3 challenges raised and 3 resolved**, 3 node amendments. Six of the nineteen nodes
  are the completeness branch alone.
- **Cited children:** `lem-hcb4-canonical-gram` (1.1.2 and 1.2.2.1.2),
  `lem-hcb4-canonical-closeness` (1.3.1); definitions `def-canonical-corner-identifications`,
  `def-ha-map`, `def-compressed-corner` (1.2.2.1.1.1), `def-extended-epsilon-cstar-algebra`
  (1.2.2.1.1.2).
- **Inlined:** the whole Neumann sub-tree 1.2.1/1.2.2/1.2.2.2/1.2.3 into one paragraph; the
  completeness branch 1.2.2.1 with its five descendants into one paragraph; 1.3.1--1.3.3 into the
  assembly paragraph.
- **Reproduced nearly in full:** the three challenges, as a *Corrections of record* paragraph — the
  $c_{00}$/$\ell^{1}$ right-shift counterexample to the unqualified Neumann step, the
  $c_{00}$/$\ell^{2}$ counterexample to inferring completeness from an inner-product display, and the
  unregistered-axiom objection. This follows the treatment §34 gives the $\mathbb C^{3}$
  counterexample: they are refutations of record and the reason six nodes exist.
- **FLAG (deps vs tree).** Four registry `deps`, two visibly consumed.
- **FLAG (registry `defs` gap; landing-session fix, not a report issue).** The validated tree consumes
  `def-compressed-corner` and `def-extended-epsilon-cstar-algebra` essentially, but the registry
  shard's `defs:` line lists only `def-ha-map; def-hcb-datum; def-canonical-corner-identifications`.
  The third challenge is precisely about this, and its resolution was to provision the definition *in
  the workspace* — which does not propagate back to the shard. Stated in the shard's *Role in the
  chain* and in WIRING §I.
- **FLAG (what the three challenges were, exactly).** Two are mathematical (a gap in the Neumann step;
  a false inference from an inner-product display) and one is a provisioning objection with
  `target: dependencies`. I described them that way rather than as "three errors", because the third
  did not claim the argument was wrong.
- **Nothing about the contract changed.** Unlike `conj-hcb` (§29) and `lem-extcb-four-corner-merge`
  (§34), no contract amendment was made here: the challenges hit proof steps only. The shard says so
  explicitly, so the reviewer does not go looking for an amendment.

---

## Macros (wave 3b)

No new macro is needed and none is proposed as necessary. The three shards use only commands already
in `report/main.tex`; the canonical maps are written longhand as $J_{P,Q,n}$, $J_{Q,P,n}$, $J_n$
(about twenty occurrences across the three files). Wave 3's `\Jcan{P}{Q}{n}` proposal therefore
remains *open and unadopted* — deliberately, since a preamble change is a separate reviewed act and
adopting it would make the landing depend on an edit to `main.tex`. If a later wave adds more
canonical-tier material, adopting `\newcommand{\Jcan}[3]{J_{#1,#2,#3}}` and rewriting these three
shards is a mechanical, gate-checkable change.

## Build evidence (wave 3b)

- `pdflatex` twice, in the scratchpad, against the real `main.tex` preamble plus the 25 repo shards
  `00-24` and all 11 shards of this directory: **36 includes, exit 0, 74 pages, 0 LaTeX warnings, 0
  undefined references, no rerun requested.**
- Contract byte-match script over this directory: **12/12** `\contractquote` arguments are
  byte-identical to exactly one `argument/lemmas/*.md` `contract:` line.
- The **real** `scripts/check-report-shards.sh`, run unmodified against a simulated `report/` tree
  built from these shards plus the WIRING §C/§D tables: `36 shards included, labeled, cataloged, all
  <= 280 lines`, exit 0. Red→green confirmed twice (bad `SHARD-ID` prefix; deleted `SHARD-SUMMARY`).
- Per-shard: exactly one `\section` and one `\label{sec:...}` each; 123/125/144 lines for the three
  new shards, all under the ~200 target.

---

# AUTHOR-NOTES — report wave 3c (the EXT parent `conj-extcb`)

Third author, read-only on the repo. Between wave 3b and this wave `conj-extcb` was `af`-VALIDATED and
banked: `argument/lemmas/conj-extcb.md` front matter now reads `status: proved` / `af: validated`,
`proofs/conj-extcb/export.md` exists (554 lines, 46 nodes), and `argument/INDEX.md` records 70
`proved`/`validated` rows. Same method as waves 3/3b: statement = the registry `contract`, typeset,
with the ASCII original byte-verbatim underneath via `\contractquote`; proof = a narrative compression
of the validated tree in tree order, citing validated children where the export cites them and
inlining them where the export proves them in-workspace. **No step was re-derived independently, no
constant was improved, and no status was promoted** — writing up an already-banked result changes
nothing on the rigour ladder.

**Three jobs.** (1) author `35_extcb.tex`; (2) propagate the recorded status through every existing
shard that called `conj-extcb` pending/seeded/`proved-mod-audit`; (3) recount `36_status_outlook.tex`
against the current index. Renumbering: status/outlook `35 -> 36`.

## Per target

### `conj-extcb` → `35_extcb.tex`

- **Tree:** 46 statements = **40 `validated` + 6 `archived`**, all taint clean, root `validated`.
  Depth 6 below the root (the deepest is `1.5.2.2.1.2.2`). The archived nodes are
  `1.3.1.1.1`, `1.5.2.2.1.1`, `1.5.2.2.1.2.1`, `1.5.2.2.1.3`, `1.5.3.1`, `1.5.3.2` — every one a
  dependency-gated duplicate superseded by a sibling that discharges the same step from validated
  material only. **They are not part of the validated spine**; I narrate none of them as mathematics
  and say so in the Status paragraph.
- **Cited children (in the export text):** `conj-hcb` (9 uses — nodes 1.3, 1.3.1, 1.4, 1.4.1, 1.4.2,
  1.5, 1.5.2, 1.5.2.2, 1.5.3), `lem-extcb1-cross-corner-dimension` (node 1.1),
  `lem-extcb-four-corner-merge` and `lem-extcb-four-corner-norm` (node 1.6). Definitions:
  `def-extcb-datum`, `def-extended-delta-inclusion`, `def-four-corner-merging-datum`.
- **Inlined:** the whole exact-target correction sub-tree (1.2, 1.2.1, 1.2.2, 1.2.3, 1.2.3.1,
  1.2.3.1.1) into three paragraphs; the endpoint case split (1.3.1, 1.3.1.1, 1.3.1.1.2) into two
  sentences; the spatiality argument (1.3.2) into one; the ordered inverse triggers (1.4.1, 1.4.2)
  into one paragraph; the whole `1.5` merging-datum family into one paragraph.
- **FLAG (the tree proves the same three steps many times over).** `1.5.1.1`, `1.5.1.1.1`,
  `1.5.1.1.1.1`, `1.5.1.1.1.2`, `1.5.1.1.1.3` all establish the same comparison + exact involution;
  `1.5.2.2.1`, `1.5.2.2.1.2`, `1.5.2.2.1.2.2` the same product estimate; `1.5.3.1.1`, `1.5.3.1.1.1`,
  `1.5.3.1.2`, `1.5.3.1.2.1`, `1.5.3.1.3`, `1.5.3.3` the same units/norms/bijectivity bridge; and
  `1.5.3.2.1` + `1.5.3.4` the same final assembly. They differ only in which pending sibling they
  route around. **My prose proves each once.** This is the one place a 1:1 diff against the export
  will not line up, and it is deliberate — it is also why 40 validated nodes compress to 204 lines.
- **FLAG (deps vs tree).** Ten registry `deps`; the exported tree visibly consumes four. The other six
  (`lem-extcb-one-dimensional-product`, `lem-extcb-one-dimensional-corner-dimension`,
  `lem-extcb-corner-dimension-additivity`, `lem-extcb1-close-corner-dimension`,
  `lem-compcb-corner-algebra`, `lem-hcb3-uniform-square-lower`) enter through
  `lem-extcb1-cross-corner-dimension`, which declares all of them. Said in *Role in the chain*,
  following the wave-3 precedent for large mismatches.
- **FLAG (two constant ledgers).** The registry *body* records the paper-proof witness
  $C_{\rm ext}=C_{\rm merge}[1+5C_H+20C_{\rm app}(C_H+1)]$; the *tree* derives
  $C_{\rm ext}=C_{\rm merge}(D_0+1)$ with $D_0=5(C_H+\kappa)$, $\kappa=C_{\rm corr}A_0$,
  $A_0=4(C_H+1)$. The prose follows the tree and attributes the other form to the registry body,
  exactly as `29_hcb.tex` does for `conj-hcb`. I did **not** assert that the two coincide (they do
  under $C_{\rm app}=C_{\rm corr}$, but that substitution would be my arithmetic, not the export's).
- **FLAG (the registry BODY is stale).** `argument/lemmas/conj-extcb.md`'s body still opens
  "…hence `proved-mod-audit`; not `af`-validated and not L0-rigorous", contradicting its own front
  matter and `argument/INDEX.md`. The shard follows the front matter + export. Landing-session
  registry-hygiene fix (WIRING §I), not a report issue. The body's *Verifier correction* paragraph is
  current and is what the shard's "Correction of record" reproduces.
- **Constant map for the reviewer:** my $a_{\rm corr},C_{\rm corr}=57,c_u=7,K_N$ are the export's
  `a_corr,C_corr,c_u,K_N`; $A_0=4(C_H+1)$ = `A_0`; $\kappa=C_{\rm corr}A_0$ = `kappa`;
  $D_0=5(C_H+\kappa)$ = `D_0`; $C_{\rm merge},a_{\rm merge}$ are `lem-extcb-four-corner-merge`'s.
- **Environment choice.** `kind: lemma` in the registry, so `\begin{lemma}`, matching every other
  shard, tier parent or not.
- **Label.** `\label{conj:extcb}`, **not** `lem:extcb` — the `check-provenance.py` first-hyphen-to-colon
  transform. Verified by an actual `check-provenance --check` run on a landed throwaway copy
  (WIRING §H.4).
- **A step I refused to compress further.** The *order* in node 1.4: level-one bijectivity and the
  $1/4$ lower modulus are established for all four $h_{jk}$ *before* the conditional `conj-hcb`
  clauses are invoked. The export flags that the verifier checked this ordering; collapsing it into
  "apply the H-CB inverse clauses" would silently turn a conditional import into an unconditional one,
  which is precisely the error the `conj-hcb` contract amendment exists to prevent.
- **Not claimed.** The lemma adds **one** dimension. It is not an induction and nothing in the shard
  iterates it; the shard says so in the outlook (§36), not by weakening the statement.

## Propagation (job 2)

Mechanical: four sentences across `29`, `32`, `34`, `36` said `conj-extcb` was `proved-mod-audit` /
`af: seeded` / a pending consumer. Each now states the recorded `proved` / `af: validated` and points
at `\S\ref{sec:extcb}`. Full before/after table in WIRING §G3. No other prose was touched, and no
challenge-history metadata was reintroduced anywhere (the wave-3 corrections stand).

One out-of-scope correction was unavoidable: `28_hcb4_canonical_inverse.tex` asserted that
`lem-hcb4-canonical-inverse`'s `defs:` line omits `def-compressed-corner` and
`def-extended-epsilon-cstar-algebra`. Repo commit `8d0a5061` added them, so the sentence was false
about the current repo. Rewritten to record the five definitions actually listed. Flagged in WIRING §G3.

## Recount (job 3)

Derived by script from `repo-inputs/argument-INDEX.md` (the CURRENT generated index), not by hand:

- **70** rows carry `proved`/`validated` (was 69; `conj-extcb` flipped).
- **37** ids are listed in §36's reproduced inventory (was 36; `conj-extcb` added). Every one of the
  37 is a `proved`/`validated` index row.
- **33** rows in the off-route table — *the same 33 as before*, because `conj-extcb` was never in that
  table. It is an exact, index-ordered set complement: no missing, extra or duplicated id, verified by
  an order-sensitive sequence comparison. `37 + 33 = 70`.

The per-count LaTeX derivation comments introduced by the wave-3 corrections pass are kept, with their
derivations updated; one new comment records `lem-thmainext-conditional`'s `proved-mod-audit` /
`af: none` status, which §36 now names as the open item beyond the EXT tier.

Two further §36 edits were forced by the flip rather than chosen: the "what is next" paragraph (the EXT
parent is no longer "in elevation") and the qualifications paragraph (it claimed *nothing* in the
document establishes the conditional inverse hypotheses for any datum — `\S\ref{sec:extcb}` now does,
for the EXT-CB datum, and only there).

## Macros (wave 3c)

No new macro needed and none proposed. `35_extcb.tex` writes $\lVert\cdot\rVert_{\rm cb}$, $B(H)$,
$\int U^\dagger\otimes U\,dU$ and $J$-free notation longhand. Wave 3's `\Jcan{P}{Q}{n}` proposal
remains open and unadopted.

## Build evidence (wave 3c)

- `pdflatex` twice against the real `main.tex` preamble plus the 25 repo shards `00-24` and all 12
  shards of this directory: **37 includes, exit 0, 77 pages, 0 LaTeX warnings, 0 undefined
  references, no rerun requested.**
- Contract byte-match against the LIVE `argument/lemmas/*.md`: **13/13**.
- Real `scripts/check-report-shards.sh` on a simulated tree: `37 shards included, labeled, cataloged,
  all <= 280 lines`, exit 0; red→green confirmed three times (bad `SHARD-ID` prefix; deleted
  `SHARD-SUMMARY`; a padded 294-line shard).
- Real `scripts/check-provenance.py --check` on a landed throwaway copy (§A–§F applied): **0 errors**,
  with `forward labels`, `claim labels`, `claim sources`, `hash freshness`, `status drift`,
  `reverse labels`, `coverage` and `parse integrity` all `[OK]`.
- Per-shard: exactly one `\section` and one `\label{sec:...}` each; `35_extcb.tex` is 204 lines
  (above the ~200 soft target, under the 280 guard — rationale in WIRING), `36_status_outlook.tex`
  149 lines.
