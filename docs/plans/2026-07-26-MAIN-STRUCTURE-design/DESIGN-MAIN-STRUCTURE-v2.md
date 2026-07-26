# DESIGN-MAIN-STRUCTURE-v2 — acyclic repair after the binding audit

**Date:** 2026-07-26  
**Role:** fresh repair designer  
**Status:** **DESIGN ONLY; NON-RIGOROUS; DO NOT SEED.** No contract or
dependency correction below is authorized until user ratification and a fresh
hostile review.

## 0. Verdict

The four repair failures in `AUDIT-MAIN-STRUCTURE.md` can be removed at the
contract-architecture level by:

1. proving a two-sided **nested-corner comparison** before using any
   close-range argument;
2. introducing an **outer-compression transfer** whose formula is the
   Stage-2/3 compression, not the ideal-unit compression in the landed
   `lem-compcb-single-compression-transfer`;
3. making corner equivalence and the cross-union datum purely conditional
   theorems that land **before** the reset ledger; and
4. making finite recombination conditional on the complete family
   \((v_C)_C\) of one-class maps.

This produces an acyclic MAIN DAG. There is nevertheless one honest upstream
blocker:

> **ESCALATED GAP — G-S1.** The three Stage-1 split producers
> `lem-stage1-rectified-nontrivial-projection`,
> `lem-stage1-original-complementary-pair`, and
> `lem-stage1-fresh-two-point-inclusion` are not landed shards. Their
> formula-level polar prerequisites are the subject of the pending S1-POLAR
> repair round after its binding audit. No MAIN row below imports their constants until the serial
> G-S1 gate requires those three rows to be landed.

Thus this document is a well-founded design, but not yet an executable
end-to-end elevation plan. That is a successful escalation, not a theorem
failure. No mathematical counterexample to Kitaev's source argument was
found.

