STATUS: UNVERIFIED PROVER OUTPUT

# Positive-Retract Hardening

## 1. Statement proved

Let \(k,n\geq 1\).  Let \(A:\ell_\infty(k)\to\ell_\infty(n)\)
and \(M:\ell_\infty(n)\to\ell_\infty(k)\) have matrices
\[
 A=(a_{is})_{i\in[n],s\in[k]},
 \qquad
 M=(\mu_s(i))_{s\in[k],i\in[n]},
\]
whose rows are probability vectors.  Equivalently, both maps are positive
and unital.  Suppose
\[
 \|MA-I_k\|_{\infty\to\infty}\leq\varepsilon,
 \qquad 0\leq\varepsilon<\frac12.
\]
Then there is a positive unital idempotent
\(E:\ell_\infty(n)\to\ell_\infty(n)\) such that
\[
 \boxed{\ \|AM-E\|_{\infty\to\infty}
       \leq 2\sqrt{2\varepsilon}\ }.
\]
Thus the candidate constant is
\[
 C=2\sqrt2.
\]

The same proof also works at \(\varepsilon=1/2\), although that endpoint
is not part of the requested statement.  The constant \(2\sqrt2\) is the
minimum produced by the threshold construction below.  I do not claim
that it is the globally optimal universal constant.

Section 7 gives a family for which every stochastic idempotent is at
distance at least \(\sqrt{\varepsilon/2}\) from \(AM\).  Consequently the
order \(\sqrt\varepsilon\), not merely the construction used to obtain it,
is necessary for this lemma.

## 2. Norm facts

For any real \(p\times q\) matrix \(T=(t_{ij})\),
\[
 \|T\|_{\infty\to\infty}
 =\max_{i\in[p]}\sum_{j=1}^q |t_{ij}|.
 \tag{2.1}
\]
Indeed, if \(\|x\|_\infty\leq1\), then
\[
 |(Tx)_i|
 \leq\sum_j |t_{ij}||x_j|
 \leq\sum_j|t_{ij}|,
\]
which proves the upper bound in (2.1).  For a row \(i_0\) attaining the
maximum, choose \(x_j=1\) when \(t_{i_0j}\geq0\) and \(x_j=-1\) when
\(t_{i_0j}<0\).  Then
\((Tx)_{i_0}=\sum_j|t_{i_0j}|\), proving the reverse bound.

In particular, if \(P,Q\) have equally many rows, then
\[
 \|P-Q\|_{\infty\to\infty}
 =\max_i\|P_{i\bullet}-Q_{i\bullet}\|_1.
 \tag{2.2}
\]
No stochasticity is required for (2.1) or (2.2).  Stochasticity will be
essential for the factor \(2\) in the next section.

Under the present hypotheses, both \(MA\) and \(I_k\) are stochastic
matrices: a product of two nonnegative row-stochastic matrices is again
nonnegative and row-stochastic.  Thus \(MA-I_k\), just like \(AM-E\)
later, is in fact a difference of two stochastic matrices.  The important
distinction is not the norm identity, which is general, but the special
form of the row of \(I_k\), which gives the exact factor \(2\).

## 3. The one-sided mass estimate

Put \(R=MA\).  Its entries are
\[
 R_{st}=\sum_{i=1}^n\mu_s(i)a_{it}.
\]
They are nonnegative, and
\[
 \sum_{t=1}^kR_{st}
 =\sum_i\mu_s(i)\sum_ta_{it}
 =\sum_i\mu_s(i)=1.
\]
Hence every row of \(R\) is a probability vector.  For each \(s\),
\[
\begin{aligned}
 \|R_{s\bullet}-e_s\|_1
 &=|R_{ss}-1|+\sum_{t\ne s}|R_{st}|\\
 &=(1-R_{ss})+\sum_{t\ne s}R_{st}\\
 &=2(1-R_{ss}).
\end{aligned}
\tag{3.1}
\]
The second line uses \(0\leq R_{ss}\leq1\) and \(R_{st}\geq0\); the last
line uses \(\sum_{t\ne s}R_{st}=1-R_{ss}\).  Combining (2.2), (3.1), and
the hypothesis gives
\[
 2(1-R_{ss})\leq\varepsilon.
 \tag{3.2}
\]
Since \(\mu_s\) is a probability vector,
\[
\begin{aligned}
 1-R_{ss}
 &=1-\sum_i\mu_s(i)a_{is}\\
 &=\sum_i\mu_s(i)(1-a_{is}).
\end{aligned}
\]
Therefore
\[
 \boxed{\ \sum_i\mu_s(i)(1-a_{is})\leq\frac{\varepsilon}{2}\ }
 \qquad(s\in[k]).
 \tag{3.3}
\]
This proves, in particular, the claimed factor \(2\) rather than assuming
it.

