# Part 1 — `conj-l5-gap-1`

```yaml
---
id: conj-l5-gap-1
kind: conjecture
contract: >-
  There exists a universal c_5 > 0 such that, for every fixed universal c_m > 0, there exists a universal delta_5 = delta_5(c_m) > 0 for which the following holds: whenever P is an exact signed idempotent with 0 < delta(P) <= delta_5 and nonempty visible set W, v is a hidden top vertex of height H > 16*tau (tau = sqrt(delta(P))), and A is a subset of {j : ||p_j - p_v||_1 >= 4*tau and dist_1(p_j, conv{p_w : w in W}) > H - 8*tau} satisfying sum_{j in A} max(P_vj, 0) >= c_m, some top support functional phi at v satisfies sum_{j in A} max(P_vj, 0)*(H - phi(p_j)) >= c_5*c_m*tau.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height; def-co-top; def-top-support-functional
deps: lem-l5-mass-barycenter-dualization; lem-l5-top-face-ray-formula; lem-l5-positive-flow-foldback; lem-l5-universal-exterior-payer
status: conjecture
af: none
provenance: W68 repair registration of the W54 L5-GAP-1 premise, pinned to context/verdict-bridges.md item 2 and context/BRIEF-W62-STRATEGIST.md
owner: proposed
---
```

This is a registration only; no proof is claimed. The quantifier order is load-bearing: $c_5$ is universal and independent of $c_m$, while the smallness ceiling $\delta_5(c_m)$ may depend on the already fixed universal mass threshold $c_m$. The notation agrees with the locked definitions: $\tau=\sqrt{\delta(P)}$, $W=\mathcal W(P)$, $H=\max_i \operatorname{dist}_1(p_i,\operatorname{conv}W)$, and a top support functional is an affine $1$-Lipschitz $\phi$ with $\phi(p_v)=H$ and $\phi\le0$ on $\operatorname{conv}W$. The two inequalities defining $A$ are exactly the $\rho$-far, $8\tau$-co-top band. The coefficient mass is the positive submeasure of row $v$; its full-row-fiber aggregation is the clone-invariant object used by `lem-l5-mass-barycenter-dualization`.

The registered W62/W63/W64/W65/W67 families
`lem-l5-*`, `lem-ihorn-*`, `lem-icap-*`, `lem-dcap-*`, and `lem-aesc-*` form the reduction/attack tree for this conjecture. They are not asserted here to constitute a proof of the conjecture: in particular, several interfaces are calibrated only for $c_m\in(0,1)$, and the W67 AESC layer fixes $c_m=1/4$. That does not alter the pinned conjecture, and the assembly below uses only $c_m=c_*/2\in(0,1/2)$.

The pointwise sibling `conj-summit-cylinder-exclusion` does **not** imply this mass statement by selecting one functional per row and averaging. The simplex obstruction recorded in `context/FINDINGS.md` permits every atom to have a favorable dual direction while the mass barycenter re-enters the summit cylinder. Consistently with `lem-intersection-witness-confinement`, no averaged-witness mechanism is used here.

# Part 2 — `lem-intersection-branch-production`

```yaml
---
id: lem-intersection-branch-production
kind: lemma
contract: >-
  With the universal constant delta_B = 1/4, every exact signed idempotent P with 0 < delta(P) <= delta_B and nonempty visible set W, and every hidden top vertex v of height H > 16*tau (tau = sqrt(delta(P))) such that t*(v) is in (0,kappa), where kappa = tau/4, and conv{p_f - p_v : f in T(v)} intersects t*(v)*conv{p_i - p_v : i in O(v)}, admits either (i) a probability measure lambda_L on rows f satisfying ||p_f - p_v||_1 >= 4*tau and dist_1(p_f, conv W) > H - 4*tau, whose barycenter b_L satisfies ||b_L - p_v||_1 <= 2.2*tau and for which integral h(p_f) d lambda_L(f) <= (16/13)*kappa for every admissible exposer h at v, or (ii) a sub-probability measure mu_S of total mass at least tau/(2+4*delta(P)) on rows f satisfying ||p_f - p_v||_1 >= 4*tau and dist_1(p_f, conv W) <= H - 4*tau, for which integral h(p_f) d mu_S(f) <= kappa for every admissible exposer h at v.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height; def-co-top; def-actor-hull
deps: lem-optimal-face-conic-reduction; lem-always-tight-dual-support; lem-intersection-witness-confinement; lem-top-witness-third-actor
status: proposed
af: none
provenance: W68 independent registry extraction of context/l2-attack.md sections 2.6-2.7, with the missing B5 dependency repaired explicitly
owner: proposed
---
```

