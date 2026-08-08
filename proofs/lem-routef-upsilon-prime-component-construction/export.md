# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, with C_N, C_R from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon' there exist an integer m >= 1, nonzero finite-dimensional Hilbert spaces L_j and E_j for 1 <= j <= m, a finite-dimensional Hilbert space F, operators W_j:H->L_j tensor E_j, an isometry V:H->H tensor F, nonempty finite index sets Sigma_j, unitaries U_js on L_j and weights p_js for s in Sigma_j, positive contractions C_j on E_j, unit vectors xi_j in E_j, contractions Lambda_j:L_j->H tensor F, CP maps Upsilon'_j:B(H)->B(L_j), and a CP map Upsilon':B(H)->B such that B=direct-sum_{j=1}^m B(L_j), sum_j W_j^*W_j=I_H, Delta(X)=sum_j W_j^*(X_j tensor I_Ej)W_j for every X=(X_1,...,X_m) in B, Phi(T)=V^*(T tensor I_F)V for every T in B(H), p_js >= 0, sum_{s in Sigma_j}p_js=1, sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)Z(U_js tensor I_Ej)=I_Lj tensor (Tr_Lj(Z)/dim(L_j)) for every Z in B(L_j tensor E_j), where Tr_Lj denotes the unnormalized partial trace over L_j, R_j:=sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)W_jW_j^*(U_js tensor I_Ej)=I_Lj tensor C_j, 0 <= C_j <= I_Ej, ||C_j|| >= 1-C_R*eta, 1-<xi_j,C_j^*C_j xi_j> <= 2*C_R*eta, if hat-U_js denotes U_js in the j-th block of B and zero in every other block and iota_js(z):=U_js z tensor xi_j then Lambda_j:=sum_{s in Sigma_j}p_js*(Delta(hat-U_js^*) tensor I_F)V W_j^*iota_js, Upsilon'_j(T):=Lambda_j^*(Phi(T) tensor I_F)Lambda_j, Upsilon'(T):=(Upsilon'_j(T))_{j=1}^m, and ||Upsilon'||_cb <= 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Under the root hypotheses there are m >= 1 and nonzero finite-dimensional Hilbert spaces L_j such that B=direct-sum_{j=1}^m B(L_j); complete positivity of the UCP map Delta gives finite-dimensional Hilbert spaces E_j, provisionally allowed to be zero, and operators W_j:H->L_j tensor E_j satisfying sum_j W_j^*W_j=I_H and Delta(X)=sum_j W_j^*(X_j tensor I_Ej)W_j for every X=(X_1,...,X_m) in B; complete positivity and unitality of Phi give a finite-dimensional Hilbert space F and an isometry V:H->H tensor F satisfying Phi(T)=V^*(T tensor I_F)V for every T in B(H).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Because eta <= rho_Upsilon' <= rho_Delta, lem-routef-delta-normalization-closeness applies to the fixed Delta' and supplies the displayed Delta as a UCP map B->B(H); lem-routef-raw-factor-setting-formation supplies B as a finite-dimensional unital C*-algebra and supplies Phi:B(H)->B(H) as the fixed UCP input map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** By GT-kitaev-fd-cstar-structure, the finite-dimensional unital C*-algebra B is *-isomorphic to direct-sum_{j=1}^m B(L_j) for some integer m>=1 and nonzero finite-dimensional Hilbert spaces L_j; transport Delta through this *-isomorphism and henceforth identify B with that direct sum.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Apply GT-kitaev-canonical-stinespring to Delta to obtain a finite-dimensional Stinespring space G, an isometry W:H->G, and a unital *-representation pi:B->B(G) with Delta(X)=W^*pi(X)W. For each block central unit e_j put G_j=pi(e_j)G, choose matrix units e_rs^(j) in B(L_j), put E_j=pi(e_11^(j))G_j (possibly zero), and define Q_j:L_j tensor E_j->G_j by Q_j(e_r tensor z)=pi(e_r1^(j))z. The matrix-unit identities show that Q_j is unitary and Q_j^*pi(X)Q_j=X_j tensor I_Ej on G_j. Thus W_j:=Q_j^*pi(e_j)W satisfies sum_j W_j^*W_j=I_H and Delta(X)=sum_j W_j^*(X_j tensor I_Ej)W_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** Apply GT-kitaev-canonical-stinespring to Phi and use the same matrix-unit construction for the single full matrix algebra B(H): its finite-dimensional unital representation space is unitarily H tensor F for a finite-dimensional Hilbert space F, the representation is T->T tensor I_F, and the Stinespring isometry becomes V:H->H tensor F, giving Phi(T)=V^*(T tensor I_F)V.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For every j, let d_j:=dim(L_j), fix an orthonormal basis (e_j[k])_{0 <= k < d_j}, put Sigma_j:={0,...,d_j-1}^2, and for s=(a,b) in Sigma_j define U_js e_j[k]:=exp(2*pi*i*a*k/d_j)e_j[(k+b) mod d_j] and p_js:=d_j^(-2); then every U_js is unitary, p_js >= 0, sum_{s in Sigma_j}p_js=1, and for every Z in B(L_j tensor E_j), sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)Z(U_js tensor I_Ej)=I_Lj tensor (Tr_Lj(Z)/d_j), where Tr_Lj denotes the unnormalized partial trace over L_j; this twirl is a positive order-preserving contraction onto I_Lj tensor B(E_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For d_j>=1, Sigma_j={0,...,d_j-1}^2 is finite and nonempty, p_js=d_j^(-2) is nonnegative, and its d_j^2 values sum to one. The formula U_j(a,b)e_j[k]=omega_j^(a*k)e_j[k+b mod d_j], omega_j=exp(2*pi*i/d_j), sends the chosen orthonormal basis bijectively to an orthonormal basis, so every U_j(a,b) is unitary.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Writing Z=sum_{r,t=0}^{d_j-1} E_rt tensor Z_rt, direct calculation gives U_j(a,b)^* E_rt U_j(a,b)=omega_j^(a*(t-r)) E_{r-b,t-b}; summing first over a annihilates r!=t, and summing over b sends each diagonal E_rr to I_Lj. Hence the probability average is I_Lj tensor (sum_r Z_rr/d_j)=I_Lj tensor (Tr_Lj(Z)/d_j). Being an average of unitary conjugations, the twirl is positive, order preserving, unital and contractive; the formula fixes exactly I_Lj tensor B(E_j), so it is a projection onto that subalgebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every j define R_j:=sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)W_jW_j^*(U_js tensor I_Ej); then R_j=I_Lj tensor C_j for a positive contraction C_j on E_j, and, writing hat-U_js for U_js in the j-th block of B and zero elsewhere, W_j^*R_jW_j=sum_{s in Sigma_j}p_js*Delta(hat-U_js^*)Delta(hat-U_js), so lem-routef-degree-two-estimate, lem-routef-raw-factor-norms, and lem-routef-delta-normalization-closeness give ||C_j|| >= 1-(C_V+C_Delta+C_2)*eta=1-C_R*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** From sum_k W_k^*W_k=I_H, each W_j^*W_j<=I_H and hence ||W_j||<=1 and 0<=W_jW_j^*<=I. Applying the positive unital twirl of node 1.2 to W_jW_j^* gives 0<=R_j<=I and the exact formula R_j=I_Lj tensor C_j with C_j:=Tr_Lj(W_jW_j^*)/d_j, so 0<=C_j<=I_Ej and ||R_j||=||C_j||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** For hat-U_js supported in block j, the Choi formula of node 1.1 gives Delta(hat-U_js)=W_j^*(U_js tensor I_Ej)W_j and Delta(hat-U_js^*)=W_j^*(U_js^* tensor I_Ej)W_j. Multiplying, averaging, and using the definition of R_j yields the exact identity W_j^*R_jW_j=sum_s p_js*Delta(hat-U_js^*)Delta(hat-U_js).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Let e_j be the unit of the j-th block, so ||e_j||=1. Since eta<=rho_Upsilon'<=rho_T, lem-routef-raw-factor-norms gives ||tilde-Delta(e_j)||>=1-C_V*eta; since eta<=rho_Upsilon'<=rho_Delta, lem-routef-delta-normalization-closeness gives ||Delta-tilde-Delta||_cb<=C_Delta*eta. Therefore ||Delta(e_j)||>=1-(C_V+C_Delta)*eta=1-C_N*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** For each s, hat-U_js^*hat-U_js=e_j and both factors have norm one. Since eta<=rho_Upsilon'<=rho_2, lem-routef-degree-two-estimate and the probability average give ||Phi(W_j^*R_jW_j)-Delta(e_j)||<=C_2*eta. The UCP map Phi is contractive, and ||W_j||<=1, so ||Phi(W_j^*R_jW_j)||<=||W_j^*R_jW_j||<=||R_j||=||C_j||. Combining with node 1.3.3 gives ||C_j||>=1-(C_N+C_2)*eta=1-(C_V+C_Delta+C_2)*eta=1-C_R*eta, using (1.3).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Since eta <= (2*C_R)^(-1), node 1.3 gives ||C_j|| >= 1/2, so E_j is nonzero; finite-dimensional norm attainment gives a unit vector xi_j in E_j with ||C_j xi_j||=||C_j||, and positivity of C_j gives 0 <= 1-<xi_j,C_j^*C_j xi_j>=1-||C_j||^2 <= 2*C_R*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** The constants in (1.1)-(1.3) give C_R>0, and 0<=eta<=(2*C_R)^(-1) gives 0<=C_R*eta<=1/2. Node 1.3 therefore yields ||C_j||>=1-C_R*eta>=1/2. An operator on the zero Hilbert space has norm zero, so E_j is nonzero; because E_j is finite-dimensional, the positive contraction C_j attains its norm at some unit vector xi_j, with ||C_j xi_j||=||C_j||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** For that xi_j, <xi_j,C_j^*C_j xi_j>=||C_j xi_j||^2=||C_j||^2. Since C_j is a contraction, this scalar is at most one, while ||C_j||>=1-C_R*eta and 0<=C_R*eta<=1/2 imply 0<=1-<xi_j,C_j^*C_j xi_j>=1-||C_j||^2<=1-(1-C_R*eta)^2<=2*C_R*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** For every j and s in Sigma_j define iota_js:L_j->L_j tensor E_j by iota_js(z):=U_js z tensor xi_j and define Lambda_j:=sum_{s in Sigma_j}p_js*(Delta(hat-U_js^*) tensor I_F)V W_j^*iota_js; each iota_js and V is an isometry, Delta is UCP, ||W_j|| <= 1, and the p_js form a probability distribution, hence ||Lambda_j|| <= 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** For each j,s, the map iota_js:z->U_js z tensor xi_j is an isometry because U_js is unitary and xi_j is a unit vector. The composition (Delta(hat-U_js^*) tensor I_F)V W_j^*iota_js is therefore correctly typed from L_j to H tensor F, so its finite probability average defines Lambda_j with the formula in node 1.5.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** The UCP map Delta is contractive, ||hat-U_js^*||=1, V and iota_js are isometries, and ||W_j^*||=||W_j||<=1; hence every summand defining Lambda_j has norm at most one. Since p_js>=0 and sum_s p_js=1, the triangle inequality gives ||Lambda_j||<=sum_s p_js=1, so Lambda_j is a contraction.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Define Upsilon'_j(T):=Lambda_j^*(Phi(T) tensor I_F)Lambda_j and Upsilon'(T):=(Upsilon'_j(T))_{j=1}^m; tensoring the CP map Phi with I_F, compression by Lambda_j, and finite direct sums preserve complete positivity, so every Upsilon'_j and Upsilon' are CP, and at every amplification the direct-sum maximum norm and ||Lambda_j|| <= 1 give ||Upsilon'||_cb <= 1 with no block-count or amplification factor.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** For each j, T->Phi(T) tensor I_F is CP because Phi is CP and tensoring with an identity representation preserves complete positivity; compression A->Lambda_j^*A Lambda_j is CP. Their composition Upsilon'_j is CP. At every matrix level, positivity in the finite direct sum B=direct-sum_j B(L_j) is coordinatewise, so Upsilon'=(Upsilon'_j)_j is CP.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.2

**Statement:** For every q>=1 and T in M_q(B(H)), the amplification Phi_q is UCP and hence contractive, and compression gives ||(Upsilon'_j)_q(T)||<=||Lambda_j||^2*||Phi_q(T)||<=||T||. The norm in M_q(B)=direct-sum_j M_q(B(L_j)) is max_j of the component norms; therefore ||Upsilon'_q(T)||<=||T|| for every q, and taking suprema gives ||Upsilon'||_cb<=1 without any factor depending on q or m.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

