# Proof Export

## Node 1

**Statement:** Row-column compressed-product estimate: there are universal C_rc < infinity and e_rc > 0 such that, whenever e = delta+epsilon <= e_rc, P,Q are delta-projections in an extended epsilon-C*-algebra A, n >= 1, and X,Y are in M_{n,1} tensor S_{P,Q}, one has ||Co_Q(Y^dagger X) - Y^dagger X|| <= C_rc*e*||Y||*||X||, where Y^dagger X is the ambient product of the 1-by-n row Y^dagger with the n-by-1 column X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let C_co,e_co be the universal constants from lem-compcb-rectangular-product and let e_cmp be the universal threshold from lem-compcb-amplified-compression. Set C_rc=C_co and e_rc=min(e_co,e_cmp), and fix arbitrary data e=delta+epsilon<=e_rc, P,Q,A,n,X,Y satisfying node 1. It remains to prove the displayed estimate for these fixed data.

**Type:** local_assume

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For the decomposition C^(n+1)=C^n direct-sum C, let C_X be the (n+1)-by-(n+1) matrix whose upper-right n-by-1 block is X and whose other blocks are zero, and let R_Y be the matrix whose lower-left 1-by-n block is Y^dagger and whose other blocks are zero. Then C_X lies in S_{I_{n+1} tensor P,I_{n+1} tensor Q}, R_Y lies in S_{I_{n+1} tensor Q,I_{n+1} tensor P}, and ||C_X||=||X||, ||R_Y||=||Y||; hence (R_Y,C_X) is a compatible square amplified rectangular pair.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Write X=(X_i) and Y=(Y_i). Since X_i,Y_i lie in S_{P,Q}=Img(Co_{P,Q}), def-compressed-corner gives Co_{P,Q}(Y_i)^dagger=Co_{Q,P}(Y_i^dagger); hence Y_i^dagger lies in S_{Q,P}. Thus X lies in M_{n,1} tensor S_{P,Q} and Y^dagger lies in M_{1,n} tensor S_{Q,P} with the indicated orientations.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Because e<=e_rc<=e_cmp, lem-compcb-amplified-compression at level n+1 identifies M_{n+1} tensor S_{P,Q}=S_{I_{n+1} tensor P,I_{n+1} tensor Q} and M_{n+1} tensor S_{Q,P}=S_{I_{n+1} tensor Q,I_{n+1} tensor P}. Zero-padding therefore puts C_X and R_Y in precisely those compatible corners. Moreover, the operator-space matrix norm axiom makes canonical zero-padding an isometry (insertion and extraction by scalar coordinate isometries are contractive), and self-adjointness makes involution isometric; hence ||C_X||=||X|| and ||R_Y||=||Y^dagger||=||Y||. Together with node 1.2.1 this proves node 1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** The canonical maps from an n-by-1 or 1-by-n matrix corner into M_{n+1} obtained by adjoining zero rows and columns are isometries: the operator-space matrix norm axiom gives contractivity of insertion by scalar coordinate isometries and of extraction by their adjoints, yielding equality. Since A is a self-adjoint operator space, involution is isometric. Consequently ||C_X||=||X|| and ||R_Y||=||Y^dagger||=||Y||.

**Type:** qed

**Inference:** assumption

**Status:** archived

**Taint:** clean

### Node 1.3

