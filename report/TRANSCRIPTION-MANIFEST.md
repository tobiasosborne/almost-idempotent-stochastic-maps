<!--
ROLE: fidelity ledger for the typeset amsthm statements added to the OLDER report shards
  (sections 01-12, 14) in the Round-2 typesetting pass (bead aism-6q2). One row per typeset
  mathematical statement added or materially edited, so a fresh hostile verifier can check each
  transcription against the registry `contract` mechanically.
AUDIT KEY: for each row, open the section file, read the amsthm body at the given \label, and
  compare it to the `\contractquote{...}` block immediately below it (the byte-verbatim registry
  contract) and to argument/lemmas/<id>.md. The typeset statement must NOT weaken, strengthen,
  reorder quantifiers, or drop a hypothesis relative to the contract.
FIDELITY TAGS:
  verbatim-equivalent    = symbol-for-symbol the same relation/hypotheses as the contract, only
                           ASCII->LaTeX rendering (sum_i -> \sum_i, <= -> \le, sqrt -> \sqrt, etc.).
  notation-translated    = as above, plus the repo's semantic macros and/or a bound-variable rename
                           to avoid a symbol clash; no change to mathematical content.
  transcription-note-added = the contract prose was ambiguous/under-specified; the shard carries an
                           \emph{Transcription note} naming the ambiguity and the conservative reading.
-->

# Transcription fidelity manifest — report sections 01-12, 14

Pass: Round-2 report typesetting (bead `aism-6q2`). The `\contractquote{...}` block beneath each
statement is the byte-verbatim registry contract and was **not** altered by even one byte in this pass
(verified: every `\contractquote` argument is identical to `HEAD`). Section 13 is the status ledger (a
table; no theorems added) and is out of scope. Sections 15-20 already carried typeset statements before
this pass and are not re-listed here.

