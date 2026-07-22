# Closing Route 1: a mass-weighted primal absorption theorem

## Verdict and proposed theorem

The right target is a constant cap, and I believe the following deliberately conservative version is true.

**Proposed Primal Absorption Theorem (PAT).** Let \(P^2=P\), \(P\mathbf 1=\mathbf 1\), let every row have negative mass at most \(\delta\), put \(\tau=\sqrt\delta\), \(\rho=4\tau\), and \(\kappa=\tau/4\). If \(0<\delta\le 2^{-20}\), then:

1. \(W(P)\ne\varnothing\);
2. for every hidden top row vertex \(v\), with

   \[
   G=\{j:\operatorname {dist}_1(p_j,C_W)\ge \tau/4\},
   \qquad
   \widetilde\sigma_g(v)=\sum_{j\in G}P_{vj}^{+},
   \]

   one has the sharper estimate

   \[
   \boxed{\ \widetilde\sigma_g(v)\le \frac12+48\tau\ },
   \]

   and hence \(\widetilde\sigma_g(v)\le 3/4\).

This statement is **not proved below**. The reduction of PAT to one precise, primal, rank-free lemma is [NEW-ROUTINE]; that lemma itself is [NEW-HARD]. I isolate it explicitly rather than hiding the open content in “maximum principle” language. The gain over conj-kernel is that the hard lemma is a finite theorem of alternatives with a prescribed output—an affine functional—not another cap or another dual certificate.

Assuming PAT, the route closes with room. The af-validated halo-collapse inequality gives, with \(D=2+4\delta\) and \(\nu_v\le\delta\),

\[
H(1-\widetilde\sigma_g)
 \le (\widetilde\sigma-\widetilde\sigma_g)\frac{\tau}{4}+\nu_vD.
\]

Since \(\widetilde\sigma\le1+\nu_v\le1+\delta\) and \(1-\widetilde\sigma_g\ge1/4\),

\[
H\le (1+\delta)\tau+4\delta(2+4\delta)
 =\bigl(1+\delta+8\tau+16\tau\delta\bigr)\tau
 <\frac98\tau .
\]

Thus PAT implies the Kernel conclusion with \(B=9/8\). Together with the already proved \(\widetilde\sigma\le\tau\) branch, the registered bridge gives \(H\le3\tau\), then op-exposed-hull, then op-classical. [KNOWN-T0: halo collapse] [KNOWN-L5: kernel implies HLC] [KNOWN-mod-audit: the remaining trunk]

The theorem I would actually register first is the displayed \(1/2+48\tau\) estimate. The \(3/4\) cap and \(B=9/8\) are merely robust corollaries; no optimization should precede validation.

## 1. Work on the clone quotient from the first line

Let \(I\) be the validated **clone quotient**, not the coarser quotient obtained by indiscriminately merging every pair of coincident rows. For clone classes \(x,y\in I\), define

\[
\bar P_{xy}=\sum_{j:\,[j]=y}P_{ij},\qquad [i]=x.
\]

Row reproduction makes this independent of the representative \(i\). The quotient is again a unital signed idempotent and has negative-row mass no larger than \(\delta\). All masses below mean aggregate masses of clone classes. The distinction matters: merging arbitrary coincident rows could cancel a positive and a negative coefficient and would no longer represent \(\widetilde\sigma_g\). A genuine clone splits one coefficient proportionally, so its Jordan mass pushes forward without loss. [KNOWN-T0 as upstream quotient apparatus; it should be re-established as a formal shard before PAT is registered.] [RISK: if the upstream quotient does not include this Jordan-mass compatibility, work with the original indices and push the measures and currents forward only after taking positive parts.]

Write \(d(x,y)=\|p_x-p_y\|_1\). For a row \(x\), let

\[
\nu_x=\sum_y\bar P_{xy}^{-},\qquad
T_{xy}=\frac{\bar P_{xy}^{+}}{1+\nu_x}.
\]

Then \(T\) is a genuine stochastic kernel on the quotient and

\[
\|T_x-\bar P_x\|_1=2\nu_x\le2\delta . \tag{1}
\]

