# DESIGN — `lem-thmainext-conditional` af elevation

**Status:** unaudited design only. This document proves nothing, changes no
registry/definition/workspace/status, leaves `lem-thmainext-conditional` at
`proved-mod-audit` / `af: none`, leaves T0 at 168, and leaves `op-classical`
OPEN. It is written for a separate fresh hostile audit.

## 1. Verdict and one-paragraph summary

**Verdict: YES — the frozen contract is derivable from the seven frozen T0
deps, subject to hostile confirmation of the precise Q-A reading below.** I
take Q-A route (1). The validated `lem-maincb-structural-assembly` external is
consumed as one theorem: its opening instruction fixes the ledger datum `W`
used by its construction, and its closing clause says that
`C_struct=W.c0_cb*W.K_call` and `e_struct=W.epsilon_MAIN` are finite positive
universal witnesses. Thus the external does not leave existence of `W` as a
new premise of this consumer. Fix that one `W` first, define
`C_E:=W.c0_cb*W.K_call` and `epsilon_E:=W.epsilon_MAIN`, and reuse M28's very
same `B` and `v`. The method clause is a separate, load-bearing obligation of
the root: three nested packet nodes explicitly consume the corrected COL-HILB
/ H-CB inputs, the four-corner / EXT-CB inputs, and the improvement / reset
inputs. No eighth import, no second `W`, no new threshold, and no reconstruction
of MAIN is used. If an auditor instead judges M28's opening words to be an
undischarged premise, this verdict fails: the exact minimal amendment is to add
`lem-maincb-reset-constant-ledger` to the frozen `deps:` line, after user
ratification, and then redesign; `lem-maincb-witness-arithmetic` need not also
be direct because it is already named and discharged by that provider.

## 2. Node-by-node skeleton

The intended live tree has nine nodes. The displayed order is binding: the
constant-choice/binder node is the root's first and only child. A child never
cites a pending sibling; the binder is checked only after all four of its
children are validated.

```text
THX-ROOT
└── THX-BIND
    ├── THX-M28
    ├── THX-HCB
    │   └── THX-COL
    ├── THX-EXT
    │   └── THX-MERGE
    └── THX-RESET
        └── THX-IMPROVE
```

### THX-ROOT — frozen root

**Exact statement:**

```text
Extended th_main_ext assembly: there are universal C_E < infinity and epsilon_E > 0 such that every finite-dimensional extended epsilon-C*-algebra A, for 0 <= epsilon <= epsilon_E, is carried by one extended C_E*epsilon-isomorphism v:B->A from a finite-dimensional C*-algebra; the assembly uses the corrected squared COL-HILB estimate and the hostile-verified H-CB (conj-hcb), EXT-CB (conj-extcb), and Stage-1 reset packets, with constants independent of dimension, amplification level, and block data.
```

- Parent: none. Children: `THX-BIND`.
- `defs:` `def-extended-epsilon-cstar-algebra`;
  `def-fd-cstar-diagonal` (the two frozen shard imports).
- `externals:` none directly.
- Constants: receives `C_E,epsilon_E` from `THX-BIND`.

### THX-BIND — one ledger witness, constants first, same final map

**Exact statement:**

```text
Consume THX-M28 as one validated theorem. Fix once the one def-maincb-witness-ledger datum W discharged by that theorem, and never reselect it. Define C_E:=W.c0_cb*W.K_call and epsilon_E:=W.epsilon_MAIN before any analytic packet is used. For every finite-dimensional extended epsilon-C*-algebra A with 0<=epsilon<=epsilon_E, take B and v to be the very same B and v furnished by THX-M28. The validated children THX-HCB, THX-EXT, and THX-RESET discharge the three method packets named by the frozen root, while THX-M28 supplies positivity, finiteness, universality, the final source and target, bijectivity, all amplifications, and the unit estimate. Hence these choices establish THX-ROOT with no dependence on dimension, amplification level, or block data.
```

- Parent: `THX-ROOT`. Children, in order: `THX-M28`, `THX-HCB`,
  `THX-EXT`, `THX-RESET`.
- `defs:` `def-maincb-witness-ledger`;
  `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion`.
- `externals:` none directly; it consumes only its validated children.
- Constants: fixes `W` once; introduces `C_E` and `epsilon_E`; consumes
  M28's `C_struct,e_struct` identities without choosing new witnesses.

### THX-M28 — typed final witness and universality

