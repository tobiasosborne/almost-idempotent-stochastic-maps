# DESIGN-MAIN-STRUCTURE-v4 — prescribed closure repair

**Date:** 2026-07-27
**Role:** fresh independent fourth-repair designer
**Status:** **DESIGN ONLY; NON-RIGOROUS; DO NOT SEED.** Nothing below
authorizes a definition, contract, dependency, or status change. Every
proposed change is escalated for user ratification and fresh hostile review.

## 0. Verdict and exact delta from v3

**Verdict: DESIGNED-CLOSABLE, conditional on two explicit serial gates.**
This is the prescribed narrow repair of
`DESIGN-MAIN-STRUCTURE-v3.md` under the binding
`AUDIT-MAIN-STRUCTURE-v3.md`. It does not redesign any audit-confirmed
mechanism. No dimension-dependent constant, counterexample to Kitaev's
theorem, or route-level obstruction was found. The two unchanged gates are:

1. **P0 — definition provisioning and user ratification:** the four missing
   theorem-free vocabulary/data shards must be ratified and landed before
   M01; and
2. **G-S1 — unchanged Stage-1 producer gate:** the three absent Stage-1
   producers must be landed before any M19 replacement or structural target.

The exact changes from v3, and only those changes, are:

| v4 change | binding cause |
|---|---|
| Replace P0's field summaries by four schema-complete shard proposals. `def-operator-space` reproduces only the byte-verbatim Definition block at TeX 1453-1464; the rectangular construction at 1467-1475 is provenance/notation only. The three original shards remain draft and consensus-pending. | Audit §2; brief correction 7. |
| State that `def-maincb-partition-state` records neither the ambient defect nor the defect/unit tag of \(w\); every consumer needing those bounds quantifies them. Record that one current-union field cannot provide both \(U,V\) states. | Audit §2 partition-state verdict; brief correction 7. |
| Copy M03's landed `contract:` value byte-for-byte and change only its dependency to M02. Make M04's finite-dimensional extended-\(\varepsilon\) ambient hypothesis explicit. | Audit §4 M03-M04; brief correction 6. |
| Add \(\varepsilon_A\le t\) to M11-M13; add M07 directly to M12 and M13; make M13 explicitly produce a closed EXT datum with \(P_U^R,P_j^R\). | Audit §§1,4; brief correction 5. |
| Restore M19-S1's unit-preserving v2 domain: \(A\) is an extended \(\varepsilon\)-\(C^*\)-algebra and \(w\) is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion. | Audit fatal defect A; brief correction 1. |
| Give M19-S2/S3 and M26/M27 the same explicit \(A,w\) domain, so M04 licenses the original and nested ambient/map bounds. M25 also restores the v2 global \(w\)-bound. | Audit fatal defect B and retained-contract diff; brief corrections 2 and 8. |
| Make M19-R assume that the literal output is an actual extended \(d_{\rm raw}\)-inclusion/isomorphism from its named finite-dimensional \(C^*\)-algebra into \(A_R\), in addition to the two numerical guards. | Audit fatal defect C; brief correction 3. |
| Add the compressed-corner scalar call as a distinct literal type with \(t_{\rm atom}=K_{\rm call}\varepsilon\). M20 proves \(\varepsilon_{\{j\}}\le L\varepsilon\le t_{\rm atom}\le r_{\rm reset}\); M25 imports M04 directly and uses that call in its base step. | Audit fatal defect D; brief correction 4. |
| Rebuild the landing order, escalation ledger, and complete v3-audit disposition around precisely these changes. | Audit §§8-11; brief deliverable. |

Every row that `AUDIT-MAIN-STRUCTURE-v3.md` marked **VALID** is retained
verbatim. M28's target contract, the M28-only join, M27's complete-family
hypothesis, M16's \(C_{\rm s2}\) absorption, R19/R21, and G-S1's placement are
unchanged. Rows marked VALID-WITH-CORRECTIONS change only as prescribed
above.