Consequently

\[
\|T^2-T\|_{\infty\to\infty}\le6\delta+4\delta^2. \tag{2}
\]

Equation (2) is the familiar row-normalization estimate, but here it is used only internally to construct a primal affine functional for the original exact projection. [KNOWN-T0/NEW-ROUTINE: (1) is one line; (2) is the validated signed-to-stochastic estimate.]

This quotient step is not cosmetic. Duplicating a state merely divides its raw coefficients while leaving \(\bar P,T,d\), and every measure used below unchanged. No minimum atom, path product, or number of quotient classes will occur.

## 2. The exact harmonic orientation and the positive carrier

Let \(C\) be either \(C_W\), or the empty set in the anchor-production argument. For \(C=C_W\), choose a top vertex \(v\), and choose a one-Lipschitz affine support functional \(\phi\) satisfying

\[
\phi(p_v)=H,\qquad \phi\le0\text{ on }C_W.
\]

Because \(v\) is top, \(\phi(p_x)\le d(p_x,C_W)\le H\). Define

\[
z_x=H-\phi(p_x).
\]

Then

\[
0\le z_x\le D:=2+4\delta,\qquad z_v=0,\qquad \bar Pz=z. \tag{3}
\]

The orientation in the prompt is therefore correct: the deficit, not the depth, is harmonic; the top is a **minimum** of \(z\). The equality in (3) is exact because \(z\) is affine on the row space. [KNOWN-T0: harmonic-affine bridge]

Put \(a=\bar P_v\), \(m=a^+\), and \(n=a^-\), treating \(m,n\) as positive row measures. Their masses are \(1+\nu_v\) and \(\nu_v\). Two identities are the real new starting point:

\[
m\bar P-m=n(\bar P-I), \tag{4}
\]

and

\[
mz=nz\le\nu_vD\le\delta D. \tag{5}
\]

Indeed, \(a=m-n\) and \(a\bar P=a\) give (4), while \(az=(\bar Pz)_v=z_v=0\) gives (5). Combining (1) and (4),

\[
\|mT-m\|_1
 \le \|m(T-\bar P)\|_1+\|n(\bar P-I)\|_1
 \le4\delta(1+\delta). \tag{6}
\]

Thus the **actual positive recipient measure of the top row** is \(O(\delta)\)-stationary for a canonical stochastic kernel. This is aggregate and clone invariant. It is stronger and safer than iterating signed row coefficients. [NEW-ROUTINE]

There is also an exact barycenter formula. If

\[
b_m=\frac1{1+\nu_v}\sum_xm_xp_x,
\]

then

\[
\|b_m-p_v\|_1
 =\frac1{1+\nu_v}\left\|\sum_xn_x(p_x-p_v)\right\|_1
 \le\frac{\nu_vD}{1+\nu_v}\le\delta D. \tag{7}
\]

This is the legitimate form of “use the recipients' barycenter.” All positive recipients together have barycenter \(O(\delta)\) from \(p_v\). Conditionalizing on \(G\), however, loses a factor equal to the mass outside \(G\); (7) alone cannot yield a constant cap. [NEW-ROUTINE] [RISK: any proof that silently applies (7) to the conditional \(G\)-barycenter has reintroduced the missing conclusion.]

Finally, (5) supplies the only valid top-deficit charging statement needed later:

\[
m\{x:z_x\ge r\tau\}\le \frac{D}{r}\tau . \tag{8}
\]

For \(r=16\), all but \(O(\tau)\) of \(m\) lies in the co-top band \(S=\{z<16\tau\}\).

## 3. What the harmonic maximum principle does—and does not—say

The tempting slogan “deep mass must eventually reach visible anchors” is not literally valid for \(\bar P\). Since \(\bar P^2=\bar P\), a second signed step gives exactly the first step, but positive and negative contributions may cancel. Iterating raw positive paths discards those cancellations and is precisely where cloning and one-sided-ledger failures enter.

The valid replacement is the triple

