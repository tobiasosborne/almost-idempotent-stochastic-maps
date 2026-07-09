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
