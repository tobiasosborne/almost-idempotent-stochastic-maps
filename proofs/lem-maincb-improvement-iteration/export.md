# Proof Export

## Node 1

**Statement:** There are universal e_it > 0, K_disp < infinity, and K_floor < infinity such that, if B is a finite-dimensional C*-algebra, A is an extended epsilon-C*-algebra, and v:B->A is an extended d-inclusion with d+epsilon <= e_it, then one dagger-preserving v_tilde, with v_tilde_n = I_n tensor v_tilde, satisfies sup_n ||v_tilde_n - v_n|| <= K_disp*d and has extended defect at most K_floor*epsilon; for epsilon > 0 it is reached after finitely many correction steps, and for epsilon = 0 it is their operator-norm limit.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let K:=K_step>=1 and e:=e_step>0 be the universal witnesses from lem-maincb-improvement-one-step, and set e_it:=min{e,1/(4K)}, K_disp:=4K, and K_floor:=2K. For data satisfying d+epsilon<=e_it, put v_0:=v and d_0:=d. The cited lemma is applicable at j=0 and, whenever d_j<=d_0, also at j because d_j+epsilon<=d_0+epsilon<=e_it<=e; it supplies a dagger-preserving v_{j+1}, amplified as I_n tensor v_{j+1}, with sup_n||v_{j+1,n}-v_{j,n}||<=K d_j and extended defect d_{j+1}<=K(d_j^2+epsilon). If d_j>2K epsilon, then K d_j^2<=d_j/4 (since d_j<=d_0<=1/(4K)) and K epsilon<d_j/2, hence d_{j+1}<=(3/4)d_j<=d_0. Thus corrections may be iterated while above the floor. If epsilon>0 and already d_0<=2K epsilon, perform exactly the first correction anyway; then d_1<=K d_0^2+K epsilon<=d_0/4+K epsilon<=3K epsilon/2<=2K epsilon. This mandatory first step ensures the selected output is dagger-preserving.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Assume epsilon>0. If d_0<=2K epsilon, the construction in 1.1 stops after its mandatory first correction with d_1<=2K epsilon. Otherwise, repeatedly apply 1.1 while d_j>2K epsilon and stop at the first N>=1 with d_N<=2K epsilon. Such N is finite: before stopping, induction gives d_j<=(3/4)^j d_0, whereas a positive geometric sequence eventually falls below the positive number 2K epsilon. Consequently v_N is dagger-preserving and is an extended d_N-inclusion with d_N<=K_floor epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** In the epsilon>0 construction, the complete displacement telescopes. In the one-step floor case it is at most K d_0<=4K d_0. Otherwise every preterminal defect obeys d_j<=(3/4)^j d_0, so sup_n||v_{N,n}-v_{0,n}||<=sum_{j=0}^{N-1} sup_n||v_{j+1,n}-v_{j,n}||<=K sum_{j=0}^{N-1}d_j<=K d_0 sum_{j>=0}(3/4)^j=4K d_0=K_disp d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Assume epsilon=0 and apply the correction in 1.1 indefinitely. Then d_{j+1}<=K d_j^2<=d_j/4, so d_j<=4^{-j}d. Hence for k>j, sup_n||v_{k,n}-v_{j,n}||<=K sum_{r=j}^{k-1}d_r<=K d 4^{-j}/(1-1/4), which tends to zero uniformly in n. Completeness of A at level one and finite dimensionality of B therefore give an operator-norm limit linear map v_tilde:B->A; for each n its amplification is the limit of v_{j,n}=I_n tensor v_j, and the same tail estimate yields sup_n||v_tilde_n-v_n||<=K sum_{j>=0}d_j<=4K d/3<=K_disp d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The epsilon=0 limit from 1.4 is dagger-preserving and has extended defect zero. Indeed every v_j for j>=1 is dagger-preserving and the involution is isometric, so that identity passes to the operator-norm limit. At each fixed amplification, the two-sided (1+-d_j) norm bounds pass to the limit as d_j tends to zero. The d_j-homomorphism defect inequalities also pass to the limit because multiplication is continuous at every matrix level in the extended 0-C*-algebra (the product-norm axiom gives ||XY||<=||X||||Y||). Thus every v_tilde_n=I_n tensor v_tilde is a 0-homomorphism satisfying exact two-sided norm bounds, i.e. v_tilde is an extended 0-inclusion, and its extended defect is 0=K_floor epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** The constants in 1.1 are positive/finite and universal because the witnesses in lem-maincb-improvement-one-step are universal. For epsilon>0, nodes 1.2-1.3 provide the required finite correction output, floor, amplification identity, and displacement. For epsilon=0, nodes 1.4-1.5 provide their operator-norm limit with the same amplification identity, displacement bound, dagger preservation, and zero floor. These two exhaustive cases prove the root contract with e_it, K_disp, and K_floor chosen in 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

