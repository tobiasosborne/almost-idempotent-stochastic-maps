MIXED
E1: VALID — Hull-point fixedness, affine-constant cancellation, full-fiber regrouping, and the explicit \(\ell^1/\ell^\infty\) norming functional are all correct.
E2: VALID — The two sign-unions pay each row's negative budget once, zero fibers are harmless, and fiber aggregation gives the claimed global variation bound.
E3: VALID-WITH-CORRECTIONS — The estimate and recentered corollary are valid, but the statement's endpoint-pin wording must be replaced by the difference-one normalization actually used.
E4: VALID — The tail sign split, residual-row ledger, actor-window arithmetic, closed-form ceiling, quantifier order, and T0 calibration all check exactly.
E5: VALID-WITH-CORRECTIONS — The bound and fixture are valid, but the scope must state the exact triviality threshold \(\ell\le 8\delta+16\delta^2\), hence in particular the requested \(\ell\le8\delta\) regime.

# Audit basis

The conventions at the start of `PROOFS-W60-ENGINE.md` agree with both locked definitions. In particular,

\[
\delta(P)=\max_i\sum_j(-P_{ij})_+
\]

is a maximum of **row** negative masses, not a total or averaged negative mass. Every use in E1--E5 respects this: an actual row has negative mass at most \(\delta\), while a synthetic row has negative mass at most \(\delta\) by convexity. The hypotheses \(P^2=P\), \(P\mathbf 1=\mathbf 1\), the row polytope \(K(P)\), and full equal-row fibers also match the canonical definitions. I found no signed/stochastic drift.

The relevant displays in `context/PAPER-PROOF-w59.md` are compatible with the engine: its Claim 1 is the same signed-row subset ledger used here, its Claim 2 is the rank-three coordinate instance of E1's affine moment, and its Claim 4 uses the same post-aggregation sign-union bookkeeping. The engine does not import the paper's rank-three coordinates into its frame-free claims.

# E1 audit

## Synthetic rows and cancellation

For \(q=\sum_i\lambda_i p_i\in K(P)\), row idempotence gives

\[
qP=\sum_i\lambda_i(p_iP)=q.
\]

Likewise \(q\mathbf1=1\), and convexity of \(x\mapsto(-x)_+\), followed by summation over coordinates, gives \(\nu(q)\le\sum_i\lambda_i\nu(p_i)\le\delta\). These are three separate valid arguments.

For \(D=q_1-q_0\), it follows that \(DP=D\) and \(D\mathbf1=0\). Thus the affine-constant cancellation in (E1.5) is valid even though \(q_0,q_1\) are hull points rather than rows:

\[
\sum_jD_j\chi(p_j)
=L\!\left(\sum_jD_jp_j\right)+\beta\sum_jD_j
=L(DP)=L(D).
\]

Here \(\sum_jD_j=0\) follows from the already-proved hull-point mass identities, and \(DP=D\) follows from the already-proved hull-point fixedness. No row-only assumption is smuggled in. Since \(\chi(q_1)-\chi(q_0)=L(D)=1\), the moment is exactly one.

The value \(\chi(p_j)\) is constant on a full row-point fiber, so the finite coordinate sum regroups exactly to \(\sum_Qd_Q\chi(p_Q)\). Internal cancellation in a fiber changes \(d_Q\), but does not invalidate the identity.

## Normalized class

With \(s=\lVert D\rVert_1\) and \(g_j=\operatorname{sgn}(D_j)\), the construction

\[
\chi(x)=\frac{g\cdot(x-q_0)}s
\]

has \(\lVert g\rVert_\infty\le1\), \(g\cdot D=s\), the two required endpoint values, and

\[
|\chi(a)-\chi(b)|\le \frac{\lVert a-b\rVert_1}{s}.
\]

This is the correct dual norm: the dual of finite-dimensional \(\ell^1\) is \(\ell^\infty\), and the sign vector attains the norm. No unsupported infinite-dimensional attainment assertion is needed. This also specializes consistently to Claim 2 of the W59 proof.

No correction is needed.

# E2 audit

