# Three new top-down architectures for op-classical

## 0. Common target and conventions

Write \(\|A\|=\|A\|_{\infty\to\infty}=\max_i\sum_j|A_{ij}|\).  The root problem is

\[
 \tag{OC}
 \exists \eta _0,C>0\ \forall n\ \forall Q\in M_n([0,1]):
 Q\mathbf1=\mathbf1,\quad \|Q^2-Q\|\leq\eta\leq\eta _0
 \Longrightarrow
 \exists E\geq0, E\mathbf1=\mathbf1, E^2=E,
 \ \|Q-E\|\leq C\sqrt\eta .
\]

This target is **[NEW-HARD]** (the registered open problem).  I use \(\delta=\delta(P)\), \(\tau=\sqrt\delta\), \(\rho=4\tau\), \(\kappa=\tau/4\) in the signed picture.  In direct stochastic arguments I write \(\tau_Q=\sqrt\eta\).  The bridge `lem-classical-equiv` is **[KNOWN-T0]**: it converts (OC), up to universal constants, into positivity repair of an exact signed idempotent \(P\), and conversely.  The inherited implication

\[
 H(P)\le C_H\sqrt{\delta(P)}\quad\Longrightarrow\quad\text{(OC)}
\]

through `lem-hlc-implies-exposed-hull`, `thm-classical-factorization`, and `prop-approx-simplex` is **[KNOWN-L5]/[KNOWN-mod-audit]**.  I do not use any conclusion from the conditional MIN-A/POTI tree.

The architectures are deliberately different:

1. correct an approximate stochastic factorization through a commutative algebra;
2. prove a clone-quotient capacitary maximum principle for the harmonic deficit;
3. discover recurrent cores from a finite-horizon Abel kernel, then assemble the exact idempotent directly.

Only Architecture I looks close to a short proof.  Architectures II and III are research programs with explicit, falsifiable hard cores.

---

## I. Commutative factorization followed by one-shot split rounding

### I.1 Full skeleton

Dependency chain:

\[
 \mathrm{I.1a+I.1b}\Longrightarrow\mathrm{I.1}
 \Longrightarrow\mathrm{I.2}\Longrightarrow\mathrm{I.3}
 \Longrightarrow\mathrm{I.0}.
\]

**Node I.0 (root). [NEW-HARD]**  (OC) holds with

\[
 \eta_0=\min\{\eta_F,(16K_F)^{-1},K_F^{-1}\},
 \qquad C=4\sqrt{K_F},
\]

where \(K_F,\eta_F\) are the universal constants in Node I.1.

**Node I.1 (commutative approximate-retract factorization, CARF). [NEW-HARD]**  There are universal \(K_F\ge1\) and \(\eta_F>0\) such that, for every \(n\) and every stochastic \(Q\) with \(\|Q^2-Q\|\le\eta\le\eta_F\), there are an integer \(1\le k\le n\) and row-stochastic matrices

\[
 D\in M_{n,k}([0,1]),\qquad U\in M_{k,n}([0,1])
\]

such that

\[
 \tag{I.1}
 \|Q-DU\|\le K_F\eta,
 \qquad \|UD-I_k\|\le K_F\eta.
\]

**[RISK: precise hard core]** Kitaev's Theorem 12.3 supplies an \(O(\eta)\) encode/decode factorization through a genuine finite-dimensional C*-algebra, but the repository has not audited that, when the input is \(\ell_\infty^n\), the intermediary may be chosen as \(\ell_\infty^k\) and both maps may be retained as positive unital maps with the two estimates in exactly the orientations in (I.1).  Losing commutativity, positivity, or the second orientation kills this architecture.  CARF is not to be cited as a consequence of the literature until this specialization is written line by line.

CARF decomposes into two more atomic claims.

**Node I.1a (Kitaev approximate factorization). [KNOWN-mod-audit]**  For an \(\eta\)-idempotent UCP map \(\Phi\) there are a genuine finite-dimensional C*-algebra \(B\) and UCP encode/decode maps \(\Delta,\Upsilon\) for which

\[
 \|\Delta\Upsilon-\Phi\|_{cb}\le K_K\eta,
 \qquad \|\Upsilon\Delta-1_B\|_{cb}\le K_K\eta
\]

