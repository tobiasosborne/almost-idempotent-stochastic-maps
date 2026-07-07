# Proof Export

## Node 1

**Statement:** CS low-slab pincer: for an exact signed idempotent P, a row index v with nu_v = sum_j max(-P_vj, 0), an affine h with h(p_v) = 0 and 0 <= h(p_j) <= 1 for every row j, and every s > 0, one has sum over {j : h(p_j) >= s} of max(P_vj, 0) <= nu_v / s.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let a_j = P_vj, h_j = h(p_j), a_j^+ = max(a_j, 0), and a_j^- = max(-a_j, 0). Exact signed idempotence and affinity give the scalar reproduction identity 0 = sum_j a_j h_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By def-signed-idempotent, P^2 = P and P 1 = 1. Therefore for every coordinate k, (p_v)_k = P_vk = sum_j P_vj P_jk, so p_v = sum_j a_j p_j; also sum_j a_j = 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Since h is affine and the coefficients a_j sum to 1, applying h to p_v = sum_j a_j p_j gives h(p_v) = sum_j a_j h(p_j). The hypothesis h(p_v)=0 then gives 0 = sum_j a_j h_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** The scalar reproduction identity and the bounds 0 <= h_j <= 1 imply sum_j a_j^+ h_j <= nu_v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For every j, a_j = a_j^+ - a_j^- with a_j^+, a_j^- >= 0. Substituting this into 0 = sum_j a_j h_j gives sum_j a_j^+ h_j = sum_j a_j^- h_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Because 0 <= h_j <= 1 and a_j^- >= 0, one has sum_j a_j^- h_j <= sum_j a_j^-. Since a_j = P_vj, the definition of nu_v gives sum_j a_j^- = sum_j max(-P_vj,0) = nu_v, hence sum_j a_j^+ h_j <= nu_v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Using validated node 1.2.1, sum_j a_j^+ h_j = sum_j a_j^- h_j. The bounds 0 <= h_j <= 1 and a_j^- >= 0 give sum_j a_j^- h_j <= sum_j a_j^-. Since a_j = P_vj, a_j^- = max(-P_vj,0), so sum_j a_j^- = nu_v by the definition of nu_v. Therefore sum_j a_j^+ h_j <= nu_v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For A_s = {j : h_j >= s}, the inequality s * sum_{j in A_s} a_j^+ <= sum_j a_j^+ h_j holds; since s > 0, combining with the previous bound gives sum_{j in A_s} max(P_vj,0) <= nu_v / s.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For each j in A_s, h_j >= s and a_j^+ >= 0, so s a_j^+ <= a_j^+ h_j. Summing over A_s gives s * sum_{j in A_s} a_j^+ <= sum_{j in A_s} a_j^+ h_j <= sum_j a_j^+ h_j, since all a_j^+ h_j are nonnegative.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Within the notation a_j = P_vj, h_j = h(p_j), a_j^+ = max(a_j,0), and A_s = {j : h_j >= s}, the locally established sign-split estimate sum_j a_j^+ h_j <= nu_v and high-slab estimate s * sum_{j in A_s} a_j^+ <= sum_j a_j^+ h_j imply s * sum_{j in A_s} a_j^+ <= nu_v. Since s > 0, division by s yields sum_{j : h(p_j) >= s} max(P_vj,0) <= nu_v / s.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.1

**Statement:** Re-derive the sign-split bound inside node 1.3.2. Put a_j = P_vj, h_j = h(p_j), a_j^+ = max(a_j,0), and a_j^- = max(-a_j,0). Since P is an exact signed idempotent, P^2 = P and P 1 = 1, so p_v = sum_j a_j p_j and sum_j a_j = 1. Affineness of h and h(p_v)=0 give 0 = sum_j a_j h_j. As a_j = a_j^+ - a_j^- and the sums are finite, sum_j a_j^+ h_j = sum_j a_j^- h_j. Since 0 <= h_j <= 1 and a_j^- >= 0, sum_j a_j^- h_j <= sum_j a_j^- = sum_j max(-P_vj,0) = nu_v. Hence sum_j a_j^+ h_j <= nu_v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.2

**Statement:** Re-derive the high-slab localization inside node 1.3.2. Let A_s = {j : h_j >= s}. For each j in A_s, h_j >= s and a_j^+ >= 0, hence s a_j^+ <= a_j^+ h_j. Summing over A_s gives s * sum_{j in A_s} a_j^+ <= sum_{j in A_s} a_j^+ h_j. Also every omitted term a_j^+ h_j is nonnegative because a_j^+ >= 0 and h_j >= 0, so sum_{j in A_s} a_j^+ h_j <= sum_j a_j^+ h_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.2.3

**Statement:** Combining the two preceding children gives s * sum_{j in A_s} a_j^+ <= nu_v. Since s > 0, division by s gives sum_{j in A_s} a_j^+ <= nu_v / s. Finally A_s = {j : h_j >= s} = {j : h(p_j) >= s} and a_j^+ = max(P_vj,0), which is exactly sum over {j : h(p_j) >= s} of max(P_vj,0) <= nu_v / s.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

