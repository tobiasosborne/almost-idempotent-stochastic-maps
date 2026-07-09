VERDICT: VALID-WITH-CORRECTIONS — The proved support-duality/disjunction is valid, but the GAP statements need standalone quantifiers and GAP-1' must not be presented as restoring L3 or as the assembly's needed leaf.

1. Proved statement A, support-dual formula.
   Checked: cited input, status, l1/l-infinity duality, and membership in Phi_v.
   Result: valid.

   Proof input status:
   `lem-top-deficit-price` has `status: proved`.
   The definition shards used are locked definitions, not conjectural proof inputs.

   Contract used:
   `contract: Top-deficit price: for an exact signed idempotent P with delta(P) > 0 and nonempty visible set W(P), a hidden top vertex v of height H, there exists a top support functional phi (affine, phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1), and for ANY such phi, writing a_j = P_vj and z_j = H - phi(p_j) >= 0: for every subset A of row indices, sum over j in A of max(a_j,0)*z_j <= nu_v*(2+4*delta) <= delta*(2+4*delta); consequently for m >= 0, L >= 0, if sum over A of max(a_j,0) >= m and z_j >= L on A then m*L <= delta*(2+4*delta), and for delta <= 1/4, lambda > 0, theta < 1, positive v-row mass >= 1-theta on rows with z_j >= lambda*H forces H <= 3*delta/(lambda*(1-theta)), hence H <= 4*tau whenever delta <= min(1/4, (4*lambda*(1-theta)/3)^2).`

   Prover usage:
   existence of at least one affine phi with `phi(p_v)=H`, `phi<=0` on `C_W`, and l1-Lipschitz constant at most 1.

   There is no stronger-than-contract use here. The proof then uses first-principles l1/l-infinity duality, not a Euclidean norm. If `phi(x)=y.x+b` is 1-Lipschitz for l1, then `||y||_infinity <= 1`; `phi<=0` on `C_W` gives `b <= -h_C(y)`; and `y.p_v-h_C(y) <= dist_1(p_v,C_W)=H`. Hence equality forces `b=-h_C(y)` and `y in Y_v`. Conversely, for `y in Y_v`, `phi_y(x)=y.x-h_C(y)` is affine, has l1-Lipschitz constant at most 1, satisfies `phi_y<=0` on `C_W`, and has `phi_y(p_v)=H`. Thus every constructed functional is genuinely in the top support class Phi_v.

2. Proved statement B, formal disjunction.
   Checked: quantifiers, strict/non-strict boundary, well-definedness of `Cyl_v(epsilon)`, dimension-freeness, and clone-invariance.
   Result: valid.

   With statement A, `Z_v(f)=sup_{y in Y_v} y.(p_v-p_f)`. Since `Y_v` is nonempty and contained in the l-infinity unit ball, the supremum is finite. For each `epsilon>0`, exactly one of `Z_v(f) >= epsilon` and `Z_v(f) < epsilon` holds; the latter is precisely `p_f in Cyl_v(epsilon)`. Equality belongs to the visible horn, so there is no boundary leak.

   No depth-band arithmetic is used in this proof; restricting to `||p_f-p_v||_1 >= 4*tau` and `d_f > H-8*tau` is immediate. The constants `rho=4*tau` and the `8*tau` top band are copied correctly from the target L3 statement.

   Clone check: under the usual weighted clone lift, l1 row distances and support values on row points are preserved after collapsing fiber coordinates; the effective dual coefficient is the fiber-weighted average and still has l-infinity norm at most 1. Thus the cylinder predicate on actual row points is clone-invariant. No constant depends on `n`.

3. The bare l1 geometry obstruction in the prover's "Why this does not prove L3" section.
   Checked: arithmetic and duality.
   Result: valid as a warning, not as a counterexample to L3.

   For `q=(1/4,1/4,1/4,1/4)`,
   `v-q=(H/4,H/4,-H/4,-H/4)` has l1 norm `H`, and
   `f-v=(2*tau,-2*tau,0,0)` has l1 norm `4*tau`. Also
   `f-q=(H/4+2*tau,H/4-2*tau,-H/4,-H/4)`, whose l1 norm is `H` because `H>16*tau`. The unique l1 support vector for `v-q` is `(1,1,-1,-1)`, and it gives `y.(v-f)=0`. This correctly shows that first-principles l1 geometry alone cannot exclude the summit cylinder. It does not attack the exact signed-idempotent L3 because no idempotent realization or visible set is supplied.

