# W56 — Tier-2 decomposition of SL1a

AUTHOR-CLAIM strategy material only.  Nothing in this file promotes SL1a or any new
leaf.  The only established inputs used below are registry shards whose front matter
says `status: proved`; every such use quotes the consumed clause.  All measures are
measures on row **points** (equal row points are coalesced), all support language is
geometric, and all constants are independent of the number of rows.

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
takes values in `[0,1]` on every row point.

### §1.1 Standing proved inputs

The following are the only non-elementary established inputs used by the leaves or the
assembly.

* `lem-top-deficit-price` (`status: proved`) supplies “a top support functional `phi`
  (affine, `phi(p_v) = H`, `phi <= 0` on `conv{p_w : w in W}`, 1-Lipschitz for
  `l1`)” and, for every such `phi`, “`z_j = H - phi(p_j) >= 0`.”  The locked row
  geometry in `def-signed-idempotent` says that pairwise row distances are at most
  `D=2+4*delta`; hence `0<=z_j<=D`.  Also, directly from the quoted support
  properties, `phi(p_j)<=d_j`, so

      H-d_j <= z_j <= D.                                      (1.1)

  Thus `z/D` is an admissible exposer at `v`.
* `lem-harmonic-affine-bridge` (`status: proved`) says: “a vector `g` satisfies
  `Pg = g` if and only if there exists `u` with `g_i = u . p_i` for every row
  index `i`,” and “the constant term of any affine representation is absorbable into
  `u` since all row sums equal 1.”  Thus every affine row-value function distributes
  through **each** row reproduction; below this is used at a selected web row, not
  merely at `v`.
* `lem-mass-split` (`status: proved`) gives the exact row identity
  “`sum_j a_j^+ = 1 + nu_v`.”
* `lem-positive-exposedness-margin` (`status: proved`) says that every hidden
  geometrically distinct row vertex with nonempty far set has
  “`0 < t*(v) < kappa`.”  Together with elementary relative-interior existence for a
  nonempty finite LP optimum, this permits a relative-interior optimal exposer.
* `lem-always-tight-dual-support` (`status: proved`) says reduced optimal witnesses
  have supports contained in the whole-face families `T,O,Z`; and
  `lem-optimal-face-conic-reduction` (`status: proved`) says that the reduced
  witnesses are exactly the displays

      sum_T lambda_f*(p_f-p_u) + sum_Z a_z*(p_z-p_u)
        = t*(u)*sum_O gamma_i*(p_i-p_u),

  with `lambda,gamma` probability vectors and `a_z >= 0`, and that an alpha-free
  display exists exactly when the `T` and scaled-`O` hulls intersect.  These clauses
  are reserved for the further decomposition of the one hard leaf.
* In the disjoint case, `lem-separator-zero-face-obstruction` (`status: proved`)
  supplies a nonclone `z` with “`h*(p_z)=0` and `psi(p_z)<0`” and `P psi=psi`;
  `lem-zero-face-capacity-kill` (`status: proved`) says that a zero-face row shipping
  `c_r` positive mass to `{h* >= kappa}` must pay
  “`c_r*kappa <= nu_z <= delta(P)`.”
Two further proved clauses are walls, not positive inputs.  The exact relevant clause
of `lem-intersection-witness-confinement` (`status: proved`) is: “(B3) for every
admissible exposer `h` at `v`, `sum_f lambda_f*h(p_f) <= t*(v)`; (B4) for every top
support functional `phi` at `v` and every finite convex average,
`sum_f lambda_f*(H - phi(p_f)) <= t*(v)*(2+4*delta) < (1/2+delta)*tau`.”  The exact
relevant clause of `lem-l2-core-collapse` (`status: proved`) is: “every finite convex
average of top support functionals at `v` coincides ON THE ROW SET with a single top
support functional `phi_ybar`.”  Accordingly no edge below tries to obtain a
contradiction from `(lambda,Phi_v)` pairings or from averaged top faces.

All sums such as `P_fx^+` are henceforth aggregated over the full fiber of the row
point `x`; a split of one row point into clones merely splits that mass.  A fixed
vertex representation is a probability kernel `xi_x(u)` from a row point `x` to the
geometrically distinct row vertices `u`, chosen identically on clone fibers.  The
two-stage measure used below retains both coordinates:

    Gamma_f(x,u) := P_fx^+ * xi_x(u).                          (1.2)

It is coefficient mass on an actual row point followed by convex disintegration, not
literal transition mass `P_fu^+`.  Keeping `(x,u)` rather than only its `u`-marginal is
the convention that prevents the W55 carrier error and makes clone invariance explicit.

For the transient-row red test, the standard exact extension is

    P' = [[P,0],[mu*P,0]],                                   (1.3)

with `mu` a probability row: direct multiplication gives `P'^2=P'`, `P'*1=1`, the
new row is a convex row point, and its negative mass is at most `delta(P)`.  Every
leaf recomputes `W,H,phi,h` on the extended row set.  If an old antecedent remains
valid, its measures and kernels lift with zero mass on the new coefficient column and
the conclusion is unchanged; if the recomputed visible/depth data invalidate that
antecedent, the extension is outside that leaf rather than a refutation.  No proof
step assumes there are no transient rows.

## §2 THE DAG

Set once and for all

    delta_bar := 2^(-16),       tau := sqrt(delta),
    D := 2+4*delta,             (16/13)*kappa = 4*tau/13.

Suppose provisionally that an SL1a counterexample `(P,v,lambda)` exists with
`delta <= delta_bar`.  Choose any top support functional `phi`, put
`z=H-phi`, choose a relative-interior optimal exposer `h*` at `v`, and set

    q(x) := 2*z(x)/D + h*(x).

