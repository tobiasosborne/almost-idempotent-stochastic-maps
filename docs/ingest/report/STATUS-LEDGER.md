# Status Ledger

This is the single source of truth for writer agents. If a section wants to state a named result, copy the status from this ledger. If a source note sounds stronger than this ledger, the ledger wins.

Status tags:

- `PROVED`: prose proof/audit exists in the source notes.
- `PROVED-mod-audit`: proof is present but must carry the stated caveat, correction, or banking condition.
- `NUMERICAL`: verified computation only; not a theorem.
- `CONJECTURAL`: plausible or proposed, not proved.
- `OPEN`: current unsolved statement.
- `REFUTED`: source includes counterexample/contradiction.
- `RETRACTED/DOWNGRADED`: earlier stronger reading withdrawn or narrowed.
- `AMBIGUOUS`: source conflict not resolved enough for theorem use.

## A. Main Chain and Terminal Residual

| id/name | What writers may state | Status | Audit / gate | Source pointer |
|---|---|---|---|---|
| `op-classical` | Dimension-free stability of almost-idempotent row-stochastic matrices is the outer target. | OPEN | Target, not closed by campaign | `HANDOFF.md:25-41`; `ORCHESTRATION.md:9` |
| `lem-classical-equiv` | Signed-idempotent and stochastic-idempotent formulations are equivalent. | PROVED | Main repo af-validated | `../../../argument/INDEX.md` row `lem-classical-equiv` |
| `thm-cluster` | Classical target follows from clustering plus exposed-hull route. | PROVED | Main repo result imported by sidequest | `HANDOFF.md:34` |
| `op-exposed-hull` | Global exposed-hull problem remains open. | OPEN | Outer reduction target | `HANDOFF.md:34-36`; `../../../argument/INDEX.md` row `op-exposed-hull` |
| `op-exposed-hull <= HLC` | If HLC holds with `delta >= aH^2`, then exposed-hull stability follows with `C'=max(4A,1/sqrt(a))`. | PROVED-mod-audit | 2-family verified assembly; conditional on HLC | `HANDOFF.md:35-37`; `ORCHESTRATION.md:148-149`; `../../../docs/worklog.md:454-456` |
| `HLC` | Hidden localization claim `delta >= aH^2` remains unproved. | OPEN | Numerically supported; terminal theorem not proved | `notes/endgame-sigma-wall-residual.md:1-24`; `notes/wave8-fable-closer.md:554-567` |
| `HLC <= historical sigma_v-wall` | If old Branch A/B sigma-wall statements are added, HLC follows with `a=min(4/B_A^2,1/B_B^2)`. | PROVED-mod-audit | Conditional glue only | `HANDOFF.md:37-42`; `notes/endgame-sigma-wall-residual.md:13-24` |
| historical Branch A | Hidden vertex with small external mass satisfies `H <= B_A sigma tau`. | OPEN / NUMERICAL | Measured law; not proved | `HANDOFF.md:39-41`; `notes/endgame-sigma-wall-residual.md:4-8` |
| historical Branch B | Large external mass and `H>B_B tau` force exposedness. | OPEN / NUMERICAL | Measured `B_B approx 0.536`; not proved | `HANDOFF.md:39-41`; `notes/endgame-sigma-wall-residual.md:9-10` |
| `sigma_v` branch variable | Older notes overloaded `sigma_v`; final report must use `sigma_v^{off}` vs `widetilde sigma_v`. | RETRACTED/DOWNGRADED | Wave-8/9 sigma catch | `notes/wave8-fable-closer.md:353-360`; `notes/wave5-sigma-wall-parallel.md:538-557` |
| existential DMF implies HLC | One optimal witness with deep mass gives `H <= tau(2+4delta)/(4m*)+E(delta)` and the corrected `a` formula. | PROVED-mod-audit | Codex w9 logic check; conditional on DMF | `notes/wave5-sigma-wall-parallel.md:510-518`; `notes/wave8-fable-closer.md:554-567` |
| `DMF` | Deep-witness mass forcing: optimal witness mass at deficit near `H`. | OPEN | Supported numerically in probed corner/budget families; web case open | `notes/wave8-fable-closer.md:471-473`; `notes/wave8-fable-closer.md:508-552`; `notes/wave5-sigma-wall-parallel.md:538-557` |
| quantitative Baake-Sumner web stability | Exclude self-sustaining shallow hidden top-band webs. | OPEN | Identified as last structural input | `notes/wave8-fable-closer.md:530-545`; `notes/wave5-sigma-wall-parallel.md:445-461` |

