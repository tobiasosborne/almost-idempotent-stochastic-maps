# HOSTILE AUDIT — `DESIGN-M17-TYPING-v2.md`

**Date:** 2026-08-01

**Auditor role:** fresh independent hostile auditor

**Epistemic status:** audit only; no result or status is promoted.

**Final disposition:** **DESIGN-REFUTED.** The mathematical bridge route is
viable and neither advertised kill-shot forces a frozen-T0 amendment, but the
exact one-new-row/one-amended-contract package is not consumer-dischargeable:
M26 does not import the bridge it must apply. The proposed bridge also has an
ill-typed diagonal source and an incomplete direct-import list. These are local
repairs, not a route alarm, but they exceed the design as written.

## 1. Findings and exact corrections

### F1 — CRITICAL: M26 cannot use the bridge, and M17's certificate wording is an anaphor

The proposed M17 antecedent says that its maps "are the maps certified
bijective by" the bridge (`DESIGN-M17-TYPING-v2.md:89`), but it quantifies no
bridge certificate and none of the bridge's geometric inputs. This is theorem
provenance used as a predicate, not a typed mathematical hypothesis. More
decisively, the claimed chain says M26 applies the bridge
(`DESIGN-M17-TYPING-v2.md:135`), while M26's direct imports omit it
(`argument/lemmas/lem-maincb-binary-block-merge.md:6`). Registry dependencies
are the imports used by the module (`argument/README.md:9-16,43-46`), and the
provisioner registers only direct `deps:` (`scripts/provision-af-row.py:4-7,26-43`).
M17's dependency on the bridge therefore does not make the bridge theorem
available in M26's workspace.

**Exact correction to M17's contract:** retain the bridge-selected provider
pair, but replace

> whose four fixed level-one corner maps are the maps certified bijective by lem-maincb-cross-datum-bijectivity

by

> whose four fixed level-one corner maps are bijective

Thus the corrected physical line is:

```text
contract: After first fixing the universal C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum furnished by lem-maincb-cross-datum-bijectivity, C_merge,a_merge witnesses of lem-extcb-four-corner-merge, and C_iso_unit,e_iso_unit witnesses of lem-maincb-isomorphism-unit-control, there are universal D_3 < infinity and e_3 > 0 such that for every def-maincb-witness-ledger datum W with W.e_cross <= min{e_cross^0,e_3}, (C_cross^0+1)*e_3 <= a_merge, and (C_merge*(C_cross^0+1)+1)*e_3 <= e_iso_unit, every explicit Stage-3 amplified four-corner datum in A_R furnished by lem-maincb-cross-class-merging-datum with source B_U oplus B_V, with B_U and B_V finite-dimensional C*-algebras, with A_R a finite-dimensional extended epsilon_{A_R}-C*-algebra, whose four fixed level-one corner maps are bijective, and with 0 <= rho <= C_cross^0*t and 0 <= epsilon_{A_R} <= t <= W.e_cross yields an extended D_3*t-isomorphism v:B_U oplus B_V->A_R satisfying ||v(I_{B_U oplus B_V})-u_{A_R}|| <= D_3*t.
```

**Exact correction to M26's direct imports:** replace its `deps:` line by

```text
deps: lem-maincb-stage3-raw-merge; lem-maincb-stage3-call-envelope; lem-maincb-cross-datum-bijectivity; lem-maincb-reset-invariant-preservation; lem-maincb-structural-domain-ledger
```

M26 can then apply the bridge to its displayed Stage-3 inputs, obtain the plain
bijectivity premise, and pass it to M17. This changes no contract or T0 row, but
it is a third-row metadata amendment, so it refutes the design's exact package
claim (`DESIGN-M17-TYPING-v2.md:6-8`).

### F2 — MAJOR: the bridge's diagonal maps have the wrong displayed domains

The datum's four maps must have domains `q_X B_R q_Y`; the pinned source states
this as `S_{Pi_j,Pi_k}` (`approximate_algebras.tex:1325-1345`), and the project
definition packages four corner maps (`definitions/def-four-corner-merging-datum.md:13-18`).
The bridge types both cross maps on the source corners, but defines
`gamma_UU` and `gamma_VV` as composites on `B_U` and `B_V`
(`DESIGN-M17-TYPING-v2.md:21`). The canonical coordinate identifications are
standard, but omitting them makes the asserted equality with maps on
`q_U B_R q_U` and `q_V B_R q_V` ill-typed—the same class of codomain/domain
error previously caught at `AUDIT-MAINCB-REPAIR.md:24-34`.

**Exact correction:** replace the two diagonal definitions in the bridge
contract by

