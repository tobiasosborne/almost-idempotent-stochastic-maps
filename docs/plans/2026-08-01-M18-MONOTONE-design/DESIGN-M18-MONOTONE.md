# DESIGN — M18 extended-inclusion monotonicity micro-row

**Scope and status.** Design only. This file proposes exactly one new
micro-row and re-seed guidance for `lem-maincb-reset-constant-ledger`. It
does not alter a definition, registry shard, proof workspace, report, or
script, and it proves nothing. The M18 contract remains byte-identical.

## 1. Deliverable 1 — the micro-row

Proposed id: `lem-maincb-extended-inclusion-monotone`.

The registry-ready contract is the following single physical ASCII line:

```text
contract: If A is a finite-dimensional extended epsilon_A-C*-algebra, B is a finite-dimensional extended epsilon_B-C*-algebra, v:A->B is linear, and 0 <= delta <= delta', then if v is an extended delta-inclusion it is an extended delta'-inclusion, and if v is an extended delta-isomorphism it is an extended delta'-isomorphism and in particular an extended delta'-inclusion.
```

Prospective imports, exactly:

```text
defs: def-extended-delta-inclusion; def-extended-epsilon-cstar-algebra
deps:
```

No upper ceiling on `delta'` is needed. Neither the locked definition nor
the pinned source loci impose one, and the lower norm inequality only gets
weaker when `delta' > 1`.

### Clause audit

Fix an amplification `1_{M_n} tensor v`. The locked definition requires it
to be a delta-homomorphism and to satisfy the `(1-delta)` lower and
`(1+delta)` upper norm bounds.
Every clause is monotone in the required direction:

- bounded linearity and, in the star-algebra setting, star preservation are
  independent of the defect parameter;
- the unit clause weakens from `||v_n(I)-I|| <= delta` to the same bound
  with `delta'` because `delta <= delta'`;
- the multiplication clause weakens because
  `delta*||X||*||Y|| <= delta'*||X||*||Y||`;
- the lower norm clause weakens because
  `(1-delta')*||X|| <= (1-delta)*||X|| <= ||v_n(X)||`;
- the upper norm clause weakens because
  `||v_n(X)|| <= (1+delta)*||X|| <= (1+delta')*||X||`;
- the quantifier over every `n` is unchanged; and
- bijectivity is independent of the defect parameter, so the isomorphism
  conclusion and its inclusion component carry over.

Thus no non-monotone clause and no route-level obstruction is present. The
argument uses no dimension-dependent estimate.

