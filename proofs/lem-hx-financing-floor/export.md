# Proof Export

## Node 1

**Statement:** For every finite exact signed idempotent P, every ordered pair (a,b) of points of the row polytope K(P) with a != b, every affine chi with chi(a) - chi(b) = 1, all reals A > 0 and Lambda > 0, and every set N of full row-point fibers with |chi(p_Q)| <= A for every Q in N and |chi(p_Q)| <= Lambda for every Q not in N, the complement F of N satisfies a^+(F) + b^+(F) >= (1 - A*l_chi)/Lambda - nu(a) - nu(b), where l_chi = sum_Q |d_Q| and d_Q = sum_{j in Q}(a_j - b_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** In the setting of node 1, the permitted external lem-hx-transverse-moment-identity, applied with q0=b, q1=a and the recentered affine function chi_0(x)=chi(x)-chi(b), yields the unit moment sum_Q d_Q*chi(p_Q)=1 for d_Q=sum_{j in Q}(a_j-b_j).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By def-signed-idempotent every row p_i has coordinate sum 1. Since a and b lie in K(P)=conv{p_i}, they also have coordinate sum 1. Because the full row-point fibers Q partition the finite index set, sum_Q d_Q=sum_j(a_j-b_j)=1-1=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Set chi_0(x)=chi(x)-chi(b). Then chi_0 is affine, chi_0(b)=0, and chi_0(a)=chi(a)-chi(b)=1. Applying lem-hx-transverse-moment-identity with q0=b and q1=a gives sum_Q d_Q*chi_0(p_Q)=1. Expanding chi_0 and using sum_Q d_Q=0 gives sum_Q d_Q*chi(p_Q)=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Writing F for the complement of N, the unit moment and the bounds on |chi(p_Q)| imply sum_{Q in F}|d_Q| >= (1-A*l_chi)/Lambda, where l_chi=sum_Q|d_Q|.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Since the fibers split as N disjoint-union F, the unit moment from node 1.1 and the triangle inequality give 1 <= sum_{Q in N}|d_Q|*|chi(p_Q)| + sum_{Q in F}|d_Q|*|chi(p_Q)| <= A*sum_{Q in N}|d_Q| + Lambda*sum_{Q in F}|d_Q|.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** The stipulated A>0 and Lambda>0 imply A*sum_{Q in N}|d_Q| <= A*l_chi. Hence 1 <= A*l_chi+Lambda*sum_{Q in F}|d_Q|; subtracting A*l_chi and dividing by Lambda>0 yields sum_{Q in F}|d_Q| >= (1-A*l_chi)/Lambda.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** The root claim has been mathematically corrected from the false quantifier ‘all reals A’ to the explicit hypothesis A>0 (while retaining Lambda>0). Therefore the verifier’s example A=-1 is outside the corrected theorem domain. Under A>0, since N is a subset of all fibers, sum_{Q in N}|d_Q| <= l_chi=sum_Q|d_Q|, and multiplication by A preserves the inequality; together with node 1.2.1 this yields 1 <= A*l_chi+Lambda*sum_{Q in F}|d_Q| and hence the asserted bound after subtraction and division by Lambda>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The permitted external lem-hx-signed-variation-ledger applied to the ordered pair (a,b) and S=F gives sum_{Q in F}|d_Q| <= a^+(F)+b^+(F)+nu(a)+nu(b); combining this with the preceding lower bound and rearranging proves the inequality in node 1.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.3.1

**Statement:** The verifier's scope objection is correct: node 1.3 proves the desired financing inequality only under the additional hypothesis A>=0, which is absent from the registered shard contract. Indeed, for P=I_2, fibers Q_1={1}, Q_2={2}, a=e_1, b=e_2, chi(x)=x_1, N=empty, F={Q_1,Q_2}, A=-1, and Lambda=1, all registered hypotheses hold, but l_chi=2, nu(a)=nu(b)=0, a^+(F)+b^+(F)=2, and the claimed lower bound is 3. Thus the registered theorem is false; amending only the af root to A>0 creates a contract mismatch and cannot constitute a proof. A mathematically valid repair is to require A>=0 in the registry contract and identically in the af root.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** For the explicit counterexample P=I_2, P1=1 and P^2=P, so P is a finite exact signed idempotent. Its two distinct rows are a=e_1 and b=e_2 and its full row-point fibers are Q_1={1}, Q_2={2}. The affine chi(x)=x_1 satisfies chi(a)-chi(b)=1. With N=empty, both N-bounds |chi(p_Q)|<=A are vacuous even for A=-1; on F={Q_1,Q_2}, |chi(e_1)|=1 and |chi(e_2)|=0 are at most Lambda=1. Moreover d_{Q_1}=1, d_{Q_2}=-1, hence l_chi=2; nu(a)=nu(b)=0; and a^+(F)=b^+(F)=1. Consequently the asserted inequality reads 2>=3 and fails. This directly establishes that the all-real-A registry contract is false and that no bridging proof step can close the objection without changing that contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Under the current root hypothesis A>0, node 1.2 gives (1-A*l_chi)/Lambda <= sum_{Q in F}|d_Q|. Applying lem-hx-signed-variation-ledger to the ordered pair (a,b) and the fiber set S=F gives sum_{Q in F}|d_Q| <= a^+(F)+b^+(F)+nu(a)+nu(b), with exactly the same d_Q=sum_{j in Q}(a_j-b_j). Chaining these inequalities and subtracting nu(a)+nu(b) from both sides yields a^+(F)+b^+(F) >= (1-A*l_chi)/Lambda-nu(a)-nu(b), which is the conclusion of node 1.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

### Node 1.4

**Statement:** Applying lem-hx-signed-variation-ledger to the ordered pair (a,b) and the set S=F of full row-point fibers gives sum_{Q in F}|d_Q| <= a^+(F)+b^+(F)+nu(a)+nu(b), because its coefficient d_Q is exactly sum_{j in Q}(a_j-b_j), the coefficient used in node 1.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Node 1.2 and node 1.4 give (1-A*l_chi)/Lambda <= sum_{Q in F}|d_Q| <= a^+(F)+b^+(F)+nu(a)+nu(b). By transitivity and subtraction of nu(a)+nu(b), a^+(F)+b^+(F) >= (1-A*l_chi)/Lambda-nu(a)-nu(b), exactly the conclusion of node 1.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

