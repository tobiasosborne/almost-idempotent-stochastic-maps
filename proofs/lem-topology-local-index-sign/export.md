# Proof Export

## Node 1

**Statement:** Nondegenerate local fixed-point index: if x is an isolated fixed point of a smooth self-map f of a compact orientable manifold with det(I-Df_x) != 0, then its local fixed-point index is sgn det(I-Df_x).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Put A := Df_x in a finite-dimensional local chart. Since det(I-A) != 0, the linear map I-A is invertible; therefore Av=v has no nonzero solution and 1 is not an eigenvalue of A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** After restricting to a sufficiently small coordinate neighbourhood of x, GT-granas-dugundji-thm-8.5-leray-schauder applies and gives equality of local indices J(f,x)=J(A,0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Choose a coordinate ball B about x with compact closure inside the chart and small enough that f(B) lies in the target chart about x. The coordinate representative F is C^1, fixes x, and its restriction to B is compact: its image is contained in the compact image F(cl(B)) because F is continuous and cl(B) is compact in finite dimension.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.1

**Statement:** Let phi:U->E and psi:V->E be source and target coordinate charts centered at x, so phi(x)=psi(x)=0, with E finite-dimensional. Since f(x)=x lies in V and f is continuous, D:=U intersect f^{-1}(V) is an open neighbourhood of x. Hence phi(D) is an open neighbourhood of 0, so choose r>0 with the closed ball cl(B_r(0)) contained in phi(D). For F:=psi composed with f composed with phi^{-1}, F is C^1 on phi(D), fixes 0, and is defined and continuous on cl(B_r(0)). The closed ball is compact in finite dimension, so F(cl(B_r(0))) is compact and contains F(B_r(0)); therefore F(B_r(0)) is relatively compact. Thus F restricted to B_r(0) is a compact map. This stronger shrinkage, in particular f(phi^{-1}(cl(B_r(0)))) contained in V, supplies the compactness hypothesis required by GT-granas-dugundji-thm-8.5-leray-schauder.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** By node 1.1, 1 is not an eigenvalue of F'(x)=A. Thus all hypotheses of GT-granas-dugundji-thm-8.5-leray-schauder hold for the restricted coordinate map, and its conclusion (a) gives J(F,x)=J(F'(x),0)=J(A,0). Local fixed-point indices are computed in such a neighbourhood, so this is J(f,x)=J(A,0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The local fixed-point index of the linearization A at 0 is J(A,0)=sgn det(I-A).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For the linear self-map T(y):=Ay, the origin is fixed, DT_0=A, and det(I-DT_0)=det(I-A) != 0; hence 0 is its unique, and therefore isolated, fixed point.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Set h:=I-A. Then h(0)=0 and Dh_0=I-A is nonsingular, so 0 is a regular zero of h. GT-granas-dugundji-thm-8.4-brouwer-degree therefore gives, on a sufficiently small ball V about 0, d(h,V)=sgn det(I-A).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** The two permitted computations agree on the determinant sign without any unregistered locality or coordinate-invariance bridge: nodes 1.3.3.1 and 1.3.3.2 construct a compact orientable torus self-map G having the linear germ A at p and apply def-lefschetz-fixed-point-data to obtain ind(G,p)=sgn det(I-A), while node 1.3.3.3 independently proves the needed statement J(A,0)=sgn det(I-A) directly from GT-granas-dugundji-thm-8.5-leray-schauder, GT-granas-dugundji-thm-8.4-brouwer-degree, and finite-dimensional spectral factorization. In particular J(A,0)=sgn det(I-A).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.1

**Statement:** Let E be the n-dimensional chart vector space and identify it linearly with R^n. If n=0, take the one-point torus and its unique self-map; hence assume n>0. Let M=T^n, choose p in M, and choose a smooth chart kappa:B_R(0)->M with kappa(0)=p. Choose 0<r<s<R with ||A||s<R, and choose a smooth cutoff chi:B_R(0)->[0,1] such that chi=1 on B_r(0) and supp(chi) is compactly contained in B_s(0). Define G:M->M by G(kappa(y))=kappa(chi(y)Ay) for y in B_s(0), and G(q)=p for q outside kappa(B_s(0)). For y in B_s, ||chi(y)Ay||<=||A||||y||<=||A||s<R, so the first formula is defined. Since supp(chi) is compactly contained in B_s, chi is identically zero on a neighbourhood of the patch boundary partial B_s; there the first formula is kappa(0)=p, so the two formulas agree on a neighbourhood and glue smoothly. Thus G is a smooth self-map of the compact orientable manifold M, and on kappa(B_r) its coordinate representative is exactly y->Ay.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.3.1.1

**Statement:** Because 0<r<s, choose a standard smooth cutoff chi:B_R(0)->[0,1] with chi=1 on B_r(0) and supp(chi) compactly contained in B_s(0). Compact containment gives epsilon>0 such that chi(y)=0 whenever s-epsilon<||y||<s; in particular chi vanishes on a neighbourhood of the patch boundary partial B_s, not on a neighbourhood of the boundary of its own support.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.3.1.2

**Statement:** For every y in B_s, the cutoff bound 0<=chi(y)<=1 gives ||chi(y)Ay||<=||A||||y||<=||A||s<R, so kappa(chi(y)Ay) is defined; the weak middle inequality is valid also when A=0. On the annular neighbourhood where chi=0 this formula equals kappa(0)=p, the outside formula; hence the two smooth local formulas agree on an open neighbourhood of the patch boundary and glue to a smooth global G. On B_r, chi=1, so kappa^{-1} composed with G composed with kappa is y->Ay.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.3.1.2.1

**Statement:** For y in B_s, norm homogeneity and the operator-norm bound give ||chi(y)Ay||=|chi(y)| ||Ay||<=|chi(y)| ||A|| ||y||<=||A|| ||y||<=||A||s<R. If A=0, the quantities through ||A||s are all 0 and only the already assumed strict inequality 0=||A||s<R is used; thus no multiplication by a positive ||A|| is assumed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.2

**Statement:** At p the map G fixes p and, because its coordinate representative is y->Ay near 0, its differential is DG_p=A. Hence det(I-DG_p)=det(I-A) is nonzero. The registered definition def-lefschetz-fixed-point-data now applies within its actual scope (the compact orientable manifold M) and gives ind(G,p)=sgn det(I-A).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.3

**Statement:** For the linear map T(y)=Ay, put h:=id-T=I-A. At the isolated fixed point 0, the defining relation for the local fixed-point index is J(A,0):=J(T,0)=d(h,V) on any sufficiently small isolating ball V. The permitted Brouwer-degree computation gives d(h,V)=sgn det(I-A), hence J(A,0)=sgn det(I-A). This direct computation requires no comparison with the compact extension G and no germ or coordinate invariance.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.3.3.1

**Statement:** Let T(y)=Ay and h:=id-T=I-A. Apply the permitted Leray-Schauder formula GT-granas-dugundji-thm-8.5-leray-schauder directly to the finite-dimensional linear compact map T: it gives J(T,0)=(-1)^beta, where beta is the sum of the algebraic multiplicities of the characteristic values of A in (0,1). Elementary real spectral factorization gives (-1)^beta=sgn det(I-A). The validated dependency 1.3.2 gives d(h,V)=sgn det(I-A) for a sufficiently small ball V. Hence J(A,0):=J(T,0)=d(h,V)=sgn det(I-A). Thus the index-degree equality needed here is derived by comparing the two permitted formulas, not assumed as an unregistered defining relation.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.3.3.1.1

**Statement:** The finite-dimensional linear map T:E->E, T(y)=Ay, is differentiable and compact (the image of every bounded set is relatively compact in finite dimension), fixes 0, and det(I-A)!=0 implies that 1 is not an eigenvalue of T. Therefore all hypotheses of the permitted external GT-granas-dugundji-thm-8.5-leray-schauder hold with U=E, F=T, and x_0=0. Part (b) gives J(T,0)=(-1)^beta, where beta is the sum of the algebraic multiplicities of the characteristic values nu of A lying in (0,1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.3.3.1.2

**Statement:** In the characteristic-value notation used by the Leray-Schauder formula, nu is a characteristic value of A exactly when ker(I-nu A) is nonzero. For nu in (0,1), this is equivalent to A having the real eigenvalue lambda=nu^{-1}>1; conversely every real eigenvalue lambda>1 gives nu=lambda^{-1} in (0,1). The reciprocal change of variable preserves algebraic multiplicity. Hence beta is precisely the total algebraic multiplicity m_> of the real eigenvalues lambda>1 of A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.3.3.1.3

**Statement:** Over C, det(I-A) is the product of 1-lambda over all eigenvalues lambda of A, counted with algebraic multiplicity. Because A is real, every nonreal eigenvalue occurs with its conjugate and the corresponding pair contributes (1-lambda)(1-conjugate(lambda))=|1-lambda|^2>0. Every real lambda<1 contributes a positive factor, while every real lambda>1 contributes a negative factor; lambda=1 is excluded by det(I-A)!=0. Therefore sgn det(I-A)=(-1)^{m_>}=(-1)^beta, and the preceding child yields J(T,0)=sgn det(I-A).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.3.3.3.1.4

**Statement:** The validated dependency 1.3.2 applies the permitted Brouwer-degree theorem to h=I-A and yields d(h,V)=sgn det(I-A) on a sufficiently small ball V. Together with the preceding spectral computation, J(A,0):=J(T,0)=sgn det(I-A)=d(h,V). This proves the required index-degree equality from the two allowed theorem formulas and finite-dimensional linear algebra, without assuming any unregistered degree-index definition or using compact-extension locality or coordinate invariance.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Combining J(f,x)=J(A,0) with J(A,0)=sgn det(I-A), and substituting A=Df_x, gives J(f,x)=sgn det(I-Df_x), which is the claimed local fixed-point-index formula.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Direct application of the registered definition: the root assumes that f is a smooth self-map of a compact orientable manifold M, that x is a fixed point, and that det(I-Df_x) != 0. These are exactly the scope and nondegeneracy hypotheses in def-lefschetz-fixed-point-data, whose harmonised statement defines the fixed-point index by ind(f,x)=sgn det(1-Df_x), with Df_x:T_xM->T_xM. Replacing 1 by I in this endomorphism notation gives ind(f,x)=sgn det(I-Df_x). The extra hypothesis that x is isolated is not needed for this definitional implication. Therefore node 1 follows directly, with no coordinate-change or locality assertion.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

