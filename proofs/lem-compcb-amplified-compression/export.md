# Proof Export

## Node 1

**Statement:** Amplified compression identity: there is a universal e_cmp > 0 such that, whenever e=delta+epsilon <= e_cmp, every pair of delta-projections P,Q in an extended epsilon-C*-algebra and every n >= 1 satisfy 1_{M_n} tensor Co_{P,Q}=Co_{I_n tensor P,I_n tensor Q} and M_n tensor S_{P,Q}=S_{I_n tensor P,I_n tensor Q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Uniform threshold and amplified delta-projections: there is a universal e_cmp>0 such that, if e=delta+epsilon<=e_cmp, then for every n>=1 the elements P_n=I_n tensor P and Q_n=I_n tensor Q are delta-projections in the epsilon-C*-algebra M_n tensor A and the theta power series defining both Co_{P,Q} and Co_{P_n,Q_n} is in its convergence domain.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Amplified projections: by def-extended-epsilon-cstar-algebra, every M_n tensor A is an epsilon-C*-algebra with the compatible matrix multiplication, involution, unit, and diagonal amplification norm. Thus, using def-delta-projection, P_n=I_n tensor P satisfies P_n^dagger=P_n and ||P_n^2-P_n||=||I_n tensor(P^2-P)||=||P^2-P||<=delta; likewise Q_n is a delta-projection, uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Uniform convergence threshold: writing A_{P,Q}=(L_P R_Q+R_Q L_P)/2 and T_{P,Q}=2A_{P,Q}-I, def-compressed-corner gives ||A_{P,Q}^2-A_{P,Q}||<=C e with one universal C in every epsilon-C*-algebra; hence the exact operator-algebra identity T_{P,Q}^2-I=4(A_{P,Q}^2-A_{P,Q}) gives ||T_{P,Q}^2-I||<=4Ce. The same C applies in every M_n tensor A to P_n,Q_n, so choosing universal e_cmp>0 with 4C e_cmp<1 puts both T_{P,Q} and every T_{P_n,Q_n} in the theta/sgn domain specified by theta-idempotent-approximation-map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Algebraic amplification of compression: whenever the relevant theta functional calculi are defined, 1_{M_n} tensor Co_{P,Q}=Co_{P_n,Q_n}, where P_n=I_n tensor P and Q_n=I_n tensor Q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Pre-compression amplifies exactly: for X=[x_ij] in M_n tensor A, L_{P_n}R_{Q_n}(X)=[P(x_ij Q)] and R_{Q_n}L_{P_n}(X)=[(P x_ij)Q]. Consequently T_{P_n,Q_n}=I_n tensor T_{P,Q} for T_{P,Q}=L_P R_Q+R_Q L_P-I.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Use the actual entrywise amplification Gamma_n:B(A)->B(M_n tensor A), not the diagonal embedding into M_n(B(A)). For fixed n, Gamma_n is a bounded unital algebra homomorphism, so it commutes with the norm-convergent power series defining theta. Since 1.2.1 gives Gamma_n(T_{P,Q})=T_{P_n,Q_n} and the theta series is defined at both arguments, Gamma_n(Co_{P,Q})=Co_{P_n,Q_n}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** For fixed n define Gamma_n:B(A)->B(M_n tensor A) by Gamma_n(U)([x_ij])=[U(x_ij)]. This map is bounded: coordinate compression in the concrete operator space gives ||x_ij||<=||X|| for X=[x_ij], while [U(x_ij)]=sum_{i,j} E_ij tensor U(x_ij) and ||E_ij tensor y||=||y||, hence ||Gamma_n(U)X||<=n^2||U||||X|| and ||Gamma_n(U)||<=n^2||U||. Entrywise evaluation also gives Gamma_n(I)=I and Gamma_n(UV)=Gamma_n(U)Gamma_n(V). Thus Gamma_n is a continuous unital algebra homomorphism; no isometry or uniform-in-n bound is asserted. By validated node 1.2.1, Gamma_n(T_{P,Q})=T_{P_n,Q_n}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** Put T=T_{P,Q} and R=T^2-I. On ||R||<1, theta-idempotent-approximation-map defines theta(T) by the norm-convergent inverse-square-root power series: theta(T)=(I+T sum_{k>=0} b_k R^k)/2, where b_k are the scalar Taylor coefficients of (1+z)^(-1/2). For every partial sum s_N, the unital algebra-homomorphism identities from 1.2.2.1 give Gamma_n(s_N(T))=s_N(Gamma_n(T)) and Gamma_n(R)=Gamma_n(T)^2-I. Boundedness of Gamma_n permits passage to the norm limit. The separately established convergence condition at T_{P_n,Q_n}=Gamma_n(T) identifies the target limit with theta(Gamma_n(T)); hence Gamma_n(theta(T_{P,Q}))=theta(T_{P_n,Q_n}).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.3

**Statement:** By def-compressed-corner, Co_{P,Q}=theta(T_{P,Q}) and Co_{P_n,Q_n}=theta(T_{P_n,Q_n}). Node 1.2.2.2 therefore gives Co_{P_n,Q_n}=Gamma_n(Co_{P,Q})=I_n tensor Co_{P,Q}, where the last expression denotes the entrywise amplification of the operator Co_{P,Q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Range identification: if 1_{M_n} tensor Co_{P,Q}=Co_{P_n,Q_n}, then M_n tensor S_{P,Q}=S_{P_n,Q_n}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Entrywise range lemma: for any linear map C:A->A and finite n, Im(I_n tensor C)=M_n tensor Im(C). Indeed every output has entries C(x_ij), and conversely finitely many entrywise preimages x_ij assemble into one matrix preimage.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** By def-compressed-corner, S_{P,Q}=Im(Co_{P,Q}) and S_{P_n,Q_n}=Im(Co_{P_n,Q_n}); therefore the entrywise range lemma and I_n tensor Co_{P,Q}=Co_{P_n,Q_n} give M_n tensor S_{P,Q}=S_{P_n,Q_n}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

