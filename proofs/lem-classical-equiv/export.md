# Proof Export

## Node 1

**Statement:** The signed-idempotent and stochastic-idempotent formulations of classical stability are equivalent up to universal constants: Q row-stochastic with ||Q^2-Q|| <= eta gives P=theta(2Q-1) signed affine retraction with ||P-Q|| <= C eta and neg mass delta <= C eta, and conversely row-normalising p_i^+ gives Q with ||P-Q|| <= 2 delta, ||Q^2-Q|| <= 6 delta+4 delta^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Forward direction: for sufficiently small eta, any row-stochastic Q with ||Q^2-Q||_{inf->inf} <= eta produces an exact signed idempotent P=theta(2Q-I) with P1=1, P^2=P, ||P-Q||_{inf->inf} <= C eta, and negative mass delta(P) <= C eta for a universal C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Let X=2Q-I. Since Q is row-stochastic, X1=1, ||X||_{inf->inf} <= 3, and X^2-I=4(Q^2-Q), so ||X^2-I||_{inf->inf} <= 4 eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Using the validated sibling 1.1.1, write Y=X^2-I with X1=1, ||X||_{inf->inf}<=3, and ||Y||_{inf->inf}<=4 eta. For eta<=1/8 define B=(X^2)^(-1/2)=(I+Y)^(-1/2) by the convergent binomial series and set S=XB and theta(X)=(I+S)/2. Then B commutes with X, B1=1, ||B-I||_{inf->inf}<=8 eta; hence S^2=I, S1=1, and ||S-X||_{inf->inf}<=24 eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** From 1.1.1, Y=X^2-I satisfies Y1=X^2 1-1=X1-1=0, ||Y||_{inf->inf}<=4 eta, and ||X||_{inf->inf}<=3. If eta<=1/8 then ||Y||<=1/2<1, so the binomial series B=sum_{m>=0} binom(-1/2,m)Y^m converges absolutely in operator norm. Because B is the norm limit of polynomials in Y=X^2-I, it commutes with X. Since Y1=0, Y^m1=0 for all m>=1, hence B1=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.2

**Statement:** For t=||Y||_{inf->inf}<=1/2, the absolute coefficient sum gives ||B-I||<=sum_{m>=1}|binom(-1/2,m)|t^m=(1-t)^(-1/2)-1<=2t. With t<=4 eta this yields ||B-I||_{inf->inf}<=8 eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.3

**Statement:** The scalar identity ((1+z)^(-1/2))^2(1+z)=1 on |z|<1 transfers to the absolutely convergent power series in Y; therefore B^2(I+Y)=I, i.e. B^2 X^2=I. Since B commutes with X, S=XB satisfies S^2=XBXB=X^2B^2=I.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.4

**Statement:** Using B1=1 and X1=1 from 1.1.2.1, S1=XB1=X1=1. Also S-X=X(B-I), so ||S-X||_{inf->inf}<=||X||_{inf->inf}||B-I||_{inf->inf}<=3*8 eta=24 eta by 1.1.1 and 1.1.2.2. Thus the amended statement holds with K=8 and C=24.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.4.1

**Statement:** Explicit dependency import for node 1.1.2.4: this algebraic step depends on the validated local facts X1=1 and B1=1 from 1.1.2.1, ||X||_{inf->inf}<=3 from 1.1.1, and ||B-I||_{inf->inf}<=8 eta from 1.1.2.2. These are recorded as required validated dependencies here, so no unvalidated sibling fact is assumed inside this node.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

###### Node 1.1.2.4.2

**Statement:** Conditional algebra/QED: with S=XB and the imported identities B1=1 and X1=1, S1=XB1=X1=1. Also S-X=XB-X=X(B-I); by submultiplicativity of ||.||_{inf->inf} and the imported bounds, ||S-X||_{inf->inf}<=||X||_{inf->inf}||B-I||_{inf->inf}<=3*8 eta=24 eta. Thus node 1.1.2.4 proves exactly the consequences it claims, with the contested inputs supplied only through the explicit validated dependencies.

**Type:** qed

**Inference:** assumption

**Status:** archived

**Taint:** clean

###### Node 1.1.2.4.3

**Statement:** Dependency-recorded QED: relying explicitly on validated nodes 1.1.1, 1.1.2.1, and 1.1.2.2, we may use X1=1, B1=1, ||X||_{inf->inf}<=3, and ||B-I||_{inf->inf}<=8 eta. Then S1=XB1=X1=1 and S-X=X(B-I), so ||S-X||_{inf->inf}<=3*8 eta=24 eta by submultiplicativity. This child supplies the missing dependency relationship challenged in ch-c6006369fb6ad4bf.

**Type:** qed

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.1.2.5