The repeated synthetic-row claims \(rP=r\), \(r\mathbf1=1\), and \(\nu(r)\le\delta\) are independently proved, not merely cited. From total mass one, every coordinate subset \(U\) satisfies \(-\nu(r)\le r(U)\le r^+(U)\).

After fiber aggregation, the partition \(S=S_+\sqcup S_-\sqcup S_0\) is legitimate. On the two unions of original coordinate indices,

\[
\sum_{Q\in S_+}|d_Q|=a(U_+)-b(U_+)
\le a^+(S_+)+\nu(b),
\]

and

\[
\sum_{Q\in S_-}|d_Q|=b(U_-)-a(U_-)
\le b^+(S_-)+\nu(a).
\]

Thus each row's negative budget is used once on one union, not once per fiber. Fibers in \(S_0\) contribute exactly zero even if their coordinates cancel internally. Monotonicity of coordinatewise positive mass permits enlarging \(S_+\) and \(S_-\) to \(S\).

Finally,

\[
\sum_Q\left|\sum_{j\in Q}(a_j-b_j)\right|
\le\sum_j|a_j-b_j|
\]

is precisely the triangle inequality on the partition into full fibers. This proves the global bound and is clone-invariant. It is compatible with, rather than a repetition of, the W59 Claim 4 ledger.

No correction is needed.

# E3 audit

## Main split

With \(d_Q=\sum_{j\in Q}(a_j-b_j)\) and \(\chi(a)-\chi(b)=1\), E1 gives the unit moment. Splitting it over \(N\cup F\) yields

\[
1\le A\sum_{Q\in N}|d_Q|+\Lambda\sum_{Q\in F}|d_Q|.
\]

Using \(\sum_{Q\in N}|d_Q|\le\ell_\chi\), followed by E2 only on \(F\), gives (E3.4). Division by \(\Lambda>0\) and rearrangement give (E3.1) with the stated signs. The argument remains valid when \(1-A\ell_\chi\le0\); in that case the floor may simply be uninformative. The bound \(\ell_\chi\le\ell\) is E2.8 applied globally.

## Signed row diameter and recentering

For any signed mass-one row,

\[
\lVert p_i\rVert_1=1+2\nu(p_i)\le1+2\delta.
\]

Consequently row-to-row distance is at most \(2+4\delta\), and convexity gives \(\lVert p_Q-c\rVert_1\le2+4\delta\) for every \(c\in K(P)\). Positivity of the rows is not used.

For the recentered sign functional,

\[
\psi_c(x)=\ell^{-1}\sum_j\operatorname{sgn}(D_j)(x_j-c_j),
\]

one has both \(\psi_c(p_r)-\psi_c(p_s)=1\) and

\[
|\psi_c(p_Q)|\le\lVert p_Q-c\rVert_1/\ell.
\]

Therefore the radius-\(A\ell\) fibers have the required low lever, and all fibers have lever at most \((2+4\delta)/\ell\). This proves the corollary exactly for the displayed, recentered representative.

## Required correction

The statement at lines 258--261 says:

> “\(\chi\)-difference normalized so that \(\sum_Qd_Q\chi(p_Q)=1\) is applicable (i.e. \(\chi(b)=0\), \(\chi(a)=1\) after relabelling -- state it cleanly)”

That parenthetical is needlessly stronger than, and less clear than, the condition used in the proof and the recentered corollary. “After relabelling” is also ambiguous for an ordered pair because relabelling reverses the already-defined coefficients.

Apply this mechanical correction: after defining

\[
d_Q:=\sum_{j\in Q}(a_j-b_j),
\]

replace the quoted text by

> “every affine \(\chi\) satisfying \(\chi(a)-\chi(b)=1\)”

and retain the absolute lever bounds for that displayed representative. Optionally add that \(\chi(b)=0,\chi(a)=1\) is a permissible special normalization, not a hypothesis needed by the lemma. This makes the statement match both its proof and Corollary E3.3. The issue is contract wording, not a failure of the estimate.

# E4 audit

## Quantifiers and constants

The parameters \((K_R,L,K_C)\) are fixed before