For the data-coverage discussion only, `R0` denotes the pre-root screen (failure of
exactness, nonempty `W`, hidden tall top, or an SL1a web).  It is not an extra case
inside the putative-counterexample space: every SL1a counterexample has already passed
it.

The DAG has three routine leaves and one hard terminal leaf:

```text
R  SL1a web (far + d>H-4tau + ||b-p_v||<=11tau/5
|            + all-exposer mean <=4tau/13)
|
S  L-S: score-and-antipode selector
|         choose f,e in supp(lambda), both still far and co-top,
|         q(f)<=12tau/13 and ||p_f-p_e||_1>=9tau/5
|
C  L-C: reproduce at f and retain the coefficient/disintegration coupling
|         Gamma_f(x,u)=P_fx^+ xi_x(u)
|         Gamma_f{z_x,h*_x,z_u,h*_u<4tau}>1/2
|
P  L-P: radial split of the coupled co-top corner
|         Q := Gamma_f{corner and ||p_u-p_v||_1>=4tau} >= 1/4 ?
|            (equality belongs to Q)
|          /                                                   \
|       Q yes                                                Q no
|       far-vertex horn >=1/4                    near-vertex horn >1/4
|          \                                                   /
|           H-CCO: coupled-carrier completion obstruction [HARD]
|                         (one branch-labelled leaf)
X  contradiction
```

The corner in the tree is

    C_f := {(x,u): z_x<4*tau, h*(p_x)<4*tau,
                    z_u<4*tau, h*(p_u)<4*tau}.                (2.1)

By (1.1), both coordinates of every pair in `C_f` have depth strictly above
`H-4*tau`; `u` is a geometrically distinct hidden row vertex.  The hard object is
therefore one selected web row, one explicit antipode, and one exact two-stage
coefficient kernel.  It is neither the original probability `lambda`, nor
`lambda*P`, nor a dual multiplier, and no recurrence at `u` is inferred from
`Gamma_f(x,u)`.

### §2.1 Exhaustiveness and boundary ownership

`L-S` and `L-C` are a pipeline, so they introduce no cases.  `L-C` proves
`Gamma_f(C_f)>1/2`.  Partition `C_f` by the literal predicate
`||p_u-p_v||_1 >= 4*tau`.  If its far mass is at least `1/4`, including equality,
the far horn owns it.  Otherwise its far mass is strictly below `1/4`, so the near
mass is strictly above `1/4`; the near horn owns the strict complement.  These are
row-point coefficient-mass sums, not support counts.

The selector's pair satisfies only `||p_f-p_e||_1>=9*tau/5`, obtained from
`4*tau-2.2*tau=1.8*tau`; it is deliberately **not** claimed to be a mutually
`rho`-far pair.  The only `rho` predicate after selection is radial distance from the
fixed top `v`, so the B6 scale gap is respected.

The hard leaf is parameterized by the horn label and excludes both terminal tableaux
in one statement.  Consequently every counterexample at `delta <= delta_bar` follows
one and only one path from `R` to `H-CCO`; no boundary instance is lost.  Tangencies in
the hard leaf's own next-level hull split belong to the intersection side.

## §3 THE LEAVES

Every statement below is one candidate registry contract.  “May consume” contains only
registry shards whose front matter says `status: proved`; contextual gadgets and census
data occur only in the red tests.

### L-S — score-and-antipode selector

**Statement (one sentence).** For every exact signed idempotent `P` with
`0<delta(P)<=1/4`, nonempty visible set, and hidden top vertex `v` of height
`H>16*tau`, every probability measure `lambda` supported on

    B_v={x: ||p_x-p_v||_1>=4*tau and d_x>H-4*tau}

whose barycenter `b` satisfies `||b-p_v||_1<=11*tau/5` and whose integral under
every admissible exposer at `v` is at most `4*tau/13`, every top support functional
`phi` at `v`, and every admissible exposer `h` at `v`, admit row points
`f,e in supp(lambda)` such that, with `z=H-phi` and `D=2+4*delta`,
`2*z_f/D+h(p_f)<=12*tau/13` and `||p_f-p_e||_1>=9*tau/5`.

**May consume.** `lem-top-deficit-price` only.

**Mechanism.** At the point of use, the exact `status: proved` clause from
`lem-top-deficit-price` is: “there exists a top support functional `phi` (affine,
`phi(p_v) = H`, `phi <= 0` on `conv{p_w : w in W}`, 1-Lipschitz for `l1`), and for
ANY such `phi`, writing `a_j = P_vj` and `z_j = H - phi(p_j) >= 0`.”  The row-diameter
bound gives `z<=D`, so `z/D` is admissible and

    integral (2*z/D+h) dlambda
       <= 2*(4*tau/13)+4*tau/13 = 12*tau/13.                (3.1)

Choose `f` no larger than this mean.  Since `f` is `4*tau`-far and
`||b-p_v||_1<=11*tau/5`,

    ||p_f-b||_1 >= 4*tau-11*tau/5 = 9*tau/5.                (3.2)

Choose an `l1`-norming `y`, `||y||_infty<=1`, for `p_f-b`.  The identity
`integral y.(p_x-b) dlambda(x)=0` supplies `e in supp(lambda)` with
`y.(p_e-b)<=0`, hence `||p_f-p_e||_1>=y.(p_f-p_e)>=9*tau/5`.  This is a finite
averaging and dual-norm argument.

**Grade: EASY.**  It is one application of a proved support-functional clause followed
by scalar averaging and `l1/l-infinity` duality.

