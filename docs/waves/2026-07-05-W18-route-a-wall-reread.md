<!--
WAVE: W18 (Route-A wall re-read against the CONSTANT cap sigma_g <= 1/2; sketch-v2 node "ROUTE A
  to <2>4" + unscoped-surface item "Route A's wall record has not been re-read against the new
  import toolkit") — 2026-07-05, session 9, bd aism-0uf.
WORKERS: two fresh codex exec, prompts in the session scratchpad
  (PROMPT-w18-r1-d1-rederivation.md, PROMPT-w18-r2-wall-reread.md). R1 ran under an independence
  discipline: full derivation written BEFORE opening W17 (self-reported at ANSWER-R1 Phase 3).
  Both answers VERBATIM below. Workers ran no fr/bd/git and edited no tracked file.
ORCHESTRATOR: mechanical bank only — the orchestrator did NOT verify any mathematics (L5).
  LOUD CORRECTION of the orchestrator's own wave-brief hypothesis: the prompts floated
  "CAP-1/2 might be EQUIVALENT to the height bound H <= 29*tau/8 through the validated
  collapse". BOTH workers independently REFUTED the equivalence: the collapse gives
  cap => height bound and (H > 29*tau/8 => every hidden top has sigma_g > 1/2), but NOT the
  converse; CAP-1/2 is strictly stronger (it also excludes the low-height/high-sigma_g region),
  so the W17b census slack is MORE informative than "no tall instance found", not less.
HEADLINE: (R1) W17's D1 CONFIRMED twice-independently with exact constants 29/16 and 29/8, and
  STRENGTHENED — under the cap ALL rows land within 29*tau/8 of conv W (the Kernel raw
  antecedent sigma~_v > tau is unused; no raw-to-halo bridge needed); residuals = W-nonemptiness
  (genuine), delta=0 endpoint (short), the cap itself. (R2) The recorded walls do NOT bind
  CAP-1/2 as stated: B3's one-sided ledger TRANSFERRED (not dodged for free — the residual is a
  CONSTANT-MASS shallow-genuine exclusion: positive mass on rows with dist_1(.,C_W) > tau/4 AND
  canonical-separator depth < tau/4 must be <= 1/2 - 4*tau*(2+4*delta)); the class-count dead
  route BINDS-ONLY-O(1) (a delta-dependent count C/tau or C/delta would suffice and is NOT
  excluded by any recorded family — no recorded construction pushes total sigma_g toward 1/2);
  per-class "hostable mass" is NOT a proved lemma (two undisambiguated scale readings, O(tau)
  poke vs O(delta) row-negativity). VERDICT: Route A = WALL-NARROWED (was: wall-blocked).
CAVEAT (honesty): R2's Q1 depth-ledger computations consume obs-deep-leakage's harmonic
  inequality, whose shard status is HEURISTIC — the "deep slice is paid" step is itself not yet
  rigorous. Nothing in this wave is rigorous; no registry status was changed by it.
TIER: worker-tagged throughout (T0 loci; T1 short proofs, unreviewed worker arguments; T2 gaps).
-->

# W18 — Route-A wall re-read (CAP-1/2) + independent D1 re-derivation

Target statement (CAP-1/2): universal `delta_0 > 0` such that every exact signed idempotent `P`
with `0 < delta(P) <= delta_0` and nonempty `W(P)` has `sigma_g(v) <= 1/2` for every hidden top
vertex `v`.

---

## Worker R1 — independent re-derivation of D1 (verbatim ANSWER-R1.md)

[T1] VERDICT: D1 CONFIRMED. The inherited chain of inequalities is valid with exact constants, provided the symbols are read as in `argument/lemmas/conj-halo-collapse.md:4`: `sigma` is the raw invisible positive mass of the hidden top vertex, `sigma_g` is the halo-robust positive mass on rows at `ell_1` distance `> tau/4` from `conv W`, and `nu_v` is that row's negative mass.

[T1] VERDICT: D1* CONFIRMED IN ITS STATED RANGE, with the stronger clean statement: for `0 < delta(P) <= 1/4`, nonempty `W(P)`, and `sigma_g(v) <= 1/2` for every hidden top vertex `v`, one gets `H(P) <= (29/8) tau`; hence every row, and in particular every hidden row vertex with raw `sigma~_v > tau`, has distance at most `(29/8) tau` from `conv{p_w : w in W}`. The raw antecedent is unused.

### Phase 2 Source Ledger

[T0] Conventions used: signed idempotents have `P1=1`, `P^2=P`, row sums `1`, `delta = max_i sum_j max(-P_ij,0)`, `tau = sqrt(delta)`, and `delta <= 1/4` is the range of interest; see `CONVENTIONS.md:35-59`.

[T0] Exact signed idempotent input: each row has total mass `1`, and pairwise row `ell_1` distances are at most `2+4 delta`; see `definitions/def-signed-idempotent.md:13-23`.

[T0] Negative mass input: `delta(P) = max_i sum_j max{-P_ij,0}`; see `definitions/def-negative-mass.md:13-19`.

[T0] Visible set and scales: `tau = sqrt(delta)`, `rho = 4 tau`, `kappa = tau/4`, and `W(P)` is the set of `(rho,kappa)`-exposed row vertices; see `definitions/def-visible-set.md:13-20`.

[T0] Exposed/hidden input: row vertices are defined geometrically, and hidden means not `(rho,kappa)`-exposed; see `definitions/def-exposed.md:13-27`.

[T0] Height input: if `W` is nonempty, row height is `dist_1(p_i,C_W)`, `H(P)` is the maximum over all rows, and if `H>0` any maximizing vertex is hidden and is called a hidden top vertex; see `definitions/def-height.md:13-20`.

[T0] Raw invisible mass input: `sigma~_v = sum_{j: dist_1(p_j,C_W)>0} max{P_vj,0}`, over row indices `j`; see `definitions/def-invisible-mass.md:13-22`.

