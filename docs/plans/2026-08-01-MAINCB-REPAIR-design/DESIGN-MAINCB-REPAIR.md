# DESIGN — MAIN-CB two-defect interface repair

**Date:** 2026-08-01  
**Status:** DESIGN ONLY; non-rigorous until hostile audit and user ratification  
**Scope:** repair the missing reset-unit thread and the MAIN-CB anaphoric-witness ledger; no registry, proof, report, or script mutation  
**Verdict:** both defects are contract-level and are design-closable without changing a banked T0 contract. Use explicit contract clauses for unit control, one new data-only definition, one new scalar-arithmetic row, and a rebound M18 analytic ledger.

This document was designed from every item in the brief's Materials list, including the literal current shards, the two parked `af` ledgers, the EXT-CB export, and the pinned TeX source. It is not a proof and makes no rigour promotion.

Throughout the explanatory text only, write
\[
 q(v:B\to A):=\lVert v(I_B)-u_A\rVert .
\]
The registry contracts below spell this norm out and do not introduce `q` as a naked registry symbol. The repaired induction carries two parallel invariants for every current reset state:
\[
 \mathrm{RI}(R): d_R\le W.c0_{cb}\,\varepsilon_R,
 \qquad
 \mathrm{UI}(R): q(v_R)\le W.c0_{cb}\,\varepsilon_R.
\]

## 1. Unit-clause thread design

### 1.1 Decision: contract clauses only

Do **not** amend `def-maincb-reset-state`. Add explicit unit hypotheses and conclusions to the affected result contracts.

The trade-off is:

| Choice | Benefit | Cost | Verdict |
|---|---|---|---|
| Amend `def-maincb-reset-state` | The unit invariant becomes structurally inseparable from a reset state. | It changes the meaning imported by banked M07/M08 and every existing reset-state workspace; frozen T0 contracts and external snapshots would require revalidation. It also turns a data carrier into an analytic assertion. | Reject. |
| Explicit contract clauses | Leaves the canonical reset-state data and every T0 contract byte-stable; permits raw and improved unit bounds to have different coefficients; matches the audit-v3/v4 interface style. | Every producer and composition consumer must mention `UI` explicitly. | Adopt. |

The apparent extra verbosity is a useful audit property: a merge cannot silently forget its unit estimate. No consumer is left unable to discharge its obligation once M16, M17, M19-S1, M19-R, and M21--M28 are rebound as below.

### 1.2 Thread map

| Row | Unit role | Incoming estimate | Outgoing estimate / use | Design consequence |
|---|---|---|---|---|
| M12 `lem-maincb-cross-class-merging-datum` | Consumer | `q(v_U),q(v_V) <= t` | Supplies the diagonal-unit fields of `def-four-corner-merging-datum`; conclusion otherwise unchanged. | Add both hypotheses and the mandatory `lem-maincb-compressed-corner-unit-comparison` dependency. |
| M14 `lem-maincb-initial-raw-inclusion` | Frozen raw producer | Scalar map has exact unit value, hence raw `q=0`. | Feeds M19-R. | No contract amendment; use the literal scalar map in the new ledger proof. |
| M15 `lem-maincb-stage1-raw-refinement` | Frozen inclusion producer | Producer maps and complementarity data. | M19-S1 computes the literal sum map's raw unit bound without strengthening M15. | No T0 amendment; the bridge lives in M19-S1. |
| M16 `lem-maincb-stage2-raw-extension` | Raw producer | Closed EXT datum. | Output `v_+` satisfies both `d(v_+) <= D_2 t` and `q(v_+) <= D_2 t` after monotone enlargement of `D_2`. | Amend output and depend on mandatory `lem-maincb-isomorphism-unit-control`; do not cite EXT proof children as contracts. |
| M17 `lem-maincb-stage3-raw-merge` | Raw producer | Four-corner datum, including its diagonal-unit fields. | Merged raw isomorphism satisfies both bounds with `D_3 t`. | Amend output and use the same mandatory isomorphism-unit row. |
| M19-S1 `lem-maincb-stage1-call-envelope` | Raw bridge | Global input map has its unit clause. | Literal Stage-1 sum map satisfies a raw unit bound with the enlarged `D_1`. | Add explicit raw-unit conclusion; use the mandatory compressed-corner-unit comparison for the old side; M15 stays frozen. |
| M19-S2 `lem-maincb-stage2-call-envelope` | Reset consumer | Add `UI(U)` to the supplied reset state. | EXT datum passes to M16; no separate output state. | The current M13 front end does not consume the estimate explicitly, but carrying it prevents an inductive interface hole and costs no T0 change. |
| M19-S3 `lem-maincb-stage3-call-envelope` | Reset consumer / forwarder | `UI(U)` and `UI(V)`. | Since `epsilon_U,epsilon_V <= W.L*epsilon` and `W.K3 >= W.c0_cb*W.L`, both unit errors are at most `t_3`, exactly the M12 hypotheses. | Amend hypotheses and forwarding conclusion. |
| M19-R `lem-maincb-reset-invariant-preservation` | Raw-to-reset normalizer | Raw `d` and raw `q` are both at most `D t`. | Outputs both `RI(R)` and `UI(R)` using M02 plus the third clause of `prop_delta_hominc`. | Amend input/output; register the existing byte-matched GT external verbatim. |
| M21 `lem-maincb-initial-reset-inclusion` | Global reset producer | M14 raw unit, then M19-R. | Global inclusion satisfies `RI` and `UI`. | Amend output. |
| M22 `lem-maincb-maximal-reset-selection` | Selection consumer | M21 makes the set of globally `RI+UI` inclusions nonempty. | Chooses maximum source dimension in that set. | Quantify over maps satisfying both estimates. |
| M23 `lem-maincb-stage1-strict-refinement` | Global reset producer | Globally `RI+UI` input and M19-S1 raw unit. | M19-R returns a globally `RI+UI` inclusion of larger source dimension. | Amend input and output. |
| M24 `lem-maincb-stage1-maximality` | Maximality consumer | Maximum is taken in the same `RI+UI` class as M22/M23. | Concludes every atomic image is one-dimensional. | Amend the selected class; no definition change. |
| M25 `lem-maincb-one-class-extension` | Local reset producer | Global `RI+UI`; scalar base and repeated M16 outputs normalized by M19-R. | Per-class reset state has `RI(C)` and `UI(C)`. | Amend input/output. |
| M26 `lem-maincb-binary-block-merge` | Local reset consumer / producer | Two reset states with `RI+UI`. | M19-S3 -> M12 -> M17 -> M19-R gives merged `RI+UI`. | Amend inputs/output. |
| M27 `lem-maincb-stage3-finite-recombination` | Iterated merge | Every initial class state has `RI+UI`. | Every intermediate and final state has the same two invariants, without coefficient accumulation because M19-R resets after each binary merge. | Amend inputs/output. |
| M28 `lem-maincb-structural-assembly` | Final consumer / output | M22--M27 maintain global/local `UI`. | Final isomorphism satisfies both defect and unit estimates with `C_struct*epsilon`. | Amend conclusion explicitly. |

### 1.3 Mandatory modular unit helpers

The parked ledgers show that two bridge facts must be registry contracts, not proof-child citations or contingencies. They are ordinary result rows, not definitions, and both require fresh `af` elevation.

`lem-maincb-isomorphism-unit-control`
```text
contract: There are universal C_iso_unit < infinity and e_iso_unit > 0 such that if B is a finite-dimensional C*-algebra, A is a finite-dimensional extended epsilon-C*-algebra, and v:B->A is an extended delta-isomorphism with 0 <= delta+epsilon <= e_iso_unit, then ||v(I_B)-I_A|| <= C_iso_unit*(delta+epsilon); the witnesses are independent of dimension, amplification, block data, and the particular source and target.
```

This is an original surjectivity/lower-bound consequence: multiplication by `v(I_B)` is close to the identity on the range, the range is all of `A`, and the approximate target unit then gives the displayed estimate. It is not inferred from the third clause of `prop_delta_hominc` and does not need an a priori unit-nearness hypothesis. Proposed defs: `def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion`. Proposed deps: none. Provenance: the literal axioms at `approximate_algebras.tex:430-455` and the related unit argument at `:1194-1222`. Budget: 6/3/10.

