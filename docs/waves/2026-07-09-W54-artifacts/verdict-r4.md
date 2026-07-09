AUDIT: CLAUSE-HOLDS / T*POSITIVE-PROVED — the recorded far-constraint mechanism needs the missing observation that a finite geometrically distinct row vertex with nonempty rho-far set has t*(v) > 0, so the t*=0 boundary is impossible under the shard contract.

§1. Boundary analysis

The exposedness LP at u is:

- choose an affine h with h(p_u)=0 and 0 <= h(p_i) <= 1 on all rows;
- maximize t subject to t <= h(p_f) for every rho-far row f in F_u = {j : ||p_j-p_u||_1 >= rho}.

Thus an optimal exposer h* means the h-component of an optimal LP solution, equivalently an admissible h* with min_{f in F_u} h*(p_f) = t*(u), when F_u is nonempty and t*(u) is finite. LP attainment is part of the hiddenness-dual-witness proof shape.

The intended proof of the first clause is exactly:

- every rho-far row f satisfies h*(p_f) >= t*(u);
- if t*(u) > 0 and h*(p_z)=0, then z cannot be rho-far;
- therefore ||p_z-p_u||_1 < rho = 4*tau.

This works for every optimal exposer, not just relative-interior optimal exposers. Relative interior is relevant in separator-zero-face-obstruction, not here.

If one artificially allows t*(u)=0 with F_u nonempty, the localization statement is false. At t*=0, h=0 is an optimal LP solution, and indeed every optimal exposer has min_{F_u} h=0; hence some rho-far row has h=0. So relative-interior selection would not rescue the clause at that abstract boundary.

But the boundary cannot occur under this shard's stated hypotheses. Since p_u is a geometrically distinct row vertex, p_u is not in the convex hull of the other distinct row points. By strict finite-dimensional separation, there is an affine a with a(p_u)=0 and a(p_j)>0 for every row point p_j != p_u. Normalize by M=max_j a(p_j)>0 to get an admissible h=a/M with h(p_u)=0 and 0<=h(p_j)<=1. If F_u is nonempty and rho>0, far rows are not geometric clones of u, so min_{f in F_u} h(p_f)>0. Hence t*(u)>0.

For a hidden row vertex, rho=0 cannot be the nonvacuous obstruction: h=0 gives t*(u)>=0, while hidden means t*(u)<kappa. If delta=0 then kappa=0, so no row vertex is hidden. Thus a hidden geometrically distinct row vertex with F_u nonempty has delta>0, rho>0, and t*(u)>0.

Conclusion: the contract is literally true. The proof record is incomplete at the boundary only because it did not spell out the one-line positive-margin fact.

§2. Consumer audit

Direct registered consumers of lem-zero-face-localization are exactly:

- lem-zero-face-vertex-support: hypothesis is "for an exact signed idempotent P, a hidden geometrically distinct row vertex u, and an optimal exposer h* at u". It does not state t*(u)>0, but the positive-margin argument above supplies it from those hypotheses. Safe.

- lem-disjointness-huddle-reduction: hypothesis includes "delta(P)>0 and nonempty visible set", a hidden top v with H>8*tau, and a geometrically distinct row vertex u with ||p_u-p_v||_1<4*tau and t*(u)>0. Safe explicitly.

- lem-disjoint-hulls-forced-alpha: hypothesis includes "a hidden geometrically distinct row vertex u with t*(u)>0". Safe explicitly.

No other direct deps were found by grepping argument/lemmas for lem-zero-face-localization.

§3. The t*(v)>0 question

The assembly's desired one-line lemma is provable from the registered definitions alone, without lem-zero-face-localization:

Claim: every hidden geometrically distinct row vertex v with F_v={j:||p_j-p_v||_1>=4*tau} nonempty has t*(v)>0.

Proof: because v is a row vertex, p_v is outside the compact convex hull of the other distinct row points. Strict separation gives an affine a with a(p_v)=0 and a>0 on every other distinct row point. Since the row set is finite, m=min{a(p_j): p_j != p_v as a vector}>0 and M=max_j a(p_j)>0. With h=a/M, all row values lie in [0,1], h(p_v)=0, and h is admissible. Hiddenness rules out delta=0, hence rho=4*tau>0; therefore every f in F_v is not a clone of v, and h(p_f)>=m/M>0. So t*(v)>=m/M>0.

The only would-be obstruction is a clone of v included among far constraints. That happens only when rho=0, but then kappa=0 and hiddenness is impossible because h=0 gives t*(v)>=0. Thus there is no exact hidden-vertex configuration with t*=0 and nonempty F_v.

§4. Recommended registry actions

Keep lem-zero-face-localization's contract, but amend its proof note/provenance: before applying "far rows have h* >= t*", insert the positive-margin lemma above.

Preferably register a small proved lemma, e.g. "finite vertex positive exposedness margin": for any finite row configuration, any geometrically distinct row vertex v with rho>0 and nonempty F_v has t*(v)>0. Then add it as a dep of lem-zero-face-localization and any LP shard that discusses the t*=0 edge.

Clarify def-exposed or the LP notes: "optimal exposer" should mean an admissible h attaining min_F h=t*(v), or the h-component of an optimal (h,t) LP pair. At t*=0 in an abstract non-vertex LP, h=0 would indeed be optimal and localization would fail; the row-vertex positive-margin fact is what excludes that case here.
