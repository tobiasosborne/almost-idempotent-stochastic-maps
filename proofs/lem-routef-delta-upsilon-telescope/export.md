# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Delta-Upsilon telescope: for rho_DeltaUpsilon := min{rho_theta, rho_T, rho_id, rho_Delta, rho_Upsilon} and 0 <= eta <= rho_DeltaUpsilon, ||Delta Upsilon - Phi||_cb <= (C_theta+C_Delta+2*C_Upsilon)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix arbitrary W_RF, (H,Phi,eta), S, Delta', Delta, Upsilon', and Upsilon exactly as quantified in node 1, and assume 0 <= eta <= rho_DeltaUpsilon.  The definition rho_DeltaUpsilon=min{rho_theta,rho_T,rho_id,rho_Delta,rho_Upsilon}, together with rho_theta=1/8 and rho_id=min{rho_AI,epsilon_E/C_A}, implies eta is in the ranges of the following imported conclusions: ||tilde-Phi-Phi||_cb <= C_theta*eta by lem-routef-functional-calculus-closeness; tilde-Delta tilde-Upsilon=tilde-Phi by lem-routef-raw-factor-identities; ||tilde-Delta||_cb <= 1+C_T*eta by lem-routef-raw-factor-norms; ||Delta-tilde-Delta||_cb <= C_Delta*eta and Delta is UCP by lem-routef-delta-normalization-closeness; and ||Upsilon-tilde-Upsilon||_cb <= C_Upsilon*eta and Upsilon is UCP by lem-routef-upsilon-normalization-closeness.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** In the same setting, C_T*eta <= 1, hence ||tilde-Delta||_cb <= 2; also ||Upsilon||_cb=1.  Indeed, def-routef-raw-factor-setting gives C_T=C_theta+3*C_V and rho_T <= min{[4*(1+C_theta)]^(-1),[4*(1+C_V)]^(-1)}.  The formation data in lem-routef-raw-factor-setting-formation make C_theta and C_V nonnegative, so eta<=rho_T gives C_T*eta <= C_theta/[4*(1+C_theta)]+3*C_V/[4*(1+C_V)] <= 1/4+3/4=1.  The first bound now follows from lem-routef-raw-factor-norms.  The second is the standard amplification contractivity of a UCP map (and its value on the unit gives norm at least one), applied to the Upsilon furnished by lem-routef-upsilon-normalization-closeness.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Algebraic telescope implication: in any instance of the setting of node 1, suppose tilde-Delta tilde-Upsilon=tilde-Phi, ||Delta-tilde-Delta||_cb<=C_Delta*eta, ||Upsilon||_cb=1, ||tilde-Delta||_cb<=2, ||Upsilon-tilde-Upsilon||_cb<=C_Upsilon*eta, and ||tilde-Phi-Phi||_cb<=C_theta*eta.  For every amplification level q>=1, the identity tilde-Delta_q tilde-Upsilon_q=tilde-Phi_q gives Delta_q Upsilon_q-Phi_q=(Delta_q-tilde-Delta_q)Upsilon_q+tilde-Delta_q(Upsilon_q-tilde-Upsilon_q)+(tilde-Phi_q-Phi_q).  Triangle inequality and submultiplicativity give ||Delta_q Upsilon_q-Phi_q|| <= (C_Delta*eta)*1+2*(C_Upsilon*eta)+C_theta*eta=(C_theta+C_Delta+2*C_Upsilon)*eta.  Taking the supremum over q gives ||Delta Upsilon-Phi||_cb <= (C_theta+C_Delta+2*C_Upsilon)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

