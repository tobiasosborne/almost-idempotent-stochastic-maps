P1 conj-l5-gap-1: VALID-WITH-CORRECTION
P2 lem-intersection-branch-production: VALID-WITH-CORRECTION
P3 lem-huddle-charge-assembly: VALID-WITH-CORRECTION

# P1 findings

The mathematical contract is faithful. Its quantifier order is:

```text
exists universal c_5 > 0;
for every fixed universal c_m > 0, exists delta_5(c_m) > 0;
for every admissible (P,v,A), exists one top support functional phi.
```

Thus c_5 is chosen before, and is independent of, c_m; only the ceiling may depend on c_m. This is exactly `context/verdict-bridges.md` item 2. It is also the order attacked by W62: `context/DECOMPOSITION-W62-L5.md` fixes c_m in (0,1), constructs a c_5 explicitly declared independent of c_m, and lets the smallness ceilings depend on the fixed threshold.

The verdict’s range c_m > 0 is mathematically equivalent to W62’s nonvacuous range c_m in (0,1). One direction is immediate. Conversely, halve the common W62 c_5; obtain c_m = 1 from the c_m = 1/2 instance; and, for c_m > 1, choose delta_5(c_m) < c_m - 1. The antecedent is then empty because a row’s total positive mass is at most 1 + delta(P).

The remaining clauses match both pinned sources: exact signed idempotence; nonempty W; a hidden top v with H > 16 tau; weak far boundary ||p_j-p_v||_1 >= 4 tau; strict depth boundary d_j > H - 8 tau; mass S_A >= c_m; and one phi with charge at least c_5 c_m tau. No proof is claimed, and the body does not revive the prohibited pointwise-to-averaged-witness inference.

The frontmatter is not registration-correct. Every inspected `conj-*` shard uses `kind: lemma`; conjectural status is represented by `status: conjecture`. More importantly, the four `lem-l5-*` results do not prove P1 and are not consumed by its contract. They are only part of its reduction/attack tree. Listing them as unconditional `deps` creates four false prerequisite edges.

This is consistent with the comparison shards. `conj-straddling-web-exclusion` legally imports `lem-sl1a-three-cell-reduction` because that reduction’s contract directly derives the exclusion from its three cells. The standalone leaves `conj-cotop-web-coupling` and all three `conj-sl1a-*` cells have empty dependency lists. P1 is likewise a standalone target; its reduction-tree relation belongs in the body.

Exact corrected frontmatter lines:

```yaml
kind: lemma
deps:
status: conjecture
owner: B
```

`owner: B` follows the W62 `lem-l5-*` family; in any event, `owner: proposed` is not a legal registry owner.

# P2 findings

The proof is contractually honest. The full contract of `lem-intersection-witness-confinement` is:

> Intersection-branch witness confinement: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set, hidden top vertex v with t*(v) in (0, kappa), and an alpha-free reduced optimal display sum over T of lambda_f*(p_f - p_v) = t*(v)*sum over O of gamma_i*(p_i - p_v) (lambda, gamma probability vectors on T(v), O(v), per lem-optimal-face-conic-reduction): (B1) (lambda, 0, t*gamma) is a hiddenness dual witness of v with sum beta = t*(v) < kappa; (B2) the witness barycenter b = sum lambda_f p_f satisfies ||b - p_v||_1 = t*(v)*||q - p_v||_1 <= t*(v)*(2+4*delta) < (1/2+delta)*tau; (B3) for every admissible exposer h at v, sum_f lambda_f*h(p_f) <= t*(v); (B4) for every top support functional phi at v and every finite convex average, sum_f lambda_f*(H - phi(p_f)) <= t*(v)*(2+4*delta) < (1/2+delta)*tau; hence for lambda the mass at deficit >= tau is < 1/2 + delta.

It contains B1–B4 only. P2 does not consume an invented B5. B1 supplies exactly the hiddenness-dual-witness and total-beta < tau/4 hypotheses of proved `lem-top-witness-third-actor`. That shard concludes, for every c > 1/2 + delta,

```text
lambda{f in F_v : d_f > H - c tau} > 1 - (1/2 + delta)/c.
```

At c = 4 and delta <= 1/4 this is strictly greater than 13/16, so the complementary mass mu on d_f <= H - 4 tau is strictly below 3/16. The mass, depth, far-row normalization, and 13/16 versus 3/16 constants all match.

The hull hypothesis also supplies precisely what is used. `lem-optimal-face-conic-reduction` says an all-a_z = 0 reduced optimal display exists iff

```text
conv{p_f-p_v : f in T(v)} intersects
t*(v) conv{p_i-p_v : i in O(v)}.
```

This is the exact L2-core intersection predicate. The conic-reduction hypotheses follow from the hidden row vertex and t*(v) > 0. `lem-always-tight-dual-support` makes T the rho-far always-tight family and makes O nonempty iff t*(v) > 0, so the probability-vector display and T(v) subset F_v are legal.

The arithmetic checks without repair:

