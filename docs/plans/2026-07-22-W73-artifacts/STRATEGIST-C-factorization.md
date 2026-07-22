# A direct commutative factorization proof: Kitaev followed by positive-retract hardening

## Verdict

The most promising program is (2), but with one important correction and one elementary addition. The correction is that `ran(Q)` is generally the wrong approximate algebra; one must use Kitaev's spectral near-\(1\) range, or equivalently invoke his positive approximate factorization theorem. The addition is a commutative **positive-retract hardening lemma**:

> If positive unital maps
> \[
> A:\ell_\infty^k\longrightarrow \ell_\infty^n,
> \qquad M:\ell_\infty^n\longrightarrow \ell_\infty^k
> \]
> satisfy \(\|MA-I_k\|\leq\varepsilon<1/2\), then there is a stochastic idempotent \(E\) with
> \[
> \|AM-E\|_{\infty\to\infty}\leq 2\sqrt{2\varepsilon}.
> \]

The proof is a simultaneous threshold-and-conditioning construction. It neither discovers nor counts recurrent classes geometrically. Kitaev supplies the soft class coordinates; the lemma turns them into disjoint recurrent cores and leaves all other states as transients. The square root occurs exactly in optimizing
\[
\frac{\varepsilon}{\lambda}+2\lambda.
\]

Subject to a line-by-line import audit of Kitaev's Theorem 12.3, this gives a complete direct skeleton for op-classical, with no exposed hulls, hidden vertices, charts, or signed affine geometry. In the rigour vocabulary of the brief, I regard it as a strategy/sketch until that audit is done.

Throughout, \(\|\cdot\|\) means the \(\infty\to\infty\) norm for classical maps and the cb norm for matrix-algebra maps. A universal constant \(K\geq1\) is fixed so that the two estimates in Kitaev's Theorem 12.3 used below hold with constant \(K\), whenever the defect is at most his universal threshold \(\eta_{\mathrm K}\).

## The four programs and their exact hard cores

### 1. Multi-block depolarizing blend

Suppose a partition into recurrent cores were already known, together with one tentative probability \(\mu_s\) for each core. Then SBD can be applied within each core: mixing with a rank-one collapse gives contraction at rate \(1-\lambda\), and the displacement of a fixed distribution is bounded by “defect divided by \(\lambda\).” Taking \(\lambda\asymp\sqrt\eta\) gives the correct rate. There is no loss proportional to the number of blocks if the final row is estimated as a convex combination of repaired block distributions.

The difficulty is earlier. A proposed class-collapse \(H\) cannot be selected canonically from \(Q\) without already knowing which almost-invariant observables are class coordinates. Moreover,
\[
M_\lambda=(1-\lambda)Q+\lambda H
\]
is stochastic and close to \(Q\), but is not idempotent. Passing to its power limit can collapse slow modes that should instead be rounded to eigenvalue \(1\). Thus the blend does not itself create the multi-block idempotent.

There is also a basic defect in taking `ran(Q)` literally. If \(H\) is a nontrivial stochastic idempotent and
\[
Q=H+\alpha(I-H),\qquad 0<\alpha\ll1,
\]
then \(Q\) is invertible because \(H\) has only eigenvalues \(0,1\), so \(\operatorname{ran}Q=\ell_\infty^n\), although the near-zero directions are not almost fixed relative to their own norm. The estimate
\(\|Q(Qf)-Qf\|\leq\eta\|f\|\) contains the norm of a preimage, which can be \(\alpha^{-1}\|Qf\|\).

The contraction calculation also reveals why doing the blocks one at a time is dangerous. If the tentative block \(s\) leaks into a collection of other blocks, repairing each pair separately naturally produces a sum over those recipients. That is the anti-splitting wall in analytic dress. A valid multi-block blend must express every repaired row as one convex average and take a supremum over \(s\), never a sum of pairwise leakage estimates. Moreover, two tentative class collapses can be equally close to \(Q\) while inducing different assignments of borderline states; uniqueness is neither available nor needed. What is needed is an approximate retract whose internal coordinates are already positive.

**Exact hard core:** construct, without a prior partition, a positive soft retraction \(A,M\) with \(AM\approx Q\) and \(MA\approx I\). Once that exists, neither SBD nor a power limit is needed: the hardening lemma below produces the exact idempotent directly. Transient rows and non-uniqueness of the partition are not the obstruction; transient rows can retain their soft class weights.