The pinned source is
`refs/kitaev-2405.02434/approximate_algebras.tex`, SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`,
matching `refs/manifest/checksums.sha256:4`. The source itself says that its
big-\(O\) functions do not depend on additional data
(`approximate_algebras.tex:458`) and states dimension-freeness in
`th_main` and `th_main_ext` (`ibid.:460-462,1538-1540`). Those statements are
source provenance, not a status promotion of this design.

## 1. P0 — schema-complete definition proposals and ratification gate

**HARD STOP BEFORE M01.** None of the four ids below exists in the generated
38-term definition index (`definitions/INDEX.md:1-43`). All four proposals
are **ESCALATED FOR USER RATIFICATION**. They contain fields and notation
only, in accordance with R35. They contain no existence, smallness,
estimate, preservation, success, iteration, or termination assertion.

### 1.1 `def-operator-space` — cited, byte-verbatim Definition block only

```yaml
---
id: def-operator-space
term: operator space
aliases: self-adjoint operator space
kind: cited
status: draft
source: kitaev-2405.02434
locus: approximate_algebras.tex:1453-1464
sha256: e7eb512a2ec2438d
---
```

The proposed statement is exactly the following local-source block, with no
rectangular norms or consequences inserted as primitive fields:

```latex
\begin{Definition}\label{def:opspace}
A complex vector space $\calL$ is called an \emph{operator space} if each space $\Ma{n}\otimes\calL$ (for $n=1,2,\ldots$) is equipped with a norm $\|\cdot\|_n$ satisfying the following axioms:
\begin{alignat}{2}
\label{ax_R1}
\|AXB\|_n &\le\|A\|\ts\|X\|_k\ts\|B\|\qquad &
&(A\in\Ma{n,k},\quad B\in\Ma{k,n},\quad X\in\Ma{k}\otimes\calL),\\[3pt]
\label{ax_R2}
\left\|\begin{pmatrix}X&0\\ 0&Y\end{pmatrix}\right\|_{k+n} &=\max\bigl\{\|X\|_k,\|Y\|_n\bigr\}\qquad &
& (X\in\Ma{k}\otimes\calL,\quad Y\in\Ma{n}\otimes\calL).
\end{alignat}
The norm on $\calL$ itself is defined by identifying $\calL$ with $\Ma{1}\otimes\calL$. An operator space is called \emph{self-adjoint} if it is equipped with a conjugate linear involution $\dagger$ that preserves all norms $\|\cdot\|_n$.
\end{Definition}
```

**Notes / provenance.** The rectangular inclusions and induced norms at
`approximate_algebras.tex:1467-1475` are derived notation/consequences only.
They may be referenced in provenance and later proofs, but are not fields of
this cited definition. Locking remains subject to the repository byte-match
gate.

### 1.2 `def-maincb-reset-state` — original datum only

```yaml
---
id: def-maincb-reset-state
term: MAIN-CB current reset state
aliases: MAIN reset state
kind: original
status: draft
source: internal
locus: DESIGN-FUDW-DECOMP-v4.1.md:419-423; DESIGN-MAIN-STRUCTURE-v4.md §1.2
sha256: -
consensus: pending user ratification; design-only proposal 2026-07-27
---
```

**Statement.** A *MAIN-CB current reset state* consists of a current index
union \(U\); its compressed ambient \(A_U\); a recorded ambient defect
\(\varepsilon_U\); a named finite-dimensional \(C^*\)-algebra \(B_U\); a
supplied level-one map \(v_U:B_U\to A_U\); the fixed family
\((I_n\otimes v_U)_{n\ge1}\); a recorded map-defect number \(d_U\); and a
supplied tag saying whether the map is an extended inclusion or extended
isomorphism.

**Notes / provenance.** The tag is hypothesis data, not an existence or
success assertion. The shard does not assert RI(\(U\)), smallness,
admissibility, preservation, or construction.

### 1.3 `def-maincb-raw-call` — original literal-call record only

```yaml
---
id: def-maincb-raw-call
term: MAIN-CB raw call
aliases: MAIN raw-call datum
kind: original
status: draft
source: internal
locus: DESIGN-FUDW-DECOMP-v4.1.md:424-428; DESIGN-MAIN-STRUCTURE-v4.md §1.3
sha256: -
consensus: pending user ratification; design-only proposal 2026-07-27
---
```

**Statement.** A *MAIN-CB raw call* consists of a literal call-type tag
(global scalar, compressed-corner scalar, Stage 1, Stage 2, or Stage 3);
the supplied input reset states/maps; the named finite-dimensional
\(C^*\)-algebra source and explicit target corner; a pre-helper base scale
\(t\); any post-helper datum scale; the literal output level-one map and its
fixed amplification family; the recorded target ambient defect
\(\varepsilon_{\rm target}\); and a recorded raw-defect number
\(d_{\rm raw}\).

**Notes / provenance.** A recorded number does not assert that the literal
map is an extended inclusion or isomorphism. No hidden domain, smallness,
success, reset, preservation, or iteration clause is present. The two scalar
tags are distinct because M21 uses \(t_0=\varepsilon\), whereas M25's
compressed-corner base uses \(t_{\rm atom}=K_{\rm call}\varepsilon\).

### 1.4 `def-maincb-partition-state` — original geometry only

```yaml
---
id: def-maincb-partition-state
term: MAIN-CB partition state
aliases: MAIN partition state
kind: original
status: draft
source: internal
locus: DESIGN-MAIN-STRUCTURE-v4.md §1.4
sha256: -
consensus: pending user ratification; design-only proposal 2026-07-27
---
```

**Statement.** A *MAIN-CB partition state* consists of a finite atomic index
set \(J\); an ambient \(A\); a supplied commutative map
\(w:\mathbb C^J\to A\); \(P_j=w(e_j)\); the conditional relation
\(j\sim k\iff\dim S^A_{P_j,P_k}=1\); when this relation is an equivalence,
its class family \(\mathcal C\); for \(U\subseteq J\),
\(P_U=\sum_{j\in U}P_j\) and \(A_U=S^A_{P_U}\); one current union \(U\) of
classes; and a reference to one separately supplied
`def-maincb-reset-state` for that union.

**Notes / provenance.** This shard records neither the global ambient defect
nor a defect/unit tag for \(w\). Every consuming result that needs those
bounds must quantify \(A\) as an extended \(\varepsilon\)-\(C^*\)-algebra
and \(w\) as an extended inclusion explicitly. It asserts neither that
\(\sim\) is an equivalence nor that a current map exists. Its single current
union cannot supply simultaneous \(U,V\) data: M12 and M19-S3 require two
separately supplied reset states.

The distinction between the last three packages is load-bearing:
partition state records geometry, reset state records one supplied map and
its numerical/tag data, and raw call records one literal attempted call.
Only result rows may prove admissibility or preservation.

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
The global scalar call has \(t_0=\varepsilon\). The distinct scalar call
inside the compressed atomic corner has
\[
 \tag{atom-scale}t_{\rm atom}=K_{\rm call}\varepsilon.
\]
M04 gives
\(\varepsilon_{\{j\}}\le L\varepsilon\le t_{\rm atom}\), and M20 shrinks
the global domain so \(t_{\rm atom}\le r_{\rm reset}\). Every literal call
is therefore checked with its own base scale; no scalar call into a
compressed corner is incorrectly tested at \(t_0\).

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
| **M03** `lem-maincb-error-improvement` | Complete error improvement: there are universal epsilon_max^cb>0, delta_max^cb>0 and c_0^cb<infinity such that every extended delta-inclusion v:B->A from a finite-dimensional C*-algebra B into an extended epsilon-C*-algebra A with 0<=epsilon<=epsilon_max^cb and 0<=delta<=delta_max^cb can be replaced by an extended c_0^cb*epsilon-inclusion v_tilde:B->A that is bijective whenever v is bijective. | `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-improvement-iteration` | `approximate_algebras.tex:1192,1317-1319,1483-1509,1557`; byte-for-byte landed contract at `argument/lemmas/lem-maincb-error-improvement.md:4` | 5 / 3 | **SUPPORTED-WITH-DERIVATION; CONTRACT BYTE-UNCHANGED.** Only `deps:` rewires from exact-target correction to M02. |
| **M04** `lem-maincb-direct-corner-envelope` | There are universal \(L\ge1\) and \(e_{\rm env}>0\) such that, if \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra, \(0\le\varepsilon\le e_{\rm env}\), and \(w:\mathbb C^m\to A\) is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion, then every nonempty \(U\) has \(P_U\) a \(c_0^{\rm cb}\varepsilon\)-projection, every \(A_U=S^A_{P_U}\) is an extended \(L\varepsilon\)-\(C^*\)-algebra, and for \(U\subseteq R\) all subordination and complementarity errors among \(P_U,P_{R\setminus U},P_R\) are at most \(L\varepsilon\). | `def-maincb-partition-state`; `def-compressed-corner`; `def-delta-projection` | `lem-maincb-error-improvement`; `lem-compcb-corner-algebra` | `approximate_algebras.tex:1068-1084,1367-1368,1428-1435` | 6 / 3 | **SUPPORTED-WITH-DERIVATION.** Audit-v3 correction makes the ambient hypothesis self-contained; P0 supplies only notation/data. |
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
| **M11** `lem-maincb-cross-union-zero-corners` | There is a universal \(e_{\rm zero}>0\) such that, if \(A\) is a finite-dimensional extended \(\varepsilon_A\)-\(C^*\)-algebra with \(\varepsilon_A\le t\), a supplied MAIN partition state has \(w:\mathbb C^m\to A\) a non-unital extended \(t\)-inclusion with one-dimensional images \(P_j\), \(U,V\) are disjoint nonempty unions sharing no equivalence class, \(R=U\cup V\), and \(t\le e_{\rm zero}\), then \(\dim S^A_{P_U,P_V}=\dim S^A_{P_V,P_U}=0\) and \(\dim S^{A_R}_{P_U^R,P_V^R}=\dim S^{A_R}_{P_V^R,P_U^R}=0\). | `def-maincb-partition-state`; `def-compressed-corner` | `lem-maincb-nested-corner-dimension-transport`; `lem-maincb-corner-equivalence`; `lem-extcb-corner-dimension-additivity` | `approximate_algebras.tex:1363-1369,1428,1443` | 6 / 3 | **SUPPORTED-WITH-DERIVATION.** Audit-v3 correction restores the original ambient-defect hypothesis used by M08/M10. |
| **M12** `lem-maincb-cross-class-merging-datum` | There are universal \(C_{\rm cross}\ge1\) and \(e_{\rm cross}>0\) such that, if \(A\) is a finite-dimensional extended \(\varepsilon_A\)-\(C^*\)-algebra with \(\varepsilon_A\le t\), a supplied MAIN partition state comes from a non-unital extended \(t\)-inclusion \(w:\mathbb C^m\to A\) with one-dimensional images \(P_j\), has disjoint nonempty unions \(U,V\) sharing no class and \(R=U\cup V\), and two separately supplied current reset states \(v_U:B_U\to A_U\), \(v_V:B_V\to A_V\) are extended isomorphisms satisfying \(\varepsilon_U,\varepsilon_V,d_U,d_V\le t\le e_{\rm cross}\), \(d_U\le c_0^{\rm cb}\varepsilon_U\), and \(d_V\le c_0^{\rm cb}\varepsilon_V\), then M07 makes \(P_U^R,P_V^R\) common-quantitative-defect target projections, the two M09 outer-compressed diagonal maps and the unique maps between the two M11 zero corners form the explicit Stage-3 raw-call amplified four-corner datum in \(A_R\), with common defect \(\rho\le C_{\rm cross}t\). | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-four-corner-merging-datum` | `lem-maincb-error-improvement`; `lem-maincb-nested-corner-comparison`; `lem-maincb-outer-compression-transfer`; `lem-maincb-cross-union-zero-corners` | `approximate_algebras.tex:1325-1345,1358,1363-1369,1443` | 9 / 3 | **SUPPORTED-WITH-DERIVATION.** Audit-v3 correction restores the ambient bound and direct M07 export; the two reset states are separate supplied data. |
| **M13** `lem-maincb-stage2-extcb-datum` | There are universal \(C_{\rm s2}\ge1\) and \(e_{\rm s2}>0\) such that, if \(A\) is a finite-dimensional extended \(\varepsilon_A\)-\(C^*\)-algebra with \(\varepsilon_A\le t\), a supplied MAIN partition state comes from a non-unital extended \(t\)-inclusion \(w:\mathbb C^m\to A\) with one-dimensional images \(P_j\), has nonempty \(U\), \(j\notin U\), \(\dim S^A_{P_k,P_j}=1\) for every \(k\in U\), and \(R=U\cup\{j\}\), and a supplied current reset state \(v_U:M_{|U|}\to A_U\) is an extended isomorphism satisfying \(\varepsilon_U,d_U\le t\le e_{\rm s2}\) and \(d_U\le c_0^{\rm cb}\varepsilon_U\), then M07 makes \(P_U^R,P_j^R\) quantitative projections in the extended corner \(A_R\), and together with the M09 outer-compressed isomorphism they satisfy every `def-extcb-datum` clause—approximate complementarity to \(I_{A_R}\), one-dimensional \(S_{P_j^R}\), nonzero \(S_{P_U^R,P_j^R}\), and total error \(e=\delta+\varepsilon_{A_R}\)—with \(e\le C_{\rm s2}t\), forming the explicit Stage-2 raw-call closed EXT-CB datum in \(A_R\). | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-extcb-datum` | `lem-maincb-error-improvement`; `lem-maincb-nested-corner-comparison`; `lem-maincb-nested-corner-dimension-transport`; `lem-maincb-outer-compression-transfer`; `lem-maincb-corner-equivalence`; `lem-extcb-corner-dimension-additivity` | `approximate_algebras.tex:1363-1412,1430-1441`; `definitions/def-extcb-datum.md:13-17` | 10 / 3 | **SUPPORTED-WITH-DERIVATION.** Audit-v3 correction restores the ambient/M07 inputs and makes datum closure explicit; the \(C_{\rm s2}\) output is unchanged. |

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
| **M19-S1** `lem-maincb-stage1-call-envelope` | After G-S1, there are universal \(K_1\ge1\) and \(e_{{\rm call},1}>0\), with \(K_1e_{{\rm call},1}\le e_1\) and all G-S1/old-side prerequisite thresholds absorbed into \(e_{{\rm call},1}\), such that, if \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra, \(0\le\varepsilon\le e_{{\rm call},1}\), \(w:\mathbb C^m\to A\) is a supplied extended \(c_0^{\rm cb}\varepsilon\)-inclusion (including its unit clause), and some \(P_j=w(e_j)\) has \(\dim S_{P_j}>1\), then the three G-S1 producers and the literal old-side compression furnish an explicit Stage-1 raw-call datum satisfying M15 with base scale \(t_1=K_1\varepsilon\). | `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-partition-state` | `lem-maincb-direct-corner-envelope`; `lem-compcb-single-compression-transfer`; `lem-stage1-rectified-nontrivial-projection`; `lem-stage1-original-complementary-pair`; `lem-stage1-fresh-two-point-inclusion` | `approximate_algebras.tex:917-969,1419-1426` | 7 / 3 | **BLOCKED ON G-S1; OTHERWISE SUPPORTED-WITH-DERIVATION.** Audit-v3 defect A is cleared by the explicit ambient and unit-preserving v2 inclusion hypotheses. |
| **M19-S2** `lem-maincb-stage2-call-envelope` | There are universal \(K_2\ge\max\{1,L,c_0^{\rm cb}L\}\) and \(e_{{\rm call},2}>0\), with \(K_2e_{{\rm call},2}\le e_{\rm s2}\), such that, if \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra, \(w:\mathbb C^m\to A\) is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion with one-dimensional atomic images, a supplied MAIN partition state has nonempty \(U\) contained in one equivalence class, \(j\notin U\) belonging to that same class, and \(R=U\cup\{j\}\), \(0\le\varepsilon\le e_{{\rm call},2}\), and a **supplied** current reset state \(v_U:M_{|U|}\to A_U\) is an extended isomorphism satisfying \(d_U\le c_0^{\rm cb}\varepsilon_U\), then M04 gives \(\varepsilon_U,\varepsilon_R\le L\varepsilon\), so \(t_2=K_2\varepsilon\) dominates every M13 geometric defect and \(\varepsilon_U,d_U,\varepsilon_R\), and M13 furnishes the explicit Stage-2 EXT raw-call datum with post-helper total defect at most \(C_{\rm s2}t_2\). | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-extcb-datum` | `lem-maincb-direct-corner-envelope`; `lem-maincb-stage2-extcb-datum` | `approximate_algebras.tex:1428-1441` | 5 / 3 | **SUPPORTED-WITH-DERIVATION.** Audit-v3 defect B is cleared by the explicit global ambient and \(w\)-defect/unit hypotheses; \(v_U\) remains supplied. |
| **M19-S3** `lem-maincb-stage3-call-envelope` | There are universal \(K_3\ge\max\{1,L,c_0^{\rm cb}L\}\) and \(e_{{\rm call},3}>0\), with \(K_3e_{{\rm call},3}\le e_{\rm cross}\), such that, if \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra, \(w:\mathbb C^m\to A\) is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion with one-dimensional atomic images, a supplied MAIN partition state has disjoint nonempty unions \(U,V\) sharing no class and \(R=U\cup V\), \(0\le\varepsilon\le e_{{\rm call},3}\), and **two separately supplied** current reset states \(v_U:B_U\to A_U\), \(v_V:B_V\to A_V\) are extended isomorphisms satisfying \(d_U\le c_0^{\rm cb}\varepsilon_U\) and \(d_V\le c_0^{\rm cb}\varepsilon_V\), then M04 gives \(\varepsilon_U,\varepsilon_V,\varepsilon_R\le L\varepsilon\), so \(t_3=K_3\varepsilon\) dominates every M12 geometric defect and \(\varepsilon_U,\varepsilon_V,d_U,d_V,\varepsilon_R\), and M12 furnishes the explicit Stage-3 four-corner raw-call datum with \(\rho\le C_{\rm cross}t_3\). | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-four-corner-merging-datum` | `lem-maincb-direct-corner-envelope`; `lem-maincb-cross-class-merging-datum` | `approximate_algebras.tex:1428,1443` | 5 / 3 | **SUPPORTED-WITH-DERIVATION.** Audit-v3 defect B is cleared by the explicit base state; both later maps remain supplied hypotheses. |
| **M19-R** `lem-maincb-reset-invariant-preservation` | For any explicit global-scalar, compressed-corner-scalar, Stage-1, Stage-2, or Stage-3 raw call into a recorded current corner \(A_R\), assume \(A_R\) is an extended \(\varepsilon_R\)-\(C^*\)-algebra and the literal output map \(u_R:B_R\to A_R\) is an extended \(d_{\rm raw}\)-inclusion (respectively isomorphism) from the raw call's named finite-dimensional \(C^*\)-algebra source \(B_R\). If \(d_{\rm raw}\le\delta_{\max}^{\rm cb}\) and \(\varepsilon_R\le\varepsilon_{\max}^{\rm cb}\), then M03 produces an error-improved map \(v_R:B_R\to A_R\) satisfying \(d_R\le c_0^{\rm cb}\varepsilon_R\), preserves bijectivity when \(u_R\) is bijective, and leaves the source, target corner \(R\), and fixed amplification form unchanged. | `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-partition-state` | `lem-maincb-error-improvement`; `lem-maincb-reset-constant-ledger` | `approximate_algebras.tex:1317-1319,1435-1443,1557`; exact M03 contract at `lem-maincb-error-improvement.md:4` | 3 / 2 | **SUPPORTED-WITH-DERIVATION; LOAD-BEARING.** Audit-v3 defect C is cleared: the data-only raw record is not read as an inclusion theorem. |
| **M20** `lem-maincb-structural-domain-ledger` | With the earlier witnesses, set \(K_{\rm call}:=\max\{1,L,c_0^{\rm cb},K_1,K_2,K_3\}\) and \(\varepsilon_{\rm MAIN}:=\min\{e_{\rm env},e_{{\rm call},1},e_{{\rm call},2},e_{{\rm call},3},r_{\rm reset}/K_{\rm call},e_{\sim}/K_{\rm call},e_{\rm full}/K_{\rm call},[2\max\{1,c_0^{\rm cb}K_{\rm call}\}]^{-1}\}>0\). Then \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\) implies \(\varepsilon\le e_{\rm env},e_{{\rm call},1},e_{{\rm call},2},e_{{\rm call},3}\); the global scalar call uses \(t_0=\varepsilon\), the distinct compressed-corner scalar call uses \(t_{\rm atom}=K_{\rm call}\varepsilon\), and each Stage-\(i\) call uses \(t_i=K_i\varepsilon\) for \(i\in\{1,2,3\}\). All five scales are at most \(K_{\rm call}\varepsilon\le r_{\rm reset},e_{\sim},e_{\rm full}\); for every atom M04 gives \(\varepsilon_{\{j\}}\le L\varepsilon\le t_{\rm atom}\le r_{\rm reset}\); and \(c_0^{\rm cb}K_{\rm call}\varepsilon\le\tfrac12\). | `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-partition-state` | `lem-maincb-error-improvement`; `lem-maincb-direct-corner-envelope`; `lem-maincb-full-corner-identification`; `lem-maincb-corner-equivalence`; `lem-maincb-reset-constant-ledger`; `lem-maincb-stage1-call-envelope`; `lem-maincb-stage2-call-envelope`; `lem-maincb-stage3-call-envelope` | finite-minimum arithmetic; `AUDIT-MAIN-STRUCTURE-v3.md` §§1D,6 | 5 / 2 | **SUPPORTED-WITH-DERIVATION AFTER G-S1.** Audit-v3 defect D is cleared; \(C_{\rm s2}\) remains absent because M16 already absorbed it. |

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
| **M25** `lem-maincb-one-class-extension` | If \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra, \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\), a supplied MAIN partition state comes from an extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(w:\mathbb C^m\to A\), all atomic images \(P_j\) are one-dimensional, and \(C=\{j_1,\ldots,j_s\}\) is one equivalence class, then there is a current reset state \(v_C:M_s\to A_C\) that is an extended isomorphism and satisfies the **local** invariant \(d_C\le c_0^{\rm cb}\varepsilon_C\); moreover \(\varepsilon_C\le K_{\rm call}\varepsilon\), so the v2 bound \(d_C\le c_0^{\rm cb}K_{\rm call}\varepsilon\) follows. | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call` | `lem-maincb-direct-corner-envelope`; `lem-maincb-corner-equivalence`; `lem-maincb-initial-raw-inclusion`; `lem-maincb-stage2-raw-extension`; `lem-maincb-stage2-call-envelope`; `lem-maincb-reset-invariant-preservation`; `lem-maincb-structural-domain-ledger` | `approximate_algebras.tex:1430-1441` | 7 / 3 | **SUPPORTED-WITH-DERIVATION.** Audit-v3 defect D adds direct M04 and the licensed atomic scale; the global v2 inclusion hypothesis is restored. |
| **M26** `lem-maincb-binary-block-merge` | If \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra, \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\), a supplied MAIN partition state comes from an extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(w:\mathbb C^m\to A\) with one-dimensional atomic images, has disjoint nonempty unions \(U,V\) sharing no class, and two separately supplied current reset states \(v_U:B_U\to A_U\), \(v_V:B_V\to A_V\) are extended isomorphisms satisfying \(d_U\le c_0^{\rm cb}\varepsilon_U\) and \(d_V\le c_0^{\rm cb}\varepsilon_V\), then there is a current reset state \(v_{U\cup V}:B_U\oplus B_V\to A_{U\cup V}\) satisfying \(d_{U\cup V}\le c_0^{\rm cb}\varepsilon_{U\cup V}\). | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-four-corner-merging-datum` | `lem-maincb-stage3-raw-merge`; `lem-maincb-stage3-call-envelope`; `lem-maincb-reset-invariant-preservation`; `lem-maincb-structural-domain-ledger` | `approximate_algebras.tex:1352-1359,1443` | 5 / 2 | **SUPPORTED-WITH-DERIVATION.** Audit-v3 defect B restores the global ambient and unit/defect-controlled \(w\) domain; the union-stable invariant is unchanged. |
| **M27** `lem-maincb-stage3-finite-recombination` | If \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra, \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\), a supplied MAIN partition state comes from an extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(w:\mathbb C^m\to A\) with one-dimensional atomic images and has all equivalence classes \(C_1,\ldots,C_q\), and **as initial data** every \(C_a\) has a finite-dimensional \(C^*\)-algebra \(B_{C_a}\) and current reset isomorphism \(v_{C_a}:B_{C_a}\to A_{C_a}\) satisfying \(d_{C_a}\le c_0^{\rm cb}\varepsilon_{C_a}\), then there is a current reset isomorphism \(\bigoplus_{a=1}^qB_{C_a}\to A_{\cup_aC_a}\) satisfying the same local invariant at the full union. | `def-maincb-partition-state`; `def-maincb-reset-state` | `lem-maincb-binary-block-merge` **only; no M25 dependency** | `approximate_algebras.tex:1443`; `AUDIT-MAIN-STRUCTURE-v3.md` §§6-8 | 4 / 2 | **SUPPORTED-WITH-DERIVATION.** Audit-v3 defect B restores the global \(A,w\) bounds; complete-family hypothesis and M26-only dependency are unchanged. |
| **M28** `lem-maincb-structural-assembly` | There are universal \(C_{\rm struct}=c_0^{\rm cb}K_{\rm call}<\infty\) and \(e_{\rm struct}=\varepsilon_{\rm MAIN}>0\) such that every finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra \(A\), \(0\le\varepsilon\le e_{\rm struct}\), admits a finite-dimensional \(C^*\)-algebra \(B=\bigoplus_C M_{|C|}\) and one extended \(C_{\rm struct}\varepsilon\)-isomorphism \(v:B\to A\). | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-operator-space` | `lem-maincb-full-corner-identification`; `lem-maincb-corner-equivalence`; `lem-maincb-structural-domain-ledger`; `lem-maincb-maximal-reset-selection`; `lem-maincb-stage1-maximality`; `lem-maincb-one-class-extension`; `lem-maincb-stage3-finite-recombination` | `approximate_algebras.tex:1414-1444`; consumer at `lem-thmainext-conditional.md:4,26-30` | 7 / 3 | **BLOCKED ON G-S1; OTHERWISE SUPPORTED-WITH-DERIVATION.** Target contract verbatim; corrected domains and M28-only join (§10.7). |

