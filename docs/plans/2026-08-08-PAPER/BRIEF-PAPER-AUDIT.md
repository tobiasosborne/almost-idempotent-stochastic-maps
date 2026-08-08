# BRIEF — fresh faithfulness audit of paper/main.tex

You are a fresh hostile reviewer. You did NOT write `paper/main.tex`. Your
job: find every place where the paper is unfaithful to the repository's
actual state, overclaims, or would embarrass the authors in front of the
target reader (someone who knows Kitaev arXiv:2405.02434 and takes it on
faith). Finding errors is a BIG SUCCESS.

## Mandatory checks

1. **Theorem faithfulness.** The main theorem statement must match the
   strengthened `lem-routef-k-ledger` + `lem-routef-f0-assembly` contracts
   (`argument/lemmas/`): constants eta_0 = eta_K, C = K + 4*sqrt(2K),
   dimension-free, exponent 1/2, the correct norms on each side.
2. **Constant fidelity.** Every printed constant (C_theta, C_A, C_E,
   epsilon_E, eta_A, K, rho_fac, eta_K, the 2/3/24/4/sqrt(2) numerology)
   must match the registry/definition formulas
   (`definitions/def-routef-raw-factor-setting.md` (1.1)-(1.8), the F2/F3/
   PRH contracts). No invented, simplified, or misattributed constant.
3. **Attribution honesty.** Kitaev's results attributed to Kitaev; the
   repair and stochastic descent attributed to this work; no inflated
   novelty, no missing credit. Check each bibliography entry is real and
   correctly cited (no hallucinated references — check against
   refs/manifest/SOURCES.md where possible).
4. **Status honesty.** The mandatory formalisation-status remark must be
   present, accurate (lemma-level machine-adversarial validation done;
   top-level assembly in progress; no claim of completed formal
   verification), and not weaselly in either direction.
5. **Norm/picture discipline.** Every estimate says which norm (cb on M_n
   vs infinity->infinity on l_inf^n) and every crossing is marked.
6. **Mathematical correctness of the sketched arguments.** The diagonal
   seam identity, the descent chain F2 -> F3 -> PRH, and the sharpness
   family must be stated correctly (check against the registry contracts;
   the proofs are taken on faith but the STATEMENTS must be exact).
7. **Audience fit + length.** 3-5 pages, no re-exposition of Kitaev, the
   novel steps carry the weight, prose is tight.

## Verdict format

Write EXACTLY ONE file: `docs/plans/2026-08-08-PAPER/AUDIT-PAPER.md`,
headed `VERDICT: PUBLISHABLE-DRAFT` / `VERDICT: CORRECTIONS-REQUIRED`
(with an exact numbered correction list: locus + old text + required text)
/ `VERDICT: REWRITE` (fatal unfaithfulness first). Then numbered findings,
most severe first.

## Discipline

Write ONLY the verdict file. Do NOT edit the paper or anything else. No
git commit/push. Final message: verdict line + top three findings, <=6 lines.
