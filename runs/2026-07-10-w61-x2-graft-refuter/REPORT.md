# W61 decider A — PARTIAL

**Verdict: PARTIAL.  X2 was not refuted.**  The exact family below realizes the
registered thin nonclone freight mechanism and satisfies every checked
selected-corner clause except the indispensable tallness inequality
`H > 16*tau`.  This is L3 constructive evidence only: it is neither a proof of
X2 nor a proof of any weaker exclusion.

## Exact partial family

Put `q=1/k`, `d=q^2`, and `t=q/8`, with `k >= 512`.  In affine coordinates
relative to `(u,o,a)`, take

```
u = (1,0,0)
z = (1+d(1-t), td, -d)
o = (0,1,0)
a = (0,0,1)
x = (0,d,1-d)
y = (0,-d,1+d)
```

and set `P=L B`, where the rows of `B` (columns ordered `u,z,o,a,x,y`) are

```
(1,0,0,0,0,0)
(0,0,1,0,0,0)
(0,0,0,1/2,1/4,1/4).
```

The script verifies `B L=I`, hence `P^2=P`, and verifies all row sums and
`delta(P)=d` exactly.  The row points `a` and `x` lie strictly on the `o-y`
edge.  Splitting the `a`-column as `(1/2,1/4,1/4)` therefore gives row `f=a`
constant positive incoming mass on the genuinely nonvertex sources `a,x`,
while their displacement from vertex `y` is respectively `2d` and `4d`.
This is a balanced factorized graft, not raw-index cloning.

The exact visible set is `W={z,o,y}`.  Vertex `u` is the unique hidden top,
with

```
t*(u) = t - d(1-t) < q/4,
H      = 2d (t(1+d)-d)/(1+2d) > 0.
```

An exact primal closest point on the `z-y` edge and a matching 1-Lipschitz
support functional certify this height.  Taking the zero admissible exposer,
`f=a`, the displayed legal vertex kernel in `certificates.json`, and `B=B_F`,
the quotient-fiber calculation gives

```
Gamma_f(B_F) = 1/(1+d)                         >= 1/4,
M_X(B_F)     = (3-d)/(4(1+d))                  > 1/8,
T_B          = q(2-d)/(1+d)                    < 2q -> 0.
```

The strict off-diagonal test is applied to row vectors: `(a,y)` and `(x,y)`
are off diagonal, while `(y,y)` is diagonal.  There are no clones in this
family, and `xi` is checked by exact probability and barycenter identities.

## Exact obstruction

Tallness fails, and it fails asymptotically rather than at a boundary:

```
H/q = 2q^2 ((1+q^2)/8-q)/(1+2q^2) -> 0,
```

so this family has `H << 16q`.  At `k=512`, for example,

```
delta = 1/262144,
H     = 258049/140738562097152,
T_B   = 524287/134218240.
```

Thus these are not selected-corner configurations and not bad H-X data.  The
certificates are explicitly labeled partial so they cannot be mistaken for
the successful-refuter format requested in the X2 branch.

## Shapes tried and dead ends

- **Ordinary transient-row append.**  Under the standard append that preserves
  every old row, the appended state is a zero column in those old rows.
  Consequently an old selected row has `P_{f,x}^+=0`; the new transient row
  carries no incoming Gamma freight.  This is the exact graft-convention blocker recorded in
  `obs-thin-zero-face-blocker-graft`.
- **Balanced factorized split.**  Replacing one carrier column by weights
  `(1/2,1/4,1/4)` on a center and a symmetric pair preserves `B L=I` and
  succeeds on constant quotient freight, legal disintegration, mass, and
  vanishing transport.  Embedded in the banked thin zero-face geometry, it
  gives the six-row family above.  Its exact blocker is solely
  `H>16*tau`: the hidden height is `O(tau^3)`.
- **Low-rank long-chain probe.**  As non-certifying route triage, floating LPs
  were run for rank-three regular polygons and parabolic chains with
  `n=4,5,6,8,10,16,24,32,48`.  The optimized row negativity stayed bounded
  away from zero (about `0.21` for the circle and `0.11` for the parabola), so
  these fixed-rank shapes did not enter the required small-delta regime.  No
  numerical output from this probe is used as a certificate or exact claim.

## Compute and files

`search.py` uses only Python `fractions.Fraction` for the certified family.  It
checks the three instances `k=512,1024,2048`, all matrix/factor identities,
row-point geometry, explicit exposedness lower/upper certificates, the visible
set, exact height primal/dual certificates, `phi`, `h`, `f`, every `xi`
barycenter, the positive Gamma support of `B_F`, and the three target
quantities.  All checks are assertions; `python3 search.py` prints the verdict
table.  `certificates.json` contains the same three partial matrices and data.

Again, this report is constructive/numerical evidence only.  The search did
not refute X2, and failure to cross the tallness clause is not a proof of X2.
