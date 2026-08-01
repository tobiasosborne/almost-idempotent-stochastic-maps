# Proof Export

## Node 1

**Statement:** If B is a finite-dimensional C*-algebra, A is a finite-dimensional extended epsilon-C*-algebra, v:B->A is linear, and 0 <= delta <= delta', then if v is an extended delta-inclusion it is an extended delta'-inclusion, and if v is an extended delta-isomorphism it is an extended delta'-isomorphism and in particular an extended delta'-inclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Assume v is an extended delta-inclusion and fix arbitrary n>=1. By def-extended-delta-inclusion, v_n=1_{M_n} tensor v is a delta-homomorphism and, for every X, (1-delta)||X|| <= ||v_n(X)|| <= (1+delta)||X||. By GT-kitaev-def-delta-homomorphism, v_n is bounded linear, satisfies ||v_n(I)-I|| <= delta and ||v_n(XY)-v_n(X)v_n(Y)|| <= delta||X||||Y||, and in the *-algebra setting preserves the involution exactly. Since 0<=delta<=delta' and norms and products of norms are nonnegative, these inequalities imply ||v_n(I)-I|| <= delta' and ||v_n(XY)-v_n(X)v_n(Y)|| <= delta'||X||||Y||; bounded linearity and exact involution preservation are unchanged. Thus v_n is a delta'-homomorphism by GT-kitaev-def-delta-homomorphism. Moreover (1-delta')||X|| <= (1-delta)||X|| and (1+delta)||X|| <= (1+delta')||X||, since ||X||>=0, so v_n satisfies the two-sided (1+-delta') norm bounds. As n was arbitrary, def-extended-delta-inclusion makes v an extended delta'-inclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Assume v is an extended delta-isomorphism. By def-extended-delta-inclusion this means that v is an extended delta-inclusion and v is bijective. The first child makes the same map v an extended delta'-inclusion, while bijectivity is independent of the defect parameter and is unchanged. Hence the definition makes v an extended delta'-isomorphism; and every extended delta'-isomorphism is, by that same definition, in particular an extended delta'-inclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

