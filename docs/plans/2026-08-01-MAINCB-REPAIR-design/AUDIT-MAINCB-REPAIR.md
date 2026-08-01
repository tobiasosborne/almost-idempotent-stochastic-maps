# HOSTILE AUDIT — `DESIGN-MAINCB-REPAIR.md`

**Date:** 2026-08-01

**Auditor role:** fresh independent hostile design auditor

**Epistemic status:** audit only; non-rigorous; no result is promoted
**Final disposition:** **DESIGN-CONFIRMED**, subject to the three exact corrections below before user ratification.

The two analytic bridges are true with universal, amplification-independent constants; the repaired M19-R can retain one literal M02 iterate and prove that same iterate bijective; the new definition is data-only; the repaired graph is acyclic; and no T0 contract or validated external must change. I found three contract/source-typing defects, but each has a local exact correction and none is a route alarm.

## 1. Findings and mandatory exact corrections

### F1 — the isomorphism-unit helper is valid, but its advertised proof route and provenance are false as written

**Severity:** correction required; not a counterexample to the contract.

The design calls the helper an “original surjectivity/lower-bound consequence” (`DESIGN-MAINCB-REPAIR.md:67,181`). Byte-for-byte, however, the pinned source defines a `delta`-homomorphism by the unit clause `||v(I)-I|| <= delta` (`refs/kitaev-2405.02434/approximate_algebras.tex:443-450`), defines a `delta`-inclusion to be such a homomorphism plus norm bounds (`:451-454`), and defines a `delta`-isomorphism to be a bijective `delta`-inclusion (`:455`). The locked project definition preserves that chain (`definitions/def-extended-delta-inclusion.md:13-17`). Thus the proposed contract is immediate at amplification one with `C_iso_unit=1`; surjectivity and the proof at TeX `:1198-1222` are unnecessary. The alternative non-unital theorem suggested by the prose is also true by the proposed range argument, but it is not the contract that was written.

**Exact correction:** replace `DESIGN-MAINCB-REPAIR.md:67` and the provenance phrase in row 181 by:

> By `def-extended-delta-inclusion`, an extended delta-isomorphism is an extended delta-inclusion, hence at amplification one its delta-homomorphism clause gives `||v(I_B)-I_A|| <= delta <= delta+epsilon`. Therefore the displayed contract holds with the universal choice `C_iso_unit=1` (and any positive universal `e_iso_unit`). This row is a modular export of an existing explicit unit clause, not an original surjectivity theorem. A non-unital variant would require a different contract and a separate audit. Provenance: `approximate_algebras.tex:443-455,1477-1484`.

### F2 — M19-S1 identifies maps with different codomains in the `m=1` branch

**Severity:** typed-contract correction required; the analytic estimate is locally recoverable.

The proposed root says `u_1:C^{m+1}->A` and then says that, when `m=1`, `u_1` is “equal to the supplied fresh C^2-inclusion” (`DESIGN-MAINCB-REPAIR.md:187`). The supplied fresh map has codomain `A_fresh=S_{P_fresh}` (`argument/lemmas/lem-stage1-fresh-two-point-inclusion.md:4`), and the parked tree deliberately records target `A_fresh` in this branch (`proofs/lem-maincb-stage1-call-envelope/ledger/000086.json:1`). Equality is therefore ill-typed as written. The existing ingredients do close the intended ambient statement: compose with the canonical subspace embedding, use the amplified compressed-product/ambient-product estimate (`argument/lemmas/lem-compcb-rectangular-product.md:4`; TeX `:1077-1082`), and use the new compressed-unit helper plus `P_fresh=w(I)` and the incoming global unit estimate. This needs an explicit dependency and proof node; M15 alone returns the corner-valued map (`argument/lemmas/lem-maincb-stage1-raw-refinement.md:4`).

**Exact correction:** replace the final phrase of the M19-S1 contract (`DESIGN-MAINCB-REPAIR.md:187`) by:

> when `m=1`, `u_1` is the supplied fresh `C^2->A_fresh=S_{P_fresh}` inclusion followed by the canonical amplified linear embedding `A_fresh->A`; `lem-compcb-rectangular-product`, `lem-maincb-compressed-corner-unit-comparison`, `P_fresh=w(I_C)`, and the displayed incoming unit estimate furnish the asserted `A`-valued inclusion and unit bounds.

Also add the already-validated `lem-compcb-rectangular-product` to M19-S1's deps, replace its budget `10/3/14` by `11/3/14`, and add one ambient-transfer node to the `m=1` re-seed guidance at `DESIGN-MAINCB-REPAIR.md:317-320`. This changes no T0 contract.

