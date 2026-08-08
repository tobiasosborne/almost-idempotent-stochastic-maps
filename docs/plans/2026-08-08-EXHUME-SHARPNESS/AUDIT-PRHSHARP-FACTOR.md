VERDICT: LAND-WITH-EXACT-CORRECTIONS (verified old/new pairs)

# Hostile audit — factoring of `lem-prh-sharpness`

Date: 2026-08-08
Role: fresh hostile auditor; author of none of the audited artifacts
Scope: `DESIGN-PRHSHARP-FACTOR.md` only

No fatal mathematical, dependency, seeding, or consumer-interface flaw was
found.  Landing is conditional on the one exact budget-wording correction in
finding 5 and on the already-required explicit user ratification.  The
correction changes no contract, dependency, status, proof skeleton, cap, or
external.

1. **PASS — the byte-frozen main contract is byte-identical.**
   `DESIGN-PRHSHARP-FACTOR.md:95-100` reproduces
   `argument/lemmas/lem-prh-sharpness.md:4` exactly, including punctuation,
   spacing, ASCII inequalities, map directions, the semicolon, and the final
   intrinsic-sharpness clause.  A literal shell-string comparison passed; both
   newline-free lines have SHA256
   `3e88fd7684a848e35ef1dca7fdc929d71cf37169c7a19fe010d4352d3db0ad3a`.
   The main skeleton root at `DESIGN-PRHSHARP-FACTOR.md:197` is also exactly
   the contract body after removal of its Markdown node label.  The proposed
   registry delta is confined to the old empty `deps:` line: old
   `argument/lemmas/lem-prh-sharpness.md:6` = `deps:`; new
   `DESIGN-PRHSHARP-FACTOR.md:102-106` =
   `deps: lem-prh-sharpness-family-arithmetic; lem-prh-sharpness-row-coincidence`.

2. **PASS — both sub-lemma contracts are complete, correctly typed, and
   strict/weak safe.**
   The family contract at `DESIGN-PRHSHARP-FACTOR.md:26` binds real
   `lambda`, its domain `0 < lambda < 1/2`, both matrices and dimensions,
   `r,s`, `B`, all summation/max indices, `epsilon_lambda`, and `P_lambda`.
   It explicitly states the induced
   `l-infinity` norm as the maximum row `l1` norm before any consumer uses
   that convention.  The row-coincidence contract at lines 64-66 binds
   `n,F,i,j`, introduces the entries by `F=(f_ab)`, and obtains idempotence,
   nonnegativity, and row sums from `def-stochastic` (line 67).  Its hypotheses
   are exactly `f_ii>0` and `f_ij>0`; it exports equality, not an unearned
   strict estimate.

   The only per-row consequence of the max-row formula is the weak inequality
   recorded at lines 45-48 and used at lines 206-209:
   `||row_i(P)-row_i(F)||_1 <= d`.  Strictness enters separately from
   `d<lambda` and `lambda<1/2`, giving at lines 211-215
   `f_11>=1-lambda-d>1-2*lambda>0`, `f_13>=lambda-d>0`, and finally
   `2*lambda<=2*d<2*lambda`.  I checked every `<`, `>`, `<=`, and `>=` in
   the two new contracts and the slimmed-main skeleton; none repeats the
   run-1 strict-versus-weak error.