The intersection predicate is verbatim the L2-core configuration in the contract of `lem-l2-core-collapse`:

\[
 \operatorname{conv}\{p_f-p_v:f\in T(v)\}
 \cap t^*(v)\operatorname{conv}\{p_i-p_v:i\in O(v)\}\ne\varnothing.
\]

Tangency belongs to this intersecting predicate. Put

\[
 \delta=\delta(P),\qquad \tau=\sqrt\delta,\qquad
 \kappa=\tau/4,\qquad D=2+4\delta.
\]

## Consumed proved interfaces

The hypothesis clauses and outputs used below are these.

1. `lem-optimal-face-conic-reduction` applies to the exposedness LP at a hidden geometrically distinct row vertex $u$ of an exact signed idempotent with $t^*(u)>0$. Its registered contract says that the reduced optimal witnesses are exactly the displays
   \[
   \sum_{f\in T}\lambda_f(p_f-p_u)+\sum_{z\in Z}a_z(p_z-p_u)
   =t^*(u)\sum_{i\in O}\gamma_i(p_i-p_u),
   \]
   with $\lambda,\gamma$ probability vectors on $T,O$ and $a_z\ge0$, and that an all-$a_z=0$ display exists exactly when the two hulls in the contract intersect. Here $u=v$ is a hidden top vertex and $t^*(v)>0$, so every hypothesis is present.

2. `lem-always-tight-dual-support` applies to a hidden geometrically distinct row vertex of an exact signed idempotent with $\delta>0$ and nonempty visible set. Its contract identifies $T,O,Z$ as, respectively, the $\rho$-far, upper-box, and lower-box constraint families tight on the whole primal optimal face; it also says $T\ne\varnothing$, and says $O\ne\varnothing$ if and only if $t^*(v)>0$. Thus both families are nonempty here, and the proved $\rho$-far clause gives $T(v)\subseteq F_v$.

3. The full registered contract of `lem-intersection-witness-confinement` is:

   > For an exact signed idempotent $P$ with $0<\delta(P)\le1/4$, nonempty visible set, hidden top vertex $v$ with $t^*(v)\in(0,\kappa)$, and an alpha-free reduced optimal display
   > \(
   > \sum_T\lambda_f(p_f-p_v)=t^*(v)\sum_O\gamma_i(p_i-p_v)
   > \)
   > with $\lambda,\gamma$ probability vectors: (B1) $(\lambda,0,t^*\gamma)$ is a hiddenness dual witness with total beta mass $t^*(v)<\kappa$; (B2) its barycenter $b=\sum_f\lambda_fp_f$, with $q=\sum_i\gamma_ip_i$, obeys
   > \(
   > \|b-p_v\|_1=t^*(v)\|q-p_v\|_1\le t^*(v)(2+4\delta)<(1/2+\delta)\tau;
   > \)
   > (B3) for every admissible exposer $h$ at $v$,
   > \(
   > \sum_f\lambda_fh(p_f)\le t^*(v);
   > \)
   > (B4) for every top support functional at $v$, and every finite convex average, the witness-average top deficit is at most $t^*(v)(2+4\delta)<(1/2+\delta)\tau$, so its mass at deficit at least $\tau$ is $<1/2+\delta$.

   Thus B1, B2, and B3 are consumed. B4 is deliberately **not** consumed: it is the cap that certifies the averaged-witness route dead.