\[
B=K_C+1+\frac{K_C+K_R+1}{4},\qquad H=2L+6B
\]

and

\[
\delta_R=\min\{2^{-16},(4H^2)^{-1}\}
\]

are defined. Because \(B\ge5/4\), \(H>0\), so this is a positive, dimension-independent ceiling depending only on the three previously fixed constants. There is no quantifier reversal.

## Moment and global lever

For \(D=q-p_v\), synthetic fixedness and row fixedness give \(DP=D\), while both vectors have mass one, so \(D\mathbf1=0\). The affine calculation in (E4.8) therefore gives the unit moment exactly. The synthetic-row negative mass \(\nu(q)\le\delta\) is separately established.

The Lipschitz hypothesis is needed only for pairs of row points in \(K(P)\). Combining it with \(\chi(p_v)=0\) and the signed row-diameter bound correctly yields

\[
|\chi(p_Q)|\le(2+4\delta)/s,
\qquad s=\lVert D\rVert_1.
\]

## Tail sign-union ledger

On \(T_-\), where \(d_Q=q(Q)-c_Q<0\),

\[
\sum_{T_-}|d_Q|=c(U_-)-q(U_-)
\le\sum_{T_-}(c_Q)_++\nu(q)
\le(K_C+1)\delta.
\]

The use of \((c_Q)_+\) occurs after full-fiber aggregation, exactly as required.

Writing \(R=p_f-p_v+AD\), the identity on \(U_+\) is

\[
p_f(U_+)=c(U_+)-AD_++R(U_+).
\]

Hence

\[
AD_+\le\sum_{T_+}(c_Q)_++\lVert R\rVert_1+\nu(p_f)
\le(K_C+K_R+1)\delta.
\]

The signs in this rearrangement are correct. The row-\(q\) and row-\(f\) lower subset budgets are each charged once, and \(A\ge4\) gives the factor \(1/4\). Fibers with \(d_Q=0\) contribute neither variation nor moment. Thus (E4.16), \(\sum_T|d_Q|\le B\delta\), is valid.

## Core, scale window, and close

The core costs at most \(Ls\), since aggregation cannot increase \(D\)-variation. The tail costs at most \((2+4\delta)B\delta/s\). The two sides of the actor window are used in the correct places:

\[
Ls\le2L\tau,
\qquad
\frac{\delta}{s}\le2\tau.
\]

Therefore

\[
1\le\tau[2L+2(2+4\delta)B].
\]

Because \(\delta\le2^{-16}\), the bracket is strictly below \(H=2L+6B\), while the ceiling gives \(\tau\le1/(2H)\). Thus \(1<\tau H\le1/2\), a valid contradiction. All constants from the unit moment to the ceiling are accounted for.

## Small exact counterexample attack

I tested the most economical exact near-example, with three states and rank two, below the claimed T0 ceiling. Let

\[
u=1/512,\quad \delta=u^2=2^{-18},\quad
t=\frac{2u}{1+u^2},\quad \varepsilon=\frac{\delta}{1-t},
\]

\[
a=(0,1,0),\qquad
b=(1-t\varepsilon,-1-(1-t)\varepsilon,\varepsilon),
\]

and take the three rows to be \(p_1=a+b\), \(p_2=a\), and \(p_3=a+tb\). Exact rational multiplication gives \(P^2=P\), every row has mass one, and the row negative masses are \((\delta,0,0)\).

Set \(v=3\), \(f=2\), \(A=4\), and let \(q=a+(5t/4)b\in K(P)\). Then

\[
D=q-p_v=(t/4)b,\quad \lVert D\rVert_1=u=\sqrt\delta,
\quad p_f-p_v+4D=0.
\]

The norming affine coordinate \(\chi(a+\theta b)=4(\theta-t)/t\) has row values

\[
\chi(p_1)=261121/256,qquad \chi(p_2)=-4,qquad \chi(p_3)=0.
\]

Thus this example satisfies exact idempotence, the negativity ceiling, the actor window, zero residual, and the norming condition. It fails precisely at the required tail hypothesis: the \(p_v=p_3\) coefficient on the \(p_2\)-fiber alone is \(255/256\), and in fact