`lem-maincb-compressed-corner-unit-comparison`
```text
contract: There are universal C_corner_unit < infinity and e_corner_unit > 0 such that both of the following hold: if P is a t-projection in a finite-dimensional extended t-C*-algebra A with 0 <= t <= e_corner_unit, then the compressed-corner unit u_{S_P}=Co_P(P) satisfies ||I_n tensor u_{S_P}-I_n tensor P|| <= C_corner_unit*t for every n >= 1; and, under the hypotheses of lem-maincb-outer-compression-transfer with 0 <= t <= e_corner_unit, if ||v(I_B)-u_{S_P}|| <= t then its explicit outer-compressed map T=Co^{A_R}_{P^R} o Co^A_R o v satisfies ||T_n(I_n tensor I_B)-I_n tensor P^R|| <= C_corner_unit*t for every n >= 1.
```

This is the exact shard-permitted bridge demanded by the M12 parked ledger. Its first clause also supplies the old-side unit calculation in M19-S1; the fresh two-point map already satisfies `v^(2)(1,1)=I` in its frozen contract. Proposed defs: `def-compressed-corner; def-delta-projection; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-operator-space`. Proposed deps: `lem-maincb-outer-compression-transfer; lem-compcb-amplified-compression; lem-compcb-amplified-compression-identities; lem-compcb-compressed-unit-action; lem-compcb-compressed-unit-norm`. Provenance: `approximate_algebras.tex:1054-1082,1435-1441,1542-1544`. Budget: 7/3/11.

`def-extended-delta-inclusion` is not used as a substitute for this thread. Even where a lower-level source convention contains a unit condition, the repaired interfaces export the exact norm needed by the four-corner datum.

## 2. Proposed `def-maincb-witness-ledger`

### 2.1 Full proposed shard content

This is the sole new definition and is a user-ratification item. Before ratification it must remain `draft`; the landing commit may change it to `locked` only with the ratification locus recorded.

```markdown
---
id: def-maincb-witness-ledger
term: MAIN-CB witness ledger
aliases: MAIN witness tuple; MAIN-CB constants tuple
kind: original
status: draft
source: internal
locus: DESIGN-MAINCB-REPAIR.md sect 2 (hostile-audit and user-ratification candidate, 2026-08-01)
sha256: -
consensus: pending fresh hostile audit and user ratification
---

**Statement (data and typing only).** A *MAIN-CB witness ledger* is a tuple W of twelve named real scalar fields
$$
W=(c0_{cb},L,K1,K2,K3,K_{call},e_{env},e1,e_{s2},e_{cross},r_{reset},epsilon_{MAIN}).
$$
The first five fields are receiving coefficients, the sixth is a derived coefficient, the next four are receiving margins, and the last two are derived scales.

**Notes / provenance.** Pure data: this shard contains no inequality between fields, no existence, uniqueness, estimate, map, regularity, admissibility, or dimension-freeness assertion. The analytic-witness relation and scalar arithmetic are exported only by `lem-maincb-witness-arithmetic` and `lem-maincb-reset-constant-ledger`. This is the MAIN-CB instance of the typed-witness pattern in `def-stage1-polar-witness-data` and `DESIGN-S1-POLAR-v6.md` sects 2--3 and 8, motivated by `docs/LEARNINGS.md` 2026-07-28 laws (i)--(ii). Related: [[def-maincb-reset-state]], [[def-maincb-raw-call]], [[def-maincb-partition-state]].
```

### 2.2 Field typing and role

| Field | Type | Role | Provider / receiving rule |
|---|---|---|---|
| `c0_cb` | real scalar; coefficient slot | Common coefficient for global/local `RI` and `UI`. | Receive an enlargement of M03's `c_0^cb`, M02's `K_floor`, and `C_unit*(K_floor+1)` from the near-unit clause. |
| `L` | real scalar; coefficient slot | Direct-corner envelope coefficient. | Receive an enlargement of M04's `L` after `c0_cb` is fixed. |
| `K1` | real scalar; coefficient slot | Stage-1 call multiplier. | Receive an enlargement of the M19-S1 provider. |
| `K2` | real scalar; coefficient slot | Stage-2 call multiplier. | Receive an enlargement with `K2 >= max{1,L,c0_cb*L}`. |
| `K3` | real scalar; coefficient slot | Stage-3 call multiplier. | Receive an enlargement with `K3 >= max{1,L,c0_cb*L}`; this inequality forwards `UI` to M12. |
| `K_call` | real scalar; derived-coefficient slot | One comparison coefficient for all five call scales and the final corner-unit telescope. | Derived by the arithmetic row as `max{1,L+1,c0_cb,K1,K2,K3}`. |
| `e_env` | real scalar; margin slot | Direct-corner envelope domain. | Receive a shrinking of M04's margin and any global-envelope prerequisites. |
| `e1` | real scalar; margin slot | Stage-1 producer/raw-call margin. | Receive a shrinking of M15's `e_1` and every M19-S1 producer prerequisite. |
| `e_s2` | real scalar; margin slot | Stage-2 datum/raw-call margin. | Receive a shrinking of M13/M16 thresholds. |
| `e_cross` | real scalar; margin slot | Stage-3 datum/raw-call margin. | Receive a shrinking of M12/M17 thresholds. |
| `r_reset` | real scalar; derived-scale slot | Uniform raw-to-reset admissibility radius. | Derived as a finite minimum after all raw coefficients and M19-R/GT witnesses are fixed. |
| `epsilon_MAIN` | real scalar; derived-scale slot | Global induction radius. | Derived last as a finite minimum comparing every call scale with its provider margin and `r_reset`. |

The tuple deliberately omits provider-local constants `D_0,...,D_3`, `C_s2`, `C_cross`, `K_disp`, `K_floor`, `e_sim`, `e_full`, and the GT near-unit witnesses `C_unit,epsilon_unit,delta_unit,a_unit`. M18 fixes those analytic witnesses first; the tuple stores only the names transported downstream. Adding provider internals to the data tuple would recreate the polar overbinding problem and is unnecessary.

## 3. Binder/arithmetic decision and verbatim contracts

### 3.1 Decision

Use **two rows**, as in the polar precedent:

1. Add `lem-maincb-witness-arithmetic`, a small finite-max/min calculation over already fixed provider witnesses.
2. Rebind M18 `lem-maincb-reset-constant-ledger` as the analytic binder that fixes providers in dependency order and exports one compatible `def-maincb-witness-ledger` datum.

The transport rows M12, M16, M17, and M19-S1/S2/S3/R must **not** depend on M18: they quantify over an arbitrary ledger after fixing their provider witnesses. M18 may then depend on those parameterized rows and select one compatible tuple. This is the acyclic W93 pattern.

Provider order in M18 is:

1. M02 supplies `e_it,K_disp,K_floor`; M03 supplies `epsilon_max^cb,delta_max^cb,c0^0`; parameterized M19-R registers the GT external and exports `C_unit,epsilon_unit,delta_unit,a_unit` for the third clause of `prop_delta_hominc`.
2. Enlarge `c0_cb` to dominate `c0^0`, `K_floor`, and `C_unit*(K_floor+1)`.
3. With that receiving coefficient fixed, M04 supplies `L,e_env`; M06 and M10 supply `e_full,e_sim`.
4. M14--M17 and the parameterized M19 call envelopes supply `D_i` and their margins/coefficient bounds; M12 supplies its cross provider.
5. `lem-maincb-witness-arithmetic` takes the finite maximum/minimum and returns the twelve named fields; M18 records their analytic compatibility.

For fixed provider witnesses put
\[
 D_*:=\max\{1,D_0,D_1,D_2,D_3\},
\]
\[
 r_{reset}:=\min\left\{e_0,e_1,e_2,e_3,\varepsilon_{max}^{cb},\frac{\delta_{max}^{cb}}{D_*},\frac{e_{it}}{D_*+1},\varepsilon_{unit},\frac{\delta_{unit}}{\max\{1,K_{floor}\}},\frac{a_{unit}}{(1+K_{disp})D_*},\frac{1}{2(1+K_{disp})D_*}\right\},
\]
\[
 K_{call}:=\max\{1,L+1,c0_{cb},K_1,K_2,K_3\},
\]
\[
 \varepsilon_{MAIN}:=\min\left\{e_{env},\frac{e_1}{K_1},\frac{e_{s2}}{K_2},\frac{e_{cross}}{K_3},\frac{r_{reset}}{K_{call}},\frac{e_{sim}}{K_{call}},\frac{e_{full}}{K_{call}},\frac{1}{2\max\{1,c0_{cb}K_{call}\}}\right\}.
\]
Here `e_1,e_s2,e_cross` are the already-shrunk receiving margins, not new anaphors. Each denominator is positive because its provider is fixed first.