4. `lem-top-witness-third-actor` applies to an exact signed idempotent with $0<\delta\le1/4$, nonempty $W$, a hidden top $v$, and any hiddenness dual witness with total beta mass $<\tau/4$. For every $c>1/2+\delta$, its contract gives
   \[
   \lambda\{f:\operatorname{dist}_1(p_f,\operatorname{conv}W)>H-c\tau\}
   >1-\frac{1/2+\delta}{c};
   \]
   all these witness rows lie in $F_v=\{f:\|p_f-p_v\|_1\ge4\tau\}$. At $c=4$, more than $13/16$ of $\lambda$ is far and co-top.

**DEFECT AUDIT — repaired dependency mismatch, no residual proof defect.** The actual registered contract of `lem-intersection-witness-confinement` contains B1–B4, not B1–B5. In particular it does not contractually contain the depth/co-top mass clause called “B5” in `context/l2-attack.md`. Treating that body label as part of the shard contract would be invalid. The frontmatter above therefore adds the proved `lem-top-witness-third-actor`; B1 supplies exactly its small-beta-witness hypothesis, and that shard supplies the required co-top mass. No unproved fact is imported.

## Proof

The hull intersection and `lem-optimal-face-conic-reduction` give probability vectors $\lambda$ on $T(v)$ and $\gamma$ on $O(v)$ with the alpha-free display

\[
 \sum_f\lambda_f(p_f-p_v)
 =t^*(v)\sum_i\gamma_i(p_i-p_v). \tag{1}
\]

The family $T(v)$ is the always-tight $\rho$-far family, so
$\operatorname{supp}\lambda\subseteq F_v$. Apply `lem-intersection-witness-confinement` to (1). By B1, $(\lambda,0,t^*\gamma)$ is a hiddenness dual witness and its beta mass is $t^*(v)<\kappa=\tau/4$. Hence `lem-top-witness-third-actor` applies. Define

\[
 L:=\{f\in\operatorname{supp}\lambda:
       d_f>H-4\tau\},\qquad
 S:=\operatorname{supp}\lambda\setminus L,\qquad
 \mu:=\lambda(S),
\]

where $d_f=\operatorname{dist}_1(p_f,\operatorname{conv}W)$. Its $c=4$ clause gives the sharper estimate

\[
 \lambda(L)>1-\frac{1/2+\delta}{4},
 \qquad
 \mu<\frac{1/2+\delta}{4}
      =\frac18+\frac\delta4\le\frac3{16}. \tag{2}
\]

Let $b=\sum_f\lambda_fp_f$. B2 and B3 give, respectively,

\[
 \|b-p_v\|_1<(1/2+\delta)\tau, \tag{3}
\]

and, for every admissible exposer $h$ at $v$,

\[
 \sum_f\lambda_fh(p_f)\le t^*(v)<\kappa. \tag{4}
\]

The row-diameter clause of `def-signed-idempotent` is
$\|p_i-p_j\|_1\le D=2+4\delta$. Consequently the barycenter of any nonempty part of $\lambda$ is within $D$ of $p_v$. Also $h\ge0$ on all rows by `def-exposed`, so restricting the nonnegative measure in (4) can only decrease its $h$-integral.

We split at $\mu=\tau/D$, assigning equality to the first case.

### Case (i): $\mu\le\tau/D$

If $\mu=0$, take $\lambda_L=\lambda$. It is supported on far co-top rows, and (3) gives
$\|b-p_v\|_1<(1/2+\delta)\tau\le(3/4)\tau<2.2\tau$, while (4) gives every exposer average $<\kappa<(16/13)\kappa$. Thus alternative (i) holds.

Suppose now $0<\mu\le\tau/D$. Let $\lambda_L=\lambda|_L/(1-\mu)$ and let $b_L,b_S$ be the conditional barycenters of $\lambda|_L,\lambda|_S$. Then

\[
 (1-\mu)(b_L-p_v)+\mu(b_S-p_v)=b-p_v.
\]

Using (2), (3), $\|b_S-p_v\|_1\le D$, and $\mu D\le\tau$,

\[
\begin{aligned}
 \|b_L-p_v\|_1
 &\le\frac{\|b-p_v\|_1+\mu\|b_S-p_v\|_1}{1-\mu}\\
 &<\frac{(1/2+\delta)\tau+\tau}{13/16}\\
 &=\frac{16}{13}(3/2+\delta)\tau\\
 &\le\frac{28}{13}\tau
 <\frac{11}{5}\tau=2.2\tau . \tag{5}
\end{aligned}
\]

