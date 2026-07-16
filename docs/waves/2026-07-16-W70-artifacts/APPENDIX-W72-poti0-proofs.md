# Appendix: standalone proofs of the W72 POTI-0 routine batch

Everything in this appendix remains proposed / `conjecture`.  The arguments
below verify the four requested conditional derivations; they promote no
registry shard and prove neither RDSE nor LDHR-48.

## 0. Pinned datum, notation, and hypothesis audit

### 0.1 Common notation

Work on the finite full row-point quotient \(\mathcal Q=I/{\sim}\), where
\(i\sim j\) means \(p_i=p_j\).  All measures below are nonnegative measures on
the full fibers \(Q\in\mathcal Q\).  For a row \(i\),

\[
 P_i^+(F):=\sum_{R\in F}\sum_{k\in R}(P_{ik})_+.
\]

Adopt the literal antecedent of
`argument/conj-dtr-zero-oriented-surplus-exclusion.md`.  In particular,

\[
 c_m=\frac14,\qquad b=\frac{c_m}{128}=\frac1{512},
 \qquad \tau=\sqrt\delta>0,
\]

\[
 \delta\le\delta_{\rm rt}:=
 \min\left\{2^{-16},(c_m/4)^2,(c_mb/120)^2\right\},
 \quad D_0=2+4\delta,
 \quad e_\delta=2\delta(1+\delta).
 \tag{0.1}
\]

Let \(m_A\) be the original selected measure,

\[
 m_A(Q)=\sum_{j\in A\cap Q}(P_{vj})_+,qquad
 S=m_A(1)\ge c_m,qquad
 q_A=S^{-1}\sum_Qm_A(Q)p_Q.
 \tag{0.2}
\]

For the fixed selected-corner certificate
\(\mathscr C^*=(\phi,h,f^*,\eta^*)\), the fixed arbitrary reduced display
field, and the fixed full-fiber carrier set \(B\subset\mathsf D_{\rm tail}\),
write

\[
 \eta_B(Q):=\eta_D^*(B\cap Q),\quad M_B:=\eta_B(1)>\frac1{160},
 \quad \rho(Q):=\min\{m_A(Q),\eta_B(Q)\},\quad r:=\rho(1).
 \tag{0.3}
\]

Put \(z=H-\phi\),

\[
 \mathcal T_u:=\{R:|\chi_u(p_R)|>1\},\qquad
 c_{u,R}:=\sum_{k\in R}P_{uk},
\]

\[
 \mathfrak t_\phi(u):=
 \sum_{R\in\mathcal T_u}(c_{u,R})_+z(p_R),\qquad
 \mathfrak G_\phi:=
 \sum_{u\in B}\rho(u)
 [\mathfrak t_\phi(u)-D_0\delta]_+.
 \tag{0.4}
\]

Here, as in the registry contract, \(u\) indexes a full-fiber carrier and
\(\rho(u)\) is the mass of its full row-point fiber.  Finally set

\[
 C_W:=\operatorname{conv}\{p_w:w\in W\},
\]

\[
 Y_v:=\{y:\|y\|_\infty\le1,
             \ y\mathbin\cdot p_v-h_{C_W}(y)=H\},qquad
 Z_v(q_A):=\sup_{y\in Y_v}y\mathbin\cdot(p_v-q_A),
 \tag{0.5}
\]

\[
 \mathcal L_v:=\{Q:\operatorname{dist}_1(p_Q,C_W)\le\tau/4\},
 \qquad
 \mathcal E_*:=\{R:\|p_R-p_{f^*}\|_1>1/2\}.
 \tag{0.6}
\]

For an arbitrary attained certificate in
`lem-l5-top-face-ray-formula`, define, with \(c\) absent when \(\Lambda=0\),

\[
 \mathscr R_A(\Lambda,c):=
 \|p_v-q_A+\Lambda(p_v-c)\|_1-\Lambda H.
 \tag{0.7}
\]

### 0.2 Clause-by-clause check of the literal POTI-0 hypothesis block

The authoritative pinned block is the part of the `contract:` line of
`conj-dtr-zero-oriented-surplus-exclusion` preceding its conclusion.  Splitting
that single registry line only at its logical clauses, it supplies all of the
following.

1. **Constants and base datum.**  It fixes \(c_m=1/4\),
   \(b=c_m/128\), \(\delta_{\rm rt}\), and \(D_0=2+4\delta(P)\).  It assumes
   a finite exact signed idempotent \(P\), \(0<\delta(P)\le1/4\), a nonempty
   visible set \(W\), and a hidden top vertex \(v\) with
   \(H>16\tau\), \(\tau=\sqrt{\delta(P)}\).

