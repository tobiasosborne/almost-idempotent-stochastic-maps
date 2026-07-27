# Proof Export

## Node 1

**Statement:** Parameterized rectification transport: there exist C_rect^0 >= 1 and e_rect^0 in (0, 1/C_rect^0] such that, for every def-stage1-polar-witness-data tuple W with C_rect >= C_rect^0 and 0 < e_rect <= min{e_rect^0, 1/C_rect}, for every finite-dimensional epsilon_X-C*-algebra (calX, I_X, ., dagger) with 0 <= epsilon_X <= e_rect, there are on the same involutive normed space a bilinear product bold-dot and an element J = J^dagger for which (calX, J, bold-dot, dagger) satisfies every exact-unit epsilon_r-C*-algebra axiom of def-epsilon-cstar-algebra, including ||J|| = 1, where epsilon_r = C_rect*epsilon_X, and for every x, y in calX, ||J - I_X|| <= C_rect*epsilon_X and ||x bold-dot y - xy|| <= C_rect*epsilon_X*||x||*||y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Invoke the external lem-stage1-rectified-cstar-control and existentially instantiate its universal witnesses as constants c >= 1 and e in (0, 1/c]. Thus every finite-dimensional epsilon_X-C*-algebra with 0 <= epsilon_X <= e admits, on the same involutive normed space, a bilinear product bold-dot and J = J^dagger satisfying every exact-unit alpha-C*-algebra axiom of def-epsilon-cstar-algebra, including ||J|| = 1, for alpha = c*epsilon_X, together with ||J-I_X|| <= c*epsilon_X and ||x bold-dot y-xy|| <= c*epsilon_X*||x||*||y|| for all x,y.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Parameter monotonicity for the registered def-epsilon-cstar-algebra: if 0 <= alpha <= beta and (calX,J,bold-dot,dagger) satisfies every exact-unit alpha-C*-algebra axiom, then it satisfies every exact-unit beta-C*-algebra axiom. Indeed, ||x bold-dot y|| <= (1+alpha)||x||||y|| <= (1+beta)||x||||y||; the associator bound alpha||x||||y||||z|| is at most beta||x||||y||||z||; and ||x^dagger bold-dot x|| >= (1-alpha)||x||^2 >= (1-beta)||x||^2. The underlying complex Banach-space structure, bilinearity, conjugate-linearity, involutivity, isometry, anti-multiplicativity, both exact unit identities, J^dagger=J, and ||J||=1 are parameter-free requirements and remain unchanged.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Fix an arbitrary def-stage1-polar-witness-data tuple W satisfying C_rect >= c and 0 < e_rect <= min{e,1/C_rect}, and an arbitrary finite-dimensional epsilon_X-C*-algebra with 0 <= epsilon_X <= e_rect. Then epsilon_X <= e_rect <= e, so the external producer applies. Moreover epsilon_X >= 0 and C_rect >= c imply 0 <= alpha:=c*epsilon_X <= beta:=C_rect*epsilon_X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Apply lem-stage1-rectified-cstar-control to the algebra fixed in the preceding step. It supplies on the same involutive normed space a bilinear product bold-dot and J=J^dagger satisfying every exact-unit alpha-C*-algebra axiom, including ||J||=1, with alpha=c*epsilon_X, and satisfying ||J-I_X|| <= c*epsilon_X and ||x bold-dot y-xy|| <= c*epsilon_X*||x||*||y|| for every x,y.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** For the witnesses from the preceding step, apply parameter monotonicity to alpha <= beta, where beta=C_rect*epsilon_X. They therefore satisfy every exact-unit beta-C*-algebra axiom, including ||J||=1. Since c <= C_rect, epsilon_X >= 0, and ||x||||y|| >= 0, the producer estimates imply ||J-I_X|| <= C_rect*epsilon_X and ||x bold-dot y-xy|| <= C_rect*epsilon_X*||x||*||y|| for all x,y. With epsilon_r:=beta, this is exactly the required conclusion for the fixed W and input algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Set C_rect^0:=c and e_rect^0:=e. The first step gives C_rect^0 >= 1 and 0 < e_rect^0 <= 1/C_rect^0. Because W and the input algebra in the preceding steps were arbitrary under the contract hypotheses, universal generalization followed by existential generalization proves the root statement.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

