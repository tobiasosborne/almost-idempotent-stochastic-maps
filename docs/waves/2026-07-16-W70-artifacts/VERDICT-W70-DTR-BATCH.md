conj-w69-dtr-canonical-root-top-overlap: VALID
conj-w69-dtr-pinned-deficit-oriented-tail-to-ray: VALID
conj-w69-dtr-tail-coherent-weakened-conversion: VALID
ASM: VALID

## COV

The two measures are on the same finite atomic space before the minimum is
taken.  lem-l5-mass-barycenter-dualization literally defines

\[
m_A(Q)=\sum_{j\in A\cap Q}(P_{vj})_+
\]

on full row-point fibers, even when \(A\) is not fiber-saturated.
lem-dcap-root-closure literally concludes that \(\eta_D^*\) is a full-fiber
measure satisfying \(\eta_D^*\le P_{f^*}^+\).  Restricting that measure to the
row-point class \(B=\mathsf D_{\rm tail}\) therefore gives another measure on
the same quotient.  The appendix takes

\[
\rho_Q=\min\{m_A(Q),(\eta_D^*|_B)(Q)\}
\]

atom by atom and then defines \(\rho(E)=\sum_{Q\in E}\rho_Q\).  It does not use
the generally nonadditive setwise minimum
\(E\mapsto\min\{m_A(E),(\eta_D^*|_B)(E)\}\).  The two atomwise inequalities
\(\rho_Q\le m_A(Q)\) and \(\rho_Q\le(\eta_D^*|_B)(Q)\) prove the claimed common
submeasure property without asserting a common parent or positive overlap.

Clone splitting preserves each selected fiber total in \(m_A\), including a
partially selected fiber; the selected-corner kernel is constant on clone
fibers; root closure makes \(\eta_D^*\) full-fiber; and the fixed-display
predicates defining \(B\) are row-point predicates.  Hence \(m_A,q_A,S\),
\(\eta_D^*|_B\), and their atomwise minimum \(\rho\) are clone-invariant.  No
B5 overlay or I-cap quantity enters.

## POTI-R

The crucial scope extension is not an extension: it is already in the literal
banked statements.  lem-top-deficit-price applies to any top support
functional and every row index, not only to \(A\), \(B\), a tail set, or a
selected-corner support.  For the single already fixed
\(\phi\in\Phi_v\), every row point \(Q\) therefore satisfies

\[
0\le z(p_Q)=H-\phi(p_Q)\le\|p_v-p_Q\|_1\le2+4\delta=D_0.
\]

Thus the bound covers every \(R\) with \(c_{u,R}\ne0\), including every
off-tail row.  lem-top-support-dual-face also applies on the entire row set
and supplies one fixed \(y_\phi\in Y_v\) such that

\[
z(p_Q)=y_\phi\mathbin\cdot(p_v-p_Q)
\]

for every row point.  No carrier-dependent dual direction is introduced.

The sign calculation is exact.  From \(P^2=P\), \(P\mathbf1=\mathbf1\), and
affineness of \(z\),

\[
z(p_u)=\sum_Rc_{u,R}z(p_R),\qquad \sum_Rc_{u,R}=1.
\]

For every full fiber,

\[
(-c_{u,R})_+
\le\sum_{j\in R}(-P_{uj})_+,
\]

so

\[
\sum_R(-c_{u,R})_+\le\nu_u\le\delta,
\]

where \(\nu_u=\sum_j(-P_{uj})_+\) and the last inequality is the definition of
\(\delta(P)\).  Full-fiber aggregation therefore cannot increase the negative
mass.  Discarding only nonnegative positive-coefficient off-tail terms and
bounding every negative-coefficient term by \(-D_0(-c_{u,R})_+\) yields

\[
z(p_u)\ge\mathfrak t_\phi(u)-D_0\delta,
\qquad
z(p_u)\ge[\mathfrak t_\phi(u)-D_0\delta]_+.
\]

There is no sign reversal: \(z=H-\phi\), and the AESC residual convention
remains \(x_u=p_u-a_uD_u\); the latter is not altered or used with the opposite
sign in this proof.

The restriction and domination step also has the correct signs:

\[
\sum_Qm_A(Q)z(p_Q)
\ge\sum_{u\in B}\rho(u)z(p_u)
\ge\mathfrak G_\phi.
\]

