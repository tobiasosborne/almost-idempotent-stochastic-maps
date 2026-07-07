# Wave W44 — the (T1) intersection attacked four ways: support localization, geography, conic reduction, the separator obstruction (2026-07-07, session 12)

**Node:** sketch v11 (T1)/(T2), bd `aism-2fi` (P0). **Design (HANDOFF resume item 1,
reconstructed):** four independent fresh-codex provers — AR (T/O geography) ∥ AS
(optimal-face selection) ∥ AT (separator-as-exposer) ∥ AU (rank-3 decider) — + TWO SEPARATE
fresh hostile verifiers: VAR (over AR+AS, shared core) and VAT (over AT), + VAU (independent
exact recomputation of AU's certificates). Prompts + raw answers in the session-12
scratchpad (`W44/`).

## Verdicts (verbatim first lines)

- Worker AR: `PARTIAL (proved: always-tight T/O geography at hidden tops and cheap cluster
  vertices; gap: cluster-uniform top-slab T-to-O hull absorption)`
- Worker AS: `PARTIAL (proved: strict-complementarity support localization and the exact
  conic T/O/Z reduction; gap: tall-cluster sign rebalancing forcing the W43 T/O intersection)`
- Worker AT: `PARTIAL (proved: W43-separator lower-face obstruction; gap: cluster-uniform
  separator-to-ledger absorption)`
- Worker AU: `PARTIAL (proved: exact rank-3 boundary certificates for the T/O intersection,
  including failure outside the tall-heavy hypotheses and success on the banked
  top-preserving/frontier tops; gap: no rank-3 theorem forcing optimal-face T/O interlacing
  from tall heavy near-cluster hypotheses)`
- Verifier VAR: `VALID-WITH-CORRECTIONS (alpha mass 100 is minimum/reduced, not
  unrestricted; AS a_z=0 iff is existential; keep δ>0, W nonempty, t*>0 hypotheses explicit)`
- Verifier VAT: `VALID (tier: independent hostile verifier; LP bookkeeping, strict
  separation, perturbation feasibility, clone/harmonic checks, exact counterexample hunt)`
- Verifier VAU: (in flight at wave-doc time; AU codification deferred until its verdict)

## Results

1. **`lem-always-tight-dual-support` (codified; AR+AS identical core, VAR corrections).**
   Every optimal hiddenness witness is supported on the always-tight T/O/Z sets; T nonempty;
   O nonempty iff t* > 0. The redundant-centered-zero caveat is explicit (reduced witnesses).
2. **`lem-tight-far-geography` (codified; AR, VAR-validated constants).** At hidden tops the
   witness far-mass concentrates in the top slab (1 − (1/2+δ)/c law; T(v) ∩ G_a nonempty for
   H > (a + 1/2 + δ)τ); conditionally (A ≤ A0, 4τ-near a top) the same for cluster vertices
   with K = 1/2 + δ + 4(1 + A0); O-displacements are (1/2+δ)τ-small after t*-scaling.
3. **`lem-optimal-face-conic-reduction` (codified; AS, existential wording).** Optimal
   witnesses = displays sum_T λ_f d_f + sum_Z a_z d_z = t*·sum_O γ_i d_i; an all-a_z = 0
   display exists iff the W43 intersection holds. **The terminal question is now EXACTLY:
   eliminate or uniformly bound the zero-face conic term.**
4. **`lem-separator-zero-face-obstruction` (codified; AT, VAT contract verbatim).** If the
   hulls are disjoint, every strict-separator direction is centered, P-harmonic, positive on
   T, negative on O, and is blocked ONLY by a nonclone zero-face row with negative value —
   the (T2) bridge's missing piece is charging that blocker.
5. **`conj-zero-face-elimination` (registered; the VAR-approved merged terminal statement).**
   THE (T1) final form: under tall/heavy/near-cluster hypotheses the intersection holds
   cluster-uniformly — equivalently the Z-cone term is eliminable or universally bounded.
   The three prover gaps (AR hull absorption / AS sign rebalancing / AT separator absorption)
   are ONE statement, this one.
6. **AU's exact rank-3 boundary (codification pending VAU):** empty intersections REALIZED
   just OUTSIDE the tall-heavy class (W41 HEIGHT+A: H < 4τ, empty width-4 cluster, both near
   hidden rows have empty T/O intersections); every instance INSIDE the class satisfies the
   intersection (TOP-preserving with exact convex certificates; the W29 frontier). The
   hypotheses of (T1) are load-bearing in exactly the expected direction.
7. **LP-only closure is impossible (AS certificate, VAR-recomputed):** the exact 4×4
   (obs-realized-alpha-blowup family, eps = t = 1/100) needs minimum reduced alpha mass 100 —
   outside tall-heavy (H/τ = 1/505). Tallness/heaviness MUST enter any elimination mechanism.

## Banking (orchestrator)

Registry: four lemma shards + one conjecture shard (VAR/VAT as reviewers; AU's observation
deferred to VAU). Honest tiers: reviewed (L5); NOT af-validated, NOT L0. (T1) remains OPEN
in its sharpest form (conj-zero-face-elimination). Sketch v12 carries the redraw.
