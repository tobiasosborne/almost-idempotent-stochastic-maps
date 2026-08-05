# Proof Export

## Node 1

**Statement:** Kitaev diagonal repair: the direct-sum diagonal formula printed at approximate_algebras.tex:1254 and :2780-2783 is false (already for B=C direct-sum C), but every finite-dimensional C*-algebra B=direct-sum_{r=1}^m M_{d_r} has a finite phase-balanced diagonal D=sum_t q_t W_t^dagger tensor W_t with unitary W_t, q_t >= 0, sum_t q_t=1, ZD=DZ for every Z in B, pi(D)=I_B, and projective norm ||D||_pi=sum_t q_t||W_t^dagger||||W_t||=1, independently of block count and block dimensions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** For B=C direct-sum C, each component diagonal is 1 tensor 1, so each printed prescription recorded by GT-kitaev-printed-direct-sum-formula-1254 and GT-kitaev-printed-direct-sum-formula-2780-2783 produces I_B tensor I_B; with Z=(1,0), Z(I_B tensor I_B)=Z tensor I_B differs from (I_B tensor I_B)Z=I_B tensor Z, hence the printed element is not central and is not a diagonal by def-fd-cstar-diagonal.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** In each scalar summand C, choose the valid one-term component-diagonal representation p=1 and U=1. Substitution into each of GT-kitaev-printed-direct-sum-formula-1254 and GT-kitaev-printed-direct-sum-formula-2780-2783 gives the single term (1 direct-sum 1)^dagger tensor (1 direct-sum 1)=I_B tensor I_B. For Z=(1,0), the tensor-block coordinates of Z tensor I_B and I_B tensor Z differ (for example at block (1,2)), so the two module actions differ and def-fd-cstar-diagonal rules out this element as a diagonal.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For every B=direct-sum_{r=1}^m M_{d_r}, an explicit finite Weyl-unitary and sign-phase average produces D=sum_t q_t W_t^dagger tensor W_t with all W_t unitary, q_t>=0 and sum_t q_t=1; this D obeys ZD=DZ for every Z in B, pi(D)=I_B, and ||D||_pi=sum_t q_t||W_t^dagger||||W_t||=1 independently of m and the d_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For each d>=1, let omega=exp(2*pi*i/d), use indices in Z/dZ and matrix units E_ij, and set U_ab=sum_k omega^(bk) E_{k+a,k}. Then every U_ab is unitary and (1/d^2) sum_{a,b} U_ab^dagger tensor U_ab = D_d := (1/d) sum_{i,j} E_ij tensor E_ji.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.1

