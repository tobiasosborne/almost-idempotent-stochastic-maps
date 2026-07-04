# Proof Export

## Node 1

**Statement:** Collateral import bound: let P be a rank-3 exact signed idempotent (square real matrix with P^2 = P and all row sums equal to 1), let U = (u_0,u_1,u_2) be an actual-row chart whose rows p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space, define coordinates a_q(i) by p_i = sum_q a_q(i)p_{u_q}, beta_r(i) = P_{u_r i}, E_r(i) = max(sum_{q != r} max(-a_q(i),0) - (1 - a_r(i)), 0), and Phi_r(U) = sum_i max(beta_r(i),0)E_r(i); fix a pivot index s, a non-chart row j with c = a_s(j) > 0, a transverse index r != s, and let t be the remaining index, writing d_r = a_r(j) and d_t = a_t(j); on the pivot-removing chart V_j = U - u_s + j define new coordinates a_s^j(i) = a_s(i)/c and a_q^j(i) = a_q(i) - a_s(i)a_q(j)/c for q != s, E_r^j(i) = max(sum_{q != r} max(-a_q^j(i),0) - (1 - a_r^j(i)), 0), and Phi_r(V_j) = sum_i max(beta_r(i),0)E_r^j(i) (the transverse left-inverse row at r is unchanged by the move); define R_{r,j}(i) = (1/c - 1)*max(-a_s(i),0) + max(a_s(i)*d_t/c, 0) - a_s(i)*d_r/c and I_{r,j}(U) = sum_i max(beta_r(i),0)*max(R_{r,j}(i),0); then Phi_r(V_j) <= Phi_r(U) + I_{r,j}(U).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** It is enough to prove the pointwise row bound E_r^j(i) <= E_r(i) + max(R_{r,j}(i),0) for every row index i: multiplying by w_i=max(beta_r(i),0) >= 0 and summing over the finite row set gives Phi_r(V_j) <= Phi_r(U)+I_{r,j}(U) by the definitions of Phi_r(V_j), Phi_r(U), and I_{r,j}(U).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** For each row index i, w_i=max(beta_r(i),0) is nonnegative because the maximum of a real number and 0 is at least 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** If E_r^j(i) <= E_r(i)+max(R_{r,j}(i),0) for every i, then multiplying by w_i>=0 preserves the inequality: w_i E_r^j(i) <= w_i E_r(i)+w_i max(R_{r,j}(i),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** The row set is finite because P is a square real matrix; summing the preceding inequalities over i gives sum_i w_i E_r^j(i) <= sum_i w_i E_r(i)+sum_i w_i max(R_{r,j}(i),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** By the root definitions and the unchanged transverse left-inverse row, sum_i w_i E_r^j(i)=Phi_r(V_j), sum_i w_i E_r(i)=Phi_r(U), and sum_i w_i max(R_{r,j}(i),0)=I_{r,j}(U).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For every row index i, if B_i=max(-a_s(i),0)+max(-a_t(i),0)-1+a_r(i) and R_i=R_{r,j}(i), then the pivot-removing coordinate formulas give E_r^j(i) <= max(B_i+R_i,0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Fix an arbitrary row index i. Since r != s and t is the remaining chart index, the two indices q != r are exactly s and t, so E_r^j(i)=max(max(-a_s^j(i),0)+max(-a_t^j(i),0)-1+a_r^j(i),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** The pivot-removing coordinate formulas, as stated in the root and imported from external lem-pivot-removing-move, give a_s^j(i)=a_s(i)/c, a_t^j(i)=a_t(i)-a_s(i)d_t/c, and a_r^j(i)=a_r(i)-a_s(i)d_r/c; because c>0, max(-a_s^j(i),0)=(1/c)max(-a_s(i),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** For real x and y, max(x+y,0) <= max(x,0)+max(y,0); with x=-a_t(i) and y=a_s(i)d_t/c this gives max(-a_t^j(i),0)=max(-a_t(i)+a_s(i)d_t/c,0) <= max(-a_t(i),0)+max(a_s(i)d_t/c,0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** For all real x and y, max(x+y,0) <= max(x,0)+max(y,0): if x+y <= 0 then the left side is 0, while the right side is nonnegative; if x+y > 0 then max(x+y,0)=x+y <= max(x,0)+max(y,0) because x <= max(x,0) and y <= max(y,0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.2

**Statement:** With x=-a_t(i) and y=a_s(i)d_t/c, the scalar inequality gives max(-a_t(i)+a_s(i)d_t/c,0) <= max(-a_t(i),0)+max(a_s(i)d_t/c,0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.3

**Statement:** Since the coordinate formula gives a_t^j(i)=a_t(i)-a_s(i)d_t/c, the left side is max(-a_t^j(i),0), which proves the asserted bound for the t-coordinate contribution.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Substituting the preceding bounds into the inner expression for E_r^j(i) gives max(-a_s^j(i),0)+max(-a_t^j(i),0)-1+a_r^j(i) <= B_i+R_i, where B_i=max(-a_s(i),0)+max(-a_t(i),0)-1+a_r(i) and R_i=(1/c-1)max(-a_s(i),0)+max(a_s(i)d_t/c,0)-a_s(i)d_r/c=R_{r,j}(i).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.5

**Statement:** The map z -> max(z,0) is monotone, so applying it to the previous inequality gives E_r^j(i) <= max(B_i+R_i,0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every row index i, the scalar positive-part inequality max(X+Y,0) <= max(X,0)+max(Y,0), applied with X=B_i and Y=R_i, gives max(B_i+R_i,0) <= E_r(i)+max(R_{r,j}(i),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For all real X and Y, max(X+Y,0) <= max(X,0)+max(Y,0): if X+Y <= 0 the left side is 0, and if X+Y > 0 then X+Y <= max(X,0)+max(Y,0) because each real number is at most its maximum with 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Apply this scalar inequality with X=B_i and Y=R_i to obtain max(B_i+R_i,0) <= max(B_i,0)+max(R_i,0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** By the root definition of E_r(i) and because q != r means q is s or t, max(B_i,0)=max(max(-a_s(i),0)+max(-a_t(i),0)-1+a_r(i),0)=E_r(i).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.1

**Statement:** Within node 1.3.3, B_i is the local abbreviation max(-a_s(i),0)+max(-a_t(i),0)-1+a_r(i); it is not an independent variable or additional assumption.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.2

**Statement:** Since r != s and t is the remaining coordinate index among the three chart-coordinate labels, the coordinate labels q with q != r are exactly s and t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.3

**Statement:** The root definition gives E_r(i)=max(sum_{q != r} max(-a_q(i),0)-(1-a_r(i)),0), and using the preceding identification of the q != r labels this is max(max(-a_s(i),0)+max(-a_t(i),0)-1+a_r(i),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.4

**Statement:** Using the local abbreviation for B_i, max(B_i,0)=max(max(-a_s(i),0)+max(-a_t(i),0)-1+a_r(i),0), which is E_r(i) by the preceding step.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** Since R_i was defined as R_{r,j}(i), the preceding inequality is exactly max(B_i+R_i,0) <= E_r(i)+max(R_{r,j}(i),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.5

**Statement:** In this node B_i denotes max(-a_s(i),0)+max(-a_t(i),0)-1+a_r(i), and R_i denotes R_{r,j}(i), the same abbreviations used in node 1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Combining the preceding two pointwise estimates yields E_r^j(i) <= E_r(i)+max(R_{r,j}(i),0) for every row index i, and the summation step then proves the claimed collateral import bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Fix any row index i. Node 1.2 gives E_r^j(i) <= max(B_i+R_i,0), and node 1.3 gives max(B_i+R_i,0) <= E_r(i)+max(R_{r,j}(i),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.1

**Statement:** The first displayed inequality does not require pending parent node 1.2: validated nodes 1.2.1 through 1.2.5, applied to this fixed row index i, expand E_r^j(i) with q != r equal to s,t, substitute the pivot-removing coordinate formulas, use c > 0 and max(x+y,0) <= max(x,0)+max(y,0), identify B_i and R_i=R_{r,j}(i), and apply monotonicity of z -> max(z,0), giving E_r^j(i) <= max(B_i+R_i,0).

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.4.1.2

**Statement:** Dependency-pinned first inequality: requiring validated nodes 1.2.1, 1.2.2, 1.2.3, 1.2.4, and 1.2.5, their chain proves directly for this fixed row i that E_r^j(i) <= max(B_i+R_i,0); this cites only those validated children, not pending parent node 1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.1.3

**Statement:** Self-contained second inequality: set B_i=max(-a_s(i),0)+max(-a_t(i),0)-1+a_r(i) and R_i=R_{r,j}(i). Since r != s and t is the remaining chart index, the indices q != r are exactly s and t, so the root definition of E_r gives E_r(i)=max(B_i,0). The scalar inequality max(X+Y,0) <= max(X,0)+max(Y,0), applied with X=B_i and Y=R_i, gives max(B_i+R_i,0) <= max(B_i,0)+max(R_i,0)=E_r(i)+max(R_{r,j}(i),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** By transitivity of <=, E_r^j(i) <= E_r(i)+max(R_{r,j}(i),0) for that row index i; since i was arbitrary, the pointwise row bound holds for every i.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** Node 1.1 applies this pointwise row bound to the nonnegative weights max(beta_r(i),0) and identifies the resulting finite sums, yielding Phi_r(V_j) <= Phi_r(U)+I_{r,j}(U).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