## B. Day-1 Audited Belt

| id/name | What writers may state | Status | Audit / gate | Source pointer |
|---|---|---|---|---|
| L1 lone-far-row | A row at `rho` distance from the hull of the other rows is exposed with margin `rho/(2+4delta)`. | PROVED | Audited belt | `HANDOFF.md:59`; `notes/fable-hlc-attack.md:20` |
| L2 far/high row to vertex | A height/farness witness may be taken at a row vertex. | PROVED | Audited belt | `HANDOFF.md:60`; `notes/fable-hlc-attack.md:22` |
| L2' rho-shadow | Hidden vertex has a `rho`-shadow in the hull of other rows. | PROVED-mod-audit | Recursion part is gapped/vacuous at scale | `HANDOFF.md:60-61`; `notes/fable-hlc-attack.md:23` |
| C10 failed-exposedness dual | Failed exposedness has an LP dual witness; alpha mass is uncontrolled. | PROVED | Identity proved; control remains open | `HANDOFF.md:62`; `notes/fable-hlc-attack.md:219-233` |
| L4 frame-clipping | Signed coefficient frame gives height/negative-mass clipping. | PROVED | Audited belt | `HANDOFF.md:63`; `notes/wave8-fable-closer.md:370` |
| L5' leakage at global maximizer | Leakage bound holds only at a global height maximizer. | PROVED-mod-audit | General-row version false | `HANDOFF.md:63`; `notes/fable-hlc-attack.md:105-108` |
| L6 identity-frame linear bound | `delta >= H/2` in the identity frame `Rframe=[I|0]`. | PROVED-mod-audit | Metric transfer open | `HANDOFF.md:64` |
| N1 nilpotent-chain off-chain forcing | Nilpotent-chain route forces off-chain mass. | PROVED | Audited belt | `HANDOFF.md:65` |
| F1 skinny near-coincidence | Mutual-shadow/skinny configurations nearly coincide under hypotheses. | PROVED | Audited belt | `HANDOFF.md:65`; `notes/fable-hlc-attack.md:28` |
| X1 one-mode wall | Exact one-mode shell forces the wall; staircase dies by exactness. | PROVED | Audited; later subsumed by F-WR in common-pattern case | `HANDOFF.md:65-66`; `notes/fable-hlc-attack.md:30`; `notes/fable-hlc-attack.md:440-441` |
| X2 stochastic-complement rank preservation | Rank is preserved under the stochastic-complement reduction used in wave 3. | PROVED | Audited belt | `HANDOFF.md:65-66` |
| F-SS sharp shadow | Rows with self-defect have `O(delta/(1-P_ii))` shadow in other-row hull. | PROVED | Fable fact audited by wave 4 | `notes/fable-hlc-attack.md:473`; `notes/wave4/audit-summary.md:1-3` |
| F-ND near-delta exposure | Near-delta rows expose; safe constant about `0.85` after audit. | PROVED | Constants downgraded but mechanism confirmed | `notes/fable-hlc-attack.md:474`; `notes/wave4/audit-summary.md:8` |
| F-E kernel energy | `Gamma=P(g^2)-g^2`, `PGamma=0`, starvation/localization with explicit `Omega_g` dependence. | PROVED | Audit corrected constants and `R=osc(g)` dependence | `notes/fable-hlc-attack.md:475`; `notes/wave4/audit-summary.md:4-6` |
| F-GB g-budget | Positive coefficient mass at level `ell` obeys `sigma ell <= g_j + delta Omega_g`. | PROVED | Audit corrected fable's `+2.2delta` scope | `notes/fable-hlc-attack.md:476`; `notes/wave4/audit-summary.md:7` |
| F-WR wiggle rigidity | Common-pattern self-indexed webs obey rigidity; closed webs coincide up to error. | PROVED-mod-audit | Side conditions: self-indexing, small delta; separation corollary needs web radius bound | `HANDOFF.md:69-70`; `notes/fable-hlc-attack.md:477`; `notes/wave4/audit-summary.md:2-3` |
| F-BC blocker cap | S-full blockers have at most `kappa+delta` external coefficient mass. | PROVED | Audit strengthened constant | `notes/fable-hlc-attack.md:478`; `notes/wave4/audit-summary.md:8` |
| F-2R private two-shell collapse | Exact private two-shells collapse to coincident equal-input classes. | PROVED-mod-audit | Private-site case | `HANDOFF.md:70-71`; `notes/fable-hlc-attack.md:480` |
| original F-psi | Original uniform psi-gap/max-selection route. | RETRACTED/DOWNGRADED | Wave-4 audit did not confirm; wave-5 found counterexamples to literal gap | `notes/wave4/audit-summary.md:9-13`; `notes/wave5-sigma-wall-parallel.md:87-101` |
| PC private-cluster exposure | Fable private-cluster exposure statement. | PROVED-mod-audit / DOWNGRADED | Alpha loophole remains; do not use as closed theorem | `notes/fable-hlc-attack.md:213-233`; `notes/fable-hlc-attack.md:457` |
| RC energy endgame | Energy accounting route to force payment. | OPEN | Explicitly unresolved | `notes/fable-hlc-attack.md:457-458` |
| MRP day-1 residual | Middle-regime pinch was the remaining day-1 architecture. | OPEN at day 1; later NUMERICAL-safe | `notes/fable-hlc-attack.md:482-501`; `notes/mrp-decider-report.md:16-25` |

