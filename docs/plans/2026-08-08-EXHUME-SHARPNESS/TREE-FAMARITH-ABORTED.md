=== Proof Status ===

1 [[33mpending[0m/[33munresolved[0m] Witness arithmetic for PRH sharpness: for every real lambda with 0 < lambda < 1/2, let A_lambda in R^(4x2) have rows (1,0), (0,1), (1-lambda,lambda), (lambda,1-lambda), and let M_lambda in R^(2x4) have rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda); A_lambda and M_lambda have nonnegative entries and probability-vector rows and hence represent positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2); for every pair of integers r,s >= 1 and every B in R^(r x s), the induced l-infinity operator norm is ||B||_{infinity->infinity}=max_{1<=i<=r} sum_{j=1}^s |B_ij|; M_lambda A_lambda has rows (1-lambda^2,lambda^2), (lambda^2,1-lambda^2), so epsilon_lambda:=||M_lambda A_lambda-I_2||_{infinity->infinity}=2*lambda^2 and epsilon_lambda tends to 0 as lambda tends to 0; and P_lambda:=A_lambda M_lambda is row-stochastic with rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda), ((1-lambda)^2,lambda*(1-lambda),lambda*(1-lambda),lambda^2), (lambda*(1-lambda),(1-lambda)^2,lambda^2,lambda*(1-lambda)), and ||row_1(P_lambda)-row_3(P_lambda)||_1=2*lambda.
  1.1 [[32mvalidated[0m/[33munresolved[0m] Fix a real lambda with 0<lambda<1/2. Every displayed row of A_lambda and M_lambda has nonnegative entries summing to 1; hence, by def-positive-approximate-retract's probability-row equivalence, these matrices represent positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2).
    1.1.1 [[32mvalidated[0m/[33munresolved[0m] Since 0<lambda<1/2, both lambda and 1-lambda are nonnegative. Thus every entry in the four rows (1,0), (0,1), (1-lambda,lambda), (lambda,1-lambda) of A_lambda is nonnegative, and their row sums are respectively 1, 1, (1-lambda)+lambda=1, and lambda+(1-lambda)=1.
    1.1.2 [[32mvalidated[0m/[33munresolved[0m] Since lambda and 1-lambda are nonnegative, every entry in the two rows (1-lambda,0,lambda,0) and (0,1-lambda,0,lambda) of M_lambda is nonnegative, and each row sum is (1-lambda)+lambda=1.
    1.1.3 [[32mvalidated[0m/[33munresolved[0m] By the registered definition def-positive-approximate-retract, a matrix between these finite commutative l-infinity spaces represents a positive unital map exactly when it has probability-vector rows; applying this equivalence to the preceding row checks yields the asserted types and positivity/unitality of A_lambda and M_lambda.
  1.2 [[32mvalidated[0m/[33munresolved[0m] For all integers r,s>=1 and B in R^(r x s), if ||x||_infinity=max_j |x_j| and the induced norm is sup_{x != 0} ||Bx||_infinity/||x||_infinity, then ||B||_{infinity->infinity}=max_i sum_j |B_ij|.
    1.2.1 [[32mvalidated[0m/[33munresolved[0m] Let R:=max_{1<=i<=r} sum_{j=1}^s |B_ij|. For every x in R^s and every i, the triangle inequality gives |(Bx)_i|=|sum_j B_ij x_j| <= sum_j |B_ij||x_j| <= R||x||_infinity; hence ||Bx||_infinity <= R||x||_infinity and ||B||_{infinity->infinity} <= R.
    1.2.2 [[32mvalidated[0m/[33munresolved[0m] Choose an index i0 attaining the finite maximum R and define x_j=1 when B_{i0,j}>=0 and x_j=-1 when B_{i0,j}<0. Since s>=1, ||x||_infinity=1, while (Bx)_{i0}=sum_j |B_{i0,j}|=R; therefore ||Bx||_infinity>=R and ||B||_{infinity->infinity}>=R.
    1.2.3 [[32mvalidated[0m/[33munresolved[0m] The upper and lower inequalities for the same number R imply ||B||_{infinity->infinity}=R=max_i sum_j |B_ij|.
  1.3 [[32mvalidated[0m/[33munresolved[0m] Direct matrix multiplication gives M_lambda A_lambda with rows (1-lambda^2,lambda^2) and (lambda^2,1-lambda^2).
    1.3.1 [[32mvalidated[0m/[33munresolved[0m] The first row of M_lambda A_lambda is (1-lambda)row_1(A_lambda)+lambda row_3(A_lambda)=(1-lambda)(1,0)+lambda(1-lambda,lambda)=(1-lambda^2,lambda^2).
    1.3.2 [[32mvalidated[0m/[33munresolved[0m] The second row of M_lambda A_lambda is (1-lambda)row_2(A_lambda)+lambda row_4(A_lambda)=(1-lambda)(0,1)+lambda(lambda,1-lambda)=(lambda^2,1-lambda^2).
  1.4 [[33mpending[0m/[33munresolved[0m] Using the max-row norm formula, epsilon_lambda:=||M_lambda A_lambda-I_2||_{infinity->infinity}=2*lambda^2, and epsilon_lambda tends to 0 as lambda tends to 0.
    1.4.1 [[33mpending[0m/[33munresolved[0m] Subtracting I_2 from the displayed product M_lambda A_lambda gives rows (-lambda^2,lambda^2) and (lambda^2,-lambda^2). Because lambda^2>=0, each absolute row sum is 2lambda^2, so the max-row formula yields epsilon_lambda=2lambda^2.
      1.4.1.1 [[33mpending[0m/[33munresolved[0m] From the stipulated rows of A_lambda and M_lambda, direct entrywise multiplication gives M_lambda A_lambda = ((1-lambda^2, lambda^2),(lambda^2,1-lambda^2)): indeed the first row is (1-lambda)(1,0)+lambda(1-lambda,lambda)=(1-lambda^2,lambda^2), and the second is (1-lambda)(0,1)+lambda(lambda,1-lambda)=(lambda^2,1-lambda^2).
      1.4.1.2 [[33mpending[0m/[33munresolved[0m] For every real matrix B, its induced l-infinity operator norm equals its maximum absolute row sum: for ||x||_infinity<=1, |(Bx)_i|<=sum_j |B_ij|, proving the upper bound; choosing a row i_0 attaining the finite maximum and x_j=1 when B_{i_0j}>=0 and x_j=-1 when B_{i_0j}<0 gives ||x||_infinity=1 and (Bx)_{i_0}=sum_j |B_{i_0j}|, proving the reverse bound.
      1.4.1.3 [[33mpending[0m/[33munresolved[0m] Writing the stipulated rows of M_lambda as m_1=(1-lambda,0,lambda,0) and m_2=(0,1-lambda,0,lambda), multiplication by the stipulated rows of A_lambda gives m_1 A_lambda=(1-lambda)(1,0)+lambda(1-lambda,lambda)=(1-lambda^2,lambda^2) and m_2 A_lambda=(1-lambda)(0,1)+lambda(lambda,1-lambda)=(lambda^2,1-lambda^2). Hence D=M_lambda A_lambda-I_2=((-lambda^2,lambda^2),(lambda^2,-lambda^2)). For completeness, the induced l-infinity norm of any finite real matrix B is its maximum absolute row sum: if ||x||_infinity<=1 then |(Bx)_i|<=sum_j|B_ij|, while for a maximizing row i_0 the choice x_j=1 for B_{i_0j}>=0 and x_j=-1 otherwise attains sum_j|B_{i_0j}|. Since lambda^2>=0, both absolute row sums of D equal 2lambda^2; therefore ||D||_{infinity->infinity}=2lambda^2, which equals epsilon_lambda by its definition.
    1.4.2 [[32mvalidated[0m/[33munresolved[0m] For every delta>0 choose rho=sqrt(delta/2)>0. If |lambda|<rho, then 0<=epsilon_lambda=2lambda^2<2rho^2=delta; this is exactly epsilon_lambda -> 0 as lambda -> 0.
  1.5 [[32mvalidated[0m/[33munresolved[0m] Direct matrix multiplication gives P_lambda:=A_lambda M_lambda with the four rows asserted in node 1.
    1.5.1 [[32mvalidated[0m/[33munresolved[0m] Because row_1(A_lambda)=(1,0) and row_2(A_lambda)=(0,1), the first two rows of A_lambda M_lambda are row_1(M_lambda)=(1-lambda,0,lambda,0) and row_2(M_lambda)=(0,1-lambda,0,lambda).
    1.5.2 [[32mvalidated[0m/[33munresolved[0m] The third row is (1-lambda)row_1(M_lambda)+lambda row_2(M_lambda)=((1-lambda)^2,lambda(1-lambda),lambda(1-lambda),lambda^2), and the fourth is lambda row_1(M_lambda)+(1-lambda)row_2(M_lambda)=(lambda(1-lambda),(1-lambda)^2,lambda^2,lambda(1-lambda)).
  1.6 [[33mpending[0m/[33munresolved[0m] Every entry of P_lambda is nonnegative and every row sums to 1; hence P_lambda is row-stochastic.
    1.6.1 [[32mvalidated[0m/[33munresolved[0m] From 0<lambda<1/2, the factors lambda and 1-lambda are nonnegative, so every coordinate in all four displayed rows of P_lambda is nonnegative.
    1.6.2 [[32mvalidated[0m/[33munresolved[0m] The first two displayed rows each sum to (1-lambda)+lambda=1. Each of the last two sums to (1-lambda)^2+2lambda(1-lambda)+lambda^2=((1-lambda)+lambda)^2=1. Thus every row is a probability vector, which is precisely row-stochasticity.
  1.7 [[32mvalidated[0m/[33munresolved[0m] The l1-distance between row_1(P_lambda)=(1-lambda,0,lambda,0) and row_3(P_lambda)=((1-lambda)^2,lambda(1-lambda),lambda(1-lambda),lambda^2) equals 2*lambda.
    1.7.1 [[32mvalidated[0m/[33munresolved[0m] Subtracting row_3(P_lambda) from row_1(P_lambda) coordinatewise gives (lambda(1-lambda), -lambda(1-lambda), lambda^2, -lambda^2).
    1.7.2 [[32mvalidated[0m/[33munresolved[0m] Since 0<lambda<1/2 implies lambda(1-lambda)>0 and lambda^2>0, the l1 norm of that difference is 2lambda(1-lambda)+2lambda^2=2lambda((1-lambda)+lambda)=2lambda.

--- Statistics ---
Nodes: 27 total
  Epistemic: 0 [34mdraft[0m, 7 [33mpending[0m, 20 [32mvalidated[0m, 0 [36madmitted[0m, 0 [31mrefuted[0m, 0 [90marchived[0m, 0 [35mneeds_refinement[0m
  Taint: 0 [32mclean[0m, 0 [36mself_admitted[0m, 0 [31mtainted[0m, 27 [33munresolved[0m

--- Jobs ---
  Prover: 7 nodes awaiting refinement
  Verifier: 0 nodes ready for review

--- Legend ---
Epistemic States:
  [34mdraft[0m      - Work in progress (not submitted)
  [33mpending[0m    - Awaiting proof/verification
  [32mvalidated[0m  - Verified by adversarial verifier
  [36madmitted[0m   - Accepted without full verification
--- run 1 of the factored family-arithmetic row: BALLOON 27>26, 20 validated, 2 open challenges (cross-sibling deps; the 'candidate vectors are THE A,M rows' identification gap) ---
