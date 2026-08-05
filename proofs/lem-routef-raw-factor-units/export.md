# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: Raw factor-map units: for 0 <= eta <= rho_unit := rho_T, max{||tilde-Delta(I)-I||, ||tilde-Upsilon(I)-I||} <= C_T*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix the single global header W_RF and, for an arbitrary input (H,Phi,eta) to which lem-routef-raw-factor-setting-formation applies, fix the datum S furnished by that same external over W_RF. Assume 0<=eta<=rho_unit=rho_T. By def-routef-raw-factor-setting, rho_T is the minimum in (1.1), so rho_T<=1/[4*(1+C_V)]; formation gives C_A=20+(211/8)*C_theta>0, bar C_E=max{1,C_E}>=1, hence C_V=bar C_E*C_A>=0, and therefore b:=C_V*eta<=C_V/[4*(1+C_V)]<=1/4. Also C_theta=12*(sqrt(2)-1)>=0 and C_T=C_theta+3*C_V, so C_V<=C_T and 3*C_V<=C_T.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Delta-unit branch. Let e_B denote the unit element of the unital C*-algebra B; by def-routef-raw-factor-setting this is the unsubscripted I forced by a B-element type, whereas I_B denotes the identity map of B and is not used as an element. Lem-routef-raw-factor-setting-formation gives v:B->A as an extended delta-isomorphism for delta:=C_E*epsilon_AI(eta), with 0<=epsilon_AI(eta)<=C_A*eta, and def-routef-raw-factor-setting gives tilde-Delta=inclusion_{A subset B(H)} composed with v. By def-extended-delta-inclusion, the n=1 amplification v is a delta-inclusion. By the registered byte-verbatim external GT-kitaev-def-delta-homomorphism, a delta-inclusion is a delta-homomorphism and its unit clause gives ||v(e_B)-I_A||<=delta. Since bar C_E=max{1,C_E}, delta<=bar C_E*C_A*eta=C_V*eta. The unit I_A inherited by A is I_{B(H)}, and the ambient inclusion is isometric, so ||tilde-Delta(e_B)-I_{B(H)}||<=C_V*eta<=C_T*eta, the last inequality being node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Dependency audit (the verifier objection is correct). The permitted text defines an extended delta-isomorphism only by bijectivity, the two-sided amplification norm bounds, and the otherwise undefined predicate delta-homomorphism; none of the registered definitions or four externals states a unit-defect inequality. This omission is mathematically material: at eta=0 take H=C, Phi=identity, tilde-Phi=identity, A=B=C, v=-identity and u=-identity. If the undefined delta-homomorphism predicate is interpreted as imposing no additional clause, then v is bijective and every amplification is an exact isometry, all explicit raw-factor norm conclusions hold, but ||v(1)-1||=2 whereas C_V*eta=0. Thus no bridging argument from the currently permitted inputs can prove node 1.2. It becomes valid only after provisioning a permitted definition or external whose delta-homomorphism clause explicitly gives ||v(1_B)-1_A||<=delta; a pending definition request for precisely that clause has been filed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Updated challenge disposition after provisioning. The earlier dependency objection no longer blocks node 1.2: the registered byte-verbatim external GT-kitaev-def-delta-homomorphism now explicitly defines a delta-homomorphism by the unit condition ||v(I)-I||<=delta and the multiplicative condition, and defines a delta-inclusion to be such a delta-homomorphism with two-sided norm bounds. Combined with def-extended-delta-inclusion at amplification n=1, formation therefore gives ||v(e_B)-I_A||<=delta for the correctly typed unit element e_B of B. The former eta=0 map v=-id is not a counterexample because it violates both the unit condition and, in general, the multiplicative condition for a 0-homomorphism. The valid notation correction remains: I_B denotes the identity map, so the amended parent uses e_B. Consequently delta=C_E*epsilon_AI(eta)<=bar C_E*C_A*eta=C_V*eta<=C_T*eta proves the repaired Delta-unit branch.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** The missing dependency is now explicitly provisioned as the registered byte-verbatim external GT-kitaev-def-delta-homomorphism (approximate_algebras.tex:443-456). Formation supplies an extended delta-isomorphism v with delta=C_E*epsilon_AI(eta). By def-extended-delta-inclusion, its n=1 amplification v is a delta-inclusion; the external defines a delta-inclusion to be a delta-homomorphism satisfying norm bounds and defines every delta-homomorphism to obey ||v(e_B)-I_A||<=delta. Thus the required unit estimate follows directly, with the correctly typed unit element e_B rather than I_B. Since 0<=epsilon_AI(eta)<=C_A*eta and C_E<=bar C_E=max{1,C_E}, delta<=bar C_E*C_A*eta=C_V*eta; the inherited unit of A is I_{B(H)}, the inclusion A subset B(H) preserves its norm, and validated node 1.1 gives C_V<=C_T. Therefore ||tilde-Delta(e_B)-I_{B(H)}||<=C_T*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Upsilon-unit branch. Let e_B denote the unit element of the unital C*-algebra B; this is the unsubscripted I forced by an adjacent B-element type in def-routef-raw-factor-setting, whereas I_B denotes the identity map of B and is not used as an element. By lem-routef-raw-factor-norms at n=1, for every X in B, ||v(X)||=||tilde-Delta(X)|| ≥ (1-C_V*eta)||X||. Put b:=C_V*eta. Since eta ≤ rho_T ≤ 1/[4*(1+C_V)], we have b ≤ C_V/[4*(1+C_V)] < 1/4. Because v is bijective and u=v^(-1), the lower norm bound gives ||u|| ≤ 1/(1-b). Lem-routef-raw-factor-setting-formation gives tilde-Phi^2=tilde-Phi, A=Im(tilde-Phi), A with inherited unit I, and u=v^(-1). Hence I belongs to A=Im(tilde-Phi), so idempotence gives tilde-Phi(I)=I, and def-routef-raw-factor-setting gives tilde-Upsilon(I)=u(tilde-Phi(I))=u(I). Since u(v(e_B))=e_B and u is linear, tilde-Upsilon(I)-e_B=u(I)-u(v(e_B))=u(I-v(e_B)). The unit clause of the delta-homomorphism contained in the registered definition def-extended-delta-inclusion, applied to the extended C_E*epsilon_AI(eta)-isomorphism v from formation, gives ||I-v(e_B)|| ≤ C_E*epsilon_AI(eta) ≤ bar C_E*C_A*eta=C_V*eta. Therefore ||tilde-Upsilon(I)-e_B|| ≤ ||u||*||I-v(e_B)|| ≤ C_V*eta/(1-b) ≤ 4*C_V*eta/3 ≤ 3*C_V*eta ≤ C_T*eta, using b < 1/4 and C_T=C_theta+3*C_V with C_theta ≥ 0. The second unsubscripted I in the contract's expression ||tilde-Upsilon(I)-I|| has type B and is exactly e_B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Provisioned unit-defect bridge. The registered byte-verbatim external GT-kitaev-def-delta-homomorphism defines a delta-homomorphism v from a unital approximate Banach algebra to another by, in particular, ||v(I)-I|| <= delta. By def-extended-delta-inclusion, an extended delta-isomorphism is bijective and every amplification is a delta-inclusion, hence its n=1 amplification v is a delta-homomorphism in exactly this registered sense. Formation supplies v:B->A as an extended delta-isomorphism for delta:=C_E*epsilon_AI(eta). Applying the registered unit clause to the unit e_B of B and the inherited unit I of A therefore gives ||v(e_B)-I|| <= C_E*epsilon_AI(eta). Since 0<=epsilon_AI(eta)<=C_A*eta and C_E<=bar C_E:=max{1,C_E}, this is at most bar C_E*C_A*eta=C_V*eta. Thus the formerly unsupported estimate in node 1.3 is now an explicit consequence of a permitted byte-verbatim external plus def-extended-delta-inclusion; no conclusion is inferred from bijectivity or norm bounds alone.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