## C. Wave-5 to Wave-7 Harvest

| id/name | What writers may state | Status | Audit / gate | Source pointer |
|---|---|---|---|---|
| supplier-deficit lower bound | Branch A would follow from a lower bound on supplier deficit. | OPEN | Codex A reduction only | `notes/wave5-sigma-wall-parallel.md:30-39` |
| top-slab/top-band localization | No far top-band loitering without exposure or `H^2` negativity. | OPEN | Single residual after wave 5; later compressed to DMF | `notes/wave5-sigma-wall-parallel.md:193-207` |
| C10-exchange | Pairing the C10 witness with `g` gives `sum mu g + sum alpha g <= kappa Omega_g`. | PROVED | Codex A2; sharpened by W2 later | `notes/wave5-sigma-wall-parallel.md:138-144`; `notes/wave8-fable-closer.md:148-156` |
| self-starvation | Positive self-starvation bound from F-E at `v`. | PROVED-mod-audit | Wave-5 candidate; needs banking if used | `notes/wave5-sigma-wall-parallel.md:149-155` |
| height-energy anti-lemma | Canonical-`g` energy route cannot prove Branch A; its own bound is too small. | PROVED / dead-route | Negative result | `notes/wave5-sigma-wall-parallel.md:151-156`; `notes/wave8-fable-closer.md:522` |
| literal psi-gap | Uniform psi-gap for rho-far non-S-full rows. | REFUTED | Exact-rational counterexample and independent second mechanism | `notes/wave5-sigma-wall-parallel.md:87-101`; `notes/wave5-sigma-wall-parallel.md:184-191` |
| canonical-W conditioned F-psi | Corrected F-psi requiring canonical separator and high-danger-band S-fullness. | PROVED-mod-audit | Codex proof; reroutes through top-band residual | `notes/wave5-sigma-wall-parallel.md:243-253`; `notes/wave5-sigma-wall-parallel.md:302` |
| financing-row no-gain | Row exactness at the financier alone contains no `H` or `sigma` and cannot close localization. | PROVED / dead-route | Wave 6; sharpened by NG' analysis | `notes/wave5-sigma-wall-parallel.md:255-264`; `notes/wave8-fable-closer.md:274-295` |
| positive-carrier sharp shadow | Positive carrier measure of `v` shadows `v` sharply and has small mean deficit. | PROVED-mod-audit | Wave 6 candidate | `notes/wave5-sigma-wall-parallel.md:267-275` |
| carrier-blocker coupling | A far top-band blocker must couple to the carrier system. | OPEN / CONJECTURAL | Reduced but not proved; d11 supports numerically | `notes/wave5-sigma-wall-parallel.md:297-306`; `notes/d11-scale-disambiguation.md:49-58` |
| reciprocal-carrier lemma | Financier/blocker self-coupling should force height. | OPEN / CONJECTURAL | Mechanism named; later demystified as partly artifact | `notes/wave5-sigma-wall-parallel.md:278-302`; `notes/wave8-fable-closer.md:353-360` |
| column-carrier propagation | Column exactness propagates carrier overlap proportional to direct overlap. | PROVED-mod-audit | Wave 7; also carries gauge warning | `notes/wave5-sigma-wall-parallel.md:312-322` |
| raw `R Lambda=I` argument | Ungauged factorization arguments add no invariant content beyond row/column exactness. | REFUTED / dead-route | Gauge warning | `notes/wave5-sigma-wall-parallel.md:316-320` |
| binding-height identity | D9 "height = margin" is LP complementary slackness, not a hidden exactness identity. | RETRACTED/DOWNGRADED | Demystified by wave 7 | `notes/wave5-sigma-wall-parallel.md:320-323` |
| column-shadow lemma | Carrier system reproduces columns of `p_v` to `O(delta/sigma)`. | PROVED-mod-audit | Wave 7 reduction | `notes/wave5-sigma-wall-parallel.md:326-330` |
| aggregate pinning reduction | Coupling follows from aggregate pinning `sum_b mu_b P_vb >= c tau`. | PROVED-mod-audit | Reduction only; inequality not analytically proved | `notes/wave5-sigma-wall-parallel.md:326-336` |

