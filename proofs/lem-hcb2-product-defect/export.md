# Proof Export

## Node 1

**Statement:** Uniform amplified Ha product defect: there are universal C_prod < infinity and e_prod > 0 such that every H-CB datum with e <= e_prod, every n >= 1, Z in M_n tensor S_{P,S}, and W in M_n tensor S_{S,R} satisfy ||(Ha^Q_{P,R})_n(Z dot W)-(Ha^Q_{P,S})_n(Z)(Ha^Q_{S,R})_n(W)|| <= C_prod*e*||Z||||W||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Amplified column control from the allowed definitions and imports: there are universal e_q>0, K_0:=2+C_co, and K_mul:=4*K_0 such that, if e<=min{e_q,e_co,1}, then every amplified column X satisfies (1/2)||X||<=q_T(X)<=2||X||, every compatible amplified product satisfies ||A dot B||<=K_0||A||||B||, and every compatible square-by-column product satisfies q_P(A dot X)<=K_mul||A||q_R(X). This uses lem-compcb-amplified-compression and lem-compcb-rectangular-product, together with the registered definitions column-hilbert-inner-product-displays, compressed-product-display, epsilon-banach-cstar-norm-axioms, nonvanishing-delta-projection, and one-dimensional-projection-nonvanishing.

**Type:** claim

**Inference:** norm comparison and triangle inequality

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** For X in M_{n,1} tensor S_{T,Q}, lem-compcb-amplified-compression identifies the column corner at level n, and column-hilbert-inner-product-displays gives the exact whole-column identity X^dagger dot X=q_T(X)^2*u_Q. Lem-compcb-rectangular-product and epsilon-banach-cstar-norm-axioms then give | ||X^dagger dot X||-||X||^2 |<=(C_co+1)e||X||^2: compare X^dagger dot X to X^dagger X, use ||X^dagger||=||X||, and use (1-epsilon)||X||^2<=||X^dagger X||<=(1+epsilon)||X||^2.

**Type:** claim

**Inference:** by definitions and norm triangle inequality

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Because Q is one-dimensional it is nonvanishing by one-dimensional-projection-nonvanishing; compressed-product-display therefore makes u_Q the unit of its O(e)-C*-corner, so the registered unit norm axiom yields a universal C_u and threshold with | ||u_Q||-1|<=C_u e. Combining this with node 1.1.1 and ||q_T(X)^2*u_Q||=q_T(X)^2||u_Q||, choose a universal e_q>0 so that (1/2)||X||<=q_T(X)<=2||X|| for every n and every amplified column X.

**Type:** claim

**Inference:** positive scalar cancellation

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** If e<=min{e_co,1}, then lem-compcb-rectangular-product and ||AB||<=(1+epsilon)||A||||B|| imply ||A dot B||<=(1+epsilon+C_co*e)||A||||B||<=K_0||A||||B|| with K_0=2+C_co. For a square-by-column pair, node 1.1.2 gives q_P(A dot X)<=2||A dot X||<=2K_0||A||||X||<=4K_0||A||q_R(X)=K_mul||A||q_R(X).

**Type:** claim

**Inference:** triangle inequality and norm conversion

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Uniform Ha upper bound: under the threshold of node 1.1 and e<=min{e_act,1}, lem-hcb1-column-action and node 1.1 give ||(Ha^Q_{A,B})_n(U)||_op<=K_H||U|| for every amplified corner element U, where K_H:=K_mul+C_act is universal.

**Type:** claim

**Inference:** triangle inequality and operator norm

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Pointwise product-defect estimate: under all thresholds in nodes 1.1-1.2 and e<=e_as, for every X in M_{n,1} tensor S_{R,Q}, q_P(((Ha^Q_{P,R})_n(Z dot W)-(Ha^Q_{P,S})_n(Z)(Ha^Q_{S,R})_n(W))X)<=C_* e||Z||||W||q_R(X), where C_*:=C_act*K_0+4*C_as+C_act*K_mul+C_act*K_H.

**Type:** claim

**Inference:** four-term telescoping estimate

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Write H_{A,B}(U):=(Ha^Q_{A,B})_n(U). For every column X the following identity is exact by adding and subtracting compressed multiplications: [H_{P,R}(Z dot W)-H_{P,S}(Z)H_{S,R}(W)]X = [H_{P,R}(Z dot W)X-(Z dot W) dot X]+[(Z dot W) dot X-Z dot(W dot X)]+Z dot[W dot X-H_{S,R}(W)X]+[Z dot H_{S,R}(W)X-H_{P,S}(Z)H_{S,R}(W)X].

**Type:** claim

**Inference:** algebraic telescoping identity

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** The first summand of node 1.3.1 is at most C_act*e||Z dot W||q_R(X)<=C_act*K_0*e||Z||||W||q_R(X) by lem-hcb1-column-action and node 1.1.3. The second is at most 4*C_as*e||Z||||W||q_R(X): lem-hcb0-compressed-associator gives the ambient bound C_as*e||Z||||W||||X||, while node 1.1.2 gives q_P<=2|| || and ||X||<=2q_R(X).

**Type:** claim

**Inference:** application of validated imports and norm conversion

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** The third summand of node 1.3.1 is at most K_mul*C_act*e||Z||||W||q_R(X): apply the square-by-column multiplier bound in node 1.1.3 to Z and then lem-hcb1-column-action to W. The fourth is at most C_act*K_H*e||Z||||W||q_R(X): apply lem-hcb1-column-action to Z with column H_{S,R}(W)X, then apply the Ha operator bound in node 1.2 to W.

**Type:** claim

**Inference:** two applications of column action

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** Apply q_P triangle inequality to the exact identity in node 1.3.1 and add the four bounds in nodes 1.3.2-1.3.3. The coefficient is C_act*K_0+4*C_as+C_act*K_mul+C_act*K_H=C_*, proving the pointwise estimate stated in node 1.3.

**Type:** claim

**Inference:** triangle inequality and arithmetic

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Choose e_prod:=min{e_cmp,e_co,e_as,e_act,e_q,1}>0 and C_prod:=C_*<infinity. For arbitrary data in the root contract with e<=e_prod, lem-compcb-amplified-compression makes all matrix-level corners and compressed products in nodes 1.1-1.3 the required compatible amplified objects; taking the supremum of node 1.3 over q_R(X)=1 and using the operator norm in def-ha-map proves the root estimate, uniformly in n and the datum.

**Type:** claim

**Inference:** universal generalization and operator norm

**Status:** validated

**Taint:** clean

