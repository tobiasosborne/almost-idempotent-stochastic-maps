# AUDIT-MAIN-STRUCTURE-v5 — sixth-stage fresh hostile re-audit

**Date:** 2026-07-27  
**Role:** fresh independent hostile auditor  
**Status:** **AUDIT ONLY; NON-RIGOROUS; NO STATUS PROMOTION; DO NOT SEED**

## 1. Final disposition

**REPAIR-CONFIRMED.**

V5 clears both defects isolated by `AUDIT-MAIN-STRUCTURE-v4.md`. The v4-to-v5
row diff changes exactly M13, M19-S2, and M19-S3, and each change is one of
the two prescribed repairs
(`DESIGN-MAIN-STRUCTURE-v5.md:328,382-383`). No independent-state recurrence,
correction-induced defect, unbound reference, cycle, or budget overflow was
found.

This is a design-level verdict only. V5 is the landable design, gated on P0,
G-S1, and user ratification; the M07 hostile-verification stop also remains
explicit (`DESIGN-MAIN-STRUCTURE-v5.md:517-540,625-633`). Nothing in this
audit promotes a status or proves `op-classical`.

## 2. Fix 1 — partition/reset identity

**Verdict: CLEARED.**

M19-S2 now quantifies a partition state “for this same \(A,w\)” and a reset
state “for the \(U\) of that same partition state.” M19-S3 uses the identical
ambient/map tie and ties its two reset states to the \(U,V\) of that same
state (`DESIGN-MAIN-STRUCTURE-v5.md:382-383`). These are explicit identity
constraints, not merely repeated type shapes.

The tie is sufficient for the advertised M04 deductions. The partition
state defines \(P_U,A_U\) from its recorded \(A,w\)
(`DESIGN-MAIN-STRUCTURE-v5.md:170-177`), while M04 bounds every nonempty
corner of the displayed extended ambient/inclusion pair
(`DESIGN-MAIN-STRUCTURE-v5.md:287`). Therefore the
\(\varepsilon_U,\varepsilon_R\le L\varepsilon\) in M19-S2 and the
\(\varepsilon_U,\varepsilon_V,\varepsilon_R\le L\varepsilon\) in M19-S3
apply to the corners used in their conclusions, rather than to corners of an
independent state (`DESIGN-MAIN-STRUCTURE-v5.md:382-383`).

The identity constraint is recorded twice in the execution controls:

- landing step 8 requires validation that S2/S3's state records the displayed
  \(A,w\) and that the reset state(s) refer to its \(U\), respectively \(U,V\)
  (`DESIGN-MAIN-STRUCTURE-v5.md:538-540`);
- the interface and domain ledger requires every consumer to identify the
  state's ambient/map with its quantified \(A,w\), requires simultaneous
  reset states for the same state's \(U,V\), and repeats the S2/S3-specific
  identities (`DESIGN-MAIN-STRUCTURE-v5.md:575-579,607-611`).

### Independent-state recurrence hunt

No recurrence was found in the named rows.

- M12 and M13 bind the partition state to the displayed
  \(w:\mathbb C^m\to A\) with “comes from,” then type their supplied reset
  maps into the \(A_U\), respectively \(A_U,A_V\), introduced by that state
  (`DESIGN-MAIN-STRUCTURE-v5.md:327-328`). This matches the reset datum's
  fields \(U,A_U,v_U:B_U\to A_U\)
  (`DESIGN-MAIN-STRUCTURE-v5.md:111-117`).
- M21-M24 quantify no partition state together with independent reset data,
  so the flaw has no place to recur there
  (`DESIGN-MAIN-STRUCTURE-v5.md:396-399`).
- M25 binds its state to the displayed \(A,w\) and produces its reset state
  in that state's \(A_C\) (`DESIGN-MAIN-STRUCTURE-v5.md:400`).
- M26 binds its state to the displayed \(A,w\), introduces \(U,V\) in that
  state, and types the supplied reset maps into the resulting \(A_U,A_V\)
  (`DESIGN-MAIN-STRUCTURE-v5.md:401`).
- M27 likewise binds its state to the displayed \(A,w\), introduces all
  \(C_a\) there, and types every initial reset map into the corresponding
  \(A_{C_a}\) (`DESIGN-MAIN-STRUCTURE-v5.md:402`).

Thus none of M12, M13, or M21-M27 permits a good displayed \(A,w\) to be
used to bound corners belonging to a separately quantified partition state.

## 3. Fix 2 — M13 ambient-algebra producer

**Verdict: CLEARED.**

M13 directly lists `lem-compcb-corner-algebra` and explicitly assigns it the
job of making \(A_R\) an extended
\(\varepsilon_{A_R}\)-\(C^*\)-algebra
(`DESIGN-MAIN-STRUCTURE-v5.md:328`). This is exactly the missing first field
of a closed EXT-CB datum (`definitions/def-extcb-datum.md:13-17`).

