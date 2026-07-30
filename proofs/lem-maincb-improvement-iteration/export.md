# Proof Export

## Node 1

**Statement:** There are universal e_it > 0, K_disp < infinity, and K_floor < infinity such that, if B is a finite-dimensional C*-algebra, A is an extended epsilon-C*-algebra, and v:B->A is an extended d-inclusion with d+epsilon <= e_it, then one dagger-preserving v_tilde, with v_tilde_n = I_n tensor v_tilde, satisfies sup_n ||v_tilde_n - v_n|| <= K_disp*d and is an extended K_floor*epsilon-inclusion; for epsilon > 0 it is reached after finitely many correction steps, and for epsilon = 0 it is their operator-norm limit.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let K:=K_step>=1 and e:=e_step>0 be the universal witnesses supplied by the registered external lem-maincb-improvement-one-step, and set e_it:=min{e,1/(4K)}, K_disp:=4K, and K_floor:=2K. For data in the root with d+epsilon<=e_it, put v_0:=v and d_0:=d. The external is applicable at j=0 and whenever d_j<=d_0, since d_j+epsilon<=d_0+epsilon<=e_it<=e; it supplies a dagger-preserving v_{j+1}, with v_{j+1,n}=I_n tensor v_{j+1}, sup_n||v_{j+1,n}-v_{j,n}||<=K d_j, and an extended d_{j+1}-inclusion satisfying d_{j+1}<=K(d_j^2+epsilon). If d_j>2K epsilon, then K d_j^2<=d_j/4 because d_j<=d_0<=1/(4K), while K epsilon<d_j/2, so d_{j+1}<=(3/4)d_j<=d_0. Thus the correction remains legal while above the floor. If epsilon>0 and d_0<=2K epsilon, perform exactly one correction; then d_1<=K d_0^2+K epsilon<=d_0/4+K epsilon<=3K epsilon/2<=2K epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Assume epsilon>0. If d_0<=2K epsilon, the single correction specified in 1.1 stops with d_1<=2K epsilon. Otherwise repeatedly invoke lem-maincb-improvement-one-step while d_j>2K epsilon and stop at the first N>=1 with d_N<=2K epsilon. This N is finite because before stopping the estimate in 1.1 gives d_j<=(3/4)^j d_0, and a positive geometric sequence eventually falls below 2K epsilon. Every correction output is dagger-preserving, so v_N is dagger-preserving; it is an extended d_N-inclusion with d_N<=K_floor epsilon. Unpacking def-extended-delta-inclusion, each defect and norm inequality with parameter d_N remains valid after replacing d_N by the larger K_floor epsilon, so v_N is an extended K_floor*epsilon-inclusion, with v_{N,n}=I_n tensor v_N.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For the epsilon>0 construction, the displacement telescopes. In the one-step floor case it is at most K d_0<=4K d_0. Otherwise every preterminal defect obeys d_j<=(3/4)^j d_0, so sup_n||v_{N,n}-v_{0,n}||<=sum_{j=0}^{N-1}sup_n||v_{j+1,n}-v_{j,n}||<=K sum_{j=0}^{N-1}d_j<=K d_0 sum_{j>=0}(3/4)^j=4K d_0=K_disp*d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Using validated nodes 1.1 and 1.2, set K:=K_step and K_disp:=4K, with d_0=d. They provide the finite epsilon>0 stopping construction v_0,...,v_N and, for each correction index 0<=j<N, the bounds sup_n||v_{j+1,n}-v_{j,n}||<=K d_j. If d_0<=2K epsilon then N=1, hence sup_n||v_{N,n}-v_{0,n}||<=K d_0<=K_disp d. If d_0>2K epsilon, then every j<N is preterminal (d_j>2K epsilon), so 1.1 gives d_{j+1}<=(3/4)d_j; induction yields d_j<=(3/4)^j d_0 for 0<=j<N. For every n, the triangle inequality gives ||v_{N,n}-v_{0,n}||<=sum_{j=0}^{N-1}||v_{j+1,n}-v_{j,n}||. Taking sup_n and using sup_n(sum_j a_{j,n})<=sum_j sup_n a_{j,n}, followed by the one-step displacement bounds, yields sup_n||v_{N,n}-v_{0,n}||<=K sum_{j=0}^{N-1}d_j<=K d_0 sum_{j=0}^{infinity}(3/4)^j=4K d_0=K_disp d. Thus both stopping cases prove the displacement asserted in 1.3.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Assume epsilon=0 and apply lem-maincb-improvement-one-step indefinitely. The construction is legal by 1.1, and d_{j+1}<=K d_j^2<=d_j/4, so d_j<=4^{-j}d. For k>j, sup_n||v_{k,n}-v_{j,n}||<=K sum_{r=j}^{k-1}d_r<=K d 4^{-j}/(1-1/4), which tends to zero uniformly in n. Completeness of A at level one and finite dimensionality of B give an operator-norm limit linear map v_tilde:B->A. For each n, its amplification I_n tensor v_tilde is the operator-norm limit of v_{j,n}=I_n tensor v_j, and the same tail estimate gives sup_n||v_tilde_n-v_n||<=K sum_{j>=0}d_j<=4K d/3<=K_disp*d.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** The epsilon=0 limit from 1.4 is dagger-preserving and is an extended 0-inclusion. Indeed every v_j for j>=1 is dagger-preserving by lem-maincb-improvement-one-step, and the involution is isometric by def-operator-space, so dagger preservation passes to the operator-norm limit. At each fixed amplification, the two-sided (1+-d_j) bounds in def-extended-delta-inclusion pass to the limit as d_j tends to zero. Its d_j-homomorphism defining relations also pass to the limit: when epsilon=0, def-extended-epsilon-cstar-algebra makes every target amplification a 0-C*-algebra, whose product is continuous with ||XY||<=||X||||Y||, and the unit, multiplication, linearity, and dagger identities therefore have zero limiting defect. Thus each v_tilde_n=I_n tensor v_tilde is a 0-homomorphism with exact two-sided norm bounds, so v_tilde is an extended 0-inclusion, equivalently an extended K_floor*epsilon-inclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Assume epsilon=0. The already validated convergence step 1.4 supplies maps v_j:B->A with extended defects d_j tending to 0, a linear operator-norm limit v_tilde:B->A, and, for every n, v_{j,n}=I_n tensor v_j converging in operator norm to v_tilde_n=I_n tensor v_tilde (indeed uniformly in n), together with the stated displacement bound. These are precisely the existence and convergence premises used in the limit passages of node 1.5.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** The constants e_it, K_disp, and K_floor chosen in 1.1 are respectively positive, finite, and universal because the witnesses in lem-maincb-improvement-one-step are universal. For epsilon>0, 1.2 and 1.3 give a finite correction output that is dagger-preserving, has the required amplification form, is an extended K_floor*epsilon-inclusion, and obeys the K_disp*d displacement bound. For epsilon=0, 1.4 and 1.5 give the operator-norm limit with the same amplification identity and displacement bound, dagger preservation, and an extended 0=K_floor*epsilon inclusion. The two cases are exhaustive and establish every assertion of the root contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.6.1

**Statement:** Dependency bridge: require nodes 1.1, 1.2, 1.3, 1.4, and 1.5 to be validated. Then 1.1 supplies universal positive/finite constants e_it, K_disp, K_floor and the legal correction setup. In the exhaustive case epsilon>0, 1.2 supplies a finite dagger-preserving amplified output that is an extended K_floor*epsilon-inclusion, while 1.3 supplies its displacement bound sup_n ||v_{N,n}-v_n|| <= K_disp*d. In the case epsilon=0, 1.4 supplies the operator-norm limit, its amplification identity, and displacement bound, while 1.5 supplies dagger preservation and the extended 0=K_floor*epsilon-inclusion property. Hence, only after all five dependencies are validated, these conclusions jointly imply every clause of the root contract.

**Type:** claim

**Inference:** local_discharge

**Status:** validated

**Taint:** clean

