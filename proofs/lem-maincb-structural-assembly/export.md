# Proof Export

## Node 1

**Statement:** Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN admits a finite-dimensional C*-algebra B=oplus_C M_{|C|} and an extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A satisfying ||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon; hence C_struct=W.c0_cb*W.K_call and e_struct=W.epsilon_MAIN are finite positive universal witnesses.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** For every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN, there exist B=oplus_C M_{|C|} and an extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A with ||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By lem-maincb-maximal-reset-selection, there exist a positive integer m of maximum source dimension and an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** If m>=1 is of maximum source dimension and w:C^m->A is an extended W.c0_cb*epsilon-inclusion with ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, then there exist B=oplus_C M_{|C|} and an extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A with ||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** Put the nonempty set J={1,...,m}, let {e_j} be the projection basis of C^m, set P_j=w(e_j), R=w(I_{C^m}), and t=W.K_call*epsilon. Then A is an extended t-C*-algebra, every P_j and R is a t-projection, ||R-I_A|| <= W.c0_cb*epsilon <= t, every P_j is one-dimensional, and j~k iff dim S^A_{P_j,P_k}=1 is an equivalence relation with a finite nonempty class family C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.1.1

**Statement:** By lem-maincb-witness-arithmetic, W.K_call>=max{1,W.c0_cb}; hence 0<=epsilon<=t and W.c0_cb*epsilon<=t. The definitions def-extended-epsilon-cstar-algebra and def-epsilon-cstar-algebra show directly, by weakening every epsilon-bound to the larger t-bound at every amplification, that A is extended t-C*. By def-projection-basis, e_j and I are self-adjoint idempotents of norm one; since w is an extended W.c0_cb*epsilon-inclusion, def-extended-delta-inclusion and GT-kitaev-def-delta-homomorphism at level one imply P_j^dagger=P_j, R^dagger=R, ||P_j^2-P_j||<=W.c0_cb*epsilon<=t, and ||R^2-R||<=W.c0_cb*epsilon<=t. Thus def-delta-projection makes P_j,R t-projections, and the assumed near-unit bound gives ||R-I_A||<=W.c0_cb*epsilon<=t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.1.2

**Statement:** Use the particular e_sim witness from lem-maincb-corner-equivalence that was also used, together with the particular e_full witness, to instantiate the single fixed W through lem-maincb-reset-constant-ledger. Under node 1.1.2 and assuming A is extended t-C* and each P_j is a t-projection, lem-maincb-stage1-maximality gives dim S^A_{P_j}=1 for every j; with def-one-dimensional-delta-projection this makes every P_j one-dimensional. Lem-maincb-structural-domain-ledger gives t=W.K_call*epsilon<=e_sim for that same witness, so lem-maincb-corner-equivalence makes j~k iff dim S^A_{P_j,P_k}=1 an equivalence relation. Since nonempty J is finite, its equivalence classes form a finite nonempty class family C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.2

**Statement:** If nonempty J={1,...,m}, {e_j} is the projection basis of C^m, P_j=w(e_j), R=w(I_{C^m}), and t=W.K_call*epsilon; if A is extended t-C*, P_j and R are t-projections, ||R-I_A|| <= W.c0_cb*epsilon <= t, all P_j are one-dimensional, and ~ is an equivalence relation with finite nonempty class family C, then there exist B=oplus_{C in C} M_{|C|} and an extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A satisfying ||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.2.1

**Statement:** Let P_J=sum_{j in J}P_j=R and A_J=S^A_R. Use the particular e_full witness from lem-maincb-full-corner-identification that was used, together with the particular e_sim witness, to instantiate the single fixed W through lem-maincb-reset-constant-ledger. Lem-maincb-structural-domain-ledger gives t<=e_full for that same witness. Since R is a t-projection and ||R-I_A||<=t in the extended t-C*-algebra A, lem-maincb-full-corner-identification gives Co_R=Id_A and S^A_R=A. Hence A_J=A; and by def-compressed-corner its compressed unit is u_{A_J}=Co_R(R)=R.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.2.2

**Statement:** Using A_J=A and u_{A_J}=R, the class family C supports a MAIN partition state and per-class reset isomorphisms, whose finite recombination gives the asserted B and v with the target map-defect and unit bounds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.2.2.1

