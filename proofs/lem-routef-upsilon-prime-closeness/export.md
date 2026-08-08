# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Upsilon-prime CP closeness: with C_N, C_R, C_L, C_Upsilon' from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon', every Choi multiplicity space used below is nonzero and the componentwise construction produces CP Upsilon' with ||Upsilon' - tilde-Upsilon||_cb <= C_Upsilon'*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Under the fixed W_RF, input datum S, Delta', Delta, and 0 <= eta <= rho_Upsilon' of node 1, lem-routef-upsilon-prime-component-construction supplies the stated componentwise package: every Choi multiplicity space E_j occurring in it is nonzero, Upsilon' is CP, and ||Upsilon'||_cb <= 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** In the same setting, ||Upsilon' - tilde-Upsilon||_cb <= [1+C_theta+2*C_Delta+2*C_L]*eta = C_Upsilon'*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Because rho_Upsilon' <= rho_T <= rho_theta=1/8, lem-routef-functional-calculus-closeness applies; because the input is one to which lem-routef-raw-factor-setting-formation applies, ||Phi^2-Phi||_cb <= eta; and because Phi is UCP, ||Phi||_cb=1. Hence Phi-Phi tilde-Phi=(Phi-Phi^2)+Phi(Phi-tilde-Phi) and ||Phi-Phi tilde-Phi||_cb <= (1+C_theta)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For the package from lem-routef-upsilon-prime-component-construction define K_j(T):=Lambda_j^*(T tensor I_F)Lambda_j for T in B(H), and K(T):=(K_j(T))_j. Each Lambda_j is a contraction, so every compression K_j is CP with cb norm at most 1; the finite direct-sum norm is the maximum of component norms, hence ||K||_cb <= 1, and the defining formula for Upsilon'_j gives Upsilon'=K Phi.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** The factorization Upsilon'=K Phi and the preceding cutoff estimate give ||Upsilon'(I-tilde-Phi)||_cb=||K(Phi-Phi tilde-Phi)||_cb <= (1+C_theta)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** By nodes 1.2.1 and 1.2.2, Upsilon'=K Phi with ||K||_cb<=1 and ||Phi-Phi tilde-Phi||_cb<=(1+C_theta)*eta; cb-norm submultiplicativity therefore gives ||Upsilon'(I-tilde-Phi)||_cb=||K(Phi-Phi tilde-Phi)||_cb<=(1+C_theta)*eta.

**Type:** claim

**Inference:** cb_norm_submultiplicativity

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Since rho_Upsilon' <= rho_Delta, lem-routef-delta-normalization-closeness gives ||Delta-tilde-Delta||_cb <= C_Delta*eta; lem-routef-upsilon-prime-component-construction gives ||Upsilon'||_cb <= 1; and lem-routef-upsilon-prime-left-inverse gives ||Upsilon' Delta-I_B||_cb <= C_L*eta. Therefore ||Upsilon' tilde-Delta-I_B||_cb <= (C_Delta+C_L)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.5

**Statement:** Since rho_Upsilon' <= rho_T, lem-routef-raw-factor-norms gives ||tilde-Upsilon||_cb <= 1+C_T*eta. From (1.1), C_T=C_theta+3*C_V and rho_T <= min{[4*(1+C_theta)]^(-1),[4*(1+C_V)]^(-1)}, so C_theta*eta <= 1/4 and C_V*eta <= 1/4; thus C_T*eta <= 1 and ||tilde-Upsilon||_cb <= 2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.6

**Statement:** The input to formation has eta <= rho_id^corr, so lem-routef-raw-factor-identities gives tilde-Delta tilde-Upsilon=tilde-Phi. Consequently Upsilon'-tilde-Upsilon=Upsilon'(I-tilde-Phi)+(Upsilon' tilde-Delta-I_B)tilde-Upsilon. Applying the preceding cb estimates and submultiplicativity yields ||Upsilon'-tilde-Upsilon||_cb <= [(1+C_theta)+2*(C_Delta+C_L)]*eta=[1+C_theta+2*C_Delta+2*C_L]*eta=C_Upsilon'*eta by (1.3).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.6.1

**Statement:** Because the input to lem-routef-raw-factor-setting-formation has eta <= rho_id^corr, lem-routef-raw-factor-identities gives tilde-Delta tilde-Upsilon=tilde-Phi; direct expansion therefore verifies Upsilon'-tilde-Upsilon=Upsilon'(I-tilde-Phi)+(Upsilon' tilde-Delta-I_B)tilde-Upsilon. By node 1.2.3, the first summand has cb norm at most (1+C_theta)*eta. By nodes 1.2.4 and 1.2.5 plus cb-norm submultiplicativity, the second has cb norm at most 2*(C_Delta+C_L)*eta. The triangle inequality and C_Upsilon'=1+C_theta+2*C_Delta+2*C_L from (1.3) prove the statement of node 1.2.6.

**Type:** claim

**Inference:** triangle_inequality

**Status:** validated

**Taint:** clean

