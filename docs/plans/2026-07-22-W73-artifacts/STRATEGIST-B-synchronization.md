# Mechanism-design memo: the conserved current is aggregate, and the battle belongs at L5

## 0. Verdict

The selected-root weight $w_*$ dilutes because it is not a charge. It is the smallest coordinate created by a proof-dependent disintegration. Exact idempotence controls signed barycentres and aggregate moments; it does not control the least atom of an arbitrarily fine genuine quotient decomposition. Thus no refinement of the W72 estimate

\[
\sigma_B\geq w_*M_B-e_\delta,
\qquad e_\delta=2\delta(1+\delta),
\]

can become rank-uniform while its left side remains outside the objective measure $m_A$. A lower bound on $w_*$ would be an anti-splitting theorem in disguise.

There is also no unconditional, scalar, order-one energy forced by \(P^2=P\). The identity matrix already rules out most such claims. What idempotence does conserve is an operator-valued reproduction law: on every transverse coordinate belonging to the range of \(P\), the total reproduced moment is exactly one. The starvation obstruction is precisely a normalized instance of this law. Its dilution-proof scalarization is not a minimum atom and not a quadratic energy, but the total variation of an aggregate quotient current. Under the tall-huddle hypotheses this current has size \(\asymp 1\) before rescaling, hence \(\asymp\tau\) after the tail amplification. It must have one of two destinations:

1. it enters the global top-deficit charge
   \[
   \mathsf Q_v(\phi):=\sum_x \overline P_{vx}^{+}z_x^\phi
   =\sum_x\overline P_{vx}^{-}z_x^\phi
   \leq (2+4\delta)\delta,
   \]
   where \(z_x^\phi=H-\phi(p_x)\); or
2. failure of such transport gives, by a global separation/minimax argument, a **primal exposer** of \(v\).

That is the synchronization mechanism. Its hard core is an exchange-or-expose theorem for an aggregate affine-circuit current. The right place to prove it is **conj-l5-gap-1, before the S/C/I split**. POTI-0 is too low: it has already discarded the common exposedness alternative, separated the finance measure from $m_A$, and replaced an aggregate current by a selected atom. The huddle level is viable but unnecessarily broad; conj-kernel is broader still and lacks the actorized unit-moment input.

The absence of an unconditional scalar can also be seen from direct sums. Exact stochastic idempotents may have arbitrarily many recurrent blocks. Direct sum preserves \(P^2=P\), while a normalized additive scalar averages the block charges and an unnormalized one grows with rank. Neither can be the desired universal order-one obstruction. The only canonical order-one identity is \(P|_{\operatorname{ran}P}=I\), or \(BL=I\) in factorized coordinates. A scalar charge appears only after the tall configuration selects a normalized transverse demand. This is why a proposed invariant must be conditional on the huddle/actor package, yet aggregate over every root in that package.

## 1. Why $w_*$-dilution is a real escape, not a missing estimate

Pass at once to the clone quotient $\mathcal X$. For clone classes $x,y\in\mathcal X$, put

\[
\overline P_{xy}:=\sum_{j\in y}P_{ij},\qquad i\in x.
\]

The row reproduction identity makes this independent of the representative. The quotient satisfies $\overline P^2=\overline P$, $\overline P\mathbf 1=\mathbf1$, and $\delta(\overline P)\leq\delta(P)$. Thus quotienting kills literal cloning, but it does not bound the number of geometrically distinct classes. W69 is exactly the warning: genuine rank can grow while every local finance negativity is zero.

In RDSE, $w_*$ is produced only after choosing a corner/root and disintegrating a local package. Schematically, if the root measure is

\[
\mu=\sum_{r\in\mathcal R}w_r\delta_r,
\qquad \sum_r w_r=M,
\]

then \(w_*=\min_{r\in\operatorname{supp}\mu}w_r\), or a comparable selected coordinate. The invariant datum is \(M\), not \(w_*\). Replacing one relevant geometric root by \(N\) genuinely distinct roots with the same aggregate barycentric effect preserves all affine identities while permitting \(w_*\leq M/N\). No cloning is needed. Any proposed universal \(w_*\geq c\) therefore implies \(N\leq M/c\), precisely the forbidden class-count conclusion.

