# BRIEF — W73b hostile audit of Route F steps F0–F3 (aism-u4x5)

You are a FRESH, HOSTILE auditor. Your job is to try to BREAK the Route F derivation.
Finding a gap, a wrong constant, a misread hypothesis, or an inapplicable theorem is a
BIG SUCCESS. Confirming a step without finding a flaw requires you to have genuinely
attacked it. You never take the strategist's word for anything.

## Sources (all local, byte-verified)

1. THE PAPER (ground truth): `refs/kitaev-2405.02434/approximate_algebras.tex` —
   Kitaev, "Almost-idempotent quantum channels and approximate C*-algebras",
   arXiv:2405.02434v2. Byte-identical to the official arXiv e-print (SHA256
   e7eb512a2ec2438d…). The import target is `th_factorization` (tex line 2730,
   §"Approximate factorization through a C* algebra") and everything its proof rests on
   (notably `th_almost_idemp`, `th_main_ext`, and the §12 apparatus).
2. THE DERIVATION UNDER AUDIT: `docs/plans/2026-07-22-W73-artifacts/STRATEGIST-C-factorization.md`,
   sections "Root 0" through "Root 3" (and the constants in "Root 5"). Cross-reference:
   `docs/plans/2026-07-22-W73-artifacts/STRATEGIST-A-clean-slate.md` §I (an independent
   derivation of the same architecture; note where they disagree).
3. STATED third-party context (NOT verified; treat as leads, re-derive anything you use):
   `../almost-idempotent-channels/paper/FINDINGS.md` — a sibling implementation campaign's
   log of paper issues. Relevant entries: A2 (finite Pauli 1-design direct-sum diagonal
   non-centrality), C13 (F-ancilla ordering; lem_RC), C14 (Δ′ CP-ization is exactly-CP
   only for exact homomorphisms; measured O(η²) Choi negativity at multi-block η>0;
   proposed cone-projection repair), D1 (Lefschetz–Hopf non-constructive), D2 (universal
   constants unstated; empirical canaries), D4 (th_factorization proof is outline-level).
4. Problem context: `docs/plans/2026-07-22-W73-artifacts/stateofplay/00-brief.md`.

## The five audit questions — deliver a per-question verdict line

**Q1 (statement shape).** Does `th_factorization` as printed assert exactly:
(i) ‖ΔΥ−Φ‖_cb ≤ O(η); (ii) ‖Υ_n(Δ_n(X)Δ_n(Y)) − XY‖ ≤ O(η)‖X‖‖Y‖ for all
X,Y ∈ M_n⊗B (hence ‖ΥΔ−1_B‖_cb ≤ O(η)), with Δ, Υ UCP and B a finite-dim C*-algebra?
Verify the orientations and quantifiers character-by-character against the tex.

**Q2 (universality of the constants).** Trace what "O(η)" means in this paper: locate the
paper's convention (§2 / the main-theorem statements, e.g. tex:460/484 region) and
determine whether the constants in th_factorization are claimed UNIVERSAL (independent of
dim H, dim B, the number of blocks m, and the block dimensions). Then trace the proof
chain (th_factorization → th_almost_idemp → th_main_ext → the §5–§9 machinery) and flag
EVERY place where a constant could silently acquire dimension dependence. The sibling
repo's D2 entry claims the analytic constants were never extracted — assess whether the
CLAIM of universality is nevertheless clearly made and consistently maintained.

**Q3 (proof soundness of th_factorization itself).** The proof is an outline plus explicit
constructions (tex:2742–2899). Audit it as written: (a) the Δ′ CP-ization argument at
tex:2786–2796 — is the manifest-positivity claim valid for an approximate (not exact)
homomorphism Δ̃? (The sibling C14 entry says NO as written, with an O(η²) defect and a
repair that stays within O(η) — independently assess both the gap and whether the repair
[nearest-CP-map / cone projection] genuinely preserves ALL the claimed bounds, including
(5.4)-type multiplicativity, not just ‖Δ−Δ̃‖.) (b) lem_RC and the Υ′ construction
(tex:2840–2899) — check each step's stated bound. (c) The dependence on th_main_ext:
state precisely what th_main_ext must deliver (an extended O(η)-isomorphism v with which
properties?) and whether the paper proves it at that strength.

**Q4 (the classical lift, step F0).** For Φ = J∘Q∘D (J diagonal inclusion, D diagonal
conditional expectation onto ℓ∞(n) ⊂ M_n): (a) is Φ UCP? (b) is Φ² = J∘Q²∘D (i.e. DJ=id)?
(c) is ‖Φ²−Φ‖_cb = ‖Q²−Q‖_{∞→∞} EXACTLY — prove or refute the claimed cb-norm identity
for maps of the form J∘L∘D with L a classical linear map (strategist C's argument: a
scalar matrix acting between direct sums attains its max-abs-row-sum at scalar multiples
of the identity with maximizing signs — is this a correct and complete proof of BOTH
directions ≥ and ≤ at every ampliation level?).

**Q5 (commutativity forcing and compression, steps F2–F3).** Re-derive independently:
(a) ‖ΦΔ−Δ‖_cb ≤ 2Kη from (i)+(ii); (b) the commutator chain giving ‖[x,y]‖ ≤ cKη in B
(check the constants 8/10 and whether the argument needs ‖Δ‖_cb ≤ 1, which UCP gives);
(c) the claim that a noncommutative finite-dim C*-algebra contains two CONTRACTIONS with
commutator of norm exactly 2 (exhibit them or correct the constant); (d) the near-isometry
lower bound ‖Ax‖ ≥ (1−3Kη)‖x‖ for A = D∘Δ — the strategist derives ‖Δx‖ ≥ (1−Kη)‖x‖ from
(ii) and then ‖Δx‖ ≤ ‖Ax‖ + 2Kη‖x‖ from ΦΔ ≈ Δ and ran(Φ) diagonal — check BOTH
inequalities carefully (the second uses ‖ΦΔx − JAx‖ = 0? verify the identity ΦΔ = J∘(DΔ)
— is Φ(Y) = J(D(Q... careful: Φ = JQD, so Φ(Δx) = J(Q(D(Δx))) = J(Q(Ax)); the strategist
needs ‖J(Q(Ax))‖ ≤ ‖Ax‖ and the step ‖Δx‖ ≤ ‖ΦΔx‖ + 2Kη‖x‖ — re-derive the whole chain
and pin exact constants); (e) ‖MA−I_k‖ ≤ 3Kη/(1−3Kη) via ‖A(MA−I)x‖ ≤ 3Kη‖x‖ — check
whether M = Υ∘J satisfies ‖AM−Q‖ ≤ Kη as claimed from (i) by diagonal compression
(D(ΔΥ)J vs A·M — verify D∘Δ∘Υ∘J = (DΔ)(ΥJ) composes as claimed).

## Output contract

Write your full report to
`docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md` with:
- One verdict line per question: `Qn: VALID | VALID-WITH-CORRECTIONS (list) | INVALID (reason) | UNDECIDABLE-FROM-SOURCE (what is missing)`.
- For every correction: the exact tex line / report line, the flaw, the corrected statement.
- A closing section "Residual risk register": everything that still stands between Route F
  and a rigorous proof of op-classical if all your verdicts are optimistic (e.g. the
  th_main_ext proof chain you did NOT fully re-derive, constant extraction, the PRH lemma).
- Verdicts must be YOURS from the sources; the sibling FINDINGS entries are leads only.
Length: as needed; precision over brevity. Do not edit any other file.
