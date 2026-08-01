# DESIGN — M17 typed-quantification amendment

## 0. Verdict

**STOP / ESCALATE.**  The contract-local amendment below is sufficient to make
M17's two imported applications well typed, but it is **not consumer
dischargeable** from the frozen T0 contracts of M19-S3 and M12.  The missing
clause is bijectivity of the four fixed level-one corner maps.  M12's validated
proof establishes that fact internally, but neither the M12 root nor the
M19-S3 root exports it.  The 2026-07-28 typed-witness law forbids promoting
same-named internal constructions through an opaque theorem boundary.

Accordingly this document supplies all five requested design deliverables, but
the displayed contract is a **candidate, not a ratification recommendation**.
No M17 re-seed should begin until the user chooses a larger interface repair.

## 1. Candidate amended M17 contract

One physical ASCII line:

```text
contract: After first fixing the universal C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum, C_merge,a_merge witnesses of lem-extcb-four-corner-merge, and C_iso_unit,e_iso_unit witnesses of lem-maincb-isomorphism-unit-control, there are universal D_3 < infinity and e_3 > 0 such that for every def-maincb-witness-ledger datum W with W.e_cross <= min{e_cross^0,e_3}, (C_cross^0+1)*e_3 <= a_merge, and (C_merge*(C_cross^0+1)+1)*e_3 <= e_iso_unit, every amplified four-corner datum in A_R with source B_U oplus B_V, with B_U and B_V finite-dimensional C*-algebras, with A_R a finite-dimensional extended epsilon_{A_R}-C*-algebra, whose four fixed level-one corner maps are bijective, and with 0 <= rho <= C_cross^0*t and 0 <= epsilon_{A_R} <= t <= W.e_cross yields an extended D_3*t-isomorphism v:B_U oplus B_V->A_R satisfying ||v(I_{B_U oplus B_V})-u_{A_R}|| <= D_3*t.
```

The conclusion is byte-unchanged.  The additions are only the source and
target types, bijectivity of exactly the four fixed level-one maps required by
`lem-extcb-four-corner-merge`, and nonnegativity of the defect/ambient
parameters.  No sign hypothesis on `C_iso_unit` is needed.  Challenge
`ch-40fe16a76915988d` gives the sign-safe proof: for
`s=delta+epsilon_{A_R}>=0`, use
`||v(I)-u|| <= C_iso_unit*s <= abs(C_iso_unit)*s`, then multiply
`s <= (K+1)*t` only by the nonnegative `abs(C_iso_unit)`.  This avoids
silently assuming `C_iso_unit>=0` and introduces no numerical witness value.

The local ground truth has exactly these interfaces.  The source definition
types a delta-isomorphism as a bijective delta-inclusion
(`approximate_algebras.tex:443-455`).  The merge lemma assumes maps between
the four displayed source and target corners and states separately that the
combined map is bijective when all four maps are bijective
(`approximate_algebras.tex:1325-1349`; especially `:1345`).  Its Stage-3
corollary likewise requires bijective diagonal maps and zero cross-corners
(`:1352-1358`).  The unit-control provenance is confined to
`:430-455,1194-1222`, and the Stage-3 use remains the source's `:1443`.

## 2. M26 consumer dischargeability

The audit is clause-by-clause.  Here `t=t_3=W.K3*epsilon` and
`epsilon_{A_R}=epsilon_R=W.L*epsilon`, as exported by M19-S3.

| Added M17 hypothesis | T0 exporting clause available to M26 | Verdict |
|---|---|---|
| `B_U,B_V` finite-dimensional C*-algebras and source `B_U oplus B_V` | A current reset state records “a named finite-dimensional C*-algebra `B_U`” (`def-maincb-reset-state:13-20`).  M19-S3 export node 1.3.3 then says “take the named finite-dimensional C*-algebra `B_R:=B_U direct-sum B_V`” and packages that exact source (`export.md:159-173`). | **DISCHARGED.** |
| `A_R` a finite-dimensional extended `epsilon_R`-C*-algebra | M19-S3 root assumes finite-dimensional `A` (`export.md:5`).  Node 1.2.2 exports that direct-corner control “gives `A_R` an extended `L^0*epsilon`-C*-algebra structure” and records it at `epsilon_R:=W.L*epsilon` (`:87-101`); `A_R` is a compressed-corner subspace of finite-dimensional `A`, hence finite-dimensional. | **DISCHARGED.** |
| Same typed datum/map family | M19-S3 node 1.3.3 defines `v_R:B_R->A_R`, identifies its restrictions with the four supplied corner maps, and records the one fixed amplification family (`:159-173`). | **DISCHARGED.** |
| `0 <= epsilon_R <= t_3 <= W.e_cross` | M19-S3 root has `0 <= epsilon` and `W.K3>=W.L`; node 1.3.1 exports `W.L*epsilon <= t_3 <= W.e_cross` (`:135-145`), while node 1.2.2 sets `epsilon_R=W.L*epsilon` (`:87-101`). | **DISCHARGED.** |
| `0 <= rho <= C_cross^0*t_3` | M12 selects `C_cross^0>=1`; its export node 1.8 takes the common defect `rho=C_cross^0*t` (`M12 export.md:111-121`), and M19-S3 root/node 1.3 export the forwarded bound `rho<=C_cross^0*t_3` (`M19-S3 export.md:5,123-133`).  With `t_3>=0`, the constructed bound is nonnegative. | **DISCHARGED for the explicit construction.** |
| All four fixed level-one corner maps bijective | M12's **root** exports only that the constructions “form the explicit Stage-3 amplified four-corner datum” (`M12 export.md:3-13`).  M19-S3's root exports only the resulting “four-corner raw-call datum” (`M19-S3 export.md:3-13`).  Neither root says the four maps are bijective, and `def-four-corner-merging-datum:13-24` does not include bijectivity. | **NOT DISCHARGED.** |

