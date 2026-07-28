# DESIGN v3 — explicit-binder rebuild of the Stage-1 defective set

## 0. Decision

The rebuild has eight elevations:

1. three new explicit-binder bridges;
2. clean direct re-derivations of control, 13e, 13f, and 13g; and
3. one ledger-preserving repair of 13c.

The byte-frozen anaphoric parents
`lem-stage1-approximate-group-laws` and
`lem-stage1-smooth-unitary-operations` do **not** re-elevate. They remain
honest retired conjectures. Their useful content is replaced on the live
consumer path by 13e and the new explicit smooth bridge. This avoids proving
two redundant anaphoric interfaces and makes every live definite description
come from a provider that exports the full typed witness.

The two binding laws from `docs/LEARNINGS.md` govern every proof below:

1. a theorem used to discharge a root-bound definite description must export
   that same map together with its displayed source, formula, target, and
   inverse/preimage witness; and
2. a parameterized proof first fixes provider witnesses, then enlarges or
   shrinks the receiving fields by monotonicity. No estimate may treat an
   unbounded receiving coefficient as a universal constant.

The round-1 quantitative bridges and the round-2 explicit smooth bridge survive
the sweep unchanged. The sweep does not dispute their calculations; it confirms
why their binder-closed contracts are necessary. In particular, none relies on
either retracted parent.

## 1. Exact registry package

Every block in this section is one-line registry text. `AMENDED-deps-only`
means that the displayed `contract:` and `defs:` are byte-unchanged from the
current shard and only the displayed `deps:` replaces the current line.

### 1.1 NEW — `lem-stage1-explicit-group-domain-membership`

```text
contract: Explicit group-input polar-domain membership: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the first inverse component u_delta:S_delta -> calU is defined at U bold-dot V and U^dagger for every U, V in calU; moreover, U bold-dot V and U^dagger each have a right inverse.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
```

Classification: **NEW**.

The proof is a binder-closed replay of the sound
`lem-stage1-group-domain-membership` calculation. It obtains the typed pair
`(u_delta,h_delta)` from the displayed polar retraction before treating either
input, derives the product and adjoint near-unitary estimates and their right
inverses, and uses the inner inclusion for this same `S_delta`. The sound
anaphoric child is evidence for the calculation, not an external.

### 1.2 NEW — `lem-stage1-explicit-group-closeness`

```text
contract: Explicit group-input polar closeness: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the first inverse component u_delta:S_delta -> calU satisfies ||u_delta(U bold-dot V) - U bold-dot V|| <= C_grp*epsilon_r and ||u_delta(U^dagger) - U^dagger|| <= C_grp*epsilon_r for every U, V in calU.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
```

Classification: **NEW**.

The proof is a binder-closed replay of the sound
`lem-stage1-group-closeness` calculation. For each displayed input it first
uses the typed factorization
`X = u_delta(X) bold-dot h_delta(X)` supplied by the same polar inverse,
controls `h_delta(X)-J`, and returns to the first factor. It never identifies
two opaque first components by name.

### 1.3 NEW — `lem-stage1-explicit-smooth-unitary-operations`

```text
contract: Explicit smooth action/operations bridge: for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0, suppose Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, is a C^1 diffeomorphism onto the open set S_delta with inverse (u_delta, h_delta), U bold-dot V and U^dagger lie in S_delta for every U, V in calU, the same graph charts make calU a smooth embedded manifold, and this same Pi_delta and its same set-theoretic inverse are smooth without changing any point or first derivative; then the scalar action U(1) x calU -> calU, (c, U) |-> cU, and the explicit maps mu: calU x calU -> calU, mu(U, V) = u_delta(U bold-dot V), and sigma: calU -> calU, sigma(U) = u_delta(U^dagger), are smooth as maps into the embedded manifold calU, obey mu(cU, dV) = c*d*mu(U, V) and sigma(cU) = conj(c)*sigma(U), and change no point or first derivative.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-explicit-group-domain-membership; lem-stage1-polar-retraction; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse
```

Classification: **NEW**.