### M25 proof plan for the stronger invariant

Order \(C=\{j_1,\ldots,j_s\}\) and let \(U_r=\{j_1,\ldots,j_r\}\).

1. **Base \(r=1\).** The atomic one-dimensional hypothesis gives
   \(\dim A_{\{j_1\}}=1\). Directly import M04 to obtain
   \(\varepsilon_{\{j_1\}}\le L\varepsilon\le
   t_{\rm atom}=K_{\rm call}\varepsilon\). M20 gives
   \(t_{\rm atom}\le r_{\rm reset}\). Apply M14 in that target corner at
   this distinct compressed-corner scalar scale; its scalar raw map is
   bijective. M18 makes that literal call M03-admissible, and the corrected
   M19-R applies because the raw output is the actual extended
   \(d_{\rm raw}\)-isomorphism supplied by M14, producing
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
by one. The global hypotheses on \(A,w\) are retained throughout and license
each use of M04; they are not stored implicitly in the partition datum.

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
   (`approximate_algebras.tex:1363-1369`), under its explicit
   \(\varepsilon_A\le t\) hypothesis.
3. M11 then applies M08 separately in the two orientations and obtains both
   nested zero corners in \(A_{U\cup V}\).
4. M12 imports M07 directly to supply the quantitative target-projection
   data, consumes those two **nested** zero spaces, and installs the unique
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
| \(t_{\rm atom}\) | The compressed-corner scalar scale is the already-universal \(K_{\rm call}\varepsilon\). M04 supplies \(\varepsilon_{\{j\}}\le L\varepsilon\), and \(L\le K_{\rm call}\); no atom count occurs. |
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
   byte-check the operator-space Definition block, record consensus for the
   three original shards before any lock, then regenerate/check the
   definition index. No M-row lands before this.