**Exact statement (byte-verbatim current contract):**

```text
Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN admits a finite-dimensional C*-algebra B=oplus_C M_{|C|} and an extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A satisfying ||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon; hence C_struct=W.c0_cb*W.K_call and e_struct=W.epsilon_MAIN are finite positive universal witnesses.
```

- Parent: `THX-BIND`. Children: none.
- `defs:` `def-maincb-partition-state`; `def-maincb-reset-state`;
  `def-maincb-witness-ledger`; `def-operator-space`;
  `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion`.
- `externals:` `lem-maincb-structural-assembly`.
- Constants: supplies the fixed `W`, `W.c0_cb`, `W.K_call`,
  `W.epsilon_MAIN`, and the aliases `C_struct,e_struct`. This is also the
  dedicated Q-C node: its final clause, not a fresh estimate, supplies
  universality and independence from all construction indices.

### THX-HCB — corrected H-CB packet

**Exact statement:**

```text
Fix C_col,e_col supplied by THX-COL and C_H,e_H supplied by conj-hcb. Whenever the fixed assembly invokes an H-CB datum at e=delta+epsilon<=min{e_col,e_H}, first apply THX-COL to that same datum, X, and amplification n, and then apply conj-hcb to the same Q,P,R,S and n. This supplies the corrected squared COL-HILB estimate together with the H-CB adjoint, product-defect, unit, upper-norm, homomorphism, canonical-identity, and stated conditional inverse conclusions at every amplification, with constants independent of n, dim A, block count, and block dimensions.
```

- Parent: `THX-BIND`. Children: `THX-COL`.
- `defs:` `def-hcb-datum`; `def-column-hilbert-corner`;
  `def-extended-epsilon-cstar-algebra`; `def-ha-map`;
  `def-delta-projection`; `def-one-dimensional-delta-projection`;
  `def-canonical-corner-identifications`.
- `externals:` `conj-hcb`.
- Constants: introduces/consumes `C_col,e_col,C_H,e_H`; local scale
  `e=delta+epsilon`. It never substitutes the known-false unsquared display.

### THX-COL — corrected squared estimate at its point of use

**Exact statement (byte-verbatim current contract):**

```text
Corrected amplified column-Hilbert estimate: there are universal C_col < infinity and e_col > 0 such that every H-CB datum with e <= e_col, every n >= 1, and every X in M_{n,1} tensor S_{P,Q} satisfy abs(<X,X>_n-||X||_{n,1}^2) <= C_col*e*||X||_{n,1}^2.
```

- Parent: `THX-HCB`. Children: none.
- `defs:` `def-hcb-datum`; `def-column-hilbert-corner`.
- `externals:` `lem-hcb-column-hilbert-squared`.
- Constants: supplies `C_col,e_col`; consumes local `e,n`.

### THX-EXT — same-map EXT-CB packet

**Exact statement:**

```text
Fix C_merge,a_merge supplied by THX-MERGE and C_ext,e_ext supplied by conj-extcb. For every EXT-CB datum used by the fixed assembly with e=delta+epsilon<=e_ext, route its four-corner substep through THX-MERGE on the same four fixed level-one corner maps whenever rho+epsilon<=a_merge, and route the completed datum through conj-extcb on the same P,Q,v and corners. The output is one map v_+:M_{r+1}->A whose same level-one unitary and same four corner maps control every amplification, with constants independent of r, n, dim A, and block data.
```

- Parent: `THX-BIND`. Children: `THX-MERGE`.
- `defs:` `def-extcb-datum`; `def-four-corner-merging-datum`;
  `def-compressed-corner`; `def-extended-epsilon-cstar-algebra`;
  `def-ha-map`; `def-delta-projection`; `def-extended-delta-inclusion`.
- `externals:` `conj-extcb`.
- Constants: introduces/consumes `C_merge,a_merge,C_ext,e_ext`; local
  `e=delta+epsilon,rho`. The node does not identify maps merely by notation.

### THX-MERGE — corrected total-defect four-corner merge

**Exact statement (byte-verbatim current contract):**

```text
Complete four-corner merge: there are universal C_merge < infinity and a_merge > 0 such that four fixed bijective level-one corner maps satisfying def-four-corner-merging-datum with common defect rho and rho+epsilon <= a_merge combine into one extended C_merge*(rho+epsilon)-isomorphism.
```