This is the round-2 contract verbatim. The sweep strengthens its necessity
but exposes no defect in it. The scalar action is the restriction and
corestriction of ambient scalar multiplication. For the covariance formulas,
bilinearity gives
`Pi_delta(c*u_delta(X),h_delta(X)) = c*X`; the circle action preserves
`calU`, so ordinary injectivity of this one displayed `Pi_delta` gives
`u_delta(c*X)=c*u_delta(X)`. Apply this with
`X=U bold-dot V, c=c*d` and with `X=U^dagger, c=conj(c)`. No coherence
external and no old smooth-operations parent is used.

### 1.4 BYTE-UNCHANGED and retired — `lem-stage1-approximate-group-laws`

```text
contract: Quantitative approximate group laws: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), the inverse u_delta of the polar map defines C^1 maps mu(U, V) = u_delta(U bold-dot V), sigma(U) = u_delta(U^dagger) on all of calU, with mu(J, U) = mu(U, J) = U, sigma(J) = J, ||mu(U, V) - U bold-dot V|| <= C_grp*epsilon_r, ||sigma(U) - U^dagger|| <= C_grp*epsilon_r, ||mu(mu(U, V), W) - mu(U, mu(V, W))|| <= C_grp*epsilon_r, ||mu(sigma(U), U) - J|| <= C_grp*epsilon_r, and ||mu(U, sigma(U)) - J|| <= C_grp*epsilon_r.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-group-domain-membership; lem-stage1-group-closeness; lem-stage1-polar-retraction; lem-stage1-polar-coherence-naturality
```

Classification: **BYTE-UNCHANGED, retired in place**.

The shard remains `status: stated`, `af: seeded`; its `contract:`, `defs:`,
`deps:`, workspace, and retained ledger do not change. No live consumer after
this package depends on it. In `report/sections/47_stage1_group_laws.tex`, the
existing label remains a conjecture with its verbatim contract and retraction
note; only the explanatory campaign sentence is to say that the row is retired
and that the explicit bridges plus 13e are the sole live replacement path.
The corresponding `report/PROVENANCE.md` claim row must describe
`stated`/`seeded` and the retraction, not the obsolete validation.

This decision is cheaper and safer than re-elevating a redundant anaphoric
interface. The quantitative argument is still re-derived, but directly in
the explicit 13e root where its map is typed.

### 1.5 BYTE-UNCHANGED and retired — `lem-stage1-smooth-unitary-operations`

```text
contract: Smooth action/operations upgrade: under lem-stage1-approximate-group-laws, lem-stage1-smooth-unitary-atlas, and lem-stage1-smooth-polar-inverse, the scalar action U(1) x calU -> calU, (c, U) |-> cU, and the same maps mu: calU x calU -> calU, mu(U, V) = u_delta(U bold-dot V), and sigma: calU -> calU, sigma(U) = u_delta(U^dagger), are smooth as maps into the embedded manifold calU; they obey mu(cU, dV) = c*d*mu(U, V) and sigma(cU) = conj(c)*sigma(U), and no point or first derivative is changed.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-coherence-naturality; lem-stage1-approximate-group-laws; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse
```

Classification: **BYTE-UNCHANGED, retired in place**.

The shard remains `status: stated`, `af: seeded`; its registry fields,
workspace, and ledger do not change. No live consumer after the deps cleanups
below depends on it. Its section-49 report anchor remains a conjecture with
the retraction note and is updated only to point to
`lem-stage1-explicit-smooth-unitary-operations` as the live replacement.
Its provenance claim row is likewise corrected to the current
`stated`/`seeded` state.

### 1.6 AMENDED-deps-only — `lem-stage1-inversion-derivative-control`

```text
contract: Typed inversion derivative with chart retention: there exist universal C_der, C_ch, C_pol, C_grp >= 1 and kappa_der, kappa_ch, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra, s in {+1, -1}, and 0 < r <= delta satisfying C_ch*(epsilon_r + delta) <= kappa_ch, C_pol*(epsilon_r + delta) <= kappa_pol, C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), C_der*(epsilon_r + r) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta))*r + C_grp*epsilon_r < 2*delta, the globally defined sigma(U) = u_delta(U^dagger) maps chi_s(B_r^{icalH}(0)) into the same sJ-graph chart, where chi_s(A) = sJ bold-dot (J + A + g_{sJ}(A)), and F_s(A) = phi_{sJ}^par(sigma(chi_s(A))) satisfies ||D(F_s - id)(A) + 2*I_{icalH}|| <= C_der*(epsilon_r + r) for all A in B_r^{icalH}(0).
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-unitary-graph-control; lem-stage1-polar-retraction; lem-stage1-explicit-group-closeness
```