1. Land M01, then M02. Rewire M03 from
   `lem-extcb-exact-target-correction` to M02, preserving its contract line
   byte-for-byte and every other landed field. **Validate and land the
   rewired M03 after M02 and before M04**; it is not treated as an available
   rigorous dependency merely because the design proposes a rewire.
2. Land M04, M05, and M06 with the exact direct dependencies in §4.1.
3. Land M07 and hostile-check both telescope directions. If either fails,
   stop at the declared M07 gap. Then land M08 and M09.
4. Land M10, then corrected M11. Land M12 and M13 only with their explicit
   original-ambient hypotheses and direct M07 imports.
5. Land M14, M15, corrected M16, and M17.
6. Land corrected M18. Every constant in \(r_{\rm reset}\) now has an
   earlier producer.
7. **G-S1 STOP, unchanged:** wait until the three named Stage-1 producer ids
   are landed under the separate S1 design.
8. Land corrected M19-S1, M19-S2, M19-S3, then corrected M19-R.
9. Land corrected M20, including the distinct
   \(t_{\rm atom}=K_{\rm call}\varepsilon\) scalar envelope.
10. Land M21 and M22.
11. Land M23, then M24.
12. Land corrected M25 with direct M04 and the \(t_{\rm atom}\) base call.
13. Land corrected M26, then conditional M27 with their explicit global
    \(A,w\) bounds. There is no M25-to-M27 edge.
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
  their exact schema fields, kinds, and draft statuses; the cited shard is
  restricted to the byte-verbatim TeX 1453-1464 block, and the three
  original shards require a real consensus record before locking.
