VERDICT: INVALID — the assembly does not currently derive the pinned target from L1-L7 because the root object hand-off to the mass-carrying leaf hypotheses is unproved, Q3 is not strong enough for the cited L1 charge, and the charge thresholds mishandle the closed delta boundary.

1. Step A0/A1 root object: the final route "take u := v when t*(v) > 0" does not establish the leaf antecedent "mass-carrying deepest cluster vertex".

   What I checked: DECOMPOSITION first defines the root u by positive disintegrated C(v)-mass:

   > "among all geometrically distinct row vertices carrying positive conic weight in some fixed vertex representation of the C(v)-mass (lem-genuine-disintegration supplies one), let u be a DEEPEST mass-carrying cluster vertex with t*(u) > 0"

   and immediately defines:

   > `"mass-carrying" = u receives positive disintegrated weight from C(v)-rows`

   L2 and L6 then require the same object:

   > "a mass-carrying deepest cluster vertex u with intersecting always-tight hulls"

   > "a deepest mass-carrying cluster vertex u with t*(u) > 0"

   The final Step A1 replacement says:

   > "take u := v. Then u is a hidden geometrically distinct row vertex, trivially within 4*tau of v, mass-carrying (row v reproduces itself), with t*(u) > 0"

   This is not a contract consequence. "Row v reproduces itself" is signed row reproduction, not positive disintegrated C(v)-mass at v. The only disintegration contract available says:

   > `Genuine-mass disintegration: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), height H, halo width a > 0 with G_a = {j : dist_1(p_j, conv W) > a*tau} nonempty (tau = sqrt(delta)), fix for every row a vertex representation p_j = sum_v lambda_jv p_v over geometrically distinct row vertices; then every row index i satisfies g_i <= M_i^a + sum_{j in G_a} P_ij^+ * (H - d_j)/(H - a*tau), where g = P*1_{G_a}, d_j = dist_1(p_j, conv W), P_ij^+ = max(P_ij, 0), and M_i^a = sum_{j in G_a} P_ij^+ * sum_{v : d_v > a*tau} lambda_jv is positive mass supported entirely on HIDDEN row vertices at depth in (a*tau, H].`

   That contract supplies deep hidden vertex mass somewhere in the disintegration, but not inside the 4*tau ball of v. The bracketed correction in A0 admits this:

   > "its representing vertices with h-depth > 16*tau need not be rho-near v"

   The fallback "u=v" would be enough for S1, S4, S5 and the huddle-reduction hypotheses once t*(v)>0 is known, but it is not enough for L2/L6 as stated. The missing hand-off is either a lemma that v itself receives positive C(v)-mass, or a reformulation of L2/L6 to allow the pinned top u=v without the mass-carrying antecedent.

2. Step A0 abandoned proximity estimate: the displayed small-delta inequality is arithmetically false and cannot rescue root existence.

   Step A0 says received-mass proximity gives

   > `p_v within (2+4*delta)(theta_0 + 2*delta) < 4*tau...`

   With theta_0 = 1/8, the left side tends to 1/4 as delta -> 0, while 4*tau = 4*sqrt(delta) tends to 0. So the strict inequality is false for sufficiently small delta. This is in the bracketed, retracted route, so it is not the main failure, but it confirms that A0 has no independent existence proof left after the correction.

3. Step B1 / Split S3: Q3 does not match L1's hypothesis.

   Q3 is:

   > `there exist phi_1, ..., phi_k in Phi, k <= 3, whose average phi-bar has z-bar_{f} >= tau on some row f with a_f^+ >= c_m/4`

   L1 requires:

   > `sum_{j : H - phi(p_j) >= tau} max(P_vj, 0) >= c_m`

   The proved contract being consumed is:

   > `consequently for m >= 0, L >= 0, if sum over A of max(a_j,0) >= m and z_j >= L on A then m*L <= delta*(2+4*delta)`

   Q3 gives at most the L1 hypothesis with m = c_m/4, not m = c_m. Step B1 nevertheless states:

   > `If Q2 or Q3 holds: L1 applies (with phi or phi-bar) and yields c_m * tau <= delta*(2+4*delta)`

   That is a contract mismatch. It is repairable by changing Q3 to a c_m mass threshold, or by applying L1 with c_m/4 and shrinking delta_0 accordingly.

