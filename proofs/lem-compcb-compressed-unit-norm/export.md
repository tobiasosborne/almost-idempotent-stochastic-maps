# Proof Export

## Node 1

**Statement:** Compressed-unit norm estimate: there are universal C_co < infinity and e_co > 0 such that, for e=delta+epsilon <= e_co, every delta-projection T satisfies ||u_T|| <= 1+C_co*e, and every nonvanishing T satisfies abs(||u_T||-1) <= C_co*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Audit conclusion (corrected): the exact allowed inputs yield universal finite a,k and a universal threshold e_0>0 such that, for e=delta+epsilon<=e_0 and every delta-projection T, (i) either ||T||<=a*delta or T is nonvanishing, and (ii) u_T=Co_T(T) and ||Co_T-L_T R_T||<=k*e. They do not yield the ambient estimate ||XY||<=(1+epsilon)||X||||Y||, because def-extended-epsilon-cstar-algebra does not include the quantitative definition of epsilon-C*-algebra; nor do they yield abs(||u_T||-1)<=b*e for nonvanishing T, because def-compressed-corner's statement that u_T is the unit of an O(e)-C*-algebra has no registered quantitative unit-norm axiom. Consequently this node cannot supply the missing hypotheses used by nodes 1.2 and 1.3, and the root remains unproved until a permitted byte-matched base epsilon-C*-algebra definition or an allowed lemma supplies those bounds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By def-delta-projection, there are universal a<infinity and a universal validity threshold such that every delta-projection T satisfies the alternative ||T||<=a*delta or abs(||T||-1)<=a*(delta+epsilon); the second alternative is exactly the condition called nonvanishing. After enlarging a if necessary, this proves item (i).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** By def-compressed-corner, u_T=Co_T(T), and the assertion that both ||L_T R_T-Co_T|| and ||R_T L_T-Co_T|| are bounded by O(delta+epsilon) yields universal k<infinity and a universal validity threshold such that ||Co_T-L_T R_T||<=k*(delta+epsilon). These are the compression conclusions justified by the allowed definition. The further estimate ||XY||<=(1+epsilon)||X||||Y|| does not follow from any allowed input: def-extended-epsilon-cstar-algebra only says that M_1 tensor A=A is an epsilon-C*-algebra and does not supply the quantitative definition of that term. Consequently item (ii) of node 1.1, and hence the use of that estimate in node 1.2, remains unproved until the base epsilon-C*-algebra definition or an allowed multiplication-bound lemma is registered.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Audit conclusion: item (iii) is not derivable from the exact allowed inputs currently registered. def-compressed-corner states only that, for nonvanishing T, S_T is an O(delta+epsilon)-C*-algebra with unit u_T=Co_T(T); without a registered quantitative definition of eta-C*-algebra this does not imply abs(||u_T||-1)<=b*(delta+epsilon). The alternative direct comparison of u_T with T also needs the unavailable multiplication estimate identified at node 1.1.2. Thus item (iii) remains unproved pending fulfillment of the registered definition request for the quantitative multiplication and unit axioms of an epsilon-C*-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.1

**Statement:** Because T is nonvanishing, node 1.1.1 supplies abs(||T||-1)<=a*e (after using the same enlarged universal a as in item (i)); consequently ||T||<=1+a*e<=1+a when e<=1.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.1.3.2

**Statement:** By node 1.1.2, u_T=Co_T(T), ||Co_T-L_T R_T||<=k*e, and ||XY||<=(1+epsilon)||X||||Y||. Since (L_T R_T)(T)=T(TT) and ||TT-T||<=delta, bilinearity gives T(TT)-T=T(TT-T)+(TT-T). Therefore ||u_T-T||<=||(Co_T-L_T R_T)(T)||+||T(TT)-T||<=k*e*||T||+(1+epsilon)||T||*delta+delta. Using epsilon<=e<=1, delta<=e, and ||T||<=1+a from the preceding child yields ||u_T-T||<=[k*(1+a)+2*(1+a)+1]*e.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.1.3.3

**Statement:** The reverse triangle inequality gives abs(||u_T||-||T||)<=||u_T-T||. Combining this with abs(||T||-1)<=a*e from the first child and the second child gives abs(||u_T||-1)<=[a+k*(1+a)+2*(1+a)+1]*e. The bracket is a universal finite constant, and intersecting the existing validity threshold with e<=1 proves item (iii). This derivation uses no quantitative unit axiom for an eta-C*-algebra and thereby replaces the challenged inference.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

### Node 1.2

