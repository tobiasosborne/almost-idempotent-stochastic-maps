# AUDIT-MAIN-STRUCTURE-v2 — fresh hostile re-audit

**Date:** 2026-07-27  
**Role:** fresh independent hostile auditor  
**Status:** **AUDIT ONLY; NON-RIGOROUS; NO STATUS PROMOTION; DO NOT SEED**

## 1. Final disposition

**DESIGN-REFUTED.**

The central mathematical repair is substantially better than the first
repair:

1. M07's two-sided nested-corner comparison is derivable from the named
   compression estimates by a fixed-length telescope.
2. M09 is genuinely different from the landed ideal-unit compression row and
   is the right outer/nested compression shape for Stages 2 and 3.
3. M10--M13 are genuinely conditional and do not consume reset-ledger output.
4. The G-S1 stop is respected: no pre-gate row imports any of the three absent
   Stage-1 producers.
5. M27 correctly takes the complete one-class family as initial data, so the
   two inductions are no longer conflated.

Those successes do not make v2 executable. Two contract-architecture defects
remain.

### Fatal defect A — M19 is not a closed, acyclic producer

M19 quantifies only an ambient \(A\) and a commutative inclusion \(w\), but
then claims bounds for Stage-2 and Stage-3 calls "constructed from \(w\)"
(`DESIGN-MAIN-STRUCTURE-v2.md:228-231`). Those calls also require current
block maps \(v_U\) or \(v_U,v_V\): M12 and M13 state those maps as explicit
hypotheses (`DESIGN-MAIN-STRUCTURE-v2.md:169-172`), while the maps are
produced only later by M25 and M27
(`DESIGN-MAIN-STRUCTURE-v2.md:251-257`). Thus "constructed from \(w\)" has
only two possible readings:

- it hides the later existence/construction of the block maps, which creates
  a semantic M19 \(\to\) M20 \(\to\) M25/M27 \(\to\) M19 cycle; or
- it is meant conditionally, in which case the required current-map
  hypotheses and their defect bounds are absent from the contract.

The scale is also not contractually closed. M13 accepts a current map of
defect \(c_0^{\rm cb}t\) and produces an EXT datum of total defect at most
\(C_{\rm s2}t\) (`DESIGN-MAIN-STRUCTURE-v2.md:172-184`). M16 accepts a datum
whose defects are bounded by its own master error \(t\)
(`DESIGN-MAIN-STRUCTURE-v2.md:194-197`). Applying M16 to M13 therefore uses
master error \(C_{\rm s2}t\), unless a separate stronger invariant supplies a
smaller input scale. M20 checks only
\(K_{\rm call}\varepsilon\le r_{\rm reset}\), not
\(C_{\rm s2}K_{\rm call}\varepsilon\le r_{\rm reset}\)
(`DESIGN-MAIN-STRUCTURE-v2.md:230-235`). Shrinking \(e_2\) cannot turn
\(C_{\rm s2}t\) into \(t\) when no hypothesis says
\(C_{\rm s2}\le1\). M17 explicitly handles the analogous Stage-3 factor
\(\rho\le C_{\rm cross}t\); M16 does not
(`DESIGN-MAIN-STRUCTURE-v2.md:196-204`).

This is a contract defect, not a counterexample to Kitaev's theorem. A third
repair must expose the current reset-map invariant and use separate
call-specific error scales, or revise M16/M20 so every coefficient is
absorbed explicitly.

### Fatal defect B — v2 silently drops the definition-provisioning gate

The first design explicitly required `def-maincb-reset-state`,
`def-maincb-raw-call`, `def-maincb-partition-state`, and
`def-operator-space` before the result rows
(`DESIGN-MAIN-STRUCTURE.md:74-86`). The v4.1 register likewise specified
datum-only reset/raw-call definitions
(`DESIGN-FUDW-DECOMP-v4.1.md:403-428`). None is landed: the complete generated
definition index has 38 entries and contains no `def-maincb-*` or
`def-operator-space` entry (`definitions/INDEX.md:1-42`).