### 3.2 Verbatim one-line contracts

The following two lines are the registry candidates; each is one physical ASCII line.

`lem-maincb-witness-arithmetic`  
```text
contract: After first fixing positive finite universal provider witnesses D_0,D_1,D_2,D_3,e_0,e_1,e_2,e_3,epsilon_max^cb,delta_max^cb,e_it,K_disp,K_floor,epsilon_unit,delta_unit,a_unit,L,c0_cb,K_1,K_2,K_3,e_env,e_s2,e_cross,e_sim,e_full with K_2,K_3 >= max{1,L,c0_cb*L}, set D_* = max{1,D_0,D_1,D_2,D_3}; then there is a def-maincb-witness-ledger datum W whose fields satisfy W.r_reset = min{e_0,e_1,e_2,e_3,epsilon_max^cb,delta_max^cb/D_*,e_it/(D_*+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D_*),[2*(1+K_disp)*D_*]^{-1}}, W.K_call = max{1,L+1,c0_cb,K_1,K_2,K_3}, W.epsilon_MAIN = min{e_env,e_1/K_1,e_s2/K_2,e_cross/K_3,W.r_reset/W.K_call,e_sim/W.K_call,e_full/W.K_call,[2*max{1,c0_cb*W.K_call}]^{-1}}, and the remaining fields equal the correspondingly named receiving witnesses; in particular every field is positive, finite, universal, and independent of dimension, amplification, block data, class count, and stage index.
```

M18 `lem-maincb-reset-constant-ledger`  
```text
contract: After first fixing e_it,K_disp,K_floor from lem-maincb-improvement-iteration, epsilon_max^cb,delta_max^cb,c0^0 from lem-maincb-error-improvement, C_unit,epsilon_unit,delta_unit,a_unit from lem-maincb-reset-invariant-preservation, a valid enlarged c0 >= max{c0^0,K_floor,C_unit*(K_floor+1)}, L^0,e_env^0 from lem-maincb-direct-corner-envelope for this c0, e_full from lem-maincb-full-corner-identification, e_sim from lem-maincb-corner-equivalence, D_0,e_0 from lem-maincb-initial-raw-inclusion, D_1,e_1,K_1^0 from lem-maincb-stage1-call-envelope, C_s2^0,e_s2^0 from lem-maincb-stage2-extcb-datum, D_2,e_2 from lem-maincb-stage2-raw-extension, K_2^0 from lem-maincb-stage2-call-envelope, C_cross^0,e_cross^0 from lem-maincb-cross-class-merging-datum, D_3,e_3 from lem-maincb-stage3-raw-merge, and K_3^0 from lem-maincb-stage3-call-envelope, set D_* = max{1,D_0,D_1,D_2,D_3}; then there exists one def-maincb-witness-ledger datum W supplied by lem-maincb-witness-arithmetic with W.c0_cb=c0, W.L>=L^0, W.K1>=K_1^0, W.K2>=max{K_2^0,1,W.L,W.c0_cb*W.L}, W.K3>=max{K_3^0,1,W.L,W.c0_cb*W.L}, W.e_env<=e_env^0, W.e1<=e_1, W.e_s2<=min{e_s2^0,e_2}, and W.e_cross<=min{e_cross^0,e_3}, such that under the respective producer hypotheses at base scale 0 <= t <= W.r_reset and target ambient defect at most t, the literal maps u_0:C->A furnished by lem-maincb-initial-raw-inclusion and u_1:C^{m+1}->A furnished by lem-maincb-stage1-call-envelope with lem-maincb-stage1-raw-refinement are extended D_*t-inclusions, the literal maps u_2:M_{r+1}->A_R furnished by lem-maincb-stage2-call-envelope with lem-maincb-stage2-raw-extension and u_3:B_U oplus B_V->A_R furnished by lem-maincb-stage3-call-envelope with lem-maincb-stage3-raw-merge are extended D_*t-isomorphisms, and ||u_0(I_C)-I_A||,||u_1(I_{C^{m+1}})-I_A||,||u_2(I_{M_{r+1}})-u_{A_R}||,||u_3(I_{B_U oplus B_V})-u_{A_R}|| <= D_*t, so each satisfies the M02/M03 and near-unit thresholds and is eligible for lem-maincb-reset-invariant-preservation; all selected witnesses are universal and independent of dimension, amplification, block data, class count, and stage index.
```

The phrase “the near-unit clause of `prop_delta_hominc`” is backed by the exact external described in §4, not an unregistered theorem name.

## 4. Final contract table

All contract cells below are one physical line of flattened ASCII. “Changed” counts amendments to existing contracts; the arithmetic row is new. `W.field` is typed by `def-maincb-witness-ledger`. Later rows fix the particular `W` supplied by M18; pre-M18 rows fix provider witnesses first and quantify over receiving ledgers by monotonicity.

