# Proof Export

## Node 1

**Statement:** Halo-robust height collapse: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), and hidden top vertex v of height H, let sigma be the invisible mass of v, sigma_g the halo-robust invisible mass (the positive coefficient mass v places on rows at ell-1 distance > tau/4 from conv W, tau = sqrt(delta)), and nu_v the row negative mass; then H * (1 - sigma_g) <= (sigma - sigma_g) * tau/4 + nu_v * (2 + 4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Set C=conv{p_w:w in W(P)}, H_j=dist_1(p_j,C), a_j=P_{vj}, a_j^+=max(a_j,0), a_j^-=max(-a_j,0), and tau=sqrt(delta). Let G={j:H_j>tau/4}, B={j:0<H_j<=tau/4}, and Z={j:H_j=0}. Then P^2=P gives p_v=sum_j a_j p_j; lem-mass-split gives sum_j a_j^+=1+nu_v; sigma=sum_{j in G union B} a_j^+ and sigma_g=sum_{j in G} a_j^+; hence sigma_g<=sigma, sigma-sigma_g=sum_{j in B} a_j^+, and sum_{j notin G} a_j^+ - sum_j a_j^-=1-sigma_g. Also H_j<=H for every row j, H_j=0 on Z, H_j<=tau/4 on B union Z, and every x in C satisfies ||x-p_j||_1<=2+4*delta for every row j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** For an exact signed idempotent P, P^2=P and a_j=P_{vj} imply row reproduction p_v=sum_j a_j p_j. The row sum condition gives sum_j a_j=1, and with a_j=a_j^+-a_j^- and nu_v=sum_j a_j^- for row v, lem-mass-split gives sum_j a_j^+=1+nu_v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** By def-invisible-mass and the halo-robust sigma_g definition in the contract, sigma is the sum of a_j^+ over rows with H_j>0 and sigma_g is the sum of a_j^+ over rows with H_j>tau/4. With G={H_j>tau/4}, B={0<H_j<=tau/4}, and Z={H_j=0}, this gives sigma=sum_{G union B}a_j^+, sigma_g=sum_G a_j^+, sigma_g<=sigma, sigma-sigma_g=sum_B a_j^+, and sum_{j notin G}a_j^+-sum_j a_j^-=1-sigma_g by node 1.1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** By def-height, v is a hidden top vertex with H=dist_1(p_v,C) equal to the maximum row distance from C, so H_j<=H for every row j; by the definitions of B and Z, H_j<=tau/4 on B union Z and H_j=0 on Z. By the row-geometry clause of def-signed-idempotent, pairwise row distances are at most 2+4*delta; since every x in C is a convex combination of visible rows, convexity of the l1 norm gives ||x-p_j||_1<=2+4*delta for every x in C and every row j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** If sigma_g>=1, the desired inequality follows immediately: H>=0 gives H*(1-sigma_g)<=0, while sigma-sigma_g>=0, tau>=0, nu_v>=0, and 2+4*delta>=0 make the right side nonnegative.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Assume sigma_g<1 and define q=(p_v-sum_{j in G} a_j^+ p_j)/(1-sigma_g). Since p_v=sum_{j in G} a_j^+p_j+(1-sigma_g)q, the coefficients a_j^+ on G are nonnegative and have sum sigma_g<1, and H_j<=H=dist_1(p_v,C) for j in G, lem-residual-lower gives H<=dist_1(q,C); multiplying by 1-sigma_g gives H*(1-sigma_g)<= (1-sigma_g)*dist_1(q,C).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Under sigma_g<1, the same q has numerator sum_{j notin G} a_j^+ p_j - sum_j a_j^- p_j and denominator m=1-sigma_g>0. Applying lem-residual-upper with positive coefficients a_j^+ for j notin G, negative coefficients a_j^- for all j, and D_j=2+4*delta gives (1-sigma_g)*dist_1(q,C) <= sum_{j notin G} a_j^+ H_j + nu_v*(2+4*delta) <= (sigma-sigma_g)*tau/4 + nu_v*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** When sigma_g<1 and q=(p_v-sum_{j in G}a_j^+p_j)/(1-sigma_g), row reproduction gives q=(sum_{j notin G}a_j^+p_j - sum_j a_j^-p_j)/(1-sigma_g). Node 1.1.2 gives m=sum_{j notin G}a_j^+-sum_j a_j^-=1-sigma_g>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** The hypotheses of lem-residual-upper hold for C, b_j=a_j^+ on j notin G, c_j=a_j^- on all rows, p_j the corresponding rows, r_j the corresponding negative-source rows, m=1-sigma_g, and D_j=2+4*delta: all coefficients are nonnegative, q has the required quotient form, and node 1.1.3 supplies ||x-r_j||_1<=D_j for every x in C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** By lem-residual-upper, (1-sigma_g)*dist_1(q,C) <= sum_{j notin G}a_j^+H_j + nu_v*(2+4*delta). Since notin G is B union Z, node 1.1.3 gives H_j<=tau/4 on B and H_j=0 on Z, while node 1.1.2 gives sum_B a_j^+=sigma-sigma_g; therefore sum_{j notin G}a_j^+H_j <= (sigma-sigma_g)*tau/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.3.1

**Statement:** Under the sigma_g<1 branch and the q defined in node 1.3, the quotient form needed for lem-residual-upper is available inside this node: node 1.1.1 gives p_v=sum_j(a_j^+-a_j^-)p_j, so subtracting sum_{j in G}a_j^+p_j from the definition (1-sigma_g)q=p_v-sum_{j in G}a_j^+p_j gives (1-sigma_g)q=sum_{j notin G}a_j^+p_j-sum_j a_j^-p_j. Node 1.1.2 gives sum_{j notin G}a_j^+-sum_j a_j^-=1-sigma_g, and the current branch has sigma_g<1, hence m=1-sigma_g>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.3.2

**Statement:** For this application of lem-residual-upper, take C=conv W, the positive coefficients b_j=a_j^+ over indices j notin G, the negative coefficients c_k=a_k^- over all row indices k, the corresponding points p_j and r_k to be those rows of P, and D_k=2+4*delta. All coefficients are nonnegative by definition of positive and negative parts. The quotient hypothesis holds because row reproduction gives p_v=sum_j(a_j^+-a_j^-)p_j and q is defined by (1-sigma_g)q=p_v-sum_{j in G}a_j^+p_j, so q=(sum_{j notin G}a_j^+p_j-sum_k a_k^-p_k)/(1-sigma_g); node 1.1.2 gives m=sum_{j notin G}a_j^+-sum_k a_k^-=1-sigma_g, and the branch sigma_g<1 gives m>0. Finally D_k>=0 and node 1.1.3 gives ||x-r_k||_1<=D_k for every x in C. Thus lem-residual-upper yields (1-sigma_g)*dist_1(q,C)<=sum_{j notin G}a_j^+ dist_1(p_j,C)+sum_k a_k^-(2+4*delta)=sum_{j notin G}a_j^+H_j+nu_v*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.3.3

**Statement:** The remaining sum is bounded by local halo bookkeeping: node 1.4.3.3.1 gives the disjoint partition {j:notin G}=B union Z, the bounds H_j<=tau/4 on B and H_j=0 on Z, and the mass identity sum_{j in B}a_j^+=sigma-sigma_g. Therefore, as shown in node 1.4.3.3.2, nonnegativity of a_j^+ and H_j gives sum_{j notin G}a_j^+H_j=sum_{j in B}a_j^+H_j+sum_{j in Z}a_j^+H_j <= (tau/4)*sum_{j in B}a_j^+=(sigma-sigma_g)*tau/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.4.3.3.1

**Statement:** Local halo partition and mass identity, with the setup fixed explicitly: let C=C_W=conv{p_w:w in W(P)}, H_j=dist_1(p_j,C_W), a_j=P_{vj}, a_j^+=max(a_j,0), tau=sqrt(delta), G={j:H_j>tau/4}, B={j:0<H_j<=tau/4}, and Z={j:H_j=0}. Since H_j is a distance to C_W, H_j>=0 for every j, so {j:notin G}=B union Z disjointly. By def-invisible-mass, sigma is the sum of a_j^+ over rows with dist_1(p_j,C_W)>0, equivalently H_j>0. By the contract definition of the halo-robust invisible mass, sigma_g is the sum of a_j^+ over rows with dist_1(p_j,C_W)>tau/4, equivalently H_j>tau/4, i.e. over G. Since {H_j>0}=G union B disjointly, sigma=sum_{j in G}a_j^+ + sum_{j in B}a_j^+ and sigma_g=sum_{j in G}a_j^+; hence sum_{j in B}a_j^+=sigma-sigma_g. The definitions of B and Z also give H_j<=tau/4 on B and H_j=0 on Z.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.4.3.3.1.1

**Statement:** Explicit setup bridge for the verifier objection: in node 1.4.3.3.1 the symbol C is not arbitrary; it is C_W=conv{p_w:w in W(P)} from def-visible-set and def-height. The coefficients are the row-v coefficients a_j=P_{vj}, with positive parts a_j^+=max(a_j,0). Therefore def-invisible-mass applies exactly as sigma=sum_{j:dist_1(p_j,C_W)>0}a_j^+, while the contract defines sigma_g=sum_{j:dist_1(p_j,C_W)>tau/4}a_j^+. Since H_j=dist_1(p_j,C_W), the sets {H_j>0} and {H_j>tau/4} are respectively G union B and G; hence sum_{j in B}a_j^+=sigma-sigma_g. Nonnegativity of distance gives the disjoint partition {j:notin G}=B union Z, and the definitions of B and Z give H_j<=tau/4 on B and H_j=0 on Z.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.4.3.3.2

**Statement:** With H_j=dist_1(p_j,C), G={j:H_j>tau/4}, B={j:0<H_j<=tau/4}, and Z={j:H_j=0}, nonnegativity of distances gives the disjoint partition {j:notin G}=B union Z. By def-invisible-mass, sigma is the sum of a_j^+ over rows with H_j>0, and by the contract sigma_g is the sum of a_j^+ over rows with H_j>tau/4, so sigma-sigma_g=sum_{j in B}a_j^+. Also H_j=0 on Z and H_j<=tau/4 on B. Since a_j^+>=0, sum_{j notin G}a_j^+H_j=sum_{j in B}a_j^+H_j+sum_{j in Z}a_j^+H_j <= (tau/4)*sum_{j in B}a_j^+=(sigma-sigma_g)*tau/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.4

**Statement:** Boundary-inclusive halo bookkeeping for the second inequality: set C=C_W=conv{p_w:w in W(P)}, H_j=dist_1(p_j,C_W), a_j=P_{vj}, a_j^+=max(a_j,0), tau=sqrt(delta), G={j:H_j>tau/4}, N={j:0<H_j<=tau/4}, and Z={j:H_j=0}. Since H_j is a distance, H_j>=0 and hence {j:notin G}=N union Z disjointly, including the boundary H_j=tau/4 in N. By def-invisible-mass, sigma=sum_{H_j>0} a_j^+; by the contract definition of halo-robust invisible mass, sigma_g=sum_{H_j>tau/4} a_j^+=sum_{j in G}a_j^+. Therefore sigma-sigma_g=sum_{j in N}a_j^+. On Z the summand a_j^+ H_j is zero, and on N one has H_j<=tau/4, so nonnegativity of a_j^+ gives sum_{j notin G} a_j^+ H_j=sum_{j in N}a_j^+H_j+sum_{j in Z}a_j^+H_j <= (tau/4) sum_{j in N}a_j^+=(sigma-sigma_g)*tau/4. Thus the boundary rows are accounted for and the displayed final inequality in node 1.4 follows when this is combined with the lem-residual-upper bound already established for the same q and G.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Combining the two cases proves the contract: the sigma_g>=1 case is node 1.2, and in the sigma_g<1 case nodes 1.3 and 1.4 chain to H*(1-sigma_g) <= (sigma-sigma_g)*tau/4 + nu_v*(2+4*delta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Conditional combination step, available only after nodes 1.2, 1.3, and 1.4 are validated: if sigma_g>=1, node 1.2 gives exactly the desired inequality. If sigma_g<1, node 1.3 gives H*(1-sigma_g) <= (1-sigma_g)*dist_1(q,C), and node 1.4 gives (1-sigma_g)*dist_1(q,C) <= (sigma-sigma_g)*tau/4 + nu_v*(2+4*delta); transitivity gives H*(1-sigma_g) <= (sigma-sigma_g)*tau/4 + nu_v*(2+4*delta). Since exactly one of sigma_g>=1 and sigma_g<1 holds, the two validated cases prove the contract.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

