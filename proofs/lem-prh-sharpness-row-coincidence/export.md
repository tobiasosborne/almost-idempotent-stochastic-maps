# Proof Export

## Node 1

**Statement:** Row coincidence for stochastic idempotents: for every integer n >= 1, every n-by-n row-stochastic idempotent matrix F=(f_ab) over R, and all i,j in {1,...,n}, if f_ii>0 and f_ij>0 then row_i(F)=row_j(F).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Under the hypotheses of node 1, set p=row_i(F), S={a in {1,...,n}: p_a>0}, and give S the directed edges a->b exactly when f_ab>0. Then S is nonempty and closed under F, the restriction G=(f_ab)_{a,b in S} is row-stochastic, and the directed graph of G is strongly connected.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Because F is row-stochastic, p=row_i(F) is a nonnegative probability row. Idempotence gives pF=row_i(F)F=row_i(F^2)=row_i(F)=p. Also p_i=f_ii>0, so i belongs to S and S is nonempty.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For b not in S, 0=p_b=(pF)_b=sum_{a=1}^n p_a f_ab. Every summand is nonnegative, so f_ab=0 for every a in S. Thus every row indexed by S is supported on S; its entries over S still sum to 1, so G is row-stochastic.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Finite support-component lemma: if a finite row-stochastic matrix G has a stationary probability p that is strictly positive at every vertex, then no positive-entry edge joins two distinct strongly connected components. Indeed, if the condensation DAG had an edge, choose a source component C in a nontrivial weak component. It has no incoming edge and has an outgoing edge. Stationarity and absence of incoming edges give p(C)=sum_{a in C} p_a G(a,C), while the outgoing edge makes G(a,C)<1 for at least one a in C; strict positivity of p makes the displayed right side strictly less than p(C), a contradiction.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** For every a in S, f_ia=p_a>0, so the support graph contains the edge i->a. By node 1.1.3 no such edge can join distinct strongly connected components. Hence every a in S is in the component of i, so the support graph is strongly connected; together with nodes 1.1.1 and 1.1.2 this proves node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.4.1

**Statement:** By nodes 1.1.1 and 1.1.2, p is stationary for F, S is nonempty with i in S, S is closed, and G is row-stochastic. By the definition S={a:p_a>0}, p is zero off S and p_S is strictly positive; for every b in S, (p_S G)_b=sum_{a in S}p_a f_ab=sum_{a=1}^n p_a f_ab=(pF)_b=p_b, so p_S is a stationary probability for G. Therefore node 1.1.3 applies and every positive-entry edge of G has both endpoints in the same strongly connected component.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.4.2

**Statement:** For each a in S, node 1.1.1 gives i in S and g_ia=f_ia=p_a>0, hence G has the edge i->a. By the preceding child, i and a lie in the same strongly connected component. Since a was arbitrary, every vertex of S lies in the component of i, so the graph of G is strongly connected. Together with the nonemptiness, closure, and row-stochasticity supplied by nodes 1.1.1 and 1.1.2, this proves node 1.1 and hence the statement of node 1.1.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Under the hypotheses of node 1 and with p,S,G as in node 1.1, set q=row_j(F). Then j is in S, q is supported on S, and the restriction q_S is a stationary probability row for G.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Since p=row_i(F), the hypothesis f_ij>0 says p_j>0, hence j is in S. Since F is row-stochastic, q=row_j(F) is a nonnegative probability row.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Because j is in S and S is closed under F by node 1.1, f_jb=0 for every b outside S. Hence q is supported on S.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Idempotence gives qF=row_j(F)F=row_j(F^2)=row_j(F)=q. Using the support of q and the closure of S, restriction to S gives q_S G=q_S; thus q_S is a stationary probability row for G.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** Under the hypotheses of node 1, q=row_j(F) and F^2=F imply qF=row_j(F)F=row_j(F^2)=row_j(F)=q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.2

**Statement:** By node 1.1.2, G=(f_ab)_{a,b in S} is row-stochastic, and by node 1.2.2, q_a=0 for every a outside S. Hence for each b in S, (q_S G)_b=sum_{a in S} q_a f_ab=sum_{a=1}^n q_a f_ab=(qF)_b=q_b=(q_S)_b, where the penultimate equality uses node 1.2.3.1. Therefore q_S G=q_S.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.3

**Statement:** By node 1.2.1, q is nonnegative and sum_{a=1}^n q_a=1; by node 1.2.2 it vanishes outside S. Thus q_S is nonnegative and sum_{a in S} q_a=1. Together with row-stochasticity of G from node 1.1.2 and q_S G=q_S from node 1.2.3.2, this says exactly that q_S is a stationary probability row for G.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every finite row-stochastic matrix G whose positive-entry directed graph is strongly connected, any two stationary probability rows p and q with p positive in every coordinate are equal. Applying this to the p and q of nodes 1.1 and 1.2 yields row_i(F)=row_j(F).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Let G be a finite row-stochastic matrix with strongly connected positive-entry graph. Every nonzero nonnegative stationary row r for G is strictly positive: its support T is nonempty, and r_b=sum_a r_a g_ab implies that every positive edge from a vertex of T ends in T. Thus T is successor-closed; strong connectivity forces T to be the whole vertex set.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Let p and q be stationary probability rows for such a G, with p_a>0 everywhere, and set c=min_a(q_a/p_a). Then 0<=c<=1, r=q-cp is nonnegative and stationary, and r has a zero coordinate. If c<1, then sum_a r_a=1-c>0, so node 1.3.1 says r is strictly positive, contradicting its zero coordinate. Hence c=1, and r=q-p is nonnegative with coordinate sum zero, so q=p.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** For nodes 1.1 and 1.2, G is finite, row-stochastic, and strongly connected; p_S is a strictly positive stationary probability row and q_S is a stationary probability row. Node 1.3.2 gives q_S=p_S. Both full rows q and p vanish outside S, so q=p, namely row_j(F)=row_i(F).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

