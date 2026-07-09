# W56 (round 2) — Tier-2 decomposition of SL1a

AUTHOR-CLAIM strategy material only.  Nothing in this file promotes SL1a or any new
leaf.  The only established inputs used below are registry shards whose front matter
says `status: proved`; every such use quotes the consumed clause at the point of use.
All measures are measures on row **points** (equal row points are coalesced), all
support language is geometric, and all constants are independent of the number of rows.
This document is self-contained and supersedes the round-1 `DECOMPOSITION.md`; material
that survived the round-1 hostile verification (the L-S/L-C/L-P pipeline mechanics, the
assembly arithmetic, all shard quotes) is reused deliberately and is so marked.

## §1 THE PINNED TARGET

> (CONJECTURE) Co-top straddling-web exclusion (SL1a): there exists universal
> delta_0 > 0 such that no exact signed idempotent P with 0 < delta(P) <= delta_0,
> nonempty visible set, and hidden top vertex v of height H > 16*tau admits a
> probability measure lambda on rows that are simultaneously rho-far from v
> (||p_f - p_v||_1 >= 4*tau) and co-top
> (dist_1(p_f, conv W) > H - 4*tau), with barycenter within 2.2*tau of p_v and with
> average value <= (16/13)*kappa under every admissible exposer at v.
>
> — `conj-straddling-web-exclusion` (verbatim contract; `status: conjecture`)

Here `delta = delta(P)`, `tau = sqrt(delta)`, `rho = 4*tau`,
`kappa = tau/4`, `D = 2+4*delta`, `W` is the visible set,
`C_W = conv{p_w : w in W}`, `d(x) = dist_1(x,C_W)`, and
`H = max_j d(p_j)`.  An admissible exposer at `v` is affine, is zero at `p_v`, and
takes values in `[0,1]` on every row point.  Write

    B_v := {x : ||p_x - p_v||_1 >= 4*tau  and  d_x > H - 4*tau}

for the far co-top set, so an SL1a web is a probability measure `lambda` with
`supp(lambda) subset of B_v`, barycenter `b` obeying `||b - p_v||_1 <= 11*tau/5`, and
`lambda`-average `<= 4*tau/13` under every admissible exposer at `v` (the constants
`2.2*tau = 11*tau/5` and `(16/13)*kappa = 4*tau/13` are exact conversions).

### §1.0 The barycenter identity (proved inline; three lines)

Every clause SL1a imposes on `lambda` depends on `lambda` only through its barycenter
`b` and the support condition `supp(lambda) subset of B_v`.  Indeed, an admissible
exposer `h` is affine, so `integral h(p_x) dlambda(x) = h(b)`; likewise every affine
test used anywhere below has `lambda`-mean equal to its value at `b`.  Consequently:
(i) two webs with the same barycenter and support set are interchangeable in every
statement of this document; (ii) selecting a row of `supp(lambda)` at or below the mean
of an affine score is always possible and requires no tie-breaking rule of any kind.
This identity is used to discharge the round-1 verifier's finding 3 (nondeterministic
selection): all selections below are packaged EXISTENTIALLY, and the terminal leaf
excludes EVERY legal selected tuple (§2.1, §4).

### §1.1 Standing proved inputs

The following are the only non-elementary established inputs used by the leaves or the
assembly.  (These quotes are carried over from round 1, where a hostile verifier opened
all cited shards and confirmed clause fidelity.)

* `lem-top-deficit-price` (`status: proved`) supplies "a top support functional `phi`
  (affine, `phi(p_v) = H`, `phi <= 0` on `conv{p_w : w in W}`, 1-Lipschitz for
  `l1`)" and, for every such `phi`, "`z_j = H - phi(p_j) >= 0`."  The locked row
  geometry in `def-signed-idempotent` says that pairwise row distances are at most
  `D = 2+4*delta`; hence `0 <= z_j <= D`.  Also, directly from the quoted support
  properties, `phi(p_j) <= d_j`, so

      H - d_j <= z_j <= D.                                      (1.1)

  Thus `z/D` is an admissible exposer at `v`, and `z_j < 4*tau` implies
  `d_j > H - 4*tau` strictly.
* `lem-harmonic-affine-bridge` (`status: proved`) says: "a vector `g` satisfies
  `Pg = g` if and only if there exists `u` with `g_i = u . p_i` for every row
  index `i`," and "the constant term of any affine representation is absorbable into
  `u` since all row sums equal 1."  Thus every affine row-value function distributes
  through **each** row reproduction; below this is used at selected web rows and at
  corner rows, never only at `v`.
* `lem-mass-split` (`status: proved`) gives the exact row identity
  "`sum_j a_j^+ = 1 + nu_v`."
* `lem-positive-exposedness-margin` (`status: proved`): "for an exact signed
  idempotent P with rho = 4*tau > 0 (i.e. delta(P) > 0) and a geometrically distinct
  row vertex v with nonempty far set F_v = {j : ||p_j - p_v||_1 >= rho}: t*(v) > 0;
  in particular every HIDDEN geometrically distinct row vertex with F_v nonempty has
  0 < t*(v) < kappa."  Together with elementary relative-interior existence for a
  nonempty finite LP optimum, this permits a relative-interior optimal exposer at any
  hidden geometrically distinct row vertex with nonempty far set.
* `lem-always-tight-dual-support` (`status: proved`): "every optimal hiddenness dual
  witness (lambda, alpha, beta), after deleting redundant centered-zero constraints,
  has supp(lambda) contained in T, supp(beta) contained in O, and supp(alpha)
  contained in Z, where T, O, Z are the rho-far, upper-box, and lower-box constraint
  families tight on the WHOLE primal optimal face; T is nonempty, and O is nonempty
  if and only if t*(u) > 0."
* `lem-optimal-face-conic-reduction` (`status: proved`): the reduced optimal
  witnesses are exactly the displays

      sum_T lambda_f*(p_f - p_u) + sum_Z a_z*(p_z - p_u)
        = t*(u)*sum_O gamma_i*(p_i - p_u),                      (1.2)

  "with lambda and gamma probability vectors supported on T and O and coefficients
  a_z >= 0 supported on Z", and "a display with all a_z = 0 exists if and only if
  conv{p_f - p_u : f in T} intersects t*(u)*conv{p_i - p_u : i in O}."
* `lem-separator-zero-face-obstruction` (`status: proved`): for the exposedness LP at
  a hidden geometrically distinct row vertex `u` with `0 < t*(u) < inf`, a
  relative-interior optimal exposer `h*`, nonempty `T, O`, and disjoint hulls: "for
  every strict linear separator ell and every m with max over i in O of
  ell(p_i - p_u) < m < (min over f in T of ell(p_f - p_u))/t*(u), the affine
  direction psi(p) = ell(p - p_u) - m*h*(p) satisfies psi(p_u) = 0, P psi = psi on
  row values, psi(p_f) > 0 for all f in T, psi(p_i) < 0 for all i in O, and there
  exists a nonclone row z with h*(p_z) = 0 and psi(p_z) < 0."
* `lem-zero-face-capacity-kill` (`status: proved`): for a hidden geometrically
  distinct row vertex `u`, an optimal exposer `h*` at `u`, a row `z` with
  `h*(p_z) = 0`, and `c_r > 0` with kappa-high shipping `>= c_r`:
  "`c_r*kappa <= nu_z <= delta(P)`", and "no such configuration exists for
  `0 < delta < (c_r/4)^2`."

Two further proved clauses are walls, not positive inputs.  The exact relevant clause
of `lem-intersection-witness-confinement` (`status: proved`) is: "(B3) for every
admissible exposer `h` at `v`, `sum_f lambda_f*h(p_f) <= t*(v)`; (B4) for every top
support functional `phi` at `v` and every finite convex average,
`sum_f lambda_f*(H - phi(p_f)) <= t*(v)*(2+4*delta) < (1/2+delta)*tau`."  The exact
relevant clause of `lem-l2-core-collapse` (`status: proved`) is: "every finite convex
average of top support functionals at `v` coincides ON THE ROW SET with a single top
support functional `phi_ybar`."  Accordingly no edge below tries to obtain a
contradiction from `(lambda, Phi_v)` pairings or from averaged top faces.

### §1.2 Kernel and fiber conventions

All sums such as `P_fx^+` are aggregated over the full fiber of the row point `x`; a
split of one row point into clones merely splits that mass.  A vertex kernel is a
probability kernel `xi_x(u)` from row points `x` to the geometrically distinct row
vertices `u` with `p_x = sum_u xi_x(u)*p_u`, chosen identically on clone fibers, and
equal to the Dirac kernel `xi_u(u) = 1` at every vertex point.  The two-stage measure
used below retains both coordinates:

    Gamma_f(x,u) := P_fx^+ * xi_x(u).                          (1.3)

It is coefficient mass on an actual row point followed by convex disintegration, not
literal transition mass `P_fu^+` (except on the diagonal, where the Dirac convention
makes it exactly that).  Keeping `(x,u)` rather than only its `u`-marginal is the
convention that prevents the W55 carrier error and makes clone invariance explicit.
No statement below distinguishes one kernel: every leaf that consumes a kernel is
quantified over ALL kernels obeying this convention (round-1 finding 3, repaired at
the source: universal quantification replaces canonicalization, and it is free
because L-C proves its conclusion for every such kernel).

