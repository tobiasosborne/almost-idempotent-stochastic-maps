# Proof Export

## Node 1

**Statement:** Factorization bound: let P be an exact signed idempotent (square real matrix with P^2 = P and all row sums equal to 1), let delta(P) = max_i sum_j max(-P_ij, 0), let k = rank(P), and let U = (u_1, ..., u_k) be an actual-row basis of P (the rows p_{u_1}, ..., p_{u_k} of P form a basis of the row space of P) whose Gram volume satisfies Vol(U) >= (1/2) * Vol_max(P), where Vol_max(P) is the maximum Gram volume over all actual-row bases of P; define coordinates a_t(j) by p_j = sum_t a_t(j) p_{u_t}, and for each pivot index s in {1, ..., k} set beta_s(j) = P_{u_s j}, lambda_s(j) = 1 - a_s(j), mu_s(j) = sum_{t != s} max(-a_t(j), 0), sigma_s(j) = sum_{t != s} max(a_t(j), 0), E_s(j) = max(mu_s(j) - lambda_s(j), 0), Phi_s(U) = sum_j max(beta_s(j), 0) * E_s(j), and S*_s(U) = sum_j max(beta_s(j), 0) * (sigma_s(j) + 2 * max(-lambda_s(j), 0)); then for every pivot s, S*_s(U) <= 2 * Phi_s(U) + 6 * delta(P).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Pointwise reduction: fix a pivot s, write beta_j=beta_s(j), beta_j^+=max(beta_j,0), lambda_j=lambda_s(j), lambda_j^+=max(lambda_j,0), lambda_j^-=max(-lambda_j,0), and D_+=sum_j beta_j^+ lambda_j^+. Then S*_s(U) <= Phi_s(U)+2D_+. Reason: because P has row sums 1 and p_j=sum_t a_t(j)p_{u_t} while each pivot row also has row sum 1, one has sum_t a_t(j)=1 and hence lambda_j=sum_{t!=s} a_t(j)=sigma_s(j)-mu_s(j). The scalar inequality sigma_s(j)+2lambda_j^- <= E_s(j)+2lambda_j^+ follows by the two cases lambda_j>=0 and lambda_j<0; multiplying by beta_j^+ and summing gives the displayed bound.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Deficit estimate: for every fixed pivot s, with beta_j^+=max(beta_s(j),0), lambda_j^+=max(lambda_s(j),0), and D_+=sum_j beta_j^+ lambda_j^+, one has D_+ <= (1/2)*Phi_s(U)+3*delta(P).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Harmonic identity: for the fixed pivot s and every coordinate index t, sum_j beta_s(j)*a_t(j) equals 1 if t=s and equals 0 if t!=s; consequently sum_j beta_s(j)*lambda_s(j)=0. This follows from the row identity p_{u_s}P=p_{u_s} (because P^2=P), from p_j=sum_t a_t(j)p_{u_t}, from uniqueness of coordinates in the pivot-row basis, and from sum_j beta_s(j)=1 by the row-sum-one condition.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Cramer box and negative-beta mass: for every t and j, |a_t(j)|<=2; hence lambda_s(j)=1-a_s(j)<=3 for every j. Also sum_j max(-beta_s(j),0)<=delta(P). For the Cramer bound, if a_t(j)=0 there is nothing to prove; otherwise replacing pivot row p_{u_t} by actual row p_j gives an actual-row basis with Gram volume |a_t(j)|*Vol(U), so |a_t(j)|*Vol(U)<=Vol_max(P)<=2*Vol(U). The negative-beta inequality is the definition of delta(P) applied to the pivot row u_s.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Harmonic decomposition: write beta_j^+=max(beta_s(j),0), beta_j^-=max(-beta_s(j),0), lambda_j=lambda_s(j), lambda_j^+=max(lambda_j,0), lambda_j^-=max(-lambda_j,0), D_+=sum_j beta_j^+ lambda_j^+, V=sum_j beta_j^+ lambda_j^-, and D_-=sum_j beta_j^- lambda_j. If sum_j beta_s(j)lambda_s(j)=0, then D_+=V+D_- because 0=sum_j (beta_j^+-beta_j^-)(lambda_j^+-lambda_j^-)=(D_+-V)-D_-.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Overshoot bound: V<=Phi_s(U)/2. Indeed lambda_j=sigma_s(j)-mu_s(j) by the row-sum coordinate identity, so when lambda_j<0 one has E_s(j)=max(mu_s(j)-lambda_j,0)=sigma_s(j)+2*lambda_j^- >= 2*lambda_j^-; when lambda_j>=0 the term beta_j^+ lambda_j^- is zero. Multiplying by beta_j^+ and summing gives V<=Phi_s(U)/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.5

**Statement:** Negative-row bound: D_-<=3*delta(P). This follows from lambda_s(j)<=3 for all j and sum_j beta_j^-<=delta(P), since D_-=sum_j beta_j^- lambda_s(j)<=sum_j beta_j^-*3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.6

**Statement:** Deficit conclusion: the harmonic identity supplies the hypothesis of the harmonic decomposition, so D_+=V+D_-; the overshoot and negative-row bounds give V<=Phi_s(U)/2 and D_-<=3*delta(P). Hence D_+<=(1/2)*Phi_s(U)+3*delta(P).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Final assembly from validated components: fix an arbitrary pivot s and write D_+ as in node 1.1. Node 1.1 gives S*_s(U) <= Phi_s(U)+2D_+. The validated deficit-conclusion node 1.2.6 gives D_+ <= (1/2)*Phi_s(U)+3*delta(P), using the harmonic, decomposition, overshoot, and negative-row bounds already validated in 1.2.1--1.2.5. Therefore S*_s(U) <= Phi_s(U)+2*((1/2)*Phi_s(U)+3*delta(P)) = 2*Phi_s(U)+6*delta(P). Since s was arbitrary, the bound holds for every pivot s.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Bridge for the dependency challenge: for the fixed arbitrary pivot s, combine the validated pointwise reduction 1.1, S*_s(U) <= Phi_s(U)+2D_+, with the validated deficit conclusion 1.2.6, D_+ <= (1/2)*Phi_s(U)+3*delta(P). Substitution gives S*_s(U) <= Phi_s(U)+2*((1/2)*Phi_s(U)+3*delta(P)) = 2*Phi_s(U)+6*delta(P). Because the pivot s was arbitrary, this proves the required inequality for every pivot s without invoking the still-pending umbrella node 1.2 as an established premise.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.3.2

**Statement:** Bridge for the dependency challenge: for the fixed arbitrary pivot s, combine the validated pointwise reduction 1.1, S*_s(U) <= Phi_s(U)+2D_+, with the validated deficit conclusion 1.2.6, D_+ <= (1/2)*Phi_s(U)+3*delta(P). Substitution gives S*_s(U) <= Phi_s(U)+2*((1/2)*Phi_s(U)+3*delta(P)) = 2*Phi_s(U)+6*delta(P). Because the pivot s was arbitrary, this proves the required inequality for every pivot s without invoking the still-pending umbrella node 1.2 as an established premise.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