- **ESCALATED:** adding `def-operator-space` to M01-M02 and all amplified
  rows that use its vocabulary. M03's landed `defs:` field is unchanged.
- **ESCALATED:** adding `def-maincb-reset-state`,
  `def-maincb-raw-call`, and `def-maincb-partition-state` to the exact rows
  listed above.
- **INTERFACE ESCALATED:** partition state does not store the original
  ambient defect or \(w\)'s defect/unit tag; consumers quantify them.
  Simultaneous \(U,V\) use requires two supplied reset states.

### Result contracts and dependencies

- **ESCALATED:** every new result contract M01-M02, M04-M18,
  M19-S1/S2/S3/R, and M20-M28.
- **CONTRACT BYTE-UNCHANGED, DEPENDENCY ESCALATED:** M03 depends on
  `lem-maincb-improvement-iteration`; its exact landed contract line and all
  other landed fields remain unchanged.
- **CONTRACT ESCALATED:** M04 explicitly quantifies a finite-dimensional
  extended \(\varepsilon\)-\(C^*\)-algebra \(A\).
- **EXACT DEPENDENCY ESCALATED:** M05, M07, and M09 import the named COMP
  rows exactly as displayed, including M09's two amplification/identity ids.
- **INTERFACE/DEPENDENCY ESCALATED:** M11-M13 carry the original
  \(\varepsilon_A\le t\) hypothesis; M12/M13 import M07 directly; M13
  explicitly fills every closed-EXT datum field.