The penultimate strict comparison is $28/13<11/5$, equivalently $140<143$. For every admissible $h$, nonnegativity and (4) give

\[
 \int h\,d\lambda_L
 =\frac{\sum_{f\in L}\lambda_fh(p_f)}{1-\mu}
 \le\frac{t^*(v)}{1-\mu}
 <\frac{16}{13}\kappa. \tag{6}
\]

Every row in $L$ is $\rho$-far because $\operatorname{supp}\lambda\subseteq T(v)\subseteq F_v$, and it has $d_f>H-4\tau$ by definition. Equations (5)–(6) are exactly alternative (i), with stronger strict bounds.

### Case (ii): $\mu>\tau/D$

Let $\mu_S=\lambda|_S$. This is a sub-probability measure of total mass

\[
 \mu_S(1)=\mu>\frac\tau D
 =\frac{\tau}{2+4\delta}, \tag{7}
\]

so it satisfies the required weak lower bound. It is supported on $\rho$-far rows with $d_f\le H-4\tau$; the equality boundary in depth belongs to $S$. For every admissible exposer $h$, (4) and $h\ge0$ give

\[
 \int h\,d\mu_S
 =\sum_{f\in S}\lambda_fh(p_f)
 \le\sum_f\lambda_fh(p_f)
 \le t^*(v)<\kappa. \tag{8}
\]

Thus alternative (ii) holds. Cases (i) and (ii) are exhaustive, with
$\mu=\tau/D$ owned by (i), and all constants in the two registered exclusion contracts are matched exactly: $2.2\tau$, $(16/13)\kappa$, $\tau/(2+4\delta)$, and $\kappa$. This proves the proposed lemma. $\square$

# Part 3 — repaired `lem-huddle-charge-assembly`

```yaml
---
id: lem-huddle-charge-assembly
kind: lemma
contract: >-
  Assume conj-straddling-web-exclusion with ceiling delta_a, conj-shallow-counterweight-exclusion with ceiling delta_b, conj-cotop-web-coupling with ceiling delta_c and constant c_* in (0,1), and conj-l5-gap-1 with universal constant c_5 (harmlessly decreased, if necessary, so that 0 < c_5 <= 1) and ceiling delta_5(c_*/2) all hold. With delta_B = 1/4 and delta_0 = min{delta_a, delta_b, delta_c, delta_5(c_*/2), delta_B, 1/4, (c_5*c_*/6)^2}, no exact signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set W, and hidden top vertex v of height H > 16*tau carries positive coefficient mass sum_{j : ||p_j - p_v||_1 < 4*tau and dist_1(p_j, conv W) > 16*tau} max(P_vj, 0) >= 7/8.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height; def-near-cluster; def-co-top; def-actor-hull; def-top-support-functional
deps: conj-straddling-web-exclusion; conj-shallow-counterweight-exclusion; conj-cotop-web-coupling; conj-l5-gap-1; lem-intersection-branch-production; lem-hiddenness-dual-witness; lem-positive-exposedness-margin; lem-always-tight-dual-support; lem-top-deficit-price
status: proposed
af: none
provenance: W68 repair of the hostile-invalid W54 assembly bridge, conditional on the two exclusion conjectures, co-top coupling, and the newly registered L5 mass minimax
owner: proposed
---
```

The shrinking convention for $c_5$ is legitimate: if `conj-l5-gap-1` holds with $c_5'>0$, it holds with $c_5=\min\{c_5',1\}$ and the same ceilings. We relabel this smaller witness $c_5$. No strengthening of the conjecture is involved.

## Consumed interfaces and hypothesis threading

- `lem-hiddenness-dual-witness` applies to an exact signed idempotent and a hidden row vertex and says, in particular, that
  $F_v=\{j:\|p_j-p_v\|_1\ge4\tau\}$ is nonempty.