[T0] Validated collapse input used as a black box: for a hidden top vertex `v` of height `H`, with raw invisible mass `sigma`, halo-robust invisible mass `sigma_g`, and row negative mass `nu_v`, one has
`H * (1 - sigma_g) <= (sigma - sigma_g) * tau/4 + nu_v * (2 + 4*delta)`;
see `argument/lemmas/conj-halo-collapse.md:1-10`.

[T0] Kernel target input: the conjecture asks for nonempty `W(P)` and, for every hidden row vertex with raw invisible mass `sigma~_v > tau`, the distance bound `dist_1(p_v,conv W) <= B tau`; see `argument/lemmas/conj-kernel.md:1-5`.

[T0] Raw/halo warning input: raw `sigma` can exceed `1` while halo-restricted mass is `0`, so a finisher must be halo-robust; this is recorded as numerical, not rigorous, in `argument/lemmas/obs-sigma-halo-nonrobust.md:1-19`.

### Phase 2 Derivation

[T1] Fix an exact signed idempotent `P` with `0 < delta <= 1/4`, nonempty `W`, and a hidden top vertex `v`. This is exactly the hypothesis range of `argument/lemmas/conj-halo-collapse.md:4`, together with the scales in `definitions/def-visible-set.md:13-15`.

[T1] Write `a_j = P_vj`, `a_j^+ = max(a_j,0)`, `a_j^- = max(-a_j,0)`, and `nu_v = sum_j a_j^-`. Since the row sum is `sum_j a_j = 1` by `definitions/def-signed-idempotent.md:13-18`, exact arithmetic gives
`sum_j a_j^+ - sum_j a_j^- = 1`, hence
`sum_j a_j^+ = 1 + nu_v`.

[T1] Let `S_0 = {j : dist_1(p_j,C_W) > 0}` and `S_g = {j : dist_1(p_j,C_W) > tau/4}`. Because `tau > 0`, `S_g subset S_0`. By `definitions/def-invisible-mass.md:13-17` and `argument/lemmas/conj-halo-collapse.md:4`,
`sigma = sum_{j in S_0} a_j^+` and `sigma_g = sum_{j in S_g} a_j^+`, so
`0 <= sigma - sigma_g = sum_{j in S_0 \ S_g} a_j^+ <= sum_j a_j^+ = 1 + nu_v`.
Thus the inherited inequality `sigma - sigma_g <= 1 + nu_v` is valid.

[T1] Since `delta(P)` is the maximum row negative mass by `definitions/def-negative-mass.md:13-16`, the row negative mass of row `v` satisfies `nu_v <= delta`. Therefore
`1 + nu_v <= 1 + delta <= 1 + 1/4 = 5/4`.

[T1] Apply the validated collapse bound from `argument/lemmas/conj-halo-collapse.md:4`:
`H(1-sigma_g) <= (sigma-sigma_g) tau/4 + nu_v(2+4 delta)`.
Using the previous two bounds,
`(sigma-sigma_g) tau/4 <= (5/4) tau/4 = 5 tau/16`.

[T1] Also `nu_v(2+4 delta) <= delta(2+4 delta)`. Since `delta <= 1/4`, `2+4 delta <= 3`. Since `tau = sqrt(delta)` and `0 < delta <= 1/4`, one has `0 < tau <= 1/2`, hence `delta = tau^2 <= tau/2`. Therefore
`delta(2+4 delta) <= 3 delta <= 3 tau/2 = 24 tau/16`.

[T1] Adding the exact rational bounds gives
`H(1-sigma_g) <= 5 tau/16 + 24 tau/16 = 29 tau/16`.
This confirms the inherited `29/16` constant.

[T1] If in addition `sigma_g <= 1/2`, then `1-sigma_g >= 1/2`, so
`H/2 <= H(1-sigma_g) <= 29 tau/16`, hence
`H <= 29 tau/8`.
This confirms the inherited `29/8` height constant.

[T1] A slightly sharper delta-dependent version falls out before taking the worst case:
`H(1-sigma_g) <= ((1+delta) tau)/4 + delta(2+4 delta)`.
Under `sigma_g <= 1/2`, this gives
`H <= ((1+delta) tau)/2 + 2 delta(2+4 delta)`.
The uniform constant over `0 < delta <= 1/4` is still exactly `29/8`, attained by this coarse expression at `delta = 1/4`.

### Hypothesis Alignment

[T1] The collapse contract is for a hidden top vertex `v` "of height H"; see `argument/lemmas/conj-halo-collapse.md:4`. The definition of height says `H(P)` is the maximum of `dist_1(p_i,C_W)` over all rows, and a maximizing hidden vertex is a hidden top vertex; see `definitions/def-height.md:13-20`. Thus the `H` in the collapse contract is the global maximum height, not merely a private height attached to `v`.

[T1] The sentence "non-top hidden vertices are bounded by the top height" is a definitional consequence once `W` is nonempty: for every row `u`, `dist_1(p_u,C_W) <= H(P)` by the maximum definition in `definitions/def-height.md:13-17`. If `H=0`, this is immediate. If `H>0`, a hidden top vertex exists by `definitions/def-height.md:18-20`, and the preceding D1 argument bounds that common maximum `H`.

[T1] Therefore D1* does not need an extra selection argument of the form "for every hidden vertex `u` find a hidden top vertex above it"; the global maximum already dominates every row height.

### Raw Versus Halo-Robust Sigma

[T1] D1* never uses a comparison between raw `sigma~_v` and halo-robust `sigma_g(v)`. The D1 bound controls the global height `H` from the cap on hidden top vertices alone, and then the definition of `H` bounds every row.

[T1] Consequently the clean statement is stronger than the Kernel branch: under the hidden-top halo cap, every row satisfies `dist_1(p_i,C_W) <= (29/8) tau`, not only hidden row vertices with raw `sigma~_v > tau`.