The more serious defect is the measure mismatch. RX proves that a local tableau demands slack $\sigma_B$, but $\sigma_B$ is carried by finance rows measured by $\eta_D^*$, whereas RAY-EC is measured by $m_A$. A lower bound on the former is not a lower bound on the latter. Summing the local inequalities gives

\[
\sum_r\sigma_B(r)\geq M_B\sum_r w_r-N e_\delta,
\]

which either accumulates an $N\delta$ error or counts the same reusable payer several times. Taking a minimum avoids double counting but introduces $w_*$. This is the exact local/global fork: summation hits anti-splitting; selection hits dilution. The foldback lemma prevents some reuse, but one application does not change the marginal measure of the slack. A new statement must synchronize the two marginals, not improve either pointwise estimate.

The W71 law $\max_i\nu(P_i)=\beta a$ should be read in this way. In that family, $\beta$ is the total current through a root cut. Ownership asks for $\beta\geq1/8$, while the negativity capacity of the cut is $\beta\leq\tau^2/a$. The important object is the **cut current** $\beta$, not the family-specific formula. A class-wide proof should turn this into a max-flow/min-cut alternative: either an order-$\tau$ aggregate current reaches the top-owned side, or the obstructing cut is an exposer.

## 2. Audit of the proposed conserved quantities

### 2.1 The starvation unit transverse moment

This is the correct source charge, with one qualification. In an actorized tableau choose the transverse covector $\ell_u$ in the banked normalization. The identity $P^2=P$, equivalently $P=LB$ and $BL=I$, gives a relation of the form

\[
\sum_x c_{ux}\,\ell_u(p_x-p_u)=1.
\tag{2.1}
\]

The right side is not $O(\tau)$: it is one. This is why the starvation lemma can compare unit demand with $O(\tau)$ interior supply. Splitting a coefficient among several quotient roots does not alter the sum in (2.1). After weighting all tableaux by a positive root measure $\mu$, the total demand is $\mu(\mathcal R)$, not $\min_r\mu(r)$.

The qualification is orientation. The covectors \(\ell_u\) vary with \(u\). If one simply adds the signed scalar moments, rotating tableaux can cancel. If one keeps a separate coordinate for every root, the resulting direct-sum norm reimports class count and has no reason to be financed by the max-row negativity \(\delta\). The proper aggregate is therefore an \(\ell^1\)-type **current of affine-circuit coefficients**, minimized over all global routings. Total variation does not decrease when a path is subdivided, unlike a squared energy. But showing that this current has a common top-facing component, or else yields an exposer, is the new theorem—not a consequence already contained in the local starvation lemma.

### 2.2 The top-deficit charge

Let $\phi$ be a top supporting functional, normalized by

\[
\phi(p_v)=H,\qquad \phi\leq0\text{ on }C_W,
\qquad \operatorname{Lip}_1(\phi)\leq1,
\]

and set \(z_x=H-\phi(p_x)\). Affine row reproduction gives \(z=\overline Pz\), with \(z_v=0\) and \(0\leq z_x\leq D_0:=2+4\delta\). Hence

\[
0=\sum_x\overline P_{vx}z_x
=\sum_x\overline P_{vx}^+z_x-
  \sum_x\overline P_{vx}^-z_x,
\]

so

\[
\mathsf Q_v(\phi):=
\sum_x\overline P_{vx}^+z_x
=\sum_x\overline P_{vx}^-z_x
\leq D_0\nu_v\leq D_0\delta.
\tag{2.2}
\]

This is exactly clone-invariant and immune to rank growth. It is, however, an order-\(\delta\) **budget**, not an order-one source. Its role is to make an order-\(\tau\) synchronized current impossible. Conj-l5-gap-1 is already in the correct currency: it asks that some \(\phi\) put \(\Omega(\tau)\) of this charge on \(A\). The missing implication is from the family of local unit moments to this single aggregate charge.

### 2.3 Harmonic Dirichlet energy

For $z=\overline Pz$, the formal carré du champ is

\[
\mathcal E_x(z):=\frac12\sum_y\overline P_{xy}(z_y-z_x)^2
=\frac12\bigl(\overline P(z^2)_x-z_x^2\bigr),
\qquad \overline P\mathcal E(z)=0.
\tag{2.3}
\]

