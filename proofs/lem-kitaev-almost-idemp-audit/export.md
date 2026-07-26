# Proof Export

## Node 1

**Statement:** Corrected th_almost_idemp audit: let H be nonzero and let Phi:B(H)->B(H) be UCP with ||Phi^2-Phi||_cb <= eta < 1/4; for tilde-Phi=(1/2)(I+(2Phi-I)(I-4(Phi-Phi^2))^(-1/2)), A=Im(tilde-Phi), and X star Y=tilde-Phi(XY), one has tilde-Phi^2=tilde-Phi, both amplified associativity identities Phi_assoc1 and Phi_assoc2 have error at most 10*eta*||X||||Y||||Z|| after the local source type/index corrections, and for sufficiently small universal eta the inherited operator-space norms, involution, and unit make A an extended epsilon_AI(eta)-C*-algebra with epsilon_AI=max{r,20eta+2(M^5-1),3r-r^2}=O(eta), r=(3/2)((1-4eta)^(-1/2)-1), M=1+r, dimension-free at every amplification.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Spectral-correction package: in the Banach algebra of completely bounded maps under composition, F=Phi-Phi^2 has norm_cb at most eta, A0=2Phi-I satisfies A0^2=I-4F, B=(I-4F)^(-1/2) is given by the convergent binomial series, S=A0 B satisfies S^2=I, and tilde-Phi=(I+S)/2 is an idempotent unital star-preserving map with ||tilde-Phi-Phi||_cb at most r=(3/2)((1-4eta)^(-1/2)-1); consequently its image is a closed complete self-adjoint operator space containing I, and r=O(eta) universally.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Functional calculus calculation: set F=Phi-Phi^2 and A0=2Phi-I. Since F is a polynomial in Phi, A0 and F commute, A0^2=I-4F, and ||4F||_cb<1. The norm-convergent binomial series B=sum_{k>=0} binom(2k,k)F^k satisfies B=(I-4F)^(-1/2), B^2=(I-4F)^(-1), and commutes with A0. Thus S=A0B has S^2=I and P=(I+S)/2 has P^2=P. Moreover P-Phi=(1/2)A0(B-I), ||A0||_cb<=2||Phi||_cb+1<=3, and positivity of the scalar series coefficients gives ||B-I||_cb<=sum_{k>=1} binom(2k,k)eta^k=(1-4eta)^(-1/2)-1, hence ||P-Phi||_cb<=r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Structure and asymptotics: UCP implies Phi(I)=I and Phi(X^*)=Phi(X)^*. Therefore F(I)=0, B(I)=I, A0(I)=I and P(I)=I; the real-coefficient series and composition show P(X^*)=P(X)^*. A bounded idempotent has Im(P)=Ker(I-P), so its image is closed, complete in the inherited norm, self-adjoint, contains I, and its restricted matrix norms form the inherited complete operator-space structure. The same formulas commute with every matrix amplification. Finally, for 0<=eta<=1/8 the mean-value theorem gives r<=6 sqrt(2) eta, so r=O(eta) with a universal dimension-free constant.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** First amplified associativity identity: for every n and T=I_Mn tensor Phi on B(C^n tensor H), and all X,Y,Z at that level, ||T(T(T(X)T(Y))T(Z))-T(T(X)T(Y)T(Z))|| is at most 10 eta ||X||||Y||||Z||; the proof uses an internal, explicitly typed Stinespring-stack rectangle factorization and only UCP plus ||T^2-T|| at most eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Elementary uniform defect ledger: at a fixed matrix level T is UCP, hence ||T||<=1 and T(U^*)=T(U)^*, while D=T^2-T has ||D||<=eta. Thus ||T^2(U)-T(U)||<=eta||U|| and, by inserting T(U)T^2(V), ||T^2(U)T^2(V)-T(U)T(V)||<=2eta||U||||V||. Consequently G_X=T^2(T(X^*)T(X))-T(T^2(X^*)T^2(X)) has ||G_X||<=3eta||X||^2. These estimates use no dimension, trace, Kraus sum, or ancillary basis.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Internal Stinespring rectangle and correction ledger: the iterative GNS/Stinespring construction for UCP T gives Hilbert spaces K_j, isometries V_j:K_{j-1}->K_j, and contractive unital star-homomorphisms u_j:B(K_{j-1})->B(K_j), with the one-step compression identity u_j(V_j^*UV_j)=V_{j+1}^*u_{j+1}(U)V_{j+1} for U in B(K_j), and its iterates. All four source memberships are therefore U in B(K_j), never U in K_j. For R_k(X)=u_{2+k,1}((I_1-V_1V_1^*)u_1(T(X)))V_{2+k}V_{1+k}, exact multiplication and the iterated compression identity give R_k(X)^*R_k(X)=u_{k,0}(G_X), hence ||R_k(X)||<=sqrt(3eta)||X||. The auxiliary identity has final factor V_{1+k}: V_{1+k}^*V_{2+k}^*u_{2+k,1}(Z)V_{2+k}V_{1+k}=V_{1+k}^*u_{1+k,0}(V_1^*ZV_1)V_{1+k}; using V_1 there is ill-typed. With A=T(X), B=T(Y), C=T(Z), A1=T^2(X), B1=T^2(Y), C1=T^2(Z), the operator W=V_1^*R_1(X^*)^*u_{3,0}(T(Y))V_3R_0(Z) obeys ||W||<=3eta||X||||Y||||Z||, and expanding both I_1-V_1V_1^* factors then compressing gives exactly W=T(Q), Q=T(T(AB)C)-T^2(AB)C1-T(A1B1C)+T(A1B1)C1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Explicit recursive dilation, proved from complete positivity rather than imported: for any Hilbert space K and UCP map Psi:B(K)->B(K), put on the algebraic tensor product B(K) tensor K the semidefinite form <sum_i A_i tensor xi_i, sum_j B_j tensor eta_j>=sum_ij <xi_i,Psi(A_i^*B_j)eta_j>. Complete positivity of Psi makes this form positive because [A_i^*A_j] is a positive operator matrix. After quotienting its null space and completing, define pi(C)[A tensor xi]=[CA tensor xi] and Vxi=[I tensor xi]. The inequality C^*C<=||C||^2 I makes pi(C) bounded with norm at most ||C||; the defining form gives pi(C)^*=pi(C^*), pi(CD)=pi(C)pi(D), and pi(I)=I. Unitality gives V^*V=I, and direct evaluation gives V^*pi(C)V=Psi(C). Apply this construction first to Psi_0=T on B(K_0), obtaining (K_1,u_1,V_1), and recursively to the UCP map Psi_j:B(K_j)->B(K_j), Psi_j(U)=u_j(V_j^*UV_j), obtaining (K_{j+1},u_{j+1},V_{j+1}). Thus each V_j:K_{j-1}->K_j is an isometry, each u_j:B(K_{j-1})->B(K_j) is a contractive unital star-homomorphism, T(H)=V_1^*u_1(H)V_1, and for every j>=1 and U in B(K_j), u_j(V_j^*UV_j)=V_{j+1}^*u_{j+1}(U)V_{j+1}. This proves the claimed iterative system with the source type U in B(K_j), without an external Stinespring axiom.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** Self-contained rectangle and defect calculation: let T:B(K_0)->B(K_0) be UCP with ||T^2-T||<=eta and let (K_j,u_j,V_j) be any iterative system furnished by the preceding explicit construction. For b>a define u_{b,a}=u_b o ... o u_{a+1} and u_{a,a}=id; write I_j for the identity of K_j and P_1=V_1V_1^*. Induction in the one-step compression identity gives, for k>=0, H in B(K_0), and Z in B(K_1), (i) V_{k+1}^*u_{k+1,0}(H)V_{k+1}=u_{k,0}(T(H)), and (ii) V_{k+2}^*u_{k+2,1}(Z)V_{k+2}=u_{k+1,0}(V_1^*ZV_1). Hence the fully typed auxiliary identity is V_{k+1}^*V_{k+2}^*u_{k+2,1}(Z)V_{k+2}V_{k+1}=V_{k+1}^*u_{k+1,0}(V_1^*ZV_1)V_{k+1}; its final factor must be V_{k+1}, since V_1 has domain K_0 rather than K_k when k>0. Put E_X=(I_1-P_1)u_1(T(X)) in B(K_1) and H_X=V_1^*E_X^*E_XV_1. Multiplicativity of u_1 and T(U)=V_1^*u_1(U)V_1 give exactly H_X=T(T(X^*)T(X))-T^2(X^*)T^2(X). Define G_X=T(H_X)=T^2(T(X^*)T(X))-T(T^2(X^*)T^2(X)). Contractivity and the defect estimate give ||T^2(T(X^*)T(X))-T(T(X^*)T(X))||<=eta||X||^2 and ||T(T(X^*)T(X)-T^2(X^*)T^2(X))||<=2eta||X||^2, the latter by adding and subtracting T(X^*)T^2(X); therefore ||G_X||<=3eta||X||^2. For R_k(X)=u_{k+2,1}(E_X)V_{k+2}V_{k+1}, exact multiplication followed by (ii) and then (i) yields R_k(X)^*R_k(X)=V_{k+1}^*u_{k+1,0}(H_X)V_{k+1}=u_{k,0}(T(H_X))=u_{k,0}(G_X). Since star-homomorphisms are contractive, ||R_k(X)||^2<=||G_X||, so ||R_k(X)||<=sqrt(3eta)||X||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.3