- Parent: `THX-EXT`. Children: none.
- `defs:` `def-extended-epsilon-cstar-algebra`;
  `def-extended-delta-inclusion`; `def-compressed-corner`;
  `def-four-corner-merging-datum`.
- `externals:` `lem-extcb-four-corner-merge`.
- Constants: supplies `C_merge,a_merge`; consumes `rho,epsilon`.

### THX-RESET — Stage-1 reset packet with literal map identity

**Exact statement:**

```text
Fix epsilon_max^cb,delta_max^cb,c0^0 from THX-IMPROVE and C_unit,epsilon_unit,delta_unit,a_unit from lem-maincb-reset-invariant-preservation, and retain the same W fixed by THX-BIND. For every Stage-1 raw call in the fixed assembly satisfying the displayed D,t,W and ambient-defect hypotheses of lem-maincb-reset-invariant-preservation, apply THX-IMPROVE to the literal raw map and apply lem-maincb-reset-invariant-preservation to that same call and same map. The resulting v_R has d_R<=W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}||<=W.c0_cb*epsilon_R, preserves bijectivity when the raw map is bijective, and leaves the source, target corner, and amplification family unchanged. This is the Stage-1 reset packet used by THX-BIND.
```

- Parent: `THX-BIND`. Children: `THX-IMPROVE`.
- `defs:` `def-maincb-reset-state`; `def-maincb-raw-call`;
  `def-maincb-partition-state`; `def-maincb-witness-ledger`;
  `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion`.
- `externals:` `lem-maincb-reset-invariant-preservation`.
- Constants: consumes `epsilon_max^cb,delta_max^cb,c0^0`, the encapsulated
  `e_it,K_disp,K_floor`, and the same `W`; supplies/consumes
  `C_unit,epsilon_unit,delta_unit,a_unit`; local `D,t,epsilon_R,d_R`.

### THX-IMPROVE — complete error improvement at reset use

**Exact statement (byte-verbatim current contract):**

```text
Complete error improvement: there are universal epsilon_max^cb>0, delta_max^cb>0 and c_0^cb<infinity such that every extended delta-inclusion v:B->A from a finite-dimensional C*-algebra B into an extended epsilon-C*-algebra A with 0<=epsilon<=epsilon_max^cb and 0<=delta<=delta_max^cb can be replaced by an extended c_0^cb*epsilon-inclusion v_tilde:B->A that is bijective whenever v is bijective.
```

- Parent: `THX-RESET`. Children: none.
- `defs:` `def-extended-epsilon-cstar-algebra`;
  `def-extended-delta-inclusion`.
- `externals:` `lem-maincb-error-improvement`.
- Constants: supplies `epsilon_max^cb,delta_max^cb,c_0^cb`; the selected
  witness is denoted `c0^0` by `THX-RESET`.

## 3. Witness/constant ledger

| Symbol(s) | Bound where | Provider clause / use |
|---|---|---|
| `W` | `THX-BIND`, once | `THX-M28`'s opening and closing clauses; never rebound. |
| `W.c0_cb,W.K_call,W.epsilon_MAIN` | Fields of that `W` | `THX-M28`; positive, finite, universal by its final clause. |
| `C_E:=W.c0_cb*W.K_call` | `THX-BIND`, after `W` | Receiving coefficient; exactly M28's `C_struct`. |
| `epsilon_E:=W.epsilon_MAIN` | `THX-BIND`, after `W` | Receiving radius; exactly M28's `e_struct`; not shrunk. |
| `C_struct,e_struct` | `THX-M28` | M28 aliases; consumed only to prove finiteness/positivity/universality of the two receiving constants. |
| `C_col,e_col` | `THX-COL` | Corrected squared COL-HILB provider. |
| `C_H,e_H` | `THX-HCB` | `conj-hcb`; uniform across amplification and block data. |
| `C_merge,a_merge` | `THX-MERGE` | Four-corner provider at total defect `rho+epsilon`. |
| `C_ext,e_ext` | `THX-EXT` | `conj-extcb`; one-map/all-amplifications output. |
| `epsilon_max^cb,delta_max^cb,c_0^cb` | `THX-IMPROVE` | Error-improvement provider; `THX-RESET` calls the selected coefficient `c0^0`. |
| `e_it,K_disp,K_floor` | Encapsulated at `THX-RESET` | Consumed inside the imported M19-R theorem's opening binder; not independently selected and not an extra external. |
| `C_unit,epsilon_unit,delta_unit,a_unit` | `THX-RESET` | Existence furnished by the M19-R external's stated `prop_delta_hominc` clause; no ground-truth re-derivation occurs here. |
| `e=delta+epsilon`, `rho`, `D,t,epsilon_R,d_R` | Local packet parameters | Quantified local scales/defects, not universal witness choices and not fields reselected from `W`. |