## D. Wave-8 Lemmas, Corner, and Audit Corrections

| id/name | What writers may state | Status | Audit / gate | Source pointer |
|---|---|---|---|---|
| `(diamond)` dual identity | Failed-exposedness witness satisfies the exact affine vector identity and mass balance. | PROVED | Fable derivation; codex audit sound | `notes/wave8-fable-closer.md:75-101`; `notes/wave5-sigma-wall-parallel.md:420-429` |
| W2 sharp exchange | `sum mu g + sum alpha g <= t^* Omega_g`, sharper than `kappa Omega_g`. | PROVED | Codex audit sound | `notes/wave8-fable-closer.md:148-156`; `notes/wave5-sigma-wall-parallel.md:420-429` |
| W3 witness residual identities | Pushing a witness through `P` preserves affine residual but loses sign structure. | PROVED / warning | Useful identity, not a closure | `notes/wave8-fable-closer.md:158-165` |
| RF return-flow | Diagonal exactness gives carrier return-flow lower bound. | PROVED-mod-audit | Audit requires hypotheses/fix (`P_vv>=0` or sign split) | `notes/wave8-fable-closer.md:167-184`; `notes/wave5-sigma-wall-parallel.md:424-427` |
| ND' near-delta depth | Near-delta rows lie close to W and have deficit near `H`. | PROVED-mod-audit | Threshold correction: advertised `1.7tau` false at `delta=0.05`; use corrected threshold | `notes/wave8-fable-closer.md:186-224`; `notes/wave5-sigma-wall-parallel.md:424-425` |
| SF supply-forcing | Pairing the witness with `x(S)` gives S-mass forcing plus alpha-mass dichotomy. | PROVED | Reduction, not a closure | `notes/wave8-fable-closer.md:227-247`; `notes/wave8-fable-closer.md:590-592` |
| FC far-row coefficient cap | A rho-far row has bounded coefficient on `v`; off-v mass is at least `s_min`. | PROVED | Survived self-review | `notes/wave8-fable-closer.md:251-260`; `notes/wave8-fable-closer.md:593-595` |
| CPL transpose-coupling | S-full far rows must lean on carrier sites; conditional on SF branch. | PROVED-mod-audit | Wording fix for `P_vv=0`/site issue | `notes/wave8-fable-closer.md:261-270`; `notes/wave5-sigma-wall-parallel.md:426-427` |
| NG' no-gain lemma | Original stronger "consistency at any H" statement. | RETRACTED/DOWNGRADED | Audit says template/numeric support, not derived; keep only dead-route guidance | `notes/wave5-sigma-wall-parallel.md:420-423`; `notes/wave8-fable-closer.md:274-295` |
| MC margin cap | Far carrier fraction caps exposedness margin by `nu/(sigma theta_far)`. | PROVED | Special case of RW; survives audit | `notes/wave8-fable-closer.md:298-313`; `notes/wave8-fable-closer.md:596-598` |
| RW generalized row-witness | Row identity itself gives a feasible exposedness dual witness. | PROVED | Codex audit sound; exact at corner numerically | `notes/wave8-fable-closer.md:389-405`; `notes/wave8-fable-closer.md:596-600` |
| WL W-locality | A W-vertex has positive mass on far rows at most `nu/kappa`. | PROVED-mod-audit | Cleaner direct exposer proof required by audit | `notes/wave8-fable-closer.md:407-420`; `notes/wave5-sigma-wall-parallel.md:426-428` |
| ladder analysis | Long hidden ladder is the only positional route; self-indexing/quantitative Baake-Sumner is the obstruction. | CONJECTURAL / analysis | Not a theorem | `notes/wave8-fable-closer.md:430-445` |
| corner closed forms | `tau_*=2-sqrt(3)`, wall `2(2-sqrt(3))`, floor `(7+4sqrt(3))/4` for the measured family. | PROVED-mod-audit + NUMERICAL | Independent derivation confirms algebra; `t^*` optimality/family equality numerical | `notes/wave8-fable-closer.md:362-376`; `notes/wave5-sigma-wall-parallel.md:431-444`; `notes/wave8-fable-closer.md:599-605` |
| finite-corner calibration | Closer's claim that `DMF(m*=1)` reproduces entire measured envelope at finite delta. | RETRACTED/DOWNGRADED | R-handling bug; valid asymptotically only after correction | `notes/wave5-sigma-wall-parallel.md:436-444` |
| DMF + CEL implies sigma-wall/HLC | Conditional assembly through branches. | PROVED-mod-audit | Conditional on DMF and CEL; later HLC needs only existential DMF | `notes/wave8-fable-closer.md:471-492`; `notes/wave8-fable-closer.md:554-567` |
| CEL cluster-exposure lemma | Near-carrier branch closure. | OPEN | Old wound | `notes/wave8-fable-closer.md:475-479` |
| all-shallow witness obstruction map | Existing tools cannot force depth; all-shallow top-band web is the core object. | PROVED-mod-audit as obstruction map; not a theorem excluding it | `notes/wave8-fable-closer.md:508-545` |
| Baake-Sumner `delta=0` anchor | Exact idempotent Markov normal form kills shallow webs at `delta=0`. | PROVED-mod-audit | Source byte-pinned in main repo; report must cite carefully | `notes/wave5-sigma-wall-parallel.md:445-449`; `../../../docs/worklog.md:427` |

