# Proof Export

## Node 1

**Statement:** Corrected amplified column-Hilbert estimate: there are universal C_col < infinity and e_col > 0 such that every H-CB datum with e <= e_col, every n >= 1, and every X in M_{n,1} tensor S_{P,Q} satisfy abs(<X,X>_n-||X||_{n,1}^2) <= C_col*e*||X||_{n,1}^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Uniform setup of constants: from lem-compcb-rectangular-product and lem-compcb-compressed-unit-norm there exist universal C >= 1 and e_0 > 0, with e_0 <= 1/(2C), such that whenever e <= e_0 both allowed estimates hold with constant C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By lem-compcb-rectangular-product, choose universal C_p<infinity and e_p>0 for which its compatible amplified rectangular-pair estimate holds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** By lem-compcb-compressed-unit-norm, choose universal C_u<infinity and e_u>0 for which both stated compressed-unit norm estimates hold.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Set C=max{1,C_p,C_u} and e_0=min{e_p,e_u,1/(2C)}. Then C and e_0 are universal, finite/positive, both estimates remain valid with C for e<=e_0, and C*e<=1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Scalarization: for fixed admissible H-CB datum, n, and X, put r=||X||_{n,1}, h=<X,X>_n, a=||u_Q||, and b=||X^dagger X||. Then h is a nonnegative real and the defining amplified column-Hilbert identity gives X^dagger dot X=h u_Q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Because the amplified column space is a Hilbert space with its defined inner product, h=<X,X>_n is a nonnegative real.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** The defining amplified display in def-column-hilbert-corner (also registered as column-hilbert-inner-product-displays), specialized to Y=X, is X^dagger dot X=<X,X>_n u_Q=h u_Q; the other symbols r,a,b are merely the stated abbreviations.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Row-column compressed-product consequence: in the scalarized setup, whenever e <= e_rc, the validated lemma lem-compcb-row-column-product applied with Y=X gives ||Co_Q(X^dagger X)-X^dagger X|| <= C_rc*e*r^2. By node 1.2, Co_Q(X^dagger X)=h*u_Q; hence absolute homogeneity and the reverse triangle inequality yield abs(h*a-b) <= ||h*u_Q-X^dagger X|| <= C_rc*e*r^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Under this shard's exact allowed inputs, the affirmative compatibility-and-norm claim is unavailable: for n>1 the literal pair (X^dagger,X) is not a square amplified rectangular pair; the zero-paddings (X_r,X_c) are not proved to lie in the required amplified compressed corners or to preserve the compressed product; and dagger isometry gives only ||X_r||=||X_c||, not ||X_c||=||X||_{n,1}=r. Hence lem-compcb-rectangular-product cannot be applied here without additional registry-level amplification/compression-naturality and matrix-norm-identification inputs.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Let e_1 be the first standard basis column of C^n and define the canonical square zero-paddings X_c:=X e_1^* in M_n tensor S_{P,Q} and X_r:=e_1 X^dagger=X_c^dagger in M_n tensor S_{Q,P}. Thus X_c has X as its first column and zero other columns, while X_r has X^dagger as its first row and zero other rows.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.2

**Statement:** From node 1.3.1.1 one obtains only X_c in M_n tensor S_{P,Q} and X_r in M_n tensor S_{Q,P}. The stronger identifications M_n tensor S_{P,Q}=S_{P_n,Q_n} and M_n tensor S_{Q,P}=S_{Q_n,P_n}, and therefore compatibility of (X_r,X_c) for lem-compcb-rectangular-product and landing in S_{Q_n,Q_n}, do not follow from the shard's permitted definitions or from either allowed dependency contract. They would follow from the separately validated lem-compcb-amplified-compression (together with its exact amplification identities), but that result is not an allowed dependency of this shard. Hence the claimed compatibility is unavailable under the current exact input list and this branch is blocked pending registry-level dependency provisioning.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.3

**Statement:** From X_r=X_c^dagger in 1.3.1.1 and the registered dagger-isometry axiom one may conclude only ||X_r||=||X_c||. Neither def-column-hilbert-corner nor def-hcb-datum, and neither allowed dependency contract, identifies the rectangular norm r=||X||_{n,1} with the norm of the square zero-padding X_c. Hence ||X_c||=r (and therefore ||X_r||=r) does not follow from this shard's allowed inputs; the former zero-padding norm claim is withdrawn and this route requires an additional allowed norm-identification input.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.1.3.1

