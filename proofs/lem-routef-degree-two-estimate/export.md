# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness; for every integer n >= 1 and all X, Y in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Route F degree-two estimate: with C_2 := C_Delta'+4*C_Delta and rho_2 := min{rho_prod, rho_Delta', rho_Delta}, for 0 <= eta <= rho_2, every amplification satisfies ||Phi_n(Delta_n X Delta_n Y) - Delta_n(XY)|| <= C_2*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix arbitrary W_RF, S, Delta', Delta, n, X, Y as quantified in node 1 and assume 0 <= eta <= rho_2. By def-routef-raw-factor-setting and lem-routef-raw-factor-setting-formation, rho_2=min{rho_prod,rho_Delta',rho_Delta}, rho_prod=rho_T, rho_theta=1/8, rho_T <= rho_theta, rho_T <= 1/[4(1+C_V)], and C_theta,C_V,C_T,C_Delta',C_Delta are nonnegative. Hence eta <= rho_prod=rho_T <= rho_theta=1/8, eta <= rho_Delta', eta <= rho_Delta, and C_V*eta <= C_V/[4(1+C_V)] <= 1/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For the arbitrary data of node 1 under 0 <= eta <= rho_2, instantiate lem-routef-raw-factor-norms, lem-routef-raw-product-estimate, lem-routef-functional-calculus-closeness, and lem-routef-delta-normalization-closeness. Since Phi and Delta are UCP, Phi_n and Delta_n are contractive. Thus ||(Delta_n-tilde-Delta_n)Z|| <= C_Delta*eta*||Z||, ||tilde-Delta_n Z|| <= (1+C_V*eta)*||Z||, ||(Phi_n-tilde-Phi_n)Z|| <= C_theta*eta*||Z||, and ||tilde-Phi_n(tilde-Delta_n X tilde-Delta_n Y)-tilde-Delta_n(XY)|| <= C_T*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For the arbitrary data of node 1 under 0 <= eta <= rho_2, the identity Delta_n X Delta_n Y-tilde-Delta_n X tilde-Delta_n Y=(Delta_n-tilde-Delta_n)X Delta_n Y+tilde-Delta_n X (Delta_n-tilde-Delta_n)Y, the C*-norm product inequality, C_V*eta <= 1/4, and the bounds supplied in the preceding admissibility/import steps give ||Phi_n(Delta_n X Delta_n Y)-Phi_n(tilde-Delta_n X tilde-Delta_n Y)|| <= (2+C_V*eta)*C_Delta*eta*||X||*||Y|| <= 3*C_Delta*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For the arbitrary data of node 1 under 0 <= eta <= rho_2, insert tilde-Phi_n at tilde-Delta_n X tilde-Delta_n Y. The functional-calculus closeness, raw product estimate, raw factor norm, and C_V*eta <= 1/4 give ||Phi_n(tilde-Delta_n X tilde-Delta_n Y)-tilde-Delta_n(XY)|| <= [C_theta*(1+C_V*eta)^2+C_T]*eta*||X||*||Y|| <= (2*C_theta+C_T)*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** For the arbitrary data of node 1 under 0 <= eta <= rho_2, lem-routef-delta-normalization-closeness at amplification n and submultiplicativity in M_n(B) give ||tilde-Delta_n(XY)-Delta_n(XY)|| <= C_Delta*eta*||XY|| <= C_Delta*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** For the arbitrary data of node 1 under 0 <= eta <= rho_2, insert successively Phi_n(tilde-Delta_n X tilde-Delta_n Y) and tilde-Delta_n(XY), apply nodes 1.3, 1.4, and 1.5 and the triangle inequality, and use C_theta >= 0, C_Delta'=C_T+4*C_theta, and C_2=C_Delta'+4*C_Delta. This yields ||Phi_n(Delta_n X Delta_n Y)-Delta_n(XY)|| <= [3*C_Delta+C_T+2*C_theta+C_Delta]*eta*||X||*||Y|| <= C_2*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

