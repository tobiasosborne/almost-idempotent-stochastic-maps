# BRIEF — hostile audit of `DESIGN-THMAINEXT-ELEVATION.md`

You are a **fresh, independent hostile auditor**. You did **not** write the
design and you owe it nothing. **Finding a gap, an error, an unsupported step,
a hidden premise, or a decorative dependency is a BIG SUCCESS** — it is the
outcome this repository most wants from you, because the single failure mode
guarded against here is a confident, plausible, WRONG-or-overclaimed result
leaking into the rigorous record.

Write your audit to

```
docs/plans/2026-08-03-THMAINEXT-ELEVATION-design/AUDIT-THMAINEXT-ELEVATION.md
```

Repo root: `/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps`.
Read `CLAUDE.md` §§0–6 first. **Audit only** — mutate no registry shard
(`argument/`), no definition (`definitions/`), no proof workspace (`proofs/`),
and no status anywhere. Your only new file is the audit.

## What you are auditing

`docs/plans/2026-08-03-THMAINEXT-ELEVATION-design/DESIGN-THMAINEXT-ELEVATION.md`
— a fresh designer's `af` proof skeleton + seeding package for elevating
`lem-thmainext-conditional` (extended `th_main_ext` assembly) from
`proved-mod-audit` to af-validated T0. The commissioning brief is
`BRIEF-THMAINEXT-ELEVATION.md` in the same directory; read it, and hold the
design to it.

The design proposes a **nine-node tree**, hard cap 14, 17 provisioned
definitions, 7 registry externals, **no** ground-truth external. Its central
claim (its "Q-A route (1)") is that `lem-maincb-structural-assembly` (M28),
consumed as a single validated external, **already discharges** the existence
of the ledger datum `W`, so that no eighth import is needed.

## Context you must hold

- `lem-thmainext-conditional`'s `contract:` is **byte-FROZEN** and its `deps:`
  line (seven ids) is **FROZEN** — both user-ratified. A design that requires
  changing either is not thereby wrong; it is a **contract/import finding** that
  must stop and escalate. Say so plainly if that is what you conclude.
- All seven providers, and all 120 ancestors, are `status: proved` / `af:
  validated` (T0). `conj-hcb` / `conj-extcb` keep historical `conj-` prefixes
  with **no status semantics**.
- The workspace `proofs/lem-thmainext-conditional/` is an unseeded empty
  scaffold. Nothing has been seeded, proved, or banked. Your verdict decides
  whether anything is.
- Prior art you should use: `DESIGN-THMAINEXT-REWIRE.md` (the deps rewire,
  hostile-audited `DESIGN-CONFIRMED`) — especially its §3, which flagged
  exactly this witness-instantiation requirement; and
  `docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md` §§3–5, the
  paper-proof record the frozen contract encodes.

## Pre-checks already run by the orchestrator (do not redo; do challenge)

Mechanically verified before you were commissioned:

- all **17** named `definitions/def-*.md` shards exist;
- all **8** contract strings quoted in the design (the 7 providers + the target)
  **byte-match** the current `contract:` values in `argument/lemmas/<id>.md`.

These are provenance facts, not correctness facts. They do not tell you whether
the *right* definitions were provisioned, whether a needed one is missing, or
whether a quoted contract is being *used* consistently with what it says.

## Attack in this order (the design's own risk register — but you are not bound by it)

1. **Q-A: the hidden eighth premise (highest risk).** M28's contract opens
   *"Fix the `def-maincb-witness-ledger` datum `W` supplied by
   `lem-maincb-reset-constant-ledger`; …"* and closes *"hence
   `C_struct=W.c0_cb*W.K_call` and `e_struct=W.epsilon_MAIN` are finite positive
   universal witnesses."* `lem-maincb-reset-constant-ledger` is an ancestor of
   M28 but is **not** among the seven frozen deps of the target, so it will
   **not** be a registered import of this workspace.

   Decide independently — do not defer to the designer:
   - Is that contract, consumed as one `af` external, a **closed theorem** that
     supplies a usable `W` (the opening clause being an internal binder whose
     existential burden the closing clause discharges)?
   - Or is it a theorem **conditional on** a `W` that must be supplied from
     outside, so that a consumer without `lem-maincb-reset-constant-ledger`
     can derive only a conditional statement and cannot produce concrete
     universal `C_E`, `epsilon_E`?

   Check how `af` actually treats an external's statement text; check whether
   `def-maincb-witness-ledger` (pure **data** — it asserts no existence) can
   supply the datum; and look for **precedent** elsewhere in `proofs/` for a
   consumer importing a "Fix `X` supplied by `L`; …" contract *without* `L`.
   Note that M28's own workspace **did** register
   `lem-maincb-reset-constant-ledger` as an external.

   If your answer is the second reading, that is a **contract-level stop**: the
   correct outcome is DESIGN-REJECTED with the minimal amendment named (add
   `lem-maincb-reset-constant-ledger` to the frozen deps line, user-ratify,
   redesign) — **not** a patched skeleton.

