# DESIGN v2 — `lem-thmainext-conditional` af elevation

**Status:** unaudited design only. This document proves nothing, changes no
registry/definition/workspace/status, leaves `lem-thmainext-conditional` at
`proved-mod-audit` / `af: none`, leaves T0 at 168, and leaves `op-classical`
OPEN. It is written to be attacked by a separate fresh hostile auditor.

## 1. Verdict

**YES.** The re-scoped, byte-frozen contract follows from the frozen deps. It
is a near-trivial existential repackaging of
`lem-maincb-structural-assembly` (M28), and the honest af tree is **three easy
nodes**. M28 supplies one ledger datum `W`, a finite-dimensional `C*`-algebra
`B`, and the typed map `v:B->A`; it also states that
`W.c0_cb*W.K_call` and `W.epsilon_MAIN` are finite positive universal
witnesses. The consumer merely hides `W` and M28's more detailed block and
unit conclusions.

No hidden eighth premise is needed. The v1 audit settled that M28 is usable as
one closed validated external, including its phrase “`W` supplied by
`lem-maincb-reset-constant-ledger`.” The six other frozen deps are not used by
the reduced proof. Their role is registry provenance after the user-ratified
method-clause re-scope, not mathematical work to be reconstructed here.

## 2. Three-node skeleton

```text
THX2-ROOT
└── THX2-REPACKAGE
    └── THX2-M28
```

### `THX2-ROOT` — frozen root

**Exact statement:**

```text
Extended th_main_ext assembly: there are universal C_E < infinity and epsilon_E > 0 such that every finite-dimensional extended epsilon-C*-algebra A, for 0 <= epsilon <= epsilon_E, is carried by one extended C_E*epsilon-isomorphism v:B->A from a finite-dimensional C*-algebra, with constants independent of dimension, amplification level, and block data.
```

- Parent: none. Children: `THX2-REPACKAGE`.
- `defs:` `def-epsilon-cstar-algebra`, `def-operator-space`,
  `def-extended-epsilon-cstar-algebra`, `def-extended-delta-inclusion`.
- `externals:` none; it consumes its validated child.
- Constants: receives `C_E,epsilon_E` from `THX2-REPACKAGE`.

### `THX2-REPACKAGE` — eliminate `W`, retain M28's witnesses

**Exact statement:**

```text
Consume THX2-M28 as one validated theorem and fix once the single def-maincb-witness-ledger datum W supplied there. Only after fixing W, define C_E:=W.c0_cb*W.K_call and epsilon_E:=W.epsilon_MAIN. For an arbitrary finite-dimensional extended epsilon-C*-algebra A with 0<=epsilon<=epsilon_E, take B and v to be exactly the finite-dimensional C*-algebra and the same typed extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A furnished by THX2-M28. Since THX2-M28 states that these two field expressions are finite positive universal witnesses, these choices are independent of dimension, amplification level, and block data and establish THX2-ROOT.
```

- Parent: `THX2-ROOT`. Children: `THX2-M28`.
- `defs:` `def-epsilon-cstar-algebra`, `def-operator-space`,
  `def-extended-epsilon-cstar-algebra`, `def-extended-delta-inclusion`,
  `def-maincb-witness-ledger`.
- `externals:` none directly; it cites its child only.
- Constants: fixes `W` once, then introduces exactly
  `C_E:=W.c0_cb*W.K_call` and `epsilon_E:=W.epsilon_MAIN`. It neither shrinks
  the radius nor selects any packet threshold.

### `THX2-M28` — opaque target-shaped provider

**Exact statement (byte-verbatim current M28 contract):**

```text
Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN admits a finite-dimensional C*-algebra B=oplus_C M_{|C|} and an extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A satisfying ||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon; hence C_struct=W.c0_cb*W.K_call and e_struct=W.epsilon_MAIN are finite positive universal witnesses.
```

- Parent: `THX2-REPACKAGE`. Children: none.
- `defs:` `def-epsilon-cstar-algebra`, `def-operator-space`,
  `def-extended-epsilon-cstar-algebra`, `def-extended-delta-inclusion`,
  `def-maincb-witness-ledger`.
