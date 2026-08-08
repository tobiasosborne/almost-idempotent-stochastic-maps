# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, and every componentwise package (m,(L_j,E_j,W_j,Sigma_j,U_js,p_js,C_j,xi_j,Lambda_j,Upsilon'_j)_{j=1}^m,F,V,Upsilon') supplied for (W_RF,S,Delta',Delta) by lem-routef-upsilon-prime-component-construction, with C_L:=C_2+C_3+2*C_R from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon', every integer q >= 1, and every Y=(Y_1,...,Y_m) in M_q(B)=direct-sum_{j=1}^m M_q(B(L_j)), ||(Upsilon'_j)_q(Delta_q(Y))-Y_j|| <= C_L*eta*||Y|| for every j, and consequently ||(Upsilon' Delta-I_B)_q(Y)|| <= C_L*eta*||Y|| and ||Upsilon' Delta-I_B||_cb <= C_L*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix the data and hypotheses of node 1, fix q>=1, Y in M_q(B), and j. Put P_jq(Y):=sum_{s,t in Sigma_j} p_js p_jt iota_js,q^* W_j,q Delta_q(hat-U_js Y hat-U_jt^*) W_j,q^* iota_jt,q. Then ||(Upsilon'_j)_q(Delta_q(Y))-P_jq(Y)|| <= (C_2+C_3)*eta*||Y||.

**Type:** claim

**Inference:** expansion and degree-two/degree-three replacement using lem-routef-upsilon-prime-component-construction, lem-routef-degree-two-estimate, and lem-routef-degree-three-estimate

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Because rho_Upsilon'=min{rho_T,rho_id,rho_Delta,rho_2,rho_3,(2*C_R)^(-1)}, 0<=eta<=rho_Upsilon' implies eta<=rho_Delta,rho_2,rho_3. By lem-routef-delta-normalization-closeness Delta is UCP, while Phi is UCP in the def-routef-raw-factor-setting datum supplied by lem-routef-raw-factor-setting-formation. Hence every Delta_q and Phi_q is unital and contractive. Also lem-routef-upsilon-prime-component-construction gives sum_s p_js=1 with p_js>=0, sum_j W_j^*W_j=I, unit xi_j and unitary U_js; consequently ||W_j,q||<=1, each iota_js,q is an isometry, and ||hat-U_js||=1.

**Type:** claim

**Inference:** minimum bounds, cited externals, and def-ucp-map

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Let A_st:=Phi_q(Delta_q(hat-U_js) Phi_q(Delta_q(Y)) Delta_q(hat-U_jt^*)). Expanding Lambda_j and Upsilon'_j from lem-routef-upsilon-prime-component-construction at level q, and using Phi_q(T)=V_q^*(T tensor I_F)V_q, gives the exact identity (Upsilon'_j)_q(Delta_q(Y))=sum_{s,t}p_js p_jt iota_js,q^* W_j,q A_st W_j,q^* iota_jt,q.

**Type:** claim

**Inference:** substitution into the component-construction formulas

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Applying lem-routef-degree-two-estimate at n=q with X=I and the present Y, and using Delta_q(I)=I, gives ||Phi_q(Delta_q(Y))-Delta_q(Y)||<=C_2*eta*||Y||. Contractivity of Phi_q and Delta_q and ||hat-U_js||=||hat-U_jt^*||=1 therefore imply ||A_st-Phi_q(Delta_q(hat-U_js)Delta_q(Y)Delta_q(hat-U_jt^*))||<=C_2*eta*||Y||.

**Type:** claim

**Inference:** lem-routef-degree-two-estimate and contractivity

**Status:** validated

**Taint:** clean

##### Node 1.1.3.1

**Statement:** For fixed s,t in Sigma_j, define A_st exactly as in node 1.1.2 by A_st:=Phi_q(Delta_q(hat-U_js) Phi_q(Delta_q(Y)) Delta_q(hat-U_jt^*)). By node 1.1.1, Delta_q(I)=I and Phi_q,Delta_q are contractive. Applying lem-routef-degree-two-estimate at n=q with X=I and the present Y gives ||Phi_q(Delta_q(Y))-Delta_q(Y)||<=C_2*eta*||Y||. With D:=Phi_q(Delta_q(Y))-Delta_q(Y), linearity gives A_st-Phi_q(Delta_q(hat-U_js)Delta_q(Y)Delta_q(hat-U_jt^*))=Phi_q(Delta_q(hat-U_js) D Delta_q(hat-U_jt^*)). Hence contractivity and ||hat-U_js||=||hat-U_jt^*||=1 imply the asserted bound <=C_2*eta*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** By lem-routef-degree-three-estimate at n=q with X=hat-U_js, Y=Y, Z=hat-U_jt^*, the second term in node 1.1.3 differs from Delta_q(hat-U_js Y hat-U_jt^*) by at most C_3*eta*||Y||. Thus each A_st has error at most (C_2+C_3)*eta*||Y||. Sandwiching by the contractions iota_js,q^* W_j,q and W_j,q^* iota_jt,q, summing with nonnegative weights, and using sum_{s,t}p_js p_jt=1 together with node 1.1.2 proves node 1.1.

