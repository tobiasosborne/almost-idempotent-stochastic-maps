# DESIGN-MAIN-STRUCTURE-v3 — closed call envelopes and local reset invariant

**Date:** 2026-07-27
**Role:** fresh independent third-repair designer
**Status:** **DESIGN ONLY; NON-RIGOROUS; DO NOT SEED.** Nothing below
authorizes a definition, contract, dependency, or status change. Every
proposed change is escalated for user ratification and fresh hostile review.

## 0. Verdict and exact delta from v2

**Verdict: DESIGNED-CLOSABLE, conditional on two explicit serial gates.**
The two contract-architecture defects that refuted v2 are repaired without
changing the mathematical core confirmed by the binding re-audit. No
dimension-dependent constant, counterexample, or source-route obstruction was
found. The two gates are:

1. **P0 — definition provisioning and user ratification:** the four missing
   theorem-free vocabulary/data shards must be ratified and landed before
   M01; and
2. **G-S1 — unchanged Stage-1 producer gate:** the three absent Stage-1
   producers must be landed before any M19 replacement or structural target.

The exact changes from v2, and only those changes, are:

| v3 change | binding cause |
|---|---|
| Add P0 before M01 for `def-operator-space`, `def-maincb-reset-state`, `def-maincb-raw-call`, and `def-maincb-partition-state`. | `AUDIT-MAIN-STRUCTURE-v2.md:63-86,329-338,368-375` (§10.1). |
| Replace the single M19 by three call-type-specific conditional envelopes M19-S1/S2/S3. Each contract names every supplied current map; none produces a Stage-2/3 current map. | `AUDIT-MAIN-STRUCTURE-v2.md:27-61,221-222,339-344,374-376` (§10.2). |
| Choose §10.3's **first option**: M13 outputs the post-helper scale \(C_{\rm s2}t\), while corrected M16 accepts that scale and absorbs \(C_{\rm s2}\) into its universal \(D_2,e_2\). | `AUDIT-MAIN-STRUCTURE-v2.md:42-60,215-218,341-344,376-381`. |
| Add M19-R, a result row proving preservation of the stronger local invariant \(d(v_U)\le c_0^{\rm cb}\varepsilon_U\), where \(\varepsilon_U\) is the current corner's ambient defect. | `AUDIT-MAIN-STRUCTURE-v2.md:221-230,343-344,382-385` (§10.4). |
| Replace every category-valued dependency in M05/M07/M09 by exact ids. | `AUDIT-MAIN-STRUCTURE-v2.md:125-194,201-209,384-386` (§10.5). |
| Retain G-S1 after M18 and before all M19/MAIN structural rows. | `AUDIT-MAIN-STRUCTURE-v2.md:265-277,386-387` (§10.6). |
| Retain M27's complete one-class input family and the M28-only join. | `AUDIT-MAIN-STRUCTURE-v2.md:244-249,229-230,311-312,387-389` (§10.7). |
| Add the missing R22 subsection and complete the escalation ledger, including the exact future `lem-thmainext-conditional` dependency proposal. | `AUDIT-MAIN-STRUCTURE-v2.md:251-263,351-365,389-391` (§10.8). |

All other retained contracts below are copied verbatim from v2. A table row
explicitly says when one of the named corrections changes its contract,
definitions, dependencies, or domain.

