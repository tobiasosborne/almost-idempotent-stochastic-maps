# Proof Export

## Node 1

**Statement:** Witness arithmetic for PRH sharpness: for every real lambda with 0 < lambda < 1/2, let A_lambda in R^(4x2) have rows (1,0), (0,1), (1-lambda,lambda), (lambda,1-lambda), and let M_lambda in R^(2x4) have rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda); A_lambda and M_lambda have nonnegative entries and probability-vector rows and hence represent positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2); for every pair of integers r,s >= 1 and every B in R^(r x s), the induced l-infinity operator norm is ||B||_{infinity->infinity}=max_{1<=i<=r} sum_{j=1}^s |B_ij|; M_lambda A_lambda has rows (1-lambda^2,lambda^2), (lambda^2,1-lambda^2), so epsilon_lambda:=||M_lambda A_lambda-I_2||_{infinity->infinity}=2*lambda^2 and epsilon_lambda tends to 0 as lambda tends to 0; and P_lambda:=A_lambda M_lambda is row-stochastic with rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda), ((1-lambda)^2,lambda*(1-lambda),lambda*(1-lambda),lambda^2), (lambda*(1-lambda),(1-lambda)^2,lambda^2,lambda*(1-lambda)), and ||row_1(P_lambda)-row_3(P_lambda)||_1=2*lambda.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix an arbitrary real lambda with 0 < lambda < 1/2. Then lambda > 0 and 1-lambda > 1/2 > 0, so lambda, 1-lambda, lambda^2, (1-lambda)^2, and lambda(1-lambda) are all nonnegative.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For A_lambda with rows (1,0), (0,1), (1-lambda,lambda), (lambda,1-lambda), all entries are nonnegative by 1.1, and the four row sums are respectively 1, 1, (1-lambda)+lambda=1, and lambda+(1-lambda)=1; hence every row of A_lambda is a probability vector.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For M_lambda with rows (1-lambda,0,lambda,0) and (0,1-lambda,0,lambda), all entries are nonnegative by 1.1, and each row sum is (1-lambda)+lambda=1; hence every row of M_lambda is a probability vector.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** By the probability-row equivalence in def-positive-approximate-retract, 1.2 and 1.3 imply that A_lambda and M_lambda represent positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2), respectively.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** For every pair of integers r,s >= 1 and every real r-by-s matrix B, its induced l-infinity operator norm satisfies ||B||_{infinity->infinity}=max_{1<=i<=r} sum_{j=1}^s |B_ij|.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Let R:=max_{1<=i<=r} sum_{j=1}^s |B_ij|. For every x in R^s with ||x||_infinity<=1 and every i, |(Bx)_i|=|sum_j B_ij x_j|<=sum_j |B_ij||x_j|<=sum_j |B_ij|<=R. Hence ||Bx||_infinity<=R, and taking the supremum in the definition of the induced norm gives ||B||_{infinity->infinity}<=R.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Because r>=1 and the set of rows is finite, choose i_0 attaining R. Define x_j=1 if B_(i_0 j)>=0 and x_j=-1 if B_(i_0 j)<0. Then ||x||_infinity=1 and (Bx)_(i_0)=sum_j |B_(i_0 j)|=R, so ||B||_{infinity->infinity}>=||Bx||_infinity>=R. Together with 1.5.1 this proves the equality in 1.5.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.3

**Statement:** For avoidance of ambiguity, put R:=max_{1<=i<=r} sum_{j=1}^s |B_ij|. If ||x||_infinity<=1, then |x_j|<=1 for every j, and for each i the triangle inequality gives |(Bx)_i|=|sum_j B_ij x_j|<=sum_j |B_ij||x_j|<=sum_j |B_ij|<=R. Therefore ||Bx||_infinity<=R for every x with ||x||_infinity<=1, so the definition of the induced norm yields ||B||_{infinity->infinity}<=R. In the challenge test B=[1], x=(1), R=1, this reads 1<=1<=1<=1; the challenge arose by dropping the equals signs from the <= symbols already present in node 1.5.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.4

**Statement:** Put R:=max_{1<=i<=r} sum_{j=1}^s |B_ij|. For any x in R^s with ||x||_infinity<=1, each |x_j|<=1, so for every row i the triangle inequality gives |(Bx)_i|=|sum_j B_ij x_j|<=sum_j |B_ij||x_j|<=sum_j |B_ij|<=R. Taking the maximum over i and then the supremum over the l-infinity unit ball yields ||B||_{infinity->infinity}<=R. All comparisons are non-strict (for B=[1] and x=(1), each is equality). Conversely, because r>=1 is finite, choose i_0 attaining R and set x_j=1 when B_(i_0 j)>=0 and x_j=-1 otherwise. Since s>=1, ||x||_infinity=1, while (Bx)_(i_0)=sum_j |B_(i_0 j)|=R; hence ||B||_{infinity->infinity}>=||Bx||_infinity>=R. Thus ||B||_{infinity->infinity}=R, including the case R=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Direct row-by-column multiplication gives M_lambda A_lambda with first row (1-lambda)(1,0)+lambda(1-lambda,lambda)=(1-lambda^2,lambda^2) and second row (1-lambda)(0,1)+lambda(lambda,1-lambda)=(lambda^2,1-lambda^2).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** The first row of M_lambda is (1-lambda,0,lambda,0), so the first row of M_lambda A_lambda is (1-lambda)row_1(A_lambda)+lambda row_3(A_lambda)=(1-lambda)(1,0)+lambda(1-lambda,lambda)=(1-lambda+lambda-lambda^2,lambda^2)=(1-lambda^2,lambda^2).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.2

