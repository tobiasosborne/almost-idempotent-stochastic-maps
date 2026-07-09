VERDICT: PARTIAL — L2-v2 provably collapses to bare "tall + intersecting hulls at the top is impossible" (its plateau and averaging clauses are automatic consequences of lem-top-deficit-price at small delta, and t*(v) > 0 is automatic), a proved confinement package pins the exact residual object and PROVES the architect's prescribed averaging mechanism dead, the leaf closes conditionally on conj-summit-cylinder-exclusion whenever the dual face Y_v is narrow, and the unconditional residual decomposes into two named sub-leaves (SL1a = the co-top straddling-web exclusion, literally unified with the L6 residual; SL1b = shallow universally-shadowed counterweight exclusion) — BLOCKED at SL1a/SL1b.

# W54 / L2-v2 — the summit-plateau exclusion leaf (Branch II creative core)

AUTHOR artifact (hostile verification pending). Everything below is AUTHOR-CLAIM except
quoted shard contracts (status: proved, cited by id, clause quoted at point of use).
Dimension-free and clone-invariant throughout: all statements are about row points,
geometrically distinct row vertices, and coefficient-mass sums; no raw index counting.

## §0 Notation (definitions/, fixed)

P an exact signed idempotent (def-signed-idempotent: P1 = 1, P^2 = P), delta = delta(P)
(def-negative-mass), tau = sqrt(delta), rho = 4*tau, kappa = tau/4 (def-visible-set),
D := 2 + 4*delta (the row-diameter bound: def-signed-idempotent row geometry, "pairwise
l1 distances are at most 2+4delta"; delta <= 1/4 gives D <= 3, and note the exact
identity kappa*D = (1/2 + delta)*tau used throughout). W = W(P) the visible set,
C_W = conv{p_w : w in W}, d_j = dist_1(p_j, C_W), H = max_i d_i (def-height), v a hidden
top vertex (d_v = H), a_j = P_vj, a_j^+ = max(a_j, 0), nu_v = sum_j max(-a_j, 0) <= delta.
F_v = {j : ||p_j - p_v||_1 >= 4*tau}. t* = t*(v) the exposedness margin (def-exposed);
admissible exposer at v = affine h with h(p_v) = 0, 0 <= h(p_j) <= 1 on every row.
T, O, Z the always-tight far / upper-box / zero-face families of the exposedness LP at v
(lem-always-tight-dual-support); K_T = conv{p_f - p_v : f in T},
K_O = t* * conv{p_i - p_v : i in O}.
Y_v = {y : ||y||_inf <= 1, y.p_v - h_C(y) = H} the dual face (lem-top-support-dual-face),
h_C(y) = sup{y.c : c in C_W}; for y in Y_v, phi_y(x) = y.x - h_C(y) and the top-deficit
of row j is z_j(y) := H - phi_y(p_j) = y.(p_v - p_j) (since H = y.p_v - h_C(y)). For
every row j and every y in Y_v: 0 <= z_j(y) <= D and z_j(y) >= H - d_j (the two-sided
bounds from lem-top-deficit-price's mechanics, re-derived in §2.0 for self-containment).
Z_v(f) = sup_{y in Y_v} y.(p_v - p_f); Cyl_v(eps) = {x : sup_{y in Y_v} y.(p_v - x) < eps}.

THE TARGET (L2-v2, verbatim PART B R1 of the W54 tree): there exist universal
c_m in (0,1), delta_0 > 0 such that no exact signed idempotent P with
0 < delta(P) <= delta_0, nonempty visible set, and hidden top vertex v of height
H > 16*tau has, simultaneously: (1) t*(v) > 0; (2) the always-tight hulls at v INTERSECT;
(3) for every top support functional phi, sum_{j : H - phi(p_j) < tau} a_j^+ > 1 - c_m;
(4) for every average phi-bar of at most 3 top support functionals,
sum_{j : H - phi-bar(p_j) >= tau} a_j^+ < c_m/4.

## §1 Statements

### Theorem A (hypothesis collapse — PROVED)

**A1.** For every c_m in (0,1) and every exact signed idempotent P with
0 < delta <= 1/4 and delta < (c_m/12)^2, nonempty visible set, and hidden top vertex v:
clauses (3) and (4) of L2-v2 hold automatically at v, and clause (1) t*(v) > 0 holds for
every hidden geometrically distinct row vertex with F_v nonempty (in particular for v).

**A2 (equivalence).** L2-v2 is EQUIVALENT to:

> **L2-core.** There exists universal delta_0' > 0 such that no exact signed idempotent
> P with 0 < delta(P) <= delta_0', nonempty visible set, and hidden top vertex v of
> height H > 16*tau has K_T intersecting K_O (equivalently: has an alpha-free reduced
> optimal display at v, lem-optimal-face-conic-reduction).

Forward: L2-core proves L2-v2 with any c_m and delta_0 = delta_0'. Backward: L2-v2 with
(c_m, delta_0) proves L2-core with delta_0' = min(delta_0, (c_m/12)^2, 1/4).

**A3 (tree consequences).** (i) The Q2-true and Q3-v2-true branches of the W54 tree are
VACUOUS for delta < (c_m/12)^2 (L1's charge is never entered in-class; it fires only as
the arithmetic excluding large delta, exactly as the assembly uses it). (ii) The S3
split is DEGENERATE: every finite convex average of top support functionals coincides
ON THE ROW SET with a single top support functional phi_ybar, ybar in Y_v (proof in
§2.2, five lines from convexity of h_C); Q3-v2 is literally Q2 at threshold c_m/4.
(iii) Consequently the "plateau" is NOT a resource: any prover of L2-v2 gets nothing
from clauses (3)-(4) beyond delta-smallness, and any consumer may swap L2-v2 for
L2-core. The leaf is Branch-II tall-emptiness, full stop.

### Theorem B (the intersection-branch confinement package — PROVED)

Let P, v be an L2-core configuration: 0 < delta <= 1/4, W nonempty, v hidden top,
H > 16*tau (tallness is only needed where flagged), t* = t*(v) in (0, kappa), and an
alpha-free reduced optimal display (lem-optimal-face-conic-reduction):

    sum_{f in T} lambda_f (p_f - p_v) = t* sum_{i in O} gamma_i (p_i - p_v),    (INT)

lambda, gamma probability vectors on T, O. Write b = sum lambda_f p_f,
q = sum gamma_i p_i. Then:

- **B1 (witness legality).** (lambda, alpha = 0, beta = t*gamma) is a hiddenness dual
  witness of v with sum beta = t* < kappa = tau/4; all small-beta consumers
  (lem-hiddenness-depth-markov, lem-top-witness-third-actor) apply to it.
- **B2 (barycenter confinement).** b - p_v = t*(q - p_v), hence
  ||b - p_v||_1 = t*||q - p_v||_1 <= t*D < kappa*D = (1/2 + delta)*tau.
- **B3 (universal exposer defeat).** For EVERY admissible exposer h at v:
  0 <= sum_f lambda_f h(p_f) = t* sum_i gamma_i h(p_i) <= t*.
  The witness defeats every exposer ON AVERAGE, not merely at its minimum.
- **B4 (the lambda-cap).** For every y in Y_v:
  sum_f lambda_f z_f(y) = y.(p_v - b) <= t*D < (1/2 + delta)*tau; hence
  lambda{f : z_f(y) >= c*tau} < (1/2 + delta)/c for every c > 0. By A3(ii) the same
  holds verbatim for every finite convex average of top support functionals.
- **B5 (depth-deficit expectation).** sum_f lambda_f (H - d_f) <= t*D; hence
  lambda{f : d_f <= H - c*tau} < (1/2 + delta)/c, and at c = 4 (with delta <= 1/4)
  lambda{f : d_f > H - 4*tau} > 13/16 (matching lem-top-witness-third-actor).
- **B6 (spread).** For every f_0 in supp lambda there exists f_1 in supp lambda with
  ||p_{f_0} - p_{f_1}||_1 >= 4*tau - t*D > (7/2 - delta)*tau. Every witness row has a
  witness antipode; note (7/2 - delta)*tau < rho — the antipode is NOT forced rho-far
  from f_0 (honest scale gap for any "mutually rho-far" formulation).

### Proposition D (the dead-end theorem — PROVED)

In every L2-core configuration, NO top support functional and NO finite convex average
of top support functionals can see the witness at average deficit above t*D: B4 is an
identity-level cap. Consequences:

- **D1.** The architect's prescribed L2 mechanism (v1 §3: "two support functionals
  adapted to two extreme summit points would disagree by >= tau on part of the mass" /
  "turning lambda-mass into a z lower bound for a WELL-CHOSEN phi") is IMPOSSIBLE as a
  route through the witness measure lambda: for every phi in Phi_v (and every average),
  the lambda-mass seen at deficit >= tau is < 1/2 + delta — never a majority, never a
  contradiction, at ANY tallness.
