# Proof Export

## Node 1

**Statement:** Uniform compressed-unit action: there are universal C_co < infinity and e_co > 0 such that, for e=delta+epsilon <= e_co, every compatible amplified rectangular corner satisfies ||u_T dot A-A|| <= C_co*e*||A|| and ||A dot u_R-A|| <= C_co*e*||A||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Setup and uniform primitive bounds: interpret a compatible amplified rectangular corner as an extended epsilon-C*-algebra calA, n>=1, delta-projections T,R, T_n=I_n tensor T, R_n=I_n tensor R, and A in S_{T_n,R_n}; write u_{T,n}=Co_{T_n,T_n}(T_n) and u_{R,n}=Co_{R_n,R_n}(R_n). There are universal M,k<infinity and e_0>0 such that, when e=delta+epsilon<=e_0, ||T_n||,||R_n||<=M, both compression maps Co_{T_n,R_n} are within k*e of L_{T_n}R_{R_n} and R_{R_n}L_{T_n}, and A=Co_{T_n,R_n}(A).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Amplified admissibility and notation. By def-extended-epsilon-cstar-algebra, M_n tensor calA is an epsilon-C*-algebra. The block diagonals T_n=I_n tensor T and R_n=I_n tensor R are delta-projections because adjoints and products amplify entrywise and ||I_n tensor Z||=||Z||. By lem-compcb-amplified-compression, the relevant maps and spaces are the amplified compressions and corners; by lem-compcb-amplified-compression-identities each amplified Co is idempotent. Hence A in S_{T_n,R_n}=Im(Co_{T_n,R_n}) implies A=Co_{T_n,R_n}(A), while u_{T,n}=Co_{T_n,T_n}(T_n) lies in S_{T_n,T_n}, and similarly for R.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Uniform constants. Unpack the universal O-terms in def-delta-projection and def-compressed-corner: there are universal a,k<infinity and e_0>0 such that every delta-projection S in an epsilon-C*-algebra with e<=e_0 obeys either ||S||<=a*delta or ||S||<=1+a*e, and ||Co_{S,V}-L_S R_V||,||Co_{S,V}-R_V L_S||<=k*e for every compatible delta-projection V. Shrink e_0<=1 and set M=max(a,1+a). Applying this inside M_n tensor calA gives ||T_n||,||R_n||<=M and all assertions of node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Uniform compressed-unit comparison: after possibly decreasing e_0, there is a universal K_u<infinity such that ||u_{T,n}-T_n||<=K_u*e, ||u_{R,n}-R_n||<=K_u*e, and ||u_{T,n}||,||u_{R,n}||<=M+K_u for every compatible amplified rectangular corner.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Single-projection estimate. Let S be either T_n or R_n and u_S=Co_{S,S}(S). From node 1.1, ||S||<=M and ||Co_{S,S}-L_S R_S||<=k*e. Since (L_S R_S)(S)=S(S^2), the epsilon-banach-cstar-norm-axioms and ||S^2-S||<=delta give ||u_S-S||<=k*e*||S||+||S(S^2)-S||, while bilinearity gives S(S^2)-S=S(S^2-S)+(S^2-S), so ||u_S-S||<=[k*M+2*M+1]*e when e<=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Taking K_u=k*M+2*M+1 in node 1.2 and using the triangle inequality yields ||u_{T,n}||,||u_{R,n}||<=M+K_u*e<=M+K_u. The constant and threshold are universal and independent of n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Validated node 1.1.2 supplies universal finite constants M and k, independent of n, and a universal threshold e_0<=1 with ||T_n||,||R_n||<=M. Validated node 1.2.1, applied first with S=T_n and then with S=R_n, supplies ||u_{T,n}-T_n||<=(k*M+2*M+1)*e and ||u_{R,n}-R_n||<=(k*M+2*M+1)*e. Define K_u=k*M+2*M+1. For S=T_n and S=R_n separately, the triangle inequality gives ||u_S||<=||u_S-S||+||S||<=K_u*e+M<=M+K_u because 0<=e<=e_0<=1. Hence both bounds asserted in node 1.2.2 hold with a universal finite K_u and a universal threshold, independently of n; no premise from the pending parent node 1.2 is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Ambient rectangular unit action: there is a universal K_a<infinity such that, under the setup of node 1.1 and e<=e_0, ||u_{T,n}A-A||<=K_a*e*||A|| and ||A u_{R,n}-A||<=K_a*e*||A||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Left projection action. Put D=T_n(A R_n). From A=Co_{T_n,R_n}(A) and ||Co_{T_n,R_n}-L_{T_n}R_{R_n}||<=k*e in node 1.1, ||A-D||<=k*e||A||. The identity T_n A-A=T_n(A-D)+(T_nD-D)+(D-A), the epsilon-banach-cstar-norm-axioms, and ||T_n||,||R_n||<=M give ||T_n(A-D)||<=2*M*k*e||A|| and ||A R_n||<=2*M||A||. Writing Y=A R_n, approximate associativity and ||T_n^2-T_n||<=delta give ||T_nD-D||=||T_n(T_nY)-T_nY||<=[epsilon*M^2+2*delta]*||Y||<=2*M*(M^2+2)*e||A||. Thus ||T_n A-A||<=K_T*e||A|| for universal K_T=2*M*k+2*M*(M^2+2)+k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Right projection action. Put D=(T_n A)R_n. The second compression comparison in node 1.1 gives ||A-D||<=k*e||A||. Now A R_n-A=(A-D)R_n+(D R_n-D)+(D-A). Using ||T_n A||<=2*M||A||, approximate associativity to compare ((T_nA)R_n)R_n with (T_nA)(R_n^2), and ||R_n^2-R_n||<=delta yields the same kind of universal estimate ||A R_n-A||<=K_R*e||A||, with for instance K_R=2*M*k+2*M*(M^2+2)+k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Replace projections by compressed units. By node 1.2 and the multiplication bound in epsilon-banach-cstar-norm-axioms, ||(u_{T,n}-T_n)A||<=2*K_u*e||A|| and ||A(u_{R,n}-R_n)||<=2*K_u*e||A||. Combining these with nodes 1.3.1 and 1.3.2 proves node 1.3 with K_a=max(K_T,K_R)+2*K_u.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** Dependency-closed compressed-unit comparison, independent of node 1.2. Let S be T_n or R_n and put u_S=Co_{S,S}(S). Validated node 1.1 gives ||S||<=M, ||S^2-S||<=delta, and e<=e_0<=1; the universal O(e) compression comparison in registered def-compressed-corner gives a universal k<infinity (enlarging the setup constant if necessary) with ||Co_{S,S}-L_S R_S||<=k*e. Since (L_S R_S)(S)=S(S^2), the operator-norm estimate and the epsilon-banach-cstar multiplication bound give ||u_S-S||<=k*e*||S||+||S(S^2)-S||. By bilinearity, S(S^2)-S=S(S^2-S)+(S^2-S), so ||S(S^2)-S||<=(1+epsilon)||S||*||S^2-S||+||S^2-S||<=(2*M+1)*e. Hence, with the universal K_u_local=k*M+2*M+1, both ||u_{T,n}-T_n||<=K_u_local*e and ||u_{R,n}-R_n||<=K_u_local*e follow using only validated node 1.1 and registered definitions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.5

