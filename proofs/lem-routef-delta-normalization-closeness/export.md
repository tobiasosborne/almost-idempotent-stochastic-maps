# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result and for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and for every X in S.B, writing the fields of (W_RF,S) as the unqualified symbols below: Delta UCP normalization: with C_Delta := 6*C_T+7*C_Delta' and rho_Delta := min{rho_unit, rho_Delta', [2*(C_T+C_Delta')]^(-1)}, for 0 <= eta <= rho_Delta, a = Delta'(I) is invertible and Delta(X) = a^(-1/2)*Delta'(X)*a^(-1/2) is UCP with ||Delta - tilde-Delta||_cb <= C_Delta*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix W_RF, an admissible input and supplied setting S, and a Delta' supplied by lem-routef-delta-prime-closeness, and assume 0 <= eta <= rho_Delta. Put D := C_Delta' and d := (C_T+D)*eta. By def-routef-raw-factor-setting, rho_Delta <= rho_unit and rho_Delta <= rho_Delta'. Thus lem-routef-raw-factor-units and lem-routef-delta-prime-closeness give that Delta' is CP, ||Delta'-tilde-Delta||_cb <= D*eta, and ||tilde-Delta(I)-I|| <= C_T*eta. Hence a:=Delta'(I) is positive and ||a-I|| <= ||Delta'(I)-tilde-Delta(I)||+||tilde-Delta(I)-I|| <= d. Also C_theta=12*(sqrt(2)-1)>0 and, by lem-routef-raw-factor-setting-formation and def-routef-raw-factor-setting, C_A>0, bar(C_E)>=1, C_V=bar(C_E)*C_A>0, C_T=C_theta+3*C_V>0, and D=C_T+4*C_theta>0. Since rho_Delta <= [2*(C_T+D)]^(-1), 0 <= eta <= rho_Delta implies 0 <= d <= 1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For any positive a in the finite-dimensional target algebra with ||a-I|| <= d <= 1/2, finite-dimensional spectral calculus gives spectrum(a) contained in [1-d,1+d] contained in [1/2,3/2]. Thus a is invertible. If c:=a^(1/2), b:=a^(-1/2), and s:=||c-I||, then bc=cb=I and s <= d, because on spectrum(a), |sqrt(lambda)-1|=|lambda-1|/(sqrt(lambda)+1) <= |lambda-1|. The triangle inequality also gives ||c|| <= 1+s.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Under the conclusions of nodes 1.1 and 1.2, define Delta(X):=b*Delta'(X)*b for every X in B. The map Delta is CP: for every q, Delta_q is the composition of the positive map Delta'_q with conjugation by I_q tensor b, which preserves positivity. It is unital because Delta(I)=b*a*b=I. Hence Delta is UCP by def-ucp-map. Moreover every amplification Delta_q is itself UCP and therefore contractive, so ||Delta_q(Y)|| <= ||Y|| for every q and Y.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Under the conclusions of nodes 1.1-1.3, for every q write c_q:=I_q tensor c and b_q:=I_q tensor b. From Delta_q(Y)=b_q*Delta'_q(Y)*b_q and c_q*b_q=b_q*c_q=I, one has Delta'_q(Y)=c_q*Delta_q(Y)*c_q. Therefore Delta'_q(Y)-Delta_q(Y)=(c_q-I)*Delta_q(Y)*c_q+Delta_q(Y)*(c_q-I). Contractivity of Delta_q, ||c_q-I||=s, and ||c_q||=||c||<=1+s yield ||Delta'_q(Y)-Delta_q(Y)|| <= s*(2+s)*||Y|| <= d*(2+d)*||Y|| <= 3*d*||Y||. Taking the supremum over q gives ||Delta'-Delta||_cb <= 3*d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** For the fixed data of node 1.1, nodes 1.1-1.4 and the cb triangle inequality give ||Delta-tilde-Delta||_cb <= ||Delta-Delta'||_cb+||Delta'-tilde-Delta||_cb <= 3*d+D*eta=(3*C_T+4*D)*eta. Since C_T,D>=0, 3*C_T+4*D <= 6*C_T+7*D=C_Delta by def-routef-raw-factor-setting. Thus ||Delta-tilde-Delta||_cb <= C_Delta*eta. Together with nodes 1.2 and 1.3, this proves invertibility of a and the asserted UCP formula and bound for every X in S.B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

