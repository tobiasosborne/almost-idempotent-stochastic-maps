---
id: lem-sl1a-three-cell-reduction
kind: lemma
contract: If the conjectures conj-sl1a-deep-diagonal-cell, conj-sl1a-intersection-diagonal-cell, and conj-sl1a-off-diagonal-cell hold with ceilings delta_D, delta_I, and delta_X, then co-top straddling-web exclusion SL1a holds with delta_0 = min(2^(-16),delta_D,delta_I,delta_X).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-top-deficit-price; lem-harmonic-affine-bridge; lem-mass-split; lem-positive-exposedness-margin; lem-always-tight-dual-support
status: proved-candidate
owner: W56-extraction
---

# SL1a reduction to three coefficient-kernel cells

## Statement

At a scale \(0<\delta\le2^{-16}\), call \((P,v,\phi,h,f,\xi,B)\) a selected-corner datum when: \(P\) is a finite exact signed idempotent with \(\delta(P)=\delta\), nonempty visible set \(W\), and hidden top vertex \(v\) of height \(H>16\tau\), where \(\tau=\sqrt\delta\) and \(D=2+4\delta\); \(\phi\) is a top support functional at \(v\), \(z=H-\phi\), and \(h\) is an admissible exposer at \(v\); the row point \(f\) satisfies
\[
 \|p_f-p_v\|_1\ge4\tau,\qquad
 \operatorname{dist}_1(p_f,\operatorname{conv}W)>H-4\tau,\qquad
 \frac{2z(p_f)}D+h(p_f)\le\frac{12\tau}{13};
\]
\(\xi_x(u)\) is a probability kernel on geometrically distinct row vertices, constant on clone fibers, with \(p_x=\sum_u\xi_x(u)p_u\) and Dirac at vertex points; and, after defining
\[
 \Gamma_f(x,u):=\left(\sum_{j:p_j=p_x}\max(P_{fj},0)\right)\xi_x(u),
\]
\[
 C_f:=\{(x,u):z(p_x)<4\tau,\ h(p_x)<4\tau,\ z(p_u)<4\tau,\ h(p_u)<4\tau\},
\]
\[
 B_F:=C_f\cap\{\|p_u-p_v\|_1\ge4\tau\},
 \qquad B_N:=C_f\cap\{\|p_u-p_v\|_1<4\tau\},
\]
the set \(B\) is one of \(B_F,B_N\) and satisfies \(\Gamma_f(B)\ge1/4\).  For every diagonal carrier \(u\), let \(T(u),O(u)\) be the far and upper constraint families tight on the whole optimal face of the exposedness LP at \(u\), and put
\[
 K_T(u):=\operatorname{conv}\{p_r-p_u:r\in T(u)\},
 \qquad K_O(u):=t^*(u)\operatorname{conv}\{p_i-p_u:i\in O(u)\}.
\]
Finally define
\[
 M_X(B):=\Gamma_f\{(x,u)\in B:p_x\ne p_u\},
\]
\[
 M_I(B):=\Gamma_f\{(x,u)\in B:p_x=p_u,\ K_T(u)\cap K_O(u)\ne\varnothing\},
\]
\[
 M_D(B):=\Gamma_f\{(x,u)\in B:p_x=p_u,\ K_T(u)\cap K_O(u)=\varnothing\}.
\]

Assume, only as conditional hypotheses, that `conj-sl1a-off-diagonal-cell` supplies \(\delta_X\in(0,2^{-16}]\) and forbids selected-corner data with \(M_X(B)>1/8\), that `conj-sl1a-intersection-diagonal-cell` supplies \(\delta_I\in(0,2^{-16}]\) and forbids selected-corner data with \(M_I(B)\ge1/16\), and that `conj-sl1a-deep-diagonal-cell` supplies \(\delta_D\in(0,2^{-16}]\) and forbids selected-corner data with \(M_D(B)>1/16\), in each case whenever \(\delta\) does not exceed that conjecture's ceiling.

Then the following pinned contract holds with
\[
 \delta_0:=\min\{2^{-16},\delta_D,\delta_I,\delta_X\}>0:
\]

> (CONJECTURE) Co-top straddling-web exclusion (SL1a): there exists universal delta_0 > 0 such that no exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set, and hidden top vertex v of height H > 16*tau admits a probability measure lambda on rows that are simultaneously rho-far from v (||p_f - p_v||_1 >= 4*tau) and co-top (dist_1(p_f, conv W) > H - 4*tau), with barycenter within 2.2*tau of p_v and with average value <= (16/13)*kappa under every admissible exposer at v.