4. Step B1 and C2 charge arithmetic: the delta_0 boundary is not killed as written.

   The target includes the closed condition:

   > `0 < delta(P) <= delta_0`

   G8 sets only:

   > `delta_0 <= min{ 1/4, (c_m/3)^2 [L1's charge, Step B1/C2], ... (c_5 * c_m / 3)^2 [L5's charge, Step C2], ... }`

   But Step B1 derives only

   > `c_m*tau <= 3*tau^2`, hence `tau >= c_m/3`.

   If delta_0 = (c_m/3)^2 and delta = delta_0, there is no contradiction. Step C2 has the identical boundary problem with c_5*c_m/3. Step C1 is safe because G8 includes `(c_r/4)^2 / 2`, but L1/L5 need the same strict slack, e.g. half-thresholds or an explicit choice delta_0 < each charge ceiling. As written, Step D's "every leaf ends in a contradiction with delta <= delta_0" is false at the charge boundaries.

5. Step C3: L6's antecedent is not "EXACTLY" verified because of the same mass-carrying gap.

   Step C3 claims:

   > `Verify L6's hypothesis list item by item: tall (root), heavy at theta_0 = 1/8 (root), u deepest mass-carrying with t*(u) > 0 (A0/A1), disjoint hulls (Q1), every always-tight zero-face row keeps < c_r kappa-high mass (NOT-Q4), rho-far deep mass < c_m (NOT-Q5). That is EXACTLY L6's antecedent`

   The quoted L6 statement does require:

   > `a deepest mass-carrying cluster vertex u with t*(u) > 0`

   A0/A1 do not establish "mass-carrying" for u=v. The rest of the C3 audit is consistent: tall, heavy, disjoint hulls, NOT-Q4, and NOT-Q5 do match the L6 statement. The failing word is exactly "mass-carrying".

6. Branch II Step B2: L2 application has the same root-object defect, but the plateau inequality itself is okay.

   L2 requires:

   > `a mass-carrying deepest cluster vertex u with intersecting always-tight hulls`

   NOT-Q1 gives intersecting hulls, and NOT-Q2 gives the plateau condition because total positive v-row mass is at least 1:

   > `sum_j a_j^+ = 1 + nu_v`

   from the contract:

   > `Mass split: for an exact signed idempotent P and any row index v, writing a_j = P_{vj}, a_j^+ = max(a_j, 0), a_j^- = max(-a_j, 0), and nu_v = sum_j a_j^-, one has sum_j a_j^+ = 1 + nu_v.`

   Thus for every phi, NOT-Q2 gives sum_{z<tau} a_j^+ > 1 - c_m. However, the required "mass-carrying deepest" property still comes only from A0/A1 and is not proved.

7. Step C0 / AG-2 contract audit: u = v is legal in the huddle-reduction dependency chain at the contract level.

   The main contract says:

   > `Disjointness huddle reduction: for an exact signed idempotent P with delta(P) > 0 and nonempty visible set, a hidden top vertex v of height H > 8*tau, and a geometrically distinct row vertex u with ||p_u - p_v||_1 < 4*tau and t*(u) > 0: u is hidden with dist_1(p_u, conv{p_w : w in W}) > H - 4*tau, and if conv{p_f - p_u : f in T(u)} and t*(u)*conv{p_i - p_u : i in O(u)} are disjoint ... then there is a row vertex w with p_w != p_u, ||p_w - p_u||_1 < 4*tau, and dist_1(p_w, conv{p_w' : w' in W}) > H - 8*tau (hence w hidden)`

   This requires u to be a geometrically distinct row vertex, not u != v. The dependency contracts also do not require p_u != p_v:

   > `Ball-cluster exposure void: for an exact signed idempotent P and a hidden top v of height H > 4*tau, no row vertex in the ball cluster C = {k : ||p_k - p_v||_1 < 4*tau} is (rho,kappa)-exposed`

   > `Zero-face vertex support: for an exact signed idempotent P, a hidden geometrically distinct row vertex u, and an optimal exposer h* at u, every zero-face row decomposes convexly onto geometrically distinct row vertices with h* = 0, each rho-near u; if u is within 4*tau of a hidden top of height H > 8*tau, each such vertex is deep hence hidden, and a NONCLONE zero-face blocker forces a SECOND geometrically distinct deep hidden row vertex within 4*tau of u.`

   > `Separator zero-face obstruction: for the exposedness LP at a hidden geometrically distinct row vertex u of an exact signed idempotent P with 0 < t*(u) < inf, a relative-interior optimal exposer h*, and nonempty always-tight far/upper families T, O: if conv{p_f - p_u : f in T} and t*(u)*conv{p_i - p_u : i in O} are disjoint, then ... there exists a nonclone row z with h*(p_z) = 0 and psi(p_z) < 0.`

   > `Zero-face localization: for an exact signed idempotent P and a hidden geometrically distinct row vertex u, every row z with h*(p_z) = 0 for an optimal exposer h* at u satisfies ||p_z - p_u||_1 < 4*tau (rho-near); if additionally u lies within 4*tau of a hidden top v of height H, then ||p_z - p_v||_1 < 8*tau and z has depth > H - 8*tau.`

   Conclusion: AG-2 is not a contract gap. The chain even explicitly forces the output w to satisfy p_w != p_u, so the distinctness requirement appears exactly where it is needed.

