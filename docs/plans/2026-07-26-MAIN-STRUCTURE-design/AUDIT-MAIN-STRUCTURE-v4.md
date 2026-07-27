# AUDIT-MAIN-STRUCTURE-v4 — fifth-stage fresh hostile audit

**Date:** 2026-07-27  
**Role:** fresh independent hostile auditor  
**Status:** **AUDIT ONLY; NON-RIGOROUS; NO STATUS PROMOTION; DO NOT SEED**

## 1. Final disposition

**DESIGN-REFUTED.**

V4 correctly applies most of the prescribed narrow repair, but the repaired
factoring is still not closed:

1. **NEW correction-induced interface defect:** M19-S2 and M19-S3 no longer
   say that their supplied partition state is the state of the separately
   quantified \(A,w\). The good \(A,w\) to which M04 applies can therefore be
   unrelated to the state defining \(U,V,A_U,A_V,A_R\). V3 had the necessary
   words “a supplied MAIN partition state comes from ... \(w\)”; v4 deleted
   that tie while adding the global hypotheses
   (`DESIGN-MAIN-STRUCTURE-v3.md:251-252`;
   `DESIGN-MAIN-STRUCTURE-v4.md:175-190,385-386`).
2. **Incomplete M13 repair:** M13 promises a closed `def-extcb-datum`, whose
   first field is an extended ambient algebra, but no exact dependency exports
   that \(A_R\) is an extended
   \(\varepsilon_{A_R}\)-\(C^*\)-algebra. The direct producer is
   `lem-compcb-corner-algebra`, and M13 does not import it
   (`definitions/def-extcb-datum.md:13-17`;
   `argument/lemmas/lem-compcb-corner-algebra.md:4-6`;
   `DESIGN-MAIN-STRUCTURE-v4.md:305-307,333`).

These are factoring/interface defects, not counterexamples to Kitaev's route.
No dimension-dependent constant or route-level obstruction was found.
Accordingly the disposition is **DESIGN-REFUTED**, not `ROUTE-ALARM`.

## 2. Binding v3-audit verdicts

| binding item | verdict | exact audit |
|---|---|---|
| Defect A — M19-S1 non-unital domain | **CLEARED** | M19-S1 now quantifies a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra and an extended \(c_0^{\rm cb}\varepsilon\)-inclusion “including its unit clause” (`DESIGN-MAIN-STRUCTURE-v4.md:384`). Thus the v3 \(M_4\) map has \(w(1,1)=e_{11}+e_{22}+e_{33}\ne I_{M_4}\) and fails a stated hypothesis, exactly as required by `AUDIT-MAIN-STRUCTURE-v3.md:23-50`. |
| Defect B — closed M19-S2/S3 and structural domains | **NOT-CLEARED** | The requested global bounds are written, but they are not tied to the partition state whose corners occur in the conclusion (`DESIGN-MAIN-STRUCTURE-v4.md:175-190,385-386`). M25-M27 do retain the required phrase “partition state comes from” the displayed extended inclusion (`ibid.:403-405`); the regression is specifically in S2/S3. |
| Defect C — M19-R M03 eligibility | **CLEARED** | M19-R now assumes \(A_R\) extended and the literal output to be an extended \(d_{\rm raw}\)-inclusion/isomorphism from the named finite-dimensional source before invoking M03 (`ibid.:387`). Those are the literal input types in `argument/lemmas/lem-maincb-error-improvement.md:4`. |
| Defect D — compressed-corner scalar call | **CLEARED** | The raw-call proposal has distinct global/compressed scalar tags (`DESIGN-MAIN-STRUCTURE-v4.md:144-157`); M20 defines \(t_{\rm atom}=K_{\rm call}\varepsilon\) and proves \(\varepsilon_{\{j\}}\le L\varepsilon\le t_{\rm atom}\le r_{\rm reset}\) (`ibid.:388`); M25 imports M04 and uses that call (`ibid.:403,410-433`). |
| V3 exact-dependency defect — direct M07 in M12/M13 | **CLEARED** | M12 and M13 both directly list `lem-maincb-nested-corner-comparison` (`ibid.:332-333`), as prescribed by `AUDIT-MAIN-STRUCTURE-v3.md:138-147`. This does not cure the new, separate M13 ambient-export defect below. |
| P0 schema correction | **CLEARED AT DESIGN-PROPOSAL LEVEL** | All four proposals have complete displayed frontmatter; the cited proposal is limited to TeX 1453-1464; partition state says ambient/\(w\) bounds are consumer-quantified and says two simultaneous unions need two reset states (`DESIGN-MAIN-STRUCTURE-v4.md:55-190`). The ids remain absent from the generated 38-term index (`definitions/INDEX.md:1-43`), so P0 remains a real stop rather than a landed fact. |
| V3 per-row correction package | **NOT-CLEARED** | M03, M04, M11-M12, M19-S1/R, M20, and M25-M27 receive the prescribed text, but M13 lacks an exact producer for a required datum field and M19-S2/S3 lose the identity tie needed to use their new \(A,w\) hypotheses. |