## E. Wave-9 and Post-d12 Sharpening

| id/name | What writers may state | Status | Audit / gate | Source pointer |
|---|---|---|---|---|
| existential-DMF suffices | Only one optimal witness with deep mass is enough for the HLC chain. | PROVED-mod-audit | Codex w9chain, high confidence | `notes/wave5-sigma-wall-parallel.md:508-518` |
| corrected `a` formula | If `E(delta)/tau -> e`, then `a=(1/(2m*)+e)^{-2}`; `E=o(tau)` gives `a->4m*^2`. | PROVED-mod-audit | Corrects fable's simpler formula | `notes/wave5-sigma-wall-parallel.md:510-513` |
| `t^*=0` chain case | Exchange gives `sum mu g <= 0`, so DMF forces `H<=E`. | PROVED-mod-audit | Closes chain caveat | `notes/wave5-sigma-wall-parallel.md:514-516` |
| top-vertex WLOG | HLC may pick a height-maximizing row vertex; non-top hidden vertices are not WLOG. | PROVED-mod-audit | Codex w9chain | `notes/wave5-sigma-wall-parallel.md:517-518` |
| W-rows deep | If `w in W`, then `g_w >= H`. | PROVED | One-line consequence | `notes/wave5-sigma-wall-parallel.md:519-520` |
| `sigma_tilde` height-collapse | If hidden top vertex has `widetilde sigma_v <= s<1`, then `H <= delta Omega_g/(1-s)`. | PROVED | Orchestrator verified | `notes/wave5-sigma-wall-parallel.md:521-528` |
| top-separator nonnegative | For top vertex, `g_i>=0` for all rows. | PROVED-mod-audit | Sub-lemma banked with height collapse | `notes/wave5-sigma-wall-parallel.md:525-526` |
| optimal-witness vacuous depth in small-sigma case | In `widetilde sigma`-small branch every optimal witness is vacuously deep. | PROVED-mod-audit | Sub-lemma banked with height collapse | `notes/wave5-sigma-wall-parallel.md:525-528` |
| direct-two-site exclusion | Direct mutual carrying with coefficient above `1/2+O(delta)` is impossible. | PROVED-mod-audit | Partial cycle exclusion | `notes/wave5-sigma-wall-parallel.md:530-534` |
| disjoint-two-ball exclusion | Closed disjoint order-one 2-block cycles are impossible under stated return-mass inequality. | PROVED-mod-audit | Partial cycle exclusion | `notes/wave5-sigma-wall-parallel.md:530-534` |
| non-skinny payment | If mutual-shadow mass is not skinny, then `delta >= cH^2`. | PROVED-mod-audit | Partial cycle exclusion | `notes/wave5-sigma-wall-parallel.md:533-535` |
| skinny spread-mass regime | The remaining cycle/web regime with mass spread across partner rho-balls. | OPEN | Survives wave-9 partial lemmas | `notes/wave5-sigma-wall-parallel.md:535-536` |
| d12 broad "DMF supported" interpretation | D12 support applies to probed corner/budget regimes only. | RETRACTED/DOWNGRADED | Post-w9 height-collapse shows small-delta web case unmeasured | `notes/wave5-sigma-wall-parallel.md:538-557`; conflict with `notes/d12-dmf-depth-profiles.md:13-30` |
| small-delta sigma regime | At small delta with `H~tau/2`, `widetilde sigma_v -> 1`; web case is forced. | PROVED-mod-audit | Consequence of height-collapse contrapositive | `notes/wave5-sigma-wall-parallel.md:539-547` |
| decisive unmeasured datum | Witness depth profiles on verified small-delta flat-floor instances are not known. | OPEN / NUMERICAL-GAP | d13 was requested by source notes but not in required source list | `notes/wave5-sigma-wall-parallel.md:551-555` |