## Proof

The three conjectures above are open conditional premises; none is treated as established.  Fix their ceilings first and define \(\delta_0\) as in the statement.  Suppose for contradiction that SL1a fails at this ceiling.  Thus there are an exact signed idempotent \(P\), a hidden top vertex \(v\), and a probability measure \(\lambda\) on row points with
\[
 0<\delta:=\delta(P)\le\delta_0,qquad
 \tau:=\sqrt\delta\le\frac1{256},qquad
 D:=2+4\delta\le2+2^{-14}=\frac{32769}{16384},
\]
such that \(W\ne\varnothing\), \(H>16\tau\),
\[
 \operatorname{supp}\lambda\subseteq
 \{x:\|p_x-p_v\|_1\ge4\tau,\ d_x>H-4\tau\},
 \quad
 d_x:=\operatorname{dist}_1(p_x,C_W),
 \quad C_W:=\operatorname{conv}\{p_w:w\in W\},
\]
the barycenter \(b\) obeys \(\|b-p_v\|_1\le2.2\tau=11\tau/5\), and every admissible exposer \(a\) at \(v\) obeys
\[
 \int a(p_x)\,d\lambda(x)
 \le\frac{16}{13}\kappa
 =\frac{16}{13}\frac\tau4
 =\frac{4\tau}{13}. \tag{1}
\]
These are exactly the target's radius, exposer, depth, far-radius, and tallness constants.

### Affine observables and selection

We consume the proved contract `lem-top-deficit-price` verbatim:

> Top-deficit price: for an exact signed idempotent P with delta(P) > 0 and nonempty visible set W(P), a hidden top vertex v of height H, there exists a top support functional phi (affine, phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1), and for ANY such phi, writing a_j = P_vj and z_j = H - phi(p_j) >= 0: for every subset A of row indices, sum over j in A of max(a_j,0)*z_j <= nu_v*(2+4*delta) <= delta*(2+4*delta); consequently for m >= 0, L >= 0, if sum over A of max(a_j,0) >= m and z_j >= L on A then m*L <= delta*(2+4*delta), and for delta <= 1/4, lambda > 0, theta < 1, positive v-row mass >= 1-theta on rows with z_j >= lambda*H forces H <= 3*delta/(lambda*(1-theta)), hence H <= 4*tau whenever delta <= min(1/4, (4*lambda*(1-theta)/3)^2).

Choose such a \(\phi\) and set \(z:=H-\phi\).  Its \(1\)-Lipschitz property and the row-diameter bound give \(0\le z\le D\) on all row points, so \(z/D\) is an admissible exposer at \(v\).

The web makes the \(4\tau\)-far set of \(v\) nonempty.  We consume the proved contract `lem-positive-exposedness-margin` verbatim:

> “Positive exposedness margin: for an exact signed idempotent P with rho = 4*tau > 0 (i.e. delta(P) > 0) and a geometrically distinct row vertex v with nonempty far set F_v = {j : ||p_j - p_v||_1 >= rho}: t*(v) > 0; in particular every HIDDEN geometrically distinct row vertex with F_v nonempty has 0 < t*(v) < kappa (hiddenness forces delta(P) > 0, hence rho > 0, and no row vertex is hidden at delta = 0).”

Thus \(0<t^*(v)<\kappa\).  The exposedness problem is a finite linear program in the affine value profile on the finite row set; its optimal face is a nonempty polytope and has a relative-interior point.  Fix a relative-interior optimal exposer \(h\).  Only its admissibility is needed below.

Using (1) for \(z/D\) and \(h\),
\[
 \int\left(\frac{2z(p_x)}D+h(p_x)\right)d\lambda(x)
 \le2\frac{4\tau}{13}+\frac{4\tau}{13}
 =\frac{12\tau}{13}. \tag{2}
\]
The support is finite, so there is an \(f\in\operatorname{supp}\lambda\) with
\[
 \frac{2z(p_f)}D+h(p_f)\le\frac{12\tau}{13}. \tag{3}
\]
Because \(f\) remains in the support, it is still \(4\tau\)-far and has \(d_f>H-4\tau\).  No antipode or pairwise-far family is selected.

### Coupled corner, for every legal kernel