- **SCALE ESCALATED:** M13 has \(C_{\rm s2}\ge1\); M16 accepts total datum
  defect \(C_{\rm s2}t\) and absorbs it into \(D_2,e_2\); M18 records the
  call-specific-\(t\) caveat; M20 needs no extra \(C_{\rm s2}\) factor.
- **INVARIANT ESCALATED:** new M19-R proves
  \(d_R\le c_0^{\rm cb}\varepsilon_R\) only from a literal output already
  assumed to be an extended raw inclusion/isomorphism; M25-M27
  consume/preserve that local form.
- **DOMAIN ESCALATED:** M19-S1 restores the unit-preserving v2 inclusion;
  M19-S2/S3 and M25-M27 explicitly quantify the extended-\(\varepsilon\)
  ambient and extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(w\).
- **ATOMIC-CALL ESCALATED:** raw-call data distinguish global and
  compressed-corner scalar calls; M20 produces \(t_{\rm atom}\), and M25
  imports M04 directly at its base.
- **RESTORATION ESCALATED:** the silent v3 contract drifts in M03 and
  M25-M27 are restored exactly as prescribed; no broader non-unital theorem
  is proposed.
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

## 12. Disposition of every `AUDIT-MAIN-STRUCTURE-v3.md` finding

“CLEARED-BY” means repaired at design-architecture level only. It never means
proved or authorized to land. “UNCHANGED-VALID” means the v3 row or
architecture is copied without mathematical change. Audit loci below refer
to `AUDIT-MAIN-STRUCTURE-v3.md`.

### 12.1 Fatal defects, dependency defect, and P0

| binding v3-audit finding | v4 disposition |
|---|---|
| Fatal A: non-unital M19-S1 is false, with the exact \(M_4\) counterexample (§1A). | **CLEARED-BY M19-S1:** \(A\) is explicitly an extended \(\varepsilon\)-\(C^*\)-algebra and \(w\) is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion including the unit clause. |
| Fatal B: M19-S2/S3 omit the original ambient and \(w\)-defect/unit bounds (§1B). | **CLEARED-BY M19-S2/S3:** both hypotheses are explicit; M04 now licenses \(\varepsilon_U,\varepsilon_V,\varepsilon_R\le L\varepsilon\), and RI gives the map bounds. |
| Fatal B propagation to M26/M27 and silent weakening of v2 (§1B, §8). | **CLEARED-BY M26/M27:** both restore the finite-dimensional extended ambient and extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(w\). M25 restores the same v2 domain. |
| Fatal C: data-only M19-R does not assume an M03-eligible map (§1C). | **CLEARED-BY M19-R:** the literal output is assumed to be an extended \(d_{\rm raw}\)-inclusion/isomorphism from the named finite-dimensional \(C^*\)-algebra into \(A_R\), before M03 is invoked. |
| Fatal D: M20 omits the compressed-corner scalar call and M25's base is unlicensed (§1D). | **CLEARED-BY P0/M20/M25:** a distinct compressed-corner scalar tag and \(t_{\rm atom}=K_{\rm call}\varepsilon\) are explicit; M20 proves \(\varepsilon_{\{j\}}\le L\varepsilon\le t_{\rm atom}\le r_{\rm reset}\); M25 imports M04 directly. |
| M12/M13 lack M07's direct quantitative nested-projection export (§1 additional defect). | **CLEARED-BY M12/M13:** both import `lem-maincb-nested-corner-comparison` directly and use its target-projection estimates. |
| M11-M13 omit the original ambient bound (§4 M11-M13). | **CLEARED-BY M11-M13:** each states \(A\) finite-dimensional extended \(\varepsilon_A\)-\(C^*\) with \(\varepsilon_A\le t\). |
| M13 must place \(P_U^R,P_j^R\) into `def-extcb-datum` (§1, §4 M13). | **CLEARED-BY M13:** projections, complementarity, diagonal isomorphism, one-dimensional corner, nonzero cross-corner, and total \(e=\delta+\varepsilon_{A_R}\le C_{\rm s2}t\) are explicit. |
| `def-operator-space` is valid only with the square Definition block and full cited schema (§2). | **CLEARED-BY P0 §1.1:** exact YAML is supplied; TeX 1453-1464 is reproduced byte-verbatim; 1467-1475 is provenance/derived notation only. |
| `def-maincb-reset-state` needs full original/draft schema and a supplied-tag caveat (§2). | **CLEARED-BY P0 §1.2:** exact fields, draft status, consensus-pending record, and data-only caveat are explicit. |
| `def-maincb-raw-call` needs full schema; recorded defect is not an inclusion theorem; scalar scales must be distinguished (§2). | **CLEARED-BY P0 §1.3:** exact fields and caveat are explicit; global and compressed-corner scalar tags are distinct. |
| `def-maincb-partition-state` needs full schema, a decision on stored bounds, and separate \(U,V\) reset states (§2). | **CLEARED-BY P0 §1.4:** it stores neither global bound; consumers quantify both; a single current-union field cannot supply M12/M19-S3's two states. |

