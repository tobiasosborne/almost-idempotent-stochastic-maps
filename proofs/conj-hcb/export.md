# Proof Export

## Node 1

**Statement:** H-CB: there are universal C_H < infinity and e_H > 0 such that, whenever e=delta+epsilon <= e_H, Q is a level-one one-dimensional delta-projection in an extended epsilon-C*-algebra A, and P,R,S are delta-projections, the maps 1_{M_n} tensor Ha^Q_{P,R}, under the COL-HILB identification with operators on C^n tensor S_{R,Q} and C^n tensor S_{P,Q}, satisfy for every n the adjoint equality, product defect at most C_H*e*||Z||||W||, and the uniform unit, upper-norm, homomorphism, and canonical-identity closeness estimates required by lem_extension; moreover, if the level-one lower modulus of Ha^Q_{P,P} is at least 1/4, then every amplification has lower modulus at least 1-C_H*e, and if Ha^Q_{P,P} is also bijective at level one then every amplification is bijective with inverse norm at most 1+C_H*e; the analogous off-diagonal inverse bound for Ha^Q_{P,R} is asserted only when Ha^Q_{P,R} is bijective at level one and Ha^Q_{R,R} satisfies that diagonal lower-modulus hypothesis; all constants independent of n, dim A, block count, and block dimensions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Universal witness selection. Let C_H=max{1,C_prod,C_unit,C_up,C_diag,C_inv,C_rect,C_sp} and e_H=min{1,e_adj,e_prod,e_unit,e_up,e_diag,e_inv,e_rect,e_sp}, where the named positive thresholds and finite constants are supplied by lem-hcb2-amplified-adjointness, lem-hcb2-product-defect, lem-hcb3-diagonal-unit, lem-hcb3-diagonal-upper-norm, lem-hcb3-diagonal-lower-modulus, lem-hcb3-diagonal-inverse, lem-hcb3-offdiagonal-inverse, and lem-hcb4-canonical-closeness. Then C_H is universal and finite, e_H is universal and positive, e<=e_H meets every one of those imported thresholds, and each named error coefficient is at most C_H.

**Type:** claim

**Inference:** finite constant aggregation and direct application of validated registry imports

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Adjoint clause. For every n>=1 and Z in M_n tensor S_{P,R}, lem-hcb2-amplified-adjointness applies (because e<=e_H<=e_adj) and gives exactly (Ha^Q_{P,R})_n(Z)^dagger=(Ha^Q_{R,P})_n(Z^dagger).

**Type:** claim

**Inference:** finite constant aggregation and direct application of validated registry imports

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Product-defect/homomorphism clause. For every n>=1, Z in M_n tensor S_{P,S}, and W in M_n tensor S_{S,R}, lem-hcb2-product-defect and e<=e_H<=e_prod give ||(Ha^Q_{P,R})_n(Z dot W)-(Ha^Q_{P,S})_n(Z)(Ha^Q_{S,R})_n(W)||<=C_prod*e*||Z||||W||<=C_H*e*||Z||||W||; this is the asserted uniform amplified homomorphism estimate.

**Type:** claim

**Inference:** finite constant aggregation and direct application of validated registry imports

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Unit clause. For every n>=1, lem-hcb3-diagonal-unit and e<=e_H<=e_unit give ||(Ha^Q_{P,P})_n(I_n tensor u_P)-I||<=C_unit*e<=C_H*e, which is the required uniform diagonal unit estimate.

**Type:** claim

**Inference:** finite constant aggregation and direct application of validated registry imports

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Upper-norm clause. For every n>=1 and Z in M_n tensor S_P, lem-hcb3-diagonal-upper-norm and e<=e_H<=e_up give ||(Ha^Q_{P,P})_n(Z)||<=(1+C_up*e)||Z||<=(1+C_H*e)||Z||, which is the required uniform amplified upper-norm estimate.

**Type:** claim

**Inference:** finite constant aggregation and direct application of validated registry imports

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Canonical-identity closeness clause. For every n>=1, lem-hcb4-canonical-closeness and e<=e_H<=e_sp give max{||(Ha^Q_{P,Q})_n-J_{P,Q,n}||,||(Ha^Q_{Q,P})_n-J_{Q,P,n}||}<=C_sp*e<=C_H*e, with J the maps fixed by def-canonical-corner-identifications.

**Type:** claim

**Inference:** finite constant aggregation and direct application of validated registry imports

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Conditional diagonal lower-modulus clause. If the level-one lower modulus of Ha^Q_{P,P} is at least 1/4, then for every n>=1 and Z in M_n tensor S_P, lem-hcb3-diagonal-lower-modulus and e<=e_H<=e_diag give ||(Ha^Q_{P,P})_n(Z)||>=(1-C_diag*e)||Z||>=(1-C_H*e)||Z||.

**Type:** claim

**Inference:** finite constant aggregation and direct application of validated registry imports

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Conditional diagonal inverse clause. If Ha^Q_{P,P} has level-one lower modulus at least 1/4 and is bijective at level one, then lem-hcb3-diagonal-inverse and e<=e_H<=e_inv imply that every amplification is bijective and ||((Ha^Q_{P,P})_n)^(-1)||<=1+C_inv*e<=1+C_H*e for every n>=1.

**Type:** claim

**Inference:** finite constant aggregation and direct application of validated registry imports

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** Conditional off-diagonal inverse clause. If Ha^Q_{P,R} is bijective at level one and Ha^Q_{R,R} has level-one lower modulus at least 1/4, then lem-hcb3-offdiagonal-inverse and e<=e_H<=e_rect imply that every amplification of Ha^Q_{P,R} is bijective and has inverse norm at most 1+C_rect*e<=1+C_H*e.

**Type:** claim

**Inference:** finite constant aggregation and direct application of validated registry imports

**Status:** validated

**Taint:** clean

### Node 1.10

**Statement:** Uniformity and conclusion. The witnesses C_H,e_H are finite maxima/minima of universal constants only, hence are independent of n, dim A, block count, and block dimensions; combining the preceding adjoint, defect/homomorphism, unit, upper-norm, canonical-closeness, lower-modulus, and conditional inverse clauses proves every assertion in H-CB.

**Type:** claim

**Inference:** finite constant aggregation and direct application of validated registry imports

**Status:** validated

**Taint:** clean

