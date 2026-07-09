VERDICT: DECOMPOSED — in the configuration the assembly actually hands to L6 (u = v, per decomposition.md Step A1), L6 reduces through four NEW proved sub-lemmas (L6.1 co-top pinning of BOTH the witness lambda-mass and the zero-face conic a-mass; L6.2 starved-set localization; L6.3 downhill co-top zero-face forcing; L6.4 bounded-oscillation psi-normalization and the two-functional corner trap) to a SINGLE minimal open coupling sub-leaf L6.5, which is exactly the lambda-vs-P+ wall in its sharpest localized form; the psi eigen-identity delivered the pinning structure but not the kill (the internally-reproducing co-top plateau survives every single-functional maximum principle).

<!--
ROLE: W54 leaf L6 attack (AUTHOR artifact; hostile verification pending).
STATUS DISCIPLINE (L0): everything below is AUTHOR-CLAIM except quoted shard
contracts (status: proved, cited by id). L6.1-L6.4 are claimed PROVED (paper
proofs, line-by-line below, awaiting independent review). L6.5 is OPEN
(conjecture-grade) and is the isolated wall. Author: Fable prover, 2026-07-09,
session 13, wave W54, leaf L6.
Dimension-free and clone-invariant throughout: no constant depends on n; all
statements are on row points / geometrically distinct row vertices /
coefficient-mass sums; no raw index counting anywhere.
-->

# W54 / L6 — the huddle exchange starvation leaf

