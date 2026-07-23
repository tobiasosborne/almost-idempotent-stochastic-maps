STATUS: UNVERIFIED STRATEGIST OUTPUT

# W74F-C — decomposition of `th_main_ext` and universal-constant ledger

Date: 2026-07-23  
Role: fresh strategist-prover; this report is not a verifier verdict  
Primary source: `refs/kitaev-2405.02434/approximate_algebras.tex`  
Checked SHA256: `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`

## 0. Bottom line

The source gives a credible dimension-free architecture, but its proof of
`th_main_ext` is not complete. After separating level-one selection from genuinely
amplified work, the principal theorem decomposes into two load-bearing GAP nodes:

1. **H-CB:** uniform column-Hilbert and complete operator-module estimates for
   \(1_{M_n}\otimes \mathrm{Ha}^{Q}_{P,R}\);
2. **EXT-CB:** the amplified extension lemma, using the *same* level-one unitary
   \(U_1\) at every amplification.

Everything else in the `th_main_ext` adaptation is either printed with a substantive
proof or is a fixed-corner application of an unamplified lemma to
\(M_n\otimes\mathcal A\). In particular, the corrected estimate at `tex:1551-1555`
does follow, with squares, from the amplified compression estimate and the
\(\varepsilon\)-\(C^*\) axiom. It should not be grouped with H-CB as an open
mathematical gap.

The end-to-end factorization chain supports a **conditional** existential universal
constant \(K\) and threshold \(\eta_K>0\): conditional on H-CB and EXT-CB (and on a
full audit of `th_almost_idemp`), every remaining operation has a dimension-free
mechanism. The supplied TeX does **not** earn an unconditional \(K\), because it does
not close those amplified nodes.

The source itself makes both the intended strength and the incompleteness visible.
Its convention is:

> “each instance of big-\(O\) or similar notation stands for a concrete function, not depending on any additional data.” (`tex:458`)

The target is:

> “For any finite-dimensional extended \(\eps\)-\(C^*\) algebra \(\calA\), there exist a \(C^*\) algebra \(\calB\) and an extended \(O(\eps)\)-isomorphism \(v\colon\calB\to\calA\). (The implicit constant in \(O(\eps)\) does not depend on \(\calA\) or its dimensionality.)” (`tex:1538-1539`)

But the final proof instruction is only:

> “Corollary~\ref{cor_improvement} (error reduction) should be adapted to extended inclusions using Lemma~\ref{lem_approx_ext} and Proposition~\ref{prop_inc_ext}. The arguments in Section~\ref{sec_proof_main} require only trivial modifications, namely, one should use the norms \(\|\cdot\|_n\) in certain places.” (`tex:1557`)

That last sentence is not a proof that one map has all amplified bounds.

## 1. Notation and classification policy

Put
\[
e:=\delta+\varepsilon,\qquad
\mathcal A_n:=M_n\otimes\mathcal A,\qquad
P_n:=I_n\otimes P.
\]
For a linear map \(T\), write \(T_n=1_{M_n}\otimes T\). All constants below must be
independent of
\[
n,\quad \dim\mathcal A,\quad
\text{the number of simple blocks},\quad
\text{and every block dimension}.
\]

The requested classifications are used locally:

- **(a) ESTABLISHED:** the printed source contains a substantive argument for the
  stated amplified contract. This is not a repository-level verification label.
- **(b) MECHANICAL:** the amplified conclusion follows by applying a printed
  unamplified argument to \(\mathcal A_n\), with a stated norm-preserving or
  fixed-corner reason.
- **(c) GAP:** a new uniform proof is required.

A node classified (b) may import a (c)-node. “Mechanical” describes the local
implication, not the status of the whole theorem.

## 2. A necessary dependency correction

Not every unamplified lemma in `sec_proof_main` needs an amplified analogue.
The following results are used only at level one to choose the eventual block
decomposition:

- `lem_nontriv_projection` chooses a new projection in \(\mathcal A\) or
  \(\mathcal S_P\). Its statement is:

  > “Any \(\eps\)-\(C^*\) algebra \(\calA\) such that \(1<\dim\calA<\infty\) has a nontrivial \(O(\eps)\)-projection.” (`tex:931`)

- `lem_PQR` and `lem_1d_proj` prove the level-one norm and dimension facts used to
  make one-dimensional projections into equivalence classes:

  > “If \(Q\) is one-dimensional, then”  
  > “\(\bigl|\|X\cdot Y\|-\|X\|\|Y\|\bigr|\le O(\delta+\eps)\|X\|\|Y\|\).” (`tex:1162-1167`)

  > “If \(P\) and \(Q\) are one-dimensional \(\delta\)-projections in an \(\eps\)-\(C^*\) algebra, then \(\dim\calS_{P,Q}\le 1\).” (`tex:1179-1180`)

- `lem_add_dim` is used only to count level-one dimensions and to infer that
  \(\dim\mathcal S_{P,Q}=r\) in `lem_extension`; see `tex:1363-1369` and
  `tex:1382-1384`.

One must **not** apply these statements to \(Q_n=I_n\otimes Q\) as though \(Q_n\)
were one-dimensional: \(\mathcal S_{Q_n,Q_n}=M_n\otimes\mathcal S_{Q,Q}\) has
dimension \(n^2\). The correct amplification is a Hilbert **column-module**
statement, not a repeated one-dimensional-projection statement. This is precisely
why H-CB below is a real node.

