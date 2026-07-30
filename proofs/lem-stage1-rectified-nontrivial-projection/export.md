# Proof Export

## Node 1

**Statement:** There are universal C_proj<infinity and e_proj>0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0<=epsilon_X<=e_proj and 1<dim_C calX<infinity contains a nontrivial C_proj*epsilon_X-projection P_0 for the original product and original unit I_X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Choose the universal witnesses C_rect>=1 and e_rect>0 from lem-stage1-rectified-cstar-control and C_bridge<infinity and e_bridge^r>0 from lem-stage1-fixed-unitary-projection-bridge, and put D=max(1,C_bridge). Unpacking the two dimension-independent O-bounds in the def-delta-projection meaning of the bridge conclusion that P is nontrivial, choose one universal K>=1 such that both rectified nonvanishing estimates are bounded by K(D epsilon_r+epsilon_r). Put B=K(D+1)C_rect, A=C_rect(D+4), C_proj=A+6, and e_proj=min(e_rect,e_bridge^r/C_rect,1,1/B). Then C_proj<infinity and e_proj>0 are universal.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix a finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0<=epsilon_X<=e_proj and 1<dim_C calX<infinity. By def-extended-epsilon-cstar-algebra at matrix level n=1 it is an epsilon_X-C*-algebra. Apply lem-stage1-rectified-cstar-control to obtain on the same involutive normed space an exact-unit epsilon_r-C*-algebra (calX,J,bold-dot,dagger), where epsilon_r=C_rect epsilon_X, ||J-I_X||<=C_rect epsilon_X, and ||x bold-dot y-xy||<=C_rect epsilon_X||x||||y||. Since epsilon_r<=e_bridge^r, lem-stage1-fixed-unitary-projection-bridge gives a nontrivial C_bridge epsilon_r-projection P for bold-dot and J. Because D=max(1,C_bridge), the same P is, after harmless enlargement of the tolerance and its universal nonvanishing O-bound, a nontrivial delta_r-projection with delta_r=D epsilon_r=D C_rect epsilon_X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For the P obtained above, rectified nontriviality and the choice of K give | ||P||-1 |<=K(delta_r+epsilon_r)=B epsilon_X and | ||J-P||-1 |<=B epsilon_X. Since epsilon_X<=1/B, ||P||<=2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The same element P is self-adjoint for the original structure, and its original-product defect obeys ||P P-P||<=||P P-(P bold-dot P)||+||P bold-dot P-P||<=C_rect epsilon_X||P||^2+C_bridge C_rect epsilon_X<=(4C_rect+D C_rect)epsilon_X=A epsilon_X<=C_proj epsilon_X. Hence P is a C_proj epsilon_X-projection for the original product.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Let R=I_X-P. The original unit is self-adjoint, so R is self-adjoint. The approximate-unit axioms in def-epsilon-cstar-algebra give ||I_X||<=1+epsilon_X<=2, ||I_X^2-I_X||<=epsilon_X||I_X||<=2epsilon_X, and ||I_XP-P||,||PI_X-P||<=epsilon_X||P||<=2epsilon_X. Using R^2-R=(I_X^2-I_X)-(I_XP-P)-(PI_X-P)+(P^2-P) and the preceding original defect bound yields ||R^2-R||<=(A+6)epsilon_X=C_proj epsilon_X. Thus I_X-P is also a C_proj epsilon_X-projection for the original product.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** The original projection P is nonvanishing because | ||P||-1 |<=B epsilon_X=O(C_proj epsilon_X+epsilon_X). Its original-unit complement is nonvanishing because the reverse triangle inequality, rectified nontriviality, and unit closeness give | ||I_X-P||-1 |<=||I_X-J||+| ||J-P||-1 |<=(C_rect+B)epsilon_X=O(C_proj epsilon_X+epsilon_X). Together with the two C_proj epsilon_X-projection statements, def-delta-projection says that P_0:=P is nontrivial for the original product and original unit I_X. Since the algebra was arbitrary and C_proj,e_proj are universal, this proves the root contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