**Risk / exact-instance kill criterion.**  The only attack points are the normalization
`z/D` and the nonpositive counterweight row.  An exact alleged failure must either show
some row has `z` outside `[0,D]`, or have all rows other than the chosen `f` strictly
positive under the norming functional while their weighted mean is zero; either exact
certificate contradicts a displayed hypothesis.  No compactness limit is used.

**Mandatory red tests.**  **Proposition E:** PASS—both selected rows stay in the strict
co-top set `B_v`, so the shallow counterweight is not re-admitted.  **W55 starvation
gadget:** PASS—the local `A0=5,g=5*tau` tableau does not itself provide this probability
web and barycenter; an obvious co-top augmentation may satisfy the conclusion, which is
harmless because L-S claims selection, not a contradiction.  **Clone/transient:**
PASS—`lambda` is on row points and clones split its weight; under (1.3), any antecedent
that persists lifts with zero `lambda`-mass on the new row, while a newly created
antecedent is handled by the same finite average.  No support count is used.
**Coverage:** PASS—any first genuine SL1a instance enters L-S, while every banked W52
family fails the root tallness test and is not falsely claimed to exercise it.
**Proposition-D/B6 walls:** PASS—the pairing only selects `f`; the later leaf reproduces
at `f`, and the antipode scale is `9*tau/5<rho`, not mutual `rho`-separation.

**Restatement test: PASS.**  The conclusion is two row points and two scalar
inequalities; it contains no probability web or exclusion and cannot imply SL1a,
L2-core, or the huddle charge.

### L-C — coupled coefficient-kernel corner

**Statement (one sentence).** For every exact signed idempotent `P` with
`0<delta(P)<=2^(-16)`, nonempty visible set, hidden top vertex `v` of height
`H>16*tau`, top support functional `phi` with `z=H-phi`, admissible exposer `h` at
`v`, row points `f,e` satisfying `d_f,d_e>H-4*tau`,
`||p_f-p_v||_1,||p_e-p_v||_1>=4*tau`, `||p_f-p_e||_1>=9*tau/5`, and
`2*z_f/D+h(p_f)<=12*tau/13`, and every fixed probability kernel `xi_x(u)` with
`p_x=sum_u xi_x(u)p_u` over geometrically distinct row vertices (identity on a vertex
point), the measure `Gamma_f(x,u)=P_fx^+*xi_x(u)` satisfies

    Gamma_f{(x,u): z_x<4*tau, h(p_x)<4*tau,
                        z_u<4*tau, h(p_u)<4*tau} > 1/2,       (3.3)

and both coordinates of every pair in the displayed set have depth `>H-4*tau`, while
`u` is a hidden geometrically distinct row vertex.

**May consume.** `lem-harmonic-affine-bridge`, `lem-mass-split`,
and the top-support clause of `lem-top-deficit-price`.

**Mechanism.** First solve the nonvertex-support issue inside this leaf.  By elementary
finite-polytope convexity, the finite row polytope is the convex hull of its
geometrically distinct extreme row vertices.  Hence every row point `p_x` has a
probability representation `p_x=sum_u xi_x(u)p_u`; choose one kernel on row points,
and take the Dirac kernel `xi_u(u)=1` at a vertex.  This is the required
vertexization step, proved here rather than inferred from a transition measure.

At the same point, the relevant `status: proved` contract excerpt from
`lem-top-deficit-price` is: “there exists a top support functional `phi` (affine,
`phi(p_v) = H`, `phi <= 0` on `conv{p_w : w in W}`, 1-Lipschitz for `l1`), and for
ANY such `phi`, writing `a_j = P_vj` and `z_j = H - phi(p_j) >= 0`.”  Thus, by the
row-diameter definition and the elementary support estimate recorded in (1.1),
`0<=z<=D` and `H-d<=z` on every row and vertex.

Next, the exact `status: proved` clause of `lem-harmonic-affine-bridge` is that
“`g` satisfies `Pg = g` if and only if there exists `u` with
`g_i = u . p_i` for every row index `i`,” with affine constants absorbable because row
sums are one.  Apply it at the row `f` to the affine functions `z` and `h`.  With
`nu_f=sum_x P_fx^-` and

    S_f := sum_x P_fx^+*(z_x+h(p_x)),

sign splitting gives

    S_f = z_f+h(p_f)+sum_x P_fx^-*(z_x+h(p_x))
        <= z_f+h(p_f)+nu_f*(D+1).                            (3.4)

Because `D>=2`, the selector score implies

    z_f+h(p_f)
       <= (D/2)*(2*z_f/D+h(p_f)) <= 6*D*tau/13.              (3.5)

The exact `lem-mass-split` (`status: proved`) clause is
“`sum_j a_j^+ = 1 + nu_v`,” so `Gamma_f(1)=1+nu_f`.  Affineness of the kernel gives
the same moment on both marginals:

    integral (z_x+h_x) dGamma_f = S_f
      = integral (z_u+h_u) dGamma_f.                         (3.6)

If either the `x`-coordinate or `u`-coordinate is outside the corner in (3.3), its
corresponding nonnegative sum `z+h` is at least `4*tau`.  A union bound using (3.6)
twice yields

    Gamma_f(C_f)
      >= 1+nu_f-S_f/(2*tau)
      >= 1-3*D/13-tau*(D+1)/2.                              (3.7)

At `tau<=1/256`, `D<=2+2^(-14)=32769/16384`, and the last expression is at least

    58079731/109051904
      = 1/2 + 3553779/109051904 > 1/2.                       (3.8)

Finally (1.1) makes `z<4*tau` imply `d>H-4*tau` strictly.  Since
`H-4*tau>12*tau>0`, a vertex `u` there is not visible (visible vertices lie in
`C_W` and have depth zero), hence is hidden.