- `lem-positive-exposedness-margin` applies when $\rho=4\tau>0$, $v$ is a geometrically distinct row vertex, and $F_v\ne\varnothing$; for a hidden such vertex it gives $0<t^*(v)<\kappa$.
- `lem-always-tight-dual-support` applies to a hidden geometrically distinct row vertex of an exact signed idempotent with $\delta>0$ and nonempty $W$; it says $T(v)\ne\varnothing$ and $O(v)\ne\varnothing$ exactly when $t^*(v)>0$. Thus both actor hulls below are nonempty.
- `lem-intersection-branch-production` requires $0<\delta\le\delta_B=1/4$, nonempty $W$, a hidden top with $H>16\tau$, $t^*(v)\in(0,\kappa)$, and the exact intersecting-hull predicate. Its two outputs are exactly the objects forbidden by the next two assumed contracts.
- `conj-straddling-web-exclusion`, at ceiling $\delta_a$, forbids for such $P,W,v,H$ the probability measure on far co-top rows with barycenter within $2.2\tau$ and all-exposer average at most $(16/13)\kappa$.
- `conj-shallow-counterweight-exclusion`, at ceiling $\delta_b$, forbids for such $P,W,v,H$ the far shallow sub-probability of mass at least $\tau/(2+4\delta)$ and all-exposer integral at most $\kappa$.
- `conj-cotop-web-coupling`, at ceiling $\delta_c$, requires **all** of: exact signed idempotence, $0<\delta\le\delta_c$, nonempty $W$, a hidden top $v$ with $H>16\tau$, $t^*(v)>0$, disjoint always-tight hulls, and the heavy bound
  \[
  \sum_{\substack{\|p_j-p_v\|_1<4\tau\\d_j>16\tau}}(P_{vj})_+\ge7/8.
  \]
  Its output is mass at least $c_*$ on
  \[
  A=\{j:\|p_j-p_v\|_1\ge4\tau,\ d_j>H-8\tau\}. \tag{9}
  \]
  Thus the heavy premise is not suppressed; it is precisely the contrary hypothesis in the proof.
- `conj-l5-gap-1`, at $c_m=c_*/2$ and ceiling $\delta_5(c_*/2)$, applies to (9) once its mass is at least $c_*/2$, and supplies one top support functional with charge at least $c_5(c_*/2)\tau$.
- `lem-top-deficit-price` applies to every exact signed idempotent with $\delta>0$, nonempty $W$, and hidden top $v$. For **any** top support functional $\phi$, every index set $A$ satisfies
  \[
  \sum_{j\in A}(P_{vj})_+\bigl(H-\phi(p_j)\bigr)
  \le\nu_v(2+4\delta)\le\delta(2+4\delta). \tag{10}
  \]

These are all the mathematical shard contracts consumed directly by this assembly.

## Proof

Assume for contradiction that $P,W,v$ satisfy the contract and that the displayed near-cluster mass is at least $7/8$. Write $\delta=\delta(P)$, $\tau=\sqrt\delta$, and $\kappa=\tau/4$.

Because $v$ is hidden, `lem-hiddenness-dual-witness` gives $F_v\ne\varnothing$. Since $\delta>0$, $\rho=4\tau>0$, and the hidden top $v$ is a geometrically distinct row vertex. Therefore `lem-positive-exposedness-margin` gives

\[
 0<t^*(v)<\kappa. \tag{11}
\]

By `lem-always-tight-dual-support`, $T(v)$ and $O(v)$ are nonempty. Hence

\[
 K_T(v)=\operatorname{conv}\{p_f-p_v:f\in T(v)\},\qquad
 K_O(v)=t^*(v)\operatorname{conv}\{p_i-p_v:i\in O(v)\}
\]

are nonempty compact convex sets. Exactly one of the following holds:

1. $K_T(v)\cap K_O(v)\ne\varnothing$. Tangency and distance zero belong here.
2. $K_T(v)\cap K_O(v)=\varnothing$. Compactness then gives
   $\operatorname{dist}_1(K_T(v),K_O(v))>0$, which is exactly the registered disjoint-hull predicate.

Thus there is no empty-hull or zero-distance third case.

### (I) Intersecting hulls

All hypotheses of `lem-intersection-branch-production` hold: (11) supplies $t^*(v)\in(0,\kappa)$, and $\delta\le\delta_0\le\delta_B$. It produces either its alternative (i) or alternative (ii).

