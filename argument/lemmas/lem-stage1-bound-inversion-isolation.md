---
id: lem-stage1-bound-inversion-isolation
kind: lemma
contract: Parameterized same-map actual-isolation package: for every universal def-stage1-polar-witness-data tuple W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso) with C_rect,C_ch,C_pol,C_grp,C_path,C_der>=1, 0<e_rect<=1/C_rect, 0<kappa_ch,kappa_pol,kappa_der<=1/2, delta_*=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol)}, epsilon_*^r=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol),kappa_der/(8*C_der),1/C_grp,delta_*/(12*C_path*C_grp)}, e_S1=min{e_rect,epsilon_*^r/C_rect}, and r_iso=min{delta_*/4,kappa_der/(8*C_der)}, there exist universal e_quot^r>0 and epsilon_B^r>0 with epsilon_B^r=min{epsilon_*^r,e_quot^r} such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0<=epsilon_r<=epsilon_B^r and 1<dim_C calX<infinity, and for displayed data satisfying all of the following: (A_2) for every V in calUbar_delta_* and A^par in B_{2delta_*}^{icalH}(0) there is a unique g_V(A^par) in B_{2delta_*}^{calH}(0) with f_V(A^par+g_V(A^par))=0, where f_V(A)=(1/2)*(((J+A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J+A))-J), chi_V(A^par)=V bold-dot (J+A^par+g_V(A^par)) lies in calU, ||Dg_V(A^par)||<=C_ch*(epsilon_r+delta_*), ||D_{A^perp}f_V(A^par+g_V(A^par))-I_calH||<=C_ch*(epsilon_r+delta_*)<1, and these C^1 charts cover calU; (A_4) set Pi_delta_*:calU x B_{delta_*}^{calH}(J)->calX by Pi_delta_*(U,K):=U bold-dot K and set S_delta_*:=Pi_delta_*(calU x B_{delta_*}^{calH}(J)); Pi_delta_* is a C^1 diffeomorphism onto S_delta_* with unique inverse maps u_delta:S_delta_*->calU and h_delta:S_delta_*->B_{delta_*}^{calH}(J) satisfying X=u_delta(X) bold-dot h_delta(X) for every X in S_delta_* and u_delta(U)=U and h_delta(U)=J for every U in calU; (A_5) the displayed maps mu:calU x calU->calU and sigma:calU->calU are defined by mu(U,V):=u_delta(U bold-dot V) and sigma(U):=u_delta(U^dagger), are global C^1 and, for every U,V,Z in calU, mu(J,U)=mu(U,J)=U, sigma(J)=J, ||mu(U,V)-U bold-dot V||<=C_grp*epsilon_r, ||sigma(U)-U^dagger||<=C_grp*epsilon_r, ||mu(mu(U,V),Z)-mu(U,mu(V,Z))||<=C_grp*epsilon_r, ||mu(sigma(U),U)-J||<=C_grp*epsilon_r, and ||mu(U,sigma(U))-J||<=C_grp*epsilon_r; (A_6) for every U_0,U_1 in calU and q in [0,1] satisfying ||U_1-U_0||<=q, C_path*q<=1/4, and C_path*(q+epsilon_r*q+q^2)<delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), the path H(-,U_0,U_1):[0,1]->calU given by H(t,U_0,U_1):=u_delta((1-t)*U_0+t*U_1) is defined, is jointly continuous in its displayed variables, and joins U_0 to U_1, and satisfies H(t,cU_0,cU_1)=c*H(t,U_0,U_1) for every c in U(1) and t in [0,1]; (A_7) for every s in {+1,-1}, set chi_s:B_{r_iso}^{icalH}(0)->calU by chi_s(A):=sJ bold-dot (J+A+g_{sJ}(A)), let phi_{sJ}^par:chi_s(B_{r_iso}^{icalH}(0))->B_{r_iso}^{icalH}(0) be its inverse, and set F_s:B_{r_iso}^{icalH}(0)->icalH by F_s(A):=phi_{sJ}^par(sigma(chi_s(A))); then sigma maps chi_s(B_{r_iso}^{icalH}(0)) into itself and ||D(F_s-id)(A)+2I||<=C_der*(epsilon_r+r_iso) for every A in B_{r_iso}^{icalH}(0); and (R) set q_*:=C_grp*epsilon_r, set r_-:=delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), and set eta_*:=C_path*(q_*+epsilon_r*q_*+q_*^2); the guards C_ch*(epsilon_r+delta_*)<=kappa_ch, C_pol*(epsilon_r+delta_*)<=kappa_pol, q_*<r_-, C_path*q_*<=1/4, eta_*<r_-, C_der*(epsilon_r+r_iso)<=kappa_der/4<1, and (1+epsilon_r)*(1+C_ch*(epsilon_r+delta_*))*r_iso+q_*<2delta_* hold; then, for those same u_delta,h_delta,mu,sigma,H, there exist r_bidx>0 depending only on W, a space breve-calU, and maps breve-mu:breve-calU x breve-calU->breve-calU and breve-sigma:breve-calU->breve-calU such that r_bidx=r_iso and breve-calU=calU_e/U(1), set breve-e:=[J], breve-mu([U],[V])=[mu(U,V)], breve-sigma([U])=[sigma(U)], (breve-calU,breve-mu,breve-e) is a connected H-space, breve-sigma is a smooth left inversion, sigma(cU)=conj(c)*sigma(U), ||sigma(U)-U^dagger||<=C_grp*epsilon_r, breve-calU is a connected compact orientable smooth manifold without boundary of real dimension (dim_C calX)-1, breve-e is an isolated fixed point of breve-sigma with local index +1, and J and -J are the only sigma-fixed points in their respective ambient r_bidx-balls.
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra; def-h-space-left-inversion; def-lefschetz-fixed-point-data
deps: lem-stage1-bound-quotient-local-index; lem-stage1-quantitative-inverse-function
status: proved
af: validated
workspace: proofs/lem-stage1-bound-inversion-isolation
provenance: DESIGN-S1-ENDGAME-v5.md sect-2 (landed verbatim); AUDIT-S1-ENDGAME-v5.md VERDICT LAND (zero corrections); user-ratified 2026-07-30
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 10-node tree, root
`validated`, taint clean 10/10
(`proofs/lem-stage1-bound-inversion-isolation/export.md`; oracle pass;
tier routine, 10 nodes <= cap 12, budget 7/3/12). One challenge (a
strict-inequality chain asserted from A_7's non-strict bound) raised
and repaired. Ambient isolation of J,-J at r_bidx=r_iso: B0i's
quantitative inclusion first, then QIFT injectivity, per the ratified
design. Contract VERBATIM from DESIGN-S1-ENDGAME-v5 sect-2 (audit v5
LAND; ratified 2026-07-30). Position 7/13.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
7 / 3 / 12. The per-node skeleton is DESIGN-S1-ENDGAME-v5.md sect-4
(lem-stage1-bound-inversion-isolation); a hard-cap hit is a factoring stop, not a rounds bump. Constants
live in the proof body, never the contract.

**Provenance loci.** same-map coordinate and ambient clauses from B0i; `refs/kitaev-2405.02434/approximate_algebras.tex:929-943,947-955`