### §1.3 Two clone-invariant integers and the transient-row extension

For an exact signed idempotent `P` let `V(P)` be the number of geometrically distinct
row VERTICES (extreme points of the row polytope after coalescing equal row points)
and `R(P) >= V(P)` the number of geometrically distinct row POINTS.  Both are finite
positive integers, both are invariant under clone splitting (they count distinct
points, never indices), and no constant below ever depends on either — they are used
only through an extremal SELECTION (leaf L-M), which is dimension-free.

For the transient-row red test, the standard exact extension is

    P' = [[P, 0], [mu*P, 0]],                                   (1.4)

with `mu` a probability row: direct multiplication gives `P'^2 = P'`, `P'*1 = 1`, and
the new row's negative mass is `sum_j (mu*P)_j^- <= sum_i mu_i * nu_i <= delta(P)`, so
`delta(P') = delta(P)`.  The stability argument, in full (round-1 finding 7 repaired
by the verifier's own prescription): the appended row point `(mu*P, 0)` is a convex
combination of the embedded old row points `(P_i, 0)`; hence the row polytope is
unchanged up to the isometric embedding that appends one zero coordinate (`l1`
distances preserved), its geometrically distinct vertices are unchanged (a convex
combination is never a new extreme point), the admissible-exposer VALUE profiles on
the old row points are unchanged (an extended admissible exposer restricts to one, and
every old one extends with the new coordinate's coefficient free; its value at the new
row point is the `mu`-convex combination of old values, automatically in `[0,1]`), and
therefore `W`, `C_W`, every `d_j`, and `H` are unchanged.  Old coefficient fibers
acquire a zero new column, so every measure and kernel below lifts with zero mass on
the new coefficient column, and every leaf conclusion lifts verbatim.  Two honest
records: (i) `V(P') = V(P)`, and `R(P') in {R(P), R(P)+1}` (the new point may be new);
(ii) the LIFT direction only — nothing below claims the converse (that deleting a
transient row preserves a web: it need not, since a web may place mass on the appended
row point, whose convex decomposition can leave `B_v`).

## §2 THE DAG

Set once and for all

    delta_bar := 2^(-16),       tau := sqrt(delta),
    D := 2+4*delta,             (16/13)*kappa = 4*tau/13.

The DAG has four routine leaves and one hard terminal leaf:

```text
R   SL1a fails at threshold delta_H  (delta_H = the hard leaf's constant, read first)
|
M   L-M: minimal-witness selection
|        a counterexample P° attaining lex-min (V(P), R(P)) exists
|
S   L-S: score selector on the web of P°
|        f in supp(lambda) with 2*z_f/D + h*(p_f) <= 12*tau/13
|
C   L-C: reproduce at f, retain the coefficient/disintegration coupling
|        Gamma_f(x,u) = P_fx^+ * xi_x(u),  Gamma_f(C_f) > 1/2
|        (for EVERY legal kernel xi)
|
P   L-P: radial split of the coupled co-top corner
|        far-u mass >= 1/4 (label F) XOR near-u mass > 1/4 (label N)
|
H   H-W: minimal-counterexample corner-web exclusion  [HARD]
|        antecedent = the FULL SL1a data (P°, v, lambda verbatim)
|        + lex-minimality + (phi, h*, f, xi, corner, horn label)
X   contradiction
```

The corner in the tree is

    C_f := {(x,u) : z_x < 4*tau, h*(p_x) < 4*tau,
                    z_u < 4*tau, h*(p_u) < 4*tau}.              (2.1)

By (1.1), both coordinates of every pair in `C_f` have depth strictly above
`H - 4*tau`, and `u` is a hidden geometrically distinct row vertex.

### §2.1 Routing: at least one path, every tuple killed (round-1 finding 3 repaired)

The routing claim of this decomposition is exactly the following, and no more.

**(R-a) Existence.**  For every SL1a counterexample class member at `delta <= delta_H`
there exists AT LEAST ONE complete legal tuple
`(P°, v, lambda, phi, h*, f, xi, sigma)`: L-M supplies a lex-minimal counterexample
`P°` (with SOME admissible `(v, lambda)` fixed arbitrarily), `phi` exists by
`lem-top-deficit-price`, `h*` exists by `lem-positive-exposedness-margin` plus
relative-interior existence, `f` exists by L-S, a kernel `xi` exists by finite-polytope
convexity, the corner property holds by L-C for that (indeed every) kernel, and L-P
assigns THAT tuple exactly one horn label.

**(R-b) Universality.**  Different legal choices of `phi`, `h*`, `f`, `xi` are
permitted to produce different corner measures and OPPOSITE horn labels.  No
canonical choice, tie-breaking rule, or raw ordering is used anywhere (a raw ordering
would violate the clone wall).  Instead the terminal leaf H-W quantifies over every
legal tuple: its antecedent contains the tuple existentially, parameterized by the
horn label, so H-W excludes ALL legal tuples simultaneously.  The assembly needs only
(R-a) existence + (R-b) universality; the round-1 claim of exactly-once routing is
withdrawn as both false and unnecessary.

**Boundary ownership** (all owned boundaries; round-1 finding 15 conventions kept):
far `u` owns equality at `||p_u - p_v||_1 = 4*tau`; the far horn owns mass equality at
`1/4`; inside H-W, the diagonal cell owns equality at half the horn mass, the
intersection type owns hull tangency AND mass equality at `1/16`, and the capacity
side owns blocker-shipping equality at `1/16`.  These are boundaries of predicates
evaluated AFTER a tuple is fixed; by (R-b) no seam claim across tuples is made.

## §3 THE LEAVES

Every statement below is one candidate registry contract.  "May consume" contains only
registry shards whose front matter says `status: proved`; contextual gadgets and census
data occur only in the red tests.

### L-M — minimal-witness selection

**Statement (one sentence).**  For every `d_0 > 0`: if some exact signed idempotent
`P` with `0 < delta(P) <= d_0`, nonempty visible set, and hidden top vertex `v` of
height `H > 16*tau` admits a probability measure `lambda` on rows that are rho-far
from `v` and co-top (`d > H - 4*tau`) with barycenter within `11*tau/5` of `p_v` and
average value at most `4*tau/13` under every admissible exposer at `v`, then among all
such `P` there is one attaining the lexicographic minimum of `(V(P), R(P))`.

**May consume.**  None (first principles).

**Mechanism.**  The set `S = {(V(P), R(P)) : P as above}` is a nonempty subset of
`N x N`.  Its first-coordinate projection has a least element `V°`; among the pairs
with first coordinate `V°` the second coordinates have a least element `R°`; some `P`
realizes `(V°, R°)`.  This is well-ordering of the naturals, twice.  No compactness,
no limit, no attainment question: the minimized quantities are integers.

**Grade: EASY.**  Two applications of well-ordering.

**Risk / exact-instance kill criterion.**  The only conceivable attack is on
well-definedness of `V, R` (they are counts of geometrically distinct points, defined
after coalescing equal row points — `def-signed-idempotent`'s row-point vocabulary) or
on emptiness of `S` (then the lemma is vacuously true).  No exact instance can refute
a selection principle.

**Mandatory red tests.**  **Proposition E:** PASS — the class definition carries
SL1a's strict co-top support clause verbatim, so the shallow counterweight system is
not in the class and cannot be selected.  **W55 starvation gadget:** NOT APPLICABLE,
honestly recorded — the gadget is a partial tableau, not an exact signed idempotent
with the class geometry, so it is not a member of `S`'s index class and the selection
is unaffected.  **Clone/transient:** PASS — `V, R` are counts of distinct points,
invariant under clone splitting; the extension (1.4) leaves `V` unchanged and changes
`R` by at most one, so `S` changes representatives but not nonemptiness, and the
minimum is still attained.  **Coverage:** PASS — every banked family fails the
tallness clause, so `S`'s known part is empty; the selection is invoked only inside a
proof by contradiction.

**Restatement test: PASS.**  A selection principle with no exclusion content; it
implies nothing about SL1a, L2-core, or the huddle charge.

### L-S — score selector

**Statement (one sentence).**  For every exact signed idempotent `P` with
`0 < delta(P) <= 1/4`, nonempty visible set, and hidden top vertex `v` of height
`H > 16*tau`, every probability measure `lambda` supported on
`B_v = {x : ||p_x - p_v||_1 >= 4*tau and d_x > H - 4*tau}` whose integral under every
admissible exposer at `v` is at most `4*tau/13`, every top support functional `phi`
at `v`, and every admissible exposer `h` at `v`, admit a row point
`f in supp(lambda)` such that, with `z = H - phi` and `D = 2+4*delta`,
`2*z_f/D + h(p_f) <= 12*tau/13`.

**May consume.**  `lem-top-deficit-price` only.

**Mechanism.**  At the point of use, the exact `status: proved` clause from
`lem-top-deficit-price` is: "there exists a top support functional `phi` (affine,
`phi(p_v) = H`, `phi <= 0` on `conv{p_w : w in W}`, 1-Lipschitz for `l1`), and for
ANY such `phi`, writing `a_j = P_vj` and `z_j = H - phi(p_j) >= 0`."  The row-diameter
bound gives `z <= D`, so `z/D` is admissible and, using the exposer clause twice
(at `z/D` and at `h`) with the barycenter identity of §1.0,

    integral (2*z/D + h) dlambda = (2*z/D + h)(b)
       <= 2*(4*tau/13) + 4*tau/13 = 12*tau/13.                 (3.1)

Choose `f` with score at most this mean (a mean over a probability measure is attained
or undercut on the support).  This is one application of a proved support-functional
clause followed by scalar averaging.

**Change from round 1, accounted (verifier finding 4).**  Round 1's second conclusion
— an antipode `e in supp(lambda)` with `||p_f - p_e||_1 >= 9*tau/5`, extracted from
the `11*tau/5` barycenter clause — is DELETED, because no downstream consumer used it
(it was a decoration on the hard leaf).  Nothing is lost: the hard leaf now retains
`lambda` and its barycenter clause VERBATIM (§3 H-W), so the full barycenter
information — of which the antipode was a two-line corollary via `l1`-duality — is
available to the hard leaf's prover on demand, at exactly the strength SL1a grants.
Accordingly L-S's hypotheses no longer mention the barycenter at all; the `9*tau/5`
constant disappears from this document, and the `11*tau/5` constant now enters only
through the hard leaf's verbatim antecedent.

**Grade: EASY.**

**Risk / exact-instance kill criterion.**  The attack points are the normalization
`z/D` (kill: exhibit a row with `z` outside `[0, D]`, contradicting (1.1)) and the
mean-selection step (kill: a probability measure whose every support point exceeds
its own affine mean — impossible by finite averaging).  No compactness is used.

**Mandatory red tests.**  **Proposition E:** PASS — the selected row stays in the
strict co-top set `B_v`, so the shallow counterweight is not re-admitted.
**W55 starvation gadget:** the literal `A0 = 5, g = 5*tau` tableau does NOT satisfy
L-S's antecedent (it is not an exact idempotent with nonempty visible set and
`H > 16*tau`, and it provides no probability web) — recorded as a definite NO; a
completed co-top analogue would merely receive a selected row, and L-S claims
selection, not a contradiction.  **Clone/transient:** PASS — `lambda` is on row
points and clones split its weight; under (1.4) any persisting antecedent lifts with
zero mass on the new coefficient column, and the same finite average reselects.
**Coverage:** PASS — any first genuine SL1a instance enters L-S; every banked W52
family fails the root tallness test and is not claimed to exercise it.
**Proposition-D/B6 walls:** PASS — the pairing only selects `f`; the later leaf
reproduces at `f`; no pairwise-separation clause of any kind remains in this leaf.