Alternative (i) is the probability measure forbidden by `conj-straddling-web-exclusion`; its ceiling applies because $\delta\le\delta_0\le\delta_a$. Alternative (ii) is the sub-probability measure forbidden by `conj-shallow-counterweight-exclusion`; its ceiling applies because $\delta\le\delta_0\le\delta_b$. Either output is a contradiction. No average of top support functionals, no reciprocal of $t^*(v)$, and no interpretation of conic coefficients as transitions occurs in this branch.

### (II) Disjoint hulls

Here every hypothesis of `conj-cotop-web-coupling` is present. In particular, the heavy hypothesis is the contradictory $7/8$ assumption, including its strict near boundary $\|p_j-p_v\|_1<4\tau$, and $\delta\le\delta_c$. The conjecture therefore gives for the set $A$ in (9)

\[
 S_A:=\sum_{j\in A}(P_{vj})_+\ge c_*\ge c_*/2. \tag{12}
\]

The distance boundary $\|p_j-p_v\|_1=4\tau$ belongs to this far set, and the depth band is the exact strict band required by both coupling and L5. Since $\delta\le\delta_5(c_*/2)$, `conj-l5-gap-1` applied with $c_m=c_*/2$ gives a top support functional $\phi$ such that

\[
 \sum_{j\in A}(P_{vj})_+\bigl(H-\phi(p_j)\bigr)
 \ge \frac{c_5c_*}{2}\tau. \tag{13}
\]

For this same $\phi$, `lem-top-deficit-price` and (10) give the opposite estimate

\[
 \sum_{j\in A}(P_{vj})_+\bigl(H-\phi(p_j)\bigr)
 \le\delta(2+4\delta)=\tau^2(2+4\delta). \tag{14}
\]

Set $x=c_5c_*/6$. The harmless normalization $c_5\le1$ and the coupling contract's $c_*<1$ give $0<x<1/6$. From the chosen ceiling,

\[
 \tau=\sqrt\delta\le x,
 \qquad
 \delta\le x^2<1/36<1/4,
 \qquad
 2+4\delta<3. \tag{15}
\]

Consequently (14) is strictly less than

\[
 3\tau^2\le3x\tau=\frac{c_5c_*}{2}\tau, \tag{16}
\]

contradicting (13). The strict inequality in (16) survives the endpoint
$\delta=x^2$ because (15) has $2+4\delta<3$. Thus the verdict's proposed ceiling exponent $2$ and denominator $6$ are correct; no additional strict ceiling is needed.

Both exhaustive hull branches contradict the assumed heavy top, proving the conditional assembly. $\square$

## Calibration, containment, and exact dependency audit

For $(a,\theta_0)=(16,1/8)$, the full `conj-near-cluster-absorption` tallness threshold is

\[
 \frac{5a/4+3/2}{\theta_0}\tau
 =\frac{20+3/2}{1/8}\tau
 =172\tau.
\]

The repaired assembly excludes mass $\ge7/8$ already for $H>16\tau$, so its regime contains the conjecture's $H>172\tau$ regime. Its conclusion is in fact strict mass $<7/8$, and therefore implies the conjecture's weak mass bound $\le7/8$ on that narrower regime. This calibration and containment are body consequences, not clauses of the repaired contract.

The two appearances of $1/4$ in $\delta_0$ are intentionally transparent but numerically redundant: Part 2 has $\delta_B=1/4$, while the separate $1/4$ records the top-deficit arithmetic ceiling proposed by the verdict. Removing either would not change the minimum in this draft. The exact direct dependency list is the one in the redrafted frontmatter. In particular, `lem-l2-core-collapse` is dropped: the proof never consumes its equivalence or averaging statement, because `lem-intersection-branch-production` directly produces the SL1a/SL1b-forbidden object. `lem-optimal-face-conic-reduction` and `lem-top-witness-third-actor` are dependencies of that production lemma rather than additional direct dependencies of the assembly; `lem-always-tight-dual-support` remains a direct assembly dependency because it rules out empty actor hulls before the root split.