- `externals:` `lem-maincb-structural-assembly` only.
- Constants: supplies the one `W`, its three used fields, and the universal
  aliases `C_struct,e_struct`. Its `B` and `v` are the final witnesses; no map
  from a reset or packet theorem is substituted.

The only point with any logical content beyond literal renaming is
existential elimination: M28's closed theorem supplies one `W` and certifies
the two relevant projections as universal witnesses. The parent projects
those fields from that same datum. The source typing of `B`
and the all-amplification meaning of “extended isomorphism” are explicit in
M28 and `def-extended-delta-inclusion`; neither requires a new lemma.

## 3. The six non-M28 frozen deps

| Frozen dep | Used by the reduced proof? | Disposition |
|---|---:|---|
| `conj-hcb` | No | Register as an allowed external; do not cite it or create a node. |
| `conj-extcb` | No | Register as an allowed external; do not cite it or create a node. |
| `lem-hcb-column-hilbert-squared` | No | Register as an allowed external; do not cite it or create a node. |
| `lem-maincb-error-improvement` | No | Register as an allowed external; do not cite it or create a node. |
| `lem-maincb-reset-invariant-preservation` | No | Register as an allowed external; do not cite it or create a node. |
| `lem-extcb-four-corner-merge` | No | Register as an allowed external; do not cite it or create a node. |

**Seeding recommendation.** Register all seven frozen deps exactly once,
because `scripts/af-orchestrate.py` instructs the prover to register every
declared dep and the registry deliberately retains all seven edges. Cite only
M28 in the tree. This keeps the af scope aligned with the frozen DAG without
pretending that scope membership is proof use.

`check-refs.py` classifies each literal `proofs/<dep-id>` source with no
`refs/` locus as `skip_import`; it does not require a registered import to be
cited. The linker independently checks that all frozen deps resolve and are
validated for status propagation, but it does not equate the registry deps
list with cited af externals. Thus unused registration is mechanically safe.
Omitting the six would probably not fail either gate, but would violate the
standard orchestration prompt and make the workspace's declared scope less
faithful to the intentionally unreduced registry line.

The same distinction applies to `def-fd-cstar-diagonal`: register it because
it is on the frozen target `defs:` line, but cite it in no node. The reduced
contract and proof contain no diagonal argument.

## 4. Witness/constant ledger

| Symbol | Bound where | Provider and use |
|---|---|---|
| `W` | `THX2-REPACKAGE`, once | Supplied by `THX2-M28`, which closes the two used projections as universal witnesses; fixed before either receiving constant. |
| `W.c0_cb` | field of that `W` | Positive finite universal factor in M28's coefficient. |
| `W.K_call` | field of that `W` | Positive finite universal factor in M28's coefficient. |
| `W.epsilon_MAIN` | field of that `W` | Positive finite universal radius in M28. |
| `C_E:=W.c0_cb*W.K_call` | after `W` | Exactly M28's `C_struct`; not altered or enlarged. |
| `epsilon_E:=W.epsilon_MAIN` | after `W` | Exactly M28's `e_struct`; not shrunk against any other threshold. |
| `B,v` | quantified application after the constants | Exactly M28's finite-dimensional `C*`-algebra and same typed map for the arbitrary `A,epsilon`. |

No H-CB, EXT-CB, COL-HILB, merge, improvement, or reset constant is selected
or consumed.

## 5. Seeding package

### Root conjecture

Use this text byte-for-byte:

```text
Extended th_main_ext assembly: there are universal C_E < infinity and epsilon_E > 0 such that every finite-dimensional extended epsilon-C*-algebra A, for 0 <= epsilon <= epsilon_E, is carried by one extended C_E*epsilon-isomorphism v:B->A from a finite-dimensional C*-algebra, with constants independent of dimension, amplification level, and block data.
```

### Unique `af def-add` list

Register each name exactly once; inspect `af defs` first and cleanly re-seed
rather than adding a duplicate:

