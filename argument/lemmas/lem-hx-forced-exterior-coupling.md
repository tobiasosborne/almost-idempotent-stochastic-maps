---
id: lem-hx-forced-exterior-coupling
kind: lemma
contract: For every finite exact signed idempotent P, every pair of row indices (r,s), and every point c of the row polytope K(P), the full row-point fibers Q with ||p_Q - c||_1 > 1/2 jointly carry positive coefficient mass P_r^+ + P_s^+ at least ||p_r - p_s||_1/(2*(2 + 4*delta(P))) - 2*delta(P).
defs: def-signed-idempotent; def-negative-mass
deps: lem-hx-financing-floor
status: proved
af: none
provenance: W60 wave (docs/waves/2026-07-10-W60-artifacts/): codex prover (gpt-5.6-sol, high) PROOFS-W60-ENGINE.md §E5; fresh hostile codex verifier (gpt-5.6-sol, xhigh), batched verdict VERDICT-W60-ENGINE.md line 'E5: VALID-WITH-CORRECTIONS' (scope: exact triviality threshold l <= 8*delta + 16*delta^2 recorded; correction applied in-file and here). Reviewer != author.
owner: B
---

**Role (W60 engine bank, 5/5 — the strategic byproduct).** The first banked
forced-coupling LOWER bound: exact idempotence forces long-range positive
financing proportional to row separation — the missing demand-side direction
behind `conj-cotop-web-coupling` (L6.5) and the W37/W38 coupling walls. Pure
instantiation of [[lem-hx-financing-floor]] (recentred sign functional, ball
radius 1/2, \(\Lambda=(2+4\delta)/\ell\)).

**Statement.** For rows \(r,s\) at distance \(\ell=\lVert p_r-p_s\rVert_1\) and any
\(c\in K(P)\):
\[ P_r^+ + P_s^+\ \text{on}\ \{Q:\lVert p_Q-c\rVert_1>1/2\}\ \ \ge\ \
   \frac{\ell}{2(2+4\delta)}-2\delta. \]

**Fixture (verifier-checked).** δ=0 two-block stochastic idempotent family: the
bound is valid with exactly a factor-two slack at the endpoint example (the
family-specific \(\ell/2\) is attained); endpoint ownership under the strict
\(>1/2\) is correct.

**Scope (verifier-prescribed exact threshold).** The lower bound is nonpositive —
trivially true, uninformative — iff \(\ell\le4\delta(2+4\delta)=8\delta+16\delta^2\);
in particular vacuous throughout \(\ell\le8\delta\). It does not say which row
pays, identify a fiber, or furnish any selected-corner datum. Clone-invariant.
Signed picture.

**Rigour tier.** L5 (fresh hostile codex, batched W60 verdict; scope correction
applied as prescribed). NOT af-validated. af-elevation candidate. Intended
consumers: the L6.5 coupling front (`conj-cotop-web-coupling`), route-fork hard
nodes (aism-ur9).