**Statement:** Exact W expansion with all symbols declared: under the same iterative system, set A=T(X), B=T(Y), C=T(Z), A_1=T(A)=T^2(X), B_1=T(B)=T^2(Y), C_1=T(C)=T^2(Z), P_1=V_1V_1^*, and E_U=(I_1-P_1)u_1(T(U)). Then R_0(Z)=u_{2,1}(E_Z)V_2V_1 and R_1(X^*)=u_{3,1}(E_{X^*})V_3V_2, with E_{X^*}^*=u_1(A)(I_1-P_1). Put D=V_1^*u_1(A)(I_1-P_1)u_1(B)V_1=T(AB)-A_1B_1. For W=V_1^*R_1(X^*)^*u_{3,0}(B)V_3R_0(Z), multiplicativity and the two compression identities give the explicit chain W=V_1^*V_2^*u_2(u_1(D)(I_1-P_1)u_1(C))V_2V_1=T(V_1^*u_1(D)(I_1-P_1)u_1(C)V_1)=T(T(DC)-T(D)C_1). Substituting D and using linearity yields W=T(Q), where Q=T(T(AB)C)-T^2(AB)C_1-T(A_1B_1C)+T(A_1B_1)C_1, exactly as claimed. Finally, the rectangle bound from the preceding calculation and contractivity of u_{3,0} give ||W||<=||R_1(X^*)|| ||B|| ||R_0(Z)||<=sqrt(3eta)||X|| ||Y|| sqrt(3eta)||Z||=3eta||X||||Y||||Z||. Thus neither W=T(Q) nor its norm estimate is an undeclared premise.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.2.3.1