## 3. Two decisive defects

### 3.1 NEW defect: M19-S2/S3 quantify an unrelated good \(A,w\)

`def-maincb-partition-state` contains its own ambient \(A\), supplied map
\(w\), projections, unions, and compressed ambients
(`DESIGN-MAIN-STRUCTURE-v4.md:175-182`). It deliberately stores no ambient
defect or defect/unit tag for that \(w\); a consumer must quantify those
bounds (`ibid.:184-190`).

M19-S2 and M19-S3 instead have this logical shape:

- quantify a good extended ambient \(A\);
- quantify a good extended inclusion \(w:\mathbb C^m\to A\);
- separately quantify “a supplied MAIN partition state” with \(U\), or
  \(U,V\).

They never say that the state's recorded ambient and map equal the displayed
\(A,w\) (`ibid.:385-386`). Hence M04 applies to the displayed good pair, while
\(A_U,A_V,A_R\) may be the corners of another state. The asserted deductions
\(\varepsilon_U,\varepsilon_R\le L\varepsilon\) and
\(\varepsilon_U,\varepsilon_V,\varepsilon_R\le L\varepsilon\) do not follow.
This is not merely omitted prose: v3 S2/S3 explicitly said that the state
“comes from” the displayed \(w\) (`DESIGN-MAIN-STRUCTURE-v3.md:251-252`), and
v4 M12/M13/M25-M27 still use that binding phrase
(`DESIGN-MAIN-STRUCTURE-v4.md:332-333,403-405`).

**Exact correction required:** in M19-S2 and M19-S3 replace the independent
state clause by “a supplied MAIN partition state for this same \(A,w\)” (or
the v3 phrase “comes from” this displayed \(w:\mathbb C^m\to A\)). State that
the supplied reset state(s) refer to the \(U\), respectively \(U,V\), of that
same partition state. Record this identity constraint in the interface/domain
escalation ledger; its current entries mention only separately quantified
bounds and two reset states (`ibid.:574-576,599-601`).

### 3.2 Incomplete repair: M13 has no exact ambient-algebra producer

The actual closed EXT-CB datum begins with an extended
\(\varepsilon\)-\(C^*\)-algebra \(\mathcal A\), and its total error is
\(e=\delta+\varepsilon\) (`definitions/def-extcb-datum.md:13-17`). M13
therefore must export not only its nested projections, complementarity,
dimension, nonzero cross-corner, and map, but also that the target ambient
\(A_R\) is an extended algebra with a quantitative
\(\varepsilon_{A_R}=O(t)\) bound.

M13's exact dependencies are M03, M07-M10, and corner-dimension additivity
(`DESIGN-MAIN-STRUCTURE-v4.md:333`). M07 exports nested projections and two
comparison estimates, not the extended-algebra status of \(A_R\)
(`ibid.:305`). M09 exports the outer-compressed isomorphism, not that ambient
field (`ibid.:307`). Proof-internal dependencies are not exported facts—the
same rule used by the binding v3 audit to require M07 directly
(`AUDIT-MAIN-STRUCTURE-v3.md:138-147`).

The exact landed producer is `lem-compcb-corner-algebra`, whose contract says
that a nonvanishing approximate projection produces an extended compressed
corner with a universal defect bound
(`argument/lemmas/lem-compcb-corner-algebra.md:4-6`). M13 does not directly
import it.

**Exact correction required:** add `lem-compcb-corner-algebra` as a direct M13
dependency; absorb its \(e_{\rm ca}\) threshold and universal corner-algebra
coefficient into \(e_{\rm s2}\) and \(C_{\rm s2}\); and add that dependency
and threshold to the serial landing step and escalation ledger. Merely saying
“in the extended corner \(A_R\)” in the conclusion does not produce a required
input field (`DESIGN-MAIN-STRUCTURE-v4.md:333,532-533,589-594`).