### F3 — M20 retains an avoidable definite-description binder for `e_sim,e_full`

**Severity:** typed-witness wording correction required; scalar arithmetic is correct.

M20 says to fix the “compatible `e_sim,e_full` provider witnesses fixed by” M18 (`DESIGN-MAINCB-REPAIR.md:192`). M18 fixes those witnesses as inputs and returns a `W`; it does not make them fields of `W` (`:123,170-171`). The intended same-instance relation is recoverable from M06/M10, M18, and the arithmetic row, but the wording still relies on the kind of opaque definite description forbidden by the brief (`BRIEF-MAINCB-REPAIR.md:109-115`) and the typed-witness law (`docs/LEARNINGS.md:121-125`).

**Exact correction:** replace the opening of M20 by:

> After first fixing a particular universal `e_sim>0` witness furnished by `lem-maincb-corner-equivalence` and a particular universal `e_full>0` witness furnished by `lem-maincb-full-corner-identification`, fix one `def-maincb-witness-ledger` datum `W` whose existence is furnished by `lem-maincb-reset-constant-ledger` instantiated with those same `e_sim,e_full` witnesses; then ...

The remainder of the M20 contract is unchanged. Its deps already contain M06, M10, and M18 (`DESIGN-MAINCB-REPAIR.md:192`).

## 2. Byte-for-byte source audit

The pinned file has SHA256 `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`, exactly matching `refs/manifest/checksums.sha256:4` and `refs/manifest/sources.lock.json:34`.

| Source locus | Byte-level result and design consequence |
|---|---|
| TeX `:430-455` | Matches the approximate-unit axioms and homomorphism/inclusion/isomorphism definitions. It exposes F1: ordinary inclusions already contain the unit clause. |
| TeX `:917-969` | Matches the projection/nontrivial-projection material cited for Stage 1; no dimension-dependent constant is introduced. |
| TeX `:1054-1082` | Matches the symmetric compression, its `O(delta+epsilon)` comparison with left/right multiplication, and `u_P=Co_P(P)`; it supports both clauses of the compressed-unit bridge after rescaling the nested-corner parameters. |
| TeX `:1192-1222` | The proposition and proof match exactly. The third clause requires a prior fixed positive unit-nearness threshold; the design's `a_unit/((1+K_disp)D)` term supplies it. |
| TeX `:1256-1319` | Matches the Newton correction and Corollary `cor_improvement`. The corollary only existentially preserves bijectivity; it does not identify its output with M02's output. The repaired M19-R correctly avoids that identification. |
| TeX `:1325-1359` | Matches the four-corner datum and direct merge. Crucially `merging2` is closeness to `P_j`, not to `Co_{P_j}(P_j)` (`:1333-1336`), exactly the parked M12 defect. |
| TeX `:1363-1412` | Matches corner-dimension additivity and the level-one extension construction. It does not itself export a separate ambient-unit estimate. |
| TeX `:1414-1444` | Matches the three-stage architecture, including outer compression at `:1435-1441` and reset after extension/merge at `:1441-1443`. |
| TeX `:1542-1544` | Matches amplification of projections, compressions, and corner subspaces, with the same level-one maps. |
| TeX `:1557` | Says the error-reduction argument “should be adapted”; it is not a theorem-level external. The design is safe only because M02/M03 are already af-validated and M19-R imports them, rather than treating `:1557` as ground truth. |

The JSON registration at `proofs/lem-stage1-fresh-two-point-inclusion/externals/3404276169020d3b.json:3-4` reproduces TeX `:1194-1196` byte-for-byte, including the non-unital hypothesis and conditional third clause. Reusing that registration without altering the validated workspace is valid (`DESIGN-MAINCB-REPAIR.md:249-256`).

## 3. Hostile attack of the three advertised analytic risks

### 3.1 Isomorphism-unit bridge — **VALID-WITH-CORRECTIONS**

Under the actual contract it is immediate by F1. Even under the stronger intended non-unital reading, for `y=v(x)` multiplicative defect and the approximate source unit give `||v(I_B)y-y|| <= C(delta+epsilon)||x||`; the lower norm transfers this to `C'(delta+epsilon)||y||`, and applying it to `y=I_A` plus the target approximate-unit axiom gives the desired bound. Every coefficient is universal and no dimension or amplification count appears. There is no counterexample, but the source/proof description must be corrected.