The finite row polytope is the convex hull of its geometrically distinct vertices.  Hence there exists a probability kernel \(\xi_x(u)\) with
\(p_x=\sum_u\xi_x(u)p_u\), chosen on row points and Dirac at vertex points.  Fix any such kernel; the calculation below works for every choice.  Aggregate positive coefficient mass over the full row-point fiber and set
\[
 \Gamma_f(x,u):=P_{fx}^+\xi_x(u),
 \qquad
 C_f:=\{(x,u):z(p_x)<4\tau,\ h(p_x)<4\tau,\ z(p_u)<4\tau,\ h(p_u)<4\tau\}.
\]

We consume `lem-harmonic-affine-bridge` verbatim:

> “Harmonic-affine bridge: for an exact signed idempotent P with rows p_i = (P_ij)_j, a vector g satisfies Pg = g if and only if there exists u with g_i = u . p_i for every row index i; in the forward direction u = g works (g_i = p_i . g), and the constant term of any affine representation is absorbable into u since all row sums equal 1.”

Therefore the affine row-value functions \(z\) and \(h\) reproduce at row \(f\).  With \(\nu_f\) the negative mass in that row and
\[
 S_f:=\sum_xP_{fx}^+\bigl(z(p_x)+h(p_x)\bigr),
\]
sign splitting, \(0\le z\le D\), and \(0\le h\le1\) give
\[
 S_f\le z(p_f)+h(p_f)+\nu_f(D+1)
 \le\frac{6D\tau}{13}+\nu_f(D+1), \tag{4}
\]
where the last inequality uses \(D\ge2\) and (3).

We consume `lem-mass-split` verbatim:

> “Mass split: for an exact signed idempotent P and any row index v, writing a_j = P_{vj}, a_j^+ = max(a_j, 0), a_j^- = max(-a_j, 0), and nu_v = sum_j a_j^-, one has sum_j a_j^+ = 1 + nu_v.”

Thus \(\Gamma_f(1)=1+\nu_f\).  Affinity and the kernel identity give the same \((z+h)\)-moment \(S_f\) on the \(x\)- and \(u\)-marginals.  Failure of either pair of corner inequalities costs at least \(4\tau\) in its marginal, so a two-coordinate union bound gives
\[
 \begin{aligned}
 \Gamma_f(C_f)
 &\ge1+\nu_f-\frac{S_f}{2\tau}\\
 &\ge1-\frac{3D}{13}-\frac{\tau(D+1)}2\\
 &\ge\frac{58079731}{109051904}
 =\frac12+\frac{3553779}{109051904}>\frac12. \tag{5}
 \end{aligned}
\]
The last rational is the value at \(\tau=1/256\), \(D=32769/16384\).

For later carrier typing, observe that \(\phi(p_y)\le d_y\) for every row point \(y\): for \(c\in C_W\), the support and Lipschitz properties give \(\phi(p_y)\le\phi(c)+\|p_y-c\|_1\le\|p_y-c\|_1\), and then take the infimum.  Hence
\[
 H-d_y\le z(p_y). \tag{6}
\]
Every vertex coordinate \(u\) in \(C_f\) therefore has
\(d_u>H-4\tau>12\tau>0\), so it is hidden.  Moreover every visible \(w\) satisfies
\(\|p_u-p_w\|_1\ge d_u>4\tau\), so the far set of \(u\) is nonempty.  The quoted positive-margin contract gives \(0<t^*(u)<\kappa\).

We consume the proved contract `lem-always-tight-dual-support` verbatim:

> “Always-tight dual support: for the exposedness LP at a hidden geometrically distinct row vertex u of an exact signed idempotent P with delta(P) > 0 and nonempty visible set, every optimal hiddenness dual witness (lambda, alpha, beta), after deleting redundant centered-zero constraints, has supp(lambda) contained in T, supp(beta) contained in O, and supp(alpha) contained in Z, where T, O, Z are the rho-far, upper-box, and lower-box constraint families tight on the WHOLE primal optimal face; T is nonempty, and O is nonempty if and only if t*(u) > 0.”

Thus the carrier families \(T(u),O(u)\) in the conditional cell contracts are nonempty.  Define
\[
 K_T(u):=\operatorname{conv}\{p_r-p_u:r\in T(u)\},
 \qquad
 K_O(u):=t^*(u)\operatorname{conv}\{p_i-p_u:i\in O(u)\}.
\]
The two compact sets either intersect (type I) or are disjoint (type D), with intersection and tangency owned by type I.

