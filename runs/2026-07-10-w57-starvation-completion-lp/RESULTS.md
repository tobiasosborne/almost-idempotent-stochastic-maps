# Exact decision results

Status: **AUTHOR-CLAIM**. Exact rational certificates are supplied for hostile
mechanical checking. This report does not promote H-X, L6.5, or a new registry
shard.

## Outcome

**INFEASIBLE-CERTIFICATE, scoped to the minimal rank-three actor-hull family.**
All three decided support cases are infeasible. The certificate is stronger
than the literal metric and geometry cells: it proves that even after dropping
those cells, $BL=I$ and the necessary individual consequences of the
all-row budget $\nu_i\le s^2$ are inconsistent.

This is not a global decision of the starvation completion question. Rank three
with an additional vertex outside the actor hull is the first unresolved case;
general higher-rank/redundant-support cases are also outside this certificate.
Consequently there is no H-X refuter here, and neither H-X nor L6.5 is proved.

| case | rank / support pattern | exact verdict | independent raw check |
|---|---|---|---|
| `literal_r3_actor5` | $r=3$; five W55 actors, arbitrary unknown sign cells, clone aggregates allowed | infeasible | PASS |
| `hx_near_r3_actor5` | same actor cell plus row-$f$ near freight through $w\mapsto(v,f)$ | infeasible | PASS |
| `hx_far_r3_nonvertex6` | actor5 plus one zero-top midpoint freight row, compressed by nonvertex aggregation | infeasible | PASS |

The two H-X-named cases verify the exact near/far kernel and off-diagonal mass
arithmetic, but they are **formal constrained horn relaxations**, not realized
H-X selected-corner data. In the canonical actor polytope, $f$ and $z$ are
visible and $v$ is too close to their visible hull. The full co-top/tall/hidden
cells formulated in `FORMULATION.md` are therefore empty before a genuine H-X
instance appears. The checker deliberately reports only the algebraic gadget,
metric obstruction, freight arithmetic, Farkas identity, and stability bounds;
it does not print an H-X geometry PASS.

## Exact obstruction

With $e=(P_{fv},P_{fz},P_{zf},P_{ov},P_{ow})$, the raw certificate gives five
strictly positive rational multipliers $N_i$ and six unrestricted $BL=I$
equality multipliers such that

\[
\sum_iN_i e_i=-M.
\]

If every row has negative mass at most $t=s^2$, then every $e_i\ge-t$, forcing
$M\le t\sum_iN_i$. At $A=5,s=1/256$, the exact contradiction is

\[
M-t\sum_iN_i
=\frac{555569345906618009855}{18446744073709551616}>0,
\]

and

\[
\frac{M}{\sum_iN_i}
=\frac{434073047116546305}{2260705411136539904}.
\]

Independently, the actor-only metric cell is impossible because the $D$ moment
gives

\[
1\le A\|D\|_1=As<1.
\]

The full formulas and equality multipliers are in `CERTIFICATE.md` and the raw
JSON files.

## Stability

The checker rederives the exact rational bounding chain

\[
N_0<1,\quad N_1<8,\quad N_2<253,\quad N_3<1,\quad N_4<1,
\]

so $D_*:=\sum N_i<264$, while $M>A^2\ge16$. Therefore, uniformly for every
rational $A\in[4,6]$ and $0<s\le1/256$,

\[
\frac{M}{D_*}>\frac2{33}>\frac1{65536}\ge s^2.
\]

The multipliers do not use the norm, distance, or $g$ constraints. Adding any
requirement $g\in[4s,6s]$ cannot restore feasibility. For the nonvacuous
singleton tableau, $g$ is linked to $A$ by $g=As$; no independent two-parameter
singleton perturbation is claimed.

## Equality-only relaxation and the mechanism boundary

The raw files include an exact sample

\[
B=(c,\ e_z-c,\ e_o-c)^T
\]

that satisfies $BL=I$, $P^2=P$, all row sums, both affine gadget identities,
and the top-row coefficient pins. It deliberately drops the norm and negativity
thresholds. The checker recomputes

\[
\delta(P)=\frac{21475229695}{4294967296}>s^2,
\qquad
\|Z\|_1=\frac{65537}{32768}>s.
\]

Thus the left-inverse/reproduction equations are consistent. Three distinct
constraints block this nearby algebraic relaxation:

1. the five-entry Farkas identity blocks the all-row $s^2$ negativity budget;
2. the $D$ moment blocks the literal $\|Z\|_1=s$ pin in actor-only support;
3. fixed exposers for $f,z$ block the tall/hidden/co-top geometry without a new
   vertex.

An extra vertex is exactly what can alter all three mechanisms, and is the next
undecided support family.

## Verbatim `decide.py` output

```text
CASE literal_r3_actor5 INFEASIBLE margin=555569345906618009855/18446744073709551616 R=434073047116546305/2260705411136539904
CASE hx_near_r3_actor5 INFEASIBLE margin=555569345906618009855/18446744073709551616 R=434073047116546305/2260705411136539904
CASE hx_far_r3_nonvertex6 INFEASIBLE margin=555569345906618009855/18446744073709551616 R=434073047116546305/2260705411136539904
STABILITY PASS A in [4,6], 0<s<=1/256; certificate ignores added g constraints, singleton locus g=A*s
RAW 3 certificate files written
```

## Verbatim `check.py` output

```text
PASS hx_far_r3_nonvertex6 BL=PASS P2=PASS affine_gadget=PASS metric_obstruction=PASS Farkas=PASS stability=PASS sample_budget=FAIL(expected-relaxation) sample_norm=FAIL(expected-relaxation) margin=555569345906618009855/18446744073709551616
PASS hx_near_r3_actor5 BL=PASS P2=PASS affine_gadget=PASS metric_obstruction=PASS Farkas=PASS stability=PASS sample_budget=FAIL(expected-relaxation) sample_norm=FAIL(expected-relaxation) margin=555569345906618009855/18446744073709551616
PASS literal_r3_actor5 BL=PASS P2=PASS affine_gadget=PASS metric_obstruction=PASS Farkas=PASS stability=PASS sample_budget=FAIL(expected-relaxation) sample_norm=FAIL(expected-relaxation) margin=555569345906618009855/18446744073709551616
OVERALL PASS
```

The two `FAIL(expected-relaxation)` fields are intentional checks of the
non-feasible sample, not certificate failures.

## Raw files

- `raw/literal_r3_actor5.json`
- `raw/hx_near_r3_actor5.json`
- `raw/hx_far_r3_nonvertex6.json`

## Candidate lemma contract

**Minimal actor-hull starvation completion obstruction:** There is a universal rational $s_0>0$ such that, for every $0<s\le s_0$, no rank-three exact signed idempotent with row negativity at most $s^2$, after clone aggregation and deletion of zero-top nonvertex rows in the local actor hull, can have five factor-row fibers $v,w,f,z,o$ satisfying $F+A Z=s^2O$, $p_w-p_v=sF/(1+s)$, $A\in[4,6]$, and the pinned top-row fiber masses $(1-s,s+s^2,-s^2,0,0)$.
