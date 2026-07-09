VERDICT: VALID-WITH-CORRECTIONS — The u := v repair now typechecks modulo the explicit R4 t*(v)=0 audit, but G8 must synchronize c_m, c_r, and theta_0 with the existential leaf constants and must include delta_0(L5).

1. Required correction: G8-v2 still fixes constants not delivered by L2-v2/L6-v2, and it still omits L5's small-delta ceiling.

   Daylight:

   > **L2-v2 (summit-plateau exclusion).** There exist universal c_m in (0,1), delta_0 > 0 such that no exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set, and hidden top vertex v of height H > 16*tau has, simultaneously: t*(v) > 0; the always-tight hulls at v INTERSECT; for every top support functional phi, sum_{j : H - phi(p_j) < tau} max(P_vj, 0) > 1 - c_m; and for every average phi-bar of at most 3 top support functionals, sum_{j : H - phi-bar(p_j) >= tau} max(P_vj, 0) < c_m/4.

   > **L6-v2 (huddle exchange starvation).** There exist universal c_r in (0,1), c_m in (0,1), theta_0 in (0,1), delta_0 > 0 such that no exact signed idempotent P with 0 < delta(P) <= delta_0 and nonempty visible set has a hidden top v with H > 16*tau, heaviness sum_{C(v)} P_vj^+ >= 1 - theta_0 (a = 16), t*(v) > 0, DISJOINT always-tight hulls at v, every always-tight zero-face row z at v keeping sum_{j : h*(p_j) >= kappa} max(P_zj, 0) < c_r, and sum_{j : ||p_j - p_v||_1 >= 4*tau, d_j > H - 8*tau} max(P_vj, 0) < c_m.

   These leaves do not state that their constants are c_m = 1/4, c_r = 1/2, theta_0 = 1/8. The old G8 entries hard-code those values. That is not justified unless the leaves are strengthened to those exact thresholds.

   A second miss is L5. Its statement says:

   > **Statement.** There exist universal c_5 > 0, delta_0 > 0 such that for every exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set, hidden top v with H > 16*tau, and every index set A contained in {j : ||p_j - p_v||_1 >= 4*tau, d_j > H - 8*tau} with sum_{j in A} max(P_vj, 0) >= c_m: some top support functional phi has sum_{j in A} max(P_vj, 0) * (H - phi(p_j)) >= c_5 * tau * c_m.

   But G8-v2 is:

   > **G8 entry 7-v2:** delta_0 := (1/2) * min{ 1/4, (c_m/3)^2, (c_m/12)^2 [Q3-v2 charge], (c_r/4)^2, (c_5*c_m/3)^2, delta_0(L2), delta_0(L3), delta_0(L6), delta_0(L7) }.

   Required correction: choose the split constants after reading the existential leaves. For example, if L2-v2 supplies (m_2, d_2) and L6-v2 supplies (r_6, m_6, th_6, d_6), take

   `c_m = (1/2) * min{1/4, m_2, m_6}`,
   `c_r = (1/2) * min{1/2, r_6}`,
   `theta_0 = (1/2) * min{1/8, th_6, 1/2 - c_m}`.

   Then, after L3/L5/L7 deliver their constants at these choices, set

   `delta_0 = (1/2) * min{1/4, (c_m/3)^2, (c_m/12)^2, (c_r/4)^2, (c_5*c_m/3)^2, d_2, delta_0(L3), delta_0(L5), d_6, delta_0(L7)}`.

   Monotonicity makes the smaller c_m, c_r, theta_0 legal for L2-v2 and L6-v2: their antecedents only get stronger. Without this correction, the assembly does not literally derive the target from the stated leaves.

2. Prior root-object findings 1, 2, 5, and 6 are repaired at the assembly level.

   N0-v2 sets u := v and L2-v2/L6-v2 remove "deepest mass-carrying" from the leaf antecedents. After this substitution, I found no live step that needs positive disintegrated C(v)-mass at u or any deepness beyond d_v = H. The old A0 proximity route is no longer load-bearing.

   Merge note: old V1 prose in B2/C3 still says "deepest mass-carrying" if read without the delta. The delta says those phrases are struck everywhere, so this is not a proof gap, but a merged V2 should delete the stale words.

3. The t*(v)=0 closure is explicitly pending the R4 shard audit, and no later branch silently uses the degenerate case.

   Delta wording correctly says the closure is only contract-level and caveated:

   > CAVEAT (V-ASM AG-1 audit): the localization shard's recorded mechanism degenerates at t* = 0; a shard-proof audit (dispatched as W54-R4) must confirm its contract covers the boundary before this closure is trusted

   After N0-v2, every later use is under t*(v) > 0: S1's K_O(v), the conic reduction in B2, the huddle reduction in C0, separator-zero-face obstruction, and L2-v2/L6-v2. Nothing else depends on t*(v)=0 cases.

4. Step B1-v2 and Q3-v2 now match the registered L1 shard.

   Registered contract:

   > Averaged deficit charge: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), a hidden top vertex v of height H, any c_m > 0, and any phi that is a top support functional at v (affine, phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1) or a finite convex average of top support functionals at v: if sum over {j : H - phi(p_j) >= tau} of max(P_vj, 0) >= c_m then c_m*tau <= delta*(2+4*delta); in particular no such configuration exists for 0 < delta < min(1/4, (c_m/3)^2).

   Q2 applies this with parameter c_m. Q3-v2 applies it with parameter c_m/4. The charge ceilings are therefore (c_m/3)^2 and (c_m/12)^2, exactly as G8-v2 says.