**Statement:** The dagger axiom applies to the square element X_c and, using X_r=X_c^dagger from 1.3.1.1, yields ||X_r||=||X_c^dagger||=||X_c||. This equality contains no occurrence of the independently denoted rectangular norm r=||X||_{n,1}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.1.3.2

**Statement:** The complete allowed-input audit is negative: def-column-hilbert-corner supplies the amplified space and sesquilinear identity, def-hcb-datum supplies only data and notation, lem-compcb-rectangular-product is conditional on a compatible pair, and lem-compcb-compressed-unit-norm concerns compressed units. None states that X maps isometrically to Xe_1^*. Therefore appending ||X_c||=r would be a new external hypothesis, not a derivation; the asserted equality must be removed rather than proved here.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.4

**Statement:** For the canonical zero-paddings from 1.3.1.1, direct block multiplication alone gives X_r X_c=E_{11} tensor (X^dagger X). The present shard's allowed inputs do not supply amplification naturality Co_{Q_n,Q_n}(E_{11} tensor Z)=E_{11} tensor Co_Q(Z), nor a square-zero-padding norm isometry. Consequently no identity between X_r dot X_c and E_{11} tensor (X^dagger dot X), and no equality ||X_r dot X_c-X_rX_c||=||X^dagger dot X-X^dagger X||, follows here; those former assertions are withdrawn.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.5

**Statement:** The type error cannot be repaired from the current inputs: 1.3.1.2 and 1.3.1.4 show that the padded factors lack the required amplified-corner memberships and compressed-product/norm identifications, while 1.3.1.3--1.3.1.3.2 show that dagger isometry proves only ||X_r||=||X_c||. Therefore neither compatibility/product landing nor equality with r follows, so the affirmative application must be withdrawn pending new registry dependencies.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Allowed-input diagnosis for the proposed rectangular-product step: the literal pair (X^dagger,X) is nonsquare, and the canonical square zero-paddings B=Xe_1^* and A_0=B^dagger cannot repair the application under this shard's exact allowed inputs. By validated nodes 1.3.2.1--1.3.2.3, those inputs do not establish the amplified-corner memberships needed for compatibility, the compressed-product identification with E_11 tensor (X^dagger dot X), or the matrix-norm identifications with r and with ||h u_Q-X^dagger X||. Therefore lem-compcb-rectangular-product cannot be instantiated here, and the estimate ||h u_Q-X^dagger X|| <= C*e*r^2 is not established at this node; a suitable additional validated registry dependency is required.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Let e_1 be the first coordinate column and define B=Xe_1^* and A_0=B^dagger=e_1X^dagger. From X in M_{n,1} tensor S_{P,Q}, entrywise zero-padding yields only B in M_n tensor S_{P,Q}; entrywise adjunction yields only A_0 in M_n tensor (S_{P,Q})^dagger, where (S_{P,Q})^dagger={x^dagger:x in S_{P,Q}}. None of def-hcb-datum, def-column-hilbert-corner, lem-compcb-rectangular-product, or lem-compcb-compressed-unit-norm establishes either M_n tensor S_{P,Q}=S_{P_n,Q_n} or (S_{P,Q})^dagger subseteq S_{Q,P} (and hence does not establish A_0 in S_{Q_n,P_n}). Therefore compatibility of (A_0,B) for lem-compcb-rectangular-product is not established under this shard's exact allowed inputs, and the former affirmative compatibility and S_{Q,P}-membership claims are withdrawn.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.2.1.1

**Statement:** Writing X=sum_i E_{i1} tensor x_i with each x_i in S_{P,Q}, entrywise zero-padding gives B=sum_i E_{i1} tensor x_i in M_n tensor S_{P,Q}. Since A_0=B^dagger, entrywise adjunction gives A_0=sum_i E_{1i} tensor x_i^dagger in M_n tensor (S_{P,Q})^dagger, where (S_{P,Q})^dagger={x^dagger:x in S_{P,Q}}. The exact allowed definitions and dependencies do not establish (S_{P,Q})^dagger subseteq S_{Q,P}; therefore A_0 in M_n tensor S_{Q,P}, and hence rectangular-pair compatibility, cannot be inferred here. The former S_{Q,P}-membership assertion is withdrawn.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.2.1.2