with a universal \(K_K\).  This is a literature theorem, but its hypotheses, map directions, and numerical constant still require a repository audit; hence the tag is not [KNOWN-T0].

**Node I.1b (commutative inheritance). [NEW-HARD]**  If \(\Phi:\ell_\infty^n\to\ell_\infty^n\) is UCP, then the construction in I.1a can be carried out with \(B\cong\ell_\infty^k\), without increasing \(K_K\) by more than a universal factor.  In particular the Schrödinger-picture maps are stochastic matrices \(D,U\), giving I.1 with a universal \(K_F\).

**[RISK]** The Choi--Effros approximate product \(x\star y=\Phi(xy)\) is commutative on commutative input, which strongly suggests I.1b.  But an abstract stability isomorphism need not preserve that commutativity exactly unless the correction/merging scheme is functorial enough.  An argument merely showing that \(B\) is *close* to commutative is insufficient: the rounding below needs actual atoms \(1,\ldots,k\).

**Node I.2 (positive split-correction lemma). [NEW-ROUTINE]**  Let \(D\in\operatorname{Stoch}(n,k)\), \(U\in\operatorname{Stoch}(k,n)\), and

\[
 0\le\varepsilon\le 1/16,\qquad \|UD-I_k\|\le\varepsilon.
\]

Then there are stochastic \(D'\in\operatorname{Stoch}(n,k)\), \(U'\in\operatorname{Stoch}(k,n)\) such that

\[
 \tag{I.2}
 U'D'=I_k,\qquad
 \|D'-D\|\le2\sqrt\varepsilon,\qquad
 \|U'-U\|\le\sqrt\varepsilon,\qquad
 \|D'U'-DU\|\le3\sqrt\varepsilon.
\]

This node is essentially proved by the following construction.  Put \(t=\sqrt\varepsilon\) and

\[
 G_s=\{i:D_{is}\ge1-t\},\qquad 1\le s\le k.
\]

The \(G_s\) are disjoint because \(t\le1/4<1/2\).  Since a row of \(UD\) is a probability vector,

\[
 \sum_iU_{si}(1-D_{is})=1-(UD)_{ss}\le\varepsilon/2,
 \qquad b_s:=U_s(G_s^c)\le\frac{\varepsilon}{2t}.
\]