3. **PASS — exact matrix arithmetic and row coincidence re-derive, and the
   interfaces export exactly what the main row consumes.**
   From the matrices in `PROOF-W74F-A-PRH.md:404-425`, direct multiplication
   gives

   ```text
   M_lambda A_lambda
     = ((1-lambda^2, lambda^2),
        (lambda^2, 1-lambda^2)),

   A_lambda M_lambda rows
     = (1-lambda, 0, lambda, 0),
       (0, 1-lambda, 0, lambda),
       ((1-lambda)^2, lambda(1-lambda), lambda(1-lambda), lambda^2),
       (lambda(1-lambda), (1-lambda)^2, lambda^2, lambda(1-lambda)).
   ```

   Hence `M_lambda A_lambda-I_2` has two absolute row sums
   `2*lambda^2`, so its max-row norm is exactly `2*lambda^2`, not merely at
   most that value.  Also row 1 minus row 3 is
   `(lambda(1-lambda),-lambda(1-lambda),lambda^2,-lambda^2)`, whose `l1`
   norm is `2*lambda(1-lambda)+2*lambda^2=2*lambda`.  These are precisely
   the contract and skeleton claims at
   `DESIGN-PRHSHARP-FACTOR.md:26,140-152`, and precisely the source formulas
   at `PROOF-W74F-A-PRH.md:426-456`.

   For row coincidence, `PROOF-W74F-A-PRH.md:345-400` and the proposed
   nodes at `DESIGN-PRHSHARP-FACTOR.md:159-190` also re-derive cleanly.
   With `pi=row_i(F)` and `S=supp(pi)`, `pi F=pi`; nonnegative stationarity
   makes `S` transition-closed.  If the condensation graph had an edge, a
   finite backward trace reaches a source component with an outgoing edge.
   No flow enters that component, while stationarity says its mass equals
   itself minus a strictly positive outgoing flow, a contradiction.  Because
   `f_ii=pi_i>0`, `i` lies in `S`; because `f_ir=pi_r>0` for every `r in S`,
   the absence of inter-component edges makes `S` strongly connected.  Every
   row indexed by `S` is then a stationary probability supported on `S`.
   Stationary probabilities have full support, and for two such probabilities
   `p,q`, `c=min_r q_r/p_r` makes `q-cp` nonnegative, stationary, and zero in
   one coordinate.  If nonzero it normalizes to a stationary probability with
   proper closed support, impossible; hence `q=cp`, and total mass gives
   `c=1`.  Since `f_ij>0` puts `j in S`, rows `i,j` coincide.

   There is no interface-projection loss.  The family row exports the map
   types, exact defect, limit, complete `P_lambda` rows, norm convention, and
   exact row-1/row-3 separation consumed at lines 198-220.  The second row
   exports exactly the `n=4,i=1,j=3` implication consumed at lines 211-214;
   the main row needs none of its internal support-graph machinery.

4. **PASS — the dedicated final-clause node is quantified and dischargeable
   from the family facts alone.**
   `DESIGN-PRHSHARP-FACTOR.md:222-235` gives the frozen English clause the
   precise reading

   ```text
   for every C>0, epsilon_0>0, and beta>1/2, there is 0<lambda<1/2
   with epsilon_lambda<epsilon_0 such that every stochastic idempotent F
   has ||A_lambda M_lambda-F|| > C*epsilon_lambda^beta.
   ```

   Every quantifier is bound.  The three entries of the minimum at lines
   228-229 are positive.  The first enforces the family domain, the second
   gives `2*lambda^2<epsilon_0`, and the third, using `2*beta-1>0`, gives
   `C*2^beta*lambda^(2*beta)<lambda`.  The already-proved weak bound
   `distance>=lambda` therefore yields the required strict power-law failure.
   This establishes exactly the stipulated “no uniform exponent
   `beta>1/2`” reading and imports neither `cor-classical-sharpness` nor
   `op-classical`.