2. **Decorative dependency branches.** The frozen contract asserts *how* the
   assembly is built ("the assembly **uses** the corrected squared COL-HILB
   estimate and the hostile-verified H-CB, EXT-CB, and Stage-1 reset packets").
   The design discharges this with three packet branches. Apply its own
   deletion test: remove `THX-COL`, `THX-HCB`, `THX-MERGE`, `THX-EXT`,
   `THX-IMPROVE`, `THX-RESET` in turn — does a phrase of the method clause
   genuinely become unproved, or does the root still go through? A branch that
   can be deleted without loss is a **decorative import**, and the design must
   be rejected for it. Judge honestly whether these packet nodes are
   load-bearing proof steps or restatements of imported contracts dressed as
   nodes.

3. **The provider-to-M28 trace (the design's own §6.3 self-flag).** The packet
   nodes are written as *conditional interfaces*; they assert no linkage such as
   `W.epsilon_MAIN <= e_H`. Is that sufficient for the method clause, or does
   the clause require the packets to be applied to M28's actual data — which
   would need threshold comparisons the seven frozen contracts may not supply?
   The designer flags this as a possible stop condition. Adjudicate it.

4. **Witness and map identity** (the 2026-07-28 typed-witness laws). Exactly one
   `W`, bound before `C_E`, `epsilon_E`; final `v:B→A` is M28's own typed
   witness. Reject a second ledger selection, an M19-R map substituted for `v`,
   an intermediate corner codomain renamed `A`, or binder unification by
   repeated notation.

5. **Reset same-map discipline** in `THX-RESET`, and any reliance on the
   undeclared M02/M18 ancestors.

6. **Squared / conditional clauses.** `THX-COL` must carry
   `C_col*e*||X||_{n,1}^2` (squared — the corrected replacement for the printed
   unsquared display at `refs/kitaev-2405.02434/approximate_algebras.tex:1551-1555`);
   H-CB inverse bounds must retain their level-one hypotheses; merge must use
   `rho+epsilon <= a_merge`, not `rho` alone.

7. **Universality leakage.** `C_E`, `epsilon_E` must be exactly M28's two field
   expressions, with no minimum against freshly selected packet thresholds and
   no dependence on `n`, dimension, class count, stage, or block data.

8. **Vocabulary hygiene and omissions.** Are 17 definitions the *right* 17? The
   binding lesson from M28 run 1 (ballooned 20 > cap 13, root never challenged,
   4 of 6 challenges traced to missing workspace vocabulary) is that a defs list
   sized to the CONTRACT is not sized to the PROOF. **What is missing?** Also:
   the design asserts no ground-truth external is needed because the tree
   performs no δ-homomorphism arithmetic — test that claim.

9. **Node cap.** Is 9 live / cap 14 realistic, or is the tree under-specified in
   a way that will balloon? Is the design's balloon-classification table right?

10. **Status boundary.** Confirm the design promotes nothing: target stays
    `proved-mod-audit` / `af: none`, T0 stays 168, `op-classical` stays OPEN.

## Deliverable

Open with a one-line verdict — exactly one of:

- `DESIGN-CONFIRMED` — sound and seed-ready as written;
- `DESIGN-CONFIRMED-WITH-CORRECTIONS` — sound after the enumerated corrections,
  each given as **verbatim replacement text** so it can be applied mechanically;
- `DESIGN-REJECTED` — a contract-level, import-level, or structural finding that
  must return to design/user. State the minimal amendment; do not repair it
  yourself.

Then: a section per attack above, each with your independent finding and the
evidence (file, line, quoted text) that supports it. Separate **substantive**
from **editorial** corrections explicitly. Close with what you could **not**
determine and what a prover/verifier cohort would most likely challenge first.

Do not soften a finding to be agreeable, and do not manufacture one to look
thorough. If the design is right, say so and say exactly why the strongest
attack fails.
