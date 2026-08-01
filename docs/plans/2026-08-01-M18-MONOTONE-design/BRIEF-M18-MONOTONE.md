# BRIEF — M18 factoring: the extended-inclusion monotonicity micro-row (mini round)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation; do NOT run git commit, git push, fr, or bd. Write to
`docs/plans/2026-08-01-M18-MONOTONE-design/DESIGN-M18-MONOTONE.md`.
A fresh hostile audit and user ratification follow. This is a MINI round:
one micro-row + M18 re-seed guidance.

## The finding (M18 run 1, 2026-08-01)

M18 `lem-maincb-reset-constant-ledger` (contract at
`argument/lemmas/lem-maincb-reset-constant-ledger.md:4`, ratified) ballooned
20 nodes vs cap 16: the tree re-derives, once per stage map (u_0..u_3), the
monotonicity of extended inclusions/isomorphisms in the defect parameter.
Verifier challenges (read them in
`proofs/lem-maincb-reset-constant-ledger/ledger/`):
- `ch-ae7afbfbfbef6df2` / `ch-7074ef6283d51193`: the inference
  "u_1 is an extended D_1*t-inclusion and D_1 <= D_* hence u_1 is an
  extended D_**t*-inclusion" needs an explicit imported fact — neither
  `def-extended-delta-inclusion` alone nor any validated dep exports it.
- `ch-1c8446308b75fbed`: M16 concludes the datum ADMITS some
  v_+ (existential); M18 speaks of "the literal maps u_2 furnished by" —
  the instantiation step must be explicit and lawful.

## Your task

1. **The micro-row** — propose id (suggestion:
   `lem-maincb-extended-inclusion-monotone`): one physical ASCII line
   stating defect-monotonicity for extended delta-inclusions AND extended
   delta-isomorphisms (bijectivity carries over trivially): if v is an
   extended delta-inclusion (resp. isomorphism) between the appropriate
   finite-dimensional objects and 0 <= delta <= delta', then v is an
   extended delta'-inclusion (resp. isomorphism) — with whatever typing
   and range constraints (e.g. delta' below a definitional validity
   ceiling, if any) the locked defs force. Check
   `definitions/def-extended-delta-inclusion.md` and the pinned source
   loci it harmonizes (`approximate_algebras.tex:443-456,1477-1484`) for
   every clause (delta-homomorphism clauses incl. the unit clause;
   two-sided norm bounds) and confirm each is monotone in delta — if any
   clause is NOT monotone, STOP and report (that would be a route-level
   problem). Defs/deps (expect: defs only, deps none), provenance, budget.
2. **The existential-instantiation guidance** for M18's re-seed: the
   lawful one-node pattern fixing one v_+ from M16's existential
   conclusion and binding u_2 := v_+ (same for the other stage maps if
   affected). State whether M18's CONTRACT needs any wording change for
   this (expected: NO — the 'furnished by' phrasing is realized by
   explicit instantiation nodes; if you find it genuinely anaphoric,
   STOP and say so — that would be a ratification item).
3. **M18 re-seed guidance**: which of the 10 validated nodes survive;
   the new budget (with the micro-row imported, the four monotonicity
   re-derivations collapse to citations — expect the tree back under the
   original 12/3/16).
4. **Risk register**: top attacks on the micro-row; top two ways this
   design could be wrong.

## Hard constraints

- Exactly ONE new micro-row; NO def changes; NO T0 or ratified-contract
  amendments (M18's contract stays byte-identical unless task 2 forces a
  STOP). Typed-witness laws; dimension-free; exact refs/ loci (L1).
