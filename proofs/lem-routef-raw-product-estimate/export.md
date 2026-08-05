# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result; for every integer n >= 1 and all X, Y in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Raw tilde-Delta-product estimate: for 0 <= eta <= rho_prod := rho_T, every amplification and all X, Y satisfy ||tilde-Phi_n(tilde-Delta_n X tilde-Delta_n Y) - tilde-Delta_n(XY)|| <= C_T*eta*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix the global W_RF and arbitrary formation-admissible (H,Phi,eta), its supplied datum S, n>=1, and X,Y in M_n(S.B), with 0<=eta<=rho_prod=rho_T. Put d:=C_E*epsilon_AI(eta). By lem-routef-raw-factor-setting-formation, v:S.B->A is an extended d-isomorphism and 0<=epsilon_AI(eta)<=C_A*eta. By def-routef-raw-factor-setting, tilde-Delta is the inclusion of A into B(H) composed with v, while the multiplication on A is a star b:=tilde-Phi(ab); hence tilde-Delta_n(Z) is v_n(Z) viewed in M_n(B(H)) for every Z in M_n(S.B).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For the arbitrary data of the root and d:=C_E*epsilon_AI(eta), the extended d-isomorphism assertion for v from lem-routef-raw-factor-setting-formation and def-extended-delta-inclusion imply that v_n is a d-homomorphism. Its product-defect clause is ||v_n(XY)-v_n(X) star_n v_n(Y)||<=d*||X||*||Y||. Entrywise matrix multiplication, linearity of tilde-Phi, and def-routef-raw-factor-setting give v_n(X) star_n v_n(Y)=tilde-Phi_n(tilde-Delta_n X tilde-Delta_n Y) and v_n(XY)=tilde-Delta_n(XY). Therefore ||tilde-Phi_n(tilde-Delta_n X tilde-Delta_n Y)-tilde-Delta_n(XY)||<=d*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Put d:=C_E*epsilon_AI(eta). The formation result says that v:B->A is an extended d-isomorphism. Hence it is an extended d-inclusion, and def-extended-delta-inclusion gives, for the fixed n, that v_n=id_{M_n} tensor v is a d-homomorphism from M_n(B) to M_n(A), where the target multiplication is the amplification star_n of star. The newly provisioned byte-verbatim external GT-kitaev-def-delta-homomorphism supplies the previously missing multiplication clause, so ||v_n(XY)-v_n(X) star_n v_n(Y)|| <= d*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Under the inclusion A subseteq B(H), def-routef-raw-factor-setting gives v_n(XY)=tilde-Delta_n(XY). Moreover, for every i,j, [v_n(X) star_n v_n(Y)]_{ij}=sum_k(v(X_ik) star v(Y_kj))=sum_k tilde-Phi(v(X_ik)v(Y_kj))=tilde-Phi(sum_k tilde-Delta(X_ik)tilde-Delta(Y_kj))=[tilde-Phi_n(tilde-Delta_n(X)tilde-Delta_n(Y))]_{ij}, using the definition a star b:=tilde-Phi(ab), ordinary matrix multiplication, and linearity of tilde-Phi. The operator-space norms on A are inherited from B(H), so the inequality of the preceding child, together with ||Z||=||-Z||, is exactly ||tilde-Phi_n(tilde-Delta_n X tilde-Delta_n Y)-tilde-Delta_n(XY)|| <= d*||X||*||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The scalar header in def-routef-raw-factor-setting has bar_C_E=max{1,C_E}, C_V=bar_C_E*C_A, and C_T=C_theta+3*C_V, with C_theta=12*(sqrt(2)-1). The formation result gives 0<=epsilon_AI(eta)<=C_A*eta and d=C_E*epsilon_AI(eta); since C_E is the nonnegative defect coefficient of the extended isomorphism, d<=bar_C_E*C_A*eta=C_V*eta. Also bar_C_E>=1, C_A=20+(211/8)*C_theta>0, and C_theta>0, so C_V>=0 and C_T=C_theta+3*C_V>=C_V. Thus d<=C_T*eta. Combining this scalar bound with the multiplication-defect estimate proves the root inequality for all the arbitrary choices, with rho_prod=rho_T as defined.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

