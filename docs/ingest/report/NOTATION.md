# Canonical Notation and Glossary

This file is the writer-facing notation contract. Do not introduce new symbols in the `.tex` shards unless this file is updated first. When source notes conflict, the "report notation" column below wins.

## Canonical Notation Table

| Symbol | Meaning | First-defined-in shard |
|---|---|---|
| `n` | number of rows/states/sites | `01-linear-markov-setting` |
| `P` | exact signed affine retraction matrix, with `P1=1` and `P^2=P` | `01-linear-markov-setting` |
| `Q` | row-stochastic almost-idempotent matrix in the original problem | `01-linear-markov-setting` |
| `p_i` | row `i` of `P`, viewed as a point/coefficient vector | `01-linear-markov-setting` |
| `K` | row polytope `conv{p_i}` | `01-linear-markov-setting` |
| `\Delta_n` | standard simplex | `01-linear-markov-setting` |
| `\nu_i` | row negative mass, `sum_k (P_{ik})_-` | `01-linear-markov-setting` |
| `\delta` | max row negative mass, `max_i \nu_i` | `01-linear-markov-setting` |
| `\tau` | `sqrt(\delta)` | `02-geometry-exposedness` |
| `\rho` | exposure radius, fixed as `4\tau` | `02-geometry-exposedness` |
| `\kappa` | exposure margin, fixed as `\tau/4` | `02-geometry-exposedness` |
| `\|x\|_1` | `ell^1` norm | `01-linear-markov-setting` |
| `D_K` | `ell^1` diameter bound for `K`; use instead of source-note `D` when possible | `01-linear-markov-setting` |
| `\mathsf R` | frame/realization matrix in `P=\Lambda\mathsf R`, `\mathsf R\Lambda=I` | `01-linear-markov-setting` |
| `\Lambda` | coefficient/load matrix in `P=\Lambda\mathsf R` | `01-linear-markov-setting` |
| `\mathcal W` | set of `(rho,kappa)`-well-exposed row vertices | `02-geometry-exposedness` |
| `W` | allowed shorthand for `\mathcal W` inside formulas after first definition | `02-geometry-exposedness` |
| `C_W` | `conv(\mathcal W)` | `02-geometry-exposedness` |
| `H` | hidden height, `max_i dist_1(p_i,C_W)` | `02-geometry-exposedness` |
| `v` | a height-maximizing hidden row vertex unless otherwise stated | `02-geometry-exposedness` |
| `\phi` | canonical separator for `v`: normalized `ell^\infty` dual, zero on `C_W`, height `H` at `p_v` | `02-geometry-exposedness` |
| `g_i` | canonical deficit, `H-\phi(p_i)` | `02-geometry-exposedness` |
| `g` | deficit vector `(g_i)_i`, with `g=Pg` in the canonical setup | `02-geometry-exposedness` |
| `\Omega_g` | oscillation `max_i g_i - min_i g_i`; replaces source-note `R=osc(g)` | `02-geometry-exposedness` |
| `t^*(v)` | optimal exposedness LP margin for row `v` | `02-geometry-exposedness` |
| `F_v` | set of rows `rho`-far from `v` | `02-geometry-exposedness` |
| `h` | affine exposedness test function, `0<=h<=1`, `h(v)=0` | `02-geometry-exposedness` |
| `\mu,\alpha,\beta,\gamma` | dual witness variables for failed exposedness | `02-geometry-exposedness` |
| `A` | total alpha mass `sum_i alpha_i`; avoid using for algebras in this report | `02-geometry-exposedness` |
| `B` | total beta mass `sum_i beta_i`, equal to `t^*` for an optimal witness | `02-geometry-exposedness` |
| `S` | site set, usually positive support of `p_v` or a selected cluster support | `02-geometry-exposedness` |
| `\sigma_v^{off}` | formal off-own-site positive mass `sum_{k != v} (P_{vk})_+` | `02-geometry-exposedness` |
| `\widetilde\sigma_v` | positive coefficient mass of `v` on rows outside `conv(\mathcal W)`; includes `k=v` if `p_v notin conv(\mathcal W)` and `P_{vv}>0` | `02-geometry-exposedness` |
| `A_v` | positive carrier set `{k: P_{vk}>0}`; do not confuse with total alpha mass `A` | `02-geometry-exposedness` |
| `\lambda_k` | normalized carrier weight `P_{vk}/sigma` on a specified carrier set | `02-geometry-exposedness` |
| `m_*` | DMF deep-witness mass parameter | `08-residual-dmf` |
| `E(\delta)` | DMF depth error width | `08-residual-dmf` |
| `e` | asymptotic ratio `lim E(\delta)/\tau` when it exists | `08-residual-dmf` |
| `\Gamma` | kernel energy vector `P(g^2)-g^2` | `06-day1-belt` |
| `d_{poke}` | family poke depth in numerical constructions; replaces overloaded source `d` when clarity matters | `05-corner-theorem` |
| `\tau_*` | corner scale `2-\sqrt 3` | `05-corner-theorem` |
| `\delta_*` | corner negativity `(2-\sqrt 3)^2` | `05-corner-theorem` |

