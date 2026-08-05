# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result; for every integer n >= 1 and every X in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Raw factor-map norms: with C_V, C_T, rho_T from (1.1), for 0 <= eta <= rho_T, every amplification satisfies (1-C_V*eta)*||X|| <= ||tilde-Delta_n X|| <= (1+C_V*eta)*||X|| and max{||tilde-Delta||_cb, ||tilde-Upsilon||_cb} <= 1+C_T*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Factor branch: in the ambient finite-dimensional raw-factor setup, let A=Im(tilde-Phi), let v:B->A be the extended isomorphism furnished below, and define tilde-Delta=v (with codomain included in B(H)); then for every n and X, (1-C_V*eta)||X|| <= ||tilde-Delta_n X|| <= (1+C_V*eta)||X||, hence ||tilde-Delta||_cb <= 1+C_V*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Radius and domain: (1.1) defines bar-C_E=max{1,C_E}, C_V=bar-C_E*C_A and rho_T as a minimum containing rho_AI and epsilon_E/C_A. Thus 0<=eta<=rho_T implies eta<=rho_AI and, by lem-routef-ai-defect-linearization, epsilon_AI(eta)<=C_A*eta<=epsilon_E. In the ambient finite-dimensional setup A=Im(tilde-Phi) is finite-dimensional.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.1

**Statement:** Universal-context unpacking, not an added premise: root node 1 fixes W_RF supplied by lem-routef-raw-factor-setting-formation and then fixes an arbitrary input (H,Phi,eta) to which that result applies and a datum S supplied by it. Hence the quantified domain and conclusion of lem-routef-raw-factor-setting-formation give that H is nonzero and finite-dimensional, Phi:B(H)->B(H) is UCP, 0<=eta<=rho_id^corr, ||Phi^2-Phi||_cb<=eta, S.tilde-Phi is the displayed functional-calculus map, and S.A=Im(S.tilde-Phi). In particular, no literal identification H=C^d is assumed or needed.

**Type:** local_assume

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.1.1.1

**Statement:** The amended binding prefix of root node 1 universally fixes precisely a W_RF, an input (H,Phi,eta) in the domain of lem-routef-raw-factor-setting-formation, and a supplied setting datum S. Universally instantiate that validated external at this input: its hypotheses/domain give H nonzero finite-dimensional, Phi UCP, 0<=eta<=rho_id^corr, and ||Phi^2-Phi||_cb<=eta, while its conclusion says that the fields of S include the canonical functional-calculus tilde-Phi and A=Im(tilde-Phi). Thus every fact asserted in node 1.1.1.1 is inherited from the amended root and the allowed external; none is introduced as a new hypothesis.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.1.1.1.1

**Statement:** Instantiate lem-routef-raw-factor-setting-formation at the global W_RF and the arbitrary input (H,Phi,eta) fixed in root node 1, and select the datum S that root node 1 fixes from its existential conclusion. The external's domain supplies: H is nonzero finite-dimensional, Phi is UCP, 0<=eta<=rho_id^corr, and ||Phi^2-Phi||_cb<=eta. Its conclusion identifies the selected datum's tilde-Phi with the canonical functional-calculus formula and its A with Im(tilde-Phi).

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

##### Node 1.1.1.2

**Statement:** Equation (1.1) uses rho_AI:=eta_A and defines rho_T as a minimum containing rho_AI and epsilon_E/C_A. Hence 0<=eta<=rho_T gives 0<=eta<=eta_A and C_A*eta<=epsilon_E. Applying lem-routef-ai-defect-linearization to the nonzero H, UCP Phi, and cb-defect bound fixed in 1.1.1.1 yields epsilon_AI(eta)<=C_A*eta<=epsilon_E (and supplies the extended epsilon_AI(eta)-C*-algebra structure used by sibling 1.1.2).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.3

**Statement:** Because H=C^d with d<infinity, B(H) has finite dimension d^2. The range A=Im(tilde-Phi) of the linear map tilde-Phi:B(H)->B(H) is a linear subspace of B(H), so dim(A)<=d^2 and A is finite-dimensional.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.4

