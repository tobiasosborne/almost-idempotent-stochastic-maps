---
id: lem-maincb-stage2-extcb-datum
kind: lemma
contract: There are universal C_s2 >= 1 and e_s2 > 0, with the e_ca threshold and universal C_ca coefficient of lem-compcb-corner-algebra absorbed into e_s2 and C_s2, such that, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state comes from a non-unital extended t-inclusion w:C^m->A with one-dimensional images P_j, has nonempty U, j notin U, dim S^A_{P_k,P_j} = 1 for every k in U, and R = U union {j}, and a supplied current reset state v_U:M_{|U|}->A_U is an extended isomorphism satisfying epsilon_U, d_U <= t <= e_s2 and d_U <= c_0^cb*epsilon_U, then lem-compcb-corner-algebra makes A_R an extended epsilon_{A_R}-C*-algebra, lem-maincb-nested-corner-comparison makes P_U^R, P_j^R quantitative projections in A_R, and together with the lem-maincb-outer-compression-transfer outer-compressed isomorphism they satisfy every def-extcb-datum clause - approximate complementarity to I_{A_R}, one-dimensional S_{P_j^R}, nonzero S_{P_U^R,P_j^R}, and total error e = delta + epsilon_{A_R} - with e <= C_s2*t, forming the explicit Stage-2 raw-call closed EXT-CB datum in A_R.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call; def-extcb-datum; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-delta-projection; def-one-dimensional-delta-projection; def-compressed-corner
deps: lem-maincb-error-improvement; lem-maincb-nested-corner-comparison; lem-maincb-nested-corner-dimension-transport; lem-maincb-outer-compression-transfer; lem-maincb-corner-equivalence; lem-compcb-corner-algebra; lem-extcb-corner-dimension-additivity
status: proved
af: validated
workspace: proofs/lem-maincb-stage2-extcb-datum
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.3 row M13 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1363-1412,1430-1441
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30) — **WARNING: VACUOUS
TRUTH.** 23-node tree, root `validated`, taint clean 23/23
(`proofs/lem-maincb-stage2-extcb-datum/export.md`; oracle pass; run 3
clean re-seed). The root was closed BY CONTRADICTION OF THE
HYPOTHESES: under the locked def-maincb-partition-state field 'one
current union U of classes', the hypotheses (U a union of classes;
dim S^A_{P_k,P_j}=1 for every k in U; j notin U) are UNSATISFIABLE
(corner-equivalence forces j into U's class, hence into U), so the
contract holds vacuously. The fresh verifier confirmed the
contradiction argument sound. THIS RESULT AS LANDED IS NOT A WORKING
STAGE-2 DATUM PRODUCER: the design's Stage-2 induction (M25 proof
plan, partial-class U_r) requires a partition state whose current U
may be a PARTIAL class — a semantics the locked definition excludes.
Definition clarification ESCALATED (P0 user-decision bead); on
ratification M13 is to be re-elevated non-vacuously. Do NOT consume
this lemma downstream before that re-elevation (M19-S2/M25 would
inherit the same vacuity wall).

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
10 / 3 / 14. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.3 row M13. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1363-1412,1430-1441; definitions/def-extcb-datum.md:13-17