The true dependency graph is
\[
\begin{array}{c}
\text{P-TENS}\longrightarrow\text{COMP-CB}\longrightarrow
  \{\text{ALPHA-CB},\text{COL-HILB}\},\\
\text{COL-HILB}\longrightarrow\boxed{\text{H-CB}},\\
\text{DIAG-1}\longrightarrow\text{APPROX-CB},\qquad
\{\text{APPROX-CB},\text{INC-CB}\}\longrightarrow\text{IMPROVE-CB},\\
\{\text{ALPHA-CB},\text{INC-CB}\}\longrightarrow\text{MERGE-CB},\\
\{\text{level-one leaves},\text{H-CB},\text{APPROX-CB},
  \text{MERGE-CB}\}\longrightarrow\boxed{\text{EXT-CB}},\\
\{\text{P-TENS},\text{COMP-CB},\text{IMPROVE-CB},
  \text{MERGE-CB},\text{EXT-CB}\}\longrightarrow\text{MAIN-CB}.
\end{array}
\]

## 3. Explicit amplified lemma decomposition

### P-TENS — persistence of projection relations

**Contract.** If \(P,Q,\ldots\in\mathcal A\) obey any relation formed from a fixed
number of sums, products, involutions, and norm inequalities with error \(\delta\),
then for every \(n\ge1\), \(P_n,Q_n,\ldots\in\mathcal A_n\) obey the tensorized
relation with the same error. In particular,
\[
P_n^\dagger=P_n,\qquad
\|P_n^2-P_n\|_n=\|I_n\otimes(P^2-P)\|_n\le\delta.
\]

**Edges.** Operator-space axioms only.

**Uniform-constant mechanism.** The map \(X\mapsto I_n\otimes X\) is isometric.
The source proves:

> “Thus, the map \(X\mapsto I_n\otimes X\) is an isometric inclusion of \(\calL\) into \(\Ma{n}\otimes\calL\).” (`tex:1475`)

It then applies exactly this fact:

> “the map \(P\mapsto I_n\otimes P\) commutes with the involution and the multiplication as well as preserving the norm.” (`tex:1542`)

No matrix entry is summed and no dimension enters.

**Classification:** **(a) ESTABLISHED.**

---

### COMP-CB — compression, subspaces, and compressed products

**Contract.** For \(\delta\)-projections \(P,Q,R\), every \(n\ge1\) satisfies
\[
(\operatorname{Co}_{P,Q})_n
=\operatorname{Co}_{P_n,Q_n},\qquad
M_n\otimes\mathcal S_{P,Q}=\mathcal S_{P_n,Q_n}.
\]
The involution identity, idempotence, almost-containment estimates, and compressed
product estimates hold at all square and rectangular levels with a common constant
\(C_{\rm co}\):
\[
\|\operatorname{Co}_{P_n,R_n}(XY)-XY\|
\le C_{\rm co}e\,\|X\|\,\|Y\|.
\]

**Edges.** P-TENS and the Banach functional calculus `prop_P`.

**Uniform-constant mechanism.** Left and right multiplication by \(P_n,Q_n\) are
the amplifications of left and right multiplication by \(P,Q\). The power series
defining \(\theta\) therefore commutes term-by-term with amplification. Every
estimate is then the original estimate inside the \(\varepsilon\)-\(C^*\) algebra
\(\mathcal A_n\), whose \(\varepsilon\) is unchanged. The source defines
\(\operatorname{Co}_{P,Q}\) and records its operator estimates at `tex:1054-1064`;
its amplified claim is:

> “The map \(\Co_{P,Q}\colon\calA\to\calA\) is extended to \(1_{\Ma{n}}\otimes\Co_{P,Q}=\Co_{I_n\otimes P,\,I_n\otimes Q}\).” (`tex:1544`)

The equality of images follows from the exact equality of the maps, not from a
dimension count.

**Classification:** **(b) MECHANICAL.**

---

### ALPHA-CB — fixed-corner decomposition

**Contract.** In the hypotheses of `lem_alpha`, restricted to the only cases used
downstream, \(p,q\le2\), the maps
\[
\alpha_n:\bigoplus_{j,k}M_n\otimes\mathcal S_{P_j,Q_k}
\longrightarrow M_n\otimes\mathcal S_{P,Q}
\]
are bijections for all \(n\ge1\), with
\[
\|\alpha_n\|\le pq+C_\alpha pqe,\qquad
\|\alpha_n^{-1}\|\le1+C_\alpha pqe.
\]

**Edges.** P-TENS, COMP-CB.

**Uniform-constant mechanism.** Apply `lem_alpha` to \(\mathcal A_n\) and
\(P_{j,n},Q_{k,n}\). Its only combinatorial loss is \(pq\), and the source explicitly
limits its use:

> “In fact, the lemma will be used for \(p,q\le 2\), so all reasonable variants of the inequalities involved differ only by constant factors.” (`tex:1084`)

Thus \(pq\le4\), independently of \(n\), all block sizes, and the total number of
eventual summands.

**Classification:** **(b) MECHANICAL.**

**Source defect.** At `tex:1109`, \(\beta_{jk}\) is printed with
\(\operatorname{Co}_{P_j,Q_j}\), although its displayed codomain and every following
index require \(\operatorname{Co}_{P_j,Q_k}\). The amplified contract uses the
type-correct \(Q_k\).

---

### COL-HILB — corrected amplified one-column Hilbert structure

