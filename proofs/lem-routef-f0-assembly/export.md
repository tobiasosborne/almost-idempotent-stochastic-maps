# Proof Export

## Node 1

**Statement:** Route F F0 assembly: there are universal eta_0,C > 0, independent of n, such that for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_0 with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= C*sqrt(eta); for the universal K and eta_K supplied by lem-routef-k-ledger, one may take eta_0 := eta_K and C := K+4*sqrt(2*K).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** By lem-routef-k-ledger there are fixed scalars K and eta_K with K >= 1 and eta_K > 0, universal and independent of n; define eta_0 := eta_K and C := K+4*sqrt(2*K). Then eta_0>0 and C>0, and both constants are universal and independent of n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** The external lemma lem-routef-k-ledger supplies fixed universal scalars K and eta_K, independent of n, amplification level, simple-block count, and block dimensions, and asserts K >= 1 and eta_K > 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Set eta_0:=eta_K and C:=K+4*sqrt(2*K). The first child gives eta_0>0. Also K>=1 implies 2*K>0, so the real principal square root sqrt(2*K) is nonnegative and C>=K>=1>0. Because eta_0 and C are fixed expressions in the universal dimension-free scalars K and eta_K, they too are universal and independent of n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix arbitrary n >= 1, row-stochastic Q: l_inf^n -> l_inf^n, and 0 <= eta <= eta_0 with ||Q^2-Q||_{infinity->infinity} <= eta, and define D,J,Q_C,Phi exactly as in the root. Since eta_0=eta_K, lem-routef-k-ledger applies and supplies a stochastic idempotent E for the same Q with ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta) = C*sqrt(eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For the arbitrary data fixed in 1.2, eta_0=eta_K turns 0 <= eta <= eta_0 into 0 <= eta <= eta_K; all remaining hypotheses and the definitions of D,J,Q_C,Phi are exactly those in lem-routef-k-ledger.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Applying lem-routef-k-ledger to those data yields, for the same Q, a stochastic idempotent E with ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta). Since C=K+4*sqrt(2*K), this is exactly ||Q-E||_{infinity->infinity} <= C*sqrt(eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

