# Proof Export

## Node 1

**Statement:** Route F raw-factor setting formation: there exists one choice W_RF of the scalar header of def-routef-raw-factor-setting, independent of H, Phi, eta, dimension, amplification level, and block data, with C_theta=12*(sqrt(2)-1), C_A=20+(211/8)*C_theta, eta_A>0 and (C_A,eta_A) the fixed witnesses of lem-routef-ai-defect-linearization, C_E<infinity and epsilon_E>0 the fixed witnesses of lem-thmainext-conditional, rho_theta:=1/8, rho_AI:=eta_A, and all remaining named scalar quantities defined by (1.1)-(1.8), such that for every nonzero finite-dimensional Hilbert space H, every UCP map Phi:B(H)->B(H), and every eta with 0 <= eta <= rho_id^corr and ||Phi^2-Phi||_cb <= eta, there exist a finite-dimensional unital C*-algebra B, an extended C_E*epsilon_AI(eta)-isomorphism v:B->A, and a def-routef-raw-factor-setting datum S over this same W_RF whose fields are the displayed H,Phi,eta,B,v,u=v^(-1) and the canonical tilde-Phi,A,star,epsilon_AI(eta),tilde-Delta,tilde-Upsilon notation, with tilde-Phi^2=tilde-Phi, A an extended epsilon_AI(eta)-C*-algebra, and 0 <= epsilon_AI(eta) <= C_A*eta <= epsilon_E.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Global-witness selection. Invoke lem-routef-ai-defect-linearization once to fix universal eta_A>0 and C_A=20+(211/8)*C_theta<infinity with C_theta=12*(sqrt(2)-1), and invoke lem-thmainext-conditional once to fix universal C_E<infinity and epsilon_E>0. These choices precede and are independent of H, Phi, eta, dimension, amplification level, and block data.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Scalar-header assembly. Using the fixed eta_A,C_A,C_E,epsilon_E, take W_RF to have precisely these four receiving fields; set C_theta=12*(sqrt(2)-1), rho_theta=1/8, rho_AI=eta_A, and define every remaining named scalar in the displayed order (1.1)-(1.8) of def-routef-raw-factor-setting. These formulas are well-defined because C_A=20+(211/8)*12*(sqrt(2)-1)>0, eta_A>0, epsilon_E>0, and bar C_E=max{1,C_E}>=1, so every displayed reciprocal has a positive denominator. Thus this single W_RF is universal and input-independent.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Radius extraction. Fix an arbitrary nonzero finite-dimensional H, UCP Phi:B(H)->B(H), and eta with 0<=eta<=rho_id^corr and ||Phi^2-Phi||_cb<=eta. From rho_id^corr=min{rho_theta,rho_AI,epsilon_E/C_A}, rho_theta=1/8, and rho_AI=eta_A, obtain eta<=1/8<1/4, eta<=eta_A, and C_A*eta<=epsilon_E; the last implication uses C_A>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Kitaev application. For an arbitrary input in the root domain, eta<=rho_id^corr<=rho_theta=1/8<1/4, while ||Phi^2-Phi||_cb<=eta is assumed. Therefore lem-kitaev-almost-idemp-audit applies to the canonical tilde-Phi=(1/2)(I+(2Phi-I)(I-4(Phi-Phi^2))^(-1/2)), A=Im(tilde-Phi), and X star Y=tilde-Phi(XY), and yields tilde-Phi^2=tilde-Phi.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Approximate-algebra application. For an arbitrary input in the root domain, rho_id^corr<=rho_AI=eta_A gives 0<=eta<=eta_A, so lem-routef-ai-defect-linearization applies to the same canonical tilde-Phi,A,star and gives the extended epsilon_AI(eta)-C*-algebra structure and epsilon_AI(eta)<=C_A*eta. Also rho_id^corr<=1/8 makes 1-4eta lie in [1/2,1], hence r=(3/2)((1-4eta)^(-1/2)-1)>=0 and epsilon_AI(eta), being a maximum containing r, is nonnegative. Finally rho_id^corr<=epsilon_E/C_A and C_A=20+(211/8)*12*(sqrt(2)-1)>0 give C_A*eta<=epsilon_E. Thus 0<=epsilon_AI(eta)<=C_A*eta<=epsilon_E.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Finite-dimensional-range step. Since H is finite-dimensional, B(H) is finite-dimensional, and therefore its linear subspace A=Im(tilde-Phi) is finite-dimensional. The extended epsilon_AI(eta)-C*-algebra structure on this very same A is the one supplied by lem-routef-ai-defect-linearization.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Conditional structure-theorem application. If the canonical A is finite-dimensional, carries the extended epsilon_AI(eta)-C*-algebra structure, and satisfies 0<=epsilon_AI(eta)<=epsilon_E, then lem-thmainext-conditional applied with epsilon=epsilon_AI(eta) supplies a finite-dimensional C*-algebra B and one extended C_E*epsilon_AI(eta)-isomorphism v:B->A. Every finite-dimensional C*-algebra is unital, so B has the required finite-dimensional unital C*-algebra type.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Same-output packaging, as a pure conditional construction. Suppose the fixed header W_RF, an input H,Phi,eta, the canonical tilde-Phi,A,star,r,epsilon_AI(eta), a finite-dimensional unital C*-algebra B, an extended C_E*epsilon_AI(eta)-isomorphism v:B->A, and the asserted idempotence, approximate-algebra, and scalar-bound conclusions have been obtained. By def-extended-delta-inclusion, v is bijective, so define u=v^(-1):A->B. Then def-routef-raw-factor-setting permits one datum S over that same W_RF with exactly these fields and with tilde-Delta=iota_{A subseteq B(H)} composed with v and tilde-Upsilon=u composed with tilde-Phi. These maps have the required types, no field is reselected, and no analytic conclusion is inferred from the data definition.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** Quantifier and universality closure, as a logical implication. If eta_A,C_A,C_E,epsilon_E and hence W_RF are chosen once independently of all inputs, and if for an arbitrary H,Phi,eta in the root domain the input-dependent B,v,u,S and all displayed conclusions are obtained, then universal generalization over H,Phi,eta followed by existential introduction of the single fixed W_RF and the input-dependent B,v,S gives exactly the quantifier order and independence assertions of root node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

