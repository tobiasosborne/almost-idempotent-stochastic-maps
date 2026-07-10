# W62 L3 decider — I-horn refuter batch (exact arithmetic)

You are a fresh, independent worker. Your workspace is this directory (registry
snapshot + `context/`). Everything you produce stays inside it. This is an L3
(constructive/numerical evidence) job: **nothing you produce is a proof**, and your
report must say so.

## Target

`context/DECOMPOSITION-W62-L5.md` node **I** (`conj-w62-isotropic-cotop-web-exclusion`,
§1) — the isolated isotropic dual-simplex horn of the L5 minimax — plus, as
by-catch, the shared summit-axis threat to all three horns. Read the artifact's §1
shared notation block (it defines every object: L5 datum, G_v, Sh_v, E_c,
K_v^loc, omega, r_omega, the scalar width Omega, q_A, Y_v, Z_v) and node I's
(a)-(e) IN FULL. Note the four routine nodes R0-R3 are now PROVED (L5) as registry
shards `lem-l5-*` — consult them; your candidates must beat R3's for-all-centers
floor, which is a THEOREM now.

## Your job: hunt exact refuters, three shapes

Every genuine candidate family MUST satisfy, in exact rational arithmetic:
P_k^2 = P_k, all row sums 1, delta_k = delta(P_k) -> 0, nonempty visible set
W(P_k), a hidden top vertex v with H_k > 16*tau_k (tau = sqrt(delta)). (This
tallness clause is where BOTH W61 refuter families died — see
`context/2026-07-10-W61-deciders-and-elevation.md` and the two seed certificate
JSONs. A short local gadget without tallness is evidence only.)

1. **Heavy summit-axis spike:** one far-deep fiber Q (||p_Q - p_v||_1 >= 4*tau,
   dist_1(p_Q, C_W) > H - 8*tau) carrying P_v^+ mass >= c_m (use c_m = 1/4 as the
   working threshold) with normalized dual value Z_v(p_Q)/tau -> 0. Kills the
   whole S/C/I output interface if realized.
2. **Growing low-width dual-simplex fan:** m = 3, 4, 8, ... far-deep fibers of
   P_v^+ mass ~ c_m/m each, with (i) the TRUE normalized LP value
   Z_v(q_A)/tau -> 0 (compute Z_v exactly via the PROVED ray formula
   `lem-l5-top-face-ray-formula` — minimize over Lambda >= 0, c in C_W), (ii) the
   for-all-local-centers co-top floor of node I's hypothesis, (iii) BOTH
   ||r_omega - p_v||_1 < 1/8 AND Omega(omega) < 1/16. This is the direct exact
   realization of the low-width dual-simplex threat.
3. **Tall completions of the known seeds:** take the W61 thin transient graft and
   dyadic leak-financer (exact matrices in context JSONs) and the W55
   A0 = 5, g = 5*tau starvation plateau shape, and try to COMPLETE each to
   tallness H > 16*tau while preserving all-row negativity <= tau^2 and
   exactness. Any systematic obstruction you hit, name it precisely (which
   identity/inequality blocks, with the exact margin).

## Deliverables (all inside this directory)

1. `search.py` — self-contained exact-rational (fractions.Fraction) construction +
   verification; every check an exact assertion (P^2 = P entrywise; delta; W and
   hiddenness certificates; H with primal+dual certificates; the fiber quotient;
   Z_v via the ray formula with an exact minimizing pair exhibited; r_omega,
   Omega(omega); the local-center floor). "Runs without errors" is not a pass.
2. `certificates.json` — exact rational matrices + all quantities for any hit or
   best near-miss per shape.
3. `REPORT.md` — verdict per shape: REALIZED (kills/restates I — show the
   certificate) / BLOCKED (name the exact binding inequality per attempted
   family, with margins) / PARTIAL. State explicitly this is L3 evidence, never
   proof. Record shapes tried, parameter ranges, dead ends, and WHERE tallness
   binds if it does.

## Discipline

- `context/FINDINGS.md` dead routes are absolute; all quantities clone-invariant
  (full fibers, row points, l1); signed picture; no probabilistic readings.
- Timebox: prefer three honest BLOCKED-with-named-margins verdicts over one
  half-verified REALIZED. Final answer: three verdict lines + one sentence.