Classification: **AMENDED-deps-only**. Cleanly re-seed; do not resume the
defective old tree.

Choose fixed provider witnesses `(C_g,k_g)` from graph control,
`(P_r,k_r)` from polar retraction, and `(G_c,P_c,k_c)` from explicit
closeness. Set

```text
C_ch = max{1,C_g},  kappa_ch = min{1/2,k_g},
C_pol = max{1,P_r,P_c},  kappa_pol = min{1/2,k_r,k_c},
C_grp = max{1,G_c}.
```

Replay the local chart-retention and differentiated-factorization calculation
for the typed inverse exported by the last two providers and the typed graph
exported by the first. The finitely many Neumann/smallness cutoffs in that
calculation have a universal minimum `k_D`, and its finitely many derivative
coefficients have a universal maximum `D`; take
`C_der=max{1,D}` and
`kappa_der=min{1/2,k_D,1/(2*C_der)}`. This is legitimate because
`C_g,G_c,P_r,P_c` were fixed before the local calculation. The old node-1.3
substitution is absent.

### 1.7 AMENDED-deps-only — `lem-stage1-approximate-group-laws-transport` (13e)

```text
contract: Parameterized approximate-group transport: there exist C_grp^0, C_pol^0 >= 1 and kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_grp >= C_grp^0, C_pol >= C_pol^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra and every delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the formulas mu(U, V) = u_delta(U bold-dot V) and sigma(U) = u_delta(U^dagger) define C^1 maps on all of calU x calU and calU, respectively, and for every U, V, Z in calU, mu(J, U) = mu(U, J) = U, sigma(J) = J, ||mu(U, V) - U bold-dot V|| <= C_grp*epsilon_r, ||sigma(U) - U^dagger|| <= C_grp*epsilon_r, ||mu(mu(U, V), Z) - mu(U, mu(V, Z))|| <= C_grp*epsilon_r, ||mu(sigma(U), U) - J|| <= C_grp*epsilon_r, and ||mu(U, sigma(U)) - J|| <= C_grp*epsilon_r.
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-explicit-group-domain-membership; lem-stage1-explicit-group-closeness; lem-stage1-polar-retraction
```

Classification: **AMENDED-deps-only**. Cleanly re-seed the workspace; the
old 37-node paused tree is not a repair base.

Fix witnesses `(G_d,P_d,k_d)`, `(G_c,P_c,k_c)`, and `(P_r,k_r)` from the
three providers before quantifying over the receiving tuple, and take

```text
C_grp^0 = max{G_d,8*G_c,8},
C_pol^0 = max{P_d,P_c,P_r},
kappa_pol^0 = min{k_d,k_c,k_r,1/16}.
```

The receiving guards imply all three fixed provider guards. All providers
display the identical `Pi_delta`, source, image-defined target, and inverse
pair, so ordinary inverse uniqueness synchronizes them. The retraction gives
`C^1` regularity and exact basepoints; the bridges give membership and
closeness for that inverse. The associator and two inverse-defect telescopes
are replayed directly, with the constants absorbed by
`C_grp^0 >= max{8*G_c,8}`. Coherence-naturality is neither needed nor listed.

### 1.8 BYTE-UNCHANGED — `lem-stage1-maurer-cartan-transport` (13c)

```text
contract: Parameterized Maurer-Cartan transport: there exist C_ch^0 >= 1 and kappa_ch^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_ch >= C_ch^0 and 0 < kappa_ch <= kappa_ch^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_ch*(epsilon_r + delta) <= kappa_ch, and every family g = (g_U)_{U in calU} of C^1 maps g_U: B^{icalH}_{2delta}(0) -> B^{calH}_{2delta}(0) such that, for every U in calU and A^par in B^{icalH}_{2delta}(0), g_U(A^par) is the unique element of B^{calH}_{2delta}(0) satisfying f_U(A^par + g_U(A^par)) = 0, where f_U(A) = (1/2)*(((J + A^dagger) bold-dot U^dagger) bold-dot (U bold-dot (J + A)) - J), every tangent space T_U calU is the image of L_U(I + Dg_U(0)): icalH -> calX, and omega_U(Z) = (L_U^{-1} Z)^par : T_U calU -> icalH is a global C^1 bundle trivialization with distortion at most 1 + C_ch*epsilon_r, satisfying omega_{cU}(cZ) = omega_U(Z) and omega_U(iU) = iJ for every U in calU, Z in T_U calU, and c in U(1).
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-maurer-cartan-trivialization
```

