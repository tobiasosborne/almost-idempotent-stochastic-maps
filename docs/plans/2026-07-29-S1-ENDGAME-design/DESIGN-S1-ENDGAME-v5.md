# DESIGN-S1-ENDGAME-v5 — Stage-1 endgame repair round 4

Date: 2026-07-30
Role: fresh independent design mathematician
Status: **DESIGN ONLY; NON-RIGOROUS; DO NOT LAND, SEED, OR PROMOTE before a fresh hostile audit and user ratification**

## 0. Executive disposition of audit-v4 findings

This is a self-contained replacement for `DESIGN-S1-ENDGAME-v4.md`. It
preserves every surface that audit v4 accepted and repairs all three findings.

| finding | disposition |
|---|---|
| **F1** | **FIXED by R-H1 option (a), W-FREE PROVIDER.** C1 drops `lem-stage1-polar-constant-ledger` and imports the already-T0 `lem-stage1-rectified-cstar-control`. Its actual root supplies, for every sufficiently small finite-dimensional level-one epsilon_X-C*-algebra, one exact-unit product `bold-dot`, exact unit `J`, the scale identity `epsilon_r=C_rect*epsilon_X`, and the two product/unit closeness estimates (`argument/lemmas/lem-stage1-rectified-cstar-control.md:4`). An extended epsilon_X-C*-algebra supplies that level-one algebra by `def-extended-epsilon-cstar-algebra`; no `W` is required. C1 then calls C0 below `min{e_rect,e_bridge^r/C_rect}`. This removes the reselection identified at `AUDIT-S1-ENDGAME-v4.md:25-52`. |
| **F2** | **FIXED by R-H2 option (1), COMMON RECEIVING THRESHOLD.** B0a applies the actual quotient-manifold root, binds its existential `e_quot^r>0`, sets `epsilon_B^r=min{epsilon_*^r,e_quot^r}>0`, and exports both this exact threshold and the complete manifold conclusion on `epsilon_r<=epsilon_B^r`. B0i, B0s, B0b, and B1 receive and propagate those same bound witnesses; B0i and B0b no longer apply the manifold root directly. Hence no row assumes `epsilon_*^r<=e_quot^r`, repairing `AUDIT-S1-ENDGAME-v4.md:54-101`. M19-S1 explicitly permits “all G-S1/old-side prerequisite thresholds” to be absorbed into one universal `e_call,1` (`DESIGN-MAIN-STRUCTURE-v5.md:381`), so the restricted threshold preserves the consumer shape. |
| **F3** | **FIXED.** B1 now has a separate scalar-arithmetic node. For arbitrary exact-unit `0<=epsilon_r<=e_fix^r<=epsilon_B^r<=epsilon_*^r`, it derives every specialized graph, polar, path, derivative, and chart-retention guard from the displayed formulas for `delta_*`, `epsilon_*^r`, and `r_iso`; it does not call those guards literal instances of the ledger's rectified-input (R) quantifier. This is exactly the missing visible obligation at `AUDIT-S1-ENDGAME-v4.md:103-120`. |

The ambient bridge and `r_bidx=r_iso` are preserved exactly as accepted at
`AUDIT-S1-ENDGAME-v4.md:142-205`. The B-only same-witness path, binder order,
A1 grading node, A2 root-only use, sources, definitions, T0-only acyclicity,
M19/M15 clause match, and G-S1-only hand-off are unchanged.

The design still has **13 rows**. Relative to v4 it adds no row, definition,
external id, or reference. It replaces one C1 dependency with an existing T0
provider and removes two redundant direct manifold dependencies. All targets
are at most twelve and every hard cap is at most fifteen.

## 1. Same-witness architecture and literal ledger antecedents

The B chain uses the parameterized architecture. The words “ledger package,”
`LedgerPackage(W)`, and “one tuple supplied by” do not occur in any proposed
contract. The conditional roots quantify the tuple before the algebra and
spell the following consumed clauses in-line rather than obtaining them by a
second existential application:

1. **(A_2), graph data at `delta_*`:** for every `V in calUbar_delta_*` and
   `A^par in B_{2delta_*}^{icalH}(0)`, the unique
   `g_V(A^par) in B_{2delta_*}^{calH}(0)` solves the displayed equation
   `f_V(A^par+g_V(A^par))=0`; the resulting displayed `chi_V` lies in and
   covers `calU`, is `C^1`, satisfies the displayed `Dg_V` bound, and has
   invertible displayed normal derivative.
2. **(A_4), polar data at `delta_*`:** the displayed
   `Pi_delta_*(U,H)=U bold-dot H` is a `C^1` diffeomorphism onto `S_delta_*`
   with its unique displayed inverse `(u_delta_*,h_delta_*)` and both inverse
   identities.
3. **(A_5), operations at `delta_*`:** the displayed
   `mu(U,V)=u_delta_*(U bold-dot V)` and
   `sigma(U)=u_delta_*(U^dagger)` are global `C^1` maps, with
   `sigma(J)=J`, the two unit identities, the near-product and near-adjoint
   estimates, the associator estimate, and the two near-inversion estimates,
   all with coefficient `C_grp`.
4. **(A_6), paths at `delta_*`:** whenever its displayed `q`-guards hold, the
   unique displayed `u_delta_*` projects the straight path to a jointly
   continuous scalar-equivariant path with the stated endpoints.
5. **(A_7), sign charts at `r_iso`:** for both `s=+1,-1`, the displayed
   `chi_s`, the same displayed `sigma`, and
   `F_s=phi_{sJ}^par o sigma o chi_s` obey chart retention and
   `||D(F_s-id)(A)+2I||<=C_der*(epsilon_r+r_iso)`.
6. **Scalar data actually used:** the exact formulas for
   `delta_*`, `epsilon_*^r`, `e_S1`, and `r_iso`, together with the displayed
   graph, polar, path, derivative, and chart-retention guard inequalities,
   including
   `C_der*(epsilon_r+r_iso)<=kappa_der/4<1`. These guards are hypotheses of
   the conditional B0 roots. B1 derives them for arbitrary exact-unit
   `epsilon_r<=epsilon_*^r` from the minimum formulas; it does not read them
   from the ledger's (R), whose actual quantifier is only over rectified
   `epsilon_r=C_rect*epsilon_X`.

These six bullets are an audit map, not a new definition or a contract
abbreviation. Every B contract below physically repeats its required
mathematical content. B0a alone receives the non-parameterized manifold
provider's existential threshold `e_quot^r`, defines the common
`epsilon_B^r=min{epsilon_*^r,e_quot^r}`, and exports the manifold package
below it. B0i, B0s, B0b, and B1 propagate those exact bound witnesses by
applying their immediate predecessor once. B1 alone imports the polar ledger
and binds one `W` satisfying it.

In every conditional B contract, “for displayed data satisfying” is a
universal binder for the graph family and every map introduced by the
formulae that follow. “For those same maps” means literal re-export of these
bound objects, never a fresh choice.

The provider-threshold scan is exhaustive: among the direct B0 dependencies,
`lem-stage1-quotient-manifold-package` is the only non-parameterized root
whose conclusion introduces a smallness radius (`e_quot^r`; actual root at
`argument/lemmas/lem-stage1-quotient-manifold-package.md:4`). The smooth
atlas, smooth polar inverse, explicit operations, quotient-manifold topology,
QIFT, local-index, and finite-CW roots are conditional on displayed
antecedents and introduce no competing existential threshold. Therefore
`epsilon_B^r=min{epsilon_*^r,e_quot^r}` is the complete receiving minimum.

## 2. Registry-ready row tables

Every `contract:` value below occupies one physical source line, uses flattened
ASCII, and assigns no numerical value to an existential universal constant.

### Block A — coproduct construction and trace rows

| proposed id | one-line `contract:` value | defs | exact `deps:` | provenance loci | target / rounds / hard cap | feasibility |
|---|---|---|---|---|---|---|
| `lem-stage1-hspace-coproduct-tail` | H-space coproduct-tail package over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity and (M,mu,e) is an H-space, set A=H^*(M;reals), A^+=direct_sum_{k>0} A^k, and Delta=(cross product)^(-1) o mu^*; then A is a finite-dimensional graded-commutative associative unital algebra with A^0=reals*1, Delta:A->A tensor_reals A is a degree-preserving unital algebra homomorphism with Delta(1)=1 tensor 1, and for every homogeneous a in A^+ there exist a finite set J_a and homogeneous a'_j,a''_j in A^+ for j in J_a such that Delta(a)=a tensor 1+1 tensor a+sum_{j in J_a} a'_j tensor a''_j. | `def-h-space-left-inversion` | `lem-topology-kunneth-cross-product` | construction `refs/hatcher-algebraic-topology/AT.txt:17620-17652`; printed conditions `:17654-17677`; guide `refs/kitaev-2405.02434/approximate_algebras.tex:975-1016` | 10 / 4 / 15 | **SUPPORTED-WITH-DERIVATION.** No coassociativity, counit, or antipode is imported. |
| `lem-stage1-exterior-cohomology` | Exterior cohomology of a finite H-space over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity and (M,mu,e) is an H-space, set A=H^*(M;reals), A^+=direct_sum_{k>0} A^k, and Delta=(cross product)^(-1) o mu^*; then A is a finite-dimensional graded-commutative associative unital algebra with A^0=reals*1, Delta:A->A tensor_reals A is a degree-preserving unital algebra homomorphism with Delta(1)=1 tensor 1, for every homogeneous a in A^+ there exist a finite set J_a and homogeneous a'_j,a''_j in A^+ for j in J_a such that Delta(a)=a tensor 1+1 tensor a+sum_{j in J_a} a'_j tensor a''_j, and A is isomorphic as a graded algebra to an exterior algebra on a finite family of odd-positive-degree homogeneous generators. | `def-h-space-left-inversion` | `lem-stage1-hspace-coproduct-tail` | exact printed conditions `refs/hatcher-algebraic-topology/AT.txt:17654-17677`; exact Theorem 3C.4 `:17798-17800`; grading guide `refs/kitaev-2405.02434/approximate_algebras.tex:1016`; finite-total-dimensional guide `:1009-1022` | 8 / 3 / 12 | **SUPPORTED-WITH-DIRECT-LOCAL-EXTERNALS AND AN INTERNAL GRADING STEP.** |
| `lem-stage1-left-inversion-associated-graded` | Associated-graded action of a left inversion over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity, (M,mu,e) is an H-space, and sigma:M->M is a left inversion, set A=H^*(M;reals), A^+=direct_sum_{k>0} A^k, F^{p,q}=(A^+)^p intersect A^{p+q}, and E^{p,q}=F^{p,q}/F^{p+1,q-1}; then sigma^* preserves every F^{p,q} and induces (-1)^(p+q)*id on every E^{p,q} for p >= 0 and p+q >= 0. | `def-h-space-left-inversion` | `lem-stage1-exterior-cohomology` | `refs/kitaev-2405.02434/approximate_algebras.tex:1016-1049` | 9 / 3 / 14 | **SUPPORTED-WITH-DERIVATION.** All coproduct and exterior-basis data are consumed from A1's root. |
| `lem-stage1-left-inversion-trace` | Left-inversion trace over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity, (M,mu,e) is an H-space, and sigma:M->M is a left inversion, then Tr(sigma^{*k}:H^k(M;reals)->H^k(M;reals))=(-1)^k*dim_reals H^k(M;reals) for every k >= 0. | `def-h-space-left-inversion` | `lem-stage1-left-inversion-associated-graded` | `refs/kitaev-2405.02434/approximate_algebras.tex:971-972,1023-1050` | 4 / 2 / 8 | **SUPPORTED-WITH-DERIVATION.** |