Set \(U'_s=U_s1_{G_s}/(1-b_s)\) and set \(D'_i=e_s\) on \(G_s\), leaving \(D'_i=D_i\) off \(\bigcup_sG_s\).  Then \(U'D'=I_k\),

\[
 \|U'_s-U_s\|_1=2b_s\le\varepsilon/t=t,
 \qquad \|D'_i-D_i\|_1\le2t,
\]

and stochastic contractivity gives the last inequality in (I.2).  The case \(\varepsilon=0\) is immediate by taking \(G_s=\{D_{is}=1\}\).

**Node I.3 (exact retract assembly). [NEW-ROUTINE]**  With \(D',U'\) from I.2, define

\[
 E=D'U'.
\]

Then \(E\) is stochastic and

\[
 E^2=D'(U'D')U'=D'U'=E.
\]

If (I.1) holds and \(\varepsilon=K_F\eta\), then

\[
 \tag{I.3}
 \|Q-E\|\le K_F\eta+3\sqrt{K_F\eta}
 \le4\sqrt{K_F}\sqrt\eta
\]

provided \(\eta\le K_F^{-1}\).  This proves Node I.0.

### I.2 Edge mechanisms and the square root

The edge I.1a \(\Rightarrow\) I.1b should use exact commutativity of the approximate product, not a spectral or nearest-algebra argument.  Kitaev's incremental block-merging/diagonal construction should then create only one-dimensional simple summands.  Translating positive unital maps between \(\ell_\infty\)-algebras to the Schrödinger picture gives I.1.

The edge I.1 \(\Rightarrow\) I.2 is a one-sided Markov inequality used in its correct direction: the average impurity of the \(s\)-th code under \(U_s\) is at most \(\varepsilon/2\), so the mass outside the \((1-t)\)-pure set is at most \(\varepsilon/(2t)\).  Forcing membership to be pure costs \(2t\); conditioning the decoding distribution costs \(\varepsilon/t\).  Balancing

\[
 2t+\varepsilon/t
\]

at \(t=\sqrt\varepsilon\) is exactly where the \(1/2\) exponent is born.  No height estimate, class count, or iteration is involved.

### I.3 Audit against the six walls

1. **Cloning.** CARF is stated in operator norm and through stochastic maps.  Splitting a state atom simply splits the corresponding mass in \(U\); the sets \(G_s\) are level sets of the intrinsic membership function \(D_{\bullet s}\), and conditioning uses aggregate mass.  No raw-index lower bound appears.
2. **Anti-splitting.** The error is a maximum over rows.  All \(k\) atoms are rounded simultaneously, and \(\|U'-U\|=\max_s2b_s\); there is no sum over blocks and no bound on \(k\).
3. **Absorption/\(\rho\)-halo.** The proof never assigns capacity to hidden recipients and never uses raw mass near \(C_W\).  Its relevant quantity is code impurity \(1-D_{is}\), invariant under affine reparametrization of the row polytope.  Thus the affine-circuit coefficient-ratio wall is not entered.
4. **Dual direction.** The sets \(G_s\), and hence the exact cores, are constructed primally.  No dual certificate is reversed.
5. **Whole optimal face.** There is no exposedness LP or optimal face.  Exactness is the algebraic identity \(U'D'=I_k\).
6. **One-sided ledger.** Markov's inequality only proves the upper bound \(b_s\le\varepsilon/(2t)\), and that is precisely the direction used to bound the conditioning cost.  No lower finance bound is inferred from it.

### I.4 Decisive first test

Attempt Node I.1b in the smallest nontrivial form: prove that Kitaev's corrected algebra for a commutative approximate product can contain no \(M_2\) summand, with a universal separation constant, and then inspect the merging induction to show it never creates such a summand.  A particularly crisp one-day lemma is:

\[
 \tag{I-test}
 \text{if }B\text{ is finite-dimensional and factors through a commutative C*-algebra by UCP maps }
 \Delta,\Upsilon\text{ with }\|\Upsilon\Delta-1_B\|_{cb}<1/16,
 \text{ then }B\text{ is commutative.}
\]

If (I-test) is false already for \(B=M_2\), the proposed inheritance mechanism is dead.  If true, it supplies the missing rigidity step; I.2 then closes the classical theorem with explicit constants once the literature constant is audited.

---

## II. Clone-quotient potential theory and a primal capacity inequality

This route works entirely with the exact signed idempotent \(P\) and tries to turn the empirical tallness/absorption wall into a maximum principle.  Unlike MIN-A it does not partition near/far freight or charge wedges.

### II.1 Full skeleton

Dependency chain:

\[
 \mathrm{II.1+II.2+II.3+II.4+II.5}
 \Longrightarrow\mathrm{II.0}
 \xRightarrow[\text{inherited HLC spine}]{}\mathrm{(OC)}.
\]

**Node II.0 (signed root). [NEW-HARD]**  For every exact signed idempotent \(P\) with \(P\mathbf1=\mathbf1\) and \(0<\delta(P)\le2^{-16}\), one has \(W(P)\ne\varnothing\) and

\[
 \tag{II.0} H(P)\le64\sqrt{\delta(P)}=64\tau.
\]

By the inherited HLC chain and `lem-classical-equiv`, II.0 implies (OC).  **[KNOWN-L5]/[KNOWN-mod-audit]** for this edge.

**Node II.0e (zero-defect endpoint). [KNOWN-mod-audit]**  If \(\delta(P)=0\), the exact stochastic-idempotent normal form gives \(W(P)\ne\varnothing\) and \(H(P)=0\).  Thus omitting \(\delta=0\) from II.0 loses no endpoint.

**Node II.1 (clone quotient). [KNOWN-mod-audit]**  Let \(\mathcal X\) be the set of distinct row points.  For \(x=[i]\), \(y=[j]\), set

\[
 \bar P_{xy}=\sum_{b\in y}P_{ib}.
\]

Then \(\bar P\mathbf1=\mathbf1\), \(\bar P^2=\bar P\), \(\delta(\bar P)\le\delta(P)\), and every affine row-value function descends to \(\mathcal X\).  This fact is reported upstream but has not been re-established in the registry, so it is not tagged T0.

**Node II.2 (visible-point production). [NEW-HARD]**  Every such \(P\) has a row vertex \(w\) for which

\[
 \operatorname{Cap}_{\bar P}(w)\ge\kappa=\tau/4;
\]

hence \(W(P)\ne\varnothing\).  Here, with

\[
 F_v=\{x\in\mathcal X:\|p_x-p_v\|_1\ge4\tau\},
\]

define the *primal affine capacity*

\[
 \tag{II.1}
 \operatorname{Cap}_{\bar P}(v)=
 \sup\left\{\min_{x\in F_v}a_x:
 \bar Pa=a,\ a_v=0,\ 0\le a_x\le1\ (x\in\mathcal X)\right\},
\]

with the minimum over the empty set equal to \(1\).  Because \(a=\bar Pa\) iff \(a_x\) is the restriction of an affine functional on the row polytope, (II.1) is exactly the *primal* exposer program defining \(t^*(v)\).

**[RISK]** Thin zero faces and the realized \(\alpha\)-gauge blowup may make the best vertex capacity arbitrarily small even at tiny \(\delta\).  No numerical instance does so, but ordinary polytope geometry alone cannot prove II.2; exact idempotence must be used.

**Node II.3 (harmonic top package). [KNOWN-T0]**  Assuming II.2, let \(v\) be a top row vertex with \(d(p_v,C_W)=H>0\).  Then \(v\) is hidden.  There is a 1-Lipschitz affine support functional \(\phi\), with \(\phi(p_v)=H\) and \(\phi\le0\) on \(C_W\), such that

\[
 g_x:=H-\phi(p_x),\qquad 0\le g_x\le\Omega:=2+4\delta,
 \qquad g_v=0,\qquad g_w\ge H\ (w\in W),\qquad \bar Pg=g.
\]

This packages the harmonic-affine bridge and the canonical top-deficit identities.

**Node II.4 (positive shadow chain). [NEW-ROUTINE]**  Put \(\nu_x=\sum_y(\bar P_{xy})^-\) and

\[
 K_{xy}=\frac{(\bar P_{xy})^+}{1+\nu_x}.
\]

Then \(K\) is a stochastic kernel on the clone quotient and

\[
 \tag{II.2}
 |Kg(x)-g(x)|
 =\frac{\left|\sum_y(\bar P_{xy})^-(g_y-g_x)\right|}{1+\nu_x}
 \le\delta\Omega.
\]

Consequently, for the \(K\)-chain \((X_m)\),

\[
 \tag{II.3}
 \big|\mathbb E_xg(X_m)-g_x\big|\le m\delta\Omega.
\]

At the top minimum \(v\), one also has

\[
 \tag{II.4}
 Kg(v)\le\delta\Omega,\qquad K(g^2)(v)\le\delta\Omega^2.
\]

The last inequality follows from \(0\le g\le\Omega\) and harmonicity at \(v\).

**Node II.5 (quotient capacitary maximum principle, QCMP). [NEW-HARD]**  In the setting of II.3--II.4,

\[
 \tag{II.5}
 H^2\le 2^{12}\,\delta\,\operatorname{Cap}_{\bar P}(v).
\]

In particular \(\operatorname{Cap}_{\bar P}(v)\le1\), so \(H\le64\tau\), proving II.0.

**[RISK: precise hard core]** Standard Markov-chain Dirichlet principles often put capacity on the opposite side of an energy inequality.  Here (II.5) is plausible only because \(g=\bar Pg\) and \(\bar P^2=\bar P\) should collapse the Green/occupation operator to one projected step.  If that collapse does not preserve the required inequality in the presence of the signed defect, (II.5) may be false.  This is also where a one-sided energy ledger could silently point the wrong way; the statement must be tested before any proof campaign.

### II.2 Edge mechanisms and the square root

II.1 \(\Rightarrow\) II.4 replaces the signed kernel by its positive shadow without choosing individual representatives.  Equations (II.2)--(II.4) say that the harmonic deficit is a nonnegative \(O(\delta)\)-martingale, globally on quotient classes.

The intended edge II.4 \(\Rightarrow\) II.5 is a Thomson/obstacle argument.  Solve the *primal* program (II.1), use its optimizer as a stopping barrier for \(K\), and apply Cauchy--Schwarz to the aggregate defect flow crossing its level sets.  The hoped-for idempotent cancellation is

\[
 \text{(height)}^2\ \le\
 \text{(signed energy supply }\le 2^{12}\delta)\times
 \text{(primal capacity)}.
\]

The square root is generated exactly by taking the square root of this quadratic energy inequality.  Since capacity is at most one, the conclusion is dimension-free.  For a hidden top one even has \(\operatorname{Cap}(v)=t^*(v)<\tau/4\), which would sharpen (II.5) to \(H<32\delta^{3/4}\); this strengthening is a diagnostic, not needed for (OC).

II.2 is logically separate: a maximum-principle proof must first construct at least one visible boundary point.  One possible primal algorithm is to maximize (II.1) over row vertices, use the corresponding obstacle optimizer, and show that a value below \(\kappa\) at every vertex contradicts \(\bar P^2=\bar P\) after summing the aggregate quotient flux.  That summation must be over a single obstacle solution, not over vertices.

### II.3 Audit against the six walls

1. **Cloning.** Every chain, potential, capacity, and flux lives on \(\mathcal X\), and \(\bar P_{xy}\) is aggregate class mass.  Duplicating an index changes none of them.
2. **Anti-splitting.** QCMP uses one global capacity and one level-set integral.  It never sums separate estimates over quotient classes or wedges.
3. **Absorption/\(\rho\)-halo.** Capacity is not raw received mass: it is the optimum of the affine harmonic program (II.1), hence already encodes all affine-circuit coefficient ratios.  If recipients become exposed, the capacity increases and the boundary \(W\) grows; that helps rather than invalidates the estimate.
4. **Dual direction.** The exposer is the optimizer \(a\) of the primal obstacle problem.  No feasible circuit or hiddenness dual witness is run backward.
5. **Whole optimal face.** Membership in \(W\) is certified by an explicitly constructed primal \(a\), not by promoting a near-tight dual value.  There is no always-tightness claim about an optimal face.
6. **One-sided ledger.** The dangerous point is acknowledged explicitly: II.5 asserts the precise direction \(H^2\le2^{12}\delta\operatorname{Cap}\).  The proposed proof is invalid unless the signed energy identity yields that direction after projection.  No downstream step uses the reverse inequality.

### II.4 Decisive first test

Run an exact-rational LP decider for (II.5) on the existing signed-idempotent bank.  For each exact \(P\): quotient coincident rows; compute \(W\) by the exact primal LP (II.1); compute \(H\) and a top \(v\); and compute

\[
 R(P,v)=\frac{H(P)^2}{\delta(P)\operatorname{Cap}_{\bar P}(v)}.
\]

An instance with \(\operatorname{Cap}(v)=0<H\), or \(R>4096\), kills QCMP exactly.  More informatively, a family with unbounded \(R\) kills every universal constant.  If all 67,000+ records give a modest bounded ratio, especially the thin-zero-face and \(\alpha\)-blowup records, QCMP becomes a credible theorem rather than a relabeling of tallness.  The same run checks II.2 by recording \(\max_v\operatorname{Cap}(v)/\tau\).  This is one LP family, not two independent tests.

---

## III. Finite-horizon Abel cores plus global sup-norm Cheeger extraction

The infinite Cesàro limit is the wrong target: a two-state chain with transition rate \(a+b\ll1\) is \(O(a+b)\)-idempotent but its Cesàro limit collapses the two metastable states, whereas the nearby exact idempotent is the identity.  The repair is to stop at horizon \(1/\sqrt\eta\), before slow blocks merge.

### III.1 Full skeleton

Dependency chain:

\[
 \mathrm{III.1}+\bigl(\mathrm{III.2a+III.2b+III.2c}\bigr)
 \Longrightarrow\mathrm{III.2}
 \Longrightarrow\mathrm{III.3}\Longrightarrow\mathrm{III.0}.
\]

**Node III.0 (root). [NEW-HARD]**  (OC) holds with \(C=25\) and \(\eta_0=2^{-12}\), provided Node III.2 holds with the constants stated below.

**Node III.1 (Abel regularization). [NEW-ROUTINE]**  Let \(0<\eta\le2^{-12}\), \(\alpha=\sqrt\eta\), and

\[
 \tag{III.1}
 R=R_\alpha(Q):=\alpha\sum_{m\ge1}(1-\alpha)^{m-1}Q^m
 =\alpha Q\bigl(I-(1-\alpha)Q\bigr)^{-1}.
\]

Then \(R\) is stochastic, commutes with \(Q\), and

\[
 \tag{III.2}
 \|R-Q\|\le\frac{1-\alpha}{\alpha}\eta\le\sqrt\eta=\alpha,
 \qquad \|RQ-R\|\le\eta.
\]

Indeed \(\|Q^m-Q\|\le(m-1)\eta\), while

\[
 RQ-R=\frac{\alpha}{1-\alpha}(R-Q).
\]

Thus every row \(r_i\) of \(R\) is an \(\eta\)-stationary law for \(Q\), but slow communication has only been observed for geometric mean time \(1/\alpha\).

**Node III.2 (Abel cut-or-coalesce theorem, ACC). [NEW-HARD]**  Let \(Q,R,\alpha\) be as in III.1.  There exist \(k\ge1\), pairwise disjoint nonempty cores \(C_1,\ldots,C_k\subseteq[n]\), and probability laws \(\pi_s\in\Delta(C_s)\) such that

\[
 \tag{III.3}
 \max_{j\in C_s}\|r_j-\pi_s\|_1\le24\alpha\quad(1\le s\le k),
\]

and

\[
 \tag{III.4}
 \max_{i\in[n]}\operatorname{dist}_1
 \bigl(r_i,\operatorname{conv}\{\pi_1,\ldots,\pi_k\}\bigr)
 \le24\alpha.
\]

The theorem must be invariant under splitting any state atom into clones; equivalently its proof is to be carried out for finite Markov kernels on atomic measure spaces and use only aggregate cut leakage.

**[RISK: precise hard core]** ACC is the partition-discovery theorem absent from the aggregation literature.  It can fail if nonreversible directed cycles allow Abel rows to be mutually separated while every candidate core has large outgoing leakage, or if transient rows require overlapping cores.  The constants 24 are conjectural.  Unlike (OC), however, ACC is a statement purely about the positive kernel \(Q\), a fixed explicit regularization \(R\), disjoint supports, and convex hull distance; it has no stochastic-idempotent unknown.

One proposed decomposition of ACC is:

**Node III.2a (aggregate cut-or-coalesce leaf). [NEW-HARD]**  Suppose \(C_1,\ldots,C_m\) are disjoint cores already produced, with representatives \(\pi_s\) satisfying (III.3).  If some row \(r_v\) has distance greater than \(24\alpha\) from their convex hull, then there is a nonempty \(C\subseteq[n]\setminus\bigcup_{s\le m}C_s\) such that

\[
 \tag{III.5}
 Q_j(C)\ge1-8\alpha\quad(j\in C),
\]

and, for the conditioned kernel

\[
 N_C(j,\ell)=Q_{j\ell}/Q_j(C)\quad(j,\ell\in C),
\]

there is \(\xi_C\in\Delta(C)\) with

\[
 \tag{III.6}
 \|\xi_CN_C-\xi_C\|_1\le16\eta,
 \qquad \max_{j\in C}\|r_j-\xi_C\|_1\le8\alpha.
\]

**[RISK]** Requiring (III.5) for every \(j\in C\) may be too strong; the correct clone-invariant form may require an aggregate law \(\xi_C\) rather than a supremum over core states.  If so, the first test below will fail quickly.  Weakening it is legitimate only if the later pure-core estimate (III.3) remains a max-row statement; otherwise the target norm has been lost.

**Node III.2b (SBD core repair). [KNOWN-mod-audit]**  Given (III.6), put \(\lambda=\alpha\) and

\[
 M_C=(1-\lambda)N_C+\lambda\,\mathbf1\xi_C.
\]

The SBD contraction argument gives a unique stationary \(\pi_C\in\Delta(C)\) and

\[
 \tag{III.7}
 \|\pi_C-\xi_C\|_1
 \le\frac{\|\xi_CM_C-\xi_C\|_1}{\lambda}
 \le\frac{16\eta}{\alpha}=16\alpha.
\]

Together with (III.6), this yields (III.3).  The use of SBD is local but the loss is a maximum \(16\alpha\), not a sum over cores.

**Node III.2c (maximal-core termination). [NEW-ROUTINE conditional on III.2a]**  Repeatedly apply III.2a.  The cores are disjoint, so the procedure terminates after at most \(n\) steps.  At termination no row violates (III.4).  There is no quantitative use of the number of steps, hence no dimension dependence.

**Node III.3 (primal membership assembly). [NEW-ROUTINE]**  Choose, for each \(i\notin\bigcup_sC_s\), coefficients \(A_{is}\ge0\), \(\sum_sA_{is}=1\), satisfying

\[
 \left\|r_i-\sum_sA_{is}\pi_s\right\|_1\le24\alpha,
\]

and set \(A_{is}=\mathbf1_{s=t}\) for \(i\in C_t\).  Let \(A\in\operatorname{Stoch}(n,k)\), and let \(U\in\operatorname{Stoch}(k,n)\) have rows \(\pi_s\).  Disjoint support and core purity give

\[
 UA=I_k.
\]

Therefore

\[
 E=AU,\qquad E^2=A(UA)U=E,
\]

and (III.3)--(III.4) give \(\|R-E\|\le24\alpha\).  With (III.2),

\[
 \tag{III.8}
 \|Q-E\|\le25\sqrt\eta.
\]

This proves III.0.

### III.2 Edge mechanisms and the square root

III.1 chooses the only time scale at which the two available errors balance: during \(m\) steps the idempotence defect telescopes to at most \(m\eta\), while resolving communication at rate \(\alpha\) costs a horizon \(m\asymp1/\alpha\).  Thus the regularization error is \(\eta/\alpha\); taking \(\alpha=\sqrt\eta\) creates the square root before any partition is chosen.

The intended proof of III.2a is a nonreversible, sup-norm Cheeger extraction.  If \(r_v\) cannot be coalesced into the convex hull of existing core laws, Hahn--Banach gives a bounded test function separating it.  Applying the resolvent identity in III.1 to successive superlevel sets of that *single* function should produce one cut with aggregate leakage \(O(\alpha)\).  Conditioning on the cut costs \(O(\alpha)\); (III.2) supplies the \(O(\eta)\) approximate-stationarity needed in (III.6).  SBD pays \(\eta/\alpha=\alpha\) once to create a canonical core law.  Maximality then gives the hull statement globally.

This is not ordinary reversible Cheeger theory: no stationary reference measure, spectral gap, or \(L^2\) norm is allowed.  The leaf is precisely the claim that the resolvent separator can be converted to a pure core without a conditioning constant depending on \(|C|\), rank, or the number of cores.

### III.3 Audit against the six walls

1. **Cloning.** Abel regularization is functorial under atom splitting.  Cuts use \(Q_j(C)\), conditioned aggregate laws, and row \(\ell^1\) distance.  The ACC statement explicitly demands clone invariance; no per-index path floor is used.
2. **Anti-splitting.** Although cores are produced sequentially, errors are never summed.  The final bounds are \(\max_s\max_{j\in C_s}\) and a single global hull distance.  Termination uses finiteness only, not a numerical class bound.
3. **Absorption/\(\rho\)-halo.** This architecture never measures hidden mass or assigns geometric capacity near \(C_W\).  If a recipient becomes a coherent recurrent core, it is coalesced as a new \(\pi_s\); this is an output, not a failure.  The separating quantity is an Abel-row functional and aggregate cut leakage, not raw mass in an affine circuit.
4. **Dual direction.** Hahn--Banach is used only to choose a primal superlevel cut.  The actual cores, conditioned kernels, laws \(\pi_s\), and memberships \(A\) are explicitly constructed.  No upper bound on hiddenness is reversed.
5. **Whole optimal face.** There is no exposedness LP.  Core purity is the support identity \(\pi_s(C_s)=1\) and \(A|_{C_s}=e_s\), which directly implies \(UA=I\).
6. **One-sided ledger.** Telescoping supplies the upper error \(\|R-Q\|\le\eta/\alpha\); SBD supplies the upper displacement \(\|\pi_C-\xi_C\|\le16\eta/\alpha\).  The proposed Cheeger leaf must independently prove the lower/purity information (III.5); it is not inferred by reversing either upper bound.

### III.4 Decisive first test

Use exact rational instances with \(\eta=s^2\) and rational \(s\).  Then

\[
 R_s=sQ(I-(1-s)Q)^{-1}
\]

is rational.  For \(n\le9\), enumerate subsets \(C\), retain those satisfying the exact inequalities (III.5), compute the conditioned rational kernel \(N_C\), and solve an LP for a rational \(\xi_C\) satisfying (III.6).  A set-packing plus hull-distance LP then decides whether a disjoint family satisfies (III.3)--(III.4), and minimizes the best constant

\[
 L(Q)=\frac1s\min_{\{C_t,\pi_t\}}
 \max\left\{max_{t,j\in C_t}\|r_j-\pi_t\|_1,
 \max_i d_1(r_i,\operatorname{conv}\{\pi_t\})\right\}.
\]

One exact instance with \(L(Q)>24\) kills ACC as stated.  More important, a rational family with \(L(Q)\to\infty\) kills the architecture, whereas bounded \(L(Q)\) on the slow two-state, thin-blocker, growing-rank W69/W71, and nonreversible-cycle families would strongly validate the finite-horizon premise.  This test attacks the new leaf directly; it does not merely check (OC).

---

## IV. Comparison and ranking

The probabilities below are subjective research-allocation estimates for “the hard core is true *and* can be proved dimension-freely,” not confidence levels in established claims.

| rank | architecture | hard core | where \(\sqrt{\cdot}\) appears | estimated expected value | reason |
|---:|---|---|---|---:|---|
| 1 | I. commutative factorization + split rounding | commutative inheritance in Kitaev's \(O(\eta)\) factorization | threshold balance \(t+\eta/t\) | **45%** | The closing lemma is already elementary and exact; the literature supplies almost all preceding structure. Exact commutativity of \(x\star y\) is a strong invariant. Main danger: the factorization theorem may not preserve the commutative category or the needed map orientation. |
| 2 | III. Abel cores + sup-norm Cheeger | ACC / aggregate cut-or-coalesce | time balance \(\alpha+\eta/\alpha\), then SBD \(\eta/\alpha\) | **18%** | It matches the exact stochastic-idempotent normal form and correctly distinguishes slow blocks from the infinite Cesàro limit. It also has a clean exact-rational decider. The missing nonreversible sup-norm Cheeger theorem is substantial and may secretly be equivalent to partition discovery. |
| 3 | II. quotient capacitary maximum principle | visible-point production and \(H^2\le4096\delta\operatorname{Cap}\) | Cauchy--Schwarz in a global signed-energy inequality | **8%** | It attacks the empirically dominant tallness wall in the most native clone-invariant language and gives a primal exposer. But the direction of the proposed capacity inequality is genuinely suspect, and thin optimal faces may refute visible-point production. Its cheap LP decider should be run before theoretical effort. |

### Recommended order of attack

First prove or refute (I-test), then audit the commutative specialization of Kitaev's factorization.  This is the only architecture whose post-hard-core portion is completely closed with explicit constants and no inherited geometric conjecture.  In parallel only in a later campaign, run the exact QCMP and ACC deciders.  If QCMP survives thin-face data, attempt the one-step signed Thomson identity; if ACC survives directed and growing-rank families, attack the single-separator cut-or-coalesce lemma rather than building a multiblock argument directly.

The central strategic distinction is that all three routes construct the exact recurrent-class structure *before* invoking the final norm estimate: I by pure code atoms, II by a primal quotient boundary, III by disjoint Abel cores.  None asks a local financing ledger to synchronize itself across an unbounded number of classes, which is the recurring failure mode of the present proof tree.
