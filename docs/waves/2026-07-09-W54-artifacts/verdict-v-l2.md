VERDICT: VALID-WITH-CORRECTIONS — The proved core survives, but the answer must correct a contract overreach, a false "never a majority" consequence, and several boundary/constant statements.

1. Theorem A, hypothesis collapse: essentially valid, with one contract-use correction required.

   Checked contracts and statuses. The proof inputs used here are all `status: proved`: `lem-positive-exposedness-margin`, `lem-hiddenness-dual-witness`, `lem-top-deficit-price`, `lem-averaged-deficit-charge`, `lem-mass-split`, `lem-top-support-dual-face`, and `lem-optimal-face-conic-reduction`.

   Relevant contract lines:

   `lem-positive-exposedness-margin`: "contract: Positive exposedness margin: for an exact signed idempotent P with rho = 4*tau > 0 (i.e. delta(P) > 0) and a geometrically distinct row vertex v with nonempty far set F_v = {j : ||p_j - p_v||_1 >= rho}: t*(v) > 0; in particular every HIDDEN geometrically distinct row vertex with F_v nonempty has 0 < t*(v) < kappa (hiddenness forces delta(P) > 0, hence rho > 0, and no row vertex is hidden at delta = 0)."

   `lem-top-deficit-price`: "contract: Top-deficit price: for an exact signed idempotent P with delta(P) > 0 and nonempty visible set W(P), a hidden top vertex v of height H, there exists a top support functional phi (affine, phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1), and for ANY such phi, writing a_j = P_vj and z_j = H - phi(p_j) >= 0: for every subset A of row indices, sum over j in A of max(a_j,0)*z_j <= nu_v*(2+4*delta) <= delta*(2+4*delta); consequently for m >= 0, L >= 0, if sum over A of max(a_j,0) >= m and z_j >= L on A then m*L <= delta*(2+4*delta), and for delta <= 1/4, lambda > 0, theta < 1, positive v-row mass >= 1-theta on rows with z_j >= lambda*H forces H <= 3*delta/(lambda*(1-theta)), hence H <= 4*tau whenever delta <= min(1/4, (4*lambda*(1-theta)/3)^2)."

   `lem-averaged-deficit-charge`: "contract: Averaged deficit charge: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), a hidden top vertex v of height H, any c_m > 0, and any phi that is a top support functional at v (affine, phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1) or a finite convex average of top support functionals at v: if sum over {j : H - phi(p_j) >= tau} of max(P_vj, 0) >= c_m then c_m*tau <= delta*(2+4*delta); in particular no such configuration exists for 0 < delta < min(1/4, (c_m/3)^2)."

   The arithmetic is correct: with A = {z_j >= tau}, `tau * sum_A a_j^+ <= delta*(2+4*delta) <= 3*delta`, hence `sum_A a_j^+ <= 3*tau`; `tau < c_m/12` gives clause (4) at threshold `c_m/4` and clause (3) at threshold `c_m`.

   Required correction: in §2.1 A1 clause (4), the prover writes that `lem-averaged-deficit-charge` licenses the statement that "a finite convex average of top support functionals at v is again one". That sentence is stronger than the contract quoted above. The contract gives the charge bound for finite convex averages; it does not assert identity as a top support functional. The proof can be fixed by either invoking `lem-averaged-deficit-charge` directly with threshold `c_m/4`, or by first using the §2.2 convexity argument / `lem-top-support-dual-face` to identify the average with a member of `Phi_v` on rows before applying `lem-top-deficit-price`.

   A2's equivalence with L2-core is valid after that correction. The `t*(v)>0` hypothesis needed by `lem-optimal-face-conic-reduction` is supplied by the positive-exposedness contract, and hiddenness gives `t*(v)<kappa`.

2. A3, averaging collapse: valid, but cite the right source.

   Relevant contract:

   `lem-top-support-dual-face`: "contract: Top-support dual face: for an exact signed idempotent P with delta(P) > 0, nonempty visible set W(P), and hidden top vertex v of height H, writing Phi_v = {phi affine, phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1}, h_C(y) = sup{y.c : c in conv{p_w : w in W}}, and Y_v = {y : ||y||_inf <= 1, y.p_v - h_C(y) = H}: Y_v is nonempty, on the row set Phi_v is exactly {phi_y(x) = y.x - h_C(y) : y in Y_v}, and for every row f the top-deficit supremum Z_v(f) := sup over phi in Phi_v of (H - phi(p_f)) equals sup over y in Y_v of y.(p_v - p_f) and is finite; hence for every eps > 0 exactly one of Z_v(f) >= eps (visible horn, owning equality) or p_f in Cyl_v(eps) := {x : sup over y in Y_v of y.(p_v - x) < eps} (summit-cylinder horn) holds."

   The convexity proof that a finite convex average of top support functionals is represented by `ybar in Y_v` checks out: the l-infinity ball is convex, `h_C` is convex, and the reverse inequality follows from the definition of `H` as `dist_1(p_v,C_W)`. This is dimension-free and clone-invariant. The conclusion should be attributed to `lem-top-support-dual-face` plus convexity, not to an uncontracted body note of `lem-averaged-deficit-charge`.