[T0] The raw/halo mismatch is real as a warning: `argument/lemmas/obs-sigma-halo-nonrobust.md:4-19` records an exact numerical certificate where raw `sigma` is `5343/5000 > 1` while halo-restricted mass is `0`. Since that shard has status `numerical` at `argument/lemmas/obs-sigma-halo-nonrobust.md:7`, I use it only as a warning against raw caps, not as a rigorous proof input.

### Equivalence Check

[T1] Let `C = 29/16` and `B = 29/8 = 2C`. D1 proves, for each hidden top vertex `v`, the coarse inequality
`H(1-sigma_g(v)) <= C tau`.

[T1] One direction is exact: if `sigma_g(v) <= 1/2`, then `1-sigma_g(v) >= 1/2`, and therefore `H <= 2C tau = B tau`.

[T1] The tall-obstruction contrapositive is also exact: if `H > B tau`, then
`1-sigma_g(v) <= C tau/H < C tau/(B tau) = C/B = 1/2`,
so `sigma_g(v) > 1/2`.

[T1] LOUD CONCLUSION: the validated collapse plus the coarse `29/16` assembly proves that any vertex witnessing a height violation beyond `(29/8) tau` must violate the `1/2` halo cap, but it does NOT prove that the halo cap is equivalent to the height bound.

[T1] Quantifier placement matters. If hidden top vertices exist and `H > B tau`, then every hidden top vertex has `sigma_g(v) > 1/2`, because every hidden top vertex has the same global height `H`. Conversely, `H <= B tau` does not imply `sigma_g(v) <= 1/2` for any or all hidden top vertices from these inputs.

[T1] Formal arithmetic countermodel to the reverse implication from the inequality alone: take any `tau > 0`, set `H = C tau`, and set `sigma_g = 3/4`. Then `H(1-sigma_g) = C tau/4 <= C tau` and `H <= B tau`, but `sigma_g > 1/2`. This is not claimed to be realized by an idempotent; it shows the reverse implication is not a logical consequence of the validated inequality.

[T1] The exact slack statement is: with
`R_v = (sigma-sigma_g) tau/4 + nu_v(2+4 delta)`,
the validated inequality gives `H(1-sigma_g) <= R_v`. If `H > B tau`, then
`sigma_g > 1 - R_v/(B tau)`. Since the coarse proof gives `R_v <= C tau`, this threshold is at least `1/2`; if `R_v < C tau`, the required cap violation is strictly stronger than `sigma_g > 1/2`.

### Residual Ledger

[T2] Residual: nonempty `W(P)` in the Kernel range. D1 assumes nonempty `W`; `conj-kernel` requires existence of some universal `delta_0 > 0` for which `W(P)` is nonempty; see `argument/lemmas/conj-kernel.md:3-5`. The D1 arithmetic works up to `delta_0 <= 1/4`, but it does not prove nonemptiness for any positive `delta_0`. Price: genuine gap relative to the full Kernel contract.

[T1] Residual: non-top hidden vertices. Price: trivial once `W` is nonempty and `H` is bounded, by `definitions/def-height.md:13-20`.

[T1] Residual: raw-vs-halo bridge. Price: none for D1*. No inequality relating raw `sigma~` to `sigma_g` is needed, because the cap gives a global height bound.

[T2] Residual: the hidden-top halo cap itself. D1* assumes `sigma_g(v) <= 1/2` for every hidden top vertex. Proving such a cap, or even the weaker sufficient condition that at least one hidden top vertex has `sigma_g <= 1/2` when `H>0`, is not supplied by the Phase 1 sources. Price: genuine gap if the goal is to prove the Kernel Conjecture rather than prove the conditional D1* implication.

[T2] Residual: the zero-defect endpoint. The validated collapse hypotheses require `0 < delta(P) <= 1/4`; see `argument/lemmas/conj-halo-collapse.md:4`. The Kernel contract is stated with `delta(P) <= delta_0`; see `argument/lemmas/conj-kernel.md:3-5`. A full Kernel proof needs a separate `delta=0` branch or a convention excluding it from the conditional reduction. Price: short if an existing stochastic-idempotent anchor may be cited, but not discharged from the Phase 1 sources alone.

### Phase 3 Comparison With W17's D1

[T0] I opened `docs/waves/2026-07-05-W17-ex-kernel-dictionary.md` only after the Phase 2 derivation above was written to this file. W17 states D1 at `docs/waves/2026-07-05-W17-ex-kernel-dictionary.md:31-32` and summarizes it in the table at `docs/waves/2026-07-05-W17-ex-kernel-dictionary.md:42-46`.

[T1] Agreement: W17 uses the same validated halo-collapse inequality, the same estimates `sigma-sigma_g <= 1+nu_v <= 1+delta <= 5/4`, `nu_v <= delta`, `delta <= 1/4`, and `delta=tau^2 <= tau/2`, and the same exact constants `29/16` and `29/8`; compare `docs/waves/2026-07-05-W17-ex-kernel-dictionary.md:31-32` with the Phase 2 derivation above.

[T1] Agreement: W17's sentence "Non-top hidden vertices are bounded by the top height" at `docs/waves/2026-07-05-W17-ex-kernel-dictionary.md:32` matches the definition-level maximum argument from `definitions/def-height.md:13-20`.

[T1] Agreement: W17's "only sigma_g > 1/2 hidden top vertices matter" phrasing at `docs/waves/2026-07-05-W17-ex-kernel-dictionary.md:7-9` and `docs/waves/2026-07-05-W17-ex-kernel-dictionary.md:45` is the tall-obstruction contrapositive: if `H > (29/8) tau`, then every hidden top vertex has `sigma_g > 1/2`.

[T1] Discrepancy or added correction: W17 does not spell out the non-equivalence. The D1 inequality proves `sigma_g <= 1/2 => H <= (29/8) tau` and its contrapositive `H > (29/8) tau => sigma_g > 1/2`, but it does not prove `H <= (29/8) tau => sigma_g <= 1/2`. Thus the constant cap is a sufficient input, not an equivalent reformulation of the height bound.