### Block B — parameterized same-witness quotient package

For compactness of prose, each contract labels its in-line conjuncts
`(A_2)`--`(R)`, but the labels are followed by the actual consumed assertions;
they do not name a new predicate.

| proposed id | one-line `contract:` value | defs | exact `deps:` | provenance loci | target / rounds / hard cap | feasibility |
|---|---|---|---|---|---|---|
| `lem-stage1-bound-quotient-left-inversion` | Parameterized bound quotient H-space package: for every universal def-stage1-polar-witness-data tuple W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso) with C_rect,C_ch,C_pol,C_grp,C_path,C_der>=1, 0<e_rect<=1/C_rect, 0<kappa_ch,kappa_pol,kappa_der<=1/2, delta_*=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol)}, epsilon_*^r=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol),kappa_der/(8*C_der),1/C_grp,delta_*/(12*C_path*C_grp)}, e_S1=min{e_rect,epsilon_*^r/C_rect}, and r_iso=min{delta_*/4,kappa_der/(8*C_der)}, there exist universal e_quot^r>0 and epsilon_B^r>0 with epsilon_B^r=min{epsilon_*^r,e_quot^r} such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0<=epsilon_r<=epsilon_B^r and 1<dim_C calX<infinity, and for displayed data satisfying all of the following: (A_2) for every V in calUbar_delta_* and A^par in B_{2delta_*}^{icalH}(0) there is a unique g_V(A^par) in B_{2delta_*}^{calH}(0) with f_V(A^par+g_V(A^par))=0, where f_V(A)=(1/2)*(((J+A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J+A))-J), chi_V(A^par)=V bold-dot (J+A^par+g_V(A^par)) lies in calU, ||Dg_V(A^par)||<=C_ch*(epsilon_r+delta_*), ||D_{A^perp}f_V(A^par+g_V(A^par))-I_calH||<=C_ch*(epsilon_r+delta_*)<1, and these C^1 charts cover calU; (A_4) set Pi_delta_*:calU x B_{delta_*}^{calH}(J)->calX by Pi_delta_*(U,K):=U bold-dot K and set S_delta_*:=Pi_delta_*(calU x B_{delta_*}^{calH}(J)); Pi_delta_* is a C^1 diffeomorphism onto S_delta_* with unique inverse maps u_delta:S_delta_*->calU and h_delta:S_delta_*->B_{delta_*}^{calH}(J) satisfying X=u_delta(X) bold-dot h_delta(X) for every X in S_delta_* and u_delta(U)=U and h_delta(U)=J for every U in calU; (A_5) the displayed maps mu:calU x calU->calU and sigma:calU->calU are defined by mu(U,V):=u_delta(U bold-dot V) and sigma(U):=u_delta(U^dagger), are global C^1 and, for every U,V,Z in calU, mu(J,U)=mu(U,J)=U, sigma(J)=J, ||mu(U,V)-U bold-dot V||<=C_grp*epsilon_r, ||sigma(U)-U^dagger||<=C_grp*epsilon_r, ||mu(mu(U,V),Z)-mu(U,mu(V,Z))||<=C_grp*epsilon_r, ||mu(sigma(U),U)-J||<=C_grp*epsilon_r, and ||mu(U,sigma(U))-J||<=C_grp*epsilon_r; (A_6) for every U_0,U_1 in calU and q in [0,1] satisfying ||U_1-U_0||<=q, C_path*q<=1/4, and C_path*(q+epsilon_r*q+q^2)<delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), the path H(-,U_0,U_1):[0,1]->calU given by H(t,U_0,U_1):=u_delta((1-t)*U_0+t*U_1) is defined, is jointly continuous in its displayed variables, and joins U_0 to U_1, and satisfies H(t,cU_0,cU_1)=c*H(t,U_0,U_1) for every c in U(1) and t in [0,1]; and (R) set q_*:=C_grp*epsilon_r, set r_-:=delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), and set eta_*:=C_path*(q_*+epsilon_r*q_*+q_*^2); the guards C_ch*(epsilon_r+delta_*)<=kappa_ch, C_pol*(epsilon_r+delta_*)<=kappa_pol, q_*<r_-, C_path*q_*<=1/4, and eta_*<r_- hold; then, for those same u_delta,h_delta,mu,sigma,H, there exist a space breve-calU and maps breve-mu:breve-calU x breve-calU->breve-calU and breve-sigma:breve-calU->breve-calU such that breve-calU=calU_e/U(1), set breve-e:=[J], breve-mu([U],[V])=[mu(U,V)], breve-sigma([U])=[sigma(U)], (breve-calU,breve-mu,breve-e) is a connected H-space, breve-sigma is a smooth left inversion, sigma(cU)=conj(c)*sigma(U), and ||sigma(U)-U^dagger||<=C_grp*epsilon_r for every c in U(1) and U in calU, and breve-calU is a connected compact orientable smooth manifold without boundary of real dimension (dim_C calX)-1. | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `def-h-space-left-inversion` | `lem-stage1-smooth-unitary-atlas`; `lem-stage1-smooth-polar-inverse`; `lem-stage1-explicit-smooth-unitary-operations`; `lem-stage1-quotient-manifold-package`; `lem-topology-quotient-manifold` | exact ledger clauses `argument/lemmas/lem-stage1-polar-constant-ledger.md:4`; `refs/kitaev-2405.02434/approximate_algebras.tex:895-912,945-955` | 9 / 4 / 13 | **SUPPORTED-WITH-TYPED COMMON THRESHOLD.** It binds the manifold provider radius and does not import or apply the polar ledger. |
| `lem-stage1-bound-quotient-local-index` | Parameterized same-map quotient local-index and ambient-chart package: for every universal def-stage1-polar-witness-data tuple W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso) with C_rect,C_ch,C_pol,C_grp,C_path,C_der>=1, 0<e_rect<=1/C_rect, 0<kappa_ch,kappa_pol,kappa_der<=1/2, delta_*=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol)}, epsilon_*^r=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol),kappa_der/(8*C_der),1/C_grp,delta_*/(12*C_path*C_grp)}, e_S1=min{e_rect,epsilon_*^r/C_rect}, and r_iso=min{delta_*/4,kappa_der/(8*C_der)}, there exist universal e_quot^r>0 and epsilon_B^r>0 with epsilon_B^r=min{epsilon_*^r,e_quot^r} such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0<=epsilon_r<=epsilon_B^r and 1<dim_C calX<infinity, and for displayed data satisfying all of the following: (A_2) for every V in calUbar_delta_* and A^par in B_{2delta_*}^{icalH}(0) there is a unique g_V(A^par) in B_{2delta_*}^{calH}(0) with f_V(A^par+g_V(A^par))=0, where f_V(A)=(1/2)*(((J+A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J+A))-J), chi_V(A^par)=V bold-dot (J+A^par+g_V(A^par)) lies in calU, ||Dg_V(A^par)||<=C_ch*(epsilon_r+delta_*), ||D_{A^perp}f_V(A^par+g_V(A^par))-I_calH||<=C_ch*(epsilon_r+delta_*)<1, and these C^1 charts cover calU; (A_4) set Pi_delta_*:calU x B_{delta_*}^{calH}(J)->calX by Pi_delta_*(U,K):=U bold-dot K and set S_delta_*:=Pi_delta_*(calU x B_{delta_*}^{calH}(J)); Pi_delta_* is a C^1 diffeomorphism onto S_delta_* with unique inverse maps u_delta:S_delta_*->calU and h_delta:S_delta_*->B_{delta_*}^{calH}(J) satisfying X=u_delta(X) bold-dot h_delta(X) for every X in S_delta_* and u_delta(U)=U and h_delta(U)=J for every U in calU; (A_5) the displayed maps mu:calU x calU->calU and sigma:calU->calU are defined by mu(U,V):=u_delta(U bold-dot V) and sigma(U):=u_delta(U^dagger), are global C^1 and, for every U,V,Z in calU, mu(J,U)=mu(U,J)=U, sigma(J)=J, ||mu(U,V)-U bold-dot V||<=C_grp*epsilon_r, ||sigma(U)-U^dagger||<=C_grp*epsilon_r, ||mu(mu(U,V),Z)-mu(U,mu(V,Z))||<=C_grp*epsilon_r, ||mu(sigma(U),U)-J||<=C_grp*epsilon_r, and ||mu(U,sigma(U))-J||<=C_grp*epsilon_r; (A_6) for every U_0,U_1 in calU and q in [0,1] satisfying ||U_1-U_0||<=q, C_path*q<=1/4, and C_path*(q+epsilon_r*q+q^2)<delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), the path H(-,U_0,U_1):[0,1]->calU given by H(t,U_0,U_1):=u_delta((1-t)*U_0+t*U_1) is defined, is jointly continuous in its displayed variables, and joins U_0 to U_1, and satisfies H(t,cU_0,cU_1)=c*H(t,U_0,U_1) for every c in U(1) and t in [0,1]; (A_7) for every s in {+1,-1}, set chi_s:B_{r_iso}^{icalH}(0)->calU by chi_s(A):=sJ bold-dot (J+A+g_{sJ}(A)), let phi_{sJ}^par:chi_s(B_{r_iso}^{icalH}(0))->B_{r_iso}^{icalH}(0) be its inverse, and set F_s:B_{r_iso}^{icalH}(0)->icalH by F_s(A):=phi_{sJ}^par(sigma(chi_s(A))); then sigma maps chi_s(B_{r_iso}^{icalH}(0)) into itself and ||D(F_s-id)(A)+2I||<=C_der*(epsilon_r+r_iso) for every A in B_{r_iso}^{icalH}(0); and (R) set q_*:=C_grp*epsilon_r, set r_-:=delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), and set eta_*:=C_path*(q_*+epsilon_r*q_*+q_*^2); the guards C_ch*(epsilon_r+delta_*)<=kappa_ch, C_pol*(epsilon_r+delta_*)<=kappa_pol, q_*<r_-, C_path*q_*<=1/4, eta_*<r_-, C_der*(epsilon_r+r_iso)<=kappa_der/4<1, and (1+epsilon_r)*(1+C_ch*(epsilon_r+delta_*))*r_iso+q_*<2delta_* hold; then, for those same u_delta,h_delta,mu,sigma,H,chi_s,F_s, there exist a space breve-calU, maps breve-mu:breve-calU x breve-calU->breve-calU and breve-sigma:breve-calU->breve-calU, and maps psi_s:chi_s(B_{r_iso}^{icalH}(0))->B_{r_iso}^{icalH}(0) for s in {+1,-1} such that breve-calU=calU_e/U(1), set breve-e:=[J], breve-mu([U],[V])=[mu(U,V)], breve-sigma([U])=[sigma(U)], (breve-calU,breve-mu,breve-e) is a connected H-space, breve-sigma is a smooth left inversion, sigma(cU)=conj(c)*sigma(U), ||sigma(U)-U^dagger||<=C_grp*epsilon_r, breve-calU is a connected compact orientable smooth manifold without boundary of real dimension (dim_C calX)-1, chi_s:B_{r_iso}^{icalH}(0)->calU has chi_s(0)=sJ and inverse psi_s=phi_{sJ}^par on its image, sigma retains that image, F_s=psi_s o sigma o chi_s and ||D(F_s-id)(A)+2I||<1, calU intersect B_{r_iso}(sJ) is contained in chi_s(B_{r_iso}^{icalH}(0)), and ||A-B||<=||chi_s(A)-chi_s(B)|| for A,B in B_{r_iso}^{icalH}(0); for these same maps, breve-e is an isolated fixed point of breve-sigma, i*reals*J is D-sigma_J-invariant, ||D-breve-sigma_{breve-e}+I||<1 in the quotient norm, det(I-D-breve-sigma_{breve-e})>0, and the local index of breve-e is +1. | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `def-h-space-left-inversion`; `def-lefschetz-fixed-point-data` | `lem-stage1-bound-quotient-left-inversion`; `lem-stage1-smooth-unitary-atlas`; `lem-stage1-smooth-polar-inverse`; `lem-stage1-explicit-smooth-unitary-operations`; `lem-stage1-quantitative-inverse-function`; `lem-topology-local-index-sign` | exact ledger clauses `argument/lemmas/lem-stage1-polar-constant-ledger.md:4`; QIFT root `argument/lemmas/lem-stage1-quantitative-inverse-function.md:4`; quotient/index source `refs/kitaev-2405.02434/approximate_algebras.tex:947-968` | 10 / 4 / 15 | **SUPPORTED-WITH-COMMON-THRESHOLD AMBIENT BRIDGE.** The manifold package and `epsilon_B^r` come from B0a; the two quantitative root clauses concern the same formula-defined `chi_s` and `sigma`. |
| `lem-stage1-bound-inversion-isolation` | Parameterized same-map actual-isolation package: for every universal def-stage1-polar-witness-data tuple W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso) with C_rect,C_ch,C_pol,C_grp,C_path,C_der>=1, 0<e_rect<=1/C_rect, 0<kappa_ch,kappa_pol,kappa_der<=1/2, delta_*=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol)}, epsilon_*^r=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol),kappa_der/(8*C_der),1/C_grp,delta_*/(12*C_path*C_grp)}, e_S1=min{e_rect,epsilon_*^r/C_rect}, and r_iso=min{delta_*/4,kappa_der/(8*C_der)}, there exist universal e_quot^r>0 and epsilon_B^r>0 with epsilon_B^r=min{epsilon_*^r,e_quot^r} such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0<=epsilon_r<=epsilon_B^r and 1<dim_C calX<infinity, and for displayed data satisfying all of the following: (A_2) for every V in calUbar_delta_* and A^par in B_{2delta_*}^{icalH}(0) there is a unique g_V(A^par) in B_{2delta_*}^{calH}(0) with f_V(A^par+g_V(A^par))=0, where f_V(A)=(1/2)*(((J+A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J+A))-J), chi_V(A^par)=V bold-dot (J+A^par+g_V(A^par)) lies in calU, ||Dg_V(A^par)||<=C_ch*(epsilon_r+delta_*), ||D_{A^perp}f_V(A^par+g_V(A^par))-I_calH||<=C_ch*(epsilon_r+delta_*)<1, and these C^1 charts cover calU; (A_4) set Pi_delta_*:calU x B_{delta_*}^{calH}(J)->calX by Pi_delta_*(U,K):=U bold-dot K and set S_delta_*:=Pi_delta_*(calU x B_{delta_*}^{calH}(J)); Pi_delta_* is a C^1 diffeomorphism onto S_delta_* with unique inverse maps u_delta:S_delta_*->calU and h_delta:S_delta_*->B_{delta_*}^{calH}(J) satisfying X=u_delta(X) bold-dot h_delta(X) for every X in S_delta_* and u_delta(U)=U and h_delta(U)=J for every U in calU; (A_5) the displayed maps mu:calU x calU->calU and sigma:calU->calU are defined by mu(U,V):=u_delta(U bold-dot V) and sigma(U):=u_delta(U^dagger), are global C^1 and, for every U,V,Z in calU, mu(J,U)=mu(U,J)=U, sigma(J)=J, ||mu(U,V)-U bold-dot V||<=C_grp*epsilon_r, ||sigma(U)-U^dagger||<=C_grp*epsilon_r, ||mu(mu(U,V),Z)-mu(U,mu(V,Z))||<=C_grp*epsilon_r, ||mu(sigma(U),U)-J||<=C_grp*epsilon_r, and ||mu(U,sigma(U))-J||<=C_grp*epsilon_r; (A_6) for every U_0,U_1 in calU and q in [0,1] satisfying ||U_1-U_0||<=q, C_path*q<=1/4, and C_path*(q+epsilon_r*q+q^2)<delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), the path H(-,U_0,U_1):[0,1]->calU given by H(t,U_0,U_1):=u_delta((1-t)*U_0+t*U_1) is defined, is jointly continuous in its displayed variables, and joins U_0 to U_1, and satisfies H(t,cU_0,cU_1)=c*H(t,U_0,U_1) for every c in U(1) and t in [0,1]; (A_7) for every s in {+1,-1}, set chi_s:B_{r_iso}^{icalH}(0)->calU by chi_s(A):=sJ bold-dot (J+A+g_{sJ}(A)), let phi_{sJ}^par:chi_s(B_{r_iso}^{icalH}(0))->B_{r_iso}^{icalH}(0) be its inverse, and set F_s:B_{r_iso}^{icalH}(0)->icalH by F_s(A):=phi_{sJ}^par(sigma(chi_s(A))); then sigma maps chi_s(B_{r_iso}^{icalH}(0)) into itself and ||D(F_s-id)(A)+2I||<=C_der*(epsilon_r+r_iso) for every A in B_{r_iso}^{icalH}(0); and (R) set q_*:=C_grp*epsilon_r, set r_-:=delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), and set eta_*:=C_path*(q_*+epsilon_r*q_*+q_*^2); the guards C_ch*(epsilon_r+delta_*)<=kappa_ch, C_pol*(epsilon_r+delta_*)<=kappa_pol, q_*<r_-, C_path*q_*<=1/4, eta_*<r_-, C_der*(epsilon_r+r_iso)<=kappa_der/4<1, and (1+epsilon_r)*(1+C_ch*(epsilon_r+delta_*))*r_iso+q_*<2delta_* hold; then, for those same u_delta,h_delta,mu,sigma,H, there exist r_bidx>0 depending only on W, a space breve-calU, and maps breve-mu:breve-calU x breve-calU->breve-calU and breve-sigma:breve-calU->breve-calU such that r_bidx=r_iso and breve-calU=calU_e/U(1), set breve-e:=[J], breve-mu([U],[V])=[mu(U,V)], breve-sigma([U])=[sigma(U)], (breve-calU,breve-mu,breve-e) is a connected H-space, breve-sigma is a smooth left inversion, sigma(cU)=conj(c)*sigma(U), ||sigma(U)-U^dagger||<=C_grp*epsilon_r, breve-calU is a connected compact orientable smooth manifold without boundary of real dimension (dim_C calX)-1, breve-e is an isolated fixed point of breve-sigma with local index +1, and J and -J are the only sigma-fixed points in their respective ambient r_bidx-balls. | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `def-h-space-left-inversion`; `def-lefschetz-fixed-point-data` | `lem-stage1-bound-quotient-local-index`; `lem-stage1-quantitative-inverse-function` | same-map coordinate and ambient clauses from B0i; `refs/kitaev-2405.02434/approximate_algebras.tex:929-943,947-955` | 7 / 3 / 12 | **SUPPORTED-WITH-QUANTITATIVE AMBIENT ISOLATION.** No import of the anaphoric uniform-isolation root is used to identify the map. |
| `lem-stage1-bound-quotient-index-data` | Parameterized complete quotient package: for every universal def-stage1-polar-witness-data tuple W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso) with C_rect,C_ch,C_pol,C_grp,C_path,C_der>=1, 0<e_rect<=1/C_rect, 0<kappa_ch,kappa_pol,kappa_der<=1/2, delta_*=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol)}, epsilon_*^r=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol),kappa_der/(8*C_der),1/C_grp,delta_*/(12*C_path*C_grp)}, e_S1=min{e_rect,epsilon_*^r/C_rect}, and r_iso=min{delta_*/4,kappa_der/(8*C_der)}, there exist universal e_quot^r>0 and epsilon_B^r>0 with epsilon_B^r=min{epsilon_*^r,e_quot^r} such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0<=epsilon_r<=epsilon_B^r and 1<dim_C calX<infinity, and for displayed data satisfying all of the following: (A_2) for every V in calUbar_delta_* and A^par in B_{2delta_*}^{icalH}(0) there is a unique g_V(A^par) in B_{2delta_*}^{calH}(0) with f_V(A^par+g_V(A^par))=0, where f_V(A)=(1/2)*(((J+A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J+A))-J), chi_V(A^par)=V bold-dot (J+A^par+g_V(A^par)) lies in calU, ||Dg_V(A^par)||<=C_ch*(epsilon_r+delta_*), ||D_{A^perp}f_V(A^par+g_V(A^par))-I_calH||<=C_ch*(epsilon_r+delta_*)<1, and these C^1 charts cover calU; (A_4) set Pi_delta_*:calU x B_{delta_*}^{calH}(J)->calX by Pi_delta_*(U,K):=U bold-dot K and set S_delta_*:=Pi_delta_*(calU x B_{delta_*}^{calH}(J)); Pi_delta_* is a C^1 diffeomorphism onto S_delta_* with unique inverse maps u_delta:S_delta_*->calU and h_delta:S_delta_*->B_{delta_*}^{calH}(J) satisfying X=u_delta(X) bold-dot h_delta(X) for every X in S_delta_* and u_delta(U)=U and h_delta(U)=J for every U in calU; (A_5) the displayed maps mu:calU x calU->calU and sigma:calU->calU are defined by mu(U,V):=u_delta(U bold-dot V) and sigma(U):=u_delta(U^dagger), are global C^1 and, for every U,V,Z in calU, mu(J,U)=mu(U,J)=U, sigma(J)=J, ||mu(U,V)-U bold-dot V||<=C_grp*epsilon_r, ||sigma(U)-U^dagger||<=C_grp*epsilon_r, ||mu(mu(U,V),Z)-mu(U,mu(V,Z))||<=C_grp*epsilon_r, ||mu(sigma(U),U)-J||<=C_grp*epsilon_r, and ||mu(U,sigma(U))-J||<=C_grp*epsilon_r; (A_6) for every U_0,U_1 in calU and q in [0,1] satisfying ||U_1-U_0||<=q, C_path*q<=1/4, and C_path*(q+epsilon_r*q+q^2)<delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), the path H(-,U_0,U_1):[0,1]->calU given by H(t,U_0,U_1):=u_delta((1-t)*U_0+t*U_1) is defined, is jointly continuous in its displayed variables, and joins U_0 to U_1, and satisfies H(t,cU_0,cU_1)=c*H(t,U_0,U_1) for every c in U(1) and t in [0,1]; (A_7) for every s in {+1,-1}, set chi_s:B_{r_iso}^{icalH}(0)->calU by chi_s(A):=sJ bold-dot (J+A+g_{sJ}(A)), let phi_{sJ}^par:chi_s(B_{r_iso}^{icalH}(0))->B_{r_iso}^{icalH}(0) be its inverse, and set F_s:B_{r_iso}^{icalH}(0)->icalH by F_s(A):=phi_{sJ}^par(sigma(chi_s(A))); then sigma maps chi_s(B_{r_iso}^{icalH}(0)) into itself and ||D(F_s-id)(A)+2I||<=C_der*(epsilon_r+r_iso) for every A in B_{r_iso}^{icalH}(0); and (R) set q_*:=C_grp*epsilon_r, set r_-:=delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), and set eta_*:=C_path*(q_*+epsilon_r*q_*+q_*^2); the guards C_ch*(epsilon_r+delta_*)<=kappa_ch, C_pol*(epsilon_r+delta_*)<=kappa_pol, q_*<r_-, C_path*q_*<=1/4, eta_*<r_-, C_der*(epsilon_r+r_iso)<=kappa_der/4<1, and (1+epsilon_r)*(1+C_ch*(epsilon_r+delta_*))*r_iso+q_*<2delta_* hold; then, for those same u_delta,h_delta,mu,sigma,H, there exist r_bidx>0 depending only on W, a space breve-calU, and maps breve-mu:breve-calU x breve-calU->breve-calU and breve-sigma:breve-calU->breve-calU such that r_bidx=r_iso and breve-calU=calU_e/U(1), set breve-e:=[J], breve-mu([U],[V])=[mu(U,V)], breve-sigma([U])=[sigma(U)], (breve-calU,breve-mu,breve-e) is a connected H-space, breve-sigma is a smooth left inversion, sigma(cU)=conj(c)*sigma(U), ||sigma(U)-U^dagger||<=C_grp*epsilon_r, breve-calU is a connected compact orientable smooth manifold without boundary of real dimension (dim_C calX)-1 and is homeomorphic to a finite simplicial complex, breve-e is an isolated fixed point of breve-sigma with local index +1, J and -J are the only sigma-fixed points in their respective ambient r_bidx-balls, and for every breve-sigma-fixed class breve-V there exist U_0 in calU_e and c,a in U(1) such that [U_0]=breve-V, sigma(U_0)=c*U_0, a^2=c, sigma(a*U_0)=a*U_0, and sigma(-a*U_0)=-a*U_0. | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `def-h-space-left-inversion`; `def-lefschetz-fixed-point-data` | `lem-stage1-bound-inversion-isolation`; `lem-stage1-quotient-finite-cw` | received manifold package from B0s; finite-CW root `argument/lemmas/lem-stage1-quotient-finite-cw.md:4`; phase lift `refs/kitaev-2405.02434/approximate_algebras.tex:939-955` | 5 / 2 / 9 | **SUPPORTED-WITH-RECEIVED-MANIFOLD-ANTECEDENT.** It propagates B0s's `epsilon_B^r` and manifold package and does not select a ledger witness. |
| `lem-stage1-extra-fixed-class` | Bound extra fixed class with one ledger selection: there exist one def-stage1-polar-witness-data tuple W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso) such that C_rect,C_ch,C_pol,C_grp,C_path,C_der>=1, 0<e_rect<=1/C_rect, 0<kappa_ch,kappa_pol,kappa_der<=1/2, delta_*=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol)}, epsilon_*^r=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol),kappa_der/(8*C_der),1/C_grp,delta_*/(12*C_path*C_grp)}, e_S1=min{e_rect,epsilon_*^r/C_rect}, r_iso=min{delta_*/4,kappa_der/(8*C_der)}, and there are universal e_quot^r>0, epsilon_B^r>0, C_fix<infinity, 0<e_fix^r<=epsilon_B^r, and r_bidx>0 with epsilon_B^r=min{epsilon_*^r,e_quot^r} and C_fix>=C_grp such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0<=epsilon_r<=e_fix^r and 1<dim_C calX<infinity, there exist a family g=(g_V:B_{2delta_*}^{icalH}(0)->B_{2delta_*}^{calH}(0))_{V in calUbar_delta_*}, maps u_delta,h_delta,mu,sigma,H, a space breve-calU, maps breve-mu:breve-calU x breve-calU->breve-calU and breve-sigma:breve-calU->breve-calU, a breve-sigma-fixed class breve-U, U_0 in calU_e, c,a in U(1), and U in calU_e such that all of the following hold: (A_2) for every V in calUbar_delta_* and A^par in B_{2delta_*}^{icalH}(0), g_V(A^par) is the unique element of B_{2delta_*}^{calH}(0) with f_V(A^par+g_V(A^par))=0, where f_V(A)=(1/2)*(((J+A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J+A))-J), chi_V(A^par)=V bold-dot (J+A^par+g_V(A^par)) lies in calU, ||Dg_V(A^par)||<=C_ch*(epsilon_r+delta_*), ||D_{A^perp}f_V(A^par+g_V(A^par))-I_calH||<=C_ch*(epsilon_r+delta_*)<1, and these C^1 charts cover calU; (A_4) set Pi_delta_*:calU x B_{delta_*}^{calH}(J)->calX by Pi_delta_*(V,K):=V bold-dot K and set S_delta_*:=Pi_delta_*(calU x B_{delta_*}^{calH}(J)); Pi_delta_* is a C^1 diffeomorphism onto S_delta_* with unique inverse maps u_delta:S_delta_*->calU and h_delta:S_delta_*->B_{delta_*}^{calH}(J) satisfying X=u_delta(X) bold-dot h_delta(X) for every X in S_delta_* and u_delta(V)=V and h_delta(V)=J for every V in calU; (A_5) the displayed maps mu:calU x calU->calU and sigma:calU->calU are defined by mu(V_1,V_2):=u_delta(V_1 bold-dot V_2) and sigma(V):=u_delta(V^dagger), are global C^1 and, for every V,V_1,V_2,V_3 in calU, mu(J,V)=mu(V,J)=V, sigma(J)=J, ||mu(V_1,V_2)-V_1 bold-dot V_2||<=C_grp*epsilon_r, ||sigma(V)-V^dagger||<=C_grp*epsilon_r, ||mu(mu(V_1,V_2),V_3)-mu(V_1,mu(V_2,V_3))||<=C_grp*epsilon_r, ||mu(sigma(V),V)-J||<=C_grp*epsilon_r, and ||mu(V,sigma(V))-J||<=C_grp*epsilon_r; (A_6) for every V_0,V_1 in calU and q in [0,1] satisfying ||V_1-V_0||<=q, C_path*q<=1/4, and C_path*(q+epsilon_r*q+q^2)<delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), the path H(-,V_0,V_1):[0,1]->calU given by H(t,V_0,V_1):=u_delta((1-t)*V_0+t*V_1) is defined, is jointly continuous in its displayed variables, and joins V_0 to V_1, and satisfies H(t,c_0*V_0,c_0*V_1)=c_0*H(t,V_0,V_1) for every c_0 in U(1) and t in [0,1]; (A_7) for every s in {+1,-1}, set chi_s:B_{r_iso}^{icalH}(0)->calU by chi_s(A):=sJ bold-dot (J+A+g_{sJ}(A)), let phi_{sJ}^par:chi_s(B_{r_iso}^{icalH}(0))->B_{r_iso}^{icalH}(0) be its inverse, and set F_s:B_{r_iso}^{icalH}(0)->icalH by F_s(A):=phi_{sJ}^par(sigma(chi_s(A))); then sigma maps chi_s(B_{r_iso}^{icalH}(0)) into itself and ||D(F_s-id)(A)+2I||<=C_der*(epsilon_r+r_iso) for every A in B_{r_iso}^{icalH}(0); (R) set q_*:=C_grp*epsilon_r, set r_-:=delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), and set eta_*:=C_path*(q_*+epsilon_r*q_*+q_*^2); the guards C_ch*(epsilon_r+delta_*)<=kappa_ch, C_pol*(epsilon_r+delta_*)<=kappa_pol, q_*<r_-, C_path*q_*<=1/4, eta_*<r_-, C_der*(epsilon_r+r_iso)<=kappa_der/4<1, and (1+epsilon_r)*(1+C_ch*(epsilon_r+delta_*))*r_iso+q_*<2delta_* hold; moreover r_bidx=r_iso and breve-calU=calU_e/U(1), set breve-e:=[J], breve-mu([V_1],[V_2])=[mu(V_1,V_2)], breve-sigma([V])=[sigma(V)], (breve-calU,breve-mu,breve-e) is a connected H-space, breve-sigma is a smooth left inversion, sigma(c_0*V)=conj(c_0)*sigma(V) and ||sigma(V)-V^dagger||<=C_grp*epsilon_r for every c_0 in U(1) and V in calU, breve-calU is a connected compact orientable smooth manifold without boundary of real dimension (dim_C calX)-1 and is homeomorphic to a finite simplicial complex, breve-e is an isolated fixed point of breve-sigma with local index +1, J and -J are the only sigma-fixed points in their respective ambient r_bidx-balls, breve-U!=breve-e, [U_0]=breve-U, sigma(U_0)=c*U_0, a^2=c, U=a*U_0, [U]=breve-U, sigma(U)=U, ||U-U^dagger||<=C_fix*epsilon_r, ||U-J||>=r_bidx, and ||U+J||>=r_bidx. | `def-epsilon-cstar-algebra`; `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-h-space-left-inversion`; `def-lefschetz-fixed-point-data` | the fixed ten, in order: `lem-stage1-uniform-inversion-isolation`; `lem-stage1-quotient-manifold-package`; `lem-stage1-quotient-finite-cw`; `lem-stage1-quotient-left-inversion`; `lem-stage1-left-inversion-trace`; `lem-topology-lefschetz-hopf`; `lem-topology-local-index-sign`; `lem-topology-orientable-top-cohomology`; `lem-stage1-quotient-inversion-index-data`; `lem-finite-polyhedron-maximal-simplex-placement`; plus `lem-stage1-polar-constant-ledger`; `lem-stage1-bound-quotient-index-data` | `refs/kitaev-2405.02434/approximate_algebras.tex:945-969`; trace `:971-1050`; fixed ten `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v6.md:234-263`; ledger root `argument/lemmas/lem-stage1-polar-constant-ledger.md:4` | 12 / 4 / 15 | **SUPPORTED-WITH-EXACTLY ONE LEDGER APPLICATION AND EXPLICIT SCALAR ARITHMETIC.** The fixed ten remain byte-ordered; the last two deps are the unique instantiator and the typed conditional package. |