**Contract.** Suppose \(Q\) is a one-dimensional level-one
\(\delta\)-projection. For each \(n\ge1\), put
\[
\mathsf H^{(n)}_{P,Q}:=M_{n,1}\otimes\mathcal S_{P,Q},\qquad
\langle Y,X\rangle_n:=\sum_{\ell=1}^n
 \langle Y_{\ell1},X_{\ell1}\rangle.
\]
Then
\[
Y^\dagger\cdot X=\langle Y,X\rangle_n\,\widetilde Q
\]
and there is a universal \(C_{\rm col}\) such that
\[
\left|\langle X,X\rangle_n-\|X\|_{n,1}^2\right|
\le C_{\rm col}e\,\|X\|_{n,1}^2.
\]
Consequently,
\[
(1-C'_{\rm col}e)\|X\|_{n,1}
\le\sqrt{\langle X,X\rangle_n}
\le(1+C'_{\rm col}e)\|X\|_{n,1}
\]
for a universal smallness threshold.

**Edges.** COMP-CB and the \(\varepsilon\)-\(C^*\) axiom in
\(M_{n+1}\otimes\mathcal A\).

**Uniform-constant mechanism.** Treat \(X\) as one rectangular operator-space
element and use the \(C^*\) inequality and compressed-product bound once. Do not
estimate \(\sum_\ell X_{\ell1}^\dagger X_{\ell1}\) entry by entry. This avoids an
\(n\)-factor.

The source prints the exact inner-product identity at `tex:1547-1550`, but the
following displayed estimate omits the squares:

> “\(\bigl|\braket{X}{X}-\|X\|_{n,1}\bigr| \le O(\delta+\eps)\ts\|X\|_{n,1}\)” (`tex:1551-1553`)

The corrected proof is in Section 4 below.

**Classification:** **(b) MECHANICAL, WITH THE PRINTED TYPO CORRECTED.**

---

### H-CB — complete \(\mathrm{Ha}\)-module estimates

**Contract.** Let \(Q\) be one-dimensional at level one and let
\[
h_{P,R}:=\mathrm{Ha}^{Q}_{P,R}:
\mathcal S_{P,R}\to
\mathcal B(\mathcal S_{R,Q},\mathcal S_{P,Q}).
\]
For all \(n\ge1\), identify
\[
M_n\otimes\mathcal B(\mathcal S_{R,Q},\mathcal S_{P,Q})
\cong
\mathcal B(\mathbb C^n\otimes\mathcal S_{R,Q},
           \mathbb C^n\otimes\mathcal S_{P,Q})
\]
using the COL-HILB norms. Then a universal \(C_H\) must give, simultaneously,
\[
(h_{P,R})_n(Z)^\dagger=(h_{R,P})_n(Z^\dagger),
\]
\[
\|(h_{P,R})_n(Z\cdot W)
 -(h_{P,S})_n(Z)(h_{S,R})_n(W)\|
\le C_He\,\|Z\|\,\|W\|,
\]
and the uniform unital, norm, and inverse estimates needed for:

- \((h_{P,P})_n\) to be an extended \(C_He\)-homomorphism;
- \((h_{P,Q})_n\) and \((h_{Q,P})_n\) to be completely
  \(C_He\)-close to their canonical identity identifications.

**Edges.** COMP-CB, COL-HILB, and the level-one definition `Ha_def`.

**Why the constant is not yet sourced.** At level one the source gives exact
adjointness and approximate multiplicativity:

> “This symmetric definition enjoys the exact equality” (`tex:1151`)  
> “\(\Ha^{Q}_{R,P}(Z^\dag)=\Ha^{Q}_{P,R}(Z)^\dag.\)” (`tex:1152-1153`)

> “\(\|\Ha^{Q}_{P,R}(Z\cdot W)-\Ha^{Q}_{P,S}(Z)\ts\Ha^{Q}_{S,R}(W)\|
\le O(\delta+\eps)\ts\|Z\|\ts\|W\|\).” (`tex:1156-1159`)

For amplifications, however, the source only says:

> “Equations \eqref{Ha_dag}, \eqref{Ha_prod}, and the special properties of \(\Ha^{Q}_{P,P}\), \(\Ha^{Q}_{P,Q}\), and \(\Ha^{Q}_{Q,P}\) are generalized in a straightforward way.” (`tex:1555`)

One cannot justify this by applying `lem_PQ_Hilb` directly to \(Q_n\), because
\(Q_n\) is not one-dimensional. An entrywise proof of `Ha_prod` can also introduce
an \(n\)-sized sum. The required proof must work with column operators and their
operator norms.

**Shape of a closing argument.**

1. Prove from `Ha_def`, inside a single rectangular corner of
   \(M_{2n}\otimes\mathcal A\), that \((h_{P,R})_n(Z)X\) is
   \(O(e)\|Z\|\|X\|_{\rm Euc}\)-close to \(Z\cdot X\).
2. Use COL-HILB to convert this to a uniform operator norm estimate.
3. Apply the estimate to an arbitrary unit column \(X\), and use associativity in
   \(M_{2n}\otimes\mathcal A\), to prove the product defect without expanding
   matrix entries.
4. Obtain the special-map and inverse bounds by a Neumann argument at the operator
   level.

**Price.** One new universal constant \(C_H\) and one smallness threshold
\(e_H>0\); no dependence on \(n\) or any block dimension is permitted.

**Classification:** **(c) GAP.**

---

### DIAG-1 — a norm-one diagonal for the whole finite-dimensional algebra

**Contract.** Every finite-dimensional \(C^*\)-algebra \(\mathcal B\), for any
number and sizes of simple summands, has an exact diagonal
\[
D=\sum_s p_sU_s^\dagger\otimes U_s,\qquad
p_s\ge0,\quad \sum_sp_s=1,
\]
with \(XD=DX\), \(\pi(D)=I_\mathcal B\), and projective norm \(1\). The same
convex representation controls every amplification with no \(n\)-loss.

**Edges.** None.

**Uniform-constant mechanism.** Haar averaging is a probability average of
unitaries:

> “Every finite-dimensional \(C^*\) algebra has a standard diagonal, \(D=\int dU\, (U^\dag\otimes U)\), where the integral is taken with respect to the Haar measure on the unitary group. Note that \(\|D\|=1\) because the integral can be approximated by finite sums, i.e.\ convex combinations of \(U^\dag\otimes U\).” (`tex:1245`)

This gives total weight one regardless of block count or dimension.

**Classification:** **(a) ESTABLISHED.**

**Necessary correction.** The Cartesian product formula printed at `tex:1254` and
repeated at `tex:2780-2783` is false without independent block phases. For
\(\mathbb C\oplus\mathbb C\), it produces
\(1_{\mathcal B}\otimes1_{\mathcal B}\), which is not central in the diagonal
sense. Use the full Haar average already supplied at `tex:1245`, or independently
multiply block unitaries by signs/phases and average to kill cross-block terms.
The norm-one property survives.

---

### APPROX-CB — `lem_approx_ext`

**Contract.** There are universal functions/constants such that, for every
finite-dimensional \(C^*\)-algebra \(\mathcal B\) and extended
\(\delta\)-homomorphism \(v:\mathcal B\to\mathcal A\), one level-one map
\(\widetilde v\) satisfies, for every \(n\ge1\),
\[
\widetilde v_n\text{ is an }O(\varepsilon)\text{-homomorphism},\qquad
\|\widetilde v_n-v_n\|\le C_{\rm app}\delta.
\]

**Edges.** DIAG-1 and `prop_delta_hominc`.

**Uniform-constant mechanism.** The correction uses the same norm-one diagonal
at every matrix level. The source states the full uniform contract at
`tex:1508-1510`, defines the amplified correction at `tex:1512-1520`, and proves
the only new diagonal-commutation identity by matrix elements at
`tex:1521-1535`. Because the correction is entrywise the amplification of one
level-one correction, the Newton iteration constructs one \(\widetilde v\), not
unrelated maps \(\widetilde v^{(n)}\).

The whole-algebra Haar diagonal must be used; the false optional formula at
`tex:1254` is not needed.

**Classification:** **(a) ESTABLISHED.**

---

### INC-CB — `prop_inc_ext`

**Contract.** If \(v\) is an extended \(\delta\)-homomorphism and
\(\|v(x)\|\ge\eta_0\|x\|\) at level one for some \(\eta_0>2\delta\), then one
universal \(C_{\rm inc}\) satisfies
\[
\|v_n(X)\|_n\ge(1-C_{\rm inc}e)\|X\|_n
\quad\text{for all }n\ge1.
\]
The corresponding universal upper bound follows from the ordinary
`prop_delta_hominc` applied at each level.

**Edges.** The unamplified `prop_delta_hominc` and operator-space corner axioms.

**Uniform-constant mechanism.** The source proves the fixed doubling estimate
\(a_{2n}\ge a_n/2\) at `tex:1487-1503`, then re-applies the same scalar
`prop_delta_hominc` estimate:

> “if \(a_n>2\delta\), then \(a_n\ge 1-\delta'\) for some \(\delta'=O(\delta+\eps)\) that does not depend on \(n\).” (`tex:1505`)

The loss is the fixed number \(2\), not \(n\).

**Classification:** **(a) ESTABLISHED.**

---

### IMPROVE-CB — amplified error reduction

**Contract.** There exist universal
\(\varepsilon_{\max}^{\rm cb},\delta_{\max}^{\rm cb},c_0^{\rm cb}>0\) such
that an extended \(\delta_{\max}^{\rm cb}\)-inclusion
\(v:\mathcal B\to\mathcal A\) can be replaced by one extended
\(c_0^{\rm cb}\varepsilon\)-inclusion \(\widetilde v\). If \(v\) is bijective,
\(\widetilde v\) is bijective.

**Edges.** APPROX-CB and INC-CB.

**Uniform-constant mechanism.** APPROX-CB gives one map uniformly close at every
level. Its level-one lower bound remains a fixed positive number when
\(\delta_{\max}^{\rm cb}\) is small; INC-CB upgrades that one lower bound to all
levels. Bijectivity is preserved by the ordinary Neumann perturbation argument at
level one. No block iteration occurs inside this corollary.

The unamplified source gives universal constants:

> “There exist some positive constants \(\eps_{\max}\), \(\delta_{\max}\), and \(c_0\) such that … there is also a \(c_0\eps\)-inclusion.” (`tex:1317-1318`)

The amplified source says only that this “should be adapted” (`tex:1557`), but
APPROX-CB plus INC-CB is the checkable adaptation.

**Classification:** **(b) MECHANICAL.**

---

### MERGE-CB — amplified `lem_merging` and `cor_merge_sum`

**Contract.** Suppose the four corner maps \(\gamma_{jk}\) in `lem_merging`
satisfy its adjoint, product, unit, and near-isometry hypotheses at every
amplification with the same \(\delta\). Then their single combined level-one map
\(\gamma\) is an extended \(C_{\rm merge}e\)-inclusion. Bijectivity is preserved.
In particular, if extended \(\delta\)-inclusions
\[
v_j:\mathcal B_j\to\mathcal S_{P_j}\quad(j=1,2)
\]
are placed in two approximately complementary corners, the same sum map
\[
v(X_1,X_2)=v_1(X_1)+v_2(X_2)
\]
is an extended \(C_{\rm merge}e\)-inclusion; it is bijective under the
cross-corner hypothesis of `cor_merge_sum`.

**Edges.** COMP-CB, ALPHA-CB, INC-CB.

**Uniform-constant mechanism.** For each \(n\), apply `lem_merging` to the
\(\varepsilon\)-\(C^*\) algebra \(\mathcal A_n\), with its fixed \(2\times2\)
projection partition. The source's combined map is at `tex:1338-1345`; the proof
factors it through `lem_alpha` at `tex:1348-1350`. There are exactly four corners,
so ALPHA-CB contributes at most \(pq=4\), independent of \(n\), the number of final
summands, or their sizes.

The direct-sum corollary is printed at `tex:1352-1359`.

**Classification:** **(b) MECHANICAL.**

---

### EXT-CB — amplified `lem_extension`

**Contract.** There are universal \(C_{\rm ext}\) and \(e_{\rm ext}>0\) such
that the following holds. Let \(P,Q\in\mathcal A\) be \(\delta\)-projections with
\(\|P+Q-I\|\le\delta\). Suppose
\[
v:M_r\to\mathcal S_P
\]
is an extended \(\delta\)-isomorphism, \(\dim\mathcal S_Q=1\) at level one, and
\(\mathcal S_{P,Q}\ne0\). If \(e\le e_{\rm ext}\), then there is one map
\[
v_+:M_{r+1}\to\mathcal A
\]
which is an extended \(C_{\rm ext}e\)-isomorphism. The constants are independent
of \(r\), \(n\), and \(\dim\mathcal A\).

**Edges.**

- level-one `lem_PQR`, `lem_1d_proj`, and `lem_add_dim`;
- H-CB;
- APPROX-CB;
- MERGE-CB.

**What the printed proof does.** At level one, it proves
\(\dim\mathcal S_{P,Q}=r\), constructs
\[
h_{jk}=\mathrm{Ha}^{Q}_{P_j,P_k},
\]
improves \(h_{11}v\) to an exact representation
\(\mu_{11}(A)=U_1AU_1^\dagger\), builds the other three matrix corners from the
same \(U_1\), and invokes `lem_merging`; see `tex:1382-1412`.

**What breaks under amplification.** It is not enough that \(h_{11}\) and
\(h_{12}\) are near isomorphisms at level one. One needs:

1. \(h_{11}v\) to be an **extended** approximate homomorphism, so that
   APPROX-CB returns an exact representation completely close to it;
2. all four inverse corner maps \(h_{jk}^{-1}\) to satisfy
   `merging0h`--`merging3h` at every matrix level;
3. the one unitary \(U_1\) selected at level one to give the required amplified
   off-diagonal maps, rather than selecting unrelated \(U_1^{(n)}\).

The source does not write these arguments. Its statement that the arguments need
“only trivial modifications” (`tex:1557`) does not supply them.

**Shape of a closing argument.**

1. Use H-CB to make \(h_{11}v\) an extended \(O(e)\)-homomorphism.
2. Apply APPROX-CB with exact target
   \(\mathcal B(\mathcal S_{P,Q})\), obtaining one exact \(*\)-homomorphism
   \(\mu_{11}\) completely \(O(e)\)-close.
3. The level-one dimension calculation forces \(\mu_{11}\) to be conjugation by
   one unitary \(U_1:\mathbb C^r\to\mathcal S_{P,Q}\).
4. Amplify that same \(U_1\); use H-CB and Neumann inversion to prove the four
   completely bounded versions of `merging0h`--`merging3h`.
5. Apply MERGE-CB.

**Price.** A universal \(C_{\rm ext}\) built from \(C_H,C_{\rm app}\), and
\(C_{\rm merge}\), plus a universal smallness threshold. The norm-one diagonal
in APPROX-CB prevents dependence on \(r\).

**Classification:** **(c) GAP.**

---

### MAIN-CB — assembly of `sec_proof_main`

**Contract.** For every finite-dimensional extended
\(\varepsilon\)-\(C^*\)-algebra \(\mathcal A\), one finite-dimensional
\(C^*\)-algebra \(\mathcal B\) and one map \(v:\mathcal B\to\mathcal A\) satisfy,
for every \(n\ge1\),
\[
\|v_n(XY)-v_n(X)v_n(Y)\|
\le C_{\rm main}\varepsilon\|X\|\|Y\|,
\]
\[
(1-C_{\rm main}\varepsilon)\|X\|
\le\|v_n(X)\|
\le(1+C_{\rm main}\varepsilon)\|X\|,
\]
together with the unit and involution conditions, with a universal
\(C_{\rm main}\).

**Edges.** Level-one projection selection; P-TENS; COMP-CB; IMPROVE-CB;
MERGE-CB; EXT-CB.

**Uniform-constant mechanism.** The three stages are exactly the printed stages
at `tex:1414-1444`, but with the following induction invariant:

> after each extension or binary merge, the *same level-one map* is an extended
> inclusion, and IMPROVE-CB resets its error to
> \(c_0^{\rm cb}\varepsilon'\).

The source already uses this reset at level one:

> “Finally, we use Corollary~\ref{cor_improvement} to replace \(v_{r-1}^+\) with a \(c_0\eps'\)-isomorphism \(v_r\).” (`tex:1441`)

and again after every final merge:

> “Each step includes the application of Corollary~\ref{cor_merge_sum} followed by the use of Corollary~\ref{cor_improvement} to reduce the errors.” (`tex:1443`)

Therefore the error does not accumulate with \(r\), the number of equivalence
classes, or the total block count. All merges are binary. Maximum-dimensionality
and dimension counting are level-one termination devices and contribute no norm
constant.

Once EXT-CB is supplied, this is a finite induction with a fixed error reset.

**Classification:** **(b) MECHANICAL CONDITIONAL ON THE TWO GAP NODES.**

## 4. The correction at `tex:1551-1555`

### 4.1 Correct statement

The displayed estimate must be
\[
\boxed{
\left|\langle X,X\rangle_n-\|X\|_{n,1}^{\,2}\right|
\le C(\delta+\varepsilon)\|X\|_{n,1}^{\,2}
}
\tag{4.1}
\]
for \(X\in M_{n,1}\otimes\mathcal S_{P,Q}\), with \(C\) independent of \(n\).

The source's level-one version already has the required dimensional form:

> “\(\bigl|\braket{X}{X}-\|X\|^2\bigr|\le O(\delta+\eps)\ts\|X\|^2\).” (`tex:1129-1131`)

### 4.2 Proof

Let
\[
x:=\|X\|_{n,1},\qquad t:=\langle X,X\rangle_n.
\]
By the exact column identity at `tex:1547-1550`,
\[
X^\dagger\cdot X=t\,\widetilde Q. \tag{4.2}
\]
The positivity argument in the level-one `lem_PQ_Hilb` applies to the scalar
inner product, so \(t\ge0\).

Embed \(X\) as a rectangular corner of \(M_{n+1}\otimes\mathcal A\). The
\(\varepsilon\)-\(C^*\) axiom and submultiplicativity give
\[
(1-\varepsilon)x^2
\le\|X^\dagger X\|
\le(1+\varepsilon)x^2. \tag{4.3}
\]
This uses the source's defining axiom

> “\(\|X^{\dag}X\|\ge (1-\eps)\ts\|X\|^{2}\)” (`tex:425-428`)

and its stated upper-bound consequence at `tex:430`.

By COMP-CB, applied once to the rectangular elements \(X^\dagger,X\),
\[
\|X^\dagger\cdot X-X^\dagger X\|
\le C_{\rm co}e\,x^2. \tag{4.4}
\]
Also, since \(\widetilde Q=\operatorname{Co}_Q(Q)\) and \(Q\) is a
nonvanishing \(\delta\)-projection,
\[
\bigl|\|\widetilde Q\|-1\bigr|\le C_Qe. \tag{4.5}
\]
Combining (4.2)--(4.5) gives
\[
\left|t\|\widetilde Q\|-x^2\right|
\le(\varepsilon+C_{\rm co}e)x^2.
\]
For a universal smallness threshold, \(1-C_Qe>0\); division by
\(\|\widetilde Q\|=1+O(e)\) yields
\[
|t-x^2|\le C e x^2,
\]
which is (4.1). No estimate contains a sum over the \(n\) entries of \(X\).

### 4.3 Norm comparison

Write \(t=x^2(1+s)\), where \(|s|\le Ce\). If \(Ce\le1/2\), then
\[
\frac{\sqrt t}{x}=\sqrt{1+s}
\]
and
\[
\left|\sqrt{1+s}-1\right|
=\frac{|s|}{\sqrt{1+s}+1}
\le |s|.
\]
Hence
\[
(1-Ce)x\le\sqrt t\le(1+Ce)x
\]
after enlarging \(C\) harmlessly. Thus the conclusion printed after the faulty
display,

> “and hence, \(\|X\|_\Euc=\sqrt{\braket{X}{X}}\) is equal to \(\|X\|\) up to a \(1\pm O(\eps+\delta)\) factor.” (`tex:1555`)

does genuinely follow from the corrected squared estimate.

This proof is conditional only on COMP-CB, whose amplification is mechanical; it
does not depend on H-CB.

## 5. Universal-constant ledger through `th_factorization`

### 5.1 Ledger

| Step | Bound/constant contributed | Exact dimension-free mechanism | Status/risk |
|---|---|---|---|
| Functional calculus | For \(\eta<1/4\), \(\|\widetilde\Phi-\Phi\|_{\rm cb}\le C_\theta\eta\). | A scalar Taylor series in the Banach algebra of cb maps. The source says the series “converges if \(\eta<1/4\)” and gives the cb bound (`tex:2171-2179`). No basis or block sum occurs. | Dimension-free. Use a stricter universal threshold, e.g. \(\eta\le1/8\), for a uniform linear Taylor bound. |
| Approximate-algebra estimates | \(\mathcal A=\operatorname{Im}\widetilde\Phi\) is an extended \(C_A\eta\)-\(C^*\) algebra for \(\eta\le\eta_A\). | The source states this at `tex:2192-2194` and explicitly applies the same equations to \(1_{M_n}\otimes\Phi\) at `tex:2208-2209`. UCP maps and their amplifications are contractions; the proof uses a fixed number of products and triangle inequalities. | Structurally dimension-free, but the long proof of `Phi_assoc1/2` was not independently re-proved in this wave. |
| Error reduction | Each raw inclusion below a universal \(\delta_{\max}^{\rm cb}\) is replaced by an extended \(c_0^{\rm cb}\varepsilon\)-inclusion. | APPROX-CB uses a whole-algebra diagonal of projective norm one; INC-CB turns its level-one lower bound into one bound for all \(n\). The reset occurs after each binary extension/merge, so its cost is not multiplied by the number of blocks. | Dimension-free by IMPROVE-CB; the numerical values of \(\delta_{\max}^{\rm cb},c_0^{\rm cb}\) are not extracted. |
| Tensor extension | Common constants \(C_{\rm co},C_{\rm col},C_H,C_{\rm ext}\) must control all amplified compression, column, module, and extension bounds. | Isometric tensoring handles projection relations; fixed rectangular corners handle compression and column norms; the proposed H-CB proof tests whole columns rather than entries. | **Open exactly at H-CB and EXT-CB.** This is the principal possible \(n\)-dependence. |
| Main extended structure theorem | \(v:\mathcal B\to\mathcal A\) has extended error \(C_E C_A\eta\), for \(C_A\eta\le\varepsilon_E\). | Binary merging, norm-one diagonals, and error reset after each step. | **Open:** \(C_E,\varepsilon_E\) are not earned until H-CB and EXT-CB close. |
| Raw factor maps | \(\widetilde\Delta=v\), \(\widetilde\Upsilon=v^{-1}\widetilde\Phi\), with cb norms and product errors bounded by \(C_T\eta\), where \(C_T\) is a fixed expression in \(C_\theta,C_A,C_E\). | Composition of a fixed number of extended maps. The exact identities and cb bounds are printed at `tex:2749-2766`. | Dimension-free conditional on MAIN-CB. |
| CP-ization of \(\widetilde\Delta\) | A CP map \(\Delta'\) with \(\|\Delta'-\widetilde\Delta\|_{\rm cb}\le C_{\Delta'}\eta\). | Average over an exact **whole-algebra norm-one diagonal**. Total weight is one, so there is no \(m\) or block-size factor. Complete positivity follows from exact diagonal centrality, not exact multiplicativity of \(\widetilde\Delta\). | The formula at `tex:2780-2783` is false as printed; use the valid Haar diagonal at `tex:1245`. With that repair, the local step is dimension-free. |
| Normalize \(\Delta'\) | \(\Delta(X)=a^{-1/2}\Delta'(X)a^{-1/2}\), \(a=\Delta'(I)\), and \(\|\Delta-\widetilde\Delta\|_{\rm cb}\le C_\Delta\eta\). | If \(\|a-I\|\le C_{\Delta'}\eta<1/2\), scalar functional calculus gives a universal Lipschitz bound for \(a^{-1/2}\). | No dimension dependence; requires one universal smallness inequality. Source formula at `tex:2797-2801`. |
| Degree two/three estimates | Constants \(C_2,C_3\) in `Delta_norm`, `PhiDelta1/2/3`. | Fixed-length telescoping and one use of `Phi_assoc1` at each amplification; see `tex:2803-2829`. | No \(n\)-loss because every estimate is in the amplified operator norm. |
| CP-ization of \(\widetilde\Upsilon\) | A CP component map \(\Upsilon'\) with \(\|\Upsilon'-\widetilde\Upsilon\|_{\rm cb}\le C_{\Upsilon'}\eta\). | `lem_RC` is per block (`tex:2840-2857`). The output algebra \(\bigoplus_j\mathcal B(\mathcal L_j)\) has the maximum norm, and the source estimates each component uniformly at `tex:2871-2892`; there is no sum over \(j\). | No dependence on \(m\), \(\dim\mathcal L_j\), or \(n\), conditional on the preceding \(\Delta\) estimates. |
| Normalize \(\Upsilon'\) | \(\Upsilon(X)=b^{-1/2}\Upsilon'(X)b^{-1/2}\), \(b=\Upsilon'(I)\), with \(C_\Upsilon\eta\) cb error. | Same inverse-square-root functional calculus, now in the direct-sum algebra with maximum norm. | Dimension-free for \(C_{\Upsilon'}\eta<1/2\). Source formula at `tex:2895-2899`. |
| Final factorization | One \(K\) controls `DelUps`, `UpsDel2`, and \(\|\Upsilon\Delta-I\|_{\rm cb}\). | A fixed finite number of compositions/telescoping replacements; UCP maps have cb norm one. | Conditional on the open MAIN-CB constant and the stated approximate-algebra estimates. |

### 5.2 One existential \(K\) and one threshold

Let the constants in the preceding ledger denote the actual coefficients obtained
after each fixed-length estimate, and define
\[
K:=
\max\{K_{\Delta\Upsilon},K_{\rm mult},K_{\Upsilon\Delta},1\},
\tag{5.1}
\]
where:

- \(K_{\Delta\Upsilon}\) is the finite sum/product expression obtained from
  \(C_\theta,C_A,C_E,C_{\Delta},C_{\Upsilon}\);
- \(K_{\rm mult}\) is the corresponding expression for `UpsDel2`;
- \(K_{\Upsilon\Delta}\) is the expression obtained by setting one factor to the
  unit in `UpsDel2`.

Let \(C_{\rm pre}\) be the maximum of the finitely many fixed coefficients that
relate every intermediate \(e=\delta+\varepsilon\) in MAIN-CB, before an error
reset, to the input \(C_A\eta\). Conditional on H-CB and EXT-CB,
\(C_{\rm pre}<\infty\) is universal because every raw operation is either a fixed
corner operation or uses DIAG-1. Let \(\mathfrak T\) be the finite set of all
remaining positive scalar thresholds in the functional-calculus, Neumann, and
inverse-square-root steps. Define
\[
\eta_K:=
\min\left\{
\frac18,\eta_A,\frac{\varepsilon_E}{C_A},
\frac{e_H}{C_{\rm pre}C_A},
\frac{e_{\rm ext}}{C_{\rm pre}C_A},
\frac1{2C_{\Delta'}},\frac1{2C_{\Upsilon'}},
\min\mathfrak T
\right\}.
\tag{5.2}
\]
If H-CB and EXT-CB provide finite universal constants and positive universal
thresholds, then (5.1)--(5.2) give one finite universal \(K\) and one
\(\eta_K>0\). None of their inputs depends on
\(\dim\mathcal H,\dim\mathcal B,m,\dim\mathcal L_j\), or \(n\).

Without those two gap constants, (5.1) is only a conditional definition. The TeX
claims universality, but it does not currently prove that \(C_E<\infty\) uniformly.

## 6. Prioritized attack plan

### Priority 1 — H-CB

**Difficulty:** high.  
**Load-bearing weight:** maximal.  
**Why first:** it is the first place where “apply the old lemma to
\(M_n\otimes\mathcal A\)” is invalid because \(I_n\otimes Q\) is no longer
one-dimensional. It is also the only place where a naive proof visibly risks an
\(n\)-factor.

**Attack mechanism.** Prove a standalone approximate Hilbert-module representation
lemma using rectangular corners of \(M_{2n}\otimes\mathcal A\):

1. use COL-HILB to identify the column norm uniformly;
2. prove \(h_n(Z)X\approx Z\cdot X\) directly in that column norm;
3. test operator norms on arbitrary columns, never on entries;
4. obtain `Ha_prod` from one associator estimate;
5. obtain complete inverse estimates by Neumann series.

**Potential falsity flag.** This is the diagnostic node for failure of the claimed
uniform theorem. If an extended approximate \(C^*\)-algebra can have column norms
for which left multiplication is not uniformly controlled by the corrected scalar
inner product, H-CB—and therefore `th_main_ext` at the claimed uniformity—may be
false. I found no counterexample, and the corrected COL-HILB estimate makes the
theorem plausible, but this is the place to search before investing in assembly.

### Priority 2 — EXT-CB

**Difficulty:** medium-high after H-CB.  
**Load-bearing weight:** maximal.

**Attack mechanism.** Run the five-step plan in the EXT-CB node:
extended \(h_{11}v\), APPROX-CB, one level-one unitary \(U_1\), amplify that same
unitary, then MERGE-CB. The hostile checkpoints are:

- no unitary chosen separately for each \(n\);
- complete closeness of all four corner maps;
- no dependence on the matrix size \(r\);
- exact preservation of bijectivity.

### Priority 3 — end-to-end scalar ledger after the two proofs

**Difficulty:** low-medium.  
**Load-bearing weight:** high.

This is not a new mathematical gap if the two nodes close, but it is necessary
bookkeeping. Assign symbols to every universal coefficient, choose a common
threshold before Stage 1, and verify after each raw extension/merge that its error
lies below \(\delta_{\max}^{\rm cb}\). Then evaluate (5.1)--(5.2).

## 7. Defect register

1. **Squared-norm typo (`tex:1551-1555`).** The printed display compares a scalar
   quadratic form to a norm rather than a squared norm. Section 4 gives the
   corrected statement and proof.

2. **H-CB omitted.** The phrase “generalized in a straightforward way”
   (`tex:1555`) hides the non-one-dimensionality of \(I_n\otimes Q\) and the risk
   of an \(n\)-factor.

3. **EXT-CB omitted.** The source never proves that the level-one unitary and four
   corner maps used in `lem_extension` satisfy uniform complete estimates.

4. **Single-map invariant omitted.** The final sentence at `tex:1557` does not
   explicitly maintain that every improvement, extension, and merge produces one
   level-one map whose *all* amplifications obey the bounds. MAIN-CB states the
   required invariant.

5. **False direct-sum diagonal (`tex:1254`, `tex:2780-2783`).** The Cartesian
   product of arbitrary block designs leaves cross-block terms. Full Haar averaging
   or independent block phases repairs it without a block-count loss.

6. **Compression typing typo (`tex:1109`).** The printed
   \(\beta_{jk}=\operatorname{Co}_{P_j,Q_j}\) must be
   \(\operatorname{Co}_{P_j,Q_k}\).

7. **`lem_add_dim` index typo.** The statement at `tex:1363-1364` gives both
   projection bases \(p\) elements, while the proof immediately uses indices
   \(j\) and \(k\) and sums over \(k\). The intended second cardinality is \(q\).
   This does not affect its level-one use, but it should be corrected before
   formalization.

8. **Unnecessary and false amplified one-dimensional reading.** Any argument that
   calls \(I_n\otimes Q\) one-dimensional is wrong. Only the level-one \(Q\) is
   one-dimensional; its amplifications form matrix Hilbert modules.

9. **Unexpanded Newton constants.** `lem_approx` says the correction is iterated
   “as in Newton's method” (`tex:1313`) but does not multiply out a numerical
   \(\varepsilon_{\max},\delta_{\max},c_0\). Existential universality is plausible
   because DIAG-1 has norm one; numerical extraction remains undone.

10. **Unexpanded raw-step thresholds.** The proof resets errors after each merge,
    but never records one common inequality ensuring every pre-reset error is below
    the same \(\delta_{\max}^{\rm cb}\).

11. **`th_almost_idemp` not fully re-audited here.** The source supplies a long
    dimension-free proof architecture and explicitly amplifies it at
    `tex:2208-2209`, but this strategist wave did not independently re-prove every
    identity in `tex:2239-2723`. The universal ledger therefore records this as an
    imported source theorem, not a newly checked result.

12. **Stronger-than-sketch contracts.** H-CB and EXT-CB above are stronger and more
    explicit than the prose at `tex:1555-1557`: they demand simultaneous operator
    norm, inverse, and product bounds for every \(n\), carried by one map. This
    strengthening is intentional because `th_factorization` consumes exactly that
    strength through:

    > “there exist a finite-dimensional \(C^*\) algebra \(\calB\) and an extended \(O(\eta)\)-isomorphism \(v\colon\calB\to\calA\).” (`tex:2749`)

    and the amplified product estimate at `tex:2758-2766`.

## 8. Deliverable verdict

The decomposition is therefore:

- **ESTABLISHED:** P-TENS, DIAG-1, APPROX-CB, INC-CB;
- **MECHANICAL:** COMP-CB, ALPHA-CB, corrected COL-HILB, IMPROVE-CB,
  MERGE-CB, and MAIN-CB conditional assembly;
- **GAPS:** H-CB and EXT-CB.

No claim in this report is externally verified or repository-validated. The most
valuable next result is a proof or counterexample for H-CB. A proof makes EXT-CB a
sharply scoped second target; a counterexample would directly challenge the
uniformity claimed by `th_main_ext`.