**Statement:** The contract of lem-compcb-rectangular-product requires its factors to lie in the amplified compressed corners S_{Q_n,P_n} and S_{P_n,Q_n}. The equalities M_n tensor S_{P,Q}=S_{P_n,Q_n} and M_n tensor S_{Q,P}=S_{Q_n,P_n} are additional amplification-naturality statements, not consequences of the memberships in the preceding child. Because no allowed definition or dependency supplies them, the theorem cannot be instantiated here. The validated result lem-compcb-amplified-compression would supply the missing corner identities only after it is added and propagated as a registry dependency; doing that is outside the present exact input list.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.2

**Statement:** Direct block multiplication gives only A_0B=E_{11} tensor (X^dagger X). Under this shard's exact allowed inputs, the amplification/corner naturality needed to define the relevant compressed product entrywise and infer A_0 dot B=E_{11} tensor (X^dagger dot X) is unavailable; likewise, no allowed definition or dependency supplies ||E_{11} tensor z||=||z||. Hence the former compressed-product and norm identities do not follow and are withdrawn; this node provides no bridge from the padded square product to ||h u_Q-X^dagger X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.2.2.1

**Statement:** Only the ambient block-product identity A_0B=E_{11} tensor (X^dagger X) follows by direct matrix multiplication. Under the exact allowed inputs, amplification naturality does not identify B and A_0 with the required amplified compressed corners, does not define A_0 dot B as entrywise compression of the supported block, and does not yield A_0 dot B=E_{11} tensor (X^dagger dot X). Independently, no allowed definition or dependency states the matrix-norm isometry ||E_{11} tensor z||=||z||. Therefore the former compressed-product and norm identities are withdrawn; this node supplies no bridge to ||h u_Q-X^dagger X||, and the zero-padding route remains blocked pending registry-level provisioning of both amplification/corner naturality and matrix-norm identification.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.3

**Statement:** The proposed square-zero-padding application is unavailable under this shard's exact allowed inputs. Node 1.3.2.1 yields only B in M_n tensor S_{P,Q} and A_0 in M_n tensor (S_{P,Q})^dagger, where (S_{P,Q})^dagger={x^dagger:x in S_{P,Q}}. It does not establish either B in S_{P_n,Q_n} (because M_n tensor S_{P,Q}=S_{P_n,Q_n} is unavailable) or A_0 in S_{Q_n,P_n} (because (S_{P,Q})^dagger subseteq S_{Q,P}, as well as the needed amplification identification, is unavailable). These are the memberships required for (A_0,B) to be a compatible amplified rectangular pair, and node 1.3.2.2 supplies neither membership; indeed it also withdraws the compressed-product and matrix-norm identifications. Therefore lem-compcb-rectangular-product cannot be instantiated with (A_0,B), and neither ||A_0 dot B-A_0B|| <= C e r^2 nor ||h u_Q-X^dagger X|| <= C e r^2 is established here. A valid proof of node 1.3.2 requires registry-level provisioning of the missing amplification/corner and norm-identification inputs; absent those inputs, node 1.3.2 is blocked.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.2.3.1

**Statement:** The validated meaning of a compatible amplified rectangular pair at level n requires the first factor to lie in S_{Q_n,P_n}, the second in S_{P_n,Q_n}, and the compressed product to be the corresponding corner compression. Membership merely in M_n tensor S_{Q,P} and M_n tensor S_{P,Q} is not the same premise unless amplification naturality identifies these spaces.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.2.3.2

**Statement:** By dependency 1.3.2.1, the amplification identifications required for compatibility are unavailable from the exact allowed definitions and registry dependencies of this shard. Dependency 1.3.2.2 supplies only the ambient block-product identity A_0B=E_{11} tensor (X^dagger X); it supplies no corner membership, no compressed-product identification, and no matrix-norm identification. Hence the compatibility premise is missing, so the rectangular-product theorem cannot yield the claimed estimate; the unconditional application is withdrawn rather than papered over.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Reverse triangle inequality and absolute homogeneity of the norm give abs(h*a-b)=abs(||h u_Q||-||X^dagger X||) <= ||h u_Q-X^dagger X|| <= C*e*r^2, since h>=0, a=||u_Q||, and b=||X^dagger X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** The reverse triangle inequality yields only abs(h*a-b)=abs(||h*u_Q||-||X^dagger X||) <= ||h*u_Q-X^dagger X||. The further estimate ||h*u_Q-X^dagger X|| <= C*e*r^2 written in node 1.3.3 is not a consequence of reverse triangle inequality or homogeneity; it is exactly the missing rectangular-product consequence. Therefore node 1.3.3 is usable only for the first inequality and supplies no C*e*r^2 bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.5

