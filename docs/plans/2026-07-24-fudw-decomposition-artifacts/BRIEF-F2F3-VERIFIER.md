# BRIEF — F2/F3 bridge proofs: FRESH HOSTILE VERIFICATION

You are a FRESH HOSTILE VERIFIER (codex, independent context — you are NOT the
prover and have seen none of its reasoning). Finding a counterexample, gap, or
error is a BIG SUCCESS. Object: docs/plans/2026-07-24-fudw-decomposition-artifacts/PROOF-F2F3-BRIDGE.md
(two contracts + proofs: F2 positive-unital compression; F3 retract-defect).

Read: CLAUDE.md (Laws); BRIEF-F2F3-PROVER.md (what was demanded, incl. the
permitted-material rule: nothing from the Kitaev source but sound definitions,
no quarantined/GAP row as input); the permitted sources it cites
(AUDIT-W73B-ROUTE-F.md, LEDGER-W74F-G-K.md, wave-2/W74F artifacts);
argument/lemmas/lem-prh.md and the lem-routef-prh-finish row in
DESIGN-FUDW-DECOMP-v3.md §2.5 (the exact hypothesis list the composition must feed).

Attack: (1) every inequality re-derived — hunt for a dropped factor, a wrong
norm (cb vs ∞→∞), an n- or k-dependence hiding in a constant; (2) the F2
commutativity + isomorphism construction — is it actually forced by the stated
hypotheses, or is there a counterexample algebra; (3) the composition check —
do F2+F3's conclusions LITERALLY match lem-routef-prh-finish's hypothesis list
(quantifiers, thresholds, constants); (4) permitted-material discipline — any
smuggled Kitaev theorem or quarantined-row use; (5) threshold arithmetic at
η ≤ (24K)^{-1}; (6) hypothesis hygiene — any hypothesis the downstream chain
cannot supply.

Output TWO files in the same directory, nothing else, no git:
VERDICT-F2F3-BRIDGE.md — line 1 `VERDICT: VALID | VALID-WITH-CORRECTIONS |
INVALID`, then per-contract verdict lines (F2, F3 separately), per-attack
findings with severity and ready-to-paste corrections, and a registry-impact
section (the exact contract text fit to register, if any);
ANSWER-F2F3-VERIFY.md — ≤8-line summary. Do not soften findings.
