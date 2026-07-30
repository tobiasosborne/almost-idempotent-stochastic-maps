# DESIGN-S1-ENDGAME-v3 — Stage-1 endgame repair round 2

Date: 2026-07-30
Role: fresh independent design mathematician
Status: **DESIGN ONLY; NON-RIGOROUS; DO NOT LAND, SEED, OR PROMOTE before a fresh hostile audit and user ratification**

## 0. Executive disposition of audit-v2 findings

This is a self-contained replacement for `DESIGN-S1-ENDGAME-v2.md`. It keeps
the mathematical content and interfaces not attacked by
`AUDIT-S1-ENDGAME-v2.md` and repairs every finding F1--F8.

| finding | disposition |
|---|---|
| **F1** | **FIXED.** Final B0b directly imports `lem-stage1-quotient-manifold-package`, whose root supplies connectedness, compactness, orientability, smoothness, boundarylessness, and dimension (`argument/lemmas/lem-stage1-quotient-manifold-package.md:4`). B0b then discharges the exact compact-smooth-boundaryless antecedent of `lem-stage1-quotient-finite-cw` (`argument/lemmas/lem-stage1-quotient-finite-cw.md:4`). The factored B0i also directly imports the manifold package before applying the compact-orientable-manifold local-index root (`argument/lemmas/lem-topology-local-index-sign.md:4`). This addresses the missing-root analysis at `AUDIT-S1-ENDGAME-v2.md:105-138`. |
| **F2** | **FIXED.** B0b's root existentially binds one displayed `W,(u_delta,h_delta),mu,sigma,breve-calU,breve-mu,breve-sigma` and explicitly re-exports the formulas for the maps, their scalar covariance, and `||sigma(V)-V^dagger|| <= C_grp*epsilon_r` for every `V`; B1 repeats and consumes those clauses. No property is read from a dependency body or dependency closure (`AUDIT-S1-ENDGAME-v2.md:140-164`). |
| **F3** | **FIXED.** B0b binds universal `r_bidx>0` in its leading existential. B1 binds the same carried witness in its own leading existential and uses it in both distance inequalities. There is no free `r_bidx` (`AUDIT-S1-ENDGAME-v2.md:166-179`). |
| **F4** | **FIXED.** B0i, B0s, B0b, and B1 each quantify one complete displayed package before stating its conjuncts. B0b's phase clause first quantifies a fixed class `breve-V`, then binds `U_0,c,a` and asserts `[U_0]=breve-V`. C0 contains no package anaphor, and no proposed consumer contract uses a non-unique provider by definite description (`AUDIT-S1-ENDGAME-v2.md:181-196`). |
| **F5** | **FIXED by architecture (b).** C0 applies B1 exactly once internally and exports only the resulting nontrivial projection. C1 has no B1 dependency and applies C0 exactly once to its one rectified exact-unit algebra. The bridge formula is proved inside C0 from `approximate_algebras.tex:929-943`, which contains the formula and estimate at line 939 (`AUDIT-S1-ENDGAME-v2.md:198-217`). |
| **F6** | **FIXED.** The two Hatcher externals below are restricted to the exact printed connectedness/positive-tail conditions and the exact exterior-tensor-polynomial theorem. `Delta(1)=1 tensor 1`, polynomial-factor exclusion, and finiteness of the odd generator family remain internal A0/A1 obligations (`AUDIT-S1-ENDGAME-v2.md:219-232`). |
| **F7** | **FIXED.** A0 explicitly works over `reals` and binds a finite tail family indexed by a finite set `J_a`; A1 contractually re-exports that finite-family clause, and A1--A3 write `reals` rather than an unexplained `R` (`AUDIT-S1-ENDGAME-v2.md:234-244`). |
| **F8** | **FIXED by factoring.** The former A1 becomes A0+A1 with targets 10 and 7. The former B0b becomes B0i+B0s+B0b with targets 8, 7, and 5. Each verifier-visible obligation has its own node and every row targets at most ten nodes (`AUDIT-S1-ENDGAME-v2.md:246-271`). |

The repaired design has **13 rows**: the original seven requested ids, the
three v2 helpers, and three new v3 helpers. Relative to v2 it adds exactly
`lem-stage1-hspace-coproduct-tail`,
`lem-stage1-bound-quotient-local-index`, and
`lem-stage1-bound-inversion-isolation`. It adds no definition shard, no
reference acquisition, and no new external id. All direct dependencies are T0
or earlier in the serial order.

## 1. Registry-ready row tables

Every `contract:` value below is one physical source line, flattened registry
ASCII, and assigns no numerical value to an existential universal constant.
The long B contracts deliberately repeat fields and predicates: no unnamed
provider package is part of the logical interface.

### Block A — coproduct construction and trace rows

