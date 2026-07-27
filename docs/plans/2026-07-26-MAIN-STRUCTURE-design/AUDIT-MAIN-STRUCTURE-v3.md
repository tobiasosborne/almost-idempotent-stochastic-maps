# AUDIT-MAIN-STRUCTURE-v3 — fourth-stage fresh hostile audit

**Date:** 2026-07-27  
**Role:** fresh independent hostile auditor  
**Status:** **AUDIT ONLY; NON-RIGOROUS; NO STATUS PROMOTION; DO NOT SEED**

## 1. Final disposition

**DESIGN-REFUTED.**

The central scale repair is sound: `conj-extcb` accepts a closed datum with
total error \(e=\delta+\varepsilon\), so M16 may apply it at
\(e\le C_{\rm s2}t\), take
\(D_2\ge C_{\rm ext}C_{\rm s2}\), and shrink
\(C_{\rm s2}e_2\le e_{\rm ext}\). All of these constants are universal
(`argument/lemmas/conj-extcb.md:4,23-40`;
`DESIGN-MAIN-STRUCTURE-v3.md:90-103,211-221`). The M27 complete-family
hypothesis, M28-only join, R19 measure, G-S1 placement, and absence of a
dimension leak also survive.

The replacement for M19 nevertheless fails four separate closure tests.

### Fatal defect A — M19-S1 is false under its stated non-unital hypothesis

M19-S1 assumes only a **non-unital** reset inclusion \(w\) and concludes that
the Stage-1 pieces satisfy M15 in the original ambient
(`DESIGN-MAIN-STRUCTURE-v3.md:250`). M15 requires target projections
approximately complementary to the target unit
(`ibid.:211-212`; source `approximate_algebras.tex:1352-1358`).

At zero error let
\[
 A=M_4,\qquad
 w:\mathbb C^2\longrightarrow M_4,\qquad
 w(\lambda,\mu)=\lambda(e_{11}+e_{22})+\mu e_{33}.
\]
This is an amplification-isometric non-unital exact \(*\)-homomorphism, hence
a non-unital extended \(0\)-inclusion. Its first atomic image has
\(\dim S_{e_{11}+e_{22}}=4>1\). Splitting it into \(e_{11},e_{22}\) and
retaining the old side \(e_{33}\) gives total target projection
\(e_{11}+e_{22}+e_{33}\ne I_{M_4}\). Thus no \(t_1=0\) Stage-1 datum can
satisfy M15's complementarity hypothesis. Kitaev starts Stage 1 from an
unqualified, hence unit-preserving, inclusion
(`approximate_algebras.tex:1414-1426`); v2 did likewise
(`DESIGN-MAIN-STRUCTURE-v2.md:247-250`).

**Required correction:** M19-S1 must assume that \(A\) is an extended
\(\varepsilon\)-\(C^*\)-algebra and that \(w\) is an extended
\(c_0^{\rm cb}\varepsilon\)-inclusion (unit clause included), or state the
equivalent explicit unit bound. “Non-unital reset inclusion” is not enough.

### Fatal defect B — M19-S2 and M19-S3 are still not closed envelopes

Both rows claim that \(t_i=K_i\varepsilon\) dominates the original and nested
ambient, projection, complementarity, and map defects, but neither assumes:

1. that the original \(A\) has ambient defect at most \(\varepsilon\); or
2. that the partition map \(w\) has defect at most
   \(c_0^{\rm cb}\varepsilon\).

See `DESIGN-MAIN-STRUCTURE-v3.md:251-252`. The proposed partition definition
records a map and geometry but neither defect bound
(`ibid.:64`), while the reset-state definition merely records a number and
explicitly does not impose RI (`ibid.:62`). M04 supplies
\(\varepsilon_U\le L\varepsilon\) and the geometric bounds only under the
missing hypothesis that \(w\) is an extended
\(c_0^{\rm cb}\varepsilon\)-inclusion
(`ibid.:158`). Consequently the displayed inequalities
\[
 d_U\le c_0^{\rm cb}\varepsilon_U
      \le c_0^{\rm cb}L\varepsilon\le K_2\varepsilon
\]
and its two-map Stage-3 analogue cannot even begin from the contracts as
written. Naming \(v_U\) and \(v_V\) repaired the later-map cycle, but it did
not close the base state.

The same omission propagates into M26 and M27, whose hypotheses say only
“non-unital reset inclusion” and give no defect bound for \(w\)
(`ibid.:270-271`). This is also a silent weakening of the v2 M25-M27
hypotheses, which used extended \(c_0^{\rm cb}\varepsilon\)-inclusions
(`DESIGN-MAIN-STRUCTURE-v2.md:251-253`).

