# Proof Export

## Node 1

**Statement:** There are universal C_dir < infinity and e_dir > 0 such that, if B_1,B_2 are finite-dimensional C*-algebras, P_1,P_2 are target t-projections, ||P_1+P_2-I|| <= t, and v_i:B_i->S_{P_i} are extended t-inclusions with target ambient defect at most t <= e_dir, then (x_1,x_2) |-> v_1(x_1)+v_2(x_2) is an extended C_dir*t-inclusion; bijectivity is asserted only if both v_i are bijective and both target cross-corners vanish.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Uniform amplified two-corner calculus. There are universal K_geo<infinity and e_geo>0 such that, under the root hypotheses with t<=e_geo, for every n, writing A_n=M_n tensor A, p_i=I_n tensor P_i and C_ij=Co_{p_i,p_j}, one has ||p_i||<=2, ||p_1 p_2||+||p_2 p_1||<=K_geo t, ||C_ii||<=K_geo, ||C_ii C_jj||<=K_geo t for i!=j, and ||C_ii(a_1+a_2)-a_i||<=K_geo t max(||a_1||,||a_2||) whenever a_i is in M_n tensor S_{P_i}. The constants and threshold are independent of n and all dimensions. This uses def-operator-space, def-compressed-corner, def-delta-projection, lem-compcb-amplified-compression, and lem-compcb-amplified-compression-identities.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Amplified projections are uniformly bounded and almost orthogonal. By def-operator-space and lem-compcb-amplified-compression, p_i=I_n tensor P_i are t-projections and ||p_1+p_2-I||<=t at every n. In the target epsilon-C*-algebra A_n, epsilon<=t. Hence (1-t)||p_i||^2<=||p_i^2||<=||p_i||+t, so ||p_i||<=2 for t<=1/4. Put s=p_1+p_2 and r=s-I. The exact bilinear identity p_1p_2=p_1r+(p_1I-p_1)-(p_1^2-p_1), and its index-swapped version, together with the product and approximate-unit axioms, gives ||p_1p_2||+||p_2p_1||<=12t. No associativity is used in this identity.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Uniform compression and cross-extraction bounds, proved without using any sibling. Fix n and i!=j, and put p=p_i, q=p_j. By the operator-space block-diagonal axiom and the amplified algebra structure, p,q are t-projections, ||p+q-I||<=t, and the ambient defect epsilon satisfies epsilon<=t. For t<=1/4, the C*-lower bound and projection defect give (1-t)||p||^2<=||p^2||<=||p||+t, and similarly for q, hence ||p||,||q||<=2. With r=p+q-I, the exact bilinear identity pq=pr+(pI-p)-(p^2-p), valid without associativity, gives ||pq||<=6t from the product, approximate-unit, and t-projection axioms; the swapped identity gives ||qp||<=6t. Let c_Co be the universal constant in def-compressed-corner and reduce the threshold so its estimate applies at every amplified level. Then C_kk differs from X|->p_k(Xp_k) by at most d=2*c_Co*t in operator norm. Consequently ||C_kk||<=K_0:=7+c_Co universally. If a=C_jj(a), then ||a-q(aq)||<=d||a|| and ||C_ii(a)-p(ap)||<=d||a||. Put Z=(aq)p. Using ||p||,||q||<=2, epsilon,t<=1/4, and ||pq||<=6t, the product and associator axioms give ||p([q(aq)]p)|| <= ||p([q(aq)]p-qZ)||+||p(qZ)-(pq)Z||+||(pq)Z|| <=25t||a||+25t||a||+47t||a||=97t||a||. Also ||p((a-q(aq))p)||<= (25/4)d||a||. Therefore ||C_ii(a)||<=(97+15*c_Co)t||a||=:K_1*t||a||. Applying this with a=C_jj(X) yields ||C_ii C_jj||<=K_1*K_0*t. By lem-compcb-amplified-compression, M_n tensor S_{P_i}=S_{p_i}; by lem-compcb-amplified-compression-identities, C_ii is idempotent, so C_ii(a_i)=a_i for every a_i in M_n tensor S_{P_i}. Hence ||C_ii(a_1+a_2)-a_i||<=K_1*t*max(||a_1||,||a_2||). Taking K_geo=max{2,12,K_0,K_1,K_0*K_1} and the minimum of the universal thresholds proves node 1.1 uniformly in n and all dimensions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Extended inclusion from the uniform corner calculus. Under the root hypotheses and the threshold of node 1.1, define V_n=I_n tensor V by V_n(X_1,X_2)=v_{1,n}(X_1)+v_{2,n}(X_2). There is a universal K_inc such that every V_n is a K_inc*t-homomorphism and satisfies (1-K_inc*t)||X||<=||V_n(X)||<=(1+K_inc*t)||X|| for the C*-direct-sum norm ||X||=max(||X_1||,||X_2||). Thus V is an extended K_inc*t-inclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Uniform coarse norm bounds, proved without using pending node 1.1. Fix n, write p_i=I_n tensor P_i, C_ii=Co_{p_i}, a_i=v_{i,n}(X_i), M=max_i||a_i||, and ||X||=max_i||X_i||. Amplification and the operator-space block-diagonal axiom preserve the t-projection defects and ||p_1+p_2-I||<=t. At this amplified level the ambient defect epsilon is at most t. For t<=1/4, the C*-lower bound and ||p_i^2-p_i||<=t give (1-t)||p_i||^2<=||p_i^2||<=||p_i||+t, hence ||p_i||<=2. Put r=p_1+p_2-I. The exact bilinear identity p_i p_j=p_i r+(p_i I-p_i)-(p_i^2-p_i) for i!=j, followed only by the product and approximate-unit axioms, gives ||p_i p_j||<=6t. Let c_0 and e_0 be universal constants furnished by the two compression-approximation bounds in def-compressed-corner, so for t<=e_0 and epsilon<=t, C_ii differs from each of z|->p_i(zp_i) and z|->(p_i z)p_i by at most 2c_0 t in operator norm. The preceding bound and the product axiom give a universal K_0 with ||C_ii||<=K_0. Since lem-compcb-amplified-compression identifies M_n tensor S_{P_j} with S_{p_j} and lem-compcb-amplified-compression-identities makes C_jj idempotent, a_j=C_jj(a_j), hence ||a_j-p_j(a_jp_j)||<=2c_0t||a_j||. Also ||C_ii(a_j)-p_i(a_jp_i)||<=2c_0t||a_j||. Substitute p_j(a_jp_j) for a_j in the latter nested product. Two applications of the associator axiom transform p_i((p_j(a_jp_j))p_i) into p_i(p_j(a_j(p_jp_i))) with total error at most a universal constant times t||a_j||: all p_i,p_j have norm at most 2, epsilon<=t, and the product bound is uniform. The final nested product has norm at most a universal constant times ||a_j||||p_jp_i||<=6t||a_j||. Therefore there is a universal K_1 with ||C_ii(a_j)||<=K_1t||a_j|| for i!=j. Put K=max{K_0,K_1,1}. Because C_ii(a_i)=a_i, linearity yields ||a_i||<=K||V_n(X)||+KtM. If t<=1/(2K), then M<=2K||V_n(X)||. The extended t-inclusion bounds give (1-t)||X||<=M<=(1+t)||X||, while the triangle inequality gives ||V_n(X)||<=2(1+t)||X||. Thus, after also taking t<=1/2, (4K)^{-1}||X||<=||V_n(X)||<=3||X||, with constants and threshold independent of n and all dimensions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Uniform star, unit, and product defects. Star preservation is exact because each v_i preserves dagger. Let u_i=Co_{p_i}(p_i), the compressed unit from def-compressed-corner; the compression approximation and the t-projection relation give ||u_i-p_i||<=K_u*t, and the unit clause for v_i gives ||v_{i,n}(I)-u_i||<=t. Together with ||p_1+p_2-I||<=t this gives ||V_n(I)-I||<=K_u'*t. For products, writing a_i=v_{i,n}(X_i), b_i=v_{i,n}(Y_i), each diagonal difference ||v_{i,n}(X_iY_i)-a_i b_i|| is at most t||X_i||||Y_i|| plus the compressed-versus-ambient error from lem-compcb-rectangular-product, hence at most K_d*t||X||||Y||. For i!=j, the compression approximation a_i=p_i(a_ip_i)+O(t)||a_i|| and b_j=p_j(b_jp_j)+O(t)||b_j||, the associator axiom, and node 1.1.1 expose the factor p_ip_j and give ||a_i b_j||<=K_x*t||a_i||||b_j||. Expanding the binary product of the two sums and adding the two diagonal and two cross estimates gives ||V_n(XY)-V_n(X)V_n(Y)||<=K_alg*t||X||||Y||. All constants are universal and level-independent; lem-compcb-corner-algebra supplies the uniform compressed-corner algebra structure and lem-compcb-rectangular-product supplies its compatible amplified product estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Uniform coarse-to-sharp C*-norm bootstrap. Let 0<c<=C be fixed. There are constants eta_b>0 and K_b<infinity, depending only on c,C, such that the following holds. If W:D->E is a star-preserving d-homomorphism from an exact C*-algebra D to an epsilon-C*-algebra E, c||z||<=||Wz||<=C||z|| for all z, and eta=d+epsilon<=eta_b, then (1-K_b*eta)||z||<=||Wz||<=(1+K_b*eta)||z|| for all z. Proof: by homogeneity take ||z||=1, define z_0=z and z_{m+1}=z_m^dagger z_m, and put a_m=||Wz_m||. Exactness of D gives ||z_m||=1, hence c<=a_m<=C. Star preservation, the d-homomorphism estimate, and the target product/C*-axioms give (1-epsilon)a_m^2-d<=a_{m+1}<=(1+epsilon)a_m^2+d. Since a_m>=c, if eta is small enough then a_{m+1}/a_m^2 lies in [1-K_1*eta,1+K_1*eta], with K_1 depending only on c; therefore r_m=log(a_{m+1})-2log(a_m) satisfies |r_m|<=K_2*eta uniformly in m. Writing b_m=log(a_m), iteration yields b_0=2^(-N)b_N-sum_{m=0}^{N-1}2^(-m-1)r_m. Since b_N is uniformly bounded by max{|log c|,|log C|}, letting N tend to infinity gives |log(a_0)|<=K_2*eta. After decreasing eta_b, exponentiation gives 1-K_b*eta<=a_0<=1+K_b*eta. Rescaling proves the assertion for arbitrary z (with z=0 immediate).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Optional bijectivity. If v_1 and v_2 are bijective and S_{P_1,P_2}=S_{P_2,P_1}=0, then V is bijective: injectivity follows from node 1.2's lower bound, while surjectivity follows from an invertible four-corner reconstruction operator. Namely beta(Z)=(Co_{P_j,P_k}Z)_{j,k}, alpha((Z_jk))=sum_{j,k}Z_jk, and ||alpha beta-I_A||<=K_rec*t<1; hence alpha is onto, and when both cross-corner ranges vanish its range is S_{P_1}+S_{P_2}=range(V).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Four-corner reconstruction is invertible. At level one define beta:A->direct_sum_{j,k}S_{P_j,P_k} by beta(Z)=(Co_{P_j,P_k}Z) and alpha by summation. Put s=P_1+P_2=I+r, ||r||<=t. By the compression estimate in def-compressed-corner, alpha beta(Z) differs from sum_{j,k}P_j(ZP_k)=s(Zs) by at most K_c*t||Z||. Bilinearity with the displayed parentheses gives the exact expansion s(Zs)=I(ZI)+I(Zr)+r(ZI)+r(Zr). The approximate-unit and product axioms, ||r||<=t, and t<=1 show ||s(Zs)-Z||<=K_s*t||Z||. Hence ||alpha beta-I_A||<=K_rec*t. Choosing t<1/(2K_rec), the Neumann series makes alpha beta invertible, so alpha is surjective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Conclude bijectivity under exactly the stated extra hypotheses. If S_{P_1,P_2}=S_{P_2,P_1}=0, validated node 1.3.1 makes alpha:S_{P_1} direct_sum S_{P_2}->A, alpha(a_1,a_2)=a_1+a_2, surjective. If each v_i is bijective onto S_{P_i}, then range(V)=S_{P_1}+S_{P_2}=A, so V is surjective. Injectivity is established independently in the child below by a level-one cross-extraction estimate from the permitted compression axioms, without invoking pending node 1.2. Hence V is bijective. Without both diagonal bijectivity and both zero-cross-corner assumptions no surjectivity statement is made.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Independent level-one injectivity and completion. Put p_i=P_i and C_i=Co_{p_i}. The target ambient defect epsilon is at most t. For t<=1/4, the C*-lower bound and ||p_i^2-p_i||<=t give (1-t)||p_i||^2<=||p_i^2||<=||p_i||+t, hence ||p_i||<=2. With r=p_1+p_2-I, bilinearity gives the exact identity p_i p_j=p_i r+(p_i I-p_i)-(p_i^2-p_i) for i!=j; the product and approximate-unit axioms therefore give ||p_i p_j||<=6t. Let c_C be the universal constant in the two compression-approximation bounds of def-compressed-corner. For a_j in S_{p_j}, idempotence of C_j gives C_j(a_j)=a_j, so ||a_j-p_j(a_jp_j)||<=2c_C*t||a_j||; also ||C_i(a_j)-p_i(a_jp_i)||<=2c_C*t||a_j||. Substitution, the product bound, and two applications of the associator axiom yield p_i((p_j(a_jp_j))p_i)=((p_i p_j)(a_jp_j))p_i+E with ||E||<=K_a*t||a_j||, since epsilon<=t and ||p_i||,||p_j||<=2. The exposed factor ||p_i p_j||<=6t then gives a universal K_x with ||C_i(a_j)||<=K_x*t||a_j|| for i!=j. Now suppose V(x_1,x_2)=0 and write a_i=v_i(x_i). Then a_1=-a_2, so M=||a_1||=||a_2||, while a_1=C_1(a_1)=-C_1(a_2) implies M<=K_x*t*M. After the universal threshold reduction t<1/K_x, M=0. Bijectivity of each v_i implies x_i=0, hence V is injective, without node 1.2. Validated node 1.3.1 and the vanishing cross-corners make alpha:S_{P_1} direct_sum S_{P_2}->A surjective; diagonal bijectivity gives range(V)=range(alpha)=A. Thus V is also surjective and hence bijective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Final universal constants and root assembly. Let e_cmp be the minimum of the thresholds in lem-compcb-amplified-compression and lem-compcb-amplified-compression-identities, and let e_ca,e_co be the thresholds in lem-compcb-corner-algebra and lem-compcb-rectangular-product. Choose e_dir>0 to be the minimum of e_geo, half of e_cmp,e_ca,e_co, all threshold reductions explicitly required in nodes 1.2 and 1.3, and 1/(2K_rec); this is a finite minimum of positive universal numbers. Since projection defect and target ambient defect are each at most t, every external is applied with total error at most 2t. Put C_dir=max{1,K_inc}. For t<=e_dir, node 1.2 proves that V is an extended C_dir*t-inclusion at every amplification. Under the contract's additional diagonal-bijectivity and two zero-cross-corner hypotheses, node 1.3 proves V bijective. This is exactly the root claim, with no bijectivity conclusion otherwise.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Dependency-checked final assembly. Require validated nodes 1.2 and 1.3. Let e_inc>0 be the universal threshold furnished by node 1.2 (including node 1.1 and its amplified-compression and corner-algebra threshold reductions), and let e_bij>0 be the universal threshold furnished by node 1.3 (including K_rec*t<1). Let e_cmp be the minimum of the two amplified-compression thresholds and let e_ca,e_co be the corner-algebra and rectangular-product thresholds. Set e_dir=min{e_inc,e_bij,e_cmp/2,e_ca/2,e_co/2}>0 and C_dir=max{1,K_inc}<infinity. Because the projection defect and ambient defect are each at most t, t<=e_dir implies total error t+epsilon<=2t is below every external threshold. The validated conclusion of node 1.2 then says at every amplification that V(x_1,x_2)=v_1(x_1)+v_2(x_2) is a C_dir*t-homomorphism with the two-sided (1+/-C_dir*t) norm bounds, hence an extended C_dir*t-inclusion. If both v_i are bijective and both cross-corners vanish, the validated conclusion of node 1.3 additionally makes V bijective; absent those extra hypotheses no bijectivity is concluded. Thus the root contract follows.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

