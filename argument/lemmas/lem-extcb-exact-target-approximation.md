---
id: lem-extcb-exact-target-approximation
kind: lemma
contract: Exact-target complete approximation: there are universal C_app<infinity and a_app>0 such that every extended alpha-homomorphism T:M_r->B(H) with alpha<=a_app is completely C_app*alpha-close to one exact unital *-homomorphism mu:M_r->B(H).
defs: def-extended-epsilon-cstar-algebra
deps: lem-extcb-exact-target-correction
status: stated
af: none
provenance: DESIGN-FUDW-DECOMP-v4.1.md register row (EXT-CB premise APP, approximate_algebras.tex 1508-1535), contract UNCHANGED from the register; role narrowed to the M_r bridge per DESIGN-GAP-EA.md §2.2 (aism-fbh8, design codex job 2026-07-26)
owner: A
---

**Status.** The v4.1 register's exact-target row, unchanged contract, now
positioned as the M_r-specific BRIDGE over the general
`lem-extcb-exact-target-correction` (DESIGN-GAP-EA.md option (a)). `stated`
until its own (tiny) af workspace validates.

**Bridge scope.** The proof should ONLY unpack the extended-homomorphism
definition (`def-extended-epsilon-cstar-algebra` carries the cited definition
of an extended delta-homomorphism and its amplifications), specialize B = M_r,
and identify a unital dagger-homomorphism with a unital *-homomorphism. It must
NOT import `conj-hcb`, `def-extcb-datum`, or the h11/v notation of the
`conj-extcb` node 1.3.1 consumer pattern (DESIGN-GAP-EA.md §4.2). Frontmatter
deviations from the v4.1 register row, both design-justified: no
`def-extended-delta-inclusion` (the hypothesis is a homomorphism, not an
inclusion) and no `def-operator-space` (absent from definitions/ — a dangling
id is a linker error).

**Seeding plan (after the correction row validates).** 2-3 nodes: root + one
definition-unpacking application (+ optional dagger-vs-* terminology bridge if
the verifier demands it). def-add: `def-extended-epsilon-cstar-algebra`.
External: the full validated contract of `proofs/lem-extcb-exact-target-correction`.

**Consumers.** `lem-extcb2-exact-representation` (keeps deps `conj-hcb`;
`lem-extcb-exact-target-approximation` per the v4.1 register).