**Statement:** Dependency-closed assembly. By node 1.3.4 and e<=1, ||(u_{T,n}-T_n)A||<=(1+epsilon)||u_{T,n}-T_n||||A||<=2*K_u_local*e||A||, and likewise ||A(u_{R,n}-R_n)||<=2*K_u_local*e||A||. Bilinearity yields u_{T,n}A-A=(u_{T,n}-T_n)A+(T_nA-A) and A u_{R,n}-A=A(u_{R,n}-R_n)+(A R_n-A). Combining the preceding estimates with validated nodes 1.3.1 and 1.3.2 proves both bounds in node 1.3 with the universal K_a=max(K_T,K_R)+2*K_u_local. This derivation does not invoke pending node 1.2.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Compressed-product assembly: combining the ambient estimates with lem-compcb-rectangular-product yields universal C_co<infinity and e_co>0 for which ||u_{T,n} dot A-A||<=C_co*e*||A|| and ||A dot u_{R,n}-A||<=C_co*e*||A||; these u_{T,n},u_{R,n} are the amplified compressed units denoted u_T,u_R in the root.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** The pairs (u_{T,n},A) in S_{T_n,T_n} x S_{T_n,R_n} and (A,u_{R,n}) in S_{T_n,R_n} x S_{R_n,R_n} are compatible amplified rectangular pairs by node 1.1. Therefore lem-compcb-rectangular-product supplies universal C_p<infinity and e_p>0 such that, whenever e=delta+epsilon<=e_p, ||u_{T,n} dot A-u_{T,n}A||<=C_p*e*||u_{T,n}||||A|| and ||A dot u_{R,n}-A u_{R,n}||<=C_p*e*||A||||u_{R,n}||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Choose e_co as the minimum of e_0, the thresholds in lem-compcb-amplified-compression, lem-compcb-amplified-compression-identities, and lem-compcb-rectangular-product, and 1; choose C_co=K_a+C_p*(M+K_u). Nodes 1.2-1.4.1 and the triangle inequality then give both root bounds. All constants and e_co are universal and independent of n, calA, T,R,A; by lem-compcb-amplified-compression, u_{T,n}=Co_{T_n}(T_n)=I_n tensor Co_T(T) and similarly for R, so this is exactly the root notation.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.2.1