#### Root-only and ambient-inradius checks

1. B0a--B0b have no direct polar-ledger dependency. Their universal `W`
   binder precedes every field and displayed map. B0a invokes the distinct
   T0 quotient-manifold provider, binds its `e_quot^r`, defines
   `epsilon_B^r=min{epsilon_*^r,e_quot^r}`, and exports the complete manifold
   package on that common range.
2. B0i, B0s, and B0b each apply only their immediate B predecessor and
   propagate the same `e_quot^r,epsilon_B^r`; none re-eliminates the manifold
   provider. B1 has the only direct polar-ledger edge. Its first proof node
   eliminates that existential once; C0 absorbs the resulting threshold and
   C1 uses the W-free rectification root. Thus no later row or node invokes
   the polar ledger again.
3. The B0i ambient clause is proved quantitatively. For `s=+1,-1`, apply the
   QIFT root to the real Banach-space affine map
   `Theta_s(B)=sJ+sB` with `V=sI` and derivative error zero. If
   `U in calU` and `||U-sJ||<r_iso`, this gives the unique
   `B=s(U-sJ)` with `||B||<r_iso`. Its anti-Hermitian and Hermitian parts
   each have norm at most `||B||`; the exact (A_2) zero equation and uniqueness
   force the Hermitian part to equal `g_{sJ}` of the anti-Hermitian part.
   Hence `U` lies in the displayed `chi_s(B_{r_iso})`. Taking the
   anti-Hermitian part of a chart difference gives the exported lower-Lipschitz
   inequality. Every constant is `1` or the universal field `r_iso`; there is
   no dimension or algebra dependence.