- **D2.** conj-summit-cylinder-exclusion, even if PROVED with any constant c_3, cannot
  close L2-v2 through the lambda-pairing: pointwise exclusion (each deep far row has its
  own y_f with z >= c_3*tau) is consistent with B2/B4 because Cyl_v(eps) is convex and
  contains p_v — the barycenter of excluded points re-enters the cylinder. The
  known FINDINGS wall ("pointwise visibility does NOT average up") is here PROVED to
  bind in-configuration, not merely exhibited on a toy simplex.
- **D3.** Any future L2 prover must therefore couple to v's own coefficients a_j^+, to
  second-order idempotence (row reproduction at rows other than v), or to the
  always-tight/visible-set structure — not to (lambda, Phi_v) pairings alone.

### Theorem C (conditional narrow-face closer — PROVED implication)

Define the dual-face oscillation of the configuration on the far-deep band
B_v = {f : ||p_f - p_v||_1 >= 4*tau, d_f > H - 4*tau}:

    omega_v := (1/tau) * sup{ (y' - y'').(p_v - p_f) : y', y'' in Y_v, f in B_v }.

IF conj-summit-cylinder-exclusion holds with constants (c_3, delta_0(L3)), THEN no
L2-core configuration with delta <= min(1/4, delta_0(L3)) has
omega_v <= c_3 - (16/13)(1/2 + delta). In particular (omega_v = 0): if Y_v is a
singleton, cylinder exclusion with c_3 > (16/13)(1/2 + delta_0) closes Branch II
outright. The unconditional residual of L2-core relative to the sibling conjecture is
exactly the WIDE-dual-face case (a summit creased in many dual directions).

### The sub-leaf system (proved reductions; SL1a/SL1b OPEN)

**SL1 (straddling far-witness exclusion).** There exists universal delta_0 > 0 such
that for every exact signed idempotent P with 0 < delta <= delta_0, W nonempty, hidden
top v with H > 16*tau, NO probability vector lambda on the rows satisfies
simultaneously: (a) supp lambda subset of F_v; (b) ||sum_f lambda_f p_f - p_v||_1 <=
(1/2 + delta)*tau; (c) lambda{f : d_f > H - 4*tau} > 13/16; (d) sum_f lambda_f h(p_f)
<= kappa for every admissible exposer h at v.

*Proved:* SL1 implies L2-core, hence L2-v2 (the display's lambda satisfies (a)-(d) with
(d) at the stronger value t* < kappa). Proof §2.6.

**Proved split (§2.7).** In any L2-core configuration, with mu := lambda{f : d_f <=
H - 4*tau} < 1/8 + delta/4, exactly one of:

- **Case (i)** mu <= tau/D. Then the conditional witness lambda_L on the co-top part
  L = supp lambda ∩ {d > H - 4*tau} is a probability on far co-top rows with barycenter
  within (16/13)(3/2 + delta)*tau <= (28/13)*tau < 2.2*tau of p_v and universal
  admissible-exposer average <= (16/13)*t* < (16/13)*kappa. Killing this object is:

  > **SL1a (co-top straddling-web exclusion — the L6-unified rigidity target).** No
  > exact signed idempotent with 0 < delta <= delta_0, W nonempty, hidden top v,
  > H > 16*tau admits a probability measure on rows that are simultaneously rho-far
  > from v and at depth > H - 4*tau, with barycenter within 2.2*tau of p_v and with
  > average value <= (16/13)*kappa under every admissible exposer at v.

- **Case (ii)** mu > tau/D. Then the shallow part S = supp lambda ∩ {d <= H - 4*tau}
  is a sub-probability of mass mu in (tau/D, 1/8 + delta/4) on rows that are rho-far
  from v AND shallow, whose conditional average under EVERY admissible exposer at v is
  <= t*/mu < kappa*D/tau = (1/2 + delta) — and, per-row, every f in S with
  lambda_f >= m has sup_{h admissible} h(p_f) <= t*/m (the universal-shadow pin).
  Killing this object is:

  > **SL1b (shallow universally-shadowed counterweight exclusion).** No exact signed
  > idempotent with 0 < delta <= delta_0, W nonempty, hidden top v, H > 16*tau admits
  > a sub-probability mu_S of mass >= tau/D on rows f with ||p_f - p_v||_1 >= 4*tau
  > and d_f <= H - 4*tau such that sum_f mu_S(f) h(p_f) <= kappa for every admissible
  > exposer h at v.

**Sub-assembly (checkable): SL1a AND SL1b imply SL1 (weakened-(d) form) imply L2-core
imply L2-v2.** All reductions proved in §2.6-§2.7; the leaf constants are explicit.

### Proposition E (the co-top form is NOT forced — PROVED cap-consistency analysis)

The convergence hint's mutual-exposure rigidity statement ("a straddling family of
mutually rho-far CO-TOP vertices...") is NOT what Branch II forces: a two-point weight
system with a deep pole of mass 1 - m and a FULLY SHALLOW counterweight of mass
m ~ 4*tau/D satisfies B2, B5 (all Markov caps) and the third-actor constraint whenever
H <= (1/2 + delta)/2 - epsilon, saturating the depth-deficit budget B5 exactly; it is
blocked only by B3's universal-shadow pin (the counterweight must be <= t*/m-low for
EVERY admissible exposer). Hence (a) any correct rigidity statement must either include
the exposer-defeat clause (d) or restrict to Case (i); (b) SL1b is exactly the missing
counterweight kill; (c) the escape lives only at absolute height H < ~1/4 — which is
the regime that matters (delta -> 0). Details §2.8. NOTE: this is an analysis of the
CAP SYSTEM, not an exact signed idempotent; it refutes the inference "banked caps imply
co-top straddle", not any conjecture.