- Equality mu = tau/D is owned by case (i). Case (ii) therefore has mu > tau/D and meets SL1b’s weak lower bound mu_S(1) >= tau/D.
- From `(1-mu)(b_L-p_v) + mu(b_S-p_v) = b-p_v`, the triangle inequality gives the displayed bound in the correct direction. Every row is within D = 2 + 4 delta of row p_v, hence so is the S-barycenter.
- The numerator is `(1/2+delta)tau + (tau/D)D = (3/2+delta)tau`. Since mu < 3/16, renormalization costs less than 16/13; at delta <= 1/4 the result is at most 28 tau/13 < 2.2 tau.
- `def-exposed` states 0 <= h(p_j) <= 1 on every row. Restriction cannot increase the unnormalized exposer integral, and renormalizing the L-part costs less than 16/13.

The mu = 0, empty-side, depth-equality, and hull-tangency boundaries are owned. No averaged top-support witness is used; B4 is cited only as the certificate that this dead route remains dead.

The sole correction is registry metadata. A checked conditional proof may have conjectural dependencies and still has `status: proved`, as elsewhere in this registry. `proposed` is neither a registered mathematical status nor a legal owner. Exact corrected text:

```yaml
status: proved
provenance: REPAIR-W68-bridge.md Part 2 (W68 extraction of context/l2-attack.md §§2.6–2.7; independently checked in VERDICT-W68-bridge.md; the prose-only B5 is replaced by the proved lem-top-witness-third-actor interface)
owner: A
```

# P3 findings

The contract is explicitly conditional on all four conjectures, with their witnesses and ceilings exposed: SL1a at delta_a, SL1b at delta_b, co-top coupling at (c_*, delta_c), and L5 at (c_5, delta_5(c_*/2)). Shrinking c_5 to min(c_5,1) preserves L5 with the same ceilings.

The conclusion uses exactly the original strict near set

```text
{j : ||p_j-p_v||_1 < 4 tau and d_j > 16 tau}
```

and excludes its weak heavy boundary mass >= 7/8 for H > 16 tau. This is the original bridge/verdict target and is stronger than the a = 16, theta_0 = 1/8 near-cluster conclusion on its H > 172 tau regime.

Branch (I) is legal. A hidden vertex has F_v nonempty by `lem-hiddenness-dual-witness`. Since delta > 0, `lem-positive-exposedness-margin` then gives the full 0 < t*(v) < kappa bound. `lem-always-tight-dual-support` gives nonempty T(v) and O(v). Thus P2’s delicate t*(v) in (0,kappa) hypothesis is supplied. Its outputs match the SL1a and SL1b contracts exactly, including weak/strict boundaries and all constants.

Branch (II) also matches. `conj-cotop-web-coupling` receives tallness, t*(v) > 0, disjoint always-tight hulls, and the contrary 7/8 heavy hypothesis. It returns S_A >= c_* on exactly

```text
A = {j : ||p_j-p_v||_1 >= 4 tau and d_j > H - 8 tau}.
```

This is the carrier consumed by L5. Applying L5 at c_m = c_*/2 yields charge at least c_5 c_* tau/2. `lem-top-deficit-price` applies to the same A and every top support functional, including L5’s chosen phi, and gives the opposite bound delta(2 + 4 delta).

The square ceiling is correct. Put x = c_5 c_*/6. From delta <= x^2, tau <= x. Since c_5 <= 1 and c_* < 1, delta < 1/36 and 2 + 4 delta < 3. Hence

```text
delta(2+4 delta) < 3 tau^2
                   <= 3 x tau
                    = (c_5 c_*/2) tau.
```

Strictness survives the endpoint delta = x^2. Neither the exponent 2 nor denominator 6 needs repair.

The root split is exhaustive: the nonempty finite convex hulls either intersect, with tangency included, or compactness gives positive distance. The t* = 0, empty-T, and empty-O cases are eliminated before the split. No old L2 equivalence, averaged-witness mechanism, huddle recursion, or dead route is used. Dropping `lem-l2-core-collapse` is correct; P2 operates directly at configuration level. The remaining direct dependencies are genuinely consumed.

There is one harmless contract cleanup: the literal `1/4` duplicates delta_B = 1/4. The named delta_B already pays P2’s ceiling and the D <= 3 arithmetic, while the square ceiling supplies strictness. Remove the duplicate so every listed entry has a distinct use. Exact corrected fragment:

```text
With delta_B = 1/4 and delta_0 = min{delta_a, delta_b, delta_c, delta_5(c_*/2), delta_B, (c_5*c_*/6)^2}, no exact signed idempotent ...
```

The metadata needs the same schema correction as P2:

```yaml
status: proved
provenance: REPAIR-W68-bridge.md Part 3 (conditional W68 repair of the W54 huddle-charge assembly; independently checked in VERDICT-W68-bridge.md)
owner: A
```

# CROSS-CUTTING

`deps` are unconditional proof imports, not bibliography, provenance, or attack-tree arrows. P1 must have no lemma dependencies; its W62 reduction-tree relation belongs in the body until a registered reduction lemma actually concludes P1. P2 and P3 list results their displayed proofs directly consume. With P1’s false edges removed, P3’s direct import of P1 remains legal and no cycle or hidden shard consumption appears.

The three proposed contracts contain no impermissible ‘hence’ clauses. P2’s B4 is not promoted into a depth-mass clause, P3 never averages row-dependent support functionals, and the simplex/witness-averaging wall remains respected. Apart from the exact frontmatter and duplicate-ceiling corrections above, the constants, quantifiers, boundary ownership, and DAG-level consumption are consistent.

