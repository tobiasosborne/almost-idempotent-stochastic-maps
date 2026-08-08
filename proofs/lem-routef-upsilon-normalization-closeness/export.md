# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, and every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and for every X in B(H), writing the fields of (W_RF,S) as the unqualified symbols below: Upsilon UCP normalization: with C_Upsilon := 6*C_T+7*C_Upsilon' and rho_Upsilon := min{rho_unit, rho_Upsilon', [2*(C_T+C_Upsilon')]^(-1)}, for 0 <= eta <= rho_Upsilon, b = Upsilon'(I) is invertible and Upsilon(X) = b^(-1/2)*Upsilon'(X)*b^(-1/2) is UCP with ||Upsilon - tilde-Upsilon||_cb <= C_Upsilon*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix W_RF, (H,Phi,eta), S, Delta-prime, Delta, Upsilon-prime, and X exactly as quantified in node 1, and assume 0 <= eta <= rho_Upsilon. Then the scalar definition of rho_Upsilon and the imported lemmas give eta <= rho_unit, eta <= rho_Upsilon-prime, Upsilon-prime completely positive, ||Upsilon-prime-tilde-Upsilon||_cb <= C_Upsilon-prime*eta, and ||tilde-Upsilon(I)-I|| <= C_T*eta; moreover d:=(C_T+C_Upsilon-prime)*eta satisfies 0 <= d <= 1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** The ambient objects have the required types and common witness package because lem-routef-raw-factor-setting-formation supplies W_RF and S, lem-routef-delta-prime-closeness supplies the fixed Delta', and lem-routef-delta-normalization-closeness supplies the fixed Delta from that same Delta'; thus lem-routef-upsilon-prime-closeness applies to the fixed Upsilon'.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** From rho_Upsilon=min{rho_unit,rho_Upsilon',[2*(C_T+C_Upsilon')]^(-1)} and 0<=eta<=rho_Upsilon, one has eta<=rho_unit, eta<=rho_Upsilon', and eta<=[2*(C_T+C_Upsilon')]^(-1). Applying lem-routef-raw-factor-units and lem-routef-upsilon-prime-closeness gives ||tilde-Upsilon(I)-I||<=C_T*eta, Upsilon' CP, and ||Upsilon'-tilde-Upsilon||_cb<=C_Upsilon'*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** The scalar ledger in def-routef-raw-factor-setting makes C_T and C_Upsilon' finite and nonnegative, so d=(C_T+C_Upsilon')*eta is nonnegative; multiplying eta<=[2*(C_T+C_Upsilon')]^(-1) by C_T+C_Upsilon' gives d<=1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.1

**Statement:** By lem-routef-raw-factor-setting-formation, C_theta=12*(sqrt(2)-1) and C_A=20+(211/8)*C_theta are finite positive reals, eta_A and epsilon_E are positive, C_E is a finite real, and all remaining scalar quantities are defined by equations (1.1)-(1.8) of def-routef-raw-factor-setting. Those equations give bar-C_E=max{1,C_E}>=1, C_V=bar-C_E*C_A>0, C_T=C_theta+3*C_V>0, and recursively finite nonnegative C_Delta-prime,C_Delta,C_2,C_3,C_N,C_R,C_L and C_Upsilon'=1+C_theta+2*C_Delta+2*C_L>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.2