### Refuter obligations (what a wide-flat-summit must satisfy)

Any exact rational refutation of L2-v2 must produce P with delta <= delta_0 and:
- **R1** H > 16*tau — the never-realized tall class (FINDINGS 2026-07-07 W49F: all
  banked census ratios H^2/delta < 16; every W52 tall entry reverted or inflated delta).
- **R2** an alpha-free display at the top: K_T must pass within t*D <= kappa*D of the
  origin — the far displacement hull must contain a point of l1-norm < (1/2+delta)*tau
  while every generator has norm >= 4*tau (a precision-t*D straddle, tightening as
  t* -> 0).
- **R3** the witness rows must be ALWAYS-TIGHT (h* = t* for the WHOLE optimal face of
  the exposedness LP, lem-always-tight-dual-support) — an infinite-family constraint
  invisible to measure-level constructions; W42's hard stop ("near-zero values certify
  nothing") cuts the other way here: the refuter must PIN tightness, not approximate it.
- **R4** for every y in Y_v some far row has z(y) <= t*D (automatic: z(y)/D is an
  admissible exposer, §2.3), so the summit must be "sequentially blind in every dual
  direction" — for a wide Y_v these are many independent constraints; for a narrow Y_v
  Theorem C + the sibling conjecture kill the instance. The refuter is squeezed from
  both sides: narrow face -> Theorem C; wide face -> many blindness constraints.
- **R5** the Case (ii) escape needs a shallow far row kept <= t*/m under EVERY
  admissible exposer at v while B5 charges m*(H - d) <= t*D — at the budget boundary.
- **R6** clone-invariance: cloning cannot create the straddle (all constraints are on
  geometrically distinct row points / mass sums).