```text
af def-add def-epsilon-cstar-algebra --file definitions/def-epsilon-cstar-algebra.md -d proofs/lem-thmainext-conditional
af def-add def-operator-space --file definitions/def-operator-space.md -d proofs/lem-thmainext-conditional
af def-add def-extended-epsilon-cstar-algebra --file definitions/def-extended-epsilon-cstar-algebra.md -d proofs/lem-thmainext-conditional
af def-add def-extended-delta-inclusion --file definitions/def-extended-delta-inclusion.md -d proofs/lem-thmainext-conditional
af def-add def-maincb-witness-ledger --file definitions/def-maincb-witness-ledger.md -d proofs/lem-thmainext-conditional
af def-add def-fd-cstar-diagonal --file definitions/def-fd-cstar-diagonal.md -d proofs/lem-thmainext-conditional
```

This fixes v1's real omission: the base `def-epsilon-cstar-algebra` is
provisioned because `def-extended-epsilon-cstar-algebra` is defined in terms
of it. `def-operator-space` is the other base vocabulary named in that
definition. The ledger and extended-isomorphism definitions are proof
vocabulary exposed by M28. The diagonal definition is frozen metadata only.

### Exact `af add-external` entries

Register each name once. Every source has a literal `proofs/<dep-id>` path and
then the byte-verbatim current contract.

`conj-hcb`:

```text
imports validated registry lemma proofs/conj-hcb — H-CB: there are universal C_H < infinity and e_H > 0 such that, whenever e=delta+epsilon <= e_H, Q is a level-one one-dimensional delta-projection in an extended epsilon-C*-algebra A, and P,R,S are delta-projections, the maps 1_{M_n} tensor Ha^Q_{P,R}, under the COL-HILB identification with operators on C^n tensor S_{R,Q} and C^n tensor S_{P,Q}, satisfy for every n the adjoint equality, product defect at most C_H*e*||Z||||W||, and the uniform unit, upper-norm, homomorphism, and canonical-identity closeness estimates required by lem_extension; moreover, if the level-one lower modulus of Ha^Q_{P,P} is at least 1/4, then every amplification has lower modulus at least 1-C_H*e, and if Ha^Q_{P,P} is also bijective at level one then every amplification is bijective with inverse norm at most 1+C_H*e; the analogous off-diagonal inverse bound for Ha^Q_{P,R} is asserted only when Ha^Q_{P,R} is bijective at level one and Ha^Q_{R,R} satisfies that diagonal lower-modulus hypothesis; all constants independent of n, dim A, block count, and block dimensions.
```

`conj-extcb`:

```text
imports validated registry lemma proofs/conj-extcb — EXT-CB: there are universal C_ext < infinity and e_ext > 0 such that if e=delta+epsilon <= e_ext, P,Q are delta-projections in an extended epsilon-C*-algebra A with ||P+Q-I|| <= delta, v:M_r->S_P is an extended delta-isomorphism, dim S_Q=1 at level one, and S_{P,Q} is nonzero, then there is one map v_+:M_{r+1}->A whose every amplification is a C_ext*e-isomorphism; the same level-one unitary and the same four corner maps carry all amplification levels, with constants independent of r, n, and dim A.
```

`lem-hcb-column-hilbert-squared`:

```text
imports validated registry lemma proofs/lem-hcb-column-hilbert-squared — Corrected amplified column-Hilbert estimate: there are universal C_col < infinity and e_col > 0 such that every H-CB datum with e <= e_col, every n >= 1, and every X in M_{n,1} tensor S_{P,Q} satisfy abs(<X,X>_n-||X||_{n,1}^2) <= C_col*e*||X||_{n,1}^2.
```

`lem-maincb-error-improvement`:

```text
imports validated registry lemma proofs/lem-maincb-error-improvement — Complete error improvement: there are universal epsilon_max^cb>0, delta_max^cb>0 and c_0^cb<infinity such that every extended delta-inclusion v:B->A from a finite-dimensional C*-algebra B into an extended epsilon-C*-algebra A with 0<=epsilon<=epsilon_max^cb and 0<=delta<=delta_max^cb can be replaced by an extended c_0^cb*epsilon-inclusion v_tilde:B->A that is bijective whenever v is bijective.
```

`lem-maincb-reset-invariant-preservation`:

