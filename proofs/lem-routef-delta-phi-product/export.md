# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness; for every integer n >= 1 and all X, Y in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Normalized Delta product: for rho_DeltaPhi := min{rho_theta, rho_Delta, rho_2} and 0 <= eta <= rho_DeltaPhi, every amplification satisfies ||tilde-Phi_n(Delta_n X Delta_n Y) - tilde-Delta_n(XY)|| <= (C_2+C_theta+C_Delta)*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix the global package W_RF, then an arbitrary admissible input (H,Phi,eta), a datum S, Delta', Delta, an integer n>=1, and X,Y in M_n(S.B), exactly as in the root prefix. By def-routef-raw-factor-setting, rho_DeltaPhi=min{rho_theta,rho_Delta,rho_2}; hence 0<=eta<=rho_DeltaPhi implies eta<=rho_theta=1/8, eta<=rho_Delta, and eta<=rho_2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Under the fixed data and radius bounds of 1.1, lem-routef-functional-calculus-closeness gives ||tilde-Phi-Phi||_cb<=C_theta*eta, hence ||(tilde-Phi_n-Phi_n)(Z)||<=C_theta*eta*||Z|| for every Z in M_n(B(H)); and lem-routef-delta-normalization-closeness gives that Delta is UCP and ||Delta-tilde-Delta||_cb<=C_Delta*eta, hence ||(Delta_n-tilde-Delta_n)(W)||<=C_Delta*eta*||W|| for every W in M_n(S.B).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Because Delta is UCP by 1.2, def-ucp-map says every amplification Delta_n is unital positive and therefore contractive. Consequently ||Delta_n X Delta_n Y||<=||Delta_n X||*||Delta_n Y||<=||X||*||Y||; also the C*-algebra norm on M_n(S.B) gives ||XY||<=||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Since eta<=rho_2 by 1.1 and Delta',Delta are precisely the maps fixed in the root prefix, lem-routef-degree-two-estimate applies and yields ||Phi_n(Delta_n X Delta_n Y)-Delta_n(XY)||<=C_2*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Linearity gives the exact decomposition tilde-Phi_n(Delta_n X Delta_n Y)-tilde-Delta_n(XY)=(tilde-Phi_n-Phi_n)(Delta_n X Delta_n Y)+[Phi_n(Delta_n X Delta_n Y)-Delta_n(XY)]+(Delta_n-tilde-Delta_n)(XY). Therefore the triangle inequality bounds its norm by the sum of the norms of these three displayed summands.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Apply the two cb estimates of 1.2 to the first and third summands in 1.5, the norm bounds of 1.3 to their arguments, and the degree-two estimate 1.4 to the middle summand. The resulting upper bound is C_theta*eta*||X||*||Y||+C_2*eta*||X||*||Y||+C_Delta*eta*||X||*||Y||=(C_2+C_theta+C_Delta)*eta*||X||*||Y||, which is exactly the root conclusion for the arbitrary fixed data; universal generalization proves node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

