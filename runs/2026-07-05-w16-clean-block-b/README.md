# Run bundle: clean-block B/δ amplification + direct-FE identity (arm G wave 16) — 2026-07-05

**Status: L3 numerical evidence + exact T1 identity certificate. NEVER rigorous.** Exact ℚ
throughout. Codex-worker-authored (prompt in the session scratchpad), orchestrator-recomputed
(see Invariant). Companion wave artifact: `docs/waves/2026-07-05-W16-b-restricted.md`.

## Hypothesis / adversarial question

Wave 16 on `conj-b-restricted` (B_{r,s} ≤ K·δ at capped θ-half Φ-argmins carrying a clean
Γ-block): prove via inadmissibility-surviving argmin structure, or amplify B/δ past ~1 on
certified clean-block instances.

## Headline findings

- **Amplify side:** 9 certified clean-block instances; best `B/δ = 0.7776403…` — achieved by the
  wave-13 record instance, which (NEW, verified here) itself carries a clean Γ-block at the tied
  argmin `(0,2,4)` (`Ψ = 1/200 < M ≤ Γ = 7/250`). The 0.77764 family wall binds identically with
  and without the clean-block constraint; cloning does not amplify; extra-carrier and
  rotated-bridge probes LOSE the clean branch. Crossing 1: NO.
- **Prove side (T1, exact, seed-verified):** the direct-FE identity
  `Σ_{k∈J} W_k(β_k − A_k^J) = S_J` (row reproduction in the s-coordinate, β-weighted over the
  carrier set J) — the G8 recipe applied to B itself. Conditional theorem: if the carrier
  self-defect `D_J ≥ λ·B` and `D_J ≤ C·δ` uniformly, then `B ≤ (C/λ)·δ`. Seed value
  `λ = 157/500`. The named residual = a uniform positive floor for `D_J/B`.
- The Γ-block SEES the carrier through the import ledger (single nonzero term, on the carrier
  row) but in the lower-forcing direction only.

## Honest scope

Verdict UNDECIDED. Evidence (bounded families, wall at 0.77764) leans toward the conjecture
being TRUE with `K ~ 1`; nothing here is proof. The `D_J/B → 0` hunt (the named killer/isolator
of the direct-FE route) has NOT been run — it is the follow-up decider.

## Command (re-run)

```bash
python3 runs/2026-07-05-w16-clean-block-b/scripts/w16_identity.py        # direct-FE identity + seed asserts
python3 runs/2026-07-05-w16-clean-block-b/scripts/w16_b_restricted.py    # 9-point certified amplifier
python3 runs/2026-07-05-w16-clean-block-b/scripts/orch_verify_best_point.py  # independent check
```

## Invariant / known-value check

Worker scripts hard-assert: `B·L = I₃`, `P = L·B`, `P² = P`, row sums 1, complete θ-half
enumeration, argmin/maximal-pivot/clean-block per point, `A = B + C − D`, the G12 + wave-15
calibrations, the direct-FE identity lhs = rhs on the seed, and best ratio < 1.
**Orchestrator recomputation (independent code, `scripts/orch_verify_best_point.py`):** rebuilds
the best point's P from L,B; re-derives coordinates, volumes, θ-half census, the argmin TIE,
the clean Γ-block (searching all tied argmins), and `B/δ = 0.7776403123839672` — match. Exit 0.

## Next

Follow-up decider (wave-16b, dispatched same day): minimize `D_J/B_{r,s}` over certified
clean-block instances — a certified family with `D_J/B → 0` kills the direct-FE proof route; a
persistent positive floor isolates the exact theorem to prove for `conj-b-restricted`.
