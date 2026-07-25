# Proof Export

## Node 1

**Statement:** Level-one one-dimensional corner product: there are universal C_PQR < infinity and e_PQR > 0 such that, for e=delta+epsilon <= e_PQR, if Q is one-dimensional then abs(||X dot Y||-||X||||Y||) <= C_PQR*e*||X||||Y|| for X in S_{P,Q} and Y in S_{Q,R}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Uniform definitional estimates: there are universal finite B,C0 and t0>0 such that, whenever e=delta+epsilon<=t0 and Q is one-dimensional, Q is nonvanishing, u=Co_Q(Q) satisfies abs(||u||-1)<=C0*e, every delta-projection has norm at most B, every compatible compressed product satisfies ||A dot B-AB||<=C0*e*||A||||B||, and every Y in S_{Q,R} satisfies ||uY-Y||<=C0*e*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Nonvanishing and compressed-unit bounds: def-one-dimensional-delta-projection and one-dimensional-projection-nonvanishing give that dim S_Q=1 implies Q is nonvanishing. Applying lem-compcb-corner-algebra with P=Q gives universal C_ca,e_ca and makes S_Q an extended gamma-C*-algebra, gamma=C_ca*e, with unit u=Co_Q(Q); hence the registered unit axiom gives abs(||u||-1)<=C_ca*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Uniform elementary bounds: the delta-projection dichotomy and e<=t imply a universal bound ||P||,||Q||,||R||<=B; the epsilon-Banach product and associator axioms then bound all products used below, while def-compressed-corner (compressed-product-display) supplies a universal C_dot and t_dot>0 with ||A dot B-AB||<=C_dot*e*||A||||B|| for each compatible pair.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Rectangular left-unit consequence: after shrinking the universal threshold, the definitions imply ||uY-Y||<=C_L*e*||Y|| for every Y in S_{Q,R}, with universal C_L.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.1

**Statement:** Compression of Q is close to Q: u=Co_Q(Q), and the defining estimate Co_Q(A)=Q(AQ)+O(e)||A|| together with ||Q^2-Q||<=delta, the epsilon-associator axiom, and the uniform projection bound from node 1.1.2 gives ||u-Q||<=C_uQ*e for a universal C_uQ.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.2

**Statement:** The left Q-action is close to the identity on S_{Q,R}: since Y=Co_{Q,R}(Y), the compression estimate gives ||Y-Q(YR)||<=C_dot*e*||Y||. Applying Q, then using Q^2=Q+O(delta), the epsilon-associator axiom, and the uniform projection bounds, yields ||QY-Y||<=C_QY*e*||Y|| with universal C_QY.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.3

**Statement:** Combine the preceding estimates with the epsilon-Banach product bound: ||uY-Y||<=||uY-QY||+||QY-Y||<=(1+epsilon)||u-Q||||Y||+C_QY*e*||Y||<=C_L*e*||Y|| after e<=1, for universal C_L.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** Choose C0=max{C_ca,C_dot,C_L,1}, B enlarged if necessary, and t0>0 below all preceding thresholds and below 1/(2*C0). Then all estimates asserted in node 1.1 hold simultaneously.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** One-dimensional scalarization and coefficient estimate: under the setup of node 1.1, for X in S_{P,Q} there is a real scalar h with X^dagger dot X=h*u, and abs(|h|-||X||^2)<=C1*e*||X||^2 for one universal finite C1 after a universal threshold shrink.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Exact scalarization: X^dagger lies in S_{Q,P} by the compression adjoint identity, so a:=X^dagger dot X lies in S_Q. Since dim S_Q=1 and ||u||>=1-C0*e>=1/2, u is nonzero and spans S_Q; hence a=h*u for a unique scalar h. The inherited involution gives a^dagger=a and u^dagger=u, so h is real.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Ambient-to-compressed square estimate: compressed-product-display and dagger isometry give ||a-X^dagger X||<=C0*e*||X||^2. The epsilon-C*-axioms give (1-e)||X||^2<=||X^dagger X||<=(1+e)||X||^2. Therefore abs(||a||-||X||^2)<=(C0+1)*e*||X||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Coefficient extraction: ||a||=|h|||u||, abs(||u||-1)<=C0*e, and ||u||>=1/2. The preceding square estimate first gives |h|<=2[1+(C0+1)e]||X||^2, and then abs(|h|-||X||^2)<=abs(|h|-|h|||u||)+abs(||a||-||X||^2)<=C1*e*||X||^2 for a universal finite C1 after e<=min{t0,1}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Squared-norm comparison: under nodes 1.1-1.2 there is one universal finite C2 such that W=X dot Y obeys abs(||W||^2-||X||^2||Y||^2)<=C2*e*||X||^2||Y||^2 for all X in S_{P,Q}, Y in S_{Q,R}, after a universal threshold shrink.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Reduction to the ambient square: put r=||X||, s=||Y||, Z=XY and W=X dot Y. The compressed-product estimate gives ||W-Z||<=C0*e*r*s, while the epsilon-product bound gives ||Z||<= (1+e)r*s and hence ||W||<=C_W*r*s for a universal C_W. Applying the epsilon-C*-lower axiom and the product upper bound to Z gives abs(||Z^dagger Z||-||Z||^2)<=e*||Z||^2. Therefore abs(||W||^2-||Z^dagger Z||)<=C3*e*r^2*s^2 for universal C3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Associator and scalar substitution: with a=X^dagger dot X=h*u from node 1.2, the epsilon-associator axiom, compressed-product closeness, and node 1.1 give ||(XY)^dagger(XY)-h*Y^dagger Y||<=C4*e*r^2*s^2 for a universal finite C4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Two uses of approximate associativity and exact involution give ||(XY)^dagger(XY)-Y^dagger((X^dagger X)Y)||<=C_as*e*r^2*s^2: indeed (XY)^dagger=Y^dagger X^dagger exactly, and both reassociations are bounded by epsilon times the four factor norms, with intermediate products bounded by the epsilon-product axiom.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.2

