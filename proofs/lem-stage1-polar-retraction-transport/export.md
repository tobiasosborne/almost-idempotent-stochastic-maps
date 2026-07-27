# Proof Export

## Node 1

**Statement:** Parameterized polar-retraction transport: there exist C_pol^0 >= 1 and kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_pol >= C_pol^0 and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0 with C_pol*(epsilon_r + delta) <= kappa_pol, the map Pi_delta: calU x B^{calH}_delta(J) -> calX, Pi_delta(U, H) = U bold-dot H, is a C^1 diffeomorphism onto the open set S_delta := Pi_delta(calU x B^{calH}_delta(J)), its inverse (u_delta, h_delta): S_delta -> calU x B^{calH}_delta(J) satisfies X = u_delta(X) bold-dot h_delta(X), u_delta(U) = U, and h_delta(U) = J for every X in S_delta and U in calU, and calU_{delta - C_pol*(epsilon_r*delta + delta^2)} subseteq S_delta subseteq calU_{delta + C_pol*(epsilon_r*delta + delta^2)}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** By lem-stage1-polar-retraction, fix universal constants C_* >= 1 and kappa_* in (0, 1/2] witnessing that lemma. Define C_pol^0 := C_* and kappa_pol^0 := kappa_*; these are universal and have the ranges required at the root.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix an arbitrary def-stage1-polar-witness-data tuple W and arbitrary algebra and delta satisfying the root hypotheses. The exact unit J obeys J bold-dot J = J and ||J|| = 1; applying the product-norm axiom of def-epsilon-cstar-algebra to J,J gives 1 = ||J bold-dot J|| <= (1 + epsilon_r)||J||^2 = 1 + epsilon_r, hence epsilon_r >= 0. Thus t := epsilon_r + delta > 0 and A := epsilon_r*delta + delta^2 = delta*t >= 0. Since C_* <= C_pol and t >= 0, the assumed guard gives C_*t <= C_pol*t <= kappa_pol <= kappa_*, which is exactly the guard needed for lem-stage1-polar-retraction at (C_*, kappa_*).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Apply lem-stage1-polar-retraction with its fixed constants (C_*, kappa_*) to the arbitrary algebra and delta, using the guard from the preceding step. With S_delta taken to be the image Pi_delta(calU x B^{calH}_delta(J)), it gives that S_delta is open, Pi_delta is a C^1 diffeomorphism onto S_delta, the inverse (u_delta,h_delta) has X = u_delta(X) bold-dot h_delta(X), u_delta(U) = U, and h_delta(U) = J, and it gives the base sandwich calU_{delta - C_*A} subseteq S_delta subseteq calU_{delta + C_*A}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Because C_pol >= C_* and A >= 0, delta - C_pol*A <= delta - C_*A and delta + C_*A <= delta + C_pol*A. By def-approximate-unitary-space, if r <= s then calU_r subseteq calU_s: the right-inverse condition is unchanged and ||X^dagger bold-dot X - J|| < 2r implies the same strict inequality with 2s. Hence calU_{delta - C_pol*A} subseteq calU_{delta - C_*A} subseteq S_delta subseteq calU_{delta + C_*A} subseteq calU_{delta + C_pol*A}. Together with the unchanged open-set, diffeomorphism, and inverse conclusions from lem-stage1-polar-retraction, this proves the root statement for the arbitrary W, algebra, and delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