3. Theorem B, confinement package: valid.

   Relevant contracts:

   `lem-optimal-face-conic-reduction`: "contract: Optimal-face conic reduction: for the exposedness LP at a hidden geometrically distinct row vertex u of an exact signed idempotent P with t*(u) > 0, the reduced optimal hiddenness dual witnesses are exactly the displays sum over f in T of lambda_f*(p_f - p_u) + sum over z in Z of a_z*(p_z - p_u) = t*(u) * sum over i in O of gamma_i*(p_i - p_u), with lambda and gamma probability vectors supported on T and O and coefficients a_z >= 0 supported on Z (T, O, Z the always-tight families); a display with all a_z = 0 exists if and only if conv{p_f - p_u : f in T} intersects t*(u)*conv{p_i - p_u : i in O}."

   `lem-always-tight-dual-support`: "contract: Always-tight dual support: for the exposedness LP at a hidden geometrically distinct row vertex u of an exact signed idempotent P with delta(P) > 0 and nonempty visible set, every optimal hiddenness dual witness (lambda, alpha, beta), after deleting redundant centered-zero constraints, has supp(lambda) contained in T, supp(beta) contained in O, and supp(alpha) contained in Z, where T, O, Z are the rho-far, upper-box, and lower-box constraint families tight on the WHOLE primal optimal face; T is nonempty, and O is nonempty if and only if t*(u) > 0."

   `lem-hiddenness-depth-markov`: "contract: Hiddenness depth-Markov: for an exact signed idempotent P with delta(P) > 0, nonempty visible set W(P), hidden top vertex v of height H, and any hiddenness dual witness (lambda, alpha, beta) of v with sum_i beta_i < kappa = tau/4 (tau = sqrt(delta)), one has for every c > 0: lambda{f in F_v : dist_1(p_f, conv{p_w : w in W}) > H - c*tau} > 1 - (1/2 + delta)/c."

   The display gives `b-p_v = t*(q-p_v)`. Since all row distances are at most `D=2+4*delta`, `||b-p_v||_1 <= t*D < kappa D = (1/2+delta)tau`. The exposer identity follows by applying the linear part of an affine admissible exposer with `h(p_v)=0`. B4 and B5 are ordinary Markov applications to nonnegative deficits. B6's l1/l-infinity duality argument is sound; the possible sign of `u.(b-p_v)` is harmless because the needed contradiction is only that the average cannot be strictly bigger than `t*D`.

   Minor wording correction: "L2-core configuration" should be read as "putative L2-core counterexample/intersection configuration." L2-core itself is a nonexistence statement.

4. Proposition D, dead-end identity: identity valid; one stated consequence is false as written.

   The cap `sum_f lambda_f z_f(y) = y.(p_v-b) <= t*D` is airtight and uses only Theorem B plus `||y||_inf <= 1`. The extension to finite convex averages is valid via A3.

   Required correction: D1 says the lambda-mass at deficit `>= tau` is "never a majority". B4 only proves
   `lambda{z_f(y) >= tau} < 1/2 + delta`.
   For any positive `delta`, this upper bound can exceed `1/2`; it does not rule out a strict majority. The correct statement is: "never reaches the contradiction threshold `1/2 + delta` supplied by this cap; it may still be slightly above one half." The rest of D1, namely that the witness-measure averaging route cannot force a contradiction at threshold `1/2+delta`, survives.

   D2 is acceptable only in its stated restricted sense, "through the lambda-pairing." Convexity of `Cyl_v(eps)` and `B2` show that pointwise cylinder exclusion does not average into a one-functional lambda contradiction. This does not rule out all possible uses of `conj-summit-cylinder-exclusion`, and the text should not be read more broadly.

5. Theorem C, conditional narrow-face closer: valid as a conditional implication; tighten the epsilon wording.

   The shard `conj-summit-cylinder-exclusion` has `status: conjecture`, so it would be illegal as an unconditional input. Here it is explicitly the hypothesis of Theorem C, so this is not a status violation.

   Relevant contract:

   `conj-summit-cylinder-exclusion`: "contract: (CONJECTURE) Summit-cylinder exclusion: there exist universal c_3 > 0 and delta_0 > 0 such that for every exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set W(P), hidden top vertex v of height H > 16*tau, and every row f with ||p_f - p_v||_1 >= 4*tau and dist_1(p_f, conv{p_w : w in W}) > H - 8*tau: p_f is not in Cyl_v(c_3*tau), where Cyl_v(eps) = {x : sup over y in Y_v of y.(p_v - x) < eps} and Y_v is the dual face of lem-top-support-dual-face; equivalently Z_v(f) >= c_3*tau."

   The composition is correct. B5 gives `lambda(L)>13/16`; all rows in `L` satisfy the conjecture's far/deep hypotheses. If `Z_v(f)>=c_3 tau`, then for fixed `y_0` and approximating maximizers `y_f`,
   `z_f(y_0) >= (c_3 - omega_v - eps)tau`. Combining with B4 gives the claimed contradiction under `omega_v <= c_3 - (16/13)(1/2+delta)`.

   Required correction: the proof's phrase "run the argument with c_3 - eps and let eps -> 0" is too terse at the equality boundary. The clean version is: because `lambda(L)>13/16` strictly and `t*D < (1/2+delta)tau` strictly, choose `eps>0` small enough that `lambda(L)(c_3-omega_v-eps) > 1/2+delta` whenever `c_3-omega_v >= (16/13)(1/2+delta)`. This preserves the stated closed narrowness condition.

