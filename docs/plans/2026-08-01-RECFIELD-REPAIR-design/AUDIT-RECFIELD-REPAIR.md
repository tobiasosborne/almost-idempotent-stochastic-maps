# AUDIT — recorded-field identification repair

**Date:** 2026-08-01

**Role:** fresh independent hostile auditor

**Scope:** design audit only; no registry mutation or status promotion

## Final disposition

**DESIGN-CONFIRMED.** The six proposed contract amendments are ready for user
ratification exactly as written. I found no undischargeable `ENV` hypothesis,
no surviving assertion about a free recorded field, no forced amendment of a
frozen T0 contract or registered external, and no missing local-source fact.
There are no required textual corrections.

The central point is that `ENV` is not demanded of the Stage-1 refinement
loop. It first becomes an invariant when M25 constructs one reset state for
each equivalence class; M26 preserves it at each binary merge; M27 iterates
that exact invariant; and M28 consumes the final state. This is the call chain
implemented by the pinned source's Stage 1 / per-class Stage 2 / successive
Stage 3 structure
(`refs/kitaev-2405.02434/approximate_algebras.tex:1417`,
`refs/kitaev-2405.02434/approximate_algebras.tex:1430-1441`,
`refs/kitaev-2405.02434/approximate_algebras.tex:1443`).

## 1. Countermodel re-check

The old root is genuinely false. Its supplied reset state's
`epsilon_U` is datum-only and has no smallness assertion
(`definitions/def-maincb-reset-state.md:13-26`). The exact `M_2` model records
`epsilon_U=r>0` at global `epsilon=0`, while keeping the map defect and unit
error zero
(`proofs/lem-maincb-stage2-call-envelope/ledger/000051.json:1`); that node and
the amended general countermodel node were independently validated
(`proofs/lem-maincb-stage2-call-envelope/ledger/000067.json:1`,
`proofs/lem-maincb-stage2-call-envelope/ledger/000061.json:1`). The circular
scalar proof was also correctly challenged
(`proofs/lem-maincb-stage2-call-envelope/ledger/000058.json:1`).

The repaired M19-S2 root dissolves this model for the right reason: it assumes
the supplied field satisfies `epsilon_U <= W.L*epsilon`, so the old choice
`epsilon=0`, `epsilon_U=r>0` no longer meets the hypotheses
(`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:85`).
It does not purport to derive that bound from M04. Its `epsilon_R` is a newly
bound raw-call target field, not a field of the incoming state. M19-S3 makes
the same repair for both supplied fields and separately binds its target
field (`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:91`). No repaired row concludes a bound on a
supplied free record.

## 2. Verdicts on the six repaired contracts

| Contract | Verdict | Hostile check |
|---|---|---|
| M19-S2 `lem-maincb-stage2-call-envelope` | **VALID** | `ENV(U)` is a literal antecedent; M04 is used only to type the fresh `A_R` target. From `RI(U)` and `W.K2 >= W.c0_cb*W.L`, both `d_U` and the unit error are at most `t_2`; `W.K2 >= W.L` controls both ambient fields. These are exactly the supplied-field and fresh-target roles distinguished by the countermodel (`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:27-32`, `docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:85`). |
| M19-S3 `lem-maincb-stage3-call-envelope` | **VALID** | Both supplied records carry `ENV`; the target record is fresh. `W.K3 >= W.c0_cb*W.L` sends both `RI/UI` pairs below `t_3`, and `W.K3 >= W.L` sends all three ambient fields below `t_3` (`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:91`). |
| M20 `lem-maincb-structural-domain-ledger` | **VALID** | The amended line is purely scalar and contains no unbound atom, corner, certificate, or reset record. All inequalities follow from the fixed ledger: `K_call` is the maximum containing `L,K1,K2,K3`, and `epsilon_MAIN` contains the corresponding radius quotients (`argument/lemmas/lem-maincb-witness-arithmetic.md:4`; `docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:97`). |
| M25 `lem-maincb-one-class-extension` | **VALID** | The strengthened output is existentially constructed. At the singleton base and after every Stage-2 extension, the proof may record the predetermined M04-supported upper bound for that exact target corner, then apply frozen M19-R to the same target field. The output therefore has `ENV+RI+UI`; no old supplied field is rebound (`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:103`, `docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:120-125`). |
| M26 `lem-maincb-binary-block-merge` | **VALID** | Both inputs must already have `ENV+RI+UI`; repaired M19-S3 discharges M12, M17 constructs the raw isomorphism, and frozen M19-R returns `RI+UI` on the same newly selected target field. The output explicitly returns `ENV`, making recursive use legal (`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:109`). |
| M27 `lem-maincb-stage3-finite-recombination` | **VALID** | Its induction predicate is exactly `ENV+RI+UI`. The base states are M25 outputs, and every binary step is repaired M26, so the final field remains bounded without a class-count or depth factor (`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:115`, `docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:162-175`). |