**Statement:** The previous exhaustive-impossibility and necessary-remedy claims are withdrawn. The now-allowed validated dependency lem-compcb-row-column-product applies directly, without square zero-padding: with Y=X it yields ||Co_Q(X^dagger X)-X^dagger X|| <= C_rc*e*r^2 whenever e<=e_rc. Since node 1.2 gives Co_Q(X^dagger X)=X^dagger dot X=h*u_Q, this is ||h*u_Q-X^dagger X|| <= C_rc*e*r^2, and reverse triangle inequality gives abs(h*a-b) <= C_rc*e*r^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.5.1

**Statement:** The verifier objection is accepted: failure of the literal nonsquare pair and one zero-padding construction does not prove an exhaustive impossibility or a necessary-remedy theorem. Those assertions have therefore been removed rather than defended. The added registry dependency lem-compcb-row-column-product supplies a different direct argument that requires neither a square embedding nor E_11 matrix-norm or compression-naturality identifications.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.5.2

**Statement:** Instantiate the validated contract lem-compcb-row-column-product with the datum projections P,Q and with Y=X in M_{n,1} tensor S_{P,Q}. Its hypotheses are exactly satisfied for e<=e_rc, and it gives ||Co_Q(X^dagger X)-X^dagger X|| <= C_rc*e*||X||_{n,1}*||X||_{n,1}=C_rc*e*r^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.5.3

**Statement:** By validated node 1.2, Co_Q(X^dagger X)=X^dagger dot X=h*u_Q. Hence the preceding bound is ||h*u_Q-X^dagger X|| <= C_rc*e*r^2. Since h>=0, a=||u_Q||, and b=||X^dagger X||, absolute homogeneity and the reverse triangle inequality give abs(h*a-b)=abs(||h*u_Q||-||X^dagger X||)<=||h*u_Q-X^dagger X||<=C_rc*e*r^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** C-star norm consequence: in the same setup, abs(b-r^2) <= e*r^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** The epsilon-C-star lower norm axiom applied at the amplified rectangular level gives b=||X^dagger X|| >= (1-epsilon)||X||_{n,1}^2=(1-epsilon)r^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Submultiplicativity and dagger isometry give b<= (1+epsilon)||X^dagger||||X||_{n,1}=(1+epsilon)r^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** The preceding lower and upper bounds imply abs(b-r^2)<=epsilon*r^2<=e*r^2, because delta,epsilon>=0 and e=delta+epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Compressed-unit consequence: since the one-dimensional delta-projection Q is nonvanishing, abs(a-1) <= C*e and, when e <= e_0, a >= 1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** The current allowed inputs do not imply that the datum's one-dimensional delta-projection Q is nonvanishing: def-hcb-datum assumes the qualifier 'one-dimensional', but neither it nor def-column-hilbert-corner defines that qualifier or relates it to the vanishing/nonvanishing dichotomy. Consequently the nonvanishing clause of lem-compcb-compressed-unit-norm cannot be applied until the missing one-dimensional-delta-projection definition (or an allowed lemma proving this implication) is provisioned.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Applying lem-compcb-compressed-unit-norm with T=Q yields abs(a-1)=abs(||u_Q||-1)<=C*e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.3

**Statement:** Since e<=e_0 and C*e_0<=1/2, the last estimate gives a>=1-C*e>=1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.4

**Statement:** The registered definition one-dimensional-projection-nonvanishing supplies the missing bridge: one-dimensional means dim S_Q=1, hence S_Q is not zero; since S_Q=0 if and only if Q lies in the first (vanishing) P_alternatives branch, Q cannot lie in that branch and therefore lies in the second branch, i.e. Q is nonvanishing.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Scalar synthesis: the preceding four scalar estimates imply abs(h-r^2) <= (4C+2)*e*r^2; hence C_col=4C+2 and e_col=e_0 prove the root contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** Triangle inequality with the rectangular-product and C-star consequences gives abs(h*a-r^2)<=abs(h*a-b)+abs(b-r^2)<=(C+1)*e*r^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.6.1.1