This looks conserved, but it is signed. There is no canonical positive stationary measure with which to integrate it, and the negative coefficients can pay its positive part. At the top row, $z_v=0$ and $0\leq z\leq D_0$ give only

\[
\sum_y\overline P_{vy}^+z_y^2
\leq D_0\sum_y\overline P_{vy}^+z_y
\leq D_0^2\delta.
\]

Thus this energy is another upper budget. Worse, a height change distributed over a long quotient chain has squared energy tending to zero in the absence of a rank-uniform Poincaré inequality. No such inequality is available, and importing one would be the class-count/spectral-gap wall in analytic clothing. The useful replacement is $L^1$ current or total variation: serial subdivision preserves total path length.

### 2.4 Exposedness margin $t^*$

The number $t^*(v)$ is clone-invariant, but it is not conserved and has no positive lower scale. The W54 discipline explicitly permits $t^*\downarrow0$. Moreover, the hiddenness dual only proves upper bounds on $t^*$; it cannot be reversed. What is useful is the **primal polytope**

\[
\mathcal H_v:=\{h:\ h\text{ affine},\ h(p_v)=0,
\ 0\leq h(p_x)\leq1\ \forall x\},
\]

for which

\[
t^*(v)=\max_{h\in\mathcal H_v}\min_{f\in F_v}h(p_f)
=\min_{\lambda\in\Delta(F_v)}
  \max_{h\in\mathcal H_v}\sum_f\lambda_fh(p_f).
\tag{2.4}
\]

The second equality is finite-dimensional minimax. It supplies the correct anti-cancellation device: to construct one exposer it is enough to defeat every probability $\lambda$ on far rows by an aggregate, not class-by-class, estimate.

The conclusion of this audit is sharp. There is no standalone scalar conserved charge. The source is the normalized transverse $L^1$ current; the sink is the harmonic top-deficit budget; and failure to connect source to sink must be converted into a primal exposer through (2.4).

## 3. Proposed synchronization theorem

Call \(\mathfrak D\) an **admissible pre-split L5 datum** if it is the datum of conj-l5-gap-1 before the S/C/I decomposition: it contains an exact signed idempotent \(P\), a hidden top vertex \(v\) with \(H>16\tau\), the quotient row space, the top-owned measure \(m_A\) of total mass \(S\geq s_0>0\), the actor set \(A\), owned barycentre \(q_A\), the sets \(E_*,L_v\), and the actorized tableaux supplied by the W62–W67 engine. In particular the banked estimates include the exterior-payer/tail floor and \(P_v^+(L_v)<2\tau/15\). Let \(\Phi_v\) be the compact set of normalized top supporting functionals, and define

\[
\mathsf Q_A^*:=\sup_{\phi\in\Phi_v}
\sum_{x\in A}\overline P_{vx}^+
\bigl(H-\phi(p_x)\bigr).
\]

**Root-to-top synchronization theorem (RTS).** [NEW-HARD] There are universal $\varepsilon_{\rm syn}>0$, $C_{\rm syn}<\infty$, $s_0>0$, and $\tau_0>0$ such that every admissible pre-split L5 datum with $\tau\leq\tau_0$ satisfies

\[
t^*(v)+\frac{C_{\rm syn}}{S}
\left(\mathsf Q_A^*+\delta+
      \tau P_v^+(L_v)\right)
\geq \left(\frac14+\varepsilon_{\rm syn}\right)\tau.
\tag{RTS}
\]

Equivalently, after reducing $\tau_0$ if necessary, one has the alternative

\[
\boxed{
\quad t^*(v)\geq\frac\tau4
\quad\text{or}\quad
\exists\phi\in\Phi_v:\
\sum_{x\in A}\overline P_{vx}^+z_x^\phi
\geq c_{\rm syn}S\tau.
\quad}
\tag{3.1}
\]

Here $c_{\rm syn}>0$ is universal. The constants are not cosmetic: the proof must retain a strict margin above (1/4). Any qualitative $c\tau$ exposer bound with $c\leq1/4$ is useless for the present definition of visibility.

