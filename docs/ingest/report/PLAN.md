# Classical-Portfolio Report Plan

Purpose: a self-contained LaTeX report on the two-day classical-portfolio
campaign. Writers must transcribe from `STATUS-LEDGER.md` and `NOTATION.md`,
not directly from memory. Every result statement gets a status badge.

Shard rule: each `.tex` shard should target about 120-200 lines. The report is
design-only at this stage; prose writers fill the `%% TODO` stubs later.

## Global Writing Rules

- Define every nonstandard term on first use and list it again in `99-glossary-notation.tex`.
- Never write bare `sigma_v`; use `\sigma_v^{\mathrm{off}}` or `\widetilde\sigma_v`.
- Never state a numerical result as a theorem. Use `\numresult{...}` or the `Numerical` environment.
- Never state finite-corner constants as an asymptotic theorem.
- Every theorem-like block begins with one of `\provedbadge`, `\modauditbadge`,
  `\numbadge`, `\openbadge`, `\refutedbadge`, `\downgradedbadge`.
- The only main-project facts allowed are `lem-classical-equiv` and `thm-cluster`,
  plus their role in the reduction chain.

## Shard List

### `00-abstract-roadmap.tex` -- Abstract, Reader Contract, And Roadmap

Target length: 120-160 lines.

Content outline:
- State the original problem for row-stochastic almost-idempotents in one paragraph.
- Explain the two-day campaign outcome: not a full proof, not a counterexample, but a compressed residual.
- Give the honest headline chain: `op-classical <= op-exposed-hull <= HLC <= DMF`.
- Say explicitly that DMF / shallow-web stability is the single remaining open.
- Introduce the status discipline and tell the reader badges are part of the mathematics.
- Preview the corner theorem and its exact constants as finite-corner, not asymptotic.
- Preview the audited belt and the wave-5--9 new lemmas.
- Preview the numerics record and verification gates.
- Preview the dead-route map and methodology section.
- Include a short "what a reader needs" note: basic linear algebra, convexity, Markov chains.
- Do not include any proof details.

Source notes:
`HANDOFF.md`; `ORCHESTRATION.md`; `notes/wave5-sigma-wall-parallel.md`;
`notes/wave8-fable-closer.md`; `../../../docs/worklog.md`.

Definition dependencies:
none; this shard may name only terms immediately glossed in-place and deferred
to shards `01`, `02`, and `99`.

### `01-linear-markov-setting.tex` -- Linear And Markov Setting

Target length: 160-200 lines.

Content outline:
- Define row-stochastic matrix, stochastic idempotent, and almost-idempotence defect `eta`.
- Define the signed affine retraction model `P1=1`, `P^2=P`.
- Define row vectors `p_i` as both matrix rows and points in affine space.
- Define `l^1` geometry, convex hulls, `dist_1`, and diameter.
- Define positive/negative coefficient parts, `nu_i`, and `delta=max_i nu_i`.
- State the consumed `lem-classical-equiv` with `PROVED` badge.
- State the consumed `thm-cluster` with `PROVED` badge, only at the contract level.
- Explain why the rest of the report studies exact signed idempotents.
- Include a compact example paragraph showing how a row identity reads geometrically.
- Mark all constants as universal unless explicitly construction-specific.
- Avoid any main-project Jordan/positive-map material.

Source notes:
`../../../argument/INDEX.md`; `HANDOFF.md`; `ORCHESTRATION.md`;
`notes/mrp-decider-report.md` methodology normalization.

Definition dependencies:
none.

### `02-geometry-exposedness.tex` -- Exposed Vertices, Hidden Height, And Separators

Target length: 180-220 lines.

Content outline:
- Define `tau=sqrt(delta)`, `rho=4tau`, `kappa=tau/4`.
- Define `(rho,kappa)`-exposed row vertex using affine `h`.
- Define `W`, `conv W`, hidden vertices, top vertices, and height `H`.
- Define canonical separator `phi` and deficit `g_i=H-phi(p_i)`.
- Define `R_g=osc(g)` and state why report avoids source-note `R`.
- Define formal off-self mass `sigma_v^{off}`.
- Define `tilde sigma_v` and the wave-8/9 convention, including the self-row caveat.
- Define carriers, carrier weights, own-site mass, and off-own-site mass.
- Give the first warning: old `sigma_v` branch statements are ambiguous.
- State W-rows-deep as a small `PROVED` observation.
- Include a boxed "notation clash audit" pointing to `NOTATION.md`.