**Statement:** Small-norm branch: under the bounds of node 1.1, if ||T||<=a*delta and e<=1, then ||u_T||<=||(L_T R_T)(T)||+k*e*||T||<=(1+epsilon)^2||T||^3+k*e*||T||<=(4*a^3+k*a)*e; in particular ||u_T||<=1+(4*a^3+k*a)*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Uniform assembly: set e_co=min(e_0,1) and C_co=max(b,4*a^3+k*a). For any delta-projection T with e<=e_co, the dichotomy in node 1.1 gives either node 1.2 and hence ||u_T||<=1+C_co*e, or nonvanishing T and node 1.1(iii), which gives both ||u_T||<=1+C_co*e and abs(||u_T||-1)<=C_co*e. Thus the general upper bound holds for every T and the two-sided bound holds for every nonvanishing T.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Closure audit for challenge ch-e89e1225040b7269: the verifier is correct. Under the exact allowed inputs, node 1.1 supplies only the delta-projection dichotomy, u_T=Co_T(T), and ||Co_T-L_T R_T||<=k*e. It expressly does not supply either (A) ||XY||<=(1+epsilon)||X||||Y|| or (B) abs(||u_T||-1)<=b*e for nonvanishing T. Hence node 1.2's estimate of ||(L_T R_T)(T)|| invokes unavailable (A), while node 1.3 names an undefined b and invokes a deleted item 1.1(iii), i.e. unavailable (B). The two permitted upstream amplified-compression lemmas give only amplification, idempotence, and adjoint identities, none of which bounds these norms. There is therefore no sound bridging step from the current allowed premises to the root contract. The root must remain pending, and the already-registered pending definition request for the quantitative multiplication and unit axioms of an epsilon-C*-algebra (or an allowed norm-control lemma added by the orchestrator) must be fulfilled before nodes 1.2 and 1.3 can be replaced by a valid proof.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Repaired quantitative input extraction. By the registered byte-matched axioms epsilon-banach-cstar-norm-axioms, nonvanishing-delta-projection, and def-compressed-corner, there are universal finite constants a,b,k and e_0>0 such that for e=delta+epsilon<=e_0: (i) every delta-projection T satisfies either ||T||<=a*delta or T is nonvanishing; (ii) ||XY||<=(1+epsilon)||X||||Y||; (iii) u_T=Co_T(T) and ||Co_T-L_T R_T||<=k*e; and (iv) if T is nonvanishing then abs(||T||-1)<=b*e. Here each O(delta+epsilon) or O(delta) in the registered byte-matched statements is unpacked as a universal constant after decreasing the universal threshold e_0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Small branch. Assume e<=min(e_0,1), ||T||<=a*delta, and put D=4*a^3+k*a. Since (L_T R_T)(T)=T(TT)=T(T^2), two applications of (ii) give ||(L_T R_T)(T)||<=(1+epsilon)^2||T||^3<=4*a^3*e^3<=4*a^3*e. Moreover (iii) gives ||u_T-(L_T R_T)(T)||<=k*e*||T||<=k*a*e^2<=k*a*e. Hence ||u_T||<=D*e, and therefore ||u_T||<=1+D*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Nonvanishing branch. Decrease e_0 so that e_0<=1 and b*e_0<=1. If T is nonvanishing, then (iv) gives ||T||<=2. Bilinearity and T^2=TT give T(T^2)-T=T(T^2-T)+(T^2-T). Thus (ii), ||T^2-T||<=delta, and (iii) imply ||u_T-T||<=||u_T-(L_T R_T)(T)||+||T(T^2)-T||<=k*e*||T||+(1+epsilon)||T||*delta+delta<=(2*k+5)*e. The reverse triangle inequality and (iv) now yield abs(||u_T||-1)<=abs(||u_T||-||T||)+abs(||T||-1)<=(2*k+5+b)*e; in particular ||u_T||<=1+(2*k+5+b)*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Corrected assembly addressing ch-a35e352910b1a54e. Let e_co be the decreased positive universal threshold used above and C_co=max(4*a^3+k*a,2*k+5+b). The dichotomy in repaired input node #0 sends every delta-projection to either the small branch #1 or the nonvanishing branch #2. The former gives ||u_T||<=1+C_co*e; the latter gives that upper bound and abs(||u_T||-1)<=C_co*e. This proves the root. This assembly does not use the obsolete amended node 1.1, the semantically stale nodes 1.2-1.3, or a compressed-unit norm axiom: the previously missing multiplication estimate is now supplied by the registered byte-matched epsilon-banach-cstar-norm-axioms, and the nonvanishing conclusion is derived directly by comparing u_T with T.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