**Statement:** Local derivation of the two rectangle estimates, with no sibling imported. Let U be any operator on K_0. From the one-step compression identity of the iterative system, induction gives V_{k+2}^*u_{k+2,1}(Z)V_{k+2}=u_{k+1,0}(V_1^*ZV_1) for Z in B(K_1), and V_{k+1}^*u_{k+1,0}(H)V_{k+1}=u_{k,0}(T(H)) for H in B(K_0). Put E_U=(I_1-P_1)u_1(T(U)), H_U=V_1^*E_U^*E_UV_1, and G_U=T(H_U). Multiplicativity and T(H)=V_1^*u_1(H)V_1 yield H_U=T(T(U^*)T(U))-T^2(U^*)T^2(U), hence G_U=T^2(T(U^*)T(U))-T(T^2(U^*)T^2(U)). Writing V=T(U^*)T(U), the first difference [T^2(V)-T(V)] has norm at most eta||U||^2. Moreover T(U^*)T(U)-T^2(U^*)T^2(U)=T(U^*)[T(U)-T^2(U)]+[T(U^*)-T^2(U^*)]T^2(U), so contractivity of T and T^2 and ||T^2-T||<=eta bound the norm of its image under T by 2eta||U||^2. Thus ||G_U||<=3eta||U||^2. For R_k(U)=u_{k+2,1}(E_U)V_{k+2}V_{k+1}, exact multiplication followed by the two displayed compression identities gives R_k(U)^*R_k(U)=u_{k,0}(G_U). Contractivity of the star-homomorphism u_{k,0} therefore gives ||R_k(U)||<=sqrt(3eta)||U||. In particular ||R_1(X^*)||<=sqrt(3eta)||X|| and ||R_0(Z)||<=sqrt(3eta)||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.2.3.2

