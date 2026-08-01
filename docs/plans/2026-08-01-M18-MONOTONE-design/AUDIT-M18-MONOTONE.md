# HOSTILE AUDIT — M18 extended-inclusion monotonicity micro-row

**Date:** 2026-08-01

**Auditor role:** fresh independent hostile auditor; not the design author.

**Epistemic status:** audit only. No definition, registry result, proof
workspace, or rigour status is changed.

**Final disposition:** **DESIGN-REFUTED.** The monotonicity lemma itself is
mathematically sound, with no hidden `delta'<1` ceiling, and M18's ratified
contract need not change. The proposed re-seed is nevertheless not lawful as
written: it says to retain fields of already formed raw-call records while
replacing their literal maps, and at Stage 2 the retained source and target do
not even type the selected extension witness. The micro-row should also use the
plain-C*-source / extended-target typing exported by every banked consumer.

## 1. Clause-by-clause monotonicity audit

At every amplification `v_n = 1_{M_n} tensor v`, the locked harmonized
definition imports the clauses at
`refs/kitaev-2405.02434/approximate_algebras.tex:443-456` and applies them
amplificationwise via `:1477-1484`. For `0 <= delta <= delta'`:

- bounded linearity is parameter-free;
- exact star preservation is parameter-free;
- the unit clause is monotone because
  `||v_n(I)-I|| <= delta <= delta'`;
- the multiplication clause is monotone because norms are nonnegative and
  `delta*||X||*||Y|| <= delta'*||X||*||Y||`;
- the lower norm clause has the sign used in the design:
  `(1-delta')||X|| <= (1-delta)||X|| <= ||v_n(X)||`;
- the upper norm clause is monotone because
  `||v_n(X)|| <= (1+delta)||X|| <= (1+delta')||X||`;
- the universal quantifier over `n` and the fixed family `1_{M_n} tensor v`
  do not change; and
- level-one bijectivity is parameter-free, so an extended
  `delta`-isomorphism remains an extended `delta'`-isomorphism and hence an
  extended `delta'`-inclusion.

There is no definitional ceiling `delta'<1`. When `delta'>1` the lower bound
becomes vacuous but remains a valid weaker inequality. A later argument that
tries to *derive* injectivity from the `delta'` lower bound would need
`delta'<1`; this lemma does not do that. For the isomorphism branch,
bijectivity is retained from the original predicate. Thus the design's clause
audit and source SHA256 are correct, and no route-level obstruction exists.

## 2. Findings and exact corrections

### F1 — MAJOR: the proposed micro-row is not in the banked consumer's source/target normal form

The contract at `DESIGN-M18-MONOTONE.md:15` requires both its source `A` and
target `B` to be extended approximate C*-algebras. This is mathematically a
valid setting: the source definition at `approximate_algebras.tex:443-455`
allows an approximate algebra as domain, and `:1477-1484` amplifies it. It is
not, however, the interface exported by any M18 consumer. The four M18 maps
have sources `C`, `C^{m+1}`, `M_{r+1}`, and `B_U oplus B_V`, all named
finite-dimensional C*-algebras, and targets `A` or `A_R`, named
finite-dimensional extended approximate C*-algebras. The same typing is used
by the banked improvement, unit-control, direct-sum, EXT-CB, and final-assembly
rows. Requiring a separately supplied extended-algebra datum on the source
creates an avoidable coercion/typing obligation that the advertised three-node
micro-row and M18 imports do not export.

**Exact correction:** replace the proposed contract by the following single
physical ASCII line (and keep the proposed `defs:`/`deps:` unchanged):

```text
contract: If B is a finite-dimensional C*-algebra, A is a finite-dimensional extended epsilon-C*-algebra, v:B->A is linear, and 0 <= delta <= delta', then if v is an extended delta-inclusion it is an extended delta'-inclusion, and if v is an extended delta-isomorphism it is an extended delta'-isomorphism and in particular an extended delta'-inclusion.
```

This is the exact special case needed by all four M18 maps. A finite-dimensional
C*-algebra carries its canonical exact (`epsilon=0`) amplified structure, so
the clause proof above applies without changing the locked definition.

### F2 — CRITICAL: Stage 2 cannot retain the old raw-call source, target, output, or raw-defect field