**Statement:** Since C_T+C_Upsilon'>0 and eta<=[2*(C_T+C_Upsilon')]^(-1), multiplication by the positive scalar C_T+C_Upsilon' gives d=(C_T+C_Upsilon')*eta<=1/2; since eta>=0, also d>=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** Notation convention for the tree: Upsilon-prime means the contract's Upsilon', and C_Upsilon-prime means the contract's C_Upsilon'; no new map or scalar is introduced.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For b:=Upsilon-prime(I), the conclusions of 1.1 imply b is positive and ||b-I|| <= d <= 1/2; consequently b is invertible, c:=b^(-1/2) exists, ||b|| <= 3/2, ||c|| <= 3/2, and ||c-I|| <= ||b-I|| <= d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Because Upsilon' is CP, b=Upsilon'(I) is positive. Since ||I||=1, evaluation at I is bounded by cb norm, and the triangle inequality with 1.1 gives ||b-I||<=||Upsilon'(I)-tilde-Upsilon(I)||+||tilde-Upsilon(I)-I||<=(C_Upsilon'+C_T)*eta=d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For positive b with ||b-I||<=d<=1/2, the finite-dimensional C*-algebra spectral theorem gives sigma(b) subset [1-d,1+d] subset [1/2,3/2]. Hence b is invertible, c=b^(-1/2) exists by continuous functional calculus, ||b||<=3/2, and ||c||<=sqrt(2)<=3/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** For every t in [1/2,3/2], |t^(-1/2)-1|=|t-1|/[sqrt(t)*(1+sqrt(t))]<=|t-1| because sqrt(t)*(1+sqrt(t))>=1. Functional calculus therefore gives ||c-I||<=||b-I||<=d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** With c=b^(-1/2), the map Upsilon(Y):=c*Upsilon-prime(Y)*c from B(H) to B is completely positive and unital, hence UCP; furthermore ||Upsilon-prime||_cb <= ||b|| <= 3/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** At every matrix level q, positivity of (id_q tensor Upsilon') and conjugation by I_q tensor c imply positivity of id_q tensor Upsilon; hence Upsilon is CP. Also Upsilon(I)=c*b*c=I by functional calculus, so Upsilon is unital and therefore UCP by def-ucp-map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Every amplification id_q tensor Upsilon is again UCP and therefore contractive by def-ucp-map, so ||Upsilon||_cb<=1; unitality gives ||Upsilon||_cb>=||Upsilon(I)||=1, hence ||Upsilon||_cb=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** By validated node 1.3.1, Upsilon is UCP. For each q>=1, id_{M_q} tensor Upsilon is unital because it sends I_q tensor I to itself, and it is completely positive because for every r>=1 its r-th amplification is, under the canonical identification M_r(M_q(B(H)))=M_{rq}(B(H)) and the corresponding codomain identification, the (rq)-th amplification id_{M_{rq}} tensor Upsilon, which is positive since Upsilon is CP. Thus every q-th amplification is UCP and hence contractive by def-ucp-map. Taking the supremum over q gives ||Upsilon||_cb<=1. Conversely the q=1 level gives ||Upsilon||_cb>=||Upsilon||>=||Upsilon(I)||/||I||=1, since Upsilon(I)=I and ||I||=1. Therefore ||Upsilon||_cb=1.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** The relation Upsilon(Y)=c*Upsilon'(Y)*c and c=b^(-1/2) rearranges to Upsilon'(Y)=b^(1/2)*Upsilon(Y)*b^(1/2). Left and right multiplication at every matrix level have norms at most ||b^(1/2)||, so ||Upsilon'||_cb<=||b^(1/2)||^2*||Upsilon||_cb=||b||<=3/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The identities Upsilon-Upsilon-prime=(c-I)Upsilon-prime c+Upsilon-prime(c-I), together with 1.2 and 1.3, give ||Upsilon-Upsilon-prime||_cb <= 6d. Therefore the triangle inequality and d=(C_T+C_Upsilon-prime)*eta yield ||Upsilon-tilde-Upsilon||_cb <= (6*C_T+7*C_Upsilon-prime)*eta=C_Upsilon*eta, completing every conclusion of node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** For every Y, adding and subtracting Upsilon'(Y)c gives Upsilon(Y)-Upsilon'(Y)=(c-I)*Upsilon'(Y)*c+Upsilon'(Y)*(c-I). Taking amplified norms and then the supremum yields ||Upsilon-Upsilon'||_cb<=||c-I||*||Upsilon'||_cb*(||c||+1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Using ||c-I||<=d, ||Upsilon'||_cb<=3/2, and ||c||<=3/2 from 1.2-1.3 gives ||Upsilon-Upsilon'||_cb<=(15/4)*d<=6*d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** By the cb-norm triangle inequality and 1.1, ||Upsilon-tilde-Upsilon||_cb<=6*d+C_Upsilon'*eta=[6*C_T+7*C_Upsilon']*eta=C_Upsilon*eta. Together with 1.2 and 1.3 this proves invertibility, the displayed normalization formula for every X in B(H), UCP, and the claimed closeness at the stated rho_Upsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