## Source-Name Mapping and Clash Resolution

| Source-note name | Report notation | Reason |
|---|---|---|
| `R = osc(g)` | `\Omega_g` | Avoids collision with the frame matrix. |
| `R` in `P=Lambda R`, `R Lambda=I` | `\mathsf R` | Keeps factorization notation distinct from oscillation. |
| `R_w` in wiggle rigidity | `r_{web}` or explicit "web radius" | Avoids the standalone `R` collision. |
| `D = diam_1` | `D_K` | Names the row-polytope diameter. |
| source `sigma_v` meaning off-own-site mass | `\sigma_v^{off}` | This is not the branch variable after the wave-8/9 catch. |
| source `sigma_v` in d8/MRP design sweeps | `\widetilde\sigma_v` | The d8 "sigma wall" was about non-W positive mass, not formal off-site mass. |
| "sigma_v-wall" | "historical sigma-wall" or "`\widetilde\sigma` wall" | Use the historical term only when discussing the campaign history. |
| `g_f = H` | "family financier identity" | Numerical/family identity, not a general theorem. |
| `delta/H^2 = 3.49` | "finite-corner floor" unless stated as numerical record | Prevents presenting a measured finite corner as an asymptotic theorem. |
| `R inert` | "`\mathsf R` inert in the final alternating LP step" | Avoids overclaiming global idempotence irrelevance. |

## Status Badge Vocabulary

| Badge | Meaning |
|---|---|
| `PROVED` | Derivation has a prose proof and survived the stated audit. |
| `PROVED-mod-audit` | Proof is structurally present but carries an explicit audit caveat, correction, or pending formal banking condition. |
| `NUMERICAL` | Verified computation with the named gate; not a theorem. |
| `CONJECTURAL` | Proposed mathematical statement supported by evidence but not proved. |
| `OPEN` | Current obstacle or unsolved statement. |
| `REFUTED` | Statement is false; source includes a counterexample or decisive contradiction. |
| `RETRACTED/DOWNGRADED` | Earlier stronger reading was withdrawn or narrowed. |
| `AMBIGUOUS` | Sources conflict or leave quantifiers/status unclear. Writers must not use as a theorem. |

## Jargon Glossary