If \(v\) is hidden, the first branch of (3.1) is impossible. The second branch is conj-l5-gap-1 after choosing \(c_5<c_{\rm syn}s_0/c_m\). It also immediately conflicts with (2.2) when \(\tau\) is sufficiently small. Most importantly, RTS contains no selected root, no sum of per-class errors, and no class-count parameter.

## 4. Proof architecture, with the hard core exposed

**Step 1: quotient before choosing anything.** [KNOWN-mod-audit] The quotient identities $\overline P^2=\overline P$, $\delta(\overline P)\leq\delta(P)$, and descent of harmonic affine deficits are available upstream. [NEW-ROUTINE] They should be re-established as registered shards and all L5 measures pushed to $\mathcal X$. No representative or raw index may occur later.

**Step 2: replace a selected root by an adversarial distribution.** [NEW-ROUTINE] Fix an arbitrary \(\lambda\in\Delta(F_v)\), as in (2.4), and retain the entire \(m_A\)-root measure; do not select an atom. [NEW-HARD] Prove a **uniform actorization-or-exposure sublemma**: either the actor disintegration can be coupled to \(m_A\otimes\lambda\) with only the registered \(O(\delta)+\tau P_v^+(L_v)\) loss, or the uncoupled part already supplies the charge/exposer term in (4.2). This compatibility is not furnished by the existing per-instance actorization. Conditional on the first branch, integrating the local starvation identities is routine: their normalized right sides add to \(S\), whereas weighted negative-part subadditivity gives

\[
\int\nu_u\,dm_A(u)\leq \delta S
\]

after normalization. This uses weighted negative-part subadditivity, not a sum over roots. No $w_*$ appears.

**Step 3: build the quotient transverse current.** [KNOWN-T0] Each actorized tableau has unit transverse moment and the robust scalar-starvation/forced-exterior-coupling conclusion. [NEW-ROUTINE] Encode all tableaux as a single finite signed current $J_\lambda$ on affine circuits of the quotient. Its norm is the minimum total variation of circuit coefficients over routings with the prescribed source marginal $m_A$. Because this is an $L^1$ norm, splitting a circuit or inserting intermediate quotient roots cannot reduce its required total transverse variation. The tail floor rescales the unit demand to

\[
\|J_\lambda\|_{\rm tr}\geq c_0S\tau.
\tag{4.1}
\]

[RISK] The norm must be defined by coefficient ratios relative to negative anchors and far positive support, not by raw transported mass or Euclidean distance. Otherwise the $\rho$-halo absorption counterexamples invalidate (4.1).

**Step 4: compress reuse by idempotence.** [KNOWN-L5] Positive-flow foldback, the universal-exterior-payer lemma, and the top-face-ray formula apply to each admissible datum. [NEW-ROUTINE] Apply foldback once to the aggregate current, not separately to its root fibers; algebraically this is the associativity \(m_A\overline P^2=(m_A\overline P)\overline P\). This prevents a finance row from being counted once for every root. [NEW-HARD] Identifying the compressed current's finance marginal with the top-owned ray objective \(R_A(\Lambda,c)\), rather than merely with exterior slack, is exactly the marginal-exchange clause of Step 5; it is not a consequence of foldback alone.

**Step 5: prove the exchange-or-expose lemma.** [NEW-HARD] This is the genuine new mathematics. For every $\lambda\in\Delta(F_v)$, prove

\[
c_0S\tau\leq C_0\left(
\mathsf Q_A^*+\delta+\tau P_v^+(L_v)
+S\max_{h\in\mathcal H_v}
      \sum_f\lambda_fh(p_f)
\right),
\tag{4.2}
\]

with $c_0/C_0>1/4$. The meaning is exact: every unit of transverse current is either exchanged into a top-owned deficit, paid by the global negative budget, lost in the registered low-tail spend, or blocked by a cut represented by a primal affine exposer.

The proposed route to (4.2) is a single global linear program. Its primal variables are a circuit-coefficient transport plan $\Gamma(x,y)$ whose source marginal is dominated by $m_A$ and whose finance marginal is the current exterior-payer measure. Constraints impose the aggregate moment identity, not one constraint per wedge. The cost records top deficit. If a feasible plan carries the current, its cost gives the first three terms on the right of (4.2). If it does not, Farkas separation gives one affine functional $h_{\lambda}$. The normalization constraints of the transport LP must force $h_\lambda(p_v)=0$, $0\leq h_\lambda\leq1$ on all quotient rows, while the unsent $\lambda$-current forces a lower $\lambda$-average on $F_v$. This is a **primal exposer construction**; no upper bound on hiddenness is run backward.