```text
imports validated registry lemma proofs/lem-maincb-reset-invariant-preservation — After first fixing the universal e_it,K_disp,K_floor witnesses of lem-maincb-improvement-iteration and epsilon_max^cb,delta_max^cb,c0^0 witnesses of lem-maincb-error-improvement, there are universal 0 < C_unit < infinity and epsilon_unit,delta_unit,a_unit > 0 furnished by the third clause of prop_delta_hominc and its implicit quantifier convention such that, for every D >= 1 and every def-maincb-witness-ledger datum W with W.c0_cb >= max{c0^0,K_floor,C_unit*(K_floor+1)} and W.r_reset <= min{epsilon_max^cb,delta_max^cb/D,e_it/(D+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D),[2*(1+K_disp)*D]^{-1}}, every explicit raw call into an extended epsilon_R-C*-corner A_R at scale 0 <= t <= W.r_reset whose literal map u_R:B_R->A_R is an extended D*t-inclusion and satisfies ||u_R(I_{B_R})-u_{A_R}|| <= D*t and epsilon_R <= t admits an error-improved map v_R:B_R->A_R satisfying d_R <= W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}|| <= W.c0_cb*epsilon_R, preserving bijectivity when u_R is bijective and leaving the source, target corner, and amplification form unchanged.
```

`lem-maincb-structural-assembly`:

```text
imports validated registry lemma proofs/lem-maincb-structural-assembly — Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN admits a finite-dimensional C*-algebra B=oplus_C M_{|C|} and an extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A satisfying ||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon; hence C_struct=W.c0_cb*W.K_call and e_struct=W.epsilon_MAIN are finite positive universal witnesses.
```

`lem-extcb-four-corner-merge`:

```text
imports validated registry lemma proofs/lem-extcb-four-corner-merge — Complete four-corner merge: there are universal C_merge < infinity and a_merge > 0 such that four fixed bijective level-one corner maps satisfying def-four-corner-merging-datum with common defect rho and rho+epsilon <= a_merge combine into one extended C_merge*(rho+epsilon)-isomorphism.
```

There is no ground-truth external in this seed. No delta-homomorphism
arithmetic is performed; do not register
`GT-kitaev-def-delta-homomorphism`. If a prover starts re-deriving M28 or
packet estimates, prune that work rather than expanding the seed.

## 6. Node cap

Expected live size: **3 nodes**. Proposed hard cap: **6**, comfortably below
the repository soft cap 26. The three-node margin allows a hostile verifier to
split the repackaging step into constant choice, typed witness reuse, and
universality if genuinely necessary.

A balloon past 6 would not indicate deep mathematics. It would mean that the
prover is re-proving M28, trying to make the six historical deps look used,
duplicating definition work, or has failed to treat M28's supplied `W` as a
closed existential witness. Stop and classify; do not raise the cap or
internalize MAIN.

## 7. Ranked hostile-audit risks

1. **M28 existential closure.** Attack whether the external really supplies
   one usable `W` with the two projected universal witnesses, rather than
   proving a statement conditional on an unimported ledger. The v1 audit
   answered yes, but this is still the key logical hinge.
2. **Universality projection.** Check that M28's “finite positive universal
   witnesses” is sufficient for independence from dimension, amplification,
   and block data; reject any extra unstated interpretation if it is not.
3. **Binder order and exact constants.** There must be one `W`, fixed before
   `C_E,epsilon_E`; the radius is exactly `W.epsilon_MAIN`, not a threshold
   minimum, and the coefficient is exactly `W.c0_cb*W.K_call`.
4. **Same typed witnesses.** The final `B,v` must be M28's own witnesses.
   Reject any replacement by a map from a packet theorem or any silent source
   or target renaming.
5. **Root drift.** Compare node 1 byte-for-byte with the current registry
   contract. Any reintroduction of the stale method clause is fatal.
6. **Unused-dep hygiene.** Confirm that the six registered but uncited
   externals remain genuinely unused and that no decorative node or fictitious
   threshold application has returned.
7. **Definition closure and uniqueness.** Confirm the six `def-add` names are
   unique, especially that base `def-epsilon-cstar-algebra` is present, and
   that `def-fd-cstar-diagonal` remains metadata rather than invented work.
8. **Rigour boundary.** This design is not a proof or promotion. Until a
   separate design audit, user ratification, fresh prover, separate verifier,
   export, oracle, gates, and banking all succeed, the target remains
   `proved-mod-audit` / `af: none`, T0 remains 168, and `op-classical` remains
   OPEN.