**Required correction:** M19-S2/S3 and every structural caller must quantify
\(A\) as an extended \(\varepsilon\)-\(C^*\)-algebra and \(w\) as an
extended \(c_0^{\rm cb}\varepsilon\)-inclusion. Restore the unit-preserving v2
form for the global Stage-1 map unless a broader non-unital theorem is
separately proposed and ratified.

### Fatal defect C — M19-R does not assume an M03-eligible map

M19-R assumes only the two numerical guards
\(d_{\rm raw}\le\delta_{\max}^{\rm cb}\) and
\(\varepsilon_R\le\varepsilon_{\max}^{\rm cb}\)
(`DESIGN-MAIN-STRUCTURE-v3.md:253`). The proposed raw-call definition is
deliberately data-only and contains no success predicate
(`ibid.:63`). Therefore “recorded raw defect” does not assert that the literal
output map is an extended \(d_{\rm raw}\)-inclusion from a
finite-dimensional \(C^*\)-algebra. M18 cannot fill this gap: its contract
applies only to a raw call already satisfying its call-specific
\(\varepsilon_{\rm target}\le t\le r_{\rm reset}\) hypotheses
(`ibid.:215`), none of which appears in M19-R.

M03 actually requires an extended inclusion with finite-dimensional source
(`argument/lemmas/lem-maincb-error-improvement.md:4`). Hence the claimed
derivation and v3 §12's “M19-R proves RI” disposition are not closed.

**Required correction:** M19-R must assume explicitly that its output map is
an extended \(d_{\rm raw}\)-inclusion (or isomorphism) from the named
finite-dimensional source into the extended
\(\varepsilon_R\)-\(C^*\)-algebra \(A_R\), or instead assume the full
conclusion of an M18-admissible call. Then M03 gives RI and preserves
bijectivity.

### Fatal defect D — M20 omits the scalar call at the base of M25

M20 declares that “the scalar call uses \(t_0=\varepsilon\)”
(`DESIGN-MAIN-STRUCTURE-v3.md:254`). That covers M21's scalar map into the
original \(A\), but not M25's base scalar map into
\(A_{\{j_1\}}\). The latter target has only
\(\varepsilon_{\{j_1\}}\le L\varepsilon\), not
\(\varepsilon_{\{j_1\}}\le\varepsilon\), from M04
(`ibid.:158`). M14 requires target ambient defect at most its base scale
(`ibid.:211`).

The M25 proof plan simply says that M18 makes this atomic scalar call
admissible (`ibid.:278-282`). It neither chooses a scale dominating
\(\varepsilon_{\{j_1\}}\) nor imports M04. M19-S2 cannot supply the missing
base estimate, because it requires the very current map that the base step is
trying to construct (`ibid.:251,283-287`). Thus RI is strong enough once a
call has completed, but the induction has no valid base call.

**Required correction:** add the compressed-corner scalar call as a distinct
literal call type. Import M04 directly into M25 and use, for example,
\(t_{\rm atom}=K_{\rm call}\varepsilon\) (or another earlier universal
multiple dominating \(L\varepsilon\)); M20 must explicitly prove
\(\varepsilon_{\{j\}}\le t_{\rm atom}\le r_{\rm reset}\).

### Additional exact-dependency defect — M12/M13 lack the quantitative nested-projection export

M12 and M13 must package \(P_U^R,P_V^R\) or \(P_U^R,P_j^R\) as target
projections with a common quantitative defect. M07 is the row that exports
that fact (`DESIGN-MAIN-STRUCTURE-v3.md:171`). M08 exports only equality of
corner dimensions (`ibid.:172`), and M09 exports an isomorphism into the
nested diagonal corner (`ibid.:173`). Neither M12 nor M13 directly imports
M07 (`ibid.:198-199`). A dependency's proof-internal imports are not exported
facts. Add M07 directly to both rows, or strengthen an intervening contract
explicitly; the former is the smaller correction.

These are defects in the proposed factoring, not a counterexample to Kitaev's
theorem. No route-level obstruction or dimension-dependent constant was
found, so the disposition is **DESIGN-REFUTED**, not `ROUTE-ALARM`.

## 2. P0 definition audit

The generated index really has none of the four ids
(`definitions/INDEX.md:1-43`). The repository schema requires at least
`id`, `term`, `kind`, and `status`; a cited shard also needs a local source
and hash, while an original shard needs a `consensus:` record
(`definitions/README.md:14-30,32-56`;
`scripts/check-defs.py:24-26,88-129`). V3 gives mathematical fields and an
informal kind/status but not an exact shard frontmatter for any proposal
(`DESIGN-MAIN-STRUCTURE-v3.md:49-64`).