### 12.2 Landed inputs and every pre-gate row

| binding v3-audit finding | v4 disposition |
|---|---|
| Amplified compression, identities, and one-sided almost-containment are valid (§3). | **UNCHANGED-VALID:** exact imports in M05/M07/M09 and M07's fixed telescope are retained. |
| Corner algebra, rectangular product, and ideal-unit single compression are valid with the recorded Stage-1-only scope (§3). | **UNCHANGED-VALID:** M09 remains the distinct outer transfer; the ideal-unit row remains confined to M15/M19-S1. |
| One-dimensional product, dimension, and additivity leaves are valid (§3). | **UNCHANGED-VALID:** M10-M13 retain them; only the missing M07/ambient interfaces are added. |
| `conj-extcb` consumes \(e=\delta+\varepsilon\), so M16's \(C_{\rm s2}\) absorption is universal (§3). | **UNCHANGED-VALID:** M16 is verbatim from v3. |
| Four-corner merge requires \(\rho+\varepsilon\le a_{\rm merge}\) (§3). | **UNCHANGED-VALID:** M17/M18 are verbatim and retain the total guard. |
| M03 stays `stated`; downstream stays `proved-mod-audit` (§3). | **UNCHANGED-VALID STATUS:** no status is promoted. |
| M01 requires corrected operator-space provisioning (§4 M01). | **CLEARED-BY P0:** M01 is otherwise verbatim. |
| M02 is valid (§4 M02). | **UNCHANGED-VALID.** |
| M03's displayed contract was not byte-verbatim (§4 M03; §8). | **CLEARED-BY M03:** the landed ASCII `contract:` value is copied byte-for-byte; only `deps:` changes to M02. |
| M04 relied on prose for the ambient (§4 M04). | **CLEARED-BY M04:** its contract explicitly quantifies a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra. |
| M05 is valid with four exact COMP imports (§4 M05). | **UNCHANGED-VALID.** |
| M06 is valid (§4 M06). | **UNCHANGED-VALID.** |
| M07's two-sided fixed telescope and five imports are valid (§4 M07). | **UNCHANGED-VALID; CONDITIONAL GAP STOP RETAINED.** |
| M08's two injections are valid (§4 M08). | **UNCHANGED-VALID.** |
| M09's distinct outer/nested map and exact amplification imports are valid (§4 M09). | **UNCHANGED-VALID.** |
| M10's equivalence proof is valid (§4 M10). | **UNCHANGED-VALID.** |
| M11 is refuted only by the omitted ambient bound (§4 M11). | **CLEARED-BY corrected M11.** |
| M12 needs the ambient bound and direct M07 import (§4 M12). | **CLEARED-BY corrected M12.** |
| M13's scale is correct but its ambient/M07/datum closure is incomplete (§4 M13). | **CLEARED-BY corrected M13;** \(C_{\rm s2}t\) is retained. |
| M14 is conditional on corrected operator-space provisioning (§4 M14). | **CLEARED-BY P0; M14 UNCHANGED.** |
| M15's explicit two-side conditional contract is valid (§4 M15). | **UNCHANGED-VALID.** |
| M16's absorption is valid (§4 M16). | **UNCHANGED-VALID.** |
| M17 is valid (§4 M17). | **UNCHANGED-VALID.** |
| M18 is valid but does not prove M19-R for arbitrary raw data (§4 M18). | **UNCHANGED-VALID M18; CLEARED-BY M19-R's actual-inclusion hypothesis.** |
| G-S1 is correctly after M18 and before M19/MAIN (§5). | **UNCHANGED-VALID:** same three absent ids, same hard stop, no pre-gate import. |

### 12.3 Every post-gate row, hazards, dimension, and retained contracts

| binding v3-audit finding | v4 disposition |
|---|---|
| M19-S1 refuted (§6). | **CLEARED-BY corrected unit-preserving M19-S1.** |
| M19-S2 refuted (§6). | **CLEARED-BY corrected explicit \(A,w,v_U\) domain.** |
| M19-S3 refuted (§6). | **CLEARED-BY corrected explicit \(A,w,v_U,v_V\) domain and two separate reset states.** |
| M19-R refuted (§6). | **CLEARED-BY actual extended raw inclusion/isomorphism hypothesis.** |
| M20 refuted (§6). | **CLEARED-BY distinct \(t_{\rm atom}\) envelope and the explicit M04 inequality.** |
| M21 target valid but wired through invalid M19-R/M20 (§6). | **CLEARED-BY corrected M19-R/M20; M21 contract is unchanged.** |
| M22 maximum argument valid once the domain is corrected (§6). | **UNCHANGED-VALID-WITH-CORRECTED-PARENTS.** |
| M23 target/domain valid except for invalid M19-S1 (§6). | **CLEARED-BY corrected M19-S1; G-S1 remains the honest blocker.** |
| M24 valid conditional on M23 (§6). | **UNCHANGED-VALID-WITH-CORRECTED-PARENT.** |
| M25 base call unlicensed and direct M04 absent (§6). | **CLEARED-BY corrected M25 and its proof plan using \(t_{\rm atom}\).** |
| M26 omits global \(w\) control (§6). | **CLEARED-BY corrected M26.** |
| M27 is valid in shape but invalid as wired (§6). | **CLEARED-BY corrected M26/M27 domain; complete-family hypothesis and M26-only dependency unchanged.** |
| M28 target is valid but subtree invalid (§6). | **CLEARED-BY corrected subtree at design level; target contract and M28-only join unchanged; P0/G-S1/M07 stops remain.** |
| R19 strict-refinement measure and maximum selection are valid (§7). | **UNCHANGED-VALID.** |
| R21 two distinct inductions and M28-only join are valid (§7). | **UNCHANGED-VALID.** |
| R22 production order is right but M11/M12 were not closed (§7). | **CLEARED-BY corrected M11/M12 and updated R22 subsection.** |
| Dimension-freeness is valid; omitted atomic call is not a route alarm (§7). | **UNCHANGED-VALID:** \(t_{\rm atom}=K_{\rm call}\varepsilon\) uses only earlier universal \(K_{\rm call},L\); no call count enters. |
| Retained-contract claim failed at M03 (§8.1). | **CLEARED-BY byte-exact M03.** |
| M25-M27 silently weakened v2's \(w\)-hypothesis (§8.2). | **CLEARED-BY restoring the extended \(c_0^{\rm cb}\varepsilon\)-inclusion and ambient hypotheses.** |
| M07-M13 architecture, inductions, R19, and G-S1 otherwise survive (§8.3). | **UNCHANGED-VALID except the prescribed M11-M13 closure clauses.** |

