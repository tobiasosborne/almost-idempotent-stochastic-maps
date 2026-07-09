<!--
ROLE: W55 strategy wave for conj-cotop-web-coupling (L6.5), session 14.
STATUS DISCIPLINE (L0): STRATEGY / AUTHOR material. The exact reductions E1-E5 and the
  small-gauge bridge passed two independent hostile reviews in this wave, but are NOT
  registry shards and NOT L0-rigorous. The coupling conjecture remains OPEN.
-->

# Wave W55 — co-top web coupling: starvation corner and completion obstruction

**Target:** `conj-cotop-web-coupling`. **Method:** decomposition-first. Three independent
lanes were used: an algebraic prover, a decomposition prover, and an adversarial refuter;
the synthesized tree then received two further hostile reviews. No status is promoted.

## Verdicts

**Algebraic lane:** `PARTIAL` — the hybrid measure `lambda*P` admits a non-tautological
co-top localization, but the exact comparison with the top row contains the unbounded
zero-face conic term. It must never be identified with `p_v`.

**Decomposition lane:** `PARTIAL` — starvation propagates by `P^2=P` into a high-return
near corner; small conic gauge reduces to SL1a/SL1b. A proposed thin/thick large-gauge
split was submitted for review.

**Adversarial lane:** an exact local starvation gadget satisfies every current scalar
ledger, even with `g/tau=5`; only global completion to a low-negativity projection remains
unresolved. Transient-row extensions are a mandatory invariance test.

**Hostile review 1:** `INVALID AS A PROOF STRATEGY, WITH A SOUND E1-E4 FRONT END.` The
small-gauge branch is repairable; “conic recurrence” incorrectly treated dual multipliers
as transition mass, and thin-corner collapse does not follow from one separator moment.

**Hostile review 2:** `PARTIAL / CONDITIONAL IMPLICATION ONLY.` E1-E5 and the small-gauge
bridge check; the moderate and large branches require genuinely new lemmas. Vertexization,
same-carrier recurrence/transversality, and exposure were not supplied.

## Exact front end: starvation creates a high-return corner

Let
`A={j: ||p_j-p_v||_1 >= 4*tau, d_j > H-8*tau}`, set
`eps=sum_{j in A} P_vj^+`, and write `L_i(S)=sum_{j in S} P_ij^+`.
Assume for contradiction `eps < 2^-10`. Fix a top deficit `z=H-phi` and a
relative-interior optimal exposer `h*`.

**E1 (two-step positive flow, hostile-checked).** For every index set `S`,

```text
sum_i P_vi^+ L_i(S)
 <= L_v(S) + (1+nu_v)*delta + nu_v*(1+delta)
 <= L_v(S) + 2*delta*(1+delta).
```

This is a direct sign split of `P^2=P`. Thus starvation by `v` propagates to almost every
row that `v` funds; unlike the hiddenness witness, this is genuine `P`-flow.

**E2-E3 (inner-corner concentration, hostile-checked).** With `eta=1/16`, define

```text
K_eta = {i: ||p_i-p_v||_1 < 4*tau, z_i < tau, h*_i < tau,
            L_i(A) <= eta}.
```

The top-deficit and exposer ledgers, followed by E1, give

```text
P_v^+(K_eta)
 >= 1 - 17*eps - (3+4*delta)*tau - 32*delta*(1+delta).
```

For example, at `tau <= 2^-9` and `eps <= 2^-10`, this exceeds `15/16`.

**E4 (corner return, hostile-checked).** Put

```text
N = {j: ||p_j-p_v||_1 < 4*tau, z_j < 8*tau, h*_j < 1/4}.
```

For every `i in K_eta`, `lem-psi-corner-trap` gives

```text
L_i(N) >= 7/8 - eta - (35/8)*tau - 4*tau^2 > 3/4
```

under the same ceiling. The complement is covered by `{z>=8*tau}`, `{h*>=1/4}`, and
the target set `A`; no count or `t*` division occurs.

**E5 (nontriviality, hostile-checked).** Disjointness plus the separator blocker and
zero-face vertex-support shards put a geometrically distinct hidden `h*=0` row vertex in
`N`. Hence failure of coupling produces a nontrivial high-return near-top corner, and
that corner also contains a hidden zero-face vertex. The reviewed statements do NOT put
return and zero-face vertexhood on the same carrier, and do not yet force exposure: the
gadget below realizes the local picture.

## Small conic gauge: a checked bridge to SL1a/SL1b

For a fixed reduced optimal display, write `A0=sum_Z a_z`. If `delta<=1/64` and
`A0<=3/32`, then