The pinned source is
`refs/kitaev-2405.02434/approximate_algebras.tex`, SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`,
matching `refs/manifest/checksums.sha256:4`. The source itself says that its
big-\(O\) functions do not depend on additional data
(`approximate_algebras.tex:458`) and states dimension-freeness in
`th_main` and `th_main_ext` (`ibid.:460-462,1538-1540`). Those statements are
source provenance, not a status promotion of this design.

## 1. P0 — definition provisioning and user-ratification gate

**HARD STOP BEFORE M01.** None of the four ids below exists in the generated
38-term definition index (`definitions/INDEX.md:1-43`). All four proposals
are **ESCALATED FOR USER RATIFICATION**. They contain fields and notation
only, in accordance with R35
(`DESIGN-FUDW-DECOMP-v4.1.md:607-608`); they contain no existence,
smallness, estimate, preservation, success, iteration, or termination
assertion.

| proposed definition | exact fields only | provenance/rationale | forbidden theorem content |
|---|---|---|---|
| `def-operator-space` | A complex vector space \(\mathcal L\); norms on every rectangular space \(M_{n,k}\otimes\mathcal L\); the two operator-space axioms; the induced rectangular inclusions; optionally an isometric involution for the self-adjoint case. | Byte-match candidate at `approximate_algebras.tex:1451-1475`; v4.1 proposal at `DESIGN-FUDW-DECOMP-v4.1.md:391`. Proposed kind `cited`, lock only after the repository's local byte-match/ratification gate. | No representation theorem, amplification estimate, or existence of a map. |
| `def-maincb-reset-state` | A current index union \(U\); its compressed ambient \(A_U\); the recorded ambient defect \(\varepsilon_U\); an exact finite-dimensional source \(C^*\)-algebra \(B_U\); a level-one map \(v_U:B_U\to A_U\); its fixed amplification family \(I_n\otimes v_U\); and a recorded map defect \(d_U\) plus inclusion/isomorphism tag. | Datum-only package specified at `DESIGN-FUDW-DECOMP-v4.1.md:403,419-423`; proposed kind `original`, draft pending sign-off. | In particular, no assertion that \(d_U\le c_0^{\rm cb}\varepsilon_U\), no existence, and no preservation theorem. |
| `def-maincb-raw-call` | A call-type tag (scalar, Stage 1, Stage 2, or Stage 3); supplied input reset states/maps; explicit source and target corners; pre-helper base scale \(t\); any post-helper datum scale; the literal output map; its fixed amplification family; target ambient defect \(\varepsilon_{\rm target}\); and recorded raw defect \(d_{\rm raw}\). | Datum-only package specified at `DESIGN-FUDW-DECOMP-v4.1.md:404,424-428`; proposed kind `original`, draft pending sign-off. | No hidden smallness, valid-domain, success, reset, preservation, or iteration clause. |
| `def-maincb-partition-state` | A finite atomic index set \(J\); a supplied commutative map \(w:\mathbb C^J\to A\); \(P_j=w(e_j)\); the relation \(j\sim k\iff\dim S^A_{P_j,P_k}=1\); when that relation is an equivalence, its class family \(\mathcal C\); for \(U\subseteq J\), \(P_U=\sum_{j\in U}P_j\) and \(A_U=S^A_{P_U}\); a current union \(U\) of classes; and a reference to its supplied `def-maincb-reset-state`. | Missing package identified at `DESIGN-MAIN-STRUCTURE.md:74-86` and `AUDIT-MAIN-STRUCTURE-v2.md:63-86`; proposed kind `original`, draft pending sign-off. | No assertion that \(\sim\) is an equivalence, that a current map exists, that cross-corners vanish, or that a merge preserves anything. |

The distinction between the last three packages is load-bearing:
`def-maincb-partition-state` records the finite geometry and current union;
`def-maincb-reset-state` records one supplied map and its two defects; and
`def-maincb-raw-call` records one literal attempted call. The result rows
below, not the definitions, prove admissibility and preservation.

## 2. Canonical scale discipline

Let \(A\) have ambient defect \(\varepsilon\), let
\(w:\mathbb C^m\to A\) be the supplied reset commutative inclusion, and use
the fields of `def-maincb-partition-state`:
\[
 P_U=\sum_{j\in U}P_j,\qquad A_U=S^A_{P_U}.
\]
Write \(\varepsilon_U\) for the recorded ambient defect of \(A_U\), \(d_U\)
for the recorded defect of its supplied current map, and \(t\) for the
**pre-helper base geometric scale of one call**.

The induction invariant to be proved by M19-R is
\[
 \tag{RI(U)} d_U\le c_0^{\rm cb}\varepsilon_U.
\]
This is not placed in a definition.

For Stage 2 there are deliberately two scales:
\[
 \tag{S2-scale}
 \text{base scale }t,
 \qquad
 \text{post-M13 EXT-datum scale }s_{\rm EXT}=C_{\rm s2}t,
 \qquad C_{\rm s2}\ge1.
\]
Corrected M16 uses `conj-extcb` at \(s_{\rm EXT}\) and outputs a raw map of
defect at most \(D_2t\), with \(D_2\) enlarged by the universal factor
\(C_{\rm s2}\). Thus M18 and M20 continue to test the base scale \(t\);
there is no false implication \(C_{\rm s2}t\le t\), and M20 need not insert a
second Stage-2 factor. This is exactly the first option in
`AUDIT-MAIN-STRUCTURE-v2.md:376-381`.

There is also no assertion that all literal calls have the same \(t\).
M19-S1/S2/S3 produce \(t_i=K_i\varepsilon\) for their respective call
types; M20 takes the finite maximum
\(K_{\rm call}=\max\{1,L,c_0^{\rm cb},K_1,K_2,K_3\}\).
Every call is checked with its own \(t_i\le K_{\rm call}\varepsilon\).

## 3. Exact landed leaves

The following are the only existing result leaves used as inputs:

- compression:
  `lem-compcb-amplified-compression`,
  `lem-compcb-amplified-compression-identities`,
  `lem-compcb-amplified-almost-containment`,
  `lem-compcb-corner-algebra`,
  `lem-compcb-rectangular-product`, and
  `lem-compcb-single-compression-transfer`
  (`argument/lemmas/lem-compcb-*.md`, exact contracts audited in
  `AUDIT-MAIN-STRUCTURE-v2.md:94-109`);
- one-dimensional corners:
  `lem-extcb-one-dimensional-product`,
  `lem-extcb-one-dimensional-corner-dimension`, and
  `lem-extcb-corner-dimension-additivity`
  (`argument/lemmas/lem-extcb-*.md`; source
  `approximate_algebras.tex:1162-1187,1363-1369`);
- extension/merge:
  `conj-extcb` and `lem-extcb-four-corner-merge`
  (`argument/lemmas/conj-extcb.md:4-6,23-40`;
  `argument/lemmas/lem-extcb-four-corner-merge.md:4-6,18-25`);
- the landed but `stated` target `lem-maincb-error-improvement`
  (`argument/lemmas/lem-maincb-error-improvement.md:4-9,21-31`); and
- the downstream non-rigorous consumer `lem-thmainext-conditional`
  (`argument/lemmas/lem-thmainext-conditional.md:4-9,26-30`).

`lem-compcb-single-compression-transfer` is used only for the literal
Stage-1 old ideal side. Its validated proof fixes an ideal unit; it is not the
outer/nested transfer used by Stages 2 and 3
(`AUDIT-MAIN-STRUCTURE-v2.md:104-106,175-194`).

## 4. Acyclic row design before G-S1

In every table, `defs` lists canonical definition imports and `deps` lists
exact result ids. A proposed id is a legal dependency only if its row is
earlier in this document. Budgets are projected direct workspaces and obey
the repository cap.

### 4.1 Improvement and direct helpers

| row / proposed id | one-line `contract:` value | defs | exact `deps:` | provenance | budget | feasibility / audit delta |
|---|---|---|---|---|---|---|
| **M01** `lem-maincb-improvement-one-step` | There are universal \(K_{\rm step}\ge1\) and \(e_{\rm step}>0\) such that, if \(B\) is a finite-dimensional \(C^*\)-algebra, \(A\) an extended \(\varepsilon\)-\(C^*\)-algebra, and \(v:B\to A\) an extended \(d\)-inclusion with \(d+\varepsilon\le e_{\rm step}\), then one dagger-preserving level-one map \(v^+\), with \(v_n^+=I_n\otimes v^+\), satisfies \(\sup_n\|v_n^+-v_n\|\le K_{\rm step}d\) and is an extended \(d^+\)-inclusion for \(d^+\le K_{\rm step}(d^2+\varepsilon)\). | `def-operator-space`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion`; `def-fd-cstar-diagonal` | none | `approximate_algebras.tex:1239-1311,1508-1535` | 8 / 3 | **SUPPORTED-WITH-DERIVATION.** Contract verbatim from v2; P0 supplies the missing vocabulary (§10.1; audit M01). |
| **M02** `lem-maincb-improvement-iteration` | There are universal \(e_{\rm it}>0\), \(K_{\rm disp}<\infty\), and \(K_{\rm floor}<\infty\) such that, if \(B\) is a finite-dimensional \(C^*\)-algebra, \(A\) is an extended \(\varepsilon\)-\(C^*\)-algebra, and \(v:B\to A\) is an extended \(d\)-inclusion with \(d+\varepsilon\le e_{\rm it}\), then one dagger-preserving \(\widetilde v\), with \(\widetilde v_n=I_n\otimes\widetilde v\), satisfies \(\sup_n\|\widetilde v_n-v_n\|\le K_{\rm disp}d\) and has extended defect at most \(K_{\rm floor}\varepsilon\); for \(\varepsilon>0\) it is reached after finitely many correction steps, and for \(\varepsilon=0\) it is their operator-norm limit. | M01 defs | `lem-maincb-improvement-one-step` | `approximate_algebras.tex:1313,1508-1535` | 6 / 3 | **SUPPORTED-WITH-DERIVATION.** Contract verbatim; P0 correction only. |
| **M03** `lem-maincb-error-improvement` | **Keep the ratified contract verbatim:** there are universal \(\varepsilon_{\max}^{\rm cb}>0,\delta_{\max}^{\rm cb}>0,c_0^{\rm cb}<\infty\) such that every extended \(\delta\)-inclusion \(v:B\to A\) from finite-dimensional \(B\) into an extended \(\varepsilon\)-\(C^*\)-algebra, with \(0\le\varepsilon\le\varepsilon_{\max}^{\rm cb}\) and \(0\le\delta\le\delta_{\max}^{\rm cb}\), can be replaced by an extended \(c_0^{\rm cb}\varepsilon\)-inclusion, preserving bijectivity. | `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion`; `def-operator-space` | `lem-maincb-improvement-iteration` | `approximate_algebras.tex:1192,1317-1319,1483-1509,1557`; landed contract at `lem-maincb-error-improvement.md:4` | 5 / 3 | **SUPPORTED-WITH-DERIVATION; CONTRACT UNCHANGED.** Only the dependency rewires from exact-target correction to M02 (audit M03). |
| **M04** `lem-maincb-direct-corner-envelope` | There are universal \(L\ge1\) and \(e_{\rm env}>0\) such that, if \(0\le\varepsilon\le e_{\rm env}\) and \(w:\mathbb C^m\to A\) is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion, then every nonempty \(U\) has \(P_U\) a \(c_0^{\rm cb}\varepsilon\)-projection, every \(A_U=S^A_{P_U}\) is an extended \(L\varepsilon\)-\(C^*\)-algebra, and for \(U\subseteq R\) all subordination and complementarity errors among \(P_U,P_{R\setminus U},P_R\) are at most \(L\varepsilon\). | `def-maincb-partition-state`; `def-compressed-corner`; `def-delta-projection` | `lem-maincb-error-improvement`; `lem-compcb-corner-algebra` | `approximate_algebras.tex:1068-1084,1367-1368,1428-1435` | 6 / 3 | **SUPPORTED-WITH-DERIVATION.** Contract verbatim; P0 supplies its canonical state notation. |
| **M05** `lem-maincb-direct-sum-inclusion-merge` | There are universal \(C_{\rm dir}<\infty\) and \(e_{\rm dir}>0\) such that, if \(B_1,B_2\) are finite-dimensional \(C^*\)-algebras, \(P_1,P_2\) are target \(t\)-projections, \(\|P_1+P_2-I\|\le t\), and \(v_i:B_i\to S_{P_i}\) are extended \(t\)-inclusions with target ambient defect at most \(t\le e_{\rm dir}\), then \((x_1,x_2)\mapsto v_1(x_1)+v_2(x_2)\) is an extended \(C_{\rm dir}t\)-inclusion; bijectivity is asserted only if both \(v_i\) are bijective and both target cross-corners vanish. | `def-operator-space`; `def-extended-delta-inclusion`; `def-compressed-corner` | `lem-compcb-amplified-compression`; `lem-compcb-amplified-compression-identities`; `lem-compcb-corner-algebra`; `lem-compcb-rectangular-product` | `approximate_algebras.tex:1325-1359,1542-1544,1557` | 8 / 3 | **SUPPORTED-WITH-DERIVATION.** Contract verbatim; vague “landed compression rows” replaced by exact ids (§10.5; audit M05). |
| **M06** `lem-maincb-full-corner-identification` | There is a universal \(e_{\rm full}>0\) such that, if \(R\) is a \(t\)-projection in an extended \(t\)-\(C^*\)-algebra and \(\|R-I\|\le t\le e_{\rm full}\), then \(\operatorname{Co}_R=I\) and \(S_R=A\), at every amplification. | `def-operator-space`; `def-compressed-corner`; `def-delta-projection` | `lem-compcb-amplified-compression`; `lem-compcb-amplified-compression-identities` | `approximate_algebras.tex:1064-1066,1542-1544` | 4 / 2 | **SUPPORTED-WITH-DERIVATION.** Verbatim. |

M05 uses the two-diagonal direct-sum corollary, not the four-bijective-corner
theorem. The source concludes an inclusion from two diagonal inclusions and
adds bijectivity only under the zero-cross-corner hypothesis
(`approximate_algebras.tex:1352-1359`).

### 4.2 Nested comparison and outer compression

