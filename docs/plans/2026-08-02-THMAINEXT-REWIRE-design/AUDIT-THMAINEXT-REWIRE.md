# Hostile audit: `lem-thmainext-conditional` dependency rewire

Date: 2026-08-02  
Auditor role: fresh independent hostile auditor  
Object audited: `DESIGN-THMAINEXT-REWIRE.md`  
Required brief: `BRIEF-THMAINEXT-REWIRE-AUDIT.md`

## Audit method and scope

I treated the proposed rewire as false until supported by the current repository bytes. I read the audit brief in full, checked the design against the current target shard, the ratified MAIN design, the W74F decomposition/proof/verdict record, all seven proposed dependency shards, their current `af` exports, the typed-witness retractions, and the current linker implementation. I also applied the proposed dependency line to an in-memory parse of the current registry and ran the linker's import, cycle, and status checks without writing the registry. Those checks returned no import, cycle, or status error. This audit does **not** promote `lem-thmainext-conditional`: the current shard remains `status: proved-mod-audit` and `af: none` (`argument/lemmas/lem-thmainext-conditional.md:7-8`).

## 1. Final dependency decision — VALID

The proposed line is byte-for-byte the ratified Step-15 line:

```text
deps: conj-hcb; conj-extcb; lem-hcb-column-hilbert-squared; lem-maincb-error-improvement; lem-maincb-reset-invariant-preservation; lem-maincb-structural-assembly; lem-extcb-four-corner-merge
```

It appears in the ratified MAIN design at `docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md:554` and in the audited design at `docs/plans/2026-08-02-THMAINEXT-REWIRE-design/DESIGN-THMAINEXT-REWIRE.md:13`. A byte comparison of the two extracted lines succeeded. The target currently imports only `conj-hcb; conj-extcb` (`argument/lemmas/lem-thmainext-conditional.md:6`), so the proposal is a genuine dependency expansion and does not disguise a contract or status change. The target contract that must remain byte-identical is at `argument/lemmas/lem-thmainext-conditional.md:4`.

The old ratified transitivity explanation is indeed stale: the v5 prose says M18 is available through M19-R (`docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md:557-560`), but current M19-R imports only M02 and M03 (`argument/lemmas/lem-maincb-reset-invariant-preservation.md:6`). The audited design correctly replaces that rationale with the current path through M28, which directly imports M18 (`argument/lemmas/lem-maincb-structural-assembly.md:6`).

## 2. Coverage against W74F and current contracts — VALID

The W74F decomposition separates the analytic package into the HCB/EXTCB route and its corrected column estimate, then the approximation, improvement, merge, extension, and final MAIN assembly nodes (`docs/plans/2026-07-22-W74F-root-harvest/DECOMP-W74F-ROOT.md:106-119`). Its final MAIN requirement is an extended map into the original ambient algebra with the structural and unit estimates (`docs/plans/2026-07-22-W74F-root-harvest/DECOMP-W74F-ROOT.md:546-589`). Every such input is covered by an exact current contract clause or by the validated closure of one of the seven proposed direct dependencies:

- **Corrected column/Hilbert-square input.** The design's Q1 is a byte-substring of the current contract at `argument/lemmas/lem-hcb-column-hilbert-squared.md:4` and of the validated export root at `proofs/lem-hcb-column-hilbert-squared/export.md:5`. This is the corrected COL input identified in W74F (`docs/plans/2026-07-22-W74F-root-harvest/DECOMP-W74F-ROOT.md:221-262`).
- **HCB input.** Q2 is a byte-substring of `argument/lemmas/conj-hcb.md:4` and `proofs/conj-hcb/export.md:5`. The export proves the conditional inverse estimate and then the uniform conclusion (`proofs/conj-hcb/export.md:89-125`), matching the W74F HCB slot (`docs/plans/2026-07-22-W74F-root-harvest/DECOMP-W74F-ROOT.md:266-331`).
- **EXTCB input.** Q3 is a byte-substring of `argument/lemmas/conj-extcb.md:4` and `proofs/conj-extcb/export.md:5`. The export keeps one map through the scale argument (`proofs/conj-extcb/export.md:101`, `proofs/conj-extcb/export.md:161`, `proofs/conj-extcb/export.md:173`, `proofs/conj-extcb/export.md:209-210`) and closes the merge (`proofs/conj-extcb/export.md:543-545`), so the design does not splice witnesses from different amplitudes.
- **Four-corner merge input.** Q4 is a byte-substring of `argument/lemmas/lem-extcb-four-corner-merge.md:4` and `proofs/lem-extcb-four-corner-merge/export.md:5`. The validated conclusion uses the corrected `rho + epsilon` form and explicitly handles the obstruction to the stronger false estimate (`proofs/lem-extcb-four-corner-merge/export.md:279-305`).
- **Improvement/reset inputs.** Q5 and Q6 are byte-substrings of the current contracts at `argument/lemmas/lem-maincb-error-improvement.md:4` and `argument/lemmas/lem-maincb-reset-invariant-preservation.md:4`, and of the export roots at `proofs/lem-maincb-error-improvement/export.md:5` and `proofs/lem-maincb-reset-invariant-preservation/export.md:5`. The former supplies the improved bijective isomorphism (`proofs/lem-maincb-error-improvement/export.md:39-49`, `proofs/lem-maincb-error-improvement/export.md:111-161`); the latter preserves the same map and adds the unit/typing control (`proofs/lem-maincb-reset-invariant-preservation/export.md:27-65`, `proofs/lem-maincb-reset-invariant-preservation/export.md:75-137`).
- **Stage-1 and structural assembly inputs.** Q7 and Q8 are byte-substrings of the single current M28 contract at `argument/lemmas/lem-maincb-structural-assembly.md:4` and its export root at `proofs/lem-maincb-structural-assembly/export.md:5`. M28 directly imports the current Stage-1 maximality row and M18 (`argument/lemmas/lem-maincb-structural-assembly.md:6`); M18 in turn imports the current Stage-1 call envelope, reset invariant, and Stage-2/3 rows (`argument/lemmas/lem-maincb-reset-constant-ledger.md:6`). The Stage-1 envelope expressly packages the three current Stage-1 producers, the literal old-side term, the unit clause, and one common witness (`argument/lemmas/lem-maincb-stage1-call-envelope.md:4-6`). Thus the repaired Stage-1 packet is in M28's current validated closure; it is not being inferred from the superseded W74F prose alone.
- **Final target-shaped map.** M28's export constructs `B` in the required finite-dimensional structural form and uses the same `v` (`proofs/lem-maincb-structural-assembly/export.md:17`, `proofs/lem-maincb-structural-assembly/export.md:41`). It transfers the unit estimate to the original ambient identity (`proofs/lem-maincb-structural-assembly/export.md:183-209`) and supplies finite positive universal witness constants (`proofs/lem-maincb-structural-assembly/export.md:219-233`). These clauses are stronger than, and therefore sufficient for, the unchanged existential target contract at `argument/lemmas/lem-thmainext-conditional.md:4`.

The detailed W74F Stage-1 packet was later corrected: the original proof packet records the split topology and old/fresh-side mechanism (`docs/plans/2026-07-22-W74F-root-harvest/PROOF-H-W74F-STAGE1.md:91-341`), while the hostile verdict identifies the old/fresh defect and records the corrected topology, exact-unit, and fresh-side requirements (`docs/plans/2026-07-22-W74F-root-harvest/VERDICT-H-W74F-STAGE1.md:17-155`). The current Stage-1 closure just cited contains those repaired producers. I found no W74F analytic input that requires an eighth direct dependency.

## 3. Typed witness ledger — VALID

The repository's retractions require one existential witness record to be bound before its fields are projected; separate scalar existentials cannot silently manufacture a typed `W` (`docs/LEARNINGS.md:93-125`, `docs/LEARNINGS.md:127-155`). The design respects that rule. M18 binds one `W` (`argument/lemmas/lem-maincb-reset-constant-ledger.md:4`), and M28 begins by fixing that supplied witness (`argument/lemmas/lem-maincb-structural-assembly.md:4`). Its export retains finite positive universal values for all witness fields (`proofs/lem-maincb-structural-assembly/export.md:219-233`).

The proposed final use is therefore type-correct: choose the target's `C_E` and `epsilon_E` from the already-bound M28 witness, existentially hide `W`, and use M28's map. If M19-R is invoked directly, the design correctly requires the same bound `W`; it does not synthesize a fresh witness from projections. No current contract amendment is needed for this rewire.

## 4. DAG and linker analysis — VALID

The audited design's claimed paths agree with the current dependency bytes:

- M28 -> M25 -> M16 -> `conj-extcb` -> `conj-hcb` -> corrected column row, using `argument/lemmas/lem-maincb-structural-assembly.md:6`, `argument/lemmas/lem-maincb-one-class-extension.md:6`, `argument/lemmas/lem-maincb-stage2-raw-extension.md:6`, `argument/lemmas/conj-extcb.md:6`, and `argument/lemmas/conj-hcb.md:6`.
- M28 -> M20 -> M03, using `argument/lemmas/lem-maincb-structural-assembly.md:6` and `argument/lemmas/lem-maincb-structural-domain-ledger.md:6`.
- M28 -> M25 -> M19-R, using `argument/lemmas/lem-maincb-one-class-extension.md:6`.
- M28 -> M18 -> M17 -> the four-corner merge row, using `argument/lemmas/lem-maincb-reset-constant-ledger.md:6` and `argument/lemmas/lem-maincb-stage3-raw-merge.md:6`.

The design is right that these transitive relationships do not make the seven direct edges invalid. They deliberately expose the complete analytic audit interface on the non-rigorous target while leaving the contract unchanged. The linker's cycle check is the DFS at `scripts/argument.py:153-176`; its availability/status rules are at `scripts/argument.py:197-236`. Applying the proposed line in memory produced no missing import, cycle, or status-propagation error. Every proposed provider is currently a validated T0 row, while the target remains non-rigorous, so the rewire neither treats a conjectural row as available nor promotes the target.

## 5. No-T0-invalidation boundary — VALID-WITH-CORRECTIONS

The substantive boundary is correct. The design changes only the target's `deps:` and provenance, leaves its contract, `status: proved-mod-audit`, and `af: none` unchanged, and does not alter any provider contract or validated workspace (`docs/plans/2026-08-02-THMAINEXT-REWIRE-design/DESIGN-THMAINEXT-REWIRE.md:179-195`). Consequently no T0 export is invalidated and no `af` orchestration is authorized by this landing.

One filesystem description is literally inaccurate. The design calls `proofs/lem-thmainext-conditional/` “presently empty” (`docs/plans/2026-08-02-THMAINEXT-REWIRE-design/DESIGN-THMAINEXT-REWIRE.md:191-195`), but the current path contains five empty scaffold directories. There are still no files and no seeded workspace state, so this does not affect the disposition. Replace that paragraph exactly with:

> `proofs/lem-thmainext-conditional/` exists and contains only the empty scaffold directories `assumptions/`, `defs/`, `lemmas/`, `locks/`, and `nodes/`; it has no files, `meta.json`, ledger, externals, export, or seed to preserve. Leave it untouched. Any later `af` elevation is a separate, explicitly authorized operation.

## 6. Exact landing package — VALID

The landing instructions are minimal and executable: preserve the contract/status/`af` fields, replace only the dependency line and provenance sentence in the authoritative shard, regenerate the generated argument views, and run the gates (`docs/plans/2026-08-02-THMAINEXT-REWIRE-design/DESIGN-THMAINEXT-REWIRE.md:197-216`). The exact dependency text is validated in section 1 above. The proposed provenance accurately describes an approved design audit if this audit's final disposition is used. No definition, provider shard, provider workspace, target workspace, report shard, or status promotion belongs in the landing.

## 7. Risk register — VALID

The register covers the material failure modes exposed by current bytes: typed-witness misuse, the stale M19-R/M18 rationale, redundant-edge confusion, Stage-1 undercoverage, codomain/unit drift, reliance on obsolete W74F prose, status promotion, workspace drift, and stale non-authoritative body prose (`docs/plans/2026-08-02-THMAINEXT-REWIRE-design/DESIGN-THMAINEXT-REWIRE.md:218-256`). In particular, treating current frontmatter and validated exports as authoritative is necessary because some historical shard body prose still describes work as pending; the design explicitly prevents that stale prose from driving the rewire. I found no omitted risk that changes the dependency decision or requires a provider amendment.

## Final disposition — DESIGN-CONFIRMED

The seven-edge rewire is supported by the current contracts and validated exports, covers the corrected W74F analytic inputs including the repaired Stage-1 closure, uses a single typed witness coherently, introduces no cycle or status-propagation failure, and leaves every T0 contract/workspace untouched. The sole correction is a literal description of the unseeded target workspace: it contains empty scaffold directories rather than being directory-empty. That correction is non-semantic and does not alter the exact dependency line, the landing package, or the no-T0-invalidation conclusion.