No contract needs `VALID-WITH-CORRECTIONS`; consequently there is no corrected
replacement text to supply.

## 3. Explicit ENV dischargeability trace

1. **Stage 1 does not consume ENV.** M21 constructs a global
   `W.c0_cb*epsilon` inclusion, M22 selects a maximum-dimensional one, and M23
   contradicts maximality by another global inclusion if an atom is not
   one-dimensional (`argument/lemmas/lem-maincb-initial-reset-inclusion.md:4`,
   `argument/lemmas/lem-maincb-maximal-reset-selection.md:4`,
   `argument/lemmas/lem-maincb-stage1-strict-refinement.md:4`). M23 neither
   supplies nor consumes an `epsilon_U` record. This agrees with the source's
   Stage-1 maximality argument
   (`refs/kitaev-2405.02434/approximate_algebras.tex:1417-1426`).
2. **M25 creates the first local ENV witnesses.** Once M24 makes the atomic
   images one-dimensional, M10 supplies the equivalence classes. For each
   class, M04 uniformly makes every nonempty corner an extended
   `L^0*epsilon`-C*-algebra (`argument/lemmas/lem-maincb-direct-corner-envelope.md:4`).
   Since the selected ledger has `W.L >= L^0`, the constructed target record
   can be fixed at the monotone upper bound `W.L*epsilon`. The singleton raw
   scalar call and every later Stage-2 target are therefore typed before M19-R
   is invoked. Frozen M19-R returns `RI/UI` for that same target field and
   leaves source and target unchanged
   (`argument/lemmas/lem-maincb-reset-invariant-preservation.md:4`). Thus every
   recursive call to repaired M19-S2 receives `ENV(U)` from the preceding
   constructed state; the final M25 state exports `ENV(C)`.
3. **M28's per-class calls are discharged.** M28 invokes M25 separately for
   each equivalence class through its dependency spine
   (`argument/lemmas/lem-maincb-structural-assembly.md:6`). Every resulting
   initial class state therefore satisfies all three clauses expected by
   repaired M27.
4. **M27's binary induction is discharged.** Distinct initial classes are
   disjoint unions sharing no class. Repaired M26 accepts two states satisfying
   `ENV+RI+UI`, applies repaired M19-S3, and emits their union with the identical
   predicate. Any later merge therefore receives `ENV` from the preceding M26
   output, not from an inference about a free record
   (`argument/lemmas/lem-maincb-binary-block-merge.md:6`,
   `argument/lemmas/lem-maincb-stage3-finite-recombination.md:6`).
5. **M28 consumes, rather than invents, the final bound.** M27 gives
   `epsilon_J <= W.L*epsilon` and hence both the final defect and corner-unit
   error at most `W.c0_cb*W.L*epsilon`. The global inclusion contributes the
   remaining `W.c0_cb*epsilon` displacement, and
   `W.K_call >= W.L+1` pays their sum
   (`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:167-173`;
   `argument/lemmas/lem-maincb-witness-arithmetic.md:4`).