2. **Original selected mass.**  Every \(j\in A\) is at distance at least
   \(4\tau\) from \(p_v\) and has depth strictly greater than \(H-8\tau\).
   The full-fiber measure in (0.2) has mass \(S\ge c_m\).

3. **I-base and ultra hypotheses.**  The measure \(\omega\) is the stated
   restriction of \(P_v^+\) to \(G_v\).  For every
   \(c\in K(P)\) with \(\|c-p_v\|_1\le1/4\), the strict shallow upper bound
   and the non-strict far-deep lower bound are present.  The parent bounds
   \(\|r_\omega-p_v\|_1<1/8\) and \(\Omega(\omega)<1/16\) hold, as do
   \(\delta\le\delta_{\rm rt}\),
   \(\|r_\omega-p_v\|_1<b\tau\), \(\Omega(\omega)<b\tau\), and the literal
   rim definition with \(\theta<\tau/D_0\).

4. **Selected certificate.**  The exhibited
   \(\mathscr C^*=(\phi,h,f^*,\eta^*)\) is explicitly obtained from
   `lem-ihorn-selected-corner-extraction` and satisfies
   \(M_X\le1/8\), \(M_I<1/16\), and \(M_D>1/16\).

5. **Arbitrary displays and tail statistics.**  The block defines
   \(\eta_D^*\), fixes an arbitrary reduced optimal display for every
   \(u\in\operatorname{supp}\eta_D^*\), and defines
   \(A_u,q_u,\ell_u,g_u\), the normalized
   \((\widetilde q_u,\widetilde A_u)\), \(\chi_u\), \(c_{u,Q}\),
   \(\operatorname{Tail}_1(u)\), \(\mathsf A_{\rm esc}\), \(h_u\), and
   \(\mathsf D_{\rm tail}\), with exactly the displayed strict and weak
   boundaries.

6. **The carrier set.**  The block quantifies over a full-fiber
   \(B\subset\mathsf D_{\rm tail}\) satisfying
   \(\eta_D^*(B)>1/160\),
   \(\operatorname{Tail}_1(u)>\tau/8\),
   \(\min_f\|p_f-x_u\|_1>3\delta\), and \(h_u\le3\delta\) for every
   \(u\in B\).  It also defines \(\mathcal U_B\) and assumes
   \(P_{f^*}^+(\mathcal U_B)>\tau/2560\).

7. **Original, unnormalized overlap.**  On the finite quotient it redefines
   the *original* \(m_A\), not \(\lambda_A\), and defines exactly
   \(S,q_A,\rho,z,\mathcal T_u,\mathfrak t_\phi,\mathfrak G_\phi\), and the
   objects \(C_W,h_{C_W},Y_v,Z_v,\mathcal L_v,\mathcal E_*\) used here.

8. **POTI-0 boundary.**  The triggering hypothesis is
   \(\mathfrak G_\phi=0\).  Thus equality remains in POTI-0.

These eight checks are the complete semantic content of the literal
hypothesis block used below.  We use no conclusion of the conjectural
`conj-dtr-zero-oriented-surplus-exclusion`; doing so would be circular.

### 0.3 W70 interface audit

The four named W70 shards were opened and compared with clauses 1--7 above.

| Shard | Literal-hypothesis check and use here |
|---|---|
| `lem-dtr-canonical-overlap` (COV) | Its long pinned block is clauses 1--7 verbatim.  Its conclusion is that the atomwise minimum \(\rho\) is an additive full-fiber common submeasure of \(m_A\) and \(\eta_D^*|_B\).  It is proved L5 and is consumed in S0 and O48 (and for the overlap notation in RX). |
| `lem-dtr-oriented-tail-ray-conversion` (POTI-R) | Its pinned block is again clauses 1--7 and its proved L5 conclusion is \(S Z_v(q_A)\ge\mathfrak G_\phi\).  At \(\mathfrak G_\phi=0\) this supplies only \(Z_v(q_A)\ge0\), so it is audited but not consumed by any proof below. |
| `lem-dtr-tail-coherent-conversion` (TC) | Besides clauses 1--7 it fixes \(r_0,\alpha,\lambda\) before the datum and assumes its coherent-carrier mass and smaller ceiling.  Those extra hypotheses are not part of POTI-0.  TC is proved L5 but is not consumed. |
| `lem-dtr-poti-assembly` | Its datum block is clauses 1--7, but its contract additionally assumes both conjectural POTI-0 and POTI+ exclusions.  Those hypotheses are unavailable here.  The shard is a proved conditional implication and is not consumed; ASM2 is proved directly below. |

Thus there is no illicit unconditional use of a conditional W70 conclusion.

## 1. S0 — exact cause split

### Pinned contract (verbatim from `POTI0-ATTACK.md` §1.2)