4. In B0s, `G_s=F_s-id` has derivative within `1` of `-2I`. QIFT therefore
   makes `G_s` injective on the displayed coordinate ball, and
   `G_s(0)=0`. A fixed ambient point in the B0i ball is first captured by the
   same chart, then has `G_s(A)=0`, hence `A=0`. Set
   `r_bidx:=r_iso`; the strict-ball convention avoids a boundary issue.
5. The fixed T0 `lem-stage1-uniform-inversion-isolation` and
   `lem-stage1-quotient-manifold-package` remain in B1's user-fixed ten-item
   list but are not re-eliminated there: same-map ambient isolation and the
   exact `e_quot^r,epsilon_B^r` manifold package are supplied by B0b. A
   literal scan of all thirteen `deps:` lists and skeletons finds
   `lem-stage1-polar-constant-ledger` in B1 only.

#### B1 scalar-arithmetic check

For B1 node 3, fix
`0<=epsilon_r<=e_fix^r<=epsilon_B^r<=epsilon_*^r`. The displayed minima give

- `C_ch*epsilon_r<=kappa_ch/4` and
  `C_ch*delta_*<=kappa_ch/4`, and the analogous two `C_pol` bounds;
- `q_*=C_grp*epsilon_r<=delta_*/(12*C_path)`;
- `epsilon_r<=1/4`,
  `C_pol*(epsilon_r+delta_*)<=kappa_pol/2<=1/4`, hence
  `r_- >= 3*delta_*/4`;