Classification: **BYTE-UNCHANGED; retained-workspace repair**.

Do not re-seed. A fresh repair verifier first revokes the current validation
of the defective node, after which the orchestrator archives only that node:

```text
af unvalidate 1.3.3 -d proofs/lem-stage1-maurer-cartan-transport --reason "Binder sweep: node 1.3.3 used an unavailable unconditional g=gbar identification." --agent w97-13c-repair-verifier -y
af archive 1.3.3 -d proofs/lem-stage1-maurer-cartan-transport --reason "Binder sweep: invalid unconditional g=gbar derivative transfer; nodes 1.3.4-1.3.7 are the typed-family bypass." -y
```

The same fresh hostile verifier then revokes the old validations on nodes
`1`, `1.3`, `1.3.7`, `1.3.6`, `1.3.5`, and `1.3.4` (dependent before
prerequisite), inspects the resulting taint queue, and re-verifies bottom-up
in the exact order

```text
for node in 1 1.3 1.3.7 1.3.6 1.3.5 1.3.4; do af unvalidate "$node" -d proofs/lem-stage1-maurer-cartan-transport --reason "Binder sweep: require fresh verification of the typed-family bypass closure." --agent w97-13c-repair-verifier -y; done
1.3.4 -> 1.3.5 -> 1.3.6 -> 1.3.7 -> 1.3 -> 1
```

using only the registered external
`lem-stage1-maurer-cartan-trivialization`. Nodes 1.3.4–1.3.7 derive the
tangent image for the arbitrary root-bound family directly from its own zero
equation, right-invertibility, intrinsic tangent dimension, and the external
bundle trivialization. Nodes 1.3.2 and 1.3.2.1 may remain as a correctly
conditional, unused side branch; node 1.3.3 is absent from the live export.
The old export is regenerated only after the fresh verifier has accepted the
new live closure.

### 1.9 AMENDED-deps-only — `lem-stage1-polar-path-transport` (13f)

```text
contract: Parameterized polar-path transport: there exist C_path^0, C_pol^0 >= 1 and kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_path >= C_path^0, C_pol >= C_pol^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_pol*(epsilon_r + delta) <= kappa_pol, every U_0, U_1 in calU, and every q in [0, 1] satisfying ||U_1 - U_0|| <= q, C_path*q <= 1/4, and C_path*(q + epsilon_r*q + q^2) < delta - C_pol*(epsilon_r*delta + delta^2), every L_{Z_t} is invertible and every Z_t = (1-t)*U_0 + t*U_1 lies in calUbar_{C_path*(q + epsilon_r*q + q^2)} for t in [0, 1], and, writing u_delta for the unique first component of the inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the map H(t, U_0, U_1) = u_delta(Z_t) is jointly continuous in (t, U_0, U_1), joins U_0 to U_1, and satisfies H(t, cU_0, cU_1) = c*H(t, U_0, U_1) for every c in U(1).
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-path-admissibility; lem-stage1-polar-retraction-transport
```

Classification: **AMENDED-deps-only**. Cleanly re-seed rather than resume the
defective 9-node tree.

Fix parent path witnesses `(A,B,k)` and the sound 13d witnesses `(P,q_pol)`,
then take

```text
C_path^0 = A,
C_pol^0 = max{B,P},
kappa_pol^0 = min{k,q_pol}.
```

Use the sound parent only for its binder-free conclusions:
`L_{Z_t}` is invertible and
`Z_t in calUbar_{A*(q+epsilon_r*q+q^2)}`. Monotonicity enlarges this to the
receiving `C_path`. The strict receiving path guard places every `Z_t` inside
the inner near-unitary radius, and the sound 13d external supplies the typed
inverse of the **same displayed** `Pi_delta` at the receiving tuple. Thus
`Z_t in S_delta` without using the parent's anaphoric path formula.
Continuity follows from the 13d `C^1` inverse and the affine path; endpoints
follow from `u_delta(U)=U`. Finally,
`Pi_delta(c*u_delta(Z_t),h_delta(Z_t))=c*Z_t` and ordinary uniqueness for
this one inverse give scalar equivariance. No coherence external is needed.

