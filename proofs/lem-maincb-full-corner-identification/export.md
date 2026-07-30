# Proof Export

## Node 1

**Statement:** There is a universal e_full > 0 such that, if R is a t-projection in an extended t-C*-algebra and ||R-I|| <= t <= e_full, then Co_R = I and S_R = A, at every amplification.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix universal constants C_co,e_co>0 witnessing the O(delta+epsilon) compression estimate in def-compressed-corner, and let e_cmp>0 be no larger than the thresholds in both lem-compcb-amplified-compression and lem-compcb-amplified-compression-identities. Put K=21+2*C_co and e_full=min{1,e_co/2,e_cmp/2,1/(2*K)}. Under the root hypotheses with t<=e_full, the level-one operator satisfies ||Co_R-I_A||<=K*t<=1/2<1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By def-compressed-corner, the statement ||L_R R_R-Co_R||=O(delta+epsilon) means that there are universal C_co,e_co>0 such that whenever delta+epsilon<=e_co, ||Co_R-L_R R_R||<=C_co*(delta+epsilon); here delta=epsilon=t, so ||Co_R-L_R R_R||<=2*C_co*t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** If 0<=t<=1, A is a t-C*-algebra and ||R-I||<=t, then ||L_R R_R-I_A||<=21*t. Indeed, for ||X||=1, def-epsilon-cstar-algebra gives ||R||<=||I||+t<=1+2*t and ||XR||<=(1+t)||R||<=6. Bilinearity gives R(XR)-X=(R-I)(XR)+(I(XR)-XR)+(XR-X) and XR-X=X(R-I)+(XI-X). Therefore ||R(XR)-X||<=((1+t)*t+t)||XR||+(1+t)*t+t<=18*t+3*t=21*t. Since L_R R_R(X)=R(XR) by def-compressed-corner, taking the supremum over ||X||=1 proves the operator-norm bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Under the same choice t<=e_full, lem-compcb-amplified-compression-identities applied with delta=epsilon=t, P=Q=R and n=1 gives Co_R^2=Co_R as an operator on A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Idempotent rigidity: if E is a bounded linear operator on a normed space with E^2=E and ||E-I||<1, then E=I; consequently, for the compression map, Co_R=I_A and S_R=Img(Co_R)=A once the preceding closeness and idempotence statements hold.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Let E be a bounded linear operator on a normed space with E^2=E and q=||E-I||<1. For arbitrary X put Y=(I-E)X. Then EY=EX-E^2X=0, so (I-E)Y=Y. Hence ||Y||=||(I-E)Y||<=q||Y||. Since q<1, this forces ||Y||=0 and Y=0. Thus (I-E)X=0 for every X and E=I. In particular, conditionally, if Co_R^2=Co_R and ||Co_R-I_A||<1, then applying this result to E=Co_R gives Co_R=I_A; def-compressed-corner then gives S_R=Img(Co_R)=Img(I_A)=A. This is a conditional implication only and does not assert or use the sibling conclusions inside this node.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Abstract rigidity. Let E be a bounded linear operator on a normed space with E^2=E and q=||E-I||<1. For arbitrary X, set Y=(I-E)X. Then EY=EX-E^2X=0, so (I-E)Y=Y. Hence ||Y||=||(I-E)Y||<=||I-E||·||Y||=q||Y||. Since (1-q)||Y||<=0 while 1-q>0 and ||Y||>=0, one has ||Y||=0 and therefore Y=0. Thus (I-E)X=0 for every X, so E=I.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.3.1.2

**Statement:** Apply the abstract rigidity result to E=Co_R. Node 1.2 supplies Co_R^2=Co_R, and node 1.1 supplies ||Co_R-I_A||<1; therefore Co_R=I_A. By def-compressed-corner, S_R=Img(Co_R), while Img(I_A)=A, hence S_R=A.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

### Node 1.4

**Statement:** For every n>=1, set R_n=I_n tensor R. By lem-compcb-amplified-compression with delta=epsilon=t and P=Q=R, Co_{R_n}=1_{M_n} tensor Co_R and S_{R_n}=M_n tensor S_R. Hence the level-one conclusions Co_R=I_A and S_R=A imply Co_{R_n}=I_{M_n tensor A} and S_{R_n}=M_n tensor A for every n, which is exactly the asserted conclusion at every amplification.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