## 4. Hardening the decoder and encoder

The case \(\varepsilon=0\) is treated separately in Section 6.  For now
assume \(0<\varepsilon<1/2\), and set
\[
 \lambda=\sqrt{\frac{\varepsilon}{2}}.
 \tag{4.1}
\]
Then \(0<\lambda<1/2\).  For \(s\in[k]\), define
\[
 C_s=\{\,i\in[n]:a_{is}>1-\lambda\,\}.
 \tag{4.2}
\]

### 4.1. The cores are disjoint and nonempty

If \(s\ne t\) and \(i\in C_s\cap C_t\), then
\[
 a_{is}+a_{it}>2(1-\lambda)>1,
\]
contradicting \(\sum_u a_{iu}=1\).  Thus the sets \(C_s\) are pairwise
disjoint.

Let
\[
 \beta_s=\mu_s(C_s^c).
\]
For \(i\in C_s^c\), the strict definition (4.2) gives
\(a_{is}\leq1-\lambda\), hence \(1-a_{is}\geq\lambda\).  Consequently
\[
 \lambda\beta_s
 \leq\sum_{i\in C_s^c}\mu_s(i)(1-a_{is})
 \leq\sum_i\mu_s(i)(1-a_{is})
 \leq\frac{\varepsilon}{2}.
\]
This is precisely the applicable direction of Markov's inequality.  It
gives
\[
 \beta_s\leq\frac{\varepsilon}{2\lambda}=\lambda<1.
 \tag{4.3}
\]
In particular, \(\mu_s(C_s)=1-\beta_s>0\), so \(C_s\ne\varnothing\).

Define the probability vector obtained by conditioning \(\mu_s\) on
\(C_s\):
\[
 \nu_s(i)=
 \begin{cases}
 \mu_s(i)/(1-\beta_s),&i\in C_s,\\
 0,&i\notin C_s.
 \end{cases}
 \tag{4.4}
\]
Its distance from \(\mu_s\) is exactly
\[
\begin{aligned}
 \|\mu_s-\nu_s\|_1
 &=\sum_{i\in C_s}
   \mu_s(i)\left|\frac1{1-\beta_s}-1\right|
   +\sum_{i\notin C_s}\mu_s(i)\\
 &=(1-\beta_s)\frac{\beta_s}{1-\beta_s}+\beta_s\\
 &=2\beta_s
 \leq\frac{\varepsilon}{\lambda}.
\end{aligned}
\tag{4.5}
\]
At the chosen value (4.1), the last quantity is \(2\lambda\).

### 4.2. Exact retraction

Let \(N:\ell_\infty(n)\to\ell_\infty(k)\) be the stochastic map whose
\(s\)-th row is \(\nu_s\).  Define
\(\widehat A:\ell_\infty(k)\to\ell_\infty(n)\) row by row by
\[
 \widehat a_i=
 \begin{cases}
 e_s,&i\in C_s,\\
 a_i,&i\notin\bigcup_{t=1}^k C_t.
 \end{cases}
 \tag{4.6}
\]
The definition is unambiguous because the cores are disjoint.  Every row
in (4.6) is a probability vector, so \(\widehat A\) is positive and
unital.

Because \(\nu_s\) is supported on \(C_s\), every row of \(\widehat A\)
sampled by \(\nu_s\) is \(e_s\).  Thus
\[
 (N\widehat A)_{s\bullet}
 =\sum_i\nu_s(i)\widehat a_i
 =e_s,
\]
or
\[
 N\widehat A=I_k.
 \tag{4.7}
\]
Set
\[
 E=\widehat A N.
 \tag{4.8}
\]
It is positive and unital as a composition of positive unital maps, and
(4.7) gives
\[
 E^2=\widehat A(N\widehat A)N
 =\widehat A I_kN=E.
 \tag{4.9}
\]
Thus \(E\) is a stochastic idempotent.

## 5. Error bound and optimization

First compare \(AM\) with \(AN\).  The \(i\)-th row difference is
\[
 (AM-AN)_{i\bullet}
 =\sum_{s=1}^k a_{is}(\mu_s-\nu_s).
\]
Using \(a_{is}\geq0\), \(\sum_s a_{is}=1\), and (4.5),
\[
\begin{aligned}
 \|(AM-AN)_{i\bullet}\|_1
 &\leq\sum_sa_{is}\|\mu_s-\nu_s\|_1\\
 &\leq\frac{\varepsilon}{\lambda}.
\end{aligned}
\]
Therefore
\[
 \|AM-AN\|_{\infty\to\infty}
 \leq\frac{\varepsilon}{\lambda}.
 \tag{5.1}
\]