## F. Numerical Campaign Inventory

| id/name | What writers may state | Status | Verification gate | Source pointer |
|---|---|---|---|---|
| 67k+ exact instances | No counterexample found across independent campaigns. | NUMERICAL | Exact constructions and robust verification gates | `HANDOFF.md:47-50` |
| d8 MRP decider | MRP middle regime is numerically safe; global min `delta/H^2 approx 3.484` at `H/tau approx 0.536`; no refutation below 3. | NUMERICAL | `d8_mrp3.verify`, multiplicity-correct W, presolve off, honest tau | `notes/mrp-decider-report.md:16-25`; `notes/mrp-decider-report.md:107-161` |
| d8 sigma-wall law | In the tested family `H/tau approx min(sigma,0.536)` and floor `max(1/sigma^2,3.49)`. | NUMERICAL | Same d8 gate | `notes/mrp-decider-report.md:127-152` |
| d8 `k_groups` effect | `k_groups` did not affect the verified floor to four digits. | NUMERICAL | d8 sweep | `notes/mrp-decider-report.md:23-25`; `notes/mrp-decider-report.md:63-79` |
| d9 dual certificates | Same level functional in both regimes; financing blocker binds; min-neg duals on pin/neg/epi. | NUMERICAL | Gurobi dual simplex, presolve off, all optimal | `notes/d9-dual-certificates.md:438-497` |
| d9 budget/wall table | Edge cells from `sigma=0.05` to `1.00` reproduce the two regimes and 3.48 floor. | NUMERICAL | All cells verified | `notes/d9-dual-certificates.md:39-497` |
| d10 far top-band feed | `M_far` remains bounded around `2.045-2.141`; literal `T_far=empty` is false. | NUMERICAL | Verified d8 instances, separator LPs | `notes/d10-certificate-mining.md:129-146` |
| d10 financier law | Along probed family, `delta_min=(1/2)g_f`, `g_f=H`. | NUMERICAL; later reinterpreted by d11 | Probe 2 verified family curves | `notes/d10-certificate-mining.md:147-183` |
| d10 scale degeneracy catch | `g_f=H` and `g_f=2delta` were indistinguishable at default scale. | RETRACTED/DOWNGRADED for original interpretation | Orchestrator catch | `notes/wave5-sigma-wall-parallel.md:353-375` |
| d11 scale sweep | D8 family rigidly lies on `g_f=H=2delta`; it is a budget-line carrier, not small-delta flat-floor carrier. | NUMERICAL | 7 verified scales, 2.06 decades | `notes/d11-scale-disambiguation.md:20-47` |
| d11 aggregate coupling `M` | `min M/tau >= 1.075` in probed wall instance and larger at small scale. | NUMERICAL | M-minimization over family realization freedom | `notes/d11-scale-disambiguation.md:49-58`; `notes/d11-scale-disambiguation.md:186-188` |
| d12 DMF probe | In 12 verified off-edge stacking instances, exposedness witnesses were 100 percent deep with `m*=1`. | NUMERICAL | HiGHS presolve off, residuals `<=3e-16`, robust W | `notes/d12-dmf-depth-profiles.md:13-30`; `notes/d12-dmf-depth-profiles.md:121-134` |
| d12 sigma-tilde finding | Probed instances had `sigma_v^{off} approx 1.01-1.07` but `widetilde sigma=0`. | NUMERICAL; later downgraded in scope | D12 gate; post-w9 reinterpretation | `notes/d12-dmf-depth-profiles.md:33-42`; `notes/wave5-sigma-wall-parallel.md:538-557` |
| d12 all-shallow search | No all-shallow witness was found in reachable verified instances. | NUMERICAL; limited scope | D12; does not settle web case | `notes/d12-dmf-depth-profiles.md:72-100`; `notes/wave5-sigma-wall-parallel.md:538-557` |