### 2. Commutative Kitaev

Kitaev correctly uses the exact spectral idempotent \(\widetilde Q=\theta(2Q-I)\), not `ran(Q)`, and puts the Choi--Effros product
\(f\star g=\widetilde Q(fg)\) on \(\operatorname{ran}\widetilde Q\). His dimension-free rigidity theorem turns this approximate \(C^*\)-algebra into a genuine finite-dimensional \(C^*\)-algebra. More useful here is his Theorem 12.3: an almost-idempotent UCP map approximately factors as \(\Delta\Upsilon\), where \(\Delta,\Upsilon\) are UCP and \(\Upsilon\Delta\) is approximately the identity, with error \(O(\eta)\).

In the commutative case the target algebra must itself be commutative. I give a quantitative proof below: \(\Delta(B)\) lies within \(2K\eta\) of diagonal matrices, so its commutators are at most \(8K\eta\); Kitaev's approximate multiplicativity then makes every commutator in \(B\) at most \(10K\eta\). A noncommutative finite-dimensional \(C^*\)-algebra contains two contractions whose commutator has norm \(2\), a contradiction for small \(\eta\).

After diagonal compression, Kitaev's maps become stochastic maps \(A,M\). A small point requiring proof is that diagonal compression might appear to destroy \(MA\approx I\). Approximate invariance of \(\Delta(B)\) makes \(A\) a near-isometry, and this recovers the inverse estimate:
\[
\|MA-I\|\leq \frac{3K\eta}{1-3K\eta}.
\]
This is the transfer step that makes the program close.

This is stronger information than an abstract algebra isomorphism. An isomorphism for the Choi--Effros product need not by itself send coordinate projections to pointwise Boolean functions: \(p\star p=p\) says \(\widetilde Q(p^2)=p\), not \(p^2=p\) in the ambient pointwise product. The positive maps \(\Delta,\Upsilon\), by contrast, encode each algebra atom as a positive partition-of-unity coordinate and each decoder row as a genuine probability measure. Their approximate inverse relation is an averaged near-Boolean statement with the correct sign. That is precisely what the threshold argument consumes.

**Exact hard core:** the original Kitaev machinery stops at a positive approximate factorization. Commutatively, the remaining positivity repair is precisely the hardening lemma. It costs \(O(\sqrt\eta)\), not \(O(\eta)\), because an average overlap of size \(\eta\) must be converted into exactly disjoint supports.

### 3. Cesaro and power limits

For every \(m\geq1\), positivity gives the useful dimension-free estimate
\[
Q^m-Q=\sum_{r=0}^{m-2}Q^r(Q^2-Q),
\qquad
\|Q^m-Q\|\leq(m-1)\eta.                                      \tag{3.1}
\]
Thus \(m\asymp\eta^{-1/2}\) keeps \(Q^m\) within \(O(\sqrt\eta)\) of \(Q\). Spectrally, every \(z\in\sigma(Q)\) satisfies \(|z(z-1)|\leq\eta\), so the spectrum lies close to \(0\) or \(1\). Nontrivial peripheral cycles are excluded for small defect, and power boundedness suppresses Jordan growth on the unit circle. None of these is the decisive issue.

The obstruction is a slow mode near \(1\). Let
\[
H=\begin{pmatrix}1&0\\1&0\end{pmatrix},\qquad
Q_a=(1-a)I+aH=H+(1-a)(I-H).
\]
Then
\[
\|Q_a^2-Q_a\|=2a(1-a),\qquad \|Q_a-I\|=2a,
\]
so the correct nearby idempotent is \(I\). But the power and Cesaro limits are \(H\), and
\(\|Q_a-H\|=2(1-a)\). At the finite time \(m\asymp a^{-1/2}\), \(Q_a^m\) is \(O(\sqrt a)\)-close to \(I\), but is not exact. The asymptotic limit makes the wrong binary decision about the slow mode.

Functional calculus makes the correct binary decision and produces an exact idempotent \(P=\theta(2Q-I)\) with \(\|P-Q\|=O(\eta)\), but \(P\) can have negative entries. Hence the power question reduces exactly to the old positivity-repair question. Working in the signed picture makes this even clearer: \(P^m=P\) and every Cesaro average equals \(P\), so exactness freezes, rather than cures, the negative mass. Row-normalizing \(P\) reintroduces an almost-idempotent stochastic map whose infinite-time limit can again choose the wrong slow modes.