**Statement:** Dependency bridge/QED: node 1.1.2 is not derived from the bare inequality ||X^2-I||<1. Its imported hypotheses X1=1, ||X||_{inf->inf}<=3, and ||X^2-I||_{inf->inf}<=4 eta are exactly the validated sibling node 1.1.1. Under eta<=1/8, substeps 1.1.2.1--1.1.2.4 prove convergence of B=(X^2)^(-1/2), B1=1, ||B-I||<=8 eta, S^2=I, S1=1, and ||S-X||<=24 eta, so the amended parent statement follows.

**Type:** qed

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** With P=theta(X)=(I+S)/2, the identities S^2=I and S1=1 give P^2=P and P1=1, so P is an exact signed idempotent by def-signed-idempotent; moreover P-Q=(S-X)/2, so ||P-Q||_{inf->inf} <= C eta, and because Q is entrywise nonnegative row-stochastic by def-stochastic, each negative entry of P is bounded by the corresponding row error, giving delta(P) <= ||P-Q||_{inf->inf} <= C eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.1

**Statement:** Dependency import and exact-idempotence algebra: using the prerequisite conclusions of 1.1.1 and 1.1.2, we have X=2Q-I (so Q=(I+X)/2), S^2=I, S1=1, and ||S-X||_{inf->inf}<=24 eta. For P=(I+S)/2, P1=(1+1)/2=1 and P^2=(I+2S+S^2)/4=(I+S)/2=P, hence P is an exact signed idempotent by def-signed-idempotent.

**Type:** claim

**Inference:** modus_ponens

**Status:** archived

**Taint:** clean

##### Node 1.1.3.2

**Statement:** Distance estimate: because P=(I+S)/2 and Q=(I+X)/2, P-Q=(S-X)/2. Therefore ||P-Q||_{inf->inf}<=(1/2)||S-X||_{inf->inf}<=12 eta, after the prerequisite bound from 1.1.2 is validated.

**Type:** claim

**Inference:** modus_ponens

**Status:** archived

**Taint:** clean

##### Node 1.1.3.3

**Statement:** Negative-mass estimate: by def-stochastic, row-stochastic Q is entrywise nonnegative. For each row i and coordinate j with P_ij<0, (P_ij)_-=-P_ij<=|P_ij-Q_ij| since Q_ij>=0; summing over j gives the negative mass of row i at most ||p_i-q_i||_1. Taking the maximum over rows gives delta(P)<=||P-Q||_{inf->inf}<=12 eta.

**Type:** claim

**Inference:** by_definition

**Status:** archived

**Taint:** clean

##### Node 1.1.3.4

**Statement:** Dependency import and exact-idempotence algebra: using the prerequisite conclusions of 1.1.1 and 1.1.2, we have X=2Q-I (so Q=(I+X)/2), S^2=I, S1=1, and ||S-X||_{inf->inf}<=24 eta. For P=(I+S)/2, P1=(1+1)/2=1 and P^2=(I+2S+S^2)/4=(I+S)/2=P, hence P is an exact signed idempotent by def-signed-idempotent.

**Type:** claim

**Inference:** modus_ponens

**Status:** archived

**Taint:** clean

##### Node 1.1.3.5

**Statement:** Distance estimate: because P=(I+S)/2 and Q=(I+X)/2, P-Q=(S-X)/2. Therefore ||P-Q||_{inf->inf}<=(1/2)||S-X||_{inf->inf}<=12 eta, after the prerequisite bound from 1.1.2 is validated.

**Type:** claim

**Inference:** modus_ponens

**Status:** archived

**Taint:** clean

##### Node 1.1.3.6

**Statement:** Negative-mass estimate: by def-stochastic, row-stochastic Q is entrywise nonnegative. For each row i and coordinate j with P_ij<0, (P_ij)_-=-P_ij<=|P_ij-Q_ij| since Q_ij>=0; summing over j gives the negative mass of row i at most ||p_i-q_i||_1. Taking the maximum over rows gives delta(P)<=||P-Q||_{inf->inf}<=12 eta.

**Type:** claim

**Inference:** by_definition

**Status:** archived

**Taint:** clean

##### Node 1.1.3.7

**Statement:** Using the prerequisite conclusions of 1.1.1 and 1.1.2: X=2Q-I, so Q=(I+X)/2; Q is row-stochastic and hence Q>=0 entrywise by def-stochastic; S^2=I, S1=1, and ||S-X||_{inf->inf}<=24 eta. With P=theta(X)=(I+S)/2, P1=(1+1)/2=1 and P^2=(I+2S+S^2)/4=(I+S)/2=P, so P is an exact signed idempotent by def-signed-idempotent. Also P-Q=(S-X)/2, hence ||P-Q||_{inf->inf}<=12 eta. By the permitted and registered definition def-negative-mass, delta(P)=max_i sum_j max{-P_ij,0}. For every i,j, Q_ij>=0 implies max{-P_ij,0}<=|P_ij-Q_ij|: if P_ij<0 then |P_ij-Q_ij|=Q_ij-P_ij>=-P_ij, while if P_ij>=0 the left side is 0. Summing over j and taking the maximum over i gives delta(P)<=max_i sum_j |P_ij-Q_ij|=||P-Q||_{inf->inf}<=12 eta. Thus the node proves exact signed idempotence, the distance bound, and the negative-mass bound with universal constant 12, conditional on validated prerequisites 1.1.1 and 1.1.2.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

