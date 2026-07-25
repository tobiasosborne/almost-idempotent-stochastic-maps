# Proof Export

## Node 1

**Statement:** Uniform Ha column action: there are universal C_act < infinity and e_act > 0 such that every H-CB datum with e <= e_act, every n >= 1, Z in M_n tensor S_{P,R}, and X in M_{n,1} tensor S_{R,Q} satisfy q_P((Ha^Q_{P,R})_n(Z)X-Z dot X) <= C_act*e*||Z||*q_R(X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Conditional nondegeneracy of the compressed unit: if Q is nonvanishing in the sense of the registered nonvanishing-delta-projection definition, then there are universal c_u>0 and e_u>0 such that every H-CB datum with e<=e_u satisfies u_Q:=Co_Q(Q)=tilde Q and ||u_Q||>=c_u. No unconditional nondegeneracy is asserted from one-dimensionality alone.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Conditional norm estimate only: if Q is nonvanishing in the sense of the registered nonvanishing-delta-projection definition, then there are universal K_0<infinity and e_0>0 such that e<=e_0 implies ||Q||>=1-K_0*e. The exact allowed inputs do not establish that the one-dimensional delta-projection Q in an H-CB datum is nonvanishing.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.1

**Statement:** Assume Q is nonvanishing. By the registered nonvanishing-delta-projection definition, the second branch gives universal constants K_0<infinity and e_0>0 such that e<=e_0 implies abs(||Q||-1)<=K_0*(delta+epsilon). Since def-hcb-datum gives e=delta+epsilon, this yields ||Q||>=1-K_0*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.2

**Statement:** The registered dichotomy also permits the small branch ||Q||<=O(delta), and none of the exact allowed definitions or external lemmas states that one-dimensionality excludes that branch. Therefore the original unconditional estimate, and its use toward parent node 1.1, remains unavailable unless a permitted one-dimensional-implies-nonvanishing input is provisioned.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Let L=L_Q and R=R_Q on the underlying Banach space and set A=LR+RL-I in the associative Banach algebra B(A), so that Co_Q=theta(A) by the compression construction. There are universal K_1<infinity and e_1>0 such that e<=e_1 implies ||tilde Q-Q||=||(theta(A)-I)Q||<=K_1*e, where tilde Q=Co_Q(Q)=u_Q. Thus theta is used only in B(A), not in the generally nonassociative epsilon-Banach-C*-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** For e below a universal threshold, the delta-projection dichotomy gives a universal M with ||Q||<=M in both alternatives. Hence ||L||,||R||<= (1+epsilon)M. Moreover the registered associator and delta-projection bounds give ||LR-RL||<=epsilon M^2, ||L^2-L||<=epsilon M^2+(1+epsilon)delta, and ||R^2-R||<=epsilon M^2+(1+epsilon)delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.2

**Statement:** Put T=(LR+RL)/2. The preceding operator bounds imply ||T||<=C and ||T^2-T||<=C_T e: first U=LR obeys ||U^2-U||<=||L||||R||||RL-LR||+||L^2-L||||R||^2+||L||||R^2-R||, and ||T-U||=||RL-LR||/2<=C e; expanding T^2-T around U then gives the assertion. Therefore A=2T-I satisfies ||A||<=C_A and ||A^2-I||=4||T^2-T||<=4C_T e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.3

**Statement:** Writing r=Q^2-Q with ||r||<=delta and retaining the indicated parentheses, (A-I)Q=Q(QQ)+(QQ)Q-2Q=2r+Qr+rQ. Thus ||(A-I)Q||<=2delta+2(1+epsilon)||Q||delta<=C_Q e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.4

**Statement:** Choose e_1 so that ||A^2-I||<1/2. In the associative operator algebra, B:=(A^2)^(-1/2) is defined by its convergent power series and ||B||<=C_B. The same series, termwise factored at 1, gives B-I=(A^2-I)K(A^2) with ||K(A^2)||<=C_K. Since A commutes with B and K(A^2), theta(A)-I=(AB-I)/2=(A-I)H(A), where H(A)=[B+(A+I)K(A^2)]/2 and ||H(A)||<=C_H. Consequently ||(theta(A)-I)Q||=||H(A)(A-I)Q||<=C_H C_Q e. Taking K_1=C_H C_Q proves the amended node, and Co_Q(Q)=tilde Q=u_Q is the registered column-inner-product identification.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Conditional combination only: assume the estimates supplied by 1.1.1 and 1.1.2 hold, namely ||Q||>=1-K_0*e and ||tilde Q-Q||<=K_1*e for e<=min(e_0,e_1), with finite K_0,K_1 and positive e_0,e_1. After replacing K_i by max(K_i,0), put S:=K_0+K_1 and set e_u:=min(e_0,e_1,1/(2*S)) if S>0, or e_u:=min(e_0,e_1) if S=0. Then e_u>0 and, for e<=e_u, ||u_Q||=||tilde Q||>=||Q||-||tilde Q-Q||>=1-S*e>=1/2. Thus c_u:=1/2 proves nondegeneracy conditional on both estimates. Because amended node 1.1.1 supplies its estimate only under the additional hypothesis that Q is nonvanishing, and the allowed inputs do not establish that hypothesis, node 1.1.3 does not by itself prove the unconditional parent 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.1

**Statement:** Assume the two estimates in node 1.1.3, including every antecedent needed for them; in particular, amended node 1.1.1 provides its estimate only when Q is nonvanishing. Since e=delta+epsilon>=0, replacing each finite K_i by max(K_i,0) weakens neither estimate, so take K_0,K_1>=0 and S:=K_0+K_1. If S>0 set e_u:=min(e_0,e_1,1/(2*S)); if S=0 set e_u:=min(e_0,e_1). Positivity of e_0,e_1 gives e_u>0. For e<=e_u, reverse triangle and u_Q=tilde Q give ||u_Q||>=||Q||-||tilde Q-Q||>=1-K_0*e-K_1*e=1-S*e. This is at least 1/2 when S>0 and is 1 when S=0. Hence ||u_Q||>=1/2 under the joint hypotheses, proving exactly the conditional statement of node 1.1.3. It does not discharge the missing nonvanishing antecedent and therefore makes no claim to prove unconditional node 1.1.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** Assume Q is nonvanishing. Validated node 1.1.1 then supplies universal finite K_0 and positive e_0 with ||Q||>=1-K_0*e for e<=e_0, while validated node 1.1.2 supplies universal finite K_1 and positive e_1 with ||u_Q-Q||<=K_1*e for e<=e_1. These are exactly the joint hypotheses of validated node 1.1.3, so that node gives c_u:=1/2 and a universal positive e_u (namely min(e_0,e_1,1/(2*(max(K_0,0)+max(K_1,0)))) when the denominator is positive, and min(e_0,e_1) otherwise) for which ||u_Q||>=c_u. This proves the amended conditional parent and deliberately makes no inference from one-dimensionality to nonvanishing.

**Type:** qed

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

#### Node 1.1.5

**Statement:** Endpoint-safe conditional assembly: assume Q is nonvanishing. By validated nodes 1.1.1 and 1.1.2 there are universal finite K_0,K_1 and universal e_0,e_1>0 such that ||Q||>=1-K_0*e whenever e<e_0 and ||u_Q-Q||<K_1*e whenever e<e_1, with u_Q=Co_Q(Q)=tilde Q. Put K_0^+=max(K_0,0), K_1^+=max(K_1,0), and S=K_0^++K_1^+. If S>0 define e_u=min(e_0/2,e_1/2,1/(2*S)); if S=0 define e_u=min(e_0/2,e_1/2); in both cases set c_u=1/2. These constants are universal and positive. For every H-CB datum with e<=e_u, positivity of e_0,e_1 gives e<=e_0/2<e_0 and e<=e_1/2<e_1, so both strict-cutoff estimates apply. Enlarging K_i to K_i^+ only weakens those estimates because e>=0. Hence the reverse triangle inequality yields ||u_Q||>=||Q||-||u_Q-Q||>=1-S*e (indeed strictly greater when using the strict second estimate). If S>0 then e<=1/(2*S), so ||u_Q||>=1/2; if S=0 then ||u_Q||>=1. Therefore ||u_Q||>=c_u for every e<=e_u, including the endpoint. This proves exactly the amended conditional parent and does not infer nonvanishing from one-dimensionality.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Uniform column norm comparison: if e<=min(e_col,1/(2*C_col)), then for T=P and T=R and every amplified column U in M_{n,1} tensor S_{T,Q}, (1-C_col*e)^(1/2)*||U||_{n,1} <= q_T(U) <= (1+C_col*e)^(1/2)*||U||_{n,1}, where q_T(U):=<U,U>_n^(1/2); this is an application of lem-hcb-column-hilbert-squared.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Apply lem-hcb-column-hilbert-squared to the H-CB datum, first with the projection T=P and then with T=R: for each compatible amplified column U, |q_T(U)^2-||U||_{n,1}^2|<=C_col*e*||U||_{n,1}^2, because q_T(U)^2=<U,U>_n by the registered column inner-product display.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Rearranging the absolute-value estimate gives (1-C_col*e)||U||_{n,1}^2<=q_T(U)^2<=(1+C_col*e)||U||_{n,1}^2. Under C_col*e<=1/2 all terms are nonnegative, so monotonicity of the square root yields exactly the two-sided comparison claimed in 1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Defect pairing estimate: for D:=(Ha^Q_{P,R})_n(Z)X-Z dot X, every Y in M_{n,1} tensor S_{P,Q} satisfies 2*|<Y,D>_n|*||u_Q|| <= C_as*e*||Y||_{n,1}*||Z||*||X||_{n,1}, provided e<=min(e_var,e_as); this follows from lem-hcb1-variational-identity and lem-hcb0-compressed-associator.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** By lem-hcb1-variational-identity, for e<=e_var and D=(Ha^Q_{P,R})_n(Z)X-Z dot X, one has 2*<Y,D>_n*u_Q=(Y^dagger dot Z) dot X-Y^dagger dot (Z dot X), with u_Q=Co_Q(Q), for every compatible amplified column Y.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** The right-hand side is precisely the compressed associator of A=Y^dagger, B=Z, C=X by def-compressed-associator. Thus lem-hcb0-compressed-associator, for e<=e_as, bounds its norm by C_as*e*||Y^dagger||*||Z||*||X||_{n,1}=C_as*e*||Y||_{n,1}*||Z||*||X||_{n,1}; the last equality is the amplified involution norm identity from the registered epsilon-Banach-C*-norm axioms.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Taking norms in the identity of 1.3.1 and using absolute homogeneity gives ||2*<Y,D>_n*u_Q||=2*|<Y,D>_n|*||u_Q||; combining this equality with 1.3.2 proves the claimed defect pairing estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Unconditional assembly: by def-hcb-datum, Q is a one-dimensional delta-projection, and the registered one-dimensional-projection-nonvanishing definition therefore makes Q nonvanishing. Validated node 1.1.4 applies with c_u=1/2 and universal e_u>0. Put t:=min(e_u,e_col,e_var,e_as,1/(2*max(C_col,1)))>0 and e_act:=t/2. If e<=e_act then e<t, so the validated norm-comparison and defect-pairing steps apply; nodes 1.4.2 and 1.4.3.1 give q_P(D)<=(C_as/c_u)*e*||Z||*q_R(X)=2*C_as*e*||Z||*q_R(X), where D:=(Ha^Q_{P,R})_n(Z)X-Z dot X. Hence C_act:=2*C_as is universal and finite, and the unconditional root estimate holds for every e<=e_act.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Choose e_act:=min(e_u,e_col,e_var,e_as,1/(2*max(C_col,1)))>0 and fix an H-CB datum with e<=e_act and compatible n,Z,X. Then 1.1 gives ||u_Q||>=c_u, while 1.2 gives ||Y||_{n,1}<=sqrt(2)*q_P(Y) and ||X||_{n,1}<=sqrt(2)*q_R(X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Insert these three bounds into 1.3: for every Y in M_{n,1} tensor S_{P,Q}, 2*c_u*|<Y,D>_n|<=2*C_as*e*q_P(Y)*||Z||*q_R(X), hence |<Y,D>_n|<= (C_as/c_u)*e*q_P(Y)*||Z||*q_R(X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** Conditional terminal cancellation: assume node 1.1 has supplied universal constants c_u>0 and e_u>0, and take e below the thresholds in 1.4.1. For D:=(Ha^Q_{P,R})_n(Z)X-Z dot X, validated node 1.4.3.1 gives q_P(D)^2<=(C_as/c_u)*e*||Z||*q_R(X)*q_P(D). If q_P(D)=0 the desired inequality is immediate, while if q_P(D)>0 division by q_P(D) gives q_P(D)<=(C_as/c_u)*e*||Z||*q_R(X). Under the stated assumption C_act:=C_as/c_u is universal and finite. This proves the column-action estimate only conditional on node 1.1; because the exact allowed inputs do not establish that Q is nonvanishing, node 1.1 and the unconditional root remain pending.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.3.1

**Statement:** By def-ha-map and compatibility of the compressed product, both (Ha^Q_{P,R})_n(Z)X and Z dot X, hence D, belong to M_{n,1} tensor S_{P,Q}; thus D is an admissible choice of Y in validated node 1.4.2. Validated node 1.2.2 gives q_P(D)^2=<D,D>_n>=0 under the threshold already used in 1.4, so |<D,D>_n|=q_P(D)^2 and q_P(D)>=0. Substituting Y=D in 1.4.2 and writing K:=(C_as/c_u)*e*||Z||*q_R(X)>=0 yields q_P(D)^2<=K*q_P(D). If q_P(D)=0, then q_P(D)<=K. If q_P(D)>0, division by q_P(D) gives q_P(D)<=K. Therefore q_P(D)<=(C_as/c_u)*e*||Z||*q_R(X), with no Riesz-duality inference and no reliance on pending node 1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.3.2

**Statement:** The open challenge is mathematically correct: the exact allowed definitions and externals for this shard do not imply that the one-dimensional delta-projection Q is nonvanishing, so they do not furnish a universal c_u>0. Validated node 1.4.3.1 proves only the cancellation conditional on such a c_u. Accordingly, node 1.4.3 has been amended to remove the unconditional claim that C_as/c_u is finite and that root node 1 is proved. The valid conclusion is: if node 1.1 is eventually proved, then C_act=C_as/c_u is a finite universal constant and the asserted estimate follows; without node 1.1 no division by c_u and no unconditional root conclusion is licensed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.4

**Statement:** The registered one-dimensional-projection-nonvanishing definition, together with def-hcb-datum, implies that Q is nonvanishing. Hence validated node 1.1.4 supplies universal c_u=1/2 and e_u>0. Combining this unconditional discharge of the nonvanishing premise with validated nodes 1.2 and 1.3 yields the root estimate with universal finite C_act=2*C_as and a universal positive e_act. The earlier negative conclusion in node 1.4.3.2 is stale after definition provisioning and is not used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.4.1

**Statement:** By def-hcb-datum, Q is a one-dimensional delta-projection, so dim S_Q=1. Therefore S_Q is not the zero space. The registered one-dimensional-projection-nonvanishing definition states that S_Q=0 exactly in the small alternative and that the opposite alternative is precisely nonvanishing. Thus Q is nonvanishing. This directly corrects the stale context assertion challenged at node 1.4.4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.4.2

**Statement:** Apply validated node 1.1.4 to the nonvanishing Q from the preceding child. It supplies universal constants c_u=1/2 and e_u>0 such that every H-CB datum with e<=e_u has ||u_Q||>=1/2. The antecedent of that conditional validated result is now discharged by an allowed registered definition, not assumed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.4.3

**Statement:** Let e_act:=(1/2)*min(e_u,e_col,e_var,e_as,1/(2*max(C_col,1)))>0. For e<=e_act, the strict threshold hypotheses of validated nodes 1.2 and 1.3 hold: e<=e_col/2<e_col, e<=e_var/2<e_var, e<=e_as/2<e_as, and, when C_col>0, e<=1/(4*max(C_col,1))<1/(2*C_col) (if C_col=0, the column-Hilbert error term vanishes and no reciprocal cutoff is needed). Thus node 1.2 gives ||Y||_{n,1}<=sqrt(2)*q_P(Y) and ||X||_{n,1}<=sqrt(2)*q_R(X), while node 1.3 and the lower bound ||u_Q||>=1/2 from node 1.4.4.2 give |<Y,D>_n|<=2*C_as*e*q_P(Y)*||Z||*q_R(X) for every compatible Y, where D=(Ha^Q_{P,R})_n(Z)X-Z dot X: the left side of 2*|<Y,D>_n|*||u_Q||<=C_as*e*||Y||_{n,1}*||Z||*||X||_{n,1} is at least |<Y,D>_n|, and the two norm comparisons multiply to the factor 2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.4.4.3.1

**Statement:** Endpoint-safe case split. Let e_act=(1/2)*min(e_u,e_col,e_var,e_as,1/(2*max(C_col,1))). Every entry of the minimum is positive, so e_act>0. If e<=e_act, then e<e_col, e<e_var, and e<e_as. If C_col>0, then 1/(2*C_col) is defined and e<=1/(4*max(C_col,1))<1/(2*C_col), so validated node 1.2 applies and yields ||U||_{n,1}<=sqrt(2)*q_T(U) for T=P,R. If C_col=0, node 1.2 is not invoked: the column-Hilbert squared estimate recorded in validated node 1.2.1, applied at e<e_col, has zero right-hand side and gives q_T(U)^2=||U||_{n,1}^2; since both quantities are nonnegative, q_T(U)=||U||_{n,1}, which implies the same comparison. Thus in both cases the two norm comparisons needed by the parent hold, and e<e_var,e_as makes validated node 1.3 applicable. No reciprocal involving C_col is formed in the zero case.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.4.4.3.1.1

**Statement:** For e<=e_act, positivity of e_col,e_var,e_as and the factor 1/2 give e<=e_col/2<e_col, e<=e_var/2<e_var, and e<=e_as/2<e_as. Thus the column-Hilbert estimate itself is available at e<e_col, and the strict e_var,e_as hypotheses of validated node 1.3 hold, including at e=e_act.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.4.4.3.1.2

**Statement:** Case C_col>0. The reciprocal 1/(2*C_col) is defined, and e<=1/(4*max(C_col,1))<1/(2*C_col): if 0<C_col<=1, the left cutoff is 1/4 while 1/(2*C_col)>=1/2; if C_col>=1, the comparison is 1/(4*C_col)<1/(2*C_col). Together with e<e_col from the preceding child, this satisfies node 1.2 and yields ||U||_{n,1}<=sqrt(2)*q_T(U) for T=P,R.

**Type:** case

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.4.4.3.1.3

**Statement:** Case C_col=0. Do not apply node 1.2 and do not form 1/(2*C_col). By validated node 1.2.1, available because e<e_col, |q_T(U)^2-||U||_{n,1}^2|<=C_col*e*||U||_{n,1}^2=0 for T=P,R. Hence q_T(U)^2=||U||_{n,1}^2. Since q_T(U)>=0 by its square-root definition and ||U||_{n,1}>=0 by the norm axioms, q_T(U)=||U||_{n,1}, and therefore ||U||_{n,1}<=sqrt(2)*q_T(U).

**Type:** case

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.4.4.3.1.4

**Statement:** The nonnegative estimate constant C_col falls into exactly one of C_col>0 and C_col=0. The preceding two cases therefore establish the needed norm comparisons for T=P,R without asserting node 1.2's undefined reciprocal antecedent in the zero case. Independently, the first child supplies e<e_var,e_as, so node 1.3 applies. This is precisely the corrected endpoint bridge used by the parent.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.4.4

**Statement:** By def-ha-map and product compatibility, D lies in M_{n,1} tensor S_{P,Q}, so take Y=D in the preceding estimate. Validated node 1.2 gives q_P(D)^2=<D,D>_n>=0. Hence q_P(D)^2<=2*C_as*e*q_P(D)*||Z||*q_R(X). If q_P(D)=0 the desired bound is immediate; if q_P(D)>0, divide by q_P(D). Thus q_P(D)<=2*C_as*e*||Z||*q_R(X). Taking C_act:=2*C_as and the positive universal e_act above proves the unconditional root estimate.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.5

**Statement:** Endpoint-safe unconditional bridge. By validated node 1.4.4.1, def-hcb-datum and the registered one-dimensional-projection-nonvanishing axiom imply that Q is nonvanishing. Therefore validated node 1.1.4 supplies c_u=1/2 and universal e_u>0. Let t=min(e_u,e_col,e_var,e_as,1/(2*max(C_col,1))) and e_act=t/2. All entries of the minimum are positive, hence e_act>0; if e<=e_act then e<t, which meets the strict thresholds in nodes 1.2, 1.3, and 1.4.1, while also giving e<=e_u for node 1.1.4. Validated nodes 1.4.2 and 1.4.3.1 then yield q_P(D)<=(C_as/c_u)*e*||Z||*q_R(X)=2*C_as*e*||Z||*q_R(X). Thus C_act=2*C_as is a finite universal constant and the estimate is unconditional, including the endpoint e=e_act.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

