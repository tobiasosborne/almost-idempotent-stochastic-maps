# Revision brief (post-review pass) — execute after codex quota refresh

Draft v1 status: builds clean (main.pdf); overclaim audit = directionally honest, P 0.88
after fixes (reviews/overclaim-audit.md); readability = FAILS self-containment, P 0.25
(reviews/readability-review.md, 25 numbered defects). The revision wave fixes BOTH lists.

## Wave plan (one codex writer per item, parallel; each touches ONLY its assigned files)
1. **rev-imports (sections 01, 04, 00):** state lem-classical-equiv + thm-cluster as formal
   black-box theorems (full hypotheses, constants, norms; source: ../../argument/lemmas/
   shards — quote contracts verbatim); add the formal op-exposed-hull problem statement;
   define the HLC assembly + A_HLC or delete the constant formula; fix roadmap promises
   (defects 4, 5, 6, 24).
2. **rev-separator (02, 06, 10, 99):** ONE canonical separator definition (φ ≤ 0 on C_W,
   sup_{C_W} φ = 0, φ(p_v) = H) propagated everywhere; prove Ω_g ≤ 2+4δ as a numbered lemma
   right after defining g; fix index convention; fix σ-discipline violations incl. the
   three-way σ distinction (defects 3, 8, 11, 12, 13, 14, 23).
3. **rev-lp (02, 07):** add the exposedness primal LP in standard form + one dual derivation
   ((♦)); expand every acronym (RF/ND'/SF/FC/CPL/MC/RW/WL) in lemma titles + glossary
   (defects 7, 22).
4. **rev-belt (06):** day-1 belt: formal statement (hypotheses + conclusion + audited
   constant) for EVERY named lemma, or demote explicitly to "historical inventory" with a
   boxed warning — user requirement is self-containment, so prefer formal statements
   (defects 21, 25).
5. **rev-corner (05, 09):** state the corner family + its two laws inside §05 (PROVED-mod-
   audit for the laws, exact algebra for the consequences); campaign-nickname glossary
   before the numerics table; appendix with the key data tables/certificates inline; add
   d13 FINAL verdict (outcome (c), linear law — source: notes/wave5 final section +
   notes/d13-smalldelta-witnesses.md) (defects 15, 16, 17 + d13 insertion).
6. **rev-status (03, 08, 10, 99 + all):** harmonize pushed-witness status (PROVED death
   certificate for a DEAD ROUTE; REFUTED reserved for the stronger false claim); split
   all-shallow "existence certificate" (proved-mod-audit) from "general exclusion" (open);
   overclaim items 1, 2, 4, 5 (insert missing hypotheses: hidden TOP vertex, δ ≤ 1/4,
   B = t* > 0 with t* = 0 separate); replace the stale "decisive unmeasured datum" with the
   post-swarm open + d13-confirmed status; reconcile glossary height-collapse formula with
   the s8 cap; write the real abstract (replace stub); make the B–S δ=0 theorem + desired
   perturbative statement explicit (defects 1, 9, 10, 19, 20 + overclaim 1-5).
Then: rebuild (latexmk), re-run BOTH reviews fresh, iterate once more if readability < 0.6.
