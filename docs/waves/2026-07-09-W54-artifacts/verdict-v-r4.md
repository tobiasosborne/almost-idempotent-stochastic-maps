VERDICT: VALID-WITH-CORRECTIONS — The hidden-vertex positive-margin claim is correct, but the audit text must add the missing rho>0/hiddenness qualifier to its broad margin slogan and must not cite LP attainment as part of a shard contract that does not state it.

1. Statement attacked: §1 exposedness LP and the meaning of "optimal exposer".

   Checked input status: `lem-hiddenness-dual-witness` is `status: proved`; `lem-zero-face-localization` is `status: proved`. No illegal conjecture/heuristic/numerical input was used here.

   Contract/usage daylight:

   - Contract line:
     `contract: Hiddenness dual witness: for an exact signed idempotent P and a hidden row vertex v (rho = 4*tau, kappa = tau/4, tau = sqrt(delta(P))), writing F_v = {j : ||p_j - p_v||_1 >= rho} for the rho-far row-index set (nonempty for hidden v), there exist lambda_f >= 0 (f in F_v) with sum_f lambda_f = 1 and alpha_i, beta_i >= 0 (over all row indices i) with sum_i beta_i = t*(v) < kappa, such that sum_f lambda_f*(p_f - p_v) + sum_i alpha_i*(p_i - p_v) = sum_i beta_i*(p_i - p_v).`
   - Prover usage:
     `LP attainment is part of the hiddenness-dual-witness proof shape.`

   This is not contract-exact. The contract supplies the dual witness, not the primal LP attainment or the definition of an optimal exposer. The claim is repairable from `def-exposed` plus finite-dimensional LP compactness/closedness, but the text should not present it as an entitlement from the `lem-hiddenness-dual-witness` contract.

   Required correction 1: replace the sentence about `lem-hiddenness-dual-witness` proof shape with an explicit finite-LP argument, or register/cite a separate proved contract saying that the exposedness supremum is attained and that an optimal exposer means an admissible `h` with `min_F h = t*(v)` when `F` is nonempty and `t*(v)<infty`.

2. Statement attacked: §1 boundary analysis for `lem-zero-face-localization`.

   Contract checked:
   `contract: Zero-face localization: for an exact signed idempotent P and a hidden geometrically distinct row vertex u, every row z with h*(p_z) = 0 for an optimal exposer h* at u satisfies ||p_z - p_u||_1 < 4*tau (rho-near); if additionally u lies within 4*tau of a hidden top v of height H, then ||p_z - p_v||_1 < 8*tau and z has depth > H - 8*tau.`

   The far-constraint step is valid once `t*(u)>0`: if `h*` is optimal then every far row has `h*(p_f) >= t*(u)`, so a row with `h*(p_z)=0` cannot be far. Therefore `||p_z-p_u||_1 < rho = 4*tau`.

   The artificial `t*=0` sanity check is also correct. With `F_u` nonempty, `h=0` is admissible and has objective `0`; if `t*(u)=0`, every optimal exposer has `min_{F_u} h=0`, and because `F_u` is finite some far row lies on the zero face. Relative-interior selection does not fix that abstract boundary.

   The second constant check is sound: if additionally `||p_u-p_v||_1 < 4*tau`, then `||p_z-p_v||_1 < 8*tau` by the triangle inequality. Since `v` has height `H`, the 1-Lipschitz distance-to-`C_W` function gives the depth lower bound `> H - 8*tau`. These constants are dimension-free.