> **(a) Pinned contract — `conj-w72-poti0-exact-cause-split`.** Every pinned
> datum with \(\mathfrak G_\phi=0\) lies in exactly one of
> \[
>  \mathsf Z:=\{r=0\},
>  \qquad
>  \mathsf O:=\{r>0:\mathfrak t_\phi(u)\le D_0\delta
>                    \text{ whenever }\rho(u)>0\}.
>  \tag{S0}
> \]

### Registry shards consumed and hypothesis checks

| Shard | Exact role | Hypothesis check |
|---|---|---|
| `lem-dtr-canonical-overlap` | Makes \(\rho\) a nonnegative additive full-fiber measure and a submeasure of both pinned measures. | Its literal block is clauses 1--7 of §0.2; each is part of the pinned datum. |

The positive-part notation and finite additivity are definitions, not extra
registry inputs.

### Proof

By COV, \(\rho(Q)\ge0\) for every fiber and

\[
 r=\rho(1)=\sum_Q\rho(Q)\ge0.
\]

For every carrier fiber \(u\),

\[
 \rho(u)[\mathfrak t_\phi(u)-D_0\delta]_+\ge0.
\]

The sum of these finitely many nonnegative quantities is
\(\mathfrak G_\phi=0\).  Consequently every summand is zero.

If \(r=0\), the datum is in \(\mathsf Z\).  If \(r>0\) and
\(\rho(u)>0\), then

\[
 0=\rho(u)[\mathfrak t_\phi(u)-D_0\delta]_+
\]

and division by the positive scalar \(\rho(u)\) gives

\[
 [\mathfrak t_\phi(u)-D_0\delta]_+=0,
 \qquad\text{so}\qquad
 \mathfrak t_\phi(u)\le D_0\delta.
\]

Thus every datum belongs to \(\mathsf Z\cup\mathsf O\).  The two classes are
disjoint because their scalar conditions are \(r=0\) and \(r>0\).  In
particular equality \(r=0\) belongs to \(\mathsf Z\), as required.  No
carrier, atom, display, or positive threshold for \(r\) was selected. \(\square\)

## 2. RX — selected-root exchange ledger on \(r=0\)

Define

\[
 C_B:=\{Q:\eta_B(Q)>0\},\qquad Q_*:=Q_{f^*},
 \qquad w_*:=m_A(Q_*),
\]

\[
 \sigma_B:=(P_v^+-m_A)(C_B).
 \tag{2.1}
\]

### Pinned contract (verbatim from `POTI0-ATTACK.md` §1.3)

> **(a) Pinned contract — `conj-w72-poti0-root-selection-exchange-ledger`.**
> Every pinned datum with \(r=0\) satisfies
> \[
>  \boxed{\sigma_B\ge w_*M_B-e_\delta.}
>  \tag{RX}
> \]

### Registry shards consumed and hypothesis checks

| Shard | Exact role | Literal-hypothesis check |
|---|---|---|
| `lem-ihorn-cotop-sl1a-package` | Defines \(\lambda_A=(\mu_A|_{\{d_Q>H-4\tau\}})/(1-\theta)\) and \(S(1-\theta)\lambda_A\le P_v^+\). | It requires clauses 1--3 of §0.2.  The selected support is far/deep, \(S\ge c_m\), the I-base inequalities and strict parent bounds hold, and the pinned ultra bounds and \(\theta<\tau/D_0\) hold. |
| `lem-ihorn-selected-corner-extraction` | States literally that the selected row point \(f^*\) lies in \(\operatorname{supp}\lambda_A\). | It has the same clauses 1--3 and then constructs the public certificate of clause 4.  The pinned certificate is explicitly required to be obtained from this construction. |
| `lem-dcap-root-closure` | Gives \(\eta_D^*\le P_{f^*}^+\) as full-fiber measures. | Its antecedent is clauses 1--4.  The exact D-cell inequalities in clause 4 match its weak/strict boundaries. |
| `lem-dtr-canonical-overlap` | Identifies \(r\) with the mass of the atomwise minimum in (0.3). | Clauses 1--7 match, as audited in §0.3. |
| `lem-l5-positive-flow-foldback` | Used exactly once with source \(m_*=w_*1_{\{Q_*\}}\) and common test \(g_*=w_*1_{C_B}\). | Its generic hypotheses are checked explicitly in Step 3 below.  Its literal error is \(2\delta(1+\delta)M=e_\delta M\). |

No ICAP shard, B5 overlay, or numerical fixture is used.

### Proof

**Step 1: selected-root provenance, including partial clone fibers.**  Since
\(\delta\le1/4\), one has \(\tau\le1/2\) and \(D_0\ge2\), hence
\(\tau/D_0\le1/4\).  Thus \(\theta<\tau/D_0<1\), so
\(S(1-\theta)>0\).  On the finite full-fiber quotient, the literal formula in
`lem-ihorn-cotop-sl1a-package` gives