| Term | Plain definition | Status if it names a result |
|---|---|---|
| affine retraction | Exact idempotent affine map on row vectors, represented by `P1=1`, `P^2=P`. | Definition |
| almost idempotent stochastic matrix | Row-stochastic `Q` with small `||Q^2-Q||`. | Target setting |
| signed-idempotent formulation | Equivalent form using exact signed `P` with small row negative mass. | `lem-classical-equiv`: PROVED, af-validated in main repo |
| stochastic idempotent | Row-stochastic matrix satisfying `Q^2=Q`. | Definition |
| row negative mass | Total negative coefficient mass in one row. | Definition |
| max-neg units | Normalization where `delta=max_i nu_i`. | Definition |
| self-indexing | Convention that row coordinates are also coefficients on row labels. | Definition |
| row polytope | Convex hull of the rows of `P`. | Definition |
| hidden height | Distance from a row to `conv(W)`, maximized over rows as `H`. | Definition |
| HLC | Hidden localization claim: a dimension-free bound `delta >= a H^2`, equivalently `H=O(tau)`. | OPEN; conditional on DMF after wave 9 |
| op-classical | Original classical dimension-free stability problem for almost-idempotent stochastic matrices. | OPEN target |
| op-exposed-hull | Global exposed-hull reduction problem. | OPEN, but conditionally reduced to HLC |
| thm-cluster | Main-branch clustering theorem used in the outer reduction. | PROVED in source handoff |
| `(rho,kappa)`-exposedness | A row vertex has an affine separator zero at itself and at least `kappa` on all `rho`-far rows. | Definition |
| well-exposed vertex | A row vertex satisfying `(rho,kappa)`-exposedness. | Definition |
| `W` / `\mathcal W` | Set of well-exposed row vertices. | Definition |
| hidden vertex | Row vertex outside `conv(W)` or not controlled by the current exposed hull. | Definition |
| hidden top vertex | Hidden vertex attaining the maximal height `H`. | Definition; top-vertex WLOG for HLC is PROVED in wave 9 |
| canonical separator | Normalized affine functional separating a top hidden vertex from `conv(W)`. | Definition |
| deficit `g` | Nonnegative height loss `H-\phi(p_i)` relative to the canonical separator. | Definition |
| `Omega_g` | Oscillation of `g`; replaces source `R=osc(g)`. | Definition |
| top band | Rows with small deficit, typically `g < kappa Omega_g` or a stated variant. | Definition |
| top slab | Synonym for top band in wave-5 notes; use "top band" in report. | Definition |
| high zero face | Low-deficit face where failed-exposedness dual slack can sit. | Definition |
| exposedness LP | Linear program maximizing the margin `t^*(v)` of an exposedness separator. | Definition |
| failed-exposedness witness | Dual certificate `(mu,alpha,beta,gamma)` showing `t^*(v)<kappa`. | Definition |
| `(diamond)`-dual | Exact vector identity for a failed-exposedness witness. | PROVED (wave 8 dual derivation; audit sound) |
| alpha mass | Total slack mass `A=sum alpha_i` in the dual witness; historically uncontrolled. | Definition / open-control issue |
| blocker | A far row that binds or obstructs an exposedness separator. | Definition |
| supplier | Row supplying positive coefficient mass to a hidden row. | Definition |
| carrier | Row with positive coefficient in a selected row identity. | Definition |
| financier | Binding row that pays for an apex poke in the numerical families. | Jargon; not a universal theorem |
| witness row | Row in the support of `mu` for an exposedness-dual witness. | Definition |
| S-full | A row has almost all mass on a site set `S`, usually `x(S)>=1-kappa`. | Definition |
| `sigma_v^{off}` | Formal positive mass away from row `v`'s own index. | Definition |
| `\widetilde sigma_v` | Positive mass on non-W rows; robust branch variable after wave-8/9. | Definition |
| sigma-wall | Historical measured law `H/tau approx min(sigma,0.536)`. | NUMERICAL/OPEN; use `\widetilde sigma` if stated mathematically |
| Branch A | Small-sigma budget branch, historically `sigma<=1/2`. | OPEN as sigma-wall branch; partly superseded by DMF |
| Branch B | Large-sigma margin-pinning branch. | OPEN as sigma-wall branch; partly superseded by DMF |
| budget line | Family relation `H=2delta`, equivalently `delta=H/2`. | NUMERICAL/family law |
| flat floor | Measured `delta/H^2 approx 3.49` floor. | NUMERICAL; finite-corner interpretation |
| the corner | Finite point `tau_*=2-sqrt(3)` producing wall `2(2-sqrt(3))` and floor `(7+4sqrt(3))/4`. | PROVED-mod-audit / NUMERICAL-family optimality |
| corner theorem | Exact closed-form explanation of the measured corner constants. | PROVED-mod-audit; not a universal asymptotic theorem |
| MRP | Middle-regime pinch, originally the final day-1 residual. | NUMERICAL: d8 found it safe; not an analytic proof |
| DMF | Deep-witness mass forcing: an optimal witness carries mass at deficit near `H`. | OPEN terminal residual |
| existential DMF | Only one optimal witness needs deep mass. | CONDITIONAL theorem: sufficient for HLC |
| all-shallow witness | Failed-exposedness witness whose `mu` mass avoids deep rows. | OPEN obstruction object |
| shallow hidden-witness graph | Directed graph of shallow hidden vertices witnessing one another. | OPEN framework |
| two-cycle obstruction | Minimal possible all-shallow web `a -> b -> a`. | OPEN; recursion attack died here |
| quantitative Baake-Sumner stability | Needed stability theorem excluding shallow hidden webs by perturbing exact equal-input idempotent structure. | OPEN |
| CEL | Cluster-exposure lemma for near-carrier branch. | OPEN / old wound |
| FTI-2 | Distinct-vertex mutual-shadow construction/numeric route. | NUMERICAL: failed to verify small-delta web |
| `(diamond)` | The displayed dual identity in Section 02/07. | PROVED |
| row-witness | Dual witness built directly from a row identity. | RW: PROVED |
| W-locality | W-vertices have little positive mass on far rows. | WL: PROVED, with cleaner audit proof |
| height collapse | Small `\widetilde sigma` forces `H <= delta Omega_g/(1-s)`. | PROVED (wave 9) |
| web case | Large `\widetilde sigma`, where non-W top-band rows carry the mass. | OPEN |
| skinny regime | Spread-mass mutual-shadow regime not killed by wave-9 cycle lemmas. | OPEN survivor |