No other field of `W` is projected by the target tree. Its remaining fields
stay packaged in the one fixed datum; the design never manufactures a ledger
from separately named scalars.

## 4. Seeding package

### Root conjecture

Use this text byte-for-byte:

```text
Extended th_main_ext assembly: there are universal C_E < infinity and epsilon_E > 0 such that every finite-dimensional extended epsilon-C*-algebra A, for 0 <= epsilon <= epsilon_E, is carried by one extended C_E*epsilon-isomorphism v:B->A from a finite-dimensional C*-algebra; the assembly uses the corrected squared COL-HILB estimate and the hostile-verified H-CB (conj-hcb), EXT-CB (conj-extcb), and Stage-1 reset packets, with constants independent of dimension, amplification level, and block data.
```

### Unique `af def-add` list

Run each name exactly once against `proofs/lem-thmainext-conditional`:

```text
af def-add def-extended-epsilon-cstar-algebra --file definitions/def-extended-epsilon-cstar-algebra.md -d proofs/lem-thmainext-conditional
af def-add def-fd-cstar-diagonal --file definitions/def-fd-cstar-diagonal.md -d proofs/lem-thmainext-conditional
af def-add def-maincb-witness-ledger --file definitions/def-maincb-witness-ledger.md -d proofs/lem-thmainext-conditional
af def-add def-extended-delta-inclusion --file definitions/def-extended-delta-inclusion.md -d proofs/lem-thmainext-conditional
af def-add def-maincb-partition-state --file definitions/def-maincb-partition-state.md -d proofs/lem-thmainext-conditional
af def-add def-maincb-reset-state --file definitions/def-maincb-reset-state.md -d proofs/lem-thmainext-conditional
af def-add def-maincb-raw-call --file definitions/def-maincb-raw-call.md -d proofs/lem-thmainext-conditional
af def-add def-operator-space --file definitions/def-operator-space.md -d proofs/lem-thmainext-conditional
af def-add def-hcb-datum --file definitions/def-hcb-datum.md -d proofs/lem-thmainext-conditional
af def-add def-column-hilbert-corner --file definitions/def-column-hilbert-corner.md -d proofs/lem-thmainext-conditional
af def-add def-ha-map --file definitions/def-ha-map.md -d proofs/lem-thmainext-conditional
af def-add def-delta-projection --file definitions/def-delta-projection.md -d proofs/lem-thmainext-conditional
af def-add def-one-dimensional-delta-projection --file definitions/def-one-dimensional-delta-projection.md -d proofs/lem-thmainext-conditional
af def-add def-canonical-corner-identifications --file definitions/def-canonical-corner-identifications.md -d proofs/lem-thmainext-conditional
af def-add def-extcb-datum --file definitions/def-extcb-datum.md -d proofs/lem-thmainext-conditional
af def-add def-compressed-corner --file definitions/def-compressed-corner.md -d proofs/lem-thmainext-conditional
af def-add def-four-corner-merging-datum --file definitions/def-four-corner-merging-datum.md -d proofs/lem-thmainext-conditional
```

All seventeen files exist. `def-fd-cstar-diagonal` is provisioned because it
is on the frozen target `defs:` line; the nine-node proof does not invent a
diagonal argument merely to make that historical contract import appear busy.

### Exact `af add-external` entries

Each source value below contains the literal `proofs/<dep-id>` path and the
byte-verbatim current `contract:` value. Register each name once.

`conj-hcb` / `proofs/conj-hcb`:

```text
imports validated registry lemma proofs/conj-hcb — H-CB: there are universal C_H < infinity and e_H > 0 such that, whenever e=delta+epsilon <= e_H, Q is a level-one one-dimensional delta-projection in an extended epsilon-C*-algebra A, and P,R,S are delta-projections, the maps 1_{M_n} tensor Ha^Q_{P,R}, under the COL-HILB identification with operators on C^n tensor S_{R,Q} and C^n tensor S_{P,Q}, satisfy for every n the adjoint equality, product defect at most C_H*e*||Z||||W||, and the uniform unit, upper-norm, homomorphism, and canonical-identity closeness estimates required by lem_extension; moreover, if the level-one lower modulus of Ha^Q_{P,P} is at least 1/4, then every amplification has lower modulus at least 1-C_H*e, and if Ha^Q_{P,P} is also bijective at level one then every amplification is bijective with inverse norm at most 1+C_H*e; the analogous off-diagonal inverse bound for Ha^Q_{P,R} is asserted only when Ha^Q_{P,R} is bijective at level one and Ha^Q_{R,R} satisfies that diagonal lower-modulus hypothesis; all constants independent of n, dim A, block count, and block dimensions.
```

