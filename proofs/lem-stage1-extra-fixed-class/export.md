# Proof Export

## Node 1

**Statement:** Bound extra fixed class with one ledger selection: there exist one def-stage1-polar-witness-data tuple W=(C_rect,C_ch,C_pol,C_grp,C_path,C_der,e_rect,kappa_ch,kappa_pol,kappa_der,delta_*,epsilon_*^r,e_S1,r_iso) such that C_rect,C_ch,C_pol,C_grp,C_path,C_der>=1, 0<e_rect<=1/C_rect, 0<kappa_ch,kappa_pol,kappa_der<=1/2, delta_*=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol)}, epsilon_*^r=min{1/4,kappa_ch/(4*C_ch),kappa_pol/(4*C_pol),kappa_der/(8*C_der),1/C_grp,delta_*/(12*C_path*C_grp)}, e_S1=min{e_rect,epsilon_*^r/C_rect}, r_iso=min{delta_*/4,kappa_der/(8*C_der)}, and there are universal e_quot^r>0, epsilon_B^r>0, C_fix<infinity, 0<e_fix^r<=epsilon_B^r, and r_bidx>0 with epsilon_B^r=min{epsilon_*^r,e_quot^r} and C_fix>=C_grp such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0<=epsilon_r<=e_fix^r and 1<dim_C calX<infinity, there exist a family g=(g_V:B_{2delta_*}^{icalH}(0)->B_{2delta_*}^{calH}(0))_{V in calUbar_delta_*}, maps u_delta,h_delta,mu,sigma,H, a space breve-calU, maps breve-mu:breve-calU x breve-calU->breve-calU and breve-sigma:breve-calU->breve-calU, a breve-sigma-fixed class breve-U, U_0 in calU_e, c,a in U(1), and U in calU_e such that all of the following hold: (A_2) for every V in calUbar_delta_* and A^par in B_{2delta_*}^{icalH}(0), g_V(A^par) is the unique element of B_{2delta_*}^{calH}(0) with f_V(A^par+g_V(A^par))=0, where f_V(A)=(1/2)*(((J+A^dagger) bold-dot V^dagger) bold-dot (V bold-dot (J+A))-J), chi_V(A^par)=V bold-dot (J+A^par+g_V(A^par)) lies in calU, ||Dg_V(A^par)||<=C_ch*(epsilon_r+delta_*), ||D_{A^perp}f_V(A^par+g_V(A^par))-I_calH||<=C_ch*(epsilon_r+delta_*)<1, and these C^1 charts cover calU; (A_4) set Pi_delta_*:calU x B_{delta_*}^{calH}(J)->calX by Pi_delta_*(V,K):=V bold-dot K and set S_delta_*:=Pi_delta_*(calU x B_{delta_*}^{calH}(J)); Pi_delta_* is a C^1 diffeomorphism onto S_delta_* with unique inverse maps u_delta:S_delta_*->calU and h_delta:S_delta_*->B_{delta_*}^{calH}(J) satisfying X=u_delta(X) bold-dot h_delta(X) for every X in S_delta_* and u_delta(V)=V and h_delta(V)=J for every V in calU; (A_5) the displayed maps mu:calU x calU->calU and sigma:calU->calU are defined by mu(V_1,V_2):=u_delta(V_1 bold-dot V_2) and sigma(V):=u_delta(V^dagger), are global C^1 and, for every V,V_1,V_2,V_3 in calU, mu(J,V)=mu(V,J)=V, sigma(J)=J, ||mu(V_1,V_2)-V_1 bold-dot V_2||<=C_grp*epsilon_r, ||sigma(V)-V^dagger||<=C_grp*epsilon_r, ||mu(mu(V_1,V_2),V_3)-mu(V_1,mu(V_2,V_3))||<=C_grp*epsilon_r, ||mu(sigma(V),V)-J||<=C_grp*epsilon_r, and ||mu(V,sigma(V))-J||<=C_grp*epsilon_r; (A_6) for every V_0,V_1 in calU and q in [0,1] satisfying ||V_1-V_0||<=q, C_path*q<=1/4, and C_path*(q+epsilon_r*q+q^2)<delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), the path H(-,V_0,V_1):[0,1]->calU given by H(t,V_0,V_1):=u_delta((1-t)*V_0+t*V_1) is defined, is jointly continuous in its displayed variables, and joins V_0 to V_1, and satisfies H(t,c_0*V_0,c_0*V_1)=c_0*H(t,V_0,V_1) for every c_0 in U(1) and t in [0,1]; (A_7) for every s in {+1,-1}, set chi_s:B_{r_iso}^{icalH}(0)->calU by chi_s(A):=sJ bold-dot (J+A+g_{sJ}(A)), let phi_{sJ}^par:chi_s(B_{r_iso}^{icalH}(0))->B_{r_iso}^{icalH}(0) be its inverse, and set F_s:B_{r_iso}^{icalH}(0)->icalH by F_s(A):=phi_{sJ}^par(sigma(chi_s(A))); then sigma maps chi_s(B_{r_iso}^{icalH}(0)) into itself and ||D(F_s-id)(A)+2I||<=C_der*(epsilon_r+r_iso) for every A in B_{r_iso}^{icalH}(0); (R) set q_*:=C_grp*epsilon_r, set r_-:=delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), and set eta_*:=C_path*(q_*+epsilon_r*q_*+q_*^2); the guards C_ch*(epsilon_r+delta_*)<=kappa_ch, C_pol*(epsilon_r+delta_*)<=kappa_pol, q_*<r_-, C_path*q_*<=1/4, eta_*<r_-, C_der*(epsilon_r+r_iso)<=kappa_der/4<1, and (1+epsilon_r)*(1+C_ch*(epsilon_r+delta_*))*r_iso+q_*<2delta_* hold; moreover r_bidx=r_iso and breve-calU=calU_e/U(1), set breve-e:=[J], breve-mu([V_1],[V_2])=[mu(V_1,V_2)], breve-sigma([V])=[sigma(V)], (breve-calU,breve-mu,breve-e) is a connected H-space, breve-sigma is a smooth left inversion, sigma(c_0*V)=conj(c_0)*sigma(V) and ||sigma(V)-V^dagger||<=C_grp*epsilon_r for every c_0 in U(1) and V in calU, breve-calU is a connected compact orientable smooth manifold without boundary of real dimension (dim_C calX)-1 and is homeomorphic to a finite simplicial complex, breve-e is an isolated fixed point of breve-sigma with local index +1, J and -J are the only sigma-fixed points in their respective ambient r_bidx-balls, breve-U!=breve-e, [U_0]=breve-U, sigma(U_0)=c*U_0, a^2=c, U=a*U_0, [U]=breve-U, sigma(U)=U, ||U-U^dagger||<=C_fix*epsilon_r, ||U-J||>=r_bidx, and ||U+J||>=r_bidx.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** One-use ledger selection. By lem-stage1-polar-constant-ledger there exists one universal def-stage1-polar-witness-data tuple W with the six coefficients at least 1, the stated positive margin bounds, and exactly the displayed formulas for delta_*, epsilon_*^r, e_S1, and r_iso; for this same W its clauses (A_2),(A_4),(A_5),(A_6),(A_7) are available for every exact-unit epsilon_r-C*-algebra whenever their own displayed scalar guards hold. This is the sole existential elimination of lem-stage1-polar-constant-ledger, and its rectified-input clause (R) is not used for the arbitrary exact-unit input below.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Conditional bound-package application. For every W satisfying the hypotheses and formulas in node 1.1, lem-stage1-bound-quotient-index-data gives universal e_quot^r>0 and epsilon_B^r=min{epsilon_*^r,e_quot^r}>0 such that, whenever a finite-dimensional exact-unit epsilon_r-C*-algebra with epsilon_r<=epsilon_B^r and 1<dim_C calX<infinity is supplied with the literal (A_2),(A_4),(A_5),(A_6),(A_7) data and the listed scalar guards, it returns those same g,u_delta,h_delta,mu,sigma,H together with r_bidx=r_iso, breve-calU=calU_e/U(1), breve-mu, breve-sigma, the connected compact orientable smooth boundaryless (dim_C calX-1)-manifold and finite-simplicial-complex package, the H-space and smooth-left-inversion assertions, scalar covariance and near-adjoint estimate, local index +1 at the isolated breve-e=[J], both ambient sigma-isolation assertions, and the class-first phase-lift witnesses for every breve-sigma-fixed class.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Scalar guards for arbitrary exact-unit inputs. Fix W as in node 1.1 and 0<=epsilon_r<=epsilon_B^r<=epsilon_*^r. Put q_*=C_grp*epsilon_r, r_-=delta_*-C_pol*(epsilon_r*delta_*+delta_*^2), and eta_*=C_path*(q_*+epsilon_r*q_*+q_*^2). The minimum formulas imply C_ch*epsilon_r<=kappa_ch/4 and C_ch*delta_*<=kappa_ch/4, and analogously for C_pol, so C_ch*(epsilon_r+delta_*)<=kappa_ch/2<=kappa_ch and C_pol*(epsilon_r+delta_*)<=kappa_pol/2<=kappa_pol. They also give epsilon_r<=1/4, C_pol*(epsilon_r+delta_*)<=1/4, hence r_- >=3*delta_*/4; q_*<=delta_*/(12*C_path)<=delta_*/12<r_-; C_path*q_*<=delta_*/12<1/4; and eta_*=C_path*q_*(1+epsilon_r+q_*)<=61*delta_*/576<3*delta_*/4<=r_-. Further C_der*epsilon_r<=kappa_der/8 and C_der*r_iso<=kappa_der/8, so C_der*(epsilon_r+r_iso)<=kappa_der/4<1. Finally r_iso<=delta_*/4, 1+epsilon_r<=5/4, 1+C_ch*(epsilon_r+delta_*)<=5/4, and q_*<=delta_*/12, whence (1+epsilon_r)*(1+C_ch*(epsilon_r+delta_*))*r_iso+q_*<=25*delta_*/64+delta_*/12<2*delta_*. Thus every graph, polar, group, path, derivative, and chart-retention guard required by the conditional ledger clauses and lem-stage1-bound-quotient-index-data holds without using ledger clause (R).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Common-object instantiation. Choose e_fix^r:=epsilon_B^r and C_fix:=C_grp, so 0<e_fix^r<=epsilon_B^r, C_fix<infinity, and C_fix>=C_grp. For an arbitrary finite-dimensional exact-unit epsilon_r-C*-algebra with 0<=epsilon_r<=e_fix^r and 1<dim_C calX<infinity, node 1.3 permits the conditional clauses (A_2),(A_4),(A_5),(A_6),(A_7) from the single W selected by lem-stage1-polar-constant-ledger to be instantiated at delta_*. Feeding exactly those functions, inverses, operations, paths, and charts to lem-stage1-bound-quotient-index-data yields all analytic clauses (A_2),(A_4)-(A_7), all displayed guards (R), and the complete same-map quotient package listed in node 1.2, with r_bidx=r_iso.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Singleton reduction. For the package obtained in node 1.4, if breve-e were the only breve-sigma-fixed class, then Fix(breve-sigma)={breve-e} would be a finite fixed set, and breve-e has local fixed-point index +1 by lem-stage1-bound-quotient-index-data.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** Maximal-simplex antecedent. Under the singleton hypothesis of node 1.5, the homeomorphism of breve-calU with a finite simplicial complex makes it a finite polyhedron, and lem-finite-polyhedron-maximal-simplex-placement places its sole fixed point breve-e in a maximal simplex. Hence the maximal-simplex hypothesis of lem-topology-lefschetz-hopf is satisfied.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** Lefschetz value under the singleton hypothesis. Apply lem-topology-lefschetz-hopf to the finite-polyhedron model of breve-sigma using node 1.6. Since the only fixed point is breve-e and its local index is +1, the Lefschetz number is L(breve-sigma)=1. The local-index value is also consistent with lem-topology-local-index-sign and the determinant data supplied by lem-stage1-bound-quotient-index-data.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.7.1

