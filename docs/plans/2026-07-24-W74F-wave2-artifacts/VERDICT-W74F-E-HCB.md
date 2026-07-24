SHA CHECK: PASS — `sha256sum refs/kitaev-2405.02434/approximate_algebras.tex` returned `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`.

# W74F-E hostile-verifier verdict

I read the pinned source first: the \(\varepsilon\)-Banach and
\(\varepsilon\)-\(C^*\) axioms (`tex:407-440`), compression and compressed
products (`tex:1052-1082`), the level-one Hilbert and Ha-map material
(`tex:1123-1160`), `lem_extension` (`tex:1378-1412`), the operator-space
axioms (`tex:1447-1478`), and the amplification passage
(`tex:1470-1557`). I then read and attacked the prover output.

## Per-section verdicts

HCB-0: **VALID.** The five replacements in (3.1) are type-compatible
rectangular products. They can be placed as single off-diagonal blocks in
one \(M_N\otimes\mathcal A\), so the ambient associator is charged once and
Ruan corner embeddings introduce no \(N\)-factor. The charges are
\(2ce+2ce+e+2ce+2ce\le9ce\).

HCB-1a: **VALID.** Writing out only the algebraic indices (without
estimating them), the first term sums to
\[
 \sum_{i,j}(Y_i^\dagger\mathbin{\cdot}Z_{ij})\mathbin{\cdot}X_j,
\]
the second to
\[
 \sum_{i,j}Y_i^\dagger\mathbin{\cdot}(Z_{ij}\mathbin{\cdot}X_j),
\]
and the right side of `Ha_def` to
\(2\sum_{i,j}\langle Y_i,h(Z_{ij})X_j\rangle u_Q\).
This is exactly (4.1). The level-one one-dimensionality of \(Q\) gives
\(Y^\dagger\mathbin{\cdot}V=\langle Y,V\rangle u_Q\) after summing the
column coordinates, and subtracting twice this identity gives (4.3) with
the displayed sign. No estimate or hidden \(n\)-sum enters.

HCB-1b: **VALID.** Taking \(Y=D\) in (4.3) converts the whole right side
into one compressed associator. COL-HILB and
\(\|u_Q\|\ge1-ce\) allow cancellation of \(\|D\|\) with a conversion
factor less than \(2\), so \(C_{\rm act}=18c\) is safe. The multiplication
and action bounds (5.3)--(5.4) use whole rectangular norms. No norm of an
entry and no sum over a column occurs.

HCB-2: **VALID.** Amplified adjointness is the exact block adjoint of
`Ha_dag`. In (6.2), the four respective charges are
\[
 2C_{\rm act},\quad 2C_{\rm as},\quad
 4C_{\rm act},\quad 5C_{\rm act},
\]
whose sum is \(216c=24C_{\rm as}\). The third and fourth charges use the
whole-column action bounds, not a matrix-entry expansion.

HCB-3 (including §2.1 and the conditional inverse): **VALID-WITH-CORRECTIONS.**
The \(\mathbb C\oplus\mathbb C\) example is exact:
\[
 \mathcal S_P=\mathbb C\oplus\mathbb C,\qquad
 \mathcal S_{P,Q}=\mathbb C\oplus0,\qquad
 h_{P,P}(a,b)(x,0)=(ax,0),
\]
so \(h_{P,P}(0,1)=0\). It is therefore a genuine counterexample to an
inverse claim made under only the general H-CB hypotheses. It does not
satisfy the complementary-corner hypotheses of `lem_extension`, and hence
does not refute that lemma. The conditional replacement is exactly the
kind needed there: `tex:1391` first obtains level-one bijectivity and an
\(1-O(e)\) lower bound for its particular \(h_{11}\); after shrinking the
universal threshold, this gives the stipulated \(1/4\) lower bound.

The upper quadratic (7.3), lower-root dichotomy (7.7), dyadic estimate
\(a_{2n}\ge a_n/2\), and passage from powers of two to arbitrary \(n\) are
valid. The off-diagonal square argument (7.11) is also valid. Two wording
corrections are required:

1. In (1.1), \(\bigl|\|u_T\|-1\bigr|\le C_{\rm co}e\) is false for an
   arbitrary, possibly vanishing, projection \(T\) (take \(T=0\) and
   \(e=0\)). It must read
   \[
   \|u_T\|\le1+C_{\rm co}e
   \quad\text{for arbitrary }T,\qquad
   \bigl|\|u_T\|-1\bigr|\le C_{\rm co}e
   \quad\text{for nonvanishing }T.
   \]
   The proof uses the lower estimate only for the one-dimensional \(Q\),
   which is nonvanishing, and uses only the general upper estimate for
   \(u_P\). Thus no subsequent coefficient changes.