| ID | One-line contract | Defs | Deps | Exact provenance | Budget (nodes/rounds/cap) | Flag / reason |
|---|---|---|---|---|---|---|
| `lem-maincb-isomorphism-unit-control` (new) | `There are universal C_iso_unit < infinity and e_iso_unit > 0 such that if B is a finite-dimensional C*-algebra, A is a finite-dimensional extended epsilon-C*-algebra, and v:B->A is an extended delta-isomorphism with 0 <= delta+epsilon <= e_iso_unit, then ||v(I_B)-I_A|| <= C_iso_unit*(delta+epsilon); the witnesses are independent of dimension, amplification, block data, and the particular source and target.` | `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | none | TeX 430--455,1194--1222; original consequence of surjectivity, lower norm, multiplication, and target-unit axioms | 6/3/10 | New mandatory modular bridge for M16/M17. |
| `lem-maincb-compressed-corner-unit-comparison` (new) | `There are universal C_corner_unit < infinity and e_corner_unit > 0 such that both of the following hold: if P is a t-projection in a finite-dimensional extended t-C*-algebra A with 0 <= t <= e_corner_unit, then the compressed-corner unit u_{S_P}=Co_P(P) satisfies ||I_n tensor u_{S_P}-I_n tensor P|| <= C_corner_unit*t for every n >= 1; and, under the hypotheses of lem-maincb-outer-compression-transfer with 0 <= t <= e_corner_unit, if ||v(I_B)-u_{S_P}|| <= t then its explicit outer-compressed map T=Co^{A_R}_{P^R} o Co^A_R o v satisfies ||T_n(I_n tensor I_B)-I_n tensor P^R|| <= C_corner_unit*t for every n >= 1.` | `def-compressed-corner`; `def-delta-projection`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion`; `def-operator-space` | `lem-maincb-outer-compression-transfer`; `lem-compcb-amplified-compression`; `lem-compcb-amplified-compression-identities`; `lem-compcb-compressed-unit-action`; `lem-compcb-compressed-unit-norm` | TeX 1054--1082,1435--1441,1542--1544 | 7/3/11 | New mandatory shard-permitted bridge for M12/M19-S1. |
| `lem-maincb-witness-arithmetic` (new) | `After first fixing positive finite universal provider witnesses D_0,D_1,D_2,D_3,e_0,e_1,e_2,e_3,epsilon_max^cb,delta_max^cb,e_it,K_disp,K_floor,epsilon_unit,delta_unit,a_unit,L,c0_cb,K_1,K_2,K_3,e_env,e_s2,e_cross,e_sim,e_full with K_2,K_3 >= max{1,L,c0_cb*L}, set D_* = max{1,D_0,D_1,D_2,D_3}; then there is a def-maincb-witness-ledger datum W whose fields satisfy W.r_reset = min{e_0,e_1,e_2,e_3,epsilon_max^cb,delta_max^cb/D_*,e_it/(D_*+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D_*),[2*(1+K_disp)*D_*]^{-1}}, W.K_call = max{1,L+1,c0_cb,K_1,K_2,K_3}, W.epsilon_MAIN = min{e_env,e_1/K_1,e_s2/K_2,e_cross/K_3,W.r_reset/W.K_call,e_sim/W.K_call,e_full/W.K_call,[2*max{1,c0_cb*W.K_call}]^{-1}}, and the remaining fields equal the correspondingly named receiving witnesses; in particular every field is positive, finite, universal, and independent of dimension, amplification, block data, class count, and stage index.` | `def-maincb-witness-ledger` | none | finite max/min arithmetic; W93 pattern `DESIGN-S1-POLAR-v6.md` §§2--3,8 | 5/2/9 | New; factors scalar work out of M18. |
| M12 `lem-maincb-cross-class-merging-datum` | `After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding lem-maincb-direct-corner-envelope witnesses, and fixing the C_corner_unit,e_corner_unit witnesses of lem-maincb-compressed-corner-unit-comparison, there are universal C_cross^0 >= 1 and 0 < e_cross^0 <= e_corner_unit such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0 and W.e_cross <= e_cross^0, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state comes from a non-unital extended t-inclusion w:C^m->A with one-dimensional images P_j, has disjoint nonempty unions U,V sharing no class and R=U union V, and supplied current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V satisfy epsilon_U,epsilon_V,d_U,d_V <= t <= W.e_cross, d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= t, and ||v_V(I_{B_V})-u_{A_V}|| <= t, then lem-maincb-compressed-corner-unit-comparison and the nested-corner, outer-compression, and zero-cross-corner constructions form the explicit Stage-3 amplified four-corner datum in A_R with common defect rho <= C_cross^0*t.` | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-witness-ledger`; `def-four-corner-merging-datum`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion`; `def-delta-projection`; `def-one-dimensional-delta-projection`; `def-compressed-corner` | `lem-maincb-error-improvement`; `lem-maincb-direct-corner-envelope`; `lem-maincb-nested-corner-comparison`; `lem-maincb-outer-compression-transfer`; `lem-maincb-compressed-corner-unit-comparison`; `lem-maincb-cross-union-zero-corners`; `lem-compcb-corner-algebra`; `lem-compcb-amplified-compression`; `lem-compcb-amplified-compression-identities` | TeX 1054--1082,1325--1345,1358,1363--1369,1443 | 11/3/15 | Changed: adds two unit hypotheses, typed `c0`, and a mandatory modular corner-unit bridge. |
| M16 `lem-maincb-stage2-raw-extension` | `After first fixing the universal C_s2^0,e_s2^0 witnesses of lem-maincb-stage2-extcb-datum, C_ext,e_ext witnesses of conj-extcb, and C_iso_unit,e_iso_unit witnesses of lem-maincb-isomorphism-unit-control, there are universal D_2 < infinity and e_2 > 0 such that for every def-maincb-witness-ledger datum W with W.e_s2 <= min{e_s2^0,e_2}, C_s2^0*e_2 <= e_ext, and (C_ext+1)*C_s2^0*e_2 <= e_iso_unit, every explicit Stage-2 raw-call closed EXT-CB datum in A_R with total post-helper defect at most C_s2^0*t and 0 <= t <= W.e_s2 admits an extended D_2*t-isomorphism v_+:M_{r+1}->A_R satisfying ||v_+(I_{M_{r+1}})-u_{A_R}|| <= D_2*t.` | `def-maincb-raw-call`; `def-maincb-witness-ledger`; `def-extcb-datum`; `def-operator-space`; `def-extended-delta-inclusion` | `lem-maincb-stage2-extcb-datum`; `conj-extcb`; `lem-maincb-isomorphism-unit-control` | TeX 430--455,1194--1222,1378--1412,1435--1441 | 5/2/9 | Changed: modular isomorphism-unit dependency exports the raw unit bound. |
| M17 `lem-maincb-stage3-raw-merge` | `After first fixing the universal C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum, C_merge,a_merge witnesses of lem-extcb-four-corner-merge, and C_iso_unit,e_iso_unit witnesses of lem-maincb-isomorphism-unit-control, there are universal D_3 < infinity and e_3 > 0 such that for every def-maincb-witness-ledger datum W with W.e_cross <= min{e_cross^0,e_3}, (C_cross^0+1)*e_3 <= a_merge, and (C_merge*(C_cross^0+1)+1)*e_3 <= e_iso_unit, every amplified four-corner datum in A_R with common defect rho <= C_cross^0*t and target ambient defect epsilon_{A_R} <= t <= W.e_cross yields an extended D_3*t-isomorphism v:B_U oplus B_V->A_R satisfying ||v(I_{B_U oplus B_V})-u_{A_R}|| <= D_3*t.` | `def-maincb-raw-call`; `def-maincb-witness-ledger`; `def-four-corner-merging-datum`; `def-operator-space`; `def-extended-delta-inclusion` | `lem-maincb-cross-class-merging-datum`; `lem-extcb-four-corner-merge`; `lem-maincb-isomorphism-unit-control` | TeX 430--455,1194--1222,1325--1359,1443 | 5/2/9 | Changed: modular isomorphism-unit dependency exports the raw merged unit bound. |
| M19-S1 `lem-maincb-stage1-call-envelope` | `After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding lem-maincb-direct-corner-envelope witnesses, fixing the C_corner_unit,e_corner_unit witnesses of lem-maincb-compressed-corner-unit-comparison, and fixing the D_1^0,e_1^0 witnesses of lem-maincb-stage1-raw-refinement, there are universal receiving witnesses K_1^0 >= 1, D_1 >= D_1^0, and e_1 > 0 with e_1 <= min{e_1^0,e_corner_unit} and every Stage-1 producer prerequisite absorbed, such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0, W.K1 >= K_1^0, and W.e1 <= e_1, if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.e1/W.K1, w:C^m->A is a supplied extended W.c0_cb*epsilon-inclusion satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, and some P_j=w(e_j) has dim S_{P_j}>1, then the three Stage-1 producers, lem-maincb-compressed-corner-unit-comparison, and literal old-side compression furnish the explicit Stage-1 raw call at t_1=W.K1*epsilon whose literal map u_1:C^{m+1}->A is an extended D_1*t_1-inclusion and satisfies ||u_1(I_{C^{m+1}})-I_A|| <= D_1*t_1, with u_1 equal to the supplied fresh C^2-inclusion when m=1.` | `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-partition-state`; `def-maincb-witness-ledger`; `def-compressed-corner`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-direct-corner-envelope`; `lem-compcb-single-compression-transfer`; `lem-maincb-compressed-corner-unit-comparison`; `lem-stage1-rectified-nontrivial-projection`; `lem-stage1-original-complementary-pair`; `lem-stage1-fresh-two-point-inclusion`; `lem-maincb-stage1-raw-refinement`; `lem-maincb-error-improvement` | TeX 917--969,1054--1082,1352--1359,1419--1426 | 10/3/14 | Changed: typed providers, mandatory corner-unit bridge, and raw unit output. |
| M19-S2 `lem-maincb-stage2-call-envelope` | `After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding L^0,e_env^0 witnesses of lem-maincb-direct-corner-envelope, and fixing the C_s2^0,e_s2^0 witnesses of lem-maincb-stage2-extcb-datum, there is a universal K_2^0 >= 1 with every Stage-2 prerequisite absorbed such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0, W.L >= L^0, W.K2 >= max{K_2^0,1,W.L,W.c0_cb*W.L}, and W.e_s2 <= e_s2^0, if A is a finite-dimensional extended epsilon-C*-algebra, w:C^m->A is an extended W.c0_cb*epsilon-inclusion satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images, a supplied MAIN partition state for A,w has nonempty U contained in one equivalence class, j notin U in that same class, and R=U union {j}, 0 <= epsilon <= W.e_s2/W.K2, and a supplied current reset isomorphism v_U:M_{|U|}->A_U satisfies d_U <= W.c0_cb*epsilon_U and ||v_U(I_{M_{|U|}})-u_{A_U}|| <= W.c0_cb*epsilon_U, then epsilon_U,epsilon_R <= W.L*epsilon and t_2=W.K2*epsilon dominates all datum errors, so lem-maincb-stage2-extcb-datum furnishes the explicit Stage-2 EXT raw-call datum with total defect at most C_s2^0*t_2.` | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-witness-ledger`; `def-extcb-datum`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-error-improvement`; `lem-maincb-direct-corner-envelope`; `lem-maincb-stage2-extcb-datum` | TeX 1363--1412,1428--1441 | 7/3/11 | Changed: ledger binding and explicit carried local `UI`; no new analytic use of `UI`. |
| M19-S3 `lem-maincb-stage3-call-envelope` | `After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding L^0,e_env^0 witnesses of lem-maincb-direct-corner-envelope, and fixing the C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum, there is a universal K_3^0 >= 1 with every Stage-3 prerequisite absorbed such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0, W.L >= L^0, W.K3 >= max{K_3^0,1,W.L,W.c0_cb*W.L}, and W.e_cross <= e_cross^0, if A is a finite-dimensional extended epsilon-C*-algebra, w:C^m->A is an extended W.c0_cb*epsilon-inclusion satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images, a supplied MAIN partition state for A,w has disjoint nonempty unions U,V sharing no class and R=U union V, 0 <= epsilon <= W.e_cross/W.K3, and supplied current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V satisfy d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= W.c0_cb*epsilon_U, and ||v_V(I_{B_V})-u_{A_V}|| <= W.c0_cb*epsilon_V, then epsilon_U,epsilon_V,epsilon_R <= W.L*epsilon and t_3=W.K3*epsilon dominates all datum errors and both displayed unit norms, so lem-maincb-cross-class-merging-datum furnishes the explicit Stage-3 four-corner raw-call datum with rho <= C_cross^0*t_3.` | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-witness-ledger`; `def-four-corner-merging-datum`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-error-improvement`; `lem-maincb-direct-corner-envelope`; `lem-maincb-cross-class-merging-datum` | TeX 1325--1359,1428,1443 | 8/3/12 | Changed: ledger binding and unit forwarding to M12. |
| M19-R `lem-maincb-reset-invariant-preservation` | `After first fixing the universal e_it,K_disp,K_floor witnesses of lem-maincb-improvement-iteration and epsilon_max^cb,delta_max^cb,c0^0 witnesses of lem-maincb-error-improvement, there are universal 0 < C_unit < infinity and epsilon_unit,delta_unit,a_unit > 0 furnished by the third clause of prop_delta_hominc and its implicit quantifier convention such that, for every D >= 1 and every def-maincb-witness-ledger datum W with W.c0_cb >= max{c0^0,K_floor,C_unit*(K_floor+1)} and W.r_reset <= min{epsilon_max^cb,delta_max^cb/D,e_it/(D+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D),[2*(1+K_disp)*D]^{-1}}, every explicit raw call into an extended epsilon_R-C*-corner A_R at scale 0 <= t <= W.r_reset whose literal map u_R:B_R->A_R is an extended D*t-inclusion and satisfies ||u_R(I_{B_R})-u_{A_R}|| <= D*t and epsilon_R <= t admits an error-improved map v_R:B_R->A_R satisfying d_R <= W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}|| <= W.c0_cb*epsilon_R, preserving bijectivity when u_R is bijective and leaving the source, target corner, and amplification form unchanged.` | `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-partition-state`; `def-maincb-witness-ledger`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-improvement-iteration`; `lem-maincb-error-improvement`; GT external `GT-kitaev-prop-delta-hominc` | TeX 1192--1222,1256--1319,1435--1443,1557; reuse `proofs/lem-stage1-fresh-two-point-inclusion/externals/3404276169020d3b.json` | 8/3/12 | Changed: removes M18 cycle/anaphor and proves `RI+UI`. |
| M18 `lem-maincb-reset-constant-ledger` | `After first fixing e_it,K_disp,K_floor from lem-maincb-improvement-iteration, epsilon_max^cb,delta_max^cb,c0^0 from lem-maincb-error-improvement, C_unit,epsilon_unit,delta_unit,a_unit from lem-maincb-reset-invariant-preservation, a valid enlarged c0 >= max{c0^0,K_floor,C_unit*(K_floor+1)}, L^0,e_env^0 from lem-maincb-direct-corner-envelope for this c0, e_full from lem-maincb-full-corner-identification, e_sim from lem-maincb-corner-equivalence, D_0,e_0 from lem-maincb-initial-raw-inclusion, D_1,e_1,K_1^0 from lem-maincb-stage1-call-envelope, C_s2^0,e_s2^0 from lem-maincb-stage2-extcb-datum, D_2,e_2 from lem-maincb-stage2-raw-extension, K_2^0 from lem-maincb-stage2-call-envelope, C_cross^0,e_cross^0 from lem-maincb-cross-class-merging-datum, D_3,e_3 from lem-maincb-stage3-raw-merge, and K_3^0 from lem-maincb-stage3-call-envelope, set D_* = max{1,D_0,D_1,D_2,D_3}; then there exists one def-maincb-witness-ledger datum W supplied by lem-maincb-witness-arithmetic with W.c0_cb=c0, W.L>=L^0, W.K1>=K_1^0, W.K2>=max{K_2^0,1,W.L,W.c0_cb*W.L}, W.K3>=max{K_3^0,1,W.L,W.c0_cb*W.L}, W.e_env<=e_env^0, W.e1<=e_1, W.e_s2<=min{e_s2^0,e_2}, and W.e_cross<=min{e_cross^0,e_3}, such that under the respective producer hypotheses at base scale 0 <= t <= W.r_reset and target ambient defect at most t, the literal maps u_0:C->A furnished by lem-maincb-initial-raw-inclusion and u_1:C^{m+1}->A furnished by lem-maincb-stage1-call-envelope with lem-maincb-stage1-raw-refinement are extended D_*t-inclusions, the literal maps u_2:M_{r+1}->A_R furnished by lem-maincb-stage2-call-envelope with lem-maincb-stage2-raw-extension and u_3:B_U oplus B_V->A_R furnished by lem-maincb-stage3-call-envelope with lem-maincb-stage3-raw-merge are extended D_*t-isomorphisms, and ||u_0(I_C)-I_A||,||u_1(I_{C^{m+1}})-I_A||,||u_2(I_{M_{r+1}})-u_{A_R}||,||u_3(I_{B_U oplus B_V})-u_{A_R}|| <= D_*t, so each satisfies the M02/M03 and near-unit thresholds and is eligible for lem-maincb-reset-invariant-preservation; all selected witnesses are universal and independent of dimension, amplification, block data, class count, and stage index.` | `def-maincb-witness-ledger`; `def-maincb-raw-call`; `def-maincb-reset-state` | `lem-maincb-witness-arithmetic`; `lem-maincb-improvement-iteration`; `lem-maincb-error-improvement`; `lem-maincb-direct-corner-envelope`; `lem-maincb-full-corner-identification`; `lem-maincb-corner-equivalence`; `lem-maincb-cross-class-merging-datum`; `lem-maincb-initial-raw-inclusion`; `lem-maincb-stage1-raw-refinement`; `lem-maincb-stage2-extcb-datum`; `lem-maincb-stage2-raw-extension`; `lem-maincb-stage3-raw-merge`; `lem-maincb-stage1-call-envelope`; `lem-maincb-stage2-call-envelope`; `lem-maincb-stage3-call-envelope`; `lem-maincb-reset-invariant-preservation` | finite arithmetic; TeX loci inherited from providers | 12/3/16 | Changed: explicit analytic tuple binder restricted to named producer maps, with D_* bound on-line. |
| M20 `lem-maincb-structural-domain-ledger` | `Fix the def-maincb-witness-ledger datum W together with the compatible e_sim,e_full provider witnesses fixed by lem-maincb-reset-constant-ledger; then 0 <= epsilon <= W.epsilon_MAIN implies epsilon <= W.e_env, epsilon <= W.e1/W.K1, epsilon <= W.e_s2/W.K2, and epsilon <= W.e_cross/W.K3, while the global scalar scale epsilon, atomic scalar scale W.K_call*epsilon, and Stage-1, Stage-2, and Stage-3 scales W.K1*epsilon,W.K2*epsilon,W.K3*epsilon are all at most W.K_call*epsilon <= W.r_reset,e_sim,e_full; every atomic corner defect is at most W.L*epsilon <= W.K_call*epsilon and W.c0_cb*W.K_call*epsilon <= 1/2.` | `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-partition-state`; `def-maincb-witness-ledger` | `lem-maincb-error-improvement`; `lem-maincb-direct-corner-envelope`; `lem-maincb-full-corner-identification`; `lem-maincb-corner-equivalence`; `lem-maincb-reset-constant-ledger`; `lem-maincb-stage1-call-envelope`; `lem-maincb-stage2-call-envelope`; `lem-maincb-stage3-call-envelope` | finite max/min arithmetic | 7/3/11 | Changed: all comparison constants are fields of one typed datum. |
| M21 `lem-maincb-initial-reset-inclusion` | `Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN admits an extended W.c0_cb*epsilon-inclusion v:C->A satisfying ||v(I_C)-I_A|| <= W.c0_cb*epsilon.` | `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-witness-ledger`; `def-operator-space`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-initial-raw-inclusion`; `lem-maincb-reset-invariant-preservation`; `lem-maincb-structural-domain-ledger` | TeX 430--455,1194--1222,1317--1319,1417 | 5/2/9 | Changed: ledger binding and global unit output. |
| M22 `lem-maincb-maximal-reset-selection` | `Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= W.epsilon_MAIN, then the nonempty set of m admitting an extended W.c0_cb*epsilon-inclusion w:C^m->A with ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon has a maximum because the lower norm is positive and m <= dim_C A.` | `def-maincb-reset-state`; `def-maincb-witness-ledger`; `def-projection-basis`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-structural-domain-ledger`; `lem-maincb-initial-reset-inclusion` | TeX 1417 | 5/2/9 | Changed: maximal class is the `RI+UI` class. |
| M23 `lem-maincb-stage1-strict-refinement` | `Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= W.epsilon_MAIN and an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfies ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon and has some P_j=w(e_j) with dim S_{P_j}>1, then there is an extended W.c0_cb*epsilon-inclusion w_+:C^{m+1}->A satisfying ||w_+(I_{C^{m+1}})-I_A|| <= W.c0_cb*epsilon.` | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-witness-ledger`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-stage1-call-envelope`; `lem-maincb-stage1-raw-refinement`; `lem-maincb-reset-invariant-preservation`; `lem-maincb-structural-domain-ledger` | TeX 917--969,1194--1222,1419--1426 | 8/3/12 | Changed: refinement preserves the selected `RI+UI` class. |
| M24 `lem-maincb-stage1-maximality` | `Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= W.epsilon_MAIN and w:C^m->A has maximum source dimension among all extended W.c0_cb*epsilon-inclusions satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, then every projection-basis image P_j=w(e_j) satisfies dim S_{P_j}=1.` | `def-maincb-partition-state`; `def-maincb-witness-ledger`; `def-projection-basis`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-maximal-reset-selection`; `lem-maincb-stage1-strict-refinement` | TeX 1417--1426 | 4/2/8 | Changed: maximality refers to exactly M22's repaired class. |
| M25 `lem-maincb-one-class-extension` | `Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, all atomic images are one-dimensional, and C is one equivalence class, then there is a current reset isomorphism v_C:M_{|C|}->A_C satisfying d_C <= W.c0_cb*epsilon_C and ||v_C(I_{M_{|C|}})-u_{A_C}|| <= W.c0_cb*epsilon_C; moreover epsilon_C <= W.K_call*epsilon.` | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-witness-ledger`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-direct-corner-envelope`; `lem-maincb-corner-equivalence`; `lem-maincb-initial-raw-inclusion`; `lem-maincb-stage2-raw-extension`; `lem-maincb-stage2-call-envelope`; `lem-maincb-reset-invariant-preservation`; `lem-maincb-structural-domain-ledger` | TeX 1378--1412,1430--1441 | 9/3/13 | Changed: ledger binding and per-class unit output from M16/M19-R. |
| M26 `lem-maincb-binary-block-merge` | `Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon and has disjoint nonempty unions U,V sharing no class, and current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V satisfy d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= W.c0_cb*epsilon_U, and ||v_V(I_{B_V})-u_{A_V}|| <= W.c0_cb*epsilon_V, then there is a current reset isomorphism v_{U union V}:B_U oplus B_V->A_{U union V} satisfying both d_{U union V} <= W.c0_cb*epsilon_{U union V} and ||v_{U union V}(I_{B_U oplus B_V})-u_{A_{U union V}}|| <= W.c0_cb*epsilon_{U union V}.` | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-raw-call`; `def-maincb-witness-ledger`; `def-four-corner-merging-datum`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-stage3-raw-merge`; `lem-maincb-stage3-call-envelope`; `lem-maincb-reset-invariant-preservation`; `lem-maincb-structural-domain-ledger` | TeX 1194--1222,1325--1359,1443 | 8/3/12 | Changed: consumes and produces composable unit estimates. |
| M27 `lem-maincb-stage3-finite-recombination` | `Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon and has classes C_1,...,C_q, and each initial current reset isomorphism v_{C_a}:B_{C_a}->A_{C_a} satisfies d_{C_a} <= W.c0_cb*epsilon_{C_a} and ||v_{C_a}(I_{B_{C_a}})-u_{A_{C_a}}|| <= W.c0_cb*epsilon_{C_a}, then there is a current reset isomorphism v:oplus_a B_{C_a}->A_{union_a C_a} satisfying d_{union_a C_a} <= W.c0_cb*epsilon_{union_a C_a} and ||v(I_{oplus_a B_{C_a}})-u_{A_{union_a C_a}}|| <= W.c0_cb*epsilon_{union_a C_a}.` | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-witness-ledger`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-structural-domain-ledger`; `lem-maincb-binary-block-merge` | TeX 1443 | 6/2/10 | Changed: binary unit invariant is explicitly iterated. |
| M28 `lem-maincb-structural-assembly` | `Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN admits a finite-dimensional C*-algebra B=oplus_C M_{|C|} and an extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A satisfying ||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon; hence C_struct=W.c0_cb*W.K_call and e_struct=W.epsilon_MAIN are finite positive universal witnesses.` | `def-maincb-partition-state`; `def-maincb-reset-state`; `def-maincb-witness-ledger`; `def-operator-space`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-full-corner-identification`; `lem-maincb-corner-equivalence`; `lem-maincb-structural-domain-ledger`; `lem-maincb-maximal-reset-selection`; `lem-maincb-stage1-maximality`; `lem-maincb-one-class-extension`; `lem-maincb-stage3-finite-recombination` | TeX 1414--1444 | 9/3/13 | Changed: ledger binding and final unit estimate. |