### 1.10 AMENDED-deps-only — `lem-stage1-inversion-derivative-transport` (13g)

```text
contract: Parameterized inversion-derivative transport: there exist C_der^0, C_ch^0, C_pol^0, C_grp^0 >= 1 and kappa_der^0, kappa_ch^0, kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_der >= C_der^0, C_ch >= C_ch^0, C_pol >= C_pol^0, C_grp >= C_grp^0, 0 < kappa_der <= kappa_der^0, 0 < kappa_ch <= kappa_ch^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0, every s in {+1, -1}, and every 0 < r <= delta satisfying C_ch*(epsilon_r + delta) <= kappa_ch, C_pol*(epsilon_r + delta) <= kappa_pol, C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), C_der*(epsilon_r + r) <= kappa_der, and (1 + epsilon_r)*(1 + C_ch*(epsilon_r + delta))*r + C_grp*epsilon_r < 2*delta, writing u_delta for the unique first component of the inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, and g_{sJ}: B_{2delta}^{icalH}(0) -> B_{2delta}^{calH}(0) for the unique C^1 map such that, for every A in B_{2delta}^{icalH}(0), f_{sJ}(A + g_{sJ}(A)) = 0, where f_{sJ}(B) = (1/2)*(((J + B^dagger) bold-dot (sJ)^dagger) bold-dot (sJ bold-dot (J + B)) - J), define chi_s(A) = sJ bold-dot (J + A + g_{sJ}(A)) and the global C^1 map sigma(U) = u_delta(U^dagger); then sigma maps chi_s(B_r^{icalH}(0)) into the same sJ-graph chart and, with F_s(A) = phi_{sJ}^par(sigma(chi_s(A))), one has ||D(F_s - id)(A) + 2*I_{icalH}|| <= C_der*(epsilon_r + r) for every A in B_r^{icalH}(0).
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-explicit-group-domain-membership; lem-stage1-explicit-group-closeness; lem-stage1-polar-retraction; lem-stage1-unitary-graph-control
```

Classification: **AMENDED-deps-only**. Cleanly re-seed; neither the defective
run-2 tree nor the archived run-1 branch is a proof base.

This chooses audit-v2's **fixed explicit-closeness witness** repair, not the
old receiving-coefficient argument. Fix provider witnesses

```text
(G_d,P_d,k_d)  from explicit domain membership,
(G_c,P_c,k_c)  from explicit closeness,
(P_r,k_r)      from polar retraction,
(C_g,k_g)      from unitary graph control.
```

Define the base thresholds

```text
C_ch^0 = max{1,C_g},
C_pol^0 = max{1,P_d,P_c,P_r},
C_grp^0 = max{1,G_d,G_c},
kappa_ch^0 = min{1/2,k_g},
kappa_pol^0 = min{1/2,k_d,k_c,k_r}.
```

For a receiving tuple, its guards imply the fixed provider guards. In
particular,

```text
G_c*epsilon_r <= C_grp*epsilon_r
  < delta - C_pol*(epsilon_r*delta + delta^2)
  <= delta - P_c*(epsilon_r*delta + delta^2),
```

and similarly for `G_d`. Its chart-retention inequality also implies the
fixed-coefficient inequality

```text
(1+epsilon_r)*(1+C_g*(epsilon_r+delta))*r + G_c*epsilon_r < 2*delta.
```

Now replay the control calculation directly for the root-bound typed
`(u_delta,h_delta)` and root-bound typed `g_{sJ}`. Let
`d_1,...,d_m` be the finite universal coefficients in the resulting normal,
inverse, product, and differentiated-factorization bounds after the already
fixed numbers `G_c` and `C_g` are substituted, and let
`b_1,...,b_n` be the finite positive Neumann/smallness cutoffs used there.
Set

```text
D_0 = max{1,d_1,...,d_m},
k_D = min{1/2,b_1,...,b_n,1/(2*D_0)},
C_der^0 = D_0,
kappa_der^0 = k_D.
```

