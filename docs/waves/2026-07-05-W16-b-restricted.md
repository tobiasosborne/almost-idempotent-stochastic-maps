<!--
WAVE: arm G wave 16 (conj-b-restricted prove-or-amplify) — 2026-07-05, session 8, bd aism-cpn.
WORKER: fresh codex exec (prompt: session scratchpad PROMPT-w16-b-restricted.md). Answer VERBATIM below.
ORCHESTRATOR: both worker scripts rerun clean (exit 0); headline best point INDEPENDENTLY
  recomputed (runs/2026-07-05-w16-clean-block-b/scripts/orch_verify_best_point.py — rebuilds P,
  re-derives the argmin TIE and finds the clean block on (0,2,4)): CONFIRMED, B/delta = 0.7776403.
  NEW fact: the wave-13 record instance itself carries a clean Gamma-block — the 0.77764 wall
  binds with and without the block. Verdict UNDECIDED; named residual = uniform floor for the
  carrier self-defect D_J/B (the direct-FE conditional theorem); follow-up decider dispatched.
TIER: T0 certificates; T1 identity + conditional theorem; T3 the irrational family-limit law.
-->

# Wave 16 Branch-Restricted B-Lemma Report

Verdict: **UNDECIDED**.

I did not edit tracked repo files and did not run `fr`, `bd`, or mutating `git`.
All artifacts are under `waves-scratch/w16-b-restricted/`.

Rerun commands:

```bash
python3 waves-scratch/w16-b-restricted/w16_identity.py
python3 waves-scratch/w16-b-restricted/w16_b_restricted.py
python3 -m py_compile waves-scratch/w16-b-restricted/w16_identity.py waves-scratch/w16-b-restricted/w16_b_restricted.py
```

## T0 Seed Certificate

The wave-15 seed reconstructs exactly:

```text
delta = 55319/1000000
U = (0,2,4), s = 2, r = 1, clean row j = 1
Phi(U) = (0, 679/24625, 219870541/7880000000)
Psi_j = 1/200 < M = 219870541/7880000000 <= Gamma_j = 7/250
B_{1,2} = 42/985
B/delta = 8400000/10897843
```

The sole B-carrier is row `i=3`:

```text
beta = 7/10, a_s = -12/197, contribution = 42/985
P_33 = 343/500, nu_i = 2666319/50000000
|a_s| m_U = (12/197)(197/200) = 3/50 < 1/2
```

So the seed realizes the warning from wave 13: the B-mass is volume-inadmissible, while the clean Gamma-block row is a different row (`j=1`).

## T1 Direct FE Identity

Let `beta_i=P_{u_r i}`, `x_i=a_s(i)`, `W_i=x_i^-`, and
`J={i: beta_i>0 and x_i<0}`. Row reproduction in the `s` coordinate gives, for every `i in J`,

```text
x_i = sum_k P_ik x_k.
```

Splitting signs and summing against `beta_i` gives the exact identity

```text
sum_{k in J} W_k (beta_k - A_k^J) = S_J,
A_k^J = sum_{i in J} beta_i P_ik^+,
```

where

```text
S_J =
sum_{i in J} beta_i [
  -P_ii^- W_i
  - sum_{k in J, k!=i} P_ik^- W_k
  + sum_{k notin J} (P_ik^+ W_k + P_ik^- x_k^+ - P_ik^+ x_k^+ - P_ik^- W_k)
].
```

On the seed:

```text
J = {3}
A_3^J = 2401/5000
lhs = rhs = 3297/246250
lhs/B = 157/500
lhs/delta = 2637600/10897843
internal positive-transfer excess = 0
```

This is the exact direct version of the G8 FE mechanism. It controls the self-defect-weighted quantity `(157/500)B` on the seed, not raw `B` in general.

## T1 Gamma-Block Anatomy

For the clean row `j=1`, the CI/Gamma import data are

```text
c = a_s(j) = 200/197
d_r = 5/197
d_t = -8/197
I = 21/9850
```

The complete import ledger has a single nonzero term, again on the B-carrier row `3`:

```text
R_3 = 3/985, beta_3^+ R_3 = 21/9850.
```

The reduction bound is

```text
I <= (13/200) B + 0 A = 273/98500.
```

This is diagnostically useful: the Gamma-block sees the carrier. But it is the wrong direction for the desired theorem; it is lower-forcing import, not an upper charge of `B`.

## T1 Conditional Result

The sharp conditional result I can honestly prove from the direct identity is:

If every target instance satisfies

```text
D_J := sum_{k in J} W_k (beta_k - A_k^J) >= lambda B_{r,s}
and D_J <= C delta(P),
```

for universal `lambda>0` and `C<infty`, then

```text
B_{r,s} <= (C/lambda) delta(P).
```

The seed has `lambda=157/500`. The unresolved content is exactly a uniform positive lower bound for this aggregate carrier self-defect, or an independent Gamma-specific replacement for it. The clean-block inequality alone did not supply that reversal.

## T0/T3 Amplification

The amplifier script certified 9 clean Gamma-block instances. Best certified point:

```text
family = variable-insert-shape-boundary
shape-a = 6332623/370881409
delta = 590855669597640985598471/10775740230179796072754000
B = 42/985
B/delta = 90516217933510287011133600/116398566910735274162898787
```

This improves the seed ratio but remains below `1`. Duplicate inserts at `n=7` and `n=9` reproduce the same ratio, so cloning did not amplify. Extra-carrier and rotated-bridge probes lost the clean Gamma branch. In the tested one-parameter boundary family, the active law is

```text
y = 2679363 / (49000(22a+799)),
```

and the row-loss balance is the irrational value

```text
a = -5500573/293216 + sqrt(757785147162145)/1466080,
```

with limiting `B/delta` about `0.777640312383967`. This family-specific law is T3 outside the certified rational points.

## Hard Asserts

The scripts hard-assert: `B_left L = I_3`; `P=L B_left`; `P^2=P`; row sums `1`; seed `delta`; complete theta-half chart enumeration; seed unique argmin; maximal pivot; clean-block inequalities; `B_{1,2}=42/985`; carrier set and carrier inadmissibility; direct FE identity `lhs=rhs`; CI import terms; G12 calibration; wave-15 seed calibration; per-point cross-pivot cancellation `A=B+C-D`; per-point clean Gamma branch; best ratio `<1`; and Python compilation.

## T2 Read And Next Experiment

T2 read: the clean Gamma-block is not empty and it does touch the B-carrier through the import ledger, but the algebra still points the wrong way. The live residual is a uniform carrier self-defect/import-reversal principle, not another emptiness or carrier-negativity charge.

Most informative next experiment: optimize clean-block instances for **small direct-FE floor**

```text
D_J / B_{r,s}
```

while also recording `B/delta`. A certified family with `D_J/B -> 0` would kill the direct-FE proof route; a persistent positive floor would isolate the exact theorem to prove.