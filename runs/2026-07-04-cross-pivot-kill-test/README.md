# Run bundle: cross-pivot mass kill test (arm G, post-wave-11) — 2026-07-04

**Status: L3 numerical evidence. NEVER rigorous.** Exact ℚ arithmetic throughout (no floats anywhere).
Orchestrator-authored decision check, run BEFORE dispatching arm G wave 12, per the 2026-07-04 session
audit ("cheap decisive pre-check instead of another narrowing wave").

## Hypothesis

Wave G11 reduced the dominant (PRT) collateral import to the cross-pivot masses
`B_{r,s} = Σ_i β_r(i)⁺ a_s(i)⁻` and `C_{r,s} = Σ_i β_r(i)⁻ a_s(i)⁺` and flagged that neither lives in
the pivot-s unified budget `G_class⁻ + S₋^μ + SIGMA (+FanRes)`. Kill question: on the certified
instances already in the record, does `B+C` dwarf the budget (⇒ the charge is dead on arrival and the
budget needs a fourth reactive patch), or is it comparable (⇒ the charge is a live proof target)?

## Command (re-run)

```bash
python3 runs/2026-07-04-cross-pivot-kill-test/scripts/cross_pivot_masses.py
```

Deterministic (no seeds, no search): rebuilds all six certified instances from their wave-recorded
`L`/`B` blocks (G5 two-orphan family at h=1/10, 1/100; the G9 (V) and (P) instances; the G10 δ=49/60
witness (UNCAPPED, tooling); the G11 near miss), asserts `BL=I`, `P²=P`, `P·1=1` on each, and computes
`B_{r,s}`, `C_{r,s}`, and the pivot-s budget at each certified argmin/maximal pivot for both
transverse `r`.

## Invariant / known-value check

The script HARD-ASSERTS, per instance, the exact `δ(P)` and budget totals recorded in the wave
artifacts and the orchestrator rechecks (e.g. G9-(V): δ=1/4, budget=4427/16640; near miss: budget
71/200), plus the structural idempotence checks; it exits nonzero on any mismatch. Final assertion:
12 (instance, r) pairs computed, `B_{r,s} = 0` on all of them.

## Finding (headline + honest scope)

1. **`B_{r,s} = 0` on every certified instance at every transverse pivot** — including the uncapped
   G10 witness. The mass G11 flagged as the unfinanced danger is absent from ALL existing data.
2. **`C_{r,s} ≤ 2δ` trivially** (observation, not part of the computation): `Σ_i β_r(i)⁻ = ν_{u_r} ≤ δ`
   is the transverse chart row's own negativity, and `a_s(i)⁺ ≤ 2` by the θ-½ Cramer box
   (proved-mod-audit wave material) — so the C-mass is financed at the δ scale unconditionally.
3. **All ratios `(B+C)/budget ≤ 2499/1376 ≈ 1.82`** (worst: G5 h=1/100); nothing explodes even uncapped.
4. **Scope limits (honest):** six instances only, all sharing the identity-block construction style;
   `B = 0` may be an artifact of that style — no sweep ever optimized FOR `B > 0`; the Cramer-box
   bound on C is mod-audit, not rigorous; comparability of `B+C` to the budget on these instances
   does NOT establish the (CHARGE) inequality anywhere.

**Consequence for the campaign:** the (PRT) cross-pivot residual localizes to the **B-question** — is
`B_{r,s}` forced to be 0 (or O(δ)) at capped θ-½ argmins? — plus one assembly check (does the (PRT)
chain tolerate the additive `2δ` financing of C?). No fourth budget patch is demanded by the data.

## Next

Arm G wave 12 (reframed, bd `aism-4uh`): (i) adversarial hunt for a capped certified argmin with
`B_{r,s} > 0` (realize it or prove `B ≤ C·δ` there); (ii) the assembly-tolerance check for the `+2δ`
term. `lem-import-reduction` deliberately NOT elevated pre-decision (session-audit policy).

## Addendum (2026-07-04, post wave G12)

The scope caveat above was warranted: wave G12 (`docs/waves/2026-07-04-G12-b-question.md`) REFUTED the
`B_{r,s} = 0` extrapolation with an exact certified capped argmin carrying `B_{1,2} = 2/57` (still
sub-δ: `B/δ = 8/57`). This bundle's data and invariants stand unchanged; only the tempting
generalization died, exactly as the honest-scope note anticipated. The live target is now the
branch-sensitive `B ≤ K·δ` (bd wave-13 issue).
