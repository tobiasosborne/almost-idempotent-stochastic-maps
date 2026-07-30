---
id: lem-maincb-error-improvement
kind: lemma
contract: Complete error improvement: there are universal epsilon_max^cb>0, delta_max^cb>0 and c_0^cb<infinity such that every extended delta-inclusion v:B->A from a finite-dimensional C*-algebra B into an extended epsilon-C*-algebra A with 0<=epsilon<=epsilon_max^cb and 0<=delta<=delta_max^cb can be replaced by an extended c_0^cb*epsilon-inclusion v_tilde:B->A that is bijective whenever v is bijective.
defs: def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-improvement-iteration
status: stated
af: seeded
workspace: proofs/lem-maincb-error-improvement
provenance: kitaev-2405.02434 approximate_algebras.tex:1256-1319 (DECOMP IMPROVE-CB; the narrowed hypotheses — finite-dimensional source B and epsilon <= epsilon_max^cb — are the literal source hypotheses at 1317-1319 that the v4.1 register text suppressed); DESIGN-GAP-EA.md §2.3 (narrowing USER-RATIFIED in-session 2026-07-26); DESIGN-FUDW-DECOMP-v4.1.md register row
owner: A
---

**Status.** IMPROVE-CB, the consumer gate of the GAP-EA discharge: `stated`
target of the MAIN-CB chain, now safe to seed. **Contract = the
DESIGN-GAP-EA §2.3 NARROWED form, user-ratified 2026-07-26** — the v4.1
register's broad form suppressed two literal source hypotheses
(finite-dimensional source algebra; ambient defect below a universal
epsilon_max^cb) and would have repeated the quarantined local-domain failure
pattern if seeded unnarrowed.

**Dep wiring (REWIRED 2026-07-30 per DESIGN-MAIN-STRUCTURE-v5.md sect-10
step 1; user-ratified).** Deps rewired from
`lem-extcb-exact-target-correction` to `lem-maincb-improvement-iteration`
(M02) — the audited MAIN design derives the complete error improvement
from the one-step improvement (M01) iterated to the K_floor*epsilon floor
(M02), exactly the source route approximate_algebras.tex:1256-1319.
CONTRACT BYTE-UNCHANGED (audit v4/v5: character-for-character exact).
Original 2026-07-26 wiring note preserved in git history.

**Proof shape (when seeded — remeasure independently, DESIGN-GAP-EA §3.3).**
The exact-target correction subtree alone does NOT prove this: the target
here is an extended epsilon-C*-algebra, not B(H), so the proof must treat an
approximate target and stop the Newton iteration at an O(epsilon) floor,
following approximate_algebras.tex:1256-1319. Bijectivity/lower-norm control
is separate (DESIGN-GAP-EA §4.7/§4.9). R12 applies; do not absorb a second
Newton chain by raising the node cap.

**Consumers.** The eight MAIN `stated` targets and the reset chain
(`lem-maincb-split-corner-defect`, `lem-maincb-reset-constant-ledger`, the
three raw-reset rows, `lem-maincb-stage1-strict-refinement`,
`lem-stage1-old-side-compression`) per the v4.1 register.