These are universal because every coefficient on which they depend was
fixed before the receiving tuple was introduced. The receiving
`C_der >= C_der^0` and
`C_der*(epsilon_r+r) <= kappa_der <= kappa_der^0` then give both the local
smallness hypotheses and
`D_0*(epsilon_r+r) <= C_der*(epsilon_r+r)`. This is the required derivative
estimate. No step absorbs the unbounded receiving `C_grp`; it appears only
through monotonicity. Neither 13e, the anaphoric control result, nor either
old parent is an external.

### 1.11 AMENDED-deps-only — rows 14+

For `lem-stage1-uniform-inversion-isolation`:

```text
contract: There are universal e_iso^r > 0, r_iso > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_iso^r, J and -J are the only fixed points of the smooth sigma in their respective ambient r_iso-balls.
defs: def-epsilon-cstar-algebra; def-approximate-unitary-space
deps: lem-stage1-quantitative-inverse-function; lem-stage1-explicit-smooth-unitary-operations; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse; lem-stage1-polar-constant-ledger
```

Classification: **AMENDED-deps-only**. Row 13 `(A_7)` supplies the derivative
estimate for the explicit `sigma`; the new smooth bridge supplies its
regularity.

For `lem-stage1-quotient-manifold-package`:

```text
contract: There is a universal e_quot^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_quot^r and 1 < N = dim_C calX < infinity, breve-calU = calU_e/U(1) is a connected compact orientable smooth manifold without boundary of real dimension N - 1.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-maurer-cartan-trivialization; lem-stage1-smooth-unitary-atlas; lem-stage1-polar-constant-ledger; lem-topology-quotient-manifold
```

Classification: **AMENDED-deps-only**.

Choose the local scalar-action proof. Scalar multiplication is smooth in the
ambient finite-dimensional space, preserves `calU` by the exact unitary
equations and an explicit right inverse, and therefore restricts/corestricts
smoothly through the sound embedded atlas. This proof is binder-free and
does not need a polar inverse. Depending on the new smooth bridge here would
unnecessarily couple the quotient-manifold construction to a chosen
`delta` and its polar antecedents.

For `lem-stage1-quotient-left-inversion`:

```text
contract: There is a universal e_H^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_H^r, the scalar-equivariant mu, sigma and the jointly continuous projected straight paths descend to breve-calU; the descended multiplication makes it a connected H-space, and the descended smooth map breve-sigma is a left inversion.
defs: def-approximate-unitary-space; def-h-space-left-inversion; def-epsilon-cstar-algebra
deps: lem-stage1-explicit-smooth-unitary-operations; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse; lem-stage1-polar-constant-ledger; lem-stage1-quotient-manifold-package
```

Classification: **AMENDED-deps-only**. Row 13 `(A_5)` and `(A_6)` provide
the explicit group operations and paths; the new bridge provides smoothness
and covariance for those same maps.

For `lem-stage1-quotient-inversion-index-data`:

```text
contract: There is a universal e_idx^r > 0 such that, for every finite-dimensional exact-unit epsilon_r-C*-algebra with 0 <= epsilon_r <= e_idx^r and 1 < N = dim_C calX < infinity, the scalar class breve-e = [J] is an isolated fixed point of the smooth breve-sigma, the vertical line iR*J is D-sigma_J-invariant, ||D-breve-sigma_{breve-e} + I|| < 1 in the quotient norm, and det(I - D-breve-sigma_{breve-e}) > 0, so its local index is +1; more precisely, there is a quotient neighborhood calN of [J] such that if [U] in calN is fixed, choose a representative U_0 close to J and c in U(1) with sigma(U_0) = c*U_0, choose a in U(1) with a^2 = c, and use sigma(a*U_0) = conj(a)*sigma(U_0) = a*U_0: the two actual fixed lifts +-a*U_0 lie in the J- and -J-isolation balls, hence equal J and -J, so [U] = [J].
defs: def-approximate-unitary-space; def-lefschetz-fixed-point-data; def-epsilon-cstar-algebra
deps: lem-stage1-uniform-inversion-isolation; lem-stage1-explicit-smooth-unitary-operations; lem-stage1-smooth-unitary-atlas; lem-stage1-smooth-polar-inverse; lem-stage1-polar-constant-ledger; lem-stage1-quotient-manifold-package; lem-stage1-quotient-left-inversion; lem-topology-local-index-sign
```