**Type:** claim

**Inference:** lem-routef-degree-three-estimate, triangle inequality, and probability averaging

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Under the same fixed data, define P_jq(Y):=sum_{s,t in Sigma_j} p_js p_jt iota_js,q^* W_j,q Delta_q(hat-U_js Y hat-U_jt^*) W_j,q^* iota_jt,q. Then P_jq(Y)=alpha_j Y_j where alpha_j:=<xi_j,C_j^*C_j xi_j>, and ||P_jq(Y)-Y_j|| <= 2*C_R*eta*||Y||.

**Type:** claim

**Inference:** exact block expansion and averaged compression using lem-routef-upsilon-prime-component-construction

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Let P_j:=W_jW_j^*, let iota_j0(z):=z tensor xi_j, let u_js,q:=I_q tensor U_js on C^q tensor L_j, and let Ucal_js,q:=I_q tensor U_js tensor I_Ej on C^q tensor L_j tensor E_j. From Delta(X)=sum_k W_k^*(X_k tensor I_Ek)W_k in lem-routef-upsilon-prime-component-construction and the fact that hat-U_js Y hat-U_jt^* has only block j nonzero, Delta_q(hat-U_js Y hat-U_jt^*)=W_j,q^*[(u_js,q Y_j u_jt,q^*) tensor I_Ej]W_j,q. Substitution in P_jq(Y), with iota_js,q=Ucal_js,q iota_j0,q, gives P_jq(Y)=iota_j0,q^* [sum_s p_js Ucal_js,q^* P_j,q Ucal_js,q] (Y_j tensor I_Ej) [sum_t p_jt Ucal_jt,q^* P_j,q Ucal_jt,q] iota_j0,q.

**Type:** claim

**Inference:** block formula from lem-routef-upsilon-prime-component-construction and finite double-sum factorization

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** By the identity R_j=sum_s p_js (U_js^* tensor I_Ej)P_j(U_js tensor I_Ej)=I_Lj tensor C_j in lem-routef-upsilon-prime-component-construction, both bracketed sums in node 1.2.1 equal I_q tensor R_j=I_q tensor I_Lj tensor C_j. Therefore P_jq(Y)=iota_j0,q^*(I_q tensor I_Lj tensor C_j)(Y_j tensor I_Ej)(I_q tensor I_Lj tensor C_j)iota_j0,q=<xi_j,C_j^*C_j xi_j>Y_j=alpha_jY_j.

**Type:** claim

**Inference:** substitution of the averaged range operator and compression by xi_j

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Since C_j is a positive contraction and xi_j is a unit vector, 0<=alpha_j=<xi_j,C_j^*C_j xi_j><=1, so |1-alpha_j|=1-alpha_j. The component-construction bound 1-<xi_j,C_j^*C_j xi_j><=2*C_R*eta and ||Y_j||<=||Y|| now give ||P_jq(Y)-Y_j||=|1-alpha_j|*||Y_j||<=2*C_R*eta*||Y||, proving node 1.2.

**Type:** claim

**Inference:** positive-contraction spectral bound and lem-routef-upsilon-prime-component-construction

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** The opening clause of node 1.2 now binds P_jq(Y) explicitly by the same finite double-sum formula used in node 1.1. Therefore every occurrence of P_jq(Y) in nodes 1.2.1--1.2.3 is in scope from its ancestor 1.2, and node 1.3 combines the estimates of nodes 1.1 and 1.2 for one and the same explicitly defined operator P_jq(Y).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** By the two preceding estimates and C_L=C_2+C_3+2*C_R, every j satisfies ||(Upsilon'_j)_q(Delta_q(Y))-Y_j|| <= C_L*eta*||Y||.

**Type:** claim

**Inference:** triangle_inequality

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Since Upsilon'(T)=(Upsilon'_j(T))_j and M_q(B) has the finite direct-sum maximum norm, the component estimates give ||(Upsilon' Delta-I_B)_q(Y)|| <= C_L*eta*||Y|| for every q,Y; taking the supremum over q and nonzero Y gives ||Upsilon' Delta-I_B||_cb <= C_L*eta.

**Type:** claim

**Inference:** direct-sum norm and definition of completely bounded norm

**Status:** validated

**Taint:** clean