\[
 \lambda_A(Q)=
 \frac{m_A(Q)}{S(1-\theta)}
 \quad\text{on }\{d_Q>H-4\tau\}.
 \tag{2.2}
\]

The extraction shard chooses \(f^*\in\operatorname{supp}\lambda_A\).  For a
finite atomic probability this means
\(\lambda_A(Q_{f^*})>0\).  Equation (2.2) then gives

\[
 w_*=m_A(Q_{f^*})=S(1-\theta)\lambda_A(Q_{f^*})>0.
 \tag{2.3}
\]

This remains valid when \(A\) selects only part of the clone fiber:
\(m_A(Q_{f^*})=\sum_{j\in A\cap Q_{f^*}}(P_{vj})_+\) is the mass of the
*entire quotient atom*, computed from the selected indices in that atom.
Positive atom mass does not require \(A\) to contain every clone.  Thus the
literal shards do deliver the full-fiber positivity required by RX; there is
no selected-root provenance defect.

Also, fiber by fiber,

\[
 m_A(Q)=\sum_{j\in A\cap Q}(P_{vj})_+
 \le\sum_{j\in Q}(P_{vj})_+=P_v^+(Q),
 \tag{2.4}
\]

so \(m_A\le P_v^+\) and \(\sigma_B\ge0\).

**Step 2: zero overlap is atomwise zero support.**  Since \(r=0\),

\[
 0=r=\sum_Q\min\{m_A(Q),\eta_B(Q)\}.
\]

Every summand is nonnegative, so for every \(Q\),

\[
 \min\{m_A(Q),\eta_B(Q)\}=0.
 \tag{2.5}
\]

If \(Q\in C_B\), then \(\eta_B(Q)>0\).  If also \(m_A(Q)>0\), the minimum
in (2.5) would be positive.  Therefore

\[
 Q\in C_B\Longrightarrow m_A(Q)=0,
 \qquad m_A(C_B)=0.
 \tag{2.6}
\]

This is the required atomwise argument; no cancellation is possible.  It
follows that

\[
 \sigma_B=(P_v^+-m_A)(C_B)=P_v^+(C_B).
 \tag{2.7}
\]

Root closure gives \(\eta_D^*\le P_{f^*}^+\).  Restricting to \(B\) preserves
the inequality, so

\[
 \eta_B\le P_{f^*}^+,qquad
 P_{f^*}^+(C_B)\ge\eta_B(C_B)=M_B>\frac1{160}.
 \tag{2.8}
\]

**Step 3: the one legal foldback and every factor in the ledger.**  Let

\[
 m_*:=w_*1_{\{Q_*\}},\qquad
 g_*:=w_*1_{C_B}.
\]

At \(Q_*\), \(m_*(Q_*)=w_*=m_A(Q_*)\); elsewhere it is zero.  Hence, using
(2.4),

\[
 0\le m_*\le m_A\le P_v^+.
\]

Thus \(m_*\) is a legal nonnegative full-fiber source for
`lem-l5-positive-flow-foldback`.  The test is a single common full-fiber
test, independent of any carrier, and

\[
 0\le g_*\le w_*.
\]

Consequently the foldback parameter is exactly \(M=w_*\).  Because all rows
in \(Q_*\) equal the row \(p_{f^*}\), its left side is

\[
 \begin{aligned}
 \sum_Qm_*(Q)P_Q^+(g_*)
 &=m_*(Q_*)P_{Q_*}^+(w_*1_{C_B})\\
 &=w_*\,[w_*P_{f^*}^+(C_B)]
 =w_*^2P_{f^*}^+(C_B).
 \end{aligned}
\]

Its top-row term and error are, respectively,

\[
 P_v^+(g_*)=w_*P_v^+(C_B),
 \qquad
 2\delta(1+\delta)M=w_*e_\delta.
\]

The one undivided ledger is therefore exactly

\[
 w_*^2P_{f^*}^+(C_B)
 \le w_*P_v^+(C_B)+w_*e_\delta.
 \tag{2.9}
\]

The shard scales its error by the test bound \(M\); here
\(M=w_*=m_*(1)\), so the error is literally source-mass-scaled.

By (2.3), division by \(w_*>0\) is legal and gives

\[
 w_*P_{f^*}^+(C_B)\le P_v^+(C_B)+e_\delta.
\]

Using (2.8) and then (2.7),

\[
 w_*M_B
 \le w_*P_{f^*}^+(C_B)
 \le \sigma_B+e_\delta,
\]

which rearranges to

\[
 \boxed{\sigma_B\ge w_*M_B-e_\delta}.
\]