### 3.2 Compressed-corner bridge — **VALID**

At amplification `n`, TeX `:1054-1064,1542-1544` compares `Co_{P_n}(P_n)` with `P_n(P_nP_n)` and the projection axiom compares that with `P_n`, giving the first clause uniformly. For M09's map, telescope through `Co_R(v(I)-u_{S_P})`, `Co_R(u_{S_P}-P)`, and `Co^{A_R}_{P^R}(P^R)-P^R`; the nested corner has projection/algebra parameters `C_nest*t` and `O(C_ca*t)`, so the coefficient is enlarged by those fixed universal factors. This directly answers parked challenge `ch-41d...`, which rejected the smaller coefficient (`proofs/lem-maincb-cross-class-merging-datum/ledger/000070.json:1`). The existential `C_corner_unit,e_corner_unit` can absorb both the coefficient and the rescaled threshold. No dimension leak occurs.

### 3.3 M19-R same witness — **VALID**

Use the literal output `v_R` of frozen M02, not M03's existential output. Frozen M02 supplies `||v_R-u_R|| <= K_disp*D*t` and makes this same map an extended `K_floor*epsilon_R`-inclusion (`argument/lemmas/lem-maincb-improvement-iteration.md:4`). If `u_R` is bijective, then
`||v_R x|| >= [1-(1+K_disp)D*t]||x|| >= ||x||/2`
by the last radius term in M19-R (`DESIGN-MAINCB-REPAIR.md:190`); equality of the finite source/target dimensions then makes that same `v_R` bijective. Its preliminary unit distance is at most `(1+K_disp)D*t <= a_unit`, so TeX `:1194-1222` applies to that same map and gives `C_unit(K_floor+1)epsilon_R`. M03 supplies only the universal admissibility/coefficient witnesses. The old anaphor is not relocated.

## 4. Verdict by design section

| Design section | Verdict | Reason |
|---|---|---|
| §1 Unit-clause thread | **VALID-WITH-CORRECTIONS** | Thread is complete and both bridges are true; apply F1 and the `m=1` typing correction F2 (`DESIGN-MAINCB-REPAIR.md:23-76`). |
| §2 Witness definition | **VALID** | Twelve real fields only; the shard explicitly asserts no positivity, relation, existence, or analytic property (`:84-123`), matching `definitions/def-stage1-polar-witness-data.md:13-29`. |
| §3 Binder/arithmetic | **VALID-WITH-CORRECTIONS** | Max/min arithmetic and provider order are sound; apply F3 to the M20 receiver (`:129-170`). |
| §4 Contract table | **VALID-WITH-CORRECTIONS** | Apply F1-F3; all other producer/consumer interfaces match (`:179-202`). |
| §5 Definitions | **VALID** | Exactly one new data definition; all existing definitions remain unchanged (`:204-220`). |
| §6 No-T0 cascade | **VALID** | The 14 frozen contracts at `argument/lemmas/lem-maincb-*.md:4` remain byte-stable; only pending/seeded roots change (`:222-256`). |
| §7 Dimension/arithmetic | **VALID** | All maxima/minima are finite universal operations; RI/UI reset after every call, and `K_call>=L+1` closes the final telescope (`:258-291`). |
| §8 Re-seed guidance | **VALID-WITH-CORRECTIONS** | M12 guidance answers all four parked unit challenges; M19-S1 also needs F2's one ambient-transfer node (`:293-322`). |
| §9 Landing order | **VALID** | The order is topological: helpers/arithmetic, M12, M16/M17, parameterized M19 rows, M18, then consumers (`:324-341`). All caps remain below 26 after F2. |
| §10 Risk register | **VALID-WITH-CORRECTIONS** | The risks close, but F1 changes the characterization of the first bridge and F2 must be listed as the Stage-1 codomain risk (`:343-382`). |

## 5. Verdict per amended/new contract and definition

