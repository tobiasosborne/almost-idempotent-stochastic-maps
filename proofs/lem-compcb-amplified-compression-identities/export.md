# Proof Export

## Node 1

**Statement:** Amplified compression identities: there is a universal e_cmp > 0 such that, whenever A is an extended epsilon-C*-algebra, e=delta+epsilon <= e_cmp, P,Q are delta-projections in A, n >= 1, and X is in M_n tensor A, one has Co_{P_n,Q_n}^2=Co_{P_n,Q_n} and Co_{P_n,Q_n}(X)^dagger=Co_{Q_n,P_n}(X^dagger), where P_n=I_n tensor P and Q_n=I_n tensor Q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Threshold and amplification identification: let e_cmp>0 be the universal constant supplied by lem-compcb-amplified-compression. If e=delta+epsilon<=e_cmp, P,Q are delta-projections in the extended epsilon-C*-algebra A, and n>=1, then with P_n=I_n tensor P and Q_n=I_n tensor Q one has Co_{P_n,Q_n}=1_{M_n} tensor Co_{P,Q}; applying the same cited lemma to the ordered pair (Q,P) also gives Co_{Q_n,P_n}=1_{M_n} tensor Co_{Q,P}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Level-one exact identities: for the compression maps T=Co_{P,Q} and U=Co_{Q,P}, def-compressed-corner gives T^2=T and T(x)^dagger=U(x^dagger) for every x in A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Entrywise amplification transfer: if linear maps T,U on a self-adjoint operator space satisfy T^2=T and T(x)^dagger=U(x^dagger) for every x, then for every n>=1 their canonical amplifications T_n=1_{M_n} tensor T and U_n=1_{M_n} tensor U satisfy T_n^2=T_n and T_n(X)^dagger=U_n(X^dagger) for every X in M_n tensor A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Amplified idempotence entrywise: for X=[x_ij] in M_n tensor A, the definition of the canonical amplification gives (T_n^2 X)_ij=T(T(x_ij))=(T^2)(x_ij)=T(x_ij)=(T_n X)_ij; hence T_n^2=T_n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Amplified adjoint symmetry entrywise: for X=[x_ij] in M_n tensor A, matrix involution and canonical amplification give (T_n(X)^dagger)_ij=T(x_ji)^dagger=U(x_ji^dagger), while (U_n(X^dagger))_ij=U((X^dagger)_ij)=U(x_ji^dagger); hence T_n(X)^dagger=U_n(X^dagger).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Contract reconciliation and final discharge: the current registry contract in argument/lemmas/lem-compcb-amplified-compression-identities.md is exactly the present node-1 statement, including that A is an extended epsilon-C*-algebra and P,Q are delta-projections in A. Hence child 1.1 uses no hypothesis absent from the advertised contract. For the universal e_cmp supplied there, 1.1 identifies Co_{P_n,Q_n} and Co_{Q_n,P_n} with the respective canonical amplifications; 1.2 gives level-one idempotence and adjoint symmetry; and 1.3 transfers those two identities to every n and X. Therefore children 1.1--1.3 prove node 1 as presently registered, and there is no remaining contract drift.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