5. **EXACT CORRECTION REQUIRED — distinguish the rounded integer lower
   expectations from the unrounded `1.5x` total.**
   The individual budgets at `DESIGN-PRHSHARP-FACTOR.md:50-53,87-90,
   192-193,237-244` are honest: designed counts are `7,6,5`; integer live
   expectations are `11--21`, `9--18`, `8--15`; hard caps are `26,22,18`.
   Thus every `3x` endpoint is strictly below its cap:
   `21<26`, `18<22`, `15<18`, and every cap is at most 26.  The expected
   ranges sum to `28--54`, and the hard caps sum to 66, so the pieces cover
   the observed 28-live/31-total monolith with margin.

   One sentence at lines 240-241 is arithmetically ambiguous: the exact
   unrounded sum is `1.5*(7+6+5)=27`, while 28 is obtained only by rounding
   each target upward (`ceil(10.5)+ceil(9)+ceil(7.5)=11+9+8=28`).  Apply this
   verified old/new pair:

   **OLD**

   > The three 1.5x lower endpoints sum to 28 live nodes, matching the observed
   > 28--31-node monolith rather than the rejected eight-node projection.

   **NEW**

   > Rounding each per-target 1.5x lower endpoint upward gives 11+9+8=28 live
   > nodes (the unrounded total is 27); the summed 28--54 live-expectation range
   > covers the observed 28--31-node monolith with margin rather than using the
   > rejected eight-node projection.

6. **PASS — the seeding packages are exact and the fact census is covered.**
   The family row registers only `def-positive-approximate-retract`
   (`DESIGN-PRHSHARP-FACTOR.md:253-264`); its matrix norm identity and all
   products are proved in-tree.  The coincidence row registers only
   `def-stochastic` (lines 266-278); support closure, condensation, and
   uniqueness are proved in-tree.  The main row retains exactly its two
   existing definitions (lines 280-290).  No undeclared theorem external is
   needed.

   Literal comparison after removing only the required source prefix shows
   E1 at line 299 byte-identical to the family contract at line 26, and E2 at
   line 311 byte-identical to the coincidence contract at line 66.  Both use
   the literal validated-workspace paths
   `proofs/lem-prh-sharpness-family-arithmetic` and
   `proofs/lem-prh-sharpness-row-coincidence`.  The corresponding skeleton
   roots at lines 122 and 159 are also byte-identical to their contracts.

   The W139 census at `DESIGN-EXHUME-SHARPNESS-V2.md:518-544` remains complete
   under this factoring: its facts 1,2,7,15 are internalized by the family
   row; facts 10-13 by the coincidence row; and facts 9,14,15,17,18 plus the
   elementary quantifier logic by the main row.  Fact 13, the only named
   nontrivial textbook theorem, is explicitly reproved by the minimum-ratio
   nodes rather than smuggled in as an external.

7. **PASS — dependencies are acyclic and statuses are honest.**
   Both new shards have empty `deps:`, `status: stated`, and `af: none` at
   `DESIGN-PRHSHARP-FACTOR.md:28-30,68-70`.  The proposed graph is

   ```text
   family-arithmetic ----\
                          > lem-prh-sharpness --> cor-classical-sharpness
   row-coincidence ------/
   ```

   so no cycle is introduced.  The main row remains
   `proved-mod-audit` / `af: seeded` during the deps-only edit
   (`DESIGN-PRHSHARP-FACTOR.md:102-112,334-340`).  Lines 1,14-15,19-20,
   58-60,248-251,326-340 repeatedly flag that adding the two dependencies is
   unauthorized until explicit user ratification.  No design statement
   performs or implies a status promotion.

8. **PASS — the existing consumer remains valid unchanged.**
   `argument/lemmas/cor-classical-sharpness.md:4` consumes only the existential
   witnesses, exact defect, and every-idempotent lower bound in the unchanged
   main contract; its sole dependency remains `deps: lem-prh-sharpness` at
   line 6.  Because the provider's contract and literal workspace path
   `proofs/lem-prh-sharpness` do not change, the consumer external specified at
   `DESIGN-EXHUME-SHARPNESS-V2.md:501-512` remains byte-valid without edits.
   The new helper rows are implementation dependencies of the provider, not
   new consumer imports.  This is stated correctly at
   `DESIGN-PRHSHARP-FACTOR.md:341-343`.

**Landing condition.** Apply only the finding-5 OLD/NEW sentence replacement,
obtain explicit user ratification of the deps-only registry change, and then
follow the bottom-up clean-reseed order at
`DESIGN-PRHSHARP-FACTOR.md:324-348`.  No mathematical redesign is required.
