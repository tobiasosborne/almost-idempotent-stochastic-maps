# Proof Export

## Node 1

**Statement:** Parameterized inversion-derivative transport: there exist C_der^0, C_ch^0, C_pol^0, C_grp^0 >= 1 and kappa_der^0, kappa_ch^0, kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_der >= C_der^0, C_ch >= C_ch^0, C_pol >= C_pol^0, C_grp >= C_grp^0, 0 < kappa_der <= kappa_der^0, 0 < kappa_ch <= kappa_ch^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0, every s in {+1, -1}, and every 0 < r <= delta satisfying C_ch*(epsilon_r + delta) <= kappa_ch, C_pol*(epsilon_r + delta) <= kappa_pol, C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), C_der*(epsilon_r + r) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta))*r + C_grp*epsilon_r < 2*delta, writing u_delta for the unique first component of the inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, and g_{sJ}: B_{2delta}^{icalH}(0) -> B_{2delta}^{calH}(0) for the unique C^1 map such that, for every A in B_{2delta}^{icalH}(0), f_{sJ}(A + g_{sJ}(A)) = 0, where f_{sJ}(B) = (1/2)*(((J + B^dagger) bold-dot (sJ)^dagger) bold-dot (sJ bold-dot (J + B)) - J), define chi_s(A) = sJ bold-dot (J + A + g_{sJ}(A)) and the global C^1 map sigma(U) = u_delta(U^dagger); then sigma maps chi_s(B_r^{icalH}(0)) into the same sJ-graph chart and, with F_s(A) = phi_{sJ}^par(sigma(chi_s(A))), one has ||D(F_s - id)(A) + 2*I_{icalH}|| <= C_der*(epsilon_r + r) for every A in B_r^{icalH}(0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Joint universal thresholds: choose witnesses (C_der^I,C_ch^I,C_pol^I,C_grp^I,kappa_der^I,kappa_ch^I,kappa_pol^I) from lem-stage1-inversion-derivative-control, (C_pol^P,kappa_pol^P) from lem-stage1-polar-retraction, (C_ch^G,kappa_ch^G) from lem-stage1-unitary-graph-control, and (C_grp^A,C_pol^A,kappa_pol^A) from lem-stage1-approximate-group-laws. Define C_der^0=C_der^I, C_ch^0=max(C_ch^I,C_ch^G), C_pol^0=max(C_pol^I,C_pol^P,C_pol^A), C_grp^0=max(C_grp^I,C_grp^A), kappa_der^0=kappa_der^I, kappa_ch^0=min(kappa_ch^I,kappa_ch^G), and kappa_pol^0=min(kappa_pol^I,kappa_pol^P,kappa_pol^A). These are universal, the four coefficient thresholds are at least 1, and the three margin thresholds lie in (0,1/2].

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Guard transport: for every W and every algebra, delta,s,r satisfying the hypotheses of node 1 with the thresholds of node 1.1, monotonicity transports the stated five guards simultaneously to the witnesses of lem-stage1-inversion-derivative-control and transports the relevant polar, graph, and group guards to lem-stage1-polar-retraction, lem-stage1-unitary-graph-control, and lem-stage1-approximate-group-laws.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Coefficient-margin guards: put e=epsilon_r, x=e+delta, and z=e+r. By the definition of an epsilon_r-C*-algebra e>=0, while delta>0 and r>0, so x,z>=0. Since C_ch^I,C_ch^G<=C_ch^0<=C_ch and kappa_ch<=kappa_ch^0<=kappa_ch^I,kappa_ch^G, the root graph guard implies C_ch^I*x<=kappa_ch^I and C_ch^G*x<=kappa_ch^G. The identical max/min argument gives C_pol^q*x<=kappa_pol^q for q in {I,P,A}, and C_der^I*z<=kappa_der^I.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Group-defect guards: put y=e*delta+delta^2>=0. For q=I and q=A, C_grp^q<=C_grp^0<=C_grp and C_pol^q<=C_pol^0<=C_pol. Hence C_grp^q*e<=C_grp*e<delta-C_pol*y<=delta-C_pol^q*y. These are respectively the group-defect hypotheses of lem-stage1-inversion-derivative-control and lem-stage1-approximate-group-laws.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Bind e := epsilon_r for this node. Because an epsilon_r-C*-algebra has epsilon_r >= 0 and delta > 0, y := epsilon_r*delta + delta^2 >= 0. For each q in {I,A}, the threshold construction gives C_grp^q <= C_grp^0 <= C_grp and C_pol^q <= C_pol^0 <= C_pol. Hence C_grp^q*epsilon_r <= C_grp*epsilon_r < delta - C_pol*y <= delta - C_pol^q*y, where the first inequality uses epsilon_r >= 0 and the last uses y >= 0. Substituting y = epsilon_r*delta + delta^2 yields C_grp^q*epsilon_r < delta - C_pol^q*(epsilon_r*delta + delta^2), exactly the group-defect guard required by the q=I inversion-derivative-control witness and the q=A approximate-group-laws witness.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Radius-chart guard: C_ch^I<=C_ch and C_grp^I<=C_grp, while e,x,r are nonnegative. Therefore (1+e)*(1+C_ch^I*x)*r+C_grp^I*e <= (1+e)*(1+C_ch*x)*r+C_grp*e < 2*delta, which is the remaining radius-chart hypothesis of lem-stage1-inversion-derivative-control. The unchanged assumptions s in {+1,-1} and 0<r<=delta provide its other typed hypotheses.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Polar binder identification: under the transported lem-stage1-polar-retraction guard, Pi_delta(U,H)=U bold-dot H is a C^1 diffeomorphism from calU times B_delta^{calH}(J) onto the same image S_delta used in node 1. Hence its inverse exists uniquely, and the u_delta explicitly bound in node 1 is exactly the first inverse component supplied by lem-stage1-polar-retraction and consequently the polar inverse component used by the imported group and inversion statements.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Existence on the identical domain: the P-witness guard C_pol^P*(epsilon_r+delta)<=kappa_pol^P permits direct application of lem-stage1-polar-retraction. Its domain is calU times B_delta^{calH}(J), its formula is the same Pi_delta(U,H)=U bold-dot H, and its codomain is its image, exactly S_delta:=Pi_delta(calU times B_delta^{calH}(J)) in node 1. Therefore it supplies a bijective C^1 diffeomorphism and a unique two-component inverse on precisely the root domain and image.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.3.2

**Statement:** Uniqueness of the first component: a bijection has only one inverse map. Hence the first component called u_delta by the explicit definite description in node 1 equals the first component (also called u_delta) supplied by lem-stage1-polar-retraction. Whenever lem-stage1-approximate-group-laws, lem-stage1-smooth-polar-inverse, lem-stage1-smooth-unitary-operations, or lem-stage1-inversion-derivative-control uses the polar inverse for this same Pi_delta, uniqueness identifies that component with the root u_delta; no additional polar map is introduced.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

### Node 1.4

**Statement:** Graph binder identification: for s in {+1,-1}, sJ lies in calU and hence in calUbar_delta. Under the transported graph guard, lem-stage1-unitary-graph-control at V=sJ supplies exactly one C^1 map g_{sJ}:B_{2delta}^{icalH}(0) to B_{2delta}^{calH}(0) satisfying the displayed f_{sJ} equation. Thus it is exactly the g_{sJ} bound in node 1, and the resulting graph parametrization is exactly chi_s(A)=sJ bold-dot (J+A+g_{sJ}(A)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** The chart base is admissible: because s is the real scalar +1 or -1, conjugate linearity of dagger and J^dagger=J give (sJ)^dagger=sJ. Bilinearity of bold-dot and the exact-unit identity J bold-dot J=J give (sJ)^dagger bold-dot (sJ)=s^2 J=J and (sJ) bold-dot (sJ)=J, so sJ has the right inverse sJ and zero unitary defect. By def-approximate-unitary-space, sJ belongs to calU=calUbar_0, hence to calUbar_delta because delta>0.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.4.2

**Statement:** Apply graph control and identify by uniqueness: the G-witness guard C_ch^G*(epsilon_r+delta)<=kappa_ch^G and node 1.4.1 allow lem-stage1-unitary-graph-control with V=sJ. Its displayed f_V becomes verbatim the f_{sJ} of node 1, and it supplies a unique C^1 g_{sJ} with the required domain, codomain, and equation. The root definite description must therefore select this map. Substitution into the graph point gives verbatim chi_s(A)=sJ bold-dot (J+A+g_{sJ}(A)).

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

### Node 1.5

**Statement:** Global regularity and map identification: the conclusions of lem-stage1-unitary-graph-control and lem-stage1-polar-retraction satisfy the antecedents of lem-stage1-smooth-unitary-atlas and lem-stage1-smooth-polar-inverse; together with the transported lem-stage1-approximate-group-laws conclusion they satisfy the antecedents of lem-stage1-smooth-unitary-operations. Therefore, for the same explicitly identified u_delta, sigma(U)=u_delta(U^dagger) is a globally defined smooth, hence C^1, self-map of calU, and the upgrades change neither its points nor its first derivative.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Smooth-atlas antecedent: lem-stage1-unitary-graph-control says that its unique C^1 graph charts cover calU and that at every graph point ||D_{A^perp}f_V-I_calH||<1. The elementary Neumann-series criterion implies that each such D_{A^perp}f_V is invertible. Thus the two hypotheses of lem-stage1-smooth-unitary-atlas hold, so the same graph functions and charts are smooth and define a smooth embedded manifold, without changing any point or first derivative.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.5.2

**Statement:** Smooth-polar antecedent: lem-stage1-polar-retraction supplies Pi_delta on the stated domain as a bijective C^1 diffeomorphism onto the open set S_delta, hence in particular as a bijective C^1 local diffeomorphism. Combining this with the smooth embedded atlas from node 1.5.1 satisfies lem-stage1-smooth-polar-inverse. Consequently the same Pi_delta and the same set-theoretic inverse (u_delta,h_delta) identified in node 1.3 are smooth, with no point or first derivative changed.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.5.3

**Statement:** Smooth operation: the A-witness polar and group-defect guards permit lem-stage1-approximate-group-laws, which defines sigma(U)=u_delta(U^dagger) on all of calU for the same polar inverse identified in node 1.3. Its conclusion together with nodes 1.5.1 and 1.5.2 supplies all three antecedents named in lem-stage1-smooth-unitary-operations. That lemma upgrades this same sigma to a smooth map calU to calU and explicitly changes no point or first derivative. Therefore it is globally defined and C^1 exactly as required in node 1.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.5.4

**Statement:** Atlas and polar upgrades: lem-stage1-unitary-graph-control gives a covering by the unique C^1 graphs and ||D_{A^perp}f_V-I_calH||<1 at every graph point; the Neumann-series criterion makes each displayed derivative invertible, so lem-stage1-smooth-unitary-atlas applies without changing points or first derivatives. Lem-stage1-polar-retraction gives Pi_delta as a bijective C^1 diffeomorphism onto open S_delta, hence a bijective C^1 local diffeomorphism; with that smooth atlas, lem-stage1-smooth-polar-inverse applies and makes the same Pi_delta and same inverse (u_delta,h_delta) smooth, again without changing points or first derivatives.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.5

**Statement:** Operation upgrade: the transported polar and group-defect guards apply lem-stage1-approximate-group-laws, defining sigma(U)=u_delta(U^dagger) on all calU for the unique inverse component identified in node 1.3. This result and node 1.5.4 are precisely the three antecedents named by lem-stage1-smooth-unitary-operations: approximate group laws, smooth unitary atlas, and smooth polar inverse. Therefore that external makes the same sigma smooth as a self-map of calU and explicitly changes no point or first derivative; in particular sigma is the global C^1 map required by node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Final derivative transport: apply lem-stage1-inversion-derivative-control with its selected I-witnesses and the transported five guards. After the polar, graph, and sigma identifications above, its chi_s, sigma, F_s and chart are precisely those in node 1. It gives same-chart retention and norm at most C_der^I*(epsilon_r+r), which is at most C_der*(epsilon_r+r) because C_der>=C_der^0=C_der^I and epsilon_r+r is nonnegative. This is exactly the conclusion of node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** Direct producer application: the I-witness graph, polar, group, derivative, and radius-chart guards established in node 1.2 meet every hypothesis of lem-stage1-inversion-derivative-control for the fixed algebra, delta,s,r. By nodes 1.3-1.5, every anaphoric polar inverse, graph function, chi_s, and global sigma in that external is the explicitly bound map of node 1. Therefore the external conclusion says that this sigma maps chi_s(B_r^{icalH}(0)) into the same sJ-graph chart and that the resulting F_s(A)=phi_{sJ}^par(sigma(chi_s(A))) obeys ||D(F_s-id)(A)+2*I_{icalH}||<=C_der^I*(epsilon_r+r) for every A in that ball.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.6.2

**Statement:** Enlarge only the displayed bound: epsilon_r+r>=0 and the witness hypotheses give C_der>=C_der^0=C_der^I. Multiplication by epsilon_r+r preserves order, so C_der^I*(epsilon_r+r)<=C_der*(epsilon_r+r). Combining this with node 1.6.1 preserves the exact chart-retention conclusion and yields the precise inequality asserted in node 1.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