**Count:** 17 existing contracts are amended: M12, M16--M18, M19-S1/S2/S3/R, and M20--M28. Three result contracts are new: `lem-maincb-isomorphism-unit-control`, `lem-maincb-compressed-corner-unit-comparison`, and `lem-maincb-witness-arithmetic`. M13--M15 and all other T0 contracts remain byte-unchanged.

## 5. Definition-layer table

| Definition | Action | Role in repair | Ratification consequence |
|---|---|---|---|
| `def-maincb-witness-ledger` | Add exactly once, full draft in §2. | Typed names for all twelve formerly anaphoric constants/scales. | New `original` definition; user ratification required before locking. |
| `def-maincb-partition-state` | Reuse unchanged. | Carries the nonempty-subset-of-`J` partition and corner indexing. | Its 2026-07-30 amendment remains byte-stable. |
| `def-maincb-reset-state` | Reuse unchanged. | Data carrier for source, corner, and current map. | Avoids cascade into banked T0 consumers. |
| `def-maincb-raw-call` | Reuse unchanged. | Names the four raw call kinds. | Raw unit bounds are result clauses, not a datatype change. |
| `def-four-corner-merging-datum` | Reuse unchanged. | Its existing diagonal-unit field is discharged by repaired M12. | No weakening of the datum. |
| `def-extended-delta-inclusion` | Reuse unchanged. | Inclusion/isomorphism defect type. | It is not treated as exporting the required explicit reset-unit estimate. |
| `def-extcb-datum` | Reuse unchanged. | Stage-2 closed EXT input. | M16 exports an extra property of the constructed `v_+`. |
| `def-compressed-corner` | Reuse unchanged. | Provides the actual target corner unit in the M12 compression telescope. | No second “corner unit” definition. |
| `def-extended-epsilon-cstar-algebra` | Reuse unchanged. | Ambient/corner error typing. | No change. |
| `def-operator-space` | Reuse unchanged. | Amplified map norms. | No change. |
| `def-delta-projection`, `def-one-dimensional-delta-projection`, `def-projection-basis` | Reuse unchanged. | Projection and maximality interfaces. | No change. |

