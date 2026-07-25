# Proof Export

## Node 1

**Statement:** Off-diagonal Ha inverse propagation: there are universal C_rect < infinity and e_rect > 0 such that, for every H-CB datum with e <= e_rect, if Ha^Q_{P,R} is bijective at level one and Ha^Q_{R,R} has level-one lower modulus at least 1/4, then every amplification of Ha^Q_{P,R} is bijective with inverse norm at most 1+C_rect*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Constant ledger and arbitrary-data setup. Let C_prod,e_prod and C_diag,e_diag be universal witnesses from lem-hcb2-product-defect and lem-hcb3-diagonal-lower-modulus, and let e_adj be the threshold from lem-hcb2-amplified-adjointness. Unpack the universal O(e) constant in the registered compressed-product-display as C_cp<infinity with a universal validity threshold e_cp>0. Put B=1+C_cp, A=max{1,C_diag+B+C_prod}, C_rect=2*A, and e_rect=min{e_adj,e_prod,e_diag,e_cp,1/(2*A)}. Fix an H-CB datum with e<=e_rect satisfying the two hypotheses, an arbitrary n>=1, and write T_n=(Ha^Q_{P,R})_n and D_n=(Ha^Q_{R,R})_n. These constants are universal, C_rect<infinity, e_rect>0, and A*e<=1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Witness and arithmetic discharge. The named external contracts supply finite nonnegative universal estimate constants and positive universal thresholds. The ground-truth compressed-product-display assertion ||X dot Y-XY||<=O(delta+epsilon)||X||||Y|| means precisely that some finite nonnegative universal C_cp and positive universal e_cp make this bound hold whenever e=delta+epsilon<=e_cp; applying a smaller positive threshold if necessary is harmless. Thus B=1+C_cp and A=max{1,C_diag+B+C_prod} are finite with A>=1, C_rect=2*A is finite, and the minimum defining e_rect is positive. From e<=e_rect<=1/(2*A), one has A*e<=1/2. This verifies every constants claim in node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Rectangular square estimate. For every Z in M_n tensor S_{P,R}, the registered compression, extended-epsilon-C*-algebra, and matrix-norm definitions imply ||Z^dagger dot Z|| >= (1-B*e)||Z||^2, with B from node 1.1 and uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Amplified compression/type calculation. Put P_n=I_n tensor P and R_n=I_n tensor R. In the registered theta compression construction, left and right multiplication by P_n,R_n act entrywise, so the operator to which theta is applied is id_{M_n} tensor the corresponding level-one operator. The registered power-series formula for theta therefore gives Co_{P_n,R_n}=id_{M_n} tensor Co_{P,R}, and similarly for the reversed and R,R corners. The operator-space matrix-norm axioms preserve the delta-defects under I_n tensor -, so these are the corresponding amplified compressed corners in the extended algebra M_n tensor A. Consequently Z belongs to S_{P_n,R_n}, Z^dagger belongs to S_{R_n,P_n}, and the amplified product Z^dagger dot Z is Co_{R_n,R_n}(Z^dagger Z), exactly the product to which compressed-product-display applies inside M_n tensor A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Norm calculation. Apply compressed-product-display inside M_n tensor A to the compatible pair Z^dagger,Z from node 1.2.1: ||Z^dagger dot Z-Z^dagger Z||<=C_cp*e*||Z^dagger||||Z||=C_cp*e*||Z||^2, where dagger isometry is part of epsilon-banach-cstar-norm-axioms. Since A is extended epsilon-C*, the same registered axioms at level n give ||Z^dagger Z||>=(1-epsilon)||Z||^2. Reverse triangle inequality and 0<=epsilon<=e yield ||Z^dagger dot Z||>=(1-epsilon-C_cp*e)||Z||^2>=(1-(1+C_cp)*e)||Z||^2=(1-B*e)||Z||^2, proving node 1.2 uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Ha lower-modulus estimate. For every Z in M_n tensor S_{P,R}, exact amplified adjointness, amplified product defect, the assumed diagonal anchor through lem-hcb3-diagonal-lower-modulus, and node 1.2 imply ||T_n(Z)||^2 >= (1-A*e)||Z||^2 and hence ||T_n(Z)|| >= (1-A*e)||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Adjoint/product comparison. Instantiate lem-hcb2-product-defect with its corner indices (R,P,R), first factor Z^dagger in M_n tensor S_{R,P}, and second factor Z in M_n tensor S_{P,R}. Using dagger isometry gives ||D_n(Z^dagger dot Z)-(Ha^Q_{R,P})_n(Z^dagger)T_n(Z)||<=C_prod*e*||Z||^2. By lem-hcb2-amplified-adjointness, (Ha^Q_{R,P})_n(Z^dagger)=T_n(Z)^dagger. The C*-identity for bounded operators between the amplified Hilbert column spaces gives ||T_n(Z)^dagger T_n(Z)||=||T_n(Z)||^2; hence reverse triangle inequality yields ||T_n(Z)||^2>=||D_n(Z^dagger dot Z)||-C_prod*e*||Z||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Diagonal anchor and arithmetic. The root hypothesis and lem-hcb3-diagonal-lower-modulus applied with P=R and X=Z^dagger dot Z give ||D_n(X)||>=(1-C_diag*e)||X||. Node 1.1 gives C_diag*e<=A*e<=1/2, so the coefficient is nonnegative; node 1.2 therefore implies ||D_n(X)||>=(1-C_diag*e)(1-B*e)||Z||^2. Substitute this in node 1.3.1 and expand: ||T_n(Z)||^2 >= [(1-C_diag*e)(1-B*e)-C_prod*e]||Z||^2 >= [1-(C_diag+B+C_prod)*e]||Z||^2 >= (1-A*e)||Z||^2. Since 0<=A*e<=1/2 and sqrt(1-x)>=1-x for 0<=x<=1, taking square roots yields ||T_n(Z)||>=(1-A*e)||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Set X=Z^dagger dot Z. By node 1.1, e<=e_diag, and the root lower-modulus hypothesis for Ha^Q_{R,R}; hence lem-hcb3-diagonal-lower-modulus with P=R gives ||D_n(X)||>=(1-C_diag*e)||X||. Also e>=0 and A>=C_diag, while A*e<=1/2, so 1-C_diag*e>=1-A*e>=1/2. The nonnegative coefficient permits multiplication of node 1.2, yielding ||D_n(X)||>=(1-C_diag*e)(1-B*e)||Z||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.2

