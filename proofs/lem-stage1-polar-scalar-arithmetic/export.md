# Proof Export

## Node 1

**Statement:** Universal Stage-1 polar arithmetic: for every C_rect, C_ch, C_pol, C_grp, C_path, C_der >= 1, e_rect in (0, 1/C_rect], and kappa_ch, kappa_pol, kappa_der in (0, 1/2], setting delta_* = min{1/4, kappa_ch/(4*C_ch), kappa_pol/(4*C_pol)}, epsilon_*^r = min{1/4, kappa_ch/(4*C_ch), kappa_pol/(4*C_pol), kappa_der/(8*C_der), 1/C_grp, delta_*/(12*C_path*C_grp)}, e_S1 = min{e_rect, epsilon_*^r/C_rect}, r_iso = min{delta_*/4, kappa_der/(8*C_der)}, epsilon_r = C_rect*epsilon_X, q = C_grp*epsilon_r, r_- = delta_* - C_pol*(epsilon_r*delta_* + delta_*^2), and eta = C_path*(q + epsilon_r*q + q^2), every 0 <= epsilon_X <= e_S1 satisfies C_ch*(epsilon_r + delta_*) <= kappa_ch, C_pol*(epsilon_r + delta_*) <= kappa_pol, q < r_-, C_path*q <= 1/4, eta < r_-, C_der*(epsilon_r + r_iso) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta_*))*r_iso + q < 2*delta_*; moreover r_- >= 3*delta_*/4, eta <= delta_*/4, and C_der*(r_iso + epsilon_r) <= kappa_der/4 < 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** From the minimum definitions and the stated ranges, the channel and polar bounds hold: C_ch*(epsilon_r + delta_*) <= kappa_ch, C_pol*(epsilon_r + delta_*) <= kappa_pol, and r_- >= 3*delta_*/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Because e_S1 <= epsilon_*^r/C_rect, 0 <= epsilon_X <= e_S1, and C_rect >= 1, one has 0 <= epsilon_r = C_rect*epsilon_X <= epsilon_*^r. Since epsilon_*^r <= kappa_ch/(4*C_ch) and delta_* <= kappa_ch/(4*C_ch), C_ch*(epsilon_r + delta_*) <= kappa_ch/2 <= kappa_ch.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** The same epsilon_r <= epsilon_*^r bound, together with epsilon_*^r <= kappa_pol/(4*C_pol) and delta_* <= kappa_pol/(4*C_pol), gives C_pol*(epsilon_r + delta_*) <= kappa_pol/2 <= kappa_pol.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Using r_- = delta_* - C_pol*(epsilon_r*delta_* + delta_*^2) = delta_*[1 - C_pol*(epsilon_r + delta_*)], the preceding minimum bounds give C_pol*(epsilon_r + delta_*) <= kappa_pol/2 <= 1/4; since delta_* > 0, therefore r_- >= (3/4)*delta_*.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** From the same hypotheses, q < r_-, C_path*q <= 1/4, eta <= delta_*/4, and eta < r_-.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** From epsilon_r <= epsilon_*^r <= delta_*/(12*C_path*C_grp), positivity of the coefficients, and q = C_grp*epsilon_r, one gets 0 <= q <= delta_*/(12*C_path) <= delta_*/12. Thus C_path*q <= delta_*/12 <= 1/48 < 1/4, using delta_* <= 1/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** The polar estimate follows directly from the defining minima: C_pol*(epsilon_r + delta_*) <= kappa_pol/2 <= 1/4, hence r_- = delta_*[1-C_pol*(epsilon_r+delta_*)] >= 3*delta_*/4. Since delta_* > 0 and q <= delta_*/12, q < 3*delta_*/4 <= r_-.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Because 0 <= epsilon_r <= epsilon_*^r <= 1/4 and 0 <= q <= delta_*/12 <= 1/48, one has 1+epsilon_r+q <= 61/48 < 3. Together with C_path*q <= delta_*/12 and eta = C_path*q*(1+epsilon_r+q), this gives eta <= delta_*/4; moreover delta_*/4 < 3*delta_*/4 <= r_-, so eta < r_-.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The derivative-scale definition and epsilon bound give C_der*(epsilon_r + r_iso) <= kappa_der and C_der*(r_iso + epsilon_r) <= kappa_der/4 < 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** The minimum definitions give epsilon_r <= epsilon_*^r <= kappa_der/(8*C_der) and r_iso <= kappa_der/(8*C_der). Hence C_der*(epsilon_r+r_iso) = C_der*(r_iso+epsilon_r) <= kappa_der/4.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Since 0 < kappa_der <= 1/2, one has kappa_der/4 <= kappa_der and kappa_der/4 <= 1/8 < 1. Combining these with the preceding common bound yields both derivative conclusions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The remaining product guard holds: (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta_*))*r_iso + q < 2*delta_*.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** The defining minima imply 0 <= epsilon_r <= 1/4, C_ch*(epsilon_r+delta_*) <= kappa_ch/2 <= 1/4, 0 < r_iso <= delta_*/4, and 0 <= q <= delta_*/12.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Applying those four nonnegative bounds gives (1+epsilon_r)*(1+C_ch*(epsilon_r+delta_*))*r_iso+q <= (5/4)*(5/4)*(delta_*/4)+delta_*/12 = (91/192)*delta_*. Since delta_* > 0 and 91/192 < 2, this is strictly less than 2*delta_*.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