**Statement:** Finite-polyhedron presentation without conjugating the map. Let h:breve-calU->|K| be the homeomorphism to the realization of a finite simplicial complex supplied by lem-stage1-bound-quotient-index-data, and transport the finite-polyhedron structure of |K| along h to the same underlying topological space breve-calU. Denote this finite-polyhedron presentation by X, and let f:X->X be the same underlying function breve-sigma (not h o breve-sigma o h^{-1}). Under the singleton hypothesis Fix(f)={breve-e}; node 1.6 (using lem-finite-polyhedron-maximal-simplex-placement) places breve-e in a maximal simplex of this presentation. Because X and breve-calU have the same underlying space and f and breve-sigma are literally the same self-map, the local index occurring in lem-topology-lefschetz-hopf is exactly ind(f,breve-e)=ind(breve-sigma,breve-e)=+1 as supplied by lem-stage1-bound-quotient-index-data, and f^{*k}=breve-sigma^{*k} on the same cohomology groups, hence L(f)=L(breve-sigma). No invariance of index under homeomorphic conjugacy is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.7.2

**Statement:** Direct Lefschetz-Hopf application, without conjugating the map. Under the singleton hypothesis, validated node 1.5 gives Fix(breve-sigma)={breve-e} and validated node 1.6 gives that breve-calU, with the finite-polyhedron presentation supplied by the bound quotient package, is a finite polyhedron whose unique fixed point breve-e lies in a maximal simplex. The same package instantiated in validated node 1.4 gives ind(breve-sigma,breve-e)=+1. Therefore lem-topology-lefschetz-hopf applies directly to breve-sigma:breve-calU->breve-calU and yields L(breve-sigma)=sum_{x in Fix(breve-sigma)} ind(breve-sigma,x)=ind(breve-sigma,breve-e)=1. No conjugated map f and no homeomorphic-conjugacy invariance of local fixed-point index are used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.8