\[
\bar Pz=z,\qquad \|mT-m\|_1=O(\delta),\qquad \|T^2-T\|=O(\delta). \tag{9}
\]

It says: the positive top-row recipients form an almost stationary **measure**, their average deficit is \(O(\delta)\), and one stochastic step is already stationary up to \(O(\delta)\). Therefore a mass \(s>1/2\) in a set \(A\) has an excess-over-half overlap of size roughly \(2s-1\) with its own next generation. That excess cannot disappear by splitting it among many classes. It must either circulate tangentially inside the low-deficit carrier or cross a \(\rho\)-far cut. This is the quantitative version of the W30 “anchorless witness” observation.

But (9) alone does not prohibit a tangential cycle of many co-top classes. A maximum principle for \(z\) cannot see such a cycle because \(z\) is almost constant there. This is exactly why the old canonical-\(g\) energy and far-side-return arguments died. The missing ingredient must turn tangential circulation into an affine peak, not merely bound its scalar deficit. [RISK]

## 4. The single hard lemma: aggregate peak-or-leak

Here is the lemma on which PAT should be made to stand or fall.

**Aggregate Primal Absorption Lemma (APAL).** Let the quotient data \((\bar P,T,d)\) obey (1)–(2), let \(v,m,z\) obey (3)–(6), and let \(C\) be the convex hull of any collection of already \((\rho,\kappa)\)-visible row vertices. Set

\[
A_C=\{x:\operatorname {dist}_1(p_x,C)\ge\tau/4\};
\]

if \(C=\varnothing\), set \(A_C=I\). Then one of the following holds:

1. \(m(A_C)\le1/2+48\tau\); or
2. the procedure in the proof constructs a quotient row vertex \(u\in A_C\) and a vector \(f\) such that \(r=\bar Pf\) satisfies

   \[
   r_u=\max_xr_x,\qquad
   r_u-r_x\ge\kappa\bigl(\max r-\min r\bigr)
   \quad\text{whenever }d(u,x)\ge\rho. \tag{10}
   \]

APAL is [NEW-HARD]. Its conclusion is primal. If \(R=\max r-\min r>0\), define

\[
h(p_x)=\frac{r_u-r_x}{R}. \tag{11}
\]

Then \(h(p_u)=0\), \(0\le h\le1\) on every row, and \(h(p_x)\ge\kappa\) on every \(\rho\)-far row. Thus \(u\) is visible. No inference is made from a small dual optimum; (11) is the requested explicit admissible exposer. [NEW-ROUTINE once (10) is known]

The most promising proof of APAL is a single mass-weighted theorem of alternatives, not a recursion over recipient classes:

**Step A: discard vertical leakage.** By (8), replace \(m|_{A_C}\) by its restriction to \(A_C\cap S\), losing at most \(D\tau/16\). [KNOWN-T0/NEW-ROUTINE]

**Step B: form the self-overlap current.** Couple \(m|_{A_C\cap S}\) to its one-step image under \(T\). Because the total carrier mass exceeds \(1/2\) and (6) is \(O(\tau^2)\), max-flow/min-cut leaves an excess current of mass

\[
2m(A_C)-1-O(\tau)
\]

whose two marginals lie in the same aggregate carrier. Capacities are the measures \(m_x\) and \(m_xT_{xy}\), never individual lower bounds. [NEW-ROUTINE for the finite transport duality] [RISK: the exact \(48\) ledger must be checked, not guessed.]

**Step C: near current versus far current.** Split the current by the metric condition \(d(x,y)<\rho\), without splitting it by geometric class or wedge. A near current is retained as a measure; it is not followed along raw paths. A far current is measured by total transported mass, with \(\rho\) as its displacement scale. [NEW-ROUTINE]

**Step D: use one-step stationarity.** Compare the barycenter of the current before and after applying \(T\). Equations (2), (6), and (5) give only \(O(\delta)\) available error. The desired rank-free estimate is

\[
\rho\,\|\Gamma_{\mathrm{far}}\|
 \le C_0\bigl(\|T^2-T\|+\|mT-m\|_1+mz\bigr), \tag{12}
\]

