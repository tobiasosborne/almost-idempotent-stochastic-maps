# Proof Export

## Node 1

**Statement:** Polar coherence and scalar naturality: for every exact-unit algebra and every two polar data (delta_j, S_j, u_j, h_j), j = 1, 2, for which Pi_{delta_j}: calU x B^{calH}_{delta_j}(J) -> S_j, (U, H) |-> U bold-dot H, is bijective with inverse (u_j, h_j), one has (u_1, h_1) = (u_2, h_2) on S_1 intersect S_2; moreover, for c in U(1) and X, cX in S_j, u_j(cX) = c*u_j(X) and h_j(cX) = h_j(X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Coherence on overlaps: for arbitrary permitted polar data and every X in S_1 intersect S_2, (u_1(X),h_1(X))=(u_2(X),h_2(X)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Fix X in S_1 intersect S_2. Because (u_j,h_j) is the inverse of Pi_{delta_j}, for each j=1,2 the pair p_j=(u_j(X),h_j(X)) belongs to calU x B^{calH}_{delta_j}(J) and Pi_{delta_j}(p_j)=u_j(X) bold-dot h_j(X)=X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Choose k in {1,2} with delta_k=max(delta_1,delta_2). Both p_1 and p_2 lie in calU x B^{calH}_{delta_k}(J): p_k does by its inverse-domain membership, and for l different from k the inclusion B^{calH}_{delta_l}(J) subseteq B^{calH}_{delta_k}(J) follows from delta_l<=delta_k. Since every Pi_delta has the same formula (U,H)|->U bold-dot H, both pairs have Pi_{delta_k}-image X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** The assumed bijectivity of Pi_{delta_k} makes it injective on calU x B^{calH}_{delta_k}(J). Applying injectivity to the two domain points from the preceding step gives p_1=p_2, hence u_1(X)=u_2(X) and h_1(X)=h_2(X). Since X was arbitrary in S_1 intersect S_2, coherence holds there.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Scalar naturality in each chart: for j in {1,2}, c in U(1), and X,cX in S_j, one has u_j(cX)=c*u_j(X) and h_j(cX)=h_j(X).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Fix j, c in U(1), and X,cX in S_j. The inverse property gives p=(u_j(X),h_j(X)) in calU x B^{calH}_{delta_j}(J) with u_j(X) bold-dot h_j(X)=X; applied to cX it also gives q=(u_j(cX),h_j(cX)) in the same domain with Pi_{delta_j}(q)=cX.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Scalar closure of calU: if U is in calU and c is in U(1), then cU is in calU. Indeed, by def-approximate-unitary-space, U^dagger bold-dot U=J and U has a right inverse V. Conjugate-linearity of dagger, bilinearity of the algebra product, and bar(c)c=1 give (cU)^dagger bold-dot(cU)=J; and (cU) bold-dot(c^{-1}V)=J, so cU has a right inverse. No associativity or positivity is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** By scalar closure and the domain membership of p, the pair p_c=(c*u_j(X),h_j(X)) lies in calU x B^{calH}_{delta_j}(J). Bilinearity in the first variable yields Pi_{delta_j}(p_c)=(c*u_j(X)) bold-dot h_j(X)=c*(u_j(X) bold-dot h_j(X))=cX.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Both q and p_c are in the domain of Pi_{delta_j} and have image cX. Injectivity of the assumed bijection Pi_{delta_j} gives q=p_c. Equality of components is exactly u_j(cX)=c*u_j(X) and h_j(cX)=h_j(X), proving scalar naturality.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

