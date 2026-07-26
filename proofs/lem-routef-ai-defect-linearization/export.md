# Proof Export

## Node 1

**Statement:** Approximate-algebra defect linearization: set C_theta=12*(sqrt(2)-1). There are universal C_A < infinity and eta_A > 0, with C_A=20+(211/8)*C_theta, such that for every nonzero Hilbert space H, every UCP map Phi:B(H)->B(H), and every eta satisfying 0 <= eta <= eta_A and ||Phi^2-Phi||_cb <= eta, if tilde-Phi=(1/2)*(I+(2*Phi-I)*(I-4*(Phi-Phi^2))^(-1/2)), A=Im(tilde-Phi), X star Y=tilde-Phi(XY), r=(3/2)*((1-4*eta)^(-1/2)-1), and epsilon_AI(eta)=max{r,20*eta+2*((1+r)^5-1),3*r-r^2}, then the inherited operator-space norms, involution, and unit together with star make A an extended epsilon_AI(eta)-C*-algebra and epsilon_AI(eta) <= C_A*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** By lem-kitaev-almost-idemp-audit, there is a universal eta_* > 0 such that, after shrinking eta_* below 1/4 if necessary, under that lemma's hypotheses and notation and for 0 <= eta <= eta_*, A=Im(tilde-Phi) is an extended epsilon_AI(eta)-C*-algebra with epsilon_AI(eta)=max{r,20eta+2(M^5-1),3r-r^2}, where r=(3/2)((1-4eta)^(-1/2)-1) and M=1+r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For the constant C_theta=12*(sqrt(2)-1) fixed by lem-routef-functional-calculus-closeness, every 0 <= eta <= 7/64 satisfies 0 <= r <= C_theta*eta, r <= 1/2, and 2*((1+r)^5-1) <= (211/8)*r, where r=(3/2)*((1-4eta)^(-1/2)-1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** The external lemma lem-routef-functional-calculus-closeness fixes C_theta=12*(sqrt(2)-1); in particular C_theta is a positive universal constant because sqrt(2)>1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For eta=0 one has r=0. For 0<eta<=7/64<1/8, put t=sqrt(1-4eta). Then r/eta=6/(t*(1+t)) and t>=1/sqrt(2), so r/eta<=12/(sqrt(2)+1)=12*(sqrt(2)-1)=C_theta. Thus 0<=r<=C_theta*eta throughout 0<=eta<=7/64.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** If 0<=eta<=7/64, then 1-4eta>=9/16, so (1-4eta)^(-1/2)<=4/3 and therefore r=(3/2)*((1-4eta)^(-1/2)-1)<=1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** For 0<=r<=1/2, the binomial identity gives 2*((1+r)^5-1)=2*r*(5+10*r+10*r^2+5*r^3+r^4). The parenthesized polynomial is increasing for r>=0 and at r=1/2 equals 211/16, hence 2*((1+r)^5-1)<=(211/8)*r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The conclusions of nodes 1.1 and 1.2 imply the root contract: choose eta_A=min{eta_*,7/64} and C_A=20+(211/8)*C_theta; then eta_A>0 is universal, A is the required extended epsilon_AI(eta)-C*-algebra for 0 <= eta <= eta_A, and epsilon_AI(eta) <= C_A*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** With eta_A=min{eta_*,7/64}, eta_A is universal and strictly positive; for every 0<=eta<=eta_A, node 1.1 applies because eta<=eta_*, and all estimates in node 1.2 apply because eta<=7/64.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Using M=1+r and node 1.2, 20*eta+2*(M^5-1) <= 20*eta+(211/8)*r <= (20+(211/8)*C_theta)*eta=C_A*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Since C_theta>0, C_A-C_theta=20+(203/8)*C_theta>0 and C_A-3*C_theta=20+(187/8)*C_theta>0. Thus node 1.2 gives r<=C_A*eta and 3*r-r^2<=3*r<=C_A*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** For 0<=eta<=eta_A, node 1.1 supplies the extended epsilon_AI(eta)-C*-algebra structure and the displayed maximum formula. Nodes 1.3.2 and 1.3.3 bound every entry of that maximum by C_A*eta, so epsilon_AI(eta)<=C_A*eta; this is exactly the root conclusion with the stated C_A and eta_A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Let eta_* > 0 be the universal threshold supplied by node 1.1, already shrunk below 1/4, and set eta_A=min{eta_*,7/64}. Fix an arbitrary nonzero Hilbert space H, an arbitrary UCP map Phi:B(H)->B(H), and eta with 0<=eta<=eta_A and ||Phi^2-Phi||_cb<=eta; define tilde-Phi, A, star, r, and epsilon_AI(eta) exactly as in the amended root. Then eta<=eta_* and eta<1/4, so all hypotheses of node 1.1 are satisfied and it gives the stated extended epsilon_AI(eta)-C*-algebra structure with epsilon_AI(eta)=max{r,20*eta+2*((1+r)^5-1),3*r-r^2}. Also eta<=7/64, so node 1.2 gives 0<=r<=C_theta*eta, r<=1/2, and 2*((1+r)^5-1)<=(211/8)*r. Therefore 20*eta+2*((1+r)^5-1)<=(20+(211/8)*C_theta)*eta=C_A*eta. Moreover C_A-C_theta=20+(203/8)*C_theta>0 and C_A-3*C_theta=20+(187/8)*C_theta>0, whence r<=C_A*eta and 3*r-r^2<=3*r<=C_A*eta. Every entry in the displayed maximum is thus at most C_A*eta. Since H, Phi, and eta were arbitrary under the amended hypotheses, this proves the amended root; eta_A is positive and universal because eta_* is.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

