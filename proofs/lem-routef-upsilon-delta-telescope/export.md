# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Upsilon-Delta telescope: for rho_UpsilonDelta := min{rho_T, rho_id, rho_Delta, rho_Upsilon} and 0 <= eta <= rho_UpsilonDelta, ||Upsilon Delta - I_B||_cb <= (C_Upsilon+2*C_Delta)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Under the ambient choices and 0 <= eta <= rho_UpsilonDelta, establish the exact raw identity, the two normalization-closeness estimates, the complete contraction of Delta, and the bound ||tilde-Upsilon||_cb <= 2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Unfolding rho_UpsilonDelta=min{rho_T,rho_id,rho_Delta,rho_Upsilon} gives eta<=rho_T, eta<=rho_Delta, and eta<=rho_Upsilon; moreover (1.1) gives rho_T<=min{rho_theta,rho_AI,epsilon_E/C_A}=rho_id^corr, so eta<=rho_id^corr.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** By lem-routef-raw-factor-identities at eta<=rho_id^corr, tilde-Upsilon tilde-Delta=I_B, and hence tilde-Upsilon_n tilde-Delta_n=(I_B)_n for every amplification n>=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** By lem-routef-delta-normalization-closeness at eta<=rho_Delta and lem-routef-upsilon-normalization-closeness at eta<=rho_Upsilon, Delta is UCP and ||Delta-tilde-Delta||_cb<=C_Delta*eta, while ||Upsilon-tilde-Upsilon||_cb<=C_Upsilon*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** Because Delta is UCP, each amplification Delta_n is UCP and therefore contractive by def-ucp-map; thus ||Delta_n||<=1 for every n>=1 (equivalently, Delta is a complete contraction).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.5

**Statement:** By lem-routef-raw-factor-norms at eta<=rho_T, ||tilde-Upsilon||_cb<=1+C_T*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.6

**Statement:** The scalar ledger in def-routef-raw-factor-setting gives C_T=C_theta+3*C_V and rho_T<=min{[4*(1+C_theta)]^(-1),[4*(1+C_V)]^(-1)}. Here C_theta=12*(sqrt(2)-1)>=0 and C_V=max{1,C_E}*C_A>=0 by lem-routef-raw-factor-setting-formation. Hence eta<=rho_T implies C_theta*eta<=1/4 and C_V*eta<=1/4, so C_T*eta<=1 and therefore 1+C_T*eta<=2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Assuming the facts established in child 1.1, apply the amplification-level two-term telescope and then take the supremum over amplification levels to obtain ||Upsilon Delta - I_B||_cb <= (C_Upsilon+2*C_Delta)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For each n>=1, amplification respects sums and compositions; using tilde-Upsilon_n tilde-Delta_n=(I_B)_n, the exact identity (Upsilon Delta-I_B)_n=(Upsilon_n-tilde-Upsilon_n)Delta_n+tilde-Upsilon_n(Delta_n-tilde-Delta_n) holds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For each n>=1, the triangle inequality and submultiplicativity applied to child 1.2.1, together with ||Upsilon_n-tilde-Upsilon_n||<=C_Upsilon*eta, ||Delta_n||<=1, ||tilde-Upsilon_n||<=2, and ||Delta_n-tilde-Delta_n||<=C_Delta*eta from child 1.1, give ||(Upsilon Delta-I_B)_n||<=(C_Upsilon+2*C_Delta)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Taking the supremum over all n>=1 in the uniform estimate of child 1.2.2 and using the definition of completely bounded norm gives ||Upsilon Delta-I_B||_cb<=(C_Upsilon+2*C_Delta)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** By validated node 1.2.2, for every integer n>=1 one has ||(Upsilon Delta-I_B)_n||<=(C_Upsilon+2*C_Delta)*eta. This node explicitly depends on 1.2.2. Therefore, by the definition ||T||_cb:=sup_{n>=1}||T_n|| applied to T=Upsilon Delta-I_B, taking the supremum of the preceding uniform inequalities yields ||Upsilon Delta-I_B||_cb<=sup_{n>=1}(C_Upsilon+2*C_Delta)*eta=(C_Upsilon+2*C_Delta)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