**Restatement test: PASS.**  The conclusion is one row point and one scalar
inequality; it contains no exclusion and cannot imply SL1a, L2-core, or the huddle
charge.

### L-C — coupled coefficient-kernel corner

(Statement, mechanism, and arithmetic UNCHANGED from round 1, where the verifier
independently re-derived every displayed constant — finding 8 — and confirmed every
quoted clause — finding 9.  Restated in full for self-containment.)

**Statement (one sentence).**  For every exact signed idempotent `P` with
`0 < delta(P) <= 2^(-16)`, nonempty visible set, hidden top vertex `v` of height
`H > 16*tau`, top support functional `phi` with `z = H - phi`, admissible exposer `h`
at `v`, row point `f` satisfying `d_f > H - 4*tau`, `||p_f - p_v||_1 >= 4*tau`, and
`2*z_f/D + h(p_f) <= 12*tau/13`, and every vertex kernel `xi` obeying the §1.2
convention (probability weights over geometrically distinct row vertices, Dirac at
vertex points, clone-fiber-constant), the measure `Gamma_f(x,u) = P_fx^+ * xi_x(u)`
satisfies

    Gamma_f{(x,u) : z_x < 4*tau, h(p_x) < 4*tau,
                    z_u < 4*tau, h(p_u) < 4*tau} > 1/2,        (3.2)

and both coordinates of every pair in the displayed set have depth `> H - 4*tau`,
while `u` is a hidden geometrically distinct row vertex.

**May consume.**  `lem-harmonic-affine-bridge`, `lem-mass-split`, and the top-support
clause of `lem-top-deficit-price`.