`conj-extcb` / `proofs/conj-extcb`:

```text
imports validated registry lemma proofs/conj-extcb — EXT-CB: there are universal C_ext < infinity and e_ext > 0 such that if e=delta+epsilon <= e_ext, P,Q are delta-projections in an extended epsilon-C*-algebra A with ||P+Q-I|| <= delta, v:M_r->S_P is an extended delta-isomorphism, dim S_Q=1 at level one, and S_{P,Q} is nonzero, then there is one map v_+:M_{r+1}->A whose every amplification is a C_ext*e-isomorphism; the same level-one unitary and the same four corner maps carry all amplification levels, with constants independent of r, n, and dim A.
```

`lem-hcb-column-hilbert-squared` / `proofs/lem-hcb-column-hilbert-squared`:

```text
imports validated registry lemma proofs/lem-hcb-column-hilbert-squared — Corrected amplified column-Hilbert estimate: there are universal C_col < infinity and e_col > 0 such that every H-CB datum with e <= e_col, every n >= 1, and every X in M_{n,1} tensor S_{P,Q} satisfy abs(<X,X>_n-||X||_{n,1}^2) <= C_col*e*||X||_{n,1}^2.
```

`lem-maincb-error-improvement` / `proofs/lem-maincb-error-improvement`:

```text
imports validated registry lemma proofs/lem-maincb-error-improvement — Complete error improvement: there are universal epsilon_max^cb>0, delta_max^cb>0 and c_0^cb<infinity such that every extended delta-inclusion v:B->A from a finite-dimensional C*-algebra B into an extended epsilon-C*-algebra A with 0<=epsilon<=epsilon_max^cb and 0<=delta<=delta_max^cb can be replaced by an extended c_0^cb*epsilon-inclusion v_tilde:B->A that is bijective whenever v is bijective.
```

`lem-maincb-reset-invariant-preservation` / `proofs/lem-maincb-reset-invariant-preservation`:

```text
imports validated registry lemma proofs/lem-maincb-reset-invariant-preservation — After first fixing the universal e_it,K_disp,K_floor witnesses of lem-maincb-improvement-iteration and epsilon_max^cb,delta_max^cb,c0^0 witnesses of lem-maincb-error-improvement, there are universal 0 < C_unit < infinity and epsilon_unit,delta_unit,a_unit > 0 furnished by the third clause of prop_delta_hominc and its implicit quantifier convention such that, for every D >= 1 and every def-maincb-witness-ledger datum W with W.c0_cb >= max{c0^0,K_floor,C_unit*(K_floor+1)} and W.r_reset <= min{epsilon_max^cb,delta_max^cb/D,e_it/(D+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D),[2*(1+K_disp)*D]^{-1}}, every explicit raw call into an extended epsilon_R-C*-corner A_R at scale 0 <= t <= W.r_reset whose literal map u_R:B_R->A_R is an extended D*t-inclusion and satisfies ||u_R(I_{B_R})-u_{A_R}|| <= D*t and epsilon_R <= t admits an error-improved map v_R:B_R->A_R satisfying d_R <= W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}|| <= W.c0_cb*epsilon_R, preserving bijectivity when u_R is bijective and leaving the source, target corner, and amplification form unchanged.
```

`lem-maincb-structural-assembly` / `proofs/lem-maincb-structural-assembly`:

```text
imports validated registry lemma proofs/lem-maincb-structural-assembly — Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN admits a finite-dimensional C*-algebra B=oplus_C M_{|C|} and an extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A satisfying ||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon; hence C_struct=W.c0_cb*W.K_call and e_struct=W.epsilon_MAIN are finite positive universal witnesses.
```

`lem-extcb-four-corner-merge` / `proofs/lem-extcb-four-corner-merge`:

