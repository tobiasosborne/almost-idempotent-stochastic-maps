# Proof Export

## Node 1

**Statement:** Negative-part subadditivity: for all vectors x and y in R^d, writing n(w) = sum_l max(-w(l), 0), one has n(x + y) <= n(x) + n(y).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Scalar inequality: for all real numbers a and b, max(-(a+b), 0) <= max(-a, 0) + max(-b, 0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Case a+b >= 0: then -(a+b) <= 0, so max(-(a+b),0)=0; also max(-a,0) and max(-b,0) are nonnegative, hence 0 <= max(-a,0)+max(-b,0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Case a+b < 0: then max(-(a+b),0)=-(a+b)=(-a)+(-b); since -a <= max(-a,0) and -b <= max(-b,0), adding gives max(-(a+b),0) <= max(-a,0)+max(-b,0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** The two cases a+b >= 0 and a+b < 0 exhaust all real a,b, so the scalar inequality holds for all real numbers a and b.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Coordinatewise transfer: for vectors x,y in R^d, the scalar inequality gives max(-(x+y)(l), 0) <= max(-x(l), 0) + max(-y(l), 0) for every coordinate l, since (x+y)(l)=x(l)+y(l).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For each coordinate l of vectors in R^d, vector addition is coordinatewise: (x+y)(l)=x(l)+y(l).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For each coordinate l, set a=x(l) and b=y(l). Since (x+y)(l)=x(l)+y(l), a direct scalar case argument gives max(-(x+y)(l),0) <= max(-x(l),0)+max(-y(l),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Inline scalar case proof for the fixed coordinate l: let a=x(l) and b=y(l). If a+b>=0, then max(-(a+b),0)=0, while max(-a,0) and max(-b,0) are nonnegative, so max(-(a+b),0) <= max(-a,0)+max(-b,0). If a+b<0, then max(-(a+b),0)=-(a+b)=(-a)+(-b); also -a<=max(-a,0) and -b<=max(-b,0), hence adding the two inequalities gives max(-(a+b),0) <= max(-a,0)+max(-b,0). Substituting a=x(l), b=y(l), and (x+y)(l)=x(l)+y(l) gives the coordinate inequality with no use of node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Finite summation: summing the coordinatewise inequalities over l and using n(w)=sum_l max(-w(l),0) gives n(x+y) <= n(x)+n(y).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Finite sums preserve coordinatewise inequalities: from the bounds in node 1.2 for every l, summing over l gives sum_l max(-(x+y)(l),0) <= sum_l (max(-x(l),0)+max(-y(l),0)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Finite additivity and the definition of n identify the inequality in node 1.3.1 as n(x+y) <= n(x)+n(y): the left side sum_l max(-(x+y)(l),0) is n(x+y), while sum_l (max(-x(l),0)+max(-y(l),0)) equals sum_l max(-x(l),0)+sum_l max(-y(l),0)=n(x)+n(y).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** By the definition n(w)=sum_l max(-w(l),0), applied to w=x+y, the left side of node 1.3.1, sum_l max(-(x+y)(l),0), is n(x+y). This is the only place where n(x+y) is identified.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.2

**Statement:** Finite additivity of sums gives sum_l (max(-x(l),0)+max(-y(l),0)) = sum_l max(-x(l),0) + sum_l max(-y(l),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.3

**Statement:** Using the finite-additivity identity from node 1.3.2.2, the mixed right-hand sum in node 1.3.1 is sum_l max(-x(l),0)+sum_l max(-y(l),0). By the definition of n applied separately to w=x and w=y, these two sums are n(x) and n(y), respectively, so the mixed right-hand sum is n(x)+n(y).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.4

**Statement:** Combining node 1.3.1 with nodes 1.3.2.1, 1.3.2.2, and 1.3.2.3 substitutes n(x+y) for the left-hand sum and n(x)+n(y) for the mixed right-hand sum, yielding n(x+y) <= n(x)+n(y).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