## 4. Verdict per changed row

The v3-to-v4 row-line diff changes exactly M03, M04, M11-M13,
M19-S1/S2/S3/R, M20, and M25-M27. No other M-row line changed.

| changed row | verdict | exact audit |
|---|---|---|
| M03 | **VALID** | Its contract cell is character-for-character equal to `argument/lemmas/lem-maincb-error-improvement.md:4`; only the proposed dependency is rewired to M02 (`DESIGN-MAIN-STRUCTURE-v4.md:291,524-528`). |
| M04 | **VALID** | It now explicitly quantifies a finite-dimensional extended ambient \(A\), closing the v3 self-containment defect (`ibid.:292`; `AUDIT-MAIN-STRUCTURE-v3.md:331-334`). |
| M11 | **VALID** | The original ambient is explicitly extended with \(\varepsilon_A\le t\), which supplies the M08/M10 input (`DESIGN-MAIN-STRUCTURE-v4.md:331`). |
| M12 | **VALID** | It has the original ambient bound, two separate supplied reset states, and direct M07 import (`ibid.:332`). |
| M13 | **VALID-WITH-CORRECTIONS** | The target statement is coherent, but its exact dependency list lacks `lem-compcb-corner-algebra`, so the first `def-extcb-datum` field and the \(\varepsilon_{A_R}\) term are not exported (§3.2). |
| M19-S1 | **VALID, BLOCKED ON G-S1** | The stated unit clause excludes the v3 \(M_4\) counterexample (`ibid.:358-374,384`). |
| M19-S2 | **REFUTED AS WRITTEN** | The good \(A,w\) are not tied to the partition state whose \(A_U,A_R\) are bounded (§3.1). It also consumes corrected M13. |
| M19-S3 | **REFUTED AS WRITTEN** | The same independent-state defect invalidates the claimed M04 bounds for \(A_U,A_V,A_R\) (§3.1). |
| M19-R | **VALID** | Its actual-map, finite-source, extended-ambient hypotheses match M03 literally (`ibid.:387`; `lem-maincb-error-improvement.md:4`). |
| M20 | **VALID-WITH-CORRECTIONS** | Its finite-minimum and \(t_{\rm atom}\) arithmetic are valid, but the row imports the refuted S2/S3 envelopes (`DESIGN-MAIN-STRUCTURE-v4.md:388`). |
| M25 | **VALID-WITH-CORRECTIONS** | Its restored global domain, direct M04 import, atomic base scale, and local invariant are correct (`ibid.:403,410-433`); the induction still consumes invalid M19-S2/M13. |
| M26 | **VALID-WITH-CORRECTIONS** | Its own state is explicitly tied to the restored global \(A,w\), but it consumes invalid M19-S3 (`ibid.:404`). |
| M27 | **VALID-WITH-CORRECTIONS** | The complete-family hypothesis and M26-only edge remain correct, but its sole parent is not yet derived (`ibid.:405`). |

## 5. Retained-row diff and verdicts

The complete row-line comparison found exact retention for the following
rows. “Exact” includes contract, defs, deps, provenance, budget, and audit
annotation, not merely mathematical substance.

| retained row | diff | verdict |
|---|---|---|
| M01 | exact (`v3:155`; `v4:289`) | **VALID**, gated on P0 |
| M02 | exact (`v3:156`; `v4:290`) | **VALID**, gated on P0/M01 |
| M05 | exact (`v3:159`; `v4:293`) | **VALID** |
| M06 | exact (`v3:160`; `v4:294`) | **VALID** |
| M07 | exact (`v3:171`; `v4:305`) | **VALID** with the recorded fixed-telescope gap discipline |
| M08 | exact (`v3:172`; `v4:306`) | **VALID** |
| M09 | exact (`v3:173`; `v4:307`) | **VALID** |
| M10 | exact (`v3:196`; `v4:330`) | **VALID** |
| M14 | exact (`v3:211`; `v4:345`) | **VALID**, gated on operator-space P0 |
| M15 | exact (`v3:212`; `v4:346`) | **VALID** |
| M16 | exact (`v3:213`; `v4:347`) | **VALID**; \(C_{\rm s2}\) is absorbed into \(D_2,e_2\) |
| M17 | exact (`v3:214`; `v4:348`) | **VALID** |
| M18 | exact (`v3:215`; `v4:349`) | **VALID** |
| M21 | exact (`v3:265`; `v4:399`) | **VALID-WITH-CORRECTIONS** upstream |
| M22 | exact (`v3:266`; `v4:400`) | **VALID-WITH-CORRECTIONS** upstream |
| M23 | exact (`v3:267`; `v4:401`) | **VALID**, blocked on G-S1 |
| M24 | exact (`v3:268`; `v4:402`) | **VALID**, blocked on G-S1/M23 |
| M28 | exact (`v3:272`; `v4:406`) | **VALID-WITH-CORRECTIONS**; target contract is valid, subtree is not closed |

