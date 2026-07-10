# Transcription-fidelity verdict

Ground truth is the `contract:` line in each `argument/<id>.md` file.  Semantic
macros are expanded according to `main.tex`, with notation interpreted under
`CONVENTIONS.md`.

## 01 — `lem-classical-equiv`

**Verdict: FAITHFUL-WITH-NOTE.**  Both directions, their scopes, and the exact
constants `C`, `2`, `6`, and `4` agree.  In particular, the second conclusion is
exactly `6 delta + 4 delta^2`, not a linearized substitute.

The transcription note is justified and conservative.  Convention (b) defines
the map norm on maps of `ell-infinity_n`, explicitly uses it for `Q^2-Q`, and
requires that norm to be stated; hence expanding each bare map norm in this
contract to `\|.\|_{infinity->infinity}` is the registered reading, not a change
of the inequality.  The unexpanded operator `theta` is retained exactly as the
contract gives it.  Making the universal bound constant explicit as `C>0` is
mathematically equivalent (any universal upper-bound constant may be enlarged
to a positive one).  The manifest tag and note are accurate.

## 02 — `obs-height-collapse`

**Verdict: FAITHFUL.**  After expansion, `\negmass(P)=delta(P)`,
`\vis(P)=W(P)`, `\distone=dist_1`, and `\conv\vis=conv W`.  The range
`0 < delta(P) <= 1/4`, nonemptiness, hidden-top/maximal-height hypothesis,
both named masses, and the conclusion
`H(1-sigma_v) <= nu_v(2+4 delta)` all agree exactly.  Calling the environment
an observation matches the registry kind.  The `notation-translated` manifest
tag and its note are accurate.

## 03 — `lem-mass-split`

**Verdict: FAITHFUL.**  `\posp{a_j}` and `\negp{a_j}` expand to `a_j^+`
and `a_j^-`; their defining maxima, `a_j=P_{vj}`, the definition of `nu_v`,
and `sum_j a_j^+ = 1+nu_v` are unchanged.  No quantifier or hypothesis is
lost.  The `verbatim-equivalent` manifest tag and its note are accurate.

## 04 — `lem-residual-lower`

**Verdict: FAITHFUL.**  Writing the finite hull as
`C=conv{y_1,...,y_N} subset R^n` merely names its generators and does not alter
`C`.  The decomposition of `p`, nonnegativity of every `c_j`, the definition
and strict bound `s=sum_j c_j<1`, membership of `p_j,q` in `R^n`, the
pointwise-for-every-`j` distance hypothesis, and the conclusion all match.
The generator rename recorded by the manifest is consistent, and the
`notation-translated` tag and note are accurate.

## 05 — `lem-residual-upper`

**Verdict: FAITHFUL.**  The two nonnegative coefficient families, the exact
positive residual mass `m=sum_j b_j-sum_k c_k>0`, the quotient defining `q`,
and every `D_k` hypothesis retain their original quantifiers.  Expanding
`\lone{x-r_k}` gives the contract's vector `ell_1` norm, while `\distone`
gives its `dist_1`; the final weighted bound is term-for-term identical.  The
`notation-translated` manifest tag and note are accurate.

## 06 — `lem-halo-collapse`

**Verdict: FAITHFUL.**  The signed-idempotent range, nonempty visible set,
hidden top vertex, and all three masses are retained.  The prose definition of
`sigma_g` preserves positive-coefficient mass, the strict distance cutoff
`> tau/4`, the `ell_1` metric, and `tau=sqrt(delta)`.  The conclusion expands
exactly to
`H(1-sigma_g) <= (sigma-sigma_g) tau/4 + nu_v(2+4 delta)`.
The `notation-translated` manifest tag and note are accurate.

## 07 — `lem-factorization`

**Verdict: FAITHFUL.**  The matrix, exact idempotence, row-sum, rank,
actual-row-basis, and half-maximal Gram-volume hypotheses all remain explicit.
The definitions of `a_t`, `beta_s`, `lambda_s`, `mu_s`, `sigma_s`, `E_s`,
`Phi_s`, and `S^*_s` preserve every index exclusion, positive/negative-part
maximum, factor, and summation.  The universal pivot scope and the exact bound
`S^*_s(U) <= 2 Phi_s(U)+6 delta(P)` agree.  The `notation-translated` manifest
tag and its detailed note are accurate.

## 08 — `lem-zerosum-triangle`

**Verdict: FAITHFUL.**  Only `v`—not `w`—is required to have coordinate sum
zero in both versions.  The definition of `n` and the ordered expression
`n(w-v) <= n(w)+n(v)` are exact.  The `verbatim-equivalent` manifest tag and
note are accurate.

## 09 — `lem-weighted-min`

**Verdict: FAITHFUL.**  Strict positivity of every weight, normalization
`sum_i p_i=1`, unrestricted real values of every `n_i`, the minimization range
`{1,...,m}`, and `min_i n_i <= sum_i p_i n_i` all agree.  The
`verbatim-equivalent` manifest tag and note are accurate.

## 10 — `lem-fan-payment`

**Verdict: FAITHFUL.**  The finite family, ambient dimension, strictly positive
normalized weights, coordinate-sum-zero condition for every `w_i`, and zero
weighted barycenter are all retained.  The same `n` is defined, the minimum is
over the same support indices, and the conclusion has the exact constant `2`
and identical summands.  The `verbatim-equivalent` manifest tag and note are
accurate.

## 11 — `lem-negpart-subadditive`

**Verdict: FAITHFUL.**  Both variables remain universally quantified over
`R^d`; `n(w)=sum_l max(-w(l),0)` and
`n(x+y) <= n(x)+n(y)` are unchanged.  The `verbatim-equivalent` manifest tag
and note are accurate.

## 12 — `lem-fan-payment-restricted`

**Verdict: FAITHFUL.**  The fan hypotheses match row 10's contract where
required, including coordinate-sum zero for every vector and a zero weighted
barycenter.  The minimizer is over exactly `{w_1,...,w_m}`, `A` uses the same
strict positivity test, both sums are restricted to the same `A`, and the
constant is exactly `2+sqrt(2)`.  The `verbatim-equivalent` manifest tag and
note are accurate.

## 14 — `lem-pivot-removing-move`

**Verdict: FAITHFUL.**  The rank-3 exact signed-idempotent condition retains
`P^2=P` and all row sums `1`; under Convention (b), “signed idempotent” already
denotes a real signed-measure matrix/map, while `P^2` entails square shape, so
the shortened parenthetical drops no hypothesis.  The actual-row chart,
relative Gram volume, all old-coordinate scores, half-admissible argmin and
minimality scope, maximal pivot, off-chart replacement index, nonzero `c`,
admissibility inequality, and exact volume factor all agree.  Every new-coordinate
formula and excluded index in `E_r^j`, `Psi_j`, and `Gamma_j` is unchanged, as
is `Phi_s(U) <= max(Psi_j,Gamma_j)`.  The rendered `theta`-`1/2` phrase matches
the registered “theta-half” name in Convention (d).  The
`notation-translated` manifest tag and note are accurate.