```text
||sum_T lambda_f*(p_f-p_v)||_1
 <= t*(2+4*delta) + 4*tau*A0 < (57/64)*tau.
```

Let `mu=lambda{f: d_f<=H-4*tau}`. If `mu>tau/(2+4*delta)`, its shallow restriction is
exactly an SL1b subprobability: it is rho-far and shallow, and every admissible exposer has
integral below `kappa`. If `mu<=tau/(2+4*delta)`, conditioning on the co-top part gives

```text
barycenter radius < (484/223)*tau < 2.2*tau,
all-exposer mean < (256/223)*kappa < (16/13)*kappa,
```

which is exactly the SL1a object. Therefore, conditionally,

```text
SL1a + SL1b  =>  every disjoint reduced display has A0 > 3/32.
```

This is the clean W55 link between the Branch-I and Branch-II leaves. It should be
codified only after a fresh standalone prover/verifier pass.

## Moderate gauge: the mixed co-top straddle

For `3/32<=A0<=1`, first use SL1b to delete the `O(tau)` shallow lambda-mass. Normalize
the remaining co-top lambda-mass together with the zero-face conic mass. The result is a
probability `theta` with

```text
support(theta) subset {d>H-4*tau},
||bar(theta)-p_v||_1 < 2*tau,
integral h dtheta <= kappa for every admissible h,
theta(F_v) >= 2/5,
theta{rho-near v and h*=0} >= 1/24.
```

**New candidate (OPEN): mixed co-top straddle exclusion.** No tall hidden top admits such
a measure. This is cleaner than L6.5 (no `P_v` coefficient conclusion, disjointness, or
unbounded gauge in the statement), but it is not implied by SL1a: its far rows need not
be vertices or pairwise rho-separated, and conditioning loses the SL1a constants.

## Large gauge: the actual new-math wall

For `A0>=1`, normalizing `zeta_z=a_z/A0` does yield small average top deficit and small
average `L_z(A)` under starvation; a fixed majority of the conic weight lies on zero-face
rows with `z_z<2*tau` and `L_z(A)<1/16`, each shipping more than `2/3` positive mass into
`N`. These are valid moment statements only. The `a_z` are dual LP multipliers, not
transition weights, so “conic-weighted recurrence” is not a conclusion.

The required new theorem is instead a **global completion obstruction**: a fixed-display
large-`A0` starvation cell satisfying E1-E5 cannot be completed to an exact projection
with every row negativity `O(tau^2)`; some row must pay `>=c*tau` negative mass. Since
`delta=tau^2`, this would close the branch for small `tau`.

The natural coordinates are `P=L*B`, `B*L=I`, so `P_ij=l_i*b_j` and
`sum_j b_j*l_j^T=I`. A proof must use the all-row constraints
`sum_j (-l_i*b_j)_+<=tau^2` together with the high-return corner and the reduced display.
That global left-inverse information is precisely what the harmonic ledgers omit.

## Exact local refuter target

Let `s=tau`, `t=s^2`, and choose centered displacements with

```text
F + 5*Z = t*O,       ||Z||_1=s,
p_w-p_v = (s/(1+s))*F,
P_vv=1-s, P_vw=s+s^2, P_vf=-s^2.
```

Then row reproduction at `v` is exact, `nu_v=s^2`, all positive mass is rho-near, and
the far row receives no positive inflow. The display `(lambda,a,gamma)=(delta_f,5,delta_o)`
can have `t*=s^2` and `g=5*tau`. Hence no proof using only `z,h*,ell,psi` can work.

This is not a counterexample until it is completed to a full exact idempotent with the
tall visible-hull geometry and row negativity `<=s^2`. Fixing a rational `L(s)`, sign
cells, visible anchors, and distance witnesses makes `B*L=I` plus negativity constraints
an exact LP. A rational feasible family refutes L6.5; stable dual infeasibility multipliers
are the intended discovery route to the completion obstruction. Numerics remain L3.

## Pruned routes and next attack

- DEAD: direct witness averaging; direct `lambda` to `P_v^+`; any `t*` division.
- DEAD: `g/A0` thin/thick split from one separator moment; transversality and recurrence
  can live on different carriers.
- REQUIRED invariance tests: transient-row extension, clone splitting, nonvertex T rows,
  and the exact `A0=5,g=5*tau` gadget.

**Display convention:** fix one reduced optimal display before the gauge split; all three
branches and every `A0` below refer to that display. No minimum-gauge attainment is used.

**Next order:** (1) standalone prover/verifier pass on E1-E5; (2) same for the small-gauge
bridge; (3) exact completion/refutation LP for the gadget; (4) mixed co-top straddle jointly
with SL1a; (5) only then formulate the factorization-level completion theorem.
