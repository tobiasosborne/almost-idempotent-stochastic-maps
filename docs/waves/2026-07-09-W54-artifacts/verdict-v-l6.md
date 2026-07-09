VERDICT: VALID-WITH-CORRECTIONS — The load-bearing implication L6.5 => L6-v2 checks out, but L6.3 uses an unsupported nonclone reading of the reduced display contracts and the assembly overstates equivalence/minimality.

1. **L6.1 -- reduced-witness co-top pinning.** Checked the display source, affine pairing, signs, and constants. The proof uses only `status: proved` inputs: `lem-hiddenness-dual-witness`, `lem-always-tight-dual-support`, `lem-optimal-face-conic-reduction`, `lem-top-deficit-price`, and definitions.

   Contract used correctly:
   - `lem-optimal-face-conic-reduction` contract: "the reduced optimal hiddenness dual witnesses are exactly the displays sum over f in T of lambda_f*(p_f - p_u) + sum over z in Z of a_z*(p_z - p_u) = t*(u) * sum over i in O of gamma_i*(p_i - p_u), with lambda and gamma probability vectors supported on T and O and coefficients a_z >= 0 supported on Z (T, O, Z the always-tight families)"
   - Prover usage: apply the linear part of the affine top support functional to exactly that display.

   The identity
   `sum_T lambda_f z_f + sum_Z a_z z_z = t*(v) sum_O gamma_i z_i`
   follows exactly. The bound is also correct: `0 <= z_i <= 2+4*delta`, `gamma` is a probability vector, and hiddenness gives `t*(v) < kappa = tau/4`, so `t*(v)(2+4*delta) < (1/2+delta)tau`. No dimension or clone dependence appears.

2. **L6.2 -- starved-set localization.** Checked the Markov step and the NOT-Q5 bookkeeping. This is valid as written.

   From L6.1,
   `sum_T lambda_f z_f < (1/2+delta)tau`; Markov gives
   `lambda{z_f >= c tau} < (1/2+delta)/c`.
   For `z_f < c tau`, the top support properties imply
   `d_f >= phi(p_f) = H - z_f > H - c tau`.
   At `c=4` and `delta <= 1/4`, the lower bound is strictly greater than
   `1 - (3/4)/4 = 13/16`; the set `d > H-4 tau` is contained in NOT-Q5's `d > H-8 tau`.

   The same Markov argument for `a_z z_z` is legal for non-probability conic mass because the weights are nonnegative. No illegal shard status was used.

3. **L6.3 -- downhill co-top nonclone zero-face conic mass.** The forced mass and downhill inequality are valid, but the stated proof of the `nonclone` mass-location clause uses a stronger fact than any cited contract states.

   Contract versus usage:
   - `lem-always-tight-dual-support` contract: "every optimal hiddenness dual witness (lambda, alpha, beta), after deleting redundant centered-zero constraints, has supp(lambda) contained in T, supp(beta) contained in O, and supp(alpha) contained in Z"
   - `lem-optimal-face-conic-reduction` contract: "coefficients a_z >= 0 supported on Z"
   - Prover usage in P0: "The deleted 'centered-zero' constraints are the rows geometrically coincident with p_v ... so every z in Z appearing in (DISP) has p_z != p_v: the a-carriers are nonclone."

   The contract lines do not say that every `Z` carrier in a reduced display is nonclone, nor that all geometrically coincident rows have been removed from `Z`. This is daylight in exactly the place L6.3 needs clone-invariance.

   Required correction: either delete `nonclone` from L6.3's quantitative location clause, or prove it without the unsupported P0 sentence. A repair is available: first prove the displayed downhill inequality. Since `lem-zero-face-localization` gives `||p_z-p_v||_1 < 4 tau` for all zero-face carriers, while clones have `ell(p_z-p_v)=0`, the inequality `sum_Z a_z ell(p_z-p_v) <= -g` forces more than `g/(4 tau)` conic mass on nonclone carriers with negative `ell`-displacement. Combining that with L6.2's bad-depth bound recovers the advertised co-top nonclone mass lower bound, with the proof order changed.

   Other L6.3 checks pass: `lem-disjoint-hulls-forced-alpha` contract exactly gives `sum a_z > dist_1(K_T,K_O)/(4*tau)`, and the separator arithmetic gives `sum_Z a_z ell(p_z-p_v) <= -g` with no dimension-dependent counting.