| row / proposed id | one-line `contract:` value | defs | exact `deps:` | provenance | budget | feasibility / audit delta |
|---|---|---|---|---|---|---|
| **M07** `lem-maincb-nested-corner-comparison` | There are universal \(C_{\rm nest}<\infty\) and \(e_{\rm nest}>0\) such that, whenever \(R,P,Q\) are \(t\)-projections in a finite-dimensional extended \(t\)-\(C^*\)-algebra, \(R\) is nonvanishing, \(P,Q\) are subordinate to \(R\) with all four left/right subordination errors at most \(t\le e_{\rm nest}\), \(A_R=S^A_R\), \(P^R=\operatorname{Co}^A_R(P)\), and \(Q^R=\operatorname{Co}^A_R(Q)\), then \(P^R,Q^R\) are \(C_{\rm nest}t\)-projections in \(A_R\) and, at every amplification, \(\|F^R_{P,Q}(\operatorname{Co}^A_R X)-X\|\le C_{\rm nest}t\|X\|\) for \(X\in S^A_{P,Q}\), while \(\|\operatorname{Co}^A_{P,Q}Y-Y\|\le C_{\rm nest}t\|Y\|\) for \(Y\in S^{A_R}_{P^R,Q^R}\). | `def-operator-space`; `def-compressed-corner`; `def-delta-projection` | `lem-compcb-amplified-compression`; `lem-compcb-amplified-compression-identities`; `lem-compcb-amplified-almost-containment`; `lem-compcb-corner-algebra`; `lem-compcb-rectangular-product` | `approximate_algebras.tex:1054-1082,1435-1441`; fixed telescope confirmed at `AUDIT-MAIN-STRUCTURE-v2.md:125-164` | 11 / 3 | **SUPPORTED-WITH-DERIVATION; LOAD-BEARING.** Contract verbatim; exact deps and internal-product expansions added (§10.5). |
| **M08** `lem-maincb-nested-corner-dimension-transport` | There is a universal \(e_{\rm ncd}>0\) such that, whenever \(R,P,Q\) are \(t\)-projections in a finite-dimensional extended \(t\)-\(C^*\)-algebra, \(R\) is nonvanishing, all four left/right subordination errors of \(P,Q\) to \(R\) are at most \(t\le e_{\rm ncd}\), \(A_R=S^A_R\), \(P^R=\operatorname{Co}^A_R(P)\), and \(Q^R=\operatorname{Co}^A_R(Q)\), one has \(\dim S^A_{P,Q}=\dim S^{A_R}_{P^R,Q^R}\). | M07 defs | `lem-maincb-nested-corner-comparison` | M07 plus two-sided injectivity; comparison locus `proofs/lem-extcb1-close-corner-dimension/export.md:123-161` | 3 / 2 | **SUPPORTED-WITH-DERIVATION.** Verbatim; re-audit confirmed it. |
| **M09** `lem-maincb-outer-compression-transfer` | There are universal \(C_{\rm out}<\infty\) and \(e_{\rm out}>0\) such that, whenever \(R,P\) are \(t\)-projections in a finite-dimensional extended \(t\)-\(C^*\)-algebra, \(R\) is nonvanishing, both subordination errors of \(P\) to \(R\) are at most \(t\), \(v:B\to S^A_P\) is an extended \(t\)-isomorphism, \(A_R=S^A_R\), \(P^R=\operatorname{Co}^A_R(P)\), and \(t\le e_{\rm out}\), the explicitly defined map \(T=\operatorname{Co}^{A_R}_{P^R}\circ\operatorname{Co}^A_R\circ v:B\to S^{A_R}_{P^R}\) is an extended \(C_{\rm out}t\)-isomorphism and \(T_n=I_n\otimes T\) for every \(n\). | `def-operator-space`; `def-compressed-corner`; `def-extended-delta-inclusion` | `lem-maincb-nested-corner-comparison`; `lem-maincb-nested-corner-dimension-transport`; `lem-compcb-amplified-compression`; `lem-compcb-amplified-compression-identities`; `lem-compcb-corner-algebra`; `lem-compcb-rectangular-product` | `approximate_algebras.tex:1068-1082,1435-1441,1542-1544`; `AUDIT-MAIN-STRUCTURE-v2.md:175-194` | 9 / 3 | **SUPPORTED-WITH-DERIVATION.** Contract verbatim; exact amplification/identity deps added (§10.5). |

For M07's forward direction, expand the two internal products in
\(F^R_{P,Q}\), replace them using
`lem-compcb-rectangular-product`, replace
\(P^R,Q^R,\operatorname{Co}_R X\) using the exact compression,
identity, and almost-containment rows, and finish with
\(P(XQ)=X+O(t)\|X\|\). For the reverse direction, start from
\(Y=F^R_{P,Q}Y\), expand both internal products, run the same fixed telescope,
and obtain \(\operatorname{Co}^A_{P,Q}Y=Y+O(t)\|Y\|\). This is a fixed number
of replacements at every amplification, not a sum over atoms
(`AUDIT-MAIN-STRUCTURE-v2.md:129-164`).

M08 shrinks so \(C_{\rm nest}t<1\), obtains injections in both directions,
and uses finite dimensionality. M09 uses M07 with \(P=Q\), M08 for equality
of dimensions, and exact amplification twice. If a future prover cannot
derive either M07 direction from the five exact deps, the plan stops at an
**ESCALATED GAP**; no generic close-corner substitute is permitted.

### 4.3 Conditional partition and datum rows

| row / proposed id | one-line `contract:` value | defs | exact `deps:` | provenance | budget | feasibility / audit delta |
|---|---|---|---|---|---|---|
| **M10** `lem-maincb-corner-equivalence` | There is a universal \(e_{\sim}>0\) such that, for every finite family of one-dimensional \(t\)-projections \(P_1,\ldots,P_m\) in an extended \(t\)-\(C^*\)-algebra with \(t\le e_{\sim}\), the relation \(j\sim k\iff\dim S_{P_j,P_k}=1\) is an equivalence relation. | `def-maincb-partition-state`; `def-one-dimensional-delta-projection`; `def-compressed-corner` | `lem-extcb-one-dimensional-product`; `lem-extcb-one-dimensional-corner-dimension` | `approximate_algebras.tex:1162-1187` | 6 / 3 | **SUPPORTED-WITH-DERIVATION.** Verbatim; canonical relation fields now provisioned. |
| **M11** `lem-maincb-cross-union-zero-corners` | There is a universal \(e_{\rm zero}>0\) such that, if a supplied MAIN partition state has \(w:\mathbb C^m\to A\) a non-unital extended \(t\)-inclusion with one-dimensional images \(P_j\), \(U,V\) are disjoint nonempty unions sharing no equivalence class, \(R=U\cup V\), and \(t\le e_{\rm zero}\), then \(\dim S^A_{P_U,P_V}=\dim S^A_{P_V,P_U}=0\) and \(\dim S^{A_R}_{P_U^R,P_V^R}=\dim S^{A_R}_{P_V^R,P_U^R}=0\). | `def-maincb-partition-state`; `def-compressed-corner` | `lem-maincb-nested-corner-dimension-transport`; `lem-maincb-corner-equivalence`; `lem-extcb-corner-dimension-additivity` | `approximate_algebras.tex:1363-1369,1428,1443` | 6 / 3 | **SUPPORTED-WITH-DERIVATION.** Same mathematical contract; canonical partition fields replace design-local notation (audit M11; §10.1). |
| **M12** `lem-maincb-cross-class-merging-datum` | There are universal \(C_{\rm cross}\ge1\) and \(e_{\rm cross}>0\) such that, if a supplied MAIN partition state comes from a non-unital extended \(t\)-inclusion \(w:\mathbb C^m\to A\) with one-dimensional images \(P_j\), has disjoint nonempty unions \(U,V\) sharing no class and \(R=U\cup V\), and supplied current reset states \(v_U:B_U\to A_U\), \(v_V:B_V\to A_V\) are extended isomorphisms satisfying \(\varepsilon_U,\varepsilon_V,d_U,d_V\le t\le e_{\rm cross}\), \(d_U\le c_0^{\rm cb}\varepsilon_U\), and \(d_V\le c_0^{\rm cb}\varepsilon_V\), then the two M09 outer-compressed diagonal maps and the unique maps between the two M11 zero corners form the explicit Stage-3 raw-call four-corner datum in \(A_R\), with common defect \(\rho\le C_{\rm cross}t\). | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-four-corner-merging-datum` | `lem-maincb-error-improvement`; `lem-maincb-outer-compression-transfer`; `lem-maincb-cross-union-zero-corners` | `approximate_algebras.tex:1325-1345,1358,1363-1369,1443` | 9 / 3 | **SUPPORTED-WITH-DERIVATION.** Corrected only to name the two supplied maps, their local invariant, and canonical raw-call data (audit M12; §§10.1-2,4). |
| **M13** `lem-maincb-stage2-extcb-datum` | There are universal \(C_{\rm s2}\ge1\) and \(e_{\rm s2}>0\) such that, if a supplied MAIN partition state comes from a non-unital extended \(t\)-inclusion \(w:\mathbb C^m\to A\) with one-dimensional images \(P_j\), has nonempty \(U\), \(j\notin U\), \(\dim S^A_{P_k,P_j}=1\) for every \(k\in U\), and \(R=U\cup\{j\}\), and a supplied current reset state \(v_U:M_{|U|}\to A_U\) is an extended isomorphism satisfying \(\varepsilon_U,d_U\le t\le e_{\rm s2}\) and \(d_U\le c_0^{\rm cb}\varepsilon_U\), then the M09 outer-compressed map, \(P_U^R\), and \(P_j^R\) form the explicit Stage-2 raw-call closed EXT-CB datum in \(A_R\), with total post-helper defect at most \(C_{\rm s2}t\). | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-extcb-datum` | `lem-maincb-error-improvement`; `lem-maincb-nested-corner-dimension-transport`; `lem-maincb-outer-compression-transfer`; `lem-maincb-corner-equivalence`; `lem-extcb-corner-dimension-additivity` | `approximate_algebras.tex:1363-1412,1430-1441` | 10 / 3 | **SUPPORTED-WITH-DERIVATION.** The five EXT clauses are retained; the base/post-helper scales and supplied current state are now explicit (audit M13; §10.3-4). |