## G. Refuted, Downgraded, and Dead Routes

| id/name | What writers may state | Status | Why | Source pointer |
|---|---|---|---|---|
| literal psi-gap route | False: far non-S-full rows can trade S-deficit against lambda-phi. | REFUTED | Exact-rational counterexample plus independent second counterexample | `notes/wave5-sigma-wall-parallel.md:87-101`; `notes/wave5-sigma-wall-parallel.md:184-191` |
| general-row leakage | L5' does not hold for arbitrary rows. | REFUTED / scoped | Only global maximizer version survives | `HANDOFF.md:63` |
| top-band localization as `T_far=empty` | False in literal form. | REFUTED / NUMERICAL | D10 shows robust far top-band occupancy | `notes/d10-certificate-mining.md:129-146`; `notes/wave5-sigma-wall-parallel.md:348-352` |
| canonical-g kernel energy proof | Cannot prove Branch A; canonical energy bound is too small. | DEAD ROUTE | A3 anti-lemma | `notes/wave5-sigma-wall-parallel.md:149-156` |
| row exactness at financier | Contains no `H` or `sigma`, cannot force depth. | DEAD ROUTE | w6fin/no-gain, NG' downgrade | `notes/wave5-sigma-wall-parallel.md:255-264`; `notes/wave8-fable-closer.md:274-295` |
| diagonal exactness at blocker | Vacuous or `H`-free in the relevant regimes. | DEAD ROUTE | NG' demystification | `notes/wave8-fable-closer.md:274-295`; `notes/wave8-fable-closer.md:517-519` |
| raw factorization gauge route | `R Lambda=I` arguments are not gauge-invariant. | DEAD ROUTE / REFUTED | Wave-7 gauge warning | `notes/wave5-sigma-wall-parallel.md:316-320` |
| finite-corner equals asymptotic proof | Corner constants do not prove HLC asymptotically. | RETRACTED/DOWNGRADED | R-handling bug and corner-scale analysis | `notes/wave5-sigma-wall-parallel.md:436-444`; `notes/wave8-fable-closer.md:451-466` |
| broad d12 DMF proof | D12 support does not cover small-delta web case. | RETRACTED/DOWNGRADED | Height-collapse contrapositive | `notes/wave5-sigma-wall-parallel.md:538-557` |
| averaging/quasi-stationary potentials | Route is vacuous at target scale. | DEAD ROUTE | Day-1 map | `HANDOFF.md:74-78`; `ORCHESTRATION.md:49-87` |
| height tests for projection norm excess | Re-derives weak bounds only. | DEAD ROUTE | Day-1 map | `HANDOFF.md:74-78` |
| raw circuit bounds | Do not close the exposed-hull/HLC gap. | DEAD ROUTE | Day-1 map | `HANDOFF.md:74-78` |
| unlocalized dual descent | Constant loss too large (`~1/4 >> H`). | DEAD ROUTE | Day-1 map | `HANDOFF.md:74-78` |
| maximality contradictions without localization | Do not control the high zero face. | DEAD ROUTE | Day-1 map | `HANDOFF.md:74-78` |
| rank induction via stochastic complement | Parked/dead for this route. | DEAD ROUTE | Day-1 map | `HANDOFF.md:74-78` |
| KKT localization-energy dichotomy | Did not close; energy route leaves orphans. | DEAD ROUTE | Day-1 and fable analysis | `HANDOFF.md:74-78`; `notes/fable-hlc-attack.md:317-333` |
| pure convex shadow composition | Vacuous as `mu -> 1`. | DEAD ROUTE | Day-1 map | `HANDOFF.md:74-78` |
| log-staircase/shells | Exactness/X1 is the wall; no counterexample produced. | DEAD ROUTE | Day-1 map | `HANDOFF.md:74-78` |