after quotient-current cancellations are removed by the separating functional produced in Step E. Since the right side is \(O(\delta)\) and \(\rho=4\tau\), (12) prices far current by \(O(\tau)\). [NEW-HARD]

The qualification in (12) is essential: a vector-valued circulation can cancel its own barycentric displacement. A naked inequality (12) for arbitrary currents is false. What must be proved is the **exchange-or-expose** form: either the cancellations can be exchanged into near current without changing the marginals, or a Farkas separator detects the uncancelled current and is the \(r=\bar Pf\) of (10). This is the exact hard core.

**Step E: convert failed exchange to a primal peak.** Solve the global near-exchange LP. Its variables are the whole coupling, with source capacities \(m\) and actual transition capacities \(m_xT_{xy}\). If all far current can be exchanged into near current, (2) forces it into one-step-stationary \(\rho\)-clusters; the halo condition then absorbs any cluster meeting \(C\). If exchange fails, the Farkas dual is a scalar potential on quotient rows. Project that potential by \(\bar P\), use the \(O(\delta)\) slack from (2), (5), and (6), and normalize it. The quantitative claim is that an excess current greater than \(48\tau\) leaves the strict ratio in (10). [NEW-HARD]

This last ratio preservation—not transport duality—is where proof effort belongs. It is also a clean falsification point: if projection by \(\bar P\) can flatten every separating potential while all three errors in (9) remain \(O(\delta)\), APAL is false. [RISK]

**Step F: circuit-ratio verification.** Let \((\lambda,\alpha,\beta)\) be any validated hiddenness witness at the produced \(u\): \(\lambda\) is a probability on the \(\rho\)-far set, \(\alpha\ge0\), \(\beta\ge0\), and \(\sum\beta=t^*(u)<\kappa\). Apply the explicit \(h\) from (11) to the witness balance. The left side is at least \(\kappa\) because the \(\lambda\)-mass is one and \(h\ge\kappa\) on its support; the \(\alpha\)-term is nonnegative. The right side is at most \(\sum\beta<\kappa\), because \(0\le h\le1\). Contradiction. [KNOWN-T0: witness balance and small beta] [NEW-ROUTINE]

Step F shows exactly why the theorem is about the ratio of affine-circuit coefficients. Raw recipient mass merely creates the aggregate current. Visibility comes only after the current yields a normalized affine gap whose unit far coefficient beats the \(<\kappa\) beta coefficient.

## 5. Deriving PAT from APAL

**Anchor production.** Suppose \(W=\varnothing\). Choose any row vertex \(v\) and any affine support functional maximized at \(v\); after subtracting its maximum, it gives a nonnegative harmonic deficit \(z\) with \(z_v=0\). Take \(C=\varnothing\), so \(A_C=I\). Then \(m(A_C)=1+\nu_v\), which is larger than \(1/2+48\tau\). APAL produces a visible vertex, contradicting \(W=\varnothing\). [NEW-ROUTINE conditional on APAL]

**The sigma cap.** Now \(C=C_W\), and let \(v\) be a hidden top vertex. Put

\[
G=A_C=\{x:d(p_x,C_W)\ge\tau/4\}.
\]

No visible vertex lies in \(G\), since every visible row belongs to \(C_W\). Therefore APAL's second alternative is impossible, and

\[
\widetilde\sigma_g(v)=m(G)\le\frac12+48\tau.
\]

At \(\tau\le2^{-10}\), this is \(<3/4\). The collapse calculation at the beginning gives \(H<9\tau/8\). [NEW-ROUTINE conditional on APAL]

Notice that APAL does not assume \(v\) ships its mass to a single cluster. It converts excess aggregate carrier mass into one visible peak after allowing arbitrary splitting and cancellation. This is precisely the genuinely multi-class case not tested by the old duplicate-splitting experiments.

## 6. The two-sided ledger: the proposed lower side in the prompt is false

The exact charging identity is

\[
\sum_xa_x^+z_x=\sum_xa_x^-z_x\le\nu_vD. \tag{13}
\]

