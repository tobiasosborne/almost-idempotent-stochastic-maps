# Proof Export

## Node 1

**Statement:** PRH square-root sharpness: for every 0 < lambda < 1/2 there are positive unital maps A:l-infinity(2)->l-infinity(4) and M:l-infinity(4)->l-infinity(2) with epsilon_lambda=||MA-I_2||_{infinity->infinity}=2*lambda^2 tending to 0 such that every stochastic idempotent F on l-infinity(4) satisfies ||AM-F||_{infinity->infinity} >= lambda=sqrt(epsilon_lambda/2); hence the sqrt(epsilon) order in PRH is intrinsically sharp.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** For each real lambda with 0 < lambda < 1/2, take the explicit matrices A_lambda and M_lambda from lem-prh-sharpness-family-arithmetic. They are positive unital maps of the required types, epsilon_lambda=||M_lambda A_lambda-I_2||_{infinity->infinity}=2*lambda^2 tends to 0, and P_lambda=A_lambda M_lambda has the stated rows with ||row_1(P_lambda)-row_3(P_lambda)||_1=2*lambda.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By lem-prh-sharpness-family-arithmetic, for 0 < lambda < 1/2 the matrix A_lambda with rows (1,0), (0,1), (1-lambda,lambda), (lambda,1-lambda) and the matrix M_lambda with rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda) have nonnegative entries and probability-vector rows; hence they represent positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** By lem-prh-sharpness-family-arithmetic, M_lambda A_lambda has rows (1-lambda^2,lambda^2) and (lambda^2,1-lambda^2); using its induced l-infinity norm formula gives epsilon_lambda=||M_lambda A_lambda-I_2||_{infinity->infinity}=2*lambda^2, and this tends to 0 as lambda tends to 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** By lem-prh-sharpness-family-arithmetic, P_lambda=A_lambda M_lambda is row-stochastic with rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda), ((1-lambda)^2,lambda*(1-lambda),lambda*(1-lambda),lambda^2), and (lambda*(1-lambda),(1-lambda)^2,lambda^2,lambda*(1-lambda)), and ||row_1(P_lambda)-row_3(P_lambda)||_1=2*lambda.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For each real lambda with 0 < lambda < 1/2, for the explicit A_lambda,M_lambda and P_lambda=A_lambda M_lambda of lem-prh-sharpness-family-arithmetic, every 4-by-4 stochastic idempotent F satisfies ||P_lambda-F||_{infinity->infinity} >= lambda.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Let 0 < lambda < 1/2 and let F=(f_ab) be a 4-by-4 stochastic idempotent with ||P_lambda-F||_{infinity->infinity}<lambda. The norm formula and row_1(P_lambda)=(1-lambda,0,lambda,0) from lem-prh-sharpness-family-arithmetic give |f_11-(1-lambda)|<lambda and |f_13-lambda|<lambda. Therefore f_11>1-2*lambda>0 and f_13>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For any 4-by-4 stochastic idempotent F=(f_ab), if f_11>0 and f_13>0, then lem-prh-sharpness-row-coincidence applied with i=1 and j=3 gives row_1(F)=row_3(F).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Let 0 < lambda < 1/2 and let F be a 4-by-4 matrix. If ||P_lambda-F||_{infinity->infinity}<lambda and row_1(F)=row_3(F), then the norm formula from lem-prh-sharpness-family-arithmetic gives ||row_1(P_lambda)-row_1(F)||_1<lambda and ||row_3(F)-row_3(P_lambda)||_1<lambda. The l1 triangle inequality then gives ||row_1(P_lambda)-row_3(P_lambda)||_1<2*lambda, contradicting the equality ||row_1(P_lambda)-row_3(P_lambda)||_1=2*lambda from lem-prh-sharpness-family-arithmetic.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Scalar sharpness conclusion: if epsilon_lambda=2*lambda^2 tends to 0 and every stochastic-idempotent approximation to P_lambda has error at least lambda, then lambda=sqrt(epsilon_lambda/2), so the family has a fixed positive multiple of sqrt(epsilon_lambda) as an unavoidable error and no uniformly better exponent beta>1/2 is possible.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For lambda>0 and epsilon_lambda=2*lambda^2, epsilon_lambda/2=lambda^2 and the nonnegative square root is lambda; equivalently lambda=(1/sqrt(2))*sqrt(epsilon_lambda).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** If epsilon_lambda tends to 0 and every stochastic-idempotent approximation error is at least (1/sqrt(2))*sqrt(epsilon_lambda), then for every beta>1/2 and every fixed C>0 the ratio of this lower bound to C*epsilon_lambda^beta is (1/(C*sqrt(2)))*epsilon_lambda^(1/2-beta), which tends to infinity. Thus no uniform O(epsilon^beta) bound with beta>1/2 can hold on this family, establishing intrinsic square-root-order sharpness.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