**Statement:** Combine child 1.3.2.1 with the validated adjoint/product comparison in node 1.3.1 to obtain ||T_n(Z)||^2 >= [(1-C_diag*e)(1-B*e)-C_prod*e]||Z||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.3

**Statement:** Expanding the coefficient gives 1-(C_diag+B+C_prod)e+C_diag*B*e^2. The constants and e are nonnegative, so this is at least 1-(C_diag+B+C_prod)e, which is at least 1-A*e by A>=C_diag+B+C_prod. Therefore ||T_n(Z)||^2>=(1-A*e)||Z||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.4

**Statement:** Since 0<=A*e<=1/2, the factor 1-A*e is nonnegative. Taking square roots and using sqrt(1-x)>=1-x for 0<=x<=1 gives ||T_n(Z)||>=sqrt(1-A*e)||Z||>=(1-A*e)||Z||, which is the conclusion of node 1.3.2.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Bijectivity and conclusion. Level-one bijectivity algebraically amplifies, so T_n is bijective; node 1.3 then gives ||T_n^(-1)|| <= 1/(1-A*e) <= 1+2*A*e = 1+C_rect*e. Since n was arbitrary and the constants are universal, this proves node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Algebraic amplification of bijectivity. By def-ha-map, T_1=Ha^Q_{P,R} is linear, and by hypothesis it has a two-sided linear inverse S. By the meaning of amplification, T_n=id_{M_n} tensor T_1 acts entrywise. Therefore id_{M_n} tensor S is a two-sided inverse: on an elementary tensor a tensor y, (id tensor T_1)(id tensor S)(a tensor y)=a tensor y and the reverse composition is identical, and linearity extends the identities to the algebraic matrix tensor spaces. Thus every T_n is bijective, independently of any norm estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Inverse norm and quantified conclusion. For arbitrary Y in the codomain of T_n, set Z=T_n^(-1)Y, whose existence is node 1.4.1. Node 1.3 gives ||Y||=||T_n(Z)||>=(1-A*e)||Z||, hence ||T_n^(-1)Y||<=||Y||/(1-A*e). Taking the supremum gives ||T_n^(-1)||<=1/(1-A*e). For x=A*e in [0,1/2], 1/(1-x)<=1+2*x, so this is at most 1+2*A*e=1+C_rect*e. Node 1.1 fixed arbitrary admissible data and arbitrary n and supplied universal C_rect,e_rect; therefore the asserted estimate and bijectivity hold for every amplification and establish the root.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

