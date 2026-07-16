# W70 DTR/POTI codification install notes

## Verdict gate

- COV — `VERDICT-dtr-batch.md` line 1: `conj-w69-dtr-canonical-root-top-overlap: VALID`; installed as proved.
- POTI-R — verdict line 2: `conj-w69-dtr-pinned-deficit-oriented-tail-to-ray: VALID`; installed as proved.
- TC — verdict line 3: `conj-w69-dtr-tail-coherent-weakened-conversion: VALID`; installed as proved.
- ASM — verdict line 4: `ASM: VALID`; installed as a proved conditional lemma.
- POTI-0 and POTI+ have no proved verdict lines. They are installed only as `status: conjecture`, because ASM's valid verdict authorizes their registration as its named open hypotheses.
- No verdict line is INVALID or UNDECIDED. No proved node was withheld.

## Corrections and controlling clarifications

- **NO `VALID-WITH-CORRECTION` OCCURS IN THE GOVERNING VERDICT.** Therefore no provenance line carries a correction parenthetical.
- COV incorporates the verdict's controlling atomwise clarification at verdict lines 8-29: `rho(Q)` is the atomwise minimum and `rho(E)` is its additive extension. No nonadditive setwise minimum is used. Applied in the COV contract.
- TC incorporates the already-complete appendix arithmetic `D_0*delta = D_0*tau^2 <= (alpha*lambda/16)*tau` from appendix lines 521-547 and verdict lines 152-201. The verdict explicitly says no correction is needed. No attack-text abbreviation was promoted into the contract.

## Shards, definitions, dependencies, and transcribed ranges

- `conj-dtr-zero-oriented-surplus-exclusion`: defs `def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top; def-actor-hull; def-invisible-mass`; deps EMPTY. Contract from `DTR-ATTACK.md` lines 99-142 and 408-455, with exact EC from lines 429-434; the pinned common datum is appendix lines 11-86. Refuter shape from attack lines 740-744.
- `conj-dtr-positive-oriented-surplus-gap-exclusion`: defs `def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top; def-actor-hull; def-invisible-mass`; deps EMPTY. Contract from `DTR-ATTACK.md` lines 99-142 and 457-519, including the strict POG window at lines 461-469 and exact EC at lines 486-490; pinned datum from appendix lines 11-86. Refuter and boundary ownership from attack lines 746-751.
- `lem-dtr-canonical-overlap`: defs `def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top; def-actor-hull; def-invisible-mass`. Deps `lem-l5-mass-barycenter-dualization; lem-ihorn-selected-corner-extraction; lem-dcap-root-closure; lem-aesc-guarded-hull-split`, transcribed from appendix lines 102-122. Contract/proof transcription: appendix lines 88-192; controlling verdict audit lines 6-36.
- `lem-dtr-oriented-tail-ray-conversion`: defs `def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top; def-actor-hull; def-invisible-mass`. Deps `lem-dtr-canonical-overlap; lem-ihorn-selected-corner-extraction; lem-top-deficit-price; lem-top-support-dual-face; lem-l5-mass-barycenter-dualization; lem-l5-top-face-ray-formula`, transcribed from appendix lines 225-253, with the proved COV import named at line 251. Contract/proof transcription: appendix lines 194-434; controlling verdict audit lines 38-130.
- `lem-dtr-tail-coherent-conversion`: defs `def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top; def-actor-hull; def-invisible-mass`. Deps `lem-dtr-canonical-overlap; lem-dtr-oriented-tail-ray-conversion; lem-aesc-synthetic-finance-tail-amplification`, transcribed from appendix lines 480-499. Contract/proof and optional-upgrade transcription: appendix lines 436-623; controlling verdict audit lines 132-209.
- `lem-dtr-poti-assembly`: defs `def-signed-idempotent; def-visible-set; def-height; def-exposed; def-negative-mass; def-selected-corner; def-top-support-functional; def-co-top; def-actor-hull; def-invisible-mass`. Deps `conj-dtr-zero-oriented-surplus-exclusion; conj-dtr-positive-oriented-surplus-gap-exclusion; lem-dtr-canonical-overlap; lem-dtr-oriented-tail-ray-conversion; lem-dtr-tail-coherent-conversion; lem-dcap-tall-same-center-packet`. The two conjectures and COV/POTI-R are the conditional case-split imports at appendix lines 629-661; the B4 packet is lines 662-673; TC is included because the body claims weakened display (4.5), appendix lines 753-768. Exact-EC case split is appendix lines 678-713; strict close is lines 715-751; weakened consequence is lines 753-768; verdict audit is lines 211-285.

All six contracts reuse the registry text of `argument/lem-aesc-common-tail-union.md` contract line 4 verbatim through the definition of `D_tail`, then inline the appendix lines 66-84 carrier data and the DTR/POTI objects. The union floor is included because appendix lines 66-74 explicitly make it part of the pinned datum.

## Judgment calls — flagged loudly

- **JUDGMENT CALL: ASM CONTRACT SELECTION.** The user-specified deliverable requires the assembly contract's single conclusion to be exact EC and places the strict `7*c_m*tau/960` close in the body. The appendix heading “Minimal conditional contract” instead displays the strict close at lines 646-650, although its verified case split establishes exact EC at lines 678-713 and the verdict says exact EC is obtained before either B4 spend at lines 211-232. The shard follows the explicit deliverable: exact EC is the contract; the strict close is a displayed body consequence.
- **JUDGMENT CALL: EXPLICIT `x_u`.** The inherited registry prefix defines the normalized displacement through `(q_tilde_u,A_tilde_u)`. To obey the request that `x_u` be explicit without introducing undefined `a_u,D_u`, the contracts write `x_u = p_u-A_tilde_u*(q_tilde_u-p_u)`, the same pinned quantity as attack line 116 and `context/AESC-ATTACK-W67.md` equation (0.1).
- **JUDGMENT CALL: INLINE `L_v`.** The B4 shard writes `L_v = {Q : d_Q <= tau/4}` but leaves `d_Q` inherited. To satisfy the no-undefined-symbol constraint, the new contracts inline `d_Q = dist_1(p_Q,C_W)`, consistent with the shared selected-depth notation. `E_* = {R : ||p_R-p_f*||_1 > 1/2}` is copied literally from the B4 packet.
- **JUDGMENT CALL: DIRECT DEPS ONLY.** Dependency lists contain direct proof imports, not transitive prerequisites and not reduction-tree relations. This follows the W68 ruling in the request. The only deliberate body-consequence dependency is ASM's dependency on TC, expressly required because ASM records weakened display (4.5).
