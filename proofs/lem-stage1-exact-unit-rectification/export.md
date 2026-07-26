# Proof Export

## Node 1

**Statement:** Dimension-free exact-unit rectification: there are universal C_unit < infinity and e_unit > 0 such that every finite-dimensional epsilon_X-C*-algebra with epsilon_X <= e_unit admits on the same involutive normed space an exact unit J and product bold-dot with ||J-I_X|| <= C_unit*epsilon_X and ||x bold-dot y-xy|| <= C_unit*epsilon_X*||x||||y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix an epsilon_X-C*-algebra A as in def-epsilon-cstar-algebra and assume 0 <= epsilon_X <= 1/2. Put I=I_X, a=||I||, and J=I/a. The approximate-unit axiom gives |a-1|<=epsilon_X, hence a>=1/2, so J is defined; moreover ||J||=1, J^dagger=J because I^dagger=I, and ||J-I||=|1-a|<=epsilon_X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** There is a complex-linear functional phi:A->C with ||phi||=1, phi(J)=1, and phi(x^dagger)=overline(phi(x)) for every x. Indeed, complex Hahn-Banach gives a norm-one complex-linear psi with psi(J)=1. The map psi_sharp(x)=overline(psi(x^dagger)) is complex-linear of norm one, and phi=(psi+psi_sharp)/2 has norm at most one, is Hermitian, and takes value one at the norm-one vector J; therefore ||phi||=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** By validated node 1.1, ||J||=1 and J^dagger=J. On the one-dimensional complex subspace C J define g(alpha J)=alpha. Since ||alpha J||=|alpha|, g has norm one; complex Hahn-Banach extends g to a complex-linear psi:A->C with ||psi||=1 and psi(J)=1. Define psi_sharp(x)=overline(psi(x^dagger)). Because the involution is conjugate-linear and isometric, psi_sharp is complex-linear and ||psi_sharp||=||psi||=1 (the involution is bijective, being an involution). Self-adjointness of J now gives psi_sharp(J)=overline(psi(J^dagger))=overline(psi(J))=1. Thus phi=(psi+psi_sharp)/2 is complex-linear, satisfies ||phi||<=1 and phi(J)=1, and obeys phi(x^dagger)=overline(phi(x)) by direct expansion and (x^dagger)^dagger=x. Finally 1=|phi(J)|<=||phi||||J||=||phi||, so ||phi||=1. This proves exactly the assertion of node 1.2 and repairs the missing use of J^dagger=J.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Using J and phi from the preceding steps, define the bilinear product x bold-dot y := xy + phi(x)(y-Jy) + phi(y)(x-xJ) - phi(x)phi(y)(J-JJ). Then J bold-dot y=y and x bold-dot J=x for all x,y, by substituting phi(J)=1 and cancelling the two copies of J-JJ. Thus J is a two-sided exact unit; together with ||J||=1 and J^dagger=J this is the exact-unit condition of def-epsilon-cstar-algebra. The unchanged involution is compatible with bold-dot: Hermiticity of phi, (xy)^dagger=y^dagger x^dagger, J^dagger=J, and (JJ)^dagger=JJ give (x bold-dot y)^dagger=y^dagger bold-dot x^dagger term by term. Hence the construction is on the same involutive normed space.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For any z, the product-norm and approximate-unit axioms in def-epsilon-cstar-algebra and ||J-I||<=epsilon_X give ||Jz-z|| <= ||(J-I)z||+||Iz-z|| <= ((1+epsilon_X)epsilon_X+epsilon_X)||z||=(2+epsilon_X)epsilon_X||z||, and likewise ||zJ-z|| <= (2+epsilon_X)epsilon_X||z||. Taking z=J also gives ||J-JJ|| <= (2+epsilon_X)epsilon_X because ||J||=1. Since ||phi||=1, the defining correction therefore satisfies ||x bold-dot y-xy|| <= 3(2+epsilon_X)epsilon_X||x||||y|| <= (15/2)epsilon_X||x||||y|| <= 8epsilon_X||x||||y||. Along with ||J-I_X||<=epsilon_X<=8epsilon_X, this proves the root with the universal choices e_unit=1/2 and C_unit=8.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