**Step 6: use the whole optimal face.** [NEW-HARD] The transport cone in Step 5 must be defined using \(Z(v)\), the rows tight on the entire optimal exposer face, and by intersecting the circuit constraints over that whole face. The necessary polar identity is schematically

\[
(\text{globally routable circuit-current cone})^\circ
=\mathcal H_v+\text{registered error polars}.
\tag{4.3}
\]

This is where the tightness-promotion wall actually lives. A proof for one chosen $h^*$, or for a near-optimal dual value, does not establish (4.3). [RISK] Farkas may initially produce an affine separator with the wrong box normalization or with a floor only on an average subset of $F_v$. Repairing that separator without losing the strict (1/4) margin is likely the hardest sublemma. If this repair fails, RTS as stated is false; the failure certificate should identify the missing exposedness structure rather than spawn another local ledger.

**Step 7: eliminate orientation cancellation by minimax.** [NEW-ROUTINE] Take the infimum of (4.2) over $\lambda\in\Delta(F_v)$. Equation (2.4) converts the last term exactly to $St^*(v)$. There is no choice of a favorable root and no union bound. Rearrangement yields RTS, with $\varepsilon_{\rm syn}=c_0/C_0-1/4$.

**Step 8: close the ledger in the correct direction.** [KNOWN-T0] Harmonicity gives $\mathsf Q_A^*\leq D_0\delta$. [KNOWN-L5] The tail estimate gives $P_v^+(L_v)<2\tau/15$. [NEW-ROUTINE] Since $S\geq s_0$, all error terms in RTS are $O(\tau^2)$, so for $\tau\leq\tau_0$ they are smaller than $\varepsilon_{\rm syn}\tau$. Thus hiddenness forces the charge branch, giving L5-GAP-1, and the global deficit budget then contradicts tallness.

### Decisive falsification tests

**Quotient-refinement test.** [NEW-ROUTINE] Evaluate the proposed current norm on every rank in the W69 family. Its source mass and normalized transverse variation must stay bounded below while \(w_*\to0\). If the norm decays with the least root weight, its definition has merely renamed RDSE and must be rejected.

**Cross-financing test.** [RISK] Build the smallest two-root tableau in which each root is paid entirely by the other root's finance marginal, so both local ledgers are free and neither payer is initially \(m_A\)-owned. The aggregate LP must count the resulting cycle only once. It must then either exchange the cycle into top deficit or return a normalized exposer. If it admits a zero-cost circulation with no exposing separator, (4.2) is false and the missing invariant needs an additional ownership constraint available above L5.

**Rotating-huddle test.** [RISK] Use the anticipated LDHR-48 obstruction, with local transverse directions rotating while all carrier tails remain in \(V_{48}\). A selected direction should see vanishing moment, but the minimax value in (2.4) should not. Failure here would show that the full exposer polytope still does not control orientation cancellation and would force retreat to the huddle level for extra co-top structure.

**Endpoint test.** [KNOWN-T0] At \(\delta=0\), the top-deficit budget vanishes. RTS must reduce to production of a primal exposer, consistently with the exact stochastic-idempotent normal form. Any definition of the current involving division by \(t^*\), a selected coefficient, or \(\delta\) fails this test.

## 5. Audit against the six walls

1. **Cloning.** [NEW-ROUTINE] Every measure, current, and LP variable lives on $\mathcal X$. Subdivision changes a representation but not total current or its marginals.

2. **Anti-splitting.** [NEW-HARD] RTS makes one aggregate transport problem and quantifies over one probability $\lambda$. It never proves a cap for each root and then sums. Any attempted proof of (4.2) by classifying the support of $\lambda$ would forfeit this advantage.

3. **Absorption/halo.** [NEW-HARD] Capacity is measured by affine-circuit coefficient ratios. Infeasible transport returns an exposer, so absorption is a success branch rather than an exemption. Raw mass capacities are prohibited.

