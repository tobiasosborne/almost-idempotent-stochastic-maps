# Proof Export

## Node 1

**Statement:** Uniform compressed associator: there are universal C_as < infinity and e_as > 0 such that every H-CB datum with e <= e_as and all compatible amplified rectangular A,B,C satisfy ||(A dot B) dot C-A dot (B dot C)|| <= C_as*e*||A||||B||||C||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let C_co<infinity and e_co>0 be the universal constants supplied by lem-compcb-rectangular-product, and set e_as=min(e_co,1) and C_as=2*C_co*(2+C_co)+4*C_co+1; these are universal, finite, and e_as>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By lem-compcb-rectangular-product, there exist universal C_co<infinity and e_co>0 for which, whenever e<=e_co, every compatible amplified rectangular pair X,Y obeys ||X dot Y-XY||<=C_co*e*||X||||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Because the minimum of two positive universal constants is positive and universal, e_as=min(e_co,1)>0; because finite universal constants are closed under addition and multiplication, C_as=2*C_co*(2+C_co)+4*C_co+1 is finite and universal.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix an H-CB datum with e=delta+epsilon<=e_as and compatible amplified rectangular A,B,C. Then ||A dot B|| <= (1+epsilon+C_co*e)||A||||B|| and ||B dot C|| <= (1+epsilon+C_co*e)||B||||C||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Applying lem-compcb-rectangular-product to the compatible pair A,B and using e<=e_as<=e_co gives ||A dot B-AB||<=C_co*e||A||||B||; the triangle inequality and ||AB||<=(1+epsilon)||A||||B|| from the epsilon-Banach-C*-norm axioms therefore give ||A dot B||<=(1+epsilon+C_co*e)||A||||B||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** The identical argument applied to the compatible pair B,C gives ||B dot C||<=(1+epsilon+C_co*e)||B||||C||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The compressed associator has the exact telescoping expansion ((A dot B) dot C-(A dot B)C)+(((A dot B)C-(AB)C))+(((AB)C-A(BC)))+(A(BC)-A(B dot C))+(A(B dot C)-A dot (B dot C)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For the five summands in that expansion, their norms are respectively at most C_co*e*(1+epsilon+C_co*e)||A||||B||||C||, (1+epsilon)*C_co*e||A||||B||||C||, epsilon||A||||B||||C||, (1+epsilon)*C_co*e||A||||B||||C||, and C_co*e*(1+epsilon+C_co*e)||A||||B||||C||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** For the compatible pair A dot B,C, lem-compcb-rectangular-product gives ||(A dot B) dot C-(A dot B)C||<=C_co*e||A dot B||||C||; substituting node 1.2's bound for ||A dot B|| yields the first stated estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Bilinearity gives (A dot B)C-(AB)C=(A dot B-AB)C. The epsilon-Banach-C*-norm bound and lem-compcb-rectangular-product for A,B give its norm at most (1+epsilon)||A dot B-AB||||C||<=(1+epsilon)C_co*e||A||||B||||C||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** The epsilon-Banach-C*-associator axiom applied to A,B,C is exactly ||(AB)C-A(BC)||<=epsilon||A||||B||||C||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.4

**Statement:** Bilinearity gives A(BC)-A(B dot C)=A(BC-B dot C). The epsilon-Banach-C*-norm bound and lem-compcb-rectangular-product for B,C give its norm at most (1+epsilon)||A||||BC-B dot C||<=(1+epsilon)C_co*e||A||||B||||C||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.5

**Statement:** For the compatible pair A,B dot C, lem-compcb-rectangular-product gives ||A dot (B dot C)-A(B dot C)||<=C_co*e||A||||B dot C||; symmetry of the norm under sign and node 1.2's bound for ||B dot C|| yield the fifth stated estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The triangle inequality, epsilon<=e<=1, and C_co*e<=C_co imply the associator norm is at most [2*C_co*(2+C_co)+4*C_co+1]e||A||||B||||C||=C_as*e||A||||B||||C||, completing the uniform estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Applying the triangle inequality to node 1.3 and then node 1.4 gives the coefficient [2*C_co*(1+epsilon+C_co*e)+2*(1+epsilon)*C_co+epsilon/e] multiplying e||A||||B||||C|| (with the epsilon term bounded directly by e, so no division is needed when e=0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.1.1

**Statement:** Let N=||A||||B||||C|| and denote the five summands of the validated telescoping expansion in node 1.3, in order, by T1,...,T5. Independently of node 1.4, the permitted inputs establish all five estimates: for the compatible pairs (A dot B,C) and (A,B dot C), lem-compcb-rectangular-product together with validated nodes 1.2.1 and 1.2.2 gives ||T1||<=C_co*e*(1+epsilon+C_co*e)N and ||T5||<=C_co*e*(1+epsilon+C_co*e)N; bilinearity gives T2=(A dot B-AB)C and T4=A(BC-B dot C), so the epsilon-Banach-C*-norm bound and lem-compcb-rectangular-product for (A,B) and (B,C) give ||T2||<=(1+epsilon)C_co*e*N and ||T4||<=(1+epsilon)C_co*e*N; finally the epsilon-Banach-C*-associator axiom gives ||T3||<=epsilon*N.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.1.2

**Statement:** Using node 1.3 and the five estimates just established in node 1.5.1.1, the triangle inequality yields ||(A dot B) dot C-A dot (B dot C)|| <= {2*C_co*e*(1+epsilon+C_co*e)+2*(1+epsilon)*C_co*e+epsilon}||A||||B||||C||. If e>0 this is exactly the coefficient [2*C_co*(1+epsilon+C_co*e)+2*(1+epsilon)*C_co+epsilon/e] times e||A||||B||||C||. If e=0, then 0<=epsilon<=e gives epsilon=0 and every displayed error bound is zero, so the same conclusion holds without forming epsilon/e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Since 0<=epsilon<=e<=1, one has 1+epsilon+C_co*e<=2+C_co, 1+epsilon<=2, and epsilon<=e; hence the preceding sum is at most [2*C_co*(2+C_co)+4*C_co+1]e||A||||B||||C||=C_as*e||A||||B||||C||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.5.2.1

**Statement:** Let C_co^old and e_co be witnesses supplied by lem-compcb-rectangular-product, and set C_co:=max{C_co^old,0}. This replacement preserves the upstream estimate: since e>=0 and ||A||||B||>=0, C_co>=C_co^old implies C_co^old*e*||A||||B||<=C_co*e*||A||||B||, so ||A dot B-AB||<=C_co*e*||A||||B|| still holds for every compatible pair. Thus C_co is finite, universal, and nonnegative, and all occurrences of C_co in this proof may and shall denote this normalized witness.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

