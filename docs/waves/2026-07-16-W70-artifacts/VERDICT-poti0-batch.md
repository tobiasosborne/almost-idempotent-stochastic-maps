S0: VALID
RX: VALID
O48: VALID
ASM2: VALID

## S0

The proof is exhaustive and disjoint. COV makes every \(\rho(Q)\) nonnegative,
so \(r=\rho(1)\ge 0\). Each summand
\[
\rho(u)[\mathfrak t_\phi(u)-D_0\delta]_+
\]
is nonnegative. Hence \(\mathfrak G_\phi=0\) makes every summand zero. If
\(r>0\), division is performed only for carriers with \(\rho(u)>0\), yielding
\(\mathfrak t_\phi(u)\le D_0\delta\). The alternatives \(r=0\) and \(r>0\)
are exhaustive and disjoint, with equality owned by \(\mathsf Z\). No positive
overlap threshold or further support split is introduced.

## RX

The selected-root provenance is sound, including partially selected clone
fibers. The literal contract of `lem-ihorn-cotop-sl1a-package` defines
\[
\lambda_A=\frac{(m_A/S)|_{\{d_Q>H-4\tau\}}}{1-\theta},
\]
and `lem-ihorn-selected-corner-extraction` literally places \(f^*\) in
\(\operatorname{supp}\lambda_A\). Since
\(\theta<\tau/D_0<1\) and \(S>0\), finite atomic support gives
\[
\lambda_A(Q_{f^*})>0,\qquad
m_A(Q_{f^*})=S(1-\theta)\lambda_A(Q_{f^*})>0.
\]
This is a statement about the full quotient atom \(Q_{f^*}\). When only some
clones in that fiber lie in \(A\), its mass remains
\(\sum_{j\in A\cap Q_{f^*}}(P_{vj})_+\); support positivity requires this
aggregate to be positive, not that every clone be selected. Appendix lines
271--298 bridge this point explicitly and correctly.

The zero-overlap step is atomwise. From
\[
0=r=\sum_Q\min\{m_A(Q),\eta_B(Q)\}
\]
and nonnegativity, every atomwise minimum is zero. Thus
\(\eta_B(Q)>0\) forces \(m_A(Q)=0\), so
\[
m_A(C_B)=0,\qquad
\sigma_B=(P_v^+-m_A)(C_B)=P_v^+(C_B).
\]
No cancellation or merely setwise inference is used.

The foldback invocation matches the literal shard. The source
\[
m_*=w_*1_{\{Q_*\}}
\]
satisfies \(0\le m_*\le m_A\le P_v^+\), and the single common full-fiber test
\(g_*=w_*1_{C_B}\) has \(0\le g_*\le M=w_*\). The foldback shard's literal
error is \(2\delta(1+\delta)M=e_\delta M\). It is not generically scaled by
source mass, but here \(M=w_*=m_*(1)\), so it is exactly \(w_*e_\delta\).
Before division, all factors are
\[
\sum_Qm_*(Q)P_Q^+(g_*)
=w_*^2P_{f^*}^+(C_B)
\le w_*P_v^+(C_B)+w_*e_\delta.
\]
Division by the already proved \(w_*>0\), root closure
\(P_{f^*}^+(C_B)\ge M_B\), and the atomwise identity above give exactly
\(\sigma_B\ge w_*M_B-e_\delta\).

## O48

The truncation constants and boundary are correct. The complement of
\(V_{48}=\{z<48\tau\}\) is \(z\ge48\tau\), so equality is on the high side.
For every positive-overlap carrier, S0 supplies
\(\mathfrak t_\phi(u)\le D_0\delta\), while the top-deficit shard gives
\(z\ge0\). Since \(\tau=\sqrt\delta>0\) and \(D_0=2+4\delta\le3\),
\[
\sum_{\mathcal T_u\cap\{z\ge48\tau\}}(c_{u,R})_+
\le\frac{D_0\delta}{48\tau}
=\frac{D_0\tau}{48}
\le\frac{\tau}{16}.
\]