- `C_der*epsilon_r<=kappa_der/8` and
  `C_der*r_iso<=kappa_der/8`, hence
  `C_der*(epsilon_r+r_iso)<=kappa_der/4<1`.

Consequently `q_*<r_-`, `C_path*q_*<=delta_*/12<1/4`, and
`eta_*=C_path*q_* * (1+epsilon_r+q_*)<r_-`. Finally
`r_iso<=delta_*/4`, `1+epsilon_r<=5/4`,
`1+C_ch*(epsilon_r+delta_*)<=5/4`, and
`q_*<=delta_*/12`, so
`(1+epsilon_r)*(1+C_ch*(epsilon_r+delta_*))*r_iso+q_*<2delta_*`.
These are the exact specialized guards in the B contracts. None uses the
ledger's (R) conclusion, whose actual scope is the rectified relation
`epsilon_r=C_rect*epsilon_X`
(`argument/lemmas/lem-stage1-polar-constant-ledger.md:4`;
`AUDIT-S1-ENDGAME-v4.md:103-120`).

### Block C — one-use projection bridge and the three G-S1 producers

Audit v4 accepted C0's one-use/forgetting bridge, while F1 required C1's
rectification source to change. C0 remains unchanged; C1 now uses the
W-free T0 rectification provider.

| proposed id | one-line `contract:` value | defs | exact `deps:` | provenance loci | target / rounds / hard cap | feasibility |
|---|---|---|---|---|---|---|
| `lem-stage1-fixed-unitary-projection-bridge` | Fixed-unitary projection bridge: there are universal C_bridge<infinity and e_bridge^r>0 such that every finite-dimensional exact-unit epsilon_r-C*-algebra with 0<=epsilon_r<=e_bridge^r and 1<dim_C calX<infinity contains a nontrivial C_bridge*epsilon_r-projection P for the product bold-dot and unit J. | `def-epsilon-cstar-algebra`; `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-delta-projection` | `lem-stage1-extra-fixed-class` | `refs/kitaev-2405.02434/approximate_algebras.tex:917-943`, formula and estimate at `:939` | 8 / 3 / 12 | **SUPPORTED-WITH-ONE B1 APPLICATION.** |
| `lem-stage1-rectified-nontrivial-projection` | There are universal C_proj<infinity and e_proj>0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0<=epsilon_X<=e_proj and 1<dim_C calX<infinity contains a nontrivial C_proj*epsilon_X-projection P_0 for the original product and original unit I_X. | `def-extended-epsilon-cstar-algebra`; `def-epsilon-cstar-algebra`; `def-delta-projection` | `lem-stage1-rectified-cstar-control`; `lem-stage1-fixed-unitary-projection-bridge` | `refs/kitaev-2405.02434/approximate_algebras.tex:917-945`; exact-unit provider `argument/lemmas/lem-stage1-rectified-cstar-control.md:4` | 6 / 3 / 10 | **SUPPORTED-WITH-W-FREE RECTIFICATION.** The extended input supplies a level-one epsilon_X-C*-algebra; C1 binds the provider's one rectification and applies C0, never B1 or the ledger. |
| `lem-stage1-original-complementary-pair` | There are universal C_np<infinity and e_np>0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0<=epsilon_X<=e_np and 1<dim_C calX<infinity contains nonvanishing C_np*epsilon_X-projections P' and P'' for the original product such that P'+P''=I_X and ||P'P''||,||P''P'||<=C_np*epsilon_X. | `def-extended-epsilon-cstar-algebra`; `def-delta-projection` | `lem-stage1-rectified-nontrivial-projection` | `refs/kitaev-2405.02434/approximate_algebras.tex:917-929,1419-1424` | 6 / 2 / 10 | **SUPPORTED-WITH-DERIVATION.** |
| `lem-stage1-fresh-two-point-inclusion` | There are universal C_pair<infinity and e_pair>0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0<=epsilon_X<=e_pair and 1<dim_C calX<infinity contains nonvanishing C_pair*epsilon_X-projections P',P'' with P'+P''=I_X for which the linear map v^(2):C^2->calX, v^(2)(lambda,mu)=lambda*P'+mu*P'', is an extended C_pair*epsilon_X-inclusion, satisfies v^(2)(1,1)=I_X, and sends the standard projection basis Pi',Pi'' to P',P''. | `def-extended-epsilon-cstar-algebra`; `def-delta-projection`; `def-extended-delta-inclusion`; `def-operator-space`; `def-projection-basis` | `lem-stage1-original-complementary-pair` | `refs/kitaev-2405.02434/approximate_algebras.tex:458,1192-1222,1419-1424`; external statement `:1194-1196` | 9 / 3 / 14 | **SUPPORTED-WITH-DERIVATION AND ONE LOCAL CITED EXTERNAL.** |