4. Phi-membership and the tilt failure flagged in DECOMPOSITION.
   Checked: whether the prover smuggles illegal tilted functionals into Phi_v.
   Result: no illegal tilt is used in the proved statements.

   The only constructed legal functionals are the `phi_y` with `y in Y_v`, and their Phi_v membership is verified in finding 1. The prover's later claim that the naive tilt in `DECOMPOSITION.md` can leave Phi_v is also correct: preserving l1-Lipschitzness is not enough; a legal tilt must keep both `phi(p_v)=H` and `phi<=0` on `C_W`. The support-dual formula correctly identifies legal tilts with staying inside the exposed face `Y_v` of the l-infinity ball.

5. Section 4 claim about L5 and simultaneous visibility.
   Checked: whether pointwise L3 plus averaging would already imply L5.
   Result: the prover is honest; pointwise visibility is insufficient without an additional simultaneous/minimax statement.

   DECOMPOSITION L5 requires one top support functional satisfying a mass-weighted lower bound on a whole set `A`. Pointwise L3 would only give, for each row `f in A`, some possibly different `phi_f`. Averaging the `phi_f` does not preserve the per-row lower bounds. Abstractly, take a compact convex simplex of functionals with nonnegative affine coordinates `z_j`; each coordinate has supremum 1, but for uniform weights the supremum of the weighted sum can be only `1/m`, not a dimension-free fraction of the total mass. Thus the needed "one phi for all of A" is genuinely not supplied by the proved disjunction plus averaging.

6. GAP-1 audit.
   Checked: standalone quantification and whether it fills original L3.
   Result: mathematically the right missing statement, but not standalone as written.

   Required correction: rewrite GAP-1 as:
   "There exist universal `c_3>0` and `delta_0>0` such that for every exact signed idempotent `P` with `0<delta(P)<=delta_0`, nonempty `W(P)`, hidden top vertex `v` of height `H>16*tau`, and every row `f` with `||p_f-p_v||_1>=4*tau` and `dist_1(p_f,C_W)>H-8*tau`, one has `p_f notin Cyl_v(c_3*tau)`."

   With that correction, GAP-1 genuinely restores original L3: statement B says either `Z_v(f)>=c_3*tau` or `p_f in Cyl_v(c_3*tau)`, so excluding the cylinder forces the desired deficit.

7. GAP-1' audit.
   Checked: standalone quantification and whether it restores original L3.
   Result: needs the same standalone quantifier correction, and it does not restore original L3 by itself.

   Required correction: rewrite GAP-1' as an optional residual lemma, not as an L3 replacement:
   "There exist universal `c_3>0`, `r>0`, and `delta_0>0` such that for every exact signed idempotent `P` with `0<delta(P)<=delta_0`, nonempty `W(P)`, hidden top vertex `v` of height `H>16*tau`, and every row `f` with `||p_f-p_v||_1>=4*tau` and `dist_1(p_f,C_W)>H-8*tau`, either `Z_v(f)>=c_3*tau` or `dist_1(p_f,Ax_v)<=r*tau`."

   GAP-1' leaves the alternative `dist_1(p_f,Ax_v)<=r*tau` with no lower bound on `Z_v(f)`. Therefore it is not a replacement for GAP-1 if the goal is the original L3 statement. It is only a refined residual-cylinder/axis statement that would require another lemma absorbing the axis-near rows.

8. Which gap the assembly actually needs.
   Checked: `DECOMPOSITION.md` section 4, especially B2 and L5.
   Result: the assembly as written needs full L3/GAP-1 for the B2 far-actor call, and a stronger distributional/simultaneous statement for L5.

   In B2, the assembly says that if the forced actor `f_u` is also `rho`-far from `v`, then "L3 applies to f=f_u" and delivers `z_{f_u} >= c_3*tau`. GAP-1 is exactly the missing statement that supplies this. GAP-1' would not suffice unless B2/L2 were amended to absorb the axis-near alternative. For L5, even full pointwise L3 is not enough without the separate simultaneous-visibility/minimax upgrade discussed in finding 5.

9. Degenerate cases checked.
   `W empty` is outside the hypotheses. `H=16*tau` is outside the strict `H>16*tau` target. `t*(v)=0` is not used in the proved support-duality/disjunction. Rank-2 cases are vacuous for tall hidden tops under the existing rank-two visibility shard, and in any case do not threaten statements A/B. As `delta -> 0`, statement B remains a tautological disjunction for every positive `epsilon`; no hidden dependence on `n` or clone count appears.