4. **L6.4 -- bounded-oscillation psi normalization and corner trap.** The arithmetic is valid and no step divides by `t*(v)` in a constant, but the statement/proof must pin the exposer to the shard's hypothesis.

   Contract versus usage:
   - `lem-separator-zero-face-obstruction` contract: "for the exposedness LP at a hidden geometrically distinct row vertex u ... a relative-interior optimal exposer h*, and nonempty always-tight far/upper families T, O: if ... then for every strict linear separator ell and every m with ..."
   - Prover usage: "h* an optimal exposer" and "there is a legal parameter pair (ell, m)".

   Required correction: state that `h*` is a relative-interior optimal exposer, or explicitly choose one before invoking the separator shard. With that correction, the rest checks:
   `L_T - t*L_O >= g` makes `(L_O, L_T/t*)` nonempty; the two-case choice of `m` lies in that interval and satisfies `|m| <= 3+4*delta`; the oscillation bound is
   `(2+4*delta)+(3+4*delta)=5+8*delta`; and the maximum-principle estimate
   `sum_j P_rj^+(M-psi_j) <= nu_r osc(psi) <= delta(5+8*delta)`
   is just sign-splitting of `P psi = psi`. The `(z,h*)` Markov bounds are also correct.

5. **L6.5 -- open wall.** I did not verify it as a theorem, per instructions. As a standalone statement it is fully quantified enough to close L6-v2, but it is not "strictly weaker than L6-v2" as written. It drops the NOT-Q4 hypothesis and therefore asks for the far-deep positive-mass lower bound on a larger class of configurations. This is acceptable as a stronger open sub-leaf, but the document should not call it weaker or equivalent without the extra observation that Q4 is automatically false after shrinking `delta_0` via the proved capacity bound.

6. **Assembly claim L6.5 => L6-v2 at u = v.** The forward implication is valid. Given L6.5 with constant `c_*`, choose an L6-v2 mass threshold below it, e.g. `m_6 = c_*/2`; then NOT-Q5 (`sum_A P_vj^+ < m_6`) contradicts L6.5 (`sum_A P_vj^+ >= c_*`). The extra L6-v2 hypotheses NOT-Q4 and `c_r` are unused, so any fixed `c_r in (0,1)` is harmless.

   The re-pinning is legal against `DECOMPOSITION-DELTA.md` G8-v3: G8-v3 reads leaf constants first and then shrinks `c_m`, `c_r`, and `theta_0`; shrinking `c_m` strengthens NOT-Q5, shrinking `theta_0` strengthens heaviness, and shrinking `c_r` strengthens NOT-Q4. L1's charge only needs `c_m > 0`, with `delta_0` adjusted.

   Required correction: delete or weaken the converse/equivalence sentence. L6-v2 plus the proved pieces may imply a version of L6.5 after adding automatic NOT-Q4 and shrinking constants, but L6-v2 alone does not imply the stated L6.5, because L6.5 has no NOT-Q4 hypothesis.

7. **Status, boundary, and invariance audit.** All proof-input shards actually used in L6.1-L6.4 and the assembly have `status: proved`; I found no illegal dependency on `conjecture`, `heuristic`, `numerical`, `proved-mod-audit`, `stated`, or `disproved` as a proof input. Context-only mentions remain context-only.

   Degenerate cases: `W = empty` is excluded; `t*(v)=0` is excluded from the sub-leaves and from L6-v2; the strict `H > 16 tau` boundary is respected; `delta -> 0` does not create a division by `t*`; rank-2 cases appear vacuous or harmless under the stated hypotheses. Clone-invariance is fine except for the L6.3 proof gap above, which must be repaired or the `nonclone` word removed.