| proposed id | one-line `contract:` value | defs | exact `deps:` | provenance loci | target / rounds / hard cap | feasibility |
|---|---|---|---|---|---|---|
| **NEW in v3** `lem-stage1-hspace-coproduct-tail` | H-space coproduct-tail package over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity and (M,mu,e) is an H-space, set A=H^*(M;reals), A^+=direct_sum_{k>0} A^k, and Delta=(cross product)^(-1) o mu^*; then A is a finite-dimensional graded-commutative associative unital algebra with A^0=reals*1, Delta:A->A tensor_reals A is a degree-preserving unital algebra homomorphism with Delta(1)=1 tensor 1, and for every homogeneous a in A^+ there exist a finite set J_a and homogeneous a'_j,a''_j in A^+ for j in J_a such that Delta(a)=a tensor 1+1 tensor a+sum_{j in J_a} a'_j tensor a''_j. | `def-h-space-left-inversion` | `lem-topology-kunneth-cross-product` | construction `refs/hatcher-algebraic-topology/AT.txt:17620-17652`; printed conditions `:17654-17677`; guide `refs/kitaev-2405.02434/approximate_algebras.tex:975-1016` | 10 / 4 / 15 | **SUPPORTED-WITH-DERIVATION.** This row constructs the non-coassociative coproduct and its two edge terms; it does not invoke Hopf's structure theorem. |
| `lem-stage1-exterior-cohomology` | Exterior cohomology of a finite H-space over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity and (M,mu,e) is an H-space, set A=H^*(M;reals), A^+=direct_sum_{k>0} A^k, and Delta=(cross product)^(-1) o mu^*; then A is a finite-dimensional graded-commutative associative unital algebra with A^0=reals*1, Delta:A->A tensor_reals A is a degree-preserving unital algebra homomorphism with Delta(1)=1 tensor 1, for every homogeneous a in A^+ there exist a finite set J_a and homogeneous a'_j,a''_j in A^+ for j in J_a such that Delta(a)=a tensor 1+1 tensor a+sum_{j in J_a} a'_j tensor a''_j, and A is isomorphic as a graded algebra to an exterior algebra on a finite family of odd-positive-degree homogeneous generators. | `def-h-space-left-inversion` | `lem-stage1-hspace-coproduct-tail` | exact printed conditions `refs/hatcher-algebraic-topology/AT.txt:17654-17677`; exact Theorem 3C.4 `:17798-17800`; finite-total-dimensional corollary guide `refs/kitaev-2405.02434/approximate_algebras.tex:1000-1022` | 7 / 3 / 11 | **SUPPORTED-WITH-DIRECT-LOCAL-EXTERNALS.** The row re-exports A0's explicit finite-tail package, applies the exact exterior-tensor-polynomial theorem, and separately removes polynomial generators and proves the odd generator family finite. |
| `lem-stage1-left-inversion-associated-graded` | Associated-graded action of a left inversion over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity, (M,mu,e) is an H-space, and sigma:M->M is a left inversion, set A=H^*(M;reals), A^+=direct_sum_{k>0} A^k, F^{p,q}=(A^+)^p intersect A^{p+q}, and E^{p,q}=F^{p,q}/F^{p+1,q-1}; then sigma^* preserves every F^{p,q} and induces (-1)^(p+q)*id on every E^{p,q} for p >= 0 and p+q >= 0. | `def-h-space-left-inversion` | `lem-stage1-exterior-cohomology` | `refs/kitaev-2405.02434/approximate_algebras.tex:1016-1049` | 9 / 3 / 14 | **SUPPORTED-WITH-DERIVATION.** A1's root supplies both the finite positive-positive coproduct tail and the finite odd exterior basis. |
| `lem-stage1-left-inversion-trace` | Left-inversion trace over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity, (M,mu,e) is an H-space, and sigma:M->M is a left inversion, then Tr(sigma^{*k}:H^k(M;reals)->H^k(M;reals))=(-1)^k*dim_reals H^k(M;reals) for every k >= 0. | `def-h-space-left-inversion` | `lem-stage1-left-inversion-associated-graded` | `refs/kitaev-2405.02434/approximate_algebras.tex:971-972,1023-1050` | 4 / 2 / 8 | **SUPPORTED-WITH-DERIVATION.** The filtration is finite in every degree because total cohomology is finite-dimensional. |

### Block B — one bound quotient package and the extra fixed class

The new B0i/B0s split assigns quotient differential/index work and actual
fixed-point isolation to separate rows. B0b is then a small final attachment:
it imports the manifold root directly, applies finite triangulation under its
literal antecedent, performs the global square-root phase lift, and exports the
single package B1 needs.