M13 must still prove all five v2 clauses: M09 bijectivity onto the nested
diagonal corner; scalar nested dimension from M08; nonzero cross-corner from
additivity plus same-class equivalence; exact complementarity
\(P_U^R+P_j^R=I_{A_R}\); and one maximum of the preceding universal defects.
The output is \(C_{\rm s2}t\), not \(t\).

### 4.4 Raw rows and corrected upstream reset eligibility

| row / proposed id | one-line `contract:` value | defs | exact `deps:` | provenance | budget | feasibility / audit delta |
|---|---|---|---|---|---|---|
| **M14** `lem-maincb-initial-raw-inclusion` | There are universal \(D_0<\infty\) and \(e_0>0\) such that, in every finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra with \(\varepsilon\le t\le e_0\), the scalar map \(\lambda\mapsto\lambda I_A\) is an extended \(D_0t\)-inclusion; if \(\dim A=1\), it is bijective. | `def-operator-space`; `def-maincb-raw-call`; `def-extended-delta-inclusion` | none | `approximate_algebras.tex:430-455,1467-1475` | 4 / 2 | **SUPPORTED-WITH-DERIVATION.** Verbatim; raw-call data now canonical. |
| **M15** `lem-maincb-stage1-raw-refinement` | There are universal \(D_1<\infty\) and \(e_1>0\) such that, if an explicit Stage-1 raw-call datum supplies complementary target \(t\)-projections, an old extended \(t\)-inclusion \(\mathbb C^{m-1}\to S_{P_{\rm old}}\) when \(m>1\), a fresh extended \(t\)-inclusion \(\mathbb C^2\to S_{P_{\rm fresh}}\), fixed amplification families, and every projection, complementarity, map, and target-ambient defect is at most \(t\le e_1\), then their sum map is an extended \(D_1t\)-inclusion \(\mathbb C^{m+1}\to A\); when \(m=1\), the old side is absent and the conclusion is the supplied fresh inclusion. | `def-maincb-reset-state`; `def-maincb-raw-call`; `def-operator-space` | `lem-maincb-direct-sum-inclusion-merge`; `lem-compcb-single-compression-transfer` | `approximate_algebras.tex:1352-1359,1419-1426` | 5 / 2 | **SUPPORTED-WITH-DERIVATION.** Explicit hypotheses replace the naked “Stage-1 call” (audit M15; §10.1-2). |
| **M16** `lem-maincb-stage2-raw-extension` | There are universal \(D_2<\infty\) and \(e_2>0\), chosen with \(e_2\le e_{\rm s2}\) and \(C_{\rm s2}e_2\le e_{\rm ext}\), such that every explicit Stage-2 raw-call closed EXT-CB datum in \(A_R\) whose total post-helper defect is at most \(C_{\rm s2}t\), for base scale \(0\le t\le e_2\), admits an extended \(D_2t\)-isomorphism \(M_{r+1}\to A_R\). | `def-maincb-raw-call`; `def-extcb-datum`; `def-operator-space` | `lem-maincb-stage2-extcb-datum`; `conj-extcb` | `approximate_algebras.tex:1378-1412,1435-1441`; exact `conj-extcb` contract at `argument/lemmas/conj-extcb.md:4` | 3 / 2 | **SUPPORTED-WITH-DERIVATION.** Corrected per §10.3 option 1: take, for example, \(D_2\ge C_{\rm ext}C_{\rm s2}\); no numerical radius is guessed. |
| **M17** `lem-maincb-stage3-raw-merge` | There are universal \(D_3<\infty\) and \(e_3>0\), with \(e_3\le a_{\rm merge}/(C_{\rm cross}+1)\), such that every amplified four-corner datum in \(A_R\) with common defect \(\rho\le C_{\rm cross}t\) and target ambient defect \(\varepsilon_{A_R}\le t\le e_3\) satisfies \(\rho+\varepsilon_{A_R}\le a_{\rm merge}\) and yields an extended \(D_3t\)-isomorphism \(B_U\oplus B_V\to A_R\). | `def-maincb-raw-call`; `def-four-corner-merging-datum`; `def-operator-space` | `lem-maincb-cross-class-merging-datum`; `lem-extcb-four-corner-merge` | `approximate_algebras.tex:1325-1359,1443`; `lem-extcb-four-corner-merge.md:4,18-25` | 3 / 2 | **SUPPORTED-WITH-DERIVATION.** Verbatim; canonical raw-call fields added. |
| **M18** `lem-maincb-reset-constant-ledger` | With \(D_*=\max\{1,D_0,D_1,D_2,D_3\}\) and \(r_{\rm reset}:=\min\{e_0,e_1,e_2,e_3,\varepsilon_{\max}^{\rm cb},\delta_{\max}^{\rm cb}/D_*\}>0\), every explicit scalar, Stage-1, Stage-2, or Stage-3 raw call with its own base scale \(0\le t\le r_{\rm reset}\) and target ambient defect \(0\le\varepsilon_{\rm target}\le t\)—where a Stage-2 call may have post-helper datum scale \(C_{\rm s2}t\) as licensed by M16—has \(d_{\rm raw}\le D_*t\le\delta_{\max}^{\rm cb}\) and \(\varepsilon_{\rm target}\le\varepsilon_{\max}^{\rm cb}\), hence satisfies the exact hypotheses of M03; all witnesses are positive, finite, universal, and independent of dimension, amplification, block data, and stage index. | `def-maincb-raw-call`; `def-maincb-reset-state` | `lem-maincb-error-improvement`; `lem-maincb-initial-raw-inclusion`; `lem-maincb-stage1-raw-refinement`; `lem-maincb-stage2-raw-extension`; `lem-maincb-stage3-raw-merge` | finite-minimum arithmetic; `approximate_algebras.tex:1317-1319,1414-1444,1557`; `AUDIT-MAIN-STRUCTURE-v2.md:215-220,279-301` | 4 / 2 | **SUPPORTED-WITH-DERIVATION.** Corrected to state the call-specific-\(t\) caveat and M16's absorbed Stage-2 scale; reset preservation is deliberately deferred to M19-R. |

M16 is the complete resolution of the \(C_{\rm s2}\) defect. Since
\(C_{\rm s2}\) and \(C_{\rm ext}\) are universal, replacing the EXT output
\(C_{\rm ext}(C_{\rm s2}t)\) by \(D_2t\) changes only a universal
coefficient. The condition \(C_{\rm s2}e_2\le e_{\rm ext}\) changes only a
universal positive radius. Neither depends on a dimension or induction
length.

## 5. G-S1 — unchanged hard serial stop

**G-S1 remains exactly after M18 and before every M19 replacement and MAIN
structural row.** The following ids remain absent:

1. `lem-stage1-rectified-nontrivial-projection`;
2. `lem-stage1-original-complementary-pair`, producing
   \(C_{\rm np},e_{\rm np}\); and
3. `lem-stage1-fresh-two-point-inclusion`, producing
   \(C_{\rm pair},e_{\rm pair}\).

Their source targets are `approximate_algebras.tex:917-969,1419-1424`.
This design does not reproduce or assume their polar proof. Until all three
are landed under their separate repaired and audited design, M19-S1 through
M28 are **BLOCKED / DO NOT LAND**. This is the same gate and location as v2
(`DESIGN-MAIN-STRUCTURE-v2.md:211-226`) and satisfies
`AUDIT-MAIN-STRUCTURE-v2.md:265-277,386-387`.

## 6. Closed post-gate envelopes and structural domain

The following four M19 replacements are conditional contracts. In
particular, M19-S2 and M19-S3 quantify the current maps as hypotheses; they
do not assert that M25 or M27 has already constructed those maps.

