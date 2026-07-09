VERDICT: VALID — The proved L4 claim is a direct legal instantiation of the proved affine-exposer row-capacity contract, with the strict small-delta boundary handled correctly.

1. Proved statement attacked: L4 zero-face capacity kill.

   Prover usage: instantiate `lem-affine-exposer-row-capacity` with `i = z`, `h = h*`, `eta = kappa`, and `F = {j : h*(p_j) >= kappa}`.

   Cited shard contract, verbatim:

   > contract: Affine-exposer row capacity: for an exact signed idempotent P, a row index i, an affine functional h with h(p_i) = 0 and 0 <= h(p_j) <= 1 for all rows j, any threshold eta >= 0, and any set F contained in {j : h(p_j) >= eta}: eta * sum over f in F of max(P_if, 0) <= nu_i, where nu_i is the row-i negative mass.

   Contract-versus-usage check: no daylight. `P` is exact signed idempotent by L4's hypotheses. The charged row is `i = z`, and the zero-face hypothesis gives exactly `h*(p_z) = 0`, which is the contract's `h(p_i) = 0`; the lemma does not require `z = u`, does not require `z` to be a vertex, and does not require optimality at `z`. The global box constraint is also present: by `def-exposed`, an admissible exposer for `u` satisfies `0 <= h*(p_j) <= 1` for every row `p_j`. The set condition is tautological for the chosen `F`, and `eta = kappa = sqrt(delta)/4 >= 0` because `delta > 0`.

2. Proof-input status audit.

   The only result shard consumed directly is `lem-affine-exposer-row-capacity`, whose shard status is `proved`. Its own listed dependencies, `lem-row-zero-capacity` and `lem-harmonic-affine-bridge`, also have status `proved`; no conjecture, heuristic, numerical, stated, proved-mod-audit, open, obstruction, or disproved input is used in this L4 proof. The other inputs cited by the prover are locked definitions: `def-exposed`, `def-negative-mass`, `def-visible-set`, and `def-signed-idempotent`.

3. Negative-mass ledger and arithmetic.

   The charged negative mass is the row-`z` quantity `nu_z`, not the mass of `u`. This is exactly what the capacity contract outputs after setting `i = z`:

   `kappa * sum_{j : h*(p_j) >= kappa} max(P_zj, 0) <= nu_z`.

   The Q4/L4 shipping hypothesis gives the lower bound `c_r * kappa <= nu_z`. By `def-negative-mass`,

   `delta(P) := max_i sum_j max(-P_ij, 0)`,

   so `nu_z <= delta(P)` is legitimate for every row `z`. Substituting `kappa = tau/4` and `tau = sqrt(delta)` gives

   `c_r * sqrt(delta) / 4 <= delta`.

   Since the statement assumes `delta > 0`, division by `sqrt(delta)` is legal and yields `c_r/4 <= sqrt(delta)`, hence `delta >= (c_r/4)^2`. Therefore the contradiction is exactly for `0 < delta < (c_r/4)^2`; equality is not killed. For `c_r = 1/2`, this is exactly the strict range `0 < delta < 1/64`.

4. Quantifiers and boundary cases.

   The proof is pointwise in any row `z` satisfying the zero-face and shipping hypotheses. It does not need `W != {}`, any height bound, rank assumptions, a nonzero exposedness margin, or a nonempty far set. The degenerate attacks requested do not break the proved statement as stated:

   - `W` empty: unused by L4 once an admissible `h*` and row `z` are given.
   - `H` at a threshold: unused.
   - `t*(u) = 0`: harmless; capacity uses only `h*(p_z) = 0` and the box constraints.
   - `delta -> 0`: the inequality forbids fixed positive `c_r` shipping below the strict threshold; `delta = 0` is outside the statement.
   - rank 2 or other low rank: unused.
   - clones: duplicated row points have the same affine `h*` value; the argument sums matrix mass over indices and applies rowwise to whichever cloned row index satisfies the displayed hypothesis.

5. Dimension-freeness and clone-invariance.

   No step introduces a constant depending on `n`; the only constants are `4` from `kappa = tau/4` and the external `c_r`. The proof does not count rows or divide by the number of representatives of a geometric point. Clone expansion may change the concrete matrix ledger, but whenever the cloned matrix is again an exact signed idempotent and a row `z` satisfies the same high-slab shipping hypothesis, the same row-capacity contract applies verbatim. Thus the argument itself is clone-invariant.

6. GAP audit.

   `PROVER-ANSWER.md` contains no declared GAP inside the L4 proof. The surrounding W54 decomposition leaves other leaves open, but L4 does not invoke them. The only editorial softness is the phrase "admissible at z": formally, `def-exposed` defines admissibility for a row vertex `u`; here the proof uses only the two explicit conditions `h*(p_z)=0` and `0 <= h*(p_j) <= 1` for all rows. Since the prover spells those out and the capacity shard requires no vertex property of `z`, this is not a mathematical correction.