One might try a regularized limit that stops at time \(\eta^{-1/2}\) and then Cesaro-averages only a short window. Equation (3.1) keeps every member of that window close to \(Q\), but the average remains merely almost idempotent. Conversely, averaging to a time long enough to force exact stationarity necessarily sees the slow mode and sends it to \(0\). There is no time scale that simultaneously supplies exactness and makes the correct \(0/1\) decision. A non-normal resolvent estimate can affect constants in locating the spectral subspaces, but it cannot fix this logical conflict.

**Exact hard core:** a positive finite-time rounding rule that distinguishes “slow transient” from “true recurrent” modes without using a signed spectral projection. That is equivalent in difficulty to constructing the stochastic idempotent. Spectral clustering, Jordan estimates, and peripheral rotation are secondary, not terminal, obstructions.

### 4. Sup-norm Cheeger extraction

For \(0\leq f\leq1\), set \(A_t=\{j:f_j>t\}\). There is an exact rowwise co-area identity
\[
\int_0^1\big|Q1_{A_t}(i)-1_{A_t}(i)\big|\,dt
=\sum_j q_{ij}|f_j-f_i|.                                      \tag{4.1}
\]
The defect \(|Qf(i)-f_i|\) controls only
\(\big|\sum_jq_{ij}(f_j-f_i)\big|\); positive and negative increments can cancel. Therefore no sup-norm Cheeger conclusion follows from almost harmonicity alone.

This failure already occurs for an exact stochastic idempotent:
\[
E=\begin{pmatrix}1&0&0\\0&1&0\\1/2&1/2&0\end{pmatrix},
\qquad f=(0,1,1/2)^T,qquad Ef=f.
\]
For every nontrivial threshold \(t\neq1/2\), the transient third row has boundary error \(1/2\). This is not pathology: exact idempotents require transient rows to be soft convex combinations of recurrent classes. A global hard set should not be expected to be invariant on transient rows.

At extreme values cancellation disappears. If a positive class coordinate \(a_s\) satisfies an averaged impurity estimate
\(\int(1-a_s)\,d\mu_s\leq\varepsilon/2\), then the near-one level set
\(C_s=\{a_s>1-\lambda\}\) obeys
\(\mu_s(C_s^c)\leq\varepsilon/(2\lambda)\). A family of coordinates summing to one makes the \(C_s\)'s disjoint when \(\lambda<1/2\). This is exactly the one-sided, primal Cheeger statement that is valid. Kitaev supplies the needed positive class coordinates; arbitrary harmonic functions do not.

The signed harmonic deficit \(g=Pg\) does not repair (4.1), because signed coefficients destroy the Markov/co-area interpretation. Passing to the row-normalized stochastic map gives only approximate harmonicity and retains the cancellation caused by transients.

The example also identifies the right output of a Cheeger theorem. It cannot be a partition of all states into almost-invariant sets. It should be a collection of disjoint recurrent **cores**, together with soft membership functions on the complement. On core rows the level-set indicators are stable; on the complement the soft functions, rather than their indicators, are the correct data. This is exactly the recurrent/transient normal form of a stochastic idempotent.

**Exact hard core:** first construct a positive partition of unity of near-Boolean class coordinates, with a corresponding family of measures that sees only \(O(\eta)\) average impurity. Level-set extraction can then finish, but cannot create those coordinates by itself.

## Winner: root-to-leaves proof skeleton

### Root 0: lift the classical map to a quantum channel

**[KNOWN-ROUTINE]** Let \(J:\ell_\infty^n\to M_n\) be diagonal inclusion and \(\mathcal D:M_n\to\ell_\infty^n\) the diagonal conditional expectation. Define
\[
\Phi=JQ\mathcal D:M_n\to M_n.
\]
It is UCP, and \(\Phi^2-\Phi=J(Q^2-Q)\mathcal D\). At every matrix amplification, a scalar matrix \(L=(l_{ij})\) acting between direct sums of matrix algebras has norm at most \(\max_i\sum_j|l_{ij}|\); equality is obtained by taking scalar multiples of the identity with the maximizing signs. Consequently
\[
\|\Phi^2-\Phi\|_{cb}=\|Q^2-Q\|_{\infty\to\infty}\leq\eta.     \tag{5.1}
\]

### Root 1: invoke Kitaev's positive approximate factorization