| # | Registry id | Section file | Typeset env `\label` | Fidelity | Verifier note |
|---|-------------|--------------|----------------------|----------|---------------|
| 01 | `lem-classical-equiv` | `report/sections/01_classical_equiv.tex` | `lem:classical-equiv` | transcription-note-added | Bidirectional equivalence split into two enumerated directions; both constants `C`, `2`, `6`, `4` and both defect bounds exact. **Ambiguity flagged in-shard:** (i) the contract's bare `\|\cdot\|` is read as the `\infty\to\infty` map norm `\opnorm{\cdot}` per CONVENTIONS (b); (ii) the operator `\theta` in `P=\theta(2Q-1)` is carried verbatim (the contract does not expand it). No hypothesis added or dropped. |
| 02 | `obs-height-collapse` | `report/sections/02_height_collapse.tex` | `obs:height-collapse` | notation-translated | `H*(1-sigma_v) <= nu_v*(2+4*delta)` transcribed exactly; `dist_1 -> \distone`, `conv W -> \conv\vis`, `W(P) -> \vis(P)`. Env changed proposition->observation to match registry kind `obs`; `\label` unchanged. Constant `1/4` and `(2+4delta)` exact. |
| 03 | `lem-mass-split` | `report/sections/03_mass_split.tex` | `lem:mass-split` | verbatim-equivalent | `sum_j a_j^+ = 1 + nu_v` with `a_j=P_vj`, `a_j^± = max(±..,0)`, `nu_v = sum a_j^-` transcribed symbol-for-symbol via `\posp/\negp`. |
| 04 | `lem-residual-lower` | `report/sections/04_residual_lower.tex` | `lem:residual-lower` | notation-translated | Hypotheses `c_j>=0`, `s=sum c_j<1`, `dist_1(p_j,C)<=dist_1(p,C)` and conclusion `dist_1(p,C)<=dist_1(q,C)` exact. **Bound-variable rename:** the hull's generating points are named `y_1..y_N` to avoid clashing with the moving point `q` (the contract writes only "convex hull of finitely many points"). |
| 05 | `lem-residual-upper` | `report/sections/05_residual_upper.tex` | `lem:residual-upper` | notation-translated | `m = sum b_j - sum c_k > 0`, `q = (sum b_j p_j - sum c_k r_k)/m`, `\|x-r_k\|_1 <= D_k` on `C`, conclusion `m*dist_1(q,C) <= sum b_j dist_1(p_j,C) + sum c_k D_k` exact. `dist_1 -> \distone`, `\|\cdot\|_1 -> \lone`. |
| 06 | `lem-halo-collapse` | `report/sections/06_halo_collapse.tex` | `lem:halo-collapse` | notation-translated | `H*(1-sigma_g) <= (sigma-sigma_g)*tau/4 + nu_v*(2+4*delta)` exact; the `sigma_g` definition (positive-coefficient mass on rows at ell-1 distance `> tau/4` from `conv W`, `tau=sqrt(delta)`) transcribed in prose. Constants `1/4`, `tau/4`, `(2+4delta)` exact. |
| 07 | `lem-factorization` | `report/sections/07_factorization.tex` | `lem:factorization` | notation-translated | Full auxiliary battery transcribed: `beta_s, lambda_s, mu_s, sigma_s, E_s, Phi_s, S*_s` with the exact `max(.,0)` forms, the actual-row-basis and `Vol(U) >= (1/2) Vol_max(P)` hypotheses, and conclusion `S*_s(U) <= 2 Phi_s(U) + 6 delta(P)` for every pivot `s`. Constants `1/2, 2, 6` exact. |
| 08 | `lem-zerosum-triangle` | `report/sections/08_zerosum_triangle.tex` | `lem:zerosum-triangle` | verbatim-equivalent | `v` zero coordinate sum hypothesis kept; `n(x)=sum_l max(-x(l),0)`; conclusion `n(w-v) <= n(w)+n(v)` exact. |
| 09 | `lem-weighted-min` | `report/sections/09_weighted_min.tex` | `lem:weighted-min` | verbatim-equivalent | `p_i>0`, `sum p_i=1`, `n_i` real; `min_i n_i <= sum_i p_i n_i` exact. |
| 10 | `lem-fan-payment` | `report/sections/10_fan_payment.tex` | `lem:fan-payment` | verbatim-equivalent | Zero-coordinate-sum and zero-barycenter (`sum p_i w_i=0`) hypotheses kept; conclusion `min_{i*} sum_i p_i n(w_i - w_{i*}) <= 2 sum_i p_i n(w_i)` exact (constant `2`). |
| 11 | `lem-negpart-subadditive` | `report/sections/11_negpart_subadditive.tex` | `lem:negpart-subadditive` | verbatim-equivalent | `n(x+y) <= n(x)+n(y)` for all `x,y in R^d`, `n(w)=sum_l max(-w(l),0)`, exact. |
| 12 | `lem-fan-payment-restricted` | `report/sections/12_fan_payment_restricted.tex` | `lem:fan-payment-restricted` | verbatim-equivalent | Same fan hypotheses as row 10; `w_*` = minimizer of `v -> sum_i p_i n(w_i-v)` over `{w_1..w_m}`; `A={i:n(w_i-w_*)>0}`; conclusion `sum_{A} p_i n(w_i-w_*) <= (2+sqrt2) sum_{A} p_i n(w_i)` exact (constant `2+sqrt2`). |
| 14 | `lem-pivot-removing-move` | `report/sections/14_pivot_removing_move.tex` | `lem:pivot-removing-move` | notation-translated | Full rank-3 chart battery transcribed: old coords `a_t`, `beta_r, lambda_r, mu_r, E_r, Phi_r, Phi`; the `theta-1/2 Phi-argmin` hypothesis (`m_U>=1/2`, minimality over charts with `Vol/Vol_max>=1/2`); the pivot-removing chart `V_j=U-u_s+j` with `c=a_s(j)!=0`, admissibility `|a_s(j)| m_U >= 1/2`, volume factor `|a_s(j)|`; new coords `a_s^j, a_t^j`, `E_r^j`, `Psi_j=Phi_s(V_j)`, `Gamma_j=max_{r!=s}Phi_r(V_j)`; conclusion `Phi_s(U) <= max(Psi_j, Gamma_j)` exact. Constants `1/2` exact. |

**Count:** 13 typeset statements added (one per row; sections 01-12 and 14).
