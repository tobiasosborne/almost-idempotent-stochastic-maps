---
id: def-routef-raw-factor-setting
term: Route-F raw-factor setting data
aliases: finite Route-F raw-factor setting; Route-F raw-factor scalar header; raw-factor setting datum
kind: original
status: locked
source: internal
locus: DESIGN-LEDGER-SETTING-RESCOPE-V2.md sect-1 (hostile re-audit AUDIT-LEDGER-SETTING-RESCOPE-V2.md, deletion test CLEARED: data-and-typing only)
sha256: -
consensus: user-ratified 2026-08-05 (tobiasosborne, in-session sign-off of the audited LAND-WITH-EXACT-CORRECTIONS rescope package; corrections folded in at landing)
---

**Statement (data, typing, and notation only).** *Route-F raw-factor setting
data* have two levels: a scalar header `W_RF`, and a setting datum `S` over
that header.

The scalar header has four receiving real-scalar fields
$$
(\eta_A,C_A,C_E,\varepsilon_E).
$$

The following symbols are derived notation, not independent witnesses:
$$
C_\theta:=12(\sqrt2-1),\qquad
\rho_\theta:=\frac18,\qquad
\rho_{\mathrm{AI}}:=\eta_A,\qquad
\bar C_E:=\max\{1,C_E\},
$$
$$
C_V:=\bar C_EC_A,\qquad C_T:=C_\theta+3C_V,
$$
$$
\rho_T:=\min\left\{
\rho_\theta,\rho_{\mathrm{AI}},\frac{\varepsilon_E}{C_A},
\frac1{4(1+C_\theta)},\frac1{4(1+C_V)}
\right\}.
\qquad (1.1)
$$