| row / proposed id | one-line `contract:` value | defs | exact `deps:` | provenance | budget | feasibility / audit delta |
|---|---|---|---|---|---|---|
| **M19-S1** `lem-maincb-stage1-call-envelope` | After G-S1, there are universal \(K_1\ge1\) and \(e_{{\rm call},1}>0\), with \(K_1e_{{\rm call},1}\le e_1\) and all G-S1/old-side prerequisite thresholds absorbed into \(e_{{\rm call},1}\), such that, if \(A\) is finite-dimensional, \(0\le\varepsilon\le e_{{\rm call},1}\), a supplied non-unital reset inclusion \(w:\mathbb C^m\to A\) has defect \(d_w\le c_0^{\rm cb}\varepsilon\), and some \(P_j=w(e_j)\) has \(\dim S_{P_j}>1\), then the three G-S1 producers and the literal old-side compression furnish an explicit Stage-1 raw-call datum satisfying M15 with base scale \(t_1=K_1\varepsilon\). | `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-partition-state` | `lem-maincb-direct-corner-envelope`; `lem-compcb-single-compression-transfer`; `lem-stage1-rectified-nontrivial-projection`; `lem-stage1-original-complementary-pair`; `lem-stage1-fresh-two-point-inclusion` | `approximate_algebras.tex:917-969,1419-1426` | 7 / 3 | **BLOCKED ON G-S1; OTHERWISE SUPPORTED-WITH-DERIVATION.** Names the supplied current \(w\); no Stage-2/3 map is hidden (§10.2). |
| **M19-S2** `lem-maincb-stage2-call-envelope` | There are universal \(K_2\ge\max\{1,L,c_0^{\rm cb}L\}\) and \(e_{{\rm call},2}>0\), with \(K_2e_{{\rm call},2}\le e_{\rm s2}\), such that, if a supplied MAIN partition state comes from a non-unital reset inclusion \(w:\mathbb C^m\to A\) with one-dimensional atomic images, has nonempty \(U\) contained in one equivalence class, \(j\notin U\) belonging to that same class, and \(R=U\cup\{j\}\), \(0\le\varepsilon\le e_{{\rm call},2}\), and a **supplied** current reset state \(v_U:M_{|U|}\to A_U\) is an extended isomorphism satisfying \(d_U\le c_0^{\rm cb}\varepsilon_U\), then \(t_2=K_2\varepsilon\) dominates every M13 geometric defect and \(\varepsilon_U,d_U,\varepsilon_R\), and M13 furnishes the explicit Stage-2 EXT raw-call datum with post-helper total defect at most \(C_{\rm s2}t_2\). | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-extcb-datum` | `lem-maincb-direct-corner-envelope`; `lem-maincb-stage2-extcb-datum` | `approximate_algebras.tex:1428-1441` | 5 / 3 | **SUPPORTED-WITH-DERIVATION.** Conditional on the named \(v_U\); it does not produce \(v_U\) (§10.2-4). |
| **M19-S3** `lem-maincb-stage3-call-envelope` | There are universal \(K_3\ge\max\{1,L,c_0^{\rm cb}L\}\) and \(e_{{\rm call},3}>0\), with \(K_3e_{{\rm call},3}\le e_{\rm cross}\), such that, if a supplied MAIN partition state comes from a non-unital reset inclusion \(w:\mathbb C^m\to A\) with one-dimensional atomic images, has disjoint nonempty unions \(U,V\) sharing no class and \(R=U\cup V\), \(0\le\varepsilon\le e_{{\rm call},3}\), and **supplied** current reset states \(v_U:B_U\to A_U\), \(v_V:B_V\to A_V\) are extended isomorphisms satisfying \(d_U\le c_0^{\rm cb}\varepsilon_U\) and \(d_V\le c_0^{\rm cb}\varepsilon_V\), then \(t_3=K_3\varepsilon\) dominates every M12 geometric defect and \(\varepsilon_U,\varepsilon_V,d_U,d_V,\varepsilon_R\), and M12 furnishes the explicit Stage-3 four-corner raw-call datum with \(\rho\le C_{\rm cross}t_3\). | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-four-corner-merging-datum` | `lem-maincb-direct-corner-envelope`; `lem-maincb-cross-class-merging-datum` | `approximate_algebras.tex:1428,1443` | 5 / 3 | **SUPPORTED-WITH-DERIVATION.** Conditional on both named maps; no M26/M27 existence is hidden (§10.2,4). |
| **M19-R** `lem-maincb-reset-invariant-preservation` | For any explicit scalar, Stage-1, Stage-2, or Stage-3 raw call into a recorded current corner \(A_R\), if its recorded defects satisfy \(d_{\rm raw}\le\delta_{\max}^{\rm cb}\) and \(\varepsilon_R\le\varepsilon_{\max}^{\rm cb}\), then the error-improvement map \(v_R\) satisfies \(d_R\le c_0^{\rm cb}\varepsilon_R\), preserves bijectivity, and leaves the source, target corner \(R\), and fixed amplification form unchanged. | `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-partition-state` | `lem-maincb-error-improvement`; `lem-maincb-reset-constant-ledger` | `approximate_algebras.tex:1317-1319,1435-1443,1557`; exact M03 contract at `lem-maincb-error-improvement.md:4` | 3 / 2 | **SUPPORTED-WITH-DERIVATION; NEW LOAD-BEARING ROW.** This proves RI(R), rather than placing it in “constructed from \(w\)” (§10.4). |
| **M20** `lem-maincb-structural-domain-ledger` | With the earlier witnesses, set \(K_{\rm call}:=\max\{1,L,c_0^{\rm cb},K_1,K_2,K_3\}\) and \(\varepsilon_{\rm MAIN}:=\min\{e_{\rm env},e_{{\rm call},1},e_{{\rm call},2},e_{{\rm call},3},r_{\rm reset}/K_{\rm call},e_{\sim}/K_{\rm call},e_{\rm full}/K_{\rm call},[2\max\{1,c_0^{\rm cb}K_{\rm call}\}]^{-1}\}>0\). Then \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\) implies \(\varepsilon\le e_{\rm env},e_{{\rm call},1},e_{{\rm call},2},e_{{\rm call},3}\); the scalar call uses \(t_0=\varepsilon\), while each non-scalar call type \(i\in\{1,2,3\}\) uses \(t_i=K_i\varepsilon\), and all four scales satisfy \(t_i\le K_{\rm call}\varepsilon\le r_{\rm reset},e_{\sim},e_{\rm full}\); moreover \(c_0^{\rm cb}K_{\rm call}\varepsilon\le\tfrac12\). | `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-partition-state` | `lem-maincb-error-improvement`; `lem-maincb-direct-corner-envelope`; `lem-maincb-full-corner-identification`; `lem-maincb-corner-equivalence`; `lem-maincb-reset-constant-ledger`; `lem-maincb-stage1-call-envelope`; `lem-maincb-stage2-call-envelope`; `lem-maincb-stage3-call-envelope` | finite-minimum arithmetic; `AUDIT-MAIN-STRUCTURE-v2.md:215-230,329-349` | 5 / 2 | **SUPPORTED-WITH-DERIVATION AFTER G-S1.** Domain rebuilt from closed envelopes. \(C_{\rm s2}\) is absent here because M16 already absorbed it (§10.3). |

The dependencies are acyclic:
M19-S2/S3 accept maps; M19-R proves what a completed call preserves; M20
only compares earlier constants. There is no edge from any M19 replacement
to M25, M26, or M27.

## 7. MAIN structural targets on the corrected ledger

