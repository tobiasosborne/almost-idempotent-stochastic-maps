# BRIEF — W74F-F hostile verification: attack the EXT-CB proof (aism-9lb7)

You are a FRESH HOSTILE VERIFIER. You wrote none of what you are about to read; your job
is to BREAK it. Finding a gap, an `r`- or `n`-dependent constant, a per-level object
smuggled in, or an error is a BIG SUCCESS. Reach your own verdict from the primary
source; treat NO repository document as an oracle.

## Target

`docs/plans/2026-07-24-W74F-wave2-artifacts/PROOF-W74F-F-EXTCB.md` — UNVERIFIED prover
output claiming EXT-CB (the amplified `lem_extension`, the last `th_main_ext` gap)
conditional on H-CB + APPROX-CB + MERGE-CB, with
`C_ext = C_merge[1 + 5C_H + 20C_app(C_H+1)]` and one level-one unitary carrying all
amplifications.

## Primary source (verify FIRST)

`refs/kitaev-2405.02434/approximate_algebras.tex` — `sha256sum` must equal
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`. Read `lem_extension`
(`tex:1363-1412`), `lem_merging`/`cor_merge_sum` (`tex:1330-1359`), `lem_approx_ext`
(`tex:1508-1535`), the level-one selection lemmas (`tex:1162-1180`, `tex:1363-1369`),
and the merging hypotheses `merging0h`–`merging3h` YOURSELF.

Context, read after the source, not oracles: the registered contract
`argument/lemmas/conj-extcb.md`; the premise H-CB as amended in
`argument/lemmas/conj-hcb.md` (hostile-verified separately,
`VERDICT-W74F-E-HCB.md`); the decomposition spec
`docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md` §3 EXT-CB.

## Attack surface (hit at least these)

1. **The premise ledger (§1).** Does the proof consume ONLY the amended conditional
   H-CB clauses (in particular the conditional inverse (H5)–(H6)), APPROX-CB, MERGE-CB,
   and the level-one lemmas — or does it silently assume more (an unconditional
   inverse, an unregistered uniform estimate)? Are the normalizations in §1 legitimate?
2. **EXTCB-1 (§2).** The level-one dimension calculation `dim 𝒮_{P,Q} = r`: does it
   follow from `lem_add_dim`/`lem_1d_proj` as printed, at level one only?
3. **EXTCB-2 (§3).** The exact-target APPROX-CB application: is the target genuinely
   the exact C*-algebra `ℬ(H₁)` so that `μ₁₁` is exactly multiplicative? Does the
   step forcing `μ₁₁` to be conjugation by ONE unitary hold (finite dimension,
   surjectivity, kernel triviality)? Any `r`-dependence entering here?
4. **EXTCB-3 (§4).** The conditional inverse triggers: is the level-one `1−O(e)` lower
   bound/bijectivity for the relevant `h`-maps actually established BEFORE the
   conditional H-CB inverse clauses are invoked (the exact trigger order matters — the
   `ℂ⊕ℂ` counterexample shows the unconditional form is false)?
5. **EXTCB-4 (§5) — THE PROVER'S DELIBERATE PROOF CHANGE.** The three off-`11` corners
   are DEFINED by transporting an exact spatial matrix-corner system through level-one
   Ha inverses, instead of proving the source's `tex:1407-1409` formulas completely
   close. Scrutinize hardest here: (a) is the transported system genuinely exact at
   every amplification with NO per-level choice; (b) do the four corner maps then
   satisfy every `merging0h`–`merging3h` hypothesis at every level with the claimed
   constants; (c) is `γ₁₁ = v` kept exactly, and is the only APPROX-CB error where the
   proof says it is?
6. **EXTCB-5 (§6).** MERGE-CB application and EXACT bijectivity of `v₊`: does
   bijectivity hold at every level (Neumann condition or dimension count — which, and
   is it valid)?
7. **The constant ledger (§7).** Recompute (0.1) and the threshold (1.8). Check every
   entry's independence of `r`, `n`, `dim 𝒜`, block data.
8. **Hypothesis usage (§8).** `‖P+Q−I‖ ≤ δ`, `dim 𝒮_Q = 1`, `𝒮_{P,Q} ≠ 0`: each used
   where claimed, nowhere else needed?

## Deliverable

Write exactly ONE file:
`docs/plans/2026-07-24-W74F-wave2-artifacts/VERDICT-W74F-F-EXTCB.md`

1. `SHA CHECK:` line.
2. Per-section verdicts (premise ledger, EXTCB-1…EXTCB-5, constant ledger):
   `VALID` / `VALID-WITH-CORRECTIONS` (state exactly) / `INVALID` (exhibit the failure).
3. **Overall verdict** + one-paragraph bottom line: does EXT-CB hold conditional on the
   amended H-CB with a universal constant, yes or no; what remains open.
4. **Contract-impact note**: does the registered `conj-extcb` contract need amending
   (e.g. to reflect the corner-transport construction or premise set)? Quote any exact
   replacement text.
5. Every check performed that PASSED.

## Rules

Fresh eyes; exhibit failures explicitly; do not co-author repairs beyond stating what a
correction must say; write ONLY the verdict file; no `git` commands.