4. **Dual direction.** [NEW-HARD] The separator is constructed as a primal $h\in\mathcal H_v$, followed by minimax. The hiddenness dual may diagnose the worst $\lambda$, but it is not used to infer a lower bound on $t^*$.

5. **Whole optimal face.** [NEW-HARD] Identity (4.3), not near-optimality, is the central lemma. This hard content is explicit and cannot be hidden in "LP stability."

6. **One-sided ledger.** [KNOWN-T0] RX and starvation only lower-bound required exterior finance. [NEW-HARD] Step 5 is the additional exchange theorem that either moves that finance into the objective marginal or produces an exposer. Without Step 5, the direction needed for RAY-EC does not follow.

## 6. Where the decomposition lost the needed structure

**At L5-GAP-1.** This is the last level at which \(v\), the full top-row positive measure, the choice of \(\phi\), the owned barycentre \(q_A\), the actor measure, and the entire exposedness polytope coexist. The desired conclusion is already an aggregate, clone-invariant deficit charge. The W62 ray/foldback machinery supplies enough local structure to define the current, while no root has yet been privileged. This is the optimal altitude.

**After the S/C/I split.** The proof freezes a geometric cell. That is useful for local actorization, but it fragments a single global alternative into cases. A current that moves between S, C, and I can be invisible inside every separate ledger. More importantly, the minimax variable $\lambda$ should be allowed to range over all far rows at once; conditioning it on a cell weakens the primal exposer alternative.

**At I-cap and D-cap.** Selected corners, diagonal/off-diagonal status, and local gauges enter. The unit transverse moment becomes visible here, but its orientation is local. This is exactly where an $L^2$ or selected-direction argument begins to cancel. The decomposition retains the source charge but starts losing the common affine dual in which it must be synchronized.

**At A-esc/HES/DTR.** Actorization and the synthetic finance rows make starvation rank/slab-free—a real gain—but payer ownership is no longer automatic. The local tableau says that someone must pay; it no longer says that the payer is seen by $m_A$. Thus the one-sided ledger becomes structural rather than technical.

**At POTI and especially POTI-0.** The loss is fatal for the proposed mechanism. Conditioning on $G_\phi=0$ or $r=0$ discards the positive-overlap current that a global exchange would use. RDSE then selects a root and obtains $w_*$, while $\sigma_B$ lives off the objective marginal. LDHR-48 fixes a deficit level but allows the top-face direction to rotate, precisely the cancellation that the full minimax over $\mathcal H_v$ should absorb. POTI-0 is therefore not a natural theorem; it is the residue left after the global alternative has been conditioned away.

**At the huddle-charge level.** More exposedness and cluster structure are present, including the heavy near cluster and co-top web. But the normalized transverse current has not yet been extracted, and a synchronization theorem there would entangle SL1a, SL1b, L6.5, and L5 in one statement. If the polar identity (4.3) needs extra geometric hypotheses, the huddle level is the correct place to import them; it is not the first place to formulate RTS.

**At conj-kernel.** This altitude has maximal global structure but minimal mechanism. It includes $W\neq\varnothing$, hidden mass, and the complementary $\widetilde\sigma_v>\tau$ branch, but it has neither a heavy actor measure nor a normalized tableau. A direct exchange-or-expose theorem there would be more beautiful, and exposedness absorption strongly suggests it is true, but it would have to discover both the current and its sink simultaneously. That is a strictly larger problem than RTS.

## 7. Recommendation

Move the decisive battle to **L5-GAP-1, before S/C/I**, and suspend RDSE/LDHR-48 as proof targets. Retain their exact families as tests for the aggregate transport LP: a correct RTS current should remain $\Omega(\tau)$ on W69/W71 even as $w_*\to0$, and the failed transport should reproduce the observed ownership/exposedness cut.

The next theorem should not claim that every local payer is top-owned. It should claim the global alternative (RTS): aggregate coefficient-ratio current either reaches top-deficit charge or constructs a primal exposer. That formulation explains both sides of the eighteen-wave record. Proof attempts fail locally because local finance is free; counterexamples fail globally because the only way to keep finance disjoint from top ownership is to create the cut that makes the top visible. The conserved object is the total transverse current, while exposedness is its min-cut certificate.