**Statement:** Dependency-closed assembly via children 1.4.2.1.1 and 1.4.2.1.2. The first child derives uniform bounds ||u_{T,n}||,||u_{R,n}||<=M+K_u and ambient action bounds ||u_{T,n}A-A||,||A u_{R,n}-A||<=K_a*e*||A|| directly from validated nodes 1.2.1, 1.3.1, and 1.3.2, without using pending nodes 1.2 or 1.3. The second child combines those bounds with validated node 1.4.1. Explicitly, for e<=e_co:=min(e_0,e_p,e_cmp,e_id,1), the triangle inequality gives ||u_{T,n} dot A-A||<=[C_p(M+K_u)+K_a]e||A|| and ||A dot u_{R,n}-A||<=[C_p(M+K_u)+K_a]e||A||. Thus C_co:=K_a+C_p(M+K_u) works. The constants and thresholds are universal, and lem-compcb-amplified-compression identifies the amplified compressed units with the root notation.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.4.2.1.1

**Statement:** Local bounds from validated inputs only. Put K_u:=k*M+2*M+1. Validated node 1.2.1, applied to S=T_n and S=R_n, gives ||u_{T,n}-T_n||<=K_u*e and ||u_{R,n}-R_n||<=K_u*e whenever e<=e_0<=1. Together with ||T_n||,||R_n||<=M from the validated setup, the triangle inequality gives ||u_{T,n}||,||u_{R,n}||<=M+K_u. The multiplication bound ||XY||<=(1+epsilon)||X||||Y|| and epsilon<=e<=1 give ||(u_{T,n}-T_n)A||<=2*K_u*e*||A|| and ||A(u_{R,n}-R_n)||<=2*K_u*e*||A||. Bilinearity yields u_{T,n}A-A=(u_{T,n}-T_n)A+(T_nA-A) and A u_{R,n}-A=A(u_{R,n}-R_n)+(A R_n-A). Hence validated nodes 1.3.1 and 1.3.2 imply ||u_{T,n}A-A||<=K_a*e*||A|| and ||A u_{R,n}-A||<=K_a*e*||A|| for K_a:=max(K_T,K_R)+2*K_u. Thus all four estimates are obtained without invoking pending nodes 1.2 or 1.3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.4.2.1.2

**Statement:** Final assembly from the preceding local bounds and validated node 1.4.1. Let e_co:=min(e_0,e_p,e_cmp,e_id,1), where e_p is the positive threshold in node 1.4.1 and e_cmp,e_id are the positive thresholds in lem-compcb-amplified-compression and lem-compcb-amplified-compression-identities. If e<=e_co, node 1.4.1 and the preceding child give ||u_{T,n} dot A-A||<=||u_{T,n} dot A-u_{T,n}A||+||u_{T,n}A-A||<=[C_p(M+K_u)+K_a]e||A||. Likewise ||A dot u_{R,n}-A||<=||A dot u_{R,n}-A u_{R,n}||+||A u_{R,n}-A||<=[C_p(M+K_u)+K_a]e||A||. Therefore C_co:=K_a+C_p(M+K_u) works. Every constant is finite and universal and every threshold in the minimum is positive and universal, so C_co and e_co are universal and independent of n,calA,T,R,A. Finally lem-compcb-amplified-compression identifies u_{T,n}=Co_{T_n}(T_n)=I_n tensor Co_T(T), and similarly for R, which is the root notation.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

