# Proof Export

## Node 1

**Statement:** For every finite exact signed idempotent P, every pair of row indices (r,s), and every point c of the row polytope K(P), the full row-point fibers Q with ||p_Q - c||_1 > 1/2 jointly carry positive coefficient mass P_r^+ + P_s^+ at least ||p_r - p_s||_1/(2*(2 + 4*delta(P))) - 2*delta(P).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix arbitrary admissible P,r,s,c, put delta=delta(P), a=p_r, b=p_s, ell=||a-b||_1, and let F be the full row-point fibers Q with ||p_Q-c||_1>1/2. If ell=0, then P_r^+(F)+P_s^+(F)>=0>=ell/(2*(2+4*delta))-2*delta, so the claimed bound holds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** With the same notation, if ell>0 then P_r^+(F)+P_s^+(F)>=ell/(2*(2+4*delta))-2*delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Choose u in [-1,1]^n coordinatewise so that u_j(a_j-b_j)=|a_j-b_j|, and define the affine functional chi(x)=u dot (x-c)/ell. Then chi(a)-chi(b)=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Let N be the full row-point fibers Q with ||p_Q-c||_1<=1/2, set A=1/(2*ell), and set Lambda=(2+4*delta)/ell. Then |chi(p_Q)|<=A for Q in N and |chi(p_Q)|<=Lambda for Q not in N; moreover A,Lambda>0 and the complement of N is exactly F.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Because ||u||_infinity<=1, |chi(x)|<=||x-c||_1/ell for every x. Hence for every Q in N, |chi(p_Q)|<=1/(2*ell)=A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** By def-signed-idempotent, any two rows of P have l1-distance at most 2+4*delta. Since c is a convex combination of rows, ||p_Q-c||_1<=2+4*delta for every row point p_Q, and therefore |chi(p_Q)|<=Lambda for every Q not in N. Since ell>0 and delta>=0, A,Lambda>0; by their definitions, the complement of N is exactly F.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** For d_Q=sum_{j in Q}(a_j-b_j) and l_chi=sum_Q |d_Q|, one has l_chi<=ell; also nu(a)+nu(b)<=2*delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** The full row-point fibers partition the coordinate indices, so the triangle inequality gives l_chi=sum_Q |sum_{j in Q}(a_j-b_j)|<=sum_j |a_j-b_j|=ell.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.2

**Statement:** Because a=p_r and b=p_s are rows of P, def-negative-mass gives nu(a)<=delta(P)=delta and nu(b)<=delta(P)=delta, hence nu(a)+nu(b)<=2*delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Applying lem-hx-financing-floor with the preceding chi,A,Lambda,N gives P_r^+(F)+P_s^+(F)>=ell/(2*(2+4*delta))-2*delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.4.1

**Statement:** The hypotheses established above permit the exact external lem-hx-financing-floor, which yields P_r^+(F)+P_s^+(F)>= (1-A*l_chi)/Lambda-nu(a)-nu(b). Since l_chi<=ell, A=1/(2*ell), Lambda=(2+4*delta)/ell, and nu(a)+nu(b)<=2*delta, the right side is at least (1-1/2)/((2+4*delta)/ell)-2*delta=ell/(2*(2+4*delta))-2*delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