Every discarded term is nonnegative, and \(\rho\le m_A\) is atomwise.

lem-l5-mass-barycenter-dualization is literally about the original measure
\(m_A(Q)=\sum_{j\in A\cap Q}(P_{vj})_+\), of total mass \(S\), and its
barycenter \(q_A\).  It is not about the normalized \(\lambda_A\) or the scaled
\(a_A=S(1-\theta)\lambda_A\), so no hidden renormalization occurs.  Evaluation
at the already fixed \(y_\phi\) gives

\[
S Z_v(q_A)
=\sup_{y\in Y_v}\sum_{j\in A}(P_{vj})_+
  y\mathbin\cdot(p_v-p_j)
\ge\sum_Qm_A(Q)z(p_Q)
\ge\mathfrak G_\phi.
\]

The use of lem-l5-top-face-ray-formula is legal for every attained
minimizer.  No property of a favorable certificate or tie is used.  At
\(\Lambda=0\) the formula reduces to
\(Z_v(q_A)=\|p_v-q_A\|_1\), with \(c\) omitted exactly as the shard requires.

TU remains the only positive-flow aggregation foldback.  POTI-R uses only the
single public nonnegative scalar \(z/D_0\in[0,1]\), exact row reproduction, and
integration against the already constructed common measure.  It has no
second foldback, summed pairwise demand, or carrier-dependent direction sum.
The quantities \(z,c_{u,R},\mathcal T_u,\mathfrak t_\phi,\mathfrak G_\phi\)
are all defined after full-fiber aggregation and are clone-invariant under the
compatible lift.

## TC

The pinned relation is exactly \(\tau=\sqrt\delta\), hence
\(\delta=\tau^2\); it is stated in the D-cap/I-base antecedent and in
context/AESC-ATTACK-W67.md (1.2).  The cited
lem-aesc-synthetic-finance-tail-amplification applies to every \(u\in B\):
the D-tail class retains \(g_u\ge\tau\), \(A_u\ge4\),
\(\ell_u\ge\tau/2\), and \(h_u\le3\delta\), and its literal conclusion is the
strict pointwise floor
\(\operatorname{Tail}_1(u)>\tau/8\).

For a coherent carrier, the level restriction discards nonnegative terms and
gives

\[
\mathfrak t_\phi(u)
\ge\alpha\lambda\operatorname{Tail}_1(u)
>\frac{\alpha\lambda}{8}\tau.
\]

The complete deficit arithmetic is

\[
D_0=2+4\delta\le3,
\qquad
\tau\le\frac{\alpha\lambda}{48},
\]

and therefore

\[
D_0\delta=D_0\tau^2
\le3\tau^2
\le\frac{\alpha\lambda}{16}\tau.
\]

Consequently

\[
[\mathfrak t_\phi(u)-D_0\delta]_+
>\frac{\alpha\lambda}{16}\tau.
\]

Because the quotient is finite and
\(r_{\alpha,\lambda}\ge r_0>0\), strictness survives summation:

\[
\mathfrak G_\phi>
r_0\frac{\alpha\lambda}{16}\tau.
\]

POTI-R then gives the first strict TC inequality.  Finally,

\[
S\le P_v^+(1)=1+\nu_v\le1+\delta\le1+\delta_{\rm coh},
\]

so

\[
Z_v(q_A)>
\frac{r_0\alpha\lambda}{16S}\tau
\ge
\frac{r_0\alpha\lambda}{16(1+\delta_{\rm coh})}\tau.
\]

The abbreviated attack-text inequality
\(D_0\tau\le\alpha\lambda/16\) is true, and the appendix correctly multiplies
it by \(\tau\) through \(\delta=\tau^2\) to bound the quantity actually
subtracted, \(D_0\delta\).  No correction to the contract or proof is needed.

The parameters \(r_0,\alpha,\lambda,\delta_{\rm coh}\) are fixed before the
datum; equality in the coherence test belongs to the coherent class.  The
weakened conclusion assumes no actual actor and consumes neither POTI-0 nor
POTI\(+\).  Since the coherent predicate uses only the clone-invariant
full-fiber values \(c_{u,R}\), \(z(p_R)\), and
\(\operatorname{Tail}_1(u)\), both \(\mathsf C_{\alpha,\lambda}\) and
\(r_{\alpha,\lambda}\) are clone-invariant.

## ASM

