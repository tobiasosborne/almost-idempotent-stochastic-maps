# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Route F scalar threshold: let eta_K := min{rho_fac, (24*K)^(-1), 1}; then eta_K > 0, and every 0 <= eta <= eta_K satisfies eta <= rho_fac, 0 <= eta <= min{(24*K)^(-1),1}, 3*K*eta <= 1/8 < 1, and 3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6 < 1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** In the ambient configuration quantified in node 1, lem-routef-raw-factor-setting-formation supplies the single global W_RF and the datum S, while lem-routef-delta-prime-closeness, lem-routef-delta-normalization-closeness, lem-routef-upsilon-prime-closeness, and lem-routef-upsilon-normalization-closeness supply the stipulated Delta', Delta, Upsilon', and Upsilon in that order. Applying lem-routef-k-finiteness to exactly this chain gives that K is a finite universal real scalar and rho_fac>0. Moreover, equation (1.6) of def-routef-raw-factor-setting defines K as a maximum whose entries include 1, so K>=1>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** By lem-routef-k-finiteness in the ambient configuration of node 1, rho_fac>0 and K is a finite real scalar; independently, equation (1.6) of def-routef-raw-factor-setting makes K a maximum containing 1, so K>=1>0. Hence rho_fac, (24*K)^(-1), and 1 are all strictly positive. The minimum of finitely many strictly positive real numbers is strictly positive, so equation (1.8), eta_K=min{rho_fac,(24*K)^(-1),1}, gives eta_K>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Fix any real eta with 0<=eta<=eta_K. Equation (1.8) of def-routef-raw-factor-setting and the defining order property of a minimum give eta<=rho_fac, eta<=(24*K)^(-1), and eta<=1; hence 0<=eta<=min{(24*K)^(-1),1}. Equation (1.6) makes K>=1>0, so multiplying eta<=(24*K)^(-1)=1/(24*K) by 3*K and by 4*K gives 3*K*eta<=3/24=1/8<1 and 4*K*eta<=4/24=1/6<1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Fix any real eta with 0<=eta<=eta_K. By (1.8), eta<=(24*K)^(-1); by (1.6), K>=1>0. Put x:=3*K*eta. Then 0<=x<=1/8, so 1-x>0 and 1-4*x>=1/2>0. Since 4*K*eta=(4/3)*x, common-denominator arithmetic gives 4*K*eta-x/(1-x)=x*(1-4*x)/(3*(1-x))>=0. Therefore 3*K*eta/(1-3*K*eta)=x/(1-x)<=4*K*eta. Also eta<=(24*K)^(-1) gives 4*K*eta<=1/6<1/2, completing the rational chain.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