###### Node 1.1.3.7.1

**Statement:** Scope/gap certificate for the negative-mass line: this node does not prove delta(P)<=||P-Q||_{inf->inf} from the current permitted context. In this AF node there are no local dependencies, definitions, or externals, and the lemma workspace registers only def-stochastic and def-signed-idempotent. These inputs give row-stochastic nonnegativity for Q and exact signed idempotence/row-geometry for P, but they do not define delta(P) as max_i sum_j max{-P_ij,0}. Therefore the rowwise negative-part argument is unavailable in this scope. The mathematically correct repair is to register the missing negative-mass definition (or weaken the parent statement); until then the parent delta-bound remains unproved.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.3.7.1.1

**Statement:** Allowed-scope audit: this node has no declared dependencies, local definitions, or externals, and the workspace-level af defs are only def-stochastic and def-signed-idempotent. Thus any use of a separate formula for negative mass must come from one of those two allowed definitions or it is out of scope.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.3.7.1.2

**Statement:** The two allowed definitions do not supply the needed formula. def-stochastic gives row-stochastic matrices as entrywise nonnegative maps fixing 1, and def-signed-idempotent gives P1=1 and P^2=P together with row-geometry mentioning delta(P). Neither states delta(P)=max_i sum_j max{-P_ij,0}. Therefore the expression max_i sum_j max{-P_ij,0} cannot be substituted for delta(P) inside this node.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.3.7.1.3

**Statement:** Consequent repair: under the current permitted context the negative-mass estimate is not proved. The parent delta-bound can be discharged only after the missing negative-mass definition is registered as an allowed input, or else the parent statement must be weakened to omit that bound. This child is a gap certificate, not a proof of the delta estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.3.7.2

**Statement:** Scope repair and negative-mass bridge: argument/lemmas/lem-classical-equiv.md permits def-negative-mass, and def-negative-mass is now registered in this AF workspace. Hence delta(P)=max_i sum_j max{-P_ij,0} is an allowed definition here, so the old missing-definition caveat is superseded. From 1.1.1, Q is row-stochastic, hence Q_ij>=0 by def-stochastic. From 1.1.2 and P=(I+S)/2, Q=(I+X)/2, we have P-Q=(S-X)/2 and ||P-Q||_{inf->inf}<=12 eta. For each i,j, if P_ij<0 then max{-P_ij,0}=-P_ij<=Q_ij-P_ij=|P_ij-Q_ij| because Q_ij>=0; if P_ij>=0 the same inequality is trivial. Summing over j and taking max_i gives delta(P)<=max_i sum_j |P_ij-Q_ij|=||P-Q||_{inf->inf}<=12 eta.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Converse direction: if P is an exact signed idempotent with negative mass delta and Q is obtained by row-normalising the positive parts p_i^+, then Q is row-stochastic, ||P-Q||_{inf->inf} <= 2 delta, and ||Q^2-Q||_{inf->inf} <= 6 delta+4 delta^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For row p_i of P, write p_i=p_i^+-p_i^- with disjoint nonnegative positive and negative parts, let a_i=sum_k (P_{ik})_- <= delta, and set q_i=p_i^+/(1+a_i). Since sum_k p_{ik}=1 by def-signed-idempotent, sum_k p_i^+=1+a_i, so each q_i is nonnegative of total mass 1 and Q is row-stochastic by def-stochastic.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For e_i=q_i-p_i, one has e_i=p_i^--(a_i/(1+a_i))p_i^+; the two displayed summands have disjoint supports and l1-masses a_i and a_i, so ||e_i||_1=2a_i <= 2delta. Therefore D=Q-P satisfies ||D||_{inf->inf}=max_i ||e_i||_1 <= 2delta, i.e. ||P-Q||_{inf->inf} <= 2delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** The row-geometry clause of def-signed-idempotent gives ||P||_{inf->inf} <= 1+2delta, hence ||P-I||_{inf->inf} <= 2+2delta. For each row, q_iQ-q_i=e_i(P-I)+q_iD because P^2=P; with q_i nonnegative of total mass 1, ||q_iD||_1 <= ||D||_{inf->inf} <= 2delta and ||e_i(P-I)||_1 <= (2delta)(2+2delta), so ||Q^2-Q||_{inf->inf} <= 6delta+4delta^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