Source notes:
`notes/wave8-fable-closer.md` Stage 0 and N3;
`notes/wave5-sigma-wall-parallel.md` w9chain/w9deep;
`notes/d12-dmf-depth-profiles.md`.

Definition dependencies:
`01-linear-markov-setting.tex`.

### `03-main-results-status.tex` -- Main Results And Status Table

Target length: 140-190 lines.

Content outline:
- Present the report's theorem-like inventory as a status table.
- Separate proved facts, numerical facts, conditional reductions, and opens.
- List the chain entries exactly as in `STATUS-LEDGER.md`.
- State `op-classical` remains open.
- State `op-exposed-hull <= HLC` is proved-mod-audit in the exploration lane.
- State `HLC <= DMF` is proved-mod-audit.
- State DMF and shallow-web stability are open.
- State corner closed forms are proved-mod-audit for the corner family.
- State the finite-corner calibration retraction.
- State numerics are evidence, not theorems.
- Point readers to later shards for proofs and details.

Source notes:
`report/STATUS-LEDGER.md`; `HANDOFF.md`; `notes/wave5-sigma-wall-parallel.md`;
`notes/wave8-fable-closer.md`.

Definition dependencies:
`01-linear-markov-setting.tex`; `02-geometry-exposedness.tex`.

### `04-reduction-chain.tex` -- Reduction Chain To The Residual

Target length: 180-220 lines.

Content outline:
- Draw the reduction chain as a displayed implication diagram.
- Explain `op-classical <= thm-cluster + op-exposed-hull`.
- Explain `op-exposed-hull <= HLC` and cite the two-family assembly status.
- Explain the old `HLC <= sigma_v-wall` route and why it is now notation-sensitive.
- Explain the final `HLC <= DMF` chain.
- State the corrected inequality `H <= tau(2+4delta)/(4m*) + E(delta)`.
- Explain when `a -> 4m_*^2` is legitimate: only `E=o(tau)`.
- Include the `t_*=0` closure from w9chain as part of the conditional chain.
- Explain why top-vertex WLOG is height-max only, not arbitrary hidden vertex.
- State what is not proved: DMF itself.
- Do not include day-1 belt details here.

Source notes:
`notes/wave2/W2d-grand-assembly.md`;
`notes/wave2/assembly-verification-opus.md`;
`notes/endgame-sigma-wall-residual.md`;
`notes/wave5-sigma-wall-parallel.md` w9chain;
`notes/wave8-fable-closer.md` Sec. 3.2'.

Definition dependencies:
`01-linear-markov-setting.tex`; `02-geometry-exposedness.tex`;
`03-main-results-status.tex`.

### `05-corner-theorem.tex` -- The Finite Corner And Exact Constants

Target length: 160-210 lines.

Content outline:
- Define the "corner" as the finite scale where hiding threshold meets the budget family.
- State the exact constants `tau_*=2-sqrt(3)`, `delta_*=(2-sqrt(3))^2`.
- State the wall value `H/tau=2(2-sqrt(3))`.
- State the floor `(7+4sqrt(3))/4`.
- Give the algebraic derivation from `tau^2-4tau+1>0` at the design level.
- Badge the theorem `PROVED-mod-audit`, with the exact family-law caveat.
- Explain the numerical confirmations from d9/d10/d11.
- Explicitly retract the reading "this is the asymptotic obstruction".
- Explain the budget line `H=2delta` and why it blows up as `delta -> 0`.
- Explain why slack-bearing arguments cannot recover the finite constants.
- End with writer warning: no global theorem from the corner alone.

Source notes:
`notes/wave8-fable-closer.md` N1-N6 and Sec. 3.1;
`notes/wave5-sigma-wall-parallel.md` audit 2;
`notes/d9-dual-certificates.md`;
`notes/d10-certificate-mining.md`;
`notes/d11-scale-disambiguation.md`.

Definition dependencies:
`01-linear-markov-setting.tex`; `02-geometry-exposedness.tex`.

### `06-day1-belt.tex` -- The Audited Day-1 Belt

Target length: 180-220 lines.