Next compare \(AN\) with \(E=\widehat AN\).  If
\(i\notin\bigcup_sC_s\), then \(\widehat a_i=a_i\), so the two rows agree.
If \(i\in C_s\), then the relevant rows are
\[
 (AN)_{i\bullet}=\sum_ta_{it}\nu_t,
 \qquad
 E_{i\bullet}=\nu_s.
\]
Hence
\[
\begin{aligned}
 \|(AN-E)_{i\bullet}\|_1
 &=\left\|(a_{is}-1)\nu_s+\sum_{t\ne s}a_{it}\nu_t\right\|_1\\
 &\leq(1-a_{is})\|\nu_s\|_1
      +\sum_{t\ne s}a_{it}\|\nu_t\|_1\\
 &=2(1-a_{is})\\
 &<2\lambda.
\end{aligned}
\tag{5.2}
\]
Here each \(\|\nu_t\|_1=1\), and
\(\sum_{t\ne s}a_{it}=1-a_{is}\).  Thus, replacing the strict bound by
a weak one after taking the maximum,
\[
 \|AN-E\|_{\infty\to\infty}\leq2\lambda.
 \tag{5.3}
\]
The triangle inequality, (5.1), and (5.3) give the general threshold
balance
\[
 \|AM-E\|_{\infty\to\infty}
 \leq\frac{\varepsilon}{\lambda}+2\lambda.
 \tag{5.4}
\]

For a general core threshold \(0<\lambda\leq1/2\), the right-hand side of
(5.4) has derivative
\[
 -\frac{\varepsilon}{\lambda^2}+2
\]
and strictly positive second derivative \(2\varepsilon/\lambda^3\).
Its unique minimum is therefore at
\(\lambda=\sqrt{\varepsilon/2}\).  This value is admissible exactly when
\(\varepsilon\leq1/2\).  Substitution gives
\[
 \frac{\varepsilon}{\sqrt{\varepsilon/2}}
 +2\sqrt{\frac{\varepsilon}{2}}
 =\sqrt{2\varepsilon}+\sqrt{2\varepsilon}
 =2\sqrt{2\varepsilon}.
\]
This proves the claimed estimate.

The constant \(3\) results from the unoptimized algebraic choice
\(\lambda=\sqrt\varepsilon\), for which (5.4) reads
\(3\sqrt\varepsilon\) whenever that core threshold is admissible.  It is
also automatically a valid conclusion on the whole stated range because
\(2\sqrt2<3\).  Thus \(2\sqrt2\) and \(3\) are not constants for different
claims: they are respectively the optimized and a weaker bound for the
same claim.  The direct choice \(\lambda=\sqrt\varepsilon\) has the
additional limitation \(\varepsilon<1/4\) if disjointness is justified
solely by \(\lambda<1/2\); the optimized choice has no such loss on the
requested range.

## 6. The endpoint \(\varepsilon=0\)

If \(\varepsilon=0\), then \(MA=I_k\) exactly.  No conditioning or
division by a threshold is needed.  Take
\[
 E=AM.
\]
It is positive and unital, and
\[
 E^2=(AM)(AM)=A(MA)M=AI_kM=AM=E.
\]
Moreover \(\|AM-E\|_{\infty\to\infty}=0\), which is the claimed bound at
\(\varepsilon=0\).

For comparison with the core picture, (3.3) says in this case that
\(\mu_s\) is supported on
\(\{i:a_{is}=1\}\).  At every such \(i\), the probability row \(a_i\)
must equal \(e_s\).  These exact cores are disjoint, so the limiting
support-cleaning intuition is consistent, but the direct calculation
above is simpler and avoids defining a conditional measure at
\(\lambda=0\).

## 7. Sharpness of the square-root order

The following two-scale family shows that the exponent \(1/2\) is
necessary for PRH itself.

### 7.1. An elementary row-coincidence fact

We first prove a structural fact used in the lower bound.

**Row-coincidence lemma.**  Let \(F=(f_{ij})\) be a finite stochastic
idempotent.  If \(f_{ii}>0\), then for every \(j\) with \(f_{ij}>0\),
\[
 F_{j\bullet}=F_{i\bullet}.
 \tag{7.1}
\]