```text
gamma_UU:q_U B_R q_U->S^{A_R}_{P_U^R} defined by gamma_UU((b_U,0)):=Co^{A_R}_{P_U^R}(Co^A_{P_R}(v_U(b_U))), gamma_VV:q_V B_R q_V->S^{A_R}_{P_V^R} defined by gamma_VV((0,b_V)):=Co^{A_R}_{P_V^R}(Co^A_{P_R}(v_V(b_V)))
```

This is only explicit typing of the canonical direct-sum specialization; it
does not change the mathematical maps.

### F3 — MAJOR: the bridge's proposed direct imports omit three named providers

The bridge contract directly fixes witnesses of
`lem-maincb-error-improvement`, `lem-maincb-direct-corner-envelope`, and
`lem-maincb-compressed-corner-unit-comparison` (`DESIGN-M17-TYPING-v2.md:21`),
but its proposed `deps:` contains none of them (`:27-30`). M12's dependency on
those rows is not a transitive import into the bridge workspace. This violates
the registry module rule at `argument/README.md:43-46` and typed-witness law i.

**Exact correction:** use

```text
deps: lem-maincb-error-improvement; lem-maincb-direct-corner-envelope; lem-maincb-compressed-corner-unit-comparison; lem-maincb-cross-class-merging-datum; lem-maincb-outer-compression-transfer; lem-maincb-cross-union-zero-corners
```

All six rows are currently `af: validated`; no new result is needed.

## 2. The two mandated kill-shots

### 2.1 Same-datum identification — VALID after F2's source typing

M12's root is constructive, not existential: it says that "the nested-corner,
outer-compression, and zero-cross-corner constructions form the explicit"
datum (`proofs/lem-maincb-cross-class-merging-datum/export.md:3-13`; registry
contract at `argument/lemmas/lem-maincb-cross-class-merging-datum.md:4`). The
outer construction is itself formula-bound:

> `T = Co^{A_R}_{P^R} o Co^A_R o v`

and is an extended `C_out*t`-isomorphism with `T_n=I_n tensor T`
(`proofs/lem-maincb-outer-compression-transfer/export.md:3-13`). The zero-corner
root exports dimension zero for both original and nested cross-corners
(`proofs/lem-maincb-cross-union-zero-corners/export.md:3-13`), so the maps in
those two directions are uniquely the maps `{0}->{0}`. Consequently the four
formula-bound maps in the corrected bridge are the deterministic constructions
named by the M12 root; there is no second existential datum to identify.
M12 nodes 1.4, 1.6, and 1.8 (`export.md:63-73,87-97,111-121`) agree with this
reading but are not needed as imported theorem clauses.

This differs from W93: there the imported root exported an anaphoric first
component without its typed companion/preimage identity
(`docs/LEARNINGS.md:98-125`). Here the root names formula-bearing construction
providers, and the cross maps are unique. F2 is nevertheless mandatory because
the canonical diagonal source identification must be written, not assumed.

### 2.2 Shared shrunken-witness selection — VALID

After the three provider groups are fixed, M12 exports some valid
`(C_cross^0,e_old)` and a conclusion universal over every ledger satisfying
`W.e_cross<=e_old` and every input with `t<=W.e_cross`
(`cross-class-merging-datum/export.md:5`). Replacing only the margin by
`min{e_old,e_out,e_zero}` restricts that universal antecedent, so the same
coefficient and smaller positive margin remain a valid M12 witness pair. This
is monotonicity within one provider selection, not equality between two opaque
existentials. The bridge contract explicitly exports that the resulting pair
is valid for M12, and the corrected M17 prefix fixes that bridge-furnished pair
before its receiving witnesses. M19-S3 already has the compatible ordered
prefix (`proofs/lem-maincb-stage3-call-envelope/export.md:3-13`). No shared-
witness defect remains once M26 directly imports the bridge as required by F1.

## 3. Bijectivity and M17 proof audit

- **Diagonal maps:** the outer-transfer root quoted above concludes "extended
  ... isomorphism" for the literal composite. By
  `definitions/def-extended-delta-inclusion.md:13-17`, this means bijective at
  level one. Its hypotheses follow definitionally from the supplied extended
  `t`-inclusion and reset isomorphisms: `P_R,P_X` are `t`-projections,
  coordinate identities give both subordinations, and the lower norm bound on
  the nonempty coordinate projection gives `||P_R||>=1-t`. No unexported
  bijectivity-preservation fact is used.
- **Cross maps:** dimension zero from the zero-corner root means each source
  and target is `{0}`; the unique linear map is bijective. The direct-sum source
  cross-corners are exactly zero by elementary C*-algebra arithmetic.
- **Amplifications/compcb:** exact amplification is exported at
  `proofs/lem-compcb-amplified-compression/export.md:3-13`; compression
  idempotence and adjoint compatibility at
  `proofs/lem-compcb-amplified-compression-identities/export.md:3-13`; and the
  compressed ambient structure at
  `proofs/lem-compcb-corner-algebra/export.md:3-13`. These support M12's datum
  clauses; none substitutes for the level-one bijectivity supplied by the
  outer-transfer root.