| proposal | verdict | exact audit |
|---|---|---|
| `def-operator-space` | **VALID-WITH-CORRECTIONS** | The byte-match candidate is honest only for the square-norm definition: the source defines norms on \(M_n\otimes\mathcal L\), the two axioms, and the self-adjoint variant at `approximate_algebras.tex:1453-1464`. Rectangular norms/inclusions are induced afterward and their isometry/well-definedness is derived at lines 1467-1475. Do not put those consequences into the cited definition as primitive fields. Use the byte-verbatim Definition block, with `source: kitaev-2405.02434`, `locus: approximate_algebras.tex:1453-1464`, and SHA prefix `e7eb512a2ec2438d`; reference the later rectangular construction only in provenance/notation. |
| `def-maincb-reset-state` | **VALID-WITH-CORRECTIONS** | The package is datum-only and RI is correctly excluded (`DESIGN-MAIN-STRUCTURE-v3.md:62,66-70`; v4.1 `DESIGN-FUDW-DECOMP-v4.1.md:419-423`; R17/R35 at lines 589,607). Supply exact schema fields and record user ratification in `consensus:` before changing `draft` to `locked`. Make clear that the inclusion/isomorphism tag is supplied hypothesis data, not a proved existence statement. |
| `def-maincb-raw-call` | **VALID-WITH-CORRECTIONS** | The package is theorem-free as required by v4.1 lines 424-428 and R17/R35. Supply exact schema fields. Its “recorded raw defect” must remain a number/field and must not be read as the theorem that the output is an extended inclusion; result contracts such as corrected M19-R must state that hypothesis. The scalar tag may stay single because the target corner is explicit, but M20 must distinguish its global and compressed-corner scales. |
| `def-maincb-partition-state` | **VALID-WITH-CORRECTIONS** | “When the relation is an equivalence, its class family” is conditional data, not an assertion that equivalence holds (`DESIGN-MAIN-STRUCTURE-v3.md:64`); it does not violate R35. Supply exact schema fields. Also specify whether the package records the global ambient defect and the defect/unit tag of \(w\); if it does not, every result using those bounds must quantify them explicitly. A single “current union” field cannot silently supply simultaneous \(U,V\) states; M12/M19-S3 correctly need two separately supplied reset states. |

P0 therefore exists as a valid design direction, but v3 has not specified four
schema-complete shards, and its cited operator-space field list is not
byte-faithful as written.

## 3. Landed inputs and scale discipline