Standing notation (definitions/): P an exact signed idempotent (def-signed-idempotent),
delta = delta(P), tau = sqrt(delta), rho = 4*tau, kappa = tau/4 (def-visible-set),
W = W(P), C_W = conv{p_w : w in W}, d_j = dist_1(p_j, C_W), H = max_i d_i (def-height),
nu_i = row-i negative mass, P_ij^+ = max(P_ij, 0), P_ij^- = max(-P_ij, 0).
For a hidden geometrically distinct row vertex v with 0 < t*(v) < infinity:
T = T(v), O = O(v), Z = Z(v) the always-tight far / upper-box / zero-face families of
the exposedness LP at v (lem-always-tight-dual-support), h* an optimal exposer
(h* = t* on T, h* = 1 on O, h* = 0 on Z, values in [0,1] on all rows, h*(p_v) = 0,
h* >= t* on every rho-far row), K_T = conv{p_f - p_v : f in T},
K_O = t*(v)*conv{p_i - p_v : i in O}, g = dist_1(K_T, K_O).
A "top support functional" phi at a hidden top v of height H: affine, phi(p_v) = H,
phi <= 0 on C_W, 1-Lipschitz for l1 (existence: lem-top-deficit-price contract);
z_j = H - phi(p_j) in [0, 2+4*delta], z_v = 0.
The starved set (NOT-Q5's set): A = {j : ||p_j - p_v||_1 >= 4*tau, d_j > H - 8*tau}.

**The instantiation this attack owns.** The assembly (decomposition.md §4, Steps
A0/A1 and C3) constructs the root object u as follows: "Case t*(v) > 0: take
u := v"; the case t*(v) = 0 is the assembly's registered gap AG-1, NOT part of L6.
Hence the configuration handed to L6 always has **u = v**: the deepest
mass-carrying cluster vertex IS the hidden top itself (distance 0 < 4*tau,
depth d_u = H, mass-carrying since the extremal choice at the root is free and
A1 pins it). Everything below is proved for u = v; the general u != v variant is
discussed in §2.6 (Remark R3) and is NOT consumed by the assembly.

---

## §1 THE SUB-LEAF SYSTEM

**L6.1 (Reduced-witness co-top pinning at the top — PROVED, §2.1).**
For every exact signed idempotent P with 0 < delta(P) <= 1/4 and nonempty visible
set, every hidden top vertex v of height H with t*(v) > 0, every reduced optimal
witness display (lambda, a, gamma) of the exposedness LP at v (lambda, gamma
probability vectors on T(v), O(v); a_z >= 0 on Z(v); as in
lem-optimal-face-conic-reduction), and every top support functional phi at v with
z_j = H - phi(p_j), one has the exact identity and bound
sum_{f in T} lambda_f z_f + sum_{z in Z} a_z z_z = t*(v) * sum_{i in O} gamma_i z_i
<= t*(v)*(2 + 4*delta) < (1/2 + delta)*tau,
with every summand on the left nonnegative.
[No disjointness, no tallness, no heaviness needed. The lambda-clause recovers
lem-tight-far-geography (i) restricted to reduced witnesses; the a-clause — the
zero-face conic mass is co-top — is new.]

**L6.2 (Starved-set localization of the dual requirement — PROVED, §2.2).**
Under L6.1's hypotheses, for every c > 0:
lambda{f in T(v) : ||p_f - p_v||_1 >= 4*tau and d_f > H - c*tau} > 1 - (1/2 + delta)/c
and
sum over {z in Z(v) : d_z > H - c*tau} of a_z > (sum_{z in Z} a_z) - (1/2 + delta)/c;
in particular at c = 4 and delta <= 1/4, MORE THAN 13/16 of the witness's
lambda-mass sits inside the starved set A = {j : ||p_j - p_v||_1 >= 4*tau,
d_j > H - 8*tau}.

**L6.3 (Disjointness forces downhill co-top nonclone zero-face conic mass —
PROVED, §2.3).** Under L6.1's hypotheses with additionally g = dist_1(K_T, K_O) > 0:
every reduced optimal display has sum_{z in Z} a_z > g/(4*tau); for every c > 0 at
least g/(4*tau) - (1/2 + delta)/c of that conic mass sits on rows z that are
simultaneously nonclone (p_z != p_v), rho-near v (||p_z - p_v||_1 < 4*tau),
h*-zero (h*(p_z) = 0), and co-top (d_z > H - c*tau); and for every l1-optimal
separator ell (||ell||_inf <= 1, min_{K_T} ell - max_{K_O} ell >= g) the a-weighted
total displacement is quantitatively downhill:
sum_{z in Z} a_z * ell(p_z - p_v) <= -g.

**L6.4 (Bounded-oscillation psi-normalization and the corner trap — PROVED, §2.4).**
For every exact signed idempotent P with 0 < delta(P) <= 1/4, hidden top v with
t*(v) > 0 and disjoint always-tight hulls (g > 0), there is a legal parameter pair
(ell, m) for lem-separator-zero-face-obstruction with ||ell||_inf <= 1 and
|m| <= 3 + 4*delta, so that psi(p) = ell(p - p_v) - m*h*(p) has row-oscillation
osc(psi) <= 5 + 8*delta, satisfies the shard's full sign structure, and obeys
psi >= min(g/2, g - (7/4)*tau) on T(v); moreover for EVERY row i and all
thresholds s_1, s_2, eta_1, eta_2 > 0:
(a) z_i <= s_1 implies sum_{j : z_j >= s_2} P_ij^+ <= (s_1 + nu_i*(2+4*delta))/s_2;
(b) h*(p_i) <= eta_1 implies sum_{j : h*(p_j) >= eta_2} P_ij^+ <= (eta_1 + nu_i)/eta_2;
(c) at any row r attaining M = max_j psi_j:
sum_j P_rj^+ * (M - psi_j) <= nu_r * osc(psi) <= delta*(5 + 8*delta).
[(a)+(b) = the (z, h*)-corner trap: every co-top h*-low row reproduces from co-top
h*-low rows up to explicit Markov loss; (c) = the psi-maximum principle with
NO t*-division and O(1) oscillation.]

**L6.5 (THE ISOLATED WALL — the minimal coupling sub-leaf; OPEN).**
There exist universal c_* in (0,1) and delta_0 in (0, 1/4] such that for every
exact signed idempotent P with 0 < delta(P) <= delta_0 and nonempty visible set,
every hidden top vertex v with H > 16*tau, t*(v) > 0, disjoint always-tight hulls
at v, and heaviness sum_{j in C(v)} P_vj^+ >= 1 - theta_0 (theta_0 = 1/8,
C(v) = {j : ||p_j - p_v||_1 < 4*tau, d_j > 16*tau}), one has
sum_{j in A} P_vj^+ >= c_*, where A = {j : ||p_j - p_v||_1 >= 4*tau, d_j > H - 8*tau}.
[The dual-required co-top far web (L6.2) must receive a definite fraction of the
top's OWN positive coefficient mass. This is the lambda-vs-P^+ coupling — the
named open wall (conj-min-a-w4's gap, FINDINGS 2026-07-09 W53) — in its most
hypothesis-rich localized form; a prover of L6.5 may consume ALL of L6.1-L6.4.]

**Assembly claim (PROVED, §2.5).** L6.5 implies L6 in the u = v instantiation
(the only instantiation the W54 assembly consumes), with the tree constant
re-pinned to c_m := c_*/2 (and necessarily c_* <= theta_0 + delta_0 for
non-vacuity; see Remark R2). Conversely L6 implies L6.5 vacuously on the
configuration class; so modulo the proved sub-lemmas, **L6 (u = v) is EQUIVALENT
to L6.5**: the leaf has been collapsed onto the minimal open coupling statement
with zero residual slack elsewhere.

---

## §2 PROOFS

### §2.0 Preliminaries used repeatedly

(P0) *Existence of the display.* v hidden implies the rho-far set F_v =
{j : ||p_j - p_v||_1 >= 4*tau} is nonempty and an optimal hiddenness dual witness
exists with sum_i beta_i = t*(v) (lem-hiddenness-dual-witness, contract: "there
exist lambda_f >= 0 (f in F_v) with sum_f lambda_f = 1 and alpha_i, beta_i >= 0
... with sum_i beta_i = t*(v) < kappa, such that sum_f lambda_f*(p_f - p_v) +
sum_i alpha_i*(p_i - p_v) = sum_i beta_i*(p_i - p_v)"). Since t*(v) > 0 by
hypothesis and t*(v) < kappa < infinity (v hidden, def-exposed), the reduction of
lem-always-tight-dual-support applies ("every optimal hiddenness dual witness
(lambda, alpha, beta), after deleting redundant centered-zero constraints, has
supp(lambda) contained in T, supp(beta) contained in O, and supp(alpha) contained
in Z ... T is nonempty, and O is nonempty if and only if t*(u) > 0"), and
lem-optimal-face-conic-reduction identifies the reduced optimal witnesses exactly
with the displays
sum_{f in T} lambda_f*(p_f - p_v) + sum_{z in Z} a_z*(p_z - p_v)
= t*(v) * sum_{i in O} gamma_i*(p_i - p_v)                        (DISP)
with lambda, gamma probability vectors on T, O and a_z >= 0 on Z. In particular
at least one display exists. The deleted "centered-zero" constraints are the rows
geometrically coincident with p_v (the redundant d_v = 0 constraints, per the
always-tight shard's provenance), so every z in Z appearing in (DISP) has
p_z != p_v: **the a-carriers are nonclone**.

(P1) *Affine pairing.* Any affine F : R^n -> R with linear part c distributes over
(DISP): applying c to both sides and using c(p_j - p_v) = F(p_j) - F(p_v) gives
sum_f lambda_f (F_f - F_v) + sum_z a_z (F_z - F_v) = t*(v) sum_i gamma_i (F_i - F_v).
This is finite exact linear algebra on an identity between two vectors of R^n;
no shard needed beyond (DISP) itself.

(P2) *Top-deficit facts.* A top support functional phi exists
(lem-top-deficit-price, contract: "there exists a top support functional phi
(affine, phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1)"), and
for any such phi: z_j = H - phi(p_j) >= 0 (contract: "z_j = H - phi(p_j) >= 0");
z_j = phi(p_v) - phi(p_j) <= ||p_v - p_j||_1 <= 2 + 4*delta (1-Lipschitz plus the
def-signed-idempotent row-diameter clause "pairwise l1 distances are at most
2 + 4*delta"); and phi(p_j) <= d_j for every row (1-Lipschitz gives
phi(p_j) <= phi(q) + ||p_j - q||_1 for the closest point q of C_W, and
phi(q) <= 0), hence z_j < c*tau implies d_j >= phi(p_j) = H - z_j > H - c*tau.

(P3) *Depth Lipschitzness.* |d_x - d_y| <= ||x - y||_1 for the function
dist_1(., C_W) (triangle inequality through any point of C_W; elementary).

(P4) *Ledger slack.* For any affine F and any row i, row reproduction
p_i = sum_j P_ij p_j (P^2 = P, row i) and sum_j P_ij = 1 (P1 = 1) give
F_i = sum_j P_ij F_j (this is lem-harmonic-affine-bridge's forward reading:
affine-in-position row values are P-fixed). Sign-splitting,
sum_j P_ij^+ F_j = F_i + sum_j P_ij^- F_j.

### §2.1 Proof of L6.1

Fix a display (DISP) (exists by P0) and a top support functional phi (P2).
Apply (P1) with F = phi. Since F_v = phi(p_v) = H and F_j = H - z_j,
F_j - F_v = -z_j for every row j, so
- sum_f lambda_f z_f - sum_z a_z z_z = - t*(v) sum_i gamma_i z_i,
i.e. the exact identity
sum_{f in T} lambda_f z_f + sum_{z in Z} a_z z_z = t*(v) * sum_{i in O} gamma_i z_i.
Every left-hand summand is nonnegative (lambda_f, a_z >= 0 and z >= 0 by P2).
The right side: gamma is a probability vector and 0 <= z_i <= 2 + 4*delta (P2),
so it is <= t*(v)*(2 + 4*delta). Since v is hidden, t*(v) < kappa = tau/4
(def-exposed), and kappa*(2 + 4*delta) = (1/2 + delta)*tau; the inequality
t*(v)*(2+4*delta) < (1/2 + delta)*tau is strict. QED L6.1.

*Checkable fixture note for the verifier.* The identity is an instance of (P1);
its two inputs, (DISP) and phi, come from shards each carrying exact fixtures
(lem-optimal-face-conic-reduction's W41 certificate families;
lem-top-deficit-price's VB1 check). The only new step is the pairing, which is
one line of linear algebra.

### §2.2 Proof of L6.2

By L6.1, sum_f lambda_f z_f < (1/2 + delta)*tau, all terms nonnegative. Markov:
lambda{f in T : z_f >= c*tau} <= (sum_f lambda_f z_f)/(c*tau) < (1/2 + delta)/c,
so lambda{f in T : z_f < c*tau} > 1 - (1/2 + delta)/c. For such f: d_f > H - c*tau
by (P2), and ||p_f - p_v||_1 >= 4*tau because membership in T means the rho-far
constraint of f is in the exposedness LP at v (T is a family of FAR constraints,
lem-always-tight-dual-support; the far index set is F_v by def-exposed). Since
lambda is a probability on T (DISP), the first clause follows. At c = 4,
delta <= 1/4: 1 - (1/2 + delta)/4 >= 1 - (3/4)/4 = 13/16, and
{d > H - 4*tau} is contained in {d > H - 8*tau}, so more than 13/16 of lambda
sits in A intersect T.
The a-clause: identically, sum_z a_z z_z < (1/2 + delta)*tau (L6.1), so
sum over {z : z_z >= c*tau} of a_z < (1/2 + delta)/c, and every other a-carrier
has z_z < c*tau hence d_z > H - c*tau (P2). QED L6.2.

### §2.3 Proof of L6.3

*Forced conic mass.* v is a hidden geometrically distinct row vertex with
t*(v) > 0 and disjoint always-tight hulls, so lem-disjoint-hulls-forced-alpha
applies verbatim (contract: "every reduced optimal display carries zero-face
conic mass sum a_z > dist_1(K_T, K_O)/(4*tau)"): sum_z a_z > g/(4*tau).

*Location of the a-carriers.* Every z in Z of (DISP) is nonclone (P0), satisfies
h*(p_z) = 0 (Z is the always-tight zero face: the lower box constraint is tight
on the whole optimal face, so every optimal exposer vanishes there), and is
rho-near v by lem-zero-face-localization (contract: "every row z with
h*(p_z) = 0 for an optimal exposer h* at u satisfies ||p_z - p_u||_1 < 4*tau").
Combining with L6.2's a-clause: at least g/(4*tau) - (1/2 + delta)/c of the conic
mass sits on such rows with additionally d_z > H - c*tau. (For c >= 4 the co-top
clause also follows from (P3): d_z >= d_v - ||p_z - p_v||_1 > H - 4*tau; for
c < 4 the L6.2 route is strictly stronger.)

*Downhill displacement.* K_T and K_O are compact convex (convex hulls of finitely
many points; K_O is a scalar multiple of one) and disjoint with
g = dist_1(K_T, K_O) > 0. By l1/l-infinity duality there is a linear ell with
||ell||_inf <= 1 and min_{x in K_T} ell(x) - max_{y in K_O} ell(y) >= g.
[Two-line derivation, kept for the verifier: S := K_T - K_O is compact convex
with dist_1(0, S) = g > 0; min_{s in S} ||s||_1 = max_{||ell||_inf <= 1}
min_{s in S} ell(s) is the standard support-function duality for the l1 norm
(the maximizing ell is the l-infinity-unit dual functional at the minimal-norm
point, and for every unit ell, min_S ell <= ||s*||_1); BSc-level convex duality,
used as common knowledge per L2.]
Write L_T = min_{f in T} ell(p_f - p_v) and L_O = max_{i in O} ell(p_i - p_v);
then L_T - t*(v)*L_O >= g: indeed max over K_O of ell equals
t*(v) * max_{i in O} ell(p_i - p_v) = t*(v)*L_O, since K_O = t*(v) *
conv{p_i - p_v : i in O} and t*(v) > 0, while min over K_T of ell = L_T (a linear
functional on a convex hull attains its extrema at generators). Apply (P1) with
F(x) = ell(x - p_v):
sum_f lambda_f ell(p_f - p_v) + sum_z a_z ell(p_z - p_v)
= t*(v) sum_i gamma_i ell(p_i - p_v) <= t*(v)*L_O,
and sum_f lambda_f ell(p_f - p_v) >= L_T (lambda a probability on T), so
sum_z a_z ell(p_z - p_v) <= t*(v)*L_O - L_T <= -g. QED L6.3.

### §2.4 Proof of L6.4

*Legality of a bounded (ell, m).* Take ell the optimal separator of §2.3
(||ell||_inf <= 1, L_T - t*L_O >= g > 0; it is a strict linear separator of the
two hulls, so it is a legal ell for lem-separator-zero-face-obstruction). The
shard's legal m-interval is (L_O, L_T/t*), nonempty since t* > 0 and
L_T > t*L_O. All rows lie within pairwise l1-distance 2 + 4*delta
(def-signed-idempotent), so |L_O| <= 2 + 4*delta and |L_T| <= 2 + 4*delta
(||ell||_inf <= 1). Choose
  m := (L_O + L_T/t*)/2   if L_T/t* <= 3 + 4*delta,
  m := 3 + 4*delta        otherwise.
In the first case m is the midpoint of a nonempty open interval whose endpoints
both lie in [-(2+4*delta), 3+4*delta], so m is legal and |m| <= 3 + 4*delta. In
the second case L_O <= 2 + 4*delta < 3 + 4*delta < L_T/t*, so m is legal, and
|m| = 3 + 4*delta. Either way |m| <= 3 + 4*delta.

*Oscillation.* For rows j, k: psi_j - psi_k = ell(p_j - p_k) - m*(h*_j - h*_k),
|ell(p_j - p_k)| <= 2 + 4*delta, |h*_j - h*_k| <= 1 (h* in [0,1] on rows), so
osc(psi) <= (2 + 4*delta) + (3 + 4*delta) = 5 + 8*delta. Since psi(p_v) = 0
(shard conclusion), also max_j |psi_j| <= osc(psi).

*Floor on T.* For f in T: h*_f = t* (always-tight far family), so
psi_f = ell(p_f - p_v) - m*t* >= L_T - m*t*. First m-case:
L_T - m*t* = L_T - (t*L_O + L_T)/2 = (L_T - t*L_O)/2 >= g/2. Second m-case:
L_T - (3+4*delta)*t* >= (g + t*L_O) - (3+4*delta)*t*
>= g - t*(|L_O| + 3 + 4*delta) >= g - kappa*(5 + 8*delta) >= g - (7/4)*tau
(t* < kappa = tau/4 and delta <= 1/4). Hence psi >= min(g/2, g - (7/4)*tau) on T.
The full sign structure (psi(p_v) = 0, P psi = psi as row values, psi > 0 on T,
psi < 0 on O, and a nonclone blocker z_0 with h*(p_{z_0}) = 0 and
psi(p_{z_0}) < 0) is the CONCLUSION of lem-separator-zero-face-obstruction at the
legal pair (ell, m); it is cited, not re-derived.

*(a) and (b), the corner trap.* By (P4) with F = z (affine):
sum_j P_ij^+ z_j = z_i + sum_j P_ij^- z_j <= s_1 + nu_i*(2 + 4*delta)
(0 <= z_j <= 2 + 4*delta by P2); Markov at threshold s_2 gives (a). With
F = h* (affine, values in [0,1] on rows):
sum_j P_ij^+ h*_j = h*_i + sum_j P_ij^- h*_j <= eta_1 + nu_i; Markov gives (b).
[(b) at a zero-face row (eta_1 = 0) is lem-zero-face-exchange-identity /
lem-affine-exposer-row-capacity re-derived; at other rows it is their verbatim
Markov extension. Cited for consistency, derived in one line here.]

*(c) the psi-maximum principle.* The maximum of the affine psi over row indices
is attained (finitely many rows); let r attain M = max_j psi_j. By (P4) with
F = psi: sum_j P_rj psi_j = psi_r = M, and with sum_j P_rj = 1 this gives
sum_j P_rj (M - psi_j) = 0; sign-splitting,
sum_j P_rj^+ (M - psi_j) = sum_j P_rj^- (M - psi_j) <= nu_r * osc(psi)
(0 <= M - psi_j <= osc(psi)). With nu_r <= delta this is (c). Note r can be taken
a geometrically distinct row vertex: every row is a convex combination of the
geometrically distinct row vertices and psi is affine, so the row-index maximum
is attained at a vertex. QED L6.4.

*Why (c) does not close L6 (recorded as part of the lemma's honest scope).*
(a)-(c) constrain FLOWS, not existence: a family of co-top, h*-low, mutually
reproducing rows ("the plateau") satisfies (a), (b), (c) with zero slack — every
ledger balances internally because all four functionals z, h*, ell, psi are
row-level harmonic (P4) and the plateau can be psi-flat. The maximum principle
pins only the top row of the plateau to draw from psi-near-max rows, which the
plateau itself supplies. No single-functional principle excludes it; this is the
exact shape of the residual wall L6.5 (see §4).

### §2.5 Proof of the assembly claim (L6.5 => L6, u = v instantiation)

Assume L6.5. Suppose for contradiction a configuration satisfies L6's antecedent
in the assembled form: P exact signed idempotent, 0 < delta <= delta_0, W != {},
hidden top v with H > 16*tau, heaviness sum_{C(v)} P_vj^+ >= 1 - theta_0
(theta_0 = 1/8), u = v the deepest mass-carrying cluster vertex (Step A1;
t*(v) > 0), disjoint always-tight hulls at v, NOT-Q4, and NOT-Q5 with the tree
constant c_m := c_*/2:
sum_{j in A} P_vj^+ < c_m = c_*/2.
The hypotheses of L6.5 are a sub-list of this antecedent (heaviness, tallness,
t* > 0, disjointness; NOT-Q4/NOT-Q5 are not needed by L6.5), so L6.5 yields
sum_{j in A} P_vj^+ >= c_* > c_*/2, contradicting NOT-Q5. Hence no such
configuration exists: L6 holds (u = v). The choice c_m = c_*/2 is legal for the
tree: G8 fixes c_m as a free universal constant in (0, 1/2) whose only
load-bearing roles are L1's charge (any c_m > 0 works, delta_0 adjusts) and this
mass bookkeeping. QED assembly.

*Role of L6.1-L6.4 in the assembly.* None are needed for the two-line implication
above; they are the PROVED structure that (i) makes L6.5 attackable (its prover
may assume the witness's lambda-mass is > 13/16 on A intersect T, the conic
a-mass > g/(4*tau) is downhill co-top nonclone rho-near, and the corner trap
holds), and (ii) certify that no OTHER open ingredient remains in the leaf: every
non-L6.5 step of the starvation narrative in decomposition.md §3-L6's mechanism
sketch is now either proved here or shown unnecessary.

### §2.6 Remarks

**R1 (NOT-Q4 is near-vacuous — consistency check with L4).** For every
always-tight zero-face row z, lem-affine-exposer-row-capacity at (i = z, h = h*,
eta = kappa) gives kappa * sum_{j : h*_j >= kappa} P_zj^+ <= nu_z <= delta, i.e.
the kappa-high shipping is <= 4*tau < c_r automatically once delta < (c_r/4)^2.
So Q4-true is impossible in the small-delta regime (this is exactly L4's kill),
and NOT-Q4 carries no additional information for L6 — consistent with the fact
that the proofs above never consumed it.

**R2 (constants interface — a correction the tree must absorb).** Heaviness puts
>= 1 - theta_0 of v's positive mass on C(v), and C(v) is disjoint from A
(rho-near vs rho-far), so sum_A P_vj^+ <= theta_0 + nu_v <= theta_0 + delta_0 by
lem-mass-split (sum_j P_vj^+ = 1 + nu_v). Hence any true L6.5 has
c_* <= theta_0 + delta_0 = 1/8 + delta_0, and the tree MUST take
c_m < c_* <= 1/8 + delta_0. The G8 calibration c_m = 1/4 is therefore TOO LARGE
to be closed through this decomposition; G8 already declares c_m free in
(0, 1/2), so re-pin c_m := c_*/2 (as in §2.5). This tightens the trapped-mass
bookkeeping of Step C3 (1 - theta_0 - c_m only improves) and costs nothing
elsewhere; flagged so the decomposition's G8 entry 2 gets updated.

**R3 (the u != v case is NOT consumed and NOT proved).** For a cluster vertex
u != v the pairing of §2.1 acquires the correction term
z_u * (1 + sum_z a_z - t*(u)) with z_u in [0, 4*tau), giving
sum_f lambda_f z_f + sum_z a_z z_z <= (1/2 + delta)*tau + 4*tau*(1 + sum_z a_z);
since disjointness FORCES sum_z a_z > g/(4*tau) and the conic mass is unbounded
in general (obs-realized-alpha-blowup, cited as context), the co-top pinning is
lost exactly through the alpha channel. The conditional variant with
sum alpha <= A_0 is lem-bounded-alpha-top-slab-reduction (proved, cited) — but
bounded alpha and forced alpha coexist only for g < 4*tau*A_0. Since Step A1
instantiates u := v whenever t*(v) > 0 and routes t*(v) = 0 to the assembly gap
AG-1, the u != v generality is dead weight for the W54 tree; recorded here so no
verifier mistakes L6.1 for a general-u claim.

**R4 (clone-invariance and dimension-freeness).** All statements are index-sum /
row-point statements: clones split summands without changing any total
(lambda, a, gamma live on constraint families that are clone-robust per
lem-always-tight-dual-support's reduced conventions; z, h*, ell, psi are
functions of the row point). No constant references n; no step counts indices.

---

## §3 TOOLS USED (proved shards only; clause quoted at point of use)

- **lem-hiddenness-dual-witness** — existence of the optimal witness with
  "sum_i beta_i = t*(v) < kappa" and "F_v ... nonempty for hidden v" (§2.0 P0).
- **lem-always-tight-dual-support** — "every optimal hiddenness dual witness ...
  after deleting redundant centered-zero constraints, has supp(lambda) contained
  in T, supp(beta) contained in O, and supp(alpha) contained in Z"; "T is
  nonempty, and O is nonempty if and only if t*(u) > 0" (§2.0 P0, §2.2).
- **lem-optimal-face-conic-reduction** — "the reduced optimal hiddenness dual
  witnesses are exactly the displays sum_{f in T} lambda_f*(p_f - p_u) +
  sum_{z in Z} a_z*(p_z - p_u) = t*(u) * sum_{i in O} gamma_i*(p_i - p_u), with
  lambda and gamma probability vectors ... a_z >= 0" (§2.0 P0 — the (DISP)
  object of every proof).
- **lem-top-deficit-price** — "there exists a top support functional phi (affine,
  phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1)" and
  "z_j = H - phi(p_j) >= 0" (§2.0 P2).
- **lem-disjoint-hulls-forced-alpha** — "every reduced optimal display carries
  zero-face conic mass sum a_z > dist_1(K_T, K_O)/(4*tau)" (§2.3).
- **lem-zero-face-localization** — "every row z with h*(p_z) = 0 for an optimal
  exposer h* at u satisfies ||p_z - p_u||_1 < 4*tau" (§2.3).
- **lem-separator-zero-face-obstruction** — the full conclusion "psi(p_u) = 0,
  P psi = psi on row values, psi(p_f) > 0 for all f in T, psi(p_i) < 0 for all
  i in O, and there exists a nonclone row z with h*(p_z) = 0 and psi(p_z) < 0"
  at the legal pair (ell, m), quantified "for every strict linear separator ell
  and every m with max over i in O of ell(p_i - p_u) < m < (min over f in T of
  ell(p_f - p_u))/t*(u)" (§2.4 — the legality of the bounded (ell, m) pair is
  checked against exactly this clause).
- **lem-harmonic-affine-bridge** — "a vector g satisfies Pg = g if and only if
  there exists u with g_i = u . p_i for every row index i" (§2.0 P4: every affine
  functional's row values are P-fixed; used for z, h*, ell, psi ledgers).
- **lem-mass-split** — "sum_j a_j^+ = 1 + nu_v" (§2.6 R2).
- **lem-affine-exposer-row-capacity** — "eta * sum over f in F of max(P_if, 0)
  <= nu_i" for admissible h vanishing at row i (§2.6 R1; also the one-line
  rederivation inside L6.4(b)).
- **lem-zero-face-exchange-identity** — "sum_j max(P_zj,0)*g_j =
  sum_j max(-P_zj,0)*g_j <= nu_z <= delta" (§2.4(b) consistency note).
- **lem-bounded-alpha-top-slab-reduction** — the conditional u != v confinement
  "sum over f in F_u of lambda_f * z_f < tau*((1/2 + delta) + 4*(1 + A0))"
  (§2.6 R3 only; NOT consumed by the main chain).
- Context-only (NOT proof inputs): lem-tight-far-geography (whose clause (i) the
  lambda-part of L6.1 recovers on reduced witnesses), obs-realized-alpha-blowup
  (why R3's correction term is unbounded), lem-zero-face-vertex-support and
  lem-disjointness-huddle-reduction (available huddle structure, unused),
  decomposition.md (target and mechanism source; never a proof input).

Definitions consumed: def-signed-idempotent (row geometry, diameter 2+4*delta),
def-negative-mass, def-exposed (admissible exposer, t*, hidden means t* < kappa),
def-visible-set (scales), def-height (hidden top, d_j).

---

## §4 HONEST ASSESSMENT

**Weakest step / what a refuter attacks first.** L6.5 — it is not proved, and
everything else in the leaf now hangs on it alone. The refuter's construction to
beat is sharpened by L6.1-L6.3 to a precise object: a **co-top straddling web** —
a family of geometrically distinct hidden row vertices, each at l1-distance
>= 4*tau from v but at depth > H - 4*tau (co-top), mutually reproducing (each
row's positive mass on fellow web rows, negative corrections O(delta)), whose
lambda-barycenter sits within (1/2+delta)*tau + 4*tau*(sum a_z) of p_v (the
display forces the web to STRADDLE v), while v's own positive mass stays entirely
in-cluster. Every ledger proved here (z, h*, ell, psi; L6.4 a-c) is satisfiable
by such a web with zero slack, because all four functionals are harmonic and the
web can be flat in each. What the refuter must additionally arrange — and what no
W52 construction ever achieved — is that every web vertex is itself HIDDEN
(t* < kappa) even though the web members are mutually rho-far and co-top: mutual
far-exposure is the obstruction (each web vertex is a candidate exposer-anchor
for its antipodes). That tension is not a theorem; it is exactly the never-solved
tall-construction problem (FINDINGS 2026-07-07 W49F: "the tall class has never
been realized"), which is evidence FOR L6.5 but proof of nothing.

**Whether the psi-max-principle resource actually delivered.** Partially, and
honestly: NO kill. What it delivered: (i) the observation that the psi-family is
exactly the two coupled ledgers (ell, h*) — varying m adds nothing beyond the
pair, since both are affine and hence row-level harmonic; (ii) the bounded
normalization (|m| <= 3+4*delta, osc <= 5+8*delta, NO t*-division — this
neutralizes the leaf's flagged death trap: no constant here divides by t*(u));
(iii) the corner trap and the maximum principle (L6.4 a-c) with explicit O(delta)
slack. What it could NOT do: exclude the internally-reproducing plateau — the
eigen-identity is exactly as strong at web rows as at huddle rows, so it
constrains the web's internal consistency, never its existence. The genuinely new
proved yields of this wave are the a-mass co-top pinning (L6.1's zero-face
clause, which no prior shard states) and the quantitative downhill displacement
sum a_z ell(p_z - p_v) <= -g (L6.3).

**Risk notes on my own proofs.** (1) §2.0 P0's "centered-zero = clones of v"
reading rests on lem-always-tight-dual-support's provenance note ("arbitrary
alpha can be added on d_v = 0 rows"), not its contract sentence; a hostile
verifier should confirm the reduced display's Z excludes v-clones — if it does
not, L6.3's "nonclone" clause needs the blocker route
(lem-separator-zero-face-obstruction supplies one nonclone zero-face row
unconditionally) and the a-mass location clause survives with "nonclone" deleted.
(2) §2.3's duality two-liner is classical but stated tersely; check the
compactness and the attainment. (3) L6.1 needs the display for the OPTIMAL
witness; the chain optimal-witness-exists -> reduced-display-exists is P0 —
verify no quantifier slip between "every optimal witness reduces" and "a reduced
optimal witness exists". (4) The m-choice case split in §2.4 should be checked
at the boundary L_T/t* = 3 + 4*delta (both branches legal there).

**The single decisive next question.** L6.5, and within it the sharpest
sub-question my analysis isolates: *can a set of mutually rho-far, co-top,
geometrically distinct row vertices straddling a hidden top v ALL be hidden at
scale (rho, kappa), given that each is a rho-far anchor candidate for the
others?* A YES-instance (exact rational arithmetic) refutes L6.5 and with it the
(M2) huddle-charge route through this leaf; a NO-theorem ("mutual-exposure
rigidity": among any straddling co-top family, some member is exposed) proves
L6.5 outright, because L6.2 forces the witness onto exactly such a family and
exposure contradicts co-topness (exposed => depth 0, lem-ball-cluster-exposure-
void's mechanism). I recommend registering that mutual-exposure rigidity
statement as the successor conjecture: it is lambda-free and P^+-free — it
converts the coupling wall into a pure convex-position question, which is a
strictly lower-complexity target than L6.5's mixed primal-dual form.