**Statement:** The second row of M_lambda is (0,1-lambda,0,lambda), so the second row of M_lambda A_lambda is (1-lambda)row_2(A_lambda)+lambda row_4(A_lambda)=(1-lambda)(0,1)+lambda(lambda,1-lambda)=(lambda^2,1-lambda+lambda-lambda^2)=(lambda^2,1-lambda^2). These are all rows of the 2-by-2 product, proving 1.6.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** By 1.6, M_lambda A_lambda-I_2 has rows (-lambda^2,lambda^2) and (lambda^2,-lambda^2); by the max-row formula 1.5, epsilon_lambda:=||M_lambda A_lambda-I_2||_{infinity->infinity}=max(2lambda^2,2lambda^2)=2lambda^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Since epsilon_lambda=2lambda^2 by 1.7 and the polynomial 2lambda^2 tends to 0 as real lambda tends to 0, epsilon_lambda tends to 0 as lambda tends to 0 (in particular along 0<lambda<1/2).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** Direct row-by-matrix multiplication gives P_lambda:=A_lambda M_lambda with rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda), ((1-lambda)^2,lambda(1-lambda),lambda(1-lambda),lambda^2), and (lambda(1-lambda),(1-lambda)^2,lambda^2,lambda(1-lambda)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.9.1

**Statement:** Because row_1(A_lambda)=(1,0), row_1(A_lambda M_lambda)=row_1(M_lambda)=(1-lambda,0,lambda,0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.9.2

**Statement:** Because row_2(A_lambda)=(0,1), row_2(A_lambda M_lambda)=row_2(M_lambda)=(0,1-lambda,0,lambda).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.9.3

**Statement:** Because row_3(A_lambda)=(1-lambda,lambda), row_3(A_lambda M_lambda)=(1-lambda)row_1(M_lambda)+lambda row_2(M_lambda)=((1-lambda)^2,lambda(1-lambda),lambda(1-lambda),lambda^2).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.9.4

**Statement:** Because row_4(A_lambda)=(lambda,1-lambda), row_4(A_lambda M_lambda)=lambda row_1(M_lambda)+(1-lambda)row_2(M_lambda)=(lambda(1-lambda),(1-lambda)^2,lambda^2,lambda(1-lambda)). The four computed rows are all rows of P_lambda=A_lambda M_lambda, proving 1.9.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.9.4.1

**Statement:** Write u:=row_1(M_lambda)=(1-lambda,0,lambda,0) and v:=row_2(M_lambda)=(0,1-lambda,0,lambda). By the definition of matrix multiplication and the displayed rows row_1(A_lambda)=(1,0), row_2(A_lambda)=(0,1), and row_3(A_lambda)=(1-lambda,lambda), the first three rows of A_lambda M_lambda are respectively 1*u+0*v=u=(1-lambda,0,lambda,0), 0*u+1*v=v=(0,1-lambda,0,lambda), and (1-lambda)u+lambda v=((1-lambda)^2,lambda(1-lambda),lambda(1-lambda),lambda^2).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.9.4.2

**Statement:** By the preceding computation, the first three rows have the required forms. Independently, row_4(A_lambda)=(lambda,1-lambda), so the definition of matrix multiplication gives row_4(A_lambda M_lambda)=lambda u+(1-lambda)v=(lambda(1-lambda),(1-lambda)^2,lambda^2,lambda(1-lambda)). These four calculations cover every row because A_lambda has exactly four rows; hence, with P_lambda:=A_lambda M_lambda, they establish the complete four-row list asserted in node 1.9.4 (and thus its contribution to 1.9).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.10

**Statement:** All displayed entries of P_lambda are nonnegative by 1.1; its first two row sums are 1, and each of its last two row sums is (1-lambda)^2+2lambda(1-lambda)+lambda^2=((1-lambda)+lambda)^2=1. Thus P_lambda is row-stochastic.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.11

**Statement:** Using 1.9, row_1(P_lambda)-row_3(P_lambda)=(lambda(1-lambda),-lambda(1-lambda),lambda^2,-lambda^2). By 1.1 these magnitudes sum to 2lambda(1-lambda)+2lambda^2=2lambda, so ||row_1(P_lambda)-row_3(P_lambda)||_1=2lambda.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