[T1] Discrepancy or added correction: W17's D1 is phrased as a branch reduction for HLC. For the Kernel branch, the independent derivation makes explicit that the raw antecedent `sigma~_v > tau` is unused: the low-halo cap bounds all row heights, so no raw-to-halo comparison is needed.

[T2] Non-D1 note: the adjacent W17 "door statement" at `docs/waves/2026-07-05-W17-ex-kernel-dictionary.md:34-38` uses a different later threshold shape involving `sigma_g(v)>tau`. I did not analyze that door statement here; it is outside the requested D1 constant-cap reduction.

---

## Worker R2 — adversarial wall re-read (verbatim ANSWER-R2.md)

Q1 VERDICT: TRANSFERRED. The one-sided ledger does not directly bind halo-robust `sigma_g <= 1/2`, but it leaves the constant-mass residual "genuine-outside and separator-shallow" uncontrolled. [T1; loci: docs/waves/2026-07-02-B3-sigma-cap.md:31-39, docs/waves/2026-07-02-B4-walls-check.md:53-73]
Q2 VERDICT: BINDS-ONLY-O(1). The recorded class-count wall kills the old `O(1)` quotient-class composition, not a delta-dependent `C/tau` or `C/delta` total-mass route; no recorded construction drives total `sigma_g` toward `1/2`. [T1/T2; loci: docs/waves/2026-07-02-B4-walls-check.md:101-124, argument/lemmas/obs-fwr-gap.md:18-24, docs/waves/2026-07-05-W17b-door-ratio-census.md:31-66]
Q4(b) VERDICT: HIGH-HEIGHT CONTRAPOSITIVE TRUE, EQUIVALENCE REFUTED. `sigma_g <= 1/2` implies `H <= 29*tau/8`, hence `H > 29*tau/8` implies `sigma_g > 1/2`; the converse is not supplied by the collapse inequality. [T1; loci: argument/lemmas/conj-halo-collapse.md:4, docs/waves/2026-07-05-W17-ex-kernel-dictionary.md:31-33]

Tier convention used below: [T0] exact repo locus or exact arithmetic read from the repo; [T1] short proof given here from cited inputs; [T2] named gap or priced obligation; [T3] speculation. I did not run `fr`, `bd`, or mutating `git`; I wrote only this scratch file. [T0]

### Q1 -- one-sided ledger (B3) vs CAP-1/2

**VERDICT: TRANSFERRED to the shallow-genuine residual.** [T1]

- [T0] B3's pot ledger writes `a_j=P_vj`, `sum_j a_j^+=1+nu_v`, pot 1 `pi_v` as `C_W`-mass, pot 2 as deep-but-outside, pot 3 as shallow-outside, with raw `sigma = pot2 + pot3` and `1-sigma = pi_v - nu_v`. Locus: docs/waves/2026-07-02-B3-sigma-cap.md:31-33; mass-split is now af-validated at argument/lemmas/lem-mass-split.md:1-17.
- [T0] `sigma_g` is the halo-robust positive coefficient mass on rows at `ell_1` distance `> tau/4` from `conv W`; the raw invisible mass includes all positive mass outside `C_W`, including self-mass, and the halo caveat is recorded in the definition. Loci: argument/lemmas/conj-halo-collapse.md:4, definitions/def-invisible-mass.md:13-22.
- [T1] Therefore `sigma_g` intersects pot 2 and only the genuinely far part of pot 3: it excludes pot 1 and excludes the `tau/4`-halo slice of pot 3. This is exactly B4's dodge: the target is an upper bound on genuine-outside mass, not a lower bound on `pi_v`. Locus for the dodge: docs/waves/2026-07-02-B4-walls-check.md:53-62.
- [T0] The deep-leakage shard records the harmonic inequality `sum (P_vj)^+ g_j <= (2+4*delta)*delta`, and states that visible/deep positive mass is upper-bounded by `O(delta)/H`; its status is `heuristic`, not proved. Loci: argument/lemmas/obs-deep-leakage.md:4,14-23.
- [T1] From that recorded harmonic inequality, for any separator-depth threshold `s>0`, the mass on rows with separator-depth at least `s` is at most `delta*(2+4*delta)/s`: if each such row has `g_j >= s`, then `s*mass <= sum (P_vj)^+ g_j <= delta*(2+4*delta)`. [T1 from argument/lemmas/obs-deep-leakage.md:14-17]
- [T1] At `s=tau/4`, the controlled genuine mass is at most `4*tau*(2+4*delta)`. If `delta <= 1/4`, this is at most `12*tau`. [T1]
- [T1] At `s=H`, the controlled mass is at most `delta*(2+4*delta)/H`; on the high-height branch `H>29*tau/8` this is less than `8*tau*(2+4*delta)/29`, hence at most `24*tau/29` when `delta<=1/4`. [T1]
- [T1] Thus a CAP-1/2 counterexample must place more than `1/2 - 4*tau*(2+4*delta)` positive mass in rows satisfying both `dist_1(p_j,C_W)>tau/4` and separator-depth `< tau/4`. On the high-height sub-branch, replacing the coarse `tau/4` ledger by the `H` ledger only controls the deeper slice; the same separator-shallow genuine class remains. [T1]
- [T2] The named uncontrolled mass class is: shallow-side rows, outside the `tau/4` halo of `C_W`, whose canonical-separator depth is below `tau/4`; equivalently "genuine-outside but separator-shallow" recipients. This is B4's caveat that the harmonic identity still cannot bound shallow genuine pot 3. Locus: docs/waves/2026-07-02-B4-walls-check.md:68-73.
- [T1] The old lower-bound obstruction is not a literal death certificate for CAP-1/2: CAP-1/2 asks for an upper bound on `sigma_g`, while B3's raw cap asked for a lower bound on `pi_v`. [T1; loci: docs/waves/2026-07-02-B3-sigma-cap.md:37-39, docs/waves/2026-07-02-B4-walls-check.md:64-66]
- [T2] The obligation is still structurally the old anti-splitting obligation, but weakened from excluding "pot 3 approximately all mass" to excluding "more than one half of the mass in separator-shallow genuine-outside rows, up to the `O(tau)` deep slice." Loci: docs/waves/2026-07-02-B3-sigma-cap.md:39, docs/ingest/report/kernel-conjecture.tex:318-322.