\[
\operatorname{Tail}_1(v,\chi)=66846975/66846976.
\]

So it is not a counterexample to \((K_R,L,K_C)=(3,1,0)\); it confirms that the positive top-tail cap is the indispensable obstruction rather than a hidden consequence of the other scaffold.

## T0 fixture

The W59 display has \(q=p_z\), \(\delta=t=\tau^2\), \(\lVert p_z-p_v\rVert_1=\tau\), \(A\in[4,6]\), and

\[
p_f-p_v=-A(p_z-p_v)+\delta(p_o-p_v).
\]

Since \(\lVert p_o-p_v\rVert_1\le2+4\delta<3\), the residual is strictly below \(3\delta\), so \(K_R=3\) is valid. The normalized class is nonempty by E1. For every such functional, the W59 relation for \(p_w\) gives \(|\chi(p_w)|<1\) at \(\tau\le1/256\). The only positive top coefficients are \(c_v=1-\tau\) and \(c_w=\tau+\delta\); \(c_f=-\delta\), and all others are zero. Hence the tail at \(L=1\) is exactly zero, giving \(K_C=0\).

For \((3,1,0)\), \(B=2\), \(H=14\), and

\[
\delta_R(3,1,0)=\min\{2^{-16},1/784\}=2^{-16}.
\]

At \(\tau=1/256\), E4 gives \(1\le\tau(10+16\delta)<11/256\), while W59 closes at \(45/1024=11.25/256\). These are consistent; E4 has slightly more scalar room.

No correction is needed.

# E5 audit

For \(\ell=\lVert p_r-p_s\rVert_1=0\), the claimed right side is \(-2\delta\), so the result is immediate. For \(\ell>0\), the recentered sign functional has difference one and the correct distance lever. Taking

\[
N=\{Q:\lVert p_Q-c\rVert_1\le1/2\},\qquad
F=N^c,
\]

with \(A_0=1/(2\ell)\) and \(\Lambda=(2+4\delta)/\ell\), E3 gives

\[
P_r^+(F)+P_s^+(F)
\ge \frac{1-A_0\ell_\psi}{\Lambda}-\nu(p_r)-\nu(p_s).
\]

Since \(\ell_\psi\le\ell\), the numerator is at least \(1/2\); since each actual row has negative mass at most \(\delta\), this is exactly

\[
\frac{\ell}{2(2+4\delta)}-2\delta.
\]

All inequalities have the correct direction.

For the stochastic fixture, the proposed mixture construction is idempotent: recurrent-block coordinates see the corresponding recurrent row, and transient coordinates carry zero mass. Full-fiber aggregation does not alter the calculation, even if transient indices clone a recurrent or mixture row, because both tested rows put zero coordinate mass on the transient set. The piecewise formula (E5.14), including its endpoint ownership under the strict condition \(>1/2\), is correct. The concrete matrix

\[
P=\begin{pmatrix}
1&0&0\\
0&1&0\\
1/2&1/2&0
\end{pmatrix}
\]

with \(r=1\), \(s=2\), and \(c=p_2\) has \(\ell=2\), exterior joint mass \(1\), and E5 lower bound \(1/2\). This confirms the stated factor-two slack, while the family-specific \(\ell/2\) bound is attained.

## Required correction

The scope at lines 880--881 only says:

> “Its lower bound can be vacuous when \(\ell\) is small compared with \(\delta\)”

The exact condition should be recorded. The right side of (E5.1) is nonpositive if and only if

\[
\ell\le4\delta(2+4\delta)=8\delta+16\delta^2.
\]

Because the left side is always nonnegative, E5 is then a trivial lower bound. In particular, it is vacuous throughout the specifically requested regime \(\ell\le8\delta\). Replace the quoted scope sentence by this exact threshold. This is an honesty/scope correction; it does not change the valid statement or proof.

# DEAD-ROUTE

none. The proofs use clone-invariant full-fiber quantities, never raw-index path products; E2 and E4 pay budgets on whole sign-unions, never per fiber; no censoring argument is invoked; and no canonical-frame estimate is promoted to a frame-free assertion.