Finally, because \(M_B>1/160\) and \(w_*>0\),

\[
 \sigma_B\ge w_*M_B-e_\delta
 >\frac{w_*}{160}-e_\delta.
 \tag{2.10}
\]

The foldback was invoked once, with one common nonnegative test. \(\square\)

## 3. O48 — the fixed-level starvation ledger on \(\mathsf O\)

Set

\[
 V_{48}:=\{R:z(p_R)<48\tau\},
\]

so equality \(z=48\tau\) belongs to its high-deficit complement.  For every
\(\rho(u)>0\), set

\[
 L_{48}(u):=\sum_{R\in\mathcal T_u\cap V_{48}}(c_{u,R})_+,
\]

and

\[
 \mathscr H_{48}:=\min\left\{
   \min_{\rho(u)>0}L_{48}(u),
   \min_{\rho(u)>0}P_u^+(V_{48}),
   \frac{P_v^+(V_{48})+e_\delta}{r}
 \right\}.
 \tag{3.1}
\]

### Pinned contract (verbatim from `POTI0-ATTACK.md` §1.5)

> **(a) Pinned contract — `conj-w72-poti0-fixed-level-starvation-ledger`.**
> Every pinned datum in \(\mathsf O\) satisfies
> \[
>  \boxed{\mathscr H_{48}>\frac\tau{16}.}
>  \tag{O48}
> \]

### Registry shards consumed and hypothesis checks

| Shard | Exact role | Literal-hypothesis check |
|---|---|---|
| `lem-dtr-canonical-overlap` | Gives \(0\le\rho\le m_A\) as a full-fiber measure. | Its clauses 1--7 are exactly §0.2. |
| `lem-top-deficit-price` | For the pinned top support functional, gives the used sign \(z(p_R)\ge0\) on every row fiber. | It requires an exact signed idempotent with \(\delta>0\), nonempty \(W\), and hidden top \(v\), all in clause 1; the certificate's \(\phi\) is an admissible top support functional by clauses 4--5. |
| `lem-aesc-synthetic-finance-tail-amplification` | Gives the strict pointwise floor \(\operatorname{Tail}_1(u)>\tau/8\). | Its common block is clauses 1--5.  For every \(u\in B\), clause 6 and \(B\subset\mathsf D_{\rm tail}\subset\mathsf A_{\rm esc}\) give \(g_u\ge\tau\), \(A_u\ge4\), \(\ell_u\ge\tau/2\), and \(h_u\le3\delta\), exactly its remaining hypotheses.  Hence it applies to every \(u\in B\), not merely overlapped carriers; restricting to \(\rho(u)>0\) is legal. |
| `lem-l5-positive-flow-foldback` | Used exactly once with source \(\rho\) and common test \(g_{48}=r1_{V_{48}}\). | Its source and test hypotheses are checked in Step 3.  Its literal error is \(e_\delta M\). |

Membership in \(\mathsf O\), supplied by S0, is exactly \(r>0\) together
with \(\mathfrak t_\phi(u)\le D_0\delta\) on positive \(\rho\)-mass.  No TC,
POTI-R, TU foldback, or carrier-dependent test is consumed.

### Proof

**Step 1: high-level truncation.**  Since \(\delta\le1/4\),

\[
 D_0=2+4\delta\le3.
 \tag{3.2}
\]

Fix \(u\) with \(\rho(u)>0\).  Membership in \(\mathsf O\) gives
\(\mathfrak t_\phi(u)\le D_0\delta\).  The top-deficit shard gives
\(z(p_R)\ge0\).  Hence the non-high summands in \(\mathfrak t_\phi(u)\)
are nonnegative, while on the discarded set
\(z(p_R)\ge48\tau\).  Therefore

\[
 \begin{aligned}
 48\tau
 \sum_{\substack{R\in\mathcal T_u\\z(p_R)\ge48\tau}}
      (c_{u,R})_+
 &\le
 \sum_{\substack{R\in\mathcal T_u\\z(p_R)\ge48\tau}}
      (c_{u,R})_+z(p_R)\\
 &\le \mathfrak t_\phi(u)
 \le D_0\delta.
 \end{aligned}
\]

Because \(\tau=\sqrt\delta>0\), division by \(48\tau\) is legal, and

\[
 \sum_{\substack{R\in\mathcal T_u\\z(p_R)\ge48\tau}}
      (c_{u,R})_+
 \le\frac{D_0\delta}{48\tau}
 =\frac{D_0\tau}{48}
 \le\frac{3\tau}{48}=\frac\tau{16}.
 \tag{3.3}
\]

This verifies exactly the constant and the high-side boundary in (1.14).

