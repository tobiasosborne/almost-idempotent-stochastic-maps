# Proof Export

## Node 1

**Statement:** For all reals K_R, L, K_C >= 0 there is a universal delta_R(K_R,L,K_C) in (0,2^(-16)] such that no finite exact signed idempotent P with 0 < delta(P) <= delta_R admits full row-point fibers represented by v and f, a real A >= 4 and a point q of the row polytope K(P) with sqrt(delta(P))/2 <= ||q - p_v||_1 <= 2*sqrt(delta(P)) and ||p_f - p_v + A*(q - p_v)||_1 <= K_R*delta(P), and an affine chi with chi(p_v) = 0, chi(q) = 1, and |chi(x) - chi(y)| <= ||x - y||_1/||q - p_v||_1 for all x,y in K(P), such that sum_{Q: |chi(p_Q)| > L} max(c_Q, 0) <= K_C*delta(P), where c_Q = sum_{j in Q} P_{vj}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix K_R,L,K_C >= 0 and set B := K_C+1+(K_C+K_R+1)/4, H := 2L+6B, and delta_R := min{2^(-16), 1/(4H^2)}. Then B >= 5/4 and H > 0, so delta_R depends only on the three fixed real parameters, is independent of the dimension and of P, and belongs to (0,2^(-16)].

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For these constants, every putative configuration satisfying all hypotheses of node 1 with delta := delta(P) in (0,delta_R], tau := sqrt(delta), D := q-p_v, and s := ||D||_1 necessarily satisfies 1 <= tau*[2L+2(2+4delta)B].

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Let I be the finite index set and write q as a convex combination q = sum_i lambda_i p_i. By def-signed-idempotent every row p_i has total mass one, and by def-negative-mass its negative mass nu(p_i) := sum_j max(-P_ij,0) is at most delta. Coordinatewise convexity of x -> max(-x,0) gives q*1 = 1 and nu(q) <= sum_i lambda_i nu(p_i) <= delta. Consequently, for every coordinate subset U, q(U) >= -delta and p_f(U) >= -delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** The scale window gives s >= tau/2 > 0, hence q != p_v. For every full row-point fiber Q define d_Q := sum_{j in Q}(q_j-P_vj). Applying the registered external lem-hx-transverse-moment-identity with q0=p_v, q1=q, and the given affine chi gives the exact unit moment sum_Q d_Q*chi(p_Q) = 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Every actual row p_i has ||p_i||_1 = 1+2nu(p_i) <= 1+2delta, so any two row points have l1-distance at most 2+4delta. Thus the Lipschitz hypothesis and chi(p_v)=0 give |chi(p_Q)| <= (2+4delta)/s for every fiber Q. For the core C := {Q: |chi(p_Q)| <= L}, grouping coordinates cannot increase variation, so sum_{Q in C}|d_Q| <= sum_Q|d_Q| <= ||q-p_v||_1 = s, and therefore the absolute core contribution is at most Ls.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Let T := {Q: |chi(p_Q)| > L}, split it as T_- := {Q in T: d_Q<0}, T_+ := {Q in T: d_Q>0}, and T_0 := {Q in T: d_Q=0}, and put c_Q := sum_{j in Q}P_vj. The tail cap, the negative-mass subset budgets, A>=4, and R := p_f-p_v+A(q-p_v) with ||R||_1 <= K_R*delta imply sum_{Q in T}|d_Q| <= [K_C+1+(K_C+K_R+1)/4]*delta = B*delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.4.1

**Statement:** Let U_- be the union of the coordinate fibers in T_-. Since d_Q = sum_{j in Q}(q_j-P_vj) = q(Q)-c_Q is negative on T_-, one has sum_{Q in T_-}|d_Q| = c(U_-)-q(U_-). Now c(U_-) <= sum_{Q in T_-}max(c_Q,0) <= K_C*delta by the tail cap, while q(U_-) >= -nu(q) >= -delta. Hence sum_{Q in T_-}|d_Q| <= (K_C+1)*delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.4.2

**Statement:** Let U_+ be the union of the coordinate fibers in T_+ and D_+ := sum_{Q in T_+}d_Q = sum_{Q in T_+}|d_Q|. Summing R := p_f-p_v+A(q-p_v) over U_+ gives R(U_+) = p_f(U_+)-c(U_+)+A*D_+, hence A*D_+ = c(U_+)+R(U_+)-p_f(U_+). The tail cap gives c(U_+) <= K_C*delta, the residual bound gives R(U_+) <= ||R||_1 <= K_R*delta, and def-negative-mass gives -p_f(U_+) <= nu(p_f) <= delta. Thus A*D_+ <= (K_C+K_R+1)*delta and, because A>=4, sum_{Q in T_+}|d_Q| <= (K_C+K_R+1)*delta/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.4.3

**Statement:** If sum_{Q in T_-}|d_Q| <= (K_C+1)*delta and sum_{Q in T_+}|d_Q| <= (K_C+K_R+1)*delta/4, then, because T_-, T_+, T_0 are disjoint and every Q in T_0 has d_Q=0, one has sum_{Q in T}|d_Q| <= (K_C+1)*delta+(K_C+K_R+1)*delta/4 = B*delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.5

**Statement:** Whenever the same putative configuration has the unit moment sum_Q d_Q*chi(p_Q)=1, the core bounds |chi(p_Q)|<=L and sum_C|d_Q|<=s, and the tail bounds |chi(p_Q)|<=(2+4delta)/s and sum_T|d_Q|<=B*delta, the triangle inequality yields 1 <= Ls+(2+4delta)B*delta/s. The actor window s<=2tau and s>=tau/2, together with delta=tau^2, then gives 1 <= tau*[2L+2(2+4delta)B].

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For the constants above and every 0 < delta <= delta_R, the numerical inequality 1 <= sqrt(delta)*[2L+2(2+4delta)B] is impossible: delta <= 2^(-16) gives 2+4delta < 3, while delta <= 1/(4H^2) gives sqrt(delta)*H <= 1/2; since B>0, the displayed right side is strictly less than sqrt(delta)*(2L+6B) = sqrt(delta)*H <= 1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