2. “Established separately” must mean “obtained with a universal
   \(1-O(e)\) lower bound and then made \(\ge1/4\) by shrinking the common
   threshold”; bare bijectivity alone would not provide the quantitative
   hypothesis.

HCB-4: **VALID-WITH-CORRECTIONS.** Entrywise algebra, used as an identity
rather than an estimate, gives
\[
 [Z^\dagger\mathbin{\cdot}Z]_{ij}
 =\sum_k\langle Z_{ki},Z_{kj}\rangle u_Q
 =G_{ij}u_Q.
\]
Thus (8.4) uses only the level-one fact
\(\mathcal S_{Q,Q}=\mathbb C u_Q\); it never treats
\(I_n\otimes Q\) as one-dimensional. Ruan's scalar tensor identity and
one level-\(n\) \(C^*\)-estimate then give (8.7), and (8.8)--(8.12) are
uniform.

The sentence after (8.12) should not say that two-sided norm bounds alone
imply bijectivity in the contract's potentially infinite-dimensional
generality. The correct stated reason is the Neumann condition
\[
 \|J_{P,Q,n}^{-1}(h_{P,Q,n}-J_{P,Q,n})\|
 \le \frac{40ce}{1-4ce}<1,
\]
and likewise for the adjoint corner. This condition follows from
(8.7) and (8.10), proves bijectivity, and supports the constants in
(8.13). In the finite-dimensional application, equal dimensions would
also suffice.

Constant ledger: **VALID-WITH-CORRECTIONS.** The arithmetic recomputes as
\[
\begin{aligned}
C_{\rm as}&=9c,& C_{\rm act}&=18c,\\
C_{\rm prod}&=(2\cdot18+2\cdot9+4\cdot18+5\cdot18)c=216c,\\
C_{\rm unit}&=(2\cdot18+2)c=38c,&
C_{\rm up}&=(2+216)c=218c,\\
C_{\rm diag}&=(2+3\cdot216)c=650c,&
C_{\rm rect,low}&=(650+2+216)c=868c.
\end{aligned}
\]
The inverse coefficients \(1300c\) and \(1736c\), the Gram coefficient
\(4c\), and \(C_{\rm sp}=40c\) are safe. Since \(ce\le10^{-4}\),
\[
 3C_{\rm prod}e\le0.0648<\tfrac18,\quad
 C_{\rm diag}e\le0.065,\quad
 868ce\le0.0868,\quad
 44ce\le0.0044,
\]
so every root and Neumann denominator used is valid.
\(C_H=4000c\) dominates every displayed coefficient. The only correction
to the ledger is the compressed-unit input split stated under HCB-3; it
does not alter \(c\), \(C_H\), or \(e_H=1/(10000c)\). These are explicit
relative to the sanctioned but numerically unnamed universal COMP-CB and
COL-HILB constants; they are not absolute decimal constants. No ledger
entry depends on \(n\), \(\dim\mathcal A\), a block count, or a block
dimension.

## Overall verdict

**VALID-WITH-CORRECTIONS.** Conditional on the sanctioned COMP-CB and
corrected COL-HILB inputs, H-CB holds in the conditional-inverse form with
universal, dimension-free constants; \(C_H=4000c\) and
\(e_H=1/(10000c)\) are safe relative choices. I found no \(n\)-growth
family. The unconditional inverse assertion for arbitrary \(h_{P,P}\) is
false, exactly as the prover reports, but the lower/inverse bootstrap
under a fixed level-one lower bound and bijectivity is valid and is the
form consumed by `lem_extension`. No H-CB analytic estimate remains open
after the corrections above. EXT-CB, including the construction using
one level-one \(U_1\) at every amplification, and the resulting
unconditional end-to-end \(K\)-ledger remain separate open work.

## Contract-impact note

Yes. The registered `conj-hcb` contract quantifies arbitrary
\(P,R,S\) and then mentions “inverse” without recording the necessary
faithfulness hypothesis. Replace the phrase beginning “the uniform unit,
norm, inverse, homomorphism” by the following exact clause:

> the uniform unit, upper-norm, homomorphism, and canonical-identity closeness estimates required by `lem_extension`; moreover, if the level-one lower modulus of \(Ha^Q_{P,P}\) is at least \(1/4\), then every amplification has lower modulus at least \(1-C_H e\), and if \(Ha^Q_{P,P}\) is also bijective at level one then every amplification is bijective with inverse norm at most \(1+C_H e\); the analogous off-diagonal inverse bound for \(Ha^Q_{P,R}\) is asserted only when \(Ha^Q_{P,R}\) is bijective at level one and \(Ha^Q_{R,R}\) satisfies that diagonal lower-modulus hypothesis

This does not weaken what EXT-CB or `lem_extension` can consume.
At `tex:1391`, the particular \(h_{11}\) is first proved to be a
level-one \(O(e)\)-isomorphism, hence it meets both conditional hypotheses
for a universal smallness threshold. The special \(h_{12},h_{21},h_{22}\)
corners are covered by the canonical-identity estimates.

## Checks performed that passed

1. Recomputed the primary-source SHA256 exactly.
2. Read `Ha_def`, `Ha_dag`, `Ha_prod`, the level-one Hilbert norm estimate,
   the operator-space axioms, the extended-\(C^*\) axioms, the printed
   amplification passage, and `lem_extension` directly from the pinned
   TeX.
3. Re-derived corrected COL-HILB from the exact column identity, one
   rectangular compressed-product estimate, and one \(C^*\)-estimate in
   \(M_{n+1}\otimes\mathcal A\).
4. Checked that every rectangular chain used in HCB-0 embeds isometrically
   as a sparse block chain in one square amplification.
5. Recomputed all five HCB-0 error charges.
6. Expanded every index in the claimed exact variational identity and
   checked its types, coefficients, and sign.
7. Checked that (4.2) is a sum of level-one scalar identities and does not
   apply `lem_PQ_Hilb` to \(I_n\otimes Q\).
8. Recomputed the norm conversion and cancellation in (5.1)--(5.2).
9. Checked the whole-column multiplication bound (5.3) and action bound
   (5.4).
10. Checked exact amplified adjointness block by block.
11. Recomputed each of the four product-defect terms in (6.2).
12. Checked the amplified unit estimate, after separating the arbitrary
    compressed-unit upper bound from the nonvanishing-unit lower bound.
13. Re-derived the diagonal upper quadratic and its positive-root bound.
14. Re-derived the diagonal lower quadratic, verified the two-root
    dichotomy numerically at the stated threshold, and checked the dyadic
    induction and monotonic passage to arbitrary \(n\).
15. Checked that level-one bijectivity algebraically amplifies and that
    the inverse norm is the reciprocal lower modulus.
16. Re-derived the off-diagonal square estimate and the coefficients
    \(868c\), \(1736c\), and the stated safe upper coefficient.
17. Evaluated the \(\mathbb C\oplus\mathbb C\) example exactly and checked
    both that it kills the literal unconditional inverse and that it is
    not a counterexample to the hypotheses of `lem_extension`.
18. Checked at `tex:1391` that `lem_extension` obtains level-one
    faithfulness/bijectivity before using \(h_{11}^{-1}\).
19. Expanded the Gram identity (8.4) coordinate by coordinate.
20. Checked the Ruan scalar-tensor norm step (8.5) and the one-shot
    \(C^*\) square estimate (8.6).
21. Recomputed the canonical \(J\) distortion and verified that it rules
    out an operator-space norm hidden from column action.
22. Checked (8.8)--(8.11), including the normalization by
    \(q_0=\alpha^{-1}u_Q\) and the right-unit error.
23. Verified the Neumann condition for the special maps and the inverse
    and inverse-difference constants in (8.13).
24. Recomputed every entry in the constant ledger and every smallness
    denominator/root condition.
25. Traced all uses of one-dimensionality and confirmed that each is
    level-one scalarization, never a one-dimensionality assertion for
    \(I_n\otimes Q\).
26. Searched for \(n\)-growth in exact matrix-algebra, scalar-tensor, and
    direct-sum configurations. Exact algebras reduce Ha to corner
    multiplication; direct sums produce the exhibited kernel but no
    amplification growth. For \(e>0\), the whole-column action estimate,
    the Gram estimate in the special corners, and the dyadic root
    bootstrap in faithful diagonal corners exclude the three possible
    growth mechanisms without entrywise summation.
