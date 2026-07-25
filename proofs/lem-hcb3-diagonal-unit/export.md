# Proof Export

## Node 1

**Statement:** Uniform diagonal Ha unit estimate: there are universal C_unit < infinity and e_unit > 0 such that every H-CB datum with e <= e_unit and every n >= 1 satisfy ||(Ha^Q_{P,P})_n(I_n tensor u_P)-I|| <= C_unit*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Pointwise estimate: there are universal K_u<infinity and e_0>0 such that, after taking e_0<=min(e_act,e_co), every admissible datum with e<=e_0, every n, U=I_n tensor u_P, and every X in M_{n,1} tensor S_{P,Q} satisfy q_P(((Ha^Q_{P,P})_n(U)-I)X) <= (C_act*K_u+C_co)*e*q_P(X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Uniform compressed-unit size: the registered compressed-product display, delta-projection dichotomy, and epsilon-Banach-C*-norm axioms give universal K_u<infinity and e_u>0 such that the compressed unit and all diagonal amplifications U=I_n tensor u_P satisfy ||U||<=K_u for every n and every H-CB datum with e<=e_u.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.1

**Statement:** Level-one unit bound: the compressed-product display and delta-projection dichotomy, together with the registered epsilon-Banach-C*-norm axioms, give universal K_u and e_u>0 with ||u_P||<=K_u for e<=e_u: in the nonvanishing case u_P is the unit of an O(e)-C*-algebra, and comparison of u_P^dagger dot u_P with u_P and with ||u_P||^2 bounds ||u_P||; in the vanishing case the compression formula and ||P||=O(delta) bound ||u_P|| directly.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.2

**Statement:** Direct amplified unit bound (no diagonal-isometry assumption): the registered extended epsilon-C*-norm axioms and compressed-product display, together with lem-compcb-compressed-unit-action, give universal K_u<infinity and e_u>0 such that U=I_n tensor u_P satisfies ||U||<=K_u for every n and every H-CB datum with e<=e_u.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.1.2.1

**Statement:** Fix n and U=I_n tensor u_P, and put t=||U||. Because an H-CB datum contains an extended epsilon-C*-algebra, the registered epsilon-Banach-C*-norm axioms apply at level n: ||U^dagger U|| >= (1-epsilon)t^2 >= (1-e)t^2 and ||U^dagger||=t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.1.2.2

**Statement:** Let C_pr be the universal constant in the registered compressed-product display (after restricting to its universal small-e threshold). Applied in the amplified P,P corner to U^dagger and U, it gives ||U^dagger U-U^dagger dot U|| <= C_pr*e*t^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.1.2.3

**Statement:** The allowed validated external lem-compcb-compressed-unit-action, using its right-unit estimate with A=U^dagger in the amplified P,P corner, gives ||U^dagger dot U-U^dagger|| <= C_co*e*t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.1.2.4

**Statement:** By the triangle inequality and the preceding three bounds, (1-e)t^2 <= ||U^dagger U|| <= C_pr*e*t^2+(1+C_co*e)t. If t=0 the desired bound is immediate; if t>0, division by t yields [1-(1+C_pr)e]t <= 1+C_co*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.1.2.5

**Statement:** Choose the universal threshold e_u no larger than every threshold used above and 1/[2(1+C_pr)]. Then 1-(1+C_pr)e >= 1/2, so t <= 2(1+C_co*e_u)=:K_u, uniformly in n. This proves the amended node without invoking node 1.1.1.1 or an unregistered diagonal-amplification isometry.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Ha comparison at the diagonal unit: by lem-hcb1-column-action with R=P and Z=U=I_n tensor u_P, for e<=e_act one has q_P((Ha^Q_{P,P})_n(U)X-U dot X) <= C_act*e*||U||*q_P(X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Compressed unit on the column: after decreasing the existential threshold e_co if necessary to the universal level-one norm-comparison threshold, lem-compcb-compressed-unit-action and the registered coordinate-sum inner-product display give q_P(U dot X-X)<=C_co*e*q_P(X), uniformly in n, after enlarging the existential universal constant C_co if necessary.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.1

**Statement:** Entrywise corner estimate: writing X=(X_1,...,X_n)^t, amplified multiplication by U=I_n tensor u_P is entrywise, and lem-compcb-compressed-unit-action applied to each compatible level-one P,Q corner gives ||u_P dot X_j-X_j||<=C_co*e*||X_j|| for every j when e<=e_co.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.2

**Statement:** Level-one norm conversion: the level-one inner-product/norm comparison registered in def-ha-map and column-hilbert-inner-product-displays gives universal kappa and e_q>0 such that q_P(Y)<=kappa||Y|| and ||Y||<=kappa q_P(Y) for Y in S_{P,Q} when e<=e_q; hence q_P(u_P dot X_j-X_j)<=kappa^2*C_co*e*q_P(X_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.3

**Statement:** Column summation: the registered coordinate-sum inner-product display gives q_P((Y_j)_j)^2=sum_j q_P(Y_j)^2; summing the squared coordinate estimates yields q_P(U dot X-X)<=kappa^2*C_co*e*q_P(X), uniformly in n. Since the external lemma is existential in C_co, replace its witness by the larger universal constant kappa^2*C_co and retain the notation C_co.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** Triangle step: set e_0:=(1/2)min(e_u,e_act,e_co), where e_co has already been decreased to include the level-one norm-comparison threshold. For e<=e_0, the identity ((Ha^Q_{P,P})_n(U)-I)X=((Ha^Q_{P,P})_n(U)X-U dot X)+(U dot X-X), followed by the triangle inequality for q_P and the preceding estimates, gives q_P(((Ha^Q_{P,P})_n(U)-I)X)<=(C_act*K_u+C_co)*e*q_P(X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.4.1

**Statement:** Because e_u,e_act,e_co are positive, e_0=(1/2)min(e_u,e_act,e_co)>0 and e_0<e_u,e_act,e_co. Hence e<=e_0 implies e<e_u, e<=e_act, and e<=e_co. Node 1.1.1 therefore supplies ||U||<=K_u. Node 1.1.2 supplies q_P((Ha^Q_{P,P})_n(U)X-U dot X)<=C_act*e*||U||*q_P(X); combining these two estimates gives q_P((Ha^Q_{P,P})_n(U)X-U dot X)<=C_act*K_u*e*q_P(X). Node 1.1.3 supplies q_P(U dot X-X)<=C_co*e*q_P(X). Applying the triangle inequality for q_P to the displayed algebraic identity and adding the last two bounds yields q_P(((Ha^Q_{P,P})_n(U)-I)X)<=(C_act*K_u+C_co)*e*q_P(X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Operator-norm conclusion: the pointwise estimate implies ||(Ha^Q_{P,P})_n(I_n tensor u_P)-I|| <= (C_act*K_u+C_co)*e; hence C_unit=C_act*K_u+C_co and e_unit=e_0 are universal witnesses for node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