6. SL1 / SL1a / SL1b sub-assembly: reduction valid, with two wording fixes.

   SL1 implies L2-core by B1, B2, B3, and B5; the lambda produced by an alpha-free display satisfies all four SL1 clauses. The split proof is exhaustive: either the shallow mass `mu` is `<= tau/D`, yielding the conditioned co-top object forbidden by SL1a, or `mu > tau/D`, yielding the shallow sub-probability forbidden by SL1b.

   Required correction 1: distinguish the sharper display bound from the bare SL1 bound. In an actual L2-core display, B5 gives `mu < (1/2+delta)/4 = 1/8+delta/4`. For an arbitrary SL1 object, clause (c) only gives `mu < 3/16`. The §2.7 proof correctly uses `3/16` for bare SL1, but the summary statement should not suggest that the sharper B5 value is available for every SL1 object.

   Required correction 2: in Case (i), if `mu=0`, the conditional barycenter `b_S` is undefined. The proof should split off `mu=0` or declare the term `mu beta_S` to be zero with an arbitrary choice of `beta_S`. The estimate is then unchanged.

7. Proposition E, cap-consistency of the shallow counterweight: useful and not an exact counterexample; correct two constants/phrases.

   The construction is explicitly not an exact signed idempotent, so it cannot refute SL1b or L2-v2. As a cap-consistency check it is legitimate: with
   `m = 4*tau/(D+4*tau)`, the counterweight distance is exactly `D`, the barycenter can be at `p_v`, and the B5 budget permits a fully shallow counterweight when
   `H <= ((1/2+delta)tau)/m = (1/2+delta)(D+4*tau)/4 = D(D+4*tau)/16`, which tends to `1/4` as `delta -> 0`.

   Required correction 1: the "third-actor mass" line leaves the condition unfinished. The exact condition for `1-m > 13/16` is
   `4*tau/(D+4*tau) < 3/16`, equivalently `tau < 3D/52`.

   Required correction 2: "saturating the depth-deficit budget exactly" is only true at equality in the displayed `H` bound. For smaller `H`, the constructed cap system has slack.

8. Status audit: no illegal unconditional non-proved inputs found.

   Direct unconditional proof inputs checked: `lem-top-deficit-price`, `lem-averaged-deficit-charge`, `lem-top-support-dual-face`, `lem-optimal-face-conic-reduction`, `lem-always-tight-dual-support`, `lem-positive-exposedness-margin`, `lem-hiddenness-dual-witness`, `lem-hiddenness-depth-markov`, `lem-top-witness-third-actor`, `lem-mass-split`, and `lem-harmonic-affine-bridge` are all `status: proved`. The auxiliary dependency `lem-optimal-face-alpha-free-characterization` is also `status: proved`.

   Non-proved shards named in the answer are not used as unconditional premises. `conj-summit-cylinder-exclusion` is conditional in Theorem C; the remaining named shards in §3 are explicitly listed as not used.

9. Degenerate cases, dimension, and clones.

   No counterexample found from the required edge cases. `W=empty` is excluded everywhere height/dual face is used. `H=16*tau` is excluded by the strict tallness hypothesis. `t*(v)=0` is excluded by `lem-positive-exposedness-margin` for hidden top vertices with nonempty far set; hiddenness also rules out the empty-far-set `t*=+infinity` convention. Cloning rows does not change the geometric vertex set, exposedness LP, or the mass-sum inequalities; the arguments use row points, convex combinations, and coefficient masses rather than raw row counts. All constants are functions only of `delta`, `tau`, `rho`, `kappa`, and the universal thresholds, so no dimension dependence appears.

10. Bottom line.

   The collapse L2-v2 <=> L2-core at `delta < (c_m/12)^2`, Theorem B's confinement package, Theorem C's conditional narrow-face closer, and the SL1a/SL1b reduction survive hostile checking. The answer is not literally valid as written because of the contract overreach in A1 clause (4), the false "never a majority" phrase in D1, and the smaller boundary/constant issues listed above. After those precise corrections, the proved content is valid; SL1a and SL1b remain genuine open leaves, not verified theorems.