No silent retained-row drift was found. In particular the v2 architecture's
M27 complete-family input and M28-only join survive in the changed M27 row and
exact-retained M28 row (`DESIGN-MAIN-STRUCTURE-v2.md:251-254`;
`DESIGN-MAIN-STRUCTURE-v4.md:405-406`).

## 6. Eight v2 requirements and P0/source checks

| v2-audit requirement | verdict in v4 |
|---|---|
| P0 before M01 | **CLEARED:** hard stop and topological step 0 at `DESIGN-MAIN-STRUCTURE-v4.md:55-59,520-523`. |
| Closed call-specific envelopes | **NOT-CLEARED:** M19-S2/S3's restored bounds are attached to an independent \(A,w\), not their partition state (§3.1). |
| \(C_{\rm s2}\) option | **CLEARED:** M13 has \(C_{\rm s2}\ge1\), and M16 absorbs it into \(D_2,e_2\) (`ibid.:333,347,351-356`). |
| Strong reset invariant | **CLEARED AS A ROW:** M19-R proves the local invariant only from an actual eligible raw map (`ibid.:387`); callers remain blocked by S2/S3. |
| Exact dependencies | **NOT-CLEARED GLOBALLY:** the prescribed M05/M07/M09 and M12/M13-direct-M07 imports are present (`ibid.:293,305,307,332-333`), but M13 lacks the exact ambient-corner producer (§3.2). |
| G-S1 hard stop | **CLEARED:** still after M18 and before all M19/structural rows (`ibid.:358-374,537-539`). |
| M27 complete family / M28-only join | **CLEARED IN SHAPE:** `ibid.:405-406,545-547`. |
| Complete escalation ledger | **NOT-CLEARED:** it claims M13 fills every datum field and S2/S3 quantify the needed domain, but omits both defects in §3 (`ibid.:589-601`). |

The four P0 proposals satisfy the frontmatter requirements in
`definitions/README.md:14-56`. The proposed operator-space body at
`DESIGN-MAIN-STRUCTURE-v4.md:80-91` was compared byte-for-byte with
`refs/kitaev-2405.02434/approximate_algebras.tex:1453-1464`; there is no
difference. Its SHA prefix `e7eb512a2ec2438d` agrees with the local payload.
The later rectangular construction at TeX 1467-1475 is correctly excluded
from the cited definition (`DESIGN-MAIN-STRUCTURE-v4.md:94-98`).

M03's contract was likewise compared literally, not semantically: the v4
contract cell at line 291 exactly equals the landed `contract:` value at
`argument/lemmas/lem-maincb-error-improvement.md:4`.

## 7. Landing order, hazards, and scope

The displayed dependency lists are syntactically topologically ordered, and
the M03 validation step, P0, and G-S1 occur at the prescribed positions
(`DESIGN-MAIN-STRUCTURE-v4.md:515-559`). The order is not executable as a
landing plan: step 4 would land M13 without its ambient-algebra producer, and
step 8 would land the underbound M19-S2/S3 interfaces
(`ibid.:532-540`). Steps 12-14 then consume them.

R19's maximal-selection measure, R21's two separate finite inductions, and
R22's two-zero-corner mechanism remain valid in substance
(`ibid.:441-508`; TeX 1363-1369,1414-1444). The new scalar scale and restored
domains use only finite maxima/minima of earlier universal constants
(`DESIGN-MAIN-STRUCTURE-v4.md:388`); no dependence on amplification, matrix
size, class count, block data, or induction length was found.

Nothing here authorizes a definition, contract, dependency, status, or
downstream rewire. The local TeX and landed shards support only the stated
design audit. `op-classical` remains open.
