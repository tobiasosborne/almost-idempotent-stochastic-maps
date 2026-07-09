<!--
ROLE: W56 wave record — SL1a Tier-2 decomposition, INTERRUPTED mid-run (session 14).
STATUS DISCIPLINE (L0): AUTHOR-CLAIM strategy material only, INCOMPLETE and
  UNVERIFIED (no hostile review ran). Promotes nothing. SL1a remains OPEN.
-->

# Wave W56 — SL1a Tier-2 decomposition (INTERRUPTED; partial artifact preserved)

**Target:** `conj-straddling-web-exclusion` (SL1a), selected as the most open Tier-1
leaf (the unified rigidity core of both W54 branches; l2-attack.md honest assessment:
"where all remaining hardness of (M2) lives on the intersection side").

**Method:** decomposition-first per the standing user directive (objective function of
every Tier-1 attack = decomposition into lower-complexity Tier-2 pieces). ONE codex
architect (gpt-5.6-sol, reasoning effort ultra) in a self-contained workspace (all 140
registry shards + definitions + CONVENTIONS + l2-attack + l6-attack + W55 strategy +
FINDINGS), task spec in `2026-07-09-W56-artifacts/target.md` (hard constraints:
Prop-D walls, W55 dead routes, B6 scale gap, clone-invariance; red tests: Prop-E
counterweight, W55 starvation gadget; per-leaf restatement test).

**Outcome: INTERRUPTED by user stop after ~45 min, mid-§3.** The worker was killed
before writing §3 (leaf statements), §4 (assembly), §5 (coverage), §6 (honest
assessment) and before emitting a VERDICT line. NO hostile verification ran. The
partial artifact is `2026-07-09-W56-artifacts/decomposition-PARTIAL.md`; the full
worker session log (which may contain further leaf reasoning recoverable by a resume
pass) is `2026-07-09-W56-artifacts/architect-session-log.txt.gz`.

## What the partial artifact contains (AUTHOR-CLAIM, unverified)

- **§1** — a proved-input audit: the standing shards the decomposition consumes
  (lem-top-deficit-price, lem-harmonic-affine-bridge, lem-genuine-disintegration with
  its same-carrier vertexization clause, lem-positive-exposedness-margin,
  lem-always-tight-dual-support, lem-optimal-face-conic-reduction,
  lem-separator-zero-face-obstruction, lem-zero-face-capacity-kill), with the Prop-D /
  averaging walls explicitly registered as non-inputs.
- **§2** — the proposed DAG shape: a three-leaf ROUTINE pipeline plus ONE hard
  terminal leaf, at pinned `delta_bar = 2^-16`:
  - **L-S (affine selector):** select f in supp(lambda), still rho-far and co-top,
    with `2*z_f/D + h*(p_f) <= 12*tau/13` (combines the SL1a all-exposer defeat with
    the z/D and h* exposers).
  - **L-V (same-carrier reproduction/disintegration):** row-reproduce at the SELECTED
    web row f (not at v — dodging Prop-D), disintegrate on the same carrier via
    lem-genuine-disintegration: the P_f^+-weighted vertex measure m keeps total mass
    > 3/4 on distinct vertices at depth > H - 4*tau with `integral h* dm <=
    tau*(12/13 + tau)`.
  - **L-P (discard):** discarding h* >= 4*tau mass leaves m-mass > 1/2 at h* < 4*tau;
    split by the literal predicate ||p_u - p_v||_1 >= 4*tau into far horn (>= 1/4,
    owns equality) / near horn (> 1/4).
  - **H-SCCO (same-carrier co-top completion obstruction) [HARD, the single permitted
    hard leaf]:** excludes both horn tableaux in one statement; further decomposition
    was to be supplied in §3 and was NOT written.
- **§2.1** — exhaustiveness/boundary-ownership: pipeline + one owned threshold split;
  clone-invariance convention (fiber-aggregated mass sums); B6 respected (only radial
  rho predicates from v, no pairwise separation assumed).

## Honest gaps (why this is NOT a usable surface yet)

1. §3-§6 missing: no fully-quantified leaf statements, no assembly with constant
   discipline, no red-test outcomes, no restatement-test verdicts, no VERDICT line.
2. NOTHING here is hostile-verified — the W53/W54/W55 discipline requires a fresh
   codex hostile review before any of this is treated as the surface or codified.
3. The L-S selector inequality, the L-V mass/exposer constants, and the L-P thresholds
   are AUTHOR arithmetic mid-draft; they may not survive their own §4.

## Next session (resume order)

1. Resume the architect: fresh codex (gpt-5.6-sol ultra) given the partial artifact +
   the session log to COMPLETE §3-§6 (or re-derive; the DAG shape is cheap to re-check
   against §1's quoted clauses).
2. Fresh hostile codex verification of the completed artifact (verdict-first-line).
3. Only then: codify leaves as registry conjecture shards + the proved reductions, and
   fold into the sketch (v20 delta).
4. The scratch workspace is session-local and NOT preserved beyond these artifacts;
   rebuild it from the repo (the recipe is in target.md's RESOURCES section).