| proposed id | one-line `contract:` value | defs | exact `deps:` | provenance loci | target / rounds / hard cap | feasibility |
|---|---|---|---|---|---|---|
| `lem-stage1-bound-quotient-left-inversion` | Bound quotient H-space package: there is a universal e_bind^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_bind^r and 1 < N=dim_C calX < infinity, writing W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso) for one tuple supplied by lem-stage1-polar-constant-ledger, writing (u_delta,h_delta) for the unique inverse of Pi_delta:calU x B_delta^{calH}(J)->S_delta:=Pi_delta(calU x B_delta^{calH}(J)), Pi_delta(U,H)=U bold-dot H, at delta=delta_*, defining mu(U,V)=u_delta(U bold-dot V), sigma(U)=u_delta(U^dagger), breve-calU=calU_e/U(1), breve-mu([U],[V])=[mu(U,V)], and breve-sigma([U])=[sigma(U)], these same displayed maps make (breve-calU,breve-mu,[J]) a connected H-space and make the smooth breve-sigma a left inversion; moreover sigma(J)=J, sigma(cU)=conj(c)*sigma(U), and ||sigma(U)-U^dagger|| <= C_grp*epsilon_r for every c in U(1) and U in calU. | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `def-h-space-left-inversion` | `lem-stage1-polar-constant-ledger`; `lem-stage1-smooth-unitary-atlas`; `lem-stage1-smooth-polar-inverse`; `lem-stage1-explicit-smooth-unitary-operations`; `lem-stage1-quotient-manifold-package`; `lem-topology-quotient-manifold` | row 13 clauses (A_2),(A_4)-(A_6),(R) `argument/lemmas/lem-stage1-polar-constant-ledger.md:4`; `refs/kitaev-2405.02434/approximate_algebras.tex:895-912,945-955` | 8 / 3 / 12 | **SUPPORTED-WITH-RECONSTRUCTION.** Retained from v2, with `sigma(J)=J` made explicit for the factored actual-isolation consumer. The row-13 tuple is bound first and the polar inverse is uniquely determined by its displayed map. |
| **NEW in v3** `lem-stage1-bound-quotient-local-index` | Bound same-map quotient local-index package: there is a universal e_blidx^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_blidx^r and 1 < N=dim_C calX < infinity, there exist W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso), maps u_delta,h_delta,mu,sigma,breve-mu,breve-sigma, and for each s in {+1,-1} a C^1 chart chi_s:B_{r_iso}^{icalH}(0)->calU, an inverse coordinate map psi_s:chi_s(B_{r_iso}^{icalH}(0))->B_{r_iso}^{icalH}(0), and a C^1 map F_s:B_{r_iso}^{icalH}(0)->B_{r_iso}^{icalH}(0) such that Pi_delta:calU x B_delta^{calH}(J)->S_delta, Pi_delta(U,H)=U bold-dot H, at delta=delta_* has unique inverse (u_delta,h_delta), mu(U,V)=u_delta(U bold-dot V), sigma(U)=u_delta(U^dagger), breve-calU=calU_e/U(1), breve-mu([U],[V])=[mu(U,V)], breve-sigma([U])=[sigma(U)], (breve-calU,breve-mu,[J]) is a connected H-space, breve-sigma is a smooth left inversion, sigma(J)=J, sigma(cU)=conj(c)*sigma(U), ||sigma(U)-U^dagger|| <= C_grp*epsilon_r for every c in U(1) and U in calU, breve-calU is a connected compact orientable smooth manifold without boundary of real dimension N-1, chi_s(0)=sJ, psi_s o chi_s=id, sigma(chi_s(B_{r_iso}^{icalH}(0))) is contained in chi_s(B_{r_iso}^{icalH}(0)), F_s=psi_s o sigma o chi_s, and ||D(F_s-id)(A)+2*I|| < 1 for every A in B_{r_iso}^{icalH}(0); for these same maps, breve-e=[J] is an isolated fixed point of breve-sigma, i*reals*J is D-sigma_J-invariant, ||D-breve-sigma_{breve-e}+I|| < 1 in the quotient norm, det(I-D-breve-sigma_{breve-e})>0, and the local index of breve-e is +1. | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `def-h-space-left-inversion`; `def-lefschetz-fixed-point-data` | `lem-stage1-bound-quotient-left-inversion`; `lem-stage1-polar-constant-ledger`; `lem-stage1-smooth-unitary-atlas`; `lem-stage1-smooth-polar-inverse`; `lem-stage1-explicit-smooth-unitary-operations`; `lem-stage1-quotient-manifold-package`; `lem-stage1-quantitative-inverse-function`; `lem-topology-local-index-sign` | row 13 clauses (A_5),(A_7),(R) `argument/lemmas/lem-stage1-polar-constant-ledger.md:4`; quotient/index argument `refs/kitaev-2405.02434/approximate_algebras.tex:947-968` | 8 / 3 / 13 | **SUPPORTED-WITH-FACTORED-DERIVATION.** The manifold package directly supplies compactness and orientability before the local-index theorem is invoked. The row exports the actual chart maps needed by B0s, not an anaphoric `sigma`. |
| **NEW in v3** `lem-stage1-bound-inversion-isolation` | Bound same-map actual-isolation package: there are universal e_biso^r > 0 and r_bidx > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_biso^r and 1 < N=dim_C calX < infinity, there exist W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso), maps u_delta,h_delta,mu,sigma,breve-mu,breve-sigma, and a space breve-calU such that Pi_delta:calU x B_delta^{calH}(J)->S_delta, Pi_delta(U,H)=U bold-dot H, at delta=delta_* has unique inverse (u_delta,h_delta), mu(U,V)=u_delta(U bold-dot V), sigma(U)=u_delta(U^dagger), breve-calU=calU_e/U(1), breve-mu([U],[V])=[mu(U,V)], breve-sigma([U])=[sigma(U)], (breve-calU,breve-mu,[J]) is a connected H-space, breve-sigma is a smooth left inversion, sigma(J)=J, sigma(cU)=conj(c)*sigma(U), ||sigma(U)-U^dagger|| <= C_grp*epsilon_r for every c in U(1) and U in calU, breve-calU is a connected compact orientable smooth manifold without boundary of real dimension N-1, breve-e=[J] is an isolated fixed point of breve-sigma with local index +1, and J and -J are the only sigma-fixed points in their respective ambient r_bidx-balls. | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `def-h-space-left-inversion`; `def-lefschetz-fixed-point-data` | `lem-stage1-bound-quotient-local-index`; `lem-stage1-quantitative-inverse-function` | same-map chart control from B0i; isolation mechanism `refs/kitaev-2405.02434/approximate_algebras.tex:929-943,947-955` | 7 / 3 / 12 | **SUPPORTED-WITH-FACTORED-DERIVATION.** It applies QIFT separately in the two B0i-exported charts and then forgets the chart auxiliaries while retaining the same displayed `sigma` and the universal radius. |
| `lem-stage1-bound-quotient-index-data` | Bound complete quotient package: there are universal e_bidx^r > 0 and r_bidx > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_bidx^r and 1 < N=dim_C calX < infinity, there exist W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso), maps u_delta,h_delta,mu,sigma,breve-mu,breve-sigma, and a space breve-calU such that Pi_delta:calU x B_delta^{calH}(J)->S_delta, Pi_delta(U,H)=U bold-dot H, at delta=delta_* has unique inverse (u_delta,h_delta), mu(U,V)=u_delta(U bold-dot V), sigma(U)=u_delta(U^dagger), breve-calU=calU_e/U(1), breve-mu([U],[V])=[mu(U,V)], breve-sigma([U])=[sigma(U)], (breve-calU,breve-mu,[J]) is a connected H-space, breve-sigma is a smooth left inversion, sigma(J)=J, sigma(cU)=conj(c)*sigma(U), ||sigma(U)-U^dagger|| <= C_grp*epsilon_r for every c in U(1) and U in calU, breve-calU is a connected compact orientable smooth manifold without boundary of real dimension N-1 and is homeomorphic to a finite simplicial complex, breve-e=[J] is an isolated fixed point of breve-sigma with local index +1, J and -J are the only sigma-fixed points in their respective ambient r_bidx-balls, and for every breve-sigma-fixed class breve-V there exist U_0 in calU_e and c,a in U(1) such that [U_0]=breve-V, sigma(U_0)=c*U_0, a^2=c, sigma(a*U_0)=a*U_0, and sigma(-a*U_0)=-a*U_0. | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `def-h-space-left-inversion`; `def-lefschetz-fixed-point-data` | `lem-stage1-bound-inversion-isolation`; `lem-stage1-quotient-manifold-package`; `lem-stage1-quotient-finite-cw` | manifold root `argument/lemmas/lem-stage1-quotient-manifold-package.md:4`; finite-CW conditional root `argument/lemmas/lem-stage1-quotient-finite-cw.md:4`; phase lift `refs/kitaev-2405.02434/approximate_algebras.tex:939-955` | 5 / 2 / 9 | **SUPPORTED-WITH-DIRECT-ANTECEDENTS.** The manifold dependency is direct. Its compact/smooth/boundaryless conclusion is fed clause-by-clause to the finite-CW root. The class binder precedes its representative and phase witnesses. |
| `lem-stage1-extra-fixed-class` | Bound extra fixed class: there are universal C_fix < infinity, e_fix^r > 0, and r_bidx > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_fix^r and 1 < N=dim_C calX < infinity, there exist W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso), maps u_delta,h_delta,mu,sigma,breve-mu,breve-sigma, a space breve-calU, a breve-sigma-fixed class breve-U, a representative U_0 in calU_e, phases c,a in U(1), and U in calU_e such that Pi_delta:calU x B_delta^{calH}(J)->S_delta, Pi_delta(V,H)=V bold-dot H, at delta=delta_* has unique inverse (u_delta,h_delta), mu(V_1,V_2)=u_delta(V_1 bold-dot V_2), sigma(V)=u_delta(V^dagger), breve-calU=calU_e/U(1), breve-mu([V_1],[V_2])=[mu(V_1,V_2)], breve-sigma([V])=[sigma(V)], (breve-calU,breve-mu,[J]) is a connected H-space, breve-sigma is a smooth left inversion, sigma(c_0*V)=conj(c_0)*sigma(V) and ||sigma(V)-V^dagger|| <= C_grp*epsilon_r for every c_0 in U(1) and V in calU, breve-calU is a connected compact orientable smooth manifold without boundary of real dimension N-1 and is homeomorphic to a finite simplicial complex, breve-e=[J] is an isolated fixed point of breve-sigma with local index +1, J and -J are the only sigma-fixed points in their respective ambient r_bidx-balls, breve-U != breve-e, [U_0]=breve-U, sigma(U_0)=c*U_0, a^2=c, U=a*U_0, [U]=breve-U, sigma(U)=U, ||U-U^dagger|| <= C_fix*epsilon_r, ||U-J|| >= r_bidx, and ||U+J|| >= r_bidx. | `def-epsilon-cstar-algebra`; `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-h-space-left-inversion`; `def-lefschetz-fixed-point-data` | `lem-stage1-uniform-inversion-isolation`; `lem-stage1-quotient-manifold-package`; `lem-stage1-quotient-finite-cw`; `lem-stage1-quotient-left-inversion`; `lem-stage1-left-inversion-trace`; `lem-topology-lefschetz-hopf`; `lem-topology-local-index-sign`; `lem-topology-orientable-top-cohomology`; `lem-stage1-quotient-inversion-index-data`; `lem-finite-polyhedron-maximal-simplex-placement`; `lem-stage1-bound-quotient-index-data` | `refs/kitaev-2405.02434/approximate_algebras.tex:945-969`; trace `:971-1050`; fixed ten-item ledger `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v6.md:234-263` | 10 / 3 / 15 | **SUPPORTED-WITH-ONE-EXPLICIT-PACKAGE.** The original ten dependencies remain in their fixed order; the final bound-package row is the eleventh typed provider. The same root-bound `r_bidx` occurs in both distance conclusions. |

