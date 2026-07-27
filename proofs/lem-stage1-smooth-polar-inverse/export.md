# Proof Export

## Node 1

**Statement:** Smooth polar-inverse upgrade: for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0, if lem-stage1-smooth-unitary-atlas gives the smooth embedded atlas and Pi_delta: calU x B^{calH}_delta(J) -> S_delta is the bijective C^1 local diffeomorphism of lem-stage1-polar-retraction onto an open set, then the same ambient-bilinear Pi_delta is a smooth diffeomorphism and its same set-theoretic inverse (u_delta, h_delta) is smooth; no point or first derivative is changed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Under the antecedent of node 1, lem-stage1-smooth-unitary-atlas supplies on calU the same smooth embedded graph atlas as its C^1 atlas, with no point or first derivative changed; B^{calH}_delta(J) is an open subset of the finite-dimensional real vector space calH, so calU x B^{calH}_delta(J) has the product smooth structure, while S_delta is an open subset of the finite-dimensional ambient space by lem-stage1-polar-retraction and has its open-subset smooth structure.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By lem-stage1-smooth-unitary-atlas, under its stated hypotheses the existing C^1 graph charts cover calU and the same graph functions and charts form a smooth embedded-manifold atlas, without changing any point or first derivative.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** By def-approximate-unitary-space, calH is the Hermitian real linear subspace of the finite-dimensional ambient complex vector space; hence calH is finite-dimensional over R and B^{calH}_delta(J) is an open subset of calH with its standard smooth structure.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** By lem-stage1-polar-retraction, S_delta is open in the finite-dimensional ambient space, hence has the standard open-subset smooth structure.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** The standard product construction applied to the smooth manifold calU and the open manifold B^{calH}_delta(J) gives the asserted product smooth structure on calU x B^{calH}_delta(J); together with the preceding open-subset structure on S_delta this proves node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Under the antecedent of node 1, the unchanged map Pi_delta(U,H)=U bold-dot H is smooth from calU x B^{calH}_delta(J) to S_delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** By def-epsilon-cstar-algebra, the ambient multiplication m(X,Y)=X bold-dot Y is bilinear. After choosing real bases in the finite-dimensional source and target spaces, each coordinate of m has the form sum_{i,j} c_{kij} x_i y_j, a polynomial; therefore m is C^infinity as a map of the underlying finite-dimensional real vector spaces.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Take any product chart on calU x B^{calH}_delta(J) furnished by the unchanged smooth embedded atlas from lem-stage1-smooth-unitary-atlas and the identity chart on the ball, and use the ambient identity chart on the open set S_delta. In these coordinates Pi_delta is (x,H) maps to m(iota(psi^{-1}(x)),H), where iota composed with psi^{-1} is the smooth ambient parametrization of the embedded-manifold chart; the finite-coordinate polynomial formula from the preceding step and closure of smooth maps under composition show this coordinate representative is smooth. Since such charts cover the domain and Pi_delta has values in S_delta by lem-stage1-polar-retraction, Pi_delta is smooth.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Under the antecedent of node 1, D Pi_delta is a linear isomorphism at every point: this follows from the C^1 local-diffeomorphism assertion of lem-stage1-polar-retraction by differentiating a local C^1 inverse identity in charts.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Fix a point p of calU x B^{calH}_delta(J). By the C^1 local-diffeomorphism assertion in lem-stage1-polar-retraction, there are neighborhoods of p and Pi_delta(p) on which Pi_delta has a C^1 inverse G, so in local Euclidean charts G composed with Pi_delta and Pi_delta composed with G are identity maps.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Applying the ordinary chain rule at p and Pi_delta(p) to those two identities gives DG_{Pi_delta(p)} composed with DPi_delta_p = I and DPi_delta_p composed with DG_{Pi_delta(p)} = I. Thus DPi_delta_p is a linear isomorphism; since p was arbitrary, this holds everywhere.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Under the antecedent of node 1, the bijection Pi_delta has a smooth inverse, and that inverse is exactly the already supplied set-theoretic pair (u_delta,h_delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Fix p in calU x B^{calH}_delta(J), put q=Pi_delta(p), and choose smooth charts alpha:W -> U subset R^n and beta:Z -> V subset R^n about p and q, shrinking W so Pi_delta(W) subset Z. By node 1.2 the coordinate map F=beta composed with Pi_delta composed with alpha^{-1} is smooth, and by node 1.3 its derivative at alpha(p) is invertible.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Apply GT-lee-2ed-thm-C.34 to F at alpha(p). It yields open neighborhoods U_0 of alpha(p) and V_0 of beta(q) on which F is a smooth diffeomorphism; translating through alpha and beta, Pi_delta therefore has a smooth local inverse near q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** By the bijectivity assertion of lem-stage1-polar-retraction, the global set-theoretic inverse G=Pi_delta^{-1} exists. On every local target neighborhood obtained in the preceding step, G equals the unique smooth local inverse there. These neighborhoods cover S_delta as p ranges over the domain, so G is smooth because smoothness is local; this is exactly the local-gluing argument recorded in GT-lee-2ed-cor-C.36(b).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.4

**Statement:** The inverse furnished by lem-stage1-polar-retraction is the pair (u_delta,h_delta). Since a bijection has only one set-theoretic inverse, the smooth global inverse G just obtained is exactly (u_delta,h_delta), proving node 1.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Under the antecedent of node 1, the smooth upgrade changes no point and no first derivative: lem-stage1-smooth-unitary-atlas retains the same graph charts through first order, Pi_delta remains the identical ambient-bilinear map, and its inverse remains the identical C^1 set map (u_delta,h_delta), so uniqueness of derivatives gives the same first derivatives.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** The external lemma lem-stage1-smooth-unitary-atlas expressly uses the same graph functions and graph charts as the C^1 atlas and changes no graph point or first derivative, so the source manifold upgrade is identity-on-data through first order.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** The map in both lem-stage1-polar-retraction and the present conclusion is literally Pi_delta(U,H)=U bold-dot H on the same domain and codomain, and the inverse in both is the unique set-theoretic inverse (u_delta,h_delta); thus none of these functions or their point values is replaced.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.3

**Statement:** Before the upgrade these identical maps are C^1 by lem-stage1-polar-retraction. The derivative at a point is determined uniquely by the underlying C^1 function and the unchanged first-order charts, so merely proving that these same functions are C^infinity cannot change any first derivative. Together with the preceding two steps this proves node 1.5.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