**Proof.**
Write \(\pi=F_{i\bullet}\).  Idempotence gives
\(\pi F=\pi\).  Let \(S=\{r:\pi_r>0\}\).  If \(t\notin S\), then
\[
 0=\pi_t=\sum_r\pi_rf_{rt}.
\]
All summands are nonnegative, so \(f_{rt}=0\) for every \(r\in S\).
Thus \(S\) is closed under the transitions of \(F\).

Consider the directed graph on \(S\), with an edge \(r\to t\) when
\(f_{rt}>0\).  There can be no edge between two distinct strongly
connected components.  To see this, suppose the condensation graph had
an edge.  Following incoming edges backwards from the tail of such an
edge produces a source component \(C\) which has an outgoing edge.  There
is no flow into \(C\) from \(S\setminus C\), while stationarity gives
\[
\begin{aligned}
 \pi(C)
 &=\sum_{r\in S}\pi_r F(r,C)\\
 &=\sum_{r\in C}\pi_r F(r,C)\\
 &=\pi(C)-\sum_{r\in C}\pi_r F(r,S\setminus C).
\end{aligned}
\]
The last subtracted term is positive because \(C\) has an outgoing edge
and \(\pi_r>0\) on \(S\), a contradiction.

Now \(f_{ir}=\pi_r>0\) for every \(r\in S\), so there is an edge
\(i\to r\) for every \(r\in S\).  Since there are no edges between
distinct strongly connected components, the graph on \(S\) is strongly
connected.

For each \(r\in S\), the row \(F_{r\bullet}\) is supported on \(S\), and
it is stationary because the \(r\)-th row of \(F^2=F\) says
\(F_{r\bullet}F=F_{r\bullet}\).  A finite irreducible stochastic matrix
has only one stationary probability vector; here is a short proof of
that fact.  The support of any stationary probability vector is a
nonempty closed subset, hence, by strong connectivity, is all of \(S\).
If \(q\) and \(p\) are two stationary probabilities on \(S\), put
\(c=\min_{r\in S}q_r/p_r>0\).  Then \(q-cp\) is nonnegative and
stationary and has a zero coordinate.  If it were nonzero, after
normalization it would be a stationary probability with proper support,
which is impossible.  Thus \(q=cp\), and total mass gives \(c=1\).

It follows that all rows \(F_{r\bullet}\), \(r\in S\), equal \(\pi\).
If \(f_{ij}>0\), then \(j\in S\), proving (7.1).  \(\square\)

### 7.2. The two-scale family

Fix \(0<\lambda<1/2\), take \(k=2,n=4\), and label the four states
\[
 x_1,\ x_2,\ y_1,\ y_2.
\]
Define the rows of \(A\) by
\[
\begin{array}{c|c}
 \text{state}&a_i\\ \hline
 x_1&(1,0)\\
 x_2&(0,1)\\
 y_1&(1-\lambda,\lambda)\\
 y_2&(\lambda,1-\lambda),
\end{array}
\tag{7.2}
\]
and define the two rows of \(M\) by
\[
 \mu_1=(1-\lambda)\delta_{x_1}+\lambda\delta_{y_1},
 \qquad
 \mu_2=(1-\lambda)\delta_{x_2}+\lambda\delta_{y_2}.
\tag{7.3}
\]
All displayed rows are probability vectors.  Direct substitution gives
\[
 (MA)_{1\bullet}=(1-\lambda^2,\lambda^2),
 \qquad
 (MA)_{2\bullet}=(\lambda^2,1-\lambda^2).
\]
Consequently
\[
 \|MA-I_2\|_{\infty\to\infty}=2\lambda^2.
\tag{7.4}
\]
Write
\[
 \varepsilon_\lambda=2\lambda^2.
\]
Then \(\varepsilon_\lambda\downarrow0\) with \(\lambda\downarrow0\), and
\(\varepsilon_\lambda<1/2\).

Let \(P=AM\).  From the rows (7.2),
\[
 P_{x_1\bullet}=\mu_1,
 \qquad
 P_{y_1\bullet}=(1-\lambda)\mu_1+\lambda\mu_2.
\tag{7.5}
\]
The supports of \(\mu_1\) and \(\mu_2\) are disjoint, so
\[
 \|P_{y_1\bullet}-P_{x_1\bullet}\|_1
 =\lambda\|\mu_2-\mu_1\|_1
 =2\lambda.
\tag{7.6}
\]