**[KNOWN-LIT-KITAEV]** There are a finite-dimensional \(C^*\)-algebra \(B\) and UCP maps
\[
\Delta:B\to M_n,\qquad \Upsilon:M_n\to B
\]
such that
\[
\|\Delta\Upsilon-\Phi\|_{cb}\leq K\eta,                       \tag{5.2}
\]
and, for \(x,y\in B\),
\[
\|\Upsilon(\Delta(x)\Delta(y))-xy\|
\leq K\eta\|x\|\|y\|.                                      \tag{5.3}
\]
Taking \(y=1_B\) gives
\[
\|\Upsilon\Delta-I_B\|\leq K\eta.                           \tag{5.4}
\]

**[RISK]** This is the sole large imported engine. The published theorem states universal \(O(\eta)\) constants rather than the letter \(K\); the first audit must extract one common \(K\), verify the common smallness threshold, and confirm the row-stochastic/cb norm convention. No dimension-dependent estimate is permissible here.

### Root 2: force the factor algebra to be commutative

**[NEW-ROUTINE]** From (5.2) and (5.4),
\[
\|\Phi\Delta-\Delta\|
\leq\|(\Phi-\Delta\Upsilon)\Delta\|
   +\|\Delta(\Upsilon\Delta-I_B)\|
\leq2K\eta.                                                    \tag{5.5}
\]
The range of \(\Phi\) is diagonal. For contractions \(x,y\in B\), replace \(\Delta x,\Delta y\) by the commuting diagonal matrices \(\Phi\Delta x,\Phi\Delta y\). Equation (5.5) gives
\[
\|[\Delta x,\Delta y]\|\leq8K\eta.
\]
Applying (5.3) in both orders yields
\[
\|[x,y]\|\leq10K\eta.                                       \tag{5.6}
\]
If \(B\) had a matrix summand of size at least two, two contractions supported in that summand could be chosen with commutator norm \(2\). Thus \(B\) is commutative whenever \(10K\eta<2\), and hence
\[
B\cong\ell_\infty^k                                             \tag{5.7}
\]
for some \(k\), with no bound on \(k\) required.

### Root 3: obtain a classical positive approximate retract

**[NEW-ROUTINE]** Define
\[
A=\mathcal D\Delta:\ell_\infty^k\to\ell_\infty^n,
\qquad M=\Upsilon J:\ell_\infty^n\to\ell_\infty^k,
\qquad F=AM.
\]
These maps are positive and unital, hence represented by row-stochastic matrices. Diagonal compression of (5.2) gives
\[
\|F-Q\|\leq K\eta.                                            \tag{5.8}
\]
Also, (5.5) implies
\[
\|QA-A\|=\|\mathcal D(\Phi\Delta-\Delta)\|\leq2K\eta.       \tag{5.9}
\]

The compression \(A=\mathcal D\Delta\) remains a near-isometry. Indeed, (5.4) gives
\(\|\Delta x\|\geq(1-K\eta)\|x\|\), while (5.5) and
\(\Phi\Delta x=JQA x\) give
\(\|\Delta x\|\leq\|Ax\|+2K\eta\|x\|\). Therefore
\[
\|Ax\|\geq(1-3K\eta)\|x\|.                                  \tag{5.10}
\]
Now
\[
\begin{aligned}
\|A(MA-I)x\|
 &=\|FAx-Ax\|\\
 &\leq\|(F-Q)Ax\|+\|(QA-A)x\|\\
 &\leq3K\eta\|x\|.
\end{aligned}
\]
Using (5.10) on \((MA-I)x\) yields the crucial estimate
\[
\|MA-I_k\|\leq
\varepsilon:=\frac{3K\eta}{1-3K\eta}.                         \tag{5.11}
\]

**[RISK]** The direction of (5.10) is load-bearing: one needs a lower bound for \(A\), not merely contractivity. Equations (5.4) and (5.5) supply exactly that direction.

### Root 4: positive-retract hardening