Classification: **AMENDED-deps-only**. Row 13 `(A_7)` supplies the explicit
derivative data, and the new smooth bridge supplies phase covariance and the
vertical derivative. The anaphoric control, old smooth parent, and coherence
dependencies are removed.

`lem-stage1-quotient-finite-cw` is **BYTE-UNCHANGED**:

```text
contract: For every finite-dimensional exact-unit epsilon_r-C*-algebra, if breve-calU = calU_e/U(1) is a compact smooth manifold without boundary, then breve-calU is homeomorphic to a finite simplicial complex and hence has finite CW type.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-quotient-manifold-package; lem-topology-finite-triangulation
```

### 1.12 Complete classification

| shard | classification | landing action |
|---|---|---|
| `lem-stage1-explicit-group-domain-membership` | **NEW** | Land verbatim as `stated`/`af: none`, then seed. |
| `lem-stage1-explicit-group-closeness` | **NEW** | Land verbatim as `stated`/`af: none`, then seed. |
| `lem-stage1-explicit-smooth-unitary-operations` | **NEW** | Land verbatim as `stated`/`af: none`, then seed. |
| `lem-stage1-approximate-group-laws` | **BYTE-UNCHANGED** | Leave `stated`/`seeded`, deps and workspace unchanged; retain conjecture anchor. |
| `lem-stage1-smooth-unitary-operations` | **BYTE-UNCHANGED** | Leave `stated`/`seeded`, deps and workspace unchanged; retain conjecture anchor. |
| `lem-stage1-inversion-derivative-control` | **AMENDED-deps-only** | Replace deps and cleanly re-seed. |
| `lem-stage1-approximate-group-laws-transport` | **AMENDED-deps-only** | Replace deps and cleanly re-seed. |
| `lem-stage1-maurer-cartan-transport` | **BYTE-UNCHANGED** | Retain workspace; archive 1.3.3 and freshly verify the bypass closure. |
| `lem-stage1-polar-path-transport` | **AMENDED-deps-only** | Replace deps and cleanly re-seed. |
| `lem-stage1-inversion-derivative-transport` | **AMENDED-deps-only** | Replace deps and cleanly re-seed. |
| `lem-stage1-uniform-inversion-isolation` | **AMENDED-deps-only** | Replace deps only. |
| `lem-stage1-quotient-manifold-package` | **AMENDED-deps-only** | Replace deps only; prove scalar action locally. |
| `lem-stage1-quotient-left-inversion` | **AMENDED-deps-only** | Replace deps only. |
| `lem-stage1-quotient-inversion-index-data` | **AMENDED-deps-only** | Replace deps only. |
| `lem-stage1-quotient-finite-cw` | **BYTE-UNCHANGED** | No action. |
| fourteen sweep-certified Stage-1 providers, row 13, and the witness definition | **BYTE-UNCHANGED** | Preserve every contract, dependency, field type, workspace, and certificate. |

## 2. Strict elevation order and exact externals

The order is serial. A target is not seeded or repaired until the preceding
target is validated and banked. A hard-cap hit is a factoring stop, never
permission to enlarge the cap.

