VERDICT: CORRECTIONS-REQUIRED

1. **HIGH — the formalisation-status footnote overstates the validated coverage.**
   - **Locus:** `paper/main.tex:70--73`.
   - **Old text:** “The argument has been machine-adversarially formalized at the lemma level in this project's registry; the final strengthened ledger and top-level assembly are in progress, so this draft does not claim completed formal verification.”
   - **Required text:** “Most component lemmas have been machine-adversarially validated in this project's registry.  The scalar-header positivity lemma, factor-map packet, factor-estimate packet, strengthened ledger, and top-level assembly remain in progress, so this draft does not claim completed formal verification.”
   - **Reason:** the current registry and `HANDOFF.md` mark all five named rows `stated` / `af: none`, not merely the strengthened ledger and final assembly.  The disclaimer's last clause is honest, but its first clause currently implies more complete lemma-level coverage than exists.

2. **HIGH — the approximate-algebra paragraph drops the smallness hypothesis and misprints the defining maximum.**
   - **Locus:** `paper/main.tex:127--140`.
   - **Old text:** “After the local type and index corrections in the almost-idempotent argument, $\mathcal A$ is an extended $\varepsilon_{\rm AI}(\eta)$-$C^*$-algebra.  If
     $$r=\frac32((1-4\eta)^{-1/2}-1),\qquad
     \varepsilon_{\rm AI}(\eta)=\max\{r,,20\eta+2((1+r)^5-1),,3r-r^2\},$$
     then, for a universal $\eta_A>0$,
     $$\varepsilon_{\rm AI}(\eta)\le C_A\eta,\qquad
     C_\theta=12(\sqrt2-1),\qquad C_A=20+\frac{211}{8}C_\theta.$$”
   - **Required text:** “Set
     $$r=\frac32\bigl((1-4\eta)^{-1/2}-1\bigr),\qquad
     \varepsilon_{\rm AI}(\eta)=\max\{r,20\eta+2((1+r)^5-1),3r-r^2\}.$$
     There are universal $\eta_A>0$ and
     $C_A=20+\frac{211}{8}C_\theta$, where
     $C_\theta=12(\sqrt2-1)$, such that whenever $0\le\eta\le\eta_A$ the inherited operator-space norms, involution, and unit make $\mathcal A$ an extended $\varepsilon_{\rm AI}(\eta)$-$C^*$-algebra and
     $$\varepsilon_{\rm AI}(\eta)\le C_A\eta.$$”
   - **Reason:** this is the exact quantifier domain and formula exported by `lem-routef-ai-defect-linearization`.  As printed, the doubled commas are visibly wrong and $\eta_A$ does not constrain anything.

3. **HIGH — the sharpness statement is false for the stated parameter range and ambiguous about distance.**
   - **Locus:** `paper/main.tex:288--304`.
   - **Old text:** “For $s>0$, Hume's explicit $3\times3$ family is ... It is a signed affine retraction, its maximal row negative mass is $\delta_s=s^2$, and its distance to every stochastic idempotent equals ... Thus $Q_s$ has defect $O(s^2)$ but remains at distance $\Omega(s)$ from every stochastic idempotent.”
   - **Required text:** “For $0<s<1$, consider
     $$P_s=I-u_sv_s^{\mathsf T},\qquad
     v_s=(1,-1+s,-s),\qquad
     u_s=(1-s+s^2,-s,0)^{\mathsf T}.$$
     It is a signed affine retraction with maximal row negative mass $\delta_s=s^2$.  If $\mathcal I_{\rm stoch}$ denotes the set of stochastic idempotents, then
     $$\operatorname{dist}_{\infty\to\infty}(P_s,\mathcal I_{\rm stoch})
       :=\inf_{F\in\mathcal I_{\rm stoch}}\norm{P_s-F}_{\infty\to\infty}
       =2s-2s^2+2s^3
       =2\sqrt{\delta_s}+O(\delta_s).$$
     Normalize the positive part of each row to obtain a row-stochastic $Q_s$.  The signed--stochastic bridge gives
     $$\norm{P_s-Q_s}_{\infty\to\infty}\le2s^2,\qquad
       \norm{Q_s^2-Q_s}_{\infty\to\infty}\le6s^2+4s^4.$$
     Hence every $F\in\mathcal I_{\rm stoch}$ satisfies
     $$\norm{Q_s-F}_{\infty\to\infty}
       \ge2s-4s^2+2s^3=2s(1-s)^2,$$
     which is $\Omega(s)$ as $s\downarrow0$ and excludes every exponent $\beta>\tfrac12$.”
   - **Reason:** $\delta_s=s^2$ is only the advertised negative mass in the small-$s$ regime (the inherited source itself says “for small $s>0$”); “distance to every” cannot literally equal one common value (for example, $I$ is itself a stochastic idempotent), whereas distance to the set is the intended statement.  The replacement also makes the signed-to-stochastic triangle-inequality transfer explicit.  The unsupported public-facing eponym “Hume” should not be restored unless an identifiable citation or acknowledgment is added; no such source appears in `refs/manifest/SOURCES.md`.

4. **MEDIUM — one amplified estimate omits its norm.**
   - **Locus:** `paper/main.tex:201--203`.
   - **Old text:**
     $$\norm{\Upsilon_r(\Delta_rX\,\Delta_rY)-XY}
       \le K\eta\norm X\norm Y.$$
   - **Required text:**
     $$\norm{\Upsilon_r(\Delta_rX\,\Delta_rY)-XY}_{M_r(\mathcal B)}
       \le K\eta\norm X_{M_r(\mathcal B)}\norm Y_{M_r(\mathcal B)}.$$
   - **Reason:** the estimate is in the $C^*$-operator norm on $M_r(\mathcal B)$, not the cb norm and not an $\ell_\infty$ operator norm.  The other picture crossings are marked correctly.

5. **CLEARED — theorem and constant fidelity apart from correction 2.**  The main theorem matches `lem-routef-k-ledger` plus `lem-routef-f0-assembly`: $\eta_0=\eta_K$, $C=K+4\sqrt{2K}$, dimension independence, the $\infty\!\to\!\infty$ norms, and exponent $1/2$ are all correct.  The displayed formulas for $C_\theta$, $C_A$, $K$, $\rho_{\rm fac}$, and $\eta_K$, and the F2/F3/PRH constants $2,3,24,4,\sqrt2$, match the definition and contracts.

6. **CLEARED — seam, repair, descent, and attribution boundary.**  The diagonal seam identity is exact in both directions; the phase-balanced diagonal and CP-ization statements match their registry contracts; and the F2 $\to$ F3 $\to$ PRH chain has the correct hypotheses, norms, and numerology.  Kitaev's structural construction is credited to Kitaev, while the diagonal repair and stochastic descent are identified as contributions of this work.  All four actual bibliography entries are real and agree with `refs/manifest/SOURCES.md`; correction 3 addresses the one unsupported name appearing outside that bibliography.

7. **CLEARED — audience fit and length.**  The existing PDF is four pages.  The draft does not re-prove Kitaev's theorem, and the exact seam, repair, scalar ledger, and stochastic descent carry the exposition.  Subject to corrections 1--4, the structure and compression fit the requested audience.