| row / target id | one-line `contract:` value | defs | exact `deps:` | provenance | budget | feasibility / audit delta |
|---|---|---|---|---|---|---|
| **M21** `lem-maincb-initial-reset-inclusion` | For every finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra \(A\) with \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\), there is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(\mathbb C\to A\). | `def-maincb-reset-state`; `def-maincb-raw-call`; `def-operator-space` | `lem-maincb-initial-raw-inclusion`; `lem-maincb-reset-invariant-preservation`; `lem-maincb-structural-domain-ledger` | `approximate_algebras.tex:430-455,1317-1319,1417` | 3 / 2 | **SUPPORTED-WITH-DERIVATION.** Contract verbatim; corrected domain and M19-R replace invalid M19/M20 wiring (audit M21). |
| **M22** `lem-maincb-maximal-reset-selection` | If \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra with \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\), then the nonempty set of \(m\) admitting an extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(\mathbb C^m\to A\) has a maximum, because the lower norm is positive and hence \(m\le\dim_{\mathbb C}A\). | `def-maincb-reset-state`; `def-projection-basis` | `lem-maincb-structural-domain-ledger`; `lem-maincb-initial-reset-inclusion` | `approximate_algebras.tex:1417`; elementary finite-dimensional selection | 4 / 2 | **SUPPORTED-WITH-DERIVATION.** Verbatim. |
| **M23** `lem-maincb-stage1-strict-refinement` | If \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra with \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\) and an extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(w:\mathbb C^m\to A\) has some \(P_j=w(e_j)\) with \(\dim S_{P_j}>1\), then there is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(\mathbb C^{m+1}\to A\). | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call` | `lem-maincb-stage1-call-envelope`; `lem-maincb-stage1-raw-refinement`; `lem-maincb-reset-invariant-preservation`; `lem-maincb-structural-domain-ledger` | `approximate_algebras.tex:1419-1426` | 6 / 3 | **BLOCKED ON G-S1; OTHERWISE SUPPORTED-WITH-DERIVATION.** Contract verbatim; corrected call/state producers replace M19. |
| **M24** `lem-maincb-stage1-maximality` | If \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra with \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\) and \(w:\mathbb C^m\to A\) has maximum source dimension among all extended \(c_0^{\rm cb}\varepsilon\)-inclusions into \(A\), then every projection-basis image \(P_j=w(e_j)\) satisfies \(\dim S_{P_j}=1\). | `def-maincb-partition-state`; `def-projection-basis` | `lem-maincb-maximal-reset-selection`; `lem-maincb-stage1-strict-refinement` | `approximate_algebras.tex:1417-1426` | 3 / 2 | **SUPPORTED-WITH-DERIVATION AFTER G-S1.** Verbatim. |
| **M25** `lem-maincb-one-class-extension` | If \(A\) is finite-dimensional, \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\), a supplied MAIN partition state comes from a non-unital extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(w:\mathbb C^m\to A\), all atomic images \(P_j\) are one-dimensional, and \(C=\{j_1,\ldots,j_s\}\) is one equivalence class, then there is a current reset state \(v_C:M_s\to A_C\) that is an extended isomorphism and satisfies the **local** invariant \(d_C\le c_0^{\rm cb}\varepsilon_C\); moreover \(\varepsilon_C\le K_{\rm call}\varepsilon\), so the v2 bound \(d_C\le c_0^{\rm cb}K_{\rm call}\varepsilon\) follows. | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call` | `lem-maincb-corner-equivalence`; `lem-maincb-initial-raw-inclusion`; `lem-maincb-stage2-raw-extension`; `lem-maincb-stage2-call-envelope`; `lem-maincb-reset-invariant-preservation`; `lem-maincb-structural-domain-ledger` | `approximate_algebras.tex:1430-1441` | 7 / 3 | **SUPPORTED-WITH-DERIVATION.** Domain rebuilt and conclusion strengthened exactly as §10.4 requires (audit M25). |
| **M26** `lem-maincb-binary-block-merge` | If \(A\) is finite-dimensional, \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\), a supplied MAIN partition state comes from a non-unital reset inclusion \(w:\mathbb C^m\to A\) with one-dimensional atomic images, has disjoint nonempty unions \(U,V\) sharing no class, and supplied current reset states \(v_U:B_U\to A_U\), \(v_V:B_V\to A_V\) are extended isomorphisms satisfying \(d_U\le c_0^{\rm cb}\varepsilon_U\) and \(d_V\le c_0^{\rm cb}\varepsilon_V\), then there is a current reset state \(v_{U\cup V}:B_U\oplus B_V\to A_{U\cup V}\) satisfying \(d_{U\cup V}\le c_0^{\rm cb}\varepsilon_{U\cup V}\). | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-four-corner-merging-datum` | `lem-maincb-stage3-raw-merge`; `lem-maincb-stage3-call-envelope`; `lem-maincb-reset-invariant-preservation`; `lem-maincb-structural-domain-ledger` | `approximate_algebras.tex:1352-1359,1443` | 5 / 2 | **SUPPORTED-WITH-DERIVATION.** Union-stable domain rebuilt from the local invariant (audit M26). |
| **M27** `lem-maincb-stage3-finite-recombination` | If \(A\) is finite-dimensional, \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\), a supplied MAIN partition state comes from a non-unital reset inclusion \(w:\mathbb C^m\to A\) with one-dimensional atomic images and has all equivalence classes \(C_1,\ldots,C_q\), and **as initial data** every \(C_a\) has a finite-dimensional \(C^*\)-algebra \(B_{C_a}\) and current reset isomorphism \(v_{C_a}:B_{C_a}\to A_{C_a}\) satisfying \(d_{C_a}\le c_0^{\rm cb}\varepsilon_{C_a}\), then there is a current reset isomorphism \(\bigoplus_{a=1}^qB_{C_a}\to A_{\cup_aC_a}\) satisfying the same local invariant at the full union. | `def-maincb-partition-state`; `def-maincb-reset-state` | `lem-maincb-binary-block-merge` **only; no M25 dependency** | `approximate_algebras.tex:1443`; `AUDIT-MAIN-STRUCTURE-v2.md:244-249` | 4 / 2 | **SUPPORTED-WITH-DERIVATION.** Complete-family hypothesis and no-M25 edge retained exactly (§10.7). |
| **M28** `lem-maincb-structural-assembly` | There are universal \(C_{\rm struct}=c_0^{\rm cb}K_{\rm call}<\infty\) and \(e_{\rm struct}=\varepsilon_{\rm MAIN}>0\) such that every finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra \(A\), \(0\le\varepsilon\le e_{\rm struct}\), admits a finite-dimensional \(C^*\)-algebra \(B=\bigoplus_C M_{|C|}\) and one extended \(C_{\rm struct}\varepsilon\)-isomorphism \(v:B\to A\). | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-operator-space` | `lem-maincb-full-corner-identification`; `lem-maincb-corner-equivalence`; `lem-maincb-structural-domain-ledger`; `lem-maincb-maximal-reset-selection`; `lem-maincb-stage1-maximality`; `lem-maincb-one-class-extension`; `lem-maincb-stage3-finite-recombination` | `approximate_algebras.tex:1414-1444`; consumer at `lem-thmainext-conditional.md:4,26-30` | 7 / 3 | **BLOCKED ON G-S1; OTHERWISE SUPPORTED-WITH-DERIVATION.** Target contract verbatim; corrected domains and M28-only join (§10.7). |

### M25 proof plan for the stronger invariant

Order \(C=\{j_1,\ldots,j_s\}\) and let \(U_r=\{j_1,\ldots,j_r\}\).

1. **Base \(r=1\).** The atomic one-dimensional hypothesis gives
   \(\dim A_{\{j_1\}}=1\). Apply M14 in that target corner; its scalar raw
   map is bijective. M18 makes it M03-admissible, and M19-R produces
   \(v_{U_1}:M_1\to A_{U_1}\) with
   \(d_{U_1}\le c_0^{\rm cb}\varepsilon_{U_1}\).
2. **Inductive input.** Assume the actual current map
   \(v_{U_r}:M_r\to A_{U_r}\) is supplied and satisfies RI(\(U_r\)).
   M19-S2 names this map and packages M13's datum at base
   \(t_2=K_2\varepsilon\), with post-helper defect
   \(C_{\rm s2}t_2\).
3. **Raw extension.** Corrected M16 absorbs \(C_{\rm s2}\) and gives a raw
   \(D_2t_2\)-isomorphism into \(A_{U_{r+1}}\). M20 gives
   \(t_2\le r_{\rm reset}\), so M18 makes the raw map M03-admissible.
4. **Invariant preservation.** M19-R resets the raw map to
   \(v_{U_{r+1}}\) with
   \(d_{U_{r+1}}\le c_0^{\rm cb}\varepsilon_{U_{r+1}}\).

Thus the induction carries the local ambient defect, not the post-helper
datum defect and not an accumulated error. Its measure \(|C|-r\) decreases
by one.

## 8. Named hazards

### R19 — strict refinement measure

For an actual Stage-1 refinement sequence,
\[
 \mu_1=\dim_{\mathbb C}A-m\in\mathbb N
\]
decreases by exactly one when M23 replaces \(m\) by \(m+1\)
(`approximate_algebras.tex:1419-1426`). This proves termination but does not
infer global maximality from an arbitrary terminal point. M21 makes the
feasible dimension set nonempty, M22 selects a maximum from the bounded set,
and M23 contradicts that selected maximum if any atomic corner is not
one-dimensional. This retains the re-audit's valid R19 analysis
(`AUDIT-MAIN-STRUCTURE-v2.md:234-243`).

### R21 — two inductions and the M28-only join

M25 has state \((r,U_r,v_{U_r})\) and measure \(|C|-r\). M27 starts with the
**complete supplied family** \((v_C)_C\), has state
\((r,\cup_{a\le r}C_a,v_{\cup_{a\le r}C_a})\), and measure \(q-r\).
M27 has no M25 dependency. M28 invokes M25 once per class and is the only row
that supplies those outputs to M27. This retains the confirmed architecture
at `AUDIT-MAIN-STRUCTURE-v2.md:244-249`.

### R22 — zero-datum production and consumption

This subsection was missing from v2 and is now explicit.