**Provenance.** This is a direct definitional consequence of the locked
consensus definition `def-extended-delta-inclusion`. The exact local source
is `refs/kitaev-2405.02434/approximate_algebras.tex:443-456,1477-1484`,
SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`:
lines 443--456 contain the unit, multiplication, two-sided norm, and
bijectivity clauses, while lines 1477--1484 supply amplification typing.
The source does not state this monotonicity lemma verbatim, so the new row
should enter as `stated`, not `cited`, and obtain any later promotion only
through the normal independent af protocol.

**Build budget.** Target / rounds / hard cap: `3 / 2 / 6`. The intended
three nodes are the root, the amplificationwise inclusion-clause audit,
and the parameter-free bijectivity/isomorphism carryover. Hitting six nodes
would indicate unexpected definitional or typing drift and should stop the
run rather than enlarge the budget.

## 2. Deliverable 2 — lawful existential instantiation

The Stage-2 re-seed must use one explicit existential-elimination node in
this order:

1. Apply `lem-maincb-stage2-call-envelope` to obtain the exact closed EXT-CB
   input datum.
2. Apply `lem-maincb-stage2-raw-extension` to that datum. Its conclusion
   says that the datum admits some
   `v_+:M_{r+1}->A_R` with the extended `D_2*t`-isomorphism and unit bounds.
3. Choose one such `v_+`. Only after this choice, form the Stage-2
   `def-maincb-raw-call` record with literal output map `u_2:=v_+` and fixed
   amplification family `1_{M_n} tensor u_2 := 1_{M_n} tensor v_+`, retaining
   the supplied input, source, target corner, scales, ambient-defect field,
   and raw-defect field. The required properties now hold for the literal
   `u_2` by definitional equality, not by replacing a previously fixed map.
4. Use `D_2*t <= D_*t` and
   `lem-maincb-extended-inclusion-monotone` to weaken the isomorphism bound;
   weaken the numerical unit bound separately by the same scalar inequality.

This selection, record formation, and binding should remain one proof node.
Splitting it would recreate the challenge without adding mathematical
content.

The same pattern is required at Stage 3: apply
`lem-maincb-stage3-raw-merge`, choose its output
`v:B_U oplus B_V->A_R`, and then define the literal raw-call map `u_3:=v`
with its fixed amplification family before transporting the bounds. The
maps `u_0` and `u_1` are already literal maps in their provider conclusions,
so they require no existential-selection node.

**Instantiation verdict: contract change needed — NO.** In M18, “the
literal maps ... furnished by [the call-envelope] with [the raw-extension]”
is realized by the explicit combined construction above: the envelope
furnishes the input datum, the extension/merge furnishes an existential
output, and M18 binds that chosen output as the literal map. No pre-existing
literal map is silently identified with a different witness, and no wording
change to the ratified M18 contract is needed.

For the re-seed, provision the locked
`def-extended-delta-inclusion` vocabulary and the new micro-row external.
This is import bookkeeping only; it is not a definition or contract change.

## 3. Deliverable 3 — M18 re-seed

The ten validated nodes in run 1 all survive at the level of mathematical
obligation:

| old node | surviving content | re-seed treatment |
|---|---|---|
| `1.1.1` | receiving-field choices | replay unchanged |
| `1.1.2` | application of witness arithmetic | replay unchanged |
| `1.1.3` | receiving-field inequalities | replay unchanged |
| `1.1` | witness-ledger assembly | fold into the three preceding nodes and root assembly |
| `1.2` | `D_*` max arithmetic and reset smallness | replay unchanged |
| `1.3` | global-scalar map and unit bound | retain; cite the micro-row for `D_0*t -> D_*t` |
| `1.5.1` | Stage-2 closed-datum production | replay unchanged |
| `1.6.1` | Stage-3 four-corner-datum production | replay unchanged |
| `1.6.2` | Stage-3 merge output and unit bound | retain the provider application, but make `u_3:=v` explicit and cite the micro-row |
| `1.6` | Stage-3 conclusion | fold into the repaired Stage-3 node and root assembly |

“Survive” here does not mean copying validations into a fresh workspace. It
means their statements and arguments are not discarded by the two verifier
findings; each must be replayed and independently verified in the re-seed.

The challenged or unvalidated architecture should not be carried over:
old `1.4.1`/`1.4.2` become one Stage-1 provider-plus-citation node; old
`1.5.2`/`1.5.2.1` become the single lawful Stage-2 selection node above;
and old `1.7.1`/`1.7.1.1` become one reset-application node using the
micro-row's explicit isomorphism-to-inclusion conclusion.

### Twelve-node clean skeleton

1. Root and final assembly.
2. Fix the receiving fields.
3. Apply `lem-maincb-witness-arithmetic`.
4. Derive all stated fields and universality properties of `W`.
5. Establish the `D_*` max inequalities and reset-radius inequalities.
6. Produce `u_0`, cite monotonicity, and weaken its unit bound.
7. Produce the literal `u_1`, cite monotonicity, and weaken its unit bound.
8. Produce the exact Stage-2 closed EXT-CB datum.
9. Choose `v_+`, bind `u_2:=v_+`, cite monotonicity, and weaken its unit bound.
10. Produce the exact Stage-3 four-corner datum.
11. Choose `v`, bind `u_3:=v`, cite monotonicity, and weaken its unit bound.
12. Use the micro-row's explicit inclusion conclusions for all four maps,
    apply `lem-maincb-reset-invariant-preservation`, and assemble the root.

**Re-seed budget.** Keep the ratified original budget exactly:
target / rounds / hard cap `12 / 3 / 16`. The micro-row turns all four
defect transports into citations, while the two existential selections are
absorbed into their Stage-2 and Stage-3 application nodes. A seventeenth
node is a factoring stop, not grounds for another cap increase.

## 4. Deliverable 4 — risk register

### Top attacks on the micro-row

1. **Lower-bound direction.** A verifier should explicitly check that
   increasing the defect decreases `(1-delta)||X||`; this is the only clause
   whose direction is visually easy to reverse. The displayed chain above
   settles it, including `delta' > 1`.
2. **Missing unit or star clause.** The proof must audit the unit estimate at
   every amplification and state that exact star preservation is
   parameter-free; proving only multiplicativity and norm distortion would
   not unfold the locked delta-homomorphism.
3. **Amplification/bijectivity drift.** The same source and target and the
   same family `1_{M_n} tensor v` must be used at both defects. No inverse
   estimate is asserted; only the locked definition's level-one bijectivity
   is retained.
4. **Hidden range assumption.** No smallness ceiling may be imported from a
   downstream proposition. Proposition `prop_inc_ext` has additional
   hypotheses, but those are not clauses of the locked harmonized
   definition.

### Top two ways this design could be wrong

1. The canonical meaning of `def-extended-delta-inclusion` could have
   drifted away from its locked ampwise two-sided norm harmonization toward
   the source's proposition-hypothesis formulation at line 1481. That would
   be a definition-level conflict and a STOP, not a reason to improvise a
   different micro-row. The currently locked text has not drifted.
2. A future verifier could read the Stage-2 or Stage-3 call-envelope as
   irreversibly fixing a raw-call output before M16/M17 is applied. Under
   that reading, `u_i:=v` would replace rather than instantiate the literal
   output, and the expected NO verdict would fail. The re-seed must therefore
   exhibit the construction order and the newly formed record explicitly;
   if the provider interface forbids forming that record, stop for a
   ratified M18/provider contract repair rather than asserting equality.