**Grade: MEDIUM.**  The proof is bounded-scope measure bookkeeping: two affine
row-reproduction identities, one fixed convex kernel, and an explicit two-marginal
union bound.  The grade is MEDIUM only because keeping the transition coordinate `x`
separate from the vertex coordinate `u` is essential typing, not because any new
rigidity theorem is hidden here.

**Risk / exact-instance kill criterion.**  A refuter attacks (3.6), the sole
same-kernel step.  An exact instance kills L-C only if it supplies a declared vertex
kernel for which an affine value fails to barycentrically reproduce, or if direct
rational summation gives `Gamma_f(C_f)<=1/2` while (3.4)–(3.8) all hold.  Either is a
finite exact check.  In particular, no proof may replace `Gamma_f(x,u)` by
`P_fu^+` or infer row-`u` recurrence.

**Mandatory red tests.**  **Proposition E:** PASS—both coordinates in the conclusion
obey the strict depth band, so the shallow escape is absent.  **W55 starvation
gadget:** PASS—the exact local gadget, or its flat co-top analogue, can satisfy the
affine ledgers and hence L-C's conclusion; L-C makes no contradiction, and the later
hard leaf invokes all-row completion beyond those ledgers.  **Clone/transient:**
PASS—`P_fx^+` is aggregated over each full row-point fiber and `xi` is a kernel on
distinct points; weighted clone splitting only splits `Gamma_f`.  In (1.3), an old
selected row has zero coefficient in the appended column, so a persisting old terminal
has the same joint kernel; if the new row participates, the two affine-marginal proof
reapplies with it included.  No argument assumes its absence.
**Coverage:** PASS—the lemma accepts nonvertex web rows and therefore has no hidden
vertex-only hole; the known families still exit at the root tallness condition.
**Proposition-D/W55 carrier walls:** PASS—the new resource is exact reproduction at
the web row `f`; dual multipliers never appear, and `(x,u)` is retained precisely so
barycentric mass is not relabelled as flow.

**Restatement test: PASS.**  L-C starts from one selected row and ends with a
two-stage coefficient measure; it has no `lambda`, barycenter, universal exposer
condition, or exclusion conclusion and cannot recover SL1a in one or two lines.

### L-P — radial horn partition

**Statement (one sentence).** For every finite nonnegative measure `Gamma` on pairs
of row points `(x,u)`, every row point `v`, every `tau>0`, and every measurable set
`C` with `Gamma(C)>1/2`, exactly one of the boundary-labelled alternatives holds:

    (F) Gamma{(x,u) in C: ||p_u-p_v||_1>=4*tau} >= 1/4;

    (N) that far mass is <1/4 and
        Gamma{(x,u) in C: ||p_u-p_v||_1<4*tau} > 1/4.

**May consume.** None.

**Mechanism.** This is a decidable two-cell partition.  If (F) fails, the far mass is
strictly below `1/4`, while the near cell is its complement inside `C`; hence its mass
is `>1/2-1/4=1/4`.  Equality belongs to (F), so the alternatives are disjoint and
exhaustive.

**Grade: EASY.**  It is one line of finite-measure subtraction with explicit boundary
ownership.

**Risk / exact-instance kill criterion.**  There is no geometric input to attack.  An
exact failure would be three rational inequalities: total corner mass `>1/2`, far
mass `<1/4`, and near mass `<=1/4`; their sum is an immediate contradiction.

**Mandatory red tests.**  **Proposition E:** PASS—L-P does not alter `C`; when consumed,
every pair already has both coordinates in the strict co-top band.  **W55 starvation
gadget:** PASS—a local or co-top gadget is assigned to one horn but is not excluded by
this bookkeeping leaf.  **Clone/transient:** PASS—the predicate is radial on row
points and the quantities are coefficient-mass sums; splitting atoms or the extension
(1.3) cannot create a boundary gap in the literal two-cell partition.  **Coverage:**
PASS—every possible first tall
terminal tableau has an assigned horn, including equality; known sub-tall families
never reach it.  **B6:** PASS—there is no pairwise-separation assertion, only distance
of the vertex coordinate from the fixed `v`.

**Restatement test: PASS.**  L-P is an abstract measure dichotomy with no matrix
exclusion; it cannot imply SL1a, L2-core, or the huddle charge.

### H-CCO — coupled-carrier completion obstruction

**Statement (one sentence).** There exists a universal
`delta_H in (0,2^(-16)]` such that, for each horn label `sigma in {F,N}`, no exact
signed idempotent `P` with `0<delta(P)<=delta_H`, nonempty visible set, and hidden top
vertex `v` of height `H>16*tau` admits a top support functional `phi`, a
relative-interior optimal exposer `h*` at `v`, row points `f,e` with

    f,e in {x: ||p_x-p_v||_1>=4*tau and d_x>H-4*tau},
    ||p_f-p_e||_1>=9*tau/5,
    2*(H-phi(p_f))/D+h*(p_f)<=12*tau/13,                    (3.9)

a fixed vertex kernel `p_x=sum_u xi_x(u)p_u`, and its coupled measure
`Gamma_f(x,u)=P_fx^+*xi_x(u)` for which the corner `C_f` in (2.1) has mass `>1/2`
and satisfies, when `sigma=F`,

    Gamma_f{(x,u) in C_f: ||p_u-p_v||_1>=4*tau} >= 1/4,

or, when `sigma=N`, the same far mass is `<1/4` and the complementary strict-near
mass is `>1/4`.

**May consume.** `lem-positive-exposedness-margin`,
`lem-always-tight-dual-support`, `lem-optimal-face-conic-reduction`,
`lem-separator-zero-face-obstruction`, and `lem-zero-face-capacity-kill`,
all with `status: proved`.