1. M10 proves that the canonical relation in
   `def-maincb-partition-state` is an equivalence.
2. For disjoint unions \(U,V\) sharing no class, M11 applies exact
   dimension additivity in the original ambient to obtain both
   \(S^A_{P_U,P_V}=0\) and \(S^A_{P_V,P_U}=0\)
   (`approximate_algebras.tex:1363-1369`).
3. M11 then applies M08 separately in the two orientations and obtains both
   nested zero corners in \(A_{U\cup V}\).
4. M12 consumes those two **nested** zero spaces and installs the unique
   amplified maps \(0\to0\), together with the two named outer-compressed
   diagonal maps. Only then does a complete four-corner datum exist.
5. M19-S3 packages this result conditionally on the two current block maps;
   M17 merges it; M19-R preserves the union state.

Thus no original zero corner is reused silently in a compressed ambient, and
no off-diagonal map is asserted before its source and target have both been
proved zero. This clears the mathematical R22 issue while leaving all four
definition packages and result contracts subject to ratification
(`AUDIT-MAIN-STRUCTURE-v2.md:251-263`).

## 9. Dimension-freeness audit

| object | dimension-free check |
|---|---|
| P0 definitions | They carry only finite data and recorded defects; they introduce no constants. |
| \(K_{\rm step},K_{\rm disp},K_{\rm floor}\) | The finite-dimensional diagonal has norm one, including direct sums (`approximate_algebras.tex:1239-1254`), and one level-one correction is amplified entrywise (`ibid.:1508-1535`). |
| M05 | Exactly two diagonal blocks are merged; no atom or class sum enters the estimate (`ibid.:1325-1359`). |
| \(C_{\rm nest}\) | M07 is a fixed telescope of five exact landed estimates, independent of the number of atoms, ambient dimension, and amplification level. |
| \(C_{\rm out}\) | M09 adds two exact amplifications and finite-dimensional dimension equality; dimension is not a norm coefficient. |
| M11 | Additivity is used only to conclude that a sum of zero dimensions is zero; no quantitative cardinality sum is retained. |
| \(C_{\rm cross}\) | M12 always has four corners, independent of the number of classes already in \(U,V\). |
| \(C_{\rm s2}\) absorption | \(D_2\) may be chosen at least \(C_{\rm ext}C_{\rm s2}\), and \(e_2>0\) with \(C_{\rm s2}e_2\le e_{\rm ext}\). Both factors are earlier universal witnesses. |
| \(D_*,r_{\rm reset}\) | A fixed finite maximum/minimum of earlier universal witnesses; both exact M03 guards and the four-corner total-defect guard are present through M16/M17. |
| \(K_1,K_2,K_3,K_{\rm call}\) | Each envelope controls one literal call by a fixed maximum of earlier one-call constants. M20 also includes the fixed \(L,c_0^{\rm cb}\); the maximum is not over blocks or steps. |
| RI(\(U\)) | M19-R resets to \(c_0^{\rm cb}\varepsilon_U\) after every step. Therefore neither \(|C|\), \(q\), nor an induction index multiplies the error. |
| \(C_{\rm struct}\) | \(c_0^{\rm cb}K_{\rm call}\) is universal. The finite class count bounds only termination. |

`conj-extcb` explicitly records independence of rank, amplification,
ambient dimension, and block data
(`argument/lemmas/conj-extcb.md:23-40`). The four-corner merge is a fixed
four-map operation (`lem-extcb-four-corner-merge.md:4-6`). The corrected
\(C_{\rm s2}\) threading therefore introduces no dimension alarm.

## 10. Serial landing order

This is a genuine topological sort. A step may begin only after every
definition and result named in its `defs`/`deps` fields is landed.

0. **P0 STOP:** user-ratify and provision the four definition shards in §1;
   regenerate/check the definition index. No M-row lands before this.
1. Land M01, then M02. Rewire M03 from
   `lem-extcb-exact-target-correction` to M02; keep M03's contract verbatim.
2. Land M04, M05, and M06 with the exact direct dependencies in §4.1.
3. Land M07 and hostile-check both telescope directions. If either fails,
   stop at the declared M07 gap. Then land M08 and M09.
4. Land M10, then M11, M12, and M13.
5. Land M14, M15, corrected M16, and M17.
6. Land corrected M18. Every constant in \(r_{\rm reset}\) now has an
   earlier producer.
7. **G-S1 STOP, unchanged:** wait until the three named Stage-1 producer ids
   are landed under the separate S1 design.
8. Land M19-S1, M19-S2, M19-S3, then M19-R.
9. Land corrected M20.
10. Land M21 and M22.
11. Land M23, then M24.
12. Land M25.
13. Land M26, then conditional M27. There is no M25-to-M27 edge.
14. Land M28, which alone joins M25's family to M27.
15. Only after M28 and M19-R validate, propose the following exact
    dependency rewire for `lem-thmainext-conditional`, leaving its contract
    verbatim:

```yaml
deps: conj-hcb; conj-extcb; lem-hcb-column-hilbert-squared; lem-maincb-error-improvement; lem-maincb-reset-invariant-preservation; lem-maincb-structural-assembly; lem-extcb-four-corner-merge
```

The proposed parent has seven direct imports, hence a projected root plus
seven imports (**8 nodes / depth 2**). The reset constant ledger is available
transitively through M19-R; the complete MAIN subtree is available through
M28. This future dependency change is **ESCALATED**, not applied here.

## 11. Complete escalation ledger

### Definitions and definitions-to-results wiring

- **ESCALATED FOR USER RATIFICATION:** all four P0 definitions, including
  their exact fields, kinds, and statuses.
- **ESCALATED:** adding `def-operator-space` to M01-M03 and all amplified
  rows that use its vocabulary.
- **ESCALATED:** adding `def-maincb-reset-state`,
  `def-maincb-raw-call`, and `def-maincb-partition-state` to the exact rows
  listed above.

### Result contracts and dependencies

- **ESCALATED:** every new result contract M01-M02, M04-M18,
  M19-S1/S2/S3/R, and M20-M28.
- **CONTRACT UNCHANGED, DEPENDENCY ESCALATED:** M03 depends on
  `lem-maincb-improvement-iteration`; its ratified text remains verbatim.
- **EXACT DEPENDENCY ESCALATED:** M05, M07, and M09 import the named COMP
  rows exactly as displayed, including M09's two amplification/identity ids.
- **INTERFACE ESCALATED:** M11-M13 use canonical partition/reset/raw-call
  data; M12 and M13 quantify the current maps and RI hypotheses explicitly.
- **SCALE ESCALATED:** M13 has \(C_{\rm s2}\ge1\); M16 accepts total datum
  defect \(C_{\rm s2}t\) and absorbs it into \(D_2,e_2\); M18 records the
  call-specific-\(t\) caveat; M20 needs no extra \(C_{\rm s2}\) factor.
- **INVARIANT ESCALATED:** new M19-R proves
  \(d_R\le c_0^{\rm cb}\varepsilon_R\); M25-M27 consume/preserve that local
  form.
- **MAIN INTERFACES ESCALATED:** the corrected interfaces of all eight
  historical MAIN target ids remain subject to user ratification.
- **DOWNSTREAM DEPENDENCY ESCALATED:** the exact
  `lem-thmainext-conditional` rewire in §10; its contract is unchanged.

### Honest gaps and non-promotions

- **ESCALATED GAP G-S1:** the three producer ids remain absent.
- **CONDITIONAL GAP STOP M07:** failure of either fixed-telescope direction
  under hostile proof verification stops the plan.
- **NOT IN LOCAL REFS:** no numerical value is assigned to a big-\(O\)
  coefficient or radius; all thresholds are existential witnesses from
  exact earlier rows or finite minima of them.
- **NO STATUS PROMOTION:** every proposed MAIN row remains design-only;
  `lem-thmainext-conditional` remains `proved-mod-audit`; `op-classical`
  remains open.

## 12. Disposition of every binding re-audit finding

The following tables cover the findings in every section of
`AUDIT-MAIN-STRUCTURE-v2.md`. “Cleared” means cleared at design architecture
level only, never proved. In these tables, `audit:x-y` abbreviates the exact
locus
`docs/plans/2026-07-26-MAIN-STRUCTURE-design/AUDIT-MAIN-STRUCTURE-v2.md:x-y`.

### 12.1 Fatal defects, landed inputs, and load-bearing comparisons