This trace covers every registry caller: M25 is the only direct substantive
consumer of M19-S2, and M26 is the only direct substantive consumer of
M19-S3; M18 and M20 bind or compare their universal provider witnesses but do
not supply induction states (`argument/lemmas/lem-maincb-one-class-extension.md:6`,
`argument/lemmas/lem-maincb-binary-block-merge.md:6`,
`argument/lemmas/lem-maincb-reset-constant-ledger.md:4`,
`argument/lemmas/lem-maincb-structural-domain-ledger.md:4`).

## 4. M04 selection and typed-witness law

The proposed move is lawful, with one important reading: it does not choose a
canonical or minimal defect. M04 has already fixed the provider witness
`L^0` and proves the displayed target corner has an extended
`L^0*epsilon` bound (`argument/lemmas/lem-maincb-direct-corner-envelope.md:4`).
After M18 fixes one ledger with `W.L >= L^0`
(`argument/lemmas/lem-maincb-reset-constant-ledger.md:4`), a producing row
records the explicit scalar `W.L*epsilon` for its explicit target corner. The
defining inequalities are monotone when their nonnegative tolerance is
enlarged. This is a target-specific typed field, not an equality between two
anaphoric certificates.

M25 and M26 state both the target corner and the fact that it is an extended
algebra at the selected field before stating `ENV`
(`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:103`,
`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:109`). This meets the repository's two
2026-07-28 lessons: the provider supplies the typed witness, rather than a
same-named conclusion, and repeated notation is not used to unify opaque
binders (`docs/LEARNINGS.md:121-125`, `docs/LEARNINGS.md:151-154`). No definition change is
needed: the reset definition is intentionally a data carrier with no
smallness theorem (`definitions/def-maincb-reset-state.md:22-26`), and the
partition definition intentionally carries geometry only
(`definitions/def-maincb-partition-state.md:22-32`).

## 5. Verdicts on the unchanged unbanked rows

| Contract | Verdict | Free-recorded-field attack |
|---|---|---|
| M12 `lem-maincb-cross-class-merging-datum` | **VALID** | `epsilon_U,epsilon_V,d_U,d_V <= t` and both unit estimates are hypotheses, not conclusions (`argument/lemmas/lem-maincb-cross-class-merging-datum.md:4`). Repaired M19-S3 derives every one from its two `ENV+RI+UI` inputs. |
| M18 `lem-maincb-reset-constant-ledger` | **VALID** | Its map conclusions are expressly conditional on each producer's respective hypotheses; strengthened S2/S3 domains are therefore inherited, not contradicted (`argument/lemmas/lem-maincb-reset-constant-ledger.md:4`). |
| M21 `lem-maincb-initial-reset-inclusion` | **VALID** | Its only `epsilon` is the displayed ambient defect of `A`; M19-R is applied with that same global target field. No local reset field is quantified or inferred (`argument/lemmas/lem-maincb-initial-reset-inclusion.md:4`). |
| M22 `lem-maincb-maximal-reset-selection` | **VALID** | It selects among global inclusions at the displayed ambient parameter and mentions no local recorded field (`argument/lemmas/lem-maincb-maximal-reset-selection.md:4`). |
| M23 `lem-maincb-stage1-strict-refinement` | **VALID** | Both input and output live at the displayed global parameter. It is outside the ENV induction and contains no free local record (`argument/lemmas/lem-maincb-stage1-strict-refinement.md:4`). |
| M24 `lem-maincb-stage1-maximality` | **VALID** | It is a direct maximality consequence over exactly M22's global-map class and contains no reset record (`argument/lemmas/lem-maincb-stage1-maximality.md:4`). |
| M28 `lem-maincb-structural-assembly` | **VALID** | Its conclusion contains no local recorded field. The only local value it uses internally is the M27-produced final field, now exported with ENV; the final unit telescope is paid by `K_call >= L+1` (`argument/lemmas/lem-maincb-structural-assembly.md:4`; `docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:167-173`). |