There is no second new definition. In particular, neither “unit-controlled reset state” nor “compatible ledger” becomes a definition: both are analytic predicates exported by result contracts.

## 6. Cascade and no-T0-invalidation check

### 6.1 Frozen MAIN rows

The current `status`/`af` headers and workspaces were checked for the complete frozen set. Verdicts:

| Row | Registry id | Current status | Repair verdict |
|---|---|---|---|
| M01 | `lem-maincb-improvement-one-step` | `proved / validated` | Unchanged; M19-R consumes it only through M02/M03. |
| M02 | `lem-maincb-improvement-iteration` | `proved / validated` | Unchanged; its displacement and floor witnesses are fixed by M18/M19-R. |
| M03 | `lem-maincb-error-improvement` | `proved / validated` | Unchanged; `c0^0` is received and enlarged monotonically. |
| M04 | `lem-maincb-direct-corner-envelope` | `proved / validated` | Unchanged; `L,e_env` are provider witnesses. |
| M05 | `lem-maincb-direct-sum-inclusion-merge` | `proved / validated` | Unchanged; M19-S1 proves the additional literal-map unit estimate outside M05/M15. |
| M06 | `lem-maincb-full-corner-identification` | `proved / validated` | Unchanged; `e_full` remains provider-local. |
| M07 | `lem-maincb-nested-corner-comparison` | `proved / validated` | Unchanged; principal reason not to amend `def-maincb-reset-state`. |
| M08 | `lem-maincb-nested-corner-dimension-transport` | `proved / validated` | Unchanged. |
| M09 | `lem-maincb-outer-compression-transfer` | `proved / validated` | Unchanged; M12 adds a proof-local corner-unit telescope from the literal compression construction. |
| M10 | `lem-maincb-corner-equivalence` | `proved / validated` | Unchanged; `e_sim` remains provider-local. |
| M11 | `lem-maincb-cross-union-zero-corners` | `proved / validated` | Unchanged. |
| M13 | `lem-maincb-stage2-extcb-datum` | `proved / validated` | Unchanged; M16 exports the unit property of EXT's constructed map. |
| M14 | `lem-maincb-initial-raw-inclusion` | `proved / validated` | Unchanged; literal scalar map has exact unit. |
| M15 | `lem-maincb-stage1-raw-refinement` | `proved / validated` | Unchanged; M19-S1 exports the literal sum map's unit estimate. |

