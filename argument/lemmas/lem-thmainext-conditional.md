---
id: lem-thmainext-conditional
kind: lemma
contract: Extended th_main_ext assembly: there are universal C_E < infinity and epsilon_E > 0 such that every finite-dimensional extended epsilon-C*-algebra A, for 0 <= epsilon <= epsilon_E, is carried by one extended C_E*epsilon-isomorphism v:B->A from a finite-dimensional C*-algebra, with constants independent of dimension, amplification level, and block data.
defs: def-extended-epsilon-cstar-algebra; def-fd-cstar-diagonal
deps: conj-hcb; conj-extcb; lem-hcb-column-hilbert-squared; lem-maincb-error-improvement; lem-maincb-reset-invariant-preservation; lem-maincb-structural-assembly; lem-extcb-four-corner-merge
status: proved
af: validated
provenance: docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md §§3-5 (assembly + corrected COL-HILB); PROOF-W74F-H-STAGE1.md (Stage-1 reset packet); hostile verdicts VERDICT-W74F-BATCH.md §C, VERDICT-W74F-E-HCB.md, VERDICT-W74F-F-EXTCB.md, VERDICT-W74F-H-STAGE1.md (contract restatement endorsed verbatim by the H-verdict) Dependency-only amendment prescribed by DESIGN-MAIN-STRUCTURE-v5.md sect-10 step 15, re-validated against the repaired current contracts by DESIGN-THMAINEXT-REWIRE.md, and approved by AUDIT-THMAINEXT-REWIRE.md; contract byte-UNCHANGED, status unchanged at proved-mod-audit, and af unchanged at none. METHOD-CLAUSE RE-SCOPE 2026-08-03 (option B, USER-RATIFIED in-session; bead aism-g83q): the clause "the assembly uses the corrected squared COL-HILB estimate and the hostile-verified H-CB (conj-hcb), EXT-CB (conj-extcb), and Stage-1 reset packets" was REMOVED from the contract and re-scoped as documentary provenance, on the finding of AUDIT-THMAINEXT-ELEVATION.md (DESIGN-REJECTED) that it is a factual claim about how the proof is built, not about A/B/v, and is not dischargeable from the seven frozen T0 deps. The mathematical content -- the existential in C_E, epsilon_E, the map type, and independence of dimension, amplification level and block data -- is byte-unchanged. The deps line is DELIBERATELY LEFT AT ALL SEVEN IDS: those edges are the linker-enforced record of the same "uses" statement (in particular the edge to lem-hcb-column-hilbert-squared, the corrected squared estimate replacing the paper's unsquared display), and are NOT to be transitively reduced to lem-maincb-structural-assembly. Status unchanged at proved-mod-audit, af unchanged at none: this is a re-scope, NOT a promotion.
owner: A
workspace: proofs/lem-thmainext-conditional
---

**Status.** **af-VALIDATED in-repo (2026-08-03)** — `proved` / `af: validated`, L0-rigorous.
Four-node tree, root `validated`, taint clean, FIRST PASS with ZERO
challenges: fresh-codex prover, separate fresh codex verifier per node
(CLAUDE.md §6). Export in `proofs/lem-thmainext-conditional/export.md`;
oracle `af-lem-thmainext-conditional` registered and `fr verify` PASS.
The flip is a MECHANICAL reflection of the codex ledger — no orchestrator
judgment of the proof was exercised.

**What this does and does not buy (read with the interface note below).**
The tree is: fix M28's ledger datum `W` and define the two constants
(1.1); apply M28 to arbitrary `A, epsilon` and substitute (1.2); unfold
`def-extended-delta-inclusion` for the all-amplification reading and
universality (1.3). It proves no mathematics absent from
[[lem-maincb-structural-assembly]]; its value is a validated interface
projection and DAG decoupling, per `AUDIT-THMAINEXT-ELEVATION-V2.md` §9.

**Contract restatement (2026-07-24).** Originally registered as an
explicitly conditional assembly ("assuming conj-hcb and conj-extcb");
both premises are now themselves `proved-mod-audit` (hostile-verified
this session) and the Stage-1 reset packet closed, so the contract was
restated to the exact text endorsed by `VERDICT-W74F-H-STAGE1.md`'s
registry-impact note.  The conditional `K`/`eta_K` clause moved to its
own node [[lem-routef-k-ledger]]; the id keeps its historical name (ids
are stable).

**Method-clause re-scope (2026-08-03, user-ratified — option B).** The
contract previously also asserted *how* the assembly is built ("the
assembly uses the corrected squared COL-HILB estimate and the
hostile-verified H-CB, EXT-CB, and Stage-1 reset packets"). That is a
claim about a *proof*, not about `A`, `B`, `v`;
`AUDIT-THMAINEXT-ELEVATION.md` found it not dischargeable from the seven
frozen T0 deps, because [[lem-maincb-structural-assembly]] exports no
trace of its own construction and no frozen contract supplies
`W.epsilon_MAIN <= e_H` or `<= e_ext`.  The clause is therefore recorded
here and in `provenance:` rather than proved.  **The `deps:` line keeps
all seven ids on purpose** — those edges are the *linker-enforced* form
of the same statement (above all the edge to
[[lem-hcb-column-hilbert-squared]], the corrected squared estimate that
replaces the paper's unsquared display), and a future reader must not
"simplify" them away to the transitive reduction
[[lem-maincb-structural-assembly]].  Nothing was promoted by the re-scope:
the row stays `proved-mod-audit`.  (The `af:` field later moved
`none` → `seeded` when the workspace was stood up on 2026-08-03 for the
audit-confirmed three-node elevation; seeding is not a rigour promotion
either.)

**Interface width (honest note).** After the re-scope this row is a
*thin* existential repackaging of [[lem-maincb-structural-assembly]]: it
hides the witness ledger `W`, the block form `B = ⊕_C M_{|C|}`, and the
unit estimate `||v(I_B)-I_A||`, keeping only the two universal
constants.  That is a legitimate interface for [[lem-routef-k-ledger]],
which consumes exactly `C_E, epsilon_E` as a black box — but the row is
narrow, and its af elevation is correspondingly small.

**MAIN-CB assembly.** The transcribed invariant is that every extension,
binary merge, and error-reduction step produces one level-one map whose
amplifications share the same estimate.  Error reduction resets the
error after each raw step, so neither block count nor block dimension is
accumulated.

**Squared correction.** The printed unsquared display at
`approximate_algebras.tex:1551-1555` is replaced by
\[
\left|\langle X,X\rangle_n-\lVert X\rVert_{n,1}^2\right|
\le C(\delta+\varepsilon)\lVert X\rVert_{n,1}^2.
\]
The W74F-C artifact derives this by treating \(X\) as one rectangular
operator-space element, with no entrywise \(n\)-sum.

**Conditional ledger.** Once H-CB and EXT-CB provide universal constants
and positive thresholds, all remaining coefficients form finite
sum/product expressions.  Their maximum defines \(K\), and the minimum
of the functional-calculus, H-CB, EXT-CB, Neumann, normalization, and
raw-step thresholds defines \(\eta_K>0\).  Without the two conjectures
this ledger is conditional only.
