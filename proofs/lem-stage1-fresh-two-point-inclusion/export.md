# Proof Export

## Node 1

**Statement:** There are universal C_pair<infinity and e_pair>0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0<=epsilon_X<=e_pair and 1<dim_C calX<infinity contains nonvanishing C_pair*epsilon_X-projections P',P'' with P'+P''=I_X for which the linear map v^(2):C^2->calX, v^(2)(lambda,mu)=lambda*P'+mu*P'', is an extended C_pair*epsilon_X-inclusion, satisfies v^(2)(1,1)=I_X, and sends the standard projection basis Pi',Pi'' to P',P''.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix an arbitrary finite-dimensional extended epsilon_X-C*-algebra satisfying the root hypotheses. By lem-stage1-original-complementary-pair there are universal C_np<infinity and e_np>0 and, whenever epsilon_X<=e_np, elements q_1,q_2 with q_1+q_2=I_X such that each q_i is a nonvanishing C_np*epsilon_X-projection and ||q_1q_2||,||q_2q_1||<=C_np*epsilon_X. Thus, with d=max{||q_1^2-q_1||,||q_2^2-q_2||,||q_1q_2||,||q_2q_1||}, one has d<=C_np*epsilon_X and q_i^dagger=q_i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** By the nonvanishing alternative in def-delta-projection, applied to the pair from node 1.1, there is a universal e_nv in (0,e_np] such that epsilon_X<=e_nv implies ||q_1||>=1/2 and ||q_2||>=1/2. Indeed nonvanishing gives | ||q_i||-1 |<=O(C_np*epsilon_X+epsilon_X), with a universal data-independent coefficient, so one common shrink works for both i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Define the single level-one linear map v^(2):C^2->calX by v^(2)(lambda,mu)=lambda*q_1+mu*q_2 and, for every n>=1, define only its canonical amplification v_n=id_{M_n} tensor v^(2), so v_n(A,B)=A tensor q_1+B tensor q_2. Linearity is immediate; q_i^dagger=q_i gives exact involution preservation; for the standard projection basis Pi'=(1,0), Pi''=(0,1) from def-projection-basis one has v^(2)(Pi')=q_1 and v^(2)(Pi'')=q_2; and q_1+q_2=I_X gives v^(2)(1,1)=I_X and v_n(I_n,I_n)=I_n tensor I_X exactly.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The operator-space axioms in def-operator-space imply the simple-tensor identity ||T tensor z||_n=||T||*||z|| for T in M_n and z in calX: the rectangular matrix inequality gives the upper bound, while compression by unit vectors u,v chosen with |u^*Tv|=||T|| gives ||T||*||z||=||(u^* tensor 1)(T tensor z)(v tensor 1)||<=||T tensor z||. This applies uniformly at every n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** For x=(A,B), y=(C,D) in M_n(C^2), bilinearity alone gives the exact four-term identity v_n(x)v_n(y)-v_n(xy)=AC tensor(q_1^2-q_1)+AD tensor(q_1q_2)+BC tensor(q_2q_1)+BD tensor(q_2^2-q_2). Using node 1.4, ||RS||<=||R||*||S|| for scalar matrices, and ||(A,B)||=max{||A||,||B||}, its norm is at most 4d||x||||y||. Together with the exact linearity and involution preservation in node 1.3, every v_n is a non-unital 4d-homomorphism, with a defect independent of n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Assume epsilon_X<=e_nv and normalize ||(A,B)||=1. If ||A||=1, then v_n(A,B)(I_n tensor q_1)-A tensor q_1=A tensor(q_1^2-q_1)+B tensor(q_2q_1), so node 1.4 gives error at most 2d. Since M_n tensor calX is an epsilon_X-C*-algebra by def-extended-epsilon-cstar-algebra, its defining multiplication bound gives ||v_n(A,B)(I_n tensor q_1)||<=(1+epsilon_X)||v_n(A,B)||*||q_1||. Hence ||v_n(A,B)||>=(||q_1||-2d)/((1+epsilon_X)||q_1||)>=(1-4d)/(1+epsilon_X). If instead ||B||=1, the same calculation with right multiplication by q_2 and the defect q_1q_2 gives the identical bound. After a universal further shrink ensuring d<=1/8 and epsilon_X<=1, homogeneity yields ||v_n(x)||>=1/4||x|| for every n and x.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Choose a universal e_up>0 no larger than all preceding thresholds, the smallness radii in GT-kitaev-prop-delta-hominc, and a number satisfying 8*C_np*e_up<1/4. Then delta_n:=4d<=4*C_np*epsilon_X has 2*delta_n<1/4. Apply GT-kitaev-prop-delta-hominc to each fixed canonical v_n from node 1.3: the domain M_n(C^2) is an exact C*-algebra (hence an epsilon_X-C*-algebra), the codomain M_n tensor calX is an epsilon_X-C*-algebra by def-extended-epsilon-cstar-algebra, node 1.5 supplies the delta_n-homomorphism property, and node 1.6 supplies eta=1/4. The external gives ||v_n||<=1+O(delta_n+epsilon_X) and ||v_n(x)||>=(1-O(delta_n+epsilon_X))||x||, with universal big-O coefficients independent of n and all input data.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.7.1

**Statement:** Let delta_max>0 be the universal delta-smallness radius in GT-kitaev-prop-delta-hominc, and put M:=max{C_np,1}. In the choice already made at node 1.7, shrink the universal positive threshold e_up further so that e_up<=delta_max/(4M) and e_up<=1/(64M), as well as every preceding threshold. (This is possible because C_np is finite and all listed radii are positive.) Since 0<=epsilon_X<=e_up and d<=C_np*epsilon_X, for every n we have delta_n=4d<=4C_np*epsilon_X<=4M*e_up<=delta_max; independently, 2delta_n<=8C_np*e_up<=8M*e_up<=1/8<1/4. Thus both the separate hypothesis delta_n<=delta_max and the eta compatibility 2delta_n<eta=1/4 required by GT-kitaev-prop-delta-hominc hold. Together with nodes 1.3, 1.5, and 1.6 and the domain/codomain facts stated in node 1.7, the proposition is therefore applicable to each v_n and yields exactly the two uniform norm estimates asserted there.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Because delta_n+epsilon_X<=(4*C_np+1)epsilon_X, the universal estimates in node 1.7 admit one finite universal coefficient K such that, simultaneously for all n, v_n is a K*epsilon_X-homomorphism and (1-K*epsilon_X)||x||<=||v_n(x)||<=(1+K*epsilon_X)||x||. By def-extended-delta-inclusion, the one map v^(2) is therefore an extended K*epsilon_X-inclusion; no level-dependent map or constant was chosen.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.8.1

**Statement:** Write the two universal big-O bounds supplied by node 1.7 as U*(delta_n+epsilon_X) for the upper estimate and L*(delta_n+epsilon_X) for the lower estimate, with fixed finite universal U,L independent of n and of the input algebra (enlarging either coefficient if necessary on the common smallness range). Since delta_n=4d<=4*C_np*epsilon_X, choose K=max{4*C_np,U*(4*C_np+1),L*(4*C_np+1)}. Then for every n and x one has the multiplicative defect at most 4d||x||||y||<=K*epsilon_X||x||||y||, and (1-K*epsilon_X)||x||<=||v_n(x)||<=||v_n||*||x||<=(1+K*epsilon_X)||x||. This is one K for all n. This bridge is conditional on, and may be accepted only after, validation of node 1.7.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** Set e_pair=e_up and choose the universal C_pair>=max{C_np,K,4*C_np}. Nodes 1.1-1.2 make q_1,q_2 nonvanishing C_pair*epsilon_X-projections with q_1+q_2=I_X (enlarging the defect allowance preserves that property); nodes 1.3 and 1.8 give the required single linear map, its extended C_pair*epsilon_X-inclusion bounds at every amplification, the exact unit value, and the exact standard-basis images. Taking P'=q_1 and P''=q_2 proves every clause of the root contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