- **Typed M17:** after F1 replaces the provenance-anaphor by the plain
  bijectivity property, `lem-extcb-four-corner-merge` applies exactly as its
  root requires (`proofs/lem-extcb-four-corner-merge/export.md:3-13`). The
  source/target algebra types are explicit.
- **Sign-safe unit chain:** incorporated correctly. Put
  `s=delta+epsilon_{A_R}>=0`; the unit-control root gives
  `||v(I)-u||<=C_iso_unit*s` (`proofs/lem-maincb-isomorphism-unit-control/export.md:3-13`).
  Since `C_iso_unit<=abs(C_iso_unit)`, multiplication by `s>=0` is safe. Choosing
  `e_3` with the stronger absolute-value threshold and `D_3` with absolute
  values proves the displayed conditions and the output without assuming
  either provider coefficient nonnegative. This is exactly the repair demanded
  by `ch-40fe16a76915988d` (`proofs/lem-maincb-stage3-raw-merge/ledger/000098.json:1`).

## 4. Discharge-chain re-derivation

| Link | Exported interface | Verdict |
|---|---|---|
| M26 inputs -> M19-S3 | M26 supplies the partition/reset hypotheses (`lem-maincb-binary-block-merge.md:4`); M19-S3 exports `t_3=W.K3*epsilon`, the target record, domination, and the M12 raw datum (`stage3-call-envelope/export.md:5,87-97,123-169`). | **PASS** |
| M19-S3 -> M12 | M19-S3 exports `t_3<=W.e_cross`, all datum errors `<=t_3`, and application of M12 (`:135-169`). | **PASS** |
| Same M12 input -> bridge | The bridge repeats M12's inputs, uses the same bridge-selected valid M12 pair, and re-derives bijectivity of the deterministic maps. | **PASS after F2-F3** |
| Bridge property -> typed M17 | Corrected M17 asks for the plain bijectivity property; merge and unit control then yield the claimed isomorphism and unit estimate. | **PASS locally** |
| M26 access to bridge | M26 has no direct bridge dependency, and transitive dependencies are not provisioned. | **FAIL as designed; fixed only by F1's M26 deps amendment** |

Therefore the advertised
`M26 -> M19-S3 -> (M12 + bridge) -> M17` chain is **not dischargeable under the
proposed exact package**. With F1-F3 applied, it is interface-dischargeable.
M18, M20, M26, and M17 remain `stated/seeded`; this audit establishes no T0
conclusion for those rows.

## 5. T0, definition, provenance, budget, and red-test checks

- M12, M19-S3, outer transfer, zero corners, the compcb rows, four-corner
  merge, and unit control remain byte-unchanged T0. F1 changes only seeded
  M17's contract and seeded M26's dependency metadata. F2-F3 affect only the
  proposed new row. **No T0 invalidation.**
- Existing locked definitions suffice. F2 uses the canonical direct-sum corner
  identification explicitly; **no definition amendment** is required.
- The pinned source has SHA256
  `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`,
  matching `refs/manifest/checksums.sha256:4` and
  `refs/manifest/sources.lock.json:33-34`. Relevant literal loci are
  `approximate_algebras.tex:443-455,1054-1082,1325-1359,1363-1369,1477-1484,1542-1544`.
- The bridge's **7 nodes / 3 rounds / cap 11** and M17's clean **6 nodes / 2
  rounds / cap 9** are credible after the corrections. M26 needs an explicit
  bridge-application step; its existing cap 13 remains adequate, though its
  target should be recorded as 10 rather than 9 nodes.
- The retained exact countermodel (`B=C oplus C`,
  `A_R=M_2(C) oplus M_2(C)`) is valid and remains the correct red test: deleting
  the plain bijectivity premise makes M17 false. It is not a positive-tree node.

## 6. Verdict per row

| Row | Verdict | Reason |
|---|---|---|
| `lem-maincb-cross-datum-bijectivity` | **VALID-WITH-CORRECTIONS** | Same-datum and witness shrinking are sound; apply F2's diagonal source typing and F3's complete direct imports. |
| Typed M17 (`lem-maincb-stage3-raw-merge`) | **VALID-WITH-CORRECTIONS** | Analytic proof and sign-safe unit chain close; replace the certificate anaphor by the plain bijectivity property as in F1. |

**Disposition: DESIGN-REFUTED, not ROUTE-ALARM.** The exact package omits the
M26 dependency mutation required by its own discharge chain. Applying F1-F3
would make the route viable without changing any definition or frozen T0 row,
but that corrected package requires one additional seeded-row metadata change.