#### Clause-by-clause antecedent check for F1

1. `lem-stage1-quotient-manifold-package` concludes that the canonical
   `breve-calU=calU_e/U(1)` is connected, compact, orientable, smooth,
   boundaryless, and of dimension `N-1`.
2. B0i imports that root directly. Its `breve-sigma` is smooth by the
   explicitly displayed descent package. Compactness and orientability therefore
   discharge the ambient-manifold clauses of
   `lem-topology-local-index-sign`; B0i separately proves fixedness, isolation,
   and `det(I-D-breve-sigma)>0`.
3. Final B0b also imports the manifold root directly. Compactness, smoothness,
   and boundarylessness exactly discharge the antecedent of
   `lem-stage1-quotient-finite-cw`.
4. The finite-CW root returns a homeomorphism to a finite simplicial complex;
   B0b records that conclusion for the same canonical quotient. No dependency
   closure is read in any of these steps.

### Block C — one-use projection bridge and the three G-S1 producers

This adopts audit-v2 architecture **(b)**. C0 is an exact-unit theorem that
applies B1 once internally and forgets all non-unique fixed-point witnesses
after constructing its projection. C1 selects one row-13 rectification and
applies only C0 to it.

| proposed id | one-line `contract:` value | defs | exact `deps:` | provenance loci | target / rounds / hard cap | feasibility |
|---|---|---|---|---|---|---|
| `lem-stage1-fixed-unitary-projection-bridge` | Fixed-unitary projection bridge: there are universal C_bridge < infinity and e_bridge^r > 0 such that every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_bridge^r and 1 < dim_C calX < infinity contains a nontrivial C_bridge*epsilon_r-projection P for the product bold-dot and unit J. | `def-epsilon-cstar-algebra`; `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-delta-projection` | `lem-stage1-extra-fixed-class` | `refs/kitaev-2405.02434/approximate_algebras.tex:917-943`, with `P=(2J+U+U^dagger)/4` and the `O(delta+epsilon)` conclusion at `:939` | 8 / 3 / 12 | **SUPPORTED-WITH-ONE B1 APPLICATION.** C0 performs existential elimination once, constructs the displayed `P`, proves its defect and both nonvanishing alternatives, and exports only `P`. |
| `lem-stage1-rectified-nontrivial-projection` | There are universal C_proj < infinity and e_proj > 0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0 <= epsilon_X <= e_proj and 1 < dim_C calX < infinity contains a nontrivial C_proj*epsilon_X-projection P_0 for the original product and original unit I_X. | `def-extended-epsilon-cstar-algebra`; `def-epsilon-cstar-algebra`; `def-stage1-polar-witness-data`; `def-delta-projection` | `lem-stage1-polar-constant-ledger`; `lem-stage1-fixed-unitary-projection-bridge` | `refs/kitaev-2405.02434/approximate_algebras.tex:917-945`; rectification `argument/lemmas/lem-stage1-polar-constant-ledger.md:4` clause (A_1) | 6 / 3 / 10 | **SUPPORTED-WITH-SINGLE-CONSTRUCTION TRANSPORT.** C1 fixes one rectification, applies C0 once, and transports that projection to the original product/unit. It does not apply B1. |
| `lem-stage1-original-complementary-pair` | There are universal C_np < infinity and e_np > 0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0 <= epsilon_X <= e_np and 1 < dim_C calX < infinity contains nonvanishing C_np*epsilon_X-projections P' and P'' for the original product such that P'+P''=I_X and ||P'P''||,||P''P'|| <= C_np*epsilon_X. | `def-extended-epsilon-cstar-algebra`; `def-delta-projection` | `lem-stage1-rectified-nontrivial-projection` | `refs/kitaev-2405.02434/approximate_algebras.tex:917-929,1419-1424` | 6 / 2 / 10 | **SUPPORTED-WITH-DERIVATION.** The pair is selected once and returned together. |
| `lem-stage1-fresh-two-point-inclusion` | There are universal C_pair < infinity and e_pair > 0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0 <= epsilon_X <= e_pair and 1 < dim_C calX < infinity contains nonvanishing C_pair*epsilon_X-projections P',P'' with P'+P''=I_X for which the linear map v^(2):C^2->calX, v^(2)(lambda,mu)=lambda*P'+mu*P'', is an extended C_pair*epsilon_X-inclusion, satisfies v^(2)(1,1)=I_X, and sends the standard projection basis Pi',Pi'' to P',P''. | `def-extended-epsilon-cstar-algebra`; `def-delta-projection`; `def-extended-delta-inclusion`; `def-operator-space`; `def-projection-basis` | `lem-stage1-original-complementary-pair` | `refs/kitaev-2405.02434/approximate_algebras.tex:458,1192-1222,1419-1424`; direct external `:1194-1196`, proof `:1198-1222` | 9 / 3 / 14 | **SUPPORTED-WITH-DERIVATION AND ONE LOCAL CITED EXTERNAL.** The repaired line-458 universality provenance is retained. |

## 2. Serial landing and elevation order

The following is a topological order. Every proposed dependency occurs earlier,
and every existing dependency is T0:

1. `lem-stage1-hspace-coproduct-tail` **(new v3 helper)**;
2. `lem-stage1-exterior-cohomology`;
3. `lem-stage1-left-inversion-associated-graded`;
4. `lem-stage1-left-inversion-trace`;
5. `lem-stage1-bound-quotient-left-inversion`;
6. `lem-stage1-bound-quotient-local-index` **(new v3 helper)**;
7. `lem-stage1-bound-inversion-isolation` **(new v3 helper)**;
8. `lem-stage1-bound-quotient-index-data`;
9. `lem-stage1-extra-fixed-class`;
10. `lem-stage1-fixed-unitary-projection-bridge`;
11. `lem-stage1-rectified-nontrivial-projection`;
12. `lem-stage1-original-complementary-pair`;
13. `lem-stage1-fresh-two-point-inclusion`.

