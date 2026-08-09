# TREE-CORSHARP-ABORTED — cor-classical-sharpness run 1 BALLOON abort (2026-08-09)

Run: xhigh prover / xhigh verifiers, cap 20, max 4 rounds (ratified budget, effort raised from routine per user quota green-light).
Abort: build produced 26 live nodes > cap 20 BEFORE any verification round (build-shape balloon, the FOURTH in the sharpness family: 27/28/27/26).
Classification: NO missing byte-matched fact; honest tree size ~26 vs design cap 20. Bulk = the quantifier-discharge branch (1.4-1.5, ~10 nodes: explicit b=(C*2^beta)^(-1/(2beta-1)) arithmetic + the logical packaging of the no-beta>1/2 negation) plus the defect factorization branch (1.2.x).

```
=== Proof Status ===

1 [[33mpending[0m/[33munresolved[0m] Classical square-root sharpness: for every 0 < lambda < 1/2, choose positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2) supplied by lem-prh-sharpness, and put eta_lambda=2*lambda^2 and Q_lambda=A_lambda M_lambda; then Q_lambda is row-stochastic, ||Q_lambda^2-Q_lambda||_{infinity->infinity} <= eta_lambda, and every stochastic idempotent F on l-infinity(4) satisfies ||Q_lambda-F||_{infinity->infinity} >= lambda=sqrt(eta_lambda/2). Consequently, for every C>0, eta_0>0, and beta>1/2 there exist 0<eta<min{eta_0,1/4} and a row-stochastic Q on l-infinity(4) with ||Q^2-Q||_{infinity->infinity} <= eta such that every stochastic idempotent E satisfies ||Q-E||_{infinity->infinity} > C*eta^beta; equivalently, no uniform exponent beta>1/2 can replace 1/2 in op-classical.
  1.1 [[33mpending[0m/[33munresolved[0m] For an arbitrary real lambda with 0 < lambda < 1/2, the external lem-prh-sharpness supplies positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2) satisfying ||M_lambda A_lambda-I_2||_{infinity->infinity}=2*lambda^2 and ||A_lambda M_lambda-F||_{infinity->infinity} >= lambda for every stochastic idempotent F on l-infinity(4).
    1.1.1 [[33mpending[0m/[33munresolved[0m] This is the direct application of the registered external lem-prh-sharpness at the given lambda: it gives exactly these positive unital A_lambda and M_lambda, the equality ||M_lambda A_lambda-I_2||_{infinity->infinity}=2*lambda^2, and the stated lower bound against every stochastic idempotent F.
  1.2 [[33mpending[0m/[33munresolved[0m] For the maps in 1.1, define eta_lambda=2*lambda^2 and Q_lambda=A_lambda M_lambda. Then Q_lambda is row-stochastic and ||Q_lambda^2-Q_lambda||_{infinity->infinity} <= eta_lambda.
    1.2.1 [[33mpending[0m/[33munresolved[0m] By def-positive-approximate-retract, positive unital maps between the finite l-infinity spaces have probability-vector rows. Thus the matrix product Q_lambda=A_lambda M_lambda is entrywise nonnegative and each of its row sums is one, so Q_lambda is row-stochastic by def-stochastic.
    1.2.2 [[33mpending[0m/[33munresolved[0m] Associativity and distributivity of composition give Q_lambda^2-Q_lambda=A_lambda M_lambda A_lambda M_lambda-A_lambda M_lambda=A_lambda(M_lambda A_lambda-I_2)M_lambda.
    1.2.3 [[33mpending[0m/[33munresolved[0m] A matrix with probability-vector rows has infinity-to-infinity operator norm equal to one. Hence ||A_lambda||_{infinity->infinity}=||M_lambda||_{infinity->infinity}=1, and submultiplicativity together with 1.1 and 1.2.2 gives ||Q_lambda^2-Q_lambda||_{infinity->infinity} <= 1*(2*lambda^2)*1=eta_lambda.
      1.2.3.1 [[33mpending[0m/[33munresolved[0m] For any matrix T with probability-vector rows, the infinity-to-infinity norm is the maximum absolute row sum, hence ||T||_{infinity->infinity}=1. Therefore ||A_lambda||=||M_lambda||=1; applying submultiplicativity to the identity in node 1.2.2 and the defect equality in node 1.1 yields ||Q_lambda^2-Q_lambda|| <= ||A_lambda||*||M_lambda A_lambda-I_2||*||M_lambda||=2*lambda^2=eta_lambda.
  1.3 [[33mpending[0m/[33munresolved[0m] For every stochastic idempotent F on l-infinity(4), the same Q_lambda satisfies ||Q_lambda-F||_{infinity->infinity} >= lambda=sqrt(eta_lambda/2).
    1.3.1 [[33mpending[0m/[33munresolved[0m] Because Q_lambda=A_lambda M_lambda, the lower bound in the registered external lem-prh-sharpness says directly that ||Q_lambda-F||_{infinity->infinity} >= lambda for every stochastic idempotent F on l-infinity(4).
    1.3.2 [[33mpending[0m/[33munresolved[0m] Since eta_lambda=2*lambda^2 and lambda>0, eta_lambda/2=lambda^2 and therefore sqrt(eta_lambda/2)=lambda.
  1.4 [[33mpending[0m/[33munresolved[0m] For every C>0, eta_0>0, and beta>1/2, one can choose 0<lambda<1/2 so that eta=2*lambda^2 lies in (0,min{eta_0,1/4}) and C*eta^beta<lambda; with Q=Q_lambda, 1.2 and 1.3 then give the counterexample asserted in the consequence of node 1.
    1.4.1 [[33mpending[0m/[33munresolved[0m] Let b=(C*2^beta)^(-1/(2*beta-1)) and m=min{1/(2*sqrt(2)),sqrt(eta_0/2),b}. Because C>0, eta_0>0, and 2*beta-1>0, all three entries are positive; hence m>0, and lambda=m/2 satisfies 0<lambda<m<1/2.
    1.4.2 [[33mpending[0m/[33munresolved[0m] For the lambda chosen in 1.4.1 and eta=2*lambda^2, one has 0<eta<eta_0 and eta<1/4; moreover C*eta^beta=C*2^beta*lambda^(2*beta)<lambda.
      1.4.2.1 [[33mpending[0m/[33munresolved[0m] Because lambda>0 and eta=2*lambda^2, one has eta>0.
      1.4.2.2 [[33mpending[0m/[33munresolved[0m] The inequalities lambda<sqrt(eta_0/2) and lambda<1/(2*sqrt(2)) imply eta=2*lambda^2<eta_0 and eta<1/4, respectively.
      1.4.2.3 [[33mpending[0m/[33munresolved[0m] Put r=2*beta-1>0. Since lambda<b=(C*2^beta)^(-1/r), monotonicity of positive real powers gives lambda^r<(C*2^beta)^(-1); multiplying by the positive number C*2^beta*lambda yields C*2^beta*lambda^(2*beta)<lambda, i.e. C*eta^beta<lambda.
    1.4.3 [[33mpending[0m/[33munresolved[0m] At this chosen lambda, lem-prh-sharpness and the permitted definitions produce a row-stochastic Q=Q_lambda on l-infinity(4) with ||Q^2-Q||_{infinity->infinity} <= eta and ||Q-E||_{infinity->infinity} >= lambda > C*eta^beta for every stochastic idempotent E.
      1.4.3.1 [[33mpending[0m/[33munresolved[0m] Apply the registered external lem-prh-sharpness at this 0<lambda<1/2 to obtain positive unital A_lambda and M_lambda with ||M_lambda A_lambda-I_2||_{infinity->infinity}=2*lambda^2 and ||A_lambda M_lambda-E||_{infinity->infinity} >= lambda for every stochastic idempotent E.
      1.4.3.2 [[33mpending[0m/[33munresolved[0m] Set Q=A_lambda M_lambda. By def-positive-approximate-retract its factors have probability-vector rows, so Q is row-stochastic by def-stochastic; also Q^2-Q=A_lambda(M_lambda A_lambda-I_2)M_lambda and both factor norms are one, whence ||Q^2-Q||_{infinity->infinity} <= 2*lambda^2=eta.
      1.4.3.3 [[33mpending[0m/[33munresolved[0m] For the same Q, the imported lower bound gives ||Q-E||_{infinity->infinity} >= lambda for every stochastic idempotent E, and the strict scalar inequality from 1.4.2 gives lambda>C*eta^beta.
        1.4.3.3.1 [[33mpending[0m/[33munresolved[0m] By node 1.4.3.1 and Q=A_lambda M_lambda, every stochastic idempotent E satisfies ||Q-E||_{infinity->infinity}>=lambda; by node 1.4.2, lambda>C*eta^beta. Transitivity gives ||Q-E||_{infinity->infinity}>C*eta^beta for every such E.
  1.5 [[33mpending[0m/[33munresolved[0m] The quantified counterexamples in 1.4 are logically equivalent to the statement that no uniform exponent beta>1/2, with dimension-independent constants C and eta_0, can replace exponent 1/2 in op-classical.
    1.5.1 [[33mpending[0m/[33munresolved[0m] For fixed beta>1/2, a uniform replacement exponent assertion would mean that there exist C>0 and eta_0>0 such that, for every eta with 0<eta<min{eta_0,1/4} and every row-stochastic Q with ||Q^2-Q||_{infinity->infinity} <= eta, there exists a stochastic idempotent E with ||Q-E||_{infinity->infinity} <= C*eta^beta.
    1.5.2 [[33mpending[0m/[33munresolved[0m] For each beta>1/2 and every proposed C>0 and eta_0>0, node 1.4 supplies an eta<min{eta_0,1/4} and a row-stochastic Q of defect at most eta for which every stochastic idempotent E instead has ||Q-E||_{infinity->infinity}>C*eta^beta. This is exactly the logical negation of 1.5.1, proving the equivalence.
      1.5.2.1 [[33mpending[0m/[33munresolved[0m] Fix beta>1/2 and any proposed constants C>0 and eta_0>0 from node 1.5.1. Node 1.4 gives an admissible eta and row-stochastic Q for which all stochastic idempotents E satisfy the strict reverse inequality ||Q-E||>C*eta^beta, contradicting the existential E required by node 1.5.1. Since C and eta_0 were arbitrary, no such uniform constants exist.

--- Statistics ---
Nodes: 26 total
  Epistemic: 0 [34mdraft[0m, 26 [33mpending[0m, 0 [32mvalidated[0m, 0 [36madmitted[0m, 0 [31mrefuted[0m, 0 [90marchived[0m, 0 [35mneeds_refinement[0m
  Taint: 0 [32mclean[0m, 0 [36mself_admitted[0m, 0 [31mtainted[0m, 26 [33munresolved[0m

--- Jobs ---
  Prover: 26 nodes awaiting refinement
  Verifier: 0 nodes ready for review

--- Legend ---
Epistemic States:
  [34mdraft[0m      - Work in progress (not submitted)
  [33mpending[0m    - Awaiting proof/verification
  [32mvalidated[0m  - Verified by adversarial verifier
  [36madmitted[0m   - Accepted without full verification
  [31mrefuted[0m    - Proven false
  [90marchived[0m   - Superseded or abandoned
  [35mneeds_refinement[0m - Reopened for further refinement

Taint States:
  [32mclean[0m         - No epistemic uncertainty
  [36mself_admitted[0m - Contains admitted node
  [31mtainted[0m       - Depends on tainted/refuted node
  [33munresolved[0m    - Taint status not yet computed
```
