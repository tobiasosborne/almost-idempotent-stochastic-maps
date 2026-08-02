---
id: lem-maincb-stage3-call-envelope
kind: lemma
contract: After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding L^0,e_env^0 witnesses of lem-maincb-direct-corner-envelope, and fixing the C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum, there is a universal K_3^0 >= 1 with every Stage-3 prerequisite absorbed such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0, W.L >= L^0, W.K3 >= max{K_3^0,1,W.L,W.c0_cb*W.L}, and W.e_cross <= e_cross^0, if A is a finite-dimensional extended epsilon-C*-algebra, w:C^m->A is an extended W.c0_cb*epsilon-inclusion satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images, a supplied MAIN partition state for A,w has disjoint nonempty unions U,V sharing no class and R=U union V, 0 <= epsilon <= W.e_cross/W.K3, and supplied current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V have recorded ambient fields epsilon_U,epsilon_V <= W.L*epsilon and satisfy d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= W.c0_cb*epsilon_U, and ||v_V(I_{B_V})-u_{A_V}|| <= W.c0_cb*epsilon_V, then lem-maincb-direct-corner-envelope certifies A_R with the Stage-3 raw-call target ambient record epsilon_R := W.L*epsilon, and t_3=W.K3*epsilon dominates epsilon_U,epsilon_V,d_U,d_V,epsilon_R, both displayed unit norms, and every other datum error, so lem-maincb-cross-class-merging-datum furnishes the explicit Stage-3 four-corner raw-call datum with rho <= C_cross^0*t_3.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call; def-maincb-witness-ledger; def-four-corner-merging-datum; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-error-improvement; lem-maincb-direct-corner-envelope; lem-maincb-cross-class-merging-datum; lem-maincb-extended-inclusion-monotone
status: stated
af: seeded
workspace: proofs/lem-maincb-stage3-call-envelope
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M19-S3 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1325-1359,1428,1443; recorded-field ENV repair per DESIGN-RECFIELD-REPAIR.md sect-3 (hostile-audited AUDIT-RECFIELD-REPAIR.md DESIGN-CONFIRMED zero corrections; user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, second ratification)); DEMOTED 2026-08-01 (latent unregistered-premise gap, AUDIT-CONSUMER-REPAIR.md F5 (node 1.3.3: unimported monotonicity); docs/LEARNINGS.md 2026-08-01; re-validation pending) per DESIGN-CONSUMER-REPAIR.md + AUDIT-CONSUMER-REPAIR.md (F-corrections applied verbatim); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, fifth ratification)
owner: A
---
**Status.** `stated` — DEMOTED 2026-08-01 (the banked certificate's node 1.3.3
used an unregistered monotonicity inference, AUDIT-CONSUMER-REPAIR.md F5;
docs/LEARNINGS.md 2026-08-01; the CONTRACT was never refuted). The 2026-08-01
re-validation run churned (~15-19/24 across rounds; parked tree preserved at
commit 60098719) and is superseded by the fresh 2026-08-02 re-seed below.
Re-seed run 1 (2026-08-02) ABORTED [BALLOON] at 27 live vs cap 24: the
prover assumed c0>=1 and let leaves cite pending siblings (evidence synced;
fr W113 harvest). Superseded by the v2 re-seed below.
Contract per the audited `DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M19-S3
(hostile-audit chain AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified
2026-08-01 in-session). MAIN campaign row M19-S3. NOT proved in-repo; af
re-validation pending. Its re-bank mechanically re-flips the suspended
M18/M20 (certificates intact).

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
8 / 3 / 12; scoped cap amendment 12->24 exercised transparently in the
2026-08-01 run (all growth challenge-resolving, flagged in fr log W112) and
CARRIED into the 2026-08-02 re-seed; repo ceiling 26. Per-row skeleton and
audit delta: DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance
where applicable). A hard-cap hit is a factoring stop, not a rounds bump.
Constants live in the proof body, never the contract.

**Re-seed architecture v2 (BINDING on the fresh tree, 2026-08-02; from the
parked run's factor recommendation + the run-1 balloon classification,
mirroring the VALIDATED lem-maincb-stage2-call-envelope export pattern).**
(0) FIRST child = one constant-choice node fixing ALL universal constants,
exactly as in the validated S2 export: choose a finite NONNEGATIVE
universal c0 for which lem-maincb-error-improvement remains valid (an
original finite error coefficient may be enlarged to a nonnegative one,
with lem-maincb-extended-inclusion-monotone preserving the resulting
inclusion conclusion); fix the witnesses L^0 >= 1 and e_env^0 > 0 of
lem-maincb-direct-corner-envelope and C_cross^0, e_cross^0 of
lem-maincb-cross-class-merging-datum; then CHOOSE K_3^0 explicitly to
absorb EVERY Stage-3 scalar prerequisite (the contract's 'every Stage-3
prerequisite absorbed' clause licenses this). NEVER assume c0 >= 1 —
every scalar chain must use only c0 >= 0, W.L >= L^0 >= 1,
W.K3 >= max{K_3^0,1,W.L,W.c0_cb*W.L}, and epsilon >= 0.
(0') NO node may cite a PENDING SIBLING: shared scalar facts (0 <= delta
for monotonicity; epsilon <= e_env^0; c0*epsilon <= t_3) live in the
constant-choice node or its own children and are cited from there.
(a) lem-maincb-direct-corner-envelope exports projections at `c0*epsilon`
scale and subordination/complementarity at `L^0*epsilon` scale — keep the
two scales SEPARATED from the start; never cite one export at the other's
scale. (b) lem-maincb-extended-inclusion-monotone is typed `v:B->A` with
`B` a plain finite-dimensional C*-algebra — apply it ONLY to such maps, or
derive corner-level monotonicity directly from def-extended-delta-inclusion.
(c) A def-maincb-raw-call record stores the DERIVED output map and its
scale, never the datum itself. Verify the exact two-line inequality
forwarding both unit errors to lem-maincb-cross-class-merging-datum
(design sect-11 risk row).

**Provenance loci.** approximate_algebras.tex:1325-1359,1428,1443