**Step 2: strict pointwise remainders and positive fiber aggregation.**  The
AESC shard applies to every \(u\in B\), as checked above, and gives

\[
 \operatorname{Tail}_1(u)
 =\sum_{R\in\mathcal T_u}(c_{u,R})_+>\frac\tau8.
\]

The partition uses \(z<48\tau\) for \(V_{48}\) and
\(z\ge48\tau\) for its complement.  Subtracting (3.3) from the strict floor
therefore yields

\[
 L_{48}(u)
 >\frac\tau8-\frac\tau{16}
 =\frac{2\tau-\tau}{16}
 =\frac\tau{16}.
 \tag{3.4}
\]

For each full fiber \(R\), signed aggregation satisfies

\[
 (c_{u,R})_+
 =\left(\sum_{k\in R}P_{uk}\right)_+
 \le\sum_{k\in R}(P_{uk})_+.
 \tag{3.5}
\]

Thus negative coefficients cannot invalidate the next step:

\[
 P_u^+(V_{48})
 =\sum_{R\in V_{48}}\sum_{k\in R}(P_{uk})_+
 \ge\sum_{R\in\mathcal T_u\cap V_{48}}(c_{u,R})_+
 =L_{48}(u)>\frac\tau{16}.
 \tag{3.6}
\]

**Step 3: source domination and the one undivided foldback.**  Since
\(r>0\), the finite set \(\{Q:\rho(Q)>0\}\) is nonempty.  Rows in one
full row-point fiber coincide.  Moreover,
\(\rho(Q)>0\) implies \(\eta_B(Q)>0\), so some carrier
\(u\in B\cap Q\) has positive \(\eta_D^*\)-mass; (3.6), which holds for
every carrier in \(B\), therefore gives
\(P_Q^+(V_{48})=P_u^+(V_{48})>\tau/16\) for each such \(Q\).
Multiplication by the positive weights \(\rho(Q)\), followed by summation,
gives the strict source-side inequality

\[
 \sum_Q\rho(Q)P_Q^+(V_{48})
 >\sum_Q\rho(Q)\frac\tau{16}
 =\frac{r\tau}{16}.
 \tag{3.7}
\]

This is the source-domination step; it uses all of \(\rho\), not a selected
carrier subset.

Now take the single common test

\[
 g_{48}:=r1_{V_{48}},\qquad 0\le g_{48}\le r.
\]

COV gives \(0\le\rho\le m_A\), and (2.4) gives
\(m_A\le P_v^+\).  Hence \(\rho\) is a legal source for foldback.  The test
bound is exactly \(M=r=\rho(1)\), so the foldback error is

\[
 2\delta(1+\delta)M=re_\delta.
\]

The lemma's left and top-row terms are

\[
 \sum_Q\rho(Q)P_Q^+(g_{48})
 =r\sum_Q\rho(Q)P_Q^+(V_{48}),
\]

\[
 P_v^+(g_{48})=rP_v^+(V_{48}).
\]

Multiplying (3.7) by \(r>0\) and then applying this one foldback produces
both inequalities in the exact undivided ledger:

\[
 \boxed{
 \frac{r^2\tau}{16}
 <r\sum_Q\rho(Q)P_Q^+(V_{48})
 \le rP_v^+(V_{48})+re_\delta.}
 \tag{3.8}
\]

No division preceded (3.8).  By transitivity,
\(r^2\tau/16<r(P_v^+(V_{48})+e_\delta)\).  Divide this inequality once by
\(r>0\), and then divide the resulting inequality once more by \(r>0\), to
obtain

\[
 \frac{r\tau}{16}<P_v^+(V_{48})+e_\delta,
 \qquad
 \frac{P_v^+(V_{48})+e_\delta}{r}>\frac\tau{16}.
 \tag{3.9}
\]

Equations (3.4), (3.6), and (3.9) show that all three entries of the finite
minimum (3.1) are strictly larger than \(\tau/16\).  Therefore

\[
 \boxed{\mathscr H_{48}>\frac\tau{16}}.
\]

The level \(48\tau\) was fixed once, equality belongs to the high complement,
and the foldback was invoked once with one common nonnegative test. \(\square\)

## 4. ASM2 — conditional assembly and strict close

### Single minimal conditional contract

**`conj-w72-poti0-routine-conditional-assembly` (ASM2).**  Assume the proposed
contracts S0 (`conj-w72-poti0-exact-cause-split`), RX
(`conj-w72-poti0-root-selection-exchange-ledger`), O48
(`conj-w72-poti0-fixed-level-starvation-ledger`), RDSE
(`conj-w72-poti0-root-dilution-selected-support-exchange`), and LDHR-48
(`conj-w72-poti0-low-deficit-huddle-ray-48`).  Then every pinned POTI-0 datum
with \(\mathfrak G_\phi=0\) satisfies the single conclusion

