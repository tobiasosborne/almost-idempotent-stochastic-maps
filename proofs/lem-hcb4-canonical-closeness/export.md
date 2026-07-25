# Proof Export

## Node 1

**Statement:** Canonical Ha closeness: there are universal C_sp < infinity and e_sp > 0 such that every H-CB datum with e <= e_sp satisfies max{||(Ha^Q_{P,Q})_n-J_{P,Q,n}||,||(Ha^Q_{Q,P})_n-J_{Q,P,n}||} <= C_sp*e for every n >= 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Normalized compressed-unit scalar: there are universal A<infinity and e_0>0 such that, for every H-CB datum with e<=e_0, writing u_Q for the compressed unit, alpha=q_Q(u_Q)>0 and q_0=alpha^{-1}u_Q, one has q_Q(q_0)=1 and |alpha-1|<=A e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Unit norm from the permitted corner-algebra input: by one-dimensional-projection-nonvanishing, Q is nonvanishing. Apply lem-compcb-corner-algebra with P=Q. It supplies universal C_ca<infinity and e_ca>0 such that S_Q is an extended gamma-C*-algebra with gamma=C_ca e and unit u_Q. The registered def-extended-epsilon-cstar-algebra and epsilon-banach-cstar-norm-axioms give |||u_Q||-1|<=gamma. Thus, after imposing e<=min{e_ca,1/(2 max{C_ca,1})}, 1/2<=||u_Q||<=3/2 and u_Q is nonzero.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Hilbert normalization from lem-hcb-column-hilbert-squared: apply that result at n=1 with the variable corner P specialized to Q and X=u_Q in S_{Q,Q}. Put alpha=q_Q(u_Q), which is a nonnegative real. The registered column-hilbert-inner-product-displays identify <u_Q,u_Q>=q_Q(u_Q)^2=alpha^2, while the level-one operator-space norm is ||u_Q||. Hence |alpha^2-||u_Q||^2|<=C_col e ||u_Q||^2. If C_col e<=1/2, then alpha>0 and |alpha/||u_Q||-1|<=C_col e, since |sqrt(1+t)-1|<=|t| for |t|<=1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Combine the preceding bounds. For e also satisfying C_ca e<=1/2, |alpha-1|<=|alpha-||u_Q|||+|||u_Q||-1|<=C_col e||u_Q||+C_ca e<=(3C_col/2+C_ca)e. Thus A=2C_col+C_ca works. By the canonical normalization in def-canonical-corner-identifications, q_0=alpha^{-1}u_Q; absolute homogeneity of the Hilbert norm gives q_Q(q_0)=1. Taking e_0 as the minimum of the positive thresholds just used proves node 1.1 with universal A,e_0.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Column special-map estimate: after possibly shrinking the universal threshold, there is a universal C_*<infinity such that every n>=1 and Z in M_n tensor S_{P,Q} satisfy ||(Ha^Q_{P,Q})_n(Z)-J_{P,Q,n}(Z)||_op<=C_* e ||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Adjoint reduction and action estimate. Fix n>=1, Z in M_n tensor S_{P,Q}, and X in M_{n,1} tensor S_{P,Q}; set H=(Ha^Q_{P,Q})_n(Z). By lem-hcb2-amplified-adjointness, H^dagger=(Ha^Q_{Q,P})_n(Z^dagger). By def-canonical-corner-identifications, J_{P,Q,n}(Z)^dagger=J_{Q,P,n}(Z^dagger). Apply lem-hcb1-column-action with its corner variables specialized to (Q,P), its matrix symbol equal to Z^dagger, and its column equal to X. Using the registered self-adjoint operator-space norm axiom ||Z^dagger||=||Z|| gives q_Q((H^dagger X)-(Z^dagger dot X))<=C_act e ||Z|| q_P(X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Exact scalarization of the comparison term. Put d=J_{P,Q,n}(Z)^dagger X in C^n. Entrywise, the registered column-hilbert-inner-product-displays and the defining formula for J give [(Z^dagger dot X)]_i=sum_k Z_{ki}^dagger dot X_k=d_i u_Q. Under the canonical identification by q_0 from node 1.1 this vector is alpha d, whereas J_{P,Q,n}(Z)^dagger X is d. Hence q_Q((Z^dagger dot X)-J_{P,Q,n}(Z)^dagger X)=|alpha-1| ||d||_2. Node 1.1 and lem-hcb4-canonical-gram therefore give this at most A e ||J_{P,Q,n}(Z)|| q_P(X)<=A e(1+C_J e)||Z|| q_P(X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Combine nodes 1.2.1 and 1.2.2 by the triangle inequality. If e is at most e_0, e_act, e_adj, e_J, and 1/max{C_J,1}, then for every X, q_Q((H^dagger-J_{P,Q,n}(Z)^dagger)X)<=(C_act+2A)e||Z||q_P(X). Taking the supremum over X nonzero gives ||H^dagger-J_{P,Q,n}(Z)^dagger||_op<=C_*e||Z|| for C_*=C_act+2A. Hilbert-space adjunction preserves operator norm, so ||H-J_{P,Q,n}(Z)||_op has the same bound. All constants and the threshold are universal and independent of n, proving node 1.2.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Row transfer and completion: under the same universal threshold and constant, every n>=1 and W in M_n tensor S_{Q,P} satisfy ||(Ha^Q_{Q,P})_n(W)-J_{Q,P,n}(W)||_op<=C_* e ||W||; taking suprema over nonzero Z and W proves the root with C_sp=C_* and the common positive threshold e_sp.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Fix n>=1 and W in M_n tensor S_{Q,P}. Apply lem-hcb2-amplified-adjointness to Z=W^dagger in M_n tensor S_{P,Q}: (Ha^Q_{Q,P})_n(W)=((Ha^Q_{P,Q})_n(W^dagger))^dagger. By def-canonical-corner-identifications, J_{Q,P,n}(W)=J_{P,Q,n}(W^dagger)^dagger. Thus adjoint norm invariance, node 1.2, and ||W^dagger||=||W|| give ||(Ha^Q_{Q,P})_n(W)-J_{Q,P,n}(W)||_op<=C_*e||W||. Taking the operator norm in the matrix variable (the supremum over nonzero W) gives ||(Ha^Q_{Q,P})_n-J_{Q,P,n}||<=C_*e; node 1.2 similarly gives the P,Q map norm. Therefore their maximum is at most C_*e for every n. Choose e_sp as the positive minimum of all thresholds in nodes 1.1 and 1.2 and the adjointness threshold, and C_sp=C_*. This proves the root.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