**Statement:** Trace calculation on the same quotient. The finite simplicial model gives breve-calU finite CW type and finite-dimensional total real cohomology; the package makes it connected and an H-space and makes breve-sigma a left inversion. Therefore lem-stage1-left-inversion-trace applies and gives Tr(breve-sigma^{*k}:H^k(breve-calU;reals)->H^k(breve-calU;reals))=(-1)^k b_k for every k>=0, where b_k=dim_reals H^k(breve-calU;reals).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.9

**Statement:** Lefschetz number as total Betti number. By the definition in def-lefschetz-fixed-point-data and node 1.8, L(breve-sigma)=sum_k (-1)^k Tr(breve-sigma^{*k})=sum_k (-1)^k(-1)^k b_k=sum_k b_k; the sum is finite because breve-calU has finite CW type.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.10

**Statement:** Existence of an extra fixed class. Let d=dim_R breve-calU=dim_C calX-1>0. Connectedness gives b_0=1, while lem-topology-orientable-top-cohomology applied to the connected compact orientable boundaryless d-manifold gives H^d(breve-calU;reals)!=0 and hence b_d>=1. Since d>0, node 1.9 yields L(breve-sigma)=sum_k b_k>=2, contradicting node 1.7 under the singleton hypothesis. Thus breve-sigma has a fixed class breve-U!=breve-e.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.11