```text
imports validated registry lemma proofs/lem-extcb-four-corner-merge — Complete four-corner merge: there are universal C_merge < infinity and a_merge > 0 such that four fixed bijective level-one corner maps satisfying def-four-corner-merging-datum with common defect rho and rho+epsilon <= a_merge combine into one extended C_merge*(rho+epsilon)-isomorphism.
```

There is **no ground-truth external** in this seed. The tree invokes M19-R as
an opaque validated external and performs no delta-homomorphism arithmetic.
Accordingly `GT-kitaev-def-delta-homomorphism` must not be registered merely
because it occurs in M28's internal proof. If a prover later introduces such
arithmetic, stop and cleanly re-seed with the byte-verbatim registration from
`proofs/lem-maincb-extended-inclusion-monotone/externals/`; do not patch a
running polluted seed.

## 5. Node-cap proposal

Expected live size is **9 nodes**; propose a **hard cap of 14**, with routine
tier and at most three build/repair rounds. The five-node margin permits a
verifier to split one packet's constant selection from its application or to
split final typing from universality, while remaining far below the repository
soft cap 26. A balloon past 14 is not permission to internalize MAIN. It means
one of: (i) Q-A was wrong and M28 left an inaccessible ledger premise; (ii) the
method clause cannot be connected to M28 from the seven contracts; (iii) a
listed definition was omitted at seed time; or (iv) a supposedly opaque T0
external is being re-proved. Classify first. Cases (i)–(ii) are contract/import
findings and must stop; (iii) requires a clean re-seed from this audited
package; (iv) requires pruning, not a cap increase.

## 6. Risk register for the hostile auditor

1. **Q-A / hidden eighth premise (highest risk).** Attack whether the M28 root
   is a closed theorem that supplies one usable `W`, or only a theorem after an
   unimported `W` has been supplied. A correct rejection is a contract-level
   stop. Minimal amendment: add only `lem-maincb-reset-constant-ledger` to the
   target deps after user ratification, then redesign; never smuggle it in as
   an external under the frozen line.
2. **Decorative audit branches.** Delete `THX-COL`, `THX-HCB`, `THX-MERGE`,
   `THX-EXT`, `THX-IMPROVE`, or `THX-RESET` in turn. The corresponding phrase
   of the root's method clause must become unproved. If the root still passes,
   the tree has not made that dep load-bearing and must be rejected.
3. **Missing provider-to-M28 trace.** The packet nodes are conditional
   interfaces; they do not assert unrecorded inequalities such as
   `W.epsilon_MAIN<=e_H`. Reject any proof that applies one directly to M28's
   data without its hypotheses. If the method clause is read as requiring
   those top-level applications rather than an explicit proof-tree route, the
   seven frozen contracts are insufficient and the design must stop rather
   than shrink `epsilon_E` or reconstruct MAIN.
4. **Witness and map identity.** Verify there is exactly one `W`, bound before
   `C_E,epsilon_E`, and that final `v:B->A` is M28's witness. Reject a second
   ledger selection, an M19-R map substituted for `v`, or an intermediate
   corner codomain renamed `A`.
5. **Reset same-map discipline.** In `THX-RESET`, the raw map improved by M03
   and the map carried by M19-R must be the literal maps covered by those
   contracts. Reject binder unification by repeated notation and reject any
   direct use of the undeclared M02/M18 ancestors.
6. **Squared/conditional clauses.** Check `THX-COL` has
   `C_col*e*||X||_{n,1}^2`, H-CB inverse bounds retain their level-one
   hypotheses, and merge uses `rho+epsilon<=a_merge`. Any unsquared or
   unconditional replacement is a genuine rejection.
7. **Universality leakage.** `C_E` and `epsilon_E` must be exactly the two M28
   field expressions, chosen after `W`; no minimum with newly selected packet
   thresholds and no dependence on `n`, dimension, class count, stage, or
   block data is allowed.
8. **Vocabulary/external hygiene.** Confirm all seventeen definition names
   are unique, all seven external source strings byte-match current registry
   contracts and carry literal `proofs/<id>` paths, and no GT external is
   silently added. `def-fd-cstar-diagonal` is a frozen metadata import, not a
   license to invent a diagonal lemma.
9. **Rigour/status boundary.** This plan is not an audit, proof, or elevation.
   Until a separate hostile design audit, user ratification, fresh seeding,
   fresh prover, separate verifier, export, oracle, and mechanical bank all
   succeed, the target remains `proved-mod-audit` / `af: none`, T0 remains
   168, and `op-classical` remains OPEN.