\[
 \boxed{Z_v(q_A)>\frac{7c_m}{960}\tau.}
 \tag{ASM2}
\]

The two creative hypotheses have exactly their §1.4 and §1.6 meanings:

- RDSE applies only when \(r=0\), after RX has supplied the forced package
  \((C_B,w_*,M_B,\sigma_B)\), and for every arbitrary attained ray certificate
  gives
  \[
   \mathscr R_A(\Lambda,c)\ge
   \frac18P_v^+(\mathcal E_*)-
   \frac{c_m}{16}P_v^+(\mathcal L_v).
   \tag{4.1}
  \]

- LDHR-48 applies only on \(\mathsf O\), after O48 has supplied its forced
  package, and for every arbitrary attained ray certificate gives the same
  inequality (4.1).

These are named hypotheses here; nothing in this appendix proves them.

### Registry shards consumed and hypothesis checks

| Shard | Exact role | Literal-hypothesis check |
|---|---|---|
| `lem-l5-top-face-ray-formula` | Identifies (4.1) with exact EC for every attained certificate, including \(\Lambda=0\). | It requires an exact signed idempotent with \(\delta>0\), nonempty \(W\), hidden top \(v\), and \(q_A\in K(P)\).  Clauses 1--2 give the first three.  By (0.2), \(q_A\) is a convex combination of row points because \(m_A\ge0\) and \(S>0\), so \(q_A\in K(P)\). |
| `lem-dcap-tall-same-center-packet` (B4) | B4.2 supplies the exterior term once at \(p_{f^*}\); B4.1 supplies the strict shallow upper bound last. | Its antecedent is clauses 1--4: the same I-base datum, ultra ceiling and rim bound, and the fixed D selected-corner certificate.  All weak/strict D-cell boundaries match. |
| `lem-ihorn-tall-halo-saturation` | The dependency that spends \(H>16\tau\) inside B4.1. | Its literal block is the I-base part of clauses 1--3, including the two centerwise inequalities and strict parent bounds.  Thus the pinned datum satisfies it. |

S0, RX, O48, RDSE, and LDHR-48 are the five explicitly named proposed
hypotheses of ASM2, not registry conclusions silently imported.  In
particular, `lem-dtr-poti-assembly` is not consumed.

### Proof

Fix a pinned datum with \(\mathfrak G_\phi=0\), after the constants, datum,
certificate, arbitrary kernel, arbitrary display field, \(B\), and the
diagnostics \((\rho,\mathfrak t_\phi,\mathfrak G_\phi)\) have all been fixed.
Then fix an arbitrary attained top-face certificate \((\Lambda,c)\), with
\(c\) absent if \(\Lambda=0\).

**Step 1: exhaustive residual consumption.**  S0 gives exactly one of the
following.

- If \(r=0\), RX supplies the forced package
  \((C_B,w_*,M_B,\sigma_B)\), and RDSE, on precisely this subclass, gives
  (4.1).

- If \(r>0\), S0 gives
  \(\mathfrak t_\phi(u)\le D_0\delta\) whenever \(\rho(u)>0\).  Thus the
  datum lies in \(\mathsf O\); O48 supplies its forced
  \((r,V_{48},L_{48},\mathscr H_{48},e_\delta)\) package, and LDHR-48, on
  precisely this subclass, gives (4.1).

The alternatives are exhaustive and disjoint because \(r\ge0\), with equality
owned by \(r=0\).  Each creative residual has been used only on its own
subclass.

**Step 2: the ray identity and exact EC before any B4 spend.**  The literal
ray-formula contract says

\[
 Z_v(q_A)=
 \min_{\Lambda\ge0,\ c\in C_W}
 \bigl(\|p_v-q_A+\Lambda(p_v-c)\|_1-\Lambda H\bigr),
 \tag{4.2}
\]

with \(c\) omitted at \(\Lambda=0\), and says that the minimum is attained.
Therefore *every* attained minimizer—not a favorably chosen one—has its value
equal to the minimum.  For the arbitrary attained certificate fixed above,

\[
 \mathscr R_A(\Lambda,c)=Z_v(q_A).
 \tag{4.3}
\]

If \(\Lambda=0\), the left side is literally
\(\|p_v-q_A\|_1\), with no undefined \(c\), and (4.3) still follows from
attainment.  Combining (4.1) and (4.3), in either S0 case, yields exact EC:

\[
 \boxed{
 Z_v(q_A)\ge
 \frac18P_v^+(\mathcal E_*)-
 \frac{c_m}{16}P_v^+(\mathcal L_v).}
 \tag{EC}
\]

No B4 conclusion has yet been used.