### Exhaustive residual partition

Partition \(C_f\) radially, assigning distance equality to the far side:
\[
 B_F:=C_f\cap\{\|p_u-p_v\|_1\ge4\tau\},
 \qquad
 B_N:=C_f\cap\{\|p_u-p_v\|_1<4\tau\}.
\]
If \(\Gamma_f(B_F)\ge1/4\), choose \(B=B_F\); otherwise (5) gives
\[
 \Gamma_f(B_N)=\Gamma_f(C_f)-\Gamma_f(B_F)>\frac12-\frac14=\frac14,
\]
and choose \(B=B_N\).  Thus in either case \(\Gamma_f(B)\ge1/4\).  This is the only role of the radial horn; no horn-dependent mechanism is asserted.

Every pair in \(B\) is either off diagonal or diagonal.  If \(M_X(B)>1/8\), all hypotheses of the conditionally assumed off-diagonal cell exclusion hold, contradicting it because \(\delta\le\delta_X\).  Hence suppose \(M_X(B)\le1/8\).  The diagonal mass is then at least
\[
 \Gamma_f(B)-M_X(B)\ge\frac14-\frac18=\frac18. \tag{7}
\]
Every diagonal carrier has exactly one of types I and D.  If \(M_I(B)\ge1/16\), the conditionally assumed intersection-diagonal exclusion is contradicted because \(\delta\le\delta_I\).  Otherwise \(M_I(B)<1/16\), and (7) forces
\[
 M_D(B)>\frac18-\frac1{16}=\frac1{16},
\]
contradicting the conditionally assumed deep disjoint-diagonal exclusion because \(\delta\le\delta_D\).  These three cases exhaust the residual.  The strict and weak inequalities assign every boundary: radial distance equality and radial mass equality belong to the far choice, off-diagonal equality belongs to the diagonal branch, and type-I mass equality belongs to type I.

The contradiction proves SL1a with the stated \(\delta_0\).  The selections of \(\phi,h,f,\xi\) need not be canonical: at least one legal tuple exists, and each conditional cell contract excludes every tuple satisfying its displayed hypotheses, so different choices or opposite radial cells create no routing gap.

### Corrected doubled-score constant

For completeness, the affine score
\[
 q:=\frac{2z}{D}+h
\]
has \(\lambda\)-mean at most \(12\tau/13\) by (2).  Since \(q\ge0\), Markov's inequality gives
\[
 \lambda\{q\le24\tau/13\}\ge\frac12. \tag{8}
\]
For every row \(f'\) in this sub-web, the same reproduction and two-marginal calculation, now using
\(z(p_{f'})+h(p_{f'})\le12D\tau/13\), yields
\[
 \Gamma_{f'}(C_{f'})
 \ge1-\frac{6D}{13}-\frac{\tau(D+1)}2
 \ge\frac{7746547}{109051904}
 >\frac7{100}. \tag{9}
\]
Thus the web proportion is at least \(1/2\), not \(7/13\); \(7/100\) is the uniform lower bound on each selected row's corner mass.  This corrected auxiliary resource is not needed for the three-case contradiction above.

## Notes

The front-matter dependency list contains only established imports; the three conjecture ids occur in the contract solely as explicit conditional assumptions.  The proof uses the SL1a barycenter only as part of the unweakened target hypothesis; no antipode or nonlinear-measure interchangeability is inferred from it.  All measures and coefficient sums are on row points or full fibers, every threshold is independent of matrix size, and the proof never identifies the kernel's vertex marginal with transition mass.  The conditional cell statements are the entire open surface: the invalid minimality, censoring, second-generation recursion, and far-side max-principle routes play no role.

For the standard transient-row extension
\[
 P'=\begin{pmatrix}P&0\\ \mu P&0\end{pmatrix}
\]
with \(\mu\) a probability row, direct multiplication gives \((P')^2=P'\) and \(P'\mathbf1=\mathbf1\); convexity of negative mass gives \(\delta(P')=\delta(P)\).  The new row \((\mu P,0)\) is a convex combination of the embedded old rows \((p_i,0)\), so the embedded row polytope, its geometrically distinct vertices, admissible-exposer value profiles, \(W\), and \(H\) are unchanged.  Old coefficient fibers acquire a zero new column, and the old web, selected row, and coupled measure lift without changing any displayed mass.  This is the lift direction only and uses no deletion or minimality claim.
