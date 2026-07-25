# Proof Export

## Node 1

**Statement:** Diagonal Ha inverse propagation: there are universal C_inv < infinity and e_inv > 0 such that, for every H-CB datum with e <= e_inv, if Ha^Q_{P,P} has level-one lower modulus at least 1/4 and is bijective at level one, then every amplification is bijective and ||((Ha^Q_{P,P})_n)^(-1)|| <= 1+C_inv*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let C_diag < infinity and e_diag > 0 be universal witnesses from lem-hcb3-diagonal-lower-modulus. Enlarging C_diag if necessary preserves that external conclusion, so take C_diag > 0 and define e_inv := min{e_diag,(2*C_diag)^(-1)} and C_inv := 2*C_diag. Then e_inv > 0 and C_inv < infinity are universal, and 0 <= C_diag*e <= 1/2 whenever 0 <= e <= e_inv.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix an arbitrary H-CB datum satisfying the hypotheses of node 1 and an arbitrary n >= 1, and write T := Ha^Q_{P,P}. Because T is bijective at level one, its matrix amplification T_n is bijective: by the meaning of amplification, T_n([Z_ij])=[T(Z_ij)]; hence for any target matrix [Y_ij], the matrix [T^(-1)(Y_ij)] is a preimage, while T_n([Z_ij])=0 implies T(Z_ij)=0 for every i,j and therefore Z_ij=0 for every i,j. Thus (T_n)^(-1) is the entrywise amplification of T^(-1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every H-CB datum and n fixed as in node 1, e <= e_inv <= e_diag and the assumed level-one lower modulus is at least 1/4. Therefore lem-hcb3-diagonal-lower-modulus gives ||T_n(Z)|| >= (1-C_diag*e)||Z|| for every Z in M_n tensor S_P.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** By nodes 1.2 and 1.3, for every target element Y and Z=(T_n)^(-1)Y one has ||Y||=||T_n(Z)|| >= (1-C_diag*e)||Z||. Node 1.1 gives x:=C_diag*e in [0,1/2], so 1/(1-x)=1+x/(1-x) <= 1+2x. Consequently ||(T_n)^(-1)Y|| <= (1-C_diag*e)^(-1)||Y|| <= (1+2*C_diag*e)||Y|| = (1+C_inv*e)||Y||. Since the datum and n were arbitrary, every amplification is bijective with the asserted inverse bound, proving node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

