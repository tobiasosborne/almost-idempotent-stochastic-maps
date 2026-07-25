# Proof Export

## Node 1

**Statement:** Amplified Ha variational identity: there is a universal e_var > 0 such that every H-CB datum with e <= e_var, every n >= 1, Z in M_n tensor S_{P,R}, X in M_{n,1} tensor S_{R,Q}, and Y in M_{n,1} tensor S_{P,Q} satisfy 2*<Y,(Ha^Q_{P,R})_n(Z)X-Z dot X>*Co_Q(Q)=(Y^dagger dot Z) dot X-Y^dagger dot (Z dot X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** By lem-compcb-amplified-compression-identities there is a universal e_cmp>0 for the amplified compression identities, and by lem-hcb-column-hilbert-squared there is a universal e_col>0 for the amplified column-Hilbert estimate. Set e_var=min(e_cmp,e_col)>0, and fix an arbitrary H-CB datum with e<=e_var together with n>=1 and Z,X,Y as quantified in node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Write Z=(Z_ij)_{1<=i,j<=n}, X=(X_j)_{1<=j<=n}, and Y=(Y_i)_{1<=i<=n}. By the definitions of matrix amplification, matrix dot-product, and the amplified column sesquilinear form in the H-CB datum, ((Ha^Q_{P,R})_n(Z)X)_i=sum_j Ha^Q_{P,R}(Z_ij)(X_j), (Z dot X)_i=sum_j Z_ij dot X_j, (Y^dagger dot Z)_j=sum_i Y_i^dagger dot Z_ij, and <Y,W>_n=sum_i <Y_i,W_i> for every amplified column W.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every i,j, the defining Ha identity def-ha-map applied to Z_ij in S_{P,R}, X_j in S_{R,Q}, and Y_i in S_{P,Q} gives 2*<Y_i,Ha^Q_{P,R}(Z_ij)(X_j)>*Co_Q(Q)=(Y_i^dagger dot Z_ij) dot X_j+Y_i^dagger dot (Z_ij dot X_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Summing the identities of the preceding node over i,j and using the entrywise amplification and sesquilinearity yields 2*<Y,(Ha^Q_{P,R})_n(Z)X>_n*Co_Q(Q)=sum_{i,j}((Y_i^dagger dot Z_ij) dot X_j+Y_i^dagger dot (Z_ij dot X_j)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The registered amplified column-Hilbert defining display Y^dagger dot W=<Y,W>_n*Co_Q(Q), applied to W=Z dot X and expanded entrywise, gives <Y,Z dot X>_n*Co_Q(Q)=Y^dagger dot (Z dot X)=sum_{i,j}Y_i^dagger dot (Z_ij dot X_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Associating only as explicitly displayed and using ordinary matrix multiplication, (Y^dagger dot Z) dot X=sum_{i,j}(Y_i^dagger dot Z_ij) dot X_j, whereas Y^dagger dot (Z dot X)=sum_{i,j}Y_i^dagger dot (Z_ij dot X_j); hence their difference is sum_{i,j}((Y_i^dagger dot Z_ij) dot X_j-Y_i^dagger dot (Z_ij dot X_j)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Subtract twice the identity in node 1.5 from node 1.4, use sesquilinearity in the second variable, and identify the resulting finite sum by node 1.6. This gives 2*<Y,(Ha^Q_{P,R})_n(Z)X-Z dot X>_n*Co_Q(Q)=(Y^dagger dot Z) dot X-Y^dagger dot (Z dot X). Since the datum, n,Z,X,Y were arbitrary and e_var is universal and positive, node 1 follows.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