| audit finding | disposition |
|---|---|
| Fatal A: M19 hides Stage-2/3 current maps, creating a semantic cycle or missing hypotheses (`audit:27-61`). | **CLEARED-BY M19-S2/M19-S3:** both maps are explicit hypotheses; neither envelope has a dependency on M25-M27. |
| Fatal A: M13's \(C_{\rm s2}t\) is not accepted by M16/M20 (`audit:42-60`). | **CLEARED-BY M16:** option 1 absorbs \(C_{\rm s2}\) into \(D_2,e_2\); M18/M20 test the base \(t\). |
| Fatal B: four definition packages are absent (`audit:63-86`). | **ESCALATED AT P0:** exact field-only proposals precede M01. |
| Amplified compression and identities are valid (`audit:94-98`). | **CLEARED-BY exact imports** in M05/M07/M09; no contract change to those leaves. |
| Amplified almost-containment is one-sided but supplies the needed Hermitian-side estimate (`audit:99-103`). | **CLEARED-BY M07's explicit two-direction telescope:** the reverse comparison is derived, not attributed to the one-sided leaf. |
| Corner algebra and rectangular product are valid (`audit:104-105`). | **CLEARED-BY exact imports** in M05/M07/M09. |
| Single compression is valid only for the ideal-unit setup (`audit:104-106`). | **CLEARED-BY scope separation:** it appears only in M15/M19-S1; M09 is the outer form. |
| One-dimensional product/dimension/additivity are valid (`audit:107-108`). | **CLEARED-BY M10-M13** using their exact ids. |
| `conj-extcb` is valid and dimension-free (`audit:109-111`). | **CLEARED-BY M16** with exact total-defect scaling. |
| Four-corner merge requires total smallness (`audit:112-113`). | **CLEARED-BY M17/M18** retaining \(\rho+\varepsilon_R\le a_{\rm merge}\). |
| Exact-target correction has a different codomain (`audit:114-116`). | **CLEARED-BY M01-M03:** it is not a logical dependency after the M03 rewire. |
| `lem-thmainext-conditional` needs the final uniform extended isomorphism and a future rewire (`audit:117-119`). | **ESCALATED WITH EXACT LOCUS:** M28 matches the contract; §10 gives the future deps. |
| M03 is a stated target, not an input theorem (`audit:120-121`). | **CLEARED-BY status discipline:** its contract stays `stated`; M01-M02 are its proposed proof subtree. |
| M07 is mathematically derivable but needs exact deps and internal expansions (`audit:125-164`). | **CLEARED-BY M07:** five ids and both expansion plans are explicit; verification failure remains an escalated stop. |
| M08 uses two injections and finite dimensionality (`audit:165-173`). | **CLEARED-BY unchanged M08.** |
| M09 is the correct distinct outer transfer but lacked exact amplification deps (`audit:175-194`). | **CLEARED-BY M09:** both exact amplification ids are direct dependencies. |

### 12.2 Every M-row verdict

| audit row finding (`audit:196-230`) | disposition |
|---|---|
| M01/M02 missing definition gate. | **CLEARED-BY P0;** contracts retained verbatim. |
| M03 contract valid; deps must rewire to M02. | **CLEARED-BY M03 dependency proposal;** contract verbatim. |
| M04 valid. | **CLEARED-BY unchanged M04** plus canonical partition def. |
| M05 vague deps. | **CLEARED-BY four exact COMP deps.** |
| M06 valid. | **CLEARED-BY unchanged M06.** |
| M07 exact deps/telescope required. | **CLEARED-BY M07.** |
| M08 valid. | **CLEARED-BY unchanged M08.** |
| M09 exact amplification/identity deps required. | **CLEARED-BY M09.** |
| M10 valid. | **CLEARED-BY unchanged M10.** |
| M11 needs canonical partition/raw-state data. | **CLEARED-BY P0 + corrected M11.** |
| M12 needs canonical data and explicit current maps. | **CLEARED-BY corrected M12.** |
| M13 must thread \(C_{\rm s2}\). | **CLEARED-BY corrected M13/M16.** |
| M14 valid. | **CLEARED-BY unchanged M14.** |
| M15 needs explicit hypotheses, not “Stage-1 call.” | **CLEARED-BY corrected M15 raw-call contract.** |
| M16 must absorb \(C_{\rm s2}\) or enlarge M20. | **CLEARED-BY corrected M16, option 1.** |
| M17 valid. | **CLEARED-BY unchanged M17.** |
| M18 has a common-\(t\) caveat. | **CLEARED-BY corrected M18/M20:** call-specific \(t_i\), finite maximum only. |
| M19 refuted. | **CLEARED-BY REPLACEMENT:** M19-S1/S2/S3/R; original M19 is not retained. |
| M20 refuted as wired. | **CLEARED-BY rebuilt M20** from the four closed M19 replacements and corrected M16. |
| M21 domain invalid. | **CLEARED-BY M21** using rebuilt M20 and M19-R. |
| M22 valid. | **CLEARED-BY unchanged M22.** |
| M23 needs corrected call/state producers. | **CLEARED-BY M19-S1/M19-R; ESCALATED ON G-S1.** |
| M24 valid. | **CLEARED-BY unchanged M24.** |
| M25 lacks the stronger invariant. | **CLEARED-BY corrected M25 + its four-step proof plan + M19-R.** |
| M26 domain invalid but merge mechanism valid. | **CLEARED-BY corrected local-invariant domain.** |
| M27 valid complete-family conditional theorem. | **CLEARED-BY retained complete-family hypothesis and M26-only dep.** |
| M28 target valid but subtree invalid. | **CLEARED-BY rebuilt subtree; ESCALATED ON P0/G-S1/M07 verification.** |

### 12.3 Hazards, G-S1, dimension, and inherited defects

| audit finding | disposition |
|---|---|
| R19 measure/maximality analysis valid (`audit:234-243`). | **CLEARED-BY §8 R19:** retained verbatim in substance. |
| R21 two inductions valid (`audit:244-249`). | **CLEARED-BY §8 R21:** M27 complete family and M28-only join retained. |
| R22 math valid but subsection/data definitions missing (`audit:251-263`). | **CLEARED-BY §8 R22 + P0.** |
| G-S1 is correctly located and independent of M19's failure (`audit:265-277`). | **CLEARED-BY unchanged G-S1 location; ESCALATED until its three rows land.** |
| No dimension alarm; M19/M20 failed only to expose universal coefficients (`audit:279-301`). | **CLEARED-BY §9:** all coefficients exposed; \(C_{\rm s2}\) remains universal. |
| First-audit threshold-cycle claim was not cleared by v2 (`audit:305-310`). | **CLEARED-BY conditional M19-S2/S3 + M19-R:** no backward existence edge. |
| First-audit nested comparison repair was valid (`audit:310`). | **CLEARED-BY retained M07/M08.** |
| First-audit outer compression repair valid with deps (`audit:311`). | **CLEARED-BY retained M09 + exact deps.** |
| First-audit complete-family repair valid (`audit:312`). | **CLEARED-BY retained M27/M28 shape.** |
| Original Stage-1 four-bijective misuse was cleared (`audit:316-317`). | **CLEARED-BY retained M05/M15.** |
| Original binary merge non-iterability was cleared (`audit:318`). | **CLEARED-BY retained union-stable M26.** |
| Original zero-corner reuse was cleared mathematically (`audit:319`). | **CLEARED-BY M11-M12 and explicit R22 subsection.** |
| Original reset guard remained incomplete because of \(C_{\rm s2}\) (`audit:320-321`). | **CLEARED-BY M16/M18.** |
| Original initial/maximal/final producers valid only after domain repair (`audit:322`). | **CLEARED-BY rebuilt M20/M21/M22/M28.** |

### 12.4 Landing-order, ledger, and all eight §10 requirements

| audit finding / requirement | disposition |
|---|---|
| Landing order omitted definitions (`audit:329-338`; §10.1). | **CLEARED-BY step 0 P0.** |
| Landing M19 before M25/M27 hid their outputs (`audit:339-340`; §10.2). | **CLEARED-BY conditional M19-S2/S3:** no later outputs are asserted. |
| M20 omitted \(C_{\rm s2}\) (`audit:341-342`; §10.3). | **CLEARED-BY M16 option 1.** |
| M25 had no closed invariant (`audit:343-344`; §10.4). | **CLEARED-BY M19-R and M25 proof plan.** |
| M09 dependency absent (`audit:345`; §10.5). | **CLEARED-BY exact M09 deps.** |
| G-S1 must remain in place (§10.6). | **CLEARED-BY steps 6-8 of §10.** |
| M27 complete family and M28-only join must remain (§10.7). | **CLEARED-BY M27/M28.** |
| Ledger omitted four definitions (`audit:351-357`; §10.8). | **CLEARED-BY §11 definitions ledger.** |
| Ledger omitted M09 exact dep correction (`audit:357`). | **CLEARED-BY §11 exact-dependency ledger.** |
| Ledger omitted M19/M20/M16 corrections (`audit:358`). | **CLEARED-BY §11 scale/invariant ledger.** |
| Ledger omitted future `lem-thmainext-conditional` rewire (`audit:359-365`). | **CLEARED-BY exact YAML proposal in §10 and ledger entry in §11.** |

No binding re-audit finding is papered over. The remaining items are exactly
the two serial gates P0 and G-S1, plus the declared future hostile
verification stop at M07.
