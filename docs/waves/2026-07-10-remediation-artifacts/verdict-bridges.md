# Hostile verification of the two candidate bridges

## 1. `lem-low-slab-cap-implies-min-a`

Provisional verdict: **VALID-AS-CONDITIONAL**; the present contract does not state strong enough premises to imply the contract of `conj-min-a-w4`.

Contract re-derivation.  Put
\[
c_*=(17-12\sqrt2)/2,\qquad \tau=\sqrt{\delta(P)},\qquad
G_4=\{j:d_1(p_j,C_{\mathcal W})>4\tau\}.
\]
If the low-slab cap is assumed at the *specific* witnesses
\((a,\theta)=(4,1/2)\), then its tallness threshold is
\[
\frac{5a/4+3/2}{\theta}\tau
=\frac{5+3/2}{1/2}\tau=13\tau.
\]
It supplies a hidden top vertex \(v\) and an optimal (hence admissible) exposer \(h_v^*\) for which
\[
\sum_{j\in G_4,\ h_v^*(p_j)<\tau/4}P_{vj}^+
\le 1-\tfrac12-4\tau.
\]
By `def-exposed`, \(h_v^*(p_v)=0\) and \(0\le h_v^*(p_j)\le1\), so `lem-cs-low-slab-pincer` applies with \(s=\tau/4>0\). Since
\(\nu_v\le\delta=\tau^2\), it gives
\[
\sum_{j\in G_4,\ h_v^*(p_j)\ge\tau/4}P_{vj}^+
\le \sum_{h_v^*\ge\tau/4}P_{vj}^+
\le\frac{\nu_v}{\tau/4}\le4\tau.
\]
The strict-low and weak-high pieces partition \(G_4\), hence
\(\sigma_4(v)\le(1/2-4\tau)+4\tau=1/2\).  The split and every numerical conversion are correct under those premises.

Fatal-to-the-current-unconditional-wording contract mismatches:

1. `conj-low-slab-cap` says only that *there exist* universal \(a>0\), \(\theta\in(0,1)\), and \(\delta_0>0\). It does not assert that \(a=4\), and even after imposing \(a=4\), arbitrary \(\theta\in(0,1)\) yields only \(\sigma_4(v)\le1-\theta\), not \(1/2\), with tallness threshold \(6.5\tau/\theta\), not \(13\tau\). The role-note sentence claiming the calibration is not part of the contract and cannot instantiate existential witnesses at chosen values.
2. The bridge's displayed conclusion covers only \(0<\delta(P)\le\min(\delta_0,c_*)\), whereas `conj-min-a-w4` covers the whole interval \(0<\delta(P)\le c_*\). An unspecified positive \(\delta_0<c_*\) leaves an uncovered interval, so the bridge's “i.e.” is false unless \(\delta_0\ge c_*\).
3. Dependency status check: `lem-cs-low-slab-pincer` is `status: proved` and its contract says exactly what is used.  `conj-low-slab-cap` is `status: conjecture`, not proved.  Thus the low-slab assertion is only a conditional premise, not an available proved input.  `def-slab` is also only `status: draft`, although the proof needs no substantive claim from it beyond notation.

Exact contract addition needed for the advertised implication:

> Assume the low-slab coefficient-cap statement with the fixed witnesses \(a=4\), \(\theta=1/2\), and \(\delta_0\ge(17-12\sqrt2)/2\).

Equivalently, without the lower bound on \(\delta_0\), the conclusion must be renamed as the \(\delta\le\min(\delta_0,c_*)\) restriction of **conj-min-a-w4**, not the full conjecture itself.

## 2. lem-huddle-charge-assembly

Provisional verdict: **INVALID**. Even after granting the three caveats mentioned after “modulo,” the four contracts in deps do not imply the tall near-cluster conclusion: the Branch-II sub-assembly is absent from every quoted contract.

### What the constants and the disjoint branch really give

For the advertised values \(a=16\), \(\theta_0=1/8\), the tallness threshold in the full near-cluster-absorption contract is
\[
\frac{5a/4+3/2}{\theta_0}\tau
=\frac{20+3/2}{1/8}\tau=172\tau.
\]
Thus an exclusion valid already for \(H>16\tau\) would indeed imply the conjecture on its \(H>172\tau\) regime. The cluster set and its strict inequalities are quoted correctly, and excluding mass \(\ge7/8\) is stronger than the target conclusion mass \(\le7/8\).

There is a valid conditional route on the **disjoint** always-tight-hull branch. A hidden top has a nonempty far set; lem-positive-exposedness-margin (proved) therefore gives \(t^*(v)>0\). Assuming conj-cotop-web-coupling, the root hypotheses (tall, heavy, disjoint) give a universal \(c_*>0\) and
\[
 S_A:=\sum_{j\in A}P_{vj}^+\ge c_* ,\qquad
 A=\{j:\|p_j-p_v\|_1\ge4\tau,\ d_j>H-8\tau\}.
\]
If one additionally assumes the exact W54 L5 minimax statement at, for example, \(c_m=c_*/2\), then some top support functional \(\phi\) obeys
\[
 \sum_{j\in A}P_{vj}^+\bigl(H-\phi(p_j)\bigr)
 \ge c_5c_m\tau.
\]
The proved lem-top-deficit-price gives the opposite bound \(\le\delta(2+4\delta)\le3\tau^2\) for \(\delta\le1/4\), a contradiction when \(\delta<(c_5c_m/3)^2\). This re-derivation needs neither the old L6/L7 huddle recursion nor AG-2.