3. Statement attacked: §1/§3 positive-margin proof for a hidden geometrically distinct row vertex.

   Relevant definition checked:
   `A row $p_v$ is a *row vertex* of $P$ if $p_v\notin\operatorname{conv}\{\,p_j:p_j\neq p_v\text{ as vectors of }\mathbb R^n\,\}$`
   `(geometrically coincident duplicate rows count as a single point; a repeated point is still a vertex if it lies outside the hull of the *other* points).`

   The strict-separation step is valid. Let `C` be the convex hull of the other distinct row points. It is a compact convex set in finite-dimensional `R^n`, and the row-vertex condition says `p_v notin C`. Strong separation gives an affine `a` with `a(p_v)=0` and `a>0` on `C`, hence on every other distinct row point. The fact that all rows lie in the affine hyperplane `sum x_i=1` does not break separation: separation may be performed in that affine hull and extended to an affine functional on `R^n`.

   The hidden-implies-positive-rho step is valid. From `def-visible-set`, `rho=4*sqrt(delta)` and `kappa=sqrt(delta)/4`. If `delta=0`, then `kappa=0`; `h=0` is admissible and gives `t*(v)>=0`, so the strict hidden inequality `t*(v)<kappa` is impossible. Thus a hidden row vertex has `delta>0` and `rho>0`.

   The normalization and clone checks are valid after that point. Since `F_v` is nonempty and `rho>0`, any `f in F_v` satisfies `p_f != p_v`; so there is at least one other distinct row point, `M=max_j a(p_j)>0`, and `m=min{a(p_j): p_j != p_v as a vector}>0`. With `h=a/M`, all row values lie in `[0,1]`, clones of `v` have value `0`, clones of other points inherit their positive value, and far rows cannot be clones of `v`. Hence `min_{f in F_v} h(p_f) >= m/M > 0`, so `t*(v)>0`.

   Counterexample hunt: the broad slogan on PROVER-ANSWER.md line 1 is false if read literally without hiddenness or `rho>0`. For `P=I_2`, `delta=0`, `rho=0`, each row is a geometrically distinct row vertex and `F_v` is nonempty, but every admissible exposer has the self-row in the far set and `t*(v)=0`, not `>0`. This does not refute the target claim because those vertices are not hidden (`kappa=0` and `t*(v)=0`).

   Required correction 2: every standalone statement of the auxiliary margin lemma must include either `rho>0` or the hiddenness hypotheses that imply it. The safe registry statement is the one in §4: for a finite row configuration, a geometrically distinct row vertex `v` with `rho>0` and nonempty `F_v` has `t*(v)>0`.

   Minor ordering correction: in §3, define `m=min{a(p_j): p_j != p_v as a vector}` only after establishing `delta>0`, `rho>0`, and `F_v` nonempty, since those facts ensure the set of other distinct row points is nonempty.

4. Statement attacked: §2 consumer audit.

   I re-ran the dependency search. Direct `deps:` consumers of `lem-zero-face-localization` in `argument/lemmas/*.md` are exactly:

   - `lem-zero-face-vertex-support`
   - `lem-disjointness-huddle-reduction`
   - `lem-disjoint-hulls-forced-alpha`

   The prover's hypothesis summaries match the authoritative contracts:

   - `lem-zero-face-vertex-support` contract begins:
     `contract: Zero-face vertex support: for an exact signed idempotent P, a hidden geometrically distinct row vertex u, and an optimal exposer h* at u, every zero-face row decomposes convexly onto geometrically distinct row vertices with h* = 0, each rho-near u; ...`
     It does not state `t*(u)>0`, but hiddenness plus the corrected positive-margin argument supplies it.

   - `lem-disjointness-huddle-reduction` contract begins:
     `contract: Disjointness huddle reduction: for an exact signed idempotent P with delta(P) > 0 and nonempty visible set, a hidden top vertex v of height H > 8*tau, and a geometrically distinct row vertex u with ||p_u - p_v||_1 < 4*tau and t*(u) > 0: ...`
     The prover's summary is contract-exact on the needed hypotheses.

   - `lem-disjoint-hulls-forced-alpha` contract begins:
     `contract: Disjoint hulls force alpha: for an exact signed idempotent P and a hidden geometrically distinct row vertex u with t*(u) > 0 whose always-tight hulls K_T = conv{p_f - p_u : f in T} and K_O = t*(u)*conv{p_i - p_u : i in O} are disjoint, ...`
     The prover's summary is contract-exact on the needed hypotheses.

   All three consumers are `status: proved`. The secondary shards touched while checking the consumer proof stack (`lem-separator-zero-face-obstruction`, `lem-ball-cluster-exposure-void`, `lem-always-tight-dual-support`, and `lem-optimal-face-conic-reduction`) are also `status: proved`; no illegal proof-input status appeared in this audit.

5. Degenerate cases and invariance checks.

   `F_v` empty: by `def-exposed`, `t*(v)=+infty`; such a vertex is exposed, not hidden, so it is outside the target claim.

   `delta=0`: handled above; hiddenness is impossible. This is the only clone/self-row obstruction to positive margin, because `rho=0` makes the self-row far.

   `t*=0`: possible in abstract LPs and in nonhidden `delta=0` examples, but impossible under the hidden geometrically distinct row-vertex hypotheses with nonempty `F_v`.

   Rank 2/small examples: `I_2` is the sharp counterexample to the overbroad no-`rho>0` slogan, and simultaneously confirms the target theorem is not contradicted because it has no hidden vertices.

   Clone invariance: duplicating rows does not change the convex hull of distinct row points, does not change the separating affine values, and only duplicates identical far constraints. The proof survives clones.

   Dimension freeness: the only exported constants are `4*tau` and `8*tau`; the separation margin `m/M` is configuration-dependent but used only to prove strict positivity, not to export a dimension-dependent numerical bound.

6. GAP check.

   PROVER-ANSWER.md does not declare a formal GAP to be accepted as open. Its proposed registry lemma fills the localization boundary hole exactly when stated with `rho>0` or with the hiddenness hypotheses that imply `rho>0`; without that qualifier it is false by the `P=I_2`, `delta=0`, `rho=0` counterexample above.
