# Proof Export

## Node 1

**Statement:** There are universal a_corr>0 and C_corr<infinity with the following property: if B is a finite-dimensional C*-algebra, H a finite-dimensional Hilbert space, and T:B->B(H) is linear, dagger-preserving, has ||T_n(XY)-T_n(X)T_n(Y)||<=a||X||||Y|| and ||T_n(I)-I||<=a at every n, where 0<=a<=a_corr, then one unital dagger-homomorphism mu:B->B(H) satisfies ||mu_n-T_n||<=C_corr*a at every n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Uniform cb control, exact unitalization, and the norm-one diagonal. Assume 0<=a<=a_corr<=1. At each n and ||X||=1, dagger preservation, the C*-identity in B(C^n tensor H), and the stated multiplicative defect give ||T_n(X)||^2=||T_n(X)^dagger T_n(X)||<=||T_n(X^dagger X)||+a<=M_n+a, where M_n=||T_n||. Hence M_n^2<=M_n+a and M_n<2, uniformly in n. Put e=I-T(I), choose a state phi on B, and set S_0(x)=T(x)+phi(x)e. Since ||phi||_cb=1, phi(x^dagger)=conj(phi(x)), e=e^dagger and ||e||<=a, the same level-one S_0 is dagger-preserving and exactly unital, ||S_0-T||_cb<=a, and ||S_0||_cb<3. If G_T and G_0 are the amplified defects, direct expansion gives G_0(x,y)=G_T(x,y)+phi(xy)e-phi(y)T(x)e-phi(x)eT(y)-phi(x)phi(y)e^2, with the entrywise amplified version at every n; therefore its uniform amplified bilinear norm b_0 is at most a+a+2a+2a+a^2<=7a. Set c_u=7. Finally normalized Haar measure on the compact unitary group of B gives D=int U^dagger tensor U dU. In finite dimension D is a finite convex combination sum_s p_s U_s^dagger tensor U_s, with sum_s ||p_s U_s^dagger||||U_s||=1. Haar invariance first for unitary X, and then linearity because every element of a unital C*-algebra is a linear combination of unitaries, gives XD=DX; also multiplication(D)=I. Thus D is a dimension-independent norm-one diagonal. For any linear S and amplified bilinear defect G, w prime(x)=sum_s S(p_s U_s^dagger)G(U_s,x) obeys ||w prime||_cb<=||S||_cb||G||. Its amplification is the entrywise amplification of this same level-one map, so all later bounds are uniform in n and in the dimensions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** One normalized Newton correction. Let S:B->B(H) be exactly unital and dagger-preserving, with ||S||_cb<=4, and let G(x,y)=S(xy)-S(x)S(y) have uniform amplified bilinear norm b. Use the diagonal D=sum_s a_s tensor b_s from node 1.1, where a_s=p_s U_s^dagger and b_s=U_s, and define w prime(x)=sum_s S(a_s)G(b_s,x), w doubleprime(x)=w prime(x^dagger)^dagger, w=(w prime+w doubleprime)/2, and S plus=S+w. Then ||w||_cb<=4b, w is dagger-preserving, and G(y,I)=G(I,y)=0 implies w(I)=0, so S plus is exactly unital and dagger-preserving. Write delta w(x,y)=S(x)w(y)-w(xy)+w(x)S(y). Associativity gives the exact cocycle identity S(x)G(y,z)-G(xy,z)+G(x,yz)-G(x,y)S(z)=0. Centrality of D and multiplication(D)=I then give delta w prime=G-Q prime, where R=sum_s G(a_s,b_s) and Q prime(x,y)=R G(x,y)+sum_s G(x,a_s)G(b_s,y). Hence ||Q prime||<=2b^2 at every amplification. Daggering the identity gives delta w doubleprime=G-Q doubleprime with Q doubleprime(x,y)=Q prime(y^dagger,x^dagger)^dagger and the same bound. Therefore the new defect is G_{S plus}=G-delta w-w(x)w(y)=(Q prime+Q doubleprime)/2-w(x)w(y), so its uniform amplified bilinear norm is at most 2b^2+16b^2=18b^2. Thus, with K_N=18, ||S plus-S||_cb<=4b and b plus<=K_N b^2; all formulas are amplifications of the same corrected level-one map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Convergence and exactness. Let c_u=7 and K_N=18 be supplied by nodes 1.1 and 1.2, and choose a_corr=min(1/(2 K_N c_u),1/(16 c_u)); then K_N c_u a_corr<=1/2 and 8 c_u a_corr<=1/2<1. Starting from S_0 of node 1.1, recursively apply node 1.2. If b_k is the uniform amplified bilinear defect of S_k, then b_k<=b_0 2^{-k}, every iterate has cb norm below 4, and sum_k ||S_{k+1}-S_k||_cb<=8b_0. Hence S_k converges in cb norm to one exactly unital dagger-preserving linear map mu. Since b_k tends to zero, continuity of multiplication gives mu(xy)=mu(x)mu(y). Moreover ||mu-T||_cb<=||S_0-T||_cb+||mu-S_0||_cb<=(1+8c_u)a=57a. Thus C_corr=57 works, and because convergence is in cb norm, each mu_n is the amplification of this same level-one mu and ||mu_n-T_n||<=57a at every n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Induction and limit bridge. Invoke the registered validation dependencies 1.1 and 1.2. Let b_k be the uniform amplified bilinear norm of the multiplicative defect of S_k. Node 1.1 gives an exactly unital dagger-preserving S_0 with ||S_0||_cb<3, b_0<=c_u a, and ||S_0-T||_cb<=a. Inductively suppose S_k is exactly unital and dagger-preserving, ||S_k||_cb<4, and b_k<=b_0 2^{-k}. Node 1.2 produces the same level-one map S_{k+1} at all amplifications, still exactly unital and dagger-preserving, with ||S_{k+1}-S_k||_cb<=4b_k and b_{k+1}<=K_N b_k^2. Since K_N b_0<=K_N c_u a<=1/2, b_{k+1}<=(K_N b_0)b_k<=b_k/2<=b_0 2^{-(k+1)}. The degenerate-safe geometric estimate in child 1.3.1.1 gives ||S_k-S_0||_cb<=8b_0<=8c_u a<1, including b_0=0, so ||S_k||_cb<4 and the induction closes. It also gives sum_k ||S_{k+1}-S_k||_cb<=8b_0. Therefore S_k is Cauchy in cb norm and converges to a single level-one linear map mu; exact unitality and dagger preservation pass to the limit. For fixed x,y, the boundedness ||S_k||_cb<4, convergence S_k->mu, and b_k->0 show S_k(xy)-S_k(x)S_k(y)->mu(xy)-mu(x)mu(y) while the left side has norm at most b_k||x||||y||->0. Hence mu is multiplicative. Finally ||mu-T||_cb<=||S_0-T||_cb+sum_k||S_{k+1}-S_k||_cb<=a+8c_u a=57a. Cb convergence is sup_n||(S_k-mu)_n||->0, so every mu_n is the amplification of this same mu and ||mu_n-T_n||<=57a.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Degenerate-safe geometric estimate. Suppose b_k<=b_0 2^{-k} and ||S_{k+1}-S_k||_cb<=4b_k, as obtained in the parent induction. For every k, ||S_k-S_0||_cb<=sum_{j<k}4b_j<=4b_0 sum_{j=0}^{k-1}2^{-j}<=8b_0<=8c_u a<=8c_u a_corr<=1/2<1. This includes b_0=0: then 0<=b_k<=0 gives b_k=0 for all k, and ||S_{k+1}-S_k||_cb<=0 forces every correction increment to vanish. In every case, ||S_k||_cb<=||S_0||_cb+||S_k-S_0||_cb<3+1=4, so the Newton hypothesis closes at the next step without assuming b_0>0. Likewise sum_{k>=0}||S_{k+1}-S_k||_cb<=4 sum_{k>=0}b_k<=4b_0 sum_{k>=0}2^{-k}=8b_0. These are precisely the finite-displacement and Cauchy estimates used by the parent.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