Each row lands only after hostile audit and user ratification and is elevated
only after every dependency is available. Use a fresh routine-tier prover and
a separate fresh hostile verifier per row.

After row 13, only the **G-S1 gate** is discharged. MAIN still requires the P0
definition gate and M01--M18, including M04
`lem-maincb-direct-corner-envelope`, in the order at
`DESIGN-MAIN-STRUCTURE-v5.md:512-538`. Nothing here makes M19-S1--M28
immediately eligible.

## 3. Per-row af proof skeletons

Each numbered item is one intended af node, including assembly. Fixed-term
estimates remain inside their assigned node. A hard-cap hit is a factoring
stop, not permission to conceal multiple obligations in one node.

### A0. `lem-stage1-hspace-coproduct-tail` — 10 nodes

1. Fix `M,mu,e`; set `A=H^*(M;reals)` and record finite total dimension,
   graded commutativity, associativity, unitality, and `A^0=reals*1`.
2. Verify the finitely-generated-free hypotheses of the Kunneth root for
   `M x M`.
3. Define `Delta=(cross product)^(-1) o mu^*`.
4. Use naturality of cup product and the ring Kunneth isomorphism to prove that
   `Delta` is degree-preserving and multiplicative.
5. Prove separately that the two unital ring maps give
   `Delta(1)=1 tensor 1`; do not attribute this clause to Hatcher's printed
   condition (1).
6. Use the right-unit H-space homotopy to identify the
   `A^k tensor A^0` component of `Delta(a)` as `a tensor 1`.
7. Use the left-unit homotopy to identify the
   `A^0 tensor A^k` component as `1 tensor a`.
8. Decompose the remaining degree-`k` component into positive-positive
   bidegrees.
9. Choose a finite tensor expansion in the finite-dimensional homogeneous
   summands, explicitly binding the finite set `J_a` and every tail factor.
10. Assemble the exact A0 root without coassociativity, counit, antipode, or
    homotopy associativity.

### A1. `lem-stage1-exterior-cohomology` — 7 nodes

1. Apply A0 and match only its connectedness and positive-positive tail clauses
   to `GT-hatcher-weak-hopf-conditions`.
2. Check the exact hypotheses of `GT-hatcher-hopf-structure-3C4`: real
   characteristic zero, commutative associative multiplication, and
   finite-dimensional graded pieces.
3. Obtain the printed tensor product of an exterior algebra on odd generators
   and a polynomial algebra on even generators.
4. Show that one nontrivial polynomial generator would already force infinite
   total dimension.
5. Remove the polynomial factor.
6. Show that infinitely many odd generators would give infinitely many
   linearly independent positive-degree elements, so the odd generator family
   is finite.
7. Re-export A0's explicit finite-tail package and assemble the finite odd
   exterior-algebra conclusion.

### A2. `lem-stage1-left-inversion-associated-graded` — 9 nodes

1. Fix the H-space and left inversion; apply A1 once and fix its finite
   coproduct-tail package and one finite odd exterior-generator system.
2. Degree and multiplicativity of `sigma^*` preserve `A^+`, every
   `(A^+)^p`, and every `F^{p,q}`.
3. Translate the first basepoint-preserving left-inversion homotopy into
   `cup o (sigma^* tensor id) o Delta = unit o augmentation`.
4. Insert A0's finite positive-positive coproduct formula.
5. For each exterior generator `x`, derive
   `sigma^*(x)=-x mod (A^+)^2`.
6. By multiplicativity obtain `(-1)^p` modulo `(A^+)^{p+1}` on every
   length-`p` exterior monomial.
7. Odd generator degrees make word length congruent to total degree modulo two.
8. Those monomials form a basis of each `E^{p,q}`.
9. Assemble preservation and the action `(-1)^(p+q)*id`.

### A3. `lem-stage1-left-inversion-trace` — 4 nodes

1. For fixed `k`, record the finite exhaustive filtration of `A^k`.
2. Apply finite-dimensional trace additivity to the associated graded.
3. Apply A2 and sum the quotient dimensions.
4. Assemble the trace identity for every `k`.

### B0a. `lem-stage1-bound-quotient-left-inversion` — 8 nodes

1. Fix one row-13 tuple `W`, decrease one receiving threshold, and set
   `delta=delta_*`.
2. Bind `(u_delta,h_delta)` as the unique inverse of the displayed
   `Pi_delta`; no second polar inverse is introduced.
3. Supply the same graph/atlas/inverse objects to
   `lem-stage1-explicit-smooth-unitary-operations`.
4. Obtain the exact displayed formulas, `sigma(J)=J`, scalar covariance, and
   the near-adjoint estimate for this `sigma`.
5. Define `breve-calU`, `breve-mu`, and `breve-sigma` by the displayed orbit
   formulas and prove representative independence.
6. Attach smoothness through the canonical quotient's local sections.
7. Use the row-13 group/path clauses to prove connected H-space unit laws and
   the left-inversion homotopy for this `breve-sigma`.
8. Assemble the explicitly displayed B0a package.

### B0i. `lem-stage1-bound-quotient-local-index` — 8 nodes

1. Apply B0a once, existentially bind its single displayed package, decrease
   the threshold, and keep those exact objects.
2. Apply the quotient-manifold root directly to the canonical
   `breve-calU`; record compactness, orientability, smoothness,
   boundarylessness, and dimension.
3. Instantiate row-13 (A_7) for the package's `W,u_delta,sigma`; expose the
   two graph charts and their coordinate maps without selecting another
   inversion.
4. Differentiate scalar covariance to identify the invariant vertical line and
   descend the same derivative to the quotient tangent.
5. Prove the quotient norm bound and positive determinant by the fixed Neumann
   homotopy.
6. Apply QIFT in a quotient slice to prove that `[J]` is isolated for this
   `breve-sigma`.
7. Check smoothness, compactness, orientability, isolation, and determinant
   clauses one-by-one and apply `lem-topology-local-index-sign`.
8. Re-export the one package, the two explicit chart controls, and local index
   `+1`.

### B0s. `lem-stage1-bound-inversion-isolation` — 7 nodes

1. Apply B0i once and existentially bind its one package and two displayed
   chart maps.
2. Apply QIFT to `F_+-id`, using the B0i derivative bound against `-2I`.
3. Translate chart injectivity back to `calU` and obtain the `+J` actual
   fixed-point ball.
4. Apply the same argument to `F_--id`; use only the already displayed
   sign chart and the same `sigma`.
5. Translate back and obtain the `-J` actual fixed-point ball.
6. Choose one positive universal `r_bidx` below both chart radii and absorb all
   receiving thresholds.