The design says at `DESIGN-M18-MONOTONE.md:80-85` to choose
`v_+:M_{r+1}->A_R`, bind `u_2:=v_+`, and form a raw-call record while
“retaining the supplied input, source, target corner, scales,
ambient-defect field, and raw-defect field.” This is false against the banked
provider. `lem-maincb-stage2-extcb-datum` already exports an explicit
raw-call record: its validated export node 1.7 records source `M_{|U|}`,
target `S^{A_R}_{P_U^R}`, literal output the outer-compressed map `T`, and raw
defect `delta`; `lem-maincb-stage2-call-envelope` node 1.6 packages that same
record. M16 subsequently admits an existential map with different
type `v_+:M_{r+1}->A_R`. Retaining the old source or target while setting the
output to `v_+` is ill-typed, and retaining the old literal output or raw
defect silently identifies or misrecords distinct data. This is exactly the
kind of opaque-boundary attachment prohibited by the W93 law.

**Exact correction:** use the envelope's closed EXT-CB datum only as M16's
analytic input. After existential elimination, construct a **new** Stage-2
`def-maincb-raw-call` record with source `M_{r+1}`, target `A_R`, literal
output `u_2:=v_+`, amplification family `1_{M_n} tensor v_+`, raw-defect
field `D_2*t`, and the already proved target ambient record; reuse only the
input reset data and genuinely unchanged base/post-helper scales. Do not call
this record the same record furnished by the envelope, and do not retain its
old source, target, output, or raw-defect fields.

### F3 — MAJOR: Stage 3 also has a pre-existing literal output and needs a new output record

The design's assertion at `DESIGN-M18-MONOTONE.md:101-106` that no
pre-existing literal map is replaced is also false at Stage 3. The validated
Stage-3 envelope export node 1.3.3 constructs and records a literal sum map
`v_R:B_U oplus B_V->A_R` before M17 is applied. M17's opaque contract says
that the four-corner datum “yields” an extended isomorphism `v`; it does not
export `v=v_R`. Naming the existential witness `u_3` is lawful, but identifying
it with the envelope's old output is not.

**Exact correction:** after applying M17, choose its witness `v` and construct
a new Stage-3 raw-call record with the same source and target, literal output
`u_3:=v`, its fixed amplification family, and raw-defect field `D_3*t`; reuse
the producer datum, input reset states, scales, and ambient record, but do not
assert equality with the envelope's prior `v_R` or retain its `rho` raw-defect
field as the output-map defect.

### F4 — CONFIRMED AFTER F2-F3: the existential pattern is W93-lawful and M18's contract stays byte-identical

The W93 rule permits an anaphor that resolves inside one proof to that proof's
sole explicit choice; it forbids attaching same-named outputs of opaque
contracts without a typed equality. Therefore the lawful sequence is:
instantiate the provider existential, choose one witness, define the new
literal raw-call output to be that witness, and use definitional equality only
inside that newly constructed record. With F2-F3, M18's phrase “furnished by
[envelope] with [extension/merge]” describes this composite construction and
does not require a ratified-contract amendment. Without F2-F3, the design's
claimed NO verdict is unsupported.

### F5 — CONFIRMED WITH A DENSITY WARNING: `12 / 3 / 16` is realistic, but only for the corrected records

The ten validated run-1 obligations remain mathematically reusable, not
validation-reusable. In particular, old nodes `1.6.2` and `1.6` cannot be
replayed verbatim: their wording attaches M17's existential result to the
envelope's prior literal output and must be replaced by F3's new-record node.
The twelve-node skeleton is otherwise arithmetically credible: compared with
the 20-node run it removes the Stage-1 provider/weakening parent split, the
two monotonicity-gap nodes, the redundant Stage-2 and Stage-3 parents, and the
ledger-assembly parent, while combining each existential choice with its new
record formation. Keep `12 / 3 / 16`; the four-node hard-cap headroom is the
right allowance if a verifier separates typed record construction from scalar
weakening. A seventeenth node remains a factoring stop.

## 3. Corrected re-seed obligations

The design may retain its twelve-node outline after making these two wording
changes:

1. Item 9 must say “choose `v_+`, construct a new Stage-2 raw-call record with
   source `M_{r+1}`, target `A_R`, and `u_2:=v_+`, then cite monotonicity and
   weaken the unit bound.”
2. Item 11 must say “choose `v`, construct a new Stage-3 raw-call record with
   `u_3:=v` without identifying it with the envelope's `v_R`, then cite
   monotonicity and weaken the unit bound.”

No definition change, second micro-row, T0 amendment, or M18 contract amendment
is required. The sole new row remains the corrected monotonicity micro-row in
F1, with design budget `3 / 2 / 6` and M18 re-seed budget `12 / 3 / 16`.
