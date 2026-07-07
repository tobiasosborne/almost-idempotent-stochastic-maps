# Wave W46 — the loose-delta ledger item RESOLVES to a contract re-wording (2026-07-07, session 12)

**Node:** trunk loose-delta (HANDOFF ranked item 3; W27 finding 3). **Design:** single
fresh-codex prover (worker AW: prove / refute / retire). Prompt + raw answer in the
session-12 scratchpad (`W46/`).

## Verdict (verbatim first line)

- Worker AW: `RETIRABLE + GAP (loose-delta robustness not proved/refuted; consumer
  bookkeeping runs with pinned d=delta(P); proposed re-wording below)`

## Results

1. **The robustness lemma stays OPEN but is NOT NEEDED.** The registered loose wording of
   `op-exposed-hull` does not follow from the W27 pinned proof (monotonicity gives
   e_v(C*sqrt(delta)) >= sqrt(d)/4, never >= c*sqrt(delta)); no refutation certificate
   either. But the ENTIRE downstream chain runs pinned: thm-cluster instantiates legally at
   delta = d = delta(P) (its strongest form), giving O(sqrt d); lem-classical-equiv
   (af-validated) converts d <= K*eta back to the stochastic O(sqrt eta). No consumer needs
   the free-upper-bound form (consumer loci quoted in the worker answer: thm-cluster.md:4,
   kernel-conjecture.tex:68-72, 193-220).
2. **Escalation (USER DECISION, converges with W45 G1/G4):** re-word `op-exposed-hull` to
   the pinned signed form (AW's proposed contract, worker answer §Codification) and re-audit
   `thm-classical-factorization`'s eta-scale geometry hypothesis (kappa >= c*sqrt(eta) should
   be allowed at sqrt(delta(P)), with only the final estimate in sqrt(eta)). Contract
   re-wordings ripple; queued for the user, not edited.

## Trunk ledger effect

The loose-delta item moves from OPEN MATH to a PENDING CONTRACT DECISION. If the user adopts
the pinned re-wording, the robustness lemma is retired without proof (nothing consumes it);
if the loose form is kept, the lemma returns to the ledger as genuinely open.

## Banking (orchestrator)

Wave doc + bd USER-DECISION issue only; no registry changes (contract changes escalate).
