# AUDIT-M24-NONTRIVIALITY

Status: **HOSTILE DESIGN AUDIT — non-rigorous; no status promotion.**

Date: 2026-08-02  
Role: fresh independent hostile auditor  
Target: `DESIGN-M24-NONTRIVIALITY.md`

## Executive verdict

**Final disposition: DESIGN-CONFIRMED.** The proposed route is mathematically
sound at design level: M04 applies to the exact singleton corner without a
partition-state or near-unit premise, its furnished extended-algebra unit is a
nonzero element at the frozen W-ledger scale, and the resulting lower bound
combines with M23's upper bound to prove the byte-unchanged M24 contract. I found
three non-substantive corrections: distinguish the projection-basis definition
from the standard norm-one consequence, repair the provider's provenance cell,
and sharpen one M24 elevation-guidance bullet. None changes either package row,
adds a dependency, or invalidates T0.

For the forensic citations below, `STUCK` abbreviates
`/tmp/claude-1000/-home-tobiasosborne-Projects-almost-idempotent-stochastic-maps/3dd18513-bf41-437f-80f3-7515872b1529/scratchpad/stuck-lem-maincb-stage1-maximality`.

The local Kitaev payload has SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`,
matching `refs/manifest/checksums.sha256:4`.

## Corrections required before landing

1. At `DESIGN-M24-NONTRIVIALITY.md:131` and in proof node 1.2 at
   `DESIGN-M24-NONTRIVIALITY.md:157`, replace the attribution that
   `def-projection-basis` itself gives norm one by this exact substance:
   **“`def-projection-basis` gives a nonzero self-adjoint idempotent; the
   standard C*-algebra fact that a nonzero projection has norm one gives
   `||e_j||=1`.”** The shard's byte text states the algebraic projection-basis
   relations but not the norm equation (`definitions/def-projection-basis.md:13-17`).
2. Replace the provider's source/provenance cell at
   `DESIGN-M24-NONTRIVIALITY.md:84` and `:115` by:
   **`refs/kitaev-2405.02434/approximate_algebras.tex:407-456,917-929,1054-1065,1067-1084,1477-1479; finite-dimensional linear algebra; M04 dependency provenance inherited from lem-maincb-direct-corner-envelope; 1417-1428 is Stage-1 context only.`**
   The current cell omits the extended-algebra definition at 1477-1479 and
   presents 1367-1368 and 1417-1428 as direct provider support even though the
   former is M04-transitive material and the latter is context.
3. Replace the first bullet at `DESIGN-M24-NONTRIVIALITY.md:323` by:
   **“Make the first child the fixed-W binder/admissibility child: eliminate
   the single M18-supplied W and its already-fixed witness provenance before
   defining the admissible family; choose no new universal constant and
   introduce no fresh witness afterward.”** This is the precise M24
   specialization of its binding first-child rule
   (`argument/lemmas/lem-maincb-stage1-maximality.md:26-36`).

## Deliverable 1 — option verdicts and consumer survey

**Verdict: VALID.**

- The defect record is exact. The original lower-bound inference is rejected at
  `STUCK/ledger/000026.json:1`; the root still lacks `dim S_{P_j}>=1` at
  `STUCK/ledger/000036.json:1`; and weakening the root is rejected as scope
  drift at `STUCK/ledger/000044.json:1`. The design answers these challenges by
  supplying a genuinely new lower-bound import, not by reviving `P_j!=0 =>
  S_{P_j}!=0` or manufacturing a partition state.
- **Option (a): SELECT — CONFIRMED.** M04 has no partition-state, near-unit,
  nonzero-corner, or one-dimensionality hypothesis in its contract
  (`argument/lemmas/lem-maincb-direct-corner-envelope.md:4-6`). Its validated
  same-`(A,w)` bridge explicitly binds `P_U=w(e_U)` and
  `A_U=S^A_{P_U}` without a state
  (`proofs/lem-maincb-direct-corner-envelope/export.md:63-77`).
- **Option (b): REJECTION CONFIRMED.** M10 requires one-dimensional
  projections (`argument/lemmas/lem-maincb-corner-equivalence.md:4`); M25 and
  M19-S3 require one-dimensional atomic images
  (`argument/lemmas/lem-maincb-one-class-extension.md:4`;
  `argument/lemmas/lem-maincb-stage3-call-envelope.md:4`); M26 and M27 repeat
  that literal premise (`argument/lemmas/lem-maincb-binary-block-merge.md:4`;
  `argument/lemmas/lem-maincb-stage3-finite-recombination.md:4`). Moreover the
  partition relation is only accompanied by a class family when it is an
  equivalence (`definitions/def-maincb-partition-state.md:13-20,28-30`), and
  `dim S_{P_j}<=1` does not prove reflexivity. M28 imports M10, M24, M25, and
  M27 (`argument/lemmas/lem-maincb-structural-assembly.md:4-6`).
- **Option (c): REJECTION CONFIRMED.** M18, M22, and M23 are frozen
  `proved/validated` rows (`argument/lemmas/lem-maincb-reset-constant-ledger.md:7-9`;
  `argument/lemmas/lem-maincb-maximal-reset-selection.md:7-9`;
  `argument/lemmas/lem-maincb-stage1-strict-refinement.md:7-9`). An additional
  unchanged-contract dependency exporting the missing fact is option (a), not
  a distinct repair.

## Deliverable 2 — final contract package

**Verdict: VALID-WITH-CORRECTIONS** (provenance correction 2 above only).

### Provider row, clause by clause

| Clause | Verdict | Audit |
|---|---|---|
| Fixed ledger `W` | VALID | M18 is a typed provider and explicitly binds the M04 witnesses before furnishing one `W` (`argument/lemmas/lem-maincb-reset-constant-ledger.md:4-6`). |
| `P_j` is a `W.c0_cb*epsilon`-projection | VALID | Extended inclusion gives linearity, exact star preservation, multiplicative defect, and two-sided norm bounds (`definitions/def-extended-delta-inclusion.md:13-17`); the source projection relations are at `definitions/def-projection-basis.md:13-17`. |
| `abs(||P_j||-1)<=W.c0_cb*epsilon` | VALID | Apply the two-sided norm bounds to the norm-one source projection. Positivity of the defect follows because every W-field is positive (`argument/lemmas/lem-maincb-witness-arithmetic.md:4`). |
| “hence nonvanishing” | VALID | The locked definition names the second alternative as nonvanishing (`definitions/def-delta-projection.md:22-27`). The explicit coefficient-one bound is an `O(delta+epsilon)` bound because both parameters are nonnegative. No separate big-O bridge is missing; the same quantitative interpretation is recorded in the validated M04 export (`proofs/lem-maincb-direct-corner-envelope/export.md:27-37`). |
| `S_{P_j}` contains a nonzero element | VALID | M04 applies to `U={j}` and places an extended `L^0*epsilon`-C*-algebra structure on the exact `S_{P_j}` (`argument/lemmas/lem-maincb-direct-corner-envelope.md:4`; `proofs/lem-maincb-direct-corner-envelope/export.md:39-49,75-85`). An extended algebra includes a unit in that same space (`definitions/def-extended-epsilon-cstar-algebra.md:12-16`). The ledger makes its norm defect strictly below one, as checked under Deliverable 5. |
| `dim S_{P_j}>=1` | VALID | A nonzero element of this exact finite-dimensional vector space gives positive dimension; no isomorphic-copy substitution occurs. |
| No near-unit hypothesis | VALID | Neither the direct atomic-image calculation nor M04 requires `||w(I)-I_A||` (`argument/lemmas/lem-maincb-direct-corner-envelope.md:4`). The broader provider is true, not under-specified. |
| Contract format | VALID | It is one physical ASCII line and contains no fixed numerical value for an existential universal constant (`DESIGN-M24-NONTRIVIALITY.md:69-73`). |

### M24 deps-only amendment

**Verdict: VALID.** The contract in the design is byte-identical to both the
current shard and the ratified v2 row
(`argument/lemmas/lem-maincb-stage1-maximality.md:4`;
`DESIGN-MAINCB-REPAIR-v2.md:197`). Adding the provider to the existing M18/M22/M23
dependency set is sufficient and introduces no cycle. M28's contract is also
byte-identical to the ratified row (`argument/lemmas/lem-maincb-structural-assembly.md:4`;
`DESIGN-MAINCB-REPAIR-v2.md:201`).

## Deliverable 3 — definition layer

**Verdict: VALID-WITH-CORRECTIONS** (correction 1 above).

Zero new definitions is correct. `def-delta-projection` already owns
nonvanishing (`definitions/def-delta-projection.md:2-9,22-27`),
`def-compressed-corner` owns the exact compression range, compressed product,
and unit (`definitions/def-compressed-corner.md:15-38`), and the extended
algebra definition types a multiplication and unit on that operator space
(`definitions/def-extended-epsilon-cstar-algebra.md:12-16`). The only defect is
the over-literal attribution of `||e_j||=1` to the projection-basis shard;
the conclusion is valid by standard C*-algebra theory.

## Deliverable 4 — proof architecture and budgets

**Verdict: VALID.**

The provider tree closes without line 1066. M04's singleton application is
noncircular: it first proves the image projection nonvanishing from the source
norm bounds and then invokes the generic corner-algebra result
(`proofs/lem-maincb-direct-corner-envelope/export.md:27-49`). Its assembly
explicitly removes the hidden partition-state hypothesis
(`proofs/lem-maincb-direct-corner-envelope/export.md:63-85`). The unit then lies
in the exact singleton space, not in an isomorphic substitute.

The rebuilt M24 tree also closes. Its lower child calls the new provider; its
upper child calls M23, whose exact conclusion is an admissible
`C^{m+1}->A` inclusion with the same near-unit threshold
(`argument/lemmas/lem-maincb-stage1-strict-refinement.md:4`). The scratchpad
already validated the fixed-admissibility and upper-bound shapes before the
lower-bound failure (`STUCK/ledger/000016.json:1` and
`STUCK/ledger/000019.json:1`). Targets/caps `6/3/10` and `5/2/9` are plausible
for the stated six-node and five-node decompositions and are below the hard
ceiling.

## Deliverable 5 — dimension-free ledger fit

**Verdict: VALID.** The exact chain is:

1. M18 fixes `L^0,e_env^0` before W and exports
   `W.L>=L^0`, `W.e_env<=e_env^0`
   (`argument/lemmas/lem-maincb-reset-constant-ledger.md:4`).
2. For `0<=epsilon<=W.epsilon_MAIN`, M20 exports
   `epsilon<=W.e_env` and
   `W.L*epsilon<=W.K_call*epsilon<=W.r_reset`
   (`argument/lemmas/lem-maincb-structural-domain-ledger.md:4`). Hence
   `epsilon<=e_env^0` and
   `L^0*epsilon<=W.r_reset`.
3. The arithmetic provider defines `D_*=max{1,D_0,D_1,D_2,D_3}` and makes
   `W.r_reset` a minimum containing
   `[2*(1+K_disp)*D_*]^{-1}`, with every provider witness positive
   (`argument/lemmas/lem-maincb-witness-arithmetic.md:4`). Thus
   `D_*>=1`, `K_disp>0`, and
   `W.r_reset<1/2` (the design's weaker `<=1/2` is valid).
4. M04's extended `L^0*epsilon`-C*-algebra therefore has a unit `I_S` with
   `abs(||I_S||-1)<=L^0*epsilon<1`, by the unit axiom
   (`definitions/def-epsilon-cstar-algebra.md:39-48`). Hence `I_S!=0`.

No `c0>=1` inference is used. All constants are fixed universal witnesses;
the relevant contracts expressly make them independent of dimension,
amplification, block data, class count, and stage index
(`argument/lemmas/lem-maincb-reset-constant-ledger.md:4`;
`argument/lemmas/lem-maincb-witness-arithmetic.md:4`).

## Deliverable 6 — source and provisioning audit

**Verdict: VALID-WITH-CORRECTIONS** (correction 2 above).

The bytes support the mathematical route:

- epsilon-C* and approximate-unit axioms: source `:407-440`;
- homomorphism, star, unit, multiplication, and inclusion norm clauses:
  source `:443-456`;
- delta-projection alternatives and the nonvanishing name: source `:917-929`;
- compression range/product and the corner algebra with compressed unit:
  source `:1054-1065,1077-1082`;
- Stage-1 only rules out `dim S_{P_m}>1`: source `:1417-1428`;
- extended algebra definition: source `:1477-1479`.

The excluded sentence at source `:1066` is exactly the unsupported
`S_P=0` equivalence and is not needed. The provider instead obtains a nonzero
unit from M04 plus the explicit unit norm axiom. The correction is only to make
the package provenance distinguish direct ground truth, transitive M04
provenance, and motivational context.

## Deliverable 7 — no-T0-invalidation and serial order

**Verdict: VALID.**

All neighboring MAIN rows except M24 and M28 are presently
`proved/validated`; M24 and M28 are `stated/seeded`
(`argument/lemmas/lem-maincb-stage1-maximality.md:7-9`;
`argument/lemmas/lem-maincb-structural-assembly.md:7-9`). The design changes no
validated contract, locked definition, validated workspace, or registered
external. Provider-first elevation, then the deps-only clean M24 re-seed, then
M28 is the correct serial order. M28's registered oracle is already present in
`.frontier/portfolio.json:1578-1586`, and its ratified `9/3/13` budget is
unchanged (`argument/lemmas/lem-maincb-structural-assembly.md:20-23`).

## Deliverable 8 — hostile risks and elevation guidance

**Verdict: VALID-WITH-CORRECTIONS** (correction 3 above).

The risk register attacks the right failure classes: exact-corner typing,
possible circularity, big-O vocabulary, same-instance constants, sign/order,
and distinct ledgers/maps (`DESIGN-M24-NONTRIVIALITY.md:332-350`). The design
survives each attack. Its no-pending-sibling and one-W/one-map rules agree with
the shard guidance (`argument/lemmas/lem-maincb-stage1-maximality.md:26-36`) and
with the typed-witness lesson that a provider must furnish the typed witness,
not merely a same-named conclusion (`docs/LEARNINGS.md:121-125,151-155`). The
only correction is to call M24's first child a fixed-W binder rather than a
constant-choice/provider-first child: M24 receives already selected constants
and must not reselect them.

## Package and option disposition

| Item | Verdict |
|---|---|
| Provider contract | **VALID-WITH-CORRECTIONS** — all substantive clauses valid; provenance and one explanatory norm attribution corrected above |
| M24 deps-only amendment | **VALID** — contract byte-unchanged; provider is the missing lower-bound import |
| Option (b) rejection | **CONFIRMED** |
| Option (c) rejection | **CONFIRMED** |

**FINAL DISPOSITION: DESIGN-CONFIRMED.** Apply the three exact editorial and
provenance corrections above, then the package is ready for user ratification.