**Statement:** Corrected direct synthesis (not an application of blocked node 1.3): let C_rc and e_rc be the universal constants from lem-compcb-row-column-product-CONTRACT. Enlarge the downstream setup constant C to max{C,C_rc} and narrow e_0 to min{e_0,e_rc,1/(2C)}, renaming the enlarged/narrowed pair C,e_0. Then for e<=e_0 the row-column estimate with Y=X and the scalar identity X^dagger dot X=h*u_Q give abs(h*a-b)<=C*e*r^2; together with validated node 1.4, the real triangle inequality gives abs(h*a-r^2)<=abs(h*a-b)+abs(b-r^2)<=(C+1)*e*r^2.

**Type:** claim

**Inference:** triangle_inequality

**Status:** validated

**Taint:** clean

###### Node 1.6.1.1.1

**Statement:** Let C_old,e_old be witnesses supplied by validated node 1.1, and let C_rc,e_rc be supplied by the af-validated external lem-compcb-row-column-product-CONTRACT. Set C_new=max{C_old,C_rc} and e_new=min{e_old,e_rc,1/(2*C_new)}. Then C_new and e_new are universal with C_new>=1 and e_new>0; every estimate valid with C_old for e<=e_old remains valid with C_new for e<=e_new; moreover e<=e_new implies e<=e_rc and C_new*e<=1/2. Hence one may rename C_new,e_new as C,e_0 for the downstream synthesis.

**Type:** claim

**Inference:** constant_enlargement_and_threshold_restriction

**Status:** validated

**Taint:** clean

###### Node 1.6.1.1.2

**Statement:** Under the renamed constants from node 1.6.1.1.1 and e<=e_0, one has e<=e_rc. Apply lem-compcb-row-column-product-CONTRACT to the admissible pair Y=X in M_{n,1} tensor S_{P,Q}: ||Co_Q(X^dagger X)-X^dagger X||<=C_rc*e*||X||_{n,1}^2<=C*e*r^2, because r=||X||_{n,1} and C>=C_rc. By validated node 1.2, Co_Q(X^dagger X)=X^dagger dot X=h*u_Q. Since h>=0, a=||u_Q||, and b=||X^dagger X||, absolute homogeneity gives ||h*u_Q||=h*a, and the reverse triangle inequality yields abs(h*a-b)<=||h*u_Q-X^dagger X||<=C*e*r^2.

**Type:** claim

**Inference:** row_column_product_then_reverse_triangle

**Status:** validated

**Taint:** clean

###### Node 1.6.1.1.3

**Statement:** Using node 1.6.1.1.2 and validated node 1.4, h*a-r^2=(h*a-b)+(b-r^2), so the real triangle inequality gives abs(h*a-r^2)<=abs(h*a-b)+abs(b-r^2)<=C*e*r^2+e*r^2=(C+1)*e*r^2. This derivation uses the newly allowed row-column external for the first premise and does not claim that blocked node 1.3 proves it.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.6.1.1.3.1

**Statement:** Independent derivation from permitted validated inputs: by validated node 1.6.1.1.1, after renaming the constants, e<=e_0 implies e<=e_rc and C>=C_rc. Apply the af-validated external lem-compcb-row-column-product-CONTRACT to the admissible choice Y=X in M_{n,1} tensor S_{P,Q}; it gives ||Co_Q(X^dagger X)-X^dagger X||<=C_rc*e*||X||_{n,1}^2<=C*e*r^2. Validated node 1.2 gives Co_Q(X^dagger X)=X^dagger dot X=h*u_Q, with h>=0, a=||u_Q||, b=||X^dagger X||, and r=||X||_{n,1}. Hence absolute homogeneity and reverse triangle inequality give abs(h*a-b)=abs(||h*u_Q||-||X^dagger X||)<=||h*u_Q-X^dagger X||<=C*e*r^2. Finally, validated node 1.4 gives abs(b-r^2)<=e*r^2, while h*a-r^2=(h*a-b)+(b-r^2); therefore abs(h*a-r^2)<=(C+1)*e*r^2. This proves the parent conclusion without using pending node 1.6.1.1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.2

**Statement:** The exact scalar identity a(h-r^2)=(h*a-r^2)+r^2(1-a), together with abs(a-1)<=C*e, gives a*abs(h-r^2)<=(2C+1)*e*r^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.3

**Statement:** Because a>=1/2, division gives abs(h-r^2)<=(4C+2)*e*r^2. Substituting h=<X,X>_n and r=||X||_{n,1}, and taking the universal constants C_col=4C+2 and e_col=e_0, is exactly the root conclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