7. Re-export the exact B0i package, local index, and both actual-isolation
   clauses with this bound radius.

### B0b. `lem-stage1-bound-quotient-index-data` — 5 nodes

1. Apply B0s once and existentially bind its package and `r_bidx`; no map,
   inverse, or radius is reselected.
2. Apply `lem-stage1-quotient-manifold-package` directly and match its
   canonical quotient to the package's displayed
   `breve-calU=calU_e/U(1)`.
3. Feed compactness, smoothness, and boundarylessness into
   `lem-stage1-quotient-finite-cw` and record one finite simplicial-complex
   model.
4. For every fixed class `breve-V`, first choose a representative `U_0` and
   phase `c` with `[U_0]=breve-V`; then choose `a` with `a^2=c` and use the
   displayed covariance to prove the two actual fixed lifts.
5. Assemble and explicitly re-export every field B1 consumes: map formulas,
   covariance, near-adjoint estimate, H-space/left inversion, manifold/CW,
   local index, radius/isolation, and phase lift.

### B1. `lem-stage1-extra-fixed-class` — 10 nodes

1. Apply B0b once, existentially bind its complete displayed package including
   `r_bidx`, and take the finite minimum with the original ten dependency
   thresholds without replacing any object.
2. Assume for contradiction that `breve-e=[J]` is the only fixed class of the
   bound `breve-sigma`.
3. The fixed set is the singleton `{breve-e}`; use the finite-polyhedron
   placement row to put it in a maximal simplex.
4. Apply Lefschetz-Hopf and the bound local index to obtain
   `Lambda(breve-sigma)=1`.
5. Apply A3 to this same H-space and same left inversion.
6. Substitute the traces into the definition of the Lefschetz number and
   obtain the sum of Betti numbers.
7. Connectedness supplies degree zero; orientable top cohomology and
   `N-1>0` supply a second nonzero degree, so the sum is at least two.
8. Contradict node 4 and choose `breve-U != [J]`.
9. Apply B0b's globally quantified phase clause to this class, binding
   `U_0,c,a,U`; fixedness and B0b's explicit near-adjoint estimate give the
   near-Hermitian bound.
10. The actual fixed lift is neither `J` nor `-J`; the two bound isolation
    clauses yield both inequalities with the same `r_bidx`, and the complete
    B1 conclusion is assembled.

### C0. `lem-stage1-fixed-unitary-projection-bridge` — 8 nodes

1. Apply B1 exactly once and existentially bind its one displayed package and
   actual fixed lift `U`; no witness is selected elsewhere in C0.
2. Use `sigma(U)=U` and the package's explicit near-adjoint estimate.
3. Define `P=(2J+U+U^dagger)/4` and prove `P^dagger=P`.
4. Expand `P bold-dot P-P` using a fixed number of terms, the exact unitary
   equation, the exact unit, and the epsilon-C* axioms.
5. Bound the expansion by a universal multiple of `epsilon_r`, exactly the
   `O(delta+epsilon)` bridge whose source formula is at TeX line 939.
6. If `P` is in the vanishing alternative, the formula and near-Hermitian
   estimate place `U` inside the bound `-J` isolation ball.
7. If `J-P` is in the vanishing alternative, the same fixed-term argument
   places `U` inside the bound `J` isolation ball.
8. B1's two distance inequalities exclude both branches; assemble the
   nontrivial projection and forget the non-unique B1 package.

### C1. `lem-stage1-rectified-nontrivial-projection` — 6 nodes

1. Fix one row-13 tuple and its single (A_1) rectification
   `(J,bold-dot)` of the extended input's level-one algebra.
2. Record `epsilon_r=C_rect*epsilon_X`, the exact-unit axioms, product
   closeness, and unit closeness; choose the receiving threshold monotonically.
3. Apply C0 exactly once to this rectified algebra; C1 does not apply B1.
4. Transport the fixed-term projection defect from `bold-dot` to the original
   product.
5. Replace `J-P` by `I_X-P` using unit closeness and preserve both
   nonvanishing alternatives after one threshold decrease.
6. Enlarge one universal coefficient, take one finite minimum, and assemble
   the original-product/original-unit conclusion.

### C2. `lem-stage1-original-complementary-pair` — 6 nodes

1. Apply C1 once and fix its projection before choosing receiving constants.
2. Set `P'=P_0`, `P''=I_X-P_0`; record exact complementarity.
3. Retain Hermiticity and nonvanishing for both.
4. Expand the projection defect of `P''`, including approximate-unit errors.
5. Expand `P'P''` and `P''P'` by fixed-term estimates.
6. Enlarge/decrease once and assemble the pair.

### C3. `lem-stage1-fresh-two-point-inclusion` — 9 nodes

1. Apply C2 once and fix its exact pair.
2. Define one level-one `v^(2)` and every amplification as
   `id_{M_n} tensor v^(2)`.
3. Verify linearity, dagger, basis images, and exact unit.
4. Expand the four basis products at every amplification.
5. Use the operator-space simple-tensor identity to transport nonvanishing
   uniformly.
6. Multiply by the amplified projection belonging to a larger source
   coordinate to obtain one amplification-independent crude lower modulus.
7. Invoke byte-matched `GT-kitaev-prop-delta-hominc` at `:1194-1196`; line
   `:458` licenses data-independent implicit constants and `:1192` supplies
   the smallness quantifier.
8. Choose one threshold and coefficient uniformly over all levels.
9. Apply `def-extended-delta-inclusion` and assemble.

## 4. Definition-layer audit

| definition | use | disposition |
|---|---|---|
| `def-h-space-left-inversion` | A0--A3 and the displayed quotient H-space/left inversion | Reuse unchanged. |
| `def-lefschetz-fixed-point-data` | B0i--B1 local index and Lefschetz number | Reuse unchanged. |
| `def-epsilon-cstar-algebra` | Exact-unit inputs in B0a--C1 | Reuse unchanged. |
| `def-extended-epsilon-cstar-algebra` | MAIN-facing inputs of C1--C3 | Reuse unchanged. |
| `def-stage1-polar-witness-data` | The explicitly bound fourteen-field `W` | Reuse unchanged; it is data only, so every analytic clause is stated in result roots. |
| `def-approximate-unitary-space` | `calU`, `calU_e`, quotient, polar charts, and fixed lifts | Reuse unchanged. |
| `def-delta-projection` | Nontrivial/nonvanishing outputs in C0--C3 | Reuse unchanged. |
| `def-extended-delta-inclusion` | Complete C3 conclusion | Reuse unchanged. |
| `def-operator-space` | Canonical amplifications and simple-tensor norms in C3 | Reuse unchanged. |
| `def-projection-basis` | Standard `C^2` basis in C3 | Reuse unchanged. |
| `def-compressed-corner` | M19-S1 interface typing only | Reuse unchanged. |

