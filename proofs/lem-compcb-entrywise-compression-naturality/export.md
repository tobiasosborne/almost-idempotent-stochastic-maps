# Proof Export

## Node 1

**Statement:** Entrywise compression naturality: there is a universal e_nat > 0 such that, whenever e = delta+epsilon <= e_nat, Q is a delta-projection in an extended epsilon-C*-algebra A, n >= 1, and E_{11} is the (1,1) matrix unit of M_n, every Z in A satisfies Co_{I_n tensor Q, I_n tensor Q}(E_{11} tensor Z) = E_{11} tensor Co_Q(Z).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** By lem-compcb-amplified-compression, there is a universal e_cmp > 0 such that, for every e=delta+epsilon <= e_cmp, every pair of delta-projections P,Q in an extended epsilon-C*-algebra A, and every n >= 1, the equality of linear maps Co_{I_n tensor P,I_n tensor Q}=1_{M_n} tensor Co_{P,Q} holds on M_n(A).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Let e_cmp>0 be the universal constant supplied by lem-compcb-amplified-compression and set e_nat:=e_cmp. If e=delta+epsilon <= e_nat, Q is a delta-projection in an extended epsilon-C*-algebra A, and n>=1, then specializing that external result to the pair (P,Q)=(Q,Q) gives Co_{I_n tensor Q,I_n tensor Q}=1_{M_n} tensor Co_{Q,Q}=1_{M_n} tensor Co_Q as linear maps on M_n(A); the last equality is exactly the abbreviation Co_{Q,Q}=Co_Q in def-compressed-corner.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every linear map T:A->A, the tensor-product amplification 1_{M_n} tensor T acts on elementary tensors by (1_{M_n} tensor T)(X tensor Z)=X tensor T(Z). Hence, for T=Co_Q and X=E_{11}, (1_{M_n} tensor Co_Q)(E_{11} tensor Z)=E_{11} tensor Co_Q(Z).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