**Statement:** Choose the current subset U=J. Since w is an extended W.c0_cb*epsilon-inclusion and 0<=W.c0_cb*epsilon<=t, lem-maincb-extended-inclusion-monotone makes w an extended t-inclusion. Using A_J=A, define a def-maincb-reset-state for J by epsilon_J=t, B_J=C^m, v_J=w, its fixed amplification family, d_J=t, and the extended-inclusion tag. Together with the already fixed finite J, A, w, P_j, equivalence relation and class family C, this supplies explicitly the def-maincb-partition-state for the same displayed A,w, with current subset J and the stated reset-state reference.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.2.2.1.1

**Statement:** From the dependency A_J=A and u_{A_J}=R, and from 0<=W.c0_cb*epsilon<=t, lem-maincb-extended-inclusion-monotone upgrades w to an extended t-inclusion with codomain A_J. Taking U=J, epsilon_J=t, B_J=C^m, v_J=w, the fixed amplifications, d_J=t, and the extended-inclusion tag gives every field required by def-maincb-reset-state; J is a nonempty union of all classes. Adjoining this reset-state reference to the explicitly fixed finite J,A,w,P_j, relation and class family gives every field required by def-maincb-partition-state for the same A,w.

**Type:** claim

**Inference:** by_definition_and_external_monotonicity

**Status:** validated

**Taint:** clean

###### Node 1.1.2.2.2.2

**Statement:** For every class C in the finite class family, apply lem-maincb-one-class-extension to this same explicit MAIN partition state and the original w. Its hypotheses are exactly the extended W.c0_cb*epsilon-inclusion and near-unit bound on w, 0<=epsilon<=W.epsilon_MAIN, the one-dimensional atomic images, and that C is one equivalence class. It yields a current reset isomorphism v_C:M_{|C|}->A_C with A_C extended epsilon_C-C*, epsilon_C<=W.L*epsilon<=W.K_call*epsilon, d_C<=W.c0_cb*epsilon_C, and ||v_C(I)-u_{A_C}||<=W.c0_cb*epsilon_C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.2.2.3

**Statement:** Enumerate the finite class family as C_1,...,C_q. Applying lem-maincb-stage3-finite-recombination to the explicit partition state and the per-class reset isomorphisms gives B=oplus_{a=1}^q M_{|C_a|} and a current reset isomorphism v:B->A_J with recorded epsilon_J^out<=W.L*epsilon, map defect d_J^out<=W.c0_cb*epsilon_J^out, and ||v(I_B)-u_{A_J}||<=W.c0_cb*epsilon_J^out.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.2.2.3.1

**Statement:** Because the finite nonempty family C is the family of equivalence classes of J, choose an enumeration C_1,...,C_q with q>=1 and union_{a=1}^q C_a=J. Validated node 1.1.2.2.2.1.1 supplies, for the same displayed A,w, the explicit def-maincb-partition-state with this class family, and validated node 1.1.2.2.2.2 supplies for every C_a an initial current reset isomorphism v_{C_a}:M_{|C_a|}->A_{C_a} whose recorded ambient field epsilon_{C_a} satisfies epsilon_{C_a}<=W.L*epsilon, with d_{C_a}<=W.c0_cb*epsilon_{C_a} and ||v_{C_a}(I)-u_{A_{C_a}}||<=W.c0_cb*epsilon_{C_a}. These are exactly the hypotheses of lem-maincb-stage3-finite-recombination (together with the inherited finite-dimensional extended epsilon-C*-algebra A, 0<=epsilon<=W.epsilon_MAIN, the original extended W.c0_cb*epsilon-inclusion and near-unit bounds on w, and the one-dimensional atomic images). Applying that lemma yields a current reset isomorphism v:oplus_{a=1}^q M_{|C_a|}->A_{union_a C_a}=A_J with recorded epsilon_J^out<=W.L*epsilon, d_J^out<=W.c0_cb*epsilon_J^out, and ||v(I)-u_{A_J}||<=W.c0_cb*epsilon_J^out, which is the asserted conclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.2.2.4

