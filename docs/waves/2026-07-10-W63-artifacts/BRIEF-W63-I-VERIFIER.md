# W63 batched HOSTILE verification — the I-horn routine batch (10 nodes)

You are a fresh, independent, HOSTILE verifier. You did NOT write anything in this
workspace. Finding a counterexample, gap, wrong constant, or quantifier error is a
BIG SUCCESS and exactly what you are paid for. You are the only mathematical check
these proofs will get before registry codification: be adversarial, not charitable.

## Object under review

`DECOMPOSITION-I.md` in this directory: a proposed decomposition of node I
(`conj-w62-isotropic-cotop-web-exclusion`, see context/DECOMPOSITION-W62-L5.md §1
for ALL shared notation). Your targets are its TEN routine nodes and their
Appendix A proofs:

  P  (priced ray package)          — §1.2 + A.1
  T  (tall halo saturation)        — §1.2 + A.1
  V  (dual co-top geography)       — §1.2 + A.1
  E  (universal exterior package)  — §1.2 + A.1
  ED (drift payer extraction)      — §1.2 + A.2
  EW (width payer extraction)      — §1.2 + A.3
  U  (ultra compression)           — §1.2 + A.4
  S0 (rim-to-SL1b package)         — §1.2 + A.5
  L0 (co-top SL1a package)         — §1.2 + A.5
  SC (selected-corner extraction)  — §1.2 + A.6

You are NOT asked to judge the six creative leaves (D, W, Sh, X, I∩, D∩) — they
are conjectures by design. But DO flag if a routine node's contract smuggles in a
creative claim, or if the §2 assembly's case analysis has a gap/overlap (boundary
ownership, quantifier order, constants threading in (2.1)-(2.2)).

## What to check, per node

1. **Contract vs proof**: does Appendix A prove EXACTLY the pinned contract —
   same quantifier order, same strict/non-strict boundaries, same constants?
2. **Dependency honesty**: every invoked registry shard (argument/lemmas/*.md —
   the full registry snapshot is in this workspace) must be quoted correctly:
   check the ACTUAL contract of `lem-l5-mass-barycenter-dualization`,
   `lem-l5-top-face-ray-formula`, `lem-l5-positive-flow-foldback`,
   `lem-l5-universal-exterior-payer`, `lem-top-deficit-price`,
   `lem-hx-transverse-moment-identity`, `lem-hx-financing-floor` (the CORRECTED
   A > 0 form!), `lem-hx-signed-variation-ledger`, `obs-height-collapse`,
   `lem-halo-collapse`, `lem-positive-exposedness-margin`,
   `lem-always-tight-dual-support`, `lem-optimal-face-conic-reduction`,
   `lem-cotop-witness-pinning`, `lem-zero-face-localization`,
   `lem-sl1a-score-selector`, `lem-sl1a-corner-ledger`,
   `lem-radial-horn-partition`, `lem-sl1a-three-cell-reduction`. If a hypothesis
   of the invoked lemma is not established at the call site, that is INVALID.
3. **Arithmetic**: recompute every displayed constant chain. High-suspicion
   targets: A.2's step from (A.3) to V >= c_m*b*tau/18 > k_b*tau (check
   M >= c_m vs M >= S >= c_m, the 1+M <= 9/4 claim, the tau <= c_m*b/120 use);
   A.3's (A.4) and the claimed c_m*b*tau/64 = k_b*tau (is it >= or = ? factor
   of s_+s_- handling); A.4's (A.5) 9/512 arithmetic and the M <= 5/4 claim;
   A.5's (A.6) 33/28 and (A.7) 2/7 bounds (check the 1-theta denominators and
   tau ceilings actually used); A.1's T derivation (sign of 1-sigma_g, the
   63 in (0.2) vs (T)); the SC ledger arithmetic 1/4 - 1/8 - 1/16 = 1/16 and
   whether `lem-radial-horn-partition` really yields Gamma_f(B) >= 1/4 for an
   ARBITRARY legal kernel.
4. **Clone audit**: for ED, EW, U, S0, L0: re-derive with a fiber split into two
   clone rows and with a partially selected fiber; any index-level (non-full-fiber)
   step is INVALID.
5. **Financing-floor legality**: ED/EW must construct A_lev > 0 and satisfy the
   corrected `lem-hx-financing-floor` hypotheses EXACTLY (read the shard); the
   forbidden vanished-endpoint call is any use where the pair separation is not
   bounded below at the call site.
6. **W62 interface**: the ten contracts must be consistent with the parent tree
   (context/DECOMPOSITION-W62-L5.md node I): same hypothesis class, boundary
   ownership vs sibling C (I strict at 1/8, 1/16), no silent enlargement.

## Output format (MANDATORY)

Write `VERDICT-W63-I-BATCH.md` in this directory. For each node one line:

  <NODE>: VALID | INVALID | VALID-WITH-CORRECTION — <one-sentence reason>

followed, per non-VALID node, by a precise description of the defect (the exact
displayed equation/step, a counterexample if you have one, and the minimal honest
restatement if one exists). Then one line:

  ASSEMBLY: SOUND | GAP — <reason>

Then a short section "What I checked hardest" (so the orchestrator knows coverage).
Do not touch any other file. Charity is failure; a false VALID is the worst
possible outcome.