**Statement:** Since a=X^dagger dot X and compressed-product-display gives ||X^dagger X-a||<=C0*e*r^2, the product bound twice gives ||Y^dagger((X^dagger X)Y)-Y^dagger(aY)||<=C_a*e*r^2*s^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.3

**Statement:** By a=h*u, bilinearity gives Y^dagger(aY)=h*Y^dagger(uY). Node 1.1 gives ||uY-Y||<=C0*e*s, so the product bound and |h|<=C_h*r^2 from node 1.2 imply ||h*Y^dagger(uY)-h*Y^dagger Y||<=C_u*e*r^2*s^2. Summing the three errors proves node 1.3.2 with C4=C_as+C_a+C_u.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Scalar norm estimate: the epsilon-C*-axioms give abs(||Y^dagger Y||-s^2)<=e*s^2, while node 1.2 gives abs(|h|-r^2)<=C1*e*r^2 and also |h|<=C_h*r^2. Hence abs(||h*Y^dagger Y||-r^2*s^2)<=C5*e*r^2*s^2 for universal C5.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** Combining nodes 1.3.1-1.3.3 by the reverse triangle inequality yields abs(||W||^2-r^2*s^2)<=C2*e*r^2*s^2 with C2=C3+C4+C5.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Constant assembly and square-root passage: nodes 1.1-1.3 imply the root with universal e_PQR>0 and C_PQR<infinity.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Let e_PQR be a positive universal number no larger than every threshold used in nodes 1.1-1.3, and put C_PQR=C2. These constants are universal, positive/finite, and all preceding estimates hold whenever e<=e_PQR.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** If ||X||||Y||=0, then X=0 or Y=0 and bilinearity of the compressed product gives X dot Y=0, so the root estimate is exact. Otherwise, with r=||X|| and s=||Y||, node 1.3 and the identity |a-b|=|a^2-b^2|/(a+b) for nonnegative a,b give abs(||X dot Y||-r*s)<=C2*e*r^2*s^2/(||X dot Y||+r*s)<=C2*e*r*s. Together with node 1.4.1 this is precisely the root contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.2.1

**Statement:** Dependency-gated derivation: dependency 1.4.1 fixes universal e_PQR and C_PQR=C2 and ensures e<=e_PQR lies below every threshold used in dependency 1.3. Put r=||X|| and s=||Y||. If r*s=0, then X=0 or Y=0, and bilinearity of the compressed product gives X dot Y=0, so abs(||X dot Y||-r*s)=0. If r*s>0, dependency 1.3 gives abs(||X dot Y||^2-r^2*s^2)<=C2*e*r^2*s^2. Since ||X dot Y|| and r*s are nonnegative and their sum is at least r*s>0, factorization of the difference of squares yields abs(||X dot Y||-r*s)=abs(||X dot Y||^2-r^2*s^2)/(||X dot Y||+r*s)<=C2*e*r*s=C_PQR*e*||X||||Y||. The two exhaustive cases prove the asserted estimate with the constants from 1.4.1.

**Type:** qed

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

