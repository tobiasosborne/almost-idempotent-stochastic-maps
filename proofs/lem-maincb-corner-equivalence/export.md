# Proof Export

## Node 1

**Statement:** There is a universal e_sim > 0 such that, for every finite family of one-dimensional t-projections P_1,...,P_m in an extended t-C*-algebra with t <= e_sim, the relation j ~ k iff dim S_{P_j,P_k} = 1 is an equivalence relation.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** The external lem-extcb-one-dimensional-product supplies universal C_PQR<infinity and e_PQR>0, and lem-extcb-one-dimensional-corner-dimension supplies a universal threshold e_dim>0 for its sufficiently-small hypothesis. After enlarging C_PQR to at least 1, define e_sim=min{e_PQR/2,e_dim/2,1/(4*C_PQR)}. Then e_sim>0, and t<=e_sim implies e:=t+t=2t<=e_PQR, e<=e_dim, and C_PQR*e<=1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix any t>=0 and any finite family of one-dimensional t-projections P_1,...,P_m in an extended t-C*-algebra, and suppose e:=2t satisfies e<=e_PQR, e<=e_dim, and C_PQR*e<=1/2, where the constants are as in the two named externals. Then the relation j~k iff dim S_{P_j,P_k}=1 is reflexive, symmetric, and transitive, hence is an equivalence relation.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** The relation is reflexive: for every j, one-dimensionality of the t-projection P_j means dim S_{P_j}=1, and def-compressed-corner identifies S_{P_j} as the abbreviation S_{P_j,P_j}; hence j~j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** The relation is symmetric: def-compressed-corner gives C_{P,Q}(Z)^dagger=C_{Q,P}(Z^dagger), so the conjugate-linear involution dagger restricts to a bijection S_{P,Q}->S_{Q,P}; consequently these complex vector spaces have equal dimension, and dim S_{P_j,P_k}=1 implies dim S_{P_k,P_j}=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** The relation is transitive: if j~k and k~l, then dim S_{P_j,P_l}=1, hence j~l.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** Assume j~k and k~l. Choose nonzero X in S_{P_j,P_k} and nonzero Y in S_{P_k,P_l}. By def-compressed-corner their compressed product Z:=X dot Y belongs to S_{P_j,P_l}. Applying lem-extcb-one-dimensional-product to (P_j,P_k,P_l), since P_k is one-dimensional and e=2t<=e_PQR, gives ||Z|| >= (1-C_PQR*e)||X||||Y|| >= (1/2)||X||||Y||>0; thus S_{P_j,P_l} is nonzero.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.2

**Statement:** Because S_{P_j,P_l} contains the nonzero product from child 1.2.3.1, its dimension is at least 1. Since P_j and P_l are one-dimensional t-projections and e=2t<=e_dim, lem-extcb-one-dimensional-corner-dimension gives dim S_{P_j,P_l}<=1. Therefore dim S_{P_j,P_l}=1, which is j~l.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

