# Proof Export

## Node 1

**Statement:** Uniform square lower estimate: there are universal K_sq < infinity and e_sq > 0 such that every H-CB datum with e <= e_sq, every n >= 1, and every Z in M_n tensor S_P satisfy ||Z^dagger dot Z|| >= (1-K_sq*e)||Z||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Vanishing-corner alternative: there are universal C_v<infinity and e_v>0 such that, for e=delta+epsilon<=e_v, if the delta-projection P is not nonvanishing, then its compression Co_P is zero and hence S_P={0}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Quantitative first alternative: the registered nonvanishing-delta-projection dichotomy supplies universal C_v<infinity and e_0>0 such that, when e<=e_0 and P is not nonvanishing, ||P||<=C_v*delta. For T=L_P R_P+R_P L_P, the epsilon-Banach product bound gives ||T||<=2(1+epsilon)^2||P||^2<=2(1+e)^2 C_v^2 e^2; after a universal shrink e<=e_v this is <1/3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Theta calculation: for any bounded operator T with ||T||<1/3, the registered power-series calculus gives sgn(T-I)=-I and hence theta(T-I)=(I+sgn(T-I))/2=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** Put U=I-T and X=T-I=-U. Since ||T||<1/3, U is invertible by its Neumann series and ||X^2-I||=||-2T+T^2||<=2||T||+||T||^2<7/9<1, so the registered sign power series applies. The same binomial power series gives (X^2)^(-1/2)=(U^2)^(-1/2)=U^(-1), because both sides are the convergent power-series branch equal to I at T=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.2

**Statement:** Put U=I-T and X=T-I=-U. The children establish (X^2)^(-1/2)=U^(-1) directly from ||T||<1/3. Hence the registered formulas sgn(X)=X(X^2)^(-1/2) and theta(X)=(I+sgn(X))/2 give sgn(T-I)=(-U)U^(-1)=-I and theta(T-I)=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.2.1

**Statement:** Let U=I-T and X=T-I=-U. Since ||T||<1/3, the Neumann series sum_{k>=0} T^k converges absolutely and is U^(-1). Also W:=X^2-I=U^2-I=-2T+T^2 has ||W||<=2||T||+||T||^2<7/9<1, so the registered binomial power series defining (X^2)^(-1/2) converges absolutely. In the scalar disc |z|<1/3, the branch normalized to 1 at z=0 satisfies ((1-z)^2)^(-1/2)=(1-z)^(-1)=sum_{k>=0}z^k: indeed Re(1-z)>0, so the normalized square root of (1-z)^2 is 1-z. Thus the two sides have identical Taylor series at 0; evaluating these absolutely convergent series at the single Banach-algebra element T gives (X^2)^(-1/2)=U^(-1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.1.2.2.2

**Statement:** By the preceding child and X=-U, the registered formula gives sgn(X)=X(X^2)^(-1/2)=(-U)U^(-1)=-I. Therefore theta(X)=(I+sgn(X))/2=0; since X=T-I, this is exactly sgn(T-I)=-I and theta(T-I)=0.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Conclusion of the vanishing alternative: the registered compression construction is Co_P=theta(L_P R_P+R_P L_P-I)=theta(T-I), and S_P=Img(Co_P). Nodes 1.1.1-1.1.2 therefore give Co_P=0 and S_P={0} whenever P is not nonvanishing and e<=e_v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.1

**Statement:** Dependency bridge for the essential premise: under e<=e_v and P not nonvanishing, node 1.1.1 gives, for T=L_P R_P+R_P L_P, ||T||<1/3; node 1.1.2 then gives theta(T-I)=0. This bridge depends explicitly on both sibling results and is unavailable for acceptance until both are validated.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.1.3.2

**Statement:** By the registered compression construction, Co_P=theta(L_P R_P+R_P L_P-I)=theta(T-I). Substituting theta(T-I)=0 from node 1.1.3.1 gives Co_P=0. Since S_P=Img(Co_P), the image of the zero operator is {0}, so S_P={0}.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

###### Node 1.1.3.2.1

**Statement:** Independent validated-premise discharge: assume e<=e_v and P is not nonvanishing, and put T=L_P R_P+R_P L_P. Validated node 1.1.1 gives ||T||<1/3. Universally instantiate validated node 1.1.2.2 at this T to obtain theta(T-I)=0. The registered compression construction then gives Co_P=theta(L_P R_P+R_P L_P-I)=theta(T-I)=0. Since S_P=Img(Co_P), it follows that S_P=Img(0)={0}. Thus the conclusion of node 1.1.3.2 is established without using pending node 1.1.3.1.

**Type:** qed

**Inference:** local_discharge

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Nonvanishing-corner square bound: if e<=e_ca and P is nonvanishing, then lem-compcb-corner-algebra and the extended-C*-algebra axioms give, for every n>=1 and Z in M_n tensor S_P, ||Z^dagger dot Z|| >= (1-C_ca*e)||Z||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** By the exact external lem-compcb-corner-algebra, there are universal C_ca<infinity and e_ca>0 such that, when e<=e_ca and P is a nonvanishing delta-projection, S_P with compressed product dot, inherited involution dagger, and compressed unit is an extended (C_ca*e)-C*-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** By def-extended-epsilon-cstar-algebra, the conclusion of node 1.2.1 means that every M_n tensor S_P is a (C_ca*e)-C*-algebra with the amplified compressed product and inherited involution. Its registered lower C*-axiom, applied to Z, is exactly ||Z^dagger dot Z|| >= (1-C_ca*e)||Z||^2, uniformly in n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Constant choice and exhaustion of cases: set K_sq=C_ca and e_sq=min{e_ca,e_v,1/(2*max{1,C_ca})}>0. For any H-CB datum with e<=e_sq, if P is nonvanishing then node 1.2 gives the required inequality. Otherwise node 1.1 gives S_P={0}, so M_n tensor S_P={0}, Z=0, and both sides of the required inequality are zero. The two cases exhaust P and prove the root contract for every n.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Validation-gated case discharge: require nodes 1.1 and 1.2 to be validated. Fix any H-CB datum with e<=e_sq, any n>=1, and any Z in M_n tensor S_P. Since e_sq<=e_v and e_sq<=e_ca, either P is nonvanishing, in which case validated node 1.2 yields ||Z^dagger dot Z|| >= (1-C_ca*e)||Z||^2 = (1-K_sq*e)||Z||^2, or P is not nonvanishing, in which case validated node 1.1 yields S_P={0}, hence Z=0 and the same inequality reads 0>=0. These complementary cases establish the asserted estimate for all n and Z.

**Type:** qed

**Inference:** local_discharge

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Endpoint check for the nonvanishing case: the live validated statement of node 1.2 assumes e<=e_ca. Since e<=e_sq and e_sq=min{e_ca,e_v,1/(2*max{1,C_ca})}, one has e<=e_sq<=e_ca. Therefore node 1.2 applies even when e=e_sq=e_ca and yields ||Z^dagger dot Z|| >= (1-C_ca*e)||Z||^2=(1-K_sq*e)||Z||^2 because K_sq=C_ca; no boundary point is omitted.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