5. Step B2 typechecks at u = v.

   NOT-Q1 gives intersecting always-tight hulls at v, so lem-optimal-face-conic-reduction supplies an alpha-free optimal display because t*(v) > 0. lem-bounded-alpha-forced-far-slab is legal with u = v: v is a geometrically distinct hidden top vertex, ||p_v - p_v||_1 = 0 < 4*tau, and c_w = 6 is bigger than 1/2 + delta_0 + 4 at delta_0 <= 1/4. Its exposed alternative cannot fire because v is hidden. The forced far row is now rho-far from v itself, so the old parenthetical "f_u is rho-far from u, not necessarily from v" should be deleted in a merged V2.

   NOT-Q2 gives the plateau condition in L2-v2 using lem-mass-split: total positive v-row mass is 1 + nu_v >= 1, so high mass < c_m implies low mass > 1 - c_m. NOT-Q3-v2 gives the averaged condition < c_m/4. Thus L2-v2's exact hypothesis list is met, subject to the constant synchronization in Finding 1.

6. Step C0/C3 typecheck with the exposedness LP at the top v.

   Relevant contract:

   > Disjointness huddle reduction: for an exact signed idempotent P with delta(P) > 0 and nonempty visible set, a hidden top vertex v of height H > 8*tau, and a geometrically distinct row vertex u with ||p_u - p_v||_1 < 4*tau and t*(u) > 0: u is hidden with dist_1(p_u, conv{p_w : w in W}) > H - 4*tau, and if conv{p_f - p_u : f in T(u)} and t*(u)*conv{p_i - p_u : i in O(u)} are disjoint (T(u), O(u) the always-tight far/upper families of the exposedness LP at u), then there is a row vertex w with p_w != p_u, ||p_w - p_u||_1 < 4*tau, and dist_1(p_w, conv{p_w' : w' in W}) > H - 8*tau (hence w hidden); contrapositively, if no such pair (u, w) exists then the always-tight hulls at u intersect.

   Instantiating u = v satisfies every input: v is a hidden top, H > 16*tau > 8*tau, 0 < 4*tau, and t*(v) > 0 by N0-v2/R4. Q1 supplies disjointness at v. S4/S5 then read as top-v exposedness data, and C3 feeds L6-v2 exactly: tall, heavy, t*(v) > 0, disjoint hulls at v, NOT-Q4, and NOT-Q5.

7. Step C1 is delivered by the registered L4 shard.

   Registered contract:

   > Zero-face capacity kill: for an exact signed idempotent P with delta(P) > 0, a hidden geometrically distinct row vertex u, an optimal exposer h* at u, a row z with h*(p_z) = 0, and c_r > 0 with sum over {j : h*(p_j) >= kappa} of max(P_zj, 0) >= c_r (kappa = tau/4, tau = sqrt(delta)): c_r*kappa <= nu_z <= delta(P), where nu_z is the row-z negative mass; in particular no such configuration exists for 0 < delta < (c_r/4)^2.

   Q4 gives exactly the high-slab mass hypothesis for a zero-face row at v, so h*(p_z)=0. The contradiction is c_r*tau/4 <= tau^2, hence tau >= c_r/4; G8-v2's half-slack kills the closed delta boundary.

8. Q3-v2 and all threshold boundaries are now exhaustive and clone-invariant.

   Q3-v2 is a mass-sum predicate:

   > **Q3-v2:** "there exist phi_1, ..., phi_k in Phi, k <= 3, whose average phi-bar satisfies sum_{j : H - phi-bar(p_j) >= tau} max(P_vj, 0) >= c_m/4."

   Equality belongs to Q3-v2. Its complement is the strict < c_m/4 condition consumed by L2-v2. Since this is a sum over row indices weighted by P_vj^+, cloning only splits summands and does not change the predicate. The prior raw-index a_f^+ problem is repaired.

9. Prior findings 1-11 status.

   1 repaired by N0-v2 plus L2-v2/L6-v2 removing mass-carrying; 2 repaired because A0 is no longer used; 3 repaired by Q3-v2 and the c_m/4 charge; 4 repaired by G8-v2 half-slack, subject to Finding 1's missing delta_0(L5) and constant synchronization; 5 repaired by L6-v2; 6 repaired by L2-v2 at v; 7 remains sound, u = v is legal in the huddle chain; 8 remains sound, bounded-alpha typechecks at u = v and the exposed alternative is blocked by hiddenness; 9 remains sound and is now registered as lem-zero-face-capacity-kill; 10 repaired by Q3-v2's mass-sum form; 11 remains sound, with no new dimension dependence found.

10. Bottom line.

   I found no new crack caused by re-rooting at the top v. The repaired branches derive the target from L1, L2-v2, L3, L4, L5, L6-v2, and L7 modulo the explicitly pending R4 audit, after the G8 correction in Finding 1 is applied. Without that correction, the document is not literally valid because the selected numerical constants and the L5 delta ceiling are not justified by the stated leaves.
