# Proof Export

## Node 1

**Statement:** There is a universal e_ncd > 0 such that, whenever R,P,Q are t-projections in a finite-dimensional extended t-C*-algebra, R is nonvanishing, all four left/right subordination errors of P,Q to R are at most t <= e_ncd, A_R = S^A_R, P^R = Co^A_R(P), and Q^R = Co^A_R(Q), one has dim S^A_{P,Q} = dim S^{A_R}_{P^R,Q^R}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let C_* := max{C_nest,1} and e_ncd := min{e_nest,(2C_*)^{-1}}, where C_nest,e_nest are supplied by lem-maincb-nested-corner-comparison. Then e_ncd>0 is universal. Under the hypotheses of node 1, that cited lemma applies. Writing U:=S^A_{P,Q} and V:=S^{A_R}_{P^R,Q^R}, its two linear comparison maps T:U→V and S:V→U are T(X):=F^R_{P,Q}(Co^A_R X) and S(Y):=Co^A_{P,Q}Y, and they satisfy ||TX-X||≤C_*t||X|| for X∈U and ||SY-Y||≤C_*t||Y|| for Y∈V, with C_*t≤1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** The comparison maps in node 1.1 are injective. Indeed, if TX=0 then ||X||=||TX-X||≤(1/2)||X||, so X=0; and if SY=0 then ||Y||=||SY-Y||≤(1/2)||Y||, so Y=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Because A is finite-dimensional, U and V are finite-dimensional. The injections T:U→V and S:V→U therefore give dim U≤dim V and dim V≤dim U, hence dim S^A_{P,Q}=dim S^{A_R}_{P^R,Q^R}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