### Fatal contract mismatch on the intersection branch

lem-l2-core-collapse does **not** assert Branch-II tall emptiness. Its contract asserts only the equivalence
\[
\text{L2-v2}\quad\Longleftrightarrow\quad\text{L2-core (bare intersection-branch tall emptiness)},
\]
plus the degeneracy of finite averaging. Truth of an equivalence does not prove either side. The contracts of SL1a and SL1b merely exclude their two specified measure configurations. No consumed shard contract says that an intersecting-hulls tall top produces one of those configurations. The W54 wave prose says “SL1a + SL1b => L2-core (proved sub-assembly)” but also says Proposition E was **not separately banked**. Role prose in the SL1 shards is not a contract. Consequently the bridge has no formal implication closing the intersecting branch, even if both conjectural exclusions are assumed true.

This missing Branch-II production/sub-assembly is not named by the bridge contract and is therefore fatal under the requested rule. Attempting to replace it by the old averaged-witness mechanism would use a registered FINDINGS dead route: lem-intersection-witness-confinement caps the witness-average deficit for every top support functional, and lem-l2-core-collapse itself says finite averaging is degenerate.

### Status and gap-honesty audit

- lem-l2-core-collapse is status: proved, but says only the equivalence just described.
- conj-straddling-web-exclusion, conj-shallow-counterweight-exclusion, and conj-cotop-web-coupling are all status: conjecture, not proved. Their use can only be as explicit conditional assumptions.
- AG-1 is mathematically discharged by the proved lem-positive-exposedness-margin together with nonemptiness of a hidden vertex's far set. The assembly shard omits that dependency and instead says “modulo AG-1”; this is not an explicit logical condition, but no new conjecture is needed.
- AG-2 is also not a genuine remaining condition: the formal contract of the proved lem-disjointness-huddle-reduction permits \(u=v\) (it requires that \(u\) be a geometrically distinct row vertex, not that \(p_u\ne p_v\)); moreover the shorter coupling-plus-L5 disjoint-branch proof above does not instantiate that lemma at all. Again, “modulo AG-2” is not a quantified condition.
- L5 is named only in the trailing “modulo” prose, has no registry shard, is absent from deps, and is not stated quantitatively in the bridge contract. It therefore is not honestly carried as an explicit assumption. The W54 record specifically says it is open and that pointwise visibility does not imply it by averaging.
- The final L5 charge also consumes the proved lem-top-deficit-price, and the AG-1 repair consumes the proved lem-positive-exposedness-margin; both are omitted from the bridge's deps.

A repair would have to add, verbatim, both of these mathematical assumptions (and the two proved dependencies just noted):

1. **Branch-II production/sub-assembly.** For sufficiently small universal \(\delta_B>0\), every exact signed idempotent with nonempty visible set and a hidden top \(v\) with \(H>16\tau\), \(t^*(v)>0\), and intersecting always-tight hulls at \(v\) admits either the probability measure forbidden by the exact SL1a contract or the sub-probability measure forbidden by the exact SL1b contract.
2. **L5-GAP-1 (mass minimax).** There exist universal \(c_5>0\) and, for every fixed universal \(c_m>0\), a universal \(\delta_5>0\) such that whenever \(0<\delta(P)\le\delta_5\), \(v\) is a hidden top with \(H>16\tau\), and \(A\subseteq\{j:\|p_j-p_v\|_1\ge4\tau,\ d_j>H-8\tau\}\) satisfies \(\sum_{j\in A}P_{vj}^+\ge c_m\), some top support functional \(\phi\) satisfies
\[
\sum_{j\in A}P_{vj}^+\bigl(H-\phi(p_j)\bigr)\ge c_5c_m\tau.
\]

With those additions, lem-positive-exposedness-margin and lem-top-deficit-price added to deps, and \(\delta_0\) chosen below all four conjectural ceilings, \(1/4\), and \((c_5c_*/6)^2\), a clean two-branch proof would work. That is a different, explicitly conditional contract; it does not validate the candidate as written.

## Final verdicts

1. **VALID-AS-CONDITIONAL** — the pincer composition is correct only after fixing \((a,\theta)=(4,1/2)\) as an actual premise and requiring the cap ceiling to satisfy \(\delta_0\ge(17-12\sqrt2)/2\) (or weakening the named conclusion to the restricted delta interval).
2. **INVALID** — L5 is not an explicit quantified dependency, and, more decisively, no consumed contract supplies the unmentioned SL1a/SL1b-to-L2-core production implication needed to close the intersection branch.
