<!--
ROLE: the W54 huddle-charge decomposition tree — the VERIFIED assembly of record
  (session 13, 2026-07-09). Read PART A (v1, the Fable architect original) THROUGH
  PART B (the repair delta + G8-v3, verifier-prescribed, applied verbatim).
  Verification: V-ASM INVALID -> repairs -> V-ASM-2 VALID-WITH-CORRECTIONS (G8-v3
  applied) + R4/V-R4 (AG-1 discharged via lem-positive-exposedness-margin; AG-2
  resolved). Leaf status at consolidation: L1, L4 PROVED+VALID (banked); L3 = proved
  lem-top-support-dual-face + conj-summit-cylinder-exclusion; L7 BLOCKED (two named
  gaps); L2-v2, L5, L6-v2 OPEN. STATUS DISCIPLINE (L0): a strategy artifact -
  promotes nothing; the registry shards carry the rigour tags.
-->

# PART A — the architect original (v1)

DECOMPOSITION: 7 leaves, 3 case predicates — a two-level tree over the forced huddle anatomy: split on the hull geometry at the deepest mass-carrying cluster vertex (intersect vs disjoint), then within each branch split on where the top's positive mass and the forced far-actor web sit relative to the depth band, closing every leaf through the ONE proved charging channel (lem-top-deficit-price / lem-affine-exposer-row-capacity) with an averaged-phi upgrade.

<!--
ROLE: W54 huddle-charge decomposition (AUTHOR artifact; hostile verification pending).
STATUS DISCIPLINE (L0): everything here is AUTHOR-CLAIM except quoted shard contracts
(status: proved, cited by id). The leaves L1-L7 are CONJECTURE-grade candidate lemmas.
Author: Fable decomposition architect, 2026-07-09, session 13, wave W54.
Dimension-free and clone-invariant throughout: no constant depends on n; all predicates
are stated on row POINTS / geometrically distinct row vertices / coefficient-mass sums,
never on raw index counts.
-->

# W54 decomposition of THE HUDDLE CHARGE

Notation (definitions/, fixed throughout): P an exact signed idempotent (def-signed-idempotent),
delta = delta(P) (def-negative-mass), tau = sqrt(delta), rho = 4*tau, kappa = tau/4
(def-visible-set), W = W(P) the visible set, C_W = conv{p_w : w in W}, d_j = dist_1(p_j, C_W),
H = max_i d_i (def-height), nu_i = row-i negative mass, a_j = P_vj with a_j^+ = max(a_j, 0).
For a hidden geometrically distinct row vertex u: t*(u) the exposedness margin (def-exposed);
T(u), O(u), Z(u) the always-tight far / upper-box / zero-face families of the exposedness LP
at u (lem-always-tight-dual-support); K_T(u) = conv{p_f - p_u : f in T(u)},
K_O(u) = t*(u)*conv{p_i - p_u : i in O(u)}. A "top support functional" phi at v is affine with
phi(p_v) = H, phi <= 0 on C_W, 1-Lipschitz for l1 (existence: lem-top-deficit-price contract);
z_j = H - phi(p_j) in [0, 2+4*delta] is the top-deficit of row j under phi.

---

## 1. THE PINNED TARGET

**THE HUDDLE CHARGE (tall-emptiness, heavy form — the (M2) target; identical to the
conclusion of conj-near-cluster-absorption restricted to tall tops).**

> There exist universal constants a >= 4, theta_0 in (0,1), delta_0 > 0 (none depending
> on n) such that NO exact signed idempotent P with 0 < delta(P) <= delta_0 and
> W(P) != {} has a hidden top vertex v of height H > a*tau satisfying
>
>     sum_{j in C(v)} max(P_vj, 0)  >=  1 - theta_0,
>
> where C(v) = { j : ||p_j - p_v||_1 < 4*tau  AND  d_j > a*tau }  (the rho-near deep
> cluster — both conditions required, verbatim the summand set of
> conj-near-cluster-absorption).