Let \(F\) be any stochastic idempotent on the four states, and put
\[
 d=\|P-F\|_{\infty\to\infty}.
\]
Suppose for contradiction that \(d<\lambda\).  Coordinate differences
are bounded by row \(\ell_1\)-differences, so (7.3) and (7.5) give
\[
 f_{x_1x_1}
 \geq P_{x_1x_1}-d
 =1-\lambda-d
 >1-2\lambda>0
\]
and
\[
 f_{x_1y_1}
 \geq P_{x_1y_1}-d
 =\lambda-d>0.
\]
The row-coincidence lemma therefore gives
\[
 F_{y_1\bullet}=F_{x_1\bullet}.
\]
Using this identity, (7.6), and the triangle inequality,
\[
\begin{aligned}
 2\lambda
 &=\|P_{y_1\bullet}-P_{x_1\bullet}\|_1\\
 &\leq
 \|P_{y_1\bullet}-F_{y_1\bullet}\|_1
 +\|F_{x_1\bullet}-P_{x_1\bullet}\|_1\\
 &\leq2d
 <2\lambda,
\end{aligned}
\]
a contradiction.  Hence every stochastic idempotent \(F\) satisfies
\[
 \boxed{\ \|AM-F\|_{\infty\to\infty}
       \geq\lambda
       =\sqrt{\frac{\varepsilon_\lambda}{2}}\ }.
\tag{7.7}
\]

The two scales are visible in (7.2)--(7.3): decoder contamination has
mass \(\lambda\), and the contaminated state's membership impurity is
also \(\lambda\).  Their product makes the retract defect of order
\(\lambda^2\), while an exact idempotent must pay order \(\lambda\).
Thus no \(o(\sqrt\varepsilon)\) conclusion can hold uniformly in PRH.

## 8. Hypothesis ledger

The uses of the assumptions are as follows.

1. **Rows of \(A\) are probability vectors.**  Nonnegativity and row
   sums equal to one are used to make \(MA\) stochastic, to identify
   \(1-R_{ss}\) with the nonnegative expectation in (3.3), to make cores
   disjoint, to control convex mixtures in (5.1), and to obtain the
   \(2(1-a_{is})\) bound in (5.2).

2. **Rows of \(M\) are probability vectors.**  Nonnegativity and row sums
   equal to one are used to make \(MA\) stochastic, to interpret (3.3)
   as an expectation, to apply the one-sided Markov estimate, and to
   make each conditioned row \(\nu_s\) a probability vector.

3. **Positivity and unitality.**  For maps between these finite
   \(\ell_\infty\) spaces, positivity and unitality are exactly the
   assertion that the representing rows are probability vectors.
   Nothing beyond that row description is used.  In particular, no
   faithfulness, injectivity, surjectivity, or norm assumption on \(A\)
   or \(M\) is used separately.

4. **The defect bound.**  It is used only through the rowwise estimate
   (3.3).

5. **Smallness.**  For \(0<\varepsilon<1/2\),
   \(\lambda=\sqrt{\varepsilon/2}<1/2\), which gives disjoint cores.
   It also gives \(\beta_s\leq\lambda<1\), so conditioning is legal.
   No stronger smallness hypothesis is needed.  At
   \(\varepsilon=1/2\), one has \(\lambda=1/2\); the strict inequality in
   the core definition still prevents two coordinates from both
   exceeding \(1/2\), and \(\beta_s\leq1/2<1\), so the proof actually
   includes that endpoint.

6. **Finite dimensions.**  They are used only to write finite sums,
   choose maximizing rows in (2.1), and use the elementary finite-state
   row-coincidence lemma in the sharpness argument.

## 9. Defect register

1. **Verification status.**  This is author output and has not been
   checked by the separate hostile verifier.  No claim of external
   validation is made.

2. **Known logical gaps.**  I found no unclosed step in the upper-bound
   proof, the endpoint argument, or the sharpness family.  This statement
   records the prover's accounting only; it is not a self-certification.

3. **Optimal universal constant remains open here.**  The report proves
   an upper constant \(2\sqrt2\) and a lower constant \(1/\sqrt2\) from
   the explicit family.  It does not determine the best possible
   universal constant in PRH.  What is settled is the stated
   \(2\sqrt2\)-versus-\(3\) discrepancy and the necessity of the
   square-root exponent.

4. **Correction to the prompt's norm warning.**  Under the given
   hypotheses, \(MA\) and \(I_k\) are both stochastic, so \(MA-I_k\) is a
   difference of two stochastic matrices.  The norm formula itself is
   valid for every matrix.  The special stochastic-row calculation is
   needed only for the exact equality
   \(\|R_{s\bullet}-e_s\|_1=2(1-R_{ss})\).

5. **Slightly strengthened threshold.**  The requested hypothesis is
   \(\varepsilon<1/2\).  Because the core inequalities are strict, the
   proof also covers \(\varepsilon=1/2\).  No assertion is made here for
   larger defects using this construction.
