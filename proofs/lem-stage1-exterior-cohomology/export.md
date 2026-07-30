# Proof Export

## Node 1

**Statement:** Exterior cohomology of a finite H-space over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity and (M,mu,e) is an H-space, set A=H^*(M;reals), A^+=direct_sum_{k>0} A^k, and Delta=(cross product)^(-1) o mu^*; then A is a finite-dimensional graded-commutative associative unital algebra with A^0=reals*1, Delta:A->A tensor_reals A is a degree-preserving unital algebra homomorphism with Delta(1)=1 tensor 1, for every homogeneous a in A^+ there exist a finite set J_a and homogeneous a'_j,a''_j in A^+ for j in J_a such that Delta(a)=a tensor 1+1 tensor a+sum_{j in J_a} a'_j tensor a''_j, and A is isomorphic as a graded algebra to an exterior algebra on a finite family of odd-positive-degree homogeneous generators.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** By the established external lem-stage1-hspace-coproduct-tail, under the hypotheses of node 1 the asserted entire coproduct-tail package holds: A is finite-dimensional, graded-commutative, associative, and unital with A^0=reals*1; Delta is a degree-preserving unital algebra homomorphism with Delta(1)=1 tensor 1; and every homogeneous positive-degree a has the displayed finite positive-positive tail expansion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** The data in node 1.1 satisfy the hypotheses of GT-hatcher-hopf-structure-3C4: over the characteristic-zero field reals, A is a commutative associative Hopf algebra in the precise weak sense of GT-hatcher-weak-hopf-conditions (connectedness A^0=reals*1 and the graded-algebra coproduct with positive-positive tail), and every graded piece A^n is finite-dimensional because A is finite-dimensional in total.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Applying GT-hatcher-hopf-structure-3C4 to node 1.2 yields an algebra isomorphism phi from Lambda_reals(x_i | i in I) tensor_reals reals[y_j | j in J] onto A, where each x_i maps to a homogeneous odd-degree element of A and each y_j maps to a homogeneous even-degree element of A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The isomorphism phi of node 1.3 is degree-preserving: give each formal generator the degree of its homogeneous image; phi preserves degree on every monomial because multiplication in A adds degrees, and these monomials span the tensor product. Hence phi is an isomorphism of graded algebras.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The polynomial-generator family J in node 1.3 is empty. If y_j existed, the polynomial-algebra factor would contain the linearly independent powers 1,y_j,y_j^2,...; tensoring them with the nonzero exterior unit would give infinitely many linearly independent elements, contradicting the finite-dimensionality of A through phi.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** The exterior-generator family I in node 1.3 is finite. If I were infinite, its distinct exterior-word-length-one monomials x_i would be linearly independent, and after tensoring with the polynomial unit their images under phi would make A infinite-dimensional, contradicting node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** By nodes 1.3--1.6, phi restricts to a graded-algebra isomorphism from the exterior algebra on the finite family (x_i)_{i in I} of odd-positive-degree homogeneous generators onto A; together with the full coproduct-tail package already obtained in node 1.1, this proves every clause of node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