| order | workspace | target / hard live-node cap | exact external registration list |
|---:|---|---:|---|
| 1 | `proofs/lem-stage1-explicit-group-domain-membership/` | 10 / 14 | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-polar-retraction`. |
| 2 | `proofs/lem-stage1-explicit-group-closeness/` | 12 / 16 | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-polar-retraction`. |
| 3 | `proofs/lem-stage1-explicit-smooth-unitary-operations/` | 12 / 18 | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-explicit-group-domain-membership`; `lem-stage1-polar-retraction`; `lem-stage1-smooth-unitary-atlas`; `lem-stage1-smooth-polar-inverse`. |
| 4 | `proofs/lem-stage1-inversion-derivative-control/` | 10 / 14 | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-unitary-graph-control`; `lem-stage1-polar-retraction`; `lem-stage1-explicit-group-closeness`. |
| 5 | `proofs/lem-stage1-approximate-group-laws-transport/` | 16 / 22 | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-explicit-group-domain-membership`; `lem-stage1-explicit-group-closeness`; `lem-stage1-polar-retraction`. |
| 6 | `proofs/lem-stage1-maurer-cartan-transport/` | 12 / 12 | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-maurer-cartan-trivialization`. |
| 7 | `proofs/lem-stage1-polar-path-transport/` | 10 / 14 | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-polar-path-admissibility`; `lem-stage1-polar-retraction-transport`. |
| 8 | `proofs/lem-stage1-inversion-derivative-transport/` | 22 / 25 | `def-stage1-polar-witness-data`; `def-approximate-unitary-space`; `def-epsilon-cstar-algebra`; `lem-stage1-explicit-group-domain-membership`; `lem-stage1-explicit-group-closeness`; `lem-stage1-polar-retraction`; `lem-stage1-unitary-graph-control`. |

The type discipline is checkable row by row:

- every root-bound polar inverse is either supplied by the exact displayed
  retraction external or introduced by the root and used directly;
- every root-bound graph is supplied by the external whose contract displays
  its equation, ball, codomain, and uniqueness;
- 13c does not identify its arbitrary family with the external distinguished
  family;
- 13f ignores the anaphoric path component of its parent and obtains the typed
  inverse from 13d; and
- 13e and 13g fix their provider witnesses before introducing a receiving
  tuple.

## 3. Consumer re-check

`lem-stage1-polar-constant-ledger` is **BYTE-UNCHANGED**. Its dependency line
still names transports 13a–13g and scalar arithmetic. The repaired transport
contracts are byte-identical to the clauses they feed:

- 13e is `(A_5)` verbatim;
- 13f is `(A_6)` verbatim; and
- 13g is `(A_7)` verbatim.

The linker must perform the usual byte comparison before row 13 elevates.
No bridge becomes a new row-13 field and no field changes type.
`def-stage1-polar-witness-data` therefore remains exactly the same fourteen
scalars

```text
(C_rect, C_ch, C_pol, C_grp, C_path, C_der,
 e_rect, kappa_ch, kappa_pol, kappa_der,
 delta_*, epsilon_*^r, e_S1, r_iso).
```

The extra letters used in the proofs are fixed local witnesses used to define
the existing base constants; they are not additional tuple data.

After the deps-only cleanups:

- uniform isolation reads derivative information from row 13 `(A_7)` and
  smoothness from the explicit bridge;
- quotient manifold uses a local binder-free scalar-action proof;
- quotient left inversion reads operations and paths from `(A_5)`–`(A_6)`
  and covariance/smoothness from the explicit bridge;
- quotient inversion-index data reads the derivative from `(A_7)` and phase
  covariance from the explicit bridge; and
- finite-CW is unchanged.

Thus neither retired parent nor the repaired anaphoric control theorem is an
opaque map provider for rows 14+.

## 4. Cost and stop accounting

| item | count |
|---|---:|
| Design jobs | **1 spent**: this document. |
| Hostile design-audit jobs | **1 fresh** audit before landing. |
| Fresh prover builds | **7**: three bridges, control, 13e, 13f, and 13g. |
| Ledger-preserving proof repairs | **1**: 13c archive plus fresh bypass verification; no prover rebuild. |
| Fresh hostile verifier cohorts | **8**, one strictly after each target/repair. |
| Campaign-level codex jobs before challenged repair rounds | **17** = 1 design + 1 audit + 7 provers + 8 verifier cohorts. |
| Hard live-node ceiling across the eight targets | **135** = 14 + 16 + 18 + 14 + 22 + 12 + 14 + 25. |
| Target live-node total | **104** = 10 + 12 + 12 + 10 + 16 + 12 + 10 + 22. |
| Registry shards touched at landing | **11** = 3 NEW + 8 deps-only amendments. |
| Workspaces created or cleanly re-seeded | **7**. |
| Existing workspace repaired in place | **1** (13c). |
| Elevations | **8**: 3 new bridges, first 13e validation, and re-elevations of control, 13c, 13f, 13g. |
| Retracted parents intentionally left retired | **2**: group laws and smooth operations. |
| Sweep-certified sound certificates disturbed | **0**. |

Any verifier finding that requires a contract change, a new witness-tuple
field, use of an untyped same-named map, or a coefficient depending on the
receiving tuple stops the campaign and returns to design. It is not a local
proof repair.
