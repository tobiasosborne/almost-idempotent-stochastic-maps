# Proof Export

## Node 1

**Statement:** Associated-graded action of a left inversion over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity, (M,mu,e) is an H-space, and sigma:M->M is a left inversion, set A=H^*(M;reals), A^+=direct_sum_{k>0} A^k, F^{p,q}=(A^+)^p intersect A^{p+q}, and E^{p,q}=F^{p,q}/F^{p+1,q-1}; then sigma^* preserves every F^{p,q} and induces (-1)^(p+q)*id on every E^{p,q} for p >= 0 and p+q >= 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Put I=A^+. By functoriality of real singular cohomology, sigma^*:A->A is a degree-preserving unital algebra homomorphism. Hence sigma^*(I) is contained in I and sigma^*(I^p) is contained in I^p for every p>=0; consequently sigma^* preserves F^{p,q}=I^p intersect A^{p+q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For every homogeneous a in I, the left-inversion relation and the coproduct expansion supplied by lem-stage1-exterior-cohomology give 0=sigma^*(a)+a+sum_{j in J_a} sigma^*(aPrime_j)aDoublePrime_j in A, where aPrime_j and aDoublePrime_j are the positive-degree factors appearing in that external coproduct expansion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Let ell:M->M be ell(x)=mu(sigma(x),x). By def-h-space-left-inversion, ell is homotopic to the constant map with value e. Therefore ell^*:H^*(M;reals)->H^*(M;reals) is the pullback of that constant map and ell^*(a)=0 for every positive-degree a in I.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Under the cross-product identification used to define Delta in lem-stage1-exterior-cohomology, functoriality of pullback and the diagonal formula for cup product give ell^*(a)=m_A((sigma^* tensor id)Delta(a)). Substituting the external expansion Delta(a)=a tensor 1+1 tensor a+sum_j aPrime_j tensor aDoublePrime_j yields ell^*(a)=sigma^*(a)+a+sum_j sigma^*(aPrime_j)aDoublePrime_j. Together with the preceding vanishing, this is the asserted identity.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** In the identity of node 1.2, every aPrime_j and aDoublePrime_j lies in I, and node 1.1 gives sigma^*(aPrime_j) in I; hence every product sigma^*(aPrime_j)aDoublePrime_j lies in I^2. Thus sigma^*(a) is congruent to -a modulo I^2 for each homogeneous a in I, and by homogeneous decomposition and linearity sigma^* induces -id on all of I/I^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** For p=0, lem-stage1-exterior-cohomology gives A/I=A^0=reals*1, and unitality of sigma^* gives id=(-1)^0 id. For p>=1, I^p/I^{p+1} is spanned by classes of products a_1...a_p with a_i in I. Node 1.3 lets us write sigma^*(a_i)=-a_i+r_i with r_i in I^2; multiplicativity then gives sigma^*(a_1...a_p)=(-1)^p a_1...a_p modulo I^{p+1}, because every other expanded term has at least p+1 factors from I. Therefore sigma^* induces (-1)^p id on I^p/I^{p+1}, and, being degree-preserving, on each component (I^p intersect A^n)/(I^{p+1} intersect A^n).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** By lem-stage1-exterior-cohomology, A is a graded exterior algebra on odd-positive-degree homogeneous generators, and I=A^+ is its ideal spanned by nonempty generator monomials. Consequently I^p is spanned by generator monomials of exterior length at least p, so I^p/I^{p+1} is spanned by those of length exactly p (with the empty monomial for p=0). Every length-p monomial has total cohomological degree congruent to p modulo 2 because every generator degree is odd. Thus (I^p/I^{p+1})^n=0 unless n is congruent to p modulo 2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** For p>=0 and n=p+q>=0, E^{p,q}=(I^p intersect A^n)/(I^{p+1} intersect A^n). The preceding preservation and associated-graded calculation show that sigma^* preserves F^{p,q} and acts on E^{p,q} by (-1)^p; if E^{p,q} is nonzero, exterior-length parity gives (-1)^p=(-1)^n=(-1)^(p+q), while on a zero component the asserted scalar action is automatic. This proves the contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

