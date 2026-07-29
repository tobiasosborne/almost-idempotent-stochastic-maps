# Proof Export

## Node 1

**Statement:** There is a universal e_quot^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_quot^r and 1 < N = dim_C calX < infinity, breve-calU = calU_e/U(1) is a connected compact orientable smooth manifold without boundary of real dimension N - 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix the universal witness tuple W from lem-stage1-polar-constant-ledger and set e_quot^r = min{epsilon_*^r,1/4,kappa_ch/(4*C_ch)} > 0. For every exact-unit epsilon_r-C*-algebra with epsilon_r <= e_quot^r, take delta = kappa_ch/(4*C_ch). Then C_ch*(epsilon_r+delta) <= kappa_ch/2 < kappa_ch, so (A_2) of lem-stage1-polar-constant-ledger supplies covering C^1 graph maps with D_{A^perp}f invertible, lem-stage1-smooth-unitary-atlas upgrades these unchanged charts to a smooth embedded, boundaryless manifold calU, and lem-stage1-maurer-cartan-trivialization supplies its global bundle map omega.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For the bound fixed above, scalar multiplication a(c,U)=cU defines a smooth action U(1) x calU_e -> calU_e: conjugate-linearity of dagger and bilinearity give (cU)^dagger bold-dot (cU)=bar(c)c(U^dagger bold-dot U)=J; if U bold-dot R=J then (cU) bold-dot (bar(c)R)=J; the path t mapsto exp(it theta)J joins J to cJ for c=exp(i theta), and the homeomorphism U mapsto cU therefore preserves the connected component calU_e; finally ambient scalar multiplication is smooth and restricts/corestricts smoothly through the embedded atlas.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The smooth scalar action on calU_e is free and proper. Freeness follows because cU=U and a right inverse U bold-dot R=J imply cJ=(cU) bold-dot R=U bold-dot R=J, hence c=1 since ||J||=1. Properness follows from the standard compact-group argument: U(1) is compact, and for compact K in calU_e x calU_e the inverse image under (c,U) mapsto (cU,U) is a closed subset of U(1) x pr_2(K), hence compact.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** By lem-topology-quotient-manifold, the smooth free proper U(1)-action on the smooth boundaryless manifold calU_e gives breve-calU=calU_e/U(1) its unique smooth manifold structure for which the quotient map is a smooth submersion; its local quotient charts are Euclidean open sets, so the quotient has no boundary.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The real dimension of breve-calU is N-1. Indeed lem-stage1-maurer-cartan-trivialization identifies every T_U calU with icalH. The involution decomposition calX=calH direct-sum icalH over R and multiplication by i identify calH and icalH as real forms of the N-dimensional complex space calX, so dim_R(icalH)=N and dim_R(calU_e)=N. Since dim_R U(1)=1, the dimension formula in lem-topology-quotient-manifold gives dim_R breve-calU=N-1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** The quotient breve-calU is connected: calU_e is connected by its defining choice as the connected component of J, and the surjective quotient map calU_e -> breve-calU is continuous, so its image is connected.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** The spaces calU_e and breve-calU are compact. For epsilon_r <= e_quot^r <= 1/4, any U with U^dagger bold-dot U=J obeys (1-epsilon_r)||U||^2 <= 1. Moreover L_U is injective: if U bold-dot X=0, approximate associativity gives ||X|| <= epsilon_r||U||^2||X||, whose coefficient is at most epsilon_r/(1-epsilon_r)<1; finite dimensionality makes L_U surjective, so such U has a right inverse. Hence calU is exactly the closed zero locus of U mapsto U^dagger bold-dot U-J inside a bounded set, and is compact; its connected component calU_e is closed and compact. The continuous quotient of calU_e is compact.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** The quotient breve-calU is orientable. The U(1)-equivariant bundle trivialization of lem-stage1-maurer-cartan-trivialization satisfies omega_{cU}(cZ)=omega_U(Z) and sends the vertical orbit vector iU to iJ. Thus it descends through the quotient submersion to a continuous global vector-bundle isomorphism T breve-calU -> breve-calU x (icalH/R iJ), via [Z] mapsto [omega_U(Z)]; well-definedness uses the stated equivariance, and its kernel is exactly the vertical line because omega is a fibre isomorphism. Orient the fixed line R iJ by iJ and the fixed quotient icalH/R iJ once and for all; the descended trivialization gives a global orientation of breve-calU.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

