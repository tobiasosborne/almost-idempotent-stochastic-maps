# Proof Export

## Node 1

**Statement:** Canonical corner Gram estimate: there are universal C_J < infinity and e_J > 0 such that every H-CB datum with e <= e_J, every n >= 1, and every Z in either special P,Q corner satisfy (1-C_J*e)||Z|| <= ||J_n(Z)|| <= (1+C_J*e)||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Column-corner estimate: there are universal C_col<infinity and e_col>0 such that for every H-CB datum with e<=e_col, every n>=1, and every Z in M_n tensor S_{P,Q}, (1-C_col e)||Z|| <= ||J_{P,Q,n}(Z)|| <= (1+C_col e)||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Exact Gram scalarization: for Z in M_n tensor S_{P,Q}, let G=J_{P,Q,n}(Z)^dagger J_{P,Q,n}(Z). By def-canonical-corner-identifications, column-hilbert-inner-product-displays, and compressed-product-display, entrywise [Z^dagger dot Z]_{ij}=sum_k <Z_{ki},Z_{kj}>u_Q=G_{ij}u_Q, hence Z^dagger dot Z=G tensor u_Q. By operator-space-matrix-norm-axioms (Ruan scalar-tensor invariance), ||G tensor u_Q||=||G|| ||u_Q||; by the Hilbert-space Gram identity, ||G||=||J_{P,Q,n}(Z)||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Uniform compressed-square and unit estimates: after shrinking to a universal threshold, there are universal A,B<infinity such that every Z in M_n tensor S_{P,Q} satisfies abs(||Z^dagger dot Z||-||Z||^2)<=A e ||Z||^2 and abs(||u_Q||-1)<=B e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** Compressed-square estimate from lem-compcb-rectangular-product and def-extended-epsilon-cstar-algebra together with epsilon-banach-cstar-norm-axioms and operator-space-matrix-norm-axioms: at level n, ||Z^dagger Z|| lies between (1-epsilon)||Z||^2 and (1+epsilon)||Z||^2. The external lem-compcb-rectangular-product applied to the compatible amplified pair (Z^dagger,Z) gives ||Z^dagger dot Z-Z^dagger Z||<=C_r e||Z||^2. Since epsilon<=e, the reverse triangle inequality yields abs(||Z^dagger dot Z||-||Z||^2)<=(C_r+1)e||Z||^2, uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.2

**Statement:** Compressed-unit estimate from lem-compcb-compressed-unit-norm: the one-dimensional delta-projection Q is nonvanishing by the registered one-dimensional-projection-nonvanishing definition, so for e below the external lemma threshold abs(||u_Q||-1)<=C_u e. Thus the unit part of node 1.1.2 holds with the universal choice B=C_u.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Scalar conclusion from nodes 1.1.1 and 1.1.2: if Z is nonzero and x=||J_{P,Q,n}(Z)||/||Z||, then x^2||u_Q||=||Z^dagger dot Z||/||Z||^2. Thus x^2 is between (1-Ae)/(1+Be) and (1+Ae)/(1-Be). Choose e_col no larger than the external thresholds, 1/(2 max(B,1)), and 1/max(A+B,1). Then x^2>=1-(A+B)e and x^2<=1+2(A+B)e; sqrt(1-t)>=1-t for 0<=t<=1 and sqrt(1+t)<=1+t/2 give 1-(A+B)e<=x<=1+(A+B)e. The assertion is trivial for Z=0, so C_col=A+B works.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Row-corner transfer: the column-corner estimate implies, with the same universal constants and threshold, (1-C_col e)||Z|| <= ||J_{Q,P,n}(Z)|| <= (1+C_col e)||Z|| for every Z in M_n tensor S_{Q,P}, by the defining adjunction J_{Q,P,n}(Z)=J_{P,Q,n}(Z^dagger)^dagger.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For Z in M_n tensor S_{Q,P}, put W=Z^dagger in M_n tensor S_{P,Q}. The registered self-adjoint operator-space axiom gives ||W||=||Z|| at every level, the definition def-canonical-corner-identifications gives J_{Q,P,n}(Z)=J_{P,Q,n}(W)^dagger, and operator adjunction preserves norm. Applying node 1.1 to W therefore gives both claimed row inequalities with exactly the same constants.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

