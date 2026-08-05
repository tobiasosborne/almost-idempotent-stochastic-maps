# AUDIT — KITAEV-PAIR af elevation design

Date: 2026-08-05. Role: fresh hostile auditor; not the design author.

## Verdict

**LAND-WITH-EXACT-CORRECTIONS.** The two frozen contracts are mathematically
dischargeable by the proposed Pauli/sign-average construction and the proposed
entrywise positivity argument. I found no counterexample to either mathematical
claim. The design is nevertheless not seed-ready: its advertised af trees contain
pending-sibling dependencies, and the explicit counterexample node does not itself
cite the two provenance-only printed-formula externals. Those are proof-architecture
gaps, not reasons to reword either root.

Nothing in this audit promotes either registry row.

## Independent checks

- Both proposed root strings equal their shard `contract:` values byte for byte:
  repair 482/482 bytes; CP-ization 451/451 bytes.
- The local Kitaev payload has SHA256
  `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`, matching
  the design and manifest.
- I extracted each of the design's three quoted GT payloads and checked it as one
  contiguous fixed string with `grep -Fz`: all pass, beginning at source lines
  1228, 1254, and 2780 respectively. The stated loci are accurate.
- The proposed corollary import after the em dash is byte-equal to the repair
  shard contract. Proposed definition names and external names are unique within
  each workspace package. Both target workspaces presently contain only empty
  scaffold directories.

## Numbered findings

### 1. Major/blocking — the repair construction is not an af tree

**Locus:** design lines 43-57, 112-211; especially the sibling references in
nodes `1.2.3`, `1.2.4`, and `1.2.7`. This conflicts with the binding rule in
`HANDOFF.md:121-124`: a node may not cite a pending sibling.

The seven children under `KDR-CONSTRUCTION` are a sequential proof, not seven
independent premises. `KDR-BLOCK-EXPANSION` needs the definition of `S_{jk}` from
`KDR-BLOCK-UNITARIES`; `KDR-BLOCK-DIAGONAL` needs both earlier block nodes;
`KDR-PHASE-FAMILY` explicitly cites all three; phase cancellation needs that
family; whole-diagonal centrality needs both cancellation and the block-diagonal
facts; and the norm node explicitly needs the representation and `pi(D)=I_B`.
A fresh verifier cannot validate those leaves independently.

**Exact correction:** preserve the root and the mathematical text, but replace
the seven siblings by a dependency spine

```text
KDR-CONSTRUCTION
`- KDR-NORM-AND-UNIVERSALITY
   `- KDR-WHOLE-DIAGONAL
      `- KDR-PHASE-CANCELLATION
         `- KDR-PHASE-FAMILY
            `- KDR-BLOCK-DIAGONAL
               `- KDR-BLOCK-EXPANSION
                  `- KDR-BLOCK-UNITARIES
```

and make every intermediate statement cumulative: it must export all facts its
parent uses, rather than name a node elsewhere in the tree. This changes neither
the 12-node count nor the frozen root.

### 2. Major/blocking — the counterexample node lacks its own GT citation

**Locus:** `KDR-C2-COUNTEREXAMPLE`, design lines 99-110, versus the external
declaration only on `KDR-REFUTATION`/`KDR-PRINT-LOCUS`, lines 73-97.

The concrete calculation is correct, but node `1.1.2` calls the prescription
“printed” while listing no external. The brief specifically requires an explicit
counterexample node with the printed formula imported byte-verbatim; a sibling's
provenance does not discharge that node.

**Exact correction:** list both
`GT-kitaev-printed-direct-sum-formula-1254` and
`GT-kitaev-printed-direct-sum-formula-2780-2783` as externals of node `1.1.2`,
then explicitly instantiate their Cartesian-product/direct-sum prescription at
the one-point designs before performing the displayed basis calculation. Keep
the externals provenance-only.

### 3. Major/blocking — the CP tree also cites pending siblings

**Locus:** design lines 294-304, 331-394. `KCP-MATRIX-POSITIVITY` invokes sibling
`KCP-LINEARITY`, while `KCP-METHOD-SCOPE` summarizes sibling nodes `1.2-1.2.2`.

The entrywise proof itself is sound, but this tree shape cannot enforce its
negative method clause without cross-sibling inspection.

**Exact correction:** keep seven nodes but reparent them as

```text
KCP-ROOT
|- KCP-LINEARITY
`- KCP-METHOD-SCOPE
   `- KCP-MATRIX-POSITIVITY
      |- KCP-SQUARE-IDENTITY
      |  `- KCP-ENTRYWISE-CENTRALITY
      `- KCP-POSITIVE-SUM