**Proposed new definitions: none.** The coproduct-tail conditions and the
bound quotient packages are theorem-local displayed data, not new canonical
terms. Singular cohomology, CW complexes, graded algebras, associated gradeds,
trace, exterior algebras, and `C^2` remain BSc/MSc common knowledge. This
preserves audit-v2 F13 (`AUDIT-S1-ENDGAME-v2.md:404-416`).

## 5. Dimension-freeness audit

| place | audit |
|---|---|
| A0 | Kunneth and the two edge maps are structural over `reals`. The finite tensor expansion occurs inside finite-dimensional homogeneous summands and introduces no stability coefficient. |
| A1 | Hatcher's theorem is qualitative. Excluding polynomial and infinitely many odd generators uses only total finite dimension. |
| A2--A3 | Filtration length and Betti numbers affect finite algebraic sums, never a quantitative constant. |
| B0a | One row-13 tuple and one finite minimum supply all thresholds; operations are formula-defined. |
| B0i | Quotient derivatives use operator and quotient norms. Determinant positivity is sign through an invertible homotopy, not a dimension-dependent determinant bound. |
| B0s | QIFT is applied in Banach/operator norms to two charts. The minimum of two universal radii is universal. |
| B0b | Triangulation size enters no estimate. The square-root phase lift is qualitative and uses one circle phase. |
| B1 | The contradiction needs only two nonzero cohomological degrees, not a bound on the Betti sum. |
| C0 | `P=(2J+U+U^dagger)/4` has a fixed number of terms; each nonvanishing branch uses the carried universal radius. |
| C1 | Rectification and product/unit return use fixed-term comparisons on the same involutive normed space. |
| C2 | Complement and cross-defect estimates are fixed algebraic identities. |
| C3 | Four basis products are tensor-level terms, not entry sums. TeX line 458 makes every big-O function independent of additional data. |
| M19-S1 specialization | Future M04 supplies a selected corner of defect `L*epsilon`; multiplying the three producer constants by universal `L` and taking a finite maximum/minimum introduces no dimension, amplification, atom-count, or block dependence. |

No coefficient depends on `N`, cohomology dimension, number of exterior
generators, triangulation size, amplification level, or block count. This
preserves audit-v2 F12 (`AUDIT-S1-ENDGAME-v2.md:387-402`).

## 6. Exact M19-S1 interface match

