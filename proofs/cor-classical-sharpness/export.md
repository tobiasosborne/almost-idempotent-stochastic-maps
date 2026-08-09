# Proof Export

## Node 1

**Statement:** Classical square-root sharpness: for every 0 < lambda < 1/2, choose positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2) supplied by lem-prh-sharpness, and put eta_lambda=2*lambda^2 and Q_lambda=A_lambda M_lambda; then Q_lambda is row-stochastic, ||Q_lambda^2-Q_lambda||_{infinity->infinity} <= eta_lambda, and every stochastic idempotent F on l-infinity(4) satisfies ||Q_lambda-F||_{infinity->infinity} >= lambda=sqrt(eta_lambda/2). Consequently, for every C>0, eta_0>0, and beta>1/2 there exist 0<eta<min{eta_0,1/4} and a row-stochastic Q on l-infinity(4) with ||Q^2-Q||_{infinity->infinity} <= eta such that every stochastic idempotent E satisfies ||Q-E||_{infinity->infinity} > C*eta^beta; equivalently, no uniform exponent beta>1/2 can replace 1/2 in op-classical.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix an arbitrary real 0 < lambda < 1/2. By the external lem-prh-sharpness, choose positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2) such that epsilon_lambda=||M_lambda A_lambda-I_2||_{infinity->infinity}=2*lambda^2 and such that its stated distance conclusion holds. Define eta_lambda:=2*lambda^2 and Q_lambda:=A_lambda M_lambda. Then eta_lambda=epsilon_lambda, and since lambda>0, lambda=sqrt(eta_lambda/2).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For the data chosen in 1.1, Q_lambda is row-stochastic and ||Q_lambda^2-Q_lambda||_{infinity->infinity}<=eta_lambda. Indeed, def-positive-approximate-retract says that the matrices of the positive unital maps A_lambda and M_lambda have probability-vector rows. Hence their product Q_lambda has nonnegative entries and row sums one, so it is row-stochastic by def-stochastic. A probability-row matrix has infinity-to-infinity operator norm one (its maximum absolute row sum is one), so ||A_lambda||=||M_lambda||=1. Matrix associativity and the identity maps on the relevant spaces give Q_lambda^2-Q_lambda=A_lambda M_lambda A_lambda M_lambda-A_lambda I_2 M_lambda=A_lambda(M_lambda A_lambda-I_2)M_lambda. Submultiplicativity, 1.1, and eta_lambda=2*lambda^2 therefore give ||Q_lambda^2-Q_lambda||<=||A_lambda|| ||M_lambda A_lambda-I_2|| ||M_lambda||=eta_lambda. This is precisely the weak defect bound in def-almost-idempotent whenever eta_lambda<1/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For the data chosen in 1.1, every stochastic idempotent F on l-infinity(4) satisfies ||Q_lambda-F||_{infinity->infinity}>=lambda=sqrt(eta_lambda/2). This is exactly the distance conclusion of the external lem-prh-sharpness, namely ||A_lambda M_lambda-F||>=lambda=sqrt(epsilon_lambda/2), after the definitional substitutions Q_lambda=A_lambda M_lambda and eta_lambda=epsilon_lambda from 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Let arbitrary C>0, eta_0>0, and beta>1/2 be given. All three numbers 1/(2*sqrt(2)), sqrt(eta_0/2), and (C*2^beta)^(-1/(2*beta-1)) are positive, so choose 0<lambda strictly below their minimum, and set eta:=eta_lambda=2*lambda^2 and Q:=Q_lambda as in 1.1. The first cutoff gives lambda<1/2 and eta<1/4; the second gives eta<eta_0; hence 0<eta<min{eta_0,1/4}. By 1.2, Q is row-stochastic and ||Q^2-Q||<=eta. Since 2*beta-1>0, the third strict cutoff implies C*2^beta*lambda^(2*beta)<lambda. By 1.3, every stochastic idempotent E satisfies ||Q-E||>=lambda, while C*eta^beta=C*(2*lambda^2)^beta=C*2^beta*lambda^(2*beta)<lambda; thus every such E satisfies ||Q-E||>C*eta^beta. Finally, a uniform replacement exponent beta>1/2 would mean that some fixed C>0 and eta_0>0 work in every dimension for every row-stochastic Q of defect at most eta<=eta_0, producing a stochastic idempotent E with ||Q-E||<=C*eta^beta. Applying the just-constructed dimension-four witness to those proposed C and eta_0 gives the literal contradiction that every E has ||Q-E||>C*eta^beta. Therefore no uniform beta>1/2 can replace 1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