**Statement:** Put D=W.c0_cb*W.K_call*epsilon. The direct sum B=oplus_{C in C}M_{|C|} is a finite-dimensional C*-algebra, and the recombined current reset state tags v:B->A_J as an extended d_J^out-isomorphism into the compressed algebra A_J with unit u_{A_J}=R. The unit-bearing codomain (A,I_A) is different, so lem-maincb-extended-inclusion-monotone is not applied across these units. Instead use the validated direct check in node 1.1.2.2.2.4.1: node 1.1.2.2.1 gives Co_R=Id_A and A_J=A, hence the multiplication, involution, and amplified matrix norms agree; every non-unit amplified clause weakens from d_J^out to D because 0<=d_J^out<=W.c0_cb*epsilon_J^out<=W.c0_cb*W.L*epsilon<=D, while the amplified unit clause follows from ||(I_n tensor v)(I_n tensor I_B)-I_n tensor I_A||_n<=d_J^out+||R-I_A||<=W.c0_cb*(W.L+1)*epsilon<=D, using ||R-I_A||<=W.c0_cb*epsilon and W.K_call>=W.L+1. Bijectivity is unchanged under A_J=A. Thus v:B->(A,I_A) is an extended D-isomorphism by def-extended-delta-inclusion, and at n=1 the same unit estimate gives ||v(I_B)-I_A||<=D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.2.2.4.1

**Statement:** Put D=W.c0_cb*W.K_call*epsilon and q=||R-I_A||. The Stage-3 tag makes v an extended d_J^out-isomorphism into the compressed algebra A_J, whose unit is R, so it cannot be transferred to the unit-bearing algebra (A,I_A) by lem-maincb-extended-inclusion-monotone. Instead, Co_R=Id_A and A_J=A imply that the multiplication, involution, and matrix norms of A_J are those of A; only the distinguished unit changes from R to I_A. At every amplification the non-unit clauses of the extended d_J^out-isomorphism therefore remain valid into A and weaken to defect D because d_J^out<=W.c0_cb*epsilon_J^out<=W.c0_cb*W.L*epsilon<=D. The unit clause changes by at most q: ||(I_n tensor v)(I_n tensor I_B)-I_n tensor I_A||_n <= d_J^out+q <= W.c0_cb*(W.L+1)*epsilon <= D, using q<=W.c0_cb*epsilon and W.K_call>=W.L+1. Thus direct verification of def-extended-delta-inclusion, not monotonicity across different units, makes v:B->(A,I_A) an extended D-isomorphism and also gives ||v(I_B)-I_A||<=D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.2.2.4.1.1

**Statement:** For each n>=1, identify M_n tensor A_J with M_n tensor A as a normed involutive algebra. This is legitimate because node 1.1.2.2.1 gives A_J=A and Co_R=Id_A at every amplification, while def-compressed-corner defines the corner product by compression; hence the corner product becomes the ambient product, and the inherited involution and matrix norms are unchanged. The Stage-3 extended d_J^out-isomorphism tag then supplies linearity, bijectivity, involution preservation, the d_J^out multiplication estimate, and the two-sided (1 plus-or-minus d_J^out) norm estimates for I_n tensor v with codomain M_n tensor A; these clauses do not mention the target unit and, since 0<=d_J^out<=D, each implies its D-version. For the sole unit-dependent clause, the corner tag gives ||(I_n tensor v)(I_n tensor I_B)-I_n tensor R||_n<=d_J^out. The operator-space direct-sum axiom gives ||I_n tensor (R-I_A)||_n=||R-I_A||=q, so the triangle inequality gives unit error at most d_J^out+q. From epsilon_J^out<=W.L*epsilon, d_J^out<=W.c0_cb*epsilon_J^out, q<=W.c0_cb*epsilon, and W.K_call>=W.L+1, we get d_J^out+q<=W.c0_cb*(W.L+1)*epsilon<=D. Thus every amplification is a D-isomorphism into (M_n tensor A,I_n tensor I_A), proving that v is an extended D-isomorphism; n=1 also yields ||v(I_B)-I_A||<=D.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** The scalars C_struct=W.c0_cb*W.K_call and e_struct=W.epsilon_MAIN are finite, positive, universal, and independent of dimension, amplification, block data, class count, and stage index.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** By lem-maincb-reset-constant-ledger and lem-maincb-witness-arithmetic, every field of the fixed ledger W, in particular W.c0_cb, W.K_call, and W.epsilon_MAIN, is positive, finite, universal, and independent of dimension, amplification, block data, class count, and stage index; therefore their product C_struct=W.c0_cb*W.K_call and e_struct=W.epsilon_MAIN have the asserted properties.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