It is tempting to assert \(z_x\gtrsim\tau\) for every halo-far recipient. That assertion is false: \(d(p_x,C_W)\ge\tau/4\) is a statement about distance from the anchor hull, whereas \(z_x=H-\phi(p_x)\) measures loss in one chosen top-support direction. A point can be genuinely outside and still lie on the same top supporting face, giving \(z_x=0\). The W54 convex re-entry phenomenon is exactly this geometry.

Therefore (13) does **not** imply \(\nu_v\gtrsim\tau\widetilde\sigma_g\). What it does imply is the high-deficit estimate (8). The correct two-sided ledger is:

- vertical side: high \(z\) mass costs \(\nu_v\) by (13); [KNOWN-T0]
- tangential side: low-\(z\), far, almost-stationary mass must be exchanged into near flow or pay the \(T^2-T\) defect; failed exchange constructs (11). [NEW-HARD]

This checks the direction of financing. The upper charge does not magically become a lower charge. APAL supplies a different lower mechanism—far-current displacement versus one-step stationarity—and its escape branch is the primal exposer.

## 7. Why Kernel went dormant, and why this is not a renamed dead route

The dossier records obs-deep-leakage and obs-fwr-gap only as heuristic observations, not with formal contracts. The surrounding death certificates make the reason for abandonment unambiguous.

The **\(v\)-local family** tried to read a lower bound from the top row alone: pointwise sigma selectors, a canonical-\(g\) energy, raw path products, or a self-cluster residual ledger. It died because a \(1-O(\tau)\) near cluster can satisfy every local scalar identity and pay height through \(\nu/(1-S)\); raw path floors are also destroyed by cloning. W37/38 is the decisive certificate.

The **web-rigidity family** tried to propagate hiddenness witnesses through neighboring rows: transfer \(t^*\), recur on far partners, or interpret conic multipliers as transition mass. It died because exposedness is value-normalized rather than Lipschitz in the center, alpha gauge can blow up, and dual multipliers are not transition weights. W39, W40, W42, W54–W56 close that family.

APAL is different in three checkable ways. First, its carrier is the aggregate positive measure \(m=P_v^+\), and (4)–(6) use \(P^2=P\) globally; it is not a scalar fact at \(v\). Second, it transports only the actual stochastic weights \(m_xT_{xy}\); \(\lambda,\alpha,\beta\) are never treated as dynamics. Third, its success output is the exact primal function (11), not a small dual value or a claim of whole-face membership.

The danger is equally clear. Step E may fail because a high-rank tangential circulation survives every near exchange while flattening all projected separators. If so, APAL collapses back onto the old bridge gap. That is why Step E is tagged [NEW-HARD], not [NEW-ROUTINE]. The route is new in formulation and falsifiability, not yet in theorem status.

## 8. Explicit six-wall audit

1. **Cloning.** Every state is first aggregated to its distinct-row quotient. \(m,T,z,d\), transport capacities, and objective values are invariant under duplicating a state. No raw index floor appears. **Pass**, conditional only on formally revalidating the quotient shard.

2. **Class count / anti-splitting.** APAL uses one measure and one global coupling. Errors are charged per unit transported mass and integrated once; there is no sum of a fixed loss over classes, wedges, or blocks. **Pass by design.** [RISK: a proof of Step E that peels clusters and pays a fixed error per peel would fail this wall.]

3. **Exposedness absorption / halo.** The conclusion is the coefficient-ratio statement (10), normalized to the exposer (11). The halo \(d(\cdot,C_W)\ge\tau/4\) excludes self-mass and gives absorption when a produced vertex enters \(W\). Raw mass is only the antecedent. **Pass.**

4. **Dual direction.** The algorithm outputs \(f\), \(r=\bar Pf\), and \(h\). The dual witness is used afterward only to verify the strict \(\kappa\) contradiction. **Pass if Step E is proved.** This is the principal advantage over all previous formulations.

5. **Whole-optimal-face promotion.** No near-optimal dual value is promoted to membership. The returned \(h\) is exactly feasible on all rows and has an exact far gap. **Pass in the statement.** [RISK: deriving \(h\) by taking a limit of near separators without preserving exact feasibility would re-enter this wall.]