## 6. Frozen T0 and external-interface check

No repaired contract changes a frozen provider's statement. In particular:

- M19-S2 adds a caller hypothesis before consuming frozen M04 and M13; M04
  still exports only the actual corner bound
  (`argument/lemmas/lem-maincb-direct-corner-envelope.md:4`), and M13 still
  consumes explicit `epsilon_U,d_U <= t`
  (`argument/lemmas/lem-maincb-stage2-extcb-datum.md:4`).
- M25's stronger existential export is obtained by choosing the target field
  before calling frozen M16, then applying frozen M19-R to that same field.
  M16 still supplies its extended raw isomorphism and raw unit estimate
  (`argument/lemmas/lem-maincb-stage2-raw-extension.md:4`); M19-R still
  preserves its explicit target (`argument/lemmas/lem-maincb-reset-invariant-preservation.md:4`).
- M26 uses the existing unit and four-corner bridges without strengthening
  them (`argument/lemmas/lem-maincb-compressed-corner-unit-comparison.md:4`,
  `argument/lemmas/lem-maincb-isomorphism-unit-control.md:4`).
- The only registered ground-truth external explicitly used by this repair
  chain remains M19-R's byte-matched `prop_delta_hominc` unit clause; neither
  its statement nor its registration changes
  (`argument/lemmas/lem-maincb-reset-invariant-preservation.md:28-30`;
  `refs/kitaev-2405.02434/approximate_algebras.tex:1194-1196`).

Thus the fourteen pre-session MAIN T0 rows plus the three bridge rows, M16,
and M19-R remain byte-stable. The repair strengthens only downstream consumer
interfaces or existential exports.

## 7. Source and dimension-freeness check

The recorded SHA256 is exact. The source establishes a single uniform
`epsilon'=O(epsilon)` upper bound for every subset corner
(`refs/kitaev-2405.02434/approximate_algebras.tex:1428`), constructs each class
by a reset after every Stage-2 extension
(`refs/kitaev-2405.02434/approximate_algebras.tex:1430-1441`), and successively
merges the class maps with error reduction after every Stage-3 merge
(`refs/kitaev-2405.02434/approximate_algebras.tex:1443`). It does not define any
project reset-record field. The design says exactly that
(`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:8`) and does not attribute record semantics to the
paper. No claimed ground truth is absent from the cited local source.

The repaired induction carries bounds, not sums: M25 and every M26 step reset
the target record to the same universal upper scale `W.L*epsilon`, while M19-R
returns the same `W.c0_cb` coefficient. Neither M27's induction predicate nor
M28's telescope contains the number of classes, a merge depth, an
amplification index, or a dimension
(`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:160-175`). The
dimension-free claim is therefore preserved.

## 8. Budget and re-seed verdict

**VALID.** The parked M19-S2 workspace currently has exactly the five
validated nodes named by the design: scalar margin `1.1.1`, geometry `1.1.4`,
the conditional M13 application `1.2`, and the negative-evidence nodes
`1.1.2`, `1.1.5.1`. The latter two must remain archived evidence rather than
children of the repaired proof; their validation events are at
`proofs/lem-maincb-stage2-call-envelope/ledger/000061.json:1` and
`proofs/lem-maincb-stage2-call-envelope/ledger/000067.json:1`. Fresh re-seeding is the
correct response because the old root and its scalar child were architected
around the false inference. The proposed caps 10--14 are below the repository
soft cap and are plausible for black-box reuse of the repaired dependencies
(`docs/plans/2026-08-01-RECFIELD-REPAIR-design/DESIGN-RECFIELD-REPAIR.md:127-154`).

## Findings

No genuine defect found. No correction is required before user ratification.