**Statement:** Complete W conclusion using the locally proved rectangle estimates. With the target node notation, multiplicativity and the two compression identities give D=V_1^*u_1(A)(I_1-P_1)u_1(B)V_1=T(AB)-A_1B_1 and W=V_1^*V_2^*u_2(u_1(D)(I_1-P_1)u_1(C))V_2V_1=T(V_1^*u_1(D)(I_1-P_1)u_1(C)V_1)=T(T(DC)-T(D)C_1). Substitution of D and linearity give W=T(Q), Q=T(T(AB)C)-T^2(AB)C_1-T(A_1B_1C)+T(A_1B_1)C_1. By the preceding child, contractivity of T and u_{3,0}, ||B||<=||Y||, and the isometry norms, ||W||<=||R_1(X^*)|| ||B|| ||R_0(Z)||<=3eta||X||||Y||||Z||. Thus both the exact expansion and the norm conclusion follow without importing the sibling rectangle node.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Five-plus-two eta reduction and conclusion: for F1=T(T(AB)C)-T(ABC), the last two paired terms in Q satisfy ||T(A1B1)-T^2(AB)||<=||A1B1-AB||+||T(AB)-T^2(AB)||<=3eta||X||||Y||, while ||T(A1B1C)-T(ABC)||<=2eta||X||||Y||||Z||. Hence ||Q-F1||<=5eta||X||||Y||||Z||. Contractivity gives ||T(Q)-T(F1)||<=5eta product, and because F1 is a difference of two T-valued terms, the defect estimate applied once to each gives ||T(F1)-F1||<=2eta product. Therefore ||W-F1||<=7eta product; together with ||W||<=3eta product this yields ||F1||<=10eta||X||||Y||||Z||, exactly Phi_assoc1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** Fixed-level scope and rectangle input: fix n and X,Y,Z in B(C^n tensor H), set T=I_Mn tensor Phi, A=T(X), B=T(Y), C=T(Z), A1=T^2(X), B1=T^2(Y), C1=T^2(Z), and p=||X||||Y||||Z||. By node 1.2.1, ||T||<=1 and ||T^2(U)-T(U)||<=eta||U||. Using the Stinespring objects V_j,u_j,R_k defined in node 1.2.2, set W=V_1^* R_1(X^*)^* u_{3,0}(T(Y)) V_3 R_0(Z) and Q=T(T(AB)C)-T^2(AB)C1-T(A1B1C)+T(A1B1)C1. The exact expansion in node 1.2.2 gives W=T(Q) and ||W||<=3eta p.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.3.1.1

