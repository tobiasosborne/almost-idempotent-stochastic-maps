# Proof Export

## Node 1

**Statement:** EXT-CB cross-corner dimension: there is a universal e_sel > 0 such that every EXT-CB datum with e <= e_sel satisfies (dim S_{P,Q},dim S_{Q,Q})=(r,1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix an EXT-CB datum with e=delta+epsilon small. Let D_r be the diagonal commutative C*-subalgebra of M_r with projection basis Pi_a=E_aa, put R_a=v(Pi_a), let v_D=v restricted to D_r, and let w:C->A be w(lambda)=lambda Q. The registered definitions imply, with one universal accuracy constant independent of r, that v_D and w are sufficiently accurate non-unital inclusions, that v_D(I)=v(I_r), and that w(1)=Q; moreover Q is one-dimensional because dim S_Q=1 in the datum.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By def-projection-basis, D_r is a finite-dimensional commutative C*-algebra with projection basis {Pi_a=E_aa}_{a=1}^r: Pi_a^dagger=Pi_a, Pi_a Pi_b=delta_ab Pi_b, and sum_a Pi_a=I_r. The scalar algebra C has the one-element projection basis {1}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** By def-extcb-datum, v:M_r->S_P is an extended delta-isomorphism. Hence its restriction v_D to D_r is linear, star-preserving, delta-multiplicative for the compressed product, and obeys the same two-sided norm bounds. The external lem-compcb-corner-algebra makes S_P an extended C_ca*e-C*-algebra for universal small e (P is nonvanishing because v is onto the nonzero space S_P). The registered compressed-product estimate differs from the ambient product by O(e) on bounded elements. Thus v_D, viewed as a map into A, is a non-unital c_D*e-inclusion for a universal c_D independent of r, with v_D(Pi_a)=R_a and v_D(I)=v(I_r).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Since dim S_Q=1, Q is nonvanishing. Hence the registered nonvanishing alternative gives a universal C_nv and threshold such that abs(||Q||-1)<=C_nv*(delta+epsilon)=C_nv*e (not O(delta)). Define w(lambda)=lambda Q. It is linear and star-preserving, and w(1)=Q. For every n and X in M_n(C), the Ruan axioms give the exact cross-norm identity ||(1_{M_n} tensor w)(X)||=||X tensor Q||=||X||*||Q||: the upper bound follows from X tensor Q=X(I_n tensor Q), ax_R1, and ax_R2, while the reverse bound follows by scalar row/column compression using unit vectors attaining ||X||. Thus (1-C_nv*e)||X||<=||X tensor Q||<=(1+C_nv*e)||X||. For X,Y in M_n(C), bilinearity of multiplication and the same identity give ||(XY) tensor Q-(X tensor Q)(Y tensor Q)||=||(XY) tensor (Q-Q^2)||<=delta||X||||Y||<=e||X||||Y||. Therefore every amplification is a c_Q*e-inclusion for a universal c_Q>=max{C_nv,1}; equivalently w is a sufficiently accurate non-unital extended c_Q*e-inclusion, uniformly.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** By def-one-dimensional-delta-projection, dim S_Q=1 says exactly that Q is a one-dimensional delta-projection. Taking a positive universal threshold below those in lem-compcb-corner-algebra and the registered compression/dichotomy estimates, and absorbing c_D,c_Q into the accuracy parameter allowed by lem-extcb-corner-dimension-additivity, establishes every assertion of node 1.1 without dependence on r.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.4.1

**Statement:** Nodes 1.1.1, 1.1.2, and 1.1.3 jointly establish every assertion of node 1.1: node 1.1.1 supplies that D_r and C are finite-dimensional commutative C*-algebras with the stated projection bases; node 1.1.2 supplies the uniformly accurate non-unital inclusion v_D together with v_D(Pi_a)=R_a and v_D(I)=v(I_r); and node 1.1.3 supplies the uniformly accurate non-unital inclusion w together with w(1)=Q. Finally, by def-one-dimensional-delta-projection, the EXT-CB datum assertion dim S_Q=1 says exactly that Q is one-dimensional. Taking the minimum of the finitely many universal positive thresholds and absorbing the universal constants c_D and c_Q into the accuracy allowed by lem-extcb-corner-dimension-additivity preserves universality and independence of r.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Matrix-unit corner normalization: after a universal shrink of e, every R_a=v(E_aa) is a one-dimensional delta-prime-projection in A (with delta-prime=O(e)), and every pair R_a,R_b is equivalent, i.e. dim S_{R_a,R_b}=1. All constants and the threshold are independent of r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For a,b in {1,...,r}, let c_ab:M_r->M_r be c_ab(X)=E_aa X E_bb and define the bounded operator T_ab:A->A by T_ab=v c_ab v^{-1} Co_P. Because Co_P is an idempotent with range S_P=range(v), Co_P v=v and v^{-1}Co_P v=id. Since c_ab^2=c_ab and range(c_ab)=C E_ab, T_ab is an exact bounded linear idempotent of rank one, with range C v(E_ab).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Uniform matrix-corner comparison: there are universal C_m<infinity and e_m>0, independent of r,a,b, such that for e<=e_m each R_a=v(E_aa) is a Hermitian C_m*e-projection in A and ||Co_{R_a,R_b}-T_ab||<=C_m*e as operators on A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Hermitian projection control. Star preservation gives R_a^dagger=R_a. In M_r, E_aa^2=E_aa and ||E_aa||=1. Delta-multiplicativity of v into the compressed algebra gives ||R_a dot R_a-R_a||<=delta, while the registered compressed-product estimate gives ||R_a dot R_a-R_a^2||<=c_1*e||R_a||^2. The norm bound ||R_a||<=1+delta therefore yields ||R_a^2-R_a||<=C_1*e with universal C_1, uniformly in a and r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** Uniform subordination estimate. There are universal C_s,e_s such that, for e<=e_s, every X in A satisfies ||R_a(XR_b)-R_a((Co_P X)R_b)||<=C_s*e||X||. Indeed R_a,R_b lie in S_P, so R_i=Co_P(R_i); replacing each such equality by the registered estimate Co_P(Y)=P(YP)+O(e)||Y||, and replacing Co_P(X) by P(XP)+O(e)||X||, a finite telescoping using the ambient product and associator axioms transforms R_a(XR_b) into R_a((Co_P X)R_b). The factors P,R_a,R_b and Co_P are uniformly bounded: P is nonvanishing because S_P is nonzero, ||R_i||<=1+delta by v, and the compression estimate bounds Co_P. The number of replacements is fixed, so C_s is universal and does not depend on r,a,b.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.3

**Statement:** Transported-source comparison on the P-corner. For Y=Co_P X and X_0=v^{-1}(Y), the two-sided norm bound for v gives ||X_0||<=(1-delta)^(-1)||Y||. Applying delta-multiplicativity twice to E_aa X_0 E_bb in M_r, and using lem-compcb-corner-algebra for the universal product/associator bounds in S_P, gives ||v(E_aa X_0 E_bb)-(R_a dot Y) dot R_b||<=C_2*e||X||. Replacing the two compressed products by ambient products gives ||T_ab X-R_a(YR_b)||<=C_3*e||X||. All source matrix factors have norm one, so C_2,C_3 are independent of r,a,b.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.4

**Statement:** By def-compressed-corner, for the C_1*e-projections R_a,R_b and universal small e, ||Co_{R_a,R_b}X-R_a(XR_b)||<=C_4*e||X||. Combine this with the subordination and transported-source estimates to obtain ||(Co_{R_a,R_b}-T_ab)X||<=(C_4+C_s+C_3)e||X||. Taking the supremum over ||X||=1 and enlarging C_m to dominate C_1 and C_4+C_s+C_3 proves node 1.2.2; the minimum of the finitely many positive thresholds is universal.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Close-idempotent rank lemma: if E and F are bounded idempotents on a normed space and ||E-F||<1, then restriction of F to range(E) and restriction of E to range(F) are injective; hence, if either range is finite-dimensional, dim range(E)=dim range(F).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** If x is in range(E) and Fx=0, then x=Ex=(E-F)x, so ||x||<=||E-F||||x||. When ||E-F||<1 this forces x=0; hence F restricted to range(E) is injective and dim range(E)<=dim range(F).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.2

**Statement:** Interchanging E and F gives: if y is in range(F) and Ey=0, then y=Fy=(F-E)y, so y=0. Thus E restricted to range(F) is injective and dim range(F)<=dim range(E). If either range is finite-dimensional, both inequalities are ordinary finite dimensions and give equality.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Choose e additionally so C_m*e<1. Apply the close-idempotent rank lemma to E=T_ab and F=Co_{R_a,R_b}; node 1.2.1 gives rank(T_ab)=1 and def-compressed-corner gives range(Co_{R_a,R_b})=S_{R_a,R_b}, so dim S_{R_a,R_b}=1 for every a,b. The case a=b says dim S_{R_a}=1, so each R_a is one-dimensional; the cases a,b arbitrary say the R_a are pairwise equivalent by def-one-dimensional-delta-projection. Together with their C_m*e projection defects, this proves node 1.2 with a universal threshold independent of r.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.5

**Statement:** Dependency gate and discharge: nodes 1.2.1--1.2.4 establish the matrix-corner normalization only in the EXT-CB setup and notation supplied by node 1.1. Accordingly this QED has node 1.1 as a hard validation prerequisite: it may be validated only after node 1.1 is validated. Once that prerequisite holds, node 1.1 fixes the datum and R_a=v(E_aa), nodes 1.2.1 and 1.2.2 compare the rank-one idempotent T_ab with Co_{R_a,R_b}, node 1.2.3 supplies rank invariance under distance less than one, and node 1.2.4 concludes dim S_{R_a,R_b}=1 and the asserted one-dimensionality/equivalence uniformly in r.

**Type:** qed

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Dimension dichotomy and selection: below the universal thresholds of lem-extcb-one-dimensional-corner-dimension, lem-extcb-corner-dimension-additivity, and lem-extcb1-close-corner-dimension, the numbers dim S_{R_a,Q} all equal one common d in {0,1}; additivity gives dim S_{v(I_r),Q}=r*d, close-compression range invariance gives dim S_{P,Q}=r*d, and the EXT-CB hypothesis S_{P,Q}!=0 forces d=1 and hence dim S_{P,Q}=r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Put delta_prime=C_m*e as supplied by node 1.2. For e small enough that delta_prime+epsilon is below the universal threshold in lem-extcb-one-dimensional-corner-dimension, that external applies to the one-dimensional delta_prime-projection R_a and the one-dimensional delta-projection Q (enlarge the common projection-accuracy parameter to max{delta_prime,delta}). It gives d_a:=dim S_{R_a,Q}<=1. Since d_a is a nonnegative integer, d_a is 0 or 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** The values d_a are all equal. If no d_a equals 1 they are all zero. Otherwise choose b with d_b=1; by def-one-dimensional-delta-projection this says R_b is equivalent to Q. Node 1.2 says every R_a is equivalent to R_b. The registered definitional fact that equivalence of one-dimensional projections is an equivalence relation, in particular transitive, gives R_a equivalent to Q and hence d_a=1 for every a. Thus d_a=d in {0,1} independently of a.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Assume nodes 1.2 and 1.3.1 have been validated. By node 1.3.1, each d_a=dim S_{R_a,Q} lies in {0,1}. If no index b has d_b=1, then d_a=0 for every a. Otherwise choose b with d_b=1. Node 1.2 says that R_a and R_b are one-dimensional projections and are equivalent for every a, while node 1.3.1 supplies that Q is one-dimensional; d_b=dim S_{R_b,Q}=1 therefore says, by def-one-dimensional-delta-projection, that R_b is equivalent to Q. Transitivity in that registered definition now gives R_a equivalent to Q, so dim S_{R_a,Q}=1 and d_a=1 for every a. In either case there is d in {0,1} with d_a=d for all a.

**Type:** qed

**Inference:** case split followed by definitional transitivity

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Apply lem-extcb-corner-dimension-additivity to the commutative algebras D_r and C, their projection bases from node 1.1, and the sufficiently accurate non-unital inclusions v_D,w established there. Its exact conclusion is a linear bijection S_{v(I_r),Q}->direct-sum_{a=1}^r S_{R_a,Q}; consequently dim S_{v(I_r),Q}=sum_a d_a=r*d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.1

**Statement:** Assume nodes 1.1 and 1.3.2 have been validated. Node 1.1 supplies finite-dimensional commutative C*-algebras D_r and C with projection bases {Pi_a}_{a=1}^r and {1}, sufficiently accurate non-unital inclusions v_D and w, and the exact identities v_D(I_r)=v(I_r), w(1)=Q, and v_D(Pi_a)=R_a. Therefore the allowed external lem-extcb-corner-dimension-additivity applies and gives a linear bijection S_{v_D(I_r),w(1)} -> direct-sum_{a=1}^r S_{v_D(Pi_a),w(1)}. Substituting those exact identities yields S_{v(I_r),Q} -> direct-sum_{a=1}^r S_{R_a,Q}. Hence dim S_{v(I_r),Q}=sum_{a=1}^r dim S_{R_a,Q}=sum_{a=1}^r d_a; node 1.3.2 gives d_a=d for every a, so this equals r*d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.2

**Statement:** With node 1.1 as a hard validation prerequisite (not a merely conditional meta-assumption), node 1.1 supplies the finite-dimensional commutative C*-algebras D_r and C, projection bases {Pi_a}_{a=1}^r and {1}, sufficiently accurate non-unital inclusions v_D and w, and the identities v_D(I_r)=v(I_r), w(1)=Q, and v_D(Pi_a)=R_a. The allowed external lem-extcb-corner-dimension-additivity therefore yields a linear bijection S_{v_D(I_r),w(1)} -> direct-sum_{a=1}^r S_{v_D(Pi_a),w(1)}. Substitution gives S_{v(I_r),Q} -> direct-sum_{a=1}^r S_{R_a,Q}; hence dim S_{v(I_r),Q}=sum_a dim S_{R_a,Q}. The separately validated node 1.3.2 gives dim S_{R_a,Q}=d for every a, so the dimension is r*d. This child is explicitly barred from validation until node 1.1 is validated.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.3

**Statement:** Direct dependency-complete discharge: validated node 1.3.3.1, whose registered dependencies 1.1 and 1.3.2 are both validated, supplies the complete additivity inference and proves dim S_{v(I_r),Q}=r*d. Thus node 1.3.3 follows without consuming pending node 1.3.3.2.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.3.3.1

**Statement:** Direct discharge without node 1.3.3.2: validated node 1.3.3.1 has validated registered dependencies 1.1 and 1.3.2 and proves the complete required inference. Explicitly, node 1.1 supplies D_r and C, their projection bases, the sufficiently accurate non-unital inclusions v_D and w, and v_D(I_r)=v(I_r), w(1)=Q, v_D(Pi_a)=R_a. Applying the allowed external lem-extcb-corner-dimension-additivity yields a linear bijection S_{v(I_r),Q} -> direct-sum_{a=1}^r S_{R_a,Q}. Taking dimensions and using node 1.3.2, dim S_{R_a,Q}=d for every a, gives dim S_{v(I_r),Q}=sum_{a=1}^r d=r*d. Hence node 1.3.3 is established directly from validated node 1.3.3.1; pending node 1.3.3.2 is redundant and is not used in this discharge.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** Choose e also below the universal e_close in lem-extcb1-close-corner-dimension. That exact external gives dim S_{P,Q}=dim S_{v(I_r),Q}=r*d. The EXT-CB datum assumes S_{P,Q}!=0, so its dimension is nonzero; since r>=1, d cannot be zero. Hence d=1 and dim S_{P,Q}=r, proving node 1.3.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The diagonal corner identity S_{Q,Q}=S_Q and the EXT-CB hypothesis dim S_Q=1 give dim S_{Q,Q}=1. Taking e_sel to be the minimum of the finitely many positive universal thresholds used in the preceding children proves (dim S_{P,Q},dim S_{Q,Q})=(r,1) for every datum with e<=e_sel.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