**Mechanism and required next-level decomposition.** This is the sole HARD leaf.  It
is a global completion statement, not a scalar-ledger claim.  The following is its
one-level sub-DAG; these descendant names describe a proof program and are not extra
assembly leaves.

```text
H-CCO(sigma): horn mass M_sigma >=1/4 (strictly > in the N horn)
|
|-- D/M split on diagonal carrier p_x=p_u
|     D: diagonal mass >= M_sigma/2 (equality belongs here)
|     M: off-diagonal coefficient/disintegration mass > M_sigma/2
|
|-- D branch: actual P_f^+ flow to hidden co-top row vertices u
|     |-- I: K_T(u) intersects K_O(u) on >= half the D-mass
|     |         -> H-DI: alpha-free-display completion
|     `-- not-I: disjoint hulls on > half the D-mass
|               -> blocker high shipping is capacity-killed;
|                  H-DD is the starved-blocker completion
|
`-- M branch: recurrence is at x, vertex anatomy is at u
      `-- H-MX: off-diagonal/closed-plateau factorization obstruction
```

Here every good `u` is a hidden geometrically distinct row vertex with a nonempty far
set: if the far set were empty then `t*(u)=+infinity` by definition and `u` would be
visible.  At the point of use, the verbatim contract clause of
`lem-positive-exposedness-margin` is: “for an exact signed idempotent P with
rho = 4*tau > 0 (i.e. delta(P) > 0) and a geometrically distinct row vertex v with
nonempty far set F_v = {j : ||p_j - p_v||_1 >= rho}: t*(v) > 0; in particular every
HIDDEN geometrically distinct row vertex with F_v nonempty has 0 < t*(v) < kappa
(hiddenness forces delta(P) > 0, hence rho > 0, and no row vertex is hidden at
delta = 0).”  Thus the own-exposedness LP at every direct carrier vertex is
nondegenerate; fix a relative-interior optimal exposer `h_u*` separately at each such
carrier `u`.

The `D/M` split is taken after restricting `Gamma_f` to the labelled horn.  On the
diagonal `p_x=p_u`, the Dirac convention for a vertex kernel makes the weight exactly
the aggregated literal coefficient mass `P_fu^+` on that vertex fiber.  Push this
diagonal restriction to the distinct vertex points `u`, then partition that
coefficient measure by the literal predicate
`K_T(u) intersect K_O(u) != empty`; equality/tangency belongs to `I`, and failure is
strict disjointness.  Thus the mass-halving statements in the sub-DAG are
clone-invariant partitions of row points, not a choice of a high-weight index.

For the `I/not-I` split, the verbatim relevant clause of
`lem-always-tight-dual-support` is: “every optimal hiddenness dual witness
(lambda, alpha, beta), after deleting redundant centered-zero constraints, has
supp(lambda) contained in T, supp(beta) contained in O, and supp(alpha) contained in
Z, where T, O, Z are the rho-far, upper-box, and lower-box constraint families tight
on the WHOLE primal optimal face; T is nonempty, and O is nonempty if and only if
t*(u) > 0.”  The verbatim relevant clause of
`lem-optimal-face-conic-reduction` then identifies the witnesses as

    sum_T lambda_r*(p_r-p_u)+sum_Z a_z*(p_z-p_u)
       = t*(u)*sum_O gamma_i*(p_i-p_u),                       (3.10)

“with lambda and gamma probability vectors supported on T and O and coefficients
a_z >= 0 supported on Z” and says “a display with all a_z = 0 exists if and only if
conv{p_f - p_u : f in T} intersects t*(u)*conv{p_i - p_u : i in O}.”  Tangency is
therefore owned by `I`.  Crucially, (3.10) remains an LP certificate attached to `u`;
its multipliers are never averaged as transition mass.  `H-DI` must combine the
actual coefficient edge `f -> u`, exact reproduction at `u`, and the alpha-free
constraints in one completion problem.

On the disjoint side, apply `lem-separator-zero-face-obstruction` with its exposer
variable `h*` instantiated as `h_u*`; it supplies verbatim an affine `psi` satisfying
“`psi(p_u)=0`, `P psi=psi` on row values,
`psi(p_f)>0` for all `f in T`, `psi(p_i)<0` for all `i in O`, and there exists a
nonclone row `z` with `h*(p_z)=0` and `psi(p_z)<0`.”  Thus this blocker has
`h_u*(p_z)=0`; the dummy `f in T(u)` inside the quoted shard is carrier-local and is
not the selected web row `f` of (3.9).  Make the shipping split literal: the high side
owns equality and asserts that for some disjoint carrier `u`, some legal separator,
and its supplied blocker `z`, the blocker ships at least `c_r=1/16` positive mass to
its own `{h_u*>=kappa}` slab.  On that side, the exact
`lem-zero-face-capacity-kill` clause is “`c_r*kappa<=nu_z<=delta(P)`”, which would give
`tau/64<=tau^2`, hence `tau>=1/64`, impossible under `delta_H<=2^(-16)`.
The strict complementary side says every such separator-produced blocker ships less
than `1/16`; `H-DD` is exactly this starved-blocker subcase, not the already-killed
shipping subcase.

The off-diagonal `M` branch is where the carrier distinction remains load-bearing.
It is sent directly to `H-MX`: recurrence is available at the nonvertex intermediate
row `x`, while exposedness anatomy is available at the vertex component `u`, and no
banked operation transfers one to the other without changing the terminal geometry.
`lem-censoring-exactness` was inspected but is not consumed: its algebraic exactness
output alone does not preserve the negativity scale, visible hull, `H>16*tau`
boundary, or the coupled kernel.  Censoring is therefore a diagnostic, not a claimed
induction step; see §6.

Both `H-DI/H-DD` and `H-MX` are naturally posed in global coordinates.  Choose an
actual row basis `B` and its coefficient matrix `L`; elementary exact idempotence gives

    P=L*B,                    B*L=I.                           (3.11)

For fixed `L`, fixed entrywise sign and optimal-face cells, and fixed barycentric,
supporting, and `l1`-distance certificates for the visible-hull/depth predicates, the
remaining equations and inequalities in `B` form a finite LP.  Without those fixed
geometric witnesses only the identities `B*L=I` and the entrywise negativity cells are
automatically linear.  The proposed opposite-direction duality proof treats stable
infeasibility multipliers from these certified cells as the objects to aggregate.  It
must produce a dimension-free, clone-normalized certificate; otherwise (3.11) merely repackages the
hard leaf.  This all-row left-inverse constraint is the promised resource beyond the
W55 local gadget.

**Grade: HARD.**  The original probability web, its barycenter, and the quantifier over
every exposer have been removed.  What remains is one selected row, one discrete
antipode, and a coefficient/disintegration corner tied to that row.  This is a strictly
smaller **configuration-data space** than SL1a (not a smaller subset of matrices):
`lambda`, its barycenter variable, and its whole all-exposer profile are absent.  Neither
the mixed-carrier lifting nor the clone-uniform completion certificate is routine.

**Risk / exact-instance kill criterion.**  This is the most likely false leaf.  The
first attack is `H-MX`: complete a flat low-`(z,h*)` corner that internally reproduces
while the top remains tall and hidden.  A single exact rational family with
`delta=tau^2 ->0` satisfying (3.9), the full matrix identities, the visible-hull depth
conditions, and either horn refutes H-CCO for every proposed `delta_H`.  Conversely a
local displacement tableau is not a refutation until every row is completed and
`B*L=I` plus all-row negativity are checked.

**Mandatory red tests.**  **Proposition E:** PASS—`z<4*tau` forces both coupled
coordinates into the strict co-top band, so no shallow counterweight occurs.
**W55 starvation gadget:** PASS AS A WARNING—the `A0=5,g=5*tau` gadget, or its
co-top flat analogue, satisfies the scalar pattern and may satisfy the local corner;
H-CCO therefore does not use scalar `z,h*,psi` ledgers as its kill.  It invokes the
all-row completion (3.11); a successful exact completion of the gadget with the stated
terminal geometry is precisely the kill criterion above.  **Clone/transient:**
PASS—the statement uses row-point fibers and the joint kernel, and the proposed
certificate must include all rows of `B*L=I`; clones split mass, while rows appended by
(1.3) cannot be silently deleted and remain in the global completion branch whenever
the terminal antecedent persists.  A terminal newly created by the extension is also
quantified by H-CCO.  **Coverage:**
PASS—every hypothetical first tall web is
sent to one horn and then to `D` or `M`; every banked W52 family exits at root tallness,
so none is used as fake evidence for H-CCO.  **Proposition-D/W55/B6 walls:** PASS—the
original `(lambda,Phi_v)` pairing ends after L-S, no `lambda*P=p_v` comparison or conic
multiplier flow appears, and all `rho` tests are radial from a fixed vertex.

**Restatement test: PASS, with the strengthening explicit.**  H-CCO is logically
stronger than needed because it remembers only one top support and one optimal exposer,
but it does not contain `lambda`, the `11*tau/5` barycenter condition, or the universal
exposer hypothesis and cannot reconstruct them.  Its new object is the exact
coefficient kernel at one row; deriving it from SL1a requires L-S, L-C, and L-P, so it
is not SL1a or L2-core renamed.

## §4 THE ASSEMBLY

**Claim.** `L-S + L-C + L-P + H-CCO` imply the pinned SL1a contract.

### §4.1 Constant order

Read the sole existential leaf constant first: let H-CCO supply
`delta_H in (0,2^(-16)]`.  Set

    delta_0 := delta_H.                                      (4.1)

There is no later-dependent choice.  For every `0<delta<=delta_0`,

    tau<=1/256,
    D=2+4*delta<=2+2^(-14)=32769/16384.                       (4.2)

The source constants convert, without rounding, as follows:

    (16/13)*kappa = (16/13)*(tau/4) = 4*tau/13,              (4.3)
    2.2*tau = 11*tau/5,
    4*tau-11*tau/5 = 9*tau/5,                               (4.4)
    2*(4*tau/13)+4*tau/13 = 12*tau/13.                      (4.5)

The source depth width and far radius both remain exactly `4*tau`; neither is
weakened.  The source tallness `H>16*tau` remains strict throughout.

### §4.2 Derivation

Assume for contradiction an SL1a object `(P,v,lambda)` at
`0<delta<=delta_0`.  Thus `lambda` is supported on the strict co-top/far set `B_v`,
its barycenter `b` obeys `||b-p_v||_1<=11*tau/5`, and every admissible exposer has
`lambda`-mean at most `4*tau/13` by (4.3).

1. **Fix the legal affine observables.**  At this point the exact proved clause of
   `lem-top-deficit-price` is: “there exists a top support functional `phi` (affine,
   `phi(p_v)=H`, `phi<=0` on `conv{p_w:w in W}`, 1-Lipschitz for `l1`).”  Fix one and
   put `z=H-phi`.  Since `v` is a hidden row vertex, its far set is nonempty (an empty
   far set gives `t*(v)=+infinity`, hence visibility).  The exact proved clause of
   `lem-positive-exposedness-margin` is: “every HIDDEN geometrically distinct row
   vertex with `F_v` nonempty has `0<t*(v)<kappa`.”  The finite exposedness LP
   therefore has a nonempty optimal face; fix a relative-interior optimal exposer
   `h*`.  It is admissible.

2. **Select one web row and retain the barycentric counterweight.**  Apply L-S to
   `(lambda,phi,h*)`.  Equations (4.3)–(4.5) are exactly its hypotheses and yield
   `f,e in supp(lambda)` with

       2*z_f/D+h*(p_f)<=12*tau/13,
       ||p_f-p_e||_1>=9*tau/5.                               (4.6)

   Both rows retain the original closed far condition and strict depth condition.
   This is the only use of the original barycenter and the only pairing with
   `lambda`; no contradiction is sought here.

3. **Choose the vertex kernel without changing carriers.**  By elementary
   finite-polytope convexity, every row point is a convex combination of the
   geometrically distinct extreme row vertices.  Choose a probability kernel `xi`
   realizing those combinations, with the Dirac choice at vertex points, and form the
   joint measure

       Gamma_f(x,u)=P_fx^+*xi_x(u).                          (4.7)

   The actual coefficient coordinate `x` is not discarded.

4. **Use exact reproduction at the non-top row.**  Apply L-C to the data in
   (4.6)–(4.7).  Its hypotheses include (4.2), and its endpoint computation is

       Gamma_f(C_f)
          >= 1-3*D/13-tau*(D+1)/2
          >= 58079731/109051904
          > 1/2.                                             (4.8)

   Thus both the actual row coordinate and the vertex coordinate are simultaneously
   `z<4*tau`, `h*<4*tau` on more than half a unit of coefficient-kernel mass.  From
   `H-d<=z`, each is strictly co-top.  This is the required Proposition-D escape:
   the new information came from row reproduction at `f`, not from further
   `(lambda,Phi_v)` pairings.

5. **Own the radial boundary.**  Apply L-P to `Gamma_f|C_f`.  Exactly one label is
   produced: either

       sigma=F: far-u mass >=1/4,                             (4.9F)

   with equality included, or

       sigma=N: far-u mass <1/4 and near-u mass >1/4.         (4.9N)

   There is no seam and no claim of mutual `rho`-separation.

6. **Invoke the terminal completion leaf.**  The data
   `(P,v,phi,h*,f,e,xi,Gamma_f,sigma)` satisfy H-CCO item by item: (root) exact
   idempotence, nonempty `W`, hidden top and `H>16*tau`; (4.6) the two selected rows,
   antipode scale, and score; (4.7)–(4.8) the exact coupled corner; and (4.9F) or
   (4.9N) the labelled horn.  Also `delta<=delta_0=delta_H`.  H-CCO says no such
   tuple exists, a contradiction.

Therefore no SL1a counterexample exists for `0<delta<=delta_0`; since `delta_H>0`,
this proves the pinned existential contract modulo the four leaves.  Notice that the
assembly used every pinned constant: `2.2` only in the antipode conversion (4.4),
`16/13` only in the score conversion (4.3)–(4.5), both occurrences of `4*tau` in
the unchanged far/depth predicates and the corner, and `16*tau` in the terminal
tall/hidden geometry.

### §4.3 Assembly red-test ledger

**Proposition E:** PASS.  The only conditioning/restriction is to `z<4*tau`, which
implies the original strict depth band; the shallow counterweight never enters.
**W55 exact starvation gadget:** PASS AS A WALL.  Steps 1–5 are deliberately
compatible with its co-top flat analogue; the contradiction occurs only at H-CCO,
whose stated mechanism consumes global `P=L*B`, `B*L=I` completion and all-row
negativity.  **Clone/transient:** PASS.  Every operation is on row-point measures,
full coefficient fibers, or the joint kernel; the terminal leaf retains all rows in
the completion problem, and the exact extension (1.3) has no untracked coefficient
column for an old selected row.  **Non-vacuity/coverage:** PASS.  A hypothetical first tall
web traverses every pipeline edge and exactly one horn; the known W52/banked families
fail the root, as recorded in §5.  **Proposition D:** PASS.  The only use of
`(lambda,phi,h*)` is selection; exact reproduction at the other row `f` is the
load-bearing bridge.  **W55 forbidden identifications:** PASS.  Neither `lambda*P`
nor any conic multiplier is compared with `p_v`, and `Gamma_f(x,u)` keeps flow and
vertexization coordinates separate.  **B6:** PASS.  The only pairwise bound is
`9*tau/5`, while every `rho` split is radial from `v`.

## §5 COVERAGE CHECK

This section is evidence and routing only; no census value or gadget is used in
§4.  The root requirement `H>16*tau` implies

    H^2/delta > 256,                                         (5.1)

whereas `context/FINDINGS.md` and the W52 census discussion report
`H^2/delta<16` for every banked instance.  Thus the honest location of every known
exact family is a named **pre-root exit**, not a fabricated internal horn.

| Known family / test object | Identifiable location | Why there is no uncovered space |
|---|---|---|
| `HA_t / HA_eps` delta-inflation families | `R0-not-tall` | Their attempted height increase inflates `delta`; the reported ratios remain below the root threshold (5.1). |
| Deep-append-turns-visible family | `R0-not-hidden` (and also not tall in the banked range) | The appended deep row becomes visible before it can be a hidden top.  H-CCO never assumes it is hidden by fiat. |
| TOP-preserving reversion family | `R0-not-tall` | The top geometry reverts while the reported ratio stays sub-tall; intersection/disjointness is therefore not spuriously assigned. |
| Best disjoint frontier | `R0-not-tall` | It genuinely has disjoint anatomy but `H` is far below the `16*tau` gate, so the hard leaf's disjoint descendant is not claimed to explain it in-class. |
| Proposition-E two-point counterweight cap system | `R0-not-co-top` | Its shallow counterweight violates the strict support condition `d>H-4*tau`; every later restriction preserves that condition. |
| W55 `A0=5,g=5*tau` local starvation gadget | `H-CCO refuter gate`, not yet an exact instance | It realizes the scalar front-end threat, but lacks global completion with the tall visible hull and all-row negativity.  A completed rational family would enter exactly one H-CCO horn and refute the hard leaf. |

For a future exact family there is a complete routing checklist.  If it lacks a hidden
top, tallness, nonempty `W`, or a strict co-top web, it exits at `R0`.  Otherwise L-S
selects `(f,e)`, L-C accepts vertex or nonvertex intermediate rows without loss,
L-P assigns equality to the far horn, and H-CCO assigns every coupled atom to its
diagonal or off-diagonal subbranch.  No rank, raw support size, or number of transient
rows creates an additional case.

The absence of banked in-class data is not offered as evidence that H-CCO is true.
Non-vacuity instead comes from two explicit checks on the author-claim pipeline:
L-S–L-P are stated for every putative SL1a object without a generic-position
assumption, and the W55 tableau shows that their scalar conclusions are mutually
consistent locally.  Consequently the decomposition does not win by an empty routine
leaf; it exposes global completion as the sole hard
surface.

## §6 HONEST ASSESSMENT

**Verdict on the decomposition surface.**  There are four leaves: L-S and L-P are
EASY, L-C is MEDIUM, and H-CCO is the permitted single HARD leaf.  The first three
are bounded bookkeeping tasks.  All unresolved mathematics is localized in a global
completion obstruction for one selected web row.

**Most likely false / first refuter target.**  H-CCO, especially its off-diagonal
`H-MX` descendant, is the clear risk.  The front end compresses the original
all-exposer web to one top support, one optimal exposer, an antipodal row, and a
low-low coefficient kernel.  Although this is genuine surface reduction, it is also a
logical strengthening: the hard leaf no longer gets the full barycenter or the family
of all admissible exposers.  A flat internally reproducing plateau may therefore
satisfy H-CCO without supporting any SL1a probability measure.  The first refuter job
is an exact rational `tau->0` completion of that plateau, not another scalar-moment
example.

**What a prover must actually add.**  In the diagonal branch, combine the literal
coefficient edge with each carrier vertex's own exact reproduction and whole-optimal-
face anatomy; do not average the displays.  In the mixed branch, either prove a
clone-uniform controlled-censoring lemma or extract dimension-free stable
infeasibility multipliers from the fixed-`L` completion LP.  A certificate norm that
grows with the number of row points is a failure, not a dimension-free proof.

**Parallel work that is independently dispatchable now.**

* L-S: a short exact proof audit of (3.1)–(3.2), including the `9/5` boundary.
* L-C: an independent rational check of the two-marginal identity and fraction
  `58079731/109051904`; this shares no unproved input with H-CCO.
* L-P: a one-page boundary-ownership verifier.
* H-DI: alpha-free-display completion on the direct carrier, independent of the
  off-diagonal carrier problem.
* H-DD: starved separator-blocker completion after the `c_r=1/16` capacity rejection.
* H-MX: fixed-sign `P=L*B`, `B*L=I` completion/refutation and, separately, a
  clone/transient audit of candidate dual certificates.

**Redesign relative to the inherited §2.**  I replaced the marginal
`m_u=sum_j P_fj^+ xi_ju` / “same-carrier recurrence” picture by the joint kernel
`Gamma_f(x,u)=P_fx^+xi_x(u)` and added the `9*tau/5` antipode: this preserves the
actual transition coordinate, makes vertexization an explicit MEDIUM leaf, and uses the
target's `2.2*tau` barycenter instead of silently discarding it.

**Pruned alternative decompositions.**

* More `(lambda,Phi_v)` moments: dropped because
  `lem-intersection-witness-confinement` caps their average and
  `lem-l2-core-collapse` makes finite averages a single support functional on rows.
* Direct comparison of `lambda*P` with `p_v`: dropped by the W55 identity-level wall;
  the zero-face conic correction is unbounded.
* Treat the `u`-marginal of `Gamma_f` as transition mass: dropped because it erases
  the intermediate row `x`, exactly the same-carrier error.
* Pure actual-row return leaf with no vertex kernel: valid as a front-end strengthening
  (`P_f^+` returns mostly to a co-top low slab), but dropped because it leaves
  nonvertex support unresolved inside the hard leaf.
* Thin/thick split from one separator moment: dropped because recurrence,
  transversality, and vertexhood need not occur on the same carrier.
* Carré-du-champ/variational score flatness: dropped as a closer; a flat W55-style
  plateau satisfies the stationarity and energy ledgers.
* Opposite-direction Farkas duality as a MEDIUM leaf: dropped because `P=L*B` is
  bilinear until `L` is fixed and no proved input gives a clone-uniform certificate
  bound; it remains an honest H-MX mechanism.
* Induction on geometrically distinct vertices as a completed route: dropped because
  no proved deletion lemma simultaneously controls `delta`, the visible hull, and the
  SL1a depth band; exact censoring supplies only the algebraic start.
* Pairwise-`rho` web rigidity: dropped because the only forced antipode here is
  `9*tau/5` (and the prior B6 scale is also below `rho`).

No conjecture shard is a premise anywhere in the assembly.  Proving H-CCO would finish
this decomposition; refuting it would not refute SL1a automatically, but would show
that the compression to one score/exposer lost essential global web information and
force a redesign retaining a larger barycentric object.
