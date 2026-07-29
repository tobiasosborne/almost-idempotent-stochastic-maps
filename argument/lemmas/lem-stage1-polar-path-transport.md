---
id: lem-stage1-polar-path-transport
kind: lemma
contract: Parameterized polar-path transport: there exist C_path^0, C_pol^0 >= 1 and kappa_pol^0 in (0, 1/2] such that, for every def-stage1-polar-witness-data tuple W with C_path >= C_path^0, C_pol >= C_pol^0, and 0 < kappa_pol <= kappa_pol^0, for every finite-dimensional exact-unit epsilon_r-C*-algebra, every delta > 0 with C_pol*(epsilon_r + delta) <= kappa_pol, every U_0, U_1 in calU, and every q in [0, 1] satisfying ||U_1 - U_0|| <= q, C_path*q <= 1/4, and C_path*(q + epsilon_r*q + q^2) < delta - C_pol*(epsilon_r*delta + delta^2), every L_{Z_t} is invertible and every Z_t = (1-t)*U_0 + t*U_1 lies in calUbar_{C_path*(q + epsilon_r*q + q^2)} for t in [0, 1], and, writing u_delta for the unique first component of the inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the map H(t, U_0, U_1) = u_delta(Z_t) is jointly continuous in (t, U_0, U_1), joins U_0 to U_1, and satisfies H(t, cU_0, cU_1) = c*H(t, U_0, U_1) for every c in U(1).
defs: def-stage1-polar-witness-data; def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-path-admissibility; lem-stage1-polar-retraction-transport
status: proved
af: validated
workspace: proofs/lem-stage1-polar-path-transport
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 13f, landed verbatim (LaTeX flattened to registry ASCII; incl. the v6 finite-dimensional domain restriction, audit-v5 sect-6 option 1); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). TeX 895-912; parameterized path/loss/guard monotonicity; AUDIT-S1-POLAR-v4.md sect-1.6, sect-3.
owner: A
---

**Status.** **RETRACTED from the rigorous record 2026-07-28 (sweep)** — the af validation (then the 106th rigorous result) was found DEFECTIVE by the independent Stage-1 sweep adjudication (`docs/plans/2026-07-28-13E-BINDER-design/SWEEP-ADJUDICATION-STAGE1.md`; second LEARNINGS entry of 2026-07-28; bead `aism-e1qs`): export node 1.3.1: attaches the parent path-admissibility conclusion to the root-bound explicit u_delta by sameness of notation; the parent contract exports only the anaphoric path formula (no h_delta, no displayed Pi_delta, no typed preimage identity). Status mechanically demoted proved->stated, af validated->seeded; workspace and ledger retained as the re-elevation base; repair folded into the W97 explicit-binder campaign (design v3). The CONTRACT is not in dispute, only the proof.

**Superseded status record (pre-retraction).** af-VALIDATED 2026-07-27 (106th rigorous result): first-pass —
root validated, 9/9 nodes, taint clean (tier routine, zero challenges;
the bare-u_delta parent anaphor resolved cleanly against the explicit
polar-retraction import, unlike the paused 13e). Export in the workspace;
oracle `af-lem-stage1-polar-path-transport` + `fr verify` PASS. Landed
VERBATIM from the audited `DESIGN-S1-POLAR-v6.md` §3 row 13f.

**W97 amendment (2026-07-28, deps-only).** Deps widened per the endorsed
rebuild design (`DESIGN-13E-BINDER-v3.md` §1.9; audit chain v3/v3.2, final
VERDICT LAND): `lem-stage1-polar-retraction-transport` (13d) is added as
the typed provider of the receiving tuple's displayed inverse. Contract
and defs BYTE-UNCHANGED (13f remains row-13 clause (A_6) verbatim).
Elevation queue row 7 (target/hard cap 10/14): use the parent
path-admissibility ONLY for its binder-free conclusions (L_{Z_t}
invertibility, near-unitary membership); the typed inverse of the same
displayed Pi_delta comes from 13d; equivariance by one-inverse uniqueness.
The defective 9-node tree is NOT a repair base — cleanly RE-SEED at
elevation (superseding the earlier "re-elevation base" phrasing above).

**Build-granularity discipline (BINDING on the af tree; extends the
user-ratified row-1 discipline of 2026-07-28 — run-1 there ABORTED
[BALLOON] from sub-splitting routine norm estimates).** The target is the
design's 10-node skeleton (hard cap 14). Tree discipline per design v3
sect-1.9: (i) ONE early node fixing the provider witnesses — the parent
path witnesses (A,B,k) from polar-path-admissibility and the sound 13d
witnesses (P,q_pol) from polar-retraction-transport — and setting
C_path^0 = A, C_pol^0 = max{B,P}, kappa_pol^0 = min{k,q_pol}, BEFORE
quantifying over the receiving tuple W (receiving fields transport by
monotonicity); (ii) ONE node for the parent's binder-free conclusions
(L_{Z_t} invertibility + near-unitary membership, enlarged to the
receiving C_path by monotonicity); (iii) ONE node placing Z_t in S_delta
via the strict receiving path guard + the 13d typed inverse of the SAME
displayed Pi_delta; (iv) ONE node each for continuity (13d C^1 inverse +
affine path), endpoints (u_delta(U)=U), and scalar equivariance
(Pi_delta(c*u_delta(Z_t),h_delta(Z_t))=c*Z_t + ordinary uniqueness) — do
NOT sub-split routine estimates; no coherence external. Constants live
in the proof body, never the contract; every smallness inference cites
its guard node explicitly.

**af-RE-VALIDATED 2026-07-29 (W98, elevation queue row 7).** Clean
re-seed on the widened typed spine (13d supplies the displayed inverse;
the parent supplies only binder-free conclusions — the defective
sameness-of-notation attachment is absent by construction). First-pass
run under the binding build-granularity discipline above (tier routine,
fresh codex verifier per node): root validated, 11/11 live nodes (design
target 10; hard cap 14), taint clean, 10 rounds, two in-run challenges
repaired (both strict-vs-non-strict guard transfers at permitted
equality cases; ch-fdf880fb and the root-level sibling, resolved by the
non-strict chains + node 1.10) and re-verified fresh. Export in the
workspace; oracle `af-lem-stage1-polar-path-transport` + `fr verify`
PASS. This status flip is a mechanical reflection of the codex ledger.
