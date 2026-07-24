# Proof Export

## Node 1

**Statement:** Uniform compressed-corner algebra: there are universal C_ca < infinity and e_ca > 0 such that, whenever e=delta+epsilon <= e_ca and P is a nonvanishing delta-projection, S_P with the compressed product, inherited involution, and compressed unit u_P=Co_P(P) is an extended C_ca*e-C*-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Constant ledger and amplified setup. Let the ambient algebra implicit in the delta-projection hypothesis be the extended epsilon-C*-algebra A. Let C_r,e_r; C_u,e_u; C_N,e_N be universal witnesses supplied respectively by lem-compcb-rectangular-product, lem-compcb-compressed-unit-action, and lem-compcb-compressed-unit-norm, and let e_i be supplied by lem-compcb-amplified-compression-identities. Put K_p=C_r+1, K_a=2*C_r*(K_p+3)+1, C_ca=max{K_p,K_a,C_u,C_N}, and e_ca=min{e_r,e_u,e_N,e_i,1}. These are universal with C_ca finite and e_ca>0. For e=delta+epsilon<=e_ca and every n>=1, put P_n=I_n tensor P. The amplification-naturality calculation in child 1.1.1, derived directly from def-compressed-corner and the registered theta functional calculus, proves Co_{P_n}=id_{M_n} tensor Co_P, hence S_{P_n}=M_n tensor S_P, compatibility of compressed products and units, and that P_n is a delta-projection in M_n tensor A. Thus every cited external applies on every matrix level.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Amplification naturality derived from the allowed definitions (not imported as an extra lemma). Write T_P=L_P R_P+R_P L_P-1, so def-compressed-corner gives Co_P=theta(T_P). On M_n tensor A, multiplication by P_n=I_n tensor P acts entrywise; hence T_{P_n}([X_ij])=[T_P(X_ij)], i.e. T_{P_n}=id_{M_n} tensor T_P. For every scalar x_0 and k>=0, induction gives (T_{P_n}-x_0 I)^k=id_{M_n} tensor (T_P-x_0 I)^k. Therefore every partial sum in the power-series functional calculus from theta-idempotent-approximation-map is the amplification of the corresponding partial sum at level one; taking the norm-convergent limits (at this fixed finite n) gives theta(T_{P_n})=id_{M_n} tensor theta(T_P), hence Co_{P_n}=id_{M_n} tensor Co_P. Consequently Image(Co_{P_n}) consists exactly of matrices [X_ij] with every X_ij in Image(Co_P), so S_{P_n}=M_n tensor S_P. Moreover, for X=[X_ij],Y=[Y_jk] in this space, the P_n-compressed product has entries Co_P(sum_j X_ij Y_jk)=sum_j (X_ij dot Y_jk), exactly the matrix amplification of the compressed product on S_P; and Co_{P_n}(P_n)=I_n tensor Co_P(P). Finally P_n is a delta-projection because P_n^dagger=P_n and ||P_n^2-P_n||=||I_n tensor(P^2-P)||=||P^2-P||<=delta. Since the ambient extended definition makes M_n tensor A an epsilon-C*-algebra, the four allowed amplified externals apply at each n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Complete operator-space obligation. For every n>=1, lem-compcb-amplified-compression-identities gives Co_{P_n}^2=Co_{P_n}. By def-compressed-corner, S_{P_n}=Image(Co_{P_n}) is a closed linear subspace of the complete matrix space M_n tensor A, hence is complete in the inherited norm. With the inherited matrix norms, the amplified-corner identification therefore makes S_P a complete operator space.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Amplification-naturality and completeness bridge. Define T_P=L_P R_P+R_P L_P-1 on A and T_{P_n}=L_{P_n}R_{P_n}+R_{P_n}L_{P_n}-1 on M_n tensor A. For X=(X_ij), P_n=I_n tensor P is diagonal, so the standard amplified matrix product gives (L_{P_n}R_{P_n})(X)_ij=P(X_ij P) and (R_{P_n}L_{P_n})(X)_ij=(P X_ij)P. Hence T_{P_n}=1_{M_n} tensor T_P exactly. By the registered theta-idempotent-approximation-map definition, theta is built from identity, products, and a norm-convergent scalar power series: theta(T)=(1+T(T^2)^(-1/2))/2. For fixed finite n, amplification T mapsto 1_{M_n} tensor T is a continuous unital algebra homomorphism, so it preserves powers and the norm limit defining (T^2)^(-1/2). Therefore Co_{P_n}=theta(T_{P_n})=1_{M_n} tensor theta(T_P)=1_{M_n} tensor Co_P. It follows entrywise that Image(Co_{P_n})=M_n tensor Image(Co_P): the forward inclusion follows because Co_{P_n}(X)=(Co_P(X_ij))_ij; conversely, if every Y_ij lies in Image(Co_P), idempotence gives Co_P(Y_ij)=Y_ij, hence Co_{P_n}(Y)=Y. Thus S_{P_n}=M_n tensor S_P with the inherited matrix norm, without invoking any additional external lemma. Since def-compressed-corner makes each S_{P_n}=Image(Co_{P_n}) closed and M_n tensor A is complete, every inherited matrix level is complete; in particular S_P is Banach, and the operator-space axioms are inherited by the subspace. Hence S_P with these matrix norms is a complete operator space.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Multiplication and associator obligation. Let C_r,e_r be witnesses from lem-compcb-rectangular-product and set K_p=C_r+1 and K_a=2*C_r*(K_p+3)+1. At every amplification, when e<=min{e_r,1}, def-compressed-corner and lem-compcb-rectangular-product give ||A dot B-AB||<=C_r*e*||A||||B||. The ambient extended epsilon-C*-axiom ||AB||<=(1+epsilon)||A||||B|| and epsilon<=e imply ||A dot B||<=(1+K_p*e)||A||||B||. For A,B,C in one amplified square corner, insert successively (A dot B)C, (AB)C, A(BC), and A(B dot C) between (A dot B) dot C and A dot (B dot C). The two outer rectangular-product errors are each at most C_r*e*(1+K_p*e)||A||||B||||C||; the two errors from multiplying A dot B-AB or BC-B dot C by an ambient factor are each at most (1+epsilon)*C_r*e||A||||B||||C||; and the ambient associator is at most epsilon||A||||B||||C||. Since e<=1 and epsilon<=e, the sum is at most K_a*e||A||||B||||C||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Product-norm step. Let C_r,e_r be witnesses from lem-compcb-rectangular-product and K_p=C_r+1. At every amplification and for e<=e_r, ||A dot B-AB||<=C_r*e*||A||||B||. The ambient extended epsilon-C*-multiplication bound and epsilon<=e then give ||A dot B||<=||AB||+C_r*e||A||||B||<=(1+K_p*e)||A||||B||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Associator step. Let C_r,e_r be witnesses from lem-compcb-rectangular-product, put K_p=C_r+1 and K_a=2*C_r*(K_p+3)+1, and assume e<=min{e_r,1}. The rectangular estimate plus the ambient product bound first gives ||X dot Y||<=(1+K_p*e)||X||||Y||. Now insert (A dot B)C, (AB)C, A(BC), and A(B dot C) between (A dot B) dot C and A dot (B dot C). The two outer rectangular-product errors are each at most C_r*e*(1+K_p*e)||A||||B||||C||. The two errors obtained by multiplying A dot B-AB or BC-B dot C by one ambient factor are each at most (1+epsilon)*C_r*e||A||||B||||C||, and the remaining ambient associator is at most epsilon||A||||B||||C||. Since epsilon<=e<=1, the sum is at most [2*C_r*(1+K_p)+4*C_r+1]*e||A||||B||||C||=K_a*e||A||||B||||C||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Involution and C*-norm obligation. Uniformly at every matrix level, the inherited dagger preserves the square corner, is isometric and anti-multiplicative for the compressed product, fixes the compressed unit, and the compressed product satisfies the lower approximate C*-norm bound with error (C_r+1)e, where C_r is a universal rectangular-product constant.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Dagger step. If A is in S_{P_n}, then A=Co_{P_n}(A); lem-compcb-amplified-compression-identities gives A^dagger=Co_{P_n}(A^dagger), so the inherited isometric dagger preserves the corner. For A,B in the corner, that external and ambient anti-multiplicativity give (A dot B)^dagger=Co_{P_n}((AB)^dagger)=Co_{P_n}(B^dagger A^dagger)=B^dagger dot A^dagger. Also P_n^dagger=P_n by def-delta-projection, hence u_{P,n}^dagger=Co_{P_n}(P_n)^dagger=Co_{P_n}(P_n^dagger)=u_{P,n}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Lower C*-norm step. Let C_r,e_r be witnesses from lem-compcb-rectangular-product. For A in the square corner and e<=e_r, that external applied to A^dagger and A, together with isometry of dagger and the ambient lower C*-estimate, gives ||A^dagger dot A||>=||A^dagger A||-C_r*e||A^dagger||||A||>=(1-epsilon-C_r*e)||A||^2>=(1-(C_r+1)*e)||A||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Compressed-unit obligation. For universal C_u,C_N<infinity and e_u,e_N>0 supplied by lem-compcb-compressed-unit-action and lem-compcb-compressed-unit-norm, the matrix-level compressed units act on both sides with error at most C_u*e and have norm within C_N*e of 1 whenever e<=min{e_u,e_N} and P is nonvanishing.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Unit-action step. Let C_u,e_u be witnesses from lem-compcb-compressed-unit-action. For P_n=I_n tensor P and u_{P,n}=Co_{P_n}(P_n), the external applied to the amplified square corner gives, whenever e<=e_u, ||u_{P,n} dot A-A||<=C_u*e||A|| and ||A dot u_{P,n}-A||<=C_u*e||A|| at every n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Unit-norm step. Let C_N,e_N be witnesses from lem-compcb-compressed-unit-norm. Each P_n is a delta-projection and ||P_n||=||P||, so the nonvanishing alternative for P passes to P_n. Applying the external to P_n gives abs(||u_{P,n}||-1)<=C_N*e whenever e<=e_N, uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