## 3. Serial landing and elevation order

Every existing dependency is T0; proposed dependencies occur earlier:

1. `lem-stage1-hspace-coproduct-tail`;
2. `lem-stage1-exterior-cohomology`;
3. `lem-stage1-left-inversion-associated-graded`;
4. `lem-stage1-left-inversion-trace`;
5. `lem-stage1-bound-quotient-left-inversion`;
6. `lem-stage1-bound-quotient-local-index`;
7. `lem-stage1-bound-inversion-isolation`;
8. `lem-stage1-bound-quotient-index-data`;
9. `lem-stage1-extra-fixed-class`;
10. `lem-stage1-fixed-unitary-projection-bridge`;
11. `lem-stage1-rectified-nontrivial-projection`;
12. `lem-stage1-original-complementary-pair`;
13. `lem-stage1-fresh-two-point-inclusion`.

B0a--B0b are proved as conditional rows before B1. B0a binds the manifold
provider's `e_quot^r`, and every later B row propagates the same
`epsilon_B^r`. B1 then selects the polar-ledger witness once and instantiates
the already-proved conditional chain. C0 absorbs `epsilon_B^r` into its
universal `e_bridge^r`; C1 uses the independent W-free rectification root.

After row 13, only the **G-S1 gate** is discharged. MAIN still requires its P0
definition gate and M01--M18, including M04, before M19-S1--M28 are eligible.

## 4. Per-row af proof skeletons

Each numbered step is one intended af node. A hard-cap hit is a factoring stop.

### A0. `lem-stage1-hspace-coproduct-tail` — 10 nodes

1. Fix `M,mu,e`; set `A=H^*(M;reals)` and record finite total dimension,
   graded commutativity, associativity, unitality, and `A^0=reals*1`.
2. Verify the finitely-generated-free Kunneth hypotheses for `M x M`.
3. Define `Delta=(cross product)^(-1) o mu^*`.
4. Prove degree preservation and multiplicativity from naturality and Kunneth.
5. Prove `Delta(1)=1 tensor 1` internally.
6. Use the right-unit homotopy for the `a tensor 1` edge.
7. Use the left-unit homotopy for the `1 tensor a` edge.
8. Decompose the remaining degree component into positive-positive bidegrees.
9. Bind a finite tensor expansion `J_a,(a'_j,a''_j)`.
10. Assemble without coassociativity, counit, antipode, or homotopy
    associativity.

### A1. `lem-stage1-exterior-cohomology` — 8 nodes

1. Apply A0 and match its connectedness and positive-positive tail to the
   weak-Hopf external.
2. Check characteristic zero, commutative associative multiplication, and
   finite-dimensional graded pieces for 3C.4.
3. Obtain the printed exterior-tensor-polynomial algebra isomorphism.
4. Exclude every nontrivial polynomial generator by finite total dimension.
5. Prove that the odd homogeneous generator family is finite.
6. Grade the abstract exterior source by the degrees of the homogeneous odd
   target generators.
7. Prove on generator monomials that the generator-to-generator algebra
   isomorphism and its inverse preserve total degree; this is the explicit
   `approximate_algebras.tex:1016` obligation, not part of the external.
8. Re-export A0's finite-tail clauses and assemble the graded conclusion.

### A2. `lem-stage1-left-inversion-associated-graded` — 9 nodes

1. Apply A1 once and fix its finite tail and graded exterior-generator system.
2. Show `sigma^*` preserves `A^+`, its powers, and every `F^{p,q}`.
3. Translate the left-inversion homotopy into
   `cup o (sigma^* tensor id) o Delta=unit o augmentation`.
4. Consume the finite positive-positive coproduct formula from **A1's root**.
5. Derive `sigma^*(x)=-x mod (A^+)^2` for each generator.
6. Extend to length-`p` exterior monomials by multiplicativity.
7. Use odd degrees to identify word-length parity with total-degree parity.
8. Identify those monomials as a basis of every `E^{p,q}`.
9. Assemble the action `(-1)^(p+q)*id`.

### A3. `lem-stage1-left-inversion-trace` — 4 nodes

1. Record the finite exhaustive filtration of each `A^k`.
2. Apply finite-dimensional trace additivity to its associated graded.
3. Apply A2 and sum the quotient dimensions.
4. Assemble for every `k`.

### B0a. `lem-stage1-bound-quotient-left-inversion` — 9 nodes

1. Fix the universally quantified `W` and proofs of its physically displayed
   (A_2),(A_4)--(A_6), and scalar-guard antecedents. Do not invoke the polar
   ledger.
2. Apply `lem-stage1-quotient-manifold-package`, existentially bind its typed
   `e_quot^r>0`, set
   `epsilon_B^r=min{epsilon_*^r,e_quot^r}>0`, restrict to
   `epsilon_r<=epsilon_B^r`, and record the full manifold package.
3. Bind `(u_delta,h_delta)` as the unique inverse of the displayed
   `Pi_delta_*`.
4. Feed the same graph/atlas/inverse objects to the explicit smooth-operations
   root.
5. Obtain the exact formulas, `sigma(J)=J`, covariance, and near-adjoint
   estimate for this map.
6. Bind `breve-calU`, set `breve-e:=[J]`, define the two descended maps, and
   prove representative independence.
7. Attach smoothness through local quotient sections.
8. Use the displayed group/path clauses to prove the H-space laws and the
   left-inversion homotopy.
9. Assemble the conditional package, retaining the literal estimate and the
   exact `e_quot^r,epsilon_B^r` and manifold fields.

### B0i. `lem-stage1-bound-quotient-local-index` — 10 nodes

1. Apply B0a to the already fixed `W`; bind its displayed objects once.
2. Receive B0a's exact `e_quot^r,epsilon_B^r` and every manifold field; do
   not apply the quotient-manifold root again.
3. Instantiate the physically stated (A_7) clause for the same `W`,
   `u_delta`, and formula-defined `sigma`.
4. Apply QIFT to `Theta_s(B)=sJ+sB`, simultaneously for the two signs, with
   derivative error zero and radius `r_iso`.
5. Decompose `B` into anti-Hermitian/Hermitian parts and use the physically
   stated (A_2) uniqueness to prove the ambient-chart inclusions and
   lower-Lipschitz estimates.
6. Differentiate covariance and descend the invariant vertical line.
7. Prove the quotient derivative norm bound and positive determinant.
8. Apply QIFT in the quotient slice to isolate `breve-e`.
9. Check the manifold, smoothness, isolation, and determinant antecedents and
   apply the local-index root.
10. Re-export the same maps, `breve-calU`, `breve-e`, charts, ambient bridge,
    literal near-adjoint estimate, and index.

### B0s. `lem-stage1-bound-inversion-isolation` — 7 nodes

1. Apply B0i to the same fixed `W` and bind its one package.
2. Apply QIFT to `F_+-id` against `-2I`.
3. Use B0i's `+J` ambient-chart inclusion to turn any ambient fixed point into
   a zero of that coordinate map, hence into `J`.
