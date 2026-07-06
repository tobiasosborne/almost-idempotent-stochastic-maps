# Wave W27 — trunk <2>6 re-audit: HLC ⇒ op-exposed-hull, re-derived in-repo + hostile verification (2026-07-06, session 11)

**Node:** trunk <2>6 (sketch v6 ledger item 3 — the staleness rule's oldest debt), bd `aism-54g`.
**Design:** W22 pattern — fresh codex prover R (re-derive from the registered `op-hlc` contract;
`docs/ingest/report/kernel-conjecture.tex:193-221` + the sister-repo W2d grand-assembly note as
objects of study, not oracles) + SEPARATE fresh hostile verifier VR (ingest text OFF-LIMITS).
Prompts + raw answers in the session-11 scratchpad (`W27/`).

## Verdicts (verbatim first lines)

- Worker R: `PROVED (C_2 = C_1 for the row-hull matrix; op-exposed-hull constants c = 1/4 and
  C = max{4,C_1}; class = exact signed idempotents / near-positive projections with
  d = delta(P) <= delta_0)`
- Verifier VR: `VALID-WITH-CORRECTIONS (proof works for actual `d=δ(P)` with explicit
  `W(P)≠∅`/`H(P)` defined; it does not prove the registered loose-`δ` wording)`

## Results

1. **`lem-hlc-implies-exposed-hull` (codified, proved/af:none, VR's corrected contract).** If HLC
   holds in the well-defined form (every exact signed idempotent with d = δ(P) ≤ δ₀ has W(P)
   nonempty and H(P) ≤ C₁√d), then with C = max{4, C₁}, c = 1/4 every such P has every row within
   C√d of conv W_{C√d, c√d}(P). Mechanism: W(P) = W_{4√d, √d/4} by def-visible-set; e_v(ρ)
   monotone nondecreasing in ρ (far-set shrinks; VR re-derived with the t* = +∞ empty-far-set
   convention); hull containment + the HLC height bound. The inherited localization detour
   (C' = max(4A, 1/√a)) is unnecessary under the direct registered HLC form.
2. **Matrix form (body).** Row-wise ℓ¹-projection gives Q with rows in the hull,
   ‖P − Q‖_{∞→∞} ≤ C₁√d, Q1 = 1, δ(Q) ≤ d (convexity of the negative-part functional).
   **Q is NOT proved stochastic and NOT proved idempotent** — flagged loudly; the <2>7 consumer
   (thm-classical-factorization) must be audited against exactly this interface.
3. **AUDIT FINDING (the wave's payload): the registered `op-exposed-hull` contract has a genuine
   loose-δ mismatch.** Read literally ("neg mass ≤ delta" with ρ = C√δ, κ = c√δ for a FREE upper
   bound δ ≥ δ(P)), the implication is NOT what the assembly proves: monotonicity helps ρ but the
   κ-threshold GROWS with loose δ (e_v(C√δ) ≥ √d/4 does not give ≥ c√δ). The proved statement
   pins δ = δ(P). Closing the literal wording needs a robustness lemma
   (W_{4√d,√d/4} ⊆ W_{C√δ,c√δ} for d ≤ δ ≤ δ₀) — currently OPEN.
4. **W-nonemptiness surfaces AGAIN:** def-height defines H only for W ≠ ∅; op-hlc's contract is
   silent. The codified lemma makes nonemptiness an explicit hypothesis (consistent with W30's
   independent front). VR fixture: the W25 3×3 under canonical geometry (W = {v,s}, H = 0, Q = P).

## Trunk ledger effect

<2>6 moves from [mod-audit, never independently checked] to [reviewed, codified] **in the
d = δ(P) form, W-nonemptiness explicit**; the loose-δ robustness lemma and the
stochasticity-of-Q gap are now NAMED, PRICED interface items feeding the <2>7 re-audit. Honest
tiers: reviewed paper proof (L5); NOT af-validated, NOT L0-rigorous.
