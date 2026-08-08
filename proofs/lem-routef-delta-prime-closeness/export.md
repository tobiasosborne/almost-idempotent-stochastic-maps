# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: Delta-prime CP closeness: with C_Delta' := C_T+4*C_theta and rho_Delta' := min{rho_T, rho_prod}, for 0 <= eta <= rho_Delta', the repaired norm-one diagonal produces a CP map Delta' with ||Delta' - tilde-Delta||_cb <= C_Delta'*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix the single global W_RF and then the input-dependent datum S using lem-routef-raw-factor-setting-formation. Under 0 <= eta <= rho_Delta_prime, all radius hypotheses needed below hold: eta <= rho_T, eta <= rho_prod, eta <= rho_theta=1/8, and C_V*eta <= 1/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By lem-routef-raw-factor-setting-formation, choose its one global scalar header W_RF before the input; for the fixed admissible (H,Phi,eta), choose the resulting datum S. Thus B is a finite-dimensional unital C*-algebra, Phi is UCP, tilde-Delta=iota_{A subseteq B(H)} o v, v is an extended C_E*epsilon_AI(eta)-isomorphism, and all scalar notation is exactly (1.1)-(1.8) of def-routef-raw-factor-setting.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** By def-routef-raw-factor-setting, rho_Delta_prime=min{rho_T,rho_prod}, rho_prod=rho_T, and rho_T is at most rho_theta=1/8 and at most 1/(4*(1+C_V)). Since C_A=20+(211/8)*C_theta>0 and bar_C_E=max{1,C_E}>=1, C_V=bar_C_E*C_A>=0; hence 0<=eta<=rho_Delta_prime implies eta<=rho_T, eta<=rho_prod, eta<=1/8, and C_V*eta<=C_V/(4*(1+C_V))<=1/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For the repaired finite phase-balanced diagonal of B, tilde-Delta is involution-preserving and Phi is UCP; hence cor-kitaev-diagonal-cpization makes the map Delta_prime(X)=sum_t q_t Phi(tilde-Delta(X W_t^dagger) tilde-Delta(W_t)) completely positive.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Apply lem-kitaev-diagonal-repair to the finite-dimensional C*-algebra B from 1.1: obtain a finite phase-balanced diagonal D=sum_t q_t W_t^dagger tensor W_t with each W_t unitary, q_t>=0, sum_t q_t=1, exact centrality, pi(D)=1_B, and norm-one representation.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** The map tilde-Delta is involution-preserving. Indeed, formation gives tilde-Delta=iota o v with v an extended isomorphism; by the registered definition def-extended-delta-inclusion its level-one map is a star-algebra delta-homomorphism and therefore preserves involution. By lem-routef-ai-defect-linearization (applicable since eta<=rho_T<=rho_AI=eta_A), the involution on A is the inherited ambient adjoint, so the inclusion iota:A subseteq B(H) also preserves involution. Thus tilde-Delta(X^dagger)=tilde-Delta(X)^dagger for X in B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Now cor-kitaev-diagonal-cpization applies to the diagonal from 1.2.1, the involution-preserving tilde-Delta from 1.2.2, and the UCP map Phi from 1.1; it concludes that Delta_prime(X)=sum_t q_t Phi(tilde-Delta(X W_t^dagger) tilde-Delta(W_t)) is completely positive.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every n >= 1 and X in M_n(B), the amplified maps satisfy ||Delta_prime_n(X)-tilde-Delta_n(X)|| <= (C_T+4*C_theta)*eta*||X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Fix n>=1 and X in M_n(B). For each diagonal term set U_t=I_n tensor W_t, X_t=X U_t^dagger, Y_t=U_t, and Z_t=tilde-Delta_n(X_t) tilde-Delta_n(Y_t). Entrywise amplification of the defining finite sum gives Delta_prime_n(X)=sum_t q_t Phi_n(Z_t). Since U_t is unitary, ||X_t||=||X||, ||Y_t||=1, and X_t Y_t=X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** By lem-routef-raw-factor-norms, applicable because eta<=rho_T, ||tilde-Delta_n(X_t)|| <= (1+C_V*eta)||X|| and ||tilde-Delta_n(Y_t)|| <= 1+C_V*eta. Submultiplicativity in M_n(B(H)) and C_V*eta<=1/4 therefore give ||Z_t|| <= (1+C_V*eta)^2||X|| <= (5/4)^2||X|| <= 4||X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** By lem-routef-functional-calculus-closeness, applicable because eta<=1/8, ||Phi_n-tilde-Phi_n|| <= C_theta*eta at every n. Hence 1.3.2 yields ||Phi_n(Z_t)-tilde-Phi_n(Z_t)|| <= 4*C_theta*eta*||X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** By lem-routef-raw-product-estimate, applicable because eta<=rho_prod, and because X_t Y_t=X, one has ||tilde-Phi_n(Z_t)-tilde-Delta_n(X)|| <= C_T*eta*||X_t||*||Y_t||=C_T*eta*||X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.5

**Statement:** Since q_t>=0 and sum_t q_t=1 by lem-kitaev-diagonal-repair, subtract tilde-Delta_n(X)=sum_t q_t tilde-Delta_n(X) from the formula in 1.3.1 and use the triangle inequality with 1.3.3 and 1.3.4. This gives ||Delta_prime_n(X)-tilde-Delta_n(X)|| <= sum_t q_t*(4*C_theta+C_T)*eta*||X||=(C_T+4*C_theta)*eta*||X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Taking the supremum of the level-n operator norms in the preceding uniform estimate gives ||Delta_prime-tilde-Delta||_cb <= (C_T+4*C_theta)*eta=C_Delta_prime*eta; together with complete positivity this is the root claim.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

