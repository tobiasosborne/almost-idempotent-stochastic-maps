# Proof Export

## Node 1

**Statement:** Close-compression range invariance: there is a universal e_close > 0 such that, in an EXT-CB datum with e <= e_close, the compression ranges S_{v(I_r),Q} and S_{P,Q} have the same dimension.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Uniform unit and projection control: writing R=v(I_r), there are universal C_R<infinity, M_R<infinity and e_R>0 such that every EXT-CB datum with e<=e_R has ||P||,||Q||,||R||<=M_R, ||R-P||<=C_R e, and R is a (C_R e)-projection in the ambient algebra A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Nonvanishing and norm bounds: bijectivity of v:M_r->S_P makes S_P nonzero, so the compressed-corner definition's vanishing alternative makes P nonvanishing; dim S_Q=1 likewise makes Q nonvanishing. Hence the nonvanishing delta-projection alternative gives universal bounds ||P||,||Q||<=M_1 for all sufficiently small e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Unit comparison: by lem-compcb-corner-algebra, S_P is an extended C_ca e-C*-algebra with compressed unit u_P=Co_P(P). The unit axiom for the extended delta-isomorphism v gives ||R-u_P||<=delta. The compression estimate in def-compressed-corner gives ||u_P-P(PP)||=O(e)||P||, while ||P(PP)-P||<=((1+epsilon)||P||+1)delta; therefore ||R-P||<=C_1 e with a universal C_1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Ambient projection control: the star-preserving delta-homomorphism property gives R^dagger=R and ||R dot R-R||<=delta in S_P. Since def-compressed-corner gives ||R dot R-RR||<=O(e)||R||^2, the preceding norm and closeness bounds imply ||R^2-R||<=C_2 e and ||R||<=M_2, with universal C_2,M_2; enlarging constants proves node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Uniform compression control: there are universal C_0<infinity, M_0<infinity and e_0>0 such that, for every EXT-CB datum with e<=e_0 and R=v(I_r), the maps E=Co_{R,Q} and F=Co_{P,Q} are bounded idempotents on A satisfying ||E||<=M_0 and ||E-F||<=C_0 e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Idempotence with a common adjusted defect: after enlarging C_R>=1, node 1.1 makes R,P,Q all (C_R e)-projections. Put delta'=C_R e. Since delta'+epsilon<=(C_R+1)e, choosing e universally small permits application of lem-compcb-amplified-compression-identities at n=1 to (R,Q) and (P,Q), and yields E^2=E and F^2=F.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Operator estimates: def-compressed-corner gives ||E-L_R R_Q||=O(delta'+epsilon) and ||F-L_P R_Q||=O(delta'+epsilon). For ||X||=1, the product norm axiom and node 1.1 give ||(L_R R_Q-L_P R_Q)(X)||=||(R-P)(XQ)||<=(1+epsilon)^2||R-P||||Q||<=C_3 e. The triangle inequality therefore gives ||E-F||<=C_0 e; also ||E||<=||L_R R_Q||+O(e)<=(1+epsilon)^2||R||||Q||+O(e)<=M_0, for universal C_0,M_0 and a universal smallness threshold.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Explicit prerequisite assembly (without invoking pending node 1.1): validated node 1.1.1 supplies universal M_1 and a threshold such that ||P||,||Q||<=M_1; validated node 1.1.2 supplies universal C_1 and a threshold such that ||R-P||<=C_1 e. Hence, after also requiring e<=1, ||R||<=||P||+||R-P||<=M_1+C_1=:M_R. Validated node 1.1.3 supplies universal C_2 and a threshold such that R is a C_2 e-projection. Since P and Q are delta-projections and delta<=e, setting C_R=max{1,C_2} and delta_prime=C_R e makes R,P,Q all delta_prime-projections while retaining ||R-P||<=C_1 e and the displayed uniform norm bounds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** Quantitative operator estimate from the assembled bounds: let k_cmp and e_cmp0 be universal constants witnessing the O(delta_prime+epsilon) operator-norm compression estimate in def-compressed-corner. For e small enough that delta_prime+epsilon<=(C_R+1)e<=e_cmp0 and epsilon<=1, ||E-L_R R_Q|| and ||F-L_P R_Q|| are at most k_cmp(C_R+1)e. Moreover, for every X, the product norm axiom twice gives ||(L_R R_Q-L_P R_Q)(X)||=||(R-P)(XQ)||<=(1+epsilon)^2||R-P||||Q||||X||<=4 C_1 M_1 e||X||. Thus ||E-F||<=[2k_cmp(C_R+1)+4C_1M_1]e=:C_0e. Also ||L_R R_Q||<=(1+epsilon)^2||R||||Q||<=4M_RM_1, whence ||E||<=4M_RM_1+k_cmp(C_R+1)e<=4M_RM_1+k_cmp(C_R+1)=:M_0 for e<=1. All constants and the minimum of the finitely many thresholds are universal.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Close-idempotent range lemma: if E and F are bounded idempotents on a Banach space, ||E||<=M, and ||E-F||(2M+1)<1, then W=FE+(I-F)(I-E) is invertible, W maps Ran(E) bijectively onto Ran(F), and hence dim Ran(E)=dim Ran(F).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Algebraic identities: using E^2=E and F^2=F, W=FE+(I-F)(I-E) satisfies W-I=(F-E)(2E-I) and WE=FW=FE. Hence ||W-I||<=||F-E||(2||E||+1)<1 under the stated hypothesis.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Neumann inversion and range transport: the inequality ||W-I||<1 makes W invertible by the convergent Neumann series. From WE=FW, W sends Ran(E) into Ran(F), and E W^{-1}=W^{-1}F. Thus for y in Ran(F), x=W^{-1}y obeys Ex=x and Wx=y; consequently W restricts to a linear bijection Ran(E)->Ran(F), proving equality of their dimensions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Threshold selection and conclusion: taking e_close>0 below e_R, e_0, and 1/[C_0(2M_0+1)], the preceding controls and close-idempotent range lemma give dim S_{v(I_r),Q}=dim S_{P,Q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Explicit validated-premise threshold step: require nodes 1.1 and 1.2 to be validated. Enlarge their universal constants harmlessly so that C_0>=1 and M_0>=1, and set e_close=min{e_R,e_0,1/[2 C_0(2M_0+1)]}>0. For an EXT-CB datum with e<=e_close, node 1.2 gives bounded idempotents E=Co_{R,Q}, F=Co_{P,Q}, with R=v(I_r), ||E||<=M_0 and ||E-F||<=C_0 e. Therefore ||E-F||(2||E||+1)<=C_0 e_close(2M_0+1)<=1/2<1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Range transport and identification: require node 1.3 and the preceding threshold step to be validated. Applying node 1.3 to E,F with M=M_0 gives a linear bijection Ran(E)->Ran(F), hence dim Ran(E)=dim Ran(F). By def-compressed-corner, Ran(Co_{R,Q})=S_{R,Q} and Ran(Co_{P,Q})=S_{P,Q}; since R=v(I_r), this is dim S_{v(I_r),Q}=dim S_{P,Q}, exactly the conclusion of node 1.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