8. Step B2 bounded-alpha hand-off: the contract invocation is arithmetically and logically okay once u is available.

   The contract is:

   > `Bounded-alpha forced far slab: for an exact signed idempotent P with 0 < delta(P) <= delta_0 <= 1/4 and nonempty visible set, a hidden top vertex v of height H with top support functional phi ..., a geometrically distinct row vertex u with ||p_u - p_v||_1 < 4*tau, any A_0 >= 0, and any c > 1/2 + delta_0 + 4*(1 + A_0): if F_u cap {j : dist_1(p_j, conv{p_w : w in W}) >= H - c*tau} is empty ... then u is (rho,kappa)-exposed or every hiddenness dual witness of u with sum_i beta_i < tau/4 has sum_i alpha_i > A_0; equivalently a hidden near-top vertex with a small-beta witness of alpha-mass <= A_0 forces a rho-far row from u at depth >= H - c*tau.`

   With A_0 = 0, the required lower bound is c > 1/2 + delta_0 + 4. G8 sets c_w = 6 and delta_0 <= 1/4, so 6 > 4.75. NOT-Q1 plus the conic-reduction contract supplies an alpha-free optimal display:

   > `a display with all a_z = 0 exists if and only if conv{p_f - p_u : f in T} intersects t*(u)*conv{p_i - p_u : i in O}.`

   This part is sound, conditional on having a legitimate u.

9. L4 / Step C1 capacity hand-off: contract match and arithmetic are sound.

   Q4 gives a zero-face row z with high-slab positive mass at least c_r. The capacity contract states:

   > `Affine-exposer row capacity: for an exact signed idempotent P, a row index i, an affine functional h with h(p_i) = 0 and 0 <= h(p_j) <= 1 for all rows j, any threshold eta >= 0, and any set F contained in {j : h(p_j) >= eta}: eta * sum over f in F of max(P_if, 0) <= nu_i`

   Instantiating i=z, h=h*, eta=kappa, F={h*>=kappa} gives c_r*kappa <= nu_z <= delta. Since kappa=tau/4, this gives tau >= c_r/4, and G8's `(c_r/4)^2 / 2` strict slack kills the closed delta boundary. No mismatch found here.

10. Exhaustiveness and boundary ownership: the threshold splits are dichotomies, but one branch predicate is not clone-invariant as written.

   S1 is exhaustive: compact convex hulls either intersect or have positive distance. S2, S4, and S5 are closed-threshold predicates with strict complements, and their boundaries are owned consistently by the charged sides. The heavy target boundary is closed and the leaves L6/L2 use closed or strict conditions consistently where needed.

   The defect is Q3:

   > `some row f with a_f^+ >= c_m/4`

   This is a raw index coefficient condition. Cloning a row point can split a_f^+ among duplicate indices and change whether Q3 is true. That contradicts the decomposition's own discipline:

   > `all predicates are stated on row POINTS / geometrically distinct row vertices / coefficient-mass sums, never on raw index counts.`

   Repair: state Q3 using aggregate positive mass over a geometric row point, or replace it by a mass-sum threshold over the zbar-high set. The latter also fixes the L1 mismatch in Finding 3 if the threshold is c_m.

11. Dimension-freeness: no counting dependence found in the assembly, apart from the clone issue just noted.

   The constants a, c_m, c_r, c_w, c_3, c_5, theta_0, delta_0 do not depend on n. S1 uses convex hull geometry, S2/S4/S5 use mass sums, and L7's chain length k <= 3 is a fixed constant. I found no hidden dimension-counting step in the assembly implication itself. The only invariance violation is Q3's raw-index mass condition.

## AG-1: t*(v) = 0 pinhole audit