**Mechanism.**  First the vertexization step, solved inside this leaf: by elementary
finite-polytope convexity the finite row polytope is the convex hull of its
geometrically distinct extreme row vertices, so every row point `p_x` has a
probability representation `p_x = sum_u xi_x(u)*p_u`; any kernel obeying §1.2 realizes
one.  Next, the exact `status: proved` clause of `lem-harmonic-affine-bridge` ("`g`
satisfies `Pg = g` if and only if there exists `u` with `g_i = u . p_i` for every row
index `i`," constants absorbable) applied at the row `f` to the affine functions `z`
and `h`, with `nu_f = sum_x P_fx^-` and `S_f := sum_x P_fx^+*(z_x + h(p_x))`, gives by
sign splitting

    S_f = z_f + h(p_f) + sum_x P_fx^-*(z_x + h(p_x))
        <= z_f + h(p_f) + nu_f*(D+1).                          (3.3)

Because `D >= 2`, the selector score implies

    z_f + h(p_f) <= (D/2)*(2*z_f/D + h(p_f)) <= 6*D*tau/13.    (3.4)

The exact `lem-mass-split` clause "`sum_j a_j^+ = 1 + nu_v`" (read at row `f`) gives
`Gamma_f(1) = 1 + nu_f`.  Affineness of the kernel gives the same moment on both
marginals:

    integral (z_x + h_x) dGamma_f = S_f
      = integral (z_u + h_u) dGamma_f.                         (3.5)

If either coordinate of a pair is outside the corner (2.1), its nonnegative sum
`z + h` is at least `4*tau`.  A union bound using (3.5) twice yields

    Gamma_f(C_f) >= 1 + nu_f - S_f/(2*tau)
      >= 1 - 3*D/13 - tau*(D+1)/2.                             (3.6)

At `tau <= 1/256`, `D <= 2 + 2^(-14) = 32769/16384`, the last expression is at least

    58079731/109051904 = 1/2 + 3553779/109051904 > 1/2.        (3.7)

Finally (1.1) makes `z < 4*tau` imply `d > H - 4*tau` strictly; since
`H - 4*tau > 12*tau > 0`, a vertex there is not visible, hence hidden.

**Grade: MEDIUM.**  Bounded-scope measure bookkeeping; MEDIUM only because keeping
the transition coordinate `x` separate from the vertex coordinate `u` is essential
typing.

**Risk / exact-instance kill criterion.**  A refuter attacks (3.5), the sole
same-kernel step.  An exact instance kills L-C only if it supplies a declared vertex
kernel for which an affine value fails to barycentrically reproduce, or if direct
rational summation gives `Gamma_f(C_f) <= 1/2` while (3.3)-(3.7) all hold.  Either is
a finite exact check.  No step may replace `Gamma_f(x,u)` by `P_fu^+` off the
diagonal or infer row-`u` recurrence.

**Mandatory red tests.**  **Proposition E:** PASS — both coordinates in the
conclusion obey the strict depth band.  **W55 starvation gadget:** the literal
tableau does NOT satisfy the antecedent (not a globally exact idempotent with the
tall visible-hull geometry) — a definite NO; its scalar ledgers CAN satisfy the
conclusion pattern, and L-C correctly excludes nothing.  **Clone/transient:** PASS —
`P_fx^+` is aggregated over full fibers, `xi` is clone-fiber-constant; in (1.4) an
old selected row has zero coefficient in the appended column, and if the new row
participates the two-affine-marginal proof reapplies with it included.
**Coverage:** PASS — the lemma accepts nonvertex intermediate rows; known families
exit at root tallness.  **Proposition-D/W55 carrier walls:** PASS — the new resource
is exact reproduction at the web row `f`; dual multipliers never appear; `(x,u)` is
retained so barycentric mass is never relabelled as flow.

**Restatement test: PASS.**  L-C starts from one selected row and ends with a
two-stage coefficient measure; it has no `lambda`-exclusion conclusion and cannot
recover SL1a, L2-core, or the huddle charge in any short derivation.

### L-P — radial horn partition

**Statement (one sentence).**  For every finite nonnegative measure `Gamma` on pairs
of row points `(x,u)`, every row point `v`, every `tau > 0`, and every measurable set
`C` with `Gamma(C) > 1/2`, exactly one of the boundary-labelled alternatives holds:

    (F) Gamma{(x,u) in C : ||p_u - p_v||_1 >= 4*tau} >= 1/4;

    (N) that far mass is < 1/4 and
        Gamma{(x,u) in C : ||p_u - p_v||_1 < 4*tau} > 1/4.

**May consume.**  None.

**Mechanism.**  If (F) fails, the far mass is strictly below `1/4`, and the near cell
is its complement inside `C`, so its mass exceeds `1/2 - 1/4 = 1/4`.  Equality
belongs to (F).

**Grade: EASY.**

**Risk / exact-instance kill criterion.**  There is no geometric input.  An exact
failure would be three rational inequalities whose sum is an immediate contradiction.

**Mandatory red tests.**  **Proposition E (round-1 finding 6 repaired, wording per
the verifier):** as a STANDALONE leaf L-P has no co-top or depth hypothesis at all;
the Proposition-E two-point counterweight measure can be diagonally lifted to a pair
measure and `C` can be chosen with mass `> 1/2`, so it DOES satisfy L-P's antecedent.
The correct record is therefore: the shallow object satisfies standalone L-P, whose
conclusion is exclusion-free bookkeeping (a horn label), and it is NOT re-admitted
into the assembly because there L-P is fed the specific corner `C_f`, whose
membership predicate carries `z < 4*tau` on BOTH coordinates, which by (1.1) forces
depth `> H - 4*tau` and excludes the shallow counterweight's `d <= H - 4*tau` rows.
**W55 starvation gadget:** a pair measure built from the tableau satisfies the
abstract antecedent and is merely assigned a horn — YES it satisfies, and no
exclusion follows (L-P excludes nothing).  **Clone/transient:** PASS — the predicate
is radial on row points, the quantities are mass sums; splitting atoms or the
extension (1.4) cannot create a boundary gap in a literal two-cell partition.
**Coverage:** PASS — every possible first tall terminal tableau has an assigned
horn, including equality.  **B6:** PASS — no pairwise-separation assertion exists;
only distance of the vertex coordinate from the fixed `v`.

**Restatement test: PASS.**  An abstract measure dichotomy with no matrix exclusion.

### H-W — minimal-counterexample corner-web exclusion  [the single HARD leaf]

**Statement (one sentence, horn-parameterized).**  There exists a universal
`delta_H in (0, 2^(-16)]` such that, for each horn label `sigma in {F, N}`, there is
no tuple `(P, v, lambda, phi, h*, f, xi)` in which

  (h1) `P` is an exact signed idempotent with `0 < delta(P) <= delta_H`, nonempty
       visible set, and hidden top vertex `v` of height `H > 16*tau`;
  (h2) `lambda` is a probability measure on row points with
       `supp(lambda) subset of B_v`, barycenter `b` obeying
       `||b - p_v||_1 <= 11*tau/5`, and `h(b) <= 4*tau/13` for every admissible
       exposer `h` at `v`  [the VERBATIM SL1a web clauses, nothing weakened];
  (h3) `P` attains the lexicographic minimum of `(V(P'), R(P'))` over all exact
       signed idempotents `P'` with `delta(P') <= delta_H` admitting some data
       satisfying (h1)-(h2);
  (h4) `phi` is a top support functional at `v` (`z = H - phi`) and `h*` is a
       relative-interior optimal exposer at `v`;
  (h5) `f in supp(lambda)` satisfies `2*z_f/D + h*(p_f) <= 12*tau/13`;
  (h6) `xi` is a vertex kernel obeying the §1.2 convention, and
       `Gamma_f = P_f^+ (x) xi` gives the corner `C_f` of (2.1) mass `> 1/2`;
  (h7) the horn condition holds: for `sigma = F`,
       `Gamma_f{(x,u) in C_f : ||p_u - p_v||_1 >= 4*tau} >= 1/4`; for `sigma = N`,
       that far mass is `< 1/4` and
       `Gamma_f{(x,u) in C_f : ||p_u - p_v||_1 < 4*tau} > 1/4`.

**May consume.**  `lem-positive-exposedness-margin`, `lem-always-tight-dual-support`,
`lem-optimal-face-conic-reduction`, `lem-separator-zero-face-obstruction`,
`lem-zero-face-capacity-kill`, `lem-harmonic-affine-bridge`, `lem-mass-split`,
`lem-top-deficit-price` (all `status: proved`).

**The configuration space, and exactly what was removed (round-1 finding 1
repaired).**  Round 1's hard leaf dropped SL1a's `lambda` and added a free all-row
kernel, so its antecedent ranged over a BROADER class than SL1a's and the leaf
implied SL1a by routine preprocessing — the prohibited restatement.  H-W reverses
the logical direction:

  (a) **Nothing is dropped.**  (h1)-(h2) are SL1a's antecedent verbatim, constants
      untouched (`2.2*tau = 11*tau/5`, `(16/13)*kappa = 4*tau/13`, both `4*tau`
      predicates, `H > 16*tau`).  Every H-W configuration is an SL1a configuration;
      the excluded class is a SUBSET of SL1a's.
  (b) **The matrix class is restricted** to the lexicographically minimal stratum
      (h3): a genuine restriction of the matrix configuration space, giving the
      prover a new weapon absent from SL1a — any construction of an in-class
      counterexample with strictly smaller `(V, R)` is itself a contradiction.
  (c) **The carrier family is restricted** by (h5)-(h7): the matrix must transport,
      from a single score-selected far co-top web row, majority coefficient-kernel
      mass into the doubly-low corner, with a resolved radial vertex profile.  The
      kernel is not free data adjoined to a projection: its corner property is a
      HYPOTHESIS the prover may consume, forced for every kernel by L-C.
  (d) **The logical direction.**  Round-1's H-CCO implied SL1a in one routine
      sentence.  H-W does NOT imply SL1a at all (in any number of routine lines):
      it is SILENT on non-minimal counterexamples and on configurations for which
      the tuple data are not exhibited.  Recovering SL1a from H-W requires L-M,
      L-S, L-C, and L-P — the assembly, four genuine lemmas.  Equivalently: H-W is
      implied by SL1a, not conversely; the decomposition is loss-free — no OPEN
      statement in this document (H-W or any of its descendants) is logically
      stronger than the target.

Three precise senses of "smaller", stated so a verifier can check each: as a class of
tuples, H-W's antecedent class is a strict refinement of SL1a's (every clause of
SL1a's is present, plus (h3)-(h7)); as a class of matrices, it is the lex-minimal
stratum of SL1a's counterexample class; as a logical statement, H-W is weaker than
SL1a, with the difference exactly the four routine leaves.

**Hypothesis-to-consumer table (round-1 finding 4 repaired; every carried hypothesis
has a named consumer in the proof program below).**

| Hypothesis | Consumer in the H-W program |
|---|---|
| (h1) exactness, all rows | reproduction at `f` and at corner rows (SD ledgers); harmonicity of every separator direction `psi_u`; the completion system of H-X |
| (h1) `W != {}`, `H > 16*tau` | carrier hiddenness and `F_u ⊇ W` (SD0); the depth bands; the scale of the H-D1 arithmetic |
| (h2) support in `B_v` | the web-of-corners resource (below): a `7/13`-mass sub-web of reusable corner-builders, all far and co-top |
| (h2) barycenter `11*tau/5` | H-I's near-horn geometry (the second-generation barycenter comparison); re-derivable antipodes on demand |
| (h2) all-exposer `4*tau/13` | the score Markov bound: `lambda{2*z/D + h* > 24*tau/13} < 1/2` (mean `12*tau/13` at `b`, §1.0), i.e. at least `1/2` of the web consists of rows with score `<= 24*tau/13` — the sub-program may draw MANY selected rows, not one (used by H-D and H-X as the web-of-corners resource) |
| (h3) lex-minimality | H-X's surgery route: any negativity-thrifty deletion of freight rows contradicts minimality |
| (h4) `phi`, `h*` fixed | the corner predicates; the inline corner-trap ledgers at rows `f` and `x` |
| (h5) the score | (3.3)-(3.7); the starvation ledger at `f` in H-D |
| (h6) corner `> 1/2` | SD1's diagonal/off-diagonal arithmetic |
| (h7) horn label | ROUTING inside the sub-DAG: `sigma` selects which of the per-horn mechanisms of H-D and H-I fires (far horn: row `v` itself lies in every carrier's far set; near horn: the carriers huddle rho-near `v`) — the label is consumed, not decorative |

One honest flag: the all-exposer clause is consumed above only through two affine
instantiations (the score test and its Markov form).  Its full universal strength is
part of the refuter obligations (§5, witness requirement W3) and is the intended
resource for closing H-I; if a completed proof of H-W never uses more than the two
instantiations, the leaf can be restated with them alone — that would WEAKEN (h2) and
hence strengthen the theorem, and is deferred exactly because the round-1 failure
mode was broadening the hard class prematurely.

**The one-level-deeper decomposition of H-W (round-1 finding 2 repaired: every
descendant is a fully-quantified lemma with hypotheses, conclusion, explicit
constants, and a concrete closing mechanism — no named cells).**

Write PRE(sigma) for the full conjunction (h1)-(h7) at horn label `sigma`, with
`delta_H` replaced by the descendant's own ceiling.  Two proved-inline preliminaries
and two owned splits organize the descendants.

**SD0 (carrier legality — proved inline, four lines).**  Every `u` in the vertex
coordinate of `C_f` has `z_u < 4*tau`, hence by (1.1) `d_u > H - 4*tau > 12*tau > 0`,
so `u` is not visible (visible vertices lie in `C_W` at depth `0`), i.e. `u` is a
hidden geometrically distinct row vertex; moreover every visible row `w` has
`||p_u - p_w||_1 >= dist_1(p_u, C_W) = d_u > 12*tau > 4*tau`, so `W subset of F_u`
and `F_u != {}`.  By the quoted `lem-positive-exposedness-margin` clause ("every
HIDDEN geometrically distinct row vertex with F_v nonempty has 0 < t*(v) < kappa"),
`0 < t*(u) < kappa`; a relative-interior optimal exposer `h_u*` exists; by
`lem-always-tight-dual-support`, `T(u)` is nonempty and (since `t*(u) > 0`) `O(u)` is
nonempty.  Set `K_T(u) = conv{p_r - p_u : r in T(u)}`,
`K_O(u) = t*(u)*conv{p_i - p_u : i in O(u)}`.

**SD1 (diagonal split — owned boundary).**  By the Dirac convention (§1.2), the
diagonal part of the horn-corner cell is the aggregated literal coefficient measure
`u -> P_fu^+` on hidden corner vertices in the horn.  Since the horn cell has mass
`>= 1/4`: either the diagonal mass is `>= 1/8` (equality owned by the diagonal), or
the off-diagonal mass is `> 1/8`.  Off-diagonal pairs have `x` a NON-vertex row point
(a vertex point's kernel is Dirac).

**SD2 (carrier-type split within the diagonal — owned boundary).**  Each corner-horn
vertex `u` has exactly one type: type I if `K_T(u)` intersects `K_O(u)` (tangency and
any common point owned by I), else type D (strict disjointness).  If the diagonal
mass is `>= 1/8`, then either the type-I mass is `>= 1/16` (equality owned by I) or
the type-D mass is `> 1/16`.  These are clone-invariant partitions of vertex points
weighted by fiber-aggregated coefficient mass — no index choice occurs.

**The web-of-corners resource (proved inline, two lines; consumed by H-D/H-X).**  The
score `q = 2*z/D + h*` is a fixed affine test with `q(b) <= 12*tau/13` (§1.0, (h2));
by Markov, `lambda{q > 24*tau/13} < 1/2`, so at least `1/2` of the web mass sits on
rows with score `<= 24*tau/13`, each of which satisfies (h5) with the doubled
constant and reproduces its own (weaker) corner by the L-C computation at that score:
`Gamma_{f'}(C'_{f'}) >= 1 - 6*D/13 - tau*(D+1)/2 > 7/100` at the (2.1) thresholds
(exactly `1/13 - 3/106496 - 3/512 - 1/8388608` at the ceilings).
The hard configuration therefore carries a POSITIVE-MASS FAMILY of corner-builders,
not one selected row; ledger arguments below may sum over it.

#### H-D1 — high-shipping capacity kill (PROVED; the closed boundary of H-D)

**Statement.**  For an exact signed idempotent `P` with `0 < delta(P) <= 2^(-16)`, a
hidden geometrically distinct row vertex `u` with `0 < t*(u)`, a relative-interior
optimal exposer `h_u*` at `u`, nonempty `T(u), O(u)` with `K_T(u), K_O(u)` disjoint,
and a row `z°` with `h_u*(p_{z°}) = 0`: `z°` ships less than `1/16` of its positive
mass to `{j : h_u*(p_j) >= kappa}`.

**Mechanism (verbatim composition of proved shards).**  If the shipping were
`>= c_r = 1/16`, the quoted `lem-zero-face-capacity-kill` clause gives
`c_r*kappa <= nu_{z°} <= delta(P)`, i.e. `tau/64 <= tau^2`, i.e. `tau >= 1/64` —
impossible at `tau <= 1/256`.  (The round-1 verifier independently confirmed this
arithmetic, finding 8.)  Grade: EASY, PROVED.  Consequence: inside H-D below, every
separator blocker is automatically STARVED (`< 1/16` kappa-high shipping); the
starved case is not an extra hypothesis but the only case.

#### H-D(sigma) — disjoint-carrier starvation exclusion

**Statement.**  There exists universal `delta_D in (0, 2^(-16)]` such that no tuple
satisfying PRE(sigma) at `delta <= delta_D` additionally has

    sum over type-D corner-horn vertices u of P_fu^+  >  1/16.       (H-D.1)

**Constants and normalized objects carried by the statement.**  At each type-D
carrier `u`: strict separation of the compact sets `K_T(u), K_O(u)` supplies a linear
`ell_u` with `||ell_u||_inf <= 1` (rescaling preserves strictness); the separator
interval of `lem-separator-zero-face-obstruction` is nonempty and contains an `m_u`
with `|m_u| <= D + 1 = 3 + 4*delta` (take `m_u` just above
`max_O ell_u(p_i - p_u) in [-D, D]`); the resulting `psi_u = ell_u(. - p_u) -
m_u*h_u*(.)` is P-harmonic with `psi_u(p_u) = 0`, `psi_u > 0` on `T(u)`, `psi_u < 0`
on `O(u)`, row-oscillation `osc(psi_u) <= D + (3+4*delta) = 5 + 8*delta`, and a
nonclone blocker `z°_u` with `h_u*(p_{z°_u}) = 0`, `psi_u(p_{z°_u}) < 0` (shard
clause quoted in §1.1).  These normalizations re-derive, at an arbitrary hidden
carrier, the constants that `lem-psi-corner-trap` records at a hidden top — that
shard's preamble pins `v`, so it is NOT quoted here; the two-line re-derivations
above are part of this leaf's routine surface and divide by neither `t*(u)` nor the
gap.

**Mechanism (the concrete closing program).**  Three ledgers, all exact:
(i) *the max principle at* `psi_u`: `P psi_u = psi_u` on row values, so at any row
`r` attaining `M_u = max_j psi_u(p_j)`, sign-splitting the reproduction gives
`sum_j P_rj^+*(M_u - psi_u(p_j)) = sum_j P_rj^-*(M_u - psi_u(p_j))
<= nu_r*(5+8*delta) <= delta*(5+8*delta)` — the maximizing row returns almost all
its positive mass to the near-maximal `psi_u`-slab; since `psi_u > 0` on `T(u)` and
`T(u)` is rho-far from `u`, the maximal slab is far-side.
(ii) *the corner trap at the funders*: for any row `i` with `z_i <= s_1` (in
particular `f` with `s_1 = 6*D*tau/13`, and every corner row `x` with `s_1 = 4*tau`,
and every web-of-corners row), reproduction of the affine `z` sign-splits to
`sum_{j : z_j >= s_2} P_ij^+ <= (s_1 + nu_i*D)/s_2`, and identically for `h*` with
bound `(s_1 + nu_i)/s_2` — the funders' positive mass is trapped in the doubly-low
corner band up to explicit Markov loss.
(iii) *the starvation clause from H-D1*: every blocker `z°_u` keeps `> 15/16` of its
positive mass on `{h_u* < kappa}`.
The contradiction target: `T(u)` is dual-REQUIRED (by `lem-always-tight-dual-support`
every optimal witness charges it) and `psi_u`-positive, while (ii)+(iii)+(H-D.1) make
every identified positive-mass channel into the far `psi_u`-positive region starved
at scale `tau`; ledger (i) forces SOME row to keep near-maximal `psi_u`-value with
`O(delta)` slack, and the program must show these three exact constraints plus the
all-row negativity budget `nu <= delta` cannot be simultaneously completed.  The
per-horn instantiation — the consumed horn label:
  - `sigma = F`: every carrier `u` is rho-far from `v`, so the ROW `v` itself lies in
    `F_u`; hence `h_u*(p_v) >= t*(u) > 0` (the optimal exposer is feasible:
    `h_u* >= t*(u)` on all of `F_u`), and pairing the harmonic `psi_u` with row `v`'s
    own reproduction, `psi_u(p_v) = sum_j P_vj*psi_u(p_j)`, couples the carrier
    anatomy to `v`'s coefficients `a_j` — exactly the Proposition-D-permitted channel
    (D3: "v's own coefficients").
  - `sigma = N`: every carrier `u` is rho-near `v`, so `z(p_u) < 4*tau` is forced by
    1-Lipschitzness alone and the carriers huddle jointly in the `4*tau`-ball of `v`;
    the funder `f` is rho-FAR from `v`, so (H-D.1) asserts a far row financing a
    near-`v` huddle across the exemption ball, and the ledger (ii) at `f` plus the
    web-of-corners family are the financing channels to starve.

**Grade: HARD (open).**  This is one of the two residual creative cells.
**Risk / exact-instance kill criterion.**  An exact rational family with
`delta = tau^2 -> 0` satisfying PRE(sigma) and (H-D.1) — i.e. a COMPLETED starvation
gadget with tall visible hull, all-row negativity `<= tau^2`, and a type-D corner
carrier — refutes H-D for every proposed `delta_D`.  A local tableau is not a kill
until every row is completed and all of (h1)-(h7) are checked.

#### H-I(sigma) — intersection-carrier second-web exclusion

**Statement.**  There exists universal `delta_I in (0, 2^(-16)]` such that no tuple
satisfying PRE(sigma) at `delta <= delta_I` additionally has

    sum over type-I corner-horn vertices u of P_fu^+  >=  1/16.      (H-I.1)

**Proved-inline sub-brick H-I0 (the banded second web; dispatchable now).**  For
every type-I carrier `u`: by the quoted `lem-optimal-face-conic-reduction` clause, an
alpha-free display exists — probability vectors `lambda^u` on `T(u)` and `gamma^u` on
`O(u)` with `sum lambda^u_r*(p_r - p_u) = t*(u)*sum gamma^u_i*(p_i - p_u)`.  Summing:
the `T(u)`-barycenter `b_u` obeys `||b_u - p_u||_1 = t*(u)*||q_u - p_u||_1 <=
t*(u)*D < kappa*D = (1/2+delta)*tau` (row diameter).  Pairing the display with any
admissible exposer `h` at `u` (affine, `h(p_u) = 0`):
`sum lambda^u_r*h(p_r) = t*(u)*sum gamma^u_i*h(p_i) in [0, t*(u)]` — the display
defeats EVERY exposer at `u` with budget `t*(u) < kappa`.  Finally `z` is affine and
1-Lipschitz with `z(p_u) < 4*tau` (corner), so the display's `z`-mean is
`z(b_u) <= z(p_u) + ||b_u - p_u||_1 < (9/2 + delta)*tau`, and by Markov
`lambda^u{z >= 9*tau} <= (9/2+delta)/9`, i.e.

    lambda^u{z < 9*tau} >= 1/2 - delta/9.                            (H-I.2)

So every type-I carrier spawns a SECOND-GENERATION web: a probability on rows rho-far
from `u`, barycenter within `(1/2+delta)*tau` of `p_u` (SHARPER than SL1a's
`11*tau/5`), defeating every admissible exposer at `u` with budget `t*(u) < kappa`
(SHARPER than SL1a's `(16/13)*kappa`), and co-top in the WIDENED band `9*tau` on at
least `1/2 - delta/9` of its mass (WEAKER than SL1a's `4*tau` band).  All inline
steps are two-line convexity computations; the only quoted contracts are the display
and the margin.

**Mechanism (the concrete closing program).**  The configuration is self-similar
with an exact constant ledger: center `v` (band `4*tau`, radius `11*tau/5`, budget
`4*tau/13`) begets carrier centers `u` (band `9*tau`, radius `(1/2+delta)*tau`,
budget `kappa`), each `u` hidden and co-top.  The program: (1) run the L-C corner
computation at a second-generation web row `r in T(u)` with `z_r < 9*tau` — the
corner-trap ledger (ii) of H-D applies verbatim at `s_1 = 9*tau`, producing a
second-generation corner at threshold `s_2` with mass `>= 1 - (9*tau +
nu_r*D)/s_2`; the band degradation per generation is the explicit factor visible in
(H-I.2), and `H > 16*tau` funds at most ONE such degradation step (a `9*tau`-band
row is still hidden-deep since `H - 9*tau > 7*tau > 0`, but a third generation at
band `> 16*tau` would exit the co-top regime) — so the recursion terminates in at
most two generations, and the closing step must convert the terminal generation's
display into one of the two proved kills: a type-D carrier (H-D1's capacity
arithmetic) or a violation of an exact ledger.  (2) The per-horn instantiation — the
consumed horn label and the consumed barycenter clause (h2): for `sigma = N`,
`||p_u - p_v||_1 < 4*tau`, so the second web's barycenter satisfies
`||b_u - p_v||_1 < (9/2 + delta)*tau`, within `(9/2+delta)*tau + 11*tau/5 < 7*tau`
of the FIRST web's barycenter `b` — two exposer-defeating far webs pinned in one
`7*tau` ball around the summit, whose joint displacement ledger (both barycenters
are convex combinations of rho-far row points) is the targeted overdetermination;
for `sigma = F`, `u` is rho-far from `v` and `v in F_u`, so the second web's
exposer-defeat clause applies to exposers separating `p_v`-side structure, coupling
the two generations through the always-tight geometry rather than through position.
**Named open residual, honestly:** the termination functional — a clone-invariant
monotone quantity that strictly decreases along the generation step and is bounded
below — is not yet constructed; candidates (band-normalized exposer budget
`t*/kappa`; the lex-minimality of (h3) against a generation-collapse surgery) are
recorded, not proved.

**Grade: HARD (open).**  The second residual creative cell.
**Risk / exact-instance kill criterion.**  An exact rational family realizing a
single type-I corner carrier inside a completed PRE(sigma) instance (display and
corner data checked in exact arithmetic) refutes H-I for every proposed `delta_I`.

#### H-X(sigma) — off-diagonal freight exclusion

**Statement.**  There exists universal `delta_X in (0, 2^(-16)]` such that no tuple
satisfying PRE(sigma) at `delta <= delta_X` additionally has

    Gamma_f{(x,u) in C_f ∩ (horn-sigma cell) : p_x != p_u}  >  1/8.  (H-X.1)

Equivalently: more than `1/8` of the selected row's coefficient-kernel mass rides on
NON-vertex co-top doubly-low freight rows `x` whose vertex decomposition lands on
corner vertices in the horn.

**Mechanism (the concrete closing program; two named routes, each with its
obstruction stated).**
  Route 1 — *completion infeasibility with an explicit dimension-free certificate
  basis*.  Fix the finite clone-invariant CELL DATA of a putative instance: the sign
  cells of the rows appearing in the ledgers, the type (I/D) of each corner carrier,
  the horn label, and the finite moment vector

      m(P) = ( Gamma_f(C_f);  the horn masses;  the diagonal/off-diagonal split;
               S_f and the corner-trap ledgers at f and at the freight rows x;
               nu-budgets of the ledger rows;  the blocker shippings at D-carriers;
               max/min of each psi_u over rows;  z- and h*-moments of each
               second-generation display ),

  every entry a clone-invariant scalar (a mass sum over row points or an extremum of
  an affine test).  For fixed cell data the constraints tying `m(P)` together —
  row reproduction of the affine tests `1, z, h*, psi_u` at the ledger rows
  (`lem-harmonic-affine-bridge`), the mass identities (`lem-mass-split` at each
  ledger row), the negativity budget `nu <= delta` on EVERY row, and the corner/horn
  inequalities (H-X.1) — form a finite linear system in the moment vector whose
  coefficients are universal constants and powers of `tau`.  The lemma's content is
  that this system is infeasible with margin `c*tau` for an explicit `c > 0`; the
  proof object to be produced is a single multiplier vector on the listed constraints
  (a Farkas certificate) with entries that are universal rationals — dimension-free
  and clone-normalized BY CONSTRUCTION because every constraint is already a
  row-point moment.  What must be checked before any such certificate is believed:
  that it uses at least one constraint a local tableau cannot exhibit (an all-row
  constraint: the negativity budget quantified over every row, or a second ledger
  row disjoint from the gadget's support) — otherwise the W55 gadget's feasibility
  refutes the certificate's existence (§ red tests below).
  Route 2 — *the minimality surgery* (consumes (h3)).  Freight rows are non-vertex
  row points; deleting the freight fiber would reduce `R(P)` by at least one with
  `V(P)` unchanged, contradicting (h3) — IF an exactness-preserving,
  negativity-thrifty, geometry-preserving deletion existed.  The banked exact
  deletion is censoring: `lem-censoring-exactness` (`status: proved`) gives
  `S = D + C*(I-A)^{-1}*B` with `S^2 = S`, `S*1 = 1` exactly, but its priced bound
  `delta(S) <= delta*(1 + 2*(1+delta) + (2+3*delta)*a/(1-a)) +
  (1+delta)^2*delta_A/(1-a)^2` inflates `delta` by a factor `>= 3` even for a
  nonnegative censored block — while the class is pinned at `H > 16*tau`, so a
  `sqrt(3)`-inflation of `tau` exits the tall class unless `H > 16*sqrt(3)*tau`
  already.  The surgery route therefore requires a NEW negativity-thrifty deletion
  operation (delta inflation `1 + O(tau)`), named here as its open sub-problem; a
  further obstruction recorded in §1.3(ii): deleting a row point can destroy the web
  when `lambda` rides the deleted point, so the surgery must first re-route web mass
  through the barycenter identity (§1.0: only `b` and support membership matter).
  Route 3 (bounding, not closing) — *freight self-propagation*: each freight row `x`
  is itself doubly-low (`z_x, h*(p_x) < 4*tau`), so the corner trap (H-D ledger (ii))
  applies at `x` with `s_1 = 4*tau`: freight rows re-ship their positive mass into
  the band `{z < s_2}` up to `(4*tau + nu_x*D)/s_2` loss — one band-degradation step
  inside the `16*tau` budget, which converts freight into second-generation corner
  structure but cannot terminate alone (recorded to prevent a false hope: at
  `s_2 = 8*tau` the Markov loss is `~ 1/2` per step).

**Grade: HARD (open).**  The third residual cell; jointly with H-D it is the
factorization-level completion question the W55 strategy names as the actual new-math
wall — here quantified, with the certificate's REQUIRED shape (dimension-free
multipliers on listed clone-invariant moments) and its REQUIRED non-locality (must
consume an all-row constraint) made explicit.
**Risk / exact-instance kill criterion.**  A completed exact instance carrying
`> 1/8` off-diagonal freight refutes H-X; a Farkas certificate whose every constraint
is realizable by the W55 gadget's local data is self-refuting and must be rejected.

#### H-W sub-assembly (checkable)

Let `delta_H := min(2^(-16), delta_D, delta_I, delta_X)`.  Suppose a tuple satisfies
(h1)-(h7) at `delta <= delta_H` with label `sigma`.  The horn cell has mass `>= 1/4`
(both labels).  By SD1 either the off-diagonal mass is `> 1/8` — contradicting
H-X(sigma) — or the diagonal mass is `>= 1/8`; in the latter case SD0 legalizes every
carrier and SD2 gives type-I mass `>= 1/16` — contradicting H-I(sigma) — or type-D
mass `> 1/16` — contradicting H-D(sigma) (whose blockers are automatically starved by
the proved H-D1).  Hence no tuple exists: H-D1 + H-D + H-I + H-X imply H-W, with the
constant read-order: the three descendant ceilings first, then `delta_H` as their
minimum.  Every step is mass arithmetic over owned boundaries; no selection occurs.

**H-W mandatory red tests.**
**Proposition E:** PASS — (h2) carries SL1a's strict co-top support clause verbatim
and (2.1) forces the depth band on both corner coordinates; the shallow counterweight
is excluded at the hypothesis level.
**W55 exact starvation gadget (run as a yes/no against the FULL hypotheses; round-1
finding 5 repaired).**  Does the literal `A0 = 5, g = 5*tau` tableau satisfy
(h1)-(h7)?  **NO** — item by item: (h1) fails (only the top row's reproduction is
exhibited; `P^2 = P` on all rows, the visible set, and `H > 16*tau` are absent —
`W` and `H` are not even defined for a partial tableau); (h2) fails (no probability
web with the barycenter and exposer clauses is exhibited); (h3) is inapplicable
without (h1)-(h2); (h5)-(h7) are therefore unevaluable as stated.  What the gadget
DOES satisfy: the local scalar pattern of the H-D ledgers (exact top-row
reproduction, prescribed negativity `tau^2`, zero far positive inflow, display gauge
`A0 = 5`) — so no scalar-ledger argument can close H-D or H-X, and both statements'
mechanisms are required to consume at least one resource the gadget lacks (the
all-row negativity budget, the second ledger rows, the web, or minimality).  This is
recorded per descendant in their kill criteria.
**Non-vacuity of the hard antecedent class (finding 5, second half).**  The class
{(h1)-(h7) tuples} is empty IF AND ONLY IF SL1a holds at `delta_H`: emptiness follows
from SL1a trivially (h1)-(h2) being SL1a's antecedent; conversely any SL1a
counterexample yields a tuple by L-M + L-S + L-C + L-P (§4).  The hard leaf IS the
emptiness lemma — emptiness is not a footnote escape but the exact content, and the
decomposition cannot win vacuously: proving H-W is proving SL1a's residual.  What an
in-class witness must exhibit is enumerated in §5 (W1-W5).
**Clone/transient:** PASS — all masses are fiber-aggregated, the kernel is
clone-fiber-constant, `V, R` are distinct-point counts; under (1.4) every
non-extremal clause lifts (§1.3), `V` is unchanged and `R` grows by at most one, so
the extension maps the class into the class-or-its-non-minimal-shadow, and the
assembly re-selects; no leaf claims the deletion converse (§1.3(ii)).
**Coverage:** PASS — every banked family exits at root tallness (§5); no family is
claimed as in-class evidence for or against any descendant.
**Proposition-D/W55/B6 walls:** PASS — the `(lambda, Phi_v)` pairing occurs only in
the L-S selection and the web-of-corners Markov bound (both selections, no
contradiction sought there — Proposition D caps averages, it does not forbid
selection); the load-bearing couplings are row reproduction at `f`, at freight rows,
at blockers, and at row `v` (far horn), plus the always-tight anatomy — exactly the
D3-permitted channels; no `lambda*P` vs `p_v` comparison, no dual multiplier is
treated as mass (the displays and `psi_u` remain LP certificates attached to their
carriers), no thin/thick split from a single separator moment (SD2 is a per-carrier
hull dichotomy), and no mutually-rho-far family is quantified anywhere (the antipode
is gone; all `rho`-predicates are radial from `v` or from a fixed carrier).

**Restatement test: PASS, with the logical direction stated.**  H-W does not imply
SL1a, L2-core, or the huddle charge — in one line or any number of routine lines —
because it is silent off the lex-minimal stratum and off the corner-horn structure;
it is IMPLIED by each of them restricted to its class.  The round-1 failure (a hard
leaf stronger than the target) is structurally impossible here.

## §4 THE ASSEMBLY

**Claim.**  `L-M + L-S + L-C + L-P + H-W` imply the pinned SL1a contract.

### §4.1 Constant order (existential leaf constants read FIRST)

Read the sole existential hard constant first: H-W supplies
`delta_H in (0, 2^(-16)]` (internally `delta_H = min(2^(-16), delta_D, delta_I,
delta_X)` per the sub-assembly).  Set

    delta_0 := delta_H.                                        (4.1)

No later-dependent choice exists.  For every `0 < delta <= delta_0`,

    tau <= 1/256,   D = 2+4*delta <= 2 + 2^(-14) = 32769/16384.  (4.2)

The source constants convert, without rounding:

    (16/13)*kappa = (16/13)*(tau/4) = 4*tau/13,                (4.3)
    2.2*tau = 11*tau/5,                                        (4.4)
    2*(4*tau/13) + 4*tau/13 = 12*tau/13.                       (4.5)

The source depth width and far radius both remain exactly `4*tau`; the tallness
`H > 16*tau` remains strict; the barycenter constant `11*tau/5` and exposer constant
`4*tau/13` pass VERBATIM into H-W's clause (h2) — no conversion arithmetic beyond
(4.3)-(4.5) exists in this document, and none is needed.

### §4.2 Derivation

Assume for contradiction that SL1a fails at `delta_0`, i.e. some exact signed
idempotent with `0 < delta <= delta_0` carries the full web data.

0. **Select a minimal counterexample.**  Apply L-M at `d_0 = delta_0`: some `P°`
   attains the lexicographic minimum of `(V, R)` over the (nonempty) counterexample
   class.  Fix any admissible data `(v, lambda)` for `P°`; write `b` for the web
   barycenter.  This is (h1)-(h3).
1. **Fix the legal affine observables.**  The exact proved clause of
   `lem-top-deficit-price` supplies a top support functional `phi`; put `z = H - phi`.
   Since `v` is a hidden row vertex with `F_v` nonempty (the web itself is rho-far),
   the exact proved clause of `lem-positive-exposedness-margin` gives
   `0 < t*(v) < kappa`, the finite exposedness LP has a nonempty optimal face, and a
   relative-interior optimal exposer `h*` exists.  This is (h4).
2. **Select one web row.**  Apply L-S to `(lambda, phi, h*)`: equations (4.3)-(4.5)
   are exactly its hypotheses and yield `f in supp(lambda)` with
   `2*z_f/D + h*(p_f) <= 12*tau/13`.  This is (h5), and it is the only pairing of
   `lambda` with the top-face observables — a selection, not a contradiction.
3. **Exhibit a kernel.**  By finite-polytope convexity a vertex kernel obeying §1.2
   exists (Dirac at vertices, clone-fiber-constant by construction on row points).
4. **Build the corner.**  Apply L-C to `(P°, v, phi, h*, f, xi)`: its hypotheses are
   (4.2) plus steps 1-3, and its conclusion is `Gamma_f(C_f) > 1/2` with the
   arithmetic floor (3.7).  This is (h6).
5. **Label the horn.**  Apply L-P to `Gamma_f|C_f`: exactly one of (F), (N) holds for
   THIS tuple, with owned boundary.  This is (h7) at some `sigma in {F, N}`.
6. **Terminal exclusion.**  The tuple `(P°, v, lambda, phi, h*, f, xi)` with label
   `sigma` satisfies H-W's antecedent item by item — (h1)-(h2) from step 0's class
   membership, (h3) from L-M, (h4)-(h7) from steps 1-5 — and `delta <= delta_0 =
   delta_H`.  H-W says no such tuple exists.  Contradiction.

Hence no counterexample exists at `delta <= delta_0`: SL1a holds with
`delta_0 = delta_H > 0`.  Per §2.1, the derivation claims only (R-a) existence of at
least one tuple and (R-b) that H-W excludes every legal tuple; had step 5 produced
the other label under different choices, step 6 applies verbatim at that label.

Constant audit: `11*tau/5` enters through (h2) verbatim (consumed inside H-W by the
H-I near-horn geometry); `4*tau/13` enters through (h2) and is consumed twice in
(4.5) and again inside H-W by the web-of-corners Markov bound; both `4*tau`
predicates and `H > 16*tau` pass untouched into (2.1), SD0, and the descendants.

### §4.3 Assembly red-test ledger

**Proposition E:** PASS — the only conditioning is to `z < 4*tau`, which implies the
strict depth band; the shallow counterweight never enters any step.
**W55 exact starvation gadget:** PASS AS A WALL — steps 0-5 are deliberately
compatible with a completed co-top analogue; the contradiction occurs only at H-W,
whose descendants are required (their kill criteria) to consume resources beyond any
local tableau.  **Clone/transient:** PASS — every operation is on row-point measures,
full fibers, or the joint kernel; §1.3's lift argument covers the extension, and L-M
re-selects a minimal representative when the extension creates a new row point.
**Non-vacuity/coverage:** PASS — a hypothetical first tall web traverses every
pipeline edge and exactly one horn per tuple; known families fail the root (§5).
**Proposition D:** PASS — `(lambda, phi, h*)` is used only to select; the load-bearing
bridge is reproduction at `f` and the H-W channels.  **W55 forbidden
identifications:** PASS — neither `lambda*P` nor any conic multiplier is compared
with `p_v`; `Gamma_f(x,u)` keeps flow and vertexization coordinates separate.
**B6:** PASS — no pairwise-separation clause survives anywhere in this document; all
`rho`-splits are radial from `v` or from a fixed carrier.

## §5 COVERAGE CHECK

Evidence and routing only; no census value or gadget is a proof step in §4.  The root
requirement `H > 16*tau` implies

    H^2/delta > 256,                                           (5.1)

whereas the FINDINGS census reports `H^2/delta < 16` for every banked instance.  The
honest location of every known exact family is a named PRE-ROOT exit.

| Known family / test object | Identifiable location | Why no uncovered space |
|---|---|---|
| `HA_t / HA_eps` delta-inflation families | pre-root (not tall) | height gain inflates `delta`; ratios stay below (5.1). |
| Deep-append-turns-visible family | pre-root (not hidden; not tall in the banked range) | the appended deep row becomes visible before it can be a hidden top. |
| TOP-preserving reversion family | pre-root (not tall) | top geometry reverts while the ratio stays sub-tall. |
| Best disjoint frontier | pre-root (not tall) | genuinely disjoint anatomy at `H` far below `16*tau`; H-D is not claimed to explain it in-class. |
| Proposition-E two-point counterweight system | pre-root (not co-top) | violates the strict support clause `d > H - 4*tau`, preserved by every restriction. |
| W55 `A0=5, g=5*tau` starvation gadget | H-D/H-X refuter GATE, not an instance | satisfies the local scalar ledgers only; fails (h1)-(h2) as recorded in H-W's red test. |

**What an in-class witness (a refuter of H-W, hence of SL1a) must exhibit:**
  (W1) an exact `P` (`P^2 = P`, `P*1 = 1`) with EVERY row's negative mass
       `<= delta <= delta_H` — the all-row budget, absent from every local tableau;
  (W2) nonempty `W` and `H > 16*tau`, i.e. `H^2/delta > 256` against a banked record
       that has never exceeded `16` (L3 evidence, not proof);
  (W3) far co-top row points whose convex hull contains a point `b` with
       `||b - p_v||_1 <= 11*tau/5` and `h(b) <= 4*tau/13` for every admissible
       exposer at `v` (by §1.0 this is all a web is);
  (W4) for refuting H-W IN ISOLATION, lex-minimality of `(V, R)` — though any SL1a
       counterexample at all refutes H-W THROUGH the routine leaves (the §3
       emptiness equivalence), so a refuter need not certify minimality to kill the
       program, only to kill the isolated leaf;
  (W5) the corner and horn data — automatic from L-S/L-C/L-P once (W1)-(W3) stand.
The obstruction record: every banked attempt at (W2) reverted or inflated `delta`
(the W52 families), and the completion coordinates `P = L*B`, `B*L = I` make
(W1)-(W2) an exact LP once cell data are fixed — the intended discovery route for
either a witness or H-X's certificate.  All of this is evidence-level (L3), quoted
as routing only.

Routing checklist for a future exact family: lacking a hidden top, tallness,
nonempty `W`, or a strict co-top web, it exits pre-root; otherwise L-M places a
minimal representative, L-S/L-C/L-P build a tuple, and H-W's sub-assembly routes it
to exactly one of H-D1/H-D/H-I/H-X by owned mass boundaries.  No rank, raw support
size, or transient-row count creates a case.

## §6 HONEST ASSESSMENT

**Shape.**  Five leaves: L-M, L-S, L-P EASY; L-C MEDIUM; H-W the single permitted
HARD leaf, decomposed one level further into one PROVED brick (H-D1), one
proved-inline brick (H-I0), and three fully-quantified open descendants
(H-D, H-I, H-X) with a checkable sub-assembly.  No OPEN statement in the document is
logically stronger than SL1a (the loss-free property, §3 H-W (d); the routine leaves
are unconditional bookkeeping claims) — the round-1 overshoot (a hard leaf that
implied the target outright) is structurally excluded.

**Hardest / most-likely-false.**  Because of the loss-free property, H-W is exactly
as false as SL1a; the risk concentrates in whether the three descendants are
SEPARATELY closable.  Ranked: H-X first (the completion certificate must be found
AND must consume an all-row constraint — the W55 gadget proves scalar ledgers do not
suffice); H-D second (same wall, plus the starved-blocker geometry); H-I third (its
front is proved-inline down to the banded second web; the open residual is the
termination functional).  A refuter attacks by COMPLETING the starvation gadget —
tall visible hull, all-row negativity `<= tau^2`, then any horn — which kills H-D or
H-X and with them the program; the second refuter target is an exact type-I carrier
instance against H-I.

**What a prover must actually add.**  For H-X: a Farkas certificate over the listed
clone-invariant moment system that provably uses the all-row negativity budget or a
ledger row outside the gadget's support; or the negativity-thrifty deletion operation
(inflation `1 + O(tau)`), which would arm the (h3) minimality weapon — censoring's
factor-3 inflation is the stated obstruction, not a dead route but a priced wall.
For H-I: the termination functional for the generation step (band-normalized budget
`t*/kappa` is the live candidate).  For H-D: the starvation ledger closed against
the max principle without dividing by `t*(u)` or the gap (the normalizations in the
statement already guarantee the constants are legal).

**Independently dispatchable now.**  L-M (one-paragraph proof); L-S (short exact
audit of (3.1)); L-C (independent rational re-check of (3.3)-(3.7) — already
verifier-re-derived once); L-P (one page); H-D1 (verbatim shard composition —
already verifier-checked arithmetic); H-I0 (the banded second web: a self-contained
MEDIUM lemma, prime codification candidate); the H-X moment-system formalization
(writing the finite LP explicitly for the gadget's cell data — an exact, bounded
task that either produces the certificate shape or documents its impossibility).

**Changes from round 1, summarized.**  The hard leaf now RETAINS `lambda` verbatim
and adds minimality — the class is a strict refinement, not a broadening; the
antipode and its `9*tau/5` constant are deleted (unused decoration; barycenter data
retained at full strength instead); the horn label is consumed by per-horn
mechanisms (far: `v in F_u` coupling to `a_j`; near: the huddle geometry and the
second-web barycenter comparison); the named cells H-DI/H-DD/H-MX are replaced by
quantified H-D/H-I/H-X with constants, mechanisms, kill criteria, and a checkable
sub-assembly; routing is existence-plus-universality, not exactly-once; L-P's
Proposition-E record and the transient-row lift are corrected per the verifier's own
wording.

**Pruned alternative decompositions (one line each).**
* More `(lambda, Phi_v)` moments: dead — `lem-intersection-witness-confinement` caps
  the average, `lem-l2-core-collapse` collapses averages (Proposition D).
* Direct comparison of `lambda*P` with `p_v`: dead by the W55 identity-level wall.
* Treating the `u`-marginal of `Gamma_f` as transition mass: the same-carrier error.
* Canonical kernel selection (e.g. via `lem-genuine-disintegration`'s fixed
  representation): rejected — canonicalization would need a tie rule; universal
  quantification is strictly stronger and free because L-C is kernel-universal.
* A `b`-centered horn split instead of the `p_v`-centered one: equivalent up to
  `11*tau/5` shifts; the `p_v`-radial form matches the banked vocabulary.
* Vertex-count INDUCTION as a completed route: still dropped — no proved deletion
  lemma controls `delta`, the visible hull, and the depth band simultaneously;
  retained only as H-X's Route-2 OPEN sub-problem with the censoring inflation
  obstruction priced explicitly.
* Thin/thick split from one separator moment: dead (W55); SD2 is a per-carrier hull
  dichotomy instead.
* Pairwise-rho web rigidity: dead at scale (B6); nothing pairwise remains.
* Carre-du-champ / score-flatness closers: dead — a flat W55-style plateau satisfies
  the stationarity ledgers.
* Stating the hard leaf without (h2) or without (h3): rejected — the former is the
  round-1 fatal broadening, the latter would orphan the surgery weapon and (h3)
  costs one EASY leaf.

No conjecture shard is a premise anywhere.  Proving H-D, H-I, and H-X (H-D1 is
proved) closes H-W and with it SL1a at `delta_0 = delta_H`; refuting any descendant
refutes SL1a itself (loss-free), so every descendant is a genuine prove-or-refute
target rather than a renamed residual.