**[NEW-ROUTINE; central new lemma]** Write
\[
(Ax)_i=\sum_{s=1}^k a_{is}x_s,
\qquad
(Mf)_s=\sum_{i=1}^n\mu_s(i)f_i,
\]
where every \(a_i=(a_{i1},\ldots,a_{ik})\) and every \(\mu_s\) is a probability vector. Let \(R=MA\). From \(\|R-I_k\|\leq\varepsilon\), its \(s\)-th row satisfies
\[
2(1-R_{ss})\leq\varepsilon,
\quad\text{hence}\quad
\sum_i\mu_s(i)(1-a_{is})\leq\varepsilon/2.                   \tag{5.12}
\]
Choose
\[
\lambda=\sqrt{\varepsilon/2},
\qquad C_s=\{i:a_{is}>1-\lambda\}.                            \tag{5.13}
\]
If \(\lambda<1/2\), the sets \(C_s\) are pairwise disjoint because the coordinates of \(a_i\) sum to one. Markov's inequality, used only in its valid direction, gives
\[
\beta_s:=\mu_s(C_s^c)\leq\frac{\varepsilon}{2\lambda}=\lambda. \tag{5.14}
\]
Thus \(C_s\neq\varnothing\). Let \(\nu_s\) be \(\mu_s\) conditioned on \(C_s\). Then
\[
\|\mu_s-\nu_s\|_1=2\beta_s\leq2\lambda.                     \tag{5.15}
\]

Let \(N:\ell_\infty^n\to\ell_\infty^k\) have rows \(\nu_s\), and define a new membership map \(\widehat A:\ell_\infty^k\to\ell_\infty^n\) by
\[
\widehat a_i=
\begin{cases}
e_s,&i\in C_s,\\
a_i,&i\notin\bigcup_sC_s.
\end{cases}                                                    \tag{5.16}
\]
Because the cores are disjoint and \(\nu_s\) is supported on \(C_s\),
\[
N\widehat A=I_k.                                               \tag{5.17}
\]
Set
\[
E=\widehat A N.                                                \tag{5.18}
\]
Then \(E\) is positive, unital, and
\(E^2=\widehat A(N\widehat A)N=E\): it is a stochastic idempotent. The actual recurrent class is \(S_s=\operatorname{supp}\nu_s\subseteq C_s\), and every row indexed by \(C_s\) equals \(\nu_s\). Points of \(C_s\setminus S_s\), if any, simply feed into \(S_s\). Every state outside the cores is a transient row with the original soft weights \(a_i\).

Finally, (5.15) and convexity give \(\|AM-AN\|\leq2\lambda\). For \(i\in C_s\),
\[
\left\|\sum_ta_{it}\nu_t-\nu_s\right\|_1
\leq2(1-a_{is})<2\lambda,
\]
and outside the cores \(A=\widehat A\). Hence
\[
\|AM-E\|\leq4\lambda=2\sqrt{2\varepsilon}.                  \tag{5.19}
\]

The construction is worth reading in the normal form of an exact stochastic idempotent. The rows \(\nu_s\) are the recurrent distributions, and their supports \(S_s\) are disjoint. If \(i\in C_s\), then the \(i\)-th row of \(E\) is exactly \(\nu_s\). If \(i\) lies outside every core, its row is \(\sum_s a_{is}\nu_s\), an arbitrary convex combination of recurrent distributions. Thus hardening changes only the data that exact idempotence forces us to change: it makes memberships pure on the supports of recurrent measures and preserves the legitimate softness of transient rows.

This also explains why no accumulation over \(k\) occurs. Conditioning is estimated uniformly in \(s\); changing a transient row is estimated after weighting by the probability vector \(a_i\). The identity \(N\widehat A=I_k\), rather than pairwise separation estimates, synchronizes all blocks at once. In SBD language, conditioning is the fixed-state repair and membership hardening is the multi-block collapse, but both occur in one global simplex coordinate system supplied by Kitaev.

### Root 5: constants and conclusion

**[NEW-ROUTINE]** Put
\[
\eta_0=\min\left\{\eta_{\mathrm K},\,1,\,(24K)^{-1}\right\}.
\]
For \(\eta\leq\eta_0\), (5.6) forces commutativity, and
\(\varepsilon\leq4K\eta<1/2\), so the hardening construction applies. From (5.8) and (5.19),
\[
\|Q-E\|
\leq K\eta+2\sqrt{2\varepsilon}
\leq K\eta+4\sqrt{2K\eta}
\leq \bigl(K+4\sqrt{2K}\bigr)\sqrt\eta.                     \tag{5.20}
\]
Thus the candidate universal constant is
\[
C=K+4\sqrt{2K}.
\]
It is explicit in the universal constant extracted from Kitaev's theorem and is independent of \(n\), \(k\), ranks, class sizes, and conditioning parameters.