The consumer contract at
`docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md:381`
states:

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
| Selected corner is a finite-dimensional extended algebra | **Not discharged by G-S1.** Future M04, after P0/M01--M03, supplies `S_{P_j}` as an extended `L*epsilon`-C*-algebra with its compressed unit. C1 accepts exactly this generic extended input. |
| `dim S_{P_j}>1` | Specialize `calX=S_{P_j}`; this is exactly C1--C3's strict dimension hypothesis, so no `N=1` branch is used. |
| Fresh nontrivial split | C1 returns a nontrivial projection for the original corner product/unit. C2 returns the same selected `P'` together with `P''=I_X-P'`, exact sum, and both cross defects. |
| Fresh `C^2` inclusion | C3 applies C2 once and returns that same pair, one level-one `v^(2)`, exact basis images, and `v^(2)(1,1)=I_X`. |
| Fixed amplification family | C3 defines only `id_{M_n} tensor v^(2)`. |
| Outer complementary targets | These remain `P_[1,m-1]` and `P_j`, later supplied by M04/the original inclusion; they are not C2's internal `P',P''`. |
| Literal old side | For `m>1`, T0 `lem-compcb-single-compression-transfer` supplies it as a direct M19-S1 dependency. |
| Every defect at most `t_1` | Future M19-S1 chooses `K_1` above the old-side coefficients and `L*C_proj,L*C_np,L*C_pair`, a finite universal maximum. |
| Thresholds and `K_1*e_call,1<=e_1` | Future M19-S1 takes a finite minimum after `L`-rescaling, after M04 and all other M01--M18 providers exist. |
| `m=1` | M15 omits the old side; C1--C3 still provide the fresh inclusion. |

Thus the producer shapes still match M19-S1/M15 clause-by-clause, exactly as
audit-v2 F10 settled (`AUDIT-S1-ENDGAME-v2.md:308-334`). This design claims
only removal of the G-S1 blocker.

## 7. Exact external and provenance disposition

No reference acquisition is required. Hatcher is local and hash-verified by
audit v2 (`AUDIT-S1-ENDGAME-v2.md:19-25`).

A1 registers the same two external ids proposed in v2, but with corrected,
non-strengthened statements:

1. `GT-hatcher-weak-hopf-conditions`,
   `refs/hatcher-algebraic-topology/AT.txt:17654-17677`: the imported statement
   is exactly the printed pair of conditions—`A` is connected, meaning
   `reals -> A^0`, `r |-> r*1`, is an isomorphism; and `Delta` is a graded
   algebra homomorphism whose value on every positive-degree `a` is
   `a tensor 1+1 tensor a` plus a finite sum of tensors whose two factors have
   positive degree. It imports **no** `Delta(1)` clause.
2. `GT-hatcher-hopf-structure-3C4`,
   `refs/hatcher-algebraic-topology/AT.txt:17798-17800`: the imported conclusion
   is exactly an algebra isomorphism to the tensor product of an exterior
   algebra on odd-dimensional generators and a polynomial algebra on
   even-dimensional generators. It imports **no** exterior-only conclusion.

The workspace external payloads must be byte-verbatim newline-counted slices
of those loci. A0 proves `Delta(1)=1 tensor 1`; A1 excludes the polynomial
factor and proves the odd generator family finite. Neither claim is attributed
to a stronger external.

C3 retains the v2 external and its repaired context:

- `GT-kitaev-prop-delta-hominc`,
  `refs/kitaev-2405.02434/approximate_algebras.tex:1194-1196`;
- proof `:1198-1222`;
- smallness context `:1192`;
- data-independent big-O context `:458`.

All other Kitaev ranges are clean TeX. The bridge range is
`approximate_algebras.tex:929-943`, explicitly containing line 939. No Borel,
Leray--Hirsch, standard coassociative bialgebra theorem, or unavailable source
is used.

## 8. Binder, dependency, and cascade audit

The package flow is logical existential elimination, not definite description:

1. B0a fixes row-13 `W` first and then the unique inverse of one displayed
   `Pi_delta`.
2. B0i applies B0a once, binds the returned existential package, and re-exports
   all map formulas, covariance, near-adjoint estimate, manifold data, charts,
   and index for those same objects.
3. B0s applies B0i once and re-exports the same objects plus one bound
   `r_bidx` and both actual-isolation clauses.
4. B0b applies B0s once, directly attaches the canonical manifold and finite-CW
   roots, performs the phase lift, and explicitly re-exports every field B1
   consumes.
5. B1 applies B0b once, carries the same outer `r_bidx`, and binds
   `breve-U` before `U_0,c,a,U`.
6. C0 applies B1 once and forgets the package after exporting `P`.
7. C1 applies C0 once and never applies B1.

The original ten B1 dependencies remain in byte-order and continue to serve as
the audited obligation checks. B0b is the eleventh typed provider, as in v2.
The two new factored rows are earlier dependencies of B0b, not additions to the
fixed ten-item list.

No T0 contract, definition, or existing workspace external is amended. No
retired parent or stated/seeded row is imported. The graph

`A0 -> A1 -> A2 -> A3`, `B0a -> B0i -> B0s -> B0b -> B1 -> C0 -> C1 -> C2 -> C3`,
with `A3 -> B1`, is acyclic.

## 9. Honest budgets and build granularity

| row | v2 target / cap | v3 target / rounds / cap | reason |
|---|---:|---:|---|
| A0 `hspace-coproduct-tail` | — | 10 / 4 / 15 | New construction row: Kunneth, algebra map, two edge maps, finite tail. |
| A1 `exterior-cohomology` | 8 / 12 | 7 / 3 / 11 | Now only exact-Hatcher matching, tensor classification, polynomial exclusion, and finite odd generators. |
| A2 `associated-graded` | 9 / 14 | 9 / 3 / 14 | Unchanged mathematics; now imports A0 and A1 separately. |
| A3 `trace` | 4 / 8 | 4 / 2 / 8 | Unchanged. |
| B0a `bound-quotient-left-inversion` | 8 / 12 | 8 / 3 / 12 | Retained explicit map/descent/H-space binder. |
| B0i `bound-quotient-local-index` | — | 8 / 3 / 13 | New same-map derivative, quotient isolation, determinant, and local-index branch. |
| B0s `bound-inversion-isolation` | — | 7 / 3 / 12 | New two-sign QIFT actual-isolation branch; benchmarked against the validated seven-node isolation row. |
| B0b `bound-quotient-index-data` | 9 / 14 | 5 / 2 / 9 | Now only direct manifold/CW attachment, global phase lift, and explicit re-export. |
| B1 `extra-fixed-class` | 10 / 15 | 10 / 3 / 15 | Same contradiction, now with a genuinely complete bound package. |
| C0 `fixed-unitary-projection-bridge` | 8 / 12 | 8 / 3 / 12 | One B1 application, one fixed-term bridge, two nonvanishing branches. |
| C1 `rectified-nontrivial-projection` | 7 / 12 | 6 / 3 / 10 | Applies C0 only; no duplicate B1 selection. |
| C2 `original-complementary-pair` | 6 / 10 | 6 / 2 / 10 | Unchanged. |
| C3 `fresh-two-point-inclusion` | 9 / 14 | 9 / 3 / 14 | Unchanged proof; repaired provenance retained. |

The total target is 94 nodes across 13 separately verified rows. The maximum
target is ten and the maximum hard cap is fifteen, well below 26. A0+A1 is
priced above the validated 13-node stronger-antecedent Hopf row; B0i+B0s+B0b
is priced above the validated 12-node quotient-index row plus the validated
seven-node isolation row. No hard cap is raised to hide a multi-obligation
node.

## 10. Honest hostile-verifier risk register

| row | first likely hostile attack | designed response / stop condition |
|---|---|---|
| A0 | Are both edge terms and the finite tail actually derived, and is `Delta(1)` falsely imported? | Separate unitality, two edge maps, bidegree decomposition, and finite expansion. `Delta(1)` is internal only. |
| A1 | Are the externals strengthened to exterior-only or finitely many generators? | Register the exact exterior-tensor-polynomial theorem; give separate nodes to polynomial exclusion and finite odd generators. |
| A2 | Does left inversion give the sign in total degree, not merely word length? | Separate primitive-mod-square, multiplicativity, and odd-degree parity. |
| A3 | Is the filtration finite and exhaustive? | Establish it before trace additivity. |
| B0a | Is the smooth `sigma` literally the row-13 map? | Bind `W`, then the unique inverse of the displayed `Pi_delta`, before invoking the explicit smooth bridge. |
| B0i | Are manifold hypotheses present, and are quotient derivatives for the same map? | Import the manifold root directly; expose charts and the same-map differentiated descent in the root. Stop on any second inverse or inversion. |
| B0s | Does QIFT really isolate actual fixed points in both ambient balls? | One explicit node per sign using B0i's displayed charts; one separate radius-selection node. |
| B0b | Is finite CW applied conditionally, and is `[U_0]` pre-used? | Direct manifold import feeds the finite-CW antecedent; quantify `breve-V` before `U_0,c,a`. |
| B1 | Do trace, index, phase lift, estimate, and radius concern one package? | Apply B0b once and carry its explicitly re-exported maps and `r_bidx`; no dependency-body lookup. |
| C0 | Is B1 selected twice, or does small `P` really force the correct isolation branch? | B1 is applied once inside C0; allocate one node to each branch using the line-939 formula. |
| C1 | Can a C0 package be passed through a root that does not accept it? | No package is passed. C1 invokes only C0 on its one rectified algebra. |
| C2 | Does complementarity survive the approximate original unit? | Expand both orders and the complement defect explicitly. |
| C3 | Is complete near-isometry inferred from multiplicativity alone, or are constants level-dependent? | Prove a crude amplification-uniform modulus before invoking the exact proposition with `:458` and `:1192`; stop if the external cannot be registered at those loci. |

## 11. Ratification surface and honest hand-off

User ratification is required for all 13 contracts and, relative to v2, the
three new helper ids:

- `lem-stage1-hspace-coproduct-tail`;
- `lem-stage1-bound-quotient-local-index`;
- `lem-stage1-bound-inversion-isolation`.

No new definition or external id requires ratification. The two Hatcher
external ids already proposed in v2 require corrected byte-verbatim payloads
and the exact restricted statements in section 7.

A fresh hostile audit should attack, in order:

1. the exact A0/A1 match to the two Hatcher slices;
2. B0i's direct compact-orientable-manifold antecedent and same-map quotient
   derivative;
3. B0s's two actual-isolation branches;
4. B0b's direct manifold-to-finite-CW application, complete re-export, class
   binder order, and bound `r_bidx`;
5. the one-package B1 contradiction;
6. the one-use B1 -> C0 -> C1 architecture;
7. C1's return to the original product/unit;
8. C3's line-458 universality context; and
9. the G-S1-only hand-off.

If all 13 rows later validate, the trace chain, one bound extra fixed class,
and the three G-S1 producers are available. MAIN remains separately gated on
P0 and M01--M18. This design promotes no claim about M19-S1--M28,
`lem-thmainext-conditional`, or `op-classical`.