Content outline:
- Introduce the belt as audited local facts, not the final proof.
- Present L1, L2, L2', C10, L4, L5', L6, N1, F1, X1, X2 in a table.
- Include exact caveats: L2 recursion downgraded, L5 general false, L6 frame-transfer open.
- Present the fable belt F-SS, F-ND, F-E, F-GB, F-WR, F-BC, F-2R.
- Define `Gamma=P(g^2)-g^2` only as the classical kernel-energy object.
- State side conditions for F-WR.
- State F-psi literal is refuted and not in the proved belt.
- Explain how the belt constrains but does not close the residual.
- Include a short "audit status" paragraph: constants from wave4 summary dominate originals.
- Avoid deriving new lemmas.

Source notes:
`notes/wave4/audit-summary.md`;
`notes/fable-hlc-attack.md` Sec. 6;
`notes/wave1/A1-lone-far-row.md`;
`notes/wave1/A2-recursion-triple.md`;
`notes/wave1/A3-canonical-frame-trio.md`;
`notes/wave1/A4-clipping-and-leakage.md`;
`notes/wave1/N1-no-staircase.md`;
`notes/wave1/F1-projection-norm.md`;
`notes/wave3/X1-exactness-obstruction.md`;
`notes/wave3/X2-rank-induction.md`.

Definition dependencies:
`01-linear-markov-setting.tex`; `02-geometry-exposedness.tex`.

### `07-wave-lemmas-dual-witness.tex` -- Wave-5--9 Lemmas Around The Dual Witness

Target length: 190-230 lines.

Content outline:
- Define the exposedness LP and the `(diamond)` dual witness.
- State W2 sharp exchange with `PROVED` badge.
- State W3 witness push-through as warning, not a proof engine.
- State RF, ND', SF, FC, CPL, MC, RW, WL with badges and caveats.
- Include the fixed ND' threshold and the `P_vv>=0` RF caveat.
- Explain alpha-loophole and the scalar A-dichotomy.
- Explain row-witness and W-locality as the final clean local facts.
- Summarize wave-5--7 reductions: supplier deficit, top-band localization, coupling.
- Mark carrier-blocker coupling and aggregate pinning open.
- Mark raw `R Lambda` route downgraded for gauge dependence.
- Keep proof sketches short; this is a report, not the full notebook.

Source notes:
`notes/wave5-sigma-wall-parallel.md`;
`notes/wave8-fable-closer.md`;
`notes/d9-dual-certificates.md`;
`notes/d10-certificate-mining.md`;
`notes/d11-scale-disambiguation.md`.

Definition dependencies:
`01-linear-markov-setting.tex`; `02-geometry-exposedness.tex`;
`06-day1-belt.tex`.

### `08-residual-dmf.tex` -- DMF, Shallow Webs, And The Remaining Open

Target length: 180-220 lines.

Content outline:
- Define DMF precisely with `m_*` and `E(delta)`.
- Distinguish universal DMF and existential DMF.
- State existential DMF suffices for HLC.
- Explain W-rows-deep and the role of optimal witnesses.
- State `tilde sigma` height-collapse and the small-`tilde sigma` branch.
- Explain the contrapositive: small delta forces the web case.
- Define all-shallow witness and shallow hidden web.
- State w9cycle partial exclusions: direct two-site, disjoint two-ball, non-skinny payment.
- Mark the skinny spread-web regime open.
- Explain quantitative Baake-Sumner stability as the conceptual missing theorem.
- Include the literature positioning: virgin quantitative Douglas-Ando/Baake-Sumner ground.
- End with the precise remaining problem in one boxed open statement.

Source notes:
`notes/wave8-fable-closer.md` Sec. 3.4;
`notes/wave5-sigma-wall-parallel.md` w9chain/w9deep/w9cycle/post-w9;
`notes/d12-dmf-depth-profiles.md`;
`notes/literature-sweep-hlc.md`.

Definition dependencies:
`02-geometry-exposedness.tex`; `04-reduction-chain.tex`;
`07-wave-lemmas-dual-witness.tex`.

### `09-numerics-record.tex` -- Numerical Campaigns And Verification Gates

Target length: 180-220 lines.

