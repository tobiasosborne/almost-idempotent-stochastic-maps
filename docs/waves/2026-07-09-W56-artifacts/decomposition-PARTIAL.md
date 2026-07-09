# W56 — Tier-2 decomposition of SL1a

AUTHOR-CLAIM strategy material only.  Nothing in this file promotes SL1a or any new
leaf.  The only established inputs used below are registry shards whose front matter
says `status: proved`; every such use quotes the consumed clause.  All measures are
measures on row **points** (equal row points are coalesced), all support language is
geometric, and all constants are independent of the number of rows.

## §1 THE PINNED TARGET

> **(CONJECTURE) Co-top straddling-web exclusion (SL1a).** There exists universal
> `delta_0 > 0` such that no exact signed idempotent `P` with
> `0 < delta(P) <= delta_0`, nonempty visible set, and hidden top vertex `v` of height
> `H > 16*tau` admits a probability measure `lambda` on rows that are simultaneously
> `rho`-far from `v` (`||p_f-p_v||_1 >= 4*tau`) and co-top
> (`dist_1(p_f, conv W) > H-4*tau`), with barycenter within `2.2*tau` of `p_v` and
> with average value at most `(16/13)*kappa` under every admissible exposer at `v`.
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

* `lem-top-deficit-price` (`status: proved`) says that there exists a top support
  functional `phi`, “affine, `phi(p_v)=H`, `phi <= 0` on `conv W`, 1-Lipschitz for
  `l1`,” and that for any such functional `z_j=H-phi(p_j) >= 0`.  Its proof-contract
  also gives `z_j <= D=2+4*delta` on every row.  Thus `z/D` is an admissible exposer
  at `v`.
* `lem-harmonic-affine-bridge` (`status: proved`) says: “a vector `g` satisfies
  `Pg=g` if and only if there exists `u` with `g_i=u.p_i` for every row index.”  In
  particular every affine row-value function distributes through **each** row
  reproduction; this is used at the selected web row, not merely at `v`.
* `lem-genuine-disintegration` (`status: proved`) permits one to “fix for every row a
  vertex representation `p_j=sum_v lambda_jv p_v` over geometrically distinct row
  vertices” and supplies a quantity `M_i^a` “supported entirely on HIDDEN row
  vertices at depth in `(a*tau,H]`,” with

      g_i <= M_i^a
             + sum_{j in G_a} P_ij^+*(H-d_j)/(H-a*tau).

  This exact clause is the same-carrier vertexization used below; no assertion that
  arbitrary disintegration preserves `rho`-farness is made.
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

Two further proved clauses are walls, not positive inputs.  By
`lem-intersection-witness-confinement`, in an alpha-free display the witness average
under every admissible exposer is at most `t*(v)` and its average deficit under every
top support functional is at most `t*(v)D`.  By `lem-l2-core-collapse`, “every finite
convex average of top support functionals at `v` coincides ON THE ROW SET with a
single top support functional.”  Accordingly no edge below tries to obtain a
contradiction from `(lambda,Phi_v)` pairings or from averaged top faces.

All sums such as `P_fx^+` are henceforth aggregated over the full fiber of the row
point `x`; a split of one row point into clones merely splits that mass.  A fixed
vertex representation is likewise a probability kernel on geometrically distinct row
points.  This is the convention under which every displayed measure is clone-invariant.

## §2 THE DAG

Set once and for all

    delta_bar := 2^(-16),       tau := sqrt(delta),
    D := 2+4*delta,             c_SL*tau := (16/13)*kappa = 4*tau/13.

Suppose provisionally that an SL1a counterexample `(P,v,lambda)` exists with
`delta <= delta_bar`.  Choose any top support functional `phi`, put
`z=H-phi`, and choose a relative-interior optimal exposer `h*` at `v`.

The DAG has three routine leaves and one hard terminal leaf:

```text
R  SL1a web (far + d>H-4tau + all-exposer mean <=4tau/13)
|
S  L-S: affine selector
|         choose f in supp(lambda), still far and d_f>H-4tau,
|         with 2 z_f/D + h*(p_f) <= 12tau/13
|
V  L-V: reproduce at this f and disintegrate on the same carrier
|         m = P_f^+-weighted mass on distinct vertices u with d_u>H-4tau
|         m(total)>3/4 and integral h* dm <= tau(12/13+tau)
|
P  L-P: discard h*>=4tau mass; more than 1/2 remains
|         Q := m{h*<4tau and ||p_u-p_v||_1>=4tau} >= 1/4 ?
|            (equality belongs to Q)
|          /                                                   \
|       Q yes                                                Q no
|       far horn mass >=1/4                         near horn mass >1/4
|          \                                                   /
|           H-SCCO: same-carrier co-top completion obstruction [HARD]
|                         (one leaf, branch-labelled)
X  contradiction
```

Here `m` is not an arbitrary measure.  For fixed convex vertex representations
`p_j=sum_u xi_ju p_u`, define

    G := {j : d_j > H-4*tau},
    m_u := sum_{j in G} P_fj^+ * xi_ju * 1_{d_u>H-4*tau}.

Thus the hard object is a single selected row and its genuine one-step positive
transport onto global row vertices; it is not the original probability `lambda` and is
not a dual multiplier.

### §2.1 Exhaustiveness and boundary ownership

`L-S` and `L-V` are a pipeline, so they introduce no cases.  `L-P` proves

    m{u : h*(p_u)<4*tau} > 1/2.

Partition this set by the literal predicate
`||p_u-p_v||_1 >= 4*tau`.  If its far mass is at least `1/4`, including equality,
the far horn owns it.  Otherwise its far mass is strictly below `1/4`, so the near
mass is strictly above `1/4`; the near horn owns the strict complement.  These are
row-point mass sums, not support counts.  No pairwise separation of carrier vertices
is asserted: the only `rho` predicate is radial distance from the fixed top `v`, so the
B6 scale gap is respected.

The hard leaf is parameterized by the horn label and excludes both terminal tableaux
in one statement.  Consequently every counterexample at `delta <= delta_bar` follows
one and only one path from `R` to `H-SCCO`; no boundary instance is lost.

## §3 THE LEAVES

_Built incrementally after the mandated resource audit._

## §4 THE ASSEMBLY

_Built incrementally after the mandated resource audit._

## §5 COVERAGE CHECK

_Built incrementally after the mandated resource audit._

## §6 HONEST ASSESSMENT

_Built incrementally after the mandated resource audit._