**Step 3: consume B4.2 once, at the already fixed center.**  The literal B4.2
conclusion is

\[
 P_v^+(\mathcal E_*)\ge\frac{\tau S}{8}
 \ge\frac{c_m\tau}{8},
\]

where \(\mathcal E_*\) is centered at the already fixed \(p_{f^*}\).  Hence

\[
 \frac18P_v^+(\mathcal E_*)
 \ge\frac18\frac{\tau S}{8}
 =\frac{\tau S}{64}
 \ge\frac{c_m\tau}{64},
 \tag{4.4}
\]

using the pinned \(S\ge c_m\).  This is one use of B4.2.  Substitution into
EC, whose shallow subtraction is already present, gives

\[
 Z_v(q_A)\ge
 \frac{c_m\tau}{64}-
 \frac{c_m}{16}P_v^+(\mathcal L_v).
 \tag{4.5}
\]

The separate banked tail-union floor
\(P_{f^*}^+(\mathcal U_B)>\tau/2560\) is not used as the source of (4.4);
B4.2 alone supplies its \(\tau S/8\) exterior mass at \(p_{f^*}\).

**Step 4: verify and spend B4.1 last.**  B4.1 states literally

\[
 P_v^+(\mathcal L_v)<\ell_T
 :=\delta+\frac{4\tau}{63}\left(D_0+\frac\tau4\right)
 <\frac{2\tau}{15}.
 \tag{4.6}
\]

For completeness, its final numerical inequality follows independently from
the pinned ceiling.  Since \(\delta=\tau^2\), \(D_0=2+4\tau^2\), and
\(\delta\le2^{-16}\), one has \(\tau\le1/256\), and

\[
 \begin{aligned}
 \frac{\ell_T}{\tau}
 &=\tau+\frac4{63}\left(2+4\tau^2+\frac\tau4\right)\\
 &=\frac8{63}+\frac{64\tau}{63}+\frac{16\tau^2}{63}\\
 &\le\frac8{63}+\frac1{252}+\frac1{258048}.
 \end{aligned}
\]

To compare the last expression with \(2/15\), retain the exact difference
from \(8/63\):

\[
 \frac{2}{15}-\frac8{63}=\frac2{315},
 \qquad
 \frac2{315}-\frac1{252}=\frac1{420},
 \qquad
 \frac1{258048}<\frac1{420}.
\]

Therefore

\[
 \frac8{63}+\frac1{252}+\frac1{258048}<\frac2{15},
\]

which confirms the strict second inequality in (4.6).  (The intermediate
upper bounds used only \(\tau\le1/256\).)

Now, and only now, use the strict bound in (4.6) in (4.5).  Because
\(c_m/16>0\),

\[
 \begin{aligned}
 Z_v(q_A)
 &>\frac{c_m\tau}{64}
   -\frac{c_m}{16}\frac{2\tau}{15}\\
 &=c_m\tau\left(\frac1{64}-\frac1{120}\right)\\
 &=c_m\tau\left(\frac{15}{960}-\frac8{960}\right)\\
 &=\frac{7c_m}{960}\tau.
 \end{aligned}
 \tag{4.7}
\]

Thus \(1/64=15/960\),
\((1/16)(2/15)=1/120=8/960\), and
\((15-8)/960=7/960\).  The final inequality is strict solely because B4.1 is
strict.  This proves the single conclusion (ASM2). \(\square\)

### Quantifier and scope check

The order used above is exactly

\[
 c_m\longrightarrow(b,\delta_{\rm rt})
 \longrightarrow\mathfrak d
 \longrightarrow\mathscr C^*
 \longrightarrow\text{arbitrary kernel and arbitrary display field}
 \longrightarrow B
 \longrightarrow(\rho,\mathfrak t_\phi,\mathfrak G_\phi)
 \longrightarrow\text{arbitrary attained }(\Lambda,c).
\]

Only after this order are \(C_B,w_*,\sigma_B\), and the single fixed level
\(V_{48}=\{z<48\tau\}\) formed.  None is optimized.  The proof uses signed
coefficients only through positive parts at the precise scopes displayed in
(2.9), (3.3), and (3.5); it uses clone-invariant full-fiber quantities, no
\(1/t^*\), no witness averaging, and exactly one common nonnegative test in
each of RX and O48.  It consumes no `lem-icap-*` shard, no
`lem-huddle-charge-assembly`, no `lem-intersection-branch-production`, no B5
quantity as \(\eta_D^*\), and no L3 numerical fixture.
It introduces no second web or recursive level split and does not use any
dead route recorded in `context/FINDINGS.md`.

No defect was found in S0, RX, O48, the ray identity, or the conditional ASM2
arithmetic.  RDSE and LDHR-48 remain hypotheses and are not proved here.
