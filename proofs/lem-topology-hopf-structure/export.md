# Proof Export

## Node 1

**Statement:** Hopf structure theorem in the form consumed by Stage 1: a finite-dimensional connected graded-commutative bialgebra over a characteristic-zero field is an exterior algebra on odd-degree homogeneous generators.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let A be a finite-dimensional connected graded-commutative bialgebra over a characteristic-zero field F, where the compound phrase 'connected graded' is used in the nonnegative grading convention fixed by GT-hatcher-AT-hopf-algebra-definition: A = direct-sum_{n>=0} A_n and A_0 = F·1. Then A satisfies every hypothesis of GT-hatcher-AT-thm-3C.4, with 'Hopf algebra' understood exactly as in GT-hatcher-AT-hopf-algebra-definition.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By the standard meaning of graded bialgebra, A is a unital associative graded F-algebra and its coproduct Δ:A→A⊗_F A is a degree-preserving algebra homomorphism with counit ε; the stated graded-commutativity supplies Hatcher's commutativity in the graded sense.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Connectedness says A_0=F·1, with F→A_0, r↦r1, an isomorphism, exactly condition (1) of GT-hatcher-AT-hopf-algebra-definition.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** For homogeneous a∈A_n with n>0, degree preservation gives Δ(a)∈⊕_{i=0}^n A_i⊗A_{n-i}, while the graded counit ε:A→F vanishes on A_i for i>0. Because A_0=F·1, the endpoint components have forms b⊗1 and 1⊗c. Applying the counit identities (id⊗ε)Δ(a)=a=(ε⊗id)Δ(a), all positive-degree terms vanish and the endpoint coefficients are forced to be b=a=c. Every remaining summand has both tensor factors of positive degree. Thus Δ(a)=a⊗1+1⊗a+Σ_i a'_i⊗a''_i with |a'_i|,|a''_i|>0, exactly condition (2) of GT-hatcher-AT-hopf-algebra-definition.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** Total finite-dimensionality of A implies each graded piece A_n is finite-dimensional; together with the assumed characteristic zero and the preceding associative, graded-commutative Hopf-algebra conditions, this verifies all hypotheses of GT-hatcher-AT-thm-3C.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.5

**Statement:** Terminology check: the nonnegative grading is part of the hypothesis, not a consequence of A_0 = F·1. The allowed definition GT-hatcher-AT-hopf-algebra-definition begins with A = direct-sum_{n>=0} A_n; node 1.1 now explicitly adopts that convention for the compound phrase connected graded. Therefore A_n = 0 for n<0. In particular, exterior_Q(x) with |x|=-1 is a Z-graded counterexample only to a broader statement not asserted here, and is not an instance of node 1.1 or the root contract under its registered convention.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** By GT-hatcher-AT-thm-3C.4, A is isomorphic as an algebra to Λ_F(V_odd) ⊗_F F[V_even], where the exterior-algebra generators are homogeneous of odd degree and the polynomial-algebra generators are homogeneous of even degree.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The polynomial factor F[V_even] has no generators: otherwise the displayed tensor-product algebra, and hence A, would be infinite-dimensional over F, contrary to the hypothesis.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Suppose for contradiction that V_even contains a polynomial generator x. By the defining vector-space basis of a polynomial algebra, the monomials 1,x,x^2,… are linearly independent in F[V_even], so F[V_even] is infinite-dimensional over F.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** The map j:F[V_even]→Λ_F(V_odd)⊗_F F[V_even], p↦1⊗p, is injective: the exterior algebra has the augmentation ε_Λ sending 1 to 1 and every positive exterior degree to 0, and (ε_Λ⊗id)∘j=id.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Hence Λ_F(V_odd)⊗_F F[V_even] is infinite-dimensional; the isomorphism of 1.2 would make A infinite-dimensional, contradicting A's assumed total finite-dimensionality. Therefore V_even is empty.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Since the polynomial algebra on the empty generator set is F and Λ_F(V_odd) ⊗_F F is canonically Λ_F(V_odd), A is an exterior algebra on odd-degree homogeneous generators, as claimed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