The assembly is conditionally honest.  POTI-0 and POTI\(+\) are invoked only
as the two named hypotheses in the contract.  For a fixed pinned datum the
cases are exhaustive and disjoint in the order used:

1. \(\mathfrak G_\phi=0\): POTI-0 gives EC.
2. \(\mathfrak G_\phi>0\) and
   \(\mathcal D_{\rm POTI}<0\): rearrangement gives exactly the strict POTI\(+\)
   hypothesis, so POTI\(+\) gives EC.
3. \(\mathfrak G_\phi>0\) and
   \(\mathcal D_{\rm POTI}\ge0\): POTI-R, divided by \(S>0\), gives

   \[
   Z_v(q_A)\ge\frac{\mathfrak G_\phi}{S}
   \ge\frac18P_v^+(\mathcal E_*)
      -\frac{c_m}{16}P_v^+(\mathcal L_v).
   \]

Thus \(\mathfrak G_\phi=0\) is owned by POTI-0, the strict positive shortfall
by POTI\(+\), and \(\mathcal D_{\rm POTI}=0\) by the routine close.  No boundary
is omitted.  The exact EC line is obtained before either B4 spend.

The literal B4.2 conclusion in lem-dcap-tall-same-center-packet is

\[
P_v^+(\mathcal E_*)\ge\frac{\tau S}{8},
\]

at the public center \(p_{f^*}\).  Multiplication by \(1/8\) and the literal
I-base hypothesis \(S\ge c_m\) give

\[
\frac18P_v^+(\mathcal E_*)
\ge\frac{\tau S}{64}
\ge\frac{c_m\tau}{64}.
\]

Only after this substitution does the proof use the strict B4.1 conclusion
\(P_v^+(\mathcal L_v)<2\tau/15\).  Since that term has negative coefficient,
the close is strict, and the arithmetic is

\[
\frac1{64}=\frac{15}{960},\qquad
\frac1{16}\frac2{15}=\frac1{120}=\frac8{960},\qquad
\frac{15-8}{960}=\frac7{960}.
\]

Hence

\[
Z_v(q_A)>\frac{7c_m}{960}\tau.
\]

The weakened assembly (2.5)/(4.5) is TC alone and consumes neither creative
residual.  The optional scalar upgrade is a separately stated extra
hypothesis, not a covert use of POTI-0 or POTI\(+\).

The diagnostic order is also exact:

\[
\mathcal D_{\rm EC}-\frac1S\mathcal D_{\rm POTI}
=Z_v(q_A)-\frac{\mathfrak G_\phi}{S}\ge0
\]

by POTI-R, while B4.2 and \(S\ge c_m\) give

\[
\mathcal D_{\rm leaf}-\mathcal D_{\rm EC}
=\frac18P_v^+(\mathcal E_*)-\frac{c_m\tau}{64}\ge0.
\]

Thus
\(\mathcal D_{\rm leaf}\ge\mathcal D_{\rm EC}
\ge\mathcal D_{\rm POTI}/S\), without identifying the three diagnostics.

## CROSS-CUTTING

No cross-cutting defect was found.

The selected-corner certificate, its \(\phi\), the legal kernel, and all
reduced displays are fixed before the carrier and tail measurements.  The ray
certificate is arbitrary among attained minimizers, and the proof uses only
the value identity that holds for every such minimizer, including
\(\Lambda=0\).  The fixed level parameters in TC precede the datum.

All boundary ownership agrees with the pinned tree: \(h_u=3\delta\) belongs to
D-tail; actor-residual equality belongs to T-esc; mass equality \(1/160\)
belongs to HES; coherence equality belongs to the coherent class;
\(\mathfrak G_\phi=0\) belongs to POTI-0; and
\(\mathcal D_{\rm POTI}=0\) belongs to the routine close.

The appendix consumes no lem-icap-* shard, no
lem-huddle-charge-assembly, no lem-intersection-branch-production, and no
numerical W55/W57/W58/W66 fact.  It never substitutes a B5 overlay for
\(\eta_D^*\), and it uses POTI-0/POTI\(+\) only in the conditional full
assembly.  None of the dead routes in context/FINDINGS.md or kill-list
K1--K14 is crossed.  The original \(m_A\), the D-root measure, all tail
statistics, all three diagnostics, and every public scalar are kept on
clone-invariant full row-point fibers throughout.