4. Apply QIFT to `F_--id` against `-2I`.
5. Use B0i's `-J` ambient-chart inclusion analogously.
6. Set `r_bidx=r_iso`, absorb the one receiving threshold, and record that
   it is independent of the input algebra and dimension.
7. Re-export the same package, estimate, index, and both ambient-isolation
   clauses.

### B0b. `lem-stage1-bound-quotient-index-data` — 5 nodes

1. Apply B0s to the same fixed `W`; no threshold, map, inverse, or radius is
   reselected.
2. Receive its exact `e_quot^r,epsilon_B^r` and manifold package and identify
   the canonical quotient; do not apply the manifold root again.
3. Feed compactness, smoothness, and boundarylessness into the finite-CW root.
4. For each bound fixed class, bind `U_0,c,a` in that order and prove the two
   actual fixed lifts using the same displayed covariance.
5. Re-export every B1 field, including `breve-calU`, `breve-e`, the literal
   estimate, ambient radius, and phase lift.

### B1. `lem-stage1-extra-fixed-class` — 12 nodes

1. Apply `lem-stage1-polar-constant-ledger` **once**, existentially bind its
   `W`, and record its actual universally quantified (A_2),(A_4)--(A_7)
   conclusions and the displayed formulas for
   `delta_*`, `epsilon_*^r`, and `r_iso`; do not claim the rectified-input
   (R) guards have the arbitrary exact-unit quantifier used below.
2. Apply conditional B0b to this same `W` as a conditional theorem and bind
   its exact `e_quot^r,epsilon_B^r`; set
   `e_fix^r<=epsilon_B^r`, `C_fix>=C_grp`, and `r_bidx=r_iso`.
3. For arbitrary exact-unit `epsilon_r<=e_fix^r`, derive from
   `epsilon_r<=epsilon_B^r<=epsilon_*^r` and the displayed minimum formulas
   all graph, polar, path, derivative, and chart-retention guards, including
   `C_der*(epsilon_r+r_iso)<=kappa_der/4<1`. This is scalar arithmetic, not
   an invocation of ledger clause (R).
4. Instantiate the ledger's (A_2),(A_4)--(A_7) with those derived guards,
   feed those same objects to B0b, and bind its complete package.
5. Assume `breve-e` is the only fixed class.
6. Place that singleton fixed set in a maximal simplex.
7. Apply Lefschetz-Hopf and the local index to get
   `Lambda(breve-sigma)=1`.
8. Apply A3 to this same H-space and left inversion.
9. Substitute the traces to obtain the sum of Betti numbers.
10. Use connected degree zero and positive-dimensional orientable top
    cohomology to contradict node 7 and choose `breve-U!=breve-e`.
11. Apply B0b's class-first phase clause, bind `U_0,c,a,U`, and combine
    fixedness with the literal near-adjoint estimate.
12. Use the same-map ambient isolation clauses to get both distance bounds and
    assemble.

### C0. `lem-stage1-fixed-unitary-projection-bridge` — 8 nodes

1. Apply B1 exactly once and bind its one displayed package and fixed lift.
2. Use `sigma(U)=U` and the package's literal near-adjoint estimate.
3. Define `P=(2J+U+U^dagger)/4` and prove Hermiticity.
4. Expand the fixed-term projection defect.
5. Bound it using the line-939 bridge.
6. Show the vanishing alternative for `P` forces `U` into the `-J` ball.
7. Show the vanishing alternative for `J-P` forces `U` into the `J` ball.
8. Exclude both by B1 and forget the package.

### C1. `lem-stage1-rectified-nontrivial-projection` — 6 nodes

1. Read the extended input at amplification level one and apply
   `lem-stage1-rectified-cstar-control`; bind its universal
   `C_rect,e_rect` and its one exact-unit rectification. No `W` is selected.
2. Record every exact-unit axiom, product/unit closeness, and
   `epsilon_r=C_rect*epsilon_X`.
3. Choose
   `e_proj<=min{e_rect,e_bridge^r/C_rect}` and apply C0 exactly once; do not
   apply B1 or the ledger.
4. Transport the fixed-term defect to the original product.
5. Replace `J-P` by `I_X-P` and preserve both nonvanishing alternatives.
6. Take one finite maximum/minimum and assemble.

### C2. `lem-stage1-original-complementary-pair` — 6 nodes

1. Apply C1 once and fix its projection.
2. Set `P'=P_0`, `P''=I_X-P_0`.
3. Retain Hermiticity and nonvanishing.
4. Expand the complement defect.
5. Expand both cross defects.
6. Enlarge/decrease once and assemble.

### C3. `lem-stage1-fresh-two-point-inclusion` — 9 nodes

1. Apply C2 once and fix its pair.
2. Define `v^(2)` and its canonical amplifications.
3. Verify linearity, dagger, basis images, and exact unit.
4. Expand the four basis products at every amplification.
5. Use the simple-tensor identity for uniform nonvanishing.
6. Obtain an amplification-independent crude lower modulus.
7. Invoke `GT-kitaev-prop-delta-hominc` at `:1194-1196`, with `:1192` and
   `:458`.
8. Choose one uniform threshold and coefficient.
9. Apply `def-extended-delta-inclusion` and assemble.

## 5. Definition-layer audit

| definition | use | disposition |
|---|---|---|
| `def-h-space-left-inversion` | A0--A3 and quotient H-space/left inversion | Reuse unchanged. |
| `def-lefschetz-fixed-point-data` | B0i--B1 | Reuse unchanged. |
| `def-epsilon-cstar-algebra` | exact-unit B/C inputs | Reuse unchanged. |
| `def-extended-epsilon-cstar-algebra` | C1--C3 MAIN-facing inputs | Reuse unchanged. |
| `def-stage1-polar-witness-data` | typed fourteen-field `W` only | Reuse unchanged; no analytic fact is read from it. |
| `def-approximate-unitary-space` | `calU`, quotient, charts, and fixed lifts | Reuse unchanged. |
| `def-delta-projection` | C0--C3 projection outputs | Reuse unchanged. |
| `def-extended-delta-inclusion` | C3 | Reuse unchanged. |
| `def-operator-space` | C3 amplifications | Reuse unchanged. |
| `def-projection-basis` | C3 standard basis | Reuse unchanged. |
| `def-compressed-corner` | M19-S1 typing only | Reuse unchanged. |

**Proposed new definitions: none.** The long parameterized antecedents are
result-local hypotheses, not a new `LedgerPackage` definition. Singular
cohomology, graded algebras, associated gradeds, trace, exterior algebras, and
`C^2` remain textbook notions.

## 6. Dimension-freeness audit

| place | audit |
|---|---|
| A0 | Kunneth, edge maps, and finite tensor expansions are qualitative; no stability coefficient depends on a Betti number. |
| A1 | 3C.4 and the explicit grading step are qualitative; finite total dimension excludes polynomial and infinite odd families without introducing a coefficient. |
| A2--A3 | Filtration lengths affect finite sums only. |
| B0a | `W` is fixed before the input algebra; the typed provider witness `e_quot^r` is then bound and `epsilon_B^r=min{epsilon_*^r,e_quot^r}` is a positive minimum of universal fields. All operations are formula-defined. |
| B0i ambient bridge | `Theta_s` has derivative exactly `sI`; Hermitian/anti-Hermitian projections have norm at most one; graph uniqueness is at the universal radius `r_iso`. No basis, determinant magnitude, or dimension enters. |
| B0i index | Determinant positivity is obtained by an invertible homotopy, not a dimension-dependent lower determinant bound. |
| B0s | QIFT is applied in Banach/operator norms and `r_bidx=r_iso`; the ambient capture is already quantitative. |
| B0b | Triangulation size and the circle phase enter no estimate. |
| B1 | The ledger is selected once before the algebraic/topological contradiction; the arbitrary-exact-unit guards are scalar consequences of universal minima, and only two nonzero cohomological degrees are needed. |
| C0 | The line-939 formula has a fixed number of terms and uses the proved universal ambient radius. |
| C1--C3 | W-free rectification, complement, and four basis-product estimates are fixed-term; `:458` excludes dependence on extra data. |
| M19-S1 specialization | M04's universal corner coefficient is absorbed by a finite maximum/minimum; no dimension, amplification, atom count, or block count enters. |

## 7. Exact M19-S1 interface match

The consumer contract at
`docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md:381`
is:

> After G-S1, there are universal `K_1>=1` and `e_call,1>0`, with
> `K_1*e_call,1<=e_1` and all G-S1/old-side prerequisite thresholds absorbed
> into `e_call,1`, such that, if `A` is a finite-dimensional extended
> `epsilon`-C*-algebra, `0<=epsilon<=e_call,1`,
> `w:C^m->A` is a supplied extended `c_0^cb*epsilon`-inclusion including its
> unit clause, and some `P_j=w(e_j)` has `dim S_{P_j}>1`, then the three G-S1
> producers and the literal old-side compression furnish an explicit Stage-1
> raw-call datum satisfying M15 with base scale `t_1=K_1*epsilon`.

M15's literal raw-datum contract is at the same file's line 343.

| M19-S1 / M15 clause | producer-side discharge |
|---|---|
| Selected finite-dimensional extended corner | Future M04 supplies `S_{P_j}` with original compressed product/unit; C1 accepts exactly that type. |
| `dim S_{P_j}>1` | Exactly C1--C3's strict dimension hypothesis. |
| Fresh split | C1 gives the nontrivial original-corner projection; C2 returns its jointly selected complement. |
| Fresh `C^2` inclusion | C3 consumes that same pair and returns one map, exact basis images, and exact unit. |
| Fixed amplification family | C3 uses only `id_{M_n} tensor v^(2)`. |
| Outer targets | They remain M04's `P_[1,m-1]` and `P_j`; C2's pair is internal to the fresh corner. |
| Literal old side | `lem-compcb-single-compression-transfer` supplies it for `m>1`; M15 omits it for `m=1`. |
| Common base scale | M19-S1 chooses `K_1` above the finitely many old-side and `L*C_proj,L*C_np,L*C_pair` coefficients. |
| Thresholds | C0 absorbs the B-chain restriction into `e_bridge^r`; C1 absorbs `e_rect` and `e_bridge^r/C_rect` into `e_proj`; C2/C3 take later finite minima. M19-S1 explicitly allows every G-S1 prerequisite threshold to be absorbed into its universal `e_call,1` (`DESIGN-MAIN-STRUCTURE-v5.md:381`). |