## Result-Tag Glossary

| Tag | Plain definition | Status |
|---|---|---|
| L1 | Lone-far-row lemma: a row far from the hull of the others is exposed with margin `rho/(2+4delta)`. | PROVED, audited |
| L2 | A far/high row yields a far/high row vertex. | PROVED, audited |
| L2' | Hidden vertex has a `rho`-shadow in the other-row hull. | PROVED, with recursion caveat |
| C10 | Failed-exposedness LP dual; alpha mass remains the historic crux. | PROVED identity; alpha-control OPEN |
| L4 | Frame-clipping height cap. | PROVED, audited |
| L5' | Leakage at a global height maximizer only. | PROVED, scoped; general-row version REFUTED |
| L6 | Identity-frame linear bound `delta >= H/2`. | PROVED for `\mathsf R=[I|0]`; transfer OPEN |
| N1 | Nilpotent-chain off-chain forcing. | PROVED, audited |
| F1 | Skinny near-coincidence / mutual-shadow elimination. | PROVED, audited |
| X1 | One-mode wall; exact shell obstruction. | PROVED, subsumed by F-WR in common-pattern webs |
| X2 | Stochastic-complement rank preservation. | PROVED, audited |
| F-SS | Sharp shadow: rows with nontrivial self-defect have small shadows. | PROVED, audited |
| F-ND | Near-delta exposure. | PROVED, audited with conservative constant |
| F-E | Kernel energy `Gamma=P(g^2)-g^2`, `PGamma=0`, starvation/localization bounds. | PROVED, audited with `Omega_g` dependence |
| F-GB | Deficit budget `sigma ell <= g_j + delta Omega_g`. | PROVED, audited |
| F-WR | Wiggle rigidity for common-pattern webs. | PROVED with side conditions |
| F-BC | Blocker cap, strengthened to `kappa+delta` in audit. | PROVED, audited |
| F-2R | Private two-shells collapse to coincident equal-input classes. | PROVED in private-site case |
| F-psi | Original psi-gap route. | DOWNGRADED/CONDITIONAL; literal uniform gap REFUTED |
| conditioned F-psi | Canonical-W conditioned replacement. | PROVED-mod-audit; reroutes through same residual |
| W2 | Sharp exchange `sum mu g + sum alpha g <= t^* Omega_g`. | PROVED, audited |
| W3 | Witness residual/push-through identity, with sign-loss warning. | PROVED identity / warning |
| RF | Return-flow from diagonal exactness at `v`. | PROVED with audit fixes/hypotheses |
| ND' | Near-delta depth, explaining financier identity in concentrated cases. | PROVED with threshold correction |
| SF | Supply-forcing with alpha-mass dichotomy. | PROVED reduction, not a closure |
| FC | Far-row coefficient cap. | PROVED |
| CPL | Transpose coupling from S-full blockers to carriers. | PROVED conditional on SF branch; audit wording fixes |
| NG' | Claimed no-gain/consistency lemma around blocker exactness. | RETRACTED/DOWNGRADED to analysis/dead-end guidance |
| MC | Margin cap from far carriers. | PROVED |
| RW | Generalized row-witness lemma. | PROVED |
| WL | W-locality. | PROVED, cleaner proof after audit |
| sigma-height-collapse | Small `\widetilde sigma` height-collapse lemma. | PROVED |
| direct-two-site | Wave-9 partial exclusion of strong direct two-site carrying. | PROVED partial |
| disjoint-two-ball | Wave-9 exclusion of closed disjoint order-one 2-block cycles. | PROVED partial |
| non-skinny payment | Wave-9 payment bound outside the skinny spread-mass regime. | PROVED partial |

## Forbidden Shortcuts

- Do not write `R` alone for oscillation or frame matrix.
- Do not state the historical `sigma_v` wall without saying whether the symbol is `sigma_v^{off}` or `\widetilde sigma_v`.
- Do not call the d8/d9/d10/d11/d12 numerical findings theorems.
- Do not cite F-psi as proved unless using the conditioned canonical-W replacement and its status.
- Do not present DMF, CEL, the web-case exclusion, or quantitative Baake-Sumner stability as proved.
- Do not use the corner constants as an asymptotic HLC proof.
