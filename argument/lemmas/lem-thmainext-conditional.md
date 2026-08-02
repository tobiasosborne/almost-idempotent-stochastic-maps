---
id: lem-thmainext-conditional
kind: lemma
contract: Extended th_main_ext assembly: there are universal C_E < infinity and epsilon_E > 0 such that every finite-dimensional extended epsilon-C*-algebra A, for 0 <= epsilon <= epsilon_E, is carried by one extended C_E*epsilon-isomorphism v:B->A from a finite-dimensional C*-algebra; the assembly uses the corrected squared COL-HILB estimate and the hostile-verified H-CB (conj-hcb), EXT-CB (conj-extcb), and Stage-1 reset packets, with constants independent of dimension, amplification level, and block data.
defs: def-extended-epsilon-cstar-algebra; def-fd-cstar-diagonal
deps: conj-hcb; conj-extcb; lem-hcb-column-hilbert-squared; lem-maincb-error-improvement; lem-maincb-reset-invariant-preservation; lem-maincb-structural-assembly; lem-extcb-four-corner-merge
status: proved-mod-audit
af: none
provenance: docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md §§3-5 (assembly + corrected COL-HILB); PROOF-W74F-H-STAGE1.md (Stage-1 reset packet); hostile verdicts VERDICT-W74F-BATCH.md §C, VERDICT-W74F-E-HCB.md, VERDICT-W74F-F-EXTCB.md, VERDICT-W74F-H-STAGE1.md (contract restatement endorsed verbatim by the H-verdict) Dependency-only amendment prescribed by DESIGN-MAIN-STRUCTURE-v5.md sect-10 step 15, re-validated against the repaired current contracts by DESIGN-THMAINEXT-REWIRE.md, and approved by AUDIT-THMAINEXT-REWIRE.md; contract byte-UNCHANGED, status unchanged at proved-mod-audit, and af unchanged at none.
owner: A
workspace: proofs/lem-thmainext-conditional
---

**Status.** Hostile-verified paper proof, hence `proved-mod-audit`; not
`af`-validated and not L0-rigorous.

**Contract restatement (2026-07-24).** Originally registered as an
explicitly conditional assembly ("assuming conj-hcb and conj-extcb");
both premises are now themselves `proved-mod-audit` (hostile-verified
this session) and the Stage-1 reset packet closed, so the contract was
restated to the exact text endorsed by `VERDICT-W74F-H-STAGE1.md`'s
registry-impact note.  The conditional `K`/`eta_K` clause moved to its
own node [[lem-routef-k-ledger]]; the id keeps its historical name (ids
are stable).

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