### Q2 -- anti-splitting / quotient-packing class count vs CAP-1/2

**VERDICT: BINDS-ONLY-O(1), with an opening at `C/tau` or `C/delta` depending on the per-class scale.** [T1/T2]

#### Q2(a) -- per-class hostable mass

- [T0] The recorded per-class claim is not a proved lemma: `conj-no-free-frontier` is a conjecture, and its body says mutually-shielding near-coincident twins persist hidden with "hostable mass bounded by the poke depth proportional to `nu = O(tau)`" and `t*=nu/(1+nu)<kappa`. Loci: argument/lemmas/conj-no-free-frontier.md:7,14-19.
- [T0] B4 repeats the same per-cluster shape and then multiplies it by the number of surviving genuine-outside quotient classes: `sigma_g <= (#classes) * O(tau)`. Locus: docs/waves/2026-07-02-B4-walls-check.md:101-124.
- [T1] If this `nu` is the row negative mass `nu_i` or `nu_v`, then `nu <= delta = tau^2` by definition of `delta` as the maximum row negative mass. Locus: definitions/def-negative-mass.md:52-55.
- [T1] If this `nu` is instead the exposedness/poke parameter in `t*=nu/(1+nu)<kappa=tau/4`, then `nu < tau/(4-tau)`. Under `delta<=1/4`, `tau<=1/2`, hence `nu < 2*tau/7`. [T1; loci for `kappa=tau/4`: definitions/def-visible-set.md:41-47; for the `t*` claim: argument/lemmas/conj-no-free-frontier.md:18-19]
- [T2] The record does not disambiguate these two readings in a proved statement. The conservative price is: per-class mass is only a heuristic obligation, with possible scale `O(tau)` from the poke parameter and a stronger `O(delta)` only if it can be tied to actual row negative mass. [T2]

#### Q2(b) -- what class count CAP-1/2 needs

- [T1] If each surviving class hosts at most `A*tau` positive mass, CAP-1/2 would follow from `#classes <= 1/(2*A*tau)`. If each hosts at most `A*delta`, it would follow from `#classes <= 1/(2*A*delta)`. [T1]
- [T0] B4's recorded FAIL-2 says the old composition needed a dimension-free class count because it tried to total `(#classes)*O(tau)` into a bound away from `1`; the text explicitly says the per-cluster claim totals only if the class count is `O(1)`. Locus: docs/waves/2026-07-02-B4-walls-check.md:101-124.
- [T0] The `obs-fwr-gap` obstruction says F-WR cannot merge simplex-corner clusters, gives no dimension-free cap on their number, and pushes the class-count question to quotient packing / signed quantitative Baake-Sumner. Locus: argument/lemmas/obs-fwr-gap.md:18-24.
- [T0] The cloning obstruction kills raw-index floors and forces clone-invariant quotient quantities, but it does not itself assign large positive `P_v^+` mass to many genuine-outside quotient classes. Loci: FINDINGS.md:34-39, docs/ingest/report/kernel-conjecture.tex:270-306.
- [T2] I found no recorded construction in the mandatory wall record that pushes total halo-robust `sigma_g` toward `1/2`. The exact F2 examples have `sigma_g=0` for the raw self-mass witness, `sigma_g=5991/80000` for instance A, and `sigma_g=229/3200` for instance B. Loci: docs/waves/2026-07-02-F2-sigma-cap-refuter.md:36-40.
- [T0] The W17b census measured `138` hidden top vertices in `514` rank-3 exact instances and found `0` with `sigma_g>1/2`; the best recorded `sigma_g` there is `1/25`. Loci: docs/waves/2026-07-05-W17b-door-ratio-census.md:31-66; runs/2026-07-05-door-ratio-census/data/full-report.md:25-69.
- [T1] Therefore the recorded killer families bind the `O(1)` class-count route but do not bind a delta-dependent class-count route unless one also records a family with enough hosted mass per class to make total `sigma_g>1/2`. [T1/T2]

#### Q2(c) -- cheap direct total-mass argument?

- [T1] `lem-mass-split` gives only `sum_j P_vj^+ = 1+nu_v`, so the trivial bound is `sigma_g <= 1+delta`, not `1/2`. Locus: argument/lemmas/lem-mass-split.md:1-17.
- [T1] The halo-collapse proof already packages row reproduction, mass split, the halo exemption, and residual-distance estimates into `H*(1-sigma_g) <= (sigma-sigma_g)*tau/4 + nu_v*(2+4*delta)`. Locus: argument/lemmas/conj-halo-collapse.md:4,14-30.
- [T1] This inequality bounds height from above when `1-sigma_g` is bounded below; it does not bound `sigma_g` from above. When `sigma_g` increases, the coefficient `1-sigma_g` decreases, and for `sigma_g>=1` the left side is nonpositive. [T1]
- [T2] The sharp obstruction to a cheap total-mass proof is the same as Q1: distance-to-`C_W` is not additive across different outside directions, and the harmonic/deep ledger controls separator-depth, not the total mass of separator-shallow rows at `ell_1` distance `>tau/4` from `C_W`. Loci: docs/waves/2026-07-02-B4-walls-check.md:68-73, docs/ingest/report/kernel-conjecture.tex:318-322.
- [T2] I do not see a T1-grade direct proof of CAP-1/2 from current mass-split plus residual lemmas. The missing lemma is a constant-mass shallow-genuine exclusion, not another row-sum identity. [T2]

