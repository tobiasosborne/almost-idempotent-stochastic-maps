A: VALID
B: VALID
C: VALID
D: VALID

# W74F batched hostile-verifier report

Primary source checked:
`refs/kitaev-2405.02434/approximate_algebras.tex`, SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`.

I read each target against its own brief, the source TeX, and
`AUDIT-W73B-ROUTE-F.md`. I did not treat the W73b audit as an oracle.

## A — PRH

### Attacks run

1. **Operator norm to one-sided mass.** For \(R=MA\), positivity and unitality of
   both factors make every row of \(R\) a probability vector. Hence, row by row,
   \[
   \|R_{s\bullet}-e_s\|_1
   =(1-R_{ss})+\sum_{t\ne s}R_{st}
   =2(1-R_{ss}).
   \]
   Thus
   \[
   \sum_i\mu_s(i)(1-a_{is})=1-R_{ss}\le\varepsilon/2.
   \]
   The factor \(2\) is earned and uses stochasticity exactly where the target
   says it does. The identity
   \(\|T\|_{\infty\to\infty}=\max_i\sum_j|t_{ij}|\) itself does not require
   stochasticity.

2. **Core boundary cases.** With
   \(C_s=\{i:a_{is}>1-\lambda\}\), two distinct cores cannot meet for
   \(\lambda\le1/2\): at \(\lambda=1/2\), the strict inequalities would still
   force two coordinates to have sum \(>1\). The requested
   \(\varepsilon<1/2\) gives \(\lambda=\sqrt{\varepsilon/2}<1/2\); the proof
   actually also covers \(\varepsilon=1/2\). For \(k=1\), the sole membership
   coordinate equals \(1\), so the construction degenerates correctly.

3. **Nonemptiness and conditioning.** Markov's inequality gives
   \[
   \beta_s=\mu_s(C_s^c)\le\frac{\varepsilon}{2\lambda}=\lambda<1.
   \]
   Therefore \(\mu_s(C_s)=1-\beta_s>0\), not merely
   \(C_s\ne\varnothing\), and the conditional probability \(\nu_s\) is legal.
   The purported degenerate case \(\mu_s(C_s)=0\) is excluded.

4. **Exact retraction.** Since \(\nu_s\) is supported on \(C_s\), every row of
   \(\widehat A\) sampled by \(\nu_s\) is exactly \(e_s\). Therefore
   \[
   (N\widehat A)_{st}
   =\sum_{i\in C_s}\nu_s(i)\widehat a_{it}
   =\delta_{st}.
   \]
   Rows outside all cores never enter this sum. Thus \(N\widehat A=I_k\)
   exactly and \(E=\widehat A N\) is exactly idempotent.

5. **Final norm assembly and dimension freedom.** Conditioning costs
   \(\varepsilon/\lambda\) in every row. Changing a row in \(C_s\) to the
   \(s\)-core row costs at most \(2\lambda\); a row outside all cores costs
   zero. These are maxima over rows, not sums over rows or cores. Hence
   \[
   \|AM-E\|_{\infty\to\infty}
   \le\frac{\varepsilon}{\lambda}+2\lambda.
   \]
   Minimization gives \(\lambda=\sqrt{\varepsilon/2}\) and
   \(2\sqrt{2\varepsilon}\). The value \(3\sqrt\varepsilon\) comes from the
   weaker choice \(\lambda=\sqrt\varepsilon\); the two derivations address the
   same statement.

6. **Zero endpoint.** If \(\varepsilon=0\), then \(MA=I_k\) and
   \(E=AM\) satisfies \(E^2=A(MA)M=AM\) and has zero error. No conditioning at
   \(\lambda=0\) is needed.

7. **Sharpness against every idempotent.** I rechecked the row-coincidence
   lemma used in the lower bound. For a stochastic idempotent \(F\), a state
   \(i\) with \(f_{ii}>0\) lies in a recurrent class, and every \(j\) with
   \(f_{ij}>0\) has \(F_{j\bullet}=F_{i\bullet}\). The target proves this
   without importing a classification theorem. In the displayed
   \(k=2,n=4\) family, if
   \(d=\|AM-F\|_{\infty\to\infty}<\lambda\), then both
   \(f_{x_1x_1}\) and \(f_{x_1y_1}\) are positive, forcing the \(x_1\) and
   \(y_1\) rows of \(F\) to coincide. Their corresponding \(AM\)-rows are
   \(2\lambda\) apart, contradicting \(2\lambda\le2d\). Thus every stochastic
   idempotent satisfies
   \[
   \|AM-F\|_{\infty\to\infty}\ge\lambda
   =\sqrt{\varepsilon_\lambda/2}.
   \]
   This is PRH sharpness, not an illicit transfer of the known sharpness of
   `op-classical`.

### What survived

The complete target survives, including the exponent-sharpness claim.

**Transcribable statement A.** Let \(k,n\ge1\). Let
\(A:\ell_\infty(k)\to\ell_\infty(n)\) and
\(M:\ell_\infty(n)\to\ell_\infty(k)\) be positive unital maps. If
\[
\|MA-I_k\|_{\infty\to\infty}\le\varepsilon,\qquad
0\le\varepsilon<\frac12,
\]
then there is a positive unital idempotent
\(E:\ell_\infty(n)\to\ell_\infty(n)\) such that
\[
\|AM-E\|_{\infty\to\infty}\le2\sqrt{2\varepsilon}.
\]
Moreover, there are examples with \(\varepsilon\downarrow0\) for which every
positive unital idempotent \(F\) satisfies
\[
\|AM-F\|_{\infty\to\infty}\ge\sqrt{\varepsilon/2}.
\]

No correction is required.

## B — exact whole-algebra diagonal

### Attacks run

1. **Printed formula.** At `tex:1254` and `tex:2780-2783`, the source takes
   Cartesian products of per-block unitary designs and direct-sums the chosen
   unitaries. For \(\mathcal B=\mathbb C\oplus\mathbb C\), choosing the
   one-point design \(\{1\}\) in each block gives
   \[
   D_{\rm print}=1_{\mathcal B}\otimes1_{\mathcal B}.
   \]
   For \(e_1=(1,0)\),
   \[
   e_1D_{\rm print}=e_1\otimes1_{\mathcal B}
   \ne1_{\mathcal B}\otimes e_1=D_{\rm print}e_1.
   \]
   Normalization holds, but centrality fails. The target identifies the exact
   defect.

2. **Finite repair.** For each block \(M_{d_r}\), take a finite convex
   representation
   \(D_r=\sum_\alpha p_{r\alpha}U_{r\alpha}^\dagger\otimes U_{r\alpha}\)
   of its Haar diagonal. For independent signs
   \(\epsilon\in\{\pm1\}^m\), set
   \[
   W_{\alpha,\epsilon}
   =\bigoplus_r\epsilon_rU_{r\alpha_r},\qquad
   q_{\alpha,\epsilon}=2^{-m}\prod_rp_{r\alpha_r}.
   \]
   The exact moment
   \[
   2^{-m}\sum_\epsilon\epsilon_r\epsilon_s=\delta_{rs}
   \]
   kills every cross-block tensor. Thus the repaired object is the blockwise
   sum of the true \(D_r\)'s and satisfies centrality and normalization
   exactly. No Haar integral remains in the delivered representation.

3. **Universal norm.** Every \(W_{\alpha,\epsilon}\) is unitary and the
   \(q_{\alpha,\epsilon}\)'s are probability weights, so the displayed
   coefficient sum is \(1\) and the projective norm is at most \(1\).
   Contractivity of multiplication and \(\pi(D)=I\) give the reverse
   inequality. Hence \(\|D\|_\pi=1\), independently of the number of blocks,
   all block dimensions, and the number of finite terms.

4. **Correct algebra.** At every use, the diagonal belongs to the exact
   finite-dimensional \(C^*\)-algebra \(\mathcal B\). Neither the construction
   nor the downstream argument assumes a diagonal for the approximate algebra
   \(\mathcal A\).

5. **CP-ization.** I rederived the matrix entries. Exact centrality changes
   \[
   \sum_tq_tY_{ba}^\dagger Y_{bc}W_t^\dagger\otimes W_t
   \quad\text{to}\quad
   \sum_tq_tY_{ba}^\dagger W_t^\dagger\otimes W_tY_{bc}.
   \]
   Applying
   \(a\otimes b\mapsto
   \Phi(\widetilde\Delta(a)\widetilde\Delta(b))\), summing over \(b\), and
   using preservation of the involution gives
   \[
   \Delta'_n(Y^\dagger Y)
   =\sum_tq_t\Phi_n(Z_t^\dagger Z_t)\ge0,\qquad
   Z_t=\widetilde\Delta_n((I_n\otimes W_t)Y).
   \]
   Exact multiplicativity of \(\widetilde\Delta\) is not used.

6. **Unitality and constants.** The target's symbolic estimate
   \[
   \|\Delta'-\widetilde\Delta\|_{\rm cb}
   \le(c_2+c_\Phi A^2)\eta
   \]
   follows directly from the amplified product estimate and the convex
   coefficient sum \(1\). If
   \(H=\Delta'(I)\) and \(\|H-I\|\le e\le1/2\), conjugation by \(H^{-1/2}\)
   is CP, makes the map exactly unital, and costs a universal multiple of
   \(e\). The target's safe bound \(6e\) is valid. Its degree-two and
   degree-three propagation bounds use only fixed-length telescoping and
   contain no block or amplification count.

7. **Use-site completeness.** An independent source search found the algebraic
   consumers at `tex:480-490`, `tex:1228-1319`, the repeated improvement calls
   at `tex:1415-1443`, `lem_approx_ext` at `tex:1508-1535`, the outline call at
   `tex:1557`, the whole-algebra CP construction at `tex:2771-2829`, and the
   separate per-block uses at `tex:2840-2899`. These are all present in the
   target's ledger. The occurrence at `tex:986` is the topological diagonal
   map and is irrelevant.

8. **Cone projection.** No projection onto a CP cone survives. Positivity is
   exact after the central-diagonal repair; the later inverse-square-root
   conjugation is an ordinary unitalization and preserves CP.

### What survived

The target closes the local printed-diagonal flaw and all its consumers. It
does not, and does not claim to, close the separate amplified structure-theorem
gap.

**Transcribable statement B.** Every finite-dimensional \(C^*\)-algebra
\(\mathcal B=\bigoplus_{r=1}^mM_{d_r}\) admits finitely many unitaries
\(W_t\in\mathcal B\) and weights \(q_t\ge0\), \(\sum_tq_t=1\), such that
\[
D=\sum_tq_tW_t^\dagger\otimes W_t
\]
satisfies
\[
ZD=DZ\quad(Z\in\mathcal B),\qquad
\sum_tq_tW_t^\dagger W_t=I_{\mathcal B},
\]
and
\[
\|D\|_\pi
=\sum_tq_t\|W_t^\dagger\|\,\|W_t\|=1.
\]
All bounds are independent of \(m\), the \(d_r\)'s, and
\(\dim\mathcal B\). For any involution-preserving linear
\(\widetilde\Delta:\mathcal B\to\mathcal B(\mathcal H)\) and any UCP map
\(\Phi\), the averaging formula
\[
\Delta'(X)=\sum_tq_t\Phi\!\left(
\widetilde\Delta(XW_t^\dagger)\widetilde\Delta(W_t)\right)
\]
defines a completely positive map; this conclusion uses exact centrality of
\(D\) and does not require exact multiplicativity of
\(\widetilde\Delta\).

No correction to the target is required.

## C — decomposition of `th_main_ext`

### Attacks run

1. **Completeness of the dependency set.** I traced the level-one construction
   at `tex:1054-1444`, the amplified definitions and lemmas at
   `tex:1447-1536`, and the outline at `tex:1538-1557`. Level-one projection
   selection, dimension counting, and equivalence-class selection do not need
   amplified one-dimensionality. Their outputs need tensor-stable projection,
   compression, merge, improvement, and extension estimates, all of which are
   represented in the target graph. I found no missing third hard node.

2. **P-TENS and COMP-CB.** The identity
   \(\|I_n\otimes X\|_n=\|X\|\) is proved at `tex:1475`.
   Left/right multiplication by \(I_n\otimes P\) acts entrywise, so the power
   series defining compression commutes with amplification. Hence
   \[
   1_{M_n}\otimes\operatorname{Co}_{P,Q}
   =\operatorname{Co}_{I_n\otimes P,I_n\otimes Q}
   \]
   exactly, and the equality of their images follows. This is genuinely
   mechanical.

3. **ALPHA-CB and MERGE-CB.** Applying the level-one lemmas inside
   \(M_n\otimes\mathcal A\) introduces only the fixed \(p q\) corner count.
   Every downstream use has \(p,q\le2\), so \(pq\le4\). Binary merging and
   maximum norms prevent a summand-count loss. The target gives a checkable
   reason, not merely the word “straightforward.”

4. **COL-HILB and the squared correction.** The printed formula
   `tex:1551-1553` is dimensionally wrong. For a column
   \(X\in M_{n,1}\otimes\mathcal S_{P,Q}\), the exact identity is
   \(X^\dagger\!\cdot X=\langle X,X\rangle\widetilde Q\).
   Treating \(X\) as one rectangular element in
   \(M_{n+1}\otimes\mathcal A\), rather than summing entrywise estimates, gives
   \[
   \left|\langle X,X\rangle-\|X\|_{n,1}^2\right|
   \le C(\delta+\varepsilon)\|X\|_{n,1}^2
   \]
   with \(C\) independent of \(n\). Taking square roots then gives the claimed
   \(1\pm O(\delta+\varepsilon)\) norm comparison. The target's proof is sound.

5. **APPROX-CB and INC-CB.** `lem_approx_ext` uses one level-one correction:
   its displayed \(w'_n\) is entrywise \(1_{M_n}\otimes w'\), and the same
   norm-one diagonal controls all \(n\). `prop_inc_ext` first proves the fixed
   loss \(a_{2n}\ge a_n/2\), then re-applies the scalar lower-bound proposition
   whenever \(a_n>2\delta\). Induction over dyadic levels and monotonicity of
   \(a_n\) give a common lower bound. Neither proof hides an \(n\)-factor.

6. **IMPROVE-CB.** APPROX-CB supplies one completely close map; a level-one
   lower bound stays bounded away from zero for a universal
   \(\delta_{\max}^{\rm cb}\); INC-CB promotes that bound uniformly to all
   levels. This correctly removes the input \(\delta\) from the output error
   and gives \(c_0^{\rm cb}\varepsilon\). Numerical coefficients remain
   unexpanded, but universality is the relevant contract.

7. **H-CB.** The target correctly refuses to call this mechanical.
   \(I_n\otimes Q\) is not one-dimensional:
   \(\mathcal S_{I_n\otimes Q,I_n\otimes Q}
   =M_n\otimes\mathcal S_{Q,Q}\).
   The level-one proof of the \(\mathrm{Ha}\) estimates therefore cannot simply
   be reapplied. A proof must estimate whole column operators, not \(n\)
   entries. This is a genuine gap.

8. **EXT-CB.** Even after H-CB, one must prove that the exact representation
   approximating \(h_{11}v\) is completely close, that the same level-one
   unitary \(U_1\) is amplified at every level, and that all four inverse
   corner maps satisfy the merge hypotheses completely. The source does not
   write this argument. Treating it as a second gap is correct rather than
   double-counting H-CB.

9. **MAIN-CB.** Conditional on EXT-CB, the remaining construction is a finite
   level-one selection process with binary extended merges and an amplified
   error reset after each raw step. The target states the necessary invariant:
   every stage carries one level-one map whose amplifications all satisfy the
   same bound. This makes the conditional mechanical classification
   checkable.

10. **Constant ledger and possible falsity.** The functional-calculus,
    norm-one diagonal, fixed-corner, maximum-norm, inverse-square-root, and
    fixed-length telescoping mechanisms are dimension-free. An unconditional
    \(K\) is not earned until H-CB and EXT-CB supply universal constants and
    thresholds. The target does not claim a counterexample; it labels possible
    failure of H-CB as a search risk and explicitly says that it found none.

### What survived

The decomposition is complete at the requested resolution. The theorem is not
proved by this target; the target correctly identifies the two pieces that
remain to be proved or refuted.

**Transcribable statement C.** A proof of `th_main_ext` reduces to the following
two uniform amplified statements, in addition to the established/mechanical
nodes listed in the target:

1. **H-CB.** For every amplification level \(n\), the maps
   \(1_{M_n}\otimes\mathrm{Ha}^{Q}_{P,R}\), acting on the Hilbert-column
   operator spaces induced by a level-one one-dimensional projection \(Q\),
   satisfy the adjoint, product, unit, norm, and inverse estimates required in
   `lem_extension`, with one constant independent of \(n\), the dimensions,
   and the number of summands.

2. **EXT-CB.** Under the hypotheses of `lem_extension`, if
   \(v:M_r\to\mathcal S_P\) is an extended \(\delta\)-isomorphism, then there is
   one map \(v_+:M_{r+1}\to\mathcal A\) that is an extended
   \(C_{\rm ext}(\delta+\varepsilon)\)-isomorphism, where \(C_{\rm ext}\) and
   the smallness threshold are independent of \(r\), every amplification
   level, and \(\dim\mathcal A\).

No correction to the target is required.

## D — audit of `th_almost_idemp`

### Attacks run

1. **One-rectangle estimate.** Put \(T=\Phi\) and \(D=T^2-T\), so
   \(\|T\|\le1\) and \(\|D\|\le\eta\) at every amplification. The positive
   square at `tex:2378-2380` is
   \[
   S_X^\dagger S_X
   =T^2(T(X^\dagger)T(X))
    -T(T^2(X^\dagger)T^2(X)).
   \]
   Inserting \(T(T(X^\dagger)T(X))\) costs \(\eta\|X\|^2\), while replacing
   both \(T^2(X^\dagger),T^2(X)\) costs \(2\eta\|X\|^2\). Thus
   \[
   \|S_X\|\le\sqrt{3\eta}\|X\|.
   \]
   This independently confirms a block the target marked VALID.

2. **Two-rectangle and finite-dimensional reduction.** The middle of the
   two-rectangle diagram is a contraction of norm at most \(\|Y\|\), so the
   two one-rectangle bounds give \(3\eta\|X\|\|Y\|\|Z\|\).
   I re-expanded the four algebraic terms at `tex:2574-2577`; the signs and
   nesting agree with the target's formula. Replacing the first outer \(T^2\)
   costs \(\eta\), pairing the second and fourth terms costs \(3\eta\), and
   reducing the third costs \(3\eta\), for a \(7\eta\) remainder. The final
   associativity constant is therefore \(3+7=10\).

3. **General Stinespring reduction.** The target's type correction at
   `tex:2665` is forced: the final factor must be \(V_{1+k}\), not \(V_1\).
   With that correction, `uVdV-multi` gives the next line. The \(Q\) expansion
   at `tex:2697-2719` has a \(3\eta\) paired-term cost and a \(2\eta\)
   replacement cost. Applying the outer \(T\) and restoring the two target
   terms costs another \(2\eta\), again producing \(7+3=10\).

4. **Second associativity identity.** Applying the first identity to
   \((Z^\dagger,Y^\dagger,X^\dagger)\), taking adjoints, and using exact
   involution preservation gives the second identity with the same constant.
   No second diagram argument is needed.

5. **Dimension-freedom.** The estimates use isometries, orthogonal
   projections, contractive \(*\)-homomorphisms, UCP contractions, and a fixed
   number of triangle inequalities. There is no trace, basis sum, Kraus count,
   block sum, or amplification-dependent normalization. Applying the proof to
   \(1_{M_n}\otimes\Phi\) leaves all constants unchanged.

6. **Functional calculus.** In the Banach algebra of completely bounded maps,
   \[
   (2\Phi-I)^2=I-4(\Phi-\Phi^2).
   \]
   For \(\eta<1/4\), the inverse-square-root series converges in cb norm.
   Because all factors are functions of \(\Phi\), they commute, and the sign
   has square \(I\); hence \(\widetilde\Phi\) is exactly idempotent. The target's
   dimension-free bound
   \[
   r(\eta)=\frac32\bigl((1-4\eta)^{-1/2}-1\bigr)
   \]
   is a valid upper bound for
   \(\|\widetilde\Phi-\Phi\|_{\rm cb}\).

7. **Small counterexamples.** The qubit dephasing multiplier confirms that the
   one-rectangle square constant cannot be \(1\): its ratio tends to \(2\).
   The same example and the \(\mathbb C\oplus\mathbb C\) example give
   associativity-defect ratio tending to \(1\), but neither threatens the
   constant \(10\). Amplification leaves those ratios unchanged.

### What survived

The diagrammatic \(10\eta\) result survives, as do the target's four
operator-domain corrections, the \(V_{1+k}\) correction, and its interface
formula (E9). In particular, the target's charge \(2(M^5-1)\) is valid:
before replacing \(\Phi\) by \(\widetilde\Phi\), subtract the two original
associativity identities. Their common right-hand side cancels, so only the
two nested left-hand expressions need to be replaced. Each replacement costs
at most \(M^5-1\).

### Corrected statements

The source's local type/index corrections are:
\[
X\in\mathcal B(\mathcal H_n)\quad\text{at `tex:2603` and `tex:2620`},
\]
\[
Y\in\mathcal B(\mathcal H_{n-1})\quad\text{at `tex:2608`},\qquad
Y\in\mathcal B(\mathcal H_m)\quad\text{at `tex:2624`},
\]
and the middle line at `tex:2665` must read
\[
V_{1+k}^\dagger
u_{1+k,0}(V_1^\dagger ZV_1)V_{1+k}.
\]

**Transcribable corrected statement D.** Let \(\mathcal H\ne0\), let
\(\Phi:\mathcal B(\mathcal H)\to\mathcal B(\mathcal H)\) be UCP, and suppose
\[
\|\Phi^2-\Phi\|_{\rm cb}\le\eta<\frac14.
\]
Define
\[
\widetilde\Phi
=\frac12\left(I+(2\Phi-I)
  (I-4(\Phi-\Phi^2))^{-1/2}\right),
\qquad
\mathcal A=\operatorname{Im}\widetilde\Phi,
\]
and \(X\star Y=\widetilde\Phi(XY)\). Then \(\widetilde\Phi^2=\widetilde\Phi\),
and at every amplification the two identities `Phi_assoc1` and
`Phi_assoc2` have error at most
\[
10\eta\,\|X\|\,\|Y\|\,\|Z\|.
\]
Let
\[
r=\frac32\left((1-4\eta)^{-1/2}-1\right),\qquad M=1+r.
\]
For sufficiently small universal \(\eta\), \(\mathcal A\), with its inherited
operator-space norms, involution, and unit, is an extended
\(\varepsilon_{\rm AI}(\eta)\)-\(C^*\)-algebra for
\[
\boxed{
\varepsilon_{\rm AI}(\eta)
=\max\left\{
r,\;
20\eta+2(M^5-1),\;
3r-r^2
\right\}.}
\]
In particular, \(\varepsilon_{\rm AI}(\eta)=O(\eta)\) with a universal,
dimension-free coefficient.

## Cross-target checks

### Constants and thresholds

The four targets use compatible local constants once their roles are kept
distinct:

- \(\varepsilon_{\rm AI}\) is the approximate-algebra error produced by D;
- \(K\) is a common factorization constant that exists only after C's H-CB
  and EXT-CB gaps are closed and B's repaired CP construction is inserted;
- \(\varepsilon_{\rm PRH}=\|MA-I_k\|_{\infty\to\infty}\) is A's local defect
  and is not the same symbol as \(\varepsilon_{\rm AI}\).

Conditional on a universal factorization constant \(K\), the already-audited
compression calculation gives
\[
\varepsilon_{\rm PRH}
\le\frac{3K\eta}{1-3K\eta}.
\]
Taking, for example,
\[
\eta_0\le\min\{\eta_K,(24K)^{-1},1\}
\]
gives \(\varepsilon_{\rm PRH}\le4K\eta<1/2\), so A applies. The final
conditional estimate is
\[
\|Q-E\|_{\infty\to\infty}
\le K\eta+4\sqrt{2K\eta}
\le\bigl(K+4\sqrt{2K}\bigr)\sqrt\eta.
\]
There is no incompatible meaning of \(K\) or smallness threshold in the
batch. What is missing is an unconditional \(K,\eta_K\), not consistency.

### Circularity

No proof loop was found.

- A is standalone.
- B proves an exact-algebra diagonal lemma and a conditional CP-ization
  lemma from stated map estimates; it does not invoke `th_factorization`.
- C's structure-theorem decomposition is upstream of factorization and uses
  the independently available whole-algebra Haar diagonal, not B's conclusion
  as an unproved premise.
- D proves the approximate-algebra input independently of C.

In particular, none of A-D assumes `th_factorization` in order to prove an
ingredient of `th_factorization`.

## Residual register for Route F

This batch does **not** support the claim that residual items 1-6 are all
discharged.

What survived:

1. PRH is a complete dimension-free paper proof with constant \(2\sqrt2\),
   and its \(\sqrt\varepsilon\) exponent is sharp up to constants.
2. The printed direct-sum diagonal flaw has an exact finite norm-one repair at
   every use site.
3. No cone-projection shortcut is needed.
4. The diagrammatic core of `th_almost_idemp` has a dimension-free explicit
   \(10\eta\) bound after the stated type/index corrections; its extended
   interface survives with the explicit \(\varepsilon_{\rm AI}\) above.
5. `th_main_ext` has been reduced to two named amplified gaps rather than
   accepted from the source's outline.

What remains open:

1. **H-CB:** prove or refute the complete column-Hilbert/module estimates with
   constants uniform in the amplification level.
2. **EXT-CB:** assuming H-CB, prove the amplified extension lemma using one
   level-one unitary and completely controlled four-corner maps.
3. **Final universal ledger:** after those proofs, instantiate one common
   \(K<\infty\) and \(\eta_K>0\), and check that every raw pre-improvement step
   stays below the same universal reset threshold.
4. **Literal-source and rigour closure:** the false direct-sum formulas, the
   squared-norm typo, the Stinespring type/index errors, and the remaining
   outline prose must not be imported verbatim. The surviving original
   arguments still require the repository's codification/formalization and
   provenance gates before any claim is promoted beyond
   `proved-mod-audit`.

Therefore Route F remains a conditional reduction. The principal next attack
is H-CB; a counterexample there would challenge the claimed uniformity of
`th_main_ext`, while a proof would leave EXT-CB as the final mathematical
structure-theorem gap.
