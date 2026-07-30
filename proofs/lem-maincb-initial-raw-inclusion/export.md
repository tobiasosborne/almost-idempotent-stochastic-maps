# Proof Export

## Node 1

**Statement:** There are universal D_0 < infinity and e_0 > 0 such that, in every finite-dimensional extended epsilon-C*-algebra with epsilon <= t <= e_0, the scalar map lambda |-> lambda*I_A is an extended D_0*t-inclusion; if dim A = 1, it is bijective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix D_0=2 and e_0=1/2. For every n>=1, every scalar matrix X in M_n, and every a in A, the operator-space axioms imply the exact scalar cross-norm identity ||X tensor a||_n=||X|| ||a||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** The operator-space rectangular-matrix axiom gives ||X tensor a||_n=||X(I_n tensor a)I_n||_n <= ||X|| ||I_n tensor a||_n=||X|| ||a||, where the last equality follows by repeated use of the block-diagonal axiom.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Choose unit vectors xi,eta with |eta^* X xi|=||X||. Rectangular compression and the operator-space axiom give ||X tensor a||_n >= ||eta^*(X tensor a)xi||_1=|(eta^*Xxi)| ||a||=||X|| ||a||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For v(lambda)=lambda I_A and v_n=1_{M_n} tensor v, one has v_n(X)=X tensor I_A; v_n is linear, dagger-preserving and unital, while ||v_n(X)v_n(Y)-v_n(XY)||_n <= 2 epsilon ||X|| ||Y|| for all X,Y in M_n when epsilon<=1/2.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.2.1

**Statement:** Conditional repair: suppose, in addition to the registered operator-space data, that A has a bilinear multiplication and a distinguished element I_A such that for every n and X,Y in M_n the amplification v_n(X)=X tensor I_A is linear, (X tensor I_A)(Y tensor I_A)=XY tensor I_A^2, (X tensor I_A)^dagger=X^* tensor I_A (in particular I_A^dagger=I_A), and I_n tensor I_A is the designated target unit; suppose also ||I_A^2-I_A||<=epsilon||I_A||, ||I_A||<=1+epsilon, and ||XY||<=||X||||Y||. Then, once node 1.1 is validated, v_n is linear, dagger-preserving and unital and ||v_n(X)v_n(Y)-v_n(XY)||_n<=2epsilon||X||||Y|| for epsilon<=1/2. These added structural hypotheses are not consequences of the three definitions currently registered in this workspace.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.2.1.1

**Statement:** For the conditional implication, assume exactly the additional structural hypotheses displayed in node 1.2.1: the bilinear multiplication, distinguished I_A, amplified multiplication and involution identities, designated target-unit statement, approximate-unit estimate, upper norm bound, and matrix submultiplicativity. No one of these is inferred from def-operator-space, def-maincb-raw-call, or def-extended-delta-inclusion.

**Type:** local_assume

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.2.1.2

**Statement:** Under those hypotheses, v_n(X)v_n(Y)-v_n(XY)=XY tensor (I_A^2-I_A), v_n(X^*)=v_n(X)^dagger, and v_n(I_n)=I_n tensor I_A is the designated target unit; linearity is one of the displayed hypotheses.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.2.1.3

**Statement:** Using node 1.1 only after it is validated, ||XY tensor (I_A^2-I_A)||_n=||XY|| ||I_A^2-I_A||<=||X||||Y|| epsilon||I_A||<=epsilon(1+epsilon)||X||||Y||<=2epsilon||X||||Y|| when epsilon<=1/2. Together with node 1.2.1.2 this proves the conditional conclusion. It does not prove that an extended epsilon-C*-algebra satisfies the added hypotheses; that missing implication requires definitions not registered in this workspace.

**Type:** qed

**Inference:** assumption

**Status:** archived

**Taint:** clean

### Node 1.3

**Statement:** Conditional repair only: if the scalar cross-norm identity, linearity, dagger preservation, unitality, product defect <=2epsilon||X||||Y||, and the unit bounds 1-epsilon<=||I_A||<=1+epsilon are available, then for epsilon<=t<=1/2 every amplification v_n is a 2t-homomorphism and satisfies (1-2t)||X||<=||v_n(X)||_n<=(1+2t)||X||; hence v is an extended 2t-inclusion by def-extended-delta-inclusion. The currently registered definitions do not establish all of these prerequisites, so this conditional statement does not prove the original unconditional consequence.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.3.1