The pinned source used below is
`refs/kitaev-2405.02434/approximate_algebras.tex`, SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`
(`refs/manifest/checksums.sha256:4`).

## 1. Fixed notation for contracts

This section is notation for this design, not a new definition shard.

Let \(A\) be a finite-dimensional extended
\(\varepsilon\)-\(C^*\)-algebra and let
\[
  w:\mathbb C^m\longrightarrow A,\qquad P_j=w(e_j),\qquad
  P_U=\sum_{j\in U}P_j,\qquad A_U=S^A_{P_U}.
\]
For nonempty \(U\subseteq R\), write
\[
  P_U^R=\operatorname{Co}^{A}_{P_R}(P_U)\in A_R.
\]
If \(P,Q\) are subordinate to \(R\), write
\[
  F^R_{P,Q}
  :=\operatorname{Co}^{A_R}_{P^R,Q^R},\qquad
  P^R=\operatorname{Co}^{A}_{R}(P),\quad
  Q^R=\operatorname{Co}^{A}_{R}(Q).
\]
The superscript records the ambient algebra. In particular,
\(S^A_{P,Q}\) and \(S^{A_R}_{P^R,Q^R}\) are not identified by notation.

The witnesses
\(\varepsilon_{\max}^{\rm cb},\delta_{\max}^{\rm cb},c_0^{\rm cb}\)
are those in the ratified contract of
`lem-maincb-error-improvement`. A **local master error** \(t\) is an explicit
upper bound for the target ambient defect, all projection and complementarity
defects in one raw call, and the non-reset inputs named by that call. A reset
map in such an ambient has defect at most \(c_0^{\rm cb}t\).

No contract below uses an unnamed “sufficiently small” radius.

## 2. Landed inputs

Only these already-landed shards are treated as available leaves:

- compression and corner algebra:
  `lem-compcb-amplified-compression`,
  `lem-compcb-amplified-compression-identities`,
  `lem-compcb-amplified-almost-containment`,
  `lem-compcb-corner-algebra`,
  `lem-compcb-rectangular-product`, and
  `lem-compcb-single-compression-transfer`;
- corner dimension and product:
  `lem-extcb-one-dimensional-product`,
  `lem-extcb-one-dimensional-corner-dimension`, and
  `lem-extcb-corner-dimension-additivity`;
- structural engines:
  `conj-extcb`, `lem-extcb-four-corner-merge`, and
  `lem-extcb-exact-target-correction`;
- consumer:
  `lem-thmainext-conditional`.

The existing shard `lem-maincb-error-improvement` is a `stated` target, not a
proved input. It occurs as row M03 below. In particular, its dependency on
`lem-extcb-exact-target-correction` does not by itself prove it: the target
there is \(B(H)\), whereas IMPROVE-CB has approximate codomain \(A\)
(`argument/lemmas/lem-maincb-error-improvement.md:13-31`).

## 3. Acyclic proposal table

Rows are listed in dependency order. “Earlier” in the dependency column means
an earlier M-row in this table. G-S1 is a hard serial gate, not an available
dependency.

### 3.1 Error improvement and ambient-free helper rows

| row / proposed id | one-line `contract:` value | deps (all landed or earlier) | provenance | projected af | feasibility |
|---|---|---|---|---|---|
| **M01** `lem-maincb-improvement-one-step` | There are universal \(K_{\rm step}\ge1\) and \(e_{\rm step}>0\) such that, if \(B\) is a finite-dimensional \(C^*\)-algebra, \(A\) an extended \(\varepsilon\)-\(C^*\)-algebra, and \(v:B\to A\) an extended \(d\)-inclusion with \(d+\varepsilon\le e_{\rm step}\), then one dagger-preserving level-one map \(v^+\), with \(v_n^+=I_n\otimes v^+\), satisfies \(\sup_n\|v_n^+-v_n\|\le K_{\rm step}d\) and is an extended \(d^+\)-inclusion for \(d^+\le K_{\rm step}(d^2+\varepsilon)\). | `lem-extcb-exact-target-correction` is a proof-pattern precedent only; no logical result dep is required beyond the canonical definitions. | TeX 1239–1311, 1508–1535 | 8 / 3 | **SUPPORTED-WITH-DERIVATION** |
| **M02** `lem-maincb-improvement-iteration` | There are universal \(e_{\rm it}>0\), \(K_{\rm disp}<\infty\), and \(K_{\rm floor}<\infty\) such that, if \(B\) is a finite-dimensional \(C^*\)-algebra, \(A\) is an extended \(\varepsilon\)-\(C^*\)-algebra, and \(v:B\to A\) is an extended \(d\)-inclusion with \(d+\varepsilon\le e_{\rm it}\), then one dagger-preserving \(\widetilde v\), with \(\widetilde v_n=I_n\otimes\widetilde v\), satisfies \(\sup_n\|\widetilde v_n-v_n\|\le K_{\rm disp}d\) and has extended defect at most \(K_{\rm floor}\varepsilon\); for \(\varepsilon>0\) it is reached after finitely many correction steps, and for \(\varepsilon=0\) it is their operator-norm limit. | M01 | TeX 1313, 1508–1535 | 6 / 3 | **SUPPORTED-WITH-DERIVATION** |
| **M03** `lem-maincb-error-improvement` (landed id; corrected deps only) | **Keep the ratified contract verbatim:** there are universal \(\varepsilon_{\max}^{\rm cb}>0,\delta_{\max}^{\rm cb}>0,c_0^{\rm cb}<\infty\) such that every extended \(\delta\)-inclusion \(v:B\to A\) from finite-dimensional \(B\) into an extended \(\varepsilon\)-\(C^*\)-algebra, with \(0\le\varepsilon\le\varepsilon_{\max}^{\rm cb}\) and \(0\le\delta\le\delta_{\max}^{\rm cb}\), can be replaced by an extended \(c_0^{\rm cb}\varepsilon\)-inclusion, preserving bijectivity. | M02; the landed exact-target row may remain only as an explicitly unused proof precedent | TeX 1192, 1317–1319, 1483–1509, 1557; landed shard lines 4–31 | 5 / 3 | **SUPPORTED-WITH-DERIVATION; contract already ratified** |
| **M04** `lem-maincb-direct-corner-envelope` | There are universal \(L\ge1\) and \(e_{\rm env}>0\) such that, if \(0\le\varepsilon\le e_{\rm env}\) and \(w:\mathbb C^m\to A\) is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion, then every nonempty \(U\) has \(P_U\) a \(c_0^{\rm cb}\varepsilon\)-projection, every \(A_U=S^A_{P_U}\) is an extended \(L\varepsilon\)-\(C^*\)-algebra, and for \(U\subseteq R\) all subordination and complementarity errors among \(P_U,P_{R\setminus U},P_R\) are at most \(L\varepsilon\). | M03; `lem-compcb-corner-algebra` | TeX 1068–1084, 1367–1368, 1428–1435 | 6 / 3 | **SUPPORTED-WITH-DERIVATION** |
| **M05** `lem-maincb-direct-sum-inclusion-merge` | There are universal \(C_{\rm dir}<\infty\) and \(e_{\rm dir}>0\) such that, if \(B_1,B_2\) are finite-dimensional \(C^*\)-algebras, \(P_1,P_2\) are target \(t\)-projections, \(\|P_1+P_2-I\|\le t\), and \(v_i:B_i\to S_{P_i}\) are extended \(t\)-inclusions with target ambient defect at most \(t\le e_{\rm dir}\), then \((x_1,x_2)\mapsto v_1(x_1)+v_2(x_2)\) is an extended \(C_{\rm dir}t\)-inclusion; bijectivity is asserted only if both \(v_i\) are bijective and both target cross-corners vanish. | landed compression rows | TeX 1325–1359, 1542–1544, 1557 | 8 / 3 | **SUPPORTED-WITH-DERIVATION** |
| **M06** `lem-maincb-full-corner-identification` | There is a universal \(e_{\rm full}>0\) such that, if \(R\) is a \(t\)-projection in an extended \(t\)-\(C^*\)-algebra and \(\|R-I\|\le t\le e_{\rm full}\), then \(\operatorname{Co}_R=I\) and \(S_R=A\), at every amplification. | `lem-compcb-amplified-compression` and identities | TeX 1064–1066, 1542–1544 | 4 / 2 | **SUPPORTED-WITH-DERIVATION** |

### 3.2 The comparison that the first repair assumed

| row / proposed id | one-line `contract:` value | deps | provenance | projected af | feasibility |
|---|---|---|---|---|---|
| **M07** `lem-maincb-nested-corner-comparison` | There are universal \(C_{\rm nest}<\infty\) and \(e_{\rm nest}>0\) such that, whenever \(R,P,Q\) are \(t\)-projections in a finite-dimensional extended \(t\)-\(C^*\)-algebra, \(R\) is nonvanishing, \(P,Q\) are subordinate to \(R\) with all four left/right subordination errors at most \(t\le e_{\rm nest}\), \(A_R=S^A_{R}\), \(P^R=\operatorname{Co}^A_R(P)\), and \(Q^R=\operatorname{Co}^A_R(Q)\), then \(P^R,Q^R\) are \(C_{\rm nest}t\)-projections in \(A_R\) and, at every amplification, \[\|F^R_{P,Q}(\operatorname{Co}^A_R X)-X\|\le C_{\rm nest}t\|X\|\quad(X\in S^A_{P,Q}),\] \[\|\operatorname{Co}^A_{P,Q}Y-Y\|\le C_{\rm nest}t\|Y\|\quad(Y\in S^{A_R}_{P^R,Q^R}).\] | landed amplified compression, almost-containment, corner-algebra, and rectangular-product rows | TeX 1054–1082 and 1435–1441; elementary fixed-length telescope described below | 11 / 3 | **SUPPORTED-WITH-DERIVATION; load-bearing** |
| **M08** `lem-maincb-nested-corner-dimension-transport` | There is a universal \(e_{\rm ncd}>0\) such that, whenever \(R,P,Q\) are \(t\)-projections in a finite-dimensional extended \(t\)-\(C^*\)-algebra, \(R\) is nonvanishing, all four left/right subordination errors of \(P,Q\) to \(R\) are at most \(t\le e_{\rm ncd}\), \(A_R=S^A_{R}\), \(P^R=\operatorname{Co}^A_R(P)\), and \(Q^R=\operatorname{Co}^A_R(Q)\), one has \(\dim S^A_{P,Q}=\dim S^{A_R}_{P^R,Q^R}\). | M07 | M07 plus the elementary two-sided injectivity argument; compare the same-space range lemma at `proofs/lem-extcb1-close-corner-dimension/export.md:123-161` | 3 / 2 | **SUPPORTED-WITH-DERIVATION** |
| **M09** `lem-maincb-outer-compression-transfer` | There are universal \(C_{\rm out}<\infty\) and \(e_{\rm out}>0\) such that, whenever \(R,P\) are \(t\)-projections in a finite-dimensional extended \(t\)-\(C^*\)-algebra, \(R\) is nonvanishing, both subordination errors of \(P\) to \(R\) are at most \(t\), \(v:B\to S^A_P\) is an extended \(t\)-isomorphism, \(A_R=S^A_{R}\), \(P^R=\operatorname{Co}^A_R(P)\), and \(t\le e_{\rm out}\), the explicitly defined map \[T=\operatorname{Co}^{A_R}_{P^R}\circ\operatorname{Co}^A_R\circ v:B\longrightarrow S^{A_R}_{P^R}\] is an extended \(C_{\rm out}t\)-isomorphism and \(T_n=I_n\otimes T\) for every \(n\). | M07, M08; landed corner-algebra and rectangular-product rows | TeX 1068–1082, 1435–1441, 1542–1544 | 9 / 3 | **SUPPORTED-WITH-DERIVATION** |

#### M07 derivation obligation

M07 does **not** compare two spectral compression operators on different
Banach spaces in operator norm. It proves the two displayed estimates
directly.

1. For \(X\in S^A_{P,Q}\), amplified almost-containment gives
   \(\operatorname{Co}_R X=X+O(t)\|X\|\).
2. The definition of compression in \(A_R\) makes
   \(F^R_{P,Q}(Z)\) close to the two internal left/right products by
   \(P^R,Q^R\).
3. Replace \(P^R,Q^R\) by \(P,Q\), and replace each internal compressed
   product by the ambient product, using only a fixed number of applications
   of the landed rectangular-product estimate. This gives
   \(F^R_{P,Q}(\operatorname{Co}_R X)=P(XQ)+O(t)\|X\|
   =X+O(t)\|X\|\).
4. If \(Y=F^R_{P,Q}Y\), run the same fixed telescope in the reverse
   direction to obtain
   \(\operatorname{Co}^A_{P,Q}Y=Y+O(t)\|Y\|\).

For M08, shrink so \(C_{\rm nest}t<1\). The first displayed map is injective
from the original corner to the nested corner, and the second is injective in
the reverse direction. Finite dimensionality gives equality of dimensions.

This is supported by local definitions and landed estimates, but it is not a
quoted theorem. If a prover cannot establish either displayed estimate
without a new unregistered premise, **M07 becomes GAP and the MAIN plan stops
there**. No fallback to the refuted generic close-corner row is allowed.

M09 then uses M07 with \(P=Q\): the displayed \(T\) is close to \(v\), hence
injective; its range is in the nested corner; M08 gives equality of the finite
dimensions, hence surjectivity. This is the correct outer form. The landed
ideal-unit row is not a dependency of M09.

### 3.3 Conditional structural producers before any reset ledger

| row / proposed id | one-line `contract:` value | deps | provenance | projected af | feasibility |
|---|---|---|---|---|---|
| **M10** `lem-maincb-corner-equivalence` | There is a universal \(e_{\sim}>0\) such that, for every finite family of one-dimensional \(t\)-projections \(P_1,\ldots,P_m\) in an extended \(t\)-\(C^*\)-algebra with \(t\le e_{\sim}\), the relation \(j\sim k\iff\dim S_{P_j,P_k}=1\) is an equivalence relation. | landed one-dimensional product and corner-dimension rows | TeX 1162–1187 | 6 / 3 | **SUPPORTED-WITH-DERIVATION** |
| **M11** `lem-maincb-cross-union-zero-corners` | There is a universal \(e_{\rm zero}>0\) such that, if \(w:\mathbb C^m\to A\) is a non-unital extended \(t\)-inclusion with one-dimensional images \(P_j\), \(U,V\) are disjoint nonempty unions sharing no class for the relation \(j\sim k\iff\dim S^A_{P_j,P_k}=1\), \(R=U\cup V\), and the local master error satisfies \(t\le e_{\rm zero}\), then \(\dim S^A_{P_U,P_V}=\dim S^A_{P_V,P_U}=0\) and \(\dim S^{A_R}_{P_U^R,P_V^R}=\dim S^{A_R}_{P_V^R,P_U^R}=0\). | M08, M10; landed corner-dimension additivity | TeX 1363–1369, 1428, 1443 | 6 / 3 | **SUPPORTED-WITH-DERIVATION** |
| **M12** `lem-maincb-cross-class-merging-datum` | There are universal \(C_{\rm cross}<\infty\) and \(e_{\rm cross}>0\) such that, if \(w:\mathbb C^m\to A\) is a non-unital extended \(t\)-inclusion with one-dimensional images \(P_j\), \(U,V\) are disjoint nonempty unions sharing no class for the relation \(j\sim k\iff\dim S^A_{P_j,P_k}=1\), \(R=U\cup V\), and \(v_U:B_U\to S^A_{P_U}\), \(v_V:B_V\to S^A_{P_V}\) are extended \(c_0^{\rm cb}t\)-isomorphisms with \(t\le e_{\rm cross}\), then the two outer-compressed diagonal maps and the unique off-diagonal maps \(0\to0\) form an amplified four-corner merging datum in \(A_R\) with common defect \(\rho\le C_{\rm cross}t\). | M03, M09, M11 | TeX 1325–1345, 1358, 1363–1369, 1443 | 9 / 3 | **SUPPORTED-WITH-DERIVATION; corrected target id** |
| **M13** `lem-maincb-stage2-extcb-datum` | There are universal \(C_{\rm s2}<\infty\) and \(e_{\rm s2}>0\) such that, if \(w:\mathbb C^m\to A\) is a non-unital extended \(t\)-inclusion with one-dimensional images \(P_j\), \(U\) is nonempty, \(j\notin U\), \(\dim S^A_{P_k,P_j}=1\) for every \(k\in U\), \(R=U\cup\{j\}\), and \(v_U:M_{|U|}\to S^A_{P_U}\) is an extended \(c_0^{\rm cb}t\)-isomorphism, then for \(t\le e_{\rm s2}\) the outer-compressed map, \(P_U^R\), and \(P_j^R\) form a closed EXT-CB datum in \(A_R\) with total defect at most \(C_{\rm s2}t\). | M03, M08, M09, M10; landed additivity | TeX 1363–1412, 1430–1441 | 10 / 3 | **SUPPORTED-WITH-DERIVATION** |

M13 must prove, rather than name, all five EXT-CB clauses:

- the M09 map is bijective onto \(S^{A_R}_{P_U^R}\);
- M08 with \(P=Q=P_j\) gives
  \(\dim S^{A_R}_{P_j^R}=1\);
- additivity and same-class equivalence give
  \(\dim S^A_{P_U,P_j}=|U|>0\), and M08 transports nonvanishing;
- linearity gives
  \(P_U^R+P_j^R=\operatorname{Co}_{P_R}(P_R)=I_{A_R}\);
- the common defect is the maximum of the preceding dependency-produced
  bounds.

### 3.4 Raw calls, corrected reset package, and the only upstream gate

Each raw row is conditional on a local master error \(t\). Consequently its
constants can be produced before the reset ledger without importing a reset
threshold.

| row / proposed id | one-line `contract:` value | deps | provenance | projected af | feasibility |
|---|---|---|---|---|---|
| **M14** `lem-maincb-initial-raw-inclusion` | There are universal \(D_0<\infty\) and \(e_0>0\) such that, in every finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra with \(\varepsilon\le t\le e_0\), the scalar map \(\lambda\mapsto\lambda I_A\) is an extended \(D_0t\)-inclusion; if \(\dim A=1\), it is bijective. | canonical definitions | TeX 430–455, 1467–1475 | 4 / 2 | **SUPPORTED-WITH-DERIVATION** |
| **M15** `lem-maincb-stage1-raw-refinement` | There are universal \(D_1<\infty\) and \(e_1>0\) such that, if a Stage-1 call has two diagonal extended \(t\)-inclusions into complementary corners—an old \(\mathbb C^{m-1}\) side and a fresh \(\mathbb C^2\) side—with every projection, complementarity, map, and ambient defect at most \(t\le e_1\), then their sum map is an extended \(D_1t\)-inclusion \(\mathbb C^{m+1}\to A\); when \(m=1\), the old side is absent and the conclusion is the supplied fresh inclusion. | M05; the ideal-unit landed compression row is permitted only in the proof that a supplied old side has the stated \(t\)-bound | TeX 1352–1359, 1419–1426 | 5 / 2 | **SUPPORTED-WITH-DERIVATION** |
| **M16** `lem-maincb-stage2-raw-extension` | There are universal \(D_2<\infty\) and \(e_2>0\) such that every closed EXT-CB datum in a target algebra \(A_R\), with target ambient defect and all datum defects bounded by a local master error \(t\le e_2\), admits an extended \(D_2t\)-isomorphism \(M_{r+1}\to A_R\). | M13; `conj-extcb` | TeX 1378–1412, 1435–1441 | 3 / 2 | **SUPPORTED-WITH-DERIVATION** |
| **M17** `lem-maincb-stage3-raw-merge` | There are universal \(D_3<\infty\) and \(e_3>0\), with \(e_3\le a_{\rm merge}/(C_{\rm cross}+1)\), such that every amplified four-corner datum in \(A_R\) with common defect \(\rho\le C_{\rm cross}t\) and target ambient defect \(\varepsilon_{A_R}\le t\le e_3\) satisfies \(\rho+\varepsilon_{A_R}\le a_{\rm merge}\) and yields an extended \(D_3t\)-isomorphism \(B_U\oplus B_V\to A_R\). | M12; `lem-extcb-four-corner-merge` | TeX 1325–1359, 1443 | 3 / 2 | **SUPPORTED-WITH-DERIVATION** |
| **M18** `lem-maincb-reset-constant-ledger` | With \(D_*=\max\{1,D_0,D_1,D_2,D_3\}\) and \[\boxed{r_{\rm reset}:=\min\{e_0,e_1,e_2,e_3,\varepsilon_{\max}^{\rm cb},\delta_{\max}^{\rm cb}/D_*\}>0,}\] every scalar, Stage-1 direct-sum, Stage-2 EXT, or Stage-3 four-corner raw call whose target ambient defect and local master error satisfy \(0\le\varepsilon_{\rm target}\le t\le r_{\rm reset}\) has raw map defect at most \(D_*t\le\delta_{\max}^{\rm cb}\), has \(\varepsilon_{\rm target}\le\varepsilon_{\max}^{\rm cb}\), and can be replaced by a map of defect at most \(c_0^{\rm cb}t\); all displayed constants are finite, positive, universal, and independent of dimension, amplification, block data, and stage index. | M03, M14, M15, M16, M17 | finite-minimum arithmetic; W77 finding; audit §§3,5 | 4 / 2 | **SUPPORTED-WITH-DERIVATION; corrected package** |

M16 must choose \(e_2\) from the already-produced M13 and `conj-extcb`
thresholds. M17 must choose \(e_3\) from the already-produced
\(C_{\rm cross},e_{\rm cross},C_{\rm merge},a_{\rm merge}\) witnesses. Thus
\(e_2,e_3\) absorb the nested, outer, equivalence, EXT, and total-merge
guards; M18 does not reach forward to any structural consumer.

The boxed formula explicitly includes the ratified
\(\varepsilon_{\max}^{\rm cb}\) guard omitted by v4.1. It also includes
\(\delta_{\max}^{\rm cb}/D_*\), not merely
\(\delta_{\max}^{\rm cb}\). No constant in M18 is produced by a later row.

#### G-S1 — hard serial stop

Before M19 or any Stage-1 structural row may land, the following currently
absent rows must become landed shards under their separately repaired S1
design:

1. `lem-stage1-rectified-nontrivial-projection`;
2. `lem-stage1-original-complementary-pair`, producing
   \(C_{\rm np},e_{\rm np}\);
3. `lem-stage1-fresh-two-point-inclusion`, producing
   \(C_{\rm pair},e_{\rm pair}\).

Their proposed loci are TeX 917–969 and 1419–1424, with the formula-level
polar chain supplying the proof of TeX 931. They are **NOT IN THE LANDED
REGISTRY**. This document neither assumes them nor redesigns the unresolved
polar proof. Until G-S1 closes, M19–M28 are **BLOCKED / DO NOT LAND**.

| row / proposed id | one-line `contract:` value | deps | provenance | projected af | feasibility |
|---|---|---|---|---|---|
| **M19** `lem-maincb-call-envelope` | After G-S1 is landed, there are universal \(K_{\rm call}\ge1\) and \(e_{\rm call}>0\) such that, for every finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra \(A\) and every extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(w:\mathbb C^m\to A\), all projection, complementarity, diagonal-map, outer-compression, and target-ambient defects in each literal Stage-1 split, Stage-2 one-class extension, and Stage-3 union merge constructed from \(w\) are at most \(t=K_{\rm call}\varepsilon\), whenever \(0\le\varepsilon\le e_{\rm call}\). | M03, M04, M09, M12, M13; landed ideal-unit compression row; **G-S1 landed shards** | TeX 1417–1443; fixed maxima of dependency-produced bounds | 7 / 3 | **GAP NOW; SUPPORTED-WITH-DERIVATION after G-S1** |
| **M20** `lem-maincb-structural-domain-ledger` | With witnesses from M03, M04, M06, M10, M18, and M19, set \[\boxed{\varepsilon_{\rm MAIN}:=\min\{e_{\rm env},e_{\rm call},r_{\rm reset}/K_{\rm call},e_{\sim}/K_{\rm call},e_{\rm full}/K_{\rm call},[2\max\{1,c_0^{\rm cb}K_{\rm call}\}]^{-1}\}>0.}\] Then \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\) implies \(K_{\rm call}\varepsilon\le r_{\rm reset},e_{\sim},e_{\rm full}\) and \(c_0^{\rm cb}K_{\rm call}\varepsilon\le\tfrac12\), together with the envelope hypotheses \(0\le\varepsilon\le e_{\rm env},e_{\rm call}\). | M03, M04, M06, M10, M18, M19 | pure finite-minimum arithmetic | 4 / 2 | **BLOCKED on M19; otherwise SUPPORTED** |

M18 is the corrected **upstream reset package**. M20 is a separate
**downstream structural-domain package**. This split is what removes the two
cycles found by the binding audit.

### 3.5 The eight MAIN structural targets

Except where a stronger bound is written explicitly, “reset” in the
following contracts means the explicit bound \(c_0^{\rm cb}t\) with
\(t=K_{\rm call}\varepsilon\); it is not a hidden definition. Stage 1 takes
place in the original ambient \(A\), so M21–M24 retain the stronger
\(c_0^{\rm cb}\varepsilon\) bound.

| row / target id | one-line `contract:` value | deps | provenance | projected af | feasibility |
|---|---|---|---|---|---|
| **M21** `lem-maincb-initial-reset-inclusion` | For every finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra \(A\) with \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\), there is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(\mathbb C\to A\). | M03, M14, M18, M20 | TeX 430–455, 1317–1319, 1417 | 3 / 2 | **BLOCKED on G-S1 only through M20; otherwise SUPPORTED** |
| **M22** `lem-maincb-maximal-reset-selection` | If \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra with \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\), then the nonempty set of \(m\) admitting an extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(\mathbb C^m\to A\) has a maximum, because the lower norm is positive and hence \(m\le\dim_{\mathbb C}A\). | M20, M21 | TeX 1417; elementary finite-dimensional selection | 4 / 2 | **SUPPORTED-WITH-DERIVATION** |
| **M23** `lem-maincb-stage1-strict-refinement` | If \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra with \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\) and an extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(w:\mathbb C^m\to A\) has some \(P_j=w(e_j)\) with \(\dim S_{P_j}>1\), then there is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion \(\mathbb C^{m+1}\to A\). | M03, M15, M18, M19, M20; **G-S1 landed shards**; landed ideal-unit compression row | TeX 1419–1426 | 6 / 3 | **GAP NOW on G-S1; corrected target id** |
| **M24** `lem-maincb-stage1-maximality` | If \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra with \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\) and \(w:\mathbb C^m\to A\) has maximum source dimension among all extended \(c_0^{\rm cb}\varepsilon\)-inclusions into \(A\), then every projection-basis image \(P_j=w(e_j)\) satisfies \(\dim S_{P_j}=1\). | M22, M23 | TeX 1417–1426 | 3 / 2 | **BLOCKED on M23; otherwise SUPPORTED** |
| **M25** `lem-maincb-one-class-extension` | If \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra, \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\), \(w:\mathbb C^m\to A\) is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion, \(P_j=w(e_j)\), \(P_U=\sum_{j\in U}P_j\), \(A_U=S^A_{P_U}\), and \(C=\{j_1,\ldots,j_s\}\) satisfies \(\dim S^A_{P_{j_a},P_{j_b}}=1\) for all \(a,b\), then there is an extended \(c_0^{\rm cb}K_{\rm call}\varepsilon\)-isomorphism \(v_C:M_s\to A_C\). | M03, M10, M13, M14, M16, M18, M20 | TeX 1430–1441 | 6 / 3 | **SUPPORTED-WITH-DERIVATION after M20** |
| **M26** `lem-maincb-binary-block-merge` | If \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra, \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\), \(w:\mathbb C^m\to A\) is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion, \(P_j=w(e_j)\), \(P_U=\sum_{j\in U}P_j\), \(A_U=S^A_{P_U}\), \(U,V\) are disjoint nonempty unions sharing no class for \(j\sim k\iff\dim S^A_{P_j,P_k}=1\), and extended \(c_0^{\rm cb}K_{\rm call}\varepsilon\)-isomorphisms \(v_U:B_U\to A_U\), \(v_V:B_V\to A_V\) are given, then there is an extended \(c_0^{\rm cb}K_{\rm call}\varepsilon\)-isomorphism \(v_{U\cup V}:B_U\oplus B_V\to A_{U\cup V}\). | M03, M12, M17, M18, M20 | TeX 1352–1359, 1443 | 4 / 2 | **SUPPORTED-WITH-DERIVATION after M20** |
| **M27** `lem-maincb-stage3-finite-recombination` | If \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra, \(0\le\varepsilon\le\varepsilon_{\rm MAIN}\), \(w:\mathbb C^m\to A\) is an extended \(c_0^{\rm cb}\varepsilon\)-inclusion, \(P_j=w(e_j)\), \(P_U=\sum_{j\in U}P_j\), \(A_U=S^A_{P_U}\), \(C_1,\ldots,C_q\) are all classes for \(j\sim k\iff\dim S^A_{P_j,P_k}=1\), and **as initial data** every \(C_a\) has a finite-dimensional \(C^*\)-algebra \(B_{C_a}\) and an extended \(c_0^{\rm cb}K_{\rm call}\varepsilon\)-isomorphism \(v_{C_a}:B_{C_a}\to A_{C_a}\), then there is an extended \(c_0^{\rm cb}K_{\rm call}\varepsilon\)-isomorphism \(\bigoplus_{a=1}^qB_{C_a}\to A_{\cup_aC_a}\). | M26 only; **no dependency on M25** | TeX 1443 | 4 / 2 | **SUPPORTED-WITH-DERIVATION after M20; corrected target id** |
| **M28** `lem-maincb-structural-assembly` | There are universal \(C_{\rm struct}=c_0^{\rm cb}K_{\rm call}<\infty\) and \(e_{\rm struct}=\varepsilon_{\rm MAIN}>0\) such that every finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra \(A\), \(0\le\varepsilon\le e_{\rm struct}\), admits a finite-dimensional \(C^*\)-algebra \(B=\bigoplus_C M_{|C|}\) and one extended \(C_{\rm struct}\varepsilon\)-isomorphism \(v:B\to A\). | M06, M10, M20, M22, M24, M25, M27 | TeX 1414–1444; consumer contract at `argument/lemmas/lem-thmainext-conditional.md:4,26-30` | 7 / 3 | **BLOCKED on G-S1; otherwise SUPPORTED-WITH-DERIVATION; corrected target id** |

M28 is the only join of the two inductions. It applies M25 once for each
class to produce the family explicitly required by M27, then instantiates
M27. Since \(P_{\{1,\ldots,m\}}=w(I)\) is close to \(I_A\), M06 identifies
the final direct corner with \(A\). The conclusion is the quantitative
extended isomorphism required by `lem-thmainext-conditional`, not merely a
bijective level-one map.

## 4. Well-founded measures and data flow

### R19 — Stage-1 refinement

For any actual refinement sequence,
\[
  \mu_1=\dim_{\mathbb C}A-m\in\mathbb N
\]
decreases by exactly one when M23 changes \(m\) to \(m+1\). This proves that
no refinement sequence is infinite. It does **not** prove that an arbitrary
terminal sequence is globally maximal.

The noncircular proof is instead:

1. M21 makes the feasible source-dimension set nonempty.
2. M22 uses the positive lower norm to bound it by
   \(\dim_{\mathbb C}A\) and selects a maximum.
3. M23 contradicts that selected maximum if any image corner is not
   one-dimensional.

No maximality conclusion is imported by M23.

### R21 — two distinct inductions

The one-class induction M25 has state
\[
  (r,v_r:M_r\to A_{\{j_1,\ldots,j_r\}}),\qquad
  \mu_2=|C|-r.
\]
The cross-class induction M27 has state
\[
  (r,U_r,v_{U_r}:\bigoplus_{a\le r}B_{C_a}\to A_{U_r}),\qquad
  \mu_3=q-r.
\]
M27 does not prove or import the maps \(v_C\); its contract quantifies the
entire family as initial data. M28, and only M28, invokes M25 for each class
and supplies that family to M27. This is the R19/R21 discipline requested by
the audit.

## 5. Dimension-freeness audit

| object | audit |
|---|---|
| \(K_{\rm step},K_{\rm disp},K_{\rm floor}\) | The finite-dimensional diagonal has projective norm one, including direct sums (TeX 1239–1254); the same correction is amplified entrywise (1508–1535). No block count occurs. |
| \(C_{\rm dir},e_{\rm dir}\) | The merge has exactly two blocks. Amplification uses the same two level-one maps and TeX 1542–1544,1557. |
| \(C_{\rm nest},e_{\rm nest}\) | M07 uses a fixed-length telescope of compression and product estimates. It never sums over \(U,V\), the ambient dimension, or an amplification index. |
| \(C_{\rm out},e_{\rm out}\) | M09 is M07 plus finite-dimensional injectivity and equality of dimensions. Dimension is used only as an integer equality, not in a norm estimate. |
| \(e_{\sim}\) | Transitivity composes two elements through one one-dimensional corner and uses the universal M10 product threshold. |
| additivity and zero corners | Cardinalities occur only in the exact equality \(\dim S_{P_U,P_V}=\sum_{j,k}\dim S_{P_j,P_k}\). Zero summands give zero without a quantitative sum. |
| \(C_{\rm cross},C_{\rm s2},D_0,\ldots,D_3\) | Each is a finite maximum/product of earlier universal constants. M12 has four corners; M13 adds one matrix row/column; neither counts classes. |
| \(r_{\rm reset}\) | It is the minimum of finitely many earlier positive universal witnesses. It explicitly contains both IMPROVE-CB guards. |
| \(K_{\rm call},\varepsilon_{\rm MAIN}\) | \(K_{\rm call}\) is a fixed maximum of one-call estimates. The boxed minimum is finite and contains no source dimension, amplification, class count, or induction index. |
| the three inductions | Dimension and class count bound the number of finite steps only. Every step is immediately reset, so no error is summed over those counts. |
| \(C_{\rm struct}\) | \(C_{\rm struct}=c_0^{\rm cb}K_{\rm call}\) is independent of all finite combinatorial data. |

The source convention that every \(O(\cdot)\) coefficient is independent of
additional data is at TeX 458. No dimension leak was found.

## 6. Serial landing order

The order below is a topological sort. A step may start only after every
listed predecessor is a landed shard.

1. Land M01, then M02, then rewire and elevate M03.
2. Land M04–M06.
3. Land M07; hostile verification must check both displayed estimates. If
   either fails, stop with GAP.
4. Land M08, then M09.
5. Land M10, M11, M12, and M13, in that order.
6. Land M14, M15, M16, and M17.
7. Land the corrected reset package M18. At this point every constant in its
   boxed formula has an earlier producer.
8. **STOP at G-S1** until the three named Stage-1 split rows are actually
   landed under a separately repaired and audited S1 design.
9. After G-S1, land M19 and then M20.
10. Land M21 and M22.
11. Land M23 and then M24.
12. Land M25.
13. Land M26 and then the conditional recombination theorem M27.
14. Land M28.
15. Only after M28 is validated may `lem-thmainext-conditional` be rewired or
    seeded against this structural subtree.

There is no edge from M25 to M27. Their outputs meet only at M28. There is no
edge from M23/M24 to M10 or M12. Those conditional threshold producers are
upstream of M18, eliminating the audit's two cycles.

## 7. Disposition of binding audit findings

| binding audit finding | disposition | clearing row / exact reason |
|---|---|---|
| 1. Reset threshold imported future constants and formed cycles. | **CLEARED-BY DESIGN** | M10–M17 are conditional producers with no reset-ledger dependency; M18 imports only M03 and M14–M17; M20 is a separate downstream minimum. The serial order is a topological sort. |
| 2. Close-corner transport assumed the original-vs-nested comparison. | **CLEARED-BY DESIGN, PROOF OBLIGATION EXPLICIT** | M07 states the two required comparison estimates and gives the fixed-telescope derivation from TeX 1054–1082 plus landed amplified estimates. M08 uses only those estimates. Failure of either M07 estimate is an explicit GAP stop. |
| 3. The ideal-unit compression row was misapplied to Stage 2/3. | **CLEARED-BY DESIGN** | M09 uses the explicit double outer formula \(\operatorname{Co}^{A_R}_{P^R}\operatorname{Co}^A_Rv\). The landed ideal-unit row is confined to the Stage-1 old-side restriction where its hypothesis \(P=v(q)\) is literal. |
| 4. Recombination omitted its family of one-class initial maps. | **CLEARED-BY DESIGN** | M27 quantifies \((v_C)_C\) as initial data and uses measure \(q-r\). M28 invokes M25 for every class and supplies that family. |

For completeness, the five original v4.1 defects have the following
disposition:

| original defect | disposition |
|---|---|
| Stage 1 incorrectly used four bijective corner maps. | **CLEARED-BY M05/M15:** Stage 1 uses only the direct-sum inclusion conclusion. |
| The class-only binary merge was non-iterable. | **CLEARED-BY M12/M26:** inputs are disjoint unions of classes and the output is their union. |
| Original zero corners were silently reused in a compressed ambient. | **CLEARED-BY M07/M08/M11:** original zero is transported only after the two-sided nested comparison. |
| The reset radius omitted exact consumer guards. | **CLEARED-BY M18:** both IMPROVE guards and all raw-row thresholds occur in the boxed formula; M16/M17 absorb EXT and total-merge guards. |
| Initial/maximal producers and the quantitative final conclusion were missing. | **CLEARED-BY M21/M22/M28:** nonemptiness, bounded selection, full-corner identification, and the extended \(C_{\rm struct}\varepsilon\)-isomorphism are explicit. |

## 8. Ratification and escalation ledger

- **ESCALATED FOR USER RATIFICATION:** every new contract M01–M02 and
  M04–M28; the dependency correction to M03; the corrected interfaces of all
  eight MAIN target ids.
- **NO CONTRACT CHANGE REQUESTED:** the already-ratified contract text of
  `lem-maincb-error-improvement`.
- **ESCALATED GAP:** G-S1, because its three required producer rows are absent.
- **CONDITIONAL GAP STOP:** M07 if the two-sided nested comparison cannot be
  derived from the named local inputs.
- **NOT IN LOCAL REFS:** no numerical value is asserted for any big-\(O\)
  coefficient. The plan uses named existential universal witnesses only.
- **NO STATUS PROMOTION:** all rows remain design candidates; `op-classical`
  and the MAIN chain remain open/non-rigorous at their recorded rungs.
