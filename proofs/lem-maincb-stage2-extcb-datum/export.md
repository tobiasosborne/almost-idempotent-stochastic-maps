# Proof Export

## Node 1

**Statement:** There are universal C_s2 >= 1 and e_s2 > 0, with the e_ca threshold and universal C_ca coefficient of lem-compcb-corner-algebra absorbed into e_s2 and C_s2, such that, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state comes from a non-unital extended t-inclusion w:C^m->A with one-dimensional images P_j, has nonempty U, j notin U, dim S^A_{P_k,P_j} = 1 for every k in U, and R = U union {j}, and a supplied current reset state v_U:M_{|U|}->A_U is an extended isomorphism satisfying epsilon_U, d_U <= t <= e_s2 and d_U <= c_0^cb*epsilon_U, then lem-compcb-corner-algebra makes A_R an extended epsilon_{A_R}-C*-algebra, lem-maincb-nested-corner-comparison makes P_U^R, P_j^R quantitative projections in A_R, and together with the lem-maincb-outer-compression-transfer outer-compressed isomorphism they satisfy every def-extcb-datum clause - approximate complementarity to I_{A_R}, one-dimensional S_{P_j^R}, nonzero S_{P_U^R,P_j^R}, and total error e = delta + epsilon_{A_R} - with e <= C_s2*t, forming the explicit Stage-2 raw-call closed EXT-CB datum in A_R.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Universal constant ledger (excluding the unquantified additivity input). With C_nest,e_nest, e_ncd, C_out,e_out, e_sim, and C_ca,e_ca denoting the universal witnesses in the correspondingly named registered externals, set C_delta=max{1,C_nest,C_out}, C_s2=max{1,C_delta+2*C_ca}, and e_s2=min{1/2,e_nest,e_ncd,e_out,e_sim,e_ca/2}. These are positive finite universal constants, independent of m,U,j and every amplification. If t<=e_s2 and epsilon_A<=t, then t+epsilon_A<=2*t<=e_ca, and the named nested-comparison, nested-dimension-transport, outer-transfer, corner-equivalence, and corner-algebra thresholds are met; in particular the e_ca threshold and C_ca coefficient are absorbed exactly as the root requires. No applicability threshold for lem-extcb-corner-dimension-additivity is asserted or absorbed here, because its registered contract supplies no dimension-independent quantitative threshold.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Justification and scope of the corrected ledger. The registered externals explicitly provide positive universal e_nest,e_ncd,e_out,e_sim,e_ca and finite universal C_nest,C_out,C_ca. A finite minimum of the displayed positive thresholds is positive and universal, and the displayed finite maxima are finite and universal. Thus t<=e_s2 implies each listed quantitative hypothesis; epsilon_A<=t and e_s2<=e_ca/2 give t+epsilon_A<=2*t<=e_ca. In contrast, the registered contract of lem-extcb-corner-dimension-additivity says only sufficiently accurate and supplies neither a numeric threshold nor uniformity in m or |U|. Consequently it cannot enter this universal minimum, and this node gives no permission to invoke it downstream. The nonzero cross-corner clause must therefore be proved by a separate dimension-uniform argument or a strengthened allowed external; it does not follow from this ledger.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Original-corner geometry. Put e_U=sum_{k in U}e_k, e_R=e_U+e_j, P_U=w(e_U), and P_R=w(e_R)=P_U+P_j. Then P_U,P_j,P_R are t-projections in A, P_R is nonvanishing, every left/right subordination error of P_U and P_j to P_R is at most t, A_R=S^A_{P_R}, and the local definitions P_U^R=Co^A_{P_R}(P_U), P_j^R=Co^A_{P_R}(P_j) are the compressed elements required by the nested-corner externals.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Projection and nonvanishing check. At level one, def-extended-delta-inclusion makes w a t-homomorphism preserving involution and satisfying ||w(xy)-w(x)w(y)||<=t||x||||y|| together with (1-t)||x||<=||w(x)||<=(1+t)||x||. Since U and R=U union {j} are nonempty, e_U,e_j,e_R are norm-one Hermitian projections of C^m. Hence their images P_U,P_j,P_R are Hermitian and have idempotence defect at most t, so they are t-projections by def-delta-projection. Moreover 1-t<=||P_R||<=1+t, whence | ||P_R||-1 |<=t<=t+epsilon_A; this is the nonvanishing alternative of def-delta-projection (with universal coefficient 1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Subordination and corner notation. The coordinate identities e_Ue_R=e_Re_U=e_U and e_je_R=e_Re_j=e_j, inserted in the t-multiplicative-defect inequality, give ||P_UP_R-P_U||, ||P_RP_U-P_U||, ||P_jP_R-P_j||, ||P_RP_j-P_j||<=t. Linearity gives P_R=P_U+P_j. The supplied def-maincb-partition-state defines A_R=S^A_{P_R}; set P_U^R=Co^A_{P_R}(P_U) and P_j^R=Co^A_{P_R}(P_j), which are precisely the equalities demanded by lem-maincb-nested-corner-comparison and lem-maincb-nested-corner-dimension-transport.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Target algebra and projection clauses. Apply lem-compcb-corner-algebra to the nonvanishing t-projection P_R in the extended epsilon_A-C*-algebra A. It makes A_R=S^A_{P_R}, with compressed product, inherited involution, and unit I_{A_R}=Co^A_{P_R}(P_R), an extended epsilon_{A_R}-C*-algebra for epsilon_{A_R}=C_ca*(t+epsilon_A)<=2*C_ca*t. Apply lem-maincb-nested-corner-comparison to (R,P,Q)=(P_R,P_U,P_j), using node 1.2: P_U^R and P_j^R are C_nest*t-projections in A_R.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Corner-algebra application. Since epsilon_A<=t, every defining extended epsilon_A-C*-inequality also holds with the larger parameter t. Node 1.2 makes P_R a nonvanishing t-projection. Node 1.1 gives t+epsilon_A<=e_ca. Hence lem-compcb-corner-algebra applies with delta=t and epsilon=epsilon_A and gives A_R=S^A_{P_R} the compressed product, inherited involution, and compressed unit u_R=Co^A_{P_R}(P_R), as an extended C_ca*(t+epsilon_A)-C*-algebra. Define epsilon_{A_R}=C_ca*(t+epsilon_A); then epsilon_{A_R}<=2*C_ca*t and u_R=I_{A_R}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Local corner threshold, independent of node 1.1. The root conclusion is existential in the single universal witness e_s2. Since the registered external lem-compcb-corner-algebra supplies a universal e_ca>0, impose in constructing that witness the additional restriction 0<e_s2<=e_ca/2 (intersecting any other positive universal restrictions with e_ca/2 preserves positivity). Then the root hypotheses epsilon_A<=t<=e_s2 give t+epsilon_A<=2*t<=2*e_s2<=e_ca. Thus the external's required defect threshold holds without using node 1.1 or any additivity threshold.

**Type:** claim

**Inference:** existential_witness_restriction

**Status:** validated

**Taint:** clean

##### Node 1.3.1.2

**Statement:** Validated projection premise, independent of pending node 1.2. By validated node 1.2.1, P_R is Hermitian, ||P_R^2-P_R||<=t, and 1-t<=||P_R||<=1+t. Hence P_R is a t-projection and satisfies the nonvanishing alternative | ||P_R||-1 |<=t<=t+epsilon_A. This is exactly the nonvanishing t-projection premise required by lem-compcb-corner-algebra.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.3.1.3

**Statement:** Corner-algebra conclusion from the now explicit premises. The ambient A is finite-dimensional and is an extended epsilon_A-C*-algebra by the root hypotheses. Child 1.3.1.1 proves t+epsilon_A<=e_ca, and child 1.3.1.2 proves that P_R is a nonvanishing t-projection. Apply the registered lem-compcb-corner-algebra with delta=t, epsilon=epsilon_A, and P=P_R. It equips A_R=S^A_{P_R} with the compressed product, inherited involution, and compressed unit u_R=Co^A_{P_R}(P_R), and makes it an extended C_ca*(t+epsilon_A)-C*-algebra. Set epsilon_{A_R}=C_ca*(t+epsilon_A) and I_{A_R}=u_R. Since epsilon_A<=t, epsilon_{A_R}<=2*C_ca*t. Thus every conclusion in node 1.3.1 follows using children 1.3.1.1 and 1.3.1.2, with no reliance on pending nodes 1.1 or 1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Nested-projection application. Regard A as an extended t-C*-algebra by the same parameter monotonicity. Node 1.2 supplies t-projections P_R,P_U,P_j, nonvanishing P_R, all four subordination errors at most t, A_R=S^A_{P_R}, and the exact compressed-element definitions. Since node 1.1 gives t<=e_nest, lem-maincb-nested-corner-comparison applies to (R,P,Q)=(P_R,P_U,P_j) and concludes that P_U^R and P_j^R are C_nest*t-projections in A_R. Together with the first child this proves node 1.3.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Direct nested-comparison threshold bridge, with the final witness distinguished from the preliminary ledger. Let e_s2^0 := min{1/2, e_nest, e_ncd, e_out, e_sim, e_ca/2}. The fixed-source additivity repair in validated node 1.5.2 supplies a further positive universal threshold e_{2,1} and chooses the final root witness e_s2 := min{e_s2^0,e_{2,1}}. Consequently e_s2 <= e_s2^0 by the defining property of a minimum, and e_s2^0 <= e_nest because e_nest is one of the entries defining e_s2^0. Thus the root hypothesis t <= e_s2 gives t <= e_s2 <= e_s2^0 <= e_nest, so the nested-comparison threshold is met. The additivity threshold is used only to shrink the final universal witness; this nested-comparison application itself uses no conclusion of lem-extcb-corner-dimension-additivity.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.2.1.1

**Statement:** Threshold derivation. Validated node 1.5.2 fixes the final root witness as e_s2=min{e_s2^0,e_{2,1}}, where e_s2^0 is the six-term minimum from node 1.1 and e_{2,1}>0 is the fixed-(C^2,C) additivity threshold. Hence e_s2<=e_s2^0. From the definition e_s2^0=min{1/2,e_nest,e_ncd,e_out,e_sim,e_ca/2}, one also has e_s2^0<=e_nest. Combining these inequalities with the root assumption t<=e_s2 yields t<=e_nest. This proves exactly the threshold premise needed for lem-maincb-nested-corner-comparison without asserting the false equality e_s2=e_s2^0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.2.1.1.1

**Statement:** Dependency-explicit threshold chain. Validated node 1.1 defines the preliminary ledger witness e_s2^0=min{1/2,e_nest,e_ncd,e_out,e_sim,e_ca/2}; because e_nest is an entry of this finite minimum, e_s2^0<=e_nest. Validated node 1.5.2 defines the final witness e_s2=min{e_s2^0,e_{2,1}}, so e_s2<=e_s2^0. Therefore, under the root hypothesis t<=e_s2, transitivity gives t<=e_s2<=e_s2^0<=e_nest, exactly the threshold required by lem-maincb-nested-corner-comparison.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Diagonal isomorphism clause. The current reset state supplies v_U:M_|U|->A_U=S^A_{P_U} as an extended d_U-isomorphism. Since d_U<=t, monotonicity of the defining defect and norm bounds makes it an extended t-isomorphism. Apply lem-maincb-outer-compression-transfer with R=P_R and P=P_U: the explicit map T=Co^{A_R}_{P_U^R} o Co^A_{P_R} o v_U is an extended C_out*t-isomorphism M_|U|->S^{A_R}_{P_U^R}, and T_n=I_n tensor T for every n. The extra invariant d_U<=c_0^cb*epsilon_U, with c_0^cb supplied by lem-maincb-error-improvement, is retained as part of the input reset record but no improvement is needed in this conditional row.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Dimension clauses. One has dim S^{A_R}_{P_j^R}=1 and S^{A_R}_{P_U^R,P_j^R} is nonzero.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Scalar corner. The phrase one-dimensional images P_l means, by def-one-dimensional-delta-projection, that dim S^A_{P_l}=1; in particular dim S^A_{P_j,P_j}=1. Apply lem-maincb-nested-corner-dimension-transport to (R,P,Q)=(P_R,P_j,P_j). Node 1.2 supplies the t-projections, nonvanishing, both repeated left/right subordination bounds, A_R=S^A_{P_R}, and P_j^R=Co^A_{P_R}(P_j), while node 1.1 supplies t<=e_ncd. Therefore dim S^{A_R}_{P_j^R,P_j^R}=dim S^A_{P_j,P_j}=1, i.e. dim S^{A_R}_{P_j^R}=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Cross corner, using only a fixed-source additivity threshold. Choose k_0 in the nonempty set U. If U={k_0}, then P_U=P_{k_0}, so the hypothesis dim S^A_{P_{k_0},P_j}=1 already gives S^A_{P_U,P_j} nonzero. Suppose instead that V=U\{k_0} is nonempty. Define exact non-unital *-monomorphisms alpha:C^2->C^m and beta:C->C^m by alpha(a,b)=a e_{k_0}+b e_V and beta(c)=c e_j. Because both coordinate blocks {k_0},V are nonempty and disjoint, alpha is completely isometric; beta is completely isometric as well. Hence w o alpha and w o beta inherit, at every amplification, the t-homomorphism and two-sided (1+-t) norm bounds from the supplied non-unital extended t-inclusion w. Their units map respectively to P_{k_0}+P_V=P_U and P_j, and their projection bases map to (P_{k_0},P_V) and (P_j). Apply lem-extcb-corner-dimension-additivity only to these fixed source algebras C^2 and C. Let e_{2,1}>0 denote its sufficient-accuracy threshold for this fixed pair; because the pair is fixed, e_{2,1} is a universal numerical constant independent of m,U,j and A. Write e_s2^0 for the positive ledger constant constructed in node 1.1 and take the final root witness to be e_s2=min{e_s2^0,e_{2,1}}. Every earlier deduction, which required only t<=e_s2^0, remains valid under this shrink, while t<=e_s2 now makes this fixed-source additivity call admissible. The resulting linear bijection is S^A_{P_U,P_j} -> S^A_{P_{k_0},P_j} direct_sum S^A_{P_V,P_j}. Its first summand has dimension 1 by hypothesis, so S^A_{P_U,P_j} is nonzero. In either case, lem-maincb-nested-corner-dimension-transport applied to (R,P,Q)=(P_R,P_U,P_j), with the t-projections, nonvanishing and four subordination bounds from node 1.2 and t<=e_ncd, gives dim S^{A_R}_{P_U^R,P_j^R}=dim S^A_{P_U,P_j}>0. Thus the target cross corner is nonzero; no threshold uniform over variable-dimensional C^U and no equality dim S^A_{P_U,P_j}=|U| is used.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Complementarity reduction and identified missing input. Validated node 1.2 gives P_U+P_j=P_R and P_U^R=Co^A_{P_R}(P_U), P_j^R=Co^A_{P_R}(P_j); node 1.3 gives I_{A_R}=Co^A_{P_R}(P_R). Therefore the desired equality P_U^R+P_j^R=I_{A_R} follows if Co^A_{P_R} is additive. But neither any definition registered in this workspace nor any allowed external asserts that additivity (or the defining compression formula from which it follows). Hence the former exact-complementarity claim is not derivable from the exact allowed inputs. A definition request has been filed for the compressed-corner compression map, including its defining formula and linearity/additivity; until that permitted input is provisioned, node 1.6 remains an explicit proof blocker and must not be used to discharge the complementarity clause.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Final assembly is blocked at complementarity. Let delta=C_delta*t. If nodes 1.3-1.5 are validated, they provide the target extended epsilon_{A_R}-C*-algebra, the delta-projection clauses, the extended delta-isomorphism T:M_|U|->S^{A_R}_{P_U^R} with fixed amplifications, dim S^{A_R}_{P_j^R}=1, and the nonzero cross-corner; the same constant calculation gives delta+epsilon_{A_R}<=(C_delta+2*C_ca)t<=C_s2*t. However, node 1.6 does not prove ||P_U^R+P_j^R-I_{A_R}||<=delta: it proves only that exact complementarity would follow from additivity of Co^A_{P_R}, while also establishing that this additivity (or a substitute quantitative complementarity estimate) is absent from every registered definition and allowed external. Hence the exact allowed inputs do not establish the complementarity clause of def-extcb-datum, so they do not yet form a closed EXT-CB datum or a closed Stage-2 raw call. Closure requires provisioning an allowed definition/validated lemma giving compression additivity, or another allowed estimate implying ||P_U^R+P_j^R-I_{A_R}||<=delta; no such conclusion is claimed here.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Vacuity bridge from the permitted corner-equivalence input. Choose the root witness e_s2 no larger than e_sim (and, independently, no larger than every other positive universal threshold needed for the advertised absorption clauses; choose C_s2 at least 1 and at least the finitely many advertised universal coefficients). Under the root hypotheses, epsilon_A<=t makes A an extended t-C*-algebra by monotonicity of all defining inequalities, t<=e_s2<=e_sim, and every P_l is a one-dimensional t-projection. Hence lem-maincb-corner-equivalence says that l~l' iff dim S^A_{P_l,P_l'}=1 is an equivalence relation. By def-maincb-partition-state, the supplied current U is then a union of equivalence classes. Since U is nonempty, choose k in U. The hypothesis dim S^A_{P_k,P_j}=1 says k~j, so j lies in the equivalence class of k. Because U is a union of equivalence classes and contains k, it contains that entire class, hence j in U, contradicting the root hypothesis j notin U. Thus no datum satisfies all root antecedents.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** Final discharge by contradiction. Node 1.8 derives a contradiction solely from the root antecedents, def-maincb-partition-state, def-one-dimensional-delta-projection, and the allowed validated external lem-maincb-corner-equivalence, after shrinking the existential universal e_s2 so that e_s2<=e_sim while retaining the advertised e_ca/constant absorptions. Therefore the implication asserted by node 1 holds vacuously for those universal witnesses. In particular no complementarity estimate or additivity of Co^A_{P_R} is required; nodes 1.6 and 1.7 correctly identify a gap in the nonvacuous construction route but do not obstruct this contradiction proof of the root contract.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