The checked validated non-MAIN providers also remain unchanged: `conj-extcb`, `lem-extcb-four-corner-merge`, the COMP-CB rows used by M12, and the S1-ENDGAME workspace containing the GT registration. No byte-matched external in a validated workspace is altered.

The two unit helpers are additive new rows. `lem-maincb-isomorphism-unit-control` is proved from the existing algebra/isomorphism interfaces; `lem-maincb-compressed-corner-unit-comparison` consumes the frozen compression contracts. Neither requires amendment of the contracts it imports.

### 6.2 Workspace and external verdict

- `proofs/lem-maincb-cross-class-merging-datum/`: parked at 9/10; its root contract changes, so it must be re-seeded. No validated registry result depends on its pending root.
- `proofs/lem-maincb-stage1-call-envelope/`: parked at 15/17; its root contract changes, so it must be re-seeded. No validated registry result depends on its pending root.
- Seeded, unvalidated M16--M28 workspaces whose root strings change must also be re-seeded, never ledger-patched.
- Reuse the byte-matched JSON registration `proofs/lem-stage1-fresh-two-point-inclusion/externals/3404276169020d3b.json` in the fresh M19-R workspace. Its exact source is `refs/kitaev-2405.02434/approximate_algebras.tex:1192-1196`; the proof of the clause is 1198--1222. Copy the registration semantics verbatim; do not edit the validated source workspace.

**No-T0 verdict:** PASS at design level. The repair changes zero banked contracts, zero locked definitions already used by T0, and zero validated external snapshots.

## 7. Dimension-freeness and induction arithmetic

Every provider in the formulas is universal in its source contract. Finite maxima, positive finite minima, monotone enlargements, products, and quotients by positive universal witnesses remain universal. Consequently every field of `W` is independent of `dim A`, amplification level, block data, class count, equivalence-class size, merge-tree shape, and stage index.

The arithmetic sustaining the induction is:

1. For `epsilon <= W.epsilon_MAIN`,
   \[
   t_0=\varepsilon,\quad t_{atom}=W.K_{call}\varepsilon,\quad t_i=W.K_i\varepsilon\ (i=1,2,3)
   \]
   are all at most `W.K_call*epsilon <= W.r_reset`. The three stage scales also lie below `W.e1`, `W.e_s2`, and `W.e_cross`, respectively.
2. M04 gives `epsilon_R <= W.L*epsilon <= W.K_call*epsilon`. For a reset input,
   \[
   d_R,q(v_R)\le W.c0_{cb}\,\varepsilon_R\le W.c0_{cb}W.L\varepsilon.
   \]
   The choices `W.K2,W.K3 >= W.c0_cb*W.L` make these errors at most the Stage-2/3 base scale. In particular M19-S3 supplies the two M12 unit hypotheses.
3. Every raw producer has
   \[
   d_{raw},q(u_{raw})\le D_*t.
   \]
   The definition of `W.r_reset` gives `d_raw <= delta_max^cb`, `epsilon_R <= epsilon_max^cb`, and `d_raw+epsilon_R <= (D_*+1)t <= e_it`.
4. M02 supplies `||v-u_raw|| <= K_disp*d_raw` and `d(v) <= K_floor*epsilon_R`. Hence
   \[
   q(v)\le q(u_{raw})+K_{disp}d_{raw}\le(1+K_{disp})D_*t\le a_{unit}.
   \]
   Simultaneously `epsilon_R <= epsilon_unit` and `K_floor*epsilon_R <= delta_unit`, so the third clause of `prop_delta_hominc` and its implicit small-parameter convention apply and yield
   \[
   q(v)\le C_{unit}(K_{floor}+1)\varepsilon_R\le W.c0_{cb}\varepsilon_R,
   \]
   while `d(v) <= K_floor*epsilon_R <= W.c0_cb*epsilon_R`. The additional smallness term in `r_reset` also makes the M02 perturbation small enough for the finite-dimensional bijectivity-preservation argument used by M19-R.
5. M19-R normalizes after **each** Stage-2 extension and binary Stage-3 merge. Thus no factor proportional to class size or merge depth enters `RI` or `UI`; M27 iterates a fixed invariant rather than summing raw errors.
6. `W.c0_cb*W.K_call*epsilon <= 1/2` is retained exactly as the M20 comparison needed by the maximality and full-corner steps. At the final full union, M27 gives unit error at most `W.c0_cb*epsilon_J <= W.c0_cb*W.L*epsilon`, while the global partition map gives the remaining full-corner-to-ambient unit displacement at most `W.c0_cb*epsilon`; hence the final error is at most `W.c0_cb*(W.L+1)*epsilon <= W.c0_cb*W.K_call*epsilon`. This is why the repaired arithmetic uses `W.K_call >= W.L+1`. The final coefficient `C_struct=W.c0_cb*W.K_call` is universal.

This proves only consistency of the proposed scalar ledger, not the analytic result rows.

## 8. Re-seed guidance for the parked trees

These are calibration notes, not permission to transplant ledgers. Both workspaces receive fresh roots and fresh prover/verifier contexts.

### 8.1 M12, currently 9/10

Evidence: `proofs/lem-maincb-cross-class-merging-datum/ledger/`; verifier challenges `ch-911b...` (missing diagonal unit), `ch-be7f...` (root contradiction), `ch-41d...` (invalid coefficient substitution), and `ch-a333...` (missing bridge).

| Old node | Re-seed treatment |
|---|---|
| 1.2 geometry, 1.3 target algebra/projections, 1.4 diagonal maps, 1.5 zero maps, 1.6 complementarity | Statements survive verbatim after replacing the root parameters by fixed provider/ledger names; they remain the reusable mathematical spine. |
| 1.1 provider setup | Re-state with M03 providers fixed first and `W.c0_cb,e_cross` received monotonically. Do not reuse the old anaphoric binder. |
| 1.7 | Replace completely by a direct application of the already validated `lem-maincb-compressed-corner-unit-comparison` to the two new hypotheses; the helper, not a proof-child assertion, supplies the two diagonal-unit fields. |
| 1.8 | Re-prove the root assembly after the new 1.7 validates. |
| 1.7.1 and 1.9--1.11 | Preserve only as negative-test knowledge; their attempted unit substitutions are not proof nodes for the new tree. |