No iteration is hidden in this conclusion. Kitaev is invoked once, diagonal compression is performed once, and all \(k\) cores are thresholded at the same \(\lambda\). In particular, there is no induction on the number of atoms of \(B\), no degradation of \(\eta_0\) as atoms are peeled off, and no conditioning number attached to the distributions \(\nu_s\). Those are precisely the places where standard aggregation and stochastic-complementation arguments lose dimension-free control.

## Audit against the six load-bearing walls

1. **Cloning obstruction.** All input estimates are operator-norm statements and all intermediate quantities are positive maps, probability measures, and suprema over rows. Cloning a coordinate merely splits the corresponding \(\mu_s\)-mass; (5.12)--(5.19) are unchanged. No raw-index lower bound appears.

2. **Class-count/anti-splitting.** Although there are \(k\) cores, no error is summed over \(s\). The bound \(\|AM-AN\|\leq\sum_sa_{is}\sup_s\|\mu_s-\nu_s\|_1\) uses \(\sum_sa_{is}=1\). Thus \(k\) can be arbitrary.

3. **Exposedness absorption/halo.** The proof uses no affine capacity or transported raw mass. Disjointness is the elementary simplex fact that two coordinates of one probability vector cannot both exceed \(1-\lambda>1/2\). This route bypasses, rather than reformulates, the halo wall.

4. **Dual-direction wall.** Equations (5.13)--(5.18) construct the sets, repaired measures, and final idempotent explicitly. This is a primal extraction. Markov's inequality turns the upper impurity ledger into an upper discarded-mass bound; no dual hiddenness certificate is reversed.

5. **Whole-optimal-face tightness.** There is no optimization face, exposer, or near-optimal dual value. Exactness comes from the algebraic identity \(N\widehat A=I_k\).

6. **One-sided ledger.** The directions are visible: (5.11) upper-bounds average impurity; (5.14) upper-bounds mass outside a high-coordinate core; conditioning changes \(\mu_s\) by twice that mass. The only lower estimate, (5.10), is separately proved from Kitaev's approximate left inverse and approximate diagonal invariance. No financing inequality is used backward.

## Sharp example and the unavoidable square root

The route is linear until (5.13). The exact-support requirement asks us to turn
\[
\mathbb E_{\mu_s}(1-a_s)\leq\varepsilon/2
\]
into a set on which \(a_s\) is exactly replaced by \(1\) and outside of which \(\mu_s\) is exactly removed. At threshold gap \(\lambda\), hardening the memberships costs at most \(2\lambda\), while conditioning the measures costs at most \(\varepsilon/\lambda\). Their optimum is \(\lambda=\sqrt{\varepsilon/2}\). A two-scale configuration with \(\mu_s\)-mass of order \(\sqrt\varepsilon\) on points having membership deficit of order \(\sqrt\varepsilon\) saturates the product ledger, so neither term can generally be made \(o(\sqrt\varepsilon)\).

For the signed sharp family ex-hume, \(\delta=s^2\) and every stochastic idempotent is at distance \(2s+O(s^2)\). The signed--stochastic equivalence produces almost-idempotent stochastic maps with defect \(\eta=\Theta(s^2)\) and distance \(\Omega(s)\). All stages before hardening have error \(O(\eta)\); therefore this construction necessarily spends its \(\Theta(s)=\Theta(\sqrt\eta)\) budget at the threshold/conditioning step. This is consistent with, and structurally explains, the sharp example. Powers do not evade it: finite powers remain positive but inexact, while infinite powers can select the wrong slow-mode idempotent.

## Decisive first test

The first test should be a hostile, line-by-line audit of Roots 1--3 against the exact statement of Kitaev's Theorem 12.3, not another geometric search. Extract a single numerical \(K\) and verify only these three implications:
\[
\Upsilon\Delta\approx I_B,
\qquad
\Phi\Delta\approx\Delta,
\qquad
\|\mathcal D\Delta x\|\geq(1-3K\eta)\|x\|.
\]
Then verify the commutator gap (5.6). If all four inequalities survive with universal constants, the remainder is the elementary hardening proof (5.12)--(5.19), and op-classical follows. If the route fails, it must fail at a sharply identifiable point: either Theorem 12.3 does not apply to the diagonal entanglement-breaking lift with the claimed cb defect, its approximate multiplicativity does not imply (5.4), or diagonal compression lacks the lower estimate (5.10). The displayed derivation rules out the last two on their face, so checking the theorem's precise hypotheses and constants is genuinely decisive.