### Q3 -- wall applicability audit table

| Wall / certificate | Target it was built against | Mechanism killed | CAP-1/2 applicability | One-line why |
|---|---|---|---|---|
| [T0] B3 Step B, one-sided ledger. docs/waves/2026-07-02-B3-sigma-cap.md:31-38 | [T0] Raw `epsilon=0` cap `1-sigma >= c*tau`, equivalently `pi_v >= nu_v+c*tau`. | [T0] Trying to get a lower bound on pot 1 from the harmonic/deep ledger. | [T1] BINDS-PARTIALLY / TRANSFERRED. | [T1] CAP-1/2 is an upper bound on `sigma_g`, so the sign wall is dodged, but the ledger still leaves shallow genuine pot 3 uncontrolled. |
| [T0] B3 Step C, shallow-web exclusion. docs/waves/2026-07-02-B3-sigma-cap.md:39 | [T0] Lower-bound route for raw sigma cap; exclude self-sustaining shallow web with pot 3 near full mass. | [T2] Anti-splitting / signed quantitative Baake-Sumner gap. | [T2] BINDS-PARTIALLY. | [T2] CAP-1/2 needs only exclude more than half of shallow-genuine mass, not pot 3 near `1`; same residual, weaker constant. |
| [T0] B3 Step D, low-height raw cap false risk. docs/waves/2026-07-02-B3-sigma-cap.md:41 | [T0] Height-free raw cap. | [T0/T2] Low-height `sigma -> 1` or `sigma>1` via thin halo/self mass. | [T0] SILENT for halo CAP; BINDS raw only. | [T0] F2 later realized the raw self/halo loophole exactly, with `sigma=5343/5000` and `sigma_g=0`. |
| [T0] B4 wall (a), one-sided ledger dodge. docs/waves/2026-07-02-B4-walls-check.md:36-73 | [T0] `conj-no-free-frontier => sigma_g <= 1-c`. | [T1] It kills the claim that the one-sided ledger still blocks the halo-robust framing directly. | [T1] DODGED but TRANSFERRED. | [T1] The target is an upper bound on genuine-outside mass; the remaining burden is shallow genuine mass. |
| [T0] B4 FAIL-1, uniform `kappa=tau/4` pointwise margin. docs/waves/2026-07-02-B4-walls-check.md:81-97 | [T0] Literal `conj-no-free-frontier` exposedness-production statement. | [T2] Side rows at near-equal extremity can destroy a pointwise uniform margin. | [T2] BINDS any no-free-frontier proof of CAP. | [T2] CAP-1/2 via exposedness absorption still needs a sound production rule; this failure is independent of the cap constant. |
| [T0] B4 FAIL-2, quotient class count. docs/waves/2026-07-02-B4-walls-check.md:99-126 | [T0] Totaling a per-cluster `O(tau)` mass bound into `sigma_g <= 1-c` or `O(tau)`. | [T1/T2] Need for an `O(1)` number of surviving genuine-outside quotient classes. | [T1] BINDS-ONLY-O(1). | [T1] CAP-1/2 permits `C/tau` or `C/delta` classes if per-class mass is `O(tau)` or `O(delta)`. |
| [T0] FINDINGS raw-index cloning obstruction. FINDINGS.md:34-39; docs/ingest/report/kernel-conjecture.tex:270-306 | [T0] Raw-index path-product floor. | [T0/T1] Cloning preserves geometry and `delta` but destroys raw index products. | [T1] BINDS raw-index methods; otherwise SILENT. | [T1] CAP-1/2 is already quotient/geometric in `sigma_g`, so only non-clone-invariant proof attempts are killed. |
| [T0] FINDINGS sigma-cap refuter sweep. FINDINGS.md:109-122 | [T0] Raw sigma cap and halo-robust cap stress test. | [T0] Raw cap at `epsilon=0` is false; halo cap survives tested families. | [T0/T2] RAW BINDS; HALO SILENT as proof. | [T0] Exact raw witness has `sigma>1` but `sigma_g=0`; tested halo data are L3 evidence only. |
| [T0] FINDINGS walls-check. FINDINGS.md:124-140 | [T0] `conj-no-free-frontier` as cap mechanism. | [T1/T2] One-sided ledger dodged; anti-splitting/quotient-packing hit. | [T1] BINDS-ONLY-O(1). | [T1] The finding explicitly prices the total cap through an `O(1)` class count; it does not price the constant-half target separately. |
| [T0] `obs-fwr-gap`. argument/lemmas/obs-fwr-gap.md:1-24 | [T0] F-WR/web-rigidity route to shallow class count. | [T0/T2] F-WR cannot merge simplex-corner clusters; no dimension-free cap on number. | [T2] BINDS-PARTIALLY. | [T2] It kills this proof family, but records no total `sigma_g -> 1/2` construction. |
| [T0] Ingest anti-splitting residual. docs/ingest/report/kernel-conjecture.tex:318-322 | [T0] Pin aggregate shallow carrier mass into one quotient component. | [T2] Missing dimension-free bound on geometrically distinct shallow classes hit by `P_v^+`. | [T2] BINDS-PARTIALLY. | [T2] CAP-1/2 can tolerate many more classes; the residual becomes a total-mass cap, not single-component pinning. |
| [T0] "Exclude pot 3 approximately 1" lower-side route. docs/waves/2026-07-02-B3-sigma-cap.md:37-39, docs/waves/2026-07-02-B3-sigma-cap.md:45-47 | [T0] Raw `1-sigma >= c*tau` cap; B3 R2 asks for `sigma^sh <= 1-c*tau`. | [T2] Proving mass is not almost entirely in shallow outside pot 3. | [T2] BINDS-PARTIALLY, not a statement-level death. | [T2] The killed item is a proof route/lower-side ledger need at near-full shallow mass; CAP-1/2 only needs rule out more than half of the halo-robust shallow genuine slice. |
| [T0] F2 exact raw halo witness. docs/waves/2026-07-02-F2-sigma-cap-refuter.md:34-49; argument/lemmas/obs-sigma-halo-nonrobust.md:1-19 | [T0] Literal `epsilon=0` sigma cap. | [T0] Self-mass in the `tau/4` halo makes raw `sigma>1`. | [T0] SILENT for CAP-1/2. | [T0] The same exact witness has halo-restricted mass `0`. |
| [T0] F2 genuine-recipient sweep. docs/waves/2026-07-02-F2-sigma-cap-refuter.md:21-32,36-42 | [T0] Search for halo-robust cap refuter. | [T2] No tested family entered high genuine mass; exposedness absorption was proposed as heuristic. | [T2] SILENT as theorem; evidence against cheap refuters. | [T2] It is family-limited numerical evidence, and B4 says it is structurally blind to high-dimensional class amplification. |
| [T0] W17b door-ratio census. docs/waves/2026-07-05-W17b-door-ratio-census.md:31-76 | [T0] Constant door `sigma_g>1/2` in rank-3 exact instances. | [T0/T2] No rank-3 measured hidden top entered the door; not an emptiness claim. | [T2] SILENT as theorem; useful decider evidence. | [T2] Exact rank-3 census found max `sigma_g=1/25`, but Kernel is rank-free. |

