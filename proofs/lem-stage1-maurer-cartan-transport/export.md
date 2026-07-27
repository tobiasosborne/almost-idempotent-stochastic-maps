# Proof Export

## Node 1

**Statement:** Parameterized Maurer-Cartan transport: there exist C_ch^0 >= 1 and kappa_ch^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_ch >= C_ch^0 and 0 < kappa_ch <= kappa_ch^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_ch*(epsilon_r + delta) <= kappa_ch, and every family g = (g_U)_{U in calU} of C^1 maps g_U: B^{icalH}_{2delta}(0) -> B^{calH}_{2delta}(0) such that, for every U in calU and A^par in B^{icalH}_{2delta}(0), g_U(A^par) is the unique element of B^{calH}_{2delta}(0) satisfying f_U(A^par + g_U(A^par)) = 0, where f_U(A) = (1/2)*(((J + A^dagger) bold-dot U^dagger) bold-dot (U bold-dot (J + A)) - J), every tangent space T_U calU is the image of L_U(I + Dg_U(0)): icalH -> calX, and omega_U(Z) = (L_U^{-1} Z)^par : T_U calU -> icalH is a global C^1 bundle trivialization with distortion at most 1 + C_ch*epsilon_r, satisfying omega_{cU}(cZ) = omega_U(Z) and omega_U(iU) = iJ for every U in calU, Z in T_U calU, and c in U(1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** The external lem-stage1-maurer-cartan-trivialization supplies universal constants Cbar >= 1 and kappabar in (0,1/2] for which its stated uniform conclusion holds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Choose the target constants C_ch^0 := Cbar and kappa_ch^0 := kappabar; these are universal and satisfy C_ch^0 >= 1 and kappa_ch^0 in (0,1/2].

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Fix arbitrary W, algebra, delta, and family g satisfying all hypotheses of node 1. The guard puts the algebra and delta within the scope of lem-stage1-maurer-cartan-trivialization. Without identifying g with the distinguished graph family mentioned there, the zero equation implies directly that the image of L_U(I+Dg_U(0)) is contained in T_U calU; the external bundle trivialization gives equality of dimensions, hence equality of these spaces. The external omega, distortion, and equivariance conclusions then apply to this same tangent bundle, with preliminary distortion bound 1+Cbar*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** From C_ch*(epsilon_r + delta) <= kappa_ch, C_ch >= Cbar, 0 < kappa_ch <= kappabar, and epsilon_r + delta >= 0, one has Cbar*(epsilon_r + delta) <= C_ch*(epsilon_r + delta) <= kappa_ch <= kappabar, which is precisely the smallness guard of lem-stage1-maurer-cartan-trivialization.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Conditional uniqueness bridge (and no more): suppose, in addition to the registered hypotheses, that the distinguished graph family gbar referred to in lem-stage1-maurer-cartan-trivialization is defined on B^{icalH}_{2delta}(0), takes values in B^{calH}_{2delta}(0), and satisfies f_U(A^par + gbar_U(A^par)) = 0 for every U and A^par. Then the target family's uniqueness hypothesis implies g_U(A^par) = gbar_U(A^par) for every U and A^par. The sole registered external does not supply this additional antecedent, so this node does not assert the unconditional equality g = gbar.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Fix arbitrary U in calU and A^par in B^{icalH}_{2delta}(0), and assume the additional antecedent stated at node 1.3.2. Then gbar_U(A^par) belongs to B^{calH}_{2delta}(0) and solves f_U(A^par + X) = 0. By the target hypothesis, g_U(A^par) is the unique X in that ball solving this equation. Therefore gbar_U(A^par) = g_U(A^par). Since U and A^par were arbitrary, gbar = g pointwise. This proves precisely the conditional bridge and does not claim that the registered external establishes its antecedent.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Because g and gbar are C^1 and equal pointwise on B^{icalH}_{2delta}(0), Dg_U(0) = Dgbar_U(0) for every U. Applying lem-stage1-maurer-cartan-trivialization under the guard in node 1.3.1, and substituting these derivative equalities, yields every tangent formula and the global C^1 omega formula for g, with distortion at most 1 + Cbar*epsilon_r; the identities omega_{cU}(cZ)=omega_U(Z) and omega_U(iU)=iJ are unchanged because omega is the same displayed map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** Repair of challenge ch-e67e0f72419358f7: no properties of, or equality with, the distinguished graph family are needed. The guard gives epsilon_r < 1/2 because C_ch >= 1, delta > 0, and C_ch*(epsilon_r+delta) <= kappa_ch <= 1/2. If X satisfies X^dagger bold-dot X=J, then the C-star lower bound gives ||X||^2 <= 1/(1-epsilon_r). For every Y, approximate associativity and exact unitality give ||L_{X^dagger}L_XY-Y|| <= epsilon_r||X||^2||Y|| <= epsilon_r/(1-epsilon_r)||Y||, with coefficient strictly below 1. Thus L_{X^dagger}L_X is invertible by the Neumann lemma, so L_X is injective; finite dimensionality makes L_X surjective, hence X has a right inverse. Therefore every exact zero of the displayed f_U equation lies in calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.5

**Statement:** Fix U in calU and B in icalH. Exact unitality and U^dagger bold-dot U=J give f_U(0)=0, so uniqueness forces g_U(0)=0. For all sufficiently small real t, set X_B(t)=U bold-dot (J+tB+g_U(tB)). The defining zero equation is exactly X_B(t)^dagger bold-dot X_B(t)=J because the involution reverses the product, and the preceding step gives the required right inverse, so X_B(t) lies in calU and X_B(0)=U. Differentiating at zero gives dX_B/dt at zero = L_U(B+Dg_U(0)B). Hence im L_U(I+Dg_U(0)) is contained in T_U calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.6

**Statement:** By node 1.3.1, lem-stage1-maurer-cartan-trivialization applies and supplies the fiberwise linear bundle isomorphism omega_U:T_U calU -> icalH, omega_U(Z)=(L_U^{-1}Z)^par. Consequently dim T_U calU=dim icalH. For Phi_g(B)=L_U(B+Dg_U(0)B), the inclusion from the preceding step makes omega_U(Phi_g(B)) defined, and the displayed formula gives omega_U(Phi_g(B))=(B+Dg_U(0)B)^par=B because Dg_U(0)B is Hermitian. Thus Phi_g is injective, so its image has dimension dim icalH. The inclusion between finite-dimensional spaces of equal dimension is equality: T_U calU=im L_U(I+Dg_U(0)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.7

**Statement:** The tangent bundle identified in the preceding step is the same intrinsic tangent bundle on which the external theorem already supplies omega_U(Z)=(L_U^{-1}Z)^par as a global C1 bundle trivialization, with distortion at most 1+Cbar*epsilon_r and identities omega_{cU}(cZ)=omega_U(Z), omega_U(iU)=iJ. These conclusions do not mention the distinguished graph family. Therefore they hold together with the newly established tangent formula for the arbitrary family g, completing node 1.3 without the missing antecedent flagged by the verifier.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Since C_ch >= C_ch^0 = Cbar and epsilon_r >= 0, the preliminary distortion bound 1 + Cbar*epsilon_r is at most 1 + C_ch*epsilon_r; hence the transferred conclusions are exactly all conclusions required by node 1, for every admissible datum.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