**Statement:** The ambient product R_Y C_X is zero except for its lower-right entry Y^dagger X, while the compressed product R_Y dot C_X is zero except for its lower-right entry Co_Q(Y^dagger X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Ordinary block-matrix multiplication for the n-plus-1 decomposition gives R_Y C_X=diag(0_{n by n},Y^dagger X): every other block contains a zero block, and the lower-right block is the 1-by-n row Y^dagger times the n-by-1 column X in the ambient multiplication of A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** By def-compressed-corner and the compatible memberships from node 1.2, R_Y dot C_X=Co_{I_{n+1} tensor Q,I_{n+1} tensor Q}(R_Y C_X)=Co_{I_{n+1} tensor Q}(R_Y C_X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Let J_Q=I_{n+1} tensor Q and J_P=I_{n+1} tensor P. By node 1.2, R_Y lies in S_{J_Q,J_P} and C_X lies in S_{J_P,J_Q}. Therefore def-compressed-corner, applied to the triple (J_Q,J_P,J_Q), gives R_Y dot C_X=Co_{J_Q,J_Q}(R_Y C_X). Since the same definition prescribes the abbreviation Co_R when the two indices agree, Co_{J_Q,J_Q}=Co_{J_Q}; hence R_Y dot C_X=Co_{I_{n+1} tensor Q}(R_Y C_X). This uses node 1.2 for the corner-membership premises; node 1.3.1 is used separately to identify R_Y C_X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Because e<=e_rc<=e_cmp, lem-compcb-amplified-compression applied to (Q,Q) at level n+1 says Co_{I_{n+1} tensor Q}=1_{M_{n+1}} tensor Co_Q. Applying this entrywise map to diag(0,Y^dagger X) gives diag(0,Co_Q(Y^dagger X)), proving node 1.3.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.1

**Statement:** Validated node 1.1 sets e_rc=min(e_co,e_cmp) and fixes the present data with e<=e_rc. Hence e<=e_rc<=e_cmp, so the smallness hypothesis of lem-compcb-amplified-compression is satisfied for (Q,Q) at amplification level n+1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.2

**Statement:** Apply the registered af-validated contract lem-compcb-amplified-compression-CONTRACT to (Q,Q) at level n+1, using node 1.3.3.1, to obtain Co_{I_{n+1} tensor Q,I_{n+1} tensor Q}=1_{M_{n+1}} tensor Co_{Q,Q}=1_{M_{n+1}} tensor Co_Q. By node 1.3.1, R_Y C_X=diag(0_{n by n},Y^dagger X); applying the entrywise map 1_{M_{n+1}} tensor Co_Q therefore gives diag(0_{n by n},Co_Q(Y^dagger X)). Combining this with node 1.3.2, which identifies R_Y dot C_X with Co_{I_{n+1} tensor Q,I_{n+1} tensor Q}(R_Y C_X), proves node 1.3.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Applying lem-compcb-rectangular-product to (R_Y,C_X), then using the product and norm identities above, gives ||Co_Q(Y^dagger X)-Y^dagger X|| <= C_rc*e*||Y||*||X||. Since the fixed data were arbitrary and C_rc,e_rc are universal with e_rc>0, node 1 follows.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Since e<=e_rc<=e_co and node 1.2 supplies the compatible amplified square pair (R_Y,C_X), lem-compcb-rectangular-product gives ||R_Y dot C_X-R_Y C_X|| <= C_co*e*||R_Y||*||C_X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** Validated node 1.2 gives R_Y in S_{I_{n+1} tensor Q,I_{n+1} tensor P} and C_X in S_{I_{n+1} tensor P,I_{n+1} tensor Q}. Thus, inside the single square amplification M_{n+1} tensor A, the right projection I_{n+1} tensor P of the first factor equals the left projection of the second factor. Hence (R_Y,C_X) is a compatible amplified rectangular pair in the precise sense required by lem-compcb-rectangular-product-CONTRACT.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.2

**Statement:** By node 1.1, e<=e_rc<=e_co. Instantiate the registered af-validated external lem-compcb-rectangular-product-CONTRACT at amplification size m=n+1 with A_factor=R_Y, B_factor=C_X and corner projections P_m=I_{n+1} tensor Q, Q_m=I_{n+1} tensor P, R_m=I_{n+1} tensor Q. The compatibility premise is node 1.4.1.1; therefore the external contract yields ||R_Y dot C_X-R_Y C_X|| <= C_co*e*||R_Y||*||C_X||, exactly node 1.4.1.

**Type:** qed

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

###### Node 1.4.1.2.1

**Statement:** Node 1.1 defines e_rc=min(e_co,e_cmp), fixes arbitrary data satisfying e=delta+epsilon<=e_rc, and sets C_rc=C_co; hence e<=e_co. Node 1.4.1.1 gives, in the single square amplification M_{n+1} tensor A, R_Y in S_{I_{n+1} tensor Q,I_{n+1} tensor P} and C_X in S_{I_{n+1} tensor P,I_{n+1} tensor Q}, so the pair is compatible. Applying the registered af-validated lem-compcb-rectangular-product-CONTRACT with m=n+1, A_factor=R_Y, B_factor=C_X, P_m=I_{n+1} tensor Q, Q_m=I_{n+1} tensor P, and R_m=I_{n+1} tensor Q therefore yields ||R_Y dot C_X-R_Y C_X||<=C_co*e*||R_Y||*||C_X||. This is the claim of node 1.4.1 (and C_co=C_rc by node 1.1).

**Type:** qed

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** By node 1.3 the difference on the left is the zero-padded lower-right corner Co_Q(Y^dagger X)-Y^dagger X, whose norm equals the norm of that entry by the corner-isometry argument in node 1.2; node 1.2 also gives ||R_Y||=||Y|| and ||C_X||=||X||. Substitution and C_rc=C_co yield the claimed estimate. Both upstream thresholds are positive universal constants, so e_rc=min(e_co,e_cmp)>0, while C_rc is universal and finite; universal generalization over the arbitrary data fixed in node 1.1 completes node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** Both upstream thresholds are positive universal constants, so e_rc=min(e_co,e_cmp)>0, and C_rc=C_co is universal and finite. Universal generalization over the arbitrary data fixed in node 1.1 completes node 1.

**Type:** qed

**Inference:** assumption

**Status:** archived

**Taint:** clean

