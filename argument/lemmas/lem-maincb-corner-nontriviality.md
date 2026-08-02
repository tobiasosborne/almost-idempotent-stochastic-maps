---
id: lem-maincb-corner-nontriviality
kind: lemma
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, w:C^m->A is an extended W.c0_cb*epsilon-inclusion, and e_j is any projection-basis element of C^m, then P_j=w(e_j) is a W.c0_cb*epsilon-projection satisfying | ||P_j||-1 | <= W.c0_cb*epsilon and hence is nonvanishing, while S_{P_j} contains a nonzero element and therefore dim S_{P_j} >= 1.
defs: def-maincb-witness-ledger; def-projection-basis; def-epsilon-cstar-algebra; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-delta-projection; def-compressed-corner
deps: lem-maincb-reset-constant-ledger; lem-maincb-structural-domain-ledger; lem-maincb-direct-corner-envelope; lem-maincb-witness-arithmetic
status: stated
af: seeded
workspace: proofs/lem-maincb-corner-nontriviality
provenance: DESIGN-M24-NONTRIVIALITY-v2.md sect-2.1 (landed verbatim; the aism-twpa option-(a) repair); AUDIT-M24-NONTRIVIALITY.md DESIGN-CONFIRMED (three editorial/provenance corrections applied verbatim in v2); user pre-ratified 2026-08-02 (tobiasosborne, in-session standing ratification of the audited design process, session 41); source refs/kitaev-2405.02434/approximate_algebras.tex:407-456,917-929,1054-1065,1067-1084,1477-1479; finite-dimensional linear algebra; M04 dependency provenance inherited from lem-maincb-direct-corner-envelope; 1417-1428 is Stage-1 context only
owner: A
---
**Status.** `stated` — the NEW additive nontriviality provider closing the
M24 contract-level gap (bead `aism-twpa`: challenges ch-94ae993f6abc0f5b /
ch-7411a0325c917f52 established that no prior allowed input yields
`dim S_{P_j} >= 1`; ch-37eff8dcb9a3b5d1 rejected the root weakening as
scope drift). MAIN campaign additive row (post-M23,
pre-M24 in the serial elevation order). NOT proved in-repo; af elevation
pending.

**Route (design v2 sect-4.1).** Fix exactly the W supplied by M18; the
extended `W.c0_cb*epsilon`-inclusion clauses applied to the nonzero
self-adjoint idempotent `e_j` (norm one by the standard C*-fact) give the
`W.c0_cb*epsilon`-projection estimates and `| ||P_j||-1 | <= W.c0_cb*epsilon`
— the quantitative second alternative of `def-delta-projection`
("nonvanishing"). M20 gives `epsilon <= W.e_env <= e_env^0`, so M04
(`lem-maincb-direct-corner-envelope`) applies to the singleton `U={j}` and
types the exact vector space `S_{P_j}` as an extended `L^0*epsilon`-
C*-algebra whose unit is an element of that space; the frozen
witness-arithmetic chain `L^0*epsilon <= W.L*epsilon <= W.K_call*epsilon <=
W.r_reset <= [2*(1+K_disp)*D_*]^{-1} < 1` forces `| ||I_S||-1 | < 1`, so the
unit is nonzero and `dim S_{P_j} >= 1`. The paper's sentence at tex:1066
("It is clear that S_P = 0 iff ...") is deliberately EXCLUDED — it is
motivation, never an external.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
6 / 3 / 10. Per-node skeleton: DESIGN-M24-NONTRIVIALITY-v2.md sect-4.1.
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in
the proof body, never the contract (the derived `1/2` is proof arithmetic
only).

**Elevation guidance (BINDING, 2026-08-02; design v2 sect-8.1).** (i) FIRST
child = the same-instance ledger-alignment node: name the M04 witnesses
`L^0,e_env^0` selected before M18's W, record `W.L >= L^0` and
`W.e_env <= e_env^0`; NEVER make an existential reselection after W is
fixed. (ii) The nonvanishing estimate comes directly from the inclusion
norm clause at defect `W.c0_cb*epsilon` — no hidden `c0 >= 1`; the
compressed-unit nonzeroness comes separately from `L^0*epsilon <
1`. These are separate estimates. (iii) NO reset anywhere: this row uses
the original Stage-1 `w`; importing any reset provider is a design
violation. (iv) NO node may cite a PENDING SIBLING. (v) The unit furnished
by the M04 structure must be typed as an ELEMENT of the exact `S_{P_j}` —
no isomorphic-copy substitution; the elementary fact "a finite-dimensional
vector space containing a nonzero element has dimension >= 1" is
common-knowledge linear algebra, applied to that exact space.

**Provenance loci.** `refs/kitaev-2405.02434/approximate_algebras.tex:407-456`
(epsilon-C* + inclusion clauses), `:917-929` (P_alternatives +
nonvanishing), `:1054-1065,1067-1084` (compressed corners; excluding
`:1066`), `:1477-1479` (extended algebra definition).