**Statement:** Fixed lift and near-adjoint bound. Apply the class-first phase clause of lem-stage1-bound-quotient-index-data to the extra fixed class from node 1.10: bind U_0 in calU_e and c,a in U(1) with [U_0]=breve-U, sigma(U_0)=c*U_0 and a^2=c, and set U=a*U_0. The exported covariance sigma(zV)=conj(z)*sigma(V) gives sigma(U)=conj(a)cU_0=aU_0=U because c=a^2 and |a|=1; also [U]=[U_0]=breve-U and U lies in calU_e. The literal package estimate then gives ||U-U^dagger||=||sigma(U)-U^dagger||<=C_grp*epsilon_r<=C_fix*epsilon_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.12

**Statement:** Distance bounds and final assembly. The lift U in node 1.11 is sigma-fixed and [U]=breve-U!=breve-e=[J]. If ||U-J||<r_bidx, the J-ball isolation from lem-stage1-bound-quotient-index-data forces U=J, contradicting its class; hence ||U-J||>=r_bidx. If ||U+J||<r_bidx, the -J-ball isolation forces U=-J, whose scalar class equals [J], again a contradiction; hence ||U+J||>=r_bidx. Combining nodes 1.1-1.4 and 1.10-1.11 with e_fix^r=epsilon_B^r, C_fix=C_grp, and r_bidx=r_iso supplies every existential witness, formula, analytic clause, guard, topological assertion, fixed lift, estimate, and distance conclusion in root node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