I attempted the construction (rank-2: impossible — any vertex with nonempty far set has
t* >= 4*tau/D ~ 2*tau > kappa, consistent with cor-rank-two-visible; rank-3 signed-
barycentric framing: the summit chain's ENDPOINTS must turn, and hiddenness of each
turning vertex demands its own far huggers — the anatomy the rank-3 shards codify; no
exact instance produced). The failure mechanism I hit is R3 + R2 jointly: exactness
demands whole-face tightness of the straddle, and every local repair leaked delta.

## §2 Proofs

### §2.0 Preliminaries used repeatedly

(P-i) *Row reproduction distributes affine functions.* For any affine psi and any row
index i: psi(p_i) = sum_j P_ij psi(p_j). [P^2 = P gives p_i = sum_j P_ij p_j (row i of
P^2 = P); P1 = 1 gives sum_j P_ij = 1, so the affine constant distributes. This is
lem-harmonic-affine-bridge's forward mechanics: "a vector g satisfies Pg = g if and
only if there exists u with g_i = u . p_i for every row index i ... the constant term
of any affine representation is absorbable into u since all row sums equal 1".]

(P-ii) *Two-sided z bounds.* For y in Y_v and every row j:
0 <= H - d_j <= z_j(y) = y.(p_v - p_j) <= ||y||_inf ||p_v - p_j||_1 <= D.
[Upper: Hoelder + ||y||_inf <= 1 (Y_v definition) + row diameter D
(def-signed-idempotent: "pairwise l1 distances are at most 2+4delta"). Lower: for any
c in C_W, phi_y(p_j) = phi_y(c) + y.(p_j - c) <= 0 + ||p_j - c||_1 (phi_y <= 0 on C_W
by lem-top-support-dual-face's characterization of Phi_v); take inf over c in C_W:
phi_y(p_j) <= d_j, i.e. z_j(y) >= H - d_j >= 0 since d_j <= H = max_i d_i
(def-height).]

(P-iii) *z(y)/D is an admissible exposer at v.* z(p_v)(y) = y.(p_v - p_v) = 0; by
(P-ii) 0 <= z_j(y)/D <= 1 on every row; z(y) is affine in position. Hence by
def-exposed ("An admissible exposer for a row vertex v is an affine function h with
h(p_v) = 0 and 0 <= h(p_j) <= 1 for every row p_j") it is admissible; in particular
min_{f in F_v} z_f(y)/D <= t*(v) for every y in Y_v (t* is the sup over admissible h of
the far minimum, def-exposed).

(P-iv) *Y_v nonempty; z_j(y) = H - phi_y(p_j).* lem-top-support-dual-face contract:
"Y_v is nonempty, on the row set Phi_v is exactly {phi_y(x) = y.x - h_C(y) : y in
Y_v}"; and for y in Y_v, H = y.p_v - h_C(y), so
H - phi_y(p_j) = (y.p_v - h_C(y)) - (y.p_j - h_C(y)) = y.(p_v - p_j) = z_j(y).

### §2.1 Theorem A

**A1, clause (1).** v is hidden, so F_v is nonempty (lem-hiddenness-dual-witness
contract: "F_v ... nonempty for hidden v") and delta > 0 gives rho > 0. Then
lem-positive-exposedness-margin contract: "for an exact signed idempotent P with
rho = 4*tau > 0 ... and a geometrically distinct row vertex v with nonempty far set
F_v ... t*(v) > 0; in particular every HIDDEN geometrically distinct row vertex with
F_v nonempty has 0 < t*(v) < kappa". Clause (1) holds; also t* < kappa, used throughout.

**A1, clause (4).** Let phi-bar be any convex average of at most 3 top support
functionals at v. By lem-averaged-deficit-charge's averaging licence (shard body,
V-L1-checked: "a finite convex average of top support functionals at v is again one"),
phi-bar is itself a top support functional. Apply lem-top-deficit-price, contract:
"for ANY such phi, writing a_j = P_vj and z_j = H - phi(p_j) >= 0: for every subset A
of row indices, sum over j in A of max(a_j,0)*z_j <= nu_v*(2+4*delta) <=
delta*(2+4*delta)". Take A = {j : z_j >= tau}:
tau * sum_A a_j^+ <= delta*(2+4*delta) <= 3*delta (delta <= 1/4), so
sum_A a_j^+ <= 3*delta/tau = 3*tau. For tau < c_m/12: 3*tau < c_m/4. Clause (4) holds
strictly.

**A1, clause (3).** For any top support functional phi, by the same bound
sum_{z_j >= tau} a_j^+ <= 3*tau, and by lem-mass-split ("sum_j a_j^+ = 1 + nu_v"):
sum_{z_j < tau} a_j^+ = (1 + nu_v) - sum_{z_j >= tau} a_j^+ >= 1 - 3*tau > 1 - c_m
whenever 3*tau < c_m; tau < c_m/12 suffices. Clause (3) holds strictly.

**A2, forward.** If L2-core holds with delta_0', then for delta <= delta_0' no
configuration satisfies clause (2) + tallness at all, so the simultaneous conjunction
of (1)-(4) is vacuously excluded: L2-v2 holds with any c_m in (0,1), delta_0 = delta_0'.
[Clause (2) "always-tight hulls at v intersect" = K_T ∩ K_O nonempty = existence of an
alpha-free display, by lem-optimal-face-conic-reduction contract: "a display with all
a_z = 0 exists if and only if conv{p_f - p_u : f in T} intersects
t*(u)*conv{p_i - p_u : i in O}"; its hypotheses "hidden geometrically distinct row
vertex u ... with t*(u) > 0" hold at u = v by A1 clause (1).]

**A2, backward.** Assume L2-v2 with (c_m, delta_0); let delta_0' =
min(delta_0, (c_m/12)^2, 1/4) and suppose for contradiction some P with
0 < delta <= delta_0', W nonempty, hidden top v, H > 16*tau, and K_T ∩ K_O nonempty.
By A1, clauses (1), (3), (4) hold; clause (2) holds by assumption; so P realizes the
configuration L2-v2 forbids at delta <= delta_0 — contradiction. Hence L2-core holds
with delta_0'. QED A.

### §2.2 A3(ii): averaging vacuity (the S3 split is degenerate)

Let phi_1, ..., phi_k be top support functionals, phi-bar = sum c_i phi_i a convex
average. By lem-top-support-dual-face ("on the row set Phi_v is exactly {phi_y ...}")
pick y_i in Y_v with phi_i = phi_{y_i} on rows; let ybar = sum c_i y_i. Then
||ybar||_inf <= 1 (convexity of the l-infty ball) and, since h_C is convex
(a supremum of linear functions):

    ybar.p_v - h_C(ybar) >= sum c_i (y_i.p_v - h_C(y_i)) = H,

while the reverse inequality holds because H is the maximum of y.p_v - h_C(y) over
||y||_inf <= 1 [that maximum equals H: for y in Y_v the value is H by definition, and
no y with ||y||_inf <= 1 exceeds H since y.p_v - h_C(y) <= y.p_v - y.c <=
||p_v - c||_1 for every c in C_W, hence <= d(p_v, C_W) = H]. So ybar in Y_v. On rows,
z-bar_j = H - phi-bar(p_j) = sum c_i (H - phi_i(p_j)) = sum c_i y_i.(p_v - p_j)
= ybar.(p_v - p_j) = z_j(ybar) (using (P-iv) for each i). Hence phi-bar and the single
top support functional phi_{ybar} induce identical top-deficits on every row: every
clause of L2-v2 (and every predicate of the W54 tree) evaluated on averages is already
evaluated on Phi_v. QED A3(ii). [A3(i) is the arithmetic of §2.1: at
delta < (c_m/12)^2 < (c_m/3)^2 no phi or average can carry >= c_m/4 (a fortiori
>= c_m) of a_j^+-mass at z >= tau.]

### §2.3 Theorem B

**B1.** By lem-optimal-face-conic-reduction (contract quoted in §2.1; hypotheses:
exposedness LP at hidden geometrically distinct row vertex v, t*(v) > 0 from A1), the
intersection gives a display (INT) with lambda a probability on T, gamma a probability
on O, and the contract identifies these displays as "the reduced optimal hiddenness
dual witnesses". Setting alpha = 0, beta = t*gamma: sum_i beta_i = t* < kappa = tau/4
(A1). supp lambda subset of T subset of F_v (lem-always-tight-dual-support contract:
"T, O, Z are the rho-far, upper-box, and lower-box constraint families tight on the
WHOLE primal optimal face"). This is a hiddenness dual witness in the sense of
lem-hiddenness-dual-witness with sum beta < kappa = tau/4, i.e. a small-beta witness
in the verifier-mandated reading (FINDINGS 2026-07-09 W53).

**B2.** Summing (INT): b - p_v = t*(q - p_v). q is a convex combination of rows, so
||q - p_v||_1 <= sum_i gamma_i ||p_i - p_v||_1 <= D (row diameter). Hence
||b - p_v||_1 = t*||q - p_v||_1 <= t*D < kappa*D = (tau/4)(2 + 4*delta)
= (1/2 + delta)*tau.

**B3.** Let h be admissible at v; h affine with h(p_v) = 0, so for any row j,
h(p_j) equals the linear part of h applied to (p_j - p_v). Applying that linear part
to both sides of (INT): sum_f lambda_f h(p_f) = t* sum_i gamma_i h(p_i). The right
side lies in [0, t*] since 0 <= h <= 1 on rows; the left side is a nonnegative
combination of nonnegative terms. QED B3.

**B4.** For y in Y_v: sum_f lambda_f z_f(y) = y.(sum_f lambda_f (p_v - p_f))
= y.(p_v - b) <= ||y||_inf ||p_v - b||_1 <= t*D < (1/2 + delta)*tau, by B2. Markov on
the nonnegative z (P-ii): lambda{z_f(y) >= c*tau} <= t*D/(c*tau) <
kappa*D/(c*tau) = (1/2 + delta)/c. The average clause is A3(ii). QED B4.

**B5.** By (P-ii), H - d_f <= z_f(y) for any fixed y in Y_v (nonempty by (P-iv)), so
sum_f lambda_f (H - d_f) <= sum_f lambda_f z_f(y) <= t*D by B4. Markov (each
H - d_f >= 0 since H is the max depth): lambda{d_f <= H - c*tau} <= t*D/(c*tau)
< (1/2 + delta)/c. At c = 4, delta <= 1/4: 1 - (1/2 + delta)/4 >= 1 - (3/4)/4 = 13/16.
[Cross-check: lem-top-witness-third-actor contract, applicable by B1: "at c = 4 more
than 13/16 of lambda sits on rho-far rows of depth > H - 4*tau" — same constant;
lem-hiddenness-depth-markov gives the c-parametric form.] QED B5.

**B6.** Fix f_0 in supp lambda. By l1/l-infty duality pick u with ||u||_inf <= 1 and
u.(p_{f_0} - p_v) = ||p_{f_0} - p_v||_1 >= 4*tau (f_0 in F_v). Then
sum_f lambda_f u.(p_f - p_v) = u.(b - p_v) <= ||b - p_v||_1 <= t*D. If every
f in supp lambda had u.(p_f - p_v) > t*D, the lambda-average would exceed t*D;
so some f_1 in supp lambda has u.(p_{f_1} - p_v) <= t*D. Then
||p_{f_0} - p_{f_1}||_1 >= u.(p_{f_0} - p_{f_1}) >= 4*tau - t*D
> 4*tau - (1/2 + delta)*tau = (7/2 - delta)*tau. QED B6, QED Theorem B.

### §2.4 Proposition D

B4 is proved above and holds for every y in Y_v; by A3(ii) the class {top support
functionals and their finite convex averages} induces on rows exactly {z(.)(y) : y in
Y_v}. So the supremum over the whole class of the lambda-average deficit equals
sup_{y in Y_v} y.(p_v - b) = Z_v(b) <= t*D (B2 + Hoelder), an identity-level cap:
no tallness, no constants, no escape. D1 follows since a contradiction against the
plateau clauses through lambda would need lambda-mass >= 1/2 + delta at deficit
>= tau under some member of the class, which B4 forbids. For D2: Z_v is a supremum of
linear functions of x, hence convex; Cyl_v(eps) = {Z_v < eps} is a convex set
containing p_v (Z_v(p_v) = 0); B2 places b in Cyl_v((1/2 + delta)*tau + eps') even
when every single far row is excluded from Cyl_v(c_3*tau) — no contradiction is
generable from pointwise exclusion plus the display. [Corroborating wall, not used as
premise: FINDINGS 2026-07-09 / lem-top-support-dual-face consumer note (V-L3 finding
5): "pointwise cylinder exclusion does NOT upgrade to a simultaneous
one-phi-for-a-set statement by averaging".] D3 is the disjunction of what remains:
the only quantities not capped by B2-B6 are v's own coefficients a_j^+, row
reproduction at rows other than v, and the always-tight/visible structure. QED D.

### §2.5 Theorem C

Assume conj-summit-cylinder-exclusion with constants (c_3, delta_0(L3)), an L2-core
configuration with delta <= min(1/4, delta_0(L3)), and omega_v <= c_3 -
(16/13)(1/2 + delta). Let L = {f in supp lambda : d_f > H - 4*tau}. By B5,
lambda(L) > 13/16. Every f in L has ||p_f - p_v||_1 >= 4*tau (supp lambda subset of
F_v, B1) and d_f > H - 4*tau > H - 8*tau, so f is in the conjecture's domain
("every row f with ||p_f - p_v||_1 >= 4*tau and dist_1(p_f, conv{p_w : w in W}) >
H - 8*tau"), and the conjecture yields Z_v(f) >= c_3*tau, i.e. some y_f in Y_v with
y_f.(p_v - p_f) >= c_3*tau. [Y_v is compact — closed and bounded in the l-infty ball
intersected with the affine-hull-relevant subspace — so the sup is approached within
any eps; run the argument with c_3 - eps and let eps -> 0 at the end if attainment is
questioned.] Fix any y_0 in Y_v. For f in L:

    z_f(y_0) = y_f.(p_v - p_f) - (y_f - y_0).(p_v - p_f)
             >= c_3*tau - omega_v*tau            (definition of omega_v, f in B_v).

Then by B4: (1/2 + delta)*tau > t*D >= sum_f lambda_f z_f(y_0)
>= lambda(L) * (c_3 - omega_v)*tau > (13/16)(c_3 - omega_v)*tau. Hence
c_3 - omega_v < (16/13)(1/2 + delta), i.e. omega_v > c_3 - (16/13)(1/2 + delta) —
contradicting the assumed narrowness. If Y_v = {y_0} is a singleton then omega_v = 0
and the contradiction needs only c_3 >= (16/13)(1/2 + delta). QED C.

### §2.6 SL1 implies L2-core (hence L2-v2)

Assume SL1 with its delta_0; suppose an L2-core configuration with delta <=
min(delta_0, 1/4) exists. Its display lambda satisfies: (a) supp lambda subset of
T subset of F_v (B1); (b) by B2, ||b - p_v||_1 <= t*D < (1/2 + delta)*tau; (c) by B5,
lambda{d_f > H - 4*tau} > 13/16; (d) by B3, sum lambda_f h(p_f) <= t* < kappa for
every admissible exposer h. So lambda is exactly an object SL1 forbids —
contradiction. Hence no L2-core configuration exists at delta <= min(delta_0, 1/4):
L2-core holds, and by Theorem A2 (forward) L2-v2 holds. QED.

### §2.7 The case split: SL1a AND SL1b imply SL1

Let lambda satisfy SL1(a)-(d) for some P, v with delta <= 1/4, H > 16*tau. Put
L = {f in supp lambda : d_f > H - 4*tau}, S = supp lambda \ L,
mu = lambda(S) < 1/8 + delta/4 <= 3/16 [by (c): mu < 1 - 13/16 = 3/16; the sharper
(1/2+delta)/4 form holds when lambda is a display, by B5 — for a bare SL1 object use
(c) directly: mu <= 3/16].

**Case (i): mu <= tau/D.** Define the conditional probability lambda_L(f) =
lambda_f / lambda(L) on L. Barycenter: with beta := b - p_v, beta_L := b_L - p_v,
beta_S := b_S - p_v (b_L, b_S the conditional barycenters),
(1 - mu) beta_L + mu beta_S = beta, so
||beta_L|| <= (||beta|| + mu*||beta_S||) / (1 - mu)
<= ((1/2 + delta)*tau + (tau/D)*D) / (13/16)
= (16/13)(3/2 + delta)*tau <= (28/13)*tau < 2.2*tau         (delta <= 1/4).
Exposer average: for admissible h, sum_{f in L} lambda_L(f) h(p_f) <=
(sum_f lambda_f h(p_f)) / lambda(L) <= kappa / (13/16) = (16/13)*kappa (h >= 0 on
rows, so dropping S only decreases the numerator). Every f in L is rho-far from v
(SL1(a)) and at depth > H - 4*tau. So lambda_L is exactly an object SL1a forbids.

**Case (ii): mu > tau/D.** Take mu_S = lambda restricted to S: a sub-probability of
mass mu in (tau/D, 3/16] supported on rows with ||p_f - p_v||_1 >= 4*tau (SL1(a)) and
d_f <= H - 4*tau, with sum_f mu_S(f) h(p_f) <= sum_f lambda_f h(p_f) <= kappa for
every admissible h (again h >= 0 on rows). So mu_S is exactly an object SL1b forbids.
[The per-row universal-shadow pin stated in §1 is the same inequality read at a
singleton: lambda_f h(p_f) <= kappa for each f, so sup_h h(p_f) <= kappa/lambda_f.]

The two cases are exhaustive and each contradicts its sub-leaf: SL1a AND SL1b imply
SL1. Combined with §2.6: **SL1a AND SL1b imply L2-v2**, with explicit constants
(co-top radius 2.2*tau, exposer bound (16/13)*kappa, counterweight mass window
(tau/D, 3/16]). QED.

### §2.8 Proposition E (cap-consistency of the shallow counterweight)

Consider weights lambda = (1 - m) delta_{f_E} + m delta_{f_W} with
||p_{f_E} - p_v||_1 = 4*tau, d_{f_E} = H (deep pole), and f_W placed so that
(1 - m)(p_{f_E} - p_v) + m(p_{f_W} - p_v) = 0, i.e.
||p_{f_W} - p_v||_1 = (1 - m)*4*tau/m; feasibility ||p_{f_W} - p_v||_1 <= D forces
m >= 4*tau/(D + 4*tau) ~ 2*tau. Take m = 4*tau/(D + 4*tau) and d_{f_W} = 0 (fully
shallow, hence ||p_{f_W} - p_v||_1 >= H - 0 > 16*tau >= 4*tau: f_W in F_v). Check the
banked caps at t* = kappa (worst case):
- B2: barycenter displacement 0 <= t*D. Saturated trivially.
- B5 expectation: m*(H - 0) <= t*D = (1/2 + delta)*tau requires
  H <= (1/2 + delta)*tau/m = (1/2 + delta)(D + 4*tau)/4, which at small tau is
  ~ (1/2)(2)/4 + O(tau, delta) = 1/4 + o(1). So for absolute height H < ~1/4 the
  depth-deficit budget ACCEPTS a fully shallow counterweight; the budget is spent
  exactly (the configuration is extremal for B5).
- B5 Markov at every c: lambda{d <= H - c*tau} = m for c <= H/tau, and
  m < (1/2 + delta)/c for all c <= H/tau iff m < (1/2 + delta)*tau/H — same condition.
- (c) third-actor mass: 1 - m > 13/16 holds for tau < 3/32*(D + 4*tau)/... — amply,
  since m ~ 2*tau.
What BLOCKS it is only SL1(d)/B3: an admissible exposer h with h(p_{f_W}) close to 1
would give sum lambda h >= m*h(p_{f_W}) ~ 2*tau > kappa = tau/4. So the escape needs
sup over admissible h of h(p_{f_W}) <= kappa/m ~ 1/8: the counterweight must sit in
the 1/8-low slab of EVERY admissible exposer at v ("universally shadowed") despite
being shallow (l1-near C_W at distance H from v). No banked shard forbids such a row;
no banked instance realizes one. This is exactly SL1b's content. Consequences (a)-(c)
of §1 follow. NOTE the honest scope: the two-point system is a weight assignment
satisfying the proved caps, NOT an exact signed idempotent — Proposition E refutes
only the INFERENCE "B2 + B5 + third-actor force a co-top straddle", and calibrates
what SL1b must add. QED E.

## §3 Tools used (proved shards only; clause quoted at point of use)

- lem-top-deficit-price — the subset pairing bound (A1, clauses (3)/(4)); z >= 0 and
  phi(p_j) <= d_j mechanics (P-ii).
- lem-averaged-deficit-charge — the averaging licence (A1 clause (4)); its charge
  arithmetic is re-derived inline where used.
- lem-top-support-dual-face — Phi_v = {phi_y : y in Y_v} on rows; Y_v nonempty;
  Z_v/Cyl_v vocabulary (P-iv, §2.2, Theorem C).
- lem-optimal-face-conic-reduction — the display (INT) and its iff with
  K_T ∩ K_O != {} (A2, B1).
- lem-always-tight-dual-support — supp lambda in T (rho-far family), supp beta in O;
  T, O always-tight on the whole optimal face (B1, R3).
- lem-positive-exposedness-margin — t*(v) > 0, and hidden gives t* < kappa (A1).
- lem-hiddenness-dual-witness — F_v nonempty for hidden v; the witness format (B1).
- lem-hiddenness-depth-markov / lem-top-witness-third-actor — the c-parametric depth
  Markov and the 13/16 constant at c = 4 (B5 cross-check; SL1(c) calibration).
- lem-mass-split — sum a_j^+ = 1 + nu_v (A1 clause (3)).
- lem-harmonic-affine-bridge — affine functionals distribute through rows (P-i).
- def-signed-idempotent / def-negative-mass / def-visible-set / def-exposed /
  def-height — row geometry, scales, exposer/admissibility, height/top conventions.
- NOT used as premises: conj-summit-cylinder-exclusion (hypothesis of Theorem C only),
  lem-bounded-alpha-forced-far-slab (superseded here by B5, which forces far-deep
  witness MASS, not just one actor), lem-received-mass-proximity, lem-cs-low-slab-pincer,
  lem-genuine-disintegration, lem-top-concentration (explored; not needed by the
  final statements).

## §4 Honest assessment

**Weakest step.** Nothing in §2 is deep — every proof is a two-to-ten-line
consequence of banked contracts (a hostile verifier should check: the strictness
bookkeeping in A1/A2; the h >= 0 monotonicity steps in §2.7; Y_v-compactness/
attainment in Theorem C, where I supplied the eps-fallback). The weakness of the
deliverable is structural, and I state it loudly: **after Theorem A, L2-v2 IS
Branch-II tall-emptiness** — the plateau clauses that made the leaf look like a
localized "creative core" are dead weight, so no proof of L2-v2 can be materially
easier than closing the intersection branch of (M2) outright. The tree remains sound
(exhaustiveness is untouched), but the effort estimate for L2 should be revised to
match L6's grade, and the two leaves share their hard core (below).

**Relation to conj-summit-cylinder-exclusion.** Neither reduces to the other. (a) The
sibling does NOT imply L2-v2: Proposition D2 proves the natural reduction route (pair
the exclusion with the witness through a well-chosen phi) is impossible — the
lambda-average deficit is capped at t*D by an identity, so L3's pointwise exclusion is
consistent with every Branch-II configuration. (b) L2-v2 does not imply the sibling
(the exclusion also constrains disjoint-hull configurations). (c) They SHARE the wall:
both must break z-flatness of far-deep structure using exact idempotence (the sibling
against its verified 4-point l1 witness; L2 against the counterweight/straddle
freedom), and Theorem C is the precise partial reduction: sibling + narrow dual face
(omega_v <= c_3 - (16/13)(1/2 + delta)) closes L2-core. The joint residual is the
wide-dual-face summit — I recommend the architect treat "omega_v bounded" as a new
named sub-question feeding BOTH leaves.

**Whether mutual-exposure rigidity materialized.** Partially, with a correction. The
Branch-II display does force a straddling far witness (B2, B6), and in Case (i) of
§2.7 it is a genuinely CO-TOP straddling family — SL1a is, up to constants, the same
object as the L6 attack's residual web (its §4: barycenter within
(1/2+delta)*tau + 4*tau*(sum a_z) of p_v; here sum a_z = 0 and radius 2.2*tau after
conditioning), so ONE rigidity theorem at radius O(tau), depth band 4*tau, exposer
budget O(kappa) closes the creative cores of BOTH branches. But Proposition E shows
the pure co-top form is NOT forced: a fully shallow counterweight of mass ~ 4*tau/D
passes every mass/depth cap whenever H < ~1/4 (exactly the delta -> 0 regime), and is
blocked only by the universal-shadow pin — hence the L6-style rigidity statement must
be paired with SL1b, or stated with the exposer-defeat clause included. The
convergence hint's statement, as phrased ("all near top depth"), would be REFUTED as
a claimed forced structure, though not as a sufficient target.

**Also delivered to the architect.** (1) The S3 split of the tree is degenerate
(A3(ii)): Q3-v2 = Q2 at threshold c_m/4; the tree can delete S3 without loss. (2) B6's
scale gap: straddle antipodes are forced only at (7/2 - delta)*tau < rho — any
rigidity statement quantified over "mutually rho-far" families has a hole at exactly
the exemption radius; use barycenter-radius formulations instead (as SL1a does).
(3) B5 strengthens the depth picture from Markov to an EXPECTATION bound
(sum lambda (H - d) <= t*D < (1/2+delta)*tau), which is what makes the counterweight
budget exactly computable.

**The single decisive next question.** SL1b, then SL1a — in that order. SL1b is the
new, small, well-shaped target: *can a shallow row (d <= H - 4*tau), rho-far from a
tall hidden top v, carry sup_{h admissible at v} h(p_f) <= kappa/mass with mass >
tau/D — i.e. sit in the deep shadow of EVERY exposer of v while being l1-close to the
visible hull?* Intuition against: shallow rows live near C_W, and C_W's own visible
vertices are kappa-exposed with margin >= kappa (def-visible-set), so exposers adapted
to the C_W region should be able to lift any shallow far row; but "adapted" exposers
must stay >= 0 on ALL rows including behind v, and no banked lemma performs that
lift — it is a genuine LP-geometry question, plausibly decidable by the same
complementarity toolkit that produced lem-always-tight-dual-support. If SL1b falls,
everything concentrates in SL1a = the unified co-top rigidity: prove that a probability
on rho-far co-top rows with barycenter within 2.2*tau of p_v and universal exposer
average <= (16/13)*kappa is impossible at H > 16*tau. That single statement now closes
the creative core of BOTH W54 branches; it is exactly the "tall-construction problem"
in dual form, and it is where all remaining hardness of (M2) lives on the intersection
side.