Therefore M26 cannot instantiate the candidate M17 contract from its allowed
T0 interfaces.  This is not cured by the fact that the same mathematical
construction is bijective inside M12's proof: the AF external registered in
the parked M17 workspace contains only M12's root contract, exactly as
challenge `ch-ea9888f43d6f3f92` records.  Treating internal node names as an
export would violate both typed-witness laws: the provider would not export
the typed property used by the consumer, and an opaque receiving theorem
would be identifying witnesses anaphorically rather than through a stated
monotone interface.

**Dischargeability verdict: FAIL.**  Per the brief, this is the stopping
condition and a deeper interface finding, not a completed typing fix.

## 3. Bijectivity audit of M12

M12's proof does establish bijectivity internally:

- Node 1.4 exports each diagonal map
  `T_X:B_X->S^{A_R}_{P_X^R}` as an extended `C_out*t`-isomorphism
  (`proofs/lem-maincb-cross-class-merging-datum/export.md:63-73`).  By
  `def-extended-delta-inclusion:13-17`, each such level-one map is bijective.
- Node 1.6 exports that both source and target cross-corners are zero and
  chooses the unique level-one map `0->0` in each direction
  (`export.md:87-97`); these two maps are bijective.
- Node 1.8 names the four maps as the two diagonal `T` maps and the two zero
  maps, but concludes only that they satisfy every field of
  `def-four-corner-merging-datum` (`export.md:111-121`).

The exact gap is at the theorem boundary: M12 root node 1 (`export.md:3-13`)
does not state “the four fixed level-one corner maps are bijective.”  M19-S3
does not repair the omission: its packaging node names the same diagonal and
zero maps (`proofs/lem-maincb-stage3-call-envelope/export.md:159-173`) but its
root again exports only a four-corner raw-call datum (`:3-13`).

The minimal **M17-local** fix is precisely the hypothesis in section 1:
“whose four fixed level-one corner maps are bijective.”  That makes M17
provable without touching frozen M12.  It does **not**, however, make the
M17-to-M26 edge usable.  Closing that second gap requires an exported T0
bridge or a strengthened provider/consumer interface, all forbidden by this
round's one-contract constraint.

**Bijectivity-audit verdict:** present in M12's proof body; absent from M12's
and M19-S3's exported contracts; unavailable to M26.

## 4. Parked-tree budget and re-seed guidance

Do not resume or patch the 6/11 parked tree.  Once the interface escalation is
resolved, cleanly re-seed M17 under the ratified root.  A positive tree should
fit **6 live nodes / 2 rounds / hard cap 9**: root, provider/constant choice,
merge smallness, typed merge application, unit-control range, and sign-safe
unit/conclusion assembly.  The cap need not increase; the old 11-node tree is
a diagnostic obstruction tree, not evidence for a larger positive proof.

Of the six currently validated nodes, only these survive verbatim under the
typed root:

- `1.1`, the universal `e_3,D_3` choice using absolute values;
- `1.2`, the `rho+epsilon_{A_R}` merge-smallness calculation; and
- `1.4`, the `delta+epsilon_{A_R}` unit-control range, once the new positive
  merge node supplies its `delta,v`.

Nodes `1.3`, `1.3.1`, and `1.3.2` are obstruction diagnostics for the old
root and do not survive as proof nodes; retain the counterexample only as a
red test.  Pending nodes `1.5` through `1.5.2` must be discarded.  Their
replacement must use the exact typed source/target and the sign-safe chain
from `ch-40fe16a76915988d`, never the invalid multiplication by an
unconstrained `C_iso_unit`.

Re-seeding is **blocked** by section 2, irrespective of this adequate local
budget.

## 5. Risk register and escalation

The first hostile-verifier attack should be the consumer premise ledger:
“show the exact T0 root clause from which M26 obtains bijectivity of each of
the four maps.”  There is no such clause.  Internal M12 proof nodes are not a
substitute for an exported theorem statement.

The top two ways the candidate design could be wrong are:

1. **Opaque-export violation.**  A proof could silently use M12 nodes 1.4 and
   1.6 as though M19-S3 or M26 had imported them.  This repeats the
   2026-07-28 typed-witness failure and is already ruled out by
   `ch-ea9888f43d6f3f92`.
2. **Sign or witness-identity drift.**  A new M17 tree could multiply an
   inequality by `C_iso_unit` without proving it nonnegative, or apply unit
   control to an existential merged map not identified with M19-S3's literal
   raw output.  The repair is the absolute-value chain above plus an explicit
   same-map assembly from the datum; repeated notation is not witness
   identity.

**Escalation required:** the user must choose a scope expansion before
ratification.  The smallest principled options are (a) a new validated bridge
whose contract exports bijectivity of the four explicit M12 maps and an
explicit dependency path making it available to M26, or (b) a re-ratified,
revalidated strengthened provider interface (M12 or M19-S3).  Either option
changes more than the single M17 contract and is therefore intentionally not
designed or landed here.  No definition change, M12 amendment, T0 mutation,
or M26 mutation has been made.