6. **One-sided ledger.** Equation (13) is used only in its valid direction. The missing direction is explicitly (12) plus the exchange-or-expose alternative, not a relabeling of (13). **Pass in architecture; Step D/E is the sole new burden.**

## 9. Certified pathology checks

**The \(5343/5000\) self-mass example.** Its offending mass sits only \(0.02\tau\) from \(C_W\). It is outside neither \(G\) nor \(A_C\), whose halo radius is \(\tau/4\). PAT makes no claim about the naive invisible mass and is therefore consistent. This example is the reason the halo cannot be shrunk to zero.

**The \(100/49\) hull dip.** PAT does not assert \(H\le2\delta\), nor any linear law. It gives \(H=O(\tau)\), so a finite instance with \(H/\delta=100/49\) is harmless; as \(\delta\to0\), \(H/\tau\to0\) on that family anyway.

**The corner lower bound \(B\ge2(2-\sqrt3)\).** The proposed \(B=9/8\) is larger than \(2(2-\sqrt3)\approx0.536\). There is no constants conflict.

**Alpha blow-up and \(t^*\to0\).** APAL never divides by \(t^*\) and never bounds alpha. It constructs a function with gap at least the fixed \(\kappa\), after which the small-beta witness is contradictory regardless of alpha.

**The \(\delta=0\) endpoint.** PAT is stated for \(0<\delta\). At \(\delta=0\), the exact stochastic-idempotent normal form supplies the visible recurrent rows; the non-strict exposedness convention handles the endpoint separately.

## 10. Decisive first test

The one-day test should attack Step E, not run another undirected zoo census.

Implement an exact **multi-class aggregate-peak decider** on quotient data:

1. Generate factorized rational idempotents \(P=LB\), \(BL=I\), at ranks \(4\) and \(5\), with at least three pairwise non-clone recipient classes. Optimize the exact objective \(\widetilde\sigma_g(v)\), rather than height alone.
2. For every candidate, compute \(W,C_W,v,z,m,T\) exactly. Reject any record whose “large mass” is inside the \(\tau/4\) halo.
3. Build the single near-exchange max-flow using capacities \(m_xT_{xy}\), low-deficit set \(z<16\tau\), and near relation \(d(x,y)<4\tau\).
4. If the flow cannot absorb the excess \(2m(A_C)-1\), extract its exact rational Farkas potential, project it by \(\bar P\), and test (10) directly.
5. If the flow does absorb the excess, measure whether applying \(T\) a second time violates the proposed \(O(\delta)\) far-current price. Store the exact violating cut/current, not a floating ratio.

There are three decisive outcomes. An exact instance with \(m(A_C)>1/2+48\tau\) and no peak (10) refutes APAL and this route. A family in which the required constant grows with genuine rank identifies a new anti-splitting failure. Conversely, if every high-objective relaxation is forced either into the halo or into an exact peak, the Farkas certificates reveal the missing algebraic inequality for Step E. This directly probes the one untouched empirical residual—geometrically distinct multi-class outsourcing—and cannot be passed merely because duplicate splitting is clone invariant.

In parallel, the one-day formal lemma worth registering is (4)–(8), under the name **positive-recipient carrier lemma**. It is elementary, exact, and narrows all future Kernel work to APAL. If an attempted proof of absorption does not use the \(O(\delta)\)-stationarity of \(P_v^+\), or an equivalent global invariant, it is almost certainly walking one of the dead local routes again.

## Bottom line

The harmonic deficit is useful only to squeeze massive outsourcing into a common co-top slab. It cannot charge genuinely outside mass from below. The missing theorem is tangential: more than half of the positive recipient measure is an almost stationary carrier, and exact one-step stationarity must turn its uncancellable far circulation into a normalized affine peak. The appropriate registered conjecture is APAL, with its explicit exposer output (10)–(11). Prove that one lemma and Route 1 closes with the conservative cap \(\widetilde\sigma_g\le3/4\), \(B=9/8\), and no dependence on dimension or class count.