### Q4 -- new toolkit and contrapositive check

#### Q4(a) -- transfer audit

- [T0] `lem-mass-split` is general for any exact signed idempotent and any row index, so it transfers directly to a hidden top vertex in any rank. Locus: argument/lemmas/lem-mass-split.md:1-17.
- [T0] `lem-residual-lower` and `lem-residual-upper` are frame-free `ell_1` convex-geometry lemmas and are already deps of `conj-halo-collapse`; they transfer to general rank through the collapse proof. Loci: argument/lemmas/lem-residual-lower.md:1-31, argument/lemmas/lem-residual-upper.md:1-34, argument/lemmas/conj-halo-collapse.md:5-6.
- [T0] `lem-zerosum-triangle` and `lem-weighted-min` are general elementary inequalities, not rank-3-specific, but their current registry role is payment/fan machinery; they do not by themselves connect row-`v` invisible mass to hidden-vertex geometry. Loci: argument/lemmas/lem-zerosum-triangle.md:1-19, argument/lemmas/lem-weighted-min.md:1-17.
- [T0] `lem-pivot-removing-move`, `lem-collateral-import`, `lem-cross-pivot-cancellation`, and `lem-import-reduction` are explicitly rank-3 actual-row-chart / theta-half / pivot statements. Loci: argument/lemmas/lem-pivot-removing-move.md:1-44, argument/lemmas/lem-collateral-import.md:1-40, argument/lemmas/lem-cross-pivot-cancellation.md:1-34, argument/lemmas/lem-import-reduction.md:1-30.
- [T0] `lem-negative-pivot-import` is also rank-3 actual-row-chart machinery, covers the `c<0` companion, and is `proved-mod-audit` / `af: seeded`, not af-validated. Locus: argument/lemmas/lem-negative-pivot-import.md:1-54.
- [T2] The structural blocker for importing the rank-3 pivot toolkit into Route A is the DC4 mismatch: Kernel uses row-`v` weights `P_vj`, while chart quantities use pivot weights `P_{u_s j}`, and no transport lemma exists. Locus: docs/waves/2026-07-05-DC4-equiv-assembly-audit.md:44-53; docs/waves/2026-07-05-W17-ex-kernel-dictionary.md:42-52,72-78.

#### Q4(b) -- contrapositive and equivalence audit

- [T0] The validated halo-collapse inequality is `H*(1-sigma_g) <= (sigma-sigma_g)*tau/4 + nu_v*(2+4*delta)`. Locus: argument/lemmas/conj-halo-collapse.md:4,14-30.
- [T1] Since `sigma-sigma_g <= sum_j P_vj^+ = 1+nu_v`, `nu_v<=delta`, `delta<=1/4`, and `tau=sqrt(delta)`, we have `sigma-sigma_g <= 1+delta <= 5/4`, `2+4*delta <= 3`, and `delta=tau^2 <= tau/2`. Loci: argument/lemmas/lem-mass-split.md:1-17, definitions/def-negative-mass.md:52-55, definitions/def-visible-set.md:41-47.
- [T1] Therefore the right side is at most `(5/4)*(tau/4)+3*delta <= 5*tau/16 + 3*tau/2 = 29*tau/16`. [T1]
- [T1] If `sigma_g<=1/2`, then `1-sigma_g>=1/2`, so `H/2 <= H*(1-sigma_g) <= 29*tau/16`, hence `H <= 29*tau/8`. [T1]
- [T1] Contrapositively, if `H>29*tau/8`, then `sigma_g>1/2`. This matches W17's D1 reduction. Locus: docs/waves/2026-07-05-W17-ex-kernel-dictionary.md:31-33.
- [T1] The equivalence claim is false: the proof gives `sigma_g<=1/2 => H<=29*tau/8`, not `H<=29*tau/8 => sigma_g<=1/2`. [T1]
- [T1] The genuine slack region is `sigma_g>1/2` together with `H<=29*tau/8`; the collapse inequality permits this region because it is one-sided and gives no lower bound on `H` from large `sigma_g`. [T1]
- [T2] Thus "twelvefold census slack on `sigma_g`" is not logically the same empirical fact as "no high-height instance found"; it is stronger evidence because it also searches the low-height, high-`sigma_g` region. W17b found no `sigma_g>1/2` and max `sigma_g=1/25`, but this is rank-3 numerical evidence, not rank-free proof. Loci: docs/waves/2026-07-05-W17b-door-ratio-census.md:31-66; runs/2026-07-05-door-ratio-census/data/full-report.md:25-69.

