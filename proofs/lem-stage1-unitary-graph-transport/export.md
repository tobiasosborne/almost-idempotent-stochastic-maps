# Proof Export

## Node 1

**Statement:** Parameterized unitary-graph transport: there exist C_ch^0 >= 1 and kappa_ch^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_ch >= C_ch^0 and 0 < kappa_ch <= kappa_ch^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra (calX, J, bold-dot, dagger), every delta > 0 with C_ch*(epsilon_r + delta) <= kappa_ch, every V in calUbar_delta, and every A^par in B^{icalH}_{2delta}(0), there is a unique g_V(A^par) in B^{calH}_{2delta}(0) such that f_V(A^par + g_V(A^par)) = 0, where f_V(A) = (1/2)*(((J + A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J + A)) - J), the element V bold-dot (J + A^par + g_V(A^par)) lies in calU, ||g_V(A^par) + (1/2)*(V^dagger bold-dot V - J)|| <= C_ch*(epsilon_r*delta + delta^2), ||Dg_V(A^par)|| <= C_ch*(epsilon_r + delta), and ||D_{A^perp} f_V(A^par + g_V(A^par)) - I_{calH}|| <= C_ch*(epsilon_r + delta) < 1, and these C^1 graph charts cover calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Choose C_ch^0 = C_hat and kappa_ch^0 = kappa_hat from lem-stage1-unitary-graph-control. For arbitrary W and algebraic inputs satisfying the root hypotheses, the following atomic steps verify the upstream smallness condition, apply that external theorem, and monotonically transfer every estimate to the coefficient C_ch carried by W; hence the root contract follows.

**Type:** claim

**Inference:** existential_instantiation

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** The validated external lem-stage1-unitary-graph-control supplies universal constants C_hat >= 1 and kappa_hat in (0,1/2]. Therefore C_ch^0 := C_hat and kappa_ch^0 := kappa_hat satisfy the two range requirements in the root existential quantifier.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For every exact-unit epsilon_r-C*-algebra in the root, epsilon_r >= 0: by def-epsilon-cstar-algebra, J bold-dot J = J and ||J|| = 1, while the product-norm axiom at X=Y=J gives ||J bold-dot J|| <= (1+epsilon_r)||J||^2, hence 1 <= 1+epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** For delta > 0 set s := epsilon_r + delta and q := epsilon_r*delta + delta^2. By 1.1.2, s > 0 and q = delta*s > 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** Fix any def-stage1-polar-witness-data tuple W satisfying C_ch >= C_ch^0 and 0 < kappa_ch <= kappa_ch^0, and any root inputs satisfying C_ch*(epsilon_r+delta) <= kappa_ch. With the choices in 1.1.1 and s from 1.1.3, C_hat*s <= C_ch*s <= kappa_ch <= kappa_hat. Thus C_hat*(epsilon_r+delta) <= kappa_hat, exactly the smallness hypothesis of lem-stage1-unitary-graph-control.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.5

**Statement:** Under the same hypotheses, q >= 0 and s >= 0 imply C_hat*q <= C_ch*q and C_hat*s <= C_ch*s. Moreover C_ch*s <= kappa_ch <= kappa_hat <= 1/2 < 1, so C_ch*(epsilon_r+delta) < 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.6

**Statement:** Apply lem-stage1-unitary-graph-control with its constants C_hat,kappa_hat to the given algebra, delta, V in calUbar_delta, and A^par in B^{icalH}_{2delta}(0), using 1.1.4. It gives a unique g_V(A^par) in B^{calH}_{2delta}(0) satisfying the root-displayed formula f_V(A^par+g_V(A^par))=0; it puts V bold-dot (J+A^par+g_V(A^par)) in calU; it gives the three bounds with right sides C_hat*q, C_hat*s, and C_hat*s respectively; and its resulting C^1 graph charts cover calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.7

**Statement:** Use 1.1.5 to weaken the three C_hat-bounds from 1.1.6 to C_ch*q, C_ch*s, and C_ch*s, and append the strict inequality C_ch*s < 1. Existence, uniqueness, the displayed definition of f_V, membership in calU, and C^1 chart coverage are unchanged. Since W and all algebraic inputs were arbitrary, universal generalization together with the constants chosen in 1.1.1 proves the full root contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

