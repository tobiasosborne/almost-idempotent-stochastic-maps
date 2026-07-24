# Proof Export

## Node 1

**Statement:** Uniform rectangular compressed-product estimate: there are universal C_co < infinity and e_co > 0 such that, for e=delta+epsilon <= e_co, every compatible amplified rectangular pair satisfies ||A dot B-AB|| <= C_co*e*||A||||B||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** The cited compressed-corner estimate supplies universal constants C_corner < infinity and e_corner > 0 such that in every epsilon-C*-algebra, for delta-projections U,V,W and e=delta+epsilon <= e_corner, all X in S_{U,V} and Y in S_{V,W} satisfy ||Co_{U,W}(XY)-XY|| <= C_corner*e*||X||||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By def-compressed-corner, for any triple U,V,W of delta-projections in an epsilon-C*-algebra, X dot Y=Co_{U,W}(XY) on S_{U,V} x S_{V,W}, and ||X dot Y-XY|| <= O(delta+epsilon)||X||||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Unpacking the universal big-O assertion in def-compressed-corner gives constants C_corner < infinity and e_corner > 0, independent of the algebra, projections, and elements, for which the bound in node 1.1.1 is at most C_corner*(delta+epsilon)*||X||||Y|| whenever delta+epsilon <= e_corner.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For every compatible amplified rectangular pair A,B at level n, the amplified ambient space and corners meet the hypotheses of the estimate in node 1.1, and the amplified compressed product is A dot B=Co_{P_n,R_n}(AB).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** By def-extended-epsilon-cstar-algebra, if the ambient space is an extended epsilon-C*-algebra then M_n tensor A is an epsilon-C*-algebra for every n >= 1; moreover P_n=I_n tensor P is a delta-projection whenever P is, since P_n^dagger=P_n, P_n^2-P_n=I_n tensor (P^2-P), and the block-diagonal operator norm satisfies ||I_n tensor Z||=||Z||, and likewise for Q_n and R_n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For e <= e_cmp, applying lem-compcb-amplified-compression to the pairs (P,Q), (Q,R), and (P,R) gives M_n tensor S_{P,Q}=S_{P_n,Q_n}, M_n tensor S_{Q,R}=S_{Q_n,R_n}, M_n tensor S_{P,R}=S_{P_n,R_n}, together with 1_{M_n} tensor Co_{P,Q}=Co_{P_n,Q_n} and the analogous two identities; lem-compcb-amplified-compression-identities additionally gives the idempotence and dagger identities for these amplified compression maps.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Thus a compatible amplified rectangular pair has A in S_{P_n,Q_n} and B in S_{Q_n,R_n}; by def-compressed-corner its amplified compressed product is the ordinary compressed product in M_n tensor A, namely A dot B=Co_{P_n,R_n}(AB), which belongs to S_{P_n,R_n}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Taking C_co=C_corner and e_co=min(e_corner,e_cmp), where e_cmp is the universal threshold supplied by the validated amplification dependencies, and applying node 1.1 to the amplified data from node 1.2 proves ||A dot B-AB|| <= C_co*e*||A||||B|| uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** The choices C_co=C_corner and e_co=min(e_corner,e_cmp) are universal, finite and positive; if e <= e_co then both the compressed-corner estimate of node 1.1 and the amplification identifications of node 1.2 apply.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Applying node 1.1 inside the epsilon-C*-algebra M_n tensor A to U=P_n, V=Q_n, W=R_n, X=A, Y=B, and then using A dot B=Co_{P_n,R_n}(AB) from node 1.2 yields ||A dot B-AB|| <= C_corner*e*||A||||B||=C_co*e*||A||||B||, with constants independent of n and all compatible data.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** In node 1, the phrase compatible amplified rectangular pair is an explicit abbreviation for the following data: an extended epsilon-C*-algebra calA; an integer n >= 1; delta-projections P,Q,R in calA; P_n=I_n tensor P, Q_n=I_n tensor Q, and R_n=I_n tensor R; elements A in S_{P_n,Q_n} and B in S_{Q_n,R_n}; and the compressed product A dot B defined, as in def-compressed-corner applied inside M_n tensor calA, by A dot B=Co_{P_n,R_n}(AB). Thus the quantifier every compatible amplified rectangular pair in node 1 ranges over exactly these data and no others.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