| Candidate | Verdict | Decisive check |
|---|---|---|
| `lem-maincb-isomorphism-unit-control` | **VALID-WITH-CORRECTIONS** | Contract true; apply F1 to derivation/provenance (`DESIGN-MAINCB-REPAIR.md:181`; TeX `:443-455`). |
| `lem-maincb-compressed-corner-unit-comparison` | **VALID** | Both consumers and all amplifications covered (`:182`; TeX `:1054-1082,1542-1544`). |
| `lem-maincb-witness-arithmetic` | **VALID** | All divisors are fixed positive providers; all fields are assigned (`:163-166,183`). |
| M12 cross-class datum | **VALID** | New hypotheses plus mandatory second helper clause supply `merging2` (`:184`; parked defects at ledger `000041.json:1`, `000063.json:1`, `000070.json:1`, `000091.json:1`). |
| M16 Stage-2 raw extension | **VALID** | `(C_ext+1)C_s2^0*t` is budgeted before the helper (`:185`). |
| M17 Stage-3 raw merge | **VALID** | `[C_merge(C_cross^0+1)+1]t` is budgeted (`:186`). |
| M19-S1 Stage-1 envelope | **VALID-WITH-CORRECTIONS** | Typed `c0` repairs the parked provider defect; apply F2 to the `m=1` codomain (`:187`; ledger `000031.json:1`, `000135.json:1`, `000157.json:1`, `000164.json:1`). |
| M19-S2 Stage-2 envelope | **VALID** | Incoming UI is carried only; `K2` and its absorbed prerequisites make M04/M13 applicable (`:188`). |
| M19-S3 Stage-3 envelope | **VALID** | `K3>=c0_cb*L` forwards both unit bounds exactly to M12 (`:189`). |
| M19-R reset preservation | **VALID** | Same-M02-witness calculation closes; GT registration is exact (`:190`). |
| M18 reset constant ledger | **VALID** | Providers are fixed before the receiving tuple; M19 rows do not depend back on M18 (`:170,191`). |
| M20 structural domain ledger | **VALID-WITH-CORRECTIONS** | Arithmetic correct; apply F3 to bind the same `e_sim,e_full` witnesses explicitly (`:192`). |
| M21 initial reset | **VALID** | M14's literal scalar unit is exact and M19-R supplies RI/UI (`:193`; `argument/lemmas/lem-maincb-initial-raw-inclusion.md:4`). |
| M22 maximal selection | **VALID** | M21 makes the RI+UI class nonempty; M20 gives positive lower norm (`:194`). |
| M23 strict refinement | **VALID** | After F2, its output lies in exactly M22's RI+UI class (`:195`). |
| M24 maximality | **VALID** | Predicate matches M22/M23 byte-for-byte in substance (`:196`). |
| M25 one-class extension | **VALID** | Every Stage-2 raw output is normalized by M19-R; no step count enters the coefficient (`:197`). |
| M26 binary merge | **VALID** | M19-S3 forwards UI to M12, then M17/M19-R return RI/UI (`:198`). |
| M27 finite recombination | **VALID** | Each binary output is reset before reuse; no class-count or depth factor (`:199`). |
| M28 assembly | **VALID** | M06 identifies the full corner and `K_call>=L+1` pays the two unit displacements (`:200,289`). |
| `def-maincb-witness-ledger` | **VALID AS DATA** | Exactly twelve typed real slots; no positivity, relation, witness existence, map, or estimate is smuggled into the definition (`:84-123`). |

## 6. Bridge-row duplicate audit required by the brief

| Bridge row | Truth | Consumer sufficiency | Dimension freedom | Verdict |
|---|---|---|---|---|
| `lem-maincb-isomorphism-unit-control` | True directly from the existing unit clause; the proposed non-unital range proof also closes. | Sufficient for M16 and M17 after their displayed defect-plus-ambient rescalings. | Constants use no rank, block, or amplification count. | **VALID-WITH-CORRECTIONS (F1)** |
| `lem-maincb-compressed-corner-unit-comparison` | True by the compression comparison and a two-compression telescope. | First clause closes M19-S1; second clause exactly matches M09's literal `Co^{A_R}_{P^R} o Co^A_R o v` and closes M12. | TeX `:458,1542-1544` makes the big-O/naturality uniform. | **VALID** |

## 7. Final cascade, budget, and route verdict

No amended row is af-validated, and the additive bridges consume but do not amend frozen M01-M11 or M13-M15 (`DESIGN-MAINCB-REPAIR.md:224-247`). The GT JSON is reused, not edited. The dependency direction is acyclic: parameterized transports feed M18; M18 feeds M20-M28; no transport imports M18 (`:129-142,328-337`). F2 raises only M19-S1's projected live-node count from 10 to 11, below its cap 14 and the repository cap 26. Every coefficient remains a finite expression in universal provider witnesses, with reset after every Stage-2/3 call (`:258-289`). Therefore no T0 invalidation, dimension leak, class-count accumulation, or route-level alarm was found.

**Disposition: DESIGN-CONFIRMED after applying F1-F3 verbatim; then ready for user ratification.**