#### Q4(c) -- surviving mechanism candidates

- [T2] Candidate (i), delta-dependent class count: prove a bound of the form `# genuine separator-shallow quotient classes hit by P_v^+ <= C/tau` if per-class mass is `O(tau)`, or `<= C/delta` if per-class mass is `O(delta)`, together with a per-class hostable-mass lemma. [T2]
- [T2] Kill criterion for (i): an exact high-rank family with `sigma_g>1/2` made from more than `C/tau` or `C/delta` shallow genuine classes carrying the claimed per-class scale. Cheapest decider: parametric exact feasibility/optimization over quotient shallow-web types, not another rank-3 census. [T2; loci for current census limits: docs/waves/2026-07-02-B4-walls-check.md:158-164, docs/waves/2026-07-05-W17b-door-ratio-census.md:74-76]
- [T2] Candidate (ii), mass dichotomy: prove that high positive mass on a row genuinely outside `C_W` either makes that row visible or leaves it within the `tau/4` halo; a constant-mass version would directly target CAP-1/2. [T2]
- [T2] What kills (ii) today is B4 FAIL-1: pointwise extremality in one separating direction does not control far side rows at near-equal extremity, and dense-polygon-style side rows threaten the uniform `kappa=tau/4` margin. Loci: definitions/def-exposed.md:20-39, docs/waves/2026-07-02-B4-walls-check.md:81-97.
- [T2] Cheapest decider for (ii): exact search for a hidden top with a high-mass genuine recipient that is not visible because side rows destroy the exposedness margin; this is exactly the B4 §6 FAIL-1 decider, but retargeted to total `sigma_g>1/2`. Locus: docs/waves/2026-07-02-B4-walls-check.md:217-225.
- [T2] Candidate (iii), `c<0` import / cross-pivot ledger in the vertex frame: no current transfer. The tools are rank-3 chart statements and the known mismatch is row-`v` weights versus pivot weights. Loci: argument/lemmas/lem-negative-pivot-import.md:46-54, docs/waves/2026-07-05-DC4-equiv-assembly-audit.md:44-53.
- [T2] Kill criterion for (iii): either prove a transport lemma from `P_vj^+` genuine mass to pivot-row `P_{u_sj}^+` chart mass, or exhibit a hidden top whose row-`v` genuine mass is invisible to all relevant pivot weights. Cheapest decider: continue the W17b door-ratio / zero-pivot-visibility search, but lift beyond rank 3 before treating it as Route A evidence. Loci: docs/waves/2026-07-05-W17-ex-kernel-dictionary.md:72-81, runs/2026-07-05-door-ratio-census/data/full-report.md:25-69.

### Q5 -- retarget

#### Q5(i) -- sharpest honest open statement

- [T2] The cleanest Route-A statement remains CAP-1/2 itself: there are universal `delta_0>0` such that, for `0<delta(P)<=delta_0`, `W(P)` nonempty, and hidden top vertex `v`, `sigma_g(v)<=1/2`. [T2]
- [T2] The mechanism-shaped minimal residual is more precise: for the canonical top separator at `v`, the positive mass on rows with `dist_1(p_j,C_W)>tau/4` and separator-depth `<tau/4` is at most `1/2 - 4*tau*(2+4*delta)` for sufficiently small `delta`; the deep slice is then paid by the leakage ledger. [T2; loci: argument/lemmas/obs-deep-leakage.md:14-23, docs/waves/2026-07-02-B4-walls-check.md:68-73]
- [T2] A softer symbolic version is enough for small `delta`: prove a constant `c_0>0` shallow-genuine exclusion `mass(shallow genuine) <= 1/2-c_0`, then choose `delta_0` so that `4*tau*(2+4*delta) <= c_0`. [T2]

#### Q5(ii) -- surviving candidates, ranked

1. [T2] **Delta-dependent quotient packing plus per-class hostable mass.** Candidate: per-class mass `<=A*tau` or `<=A*delta`, and class count `<=1/(2*A*tau)` or `<=1/(2*A*delta)` for classes actually hit by `P_v^+`. Kill criterion: exact high-rank shallow-web family with total `sigma_g>1/2`. Cheapest decider: exact quotient-type optimization.
2. [T2] **Mass dichotomy / visibility-or-halo.** Candidate: a row receiving large `P_v^+` mass outside `C_W` is either visible or within the halo, so constant total genuine mass cannot hide. Kill criterion: exact side-row / near-equal-extremity counterexample to uniform exposedness with high hosted mass. Cheapest decider: B4 FAIL-1 search with a `sigma_g>1/2` objective.
3. [T2] **Chart toolkit transport.** Candidate: rank-3 pivot import/cancellation can be used only after a row-to-pivot weight bridge. Kill criterion: zero-pivot-visibility high-`sigma_g` example or proof that none exists. Cheapest decider: extend W17b's door-ratio census to families designed for high `sigma_g`, then seek a rank-free formulation if no refuter appears.

#### Q5(iii) -- overall verdict

- [T2] Route A after re-read = WALL-NARROWED. The old walls do not bind CAP-1/2 as stated; they narrow it to a constant-mass shallow-genuine exclusion / delta-dependent quotient-packing problem. [T2]

#### Q5(iv) -- what the constant-cap framing buys

- [T1] CAP-1/2 buys a short, af-backed finisher to `H<=29*tau/8` by the calculation in Q4(b). [T1]
- [T2] CAP-1/2 also buys a clean refuter/search surface: find any exact hidden top with `sigma_g>1/2`, independently of chart choices and `(EX)` machinery. W17b used exactly this surface and found none in its rank-3 corpus, with max `sigma_g=1/25`, but this is not a proof. Loci: docs/waves/2026-07-05-W17b-door-ratio-census.md:31-76.
- [T1] CAP-1/2 is stronger than the paired height bound, not equivalent to it: it rules out the low-height high-`sigma_g` region as well as the high-height region. [T1]