Expected new build: about 11 live nodes, three rounds, cap 15, after the compressed-unit helper is banked. The red test is to delete either incoming unit hypothesis or the helper import: the diagonal-unit node must fail.

### 8.2 M19-S1, currently 15/17

Evidence: `proofs/lem-maincb-stage1-call-envelope/ledger/`; verifier challenges `ch-249a...`, `ch-e2b...`, `ch-a5e...`, and `ch-a6be...` all identify the unbound `c0_cb` / typed-provider failure.

| Old node | Re-seed treatment |
|---|---|
| 1.2 geometry, 1.3 producers, 1.4 old-side compression | Mathematical statements survive after systematic renaming to the fixed provider witnesses and fields of arbitrary `W`; the old-side node additionally imports the banked compressed-unit helper. |
| 1.6.1.1 literal package | Its packaging content survives; extend the conclusion by summing the helper-controlled old-side unit and the fresh map's exact `v^(2)(1,1)=I` clause. |
| 1.1 binder family | Replace completely: fix M03, the compressed-unit helper, and M15 providers first, then quantify over receiving ledger fields. |
| 1.5/1.6 obstruction nodes and archived provider attempts | Do not reuse; they encode the forbidden cross-shard existential identification. |

Expected new build: about 10 live nodes, three rounds, cap 14. The red test is to remove the inequalities relating `W.c0_cb`, `W.K1`, or `W.e1` to their providers: the binder node must fail.

## 9. Serial landing and elevation order

No rows are elevated until the complete design has a fresh hostile audit and the user ratifies the new definition and contract package.

1. Land and lock `def-maincb-witness-ledger`; regenerate the definition index.
2. Land and elevate mandatory `lem-maincb-compressed-corner-unit-comparison`, then `lem-maincb-isomorphism-unit-control`, then `lem-maincb-witness-arithmetic`.
3. Land the parameterized M12 contract and re-seed/elevate M12 using the banked compressed-unit helper.
4. Land and elevate M16, then M17. Both use the banked isomorphism-unit helper; M17 also waits for M12.
5. Land the four parameterized transport rows and elevate serially: M19-S1, M19-S2, M19-S3, M19-R. M19-S1 uses the compressed-unit helper and is first because it is the second parked blocker; M19-S3 waits for M12; M19-R registers the reused GT external.
6. Rebind and elevate M18 after all of its explicitly named provider rows are banked; it selects the single tuple and binds `D_*` on-line.
7. Rebind and elevate M20, the sole downstream comparison ledger.
8. Elevate M21 then M22; elevate M23 then M24.
9. Elevate M25, then M26, then M27.
10. Elevate M28 last, using `W.K_call >= W.L+1` in the final unit telescope.

At every changed seeded workspace, discard/re-seed the root rather than editing an existing ledger. Regenerate the argument index/DAG and exercise the full gate at each atomic landing.

The later `lem-thmainext-conditional` rewire is **out of scope**. Hand off only after M28 is banked; its design must consume M28's final unit-controlled isomorphism without reopening this package.

## 10. Honest risk register

### 10.1 Per-row hostile-verifier attack surface

| Row | First hostile attack expected | Required decisive check |
|---|---|---|
| New isomorphism-unit helper | Surjectivity and lower norm do not yield a uniform bound for `v(I_B)-I_A` in an approximate target. | Write the multiplication-by-`v(I_B)` estimate for an arbitrary target element, then apply it to the target unit with every coefficient dimension-free. |
| New compressed-unit helper | `Co_P(P)` is confused with `P`, or the two outer compressions lose the incoming unit estimate. | Prove both clauses from exact amplified compression identities and the TeX 1054--1082 comparison; perturbing either clause must break M19-S1 or M12. |
| New arithmetic | A denominator or provider was not known positive before use. | Provider-order audit and symbolic recomputation of both minima. |
| M12 | Incoming reset-unit control still does not imply the diagonal unit of the **outer compressed** target corner. | Import the mandatory compressed-unit helper and check its explicit outer-compression clause; no substitution of `u_A` for `u_{A_U}`. |
| M16 | The EXT output's defect plus target ambient defect does not lie below `e_iso_unit`. | Check `(C_ext+1)*C_s2^0*t <= e_iso_unit` before applying the mandatory isomorphism-unit helper. |
| M17 | The merged output's defect plus target ambient defect does not lie below `e_iso_unit`. | Check `(C_merge*(C_cross^0+1)+1)*t <= e_iso_unit` before applying the same helper. |
| M19-S1 | A provider remains existential inside M03/M15, or the literal sum-map unit is inferred from frozen M15 without proof. | Providers first; separate one-node unit computation from the M15 inclusion import. |
| M19-S2 | The extra incoming `UI` is silently used to prove an EXT clause not present in M13. | Treat it as carried invariant only unless an explicit literal inequality is cited. |
| M19-S3 | `W.K3` fails to dominate `W.c0_cb*W.L`. | Check the exact two-line inequality forwarding both unit errors to M12. |
| M19-R | The M02-improved map, the bijective M03 output, and the map to which `prop_delta_hominc` is applied are not the same witness. | Construct one literal M02 iterate, prove its bijectivity under the ledger threshold, then apply the GT clause to that map. |
| M18 | Dependency cycle through a transport row, or an analytic provider is hidden in the tuple. | DAG check: M19 rows do not depend on M18; tuple fields remain data-only. |
| M20 | One of five scales is omitted or `L*epsilon` is not below the atomic/Stage-3 scale. | Mechanical comparison table using `K_call,K2,K3`. |
| M21 | M14's exact scalar unit is not linked to M19-R's raw-unit hypothesis. | Evaluate the literal scalar map at the domain unit. |
| M22 | The new `RI+UI` selection set could be empty. | Import repaired M21 verbatim before applying the dimension bound. |
| M23 | The larger map lands outside M22's selected class. | Verify both output estimates have exactly coefficient `W.c0_cb*epsilon`. |
| M24 | “Maximum” quantifies over the old defect-only class. | Byte-compare the class predicate with M22/M23. |
| M25 | Repeated Stage-2 calls lose unit control between extensions. | Induct M16 raw unit -> M19-R `UI` at every added atom. |
| M26 | The M12 hypotheses are only local `W.c0_cb*epsilon_U`, not at most `t_3`. | Invoke M04 and `W.K3 >= W.c0_cb*W.L` before M12. |
| M27 | Binary merging accumulates constants with class count. | Show every binary output is reset by M19-R before reuse; never sum improved unit errors. |
| M28 | The final corner-unit telescope costs `W.L+1`, not merely `W.L`. | Use M06 and the global `UI` estimate, then invoke the repaired `W.K_call >= W.L+1`. |

### 10.2 Top three ways this design could be wrong

1. **The new isomorphism-unit theorem could be false at the claimed uniform scale.** Its proposed proof uses bijectivity to transfer approximate left-unit action to every target element. If the inverse/lower-norm estimate or approximate target-unit axiom does not close with a universal coefficient, M16/M17 cannot export `UI`; stop rather than citing EXT proof children.
2. **The new compressed-corner comparison could be under-specified.** The first clause must be strong enough for the Stage-1 old-side unit and the second must match M09's exact two-compression map. A mismatch of corner units, amplification, or subordination hypotheses reopens both parked defects.
3. **M19-R witness identity/bijectivity could fail.** The near-unit argument must apply to the same M02 iterate that is retained as the reset isomorphism. If universal smallness does not prove bijectivity of that iterate from the raw isomorphism's lower norm, the present M19-R contract is not justified; stop and factor a new strengthened transport row rather than identifying it with M03's existential output. The additional per-row audit must still trace M19-S2 and M27 for any hidden unreset composition, which would introduce a class-count factor.

### 10.3 Escalation status

- **No missing reference:** every external analytic step used here is in the pinned TeX source. The only new GT registration is a verbatim reuse of the existing `prop_delta_hominc` external.
- **No T0 escalation:** no banked contract or locked existing definition needs amendment.
- **Required decisions before landing:** user ratification of the one new `original` definition, the 17 amended contracts, and the three new result contracts, after a fresh hostile design audit.
- **Mandatory bridge elevation:** both new unit helpers must validate before either parked tree is re-seeded; they are no longer conditional risks.
- **Conditional factoring escalation:** only the M19-R same-witness/bijectivity bridge remains conditional. It must not be silently absorbed if it exceeds the stated node budget.