### 12.4 Audit of every v3-disposition claim and execution ledger

The audit's §9 rechecks v3's own disposition tables. Each repeated claim is
accounted for explicitly here.

| v3 disposition claim re-audited in audit §9 | v4 disposition |
|---|---|
| Later-map cycle is removed, but S2/S3 base bounds were absent (§9.1). | **CLEARED-BY explicit \(A,w\) hypotheses;** later maps remain supplied and acyclicity is unchanged. |
| \(C_{\rm s2}\) scale, exact compression imports, one-sided-telescope use, corner/product imports, single-compression scope, EXT dimension-freeness, four-corner total smallness, exact-target dep removal, M07, M08, and M09 (§9.1). | **UNCHANGED-VALID** in every listed item. |
| Four P0 definitions (§9.1). | **CLEARED-BY schema-complete §1 proposals and corrected cited scope.** |
| One-dimensional leaves in M10-M13 (§9.1). | **CLEARED-BY M12/M13's added M07/ambient clauses; leaves unchanged.** |
| Downstream M28 match/future rewire (§9.1). | **UNCHANGED TARGET/REWIRE; CLEARED-BY corrected subtree at design level.** |
| M03 remains stated (§9.1). | **UNCHANGED-VALID STATUS.** |
| M01/M02 definition gate; M03 exact text; M04 ambient (§9.2). | **CLEARED-BY P0, byte-exact M03, and corrected M04.** |
| M05-M10 row claims (§9.2). | **UNCHANGED-VALID.** |
| M11 canonical data claim (§9.2). | **CLEARED-BY explicit \(\varepsilon_A\le t\).** |
| M12 canonical/current-map claim (§9.2). | **CLEARED-BY ambient plus direct M07.** |
| M13 scale-thread claim (§9.2). | **CLEARED-BY ambient/M07/closed-datum additions; scale unchanged.** |
| M14-M18 row claims (§9.2). | **UNCHANGED-VALID,** with M14 relying on corrected P0. |
| M19 replacement claim (§9.2). | **CLEARED-BY all four corrected envelopes.** |
| M20 rebuilt-domain claim (§9.2). | **CLEARED-BY fifth literal call scale.** |
| M21-M24 row claims (§9.2). | **CLEARED-BY corrected parents; target contracts unchanged.** |
| M25 stronger-invariant claim (§9.2). | **CLEARED-BY licensed atomic base plus direct M04.** |
| M26 domain and M27 shape claims (§9.2). | **CLEARED-BY restored global \(A,w\) bounds; complete-family/M26-only shape unchanged.** |
| M28 rebuilt-subtree claim (§9.2). | **CLEARED-BY corrected M19/M20/M25-M27 at design level; target unchanged.** |
| R19, R21, G-S1, no-dimension-alarm, nested comparison, outer compression, complete-family repair, binary iterability, and reset \(C_{\rm s2}\) (§9.3). | **UNCHANGED-VALID.** |
| R22/zero-corner reuse (§9.3). | **CLEARED-BY M11 ambient and M12 direct M07.** |
| Threshold cycle was acyclic but not closed (§9.3). | **CLEARED-BY corrected envelope domains; no new backward edge.** |
| Stage-1 direct-sum mechanism was valid but M19-S1's domain was not (§9.3). | **CLEARED-BY unit-preserving M19-S1; M15 unchanged.** |
| Initial/maximal/final producers failed only through subtree (§9.3). | **CLEARED-BY corrected subtree at design level; G-S1 remains.** |
| P0-before-M01 requirement (§9.4). | **CLEARED-BY serial step 0 and exact schemas.** |
| Closed call-specific M19 envelopes (§9.4). | **CLEARED-BY corrected S1/S2/S3/R.** |
| Separate/absorb \(C_{\rm s2}\) (§9.4). | **UNCHANGED-VALID M16 option 1.** |
| Strong reset invariant (§9.4). | **CLEARED-BY M19-R's eligible-map hypothesis and M25's licensed base.** |
| Exact M05/M07/M09 deps, G-S1, complete M27 family, M28-only join (§9.4). | **UNCHANGED-VALID.** |
| Complete definition/dependency ledger and four-definition ledger (§9.4). | **CLEARED-BY §§1,11 and this disposition.** |
| M19/M20/M16 ledger (§9.4). | **CLEARED-BY corrected M19/M20; M16 unchanged.** |
| Downstream rewire ledger (§9.4). | **UNCHANGED-VALID exact YAML proposal.** |
| Landing order not executable (§10). | **CLEARED-BY §10:** P0 first; M03 explicitly validated/landed after M02; M11-M13 fixed; corrected M19; \(t_{\rm atom}\) before M25; global bounds in M26/M27. |
| Escalation ledger incomplete (§10). | **CLEARED-BY §11:** it now lists the P0 cited/schema correction, M11-M13 clauses, all M19 domains, M19-R eligibility, atomic scalar/M25 edge, and M03/M25-M27 drift restoration. |
| Eight exact fourth-repair requirements (§11). | **CLEARED-BY respectively:** P0 §1; M11-M13; M19-S1/S2/S3; M19-R; P0/M20/M25; M25-M27; byte-exact M03; §§10-11. |

The remaining blockers are exactly the unchanged P0 ratification gate, G-S1,
and the declared hostile-verification stop at M07. No definition, contract,
dependency, or status is changed by this document; `op-classical` remains
open.

## 13. Historical disposition of `AUDIT-MAIN-STRUCTURE-v2.md`

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