## H. Literature and External-Status Notes

| id/name | What writers may state | Status | Caveat | Source pointer |
|---|---|---|---|---|
| HLC originality | No known quantitative Douglas-Ando stability theorem was found; HLC appears original. | LITERATURE-SWEEP / not theorem | Literature sweep, not exhaustive proof | `notes/literature-sweep-hlc.md:1-15` |
| exact Douglas-Ando/Seever case | Exact contractive projections are conditional expectations/averaging operators. | CITED-background | Acquire/flag refs before final banking | `notes/literature-sweep-hlc.md:1-15` |
| Baake-Sumner equal-input normal form | Exact idempotent Markov structure anchors the `delta=0` web exclusion. | CITED-background | `baake-sumner-2007.11433` is in refs; cite final source precisely | `../../../docs/worklog.md:427`; `notes/wave8-fable-closer.md:530-545` |
| Hadwin-Li / Curgus-Jewett / Douglas / Ando follow-up refs | Potential background for final paper. | TO-ACQUIRE / provenance caveat | Do not cite as byte-grounded unless added to refs | `notes/literature-sweep-hlc.md:13-15`; `HANDOFF.md:98-99` |

## Ambiguity Watchlist

| item | Conflict | Required report handling |
|---|---|---|
| F-psi | Fable source lists it as proved-mod constant chasing, but wave-4 audit says not confirmed and wave-5 refutes literal gap. | Use `original F-psi` only as downgraded; use `conditioned F-psi` only with its conditions. |
| sigma-wall | Day-1 notes use `sigma_v`; wave-8/9 show formal off-site sigma and non-W sigma differ. | State old law historically; formulate future math using `widetilde sigma_v`. |
| corner theorem | Algebraic constants are exact for the measured family, but global optimality is numerical/mod-audit. | Badge as `PROVED-mod-audit` plus `NUMERICAL`, never unconditional theorem for all `P`. |
| d12 support | d12 says DMF supported broadly in probed instances; post-w9 says that support is corner-regime-only. | Present d12 as useful numerical evidence with downgraded scope. |
| NG' | Fable lists as proved negative result; codex audit says a stronger consistency claim was not derived. | Keep no-gain/dead-route content; do not state the stronger consistency theorem. |
| RF/CPL/ND'/WL | Wave-8 proofs survive, but audit requires fixes. | Use `PROVED-mod-audit` unless the writer explicitly includes the corrected hypotheses. |