Continue, in the displayed order, with
$$
\begin{aligned}
\rho_{\mathrm{unit}}&:=\rho_T,\\
\rho_{\mathrm{id}}&:=\min\{\rho_{\mathrm{AI}},\varepsilon_E/C_A\},\\
\rho_{\mathrm{id}}^{\mathrm{corr}}
&:=\min\{\rho_\theta,\rho_{\mathrm{AI}},\varepsilon_E/C_A\},\\
\rho_{\mathrm{prod}}&:=\rho_T,\\
C_{\Delta'}&:=C_T+4C_\theta,\\
\rho_{\Delta'}&:=\min\{\rho_T,\rho_{\mathrm{prod}}\},\\
C_\Delta&:=6C_T+7C_{\Delta'},\\
\rho_\Delta&:=\min\left\{
\rho_{\mathrm{unit}},\rho_{\Delta'},[2(C_T+C_{\Delta'})]^{-1}
\right\},\\
C_2&:=C_{\Delta'}+4C_\Delta,\\
\rho_2&:=\min\{\rho_{\mathrm{prod}},\rho_{\Delta'},\rho_\Delta\},\\
\rho_{\Delta\Phi}&:=\min\{\rho_\theta,\rho_\Delta,\rho_2\},\\
C_3&:=10+20C_\Delta+12C_\theta+2C_{\Delta'},\\
\rho_3&:=\min\{\rho_\theta,\rho_{\Delta'},\rho_\Delta,\rho_2\}.
\end{aligned}
\qquad (1.2)
$$

For the componentwise block, put
$$
\begin{aligned}
C_N&:=C_V+C_\Delta,\\
C_R&:=C_N+C_2=C_V+C_\Delta+C_2,\\
C_L&:=C_2+C_3+2C_R,\\
C_{\Upsilon'}&:=1+C_\theta+2C_\Delta+2C_L,
\end{aligned}
\qquad (1.3)
$$
$$
\rho_{\Upsilon'}:=\min\left\{
\rho_T,\rho_{\mathrm{id}},\rho_\Delta,\rho_2,\rho_3,(2C_R)^{-1}
\right\}.
\qquad (1.4)
$$

Then put
$$
\begin{aligned}
C_\Upsilon&:=6C_T+7C_{\Upsilon'},\\
\rho_\Upsilon&:=\min\left\{
\rho_{\mathrm{unit}},\rho_{\Upsilon'},
[2(C_T+C_{\Upsilon'})]^{-1}
\right\},\\
\rho_{\Delta\Upsilon}&:=\min\{
\rho_\theta,\rho_T,\rho_{\mathrm{id}},\rho_\Delta,\rho_\Upsilon\},\\
\rho_{\mathrm{mult}}&:=\min\{
\rho_T,\rho_{\mathrm{id}},\rho_{\Delta\Phi},\rho_\Upsilon\},\\
\rho_{\Upsilon\Delta}&:=\min\{
\rho_T,\rho_{\mathrm{id}},\rho_\Delta,\rho_\Upsilon\}.
\end{aligned}
\qquad (1.5)
$$

Finally,
$$
K:=\max\left\{
1,
C_\theta+C_\Delta+2C_\Upsilon,
C_\Upsilon+2(C_2+C_\theta+C_\Delta),
C_\Upsilon+2C_\Delta
\right\},
\qquad (1.6)
$$
$$
\rho_{\mathrm{fac}}:=\min\{
\rho_2,\rho_{\Delta\Upsilon},\rho_{\mathrm{mult}},
\rho_{\Upsilon\Delta}
\},
\qquad (1.7)
$$
$$
\eta_K:=\min\{\rho_{\mathrm{fac}},(24K)^{-1},1\}.
\qquad (1.8)
$$

A setting datum `S` over `W_RF` records the following typed data:

1. a nonzero finite-dimensional complex Hilbert space `H`, a
   [[def-ucp-map|UCP map]] `Phi:B(H)->B(H)`, and a real scalar `eta`;
2. a linear map `tilde-Phi:B(H)->B(H)`, its range `A:=Im(tilde-Phi)`, a
   bilinear operation `X star Y:=tilde-Phi(XY)` on `A`, and the scalar
   notation
   $$
   r:=\frac32\bigl((1-4\eta)^{-1/2}-1\bigr),
   \qquad
   \varepsilon_{\mathrm{AI}}(\eta):=
   \max\{r,20\eta+2((1+r)^5-1),3r-r^2\};
   $$
3. a finite-dimensional unital C*-algebra `B` and linear maps `v:B->A` and
   `u:A->B`; and
4. the notation
   $$
   \widetilde\Delta:=\iota_{\mathcal A\subseteq B(H)}\circ v,
   \qquad
   \widetilde\Upsilon:=u\circ\widetilde\Phi.
   $$

The displayed map `tilde-Phi` is the notation
$$
\widetilde\Phi
:=\frac12\left(I+(2\Phi-I)
\bigl(I-4(\Phi-\Phi^2)\bigr)^{-1/2}\right).
$$

For every linear map `T` occurring in a datum and every integer `q>=1`,
`T_q:=id_{M_q} tensor T`.  Registry ASCII `A` and `B` denote the two
algebras above; `I_B` denotes the unit of `B`.  An unsubscripted `I` is the
unit forced by the adjacent map types.

**Notes / provenance.** This shard asserts only the shape and notation of a
record.  In particular, it asserts none of the following: that a header or
datum exists; that any scalar is positive, finite, universal, or independent
of input data; that `||Phi^2-Phi||_cb<=eta`; that `tilde-Phi` is
idempotent; that `A` is an extended approximate C*-algebra; that `v` is an
[[def-extended-delta-inclusion|extended isomorphism]]; or any norm,
smallness, admissibility, CP, or UCP estimate for the recorded maps.  Those
assertions belong only to result rows, beginning with
`lem-routef-raw-factor-setting-formation`.  The terms “UCP map”, “extended
epsilon-C*-algebra”, and “extended delta-isomorphism” are referenced from
their canonical shards and are not redefined here.  The labels `u` and `v` do not assert an inverse
relation; that relation is a conclusion of the formation result.