The imported contract supplies the required conclusion: for universal
\(e_{\rm ca}>0,C_{\rm ca}<\infty\), a nonvanishing
\(\delta\)-projection \(P\) with
\(\delta+\varepsilon\le e_{\rm ca}\) gives \(S_P\) the structure of an
extended \(C_{\rm ca}(\delta+\varepsilon)\)-\(C^*\)-algebra
(`argument/lemmas/lem-compcb-corner-algebra.md:4-6`).

M13 supplies the nonvanishing input rather than assuming it from nowhere.
Its \(U\ne\varnothing\), \(j\notin U\), and
\(R=U\cup\{j\}\) make \(R\ne\varnothing\); its non-unital extended
\(t\)-inclusion sends the nonzero coordinate idempotent \(1_R\) to \(P_R\)
(`DESIGN-MAIN-STRUCTURE-v5.md:328`). An extended inclusion has the two-sided
\((1\pm t)\) norm bounds and is an extended \(t\)-homomorphism
(`definitions/def-extended-delta-inclusion.md:13-17`), so \(P_R\) is a
\(t\)-projection with norm bounded below by \(1-t\). After the universal
smallness shrink already assigned to \(e_{\rm s2}\), this is the
nonvanishing alternative in `def-delta-projection`
(`definitions/def-delta-projection.md:16-26`).

The arithmetic remains coherent. Since the original ambient defect and the
projection defect are each \(O(t)\), shrinking \(e_{\rm s2}\) absorbs the
\(e_{\rm ca}\) guard and enlarging \(C_{\rm s2}\) absorbs the universal
\(C_{\rm ca}\) factor (`DESIGN-MAIN-STRUCTURE-v5.md:328,330-336`). M16
already accepts the enlarged total defect \(C_{\rm s2}t\), chooses
\(e_2\le e_{\rm s2}\) with
\(C_{\rm s2}e_2\le e_{\rm ext}\), and absorbs the coefficient into \(D_2\);
M18 then uses \(e_2,D_2\), while M20 needs no additional
\(C_{\rm s2}\) factor
(`DESIGN-MAIN-STRUCTURE-v5.md:344,346,348-353,385`). No other row's
finite-minimum arithmetic changes.

The serial plan records the direct import and both absorptions at step 4
(`DESIGN-MAIN-STRUCTURE-v5.md:529-532`). The escalation ledger records the
ambient-field producer, \(e_{\rm ca}\) threshold, and \(C_{\rm ca}\)
coefficient (`DESIGN-MAIN-STRUCTURE-v5.md:592-602`).

## 4. Diff integrity and changed-text defect hunt

**Diff-integrity verdict: CLEARED.**

The complete unified v4-to-v5 diff contains only:

1. version/frontmatter and §0's exact two-fix declaration
   (`DESIGN-MAIN-STRUCTURE-v5.md:1-38`);
2. the M13 contract/dependency/audit cell and its immediately following
   scale explanation (`DESIGN-MAIN-STRUCTURE-v5.md:328-336`);
3. the M19-S2/S3 contract and audit cells
   (`DESIGN-MAIN-STRUCTURE-v5.md:382-383`);
4. the prescribed landing and escalation annotations
   (`DESIGN-MAIN-STRUCTURE-v5.md:529-540,575-611`);
5. the v4-audit disposition and mechanically induced historical section
   renumbering (`DESIGN-MAIN-STRUCTURE-v5.md:635-725,732,749,779,804,851,859,880,912,931`).

An extraction-and-diff of every M-row found no changed row other than M13,
M19-S2, and M19-S3. In particular, no retained contract, defs, provenance,
budget, or dependency cell drifted.

**New-defect hunt: none found.** The added tie language refers only to the
already quantified \(A,w,U,V\) and “that same partition state”
(`DESIGN-MAIN-STRUCTURE-v5.md:382-383`); it introduces neither
meta-language such as “the contract of” nor an unbound object. M13's new
\(e_{\rm ca},C_{\rm ca}\) names are bound by the named landed contract
(`argument/lemmas/lem-compcb-corner-algebra.md:4`).

The M13 dependency addition is acyclic: the landed corner-algebra row depends
only on the four COMP rows listed at
`argument/lemmas/lem-compcb-corner-algebra.md:6`, none of which depends on
the proposed M13. M13 remains at projected budget **10 nodes / depth 3** with
seven direct result imports, within the repository's
\(\le12\)-node/\(\le3\)-depth cap
(`DESIGN-MAIN-STRUCTURE-v5.md:275-278,328`).

## 5. Required disposition

**REPAIR-CONFIRMED — v5 is the landable design, gated on P0 + G-S1 and user
ratification.**

No `ROUTE-ALARM` condition was found: both repaired defects are
factoring/interface defects, and the audit found no counterexample,
dimension-dependent constant, or route-level obstruction.