Conclusion: at the literal contract layer, t*(v)=0 is closed by combining def-exposed, lem-hiddenness-dual-witness, and lem-zero-face-localization. However, the author's pessimistic warning is justified as a proof-mechanism warning: the localization provenance explains itself by an argument that degenerates at t*=0. From hiddenness-dual-witness plus always-tight-dual-support alone, positivity t*(v)>0 is not derivable.

Relevant contracts:

> `Hiddenness dual witness: for an exact signed idempotent P and a hidden row vertex v (rho = 4*tau, kappa = tau/4, tau = sqrt(delta(P))), writing F_v = {j : ||p_j - p_v||_1 >= rho} for the rho-far row-index set (nonempty for hidden v), there exist lambda_f >= 0 (f in F_v) with sum_f lambda_f = 1 and alpha_i, beta_i >= 0 (over all row indices i) with sum_i beta_i = t*(v) < kappa, such that sum_f lambda_f*(p_f - p_v) + sum_i alpha_i*(p_i - p_v) = sum_i beta_i*(p_i - p_v).`

> `Always-tight dual support: for the exposedness LP at a hidden geometrically distinct row vertex u of an exact signed idempotent P with delta(P) > 0 and nonempty visible set, every optimal hiddenness dual witness (lambda, alpha, beta), after deleting redundant centered-zero constraints, has supp(lambda) contained in T, supp(beta) contained in O, and supp(alpha) contained in Z, where T, O, Z are the rho-far, upper-box, and lower-box constraint families tight on the WHOLE primal optimal face; T is nonempty, and O is nonempty if and only if t*(u) > 0.`

> `Zero-face localization: for an exact signed idempotent P and a hidden geometrically distinct row vertex u, every row z with h*(p_z) = 0 for an optimal exposer h* at u satisfies ||p_z - p_u||_1 < 4*tau (rho-near); if additionally u lies within 4*tau of a hidden top v of height H, then ||p_z - p_v||_1 < 8*tau and z has depth > H - 8*tau.`

What the contracts give:

- Hiddenness-dual-witness gives F_v nonempty for hidden v.
- The exposedness definition makes h=0 feasible; if t*(v)=0, h=0 is an optimal exposer.
- Applying zero-face-localization to h*=0 says every row z has ||p_z-p_v||_1 < 4*tau. This contradicts F_v nonempty.

That is a direct contract composition, not new mathematics. So the statement "the t*=0 case is NOT closed by cited contracts" is false if contracts are treated as authoritative.

What the contracts do not give:

- Hiddenness-dual-witness by itself does not imply t*(v)>0. If t*=0 it merely gives sum beta_i=0 and the balance with the alpha side still present.
- Always-tight-dual-support by itself does not imply t*(v)>0. It explicitly allows the edge:

  > `O is nonempty if and only if t*(u) > 0`

  so at t*=0 it says O is empty, not impossible.

The role/provenance warning:

> `mechanism: far rows have h* >= t* by the LP far constraints, so h* = 0 forces rho-nearness`

At t*=0 this mechanism only gives far rows h* >= 0, which is vacuous. Therefore the contract is strong enough to close AG-1, but the shard's recorded mechanism does not justify that boundary. I do not count AG-1 as an assembly-contract gap; I do count it as a shard-proof audit risk that should be resolved before upgrading confidence.

## AG-2: u = v instantiation audit

Conclusion: no contract in the cited dependency chain requires p_u != p_v or ||p_u-p_v||_1 > 0. The u=v instantiation is legal at the contract level, provided t*(v)>0.

Exact clauses checked:

> `a hidden top vertex v of height H > 8*tau, and a geometrically distinct row vertex u with ||p_u - p_v||_1 < 4*tau and t*(u) > 0`

This admits u=v because 0<4*tau and "geometrically distinct row vertex" is a property of the row point, not a pairwise inequality.

Dependency chain:

> `ball cluster C = {k : ||p_k - p_v||_1 < 4*tau}`

contains v itself.

> `if u is within 4*tau of a hidden top of height H > 8*tau`

contains u=v.

> `for the exposedness LP at a hidden geometrically distinct row vertex u ... with 0 < t*(u) < inf`

has no reference to v and no pairwise distinctness condition.

> `if additionally u lies within 4*tau of a hidden top v of height H`

again allows u=v.

The only explicit pairwise distinctness requirement is on the output:

> `there is a row vertex w with p_w != p_u`

That is consistent and not a hidden hypothesis on the input.