V2 instead says its notation is not a definition shard and introduces
"local master error", "raw call", and "reset map" only in prose
(`DESIGN-MAIN-STRUCTURE-v2.md:45-77`). M15--M20 then use "Stage-1 call",
"Stage-2 EXT call", "Stage-3 four-corner raw call", "local master error", and
"literal ... constructed from \(w\)" inside proposed contracts
(`DESIGN-MAIN-STRUCTURE-v2.md:186-231`). These are project-specific data
packages, not textbook notions. The serial order starts immediately with M01
and never provisions the definitions
(`DESIGN-MAIN-STRUCTURE-v2.md:321-344`), and the escalation ledger omits them
(`DESIGN-MAIN-STRUCTURE-v2.md:370-383`).

Consequently the landing order violates the repository's one-canonical-
definition/no-naked-symbol discipline even before the M19 cycle is reached.

No dimension-dependent constant and no mathematical obstruction to the
source route was found. The disposition is therefore **DESIGN-REFUTED**, not
`ROUTE-ALARM`.

## 2. Ground truth and landed-input audit

The audited source file has SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`,
matching `refs/manifest/checksums.sha256:4`.

Every leaf listed in v2 §2 is present. Their authoritative contracts say:

| leaf group | verdict | exact check |
|---|---|---|
| amplified compression and identities | **VALID** | Exact amplification/range identity and exact idempotence/dagger identity are the contracts at `argument/lemmas/lem-compcb-amplified-compression.md:2-8` and `lem-compcb-amplified-compression-identities.md:2-8`. |
| amplified almost-containment | **VALID** | It is one-sided containment with the exact hypotheses \(\|P_1P-P_1\|,\|Q_1Q-Q_1\|\le\delta\), uniformly amplified (`argument/lemmas/lem-compcb-amplified-almost-containment.md:2-8`). Its proof derives the adjoint-side estimate needed for Hermitian projections (`proofs/lem-compcb-amplified-almost-containment/export.md:27-41`) and the final uniform bound (`ibid.:123-149`). |
| corner algebra and rectangular product | **VALID** | The inherited corner is an extended algebra and the compatible rectangular product is uniformly close to ambient multiplication (`argument/lemmas/lem-compcb-corner-algebra.md:2-8`; `lem-compcb-rectangular-product.md:2-8`). |
| landed single compression | **VALID, BUT IDEAL-UNIT ONLY** | The short registry contract is abstract (`argument/lemmas/lem-compcb-single-compression-transfer.md:2-8`), while the validated setup fixes a direct-summand ideal \(J\), its unit \(q\), \(P=v(q)\), and \(T=\operatorname{Co}_P v|_J\) (`proofs/lem-compcb-single-compression-transfer/export.md:15-29,63-89`). This confirms both halves of v2's claim: the row is valid, and it is not the Stage-2/3 outer transfer. |
| one-dimensional product/dimension/additivity | **VALID** | The three contracts are landed and validated at `argument/lemmas/lem-extcb-one-dimensional-product.md:2-8`, `lem-extcb-one-dimensional-corner-dimension.md:2-8`, and `lem-extcb-corner-dimension-additivity.md:2-8`. The source mechanisms are TeX 1162-1187 and 1363-1369. |
| `conj-extcb` | **VALID** | Its exact input is a closed EXT datum and its output is one amplification-uniform extended isomorphism, with constants independent of rank, amplification, and ambient dimension (`argument/lemmas/conj-extcb.md:2-8,23-40`). |
| four-corner merge | **VALID** | It requires four fixed bijective corner maps and the total smallness guard \(\rho+\varepsilon\le a_{\rm merge}\) (`argument/lemmas/lem-extcb-four-corner-merge.md:2-8,18-26`). |
| exact-target correction | **VALID, BUT DIFFERENT TARGET** | Its codomain is \(B(H)\), not the approximate algebra \(A\) (`argument/lemmas/lem-extcb-exact-target-correction.md:2-8`). |
| `lem-thmainext-conditional` | **LANDED, NON-RIGOROUS CONSUMER** | It requires the final extended \(C_E\varepsilon\)-isomorphism uniformly in amplification (`argument/lemmas/lem-thmainext-conditional.md:2-9,26-30`). Its current direct deps are only `conj-hcb; conj-extcb`, so the future MAIN rewire remains an external action (`ibid.:5-8`). |
| `lem-maincb-error-improvement` | **LANDED STATED TARGET, NOT AN INPUT THEOREM** | The narrowed contract has finite-dimensional source, approximate codomain \(A\), both explicit radii, and bijectivity preservation (`argument/lemmas/lem-maincb-error-improvement.md:2-9`). Its own body explicitly says exact-target correction alone does not prove it (`ibid.:26-31`). |

The source checks agree. The merging lemma gives only an inclusion unless all
four corner maps are bijective (TeX 1325-1350); the direct-sum corollary gives
an inclusion from two diagonal inclusions and adds bijectivity only with the
zero-cross-corner hypothesis (TeX 1352-1359). Stage 1 uses that direct-sum
corollary (TeX 1419-1426), Stage 2 uses outer compression into
\(A_r=S_{P_{[1,r]}}\) (TeX 1430-1441), and Stage 3 starts with all class maps
already constructed (TeX 1443). The tensor extension gives exact
amplification of compression (TeX 1542-1544); the printed unsquared display at
1551-1555 is irrelevant to the MAIN repair.

## 3. Load-bearing comparison and outer compression

### M07 nested-corner comparison — **VALID-WITH-CORRECTIONS**

The two-sided mathematical claim is sound at design level.

For the forward estimate:

1. If \(X\in S^A_{P,Q}\), the subordination hypotheses and amplified
   almost-containment give
   \(\operatorname{Co}^A_R X=X+O(t)\|X\|\). This is exactly the source
   mechanism at TeX 1068-1075 and the landed amplified contract at
   `argument/lemmas/lem-compcb-amplified-almost-containment.md:4-6`.
2. Direct use of the compression comparison at TeX 1054-1064 gives
   \(P^R=\operatorname{Co}_R(P)=P+O(t)\) and similarly for \(Q^R\);
   all four left/right subordination errors in M07 are enough for these two
   estimates (`DESIGN-MAIN-STRUCTURE-v2.md:125-149`).
3. In \(A_R\), the compression \(F^R_{P,Q}\) is close to the two internal
   left/right products. Each internal product is a compressed product in
   \(S_R\), so the landed rectangular estimate replaces it by the ambient
   product with \(O(t)\) error (TeX 1077-1082;
   `argument/lemmas/lem-compcb-rectangular-product.md:4-6`).
4. A fixed number of replacements of \(P^R,Q^R,\operatorname{Co}_R X\) by
   \(P,Q,X\) yields \(P(XQ)+O(t)\|X\|\), and
   \(P(XQ)=X+O(t)\|X\|\) because \(X\) is fixed by the original compression
   (TeX 1059-1064).

For the reverse estimate, \(Y=F^R_{P,Q}Y\) gives
\(Y=P^R\mathbin{\cdot_R}(Y\mathbin{\cdot_R}Q^R)+O(t)\|Y\|\).
The same fixed telescope yields \(Y=P(YQ)+O(t)\|Y\|\), and the ambient
compression comparison gives
\(\operatorname{Co}^A_{P,Q}Y=Y+O(t)\|Y\|\). No growing sum, dimension, class
count, or amplification index occurs. This is genuinely two-sided and is
strong enough for both M08 and the close-range part of M09.

The correction is architectural: M07's future shard must import the exact
amplified compression/identity, almost-containment, and rectangular-product
rows directly and spell out the internal-product telescope. The vague phrase
"landed ... rows" in the design table is not an exact future `deps:` field
(`DESIGN-MAIN-STRUCTURE-v2.md:125-128`). This is not a mathematical
refutation.

### M08 dimension transport — **VALID**

Once \(C_{\rm nest}t<1\), the forward comparison map is injective from the
original corner to the nested corner, and the reverse ambient compression is
injective in the other direction. Finite dimensionality gives equality of
dimensions (`DESIGN-MAIN-STRUCTURE-v2.md:151-153`). This argument does not
misuse the same-space close-idempotent theorem; that theorem's relevant
linear-algebra mechanism is independently visible at
`proofs/lem-extcb1-close-corner-dimension/export.md:123-161`.

### M09 outer-compression transfer — **VALID-WITH-CORRECTIONS**

M09's map
\[
  \operatorname{Co}^{A_R}_{P^R}\operatorname{Co}^A_Rv
\]
is distinct from the landed ideal-unit map. The source's Stage-2 formula is
the first outer compression \(\operatorname{Co}_{P_{[1,r]}}v\)
(TeX 1435-1441); the extra inner compression puts the range exactly in the
nested diagonal corner. M07 with \(P=Q\) gives uniform closeness, M08 gives
the equal finite dimensions needed for surjectivity, and the corner/product
estimates transfer the unit, multiplication, dagger, and norm clauses
(`DESIGN-MAIN-STRUCTURE-v2.md:127-163`).

The exact-amplification claim \(T_n=I_n\otimes T\) uses
`lem-compcb-amplified-compression` twice, once in \(A\) and once in \(A_R\).
That row is not named in M09's displayed deps. It must be a direct dependency,
along with the identities row if idempotence/dagger is used directly. This is
an exact dependency correction, not dead weight and not an underivable
formula.

## 4. Verdict per M-row

`VALID-WITH-CORRECTIONS` below means the mathematical contract can survive
only after the stated exact correction; it is not authorization to land.

| row | verdict | hostile finding |
|---|---|---|
| M01 | **VALID-WITH-CORRECTIONS** | TeX 1239-1311 and 1508-1535 support one common level-one correction and uniform amplified displacement. Provision `def-operator-space`/the matrix-norm vocabulary before landing; v1 already identified this requirement (`DESIGN-MAIN-STRUCTURE.md:74-81`). |
| M02 | **VALID-WITH-CORRECTIONS** | Newton stopping/convergence is supported at TeX 1313 and 1508-1535. It inherits M01's missing definition gate and must keep the cumulative displacement bound explicit. |
| M03 | **VALID-WITH-CORRECTIONS** | The narrowed contract is correct and must remain verbatim (`argument/lemmas/lem-maincb-error-improvement.md:4`). Rewire its logical dependency from exact-target correction to M02; exact-target is only a precedent (`ibid.:21-31`). |
| M04 | **VALID** | Images of norm-one source projections and subset sums have \(O(\varepsilon)\) projection/subordination defects, while the corner-algebra row gives the universal ambient envelope (TeX 1068-1082,1367-1368,1428). |
| M05 | **VALID-WITH-CORRECTIONS** | The inclusion and optional bijectivity clauses match TeX 1325-1359. The future deps must name the amplified compression/product rows rather than say only "landed compression rows." |
| M06 | **VALID** | TeX 1064-1066 says a projection in the close-to-unit alternative has full compression; TeX 1542-1544 transports this exactly to every amplification. |
| M07 | **VALID-WITH-CORRECTIONS** | Both directions follow by the fixed telescope in §3 above. Exact direct deps and the two internal-product expansions must be explicit. |
| M08 | **VALID** | Two injective comparison maps plus finite dimensionality give equality; no false common-space identification is used. |
| M09 | **VALID-WITH-CORRECTIONS** | The formula is the required outer/nested transfer. Add direct amplified-compression/identity deps. |
| M10 | **VALID** | Reflexivity is one-dimensionality, symmetry is dagger, and transitivity is nonzero product followed by the \(\dim\le1\) bound (TeX 1162-1187; landed contracts at `lem-extcb-one-dimensional-product.md:4-6` and `lem-extcb-one-dimensional-corner-dimension.md:4-6`). It is conditional and needs no maximal/reset input. |
| M11 | **VALID-WITH-CORRECTIONS** | Additivity gives both original zero corners (TeX 1363-1369), and M08 transports both to \(A_R\). Its future contract/deps must reference a canonical partition/raw-state definition rather than design-local notation. |
| M12 | **VALID-WITH-CORRECTIONS** | M09 supplies the diagonal maps; M11 supplies both zero nested corners, so the off-diagonal maps are legitimate bijections \(0\to0\). It is genuinely conditional on the given block maps. It still needs canonical raw-call/partition data. |
| M13 | **VALID-WITH-CORRECTIONS** | The five EXT clauses listed at v2 lines 174-184 are derivable from M08/M09, additivity, and exact complementarity in \(A_R\). Its output scale \(C_{\rm s2}t\) must be threaded explicitly into M16/M20. |
| M14 | **VALID** | The scalar-unit map satisfies uniform unit/product/norm estimates from TeX 430-455 and \(\|C\otimes I\|=\|C\|\|I\|\) at 1467-1475; in dimension one it is bijective. |
| M15 | **VALID-WITH-CORRECTIONS** | As a fully conditional two-side statement it follows from M05 and TeX 1419-1426. "Stage-1 call" must be replaced by explicit hypotheses or a ratified raw-call datum. |
| M16 | **VALID-WITH-CORRECTIONS** | `conj-extcb` gives a universal \(D_2\), but M13's \(C_{\rm s2}\) output factor is not absorbed by the present structural ledger. Either M16 must accept `defect <= C_s2*t` as M17 accepts `rho <= C_cross*t`, or M20 must use the enlarged Stage-2 master error. |
| M17 | **VALID** | It explicitly absorbs \(C_{\rm cross}\) and the total merge guard \(\rho+\varepsilon_{A_R}\le a_{\rm merge}\), matching `lem-extcb-four-corner-merge.md:4,18-25`. |
| M18 | **VALID-WITH-CORRECTIONS** | The finite minimum correctly includes both IMPROVE guards and \(\delta_{\max}^{\rm cb}/D_*\). It is valid for a supplied raw call/master error, but requires the missing canonical raw-call definition and does not itself prove that structural calls fit one common \(t\). |
| M19 | **REFUTED** | It omits the current Stage-2/3 block maps, hides later construction in "constructed from \(w\)", and collapses pre-helper and post-helper errors into one self-referential \(K_{\rm call}\varepsilon\) scale. Exact defect A in §1. |
| M20 | **REFUTED** | Its arithmetic is valid conditional on a corrected M19, but the present minimum neither repairs M19's missing state nor explicitly absorbs \(C_{\rm s2}\). |
| M21 | **VALID-WITH-CORRECTIONS** | M14 followed by M03 yields the claimed scalar reset inclusion. Its domain must be rebuilt from a corrected structural ledger; it is not mathematically dependent on G-S1 except through the current invalid M20. |
| M22 | **VALID** | M21 makes the set nonempty; \(c_0^{\rm cb}K_{\rm call}\varepsilon\le1/2\) gives injectivity and hence \(m\le\dim_\mathbb C A\). |
| M23 | **VALID-WITH-CORRECTIONS** | The direct-sum mechanism now correctly uses M15 rather than four bijective corners (TeX 1419-1426), and G-S1 is explicit. It needs a corrected call-domain/state producer in place of M19/M20. |
| M24 | **VALID** | A selected maximum and one strict \(m\mapsto m+1\) refinement give the contradiction; no iterative search for the maximum is assumed. |
| M25 | **REFUTED AS WIRED** | The class induction is mathematically plausible and its EXT clauses are present, but its current dependency path uses invalid M20 and never exposes the stronger current-map invariant needed to make the M13 \(\to\) M16 \(\to\) M18 scale close. A third repair must state that invariant. |
| M26 | **VALID-WITH-CORRECTIONS** | For explicit input block maps, M12 \(\to\) M17 \(\to\) M03 is union-stable and closes with no class-count factor. It still depends on the invalid domain ledger and missing state definitions. |
| M27 | **VALID** | The complete family is explicit initial data; starting at one class and applying M26 decreases \(q-r\) by one. No M25 dependency is needed in this conditional theorem (`DESIGN-MAIN-STRUCTURE-v2.md:252-257,292-299`). |
| M28 | **REFUTED AS WIRED; TARGET CONTRACT VALID** | Its conclusion now exactly matches the consumer, and its join of M25 with M27 is correct in shape. It cannot be derived from the present subtree because M19/M20/M25 are not closed and the definition-provisioning step is absent. |

## 5. Named hazards

### R19 — **VALID**

The actual refinement call site is M23: it changes \(m\) to \(m+1\), so
\(\dim_\mathbb C A-m\) decreases by exactly one
(`DESIGN-MAIN-STRUCTURE-v2.md:247-250,265-283`; source TeX 1419-1426).
V2 correctly does not infer global maximality from arbitrary termination.
M21/M22 first select a maximum from a nonempty bounded subset of
\(\mathbb N\), and M23 contradicts that selected maximum. No circular
maximality premise enters M23.

### R21 — **VALID**

M25 uses the one-class measure \(|C|-r\); M27 uses the cross-class measure
\(q-r\). M27 takes all \(v_C\) as initial data and has no M25 edge; M28 is the
only join (`DESIGN-MAIN-STRUCTURE-v2.md:251-260,285-300,346-348`). This matches
the source ordering at TeX 1430-1443.

### R22 — **VALID-WITH-CORRECTIONS**

M11 first gets
\(S^A_{P_U,P_V}=S^A_{P_V,P_U}=0\) from inequivalence, the one-dimensional
bound, and additivity; it then uses M08 for both nested corners. M12 consumes
those two zero spaces and installs the unique maps \(0\to0\) in the complete
four-corner datum (`DESIGN-MAIN-STRUCTURE-v2.md:169-184`). This clears the
mathematical zero-datum defect.

V2 nevertheless dropped the requested explicit R22 hazard subsection: §4
contains only R19 and R21 (`DESIGN-MAIN-STRUCTURE-v2.md:263-300`). The third
repair should record the M11 \(\to\) M12 production/consumption chain
explicitly and provision its canonical data definitions.

## 6. G-S1 gate

**VALID.** The three absent ids are correctly identified at
`DESIGN-MAIN-STRUCTURE-v2.md:27-33,211-226`. The registry contains none of
them, while `lem-stage1-exact-unit-rectification` alone is already landed
(`argument/lemmas/lem-stage1-exact-unit-rectification.md:2-8`).

No M01--M18 row imports a constant, map, or existence theorem from the three
absent producers. M15 is conditional on supplied old/fresh sides; it does not
produce them. The first actual import is M19, after the gate
(`DESIGN-MAIN-STRUCTURE-v2.md:194-230`), and the serial order stops before M19
(`ibid.:326-337`). The M19 failure is independent of G-S1; closing G-S1 would
not cure it.

## 7. Dimension-freeness

**VALID-WITH-CORRECTIONS; NO ROUTE ALARM.**

No \(n\)-, block-count-, class-count-, or stage-index-dependent stability
constant was found.

- The diagonal has norm one even for finite direct sums (TeX 1239-1254).
- Extended correction uses one level-one map at all amplifications
  (TeX 1508-1535).
- M07 and M09 use fixed-length telescopes, not sums over atoms.
- `conj-extcb` explicitly records independence of rank, amplification, and
  ambient dimension (`argument/lemmas/conj-extcb.md:23-40`).
- Four-corner merge has four fixed corners
  (`argument/lemmas/lem-extcb-four-corner-merge.md:4-6`).
- Dimension and class count bound only the number of immediately-reset finite
  steps.
- Kitaev's convention makes every \(O(\cdot)\) independent of additional data
  (TeX 458), and the final theorem repeats dimension-freeness (TeX 1538-1540).

The M19/M20 problem is not dimension dependence. It is failure to expose and
compose universal coefficients. A corrected finite maximum/minimum can remain
dimension-free once the Stage-2 scale and current-map invariant are named.

## 8. Disposition of every first-audit claim

### Binding audit's four repair failures

| first-audit finding | verdict on v2 §7 claim | reason |
|---|---|---|
| Future constants/cycles in reset architecture | **REFUTED AS CLAIMED CLEARED** | M10--M18 do remove the exact original forward-threshold cycle, but M19 hides later Stage-2/3 block-map production and M20 consumes M19. The displayed serial order is therefore not a genuine topological sort. |
| Missing original-vs-nested comparison | **VALID** | M07 states and supports both comparison directions; M08 uses only those maps. |
| Ideal-unit compression misapplied to outer compression | **VALID-WITH-CORRECTIONS** | M09 has the correct distinct formula. Add the exact amplified-compression deps. |
| Recombination omitted one-class initial family | **VALID** | M27 quantifies the complete family; M28 alone produces it through M25 and supplies it. |

### Five original v4.1 defects

| original defect | verdict on v2 disposition | reason |
|---|---|---|
| Stage 1 used four bijective corner maps | **VALID** | M05/M15 use only the direct-sum inclusion conclusion at TeX 1352-1359. |
| Class-only binary merge was non-iterable | **VALID** | M12/M26 accept disjoint unions of classes, so the output can be used at the next step. |
| Original zero corners were reused in a compressed ambient | **VALID** | M07/M08 transport dimension and M11/M12 produce and consume both nested zero corners. |
| Reset radius omitted exact guards | **REFUTED AS FULLY CLEARED** | M18 now includes both IMPROVE guards and the merge total-defect guard, but the M13 \(C_{\rm s2}\) output scale is not closed through M16/M20. |
| Initial/maximal producers and quantitative conclusion were absent | **VALID-WITH-CORRECTIONS** | M21/M22 and the M28 target contract supply exactly those missing statements. Their current derivation remains blocked by the M19/M20 and definition defects. |

The first audit's five defect findings against v4.1 remain confirmed. V2 does
not rehabilitate v4.1; it requires a smaller third repair.

## 9. Serial landing order and escalation ledger

### Landing order — **REFUTED**

The order is syntactically sorted through M18 and respects G-S1, but it is not
an executable landing order:

1. It has no initial provisioning/ratification step for
   `def-operator-space`, `def-maincb-reset-state`,
   `def-maincb-raw-call`, or the partition/current-union state
   (`DESIGN-MAIN-STRUCTURE-v2.md:321-344` versus
   `DESIGN-MAIN-STRUCTURE.md:74-86`).
2. Step 9 lands M19 before M25/M27 even though M19's "constructed from \(w\)"
   calls require their current block maps.
3. Step 9 then lands M20 with a Stage-2 radius that does not explicitly absorb
   M13's \(C_{\rm s2}\) factor.
4. M25 therefore has no contractually closed invariant/radius with which to
   iterate M13 \(\to\) M16 \(\to\) M18.
5. M09's exact amplified-compression dependency is absent from the listed
   row interface.

Steps 10--15 become meaningful only after these corrections. The G-S1 stop
itself is correctly placed.

### Escalation ledger — **REFUTED AS INCOMPLETE**

V2 escalates all new result contracts and M03's dependency correction
(`DESIGN-MAIN-STRUCTURE-v2.md:370-379`), but omits:

- ratification/provisioning of the four missing definition packages;
- the exact M09 amplified-compression dependency correction;
- replacement of M19 and the corresponding M20/M16 Stage-2 scale correction;
- the future dependency rewire of `lem-thmainext-conditional`, which the
  landing order mentions at step 15 but §8 does not list
  (`DESIGN-MAIN-STRUCTURE-v2.md:343-344,370-383`).

No already-landed mathematical contract needs to be strengthened. M03's
ratified contract remains verbatim; only its deps change. The
`lem-thmainext-conditional` contract also remains verbatim; only its future
deps change.

## 10. Exact requirements for a third repair

A third repair need not discard M07--M13 or the corrected two-induction
architecture. It must:

1. put the datum/notation provisioning and user-ratification gate before M01;
2. replace M19 by closed, call-type-specific conditional envelopes that name
   the current block maps and their reset invariant, without asserting their
   later existence;
3. separate the base geometric scale from the post-M13 EXT-datum scale, then
   either:
   - make M16 accept `datum defect <= C_s2*t` and absorb \(C_{\rm s2}\) in
     \(D_2,e_2\), or
   - put the enlarged Stage-2 master error explicitly into M20's minimum;
4. prove the stronger reset invariant actually used in the M25 induction
   (for example, defect controlled by the current corner's ambient defect),
   instead of hiding it in "constructed from \(w\)";
5. add exact direct deps to M05/M07/M09 rather than category phrases such as
   "landed compression rows";
6. retain G-S1 exactly where it is;
7. retain M27's complete-family hypothesis and the M28-only join; and
8. add the missing R22 and definition/dependency items to the escalation
   ledger.

Nothing in this audit authorizes a definition, contract, dependency, or status
change. Nothing here changes the open/non-rigorous status of the MAIN chain or
`op-classical`.
