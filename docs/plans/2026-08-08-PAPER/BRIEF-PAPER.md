# BRIEF — draft the standalone paper (USER P0, 2026-08-08)

You are a fresh writer with deep familiarity with this repository. Draft a
**tight, elegant, SMALL paper (3–5 pages)** presenting the stochastic
stability theorem and its proof via the Kitaev factorization.

## Audience (fixed by the user)

A reader who **understands Kitaev's approximate-algebras work
(arXiv:2405.02434) and is happy to take it on faith**, and who is interested
in the **novel steps required to prove the stochastic version**. Do NOT
re-prove or re-expound Kitaev; cite and use. Spend the pages on what is NEW.

## The theorem (state with explicit constants)

There exist universal eta_0, C > 0, independent of dimension n, such that
every row-stochastic Q with ||Q^2 - Q||_{infinity->infinity} <= eta <= eta_0
admits a row-stochastic idempotent E with
||Q - E||_{infinity->infinity} <= C*sqrt(eta); one may take eta_0 = eta_K
and C = K + 4*sqrt(2K) for the explicit universal K, eta_K of the
factorization ledger. The exponent 1/2 is sharp (the explicit 3x3 family —
`ex-hume` in the registry; docs/ingest records its source).

## The narrative arc (the novel steps — this IS the paper)

1. **The diagonal seam (F0).** Complexify Q to Q_C on C^n, conjugate by
   diagonal extraction/inclusion D, J: Phi := J Q_C D is UCP on M_n and the
   defect transfers EXACTLY: ||Phi^2 - Phi||_cb = ||Q^2 - Q||_{inf->inf}
   (both directions; this is what lets a commutative l_inf problem enter
   the C*-machine with no constant loss).
   Sources: `argument/lemmas/lem-routef-f0-ucp-lift.md`,
   `lem-routef-f0-defect-identity.md`.
2. **The audited Kitaev interface, with a repair.** Kitaev's
   th_almost_idemp applied to Phi yields an extended epsilon-C*-structure;
   the defect linearizes (epsilon_AI(eta) <= C_A*eta with explicit C_A);
   his diagonal step required a genuine repair (the diagonal-repair /
   CP-ization pair) — say honestly and briefly what needed repairing; the
   extension/isomorphism step is packaged as an extension theorem with
   universal (C_E, epsilon_E). Sources: `lem-kitaev-almost-idemp-audit.md`,
   `lem-routef-ai-defect-linearization.md`, `lem-kitaev-diagonal-repair.md`,
   `cor-kitaev-diagonal-cpization.md`, `lem-thmainext-conditional.md`.
3. **The dimension-free factorization ledger.** UCP maps
   Delta: B -> M_n, Upsilon: M_n -> B (B a fd C*-algebra) with
   ||Delta Upsilon - Phi||_cb <= K*eta, ||Upsilon Delta - I_B||_cb <= K*eta,
   and the amplified approximate multiplicativity <= K*eta*||X||*||Y||,
   with K, eta_K explicit scalar formulas independent of n, amplification,
   block count and block dimensions. This is the content of the 19-row
   ledger family; present it as ONE theorem (the strengthened K-ledger
   contract text is in
   `docs/plans/2026-08-08-KLEDGER-STRENGTHENED/DESIGN-KLEDGER-STRENGTHENED-V2.md`
   §2 — use its statement; do not reproduce the 19 rows).
4. **Descent back to the stochastic category (the genuinely novel finish).**
   From the factorization: F2 compresses to positive unital A, M on the
   diagonal with ||Q - AM|| <= K*eta plus the retract estimates; F3 controls
   the retract defect ||MA - I|| <= 3K*eta/(1-3K*eta); the perturbed-retract
   finish (PRH) produces a genuinely row-stochastic idempotent E with
   ||Q - E|| <= (K + 4*sqrt(2K))*sqrt(eta) — this is where sqrt(eta)
   enters, and where positivity/stochasticity is preserved rather than lost
   to the C*-category. Sources:
   `lem-routef-f2-positive-unital-compression.md`,
   `lem-routef-f3-retract-defect.md`, `lem-routef-prh-finish.md`.
5. **Sharpness.** The explicit 3x3 family shows the exponent 1/2 cannot be
   improved (one short paragraph; source via docs/ingest + the registry
   `ex-hume` shard).

## Structure (suggested; you may improve it)

Title; abstract (3-4 sentences); §1 Introduction (the theorem, why
dimension-freeness is the point, one paragraph of context: idempotent
stochastic matrices = conditional expectations onto partitions; the delta=0
anchor); §2 The diagonal seam; §3 The factorization theorem (Kitaev on
faith + the repair + the ledger, stated); §4 From the factorization to a
stochastic idempotent (the finish, with proof sketch — this section gets
the most space); §5 Sharpness + remarks. Bibliography: Kitaev
arXiv:2405.02434 + the 2-4 genuinely needed classical references (check
`refs/manifest/SOURCES.md` for what the project actually pins; do not
invent citations).

## Honesty constraints (NON-NEGOTIABLE)

- The paper may state the theorem, but MUST carry one honest remark (a
  single footnote or end-remark, not more) that the argument has been
  machine-adversarially formalised at the lemma level in this project's
  registry with the final top-level assembly in progress; no overclaim of
  completed formal verification.
- Every constant you print must be one the registry actually exports (K,
  eta_K, C_A, C_E, epsilon_E, the F2/F3/PRH numerology 2/3/24/4/sqrt(2));
  do not invent or "simplify" constants.
- Attribute Kitaev's results to Kitaev plainly; attribute the repair and
  the stochastic descent as this work's contribution; no inflated novelty
  claims and no false modesty.
- Say which picture each estimate lives in (cb norm on M_n vs
  infinity->infinity on l_inf^n) at every crossing.

## Deliverable

Write EXACTLY ONE file: `paper/main.tex` — a self-contained LaTeX article
(standard `article` or `amsart`, amsthm, no external style files), tight
enough to compile to 3–5 pages. If `latexmk` or `pdflatex` is available,
compile to check it builds (build artifacts are disposable; do not commit
anything). Aim for elegance: full prose sentences, no bullet-point
mathematics, displayed equations only where they earn it.

## Discipline

Write ONLY `paper/main.tex` (plus disposable build artifacts). Do NOT edit
`argument/`, `definitions/`, `report/`, `proofs/`, or any doc. Do NOT
commit or push. Final message: <=8 lines — page count, section list, the
constants you printed, and any place you were forced to paraphrase a
contract rather than use it directly.
