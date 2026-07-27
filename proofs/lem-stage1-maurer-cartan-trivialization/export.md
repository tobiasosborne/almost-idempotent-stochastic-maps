# Proof Export

## Node 1

**Statement:** Uniform global tangent/Maurer-Cartan control: there are universal C_ch >= 1, kappa_ch in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0 with C_ch*(epsilon_r + delta) <= kappa_ch, the graph maps supplied by lem-stage1-unitary-graph-control satisfy: every tangent space T_U calU is the image of L_U(I + Dg_U(0)): icalH -> calX, and omega_U(Z) = (L_U^{-1} Z)^par : T_U calU -> icalH is a global C^1 bundle trivialization with distortion at most 1 + C_ch*epsilon_r, satisfying omega_{cU}(cZ) = omega_U(Z) and omega_U(iU) = iJ for every c in U(1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Witness and guard selection: let C0 >= 1 and kappa0 in (0,1/2] be the universal witnesses of lem-stage1-unitary-graph-control. There is a universal K >= 1 such that, whenever 0 <= epsilon_r <= 1/4 and U is in calU, one has ||U|| <= (1-epsilon_r)^(-1/2), ||L_U|| <= 1+K*epsilon_r, and ||L_U^{-1}|| <= 1+K*epsilon_r; choose C_ch >= max(C0,K,4) large enough to absorb all fixed products of these bounds and the graph bound, and choose 0 < kappa_ch <= min(kappa0,1/4). Then C_ch*(epsilon_r+delta) <= kappa_ch implies the upstream graph guard and epsilon_r <= 1/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Approximate left multiplication estimate from def-epsilon-cstar-algebra and def-approximate-unitary-space: for U in calU, U^dagger bold-dot U=J and ||J||=1. The lower C*-inequality gives ||U||=||U^dagger|| <= (1-epsilon_r)^(-1/2), and the product inequality gives ||L_U||,||L_{U^dagger}|| <= (1+epsilon_r)||U||. The associator axiom and exact unit give ||L_{U^dagger}L_U-I|| <= epsilon_r||U||^2 <= epsilon_r/(1-epsilon_r). For epsilon_r <= 1/4 this is <1, so the Neumann lemma and finite dimensionality make L_U invertible and give ||L_U^{-1}|| <= (1-epsilon_r/(1-epsilon_r))^(-1)*(1+epsilon_r)*(1-epsilon_r)^(-1/2). These displayed scalar functions are at most 1+K*epsilon_r on [0,1/4] for a universal K, and the same is true of ||L_U||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Constant absorption and application of lem-stage1-unitary-graph-control: take its universal witnesses C0,kappa0. Choose a universal C_ch >= max(C0,K,4) large enough that every fixed product used in the tangent distortion is bounded by 1+C_ch*epsilon_r for 0 <= epsilon_r <= 1/4, and set kappa_ch=min(kappa0,1/4). If C_ch*(epsilon_r+delta)<=kappa_ch with delta>0, then C0*(epsilon_r+delta)<=kappa0 and epsilon_r<1/4, so the external graph theorem applies; enlarging C_ch once more does not spoil this implication.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Centered graph differentiation: for every admissible algebra and U in calU, the graph map of lem-stage1-unitary-graph-control centered at U satisfies g_U(0)=0 and ||Dg_U(0)|| <= C0*epsilon_r, and its graph-chart parametrization has derivative L_U(I+Dg_U(0)) at 0; hence T_U calU is exactly the image of that map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Basepoint and sharp derivative bound using lem-stage1-unitary-graph-control: exact unitality and U^dagger bold-dot U=J give f_U(0)=0, so uniqueness gives g_U(0)=0. If rho>0 also satisfies C0*(epsilon_r+rho)<=kappa0, the external theorem gives a graph germ g_U^{rho} with ||Dg_U^{rho}(0)||<=C0*(epsilon_r+rho). For two such radii, continuity at 0 and g_U^{rho}(0)=0 put both solutions in the smaller Hermitian ball on a common neighborhood; pointwise uniqueness there makes the germs, hence their derivatives at 0, equal. Taking rho down to 0 therefore yields ||Dg_U(0)||<=C0*epsilon_r for the graph map at the originally prescribed delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Tangent calculation using lem-stage1-unitary-graph-control: the centered chart is Psi_U(A)=U bold-dot (J+A+g_U(A)) for A in icalH. It obeys Psi_U(0)=U, is C^1, and differentiating the bilinear product gives D Psi_U(0)A=L_U(A+Dg_U(0)A)=L_U(I+Dg_U(0))A. Because the external theorem says these are graph charts covering calU, the image of this chart derivative is exactly T_U calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Fibrewise inverse, distortion, and regularity: on the tangent image, omega_U(Z)=(L_U^{-1}Z)^par is inverse to A maps-to L_U(A+Dg_U(0)A). The estimates from the witness step and ||Dg_U(0)|| <= C0*epsilon_r give norms of omega_U and its inverse at most 1+C_ch*epsilon_r; the displayed omega is a global C^1 bundle trivialization.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Detailed inverse/distortion/regularity argument: write P^par(X)=(X-X^dagger)/2, whose norm is at most 1 by the isometric involution in def-epsilon-cstar-algebra. For A in icalH, Dg_U(0)A lies in calH, hence P^par(A+Dg_U(0)A)=A. Therefore omega_U(L_U(A+Dg_U(0)A))=A, and the tangent-image result makes omega_U a fibrewise isomorphism with that displayed inverse. Its norm is at most ||L_U^{-1}||, while the inverse has norm at most ||L_U||*(1+||Dg_U(0)||); the witness selection absorbs both into 1+C_ch*epsilon_r. Finally U maps-to L_U is linear, inversion is C^1 on the open set of invertible endomorphisms, and P^par is fixed linear, so (U,Z) maps-to (U,P^par L_U^{-1}Z) restricts to a C^1 tangent-bundle map. A fibrewise bijective C^1 bundle map has C^1 inverse in local frames because finite-dimensional matrix inversion is C^1; thus omega is the asserted global C^1 bundle trivialization with the stated distortion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Dependency-closed inverse/distortion/regularity bridge. By validated nodes 1.1.1 and 1.1.2, L_U is invertible and both ||L_U|| and ||L_U^{-1}|| are at most 1+K*epsilon_r, with the final witness C_ch chosen to absorb the fixed products below. By validated nodes 1.2.1 and 1.2.2, g_U(0)=0, ||Dg_U(0)||<=C0*epsilon_r, Dg_U(0)(icalH) is contained in calH, and T_U calU is the image of A maps-to L_U(A+Dg_U(0)A). Let P^par(X)=(X-X^dagger)/2. The isometric involution gives ||P^par||<=1, and for A in icalH and H in calH one has P^par(A+H)=A. Hence P^par L_U^{-1} sends L_U(A+Dg_U(0)A) to A; the tangent-image equality makes it a fibrewise bijection with inverse A maps-to L_U(A+Dg_U(0)A). Its two operator norms are bounded respectively by ||L_U^{-1}|| and ||L_U||*(1+||Dg_U(0)||), hence by 1+C_ch*epsilon_r by the choice in 1.1.2. For regularity, U maps-to L_U is linear, inversion is C^1 on the open set of invertible endomorphisms, and P^par is fixed real-linear, so (U,Z) maps-to (U,P^par L_U^{-1}Z) is C^1 before restriction and therefore on TcalU. In local bundle frames it is represented by an everywhere-invertible C^1 matrix B(U); B(U)^{-1}=adj(B(U))/det(B(U)) is C^1. The local inverses agree with the displayed fibrewise inverse, so they glue to a global C^1 inverse. Thus omega is the asserted global C^1 trivialization, using only the four declared validated dependencies rather than the pending parents 1.1 and 1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.2

**Statement:** Smooth dependence of the graph derivative from the defining equation: for U in calU set B_U=D_{A^perp}f_U(0)|_{calH}:calH->calH and C_U=D_{A^par}f_U(0)|_{icalH}:icalH->calH. The upstream formula f_U(A)=(1/2)*(((J+A^dagger) bold-dot U^dagger) bold-dot (U bold-dot (J+A))-J), together with fixed bilinear multiplication and the fixed real-linear involution, shows directly that U maps-to B_U and U maps-to C_U are polynomial, hence C^1, maps into the finite-dimensional operator spaces. Since U is unitary, f_U(0)=0 and uniqueness gives g_U(0)=0. The upstream estimate at A^par=0 therefore gives ||B_U-I_calH||<=C0*epsilon_r<1, so B_U is invertible. Differentiating the C^1 identity f_U(A+g_U(A))=0 at A=0 in each anti-Hermitian direction gives C_U+B_U Dg_U(0)=0, whence Dg_U(0)=-B_U^{-1}C_U. Inversion on the open set of invertible finite-dimensional operators is C^1, so U maps-to Dg_U(0) is C^1 on calU. Consequently (U,A) maps-to (U,L_U(A+Dg_U(0)A)) is a C^1 inverse to omega; this proves inverse regularity without inferring it from mere C^1 graph-chart regularity.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.3

**Statement:** Correction to the challenged regularity inference: do not infer C^1 regularity of the inverse from a merely C^1 graph frame. Instead use node 1.3.1.2: the differentiated defining equation gives the explicit smooth formula Dg_U(0)=-B_U^{-1}C_U, with B_U and C_U polynomial in U and B_U invertible by the upstream near-identity estimate. Hence the already identified fibrewise inverse (U,A) maps to (U,L_U(A+Dg_U(0)A)) is C^1 directly. The counterexample in the challenge is inapplicable precisely because its graph derivative has no analogous smooth implicit-equation formula with invertible normal derivative.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Equivariance and central tangent: for every c in U(1), scalar multiplication carries T_U calU to T_{cU} calU and omega_{cU}(cZ)=omega_U(Z); moreover the scalar orbit through U has velocity iU and omega_U(iU)=iJ.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Scalar equivariance from def-approximate-unitary-space and bilinearity: U maps-to cU preserves calU and is a linear diffeomorphism with derivative Z maps-to cZ, hence cZ lies in T_{cU}calU. Since L_{cU}=cL_U, one has L_{cU}^{-1}(cZ)=L_U^{-1}Z, and taking the anti-Hermitian component gives omega_{cU}(cZ)=omega_U(Z).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Central tangent identity from def-approximate-unitary-space and exact unitality: the curve t maps-to exp(it)U lies in calU and has derivative iU at zero, so iU lies in T_UcalU. Complex bilinearity and U bold-dot J=U give L_U(iJ)=iU; therefore L_U^{-1}(iU)=iJ, which is anti-Hermitian because J^dagger=J, and omega_U(iU)=iJ.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