```

Remove “Together with node 1.1” from the matrix-positivity statement. Let the
root combine its two children; let `KCP-METHOD-SCOPE` cite only its validated
child/subtree and cumulatively export both all-level positivity and the
exact-centrality/no-multiplicativity conclusion.

### 4. Required pre-seed metadata correction — confirmed L2 defect

**Locus:** `argument/lemmas/cor-kitaev-diagonal-cpization.md:5`; design lines
28-32 and 396-415.

The current corollary `defs:` line omits `def-ucp-map`, even though its frozen
contract uses UCP and concludes CP. The definition also supplies positivity of
every amplification, exactly what `KCP-POSITIVE-SUM` uses.

**Exact correction:** before seeding, change only the corollary metadata to
`defs: def-fd-cstar-diagonal; def-ucp-map`. Register those two definition names
exactly once. No other definition shard is missing: matrix units, unitaries,
finite direct sums, square roots of positive matrices, and projective norms are
standard vocabulary; the projective-norm formula is additionally supplied by
the checked GT external. “Phase-balanced” is witnessed, rather than separately
defined, by the explicit sign-moment identity.

### 5. Minor/clarifying — bind the type of `Phi` in the CP proof scope

**Locus:** design lines 306-317 and 410-415.

The frozen formula forces the intended type, but “every UCP map `Phi`” is not
self-typing in isolation. The products fed to `Phi` lie in `B(H)`, and the stated
codomain of `Delta'` is `B(H)`.

**Exact correction:** without changing the root, add a binding scope sentence to
the CP skeleton/prover prompt: throughout this tree, the displayed formula is
interpreted with `Phi:B(H)->B(H)` UCP. Reject any proof using a differently typed
map.

## Mandatory attacks 1-8

1. **Root freeze — PASS.** Both independent byte comparisons pass.
2. **Refutation clause — CORRECTION REQUIRED.** The source formula and concrete
   `C direct-sum C` calculation are correct: `D_print=I tensor I`, and for
   `e_1`, `e_1D_print=e_1 tensor I != I tensor e_1=D_print e_1` in the four-term
   coordinate basis. Finding 2 is required so that this calculation node itself
   imports what it calls printed.
3. **Construction clause — MATHEMATICS PASS; TREE CORRECTION REQUIRED.** The
   generalized Pauli expansion is correct; sign averaging gives
   `2^(-m) sum_sigma sigma_r sigma_s=delta_rs` for all `m>=1` and arbitrary
   block sizes; direct-sum unitarity does not require equal dimensions. The
   resulting block sum commutes with every `Z=direct-sum_r Z_r`, not merely with
   generators, and `pi(D)=I_B`. Each unitary has
   `||W_t^dagger||||W_t||=1`; hence the displayed factor sum is one. This gives
   `||D||_pi<=1`, while contractivity of multiplication and `pi(D)=I_B` give
   `1<=||D||_pi`, so equality is exact. Only term count depends on block data.
   Finding 1 repairs af dischargeability.
4. **CP-ization — MATHEMATICS PASS; TREE CORRECTION REQUIRED.** Entrywise
   centrality gives
   `sum q_t Y_ba^dagger Y_bc W_t^dagger tensor W_t = sum q_t Y_ba^dagger
   W_t^dagger tensor W_t Y_bc`. Applying the stated bilinear map and using star
   preservation exactly once yields `sum_t q_t Phi_n(Z_t^dagger Z_t)>=0` at
   every level. No multiplication is moved through `tilde-Delta`. Linearity is
   used to define a linear `Delta'`; star preservation is used only to identify
   the left factor as an adjoint; CP of `Phi` supplies positivity of `Phi_n`.
   Unitality of `Phi` is unused but harmless. Findings 3 and 5 repair structure
   and typing.
5. **Seeding packages — PASS WITH REQUIRED CORRECTIONS 2 AND 4.** All three GT
   quotes, names, and loci pass the independent byte check; the repair import is
   exact; lists are duplicate-free. The broad poisoned external is correctly
   excluded. The order explicitly requires a validated, exported,
   oracle-checked, banked repair before the corollary is seeded.
6. **Budgets — PASS, TIGHT FOR THE REPAIR.** Caps 26 and 22 do not exceed the
   repository's 26-node soft ceiling (`>26` is the failure condition). The
   12-node repair projection has only 2.17x headroom, below the observed 3x
   worst case, but the design correctly makes a cap hit a stop-and-factor event.
   After Findings 1 and 3, the designed counts remain 12 and 7; do not raise
   either cap. If the repair reaches the cap, factor rather than squeeze in a
   27th node.
7. **Ranked risks — DISPOSED BELOW.** No unaddressed mathematical risk remains.
8. **Fresh under-specification hunt — FOUND.** The unadvertised gaps are the two
   pending-sibling architectures and the counterexample node's missing direct
   GT citations; the only residual clarification is the type of `Phi`.

## Disposition of the design's ranked risks

1. Centrality/factor order: **PASS**, recalculated entrywise.
2. All-level positivity: **PASS**; the proof uses every `n`, not a level-one or
   Choi shortcut.
3. Separate counterexample node: **CORRECTION REQUIRED** by Finding 2.
4. Arbitrary block sizes: **PASS**, including `m=1`.
5. L2/typing: **CORRECTION REQUIRED** by Findings 4-5.
6. Exact projective norm: **PASS**, with both inequalities present.
7. Poisoned GT import: **PASS**; it is excluded.
8. Finite versus dimension-free: **PASS**; no uniform term-count claim appears.
9. Downstream overreach: **PASS**; only CP is concluded.
10. Root/order drift: **PASS**; roots are exact and repair-first banking is
    enforced.

Subject to Findings 1-5, the package may be ratified for repair-first seeding.