The cited AESC tail shard is legally applicable to every \(u\in B\):
\(B\subset\mathsf D_{\rm tail}\subset\mathsf A_{\rm esc}\) supplies
\(u\in\operatorname{supp}\eta_D^*\), \(g_u\ge\tau\), \(A_u\ge4\), and
\(\ell_u\ge\tau/2\), while
\(h_u=\operatorname{dist}_1(x_u,K(P))\le3\delta\) supplies its remaining
hull-distance hypothesis. It yields the strict floor
\(\operatorname{Tail}_1(u)>\tau/8\) (also explicitly present in the pinned
carrier hypothesis). Subtracting the non-strict high-side cap gives
\[
L_{48}(u)>\frac{\tau}{16}.
\]
There is no coefficient/positive-row-mass equivocation: fiberwise,
\[
(c_{u,R})_+
=\left(\sum_{k\in R}P_{uk}\right)_+
\le\sum_{k\in R}(P_{uk})_+.
\]
After summing over \(\mathcal T_u\cap V_{48}\), this proves
\(P_u^+(V_{48})\ge L_{48}(u)>\tau/16\).

For foldback, COV and the selected-measure definition give
\(0\le\rho\le m_A\le P_v^+\). The one common full-fiber test
\(g_{48}=r1_{V_{48}}\) has \(0\le g_{48}\le M=r\). Again the shard's error is
\(e_\delta M\), and here \(M=r=\rho(1)\), hence exactly \(re_\delta\).
The support-side strict floor gives
\[
\sum_Q\rho(Q)P_Q^+(V_{48})>\frac{r\tau}{16}.
\]
Thus the complete undivided ledger is exactly
\[
\frac{r^2\tau}{16}
<r\sum_Q\rho(Q)P_Q^+(V_{48})
\le rP_v^+(V_{48})+re_\delta.
\]
Only afterward is division by \(r>0\) performed. All three entries defining
\(\mathscr H_{48}\) are therefore strictly greater than \(\tau/16\).

## ASM2

RDSE and LDHR-48 are used only as named hypotheses and only on their own
subclasses. S0 gives the exhaustive disjoint split: RX precedes RDSE when
\(r=0\), while S0 and O48 precede LDHR-48 when \(r>0\). Neither creative
residual is asserted or used elsewhere.

For the arbitrary attained ray certificate, the literal
`lem-l5-top-face-ray-formula` makes
\[
\mathscr R_A(\Lambda,c)=Z_v(q_A)
\]
for every attained minimizer. At \(\Lambda=0\), \(c\) is omitted and the
value is \(\|p_v-q_A\|_1\), so that boundary is also covered. Consequently
the RDSE/LDHR-48 output becomes exact (EC) before any B4 conclusion is used.

B4.2 is then used once, at the already fixed center \(p_{f^*}\):
\[
\frac18P_v^+(\mathcal E_*)\ge\frac{\tau S}{64}
\ge\frac{c_m\tau}{64},
\]
with the second inequality justified by the pinned \(S\ge c_m\). B4.1 is
spent last and literally supplies
\[
P_v^+(\mathcal L_v)<\ell_T
=\delta+\frac{4\tau}{63}\left(D_0+\frac{\tau}{4}\right)
<\frac{2\tau}{15}.
\]
The strict close is arithmetically exact:
\[
\frac1{64}=\frac{15}{960},\qquad
\frac1{16}\frac2{15}=\frac8{960},\qquad
\frac{15-8}{960}=\frac7{960}.
\]
The final inequality is strict because the B4.1 bound is strict.

## CROSS-CUTTING

No cross-node defect was found. The forced quantities
\(w_*,M_B,\sigma_B,r,V_{48},L_{48},\mathscr H_{48}\) are formed from the
already fixed quotient datum and display field, are never optimized, and are
clone-invariant: all raw receiver indices occur only inside full-fiber sums.
The level \(48\tau\) is fixed once; \(z=48\tau\) remains on the high side;
\(\mathfrak G_\phi=0\) remains in POTI-0; and nothing reassigns the parent
\(\mathcal D_{\rm POTI}=0\) routine-close boundary.

There is no consumption of an `lem-icap-*` shard,
`lem-huddle-charge-assembly`, `lem-intersection-branch-production`, B5 as
\(\eta_D^*\), an L3 W69/W71 fixture, TC at the zero boundary, or the
conditional `lem-dtr-poti-assembly`. The appendix also respects the two
nearest walls: RX concludes only an unselected top-mass slack ledger, not
negativity or selected overlap (K5), and O48 concludes only a fixed
low-deficit population, not EC (F19). EC enters solely through the named
RDSE/LDHR-48 hypotheses in ASM2.