**Statement:** For U_ab=sum_k omega^(bk)E_{k+a,k}, one has U_ab e_k=omega^(bk)e_{k+a}; hence U_ab sends an orthonormal basis to an orthonormal basis and is unitary (also for d=1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.2

**Statement:** Expanding U_ab^dagger tensor U_ab gives sum_{k,l} omega^(b(l-k)) E_{k,k+a} tensor E_{l+a,l}; since sum_{b=0}^{d-1}omega^(b(l-k)) is d if l=k modulo d and 0 otherwise, averaging over a,b gives (1/d)sum_{a,k}E_{k,k+a} tensor E_{k+a,k}=(1/d)sum_{i,j}E_ij tensor E_ji.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For gamma=((a_r,b_r))_{r=1}^m and sigma in {+1,-1}^m, set W_{gamma,sigma}=direct-sum_r sigma_r U^{(r)}_{a_r b_r} and q_{gamma,sigma}=2^(-m) product_r d_r^(-2). This is a finite family, every W_{gamma,sigma} is unitary, every q is positive, and the q's sum to 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** A finite direct sum of the unitary matrices sigma_r U^{(r)}_{a_r b_r} is unitary because each sigma_r has modulus one and blockwise multiplication by its adjoint gives direct-sum_r I_{d_r}; hence every W_{gamma,sigma} is unitary.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** There are 2^m product_r d_r^2 pairs (gamma,sigma), each q equals 2^(-m)product_r d_r^(-2)>0, so their sum is exactly 1; in particular the family and its convex coefficients are finite.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** For D=sum_{gamma,sigma} q_{gamma,sigma} W_{gamma,sigma}^dagger tensor W_{gamma,sigma}, the identity 2^(-m) sum_sigma sigma_r sigma_s=1 when r=s and 0 otherwise, together with the block Weyl averages, gives D=sum_r iota_r tensor iota_r(D_{d_r}); thus all cross-block tensor components vanish exactly.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** For r=s, sigma_r sigma_s=1 for every sign vector, so 2^(-m)sum_sigma sigma_r sigma_s=1; for r not equal s, pairing each sigma with the vector obtained by flipping sigma_r reverses sigma_r sigma_s and proves the average is 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.2

**Statement:** The block expansion W_{gamma,sigma}^dagger tensor W_{gamma,sigma}=sum_{r,s}sigma_r sigma_s iota_r(U^{(r),dagger}_{a_r b_r}) tensor iota_s(U^{(s)}_{a_s b_s}), after sign averaging, retains only r=s. For fixed r, summing the independent gamma coordinates outside r cancels their factors d_u^(-2), while the r-coordinate gives d_r^(-2)sum_{a_r,b_r}U^{(r),dagger}_{a_r b_r} tensor U^{(r)}_{a_r b_r}=D_{d_r}; therefore D=sum_r iota_r tensor iota_r(D_{d_r}).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** The element D_0=sum_r iota_r tensor iota_r(D_{d_r}), with D_d=(1/d)sum_{i,j}E_ij tensor E_ji, satisfies ZD_0=D_0Z for every Z in direct-sum_r M_{d_r} and pi(D_0)=I_B, hence is a diagonal by def-fd-cstar-diagonal.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.4.1

**Statement:** For a matrix unit X=E_ab in M_d, XD_d=(1/d)sum_j E_aj tensor E_jb=D_dX; by linearity this holds for every X in M_d. Since D_0 has only (r,r) tensor-block components, applying this calculation in each summand gives ZD_0=D_0Z for every Z=direct-sum_r Z_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.4.2

**Statement:** For every block M_d, the multiplication map satisfies pi(D_d)=(1/d)sum_{i,j}E_ij E_ji=(1/d)sum_{i,j}E_ii=sum_i E_ii=I_{M_d}; since multiplication preserves matching block embeddings, pi(D_0)=sum_r iota_r(pi(D_{d_r}))=direct-sum_r I_{M_{d_r}}=I_B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.2.4.2.1

**Statement:** For each block M_d, the matrix-unit identity E_ij E_ji=E_ii gives pi(D_d)=(1/d) sum_{i,j} E_ii=(1/d) sum_i d E_ii=sum_i E_ii=I_{M_d}. Because multiplication in B=direct-sum_r M_{d_r} preserves each matching block embedding iota_r, pi(D_0)=sum_r iota_r(pi(D_{d_r}))=direct-sum_r I_{M_{d_r}}=I_B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.5

**Statement:** For the above D, the displayed convex-unitary representation has sum_{gamma,sigma} q_{gamma,sigma}||W_{gamma,sigma}^dagger||||W_{gamma,sigma}||=1; GT-kitaev-projective-tensor-norm gives ||D||_pi<=1, while pi(D)=I_B forces ||D||_pi>=1, so ||D||_pi=1 for every finite m and every positive d_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.5.1

**Statement:** Every W_{gamma,sigma} is unitary, so ||W_{gamma,sigma}||=||W_{gamma,sigma}^dagger||=1; since the nonnegative q's sum to 1, the displayed representation cost is sum q||W^dagger||||W||=sum q=1, and the infimum formula in GT-kitaev-projective-tensor-norm yields ||D||_pi<=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.5.2

**Statement:** For every finite tensor representation C=sum_l A_l tensor B_l, triangle inequality and submultiplicativity give ||pi(C)||=||sum_l A_lB_l||<=sum_l||A_l||||B_l||; taking the infimum in GT-kitaev-projective-tensor-norm gives ||pi(C)||<=||C||_pi. Thus pi(D)=I_B and ||I_B||=1 imply ||D||_pi>=1, which with the upper bound proves equality without dependence on m or d_r.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