**Statement:** Correction superseding the strict inequality in node 1.1.1.3: let d=dim_C(H), which is a finite positive integer by 1.1.1.1. Then dim_C(B(H))=d^2. Since tilde-Phi:B(H)->B(H) is linear and A=Im(tilde-Phi), the rank bound for a linear map gives dim_C(A)=rank(tilde-Phi)<=dim_C(B(H))=d^2<infinity. Equality can occur (for example tilde-Phi=I), so no strict inequality is asserted or needed. Therefore A is finite-dimensional.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** By lem-routef-ai-defect-linearization, A=Im(tilde-Phi), with its inherited operator-space structure, is an extended epsilon_AI(eta)-C*-algebra. By lem-thmainext-conditional there are a finite-dimensional C*-algebra B and an extended delta-isomorphism v:B->A with delta=C_E*epsilon_AI(eta); moreover delta<=C_E*C_A*eta<=bar-C_E*C_A*eta=C_V*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** By def-extended-delta-inclusion, every amplification v_n of the extended delta-isomorphism satisfies (1-delta)||X||<=||v_nX||<=(1+delta)||X||. Since 0<=delta<=C_V*eta, these bounds imply (1-C_V*eta)||X||<=||v_nX||<=(1+C_V*eta)||X||. Under the raw-factor definition tilde-Delta=v (followed by the isometric inclusion A subset B(H)); hence these are the claimed amplification bounds, and their upper half gives ||tilde-Delta||_cb<=1+C_V*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Inverse-composition branch: with tilde-Upsilon:=v^(-1) tilde-Phi, one has ||tilde-Upsilon||_cb <= (1+C_theta*eta)/(1-C_V*eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** A UCP map is completely contractive: for every n put Psi=id_{M_n} tensor Phi. Complete positivity makes id_{M_2} tensor Psi positive; applying it to the positive block matrix [[X^*X,X^*],[X,I]] and taking the Schur complement gives Psi(X)^*Psi(X)<=Psi(X^*X). Positivity and unitality give 0<=Psi(X^*X)<=||X||^2 I, hence ||Psi(X)||<=||X||. Therefore ||Phi||_cb<=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Since rho_T<=rho_theta, lem-routef-functional-calculus-closeness applies and gives ||tilde-Phi-Phi||_cb<=C_theta*eta. The preceding complete contractivity and the triangle inequality yield ||tilde-Phi||_cb<=1+C_theta*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** In the notation feeding (1.1), rho_theta=1/8, while rho_T is a minimum containing rho_theta; hence eta<=rho_T implies 0<=eta<=1/8. Therefore lem-routef-functional-calculus-closeness gives ||tilde-Phi-Phi||_cb<=C_theta*eta. Node 1.2.1 gives ||Phi||_cb<=1, so the cb-norm triangle inequality yields ||tilde-Phi||_cb<=||Phi||_cb+||tilde-Phi-Phi||_cb<=1+C_theta*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Reapplying the extended-isomorphism estimate from lem-routef-ai-defect-linearization, lem-thmainext-conditional, and def-extended-delta-inclusion gives ||v_nX||>=(1-C_V*eta)||X|| for every n. Because (1.1) gives C_V*eta<=1/4, v_n is bijective and ||v_n^(-1)||<=1/(1-C_V*eta). Thus tilde-Upsilon_n=v_n^(-1) tilde-Phi_n has norm at most (1+C_theta*eta)/(1-C_V*eta), uniformly in n; taking the supremum gives the stated cb bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** The map v supplied by lem-thmainext-conditional is an extended isomorphism, so v is bijective and every amplification v_n=id_{M_n} tensor v is bijective with inverse id_{M_n} tensor v^(-1). The extended-inclusion lower bound, enlarged as in the factor branch, is ||v_nX||>=(1-C_V*eta)||X||. Since (1.1) gives C_V*eta<=1/4, it follows that ||v_n^(-1)||<=1/(1-C_V*eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.2

**Statement:** By definition tilde-Upsilon=v^(-1) tilde-Phi, hence tilde-Upsilon_n=v_n^(-1) tilde-Phi_n. Combining the uniform inverse bound with ||tilde-Phi_n||<=1+C_theta*eta and submultiplicativity yields ||tilde-Upsilon_n||<=(1+C_theta*eta)/(1-C_V*eta) for every n; taking the supremum over n gives the claimed cb bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.3.2.1

**Statement:** Validated node 1.2.3.1 gives, for every n, that v_n is bijective and ||v_n^(-1)|| <= (1-C_V*eta)^(-1), with 1-C_V*eta>0. Validated node 1.2.2.1 gives ||tilde-Phi||_cb <= 1+C_theta*eta, hence ||tilde-Phi_n|| <= 1+C_theta*eta for every n. Since tilde-Upsilon=v^(-1) composed with tilde-Phi and tilde-Phi_n has range in M_n(A), amplification commutes with composition, so tilde-Upsilon_n=v_n^(-1) composed with tilde-Phi_n. Therefore submultiplicativity gives ||tilde-Upsilon_n|| <= ||v_n^(-1)|| ||tilde-Phi_n|| <= (1+C_theta*eta)/(1-C_V*eta) for every n. Taking the supremum over n yields ||tilde-Upsilon||_cb <= (1+C_theta*eta)/(1-C_V*eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Scalar assembly: for 0<=eta<=rho_T, the guards in (1.1) imply C_theta*eta,C_V*eta<=1/4 and therefore (1+C_theta*eta)/(1-C_V*eta) <= 1+(C_theta+3*C_V)*eta=1+C_T*eta; also C_V<=C_T, so the two branch bounds imply max{||tilde-Delta||_cb,||tilde-Upsilon||_cb}<=1+C_T*eta, while the factor branch already gives the asserted amplification inequalities.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Put a=C_theta*eta and b=C_V*eta. The two guards [4(1+C_theta)]^(-1) and [4(1+C_V)]^(-1) in rho_T give 0<=a<=C_theta/[4(1+C_theta)]<=1/4 and 0<=b<=C_V/[4(1+C_V)]<=1/4, so 1-b>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Direct algebra gives [1+a+3b]-(1+a)/(1-b)=b*(2-a-3b)/(1-b). Because 0<=a,b<=1/4, one has 2-a-3b>=1, hence the difference is nonnegative and (1+C_theta*eta)/(1-C_V*eta)<=(1+C_theta*eta+3*C_V*eta)=1+C_T*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Since C_theta,C_V>=0 and C_T=C_theta+3*C_V, C_T>=C_V. Therefore ||tilde-Delta||_cb<=1+C_V*eta<=1+C_T*eta and the inverse-composition branch gives ||tilde-Upsilon||_cb<=1+C_T*eta. Taking their maximum proves the cb assertion, and the factor branch supplies the root's two-sided amplification assertion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