**Statement:** Self-contained exact expansion, independent of pending node 1.2.2: in the fixed-level notation of 1.2.3.1 use the validated recursive dilation of 1.2.2.1, write u_{b,a}=u_b o ... o u_{a+1}, P_1=V_1V_1^*, E_U=(I_1-P_1)u_1(T(U)), R_0(Z)=u_{2,1}(E_Z)V_2V_1, and R_1(X^*)=u_{3,1}(E_{X^*})V_3V_2. Star preservation gives E_{X^*}^*=u_1(A)(I_1-P_1). Set D=V_1^*u_1(A)(I_1-P_1)u_1(B)V_1=T(AB)-A_1B_1. Multiplicativity and the validated compression identity first give W=V_1^*V_2^*u_2(u_1(D)(I_1-P_1)u_1(C))V_2V_1, then W=T(V_1^*u_1(D)(I_1-P_1)u_1(C)V_1)=T(T(DC)-T(D)C_1). Since D=T(AB)-A_1B_1, linearity gives W=T(T(T(AB)C)-T^2(AB)C_1-T(A_1B_1C)+T(A_1B_1)C_1)=T(Q). Every product is typed in the operator algebras B(K_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.3.1.2

**Statement:** Self-contained norm estimate using only validated nodes: node 1.2.2.2 proves for the same explicitly defined rectangles that ||R_k(U)||<=sqrt(3eta)||U||. Since V_1 and V_3 are isometries and u_{3,0} is contractive, ||W||<=||R_1(X^*)|| ||u_{3,0}(B)|| ||R_0(Z)||<=sqrt(3eta)||X|| ||B|| sqrt(3eta)||Z||. Node 1.2.1 gives ||B||=||T(Y)||<=||Y||; hence ||W||<=3eta||X||||Y||||Z||=3eta p. This does not invoke the pending parent 1.2.2 or pending sibling 1.2.2.3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.2

**Statement:** Elementary perturbation estimates: contractivity of T and T^2 gives ||A||,||A1||<=||X||, ||B||,||B1||<=||Y||, and ||C||,||C1||<=||Z||. Also ||A1-A||<=eta||X|| and ||B1-B||<=eta||Y||. Hence A1B1-AB=(A1-A)B1+A(B1-B), so ||A1B1-AB||<=2eta||X||||Y||. Consequently ||T(A1B1C)-T(ABC)||<=||(A1B1-AB)C||<=2eta p, and ||T(A1B1)-T^2(AB)||<=||T(A1B1)-T(AB)||+||T(AB)-T^2(AB)||<=2eta||X||||Y||+eta||AB||<=3eta||X||||Y||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.3

**Statement:** Exact five-eta decomposition: with F1=T(T(AB)C)-T(ABC), direct cancellation in the displayed definition of Q gives Q-F1=[T(ABC)-T(A1B1C)]+[T(A1B1)-T^2(AB)]C1. Therefore the preceding estimates and ||C1||<=||Z|| give ||Q-F1||<=2eta p+3eta p=5eta p.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.4

**Statement:** Two-eta defect correction and conclusion: write R=T(AB)C and S=ABC, so F1=T(R)-T(S). Then T(F1)-F1=[T^2(R)-T(R)]-[T^2(S)-T(S)], whence ||T(F1)-F1||<=eta(||R||+||S||)<=2eta p because ||T(AB)||<=||A||||B|| and ||A||<=||X||, ||B||<=||Y||, ||C||<=||Z||. Since W=T(Q), contractivity and the five-eta bound give ||W-F1||<=||T(Q)-T(F1)||+||T(F1)-F1||<=5eta p+2eta p=7eta p. Finally ||F1||<=||W||+||W-F1||<=10eta p; substituting A=T(X), B=T(Y), C=T(Z) identifies F1 exactly with the Phi_assoc1 difference in node 1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Adjoint reduction for the second identity: for every star-preserving T, the first associativity estimate applied to (Z^*,Y^*,X^*) and then adjointed is exactly ||T(T(X)T(T(Y)T(Z)))-T(T(X)T(Y)T(Z))|| at most the same constant times ||X||||Y||||Z||; hence Phi_assoc2 follows from Phi_assoc1 with constant 10 at every amplification.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Extended approximate C-star package: writing P=tilde-Phi, d=||P-Phi||_cb at most r and M=1+r, the inherited matrix norms, involution and unit and the product X star Y=P(XY) make every M_n tensor Im(P) an epsilon_AI-algebra with exact unit and involution, submultiplicativity error r, associativity error at most 20eta+2(M^5-1), and C-star lower-norm error at most 3r-r^2; for sufficiently small universal eta their maximum epsilon_AI is less than 1, is O(eta), and all constants are independent of n and dim(H).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** All nonassociative axioms with explicit errors: at each matrix level let T=I_Mn tensor Phi and P=I_Mn tensor tilde-Phi, so ||P-T||<=r and ||P||<=M. The range of P is a closed complete self-adjoint operator space; P(I)=I, P is star-preserving, and P^2=P. Hence X star Y=P(XY) is bilinear and range-valued, I is an exact unit, and (X star Y)^*=Y^* star X^*. Also ||X star Y||<=M||X||||Y||, giving submultiplicativity error r. For X in Im(P), ||T(X)||>=||X||-r||X||=(1-r)||X||; UCP Schwarz gives ||T(X^*X)||>=||T(X)||^2, and therefore ||P(X^*X)||>=||T(X^*X)||-r||X||^2>=(1-3r+r^2)||X||^2. Thus the C-star lower-norm error is 3r-r^2 for small r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Associativity, amplification, and packaging under def-extended-epsilon-cstar-algebra: put L_P=P(P(P(X)P(Y))P(Z)) and R_P=P(P(X)P(P(Y)P(Z))). Telescoping replacement of the five map occurrences, using ||T||<=1, ||P||<=M and ||P-T||<=r=M-1, gives ||L_P-L_T|| and ||R_P-R_T|| each at most (M^5-1)||X||||Y||||Z||. Phi_assoc1 and Phi_assoc2 put L_T and R_T within 10eta product of the same T(T(X)T(Y)T(Z)), so ||L_P-R_P||<=(20eta+2(M^5-1)) product. For X,Y,Z in Im(P), L_P=(X star Y) star Z and R_P=X star (Y star Z). Taking the maximum of this error, r, and 3r-r^2 verifies every epsilon-C-star axiom at every matrix level, and the complete self-adjoint operator-space, multiplication and unit therefore satisfy def-extended-epsilon-cstar-algebra. Since r=O(eta), M^5-1<=31r for 0<=r<=1, and all displayed errors tend to zero, a universal eta_0>0 makes epsilon_AI<1 and epsilon_AI=O(eta), uniformly in n and dim(H).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.2.1

**Statement:** Dependency-explicit bridge. Require validated nodes 1.2, 1.3, and 1.4.1. Fix an amplification n and abbreviate q=||X||||Y||||Z||. Node 1.2 gives ||L_T-C_T||<=10 eta q for L_T=T(T(T(X)T(Y))T(Z)) and C_T=T(T(X)T(Y)T(Z)); node 1.3 gives ||R_T-C_T||<=10 eta q for R_T=T(T(X)T(T(Y)T(Z))). For either of the five-occurrence expressions L or R, replace its occurrences of P one at a time by T. Multilinearity of composition and multiplication, ||T||<=1, ||P||<=M, and ||P-T||<=r show that the term in which the j-th occurrence is replaced has norm at most r M^j q for some j in {0,1,2,3,4}; hence each telescoping sum is at most r(1+M+M^2+M^3+M^4)q=(M^5-1)q because M=1+r. Therefore ||L_P-R_P||<=||L_P-L_T||+||L_T-C_T||+||C_T-R_T||+||R_T-R_P||<=(20 eta+2(M^5-1))q. If X,Y,Z lie in Im(P), idempotence of P identifies L_P=(X star Y) star Z and R_P=X star (Y star Z). Node 1.4.1 supplies at this same arbitrary matrix level the complete self-adjoint operator-space structure, range-valued bilinear multiplication, exact unit and involution, submultiplicativity error r, and C-star lower-norm error 3r-r^2. Thus, with epsilon_AI=max{r,20 eta+2(M^5-1),3r-r^2}, every amplification has all the required epsilon-C-star properties, so the common operator space, multiplication, and unit satisfy def-extended-epsilon-cstar-algebra. Finally r=(3/2)((1-4 eta)^(-1/2)-1)=O(eta) as eta tends to 0; when 0<=r<=1, M^5-1=(1+r)^5-1<=31r. Hence epsilon_AI=O(eta) and tends to 0, so a universal eta_0>0 makes epsilon_AI<1. All input estimates are amplification-uniform, so the conclusion is independent of n and dim(H).

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

