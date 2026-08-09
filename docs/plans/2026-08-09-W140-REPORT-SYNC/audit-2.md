VERDICT /home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/report/sections/57_maincb_call_envelopes.tex: FIX

1. Shard file: `/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/report/sections/57_maincb_call_envelopes.tex`; result id: `lem-maincb-stage2-call-envelope`; clause: (c). Exact offending text: “Choose $c_{0}\ge0$ and set $K_{2}^{0}=\max\{1,e_{s2}^{0}/e_{\mathrm{env}}^{0}\}$.” This silently assumes the load-bearing nonnegativity of the error-improvement coefficient, whereas export node 1.1 obtains it by enlarging the original coefficient and invokes `lem-maincb-extended-inclusion-monotone` to preserve the inclusion conclusion. Exact minimal correction: replace that sentence with “Starting with the coefficient supplied by Lemma~\ref{lem:maincb-error-improvement}, enlarge it if necessary to a nonnegative $c_0$; Lemma~\ref{lem:maincb-extended-inclusion-monotone} preserves the resulting inclusion conclusion. Then set $K_{2}^{0}=\max\{1,e_{s2}^{0}/e_{\mathrm{env}}^{0}\}$.”

2. Shard file: `/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/report/sections/57_maincb_call_envelopes.tex`; result id: `lem-maincb-stage2-call-envelope`; clause: (c). Exact offending text: “The current tree has $12/12$ clean nodes and three rounds.” The exported tree has 10 nodes (root plus nine descendants), all validated and clean. Exact minimal correction: replace `$12/12$` with `$10/10$`.

VERDICT /home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/report/sections/58_maincb_selection.tex: LAND

VERDICT /home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/report/sections/59_maincb_assembly.tex: LAND

VERDICT /home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/report/sections/60_stage1_endgame_cohomology.tex: LAND

VERDICT /home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/report/sections/61_stage1_endgame_bounds.tex: FIX

3. Shard file: `/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/report/sections/61_stage1_endgame_bounds.tex`; result id: `lem-stage1-bound-quotient-local-index`; clause: (b). Exact offending text: “has charts $\chi_s:B^{\aHerm}_{r_{\mathrm{iso}}}(0)\to\Unit$ with inverses $\psi_s$, $s\in\{\pm1\}$, retained by $\sigma$”. The typeset statement omits the contract’s conclusions $\chi_s(0)=sJ$ and $\psi_s=\phi_{sJ}^{\mathrm{par}}$ on the chart image. Exact minimal correction: replace that text with “has charts $\chi_s:B^{\aHerm}_{r_{\mathrm{iso}}}(0)\to\Unit$, $s\in\{\pm1\}$, with $\chi_s(0)=sJ$ and inverse $\psi_s=\phi_{sJ}^{\mathrm{par}}$ on the image, and each chart image is retained by $\sigma$”.

4. Shard file: `/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/report/sections/61_stage1_endgame_bounds.tex`; result id: `lem-stage1-bound-quotient-index-data`; clause: (c). Exact offending text: “because $\overline a,a=1$.” Export node 1.3.3 instead uses $\overline a\,a=1$ and $c=a^2$ to obtain $\overline a\,c=a$; the shard’s comma produces neither recorded identity. Exact minimal correction: replace it with “because $\overline a\,c=\overline a\,a^2=a$.”