Thus the M19-S1/M15 clause match accepted at
`AUDIT-S1-ENDGAME-v4.md:285-321` survives the restricted receiving threshold.
This design removes only the G-S1 blocker.

## 8. External, binder, dependency, and cascade audits

### Externals

No reference acquisition is required.

1. `GT-hatcher-weak-hopf-conditions`,
   `refs/hatcher-algebraic-topology/AT.txt:17654-17677`, imports exactly
   connectedness and the positive-positive coproduct tail. It imports no
   `Delta(1)` clause.
2. `GT-hatcher-hopf-structure-3C4`,
   `refs/hatcher-algebraic-topology/AT.txt:17798-17800`, imports exactly the
   exterior-tensor-polynomial conclusion **as an algebra**. A1 proves
   polynomial exclusion, finiteness, and grading internally.
3. `GT-kitaev-prop-delta-hominc`,
   `refs/kitaev-2405.02434/approximate_algebras.tex:1194-1196`, retains proof
   `:1198-1222`, smallness context `:1192`, and data-independence `:458`.

The bridge range `:929-943` contains the formula at line 939. No Borel,
Leray--Hirsch, coassociative-bialgebra theorem, or unavailable source is used.

### Binder scan

- A0/A1 bind `M,mu,e,A,A^+,Delta,J_a` before use; A2 binds
  `M,mu,e,sigma,A,A^+,F,E`; A3 binds `M,mu,e,sigma,k`.
- Every conditional B row binds `W` before its fields. B0a binds the
  provider's `e_quot^r` before defining `epsilon_B^r`; every later B row
  receives those same witnesses before the algebra, binds the algebra before
  `calU,J`, every map before its formula is used, `a space breve-calU` before
  its quotient equation, and `set breve-e:=[J]` before H-space/index clauses.
- B0b binds `breve-V` before `U_0,c,a`; B1 binds `breve-U` before
  `U_0,c,a,U`.
- C0's existential projection is typed by its input exact-unit algebra; C1
  binds the W-free provider's `C_rect,e_rect` and rectification before their
  first use; C1--C3 bind their extended algebra, product, unit, projection
  pair, and map before use.

No bare equation is treated as a quantifier. No free symbol remains in the
thirteen proposed contracts.

### Dependency/cascade scan

The graph is

`A0 -> A1 -> A2 -> A3`,
`B0a -> B0i -> B0s -> B0b -> B1 -> C0 -> C1 -> C2 -> C3`,
with `A3 -> B1`, quotient-manifold-provider edges entering B0a and B1 (the
latter is retained but not re-eliminated because it belongs to B1's fixed
ten), the W-free rectification edge entering C1, and the one direct
polar-ledger edge entering B1.

It is acyclic. No proposed row imports a retired parent or a non-T0 row.
No T0 contract, definition, or existing external is amended. The original ten
B1 dependencies remain in their fixed order; the ledger and conditional B0b
remain its additional typed implementation providers. Across all thirteen
`deps:` lists and all thirteen skeletons,
`lem-stage1-polar-constant-ledger` occurs in B1 and nowhere else. The
provenance mentions in conditional rows are citations to the formula source,
not dependency edges or existential eliminations.

## 9. Honest budgets and build granularity

| row | v4 target / rounds / cap | v5 target / rounds / cap | reason |
|---|---:|---:|---|
| A0 `hspace-coproduct-tail` | 10 / 4 / 15 | 10 / 4 / 15 | Unchanged. |
| A1 `exterior-cohomology` | 8 / 3 / 12 | 8 / 3 / 12 | Unchanged; explicit grading remains visible. |
| A2 `associated-graded` | 9 / 3 / 14 | 9 / 3 / 14 | Unchanged; consumes A1's root only. |
| A3 `trace` | 4 / 2 / 8 | 4 / 2 / 8 | Unchanged. |
| B0a `bound-quotient-left-inversion` | 8 / 3 / 12 | 9 / 4 / 13 | Adds one typed `e_quot^r` reception/common-minimum/manifold-export node. |
| B0i `bound-quotient-local-index` | 10 / 4 / 15 | 10 / 4 / 15 | Node 2 now explicitly receives the common threshold and manifold package; the accepted two-node ambient bridge is unchanged. |
| B0s `bound-inversion-isolation` | 7 / 3 / 12 | 7 / 3 / 12 | Unchanged, including `r_bidx=r_iso`. |
| B0b `bound-quotient-index-data` | 5 / 2 / 9 | 5 / 2 / 9 | Node 2 now receives, rather than illegally reapplying, the manifold provider; finite-CW and phase lift remain. |
| B1 `extra-fixed-class` | 11 / 4 / 15 | 12 / 4 / 15 | Adds the explicit arbitrary-exact-unit scalar-arithmetic node while retaining one ledger elimination. |
| C0 `fixed-unitary-projection-bridge` | 8 / 3 / 12 | 8 / 3 / 12 | Unchanged. |
| C1 `rectified-nontrivial-projection` | 6 / 3 / 10 | 6 / 3 / 10 | Same granularity; the first node now uses the W-free T0 provider. |
| C2 `original-complementary-pair` | 6 / 2 / 10 | 6 / 2 / 10 | Unchanged. |
| C3 `fresh-two-point-inclusion` | 9 / 3 / 14 | 9 / 3 / 14 | Unchanged. |

The total target is **103 nodes across 13 rows**. (The thirteen printed v4
targets sum to 101, not the 98 stated in v4's prose.) Maximum target is twelve;
maximum hard cap is fifteen. B0i+B0s+B0b still target 22 nodes, consistent
with the validated quotient-index benchmark (12) plus isolation benchmark
(7); the extra receiving-threshold obligation is priced once in B0a, while
B0i retains the accepted two-node ambient-inradius bridge and B0b explicitly
propagates the provider witness. The topology Hopf-structure benchmark is 13;
no proposed target exceeds 12. A hard-cap hit remains a factoring stop.

## 10. Hostile-verifier risk register

| row | first likely hostile attack | designed response / stop condition |
|---|---|---|
| A0 | Are edge terms and `Delta(1)` derived rather than imported? | Separate nodes; no stronger external. |
| A1 | Does “as an algebra” silently become “graded”? | Two explicit grading nodes after the exact external. |
| A2 | Does it read A0 without a dependency? | Every tail use names A1's root only. |
| A3 | Is the filtration finite and exhaustive? | Establish before trace additivity. |
| B0a | Is `W` still a disguised selection, or is `e_quot^r` assumed comparable? | Universal typed `W` plus physical antecedents; separately eliminate the manifold root, bind `e_quot^r`, and define the explicit minimum. No polar-ledger edge. |
| B0i | Are the provider threshold, (A_7), charts, and `sigma` literally the same objects? | Receive B0a's exact `e_quot^r,epsilon_B^r`, then use the same `W`, unique `Pi` inverse, unique graph functions, and repeated formulas. Stop on any second threshold, inverse, or map. |
| B0i ambient bridge | Does chart openness masquerade as a universal inradius? | Explicit QIFT affine inverse, norm-one splitting, (A_2) uniqueness, and a root inclusion at radius `r_iso`. |
| B0s | Does coordinate injectivity imply ambient isolation? | It first invokes B0i's quantitative inclusion, then QIFT injectivity. |
| B0b | Is finite CW conditional, and is the class bound before its lift? | Received manifold antecedent at the same `epsilon_B^r`; class-first binder. |
| B1 | Is the ledger applied twice, is a different `W` passed, or are arbitrary-exact-unit guards read from (R)? | One ledger node; the same `W` goes to B0b; a separate scalar node derives the guards from the minima before instantiating (A_2),(A_4)--(A_7). |
| C0 | Does either vanishing branch use an unproved radius? | Both use B1's same-map universal `r_bidx`, now proved through B0i/B0s. |
| C1 | Is B1 or the polar ledger selected again, and does the provider accept an extended input? | C1 depends only on C0 plus `lem-stage1-rectified-cstar-control`; `def-extended-epsilon-cstar-algebra` supplies its level-one epsilon_X-C*-algebra antecedent. |
| C2 | Does complementarity survive the original approximate unit? | Explicit fixed-term expansions. |
| C3 | Is the complete lower modulus amplification-dependent? | Crude tensor-uniform modulus before the exact local external; stop if `:458` cannot be registered. |

## 11. Ratification surface and hand-off

User ratification is required for the same 13 contracts as v4. There is **no
new helper id, external id, or definition shard** relative to v4. The material
contract changes are:

1. B0a binds the quotient-manifold provider's existential threshold, defines
   and exports `epsilon_B^r`, and every later B row propagates it unchanged;
2. B0i and B0b remove their direct manifold-root applications while retaining
   their accepted mathematical outputs;
3. B1 explicitly derives the specialized scalar guards and remains the unique
   polar-ledger instantiator; and
4. C1 replaces its polar-ledger dependency with the existing T0 W-free
   rectification provider.

A fresh hostile audit should attack these three repaired interfaces first,
then re-run the already-clean source, status, ambient-bridge, M19, and hand-off
scans. If all rows
later validate, the trace chain, bound extra fixed class, and three G-S1
producers exist. MAIN remains gated on P0 and M01--M18; this design makes no
claim about M19-S1--M28, `lem-thmainext-conditional`, or `op-classical`.
