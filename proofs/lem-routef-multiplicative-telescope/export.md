# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness; for every integer n >= 1 and all X, Y in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Multiplicative telescope: for rho_mult := min{rho_T, rho_id, rho_DeltaPhi, rho_Upsilon} and 0 <= eta <= rho_mult, every amplification satisfies ||Upsilon_n(Delta_n X Delta_n Y) - XY|| <= [C_Upsilon+2*(C_2+C_theta+C_Delta)]*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Radius and operator-norm consequences. Fix the globally chosen W_RF, an admissible input and its chosen S, Delta', Delta, Upsilon', Upsilon, and fix n>=1 and X,Y in M_n(B). Assume 0<=eta<=rho_mult. By def-routef-raw-factor-setting (1.1),(1.2),(1.5), rho_mult=min{rho_T,rho_id,rho_DeltaPhi,rho_Upsilon}, rho_DeltaPhi=min{rho_theta,rho_Delta,rho_2}, rho_id^corr=min{rho_theta,rho_AI,epsilon_E/C_A}, rho_id=min{rho_AI,epsilon_E/C_A}, rho_T<=rho_theta, and C_T=C_theta+3*C_V. Hence eta is in the ranges of lem-routef-raw-factor-norms, lem-routef-raw-factor-identities, lem-routef-delta-normalization-closeness, lem-routef-delta-phi-product, and lem-routef-upsilon-normalization-closeness. The first gives ||tilde-Upsilon||_cb<=1+C_T*eta. Moreover rho_T<=1/[4(1+C_theta)] and rho_T<=1/[4(1+C_V)], while C_theta,C_V>=0, so C_T*eta<=C_theta/[4(1+C_theta)]+3*C_V/[4(1+C_V)]<=1 and therefore ||tilde-Upsilon||_cb<=2. The normalization lemma says Delta is UCP; consequently Delta is completely contractive: for each amplification, unital complete positivity and the 2-by-2/Schwarz argument give Delta_n(Z)^*Delta_n(Z)<=Delta_n(Z^*Z)<=||Z||^2 I, hence ||Delta_n(Z)||<=||Z||. In particular ||Delta_n X Delta_n Y||<=||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Exact telescope identity. Under the same choices and radius, put Z:=Delta_n(X)Delta_n(Y) and E:=tilde-Phi_n(Z)-tilde-Delta_n(XY). By lem-routef-raw-factor-identities, tilde-Delta tilde-Upsilon=tilde-Phi and tilde-Upsilon tilde-Delta=I_B; amplification preserves these composition identities. Thus tilde-Upsilon_n tilde-Phi_n=tilde-Upsilon_n tilde-Delta_n tilde-Upsilon_n=tilde-Upsilon_n and tilde-Upsilon_n tilde-Delta_n(XY)=XY. Adding and subtracting tilde-Upsilon_n(Z) therefore gives the exact equality Upsilon_n(Z)-XY=(Upsilon_n-tilde-Upsilon_n)(Z)+tilde-Upsilon_n(E).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Estimate the two telescope terms and conclude. By lem-routef-upsilon-normalization-closeness, ||Upsilon-tilde-Upsilon||_cb<=C_Upsilon*eta, so complete-contractivity of Delta yields ||(Upsilon_n-tilde-Upsilon_n)(Z)||<=C_Upsilon*eta*||X||*||Y||. By lem-routef-delta-phi-product, ||E||<=(C_2+C_theta+C_Delta)*eta*||X||*||Y||, and the bound ||tilde-Upsilon||_cb<=2 yields ||tilde-Upsilon_n(E)||<=2*(C_2+C_theta+C_Delta)*eta*||X||*||Y||. Applying the triangle inequality to the exact identity gives ||Upsilon_n(Delta_n X Delta_n Y)-XY||<=[C_Upsilon+2*(C_2+C_theta+C_Delta)]*eta*||X||*||Y||, as required for every n,X,Y.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Local radius consequences and first-term estimate. Under the hypotheses and notation of root node 1, fix n>=1 and X,Y in M_n(B), assume 0<=eta<=rho_mult, and define Z:=Delta_n(X)Delta_n(Y). From rho_mult=min{rho_T,rho_id,rho_DeltaPhi,rho_Upsilon}, rho_DeltaPhi=min{rho_theta,rho_Delta,rho_2}, rho_id=min{rho_AI,epsilon_E/C_A}, and rho_id^corr=min{rho_theta,rho_AI,epsilon_E/C_A}, we have eta<=rho_T, eta<=rho_Delta, eta<=rho_DeltaPhi, eta<=rho_Upsilon, and, because rho_T<=rho_theta, eta<=rho_id^corr. Thus the stated upstream lemmas apply. In particular, lem-routef-delta-normalization-closeness makes Delta UCP, so Delta_n is unital completely positive and hence satisfies Kadison-Schwarz: Delta_n(T)^*Delta_n(T)<=Delta_n(T^*T)<=||T||^2 I. Therefore each Delta_n is contractive and ||Z||<=||X||*||Y||. Also lem-routef-raw-factor-norms gives ||tilde-Upsilon||_cb<=1+C_T*eta. Here C_theta=12*(sqrt(2)-1)>0, bar C_E=max{1,C_E}>=1, C_A=20+(211/8)*C_theta>0, and C_V=bar C_E*C_A>=0. Since C_T=C_theta+3*C_V, eta<=rho_T<=1/[4(1+C_theta)] and eta<=rho_T<=1/[4(1+C_V)], we get C_T*eta<=C_theta/[4(1+C_theta)]+3*C_V/[4(1+C_V)]<=1, hence ||tilde-Upsilon||_cb<=2. Finally lem-routef-upsilon-normalization-closeness gives ||Upsilon-tilde-Upsilon||_cb<=C_Upsilon*eta, so ||(Upsilon_n-tilde-Upsilon_n)(Z)||<=C_Upsilon*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Local error definition, exact identity, and second-term estimate. Under the hypotheses of root node 1 and with Z from node 1.3.1, define E:=tilde-Phi_n(Z)-tilde-Delta_n(XY). The radius conclusions in node 1.3.1 permit lem-routef-raw-factor-identities and lem-routef-delta-phi-product. Amplifying tilde-Delta tilde-Upsilon=tilde-Phi and tilde-Upsilon tilde-Delta=I_B gives tilde-Upsilon_n tilde-Phi_n=tilde-Upsilon_n tilde-Delta_n tilde-Upsilon_n=tilde-Upsilon_n and tilde-Upsilon_n tilde-Delta_n(XY)=XY. Hence, by direct expansion, Upsilon_n(Z)-XY=(Upsilon_n-tilde-Upsilon_n)(Z)+tilde-Upsilon_n(tilde-Phi_n(Z)-tilde-Delta_n(XY))=(Upsilon_n-tilde-Upsilon_n)(Z)+tilde-Upsilon_n(E). Moreover lem-routef-delta-phi-product gives ||E||<=(C_2+C_theta+C_Delta)*eta*||X||*||Y||, and node 1.3.1 gives ||tilde-Upsilon||_cb<=2; therefore ||tilde-Upsilon_n(E)||<=2*(C_2+C_theta+C_Delta)*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Conclusion from the two explicit telescope bounds. By the exact equality in node 1.3.2, the triangle inequality, the first-term estimate in node 1.3.1, and the second-term estimate in node 1.3.2, ||Upsilon_n(Delta_n X Delta_n Y)-XY||=||Upsilon_n(Z)-XY||<=[C_Upsilon+2*(C_2+C_theta+C_Delta)]*eta*||X||*||Y||. Since n>=1 and X,Y were arbitrary under the root hypotheses, this is precisely the conclusion asserted by node 1.3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

