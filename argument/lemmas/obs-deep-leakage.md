---
id: obs-deep-leakage
kind: obstruction
contract: For a hidden top vertex v of height H with canonical separator phi and deep side D = {j : phi(p_j) <= 0} (contains W): H * sum_{j in D} (P_vj)^+ <= (2+4*delta)*delta; in particular the positive coefficient mass v places on the visible hull is <= (2+4*delta)*delta/H, so exactness pushes v's positive mass into the shallow near-top band and no argument local to v's row identity can lower-bound the deep-side mass.
defs: def-signed-idempotent; def-height; def-visible-set; def-negative-mass
deps: lem-canonical-separator
status: heuristic
af: none
provenance: docs/waves/2026-07-02-B1-dual-localization.md (arm B wave 1, opus worker; steps S1-S4; loci spot-checked against docs/ingest/report/kernel-conjecture.tex:225-232)
owner: A
workspace: proofs/obs-deep-leakage
---

**Arm B wave-1 harvest (2026-07-02), status HEURISTIC** — a 4-step derivation (S1–S4 in the wave
artifact) from row-exactness `p_v = sum_j P_vj p_j` + the harmonic deficit of
[[lem-canonical-separator]]: `0 = g_v = sum_j P_vj g_j` splits into
`sum (P_vj)^+ g_j = sum (P_vj)^- g_j <= Omega*nu_v <= (2+4delta)*delta`, and `g_j >= H` on `D`.
All quantities clone-invariant.

**Role (obstruction):** the bound runs the WRONG way for the linear law — it caps deep-side/visible
positive mass by `O(delta)/H`, so the frame-free height control cannot be closed locally at `v`; the
sole remaining residual is the global shallow-web exclusion / anti-splitting question
(`kernel-conjecture.tex:316-322`). Reported by the wave as consolidating five recorded dead routes
(unlocalized dual descent, quasi-stationary potentials, maximality-without-localization, rank
induction, convex shadow composition) — that consolidation claim is the wave's analysis, NOT yet
independently reviewed.

**Elevation candidate:** small self-contained tree (4 steps + 1 mod-audit input) — a natural next
`af` target on arm R after its input [[lem-canonical-separator]] is either af-validated or byte-pinned.