Constants to be produced by the assembly: (a, theta_0, delta_0), plus the internal
constants (A_0, c_w, c_r) handed between leaves (Section 4, step G8). We will exhibit the
feasible order with a = 16 as the working calibration (any a >= 16 works verbatim;
downstream consumers need only SOME universal a — conj-low-slab-cap's "1/2 is calibration,
not load-bearing" discipline).

Boundary ownership: "tall" is the STRICT inequality H > a*tau; "heavy" is the NON-strict
sum >= 1 - theta_0 (equality is inside the excluded class, matching
conj-near-cluster-absorption whose conclusion is the non-strict <= 1 - theta_0; the
boundary instance is claimed by the target, so the assembly must kill it too — it does,
all leaf hypotheses below are stated with the closed heavy condition).

Standing reductions used everywhere (all proved, cited by shard):
(R1) Every j in C(v) has depth d_j > a*tau > 4*tau and every row vertex geometrically
     inside the rho-ball of v is hidden with d > H - 4*tau (lem-ball-cluster-exposure-void,
     needs only H > 4*tau).
(R2) v itself is hidden (def-height: a height maximizer with H > 0 is hidden), so v has
     small-beta hiddenness dual witnesses (lambda, alpha, beta), sum beta < kappa,
     lambda a probability on F_v = {j : ||p_j - p_v||_1 >= rho}
     (lem-hiddenness-dual-witness).
(R3) For every c > 0 and every small-beta witness of v:
     lambda{f in F_v : d_f > H - c*tau} > 1 - (1/2 + delta)/c (lem-hiddenness-depth-markov);
     at c = 4: > 13/16 of lambda sits rho-far at depth > H - 4*tau
     (lem-top-witness-third-actor).
(R4) For ANY top support functional phi and ANY index set A:
     sum_{j in A} a_j^+ z_j <= nu_v*(2+4*delta) <= delta*(2+4*delta)
     (lem-top-deficit-price). This is the ONLY charging channel the assembly uses at v;
     its blind spot (z < 4*tau on the rho-ball) is exactly what the case tree is built to
     circumvent.

---

## 2. THE CASE TREE

The tree is over the configuration space of a putative counterexample (P, v): P an exact
signed idempotent with 0 < delta <= delta_0, W != {}, v a hidden top of height H > a*tau
carrying >= 1 - theta_0 positive mass on C(v). Extremal choice, fixed once at the root
and free: **among all hidden tops of P realizing the maximal height H, fix v; among all
geometrically distinct row vertices carrying positive conic weight in some fixed vertex
representation of the C(v)-mass (lem-genuine-disintegration supplies one), let u be a
DEEPEST mass-carrying cluster vertex with t*(u) > 0** (existence of such u is Step A0 of
the assembly, from lem-genuine-disintegration + R1; "mass-carrying" = u receives positive
disintegrated weight from C(v)-rows; ties broken arbitrarily — the argument never uses
uniqueness).

Each internal node splits on a predicate Q / not-Q with the boundary owner stated.

**NODE N0 (root).** The counterexample configuration (P, v, u) as above.

**SPLIT S1 (hull geometry at u).**
Q1: "K_T(u) and K_O(u) are DISJOINT (as compact convex sets: dist_1(K_T, K_O) > 0)."
Boundary ownership: tangency / any common point = NOT-Q1 (the intersection branch owns
gap = 0; disjointness is strict). This matches lem-rank3-zero-face-anatomy's convention
(hulls intersect iff gap_2 <= 0) and lem-separator-zero-face-obstruction's strict-separator
hypothesis, so no seam is double- or un-claimed.
  - Q1 true  -> BRANCH I  (the huddle branch: lem-disjointness-huddle-reduction fires).
  - Q1 false -> BRANCH II (the intersection branch: an alpha-free optimal display exists
                at u by lem-optimal-face-conic-reduction).

**BRANCH II (hulls intersect at u). SPLIT S2 (witness far-mass of u vs the top slab).**
By lem-optimal-face-conic-reduction (proved; t*(u) > 0), NOT-Q1 gives a reduced optimal
display of u with all zero-face coefficients a_z = 0, i.e. a small-beta hiddenness dual
witness of u with alpha = 0 <= A_0 for every A_0 >= 0. lem-bounded-alpha-forced-far-slab
(at A_0 = 0, c = c_w for any fixed c_w > 1/2 + delta_0 + 4) then forces a row f_u with
||f_u - p_u||_1 >= 4*tau and d_{f_u} >= H - c_w*tau: u drags its OWN rho-far top-slab
actor. Split on where v's positive mass interacts with such forced far actors:

Q2: "sum_{j : z_j >= tau} a_j^+ >= c_m  for some top support functional phi", where
c_m = theta-free universal constant fixed in Section 4 (c_m = 1/4 works); i.e. at least
c_m of v's positive row mass carries top-deficit >= tau under SOME phi.
Boundary ownership: equality (sum = c_m) belongs to Q2 (the charged side); NOT-Q2 is the
strict "< c_m for EVERY phi".
  - Q2 true  -> LEAF L1 (direct charge: R4 gives c_m*tau <= 3*delta, i.e. H-free
                contradiction at small delta — see assembly; this leaf is already a
                PROVED consequence of lem-top-deficit-price, kept as a leaf only to make
                the tree exhaustive-by-construction; grade EASY).
  - Q2 false -> the top's positive mass is (1 - c_m)-concentrated on {z < tau} for every
                phi. SPLIT S3 below.

**SPLIT S3 (within BRANCH II, NOT-Q2: does the forced far web stay uniformly shallow in
top-deficit under the AVERAGED functional?).**
Let Phi denote the set of top support functionals at v (nonempty, convex; R4 holds for
every element and hence for every finite convex average — z is affine in phi).
Q3: "there exist phi_1, ..., phi_k in Phi, k <= 3, whose average phi-bar has
z-bar_{f} >= tau on some row f with a_f^+ >= c_m/4 " — i.e. an averaged functional sees
mass that each single phi misses.
Boundary: equality z-bar = tau belongs to Q3.
  - Q3 true  -> LEAF L1 again (R4 applied to phi-bar — legal since Phi is convex; the
                assembly folds Q3-true into L1's charge; no separate leaf needed).
  - Q3 false -> the genuinely blind configuration: (1 - c_m) of v's mass has z < tau
                under EVERY phi in Phi and every short average. This is the rigid
                "uniform summit plateau" local structure -> LEAF L2 (plateau exclusion,
                the creative core of Branch II) and LEAF L3 (far-actor tension: the
                forced actor f_u of u must itself be priced), which jointly close the
                branch (assembly Step B).

**BRANCH I (hulls disjoint at u). The huddle fires.**
By lem-disjointness-huddle-reduction (proved; hypotheses: H > 8*tau — implied by
H > a*tau, a >= 16; u geometrically distinct, ||p_u - p_v||_1 < 4*tau from cluster
membership, t*(u) > 0): u is hidden with d_u > H - 4*tau AND there is a geometrically
distinct row vertex w, ||p_w - p_u||_1 < 4*tau, d_w > H - 8*tau (hidden). Additionally
lem-separator-zero-face-obstruction supplies the P-harmonic affine direction psi
(psi(p_u) = 0, P psi = psi, psi > 0 on T(u), psi < 0 on O(u)) and a nonclone zero-face
blocker z_0 (h*(p_{z_0}) = 0, psi(p_{z_0}) < 0), all rho-near u (lem-zero-face-localization).

**SPLIT S4 (the blocker's exposer-value budget at u).**
Q4: "the always-tight zero face Z(u) contains a row z with
sum_{j : h*(p_j) >= kappa} max(P_zj, 0) >= c_r", where h* is the (relative-interior)
optimal exposer at u fixed by the separator lemma and c_r in (0,1) universal (fixed in
Section 4; c_r = 1/2 works). I.e.: some zero-face row SHIPS at least c_r of its positive
mass to the kappa-high slab of h*.
Boundary: equality >= c_r belongs to Q4 (the charged side).
  - Q4 true  -> LEAF L4 (capacity kill: lem-affine-exposer-row-capacity at threshold
                kappa gives kappa*c_r <= nu_z <= delta, i.e. c_r*tau/4 <= delta,
                impossible for delta < (c_r/4)^2 — PROVED mechanism, grade EASY).
  - Q4 false -> every zero-face row keeps > 1 - c_r of its positive mass on the
                kappa-LOW slab {h* < kappa} of u's exposer — which by
                lem-zero-face-localization + the LP far constraints (far rows have
                h* >= t*; kappa-low rows are either rho-near u or have h* in [t*, kappa))
                confines the zero-face rows' positive mass to the 8*tau-huddle
                neighbourhood and the thin [t*, kappa) shell. SPLIT S5.

**SPLIT S5 (within Branch I, NOT-Q4: where does the huddle's returned mass exit?).**
The huddle {u, w, zero-face rows} is now a mass-trap candidate: deep (d > H - 8*tau),
mutually rho-near, each member keeping > 1 - c_r of its positive mass kappa-low. But v's
witness forces > 13/16 of lambda-mass rho-FAR from v at depth > H - 4*tau (R3), and
lem-bounded-alpha-forced-far-slab at u (with the alpha budget from S1/S4 structure)
forces far actors too. Split on the sign structure of P on the far actors:

Q5: "sum over {j : ||p_j - p_v||_1 >= 4*tau, d_j > H - 8*tau} of a_j^+ >= c_m" (v places
>= c_m positive mass on rho-FAR deep rows). Boundary: equality belongs to Q5.
  - Q5 true  -> LEAF L5 (far-deep charge: rho-far mass has z_j >= ? — NOT automatic,
                z and d are different functionals; L5 is the single-sentence lemma that
                a definite fraction of rho-far deep mass has z >= c*tau for a suitably
                CHOSEN phi — the "phi sees the far slab" leaf; grade MEDIUM).
  - Q5 false -> v's positive mass is (1 - theta_0 - c_m)-trapped in the CLOSED huddle
                system {rho-near of v} union {shallow d <= H - 8*tau}; combined with
                heaviness (>= 1 - theta_0 on C(v), which is rho-near AND deep), the
                trapped picture is: >= 1 - theta_0 - c_m of mass rho-near v, deep,
                kappa-low at u, low-z under every phi. This maximal-rigidity
                configuration is closed by LEAF L6 (the exchange-starvation kill at the
                deepest vertex u — the huddle cannot pay its own exposer ledger) plus
                LEAF L7 (the w-recursion cap: the second huddle member w, itself deep
                and hidden, repeats the anatomy at depth H - 8*tau, and two nested
                applications exhaust the 4*tau localization budget). Grade HARD-CREATIVE
                (L6), MEDIUM (L7).

**Tree summary (exhaustive by construction — every internal node is a literal Q/not-Q):**

```
N0 (P, v tall heavy, u = deepest mass-carrying cluster vertex, t*(u) > 0)
├─ S1: Q1 hulls at u DISJOINT?
│  ├─ NO  (BRANCH II: intersection, alpha-free witness at u)
│  │  ├─ S2: Q2 some phi puts >= c_m of v's mass at z >= tau?
│  │  │  ├─ YES -> L1 (deficit-price charge)               [EASY]
│  │  │  └─ NO
│  │  │     ├─ S3: Q3 an average phi-bar sees a_f^+ >= c_m/4 at z-bar >= tau?
│  │  │     │  ├─ YES -> L1 (charge phi-bar)               [EASY]
│  │  │     │  └─ NO  -> L2 + L3 (plateau exclusion + far-actor tension)
│  │  │     │            [HARD-CREATIVE + MEDIUM]
│  └─ YES (BRANCH I: huddle pair (u, w) + blocker z_0 + harmonic psi forced)
│     ├─ S4: Q4 some zero-face row ships >= c_r mass kappa-high?
│     │  ├─ YES -> L4 (capacity kill)                      [EASY]
│     │  └─ NO
│     │     ├─ S5: Q5 v puts >= c_m mass rho-far deep?
│     │     │  ├─ YES -> L5 (far-deep deficit visibility)  [MEDIUM]
│     │     │  └─ NO  -> L6 + L7 (exchange starvation + w-recursion cap)
│     │     │            [HARD-CREATIVE + MEDIUM]
```

Note on exhaustiveness: S1 is a genuine dichotomy on compact convex sets (disjoint or
not); S2/S3/S4/S5 are threshold predicates on real-valued functionals of (P, v, u) with
declared boundary ownership. No predicate mentions rank, n, or index counts; all are
clone-invariant (mass sums over row points via a_j^+ aggregation; vertex statements on
geometrically distinct vertices; Q1/Q4 quantify over the always-tight families which are
clone-robust by lem-always-tight-dual-support's nonclone conventions).

---

## 3. THE LEAVES

Every leaf is a single fully-quantified candidate lemma (registry-contract style). "May
consume" lists only status:proved shards. Constants (a, theta_0, delta_0, A_0, c_m, c_r,
c_w) are as fixed in Section 4.

### L1 — Deficit-price charge (the closer for Q2-true / Q3-true)

**Statement.** For an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty
visible set, hidden top vertex v of height H, a constant c_m > 0, and a top support
functional phi (or a finite convex average of such) with
sum_{j : H - phi(p_j) >= tau} max(P_vj, 0) >= c_m, one has H-free:
c_m * tau <= delta * (2 + 4*delta).

**May consume:** lem-top-deficit-price (its m-L clause at m = c_m, L = tau).
**Mechanism.** Direct instantiation: restrict the pairing sum to A = {j : z_j >= tau};
R4 gives c_m*tau <= delta*(2+4*delta) <= 3*delta, i.e. tau <= 3*tau^2/c_m, impossible for
tau < c_m/3. Averages of top support functionals are top support functionals (convexity
of the defining conditions: affine, value H at p_v, <= 0 on C_W, 1-Lipschitz), so the
Q3-true case is the same instantiation.
**Grade:** EASY-DERIVATION (it is a corollary of a proved shard; registered as a leaf
only to carry the tree's exhaustiveness).
**Risk note:** essentially none — the only checkable point is the convexity of the class
Phi (1-Lipschitz and the two affine constraints are convex conditions; an average of
functionals equal to H at p_v equals H at p_v). A verifier should confirm no strictness
is lost at the Q2/Q3 boundary (none is: >= throughout).

### L2 — Summit-plateau exclusion (Branch II creative core)

**Statement.** There exist universal c_m in (0,1), delta_0 > 0 such that no exact signed
idempotent P with 0 < delta(P) <= delta_0, nonempty visible set, and hidden top vertex v
of height H > 16*tau has, simultaneously, a mass-carrying deepest cluster vertex u with
intersecting always-tight hulls and, for every top support functional phi,
sum_{j : H - phi(p_j) < tau} max(P_vj, 0) > 1 - c_m.

**May consume:** lem-hiddenness-dual-witness, lem-hiddenness-depth-markov,
lem-top-witness-third-actor, lem-optimal-face-conic-reduction,
lem-bounded-alpha-forced-far-slab, lem-cs-low-slab-pincer, lem-top-deficit-price,
lem-harmonic-affine-bridge, lem-received-mass-proximity.
**Mechanism.** NOT-Q2/NOT-Q3 forces v's positive mass onto a z < tau plateau for EVERY
phi — but the set of phi's separates points of the summit region at scale d(., C_W): if
the (1-c_m)-mass support had l1-diameter >= 2*tau, two support functionals adapted to two
extreme summit points would disagree by >= tau on part of the mass, contradicting
plateau-ness under both (the averaging axis: phi-bar = (phi_1 + phi_2)/2 sees the spread).
Hence the plateau forces the mass into an l1-ball of radius O(tau) around p_v; then
lem-received-mass-proximity puts p_v within O(tau + theta) of the hull of a set at depth
> H - O(tau), while u's alpha-free witness (intersection horn) + the forced far actor of
lem-bounded-alpha-forced-far-slab (A_0 = 0) plants a rho-far row at depth >= H - c_w*tau
whose existence contradicts the plateau's diameter bound via the third-actor mass count
(R3: > 13/16 of lambda rho-far and deep, yet every rho-far deep row has z >= ? — the gap
L2 must close is exactly turning lambda-mass into a z lower bound for a WELL-CHOSEN phi).
**Grade:** HARD-CREATIVE (this is where the affine-pairing blind spot must actually be
broken; the averaging-over-phi idea is new and untested).
**Risk note:** could be FALSE if there is a configuration whose entire summit (v, cluster,
far actors) is z-flat under every phi simultaneously — i.e. the top face of the row
polytope contains a rho-spanning flat of depth-variation o(tau) carrying both v's mass
and the witness mass. No banked instance looks like this (W52: every attempted tall entry
reverted), but nothing proved excludes a "wide flat summit". If false, the refuting
family is a near-degenerate polytope whose top facet is l1-wide but d-flat; a refuter
should try a product/prism construction (clone-invariant, so cloning alone cannot make it
— the flat needs genuinely distinct vertices at equal depth).

### L3 — Far-actor deficit visibility (Branch II companion)

**Statement.** There exist universal c_3 > 0, delta_0 > 0 such that for every exact
signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set, hidden top v of
height H > 16*tau, and every row f with ||p_f - p_v||_1 >= 4*tau and d_f > H - 8*tau,
some top support functional phi at v has H - phi(p_f) >= c_3 * tau.

**May consume:** lem-top-deficit-price (existence/duality mechanics of phi),
lem-hiddenness-dual-witness (far-set geometry), first-principles l1/l-infty duality.
**Mechanism.** f is rho-far from v but nearly as deep: the candidate phi is the support
functional at v RE-CENTRED along the segment [p_v, closest point of C_W]; because
||p_f - p_v||_1 >= 4*tau, either phi already sees f at deficit >= c_3*tau, or f sits
within the "vertical cylinder" over the summit, in which case a tilted functional
phi_t = (1-t)*phi + t*psi_f (psi_f the 1-Lipschitz functional realizing
||p_f - p_v||_1 at f) can trade O(t*H) of height for a t*4*tau deficit at f; the
quantitative claim is that some legal tilt keeps phi_t in Phi while granting c_3*tau.
**Grade:** MEDIUM (a concrete two-functional convexity computation; no new objects).
**Risk note:** the tilt may leave Phi (phi_t(p_v) = H requires psi_f(p_v) = H — false in
general; the fix is an affine correction that may cost the "<= 0 on C_W" constraint).
If unfixable, L3 weakens to "H - phi(p_f) >= c_3*tau OR f is within 4*tau of the summit
axis", and L2 must absorb the second horn — flag this as the L2/L3 seam risk. A refuting
family: f directly "above" C_W at distance 4*tau sideways from v with the same closest
point — check whether l1 geometry (not Euclidean) actually permits d_f > H - 8*tau there;
at a >= 16 the depth band is narrow, which is what c_3 buys.

### L4 — Zero-face capacity kill (Branch I, Q4-true)

**Statement.** For an exact signed idempotent P with delta(P) > 0, a hidden geometrically
distinct row vertex u, an optimal exposer h* at u, a row z with h*(p_z) = 0, and c_r > 0
with sum_{j : h*(p_j) >= kappa} max(P_zj, 0) >= c_r: delta >= (c_r/4)^2... stated
single-sentence: under the listed hypotheses, c_r * kappa <= nu_z <= delta.

**May consume:** lem-affine-exposer-row-capacity (at i = z, h = h*, eta = kappa,
F = {j : h*(p_j) >= kappa}); lem-harmonic-affine-bridge (already inside that shard).
**Mechanism.** h* is admissible at z (h*(p_z) = 0, 0 <= h* <= 1 on all rows), so the
capacity shard applies verbatim: kappa * (positive z-mass on the kappa-high slab) <= nu_z.
With the Q4 mass hypothesis: c_r * tau/4 <= delta = tau^2, impossible for
tau < c_r/4, i.e. delta < (c_r/4)^2.
**Grade:** EASY-DERIVATION (verbatim composition of one proved shard).
**Risk note:** none of substance; the one contract point to check is that
lem-affine-exposer-row-capacity's hypothesis "h(p_i) = 0 and 0 <= h(p_j) <= 1 for all
rows" is exactly what h* gives at the zero-face row z (it is: z is on the zero face of an
ADMISSIBLE exposer). Boundary delta = (c_r/4)^2 is excluded by taking delta_0 strictly
smaller.

### L5 — Far-deep deficit for a chosen phi (Branch I, Q5-true)

**Statement.** There exist universal c_5 > 0, delta_0 > 0 such that for every exact
signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set, hidden top v with
H > 16*tau, and every index set A contained in {j : ||p_j - p_v||_1 >= 4*tau,
d_j > H - 8*tau} with sum_{j in A} max(P_vj, 0) >= c_m: some top support functional phi
has sum_{j in A} max(P_vj, 0) * (H - phi(p_j)) >= c_5 * tau * c_m.

**May consume:** lem-top-deficit-price (pairing legality), L3's mechanism (if L3 lands,
L5 is its mass-weighted corollary via averaging phi over the rows of A: for each f in A
pick phi_f with z >= c_3*tau, average over the a^+-weighted distribution — averaging is
legal by Phi's convexity, and the averaged functional sees >= c_3*tau/|support|... the
honest single-phi form needs the minimax/LP-duality step: max_phi min-type exchange).
**Mechanism.** Two routes: (i) corollary of L3 + a minimax step (sup over phi of the
a^+-weighted deficit is a concave-in-phi maximization over the convex compact Phi; its
value >= the a^+-average of per-row guarantees by choosing phi against the mass
distribution — von Neumann-type exchange on a bilinear pairing); (ii) direct: rho-far
PLUS deep leaves only a 8*tau-wide depth annulus at l1-distance >= 4*tau — a dimension
count-free cone argument bounds how much of that annulus can be z-flat for the OPTIMAL
phi.
**Grade:** MEDIUM (route (i) is standard given L3; the minimax step is textbook
finite-dimensional).
**Risk note:** the minimax exchange needs the pairing bilinear and Phi compact convex —
both true (Phi is cut out by finitely many affine constraints + 1-Lipschitz, compact in
the relevant finite-dimensional restriction to the affine row hull). Honest flag: if L3
fails, route (ii) alone is HARD; L5 inherits L3's risk. If both fail, Q5-true merges into
the L6 configuration and the tree survives with L6 covering more ground (see 4, Step C3).

### L6 — Huddle exchange starvation (Branch I creative core)

**Statement.** There exist universal c_r in (0,1), c_m in (0,1), theta_0 in (0,1),
delta_0 > 0 such that no exact signed idempotent P with 0 < delta(P) <= delta_0 and
nonempty visible set has a hidden top v with H > 16*tau, heaviness
sum_{C(v)} P_vj^+ >= 1 - theta_0 (a = 16), a deepest mass-carrying cluster vertex u with
t*(u) > 0, disjoint always-tight hulls, every always-tight zero-face row z at u keeping
sum_{j : h*(p_j) >= kappa} max(P_zj, 0) < c_r, and
sum over {j : ||p_j - p_v||_1 >= 4*tau, d_j > H - 8*tau} of max(P_vj, 0) < c_m.

**May consume:** lem-separator-zero-face-obstruction (the harmonic psi + blocker z_0),
lem-zero-face-exchange-identity (the exact ledger at every zero-face row),
lem-zero-face-localization, lem-zero-face-vertex-support, lem-always-tight-dual-support,
lem-hiddenness-dual-witness (at u), lem-hiddenness-depth-markov (at v),
lem-cs-low-slab-pincer, lem-cluster-return-flow, lem-harmonic-line-coordinate-row-balance,
lem-signed-carre-du-champ.
**Mechanism.** The harmonic direction psi from the separator lemma satisfies P psi = psi,
psi(p_u) = 0, psi > 0 on T(u), psi < 0 on O(u), psi(p_{z_0}) < 0. Apply the harmonic
row-balance (lem-harmonic-line-coordinate-row-balance) at u and at z_0: the psi-ledger of
each huddle row must balance to O(nu * ||psi||). But T(u) is rho-FAR from u (far family)
with psi > 0 there, while the huddle (u, w, zero-face rows, and — by NOT-Q5 — at least
1 - theta_0 - c_m of v's mass) is confined rho-near where psi is O(sign-mixed small);
u's own witness balance (lem-hiddenness-dual-witness at u:
sum lambda_f (p_f - p_u) + sum alpha_i (p_i - p_u) = sum beta_i (p_i - p_u)) forces
lambda-mass ON T(u) (lem-always-tight-dual-support), i.e. genuinely far rows must
RECEIVE the huddle's displacement — and the return-flow inequality
(lem-cluster-return-flow with C = the rho-ball of v, r = 8*tau, s_v >= 1 - theta_0 - c_m
- shallow corrections) forces out-of-cluster positive mass weighted by RETURN fractions
>= s(1-s) - O(tau), which at s close to 1 is small — the starvation: the far rows T(u)
are dual-REQUIRED (they carry lambda) but primal-STARVED (no positive coefficient mass
reaches them from the huddle, by NOT-Q4 + NOT-Q5 + heaviness), and the exchange identity
at each zero-face row (lem-zero-face-exchange-identity: kappa-high intake is paid
coin-for-coin by nu_z <= delta) caps the only remaining payment channel. The
contradiction target: the T(u)-rows' own row reproduction cannot be sustained — they sit
at depth > H - (1/2+delta)*tau (lem-rank3-supporting-functional-pinning's co-top forcing
is the rank-3 template; the rank-free version is the creative step) while receiving no
positive mass from below.
**Grade:** HARD-CREATIVE (the assembly's deepest leaf; this is the huddle charge proper,
localized to a maximally rigid configuration: everything trapped, all budgets active).
**Risk note:** MOST LIKELY FALSE-OR-UNPROVABLE-AS-STATED of the seven. The gap between
"dual-required" and "primal-starved" is exactly the lambda-vs-P^+ coupling that
conj-min-a-w4 names as open; L6 bets that in the MAXIMALLY constrained leaf (all other
exits closed by Q2-Q5 false) the coupling is forced through the harmonic psi's exact
P-invariance (psi is an eigenvector, so sum_j P_fj psi_j = psi_f at EVERY far row f —
a row-level identity, not a witness comparison; this is what no previous attempt used).
A refuter attacks by constructing a self-sustaining far web: rows in T(u) exchanging
psi-value among themselves without huddle payment. The psi-balance does not obviously
forbid that; L6's proof must show the far web's psi-values are pinned ABOVE the huddle's
(psi > 0 on T) so self-exchange cannot balance against psi(p_u) = 0 without negative
mass >= c*t*(u)*... — if that constant degrades with t*(u) -> 0, L6 FAILS (t* can be
arbitrarily small); the repair would need the t*-free blocker clause psi(p_{z_0}) < 0.
FLAG: any L6 proof whose constant divides by t*(u) is dead on arrival.

### L7 — The w-recursion cap (Branch I companion)

**Statement.** There exists universal delta_0 > 0 such that for every exact signed
idempotent P with 0 < delta(P) <= delta_0, nonempty visible set, hidden top v with
H > 16*tau, and every chain v, u_1, u_2, u_3 of geometrically distinct row vertices with
||p_{u_1} - p_v||_1 < 4*tau, ||p_{u_{k+1}} - p_{u_k}||_1 < 4*tau, each u_k hidden with
t*(u_k) > 0 and disjoint always-tight hulls at u_k: some u_k (k <= 3) has an always-tight
zero-face row z with sum_{j : h*_k(p_j) >= kappa} max(P_zj, 0) >= c_r.

**May consume:** lem-disjointness-huddle-reduction (re-applied at u_k),
lem-zero-face-localization (chain confinement: each hop < 4*tau, all within 12*tau of v),
lem-ball-cluster-exposure-void, lem-zero-face-vertex-support, lem-top-witness-third-actor.
**Mechanism.** Each disjoint-hull vertex spawns its own huddle partner one level deeper
in the localization budget (depths H - 4*tau, H - 8*tau, H - 12*tau by iterated
lem-zero-face-localization); the third-actor lemma at each level forces rho-far witness
mass at matching depth; after three nested applications the combined far-actor system
must straddle the 4*tau exemption ball of SOME chain member (pigeonhole on the l1-ball
packing at scale 4*tau inside a 12*tau ball is NOT the mechanism — that would be
dimension-dependent counting; the legal mechanism is the depth budget: the third hop's
forced far actor at depth > H - 12*tau is rho-far from u_3 but within 12*tau + 4*tau of
v, and its OWN exposer relation to u_1's h* forces the kappa-high shipping that Q4-false
denies — a value-monotonicity argument along the chain, not a count).
**Grade:** MEDIUM (mechanical iteration of proved shards + one monotonicity argument;
flagged because the final step is sketched, not proved).
**Risk note:** the chain could be indefinitely extensible in principle (nothing proved
caps chain length; depth only degrades by 4*tau per hop and H/tau > 16 allows 4 hops).
L7 as stated caps at k <= 3 by choosing a = 16; if the monotonicity step fails, the
repair is to raise a (more hops available — but then the pigeonhole temptation returns:
AVOID counting, keep the value-monotonicity form). If neither works, L7 collapses into
L6's configuration with a longer chain, and L6 must be proved chain-length-uniformly —
flag as the L6/L7 seam risk.

---

## 4. THE ASSEMBLY IMPLICATION

**Claim.** L1 AND L2 AND L3 AND L4 AND L5 AND L6 AND L7 imply THE PINNED TARGET
(Section 1), with the constant order fixed in G8 below.

**G8 constant discipline (fix FIRST, in this order; each choice depends only on earlier
ones).**
1. a := 16 (halo width; ensures H > 16*tau > 8*tau so every huddle shard fires, and
   allows the 3-hop chain of L7 with 4*tau depth loss per hop staying > 4*tau deep).
2. c_m := 1/4 (the mass threshold of Q2/Q3/Q5; any value in (0, 1/2) works — it enters
   only L1's charge and the NOT-side mass bookkeeping).
3. c_r := 1/2 (the shipping threshold of Q4; enters L4's charge and L6/L7's hypotheses).
4. c_w := 6 (the far-slab constant of lem-bounded-alpha-forced-far-slab at A_0 = 0:
   needs c_w > 1/2 + delta_0 + 4; 6 > 4.75 for every delta_0 <= 1/4). A_0 := 0 in
   Branch II (supplied by the intersection horn); Branch I does not use A_0.
5. c_3, c_5 := the universal constants delivered by L3, L5 (existence is their content;
   the assembly only needs them > 0).
6. theta_0 := 1/8 (heaviness slack; needs theta_0 + c_m < 1/2 so that
   1 - theta_0 - c_m >= 5/8 > 1/2 survives as trapped mass in Step C3; 1/8 + 1/4 = 3/8).
7. delta_0 := min over the finitely many leaf ceilings:
   delta_0 <= min{ 1/4,
                   (c_m/3)^2                    [L1's charge, Step B1/C2],
                   (c_r/4)^2 / 2                [L4's charge, Step C1 — strict],
                   (c_5 * c_m / 3)^2            [L5's charge, Step C2],
                   delta_0(L2), delta_0(L3), delta_0(L6), delta_0(L7) }.
   Every entry is a universal positive number once L2/L3/L6/L7 exist; delta_0 > 0.
This order is FEASIBLE: no entry refers to a later-chosen constant; L2/L3/L6/L7's
internal constants are existentially quantified in their statements and consumed only
through delta_0 and the fixed (a, c_m, c_r, theta_0).

**Step A0 (the root object u exists).** Assume for contradiction (P, v) is a
counterexample: 0 < delta <= delta_0, W != {}, v a hidden top with H > 16*tau, and
sum_{j in C(v)} a_j^+ >= 1 - theta_0 with C(v) = {j : ||p_j - p_v||_1 < 4*tau,
d_j > 16*tau}. Fix a vertex representation of every row over geometrically distinct row
vertices (lem-genuine-disintegration's fixed representation; its hypothesis
G_a != {} holds since C(v) != {} — heaviness with theta_0 < 1 forces a member — and
0 < delta <= 1/4). Every j in C(v) has d_j > 16*tau, so by that shard's S3.3 clause each
such row's representation puts weight >= (d_j - 16*tau)/(H - 16*tau) > 0 on vertices of
depth > 16*tau; hence SOME geometrically distinct row vertex u' at depth > 16*tau
receives positive disintegrated weight from C(v)-mass. Each such u' lies rho-near some
C(v) row... [correction: nearness of u' to v is needed. Use instead: each C(v) row j is
itself within 4*tau of v; its representing vertices with h-depth > 16*tau need not be
rho-near v. To keep the tree sound we take u among the MASS-CARRYING CLUSTER VERTICES in
the direct sense: u a geometrically distinct row vertex with p_u in the closed rho-ball
of v, d_u > H - 4*tau, receiving positive a^+-mass from row v or being a vertex of some
C(v) row's representation within the ball. Existence: v itself is such a vertex if
P_vv > 0; in general, at least one vertex in the rho-ball of v carries C(v)-mass because
C(v)-rows are rho-near v and decompose onto vertices, and lem-zero-face-localization-type
confinement is NOT available for arbitrary rows — so we PIN the fallback: if NO
geometrically distinct row vertex in the rho-ball of v other than possibilities with
t* = 0 carries mass, then all C(v)-mass rows are convex combinations of vertices OUTSIDE
the ball, and lem-received-mass-proximity at row v with A = C(v)
(sigma_A >= 1 - theta_0) puts p_v within (2+4*delta)(theta_0 + 2*delta) < 4*tau...
of conv{p_j : j in C(v)} — consistent, no contradiction; hence the honest existence
route is: u := v itself when t*(v) > 0, else the t*(v) = 0 top. See Step A1.]

**Step A1 (dichotomy on t*(v); the t* = 0 escape closed).** Since v is hidden,
t*(v) < kappa. Case t*(v) > 0: take u := v. Then u is a hidden geometrically distinct
row vertex, trivially within 4*tau of v, mass-carrying (row v reproduces itself), with
t*(u) > 0: the tree's root object exists with u = v — this is the DEEPEST possible
choice (d_u = H). Case t*(v) = 0: every admissible exposer h at v has
min_{far} h(p_f) <= 0, i.e. h vanishes somewhere on F_v... then the exposedness LP's
optimal value is 0 and by lem-always-tight-dual-support O(v) may be empty; the huddle
machinery needs t* > 0. Closure of this case: t*(v) = 0 means for EVERY admissible h at
v some rho-far row has h(p_f) = 0 (the LP optimum is attained, finitely many
constraints); apply lem-zero-face-localization to v: any row z with h*(p_z) = 0 for an
optimal exposer h* at v satisfies ||p_z - p_v||_1 < 4*tau — but the far row f has
||p_f - p_v||_1 >= 4*tau, CONTRADICTION unless the optimal-face machinery degenerates;
hence t*(v) = 0 is impossible for a hidden vertex with F_v != {} whose zero face is
rho-localized. [FLAG-A1: lem-zero-face-localization's contract is stated for a HIDDEN
vertex u and an optimal exposer h*; at t*(v) = 0 the "optimal exposer" is h = 0 or any
feasible h with objective 0, and the localization proof (far rows have h* >= t*) gives
h* >= 0 on far rows — vacuous, NOT a contradiction. The honest closure is different:
at t*(v) = 0, the always-tight far family T(v) consists of far rows with h(p_f) = 0 for
ALL admissible h; each such f is a zero-face row of every optimal exposer, and
lem-zero-face-localization's FIRST clause (h*(p_z) = 0 => rho-near) applies to
NON-degenerate optimal exposers only when t* > 0 is not required by its contract — the
shard contract says "hidden geometrically distinct row vertex u, optimal exposer h* at
u, row z with h*(p_z) = 0 => ||p_z - p_u||_1 < 4*tau" with NO t* > 0 hypothesis. Reading
the contract literally, t*(v) = 0 forces a far row f in the zero face of the optimal
exposer, and the contract yields ||p_f - p_v||_1 < 4*tau, contradicting f in F_v. So
Case t*(v) = 0 is VOID by lem-zero-face-localization alone — but a verifier MUST check
that shard's proof covers the t* = 0 boundary (its mechanism note says "far rows have
h* >= t* by the LP far constraints, so h* = 0 forces rho-nearness" — at t* = 0 this
gives h* >= 0, which does NOT force rho-nearness. HONEST STATUS: the t*(v) = 0 case is
an UNPATCHED PINHOLE in this assembly; it must either be absorbed into L6's hypotheses
(drop t*(u) > 0, work with the degenerate LP) or closed by a one-line lemma "a hidden
top has t*(v) > 0" — plausibly provable from lem-hiddenness-dual-witness's O-nonemptiness
iff t* > 0 clause plus the witness balance, but NOT proved here. Registered below as the
assembly's known gap AG-1.]

**Step B (Branch II: NOT-Q1 — hulls intersect at u).**
B1. If Q2 or Q3 holds: L1 applies (with phi or phi-bar) and yields
    c_m * tau <= delta*(2+4*delta) <= 3*delta = 3*tau^2, i.e. tau >= c_m/3,
    contradicting delta_0 <= (c_m/3)^2 (strictly below: delta <= delta_0 and the
    inequality chain is strict at the boundary since lem-top-deficit-price's
    conclusion is <=, and c_m*tau <= 3*tau^2 with tau < c_m/3 is already
    impossible — take delta_0 < (c_m/3)^2 strictly, absorbed in G8's "min/2" slack).
    Branch closed.
B2. If NOT-Q2 and NOT-Q3: the L2 + L3 configuration. NOT-Q1 gives the alpha-free
    reduced optimal display at u (lem-optimal-face-conic-reduction, t*(u) > 0), i.e. a
    small-beta witness of u with alpha = 0; lem-bounded-alpha-forced-far-slab at
    (A_0, c) = (0, c_w = 6) applies: u hidden (R1) and not exposed, so it forces a row
    f_u with ||p_{f_u} - p_u||_1 >= 4*tau and d_{f_u} >= H - 6*tau. L3 (at the 8*tau
    band: 6 < 8 so f_u qualifies... f_u is rho-far from u, not necessarily from v —
    if ||p_{f_u} - p_v||_1 < 4*tau then f_u is itself cluster-confined and becomes
    part of L2's plateau; if >= 4*tau, L3 applies to f = f_u) delivers phi with
    z_{f_u} >= c_3*tau, and L2 excludes the residual plateau configuration outright:
    L2's hypothesis list is exactly {tall, heavy is not even needed, deepest
    mass-carrying u with intersecting hulls, plateau under every phi} = the NOT-Q2 and
    NOT-Q3 data. Contradiction by L2. (L3's role is embedded: L2's mechanism consumes
    the far actor that B2 plants; if L2 is proved WITHOUT needing L3, L3 may be
    dropped — kept as a separate leaf because L2's author will want it as a module.)
    Branch closed.

**Step C (Branch I: Q1 — hulls disjoint at u).**
C0. lem-disjointness-huddle-reduction fires (H > 16*tau > 8*tau; u geometrically
    distinct, within 4*tau of v — for u = v the within-4*tau condition is trivial
    [FLAG-C0: the shard's hypothesis says "a geometrically distinct row vertex u with
    ||p_u - p_v||_1 < 4*tau"; whether u = v itself is a legal instantiation must be
    checked against its proof — its chain runs through lem-ball-cluster-exposure-void
    which is stated for vertices IN the ball cluster of v, and v is in its own ball
    cluster (distance 0 < 4*tau); the depth conclusion d_u > H - 4*tau is trivial at
    u = v. A verifier should confirm no step of the shard requires p_u != p_v;
    lem-zero-face-vertex-support's clause "u within 4*tau of a hidden top" likewise
    admits u = v on its face]): outputs the huddle partner w (geometrically distinct
    from u, ||p_w - p_u||_1 < 4*tau, d_w > H - 8*tau, hidden), the relative-interior
    optimal exposer h* at u, the harmonic psi and the nonclone blocker z_0 with
    h*(p_{z_0}) = 0 (lem-separator-zero-face-obstruction).
C1. If Q4 holds (some always-tight zero-face row z ships >= c_r positive mass to
    {h* >= kappa}): L4 gives c_r*kappa <= nu_z <= delta, i.e. c_r*tau/4 <= tau^2,
    i.e. tau >= c_r/4 — contradicting delta_0 < (c_r/4)^2 (G8 entry 7 keeps strict
    slack). Branch closed.
C2. If NOT-Q4 and Q5 (v places >= c_m positive mass rho-far and deep,
    A = {j : ||p_j - p_v||_1 >= 4*tau, d_j > H - 8*tau}, sum_A a_j^+ >= c_m):
    L5 delivers phi with sum_A a_j^+ * z_j >= c_5*c_m*tau; lem-top-deficit-price (R4,
    the subset clause at this A) gives sum_A a_j^+ z_j <= delta*(2+4*delta) <= 3*tau^2;
    hence c_5*c_m*tau <= 3*tau^2, i.e. tau >= c_5*c_m/3, contradicting
    delta_0 < (c_5*c_m/3)^2. Branch closed.
C3. If NOT-Q4 and NOT-Q5: the maximal-rigidity configuration. Verify L6's hypothesis
    list item by item: tall (root), heavy at theta_0 = 1/8 (root), u deepest
    mass-carrying with t*(u) > 0 (A0/A1), disjoint hulls (Q1), every always-tight
    zero-face row keeps < c_r kappa-high mass (NOT-Q4), rho-far deep mass < c_m
    (NOT-Q5). That is EXACTLY L6's antecedent; L6 says no such P exists.
    Contradiction. L7's role: L6's proof is permitted to assume the huddle chain
    terminates within 3 hops — if instead its internal argument re-encounters a
    disjoint-hull vertex u_2 in w's own anatomy, L7 guarantees that within 3 chain
    steps SOME chain member violates NOT-Q4's shipping bound, i.e. Q4 fires at u_k
    and C1's arithmetic (which is vertex-independent: c_r*kappa <= nu_{z} <= delta)
    closes it. So C3 is closed by L6 with L7 as its chain-termination subroutine.
    Branch closed.

**Step D (conclusion).** Steps B and C exhaust S1 (Q1 or NOT-Q1); within each, the
threshold splits are exhaustive with boundaries owned as declared (Section 2). Every
leaf ends in a contradiction with delta <= delta_0 as fixed in G8. Hence no
counterexample (P, v) exists: THE PINNED TARGET holds with
(a, theta_0, delta_0) = (16, 1/8, G8-entry-7). QED-modulo-leaves, with two REGISTERED
assembly gaps that are part of this deliverable's honest interface:
  AG-1 (Step A1): the t*(v) = 0 hidden-top case is not cleanly closed by any cited
       contract; needs the one-line lemma "hidden top => t*(v) > 0" or an L6 hypothesis
       relaxation. Until discharged, the target is proved only for counterexamples
       whose top (or SOME mass-carrying cluster vertex, if the u != v existence route
       is repaired) has t* > 0.
  AG-2 (Step C0): u = v instantiation legality of lem-disjointness-huddle-reduction
       (geometric distinctness is a property of the vertex, not of the pair, so the
       contract reads as legal — but the shard's internal chain must be audited for a
       hidden p_u != p_v use).
Both AG's are auditing tasks against existing proved shards, not new mathematics; they
are NOT leaves because their resolution is a contract reading, but a hostile verifier
should treat them as potential holes until the audit lands.

---

## 5. COVERAGE CHECK AGAINST THE W52 DATA

(Evidence of non-vacuity ONLY — no numerical fact is a proof step anywhere above.)
The four named W52 families and which branch/leaf would have blocked their entry into
the tall heavy class:

1. **HA_t / HA_eps (delta-inflation families):** as the perturbation pushed toward
   H^2/delta > 16, delta grew because the deep row's top-deficit mass stayed z-visible —
   this is exactly the L1 charge (Q2-true, Branch II): the mass never reached the blind
   rho-ball, so lem-top-deficit-price priced it and delta inflated. Leaf L1.
2. **Deep-append-turns-visible family (the B2 constraint):** the appended deep row,
   pushed far enough to be a cluster candidate, acquired exposedness — in tree terms the
   configuration failed to produce a hidden mass-carrying u at all; this is Step A0/A1
   failing FOR the counterexample (no root object), i.e. the tree's hypothesis space was
   never entered. Consistent with lem-ball-cluster-exposure-void: entry requires
   H > 4*tau FIRST, which the family never achieved.
3. **TOP-preserving reversion family (hulls intersect on every in-class approach):**
   the restored top/top-cluster behaviour forced K_T cap K_O != {} — Branch II; the
   family died by delta inflation before tallness, matching B2's composition (the
   alpha-free witness + forced far slab + L1/L2 pricing). Branch II, leaves L1/L2.
4. **Best disjoint frontier (delta = 4239/80000, H^2/delta ~ 0.228, gap-hat = 1/1939,
   reach-hat = 3/58000, A_min ~ 9.97):** genuinely disjoint hulls (Branch I) but at
   H << 4*tau — the huddle shards' H > 8*tau trigger never armed; in-tree this instance
   never satisfies the root's tallness. Its measured anatomy (tiny reach, bounded A_min)
   is the L6 configuration's SHALLOW shadow: the tree explains why it stalls — pushing
   H up while keeping disjointness would have to keep NOT-Q4/NOT-Q5 (else L4/L5-style
   pricing inflates delta), and the exact experiment saw precisely that stall.

A decomposition that could not in principle explain the data would be suspect; each
family above lands in a distinct branch, and no family lands in "uncovered space".

---

## 6. HONEST ASSESSMENT

**Most likely false / hardest leaves.**
- **L6 (huddle exchange starvation)** — the single most at-risk leaf: it is the huddle
  charge proper, localized. The dual-required/primal-starved coupling it needs is the
  named open lambda-vs-P^+ comparison (conj-min-a-w4's gap). Its one genuinely new
  resource is the row-level P-invariance of the separator direction psi (an exact
  eigen-identity at every far row, never exploited in W26-W53). If L6's constant
  degrades as t*(u) -> 0 it is dead as stated (see its risk note). A refuter attacks L6
  FIRST, with a self-sustaining far-web construction.
- **L2 (summit-plateau exclusion)** — HARD-CREATIVE; could be false if a d-flat,
  l1-wide summit facet exists. The averaging-over-phi axis is untested mathematics.
  A refuter attacks it SECOND, with a wide-flat-summit family.
- **L3/L5** — MEDIUM but with a real seam: L3's tilt construction may not stay inside
  Phi; L5 inherits L3. Their failure does not break exhaustiveness (the configurations
  fall through to L2/L6 respectively) but fattens the two creative leaves.

**What a refuter attacks first overall:** L6, then L2, then the assembly pinholes AG-1
(t* = 0 top) and AG-2 (u = v instantiation) — the two registered contract-audit gaps.

**Parallelizable now (independent inputs, no shared unproved deps):**
- L1 and L4: near-mechanical corollaries of lem-top-deficit-price /
  lem-affine-exposer-row-capacity — one codex prover each, prime af-elevation shape.
- L3: self-contained two-functional convexity problem (only first-principles duality +
  the phi-existence mechanics). Independent of everything else.
- L7: iteration of proved shards + one monotonicity step; independent of L2/L6.
- AG-1/AG-2: contract audits, dispatchable immediately as verifier tasks.
- L2 and L6 are the two creative frontiers; they share no hypothesis (different S1
  sides) and can run in parallel, but each should get the strongest (Fable-grade)
  prover. L5 should WAIT for L3's verdict.

**Pruned branches (considered, dropped, one line each):**
- Split on "w itself carries heavy cluster mass" (recursion on the huddle partner):
  subsumed by the deepest-vertex extremal choice at the root + L7's chain cap.
- Split on sign structure of P_vj on far actors (positive vs negative): folded into
  Q5's a^+-only phrasing; the negative-mass side is globally capped by nu_v <= delta
  and needs no case of its own.
- Split on the exchange-identity budget at the huddle (lem-zero-face-exchange-identity
  as its own predicate): absorbed into Q4 — the kappa-high shipping threshold is the
  operative form of the same ledger.
- A rank-3-first branch via conj-rank3-cluster-zero-face-reach: deliberately EXCLUDED
  from this tree (conjectures may appear only as leaves, and the rank-3 reach closer is
  already codified as the (iii) handle; this tree is the rank-free attack, and its
  Branch-I leaves L4/L6/L7 are the rank-free generalizations of what the rank-3 anatomy
  chain proves rigidly in the plane).

**Relation to the codified handles (consistency check):** L1+L2+L3 jointly IMPLY the
(i) handle conj-top-deficit-coupling's role on Branch II (they manufacture the Z_v(phi)
>= c*H lower bound or exclude the configuration outright); L6+L7 are a sharpened,
localized form of the (ii) web-incompatibility (GAP-B2-2) that VB2 demanded be stated
jointly with the bounded-alpha input — here the alpha input is REPLACED by the
intersection horn (A_0 = 0) on Branch II and by the zero-face shipping threshold c_r on
Branch I, so conj-tall-bounded-alpha is NOT a dependency of this tree (a deliberate
de-risking: the alpha-blow-up escape is confined to Branch I where the blocker geometry,
not an alpha bound, does the work).

# PART B — the repair delta (v2 + v3 amendment; verifier-prescribed)

<!--
ROLE: W54 decomposition REPAIR DELTA (v2) — applies the V-ASM verifier-prescribed
corrections to decomposition.md. Everything not restated here is UNCHANGED from
decomposition.md. The repairs below are VERBATIM implementations of V-ASM findings
1, 3, 4, 5, 10 (see v-asm/VERDICT.md); no new mathematical ideas are introduced by the
orchestrator. STATUS: AUTHOR artifact, re-verification pending (V-ASM-2).
-->

# Decomposition v2 delta (repairs R1-R3 per V-ASM)

## R1 — Re-root the tree at u := v (fixes V-ASM findings 1, 2, 5; uses finding 7 = AG-2 resolved)

The root object selection in §2 N0 is REPLACED by:

> **N0-v2 (root).** The counterexample configuration is (P, v) with v the pinned hidden
> top (tall, heavy). Set **u := v**. By Step A1 (t*-dichotomy) we may assume t*(v) > 0
> [the t*(v) = 0 case is closed at CONTRACT level: if t*(v) = 0 then h = 0 is an optimal
> exposer at v, and lem-zero-face-localization's first clause (every row z with
> h*(p_z) = 0 is rho-near u) applied at h* = 0 makes EVERY row rho-near v, contradicting
> F_v nonempty (lem-hiddenness-dual-witness, v hidden). CAVEAT (V-ASM AG-1 audit): the
> localization shard's recorded mechanism degenerates at t* = 0; a shard-proof audit
> (dispatched as W54-R4) must confirm its contract covers the boundary before this
> closure is trusted]. All splits S1/S4/S5 and all leaf hypotheses are evaluated AT v:
> the hull geometry, zero-face families, and exposers are those of the exposedness LP at
> the top v itself. The u = v instantiation of the entire huddle chain is contract-legal
> (V-ASM finding 7 / AG-2: no dependency requires p_u != p_v; the output w satisfies
> p_w != p_v). The phrases "deepest mass-carrying cluster vertex" are STRUCK everywhere;
> deepness is automatic (d_v = H) and mass-carrying is not needed by any assembly step.

Leaf statements L2 and L6 are restated accordingly:

> **L2-v2 (summit-plateau exclusion).** There exist universal c_m in (0,1), delta_0 > 0
> such that no exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible
> set, and hidden top vertex v of height H > 16*tau has, simultaneously: t*(v) > 0; the
> always-tight hulls at v INTERSECT; for every top support functional phi,
> sum_{j : H - phi(p_j) < tau} max(P_vj, 0) > 1 - c_m; and for every average phi-bar of
> at most 3 top support functionals, sum_{j : H - phi-bar(p_j) >= tau} max(P_vj, 0)
> < c_m/4.

> **L6-v2 (huddle exchange starvation).** There exist universal c_r in (0,1), c_m in
> (0,1), theta_0 in (0,1), delta_0 > 0 such that no exact signed idempotent P with
> 0 < delta(P) <= delta_0 and nonempty visible set has a hidden top v with H > 16*tau,
> heaviness sum_{C(v)} P_vj^+ >= 1 - theta_0 (a = 16), t*(v) > 0, DISJOINT always-tight
> hulls at v, every always-tight zero-face row z at v keeping
> sum_{j : h*(p_j) >= kappa} max(P_zj, 0) < c_r, and
> sum_{j : ||p_j - p_v||_1 >= 4*tau, d_j > H - 8*tau} max(P_vj, 0) < c_m.

(Note for the L6 prover in flight on the v1 statement: v1's extra hypotheses "deepest,
mass-carrying" may NOT be used — if its proof consumes them, the proof must be adapted
or re-run against L6-v2. The harvest step will audit this.)

## R2 — Q3 restated clone-invariantly at the c_m/4 mass threshold (fixes findings 3, 10)

> **Q3-v2:** "there exist phi_1, ..., phi_k in Phi, k <= 3, whose average phi-bar
> satisfies sum_{j : H - phi-bar(p_j) >= tau} max(P_vj, 0) >= c_m/4."
> Boundary: equality belongs to Q3-v2 (the charged side).

Step B1-v2: if Q2 holds, apply L1 at (m, L) = (c_m, tau); if Q3-v2 holds, apply L1 at
(m, L) = (c_m/4, tau) with phi-bar (legal: L1 covers finite convex averages). The
charge yields c_m*tau <= 3*tau^2 resp. (c_m/4)*tau <= 3*tau^2, contradictions for
tau < c_m/3 resp. tau < c_m/12.

## R3 — Strict boundary slack in G8 entry 7 (fixes finding 4)

> **G8 entry 7-v2:** delta_0 := (1/2) * min{ 1/4, (c_m/3)^2, (c_m/12)^2 [Q3-v2 charge],
> (c_r/4)^2, (c_5*c_m/3)^2, delta_0(L2), delta_0(L3), delta_0(L6), delta_0(L7) }.
> The factor 1/2 makes every charge ceiling STRICT at delta = delta_0, killing the
> closed-boundary escape of V-ASM finding 4 uniformly.

## Unchanged

Splits S1/S2/S4/S5 (with u = v), leaves L1/L3/L4/L5/L7 (their statements never used
"deepest mass-carrying"), Steps B2/C0/C1/C2/C3 (with u = v substituted and, in C3, the
L6-v2 hypothesis list — the item-by-item check now reads: tall, heavy, t*(v) > 0 (A1),
disjoint hulls at v (Q1), NOT-Q4, NOT-Q5 — no mass-carrying item remains), Step D, §5, §6.

## R5 (v3 amendment) — G8 constant synchronization (V-ASM-2 finding 1, applied verbatim)

G8 is re-ordered so the EXISTENTIAL leaf constants are read FIRST, and the split
thresholds are then chosen by monotonicity (shrinking c_m, c_r, theta_0 only STRENGTHENS
the L2-v2/L6-v2 antecedents, so the smaller values remain legal):

> **G8-v3.** Let L2-v2 supply (m_2, d_2) and L6-v2 supply (r_6, m_6, th_6, d_6). Set
>   c_m := (1/2)*min{1/4, m_2, m_6},
>   c_r := (1/2)*min{1/2, r_6},
>   theta_0 := (1/2)*min{1/8, th_6, 1/2 - c_m}.
> Then, after L3/L5/L7 deliver their constants (c_3, c_5, delta_0(L3), delta_0(L5),
> delta_0(L7)) at these choices, set
>   delta_0 := (1/2)*min{1/4, (c_m/3)^2, (c_m/12)^2, (c_r/4)^2, (c_5*c_m/3)^2,
>              d_2, d_6, delta_0(L3), delta_0(L5), delta_0(L7)}.
> (delta_0(L5) was previously omitted; now included.)

Merge note (V-ASM-2 finding 2): the stale "deepest mass-carrying" prose in V1's B2/C3 is
STRUCK (already declared in R1); a consolidated v3 must delete the words.

## Assembly status after V-ASM-2 + R4

V-ASM-2: `VERDICT: VALID-WITH-CORRECTIONS — The u := v repair now typechecks modulo the explicit R4 t*(v)=0 audit, but G8 must synchronize c_m, c_r, and theta_0 with the existential leaf constants and must include delta_0(L5).`
(Correction applied above.) R4: `AUDIT: CLAUSE-HOLDS / T*POSITIVE-PROVED — ...` — the
t*(v) = 0 boundary is VACUOUS under the vertex hypotheses (positive-margin lemma,
V-R4 verification in flight); AG-1 discharged modulo V-R4.