**Statement:** Assume nodes 1.1, 1.2, and 1.2.1 are validated and, additionally, assume the missing lower unit bound 1-epsilon<=||I_A|| (none of the registered definitions supplies this bound). Then node 1.1 gives ||v_n(X)||_n=||X||||I_A||, while the upper bound ||I_A||<=1+epsilon and epsilon<=t imply (1-2t)||X||<=||v_n(X)||_n<=(1+2t)||X||. Node 1.2 gives linearity, dagger preservation, unitality, and product defect <=2epsilon||X||||Y||<=2t||X||||Y||. Thus the conditional conclusion in node 1.3 follows. This explicitly does not establish the original unconditional claim without the missing extended-algebra axioms and lower unit bound.

**Type:** claim

**Inference:** modus_ponens

**Status:** archived

**Taint:** clean

### Node 1.4

**Statement:** After shrinking the universal radius to e_0=1/4, the extended 2t-inclusion established in node 1.3 implies ||I_A||=||v(1)|| >= (1-2t)||1|| >= 1/2. Hence I_A is nonzero; if dim_C A=1, the linear map v:C->A, lambda|->lambda I_A, is bijective.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.4.1

**Statement:** Assume node 1.3 and take e_0=1/4 (which is allowed because the root asserts existence of a positive universal radius). Since v is then an extended 2t-inclusion, def-extended-delta-inclusion gives at amplification n=1 the lower norm bound ||v(lambda)|| >= (1-2t)||lambda|| for every lambda in C. Setting lambda=1 and using t<=e_0=1/4 yields ||I_A||=||v(1)|| >= 1-2t >= 1/2, so I_A is nonzero. If dim_C A=1, the image of v contains the nonzero vector I_A and therefore equals A; also v(lambda)=0 implies |lambda|*||I_A||=0, hence lambda=0. Thus v is both surjective and injective, hence bijective.

**Type:** claim

**Inference:** modus_ponens

**Status:** archived

**Taint:** clean

### Node 1.5

**Statement:** Let v(lambda)=lambda I_A and v_n=1_{M_n} tensor v. By def-extended-epsilon-cstar-algebra, U_n=I_n tensor I_A is the designated unit of the epsilon-C*-algebra M_n tensor A, so v_n is linear, v_n(I_n)=U_n, and v_n(X^*)=v_n(X)^dagger because I_A^dagger=I_A. Moreover v_n(X)v_n(Y)-v_n(XY)=v_n(XY)U_n-v_n(XY); the defining approximate right-unit axiom at level n, node 1.1, ||XY||<=||X||||Y|| in M_n, and ||I_A||<=1+epsilon give ||v_n(X)v_n(Y)-v_n(XY)||_n<=epsilon||v_n(XY)||_n=epsilon||XY||||I_A||<=epsilon(1+epsilon)||X||||Y||<=2epsilon||X||||Y|| for epsilon<=1/2. Thus every v_n is a 2epsilon-homomorphism.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Take D_0=2 and e_0=1/4. For epsilon<=t<=e_0, node 1.1 and the defining unit-norm bound | ||I_A||-1 |<=epsilon in the epsilon-C*-algebra A give (1-epsilon)||X||<=||v_n(X)||_n=||X||||I_A||<=(1+epsilon)||X||, hence (1-2t)||X||<=||v_n(X)||_n<=(1+2t)||X||. The preceding homomorphism node gives 2epsilon-homomorphism defect at most 2t at every n. Therefore v is an extended 2t-inclusion by def-extended-delta-inclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** If dim_C A=1, the extended 2t-inclusion from the preceding node has at level one ||I_A||=||v(1)||>=(1-2t)||1||>=1/2 because t<=e_0=1/4. Hence I_A is nonzero. The linear map v:C->A is injective since v(lambda)=0 implies |lambda| ||I_A||=0, and it is surjective because its image contains the nonzero vector I_A in the one-dimensional complex space A. Thus v is bijective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