Content outline:
- Explain what counts as numerical evidence in the report.
- State the robust W gate: multiplicity-correct vertices, presolve-off exposedness LP.
- State honest tau and exact idempotence gates.
- Summarize d8 MRP decider: no refutation, floor 3.484, middle regime safest.
- Summarize d9 dual certificates: common level functional, financier/frame-group blockers.
- Summarize d10: far top-band occupied, financier-law measured.
- Summarize d11: `g_f=H=2delta` family line, `M/tau >= 1.075`.
- Summarize d12: deep witnesses on tested stacking instances, later global interpretation downgraded.
- Include a "not theorem" warning before every table.
- Include reproducibility pointers to scripts and JSON outputs named in notes.
- Include the final numerics verdict: no exact counterexample found in verified campaigns.

Source notes:
`notes/mrp-decider-report.md`;
`notes/d9-dual-certificates.md`;
`notes/d10-certificate-mining.md`;
`notes/d11-scale-disambiguation.md`;
`notes/d12-dmf-depth-profiles.md`;
`HANDOFF.md` numerics summary.

Definition dependencies:
`01-linear-markov-setting.tex`; `02-geometry-exposedness.tex`;
`05-corner-theorem.tex`; `08-residual-dmf.tex`.

### `10-refutations-dead-routes.tex` -- Refutations, Downgrades, And Dead Routes

Target length: 160-210 lines.

Content outline:
- State the purpose: prevent future writers from resurrecting dead arguments.
- List literal psi-gap refutation and conditioned replacement.
- List literal `T_far=empty` as numerically false.
- List canonical-g energy route failure.
- List pure vertical functional overshoot.
- List row-exactness and diagonal-exactness no-gain at the blocker.
- List raw factorization gauge warning.
- List finite-corner calibration retraction.
- List d12 global-support downgrade.
- List L2 recursion and L5 general leakage downgrades.
- Include the "dead-route map" from the orchestration note in compressed table form.
- Close by saying the remaining open is not any of these routes, but DMF/shallow-web stability.

Source notes:
`ORCHESTRATION.md`; `HANDOFF.md`;
`notes/wave5-sigma-wall-parallel.md`;
`notes/wave8-fable-closer.md`;
`notes/d10-certificate-mining.md`;
`notes/d12-dmf-depth-profiles.md`.

Definition dependencies:
`06-day1-belt.tex`; `07-wave-lemmas-dual-witness.tex`;
`08-residual-dmf.tex`; `09-numerics-record.tex`.

### `11-methodology.tex` -- Multi-Agent Methodology And Audit Catches

Target length: 130-180 lines.

Content outline:
- Explain the campaign structure: orchestrator, Codex workers, Claude-family audits, Fable closer.
- Define two-family audit and derive-first hostile review.
- State why status tags are methodological, not cosmetic.
- Explain numerical gates and red-green checks.
- Explain major catches: psi-gap refuted, NG' downgraded, sigma-tilde catch, d12 downgrade.
- Explain why independent workers converging on a residual is evidence but not proof.
- Mention local-only provenance and exploration-lane limits.
- Include a compact timeline of day 1 and day 2.
- End with handoff guidance for future proof writers: attack DMF, not dead routes.
- Do not include motivational prose.

Source notes:
`ORCHESTRATION.md`;
`HANDOFF.md`;
`notes/wave5-sigma-wall-parallel.md`;
`notes/wave8-fable-closer.md`;
`../../../docs/worklog.md`.

Definition dependencies:
`03-main-results-status.tex`; `09-numerics-record.tex`;
`10-refutations-dead-routes.tex`.

### `99-glossary-notation.tex` -- Glossary, Notation, And Index

Target length: 160-220 lines.

Content outline:
- Transcribe the canonical notation table from `NOTATION.md` in LaTeX longtable form.
- Transcribe the jargon glossary from `NOTATION.md`.
- Include source-note mapping for notation clashes.
- Include a result-badge legend.
- Include an index of named results by status.
- Include a warning box: no bare `sigma_v`, no theorem from numerics.
- Keep definitions concise; first-use definitions live in earlier shards.
- This shard is allowed to repeat definitions because it is the explicit glossary.
- Do not add new notation beyond `NOTATION.md`.
- Keep it alphabetized by term where practical.

Source notes:
`report/NOTATION.md`; `report/STATUS-LEDGER.md`.

Definition dependencies:
all prior shards.
