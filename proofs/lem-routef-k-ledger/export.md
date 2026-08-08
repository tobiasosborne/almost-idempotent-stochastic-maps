# Proof Export

## Node 1

**Statement:** Relative Route F factorization-and-finish ledger: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K >= 1 and eta_K > 0 are universal and independent of n, amplification level, simple-block count, and block dimensions, and for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then there exist a finite-dimensional unital C*-algebra B and UCP maps Delta: B -> M_n and Upsilon: M_n -> B such that ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||, and the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** By lem-routef-scalar-header-positivity, choose one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation. Writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac,(24*K)^(-1),1} for its scalar (1.8), K is finite with K >= 1, rho_fac > 0, and eta_K > 0; these scalars are universal and independent of H, Phi, eta, n, amplification level, simple-block count, and block dimensions. Thus this single W_RF has all the global scalar properties and independence required in node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix the W_RF chosen in 1.1, and fix arbitrary n >= 1, row-stochastic Q:l_inf^n->l_inf^n, and 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, with D, J, Q_C and Phi := J Q_C D exactly as in node 1. By lem-routef-factor-map-packet there exist a finite-dimensional unital C*-algebra B, one setting datum S over this same W_RF, CP maps Delta':B->M_n and Upsilon':M_n->B, and UCP maps Delta:B->M_n and Upsilon:M_n->B, all supplied in the stated serial same-datum order.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For the same W_RF, input, and packet (B,S,Delta',Delta,Upsilon',Upsilon) fixed in 1.2, lem-routef-factor-estimate-packet gives ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and, for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||. It also gives 0 <= eta <= min{(24*K)^(-1),1}, 3*K*eta <= 1/8 < 1, and 3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6 < 1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Apply lem-routef-f2-positive-unital-compression to K,n,Q,D,J,Q_C,Phi,B,Delta,Upsilon from 1.1-1.3. Its threshold and two cb-estimate hypotheses are in 1.3, and its level-one multiplicative hypothesis is the r=1 case of the amplified estimate in 1.3. Hence B is commutative and there exist k >= 1, a unital *-isomorphism iota_C:C^k->B, and positive unital maps A:l_inf^k->l_inf^n and M:l_inf^n->l_inf^k such that ||Q-AM||_{infinity->infinity} <= K*eta, ||QA-A||_{infinity->infinity} <= 2*K*eta, and ||Ax||_infinity >= (1-3*K*eta)*||x||_infinity for every x in l_inf^k.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Since 3*K*eta <= 1/8 < 1 by 1.3, apply lem-routef-f3-retract-defect to the positive unital A,M from 1.4, using all three estimates in 1.4. It yields ||MA-I_k||_{infinity->infinity} <= 3*K*eta/(1-3*K*eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Apply lem-routef-prh-finish to the positive unital maps A,M from 1.4 and the same row-stochastic Q. Its hypotheses K >= 1, 0 <= eta <= min{(24*K)^(-1),1}, ||Q-AM||_{infinity->infinity} <= K*eta, and ||MA-I_k||_{infinity->infinity} <= 3*K*eta/(1-3*K*eta) follow respectively from 1.1, 1.3, 1.4, and 1.5. Therefore the same Q admits a stochastic idempotent E with ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