The pinned TeX has SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`,
matching `refs/manifest/checksums.sha256:4`.

| check | verdict | exact locus |
|---|---|---|
| amplified compression, identities, and almost-containment | **VALID** | Exact amplification/range, idempotence/dagger, and one-sided containment are the contracts at `argument/lemmas/lem-compcb-amplified-compression.md:4-8`, `lem-compcb-amplified-compression-identities.md:4-8`, and `lem-compcb-amplified-almost-containment.md:4-8`; source mechanism at TeX 1054-1075,1542-1544. |
| corner algebra, rectangular product, and ideal-unit single compression | **VALID WITH THE RECORDED SCOPE** | Contracts at `lem-compcb-corner-algebra.md:4-8`, `lem-compcb-rectangular-product.md:4-8`, and `lem-compcb-single-compression-transfer.md:4-8`. The last is restricted to an ideal and is used only in Stage 1, as v3 says at lines 139-142. |
| one-dimensional product/dimension/additivity | **VALID** | Contracts at `lem-extcb-one-dimensional-product.md:4-8`, `lem-extcb-one-dimensional-corner-dimension.md:4-8`, and `lem-extcb-corner-dimension-additivity.md:4-8`; source TeX 1162-1187,1363-1369. |
| `conj-extcb` scale consumption | **VALID** | Its input is \(e=\delta+\varepsilon\le e_{\rm ext}\) and output is \(C_{\rm ext}e\), uniformly in rank/amplification/dimension (`argument/lemmas/conj-extcb.md:4,23-40`). Hence M16's \(C_{\rm s2}\) absorption is legitimate. |
| four-corner total guard | **VALID** | The exact contract requires \(\rho+\varepsilon\le a_{\rm merge}\) (`argument/lemmas/lem-extcb-four-corner-merge.md:4,18-25`); M17 and M18 retain it (`DESIGN-MAIN-STRUCTURE-v3.md:214-215`). |
| M03 and downstream consumer status | **VALID STATUS ACCOUNTING** | M03 remains `stated` (`argument/lemmas/lem-maincb-error-improvement.md:4-9,26-31`); `lem-thmainext-conditional` remains `proved-mod-audit` with the final uniform isomorphism in its contract (`argument/lemmas/lem-thmainext-conditional.md:4-9,26-30`). |

## 4. Verdict per pre-gate row

| row | verdict | exact audit |
|---|---|---|
| M01 | **VALID-WITH-CORRECTIONS** | The norm-one diagonal and one common amplified correction are supported at TeX 1239-1311,1508-1535. It gates on the corrected `def-operator-space` shard (`DESIGN-MAIN-STRUCTURE-v3.md:155`). |
| M02 | **VALID** | The finite-stop/\(\varepsilon=0\) limit and uniform displacement plan match TeX 1313,1508-1535; its sole result dependency M01 is earlier (`DESIGN-MAIN-STRUCTURE-v3.md:156`). |
| M03 | **VALID-WITH-CORRECTIONS** | Rewiring to M02 is correct, but the displayed text is not literally the landed contract: it says “from finite-dimensional \(B\)” instead of “from a finite-dimensional \(C^*\)-algebra \(B\)” (`DESIGN-MAIN-STRUCTURE-v3.md:157`; authoritative text `argument/lemmas/lem-maincb-error-improvement.md:4`). Copy line 4 byte-for-byte and change only `deps:`. |
| M04 | **VALID-WITH-CORRECTIONS** | The subset projection/corner envelope follows from the inclusion and compressed-corner contracts (TeX 1068-1082,1367-1368,1428-1435). For a self-contained registry contract, explicitly say that \(A\) is a finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra; v3 currently relies on §2 prose (`DESIGN-MAIN-STRUCTURE-v3.md:74-82,158`). |
| M05 | **VALID** | It uses the inclusion part of the two-diagonal corollary and adds bijectivity only with diagonal bijectivity and zero cross-corners, exactly TeX 1325-1359. The four displayed COMP ids are exact (`DESIGN-MAIN-STRUCTURE-v3.md:159`). |
| M06 | **VALID** | Close-to-unit compression becomes the full corner, uniformly amplified (TeX 1064-1066,1542-1544; v3 line 160). |
| M07 | **VALID** | The retained two-sided fixed telescope and its five exact imports match the binding re-audit (`DESIGN-MAIN-STRUCTURE-v3.md:171,175-190`; `AUDIT-MAIN-STRUCTURE-v2.md:125-164`). No growing sum occurs. |
| M08 | **VALID** | Two injections at \(C_{\rm nest}t<1\) plus finite dimensionality give equality (`DESIGN-MAIN-STRUCTURE-v3.md:172,186-188`). |
| M09 | **VALID** | The distinct outer/nested map and both amplification/identity imports are now explicit (`DESIGN-MAIN-STRUCTURE-v3.md:173`; source TeX 1435-1441,1542-1544). |
| M10 | **VALID** | Reflexivity, dagger symmetry, and nonzero product transitivity use exactly the one-dimensional rows (TeX 1162-1187; v3 line 196). |
| M11 | **REFUTED** | The contract no longer has v2's “local master error” convention, yet it does not state the original ambient defect \(\varepsilon_A\le t\) needed by M08/M10 (`DESIGN-MAIN-STRUCTURE-v3.md:197`; compare v2 lines 72-75,170). Add that hypothesis explicitly. |
| M12 | **REFUTED** | It inherits M11's missing original-ambient bound and lacks a direct M07 import for the quantitative nested target-projection defects required by `def-four-corner-merging-datum` (`DESIGN-MAIN-STRUCTURE-v3.md:198`; definition lines 13-24). |
| M13 | **REFUTED** | Its \(C_{\rm s2}t\) output scale is correct, but the input domain omits the original ambient bound and the direct M07 export needed to put \(P_U^R,P_j^R\) into a closed EXT datum (`DESIGN-MAIN-STRUCTURE-v3.md:199-205`; `definitions/def-extcb-datum.md:13-17`). |
| M14 | **VALID-WITH-CORRECTIONS** | The scalar map estimate is supported at TeX 430-455,1467-1475, conditional on the corrected operator-space shard (`DESIGN-MAIN-STRUCTURE-v3.md:211`). |
| M15 | **VALID** | The explicit two-side conditional contract fixes v2's naked “Stage-1 call” and matches TeX 1352-1359,1419-1426 (`DESIGN-MAIN-STRUCTURE-v3.md:212`). |
| M16 | **VALID** | Applying `conj-extcb` at total error \(C_{\rm s2}t\), taking \(D_2\ge C_{\rm ext}C_{\rm s2}\), and shrinking \(C_{\rm s2}e_2\le e_{\rm ext}\) is exact and universal (`DESIGN-MAIN-STRUCTURE-v3.md:213,217-221`; `conj-extcb.md:4`). |
| M17 | **VALID** | It retains \((C_{\rm cross}+1)t\le a_{\rm merge}\) and obtains \(D_3t\) from the validated total-error merge (`DESIGN-MAIN-STRUCTURE-v3.md:214`; `lem-extcb-four-corner-merge.md:4`). |
| M18 | **VALID** | Once M14-M17 exist, \(D_*\) and \(r_{\rm reset}\) are a finite universal max/min and cover both M03 guards; the Stage-2 post-helper factor has already been absorbed by M16 (`DESIGN-MAIN-STRUCTURE-v3.md:215-221`). It does not itself establish M19-R for an arbitrary data-only raw-call record. |

## 5. G-S1 verdict

**VALID.** The three ids remain absent, and v3 places the stop after M18 and
before every call envelope and structural row
(`DESIGN-MAIN-STRUCTURE-v3.md:224-240,371-395`). No M01-M18 row imports a
G-S1 producer. This exactly retains the v2 placement
(`DESIGN-MAIN-STRUCTURE-v2.md:211-226`) and the binding requirement
(`AUDIT-MAIN-STRUCTURE-v2.md:265-277,386-387`).

Closing G-S1 would not cure defects A-D above.

## 6. Verdict per post-gate row

| row | verdict | exact audit |
|---|---|---|
| M19-S1 | **REFUTED** | The non-unital hypothesis is too weak; the exact \(M_4\) example in §1 violates M15 complementarity at \(t_1=0\). Restore a unit-preserving extended \(c_0^{\rm cb}\varepsilon\)-inclusion and an explicit extended-\(\varepsilon\) ambient (`DESIGN-MAIN-STRUCTURE-v3.md:250`; TeX 1352-1358,1414-1426). |
| M19-S2 | **REFUTED** | It names \(v_U\) but omits the global ambient and \(w\)-defect hypotheses needed to invoke M04 and prove \(t_2\) dominates \(\varepsilon_U,d_U\) (`DESIGN-MAIN-STRUCTURE-v3.md:251`; M04 at line 158). |
| M19-S3 | **REFUTED** | The same closure failure occurs for \(v_U,v_V\); naming both later maps removes the semantic cycle but not the missing base-state bounds (`DESIGN-MAIN-STRUCTURE-v3.md:252`). |
| M19-R | **REFUTED** | Numerical guards plus a data-only raw-call record do not assert an extended \(d_{\rm raw}\)-inclusion with finite-dimensional source, so M03 cannot be applied (`DESIGN-MAIN-STRUCTURE-v3.md:63,253`; `lem-maincb-error-improvement.md:4`). |
| M20 | **REFUTED** | It depends on three invalid envelopes and omits the compressed-corner scalar call used at the M25 base; \(t_0=\varepsilon\) need not dominate \(\varepsilon_{\{j\}}\le L\varepsilon\) (`DESIGN-MAIN-STRUCTURE-v3.md:254,278-293`). |
| M21 | **VALID-WITH-CORRECTIONS** | The target contract follows from M14 then corrected M19-R at the global scalar scale \(t=\varepsilon\), but its present M19-R/M20 subtree is invalid (`DESIGN-MAIN-STRUCTURE-v3.md:265`). |
| M22 | **VALID-WITH-CORRECTIONS** | The finite maximum argument is correct once M21 and the corrected small domain exist (`DESIGN-MAIN-STRUCTURE-v3.md:266`; TeX 1417). |
| M23 | **VALID-WITH-CORRECTIONS** | Its own unit-preserving hypothesis and \(m\mapsto m+1\) conclusion are correct, but its M19-S1 dependency is false as stated (`DESIGN-MAIN-STRUCTURE-v3.md:267`; TeX 1419-1426). |
| M24 | **VALID-WITH-CORRECTIONS** | Maximum selection plus one valid M23 call proves the result; it is presently blocked by M23's invalid subtree (`DESIGN-MAIN-STRUCTURE-v3.md:268`). |
| M25 | **REFUTED** | RI is preserved at inductive successor calls after correcting M19-R, but the atomic scalar base has no licensed scale and M25 lacks a direct M04 import (`DESIGN-MAIN-STRUCTURE-v3.md:269,274-297`). Add M04 and a compressed-corner scalar envelope. |
| M26 | **REFUTED** | The union-stable local invariant is the right conclusion, but the hypothesis omits the defect/unit control on \(w\) needed by M19-S3 and silently changes v2's domain (`DESIGN-MAIN-STRUCTURE-v3.md:270`; v2 line 252). |
| M27 | **REFUTED AS WIRED** | The complete-family hypothesis and M26-only dependency are correct, but the global partition-map bound is missing and M26 is invalid (`DESIGN-MAIN-STRUCTURE-v3.md:271`; v2 line 253). |
| M28 | **REFUTED AS WIRED; TARGET CONTRACT VALID** | The final uniform extended isomorphism is exactly what the consumer needs, and the M28-only join is correct, but M19/M20/M25-M27 do not supply it (`DESIGN-MAIN-STRUCTURE-v3.md:272`; `lem-thmainext-conditional.md:4,26-30`). |

## 7. Hazard adjudications and dimension-freeness

### R19 — **VALID**

The actual Stage-1 call changes \(m\) to \(m+1\), so
\(\dim_{\mathbb C}A-m\) decreases by one. V3 correctly selects a maximum from
the nonempty bounded feasible set instead of treating arbitrary termination
as maximality (`DESIGN-MAIN-STRUCTURE-v3.md:301-313`; TeX 1417-1426).

### R21 — **VALID**

M25 uses \(|C|-r\); M27 takes the complete one-class family as initial data
and uses \(q-r\); only M28 joins the branches
(`DESIGN-MAIN-STRUCTURE-v3.md:315-322,269-272`). This matches Kitaev's order
at TeX 1430-1443.

### R22 — **VALID-WITH-CORRECTIONS**

The mathematical production/consumption order is right: M11 obtains both
original zero corners by additivity, M08 transports both dimensions, and M12
installs the unique \(0\to0\) maps
(`DESIGN-MAIN-STRUCTURE-v3.md:324-346`; TeX 1363-1369,1443). It is not
contractually closed until M11 states its original ambient bound and M12
imports M07's quantitative nested-projection result directly.

### Dimension-freeness — **VALID; NO ROUTE ALARM**

The source declares its \(O(\cdot)\) constants independent of additional data
and repeats dimension-freeness in both main theorems
(`approximate_algebras.tex:458,460-462,1538-1540`). The diagonal has norm one
for arbitrary finite direct sums (TeX 1239-1254); M07/M09 are fixed
telescopes; M12 has four corners; `conj-extcb` is uniform in rank,
amplification, and dimension (`conj-extcb.md:23-40`); and
\(K_{\rm call}\) is a finite maximum over call **types**, not calls
(`DESIGN-MAIN-STRUCTURE-v3.md:348-369`).

The omitted atomic-scalar call can be repaired with the already-universal
\(L\) or \(K_{\rm call}\); it is a domain omission, not a hidden
dimension-dependent coefficient.

## 8. Retained-contract diff

The claim that every retained contract is copied verbatim
(`DESIGN-MAIN-STRUCTURE-v3.md:36-38`) is false.

1. M03 does not copy the authoritative landed contract literally; exact
   correction is stated in §4 above.
2. M25-M27 replace v2's extended
   \(c_0^{\rm cb}\varepsilon\)-inclusion hypothesis on \(w\) by “non-unital”
   or unquantified “reset inclusion”
   (`DESIGN-MAIN-STRUCTURE-v2.md:251-253`;
   `DESIGN-MAIN-STRUCTURE-v3.md:269-271`). The RI correction authorizes
   changing the local current-map bound; it does not authorize weakening the
   global unit/defect hypothesis.
3. M07-M13, the two-induction architecture, R19, and G-S1 are otherwise
   retained in substance. The named M11-M13 canonical-data changes expose the
   additional missing ambient/dependency clauses found above; they do not
   justify reading those clauses into the contracts.

## 9. Audit of every v3 §12 disposition claim

“Valid” below means only that v3 accurately dispositions the prior finding at
design level. It is not a proof or authorization to land.

### 9.1 V3 §12.1 claims

| v3 §12.1 claim (`DESIGN-MAIN-STRUCTURE-v3.md:464-481`) | verdict |
|---|---|
| Fatal A later-map cycle cleared by explicit \(v_U,v_V\) | **VALID IN PART.** The later maps are explicit, but M19-S2/S3 remain non-closed because the base \(A,w\) bounds are absent (§1B). |
| \(C_{\rm s2}\) scale cleared by M16 | **VALID.** `conj-extcb.md:4` gives exactly the required linear total-error output. |
| Four definitions cleared by P0 | **VALID-WITH-CORRECTIONS.** P0 is present, but no exact schema-complete shard is specified and the operator-space field list is not byte-faithful (§2). |
| Amplified compression/identities exact imports | **VALID.** V3 lines 159,171,173 name them. |
| One-sided almost-containment handled by M07 telescope | **VALID.** V3 lines 175-184 retain both derivations. |
| Corner algebra/rectangular product exact imports | **VALID.** V3 lines 159,171,173. |
| Single compression restricted to ideal-unit Stage 1 | **VALID.** V3 lines 139-142,212,250. |
| One-dimensional product/dimension/additivity used in M10-M13 | **VALID-WITH-CORRECTIONS.** The leaves are correct; M12/M13 additionally need M07 and an ambient bound. |
| `conj-extcb` dimension-free consumption | **VALID.** `conj-extcb.md:4,23-40`; corrected M16 at v3 line 213. |
| Four-corner total smallness | **VALID.** V3 lines 214-215 match `lem-extcb-four-corner-merge.md:4,18-25`. |
| Exact-target correction removed from M03 proof edge | **VALID.** Proposed M03 dep is M02 only (v3 line 157). |
| Downstream M28 match and future rewire | **VALID-WITH-CORRECTIONS.** M28's target matches, but its subtree does not close; the exact rewire remains future-only (v3 lines 396-407). |
| M03 stays stated | **VALID.** `lem-maincb-error-improvement.md:7-8`; v3 lines 134-135,450-452. |
| M07 exact deps/telescope | **VALID.** V3 lines 171,175-190. |
| M08 two injections | **VALID.** V3 lines 172,186-188. |
| M09 outer transfer exact deps | **VALID.** V3 line 173. |

### 9.2 V3 §12.2 per-row claims

| claim (`DESIGN-MAIN-STRUCTURE-v3.md:485-513`) | verdict |
|---|---|
| M01/M02 definition gate cleared | **VALID-WITH-CORRECTIONS:** corrected operator-space shard required. |
| M03 dependency-only correction | **VALID-WITH-CORRECTIONS:** copy the landed contract literally (`lem-maincb-error-improvement.md:4`). |
| M04 unchanged valid | **VALID-WITH-CORRECTIONS:** make the ambient hypothesis self-contained. |
| M05 exact deps | **VALID.** |
| M06 valid | **VALID.** |
| M07 exact deps/telescope | **VALID.** |
| M08 valid | **VALID.** |
| M09 exact amplification deps | **VALID.** |
| M10 valid | **VALID.** |
| M11 canonical data clears finding | **REFUTED:** original ambient defect is no longer bounded (`DESIGN-MAIN-STRUCTURE-v3.md:197`). |
| M12 canonical data/current maps clear finding | **REFUTED:** missing ambient bound and direct M07 quantitative export (v3 line 198). |
| M13 \(C_{\rm s2}\) threaded | **VALID-WITH-CORRECTIONS:** scale fixed; datum closure still lacks ambient/M07 inputs (v3 lines 199-205). |
| M14 valid | **VALID-WITH-CORRECTIONS:** operator-space P0 correction. |
| M15 explicit hypotheses | **VALID.** |
| M16 absorbs \(C_{\rm s2}\) | **VALID.** |
| M17 valid | **VALID.** |
| M18 call-specific caveat | **VALID.** |
| M19 refutation cleared by S1/S2/S3/R | **REFUTED:** all four replacement rows fail a stated closure test (§1A-C). |
| M20 rebuilt and cleared | **REFUTED:** it omits the M25 atomic scalar call (§1D). |
| M21 domain cleared | **REFUTED AS WIRED:** target is valid, M19-R/M20 are not. |
| M22 valid | **VALID-WITH-CORRECTIONS:** depends on corrected M21/domain. |
| M23 corrected producers | **REFUTED AS WIRED:** M19-S1 is false under its stated hypothesis. |
| M24 valid | **VALID-WITH-CORRECTIONS:** conditional on corrected M23. |
| M25 stronger invariant clears finding | **REFUTED:** successor preservation is plausible, but the base call is unlicensed (v3 lines 278-293). |
| M26 local invariant clears domain | **REFUTED:** \(w\)'s required global bound is absent (v3 line 270). |
| M27 complete-family conditional | **VALID IN SHAPE; REFUTED AS WIRED:** family/no-M25 edge retained, but M26/domain fail. |
| M28 rebuilt subtree | **REFUTED:** target remains valid; subtree fails at M19/M20/M25. |

### 9.3 V3 §12.3 claims

| v3 §12.3 claim (`DESIGN-MAIN-STRUCTURE-v3.md:517-532`) | verdict |
|---|---|
| R19 retained | **VALID.** V3 lines 301-313; TeX 1417-1426. |
| R21 retained | **VALID.** V3 lines 315-322; TeX 1430-1443. |
| R22 cleared by subsection/P0 | **VALID-WITH-CORRECTIONS.** The prose chain is right; M11/M12 contracts are not closed. |
| G-S1 location | **VALID.** V3 lines 224-240. |
| no dimension alarm | **VALID.** V3 lines 348-369; TeX 458,1538-1540. |
| first-audit threshold cycle cleared | **VALID IN ACYCLICITY, REFUTED IN CLOSURE.** No backward existence edge remains, but the replacement hypotheses are incomplete. |
| nested comparison retained | **VALID.** |
| outer compression retained with deps | **VALID.** |
| complete-family repair retained | **VALID.** |
| Stage-1 four-bijective misuse cleared | **VALID FOR M15, REFUTED FOR M19-S1'S DOMAIN.** The direct-sum mechanism is right; non-unital \(w\) does not supply complementarity to \(I_A\). |
| binary merge iterability | **VALID IN SHAPE.** M26 accepts unions; its domain still lacks \(w\)'s bound. |
| zero-corner reuse cleared | **VALID-WITH-CORRECTIONS.** Add M11 ambient and M12 direct M07 inputs. |
| reset guard \(C_{\rm s2}\) cleared | **VALID.** |
| initial/maximal/final producers cleared | **REFUTED AS A SUBTREE.** M21/M22 targets are valid; M28 is not derived. |

### 9.4 V3 §12.4 claims and the eight binding requirements

| requirement/claim (`DESIGN-MAIN-STRUCTURE-v3.md:536-548`) | verdict |
|---|---|
| §10.1 P0 before M01 | **VALID-WITH-CORRECTIONS.** Step 0 exists (v3 lines 376-377), but exact schema fields/operator-space byte-match must be fixed. |
| §10.2 closed call-specific M19 envelopes | **REFUTED.** S1 is false for non-unital \(w\); S2/S3 omit base-state bounds. |
| §10.3 separate/absorb \(C_{\rm s2}\) | **VALID.** M16 option 1 is correct. |
| §10.4 prove the stronger reset invariant | **REFUTED AS CLOSED FACTORING.** M19-R omits the inclusion hypothesis and M25 omits the atomic base-call scale. |
| §10.5 exact M05/M07/M09 deps | **VALID.** V3 lines 159,171,173. |
| §10.6 retain G-S1 | **VALID.** V3 lines 224-240,387-390. |
| §10.7 retain complete M27 family/M28-only join | **VALID.** V3 lines 271-272,315-322. |
| §10.8 complete definition/dependency ledger | **VALID-WITH-CORRECTIONS.** The requested categories are present, but the newly exposed M07/M11-M13/M19/M20/M25 corrections are necessarily absent. |
| ledger: four definitions | **VALID-WITH-CORRECTIONS.** V3 lines 413-419; exact shard schemas missing. |
| ledger: M09 exact deps | **VALID.** V3 lines 427-428. |
| ledger: M19/M20/M16 | **REFUTED AS COMPLETE.** M16 is present; the M19/M20 entries describe invalid contracts (v3 lines 431-436). |
| ledger: downstream rewire | **VALID.** Exact YAML is at v3 lines 400-407 and repeated at lines 439-440. |

## 10. Landing order and escalation ledger

### Landing order — **REFUTED**

The order is syntactically topological for the displayed dependency lists and
places P0 and G-S1 correctly
(`DESIGN-MAIN-STRUCTURE-v3.md:371-407`). It is not executable:

1. M11-M13 would land without the original-ambient and M07 inputs they use.
2. Step 8 lands four non-closed M19 replacements.
3. Step 9 lands M20 without the atomic compressed-corner scalar call.
4. Step 12 then attempts M25's base step without M04 or a licensed scale.
5. Steps 13-14 consume M26/M27 contracts whose global \(w\)-bound was
   silently dropped.
6. Step 1 must explicitly validate/land the rewired M03 after M02 and before
   M04; “rewire M03” alone is not an available rigorous dependency under the
   repository's status-propagation rule.

### Escalation ledger — **REFUTED AS COMPLETE**

V3 does include the floor demanded by the v2 audit: four P0 definitions, the
M03 rewire, exact M05/M07/M09 imports, M16's scale absorption, M19
replacement/invariant, and the future `lem-thmainext-conditional` rewire
(`DESIGN-MAIN-STRUCTURE-v3.md:409-452`). It necessarily omits the defects
found here:

- the exact operator-space definition correction and schema-complete P0
  frontmatters;
- the M11-M13 original-ambient hypotheses and direct M07 imports;
- the unit-preserving M19-S1 hypothesis;
- the \(A,w\) base-state bounds in M19-S2/S3 and M26/M27;
- the M19-R extended-inclusion hypothesis;
- the atomic compressed-corner scalar envelope and M25's direct M04 import;
- restoration/ratification of the silent M03 and M25-M27 contract drifts.

## 11. Exact requirements for a fourth repair

A fourth repair need not redesign M07-M10, the M16 scale absorption, the two
induction measures, R19, G-S1, or the M27/M28 join. It must:

1. provide schema-complete P0 proposals and restrict the cited
   operator-space statement to the byte-matched Definition block at TeX
   1453-1464;
2. add the original ambient-defect hypothesis to M11-M13 and direct M07
   dependencies to M12/M13;
3. make M19-S1 unit-preserving, and give M19-S2/S3 explicit global
   \(A,w\) bounds in addition to their supplied current maps;
4. make M19-R assume an actual extended raw inclusion/isomorphism with
   finite-dimensional source, not merely two recorded numbers;
5. add a compressed-corner scalar call envelope, import M04 directly into
   M25, and thread its scale through M20/M18;
6. restore explicit global \(w\)-bounds in M25-M27 and do not silently
   generalize “extended inclusion” to “non-unital reset inclusion”;
7. copy the ratified M03 contract verbatim and change only its dependency;
8. rebuild the landing order and escalation ledger with these corrections.

Nothing in this audit authorizes any definition, contract, dependency, or
status change. `op-classical` remains open, and the MAIN chain remains
non-rigorous.
