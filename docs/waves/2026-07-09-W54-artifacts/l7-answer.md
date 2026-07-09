VERDICT: BLOCKED — The proved shards give the local depth/huddle anatomy, but not the cross-exposer value/coefficient monotonicity needed to force universal kappa-high shipping.

diff --git a/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l7/ANSWER.md b/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l7/ANSWER.md
new file mode 100644
index 0000000000000000000000000000000000000000..9c76e118e8b181285e3a65833571eb60b345474d
--- /dev/null
+++ b/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l7/ANSWER.md
@@ -0,0 +1,207 @@
+VERDICT: BLOCKED — The proved shards give the local depth/huddle anatomy, but not the cross-exposer value/coefficient monotonicity needed to force universal kappa-high shipping.
+
+## §1 THE STATEMENT(S)
+
+I use the following notation throughout.  Let
+\[
+  \delta=\delta(P)>0,\qquad \tau=\sqrt{\delta},\qquad \rho=4\tau,\qquad \kappa=\tau/4,
+\]
+let \(W=W(P)\), \(C_W=\operatorname{conv}\{p_w:w\in W\}\), and write
+\[
+  d_i:=\operatorname{dist}_1(p_i,C_W).
+\]
+
+### Target L7
+
+Fix \(c_r=1/2\).  The target leaf asks for a universal \(\delta_0>0\) such that the following holds.
+
+For every exact signed idempotent \(P\) with \(0<\delta(P)\le \delta_0\), nonempty \(W(P)\), and hidden top row vertex \(v\) of height \(H=H(P)>16\tau\), for every chain of geometrically distinct row vertices
+\[
+  v,u_1,u_2,u_3
+\]
+such that
+\[
+  \|p_{u_1}-p_v\|_1<4\tau,\qquad
+  \|p_{u_{k+1}}-p_{u_k}\|_1<4\tau\quad(k=1,2),
+\]
+and such that each \(u_k\) is hidden, has \(t^*(u_k)>0\), and has disjoint always-tight hulls
+\[
+  \operatorname{conv}\{p_f-p_{u_k}:f\in T(u_k)\}
+  \cap
+  t^*(u_k)\operatorname{conv}\{p_i-p_{u_k}:i\in O(u_k)\}
+  =\varnothing,
+\]
+there is some \(k\in\{1,2,3\}\) and some always-tight zero-face row \(z\in Z(u_k)\), for a relative-interior optimal exposer \(h_k^*\) at \(u_k\), such that
+\[
+  \sum_{\{j:h_k^*(p_j)\ge \kappa\}} \max(P_{zj},0)\ge c_r.
+\]
+
+I cannot prove this target from the proved shards.
+
+### Unconditional sublemma proved here
+
+Under the chain hypotheses above, the following dimension-free, clone-invariant facts do follow:
+
+1.  For \(k=1,2,3\),
+\[
+  d_{u_k}>H-4k\tau.
+\]
+In particular \(d_{u_k}>4\tau\) for all \(k\le3\), since \(H>16\tau\).
+
+2.  For each \(k=1,2,3\), after choosing a relative-interior optimal exposer \(h_k^*\) at \(u_k\), the disjointness hypothesis gives at least one nonclone always-tight zero-face row \(z_k\in Z(u_k)\) with \(h_k^*(p_{z_k})=0\).  Moreover every zero-face row for \(h_k^*\) is \(\rho\)-near \(u_k\).
+
+3.  For every such zero-face row \(z\) at any \(u_k\), the proved capacity/exchange tools give only the upper bound
+\[
+  \kappa \sum_{\{j:h_k^*(p_j)\ge \kappa\}}\max(P_{zj},0)
+  \le \nu_z\le \delta.
+\]
+Equivalently,
+\[
+  \sum_{\{j:h_k^*(p_j)\ge \kappa\}}\max(P_{zj},0)\le 4\tau.
+\]
+
+Thus for \(\tau<c_r/4\), the desired L7 conclusion is incompatible with row capacity unless the chain antecedent is already impossible.  The missing proof is precisely a no-chain argument, or equivalently a value/coefficient monotonicity argument forcing the row-capacity contradiction.
+
+### GAP-1 and GAP-2: missing standalone claims
+
+The missing monotonicity claim is the following.
+
+**GAP-1 (cross-exposer value/coefficient monotonicity).**  There exists a universal constant \(\delta_0>0\) such that the following holds in the Target L7 setting with the fixed threshold \(c_r=1/2\).  Let \(h_k^*\) be relative-interior optimal exposers at \(u_k\), and put
+\[
+  F_3^{\mathrm{deep}}
+  :=
+  \{f:\|p_f-p_{u_3}\|_1\ge4\tau,\ d_f>H-16\tau\}.
+\]
+If some hiddenness dual witness \((\lambda^{(3)},\alpha^{(3)},\beta^{(3)})\) at \(u_3\) has
+\[
+  \lambda^{(3)}(F_3^{\mathrm{deep}})>0,
+\]
+then at least one always-tight zero-face row \(z\in Z(u_k)\), for some \(k\le3\), satisfies
+\[
+  \sum_{\{j:h_k^*(p_j)\ge \kappa\}}\max(P_{zj},0)\ge c_r.
+\]
+
+There is also a separate applicability gap for producing the actor required by GAP-1:
+
+**GAP-2 (non-top third actor).**  In the Target L7 setting, \(u_3\) admits a hiddenness dual witness \((\lambda^{(3)},\alpha^{(3)},\beta^{(3)})\) with
+\[
+  \lambda^{(3)}(F_3^{\mathrm{deep}})>0.
+\]
+
+Together, GAP-1 and GAP-2 imply L7: GAP-2 supplies the third-hop deep far actor, and GAP-1 converts its existence into the required \(c_r\)-shipping conclusion.  I found no proved shard that supplies either claim, even with a larger height constant \(H>a\tau\).  The available tools locate zero-face blockers and top far witness rows, but they do not compare exposer values across different centers \(u_1,u_2,u_3\), they do not extend the third-actor theorem to non-top hidden vertices, and they do not lower-bound the positive coefficients \(P_{zj}^+\) of any zero-face row on a high slab.
+
+## §2 THE PROOF
+
+### Proof of the unconditional depth budget
+
+The function \(x\mapsto \operatorname{dist}_1(x,C_W)\) is \(1\)-Lipschitz in the \(\ell^1\) metric.  The chain inequalities give
+\[
+  \|p_{u_k}-p_v\|_1<4k\tau,\qquad k=1,2,3.
+\]
+Since \(d_v=H\), it follows that
+\[
+  d_{u_k}\ge H-\|p_{u_k}-p_v\|_1>H-4k\tau.
+\]
+For \(k\le3\), \(H>16\tau\) gives \(d_{u_k}>H-12\tau>4\tau\).  This uses only metric convexity and contains no packing or index-counting argument.
+
+### Proof of local zero-face anatomy
+
+Fix \(k\in\{1,2,3\}\).  Since \(u_k\) is hidden and \(t^*(u_k)>0\), we have \(0<t^*(u_k)<\kappa<\infty\).  Choose a relative-interior optimal exposer \(h_k^*\) at \(u_k\).  By the always-tight dual support contract, the always-tight far family \(T(u_k)\) is nonempty, and \(O(u_k)\) is nonempty because \(t^*(u_k)>0\).
+
+The always-tight hulls at \(u_k\) are disjoint by hypothesis.  Applying the separator zero-face obstruction to \(u_k\) gives a nonclone row \(z_k\) with
+\[
+  h_k^*(p_{z_k})=0.
+\]
+Because \(h_k^*\) is chosen in the relative interior of the optimal face, a lower-box constraint that is tight at \(h_k^*\) is tight on the whole optimal face; otherwise \(h_k^*\) would lie in a proper boundary face of the optimal face.  Hence \(z_k\in Z(u_k)\), the always-tight zero-face family.
+
+Finally, zero-face localization gives
+\[
+  \|p_z-p_{u_k}\|_1<4\tau
+\]
+for every row \(z\) with \(h_k^*(p_z)=0\).  This proves the local huddle/blocker part.  It does not imply any positive lower bound on the high-slab mass shipped by \(z\).
+
+### What row capacity gives, and why it does not close L7
+
+Let \(z\in Z(u_k)\).  Put \(g_j=h_k^*(p_j)\).  Since \(h_k^*\) is admissible and \(h_k^*(p_z)=0\), the zero-face exchange identity gives
+\[
+  \sum_j \max(P_{zj},0)g_j
+  =
+  \sum_j \max(-P_{zj},0)g_j
+  \le \nu_z\le \delta.
+\]
+Therefore, on the high slab \(A_k=\{j:g_j\ge\kappa\}\),
+\[
+  \kappa\sum_{j\in A_k}\max(P_{zj},0)
+  \le
+  \sum_j \max(P_{zj},0)g_j
+  \le \delta.
+\]
+Equivalently,
+\[
+  \sum_{j\in A_k}\max(P_{zj},0)\le \delta/\kappa=4\tau.
+\]
+
+This is an upper bound.  For \(\delta<(c_r/4)^2\), it rules out the L7 conclusion for any actually existing zero-face row.  Thus a proof of L7 at small \(\delta\) must prove that the whole three-hop chain antecedent is impossible.  The proved shards above do not do that.
+
+### Failed closing attempt and exact gap
+
+The intended depth-budget route would need to argue as follows.
+
+1.  The chain keeps \(u_1,u_2,u_3\) in successive near-top depth bands:
+\[
+  d_{u_1}>H-4\tau,\quad d_{u_2}>H-8\tau,\quad d_{u_3}>H-12\tau.
+\]
+
+2.  Disjointness at each \(u_k\) gives a local zero-face blocker \(z_k\in Z(u_k)\).
+
+3.  Hiddenness at the third hop should force a far actor in a compatible near-top slab.  This is GAP-2.
+
+4.  A value-monotonicity comparison should then force that actor, or a positive fraction of the relevant zero-face row's positive mass, to lie in \(\{h_k^*\ge\kappa\}\) for some earlier or current \(k\).  This is GAP-1.
+
+Step 4 is not available.  In fact, there are two precise obstructions to making it rigorous from the listed proved tools.
+
+First, the proved third-actor theorem is stated for a hidden top vertex.  The vertices \(u_1,u_2,u_3\) are deep and hidden, but they are not known to be hidden tops.  The metric depth estimate alone does not turn them into maximizers of \(d_i\), and the hiddenness-depth Markov proof is not directly portable to non-top vertices because the alpha part of a hiddenness witness has no universal bound.
+
+Second, even if a deep far actor at \(u_3\) were available, no proved shard converts that actor into positive coefficient mass from a zero-face row on any high slab \(\{h_k^*\ge\kappa\}\).  The available exact identity for zero-face rows is the exchange/capacity identity above, which bounds high-slab mass from above by \(4\tau\).  It supplies no lower bound.
+
+Therefore the proof stops at GAP-1/GAP-2.  Raising the height constant from \(16\) to a larger universal \(a\) gives more depth budget, but it does not create a non-top third-actor theorem, a cross-exposer comparison, or a coefficient lower bound; the same gap remains.
+
+## §3 TOOLS USED
+
+Only shards with status `proved` were used.
+
+- `def-signed-idempotent`: exact signed idempotent means \(P\mathbf 1=\mathbf 1\), \(P^2=P\), rows have total mass \(1\), and row geometry is measured in \(\ell^1\).
+
+- `def-negative-mass`: \(\delta(P)=\max_i\sum_j\max\{-P_{ij},0\}\).
+
+- `def-visible-set`: \(\tau=\sqrt\delta\), \(\rho=4\tau\), \(\kappa=\tau/4\), and \(W(P)\) is the set of \((\rho,\kappa)\)-exposed row vertices.
+
+- `def-exposed`: an admissible exposer \(h\) has \(h(p_v)=0\) and \(0\le h(p_j)\le1\) for every row; hidden means \(t^*(v)<\kappa\).
+
+- `def-height`: \(H(P)=\max_i\operatorname{dist}_1(p_i,C_W)\), and a hidden top \(v\) has \(d_v=H\).
+
+- `lem-always-tight-dual-support`: for the exposedness LP at a hidden geometrically distinct row vertex \(u\), \(T\) is nonempty, and \(O\) is nonempty iff \(t^*(u)>0\).
+
+- `lem-separator-zero-face-obstruction`: if \(0<t^*(u)<\infty\), \(h^*\) is a relative-interior optimal exposer, \(T,O\) are nonempty, and the always-tight hulls are disjoint, then there exists a nonclone row \(z\) with \(h^*(p_z)=0\).
+
+- `lem-zero-face-localization`: for a hidden geometrically distinct row vertex \(u\), every row \(z\) with \(h^*(p_z)=0\) for an optimal exposer \(h^*\) at \(u\) satisfies \(\|p_z-p_u\|_1<4\tau\).
+
+- `lem-zero-face-exchange-identity`: for a hidden geometrically distinct row vertex \(u\), optimal exposer \(h^*\), values \(g_j=h^*(p_j)\), and any row \(z\) with \(g_z=0\),
+\[
+  \sum_j\max(P_{zj},0)g_j=\sum_j\max(-P_{zj},0)g_j\le\nu_z\le\delta.
+\]
+
+- `lem-affine-exposer-row-capacity`: equivalently, for an admissible affine \(h\) with \(h(p_i)=0\), threshold \(\eta\ge0\), and \(F\subseteq\{j:h(p_j)\ge\eta\}\),
+\[
+  \eta\sum_{f\in F}\max(P_{if},0)\le\nu_i.
+\]
+
+- `lem-top-witness-third-actor`: consulted but not invoked at \(u_k\).  Its contract applies to a hidden top vertex \(v\), not to an arbitrary deep hidden chain vertex \(u_k\).
+
+## §4 HONEST ASSESSMENT
+
+The weakest point is not a minor constant loss; it is the missing structural bridge GAP-1, plus the non-top actor issue GAP-2.  The local huddle machinery is dimension-free and clone-invariant, but it remains local to each exposedness LP.  It does not order the values of \(h_1^*,h_2^*,h_3^*\) along the chain, and it does not couple hiddenness witness far actors to the positive row coefficients \(P_{zj}^+\) of a zero-face blocker.
+
+A refuter would attack exactly this point by trying to build a tall chain of mutually near hidden vertices whose zero-face rows keep all positive mass in low slabs.  The existing row-capacity identity is compatible with such starvation; it only says that high-slab mass is small when \(\delta\) is small.
+
+The decisive next step is a genuine cross-exposer monotonicity/coefficient lemma and a non-top third-actor extension: prove GAP-2, then prove GAP-1 showing that the third-hop far actor forces a universal amount of positive mass from some zero-face row in a \(\kappa\)-high slab.  Without those, L7 cannot be certified.

codex
Wrote [ANSWER.md](/tmp/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l7/ANSWER.md).

Verdict is `BLOCKED`: the file proves the dimension-free depth/local zero-face anatomy, but identifies the missing cross-exposer value/coefficient monotonicity and the non-top third-actor gap needed to close L7.
diff --git a/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l7/ANSWER.md b/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l7/ANSWER.md
new file mode 100644
index 0000000000000000000000000000000000000000..9c76e118e8b181285e3a65833571eb60b345474d
--- /dev/null
+++ b/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l7/ANSWER.md
@@ -0,0 +1,207 @@
+VERDICT: BLOCKED — The proved shards give the local depth/huddle anatomy, but not the cross-exposer value/coefficient monotonicity needed to force universal kappa-high shipping.
+
+## §1 THE STATEMENT(S)
+
+I use the following notation throughout.  Let
+\[
+  \delta=\delta(P)>0,\qquad \tau=\sqrt{\delta},\qquad \rho=4\tau,\qquad \kappa=\tau/4,
+\]
+let \(W=W(P)\), \(C_W=\operatorname{conv}\{p_w:w\in W\}\), and write
+\[
+  d_i:=\operatorname{dist}_1(p_i,C_W).
+\]
+
+### Target L7
+
+Fix \(c_r=1/2\).  The target leaf asks for a universal \(\delta_0>0\) such that the following holds.
+
+For every exact signed idempotent \(P\) with \(0<\delta(P)\le \delta_0\), nonempty \(W(P)\), and hidden top row vertex \(v\) of height \(H=H(P)>16\tau\), for every chain of geometrically distinct row vertices
+\[
+  v,u_1,u_2,u_3
+\]
+such that
+\[
+  \|p_{u_1}-p_v\|_1<4\tau,\qquad
+  \|p_{u_{k+1}}-p_{u_k}\|_1<4\tau\quad(k=1,2),
+\]
+and such that each \(u_k\) is hidden, has \(t^*(u_k)>0\), and has disjoint always-tight hulls
+\[
+  \operatorname{conv}\{p_f-p_{u_k}:f\in T(u_k)\}
+  \cap
+  t^*(u_k)\operatorname{conv}\{p_i-p_{u_k}:i\in O(u_k)\}
+  =\varnothing,
+\]
+there is some \(k\in\{1,2,3\}\) and some always-tight zero-face row \(z\in Z(u_k)\), for a relative-interior optimal exposer \(h_k^*\) at \(u_k\), such that
+\[
+  \sum_{\{j:h_k^*(p_j)\ge \kappa\}} \max(P_{zj},0)\ge c_r.
+\]
+
+I cannot prove this target from the proved shards.
+
+### Unconditional sublemma proved here
+
+Under the chain hypotheses above, the following dimension-free, clone-invariant facts do follow:
+
+1.  For \(k=1,2,3\),
+\[
+  d_{u_k}>H-4k\tau.
+\]
+In particular \(d_{u_k}>4\tau\) for all \(k\le3\), since \(H>16\tau\).
+
+2.  For each \(k=1,2,3\), after choosing a relative-interior optimal exposer \(h_k^*\) at \(u_k\), the disjointness hypothesis gives at least one nonclone always-tight zero-face row \(z_k\in Z(u_k)\) with \(h_k^*(p_{z_k})=0\).  Moreover every zero-face row for \(h_k^*\) is \(\rho\)-near \(u_k\).
+
+3.  For every such zero-face row \(z\) at any \(u_k\), the proved capacity/exchange tools give only the upper bound
+\[
+  \kappa \sum_{\{j:h_k^*(p_j)\ge \kappa\}}\max(P_{zj},0)
+  \le \nu_z\le \delta.
+\]
+Equivalently,
+\[
+  \sum_{\{j:h_k^*(p_j)\ge \kappa\}}\max(P_{zj},0)\le 4\tau.
+\]
+
+Thus for \(\tau<c_r/4\), the desired L7 conclusion is incompatible with row capacity unless the chain antecedent is already impossible.  The missing proof is precisely a no-chain argument, or equivalently a value/coefficient monotonicity argument forcing the row-capacity contradiction.
+
+### GAP-1 and GAP-2: missing standalone claims
+
+The missing monotonicity claim is the following.
+
+**GAP-1 (cross-exposer value/coefficient monotonicity).**  There exists a universal constant \(\delta_0>0\) such that the following holds in the Target L7 setting with the fixed threshold \(c_r=1/2\).  Let \(h_k^*\) be relative-interior optimal exposers at \(u_k\), and put
+\[
+  F_3^{\mathrm{deep}}
+  :=
+  \{f:\|p_f-p_{u_3}\|_1\ge4\tau,\ d_f>H-16\tau\}.
+\]
+If some hiddenness dual witness \((\lambda^{(3)},\alpha^{(3)},\beta^{(3)})\) at \(u_3\) has
+\[
+  \lambda^{(3)}(F_3^{\mathrm{deep}})>0,
+\]
+then at least one always-tight zero-face row \(z\in Z(u_k)\), for some \(k\le3\), satisfies
+\[
+  \sum_{\{j:h_k^*(p_j)\ge \kappa\}}\max(P_{zj},0)\ge c_r.
+\]
+
+There is also a separate applicability gap for producing the actor required by GAP-1:
+
+**GAP-2 (non-top third actor).**  In the Target L7 setting, \(u_3\) admits a hiddenness dual witness \((\lambda^{(3)},\alpha^{(3)},\beta^{(3)})\) with
+\[
+  \lambda^{(3)}(F_3^{\mathrm{deep}})>0.
+\]
+
+Together, GAP-1 and GAP-2 imply L7: GAP-2 supplies the third-hop deep far actor, and GAP-1 converts its existence into the required \(c_r\)-shipping conclusion.  I found no proved shard that supplies either claim, even with a larger height constant \(H>a\tau\).  The available tools locate zero-face blockers and top far witness rows, but they do not compare exposer values across different centers \(u_1,u_2,u_3\), they do not extend the third-actor theorem to non-top hidden vertices, and they do not lower-bound the positive coefficients \(P_{zj}^+\) of any zero-face row on a high slab.
+
+## §2 THE PROOF
+
+### Proof of the unconditional depth budget
+
+The function \(x\mapsto \operatorname{dist}_1(x,C_W)\) is \(1\)-Lipschitz in the \(\ell^1\) metric.  The chain inequalities give
+\[
+  \|p_{u_k}-p_v\|_1<4k\tau,\qquad k=1,2,3.
+\]
+Since \(d_v=H\), it follows that
+\[
+  d_{u_k}\ge H-\|p_{u_k}-p_v\|_1>H-4k\tau.
+\]
+For \(k\le3\), \(H>16\tau\) gives \(d_{u_k}>H-12\tau>4\tau\).  This uses only metric convexity and contains no packing or index-counting argument.
+
+### Proof of local zero-face anatomy
+
+Fix \(k\in\{1,2,3\}\).  Since \(u_k\) is hidden and \(t^*(u_k)>0\), we have \(0<t^*(u_k)<\kappa<\infty\).  Choose a relative-interior optimal exposer \(h_k^*\) at \(u_k\).  By the always-tight dual support contract, the always-tight far family \(T(u_k)\) is nonempty, and \(O(u_k)\) is nonempty because \(t^*(u_k)>0\).
+
+The always-tight hulls at \(u_k\) are disjoint by hypothesis.  Applying the separator zero-face obstruction to \(u_k\) gives a nonclone row \(z_k\) with
+\[
+  h_k^*(p_{z_k})=0.
+\]
+Because \(h_k^*\) is chosen in the relative interior of the optimal face, a lower-box constraint that is tight at \(h_k^*\) is tight on the whole optimal face; otherwise \(h_k^*\) would lie in a proper boundary face of the optimal face.  Hence \(z_k\in Z(u_k)\), the always-tight zero-face family.
+
+Finally, zero-face localization gives
+\[
+  \|p_z-p_{u_k}\|_1<4\tau
+\]
+for every row \(z\) with \(h_k^*(p_z)=0\).  This proves the local huddle/blocker part.  It does not imply any positive lower bound on the high-slab mass shipped by \(z\).
+
+### What row capacity gives, and why it does not close L7
+
+Let \(z\in Z(u_k)\).  Put \(g_j=h_k^*(p_j)\).  Since \(h_k^*\) is admissible and \(h_k^*(p_z)=0\), the zero-face exchange identity gives
+\[
+  \sum_j \max(P_{zj},0)g_j
+  =
+  \sum_j \max(-P_{zj},0)g_j
+  \le \nu_z\le \delta.
+\]
+Therefore, on the high slab \(A_k=\{j:g_j\ge\kappa\}\),
+\[
+  \kappa\sum_{j\in A_k}\max(P_{zj},0)
+  \le
+  \sum_j \max(P_{zj},0)g_j
+  \le \delta.
+\]
+Equivalently,
+\[
+  \sum_{j\in A_k}\max(P_{zj},0)\le \delta/\kappa=4\tau.
+\]
+
+This is an upper bound.  For \(\delta<(c_r/4)^2\), it rules out the L7 conclusion for any actually existing zero-face row.  Thus a proof of L7 at small \(\delta\) must prove that the whole three-hop chain antecedent is impossible.  The proved shards above do not do that.
+
+### Failed closing attempt and exact gap
+
+The intended depth-budget route would need to argue as follows.
+
+1.  The chain keeps \(u_1,u_2,u_3\) in successive near-top depth bands:
+\[
+  d_{u_1}>H-4\tau,\quad d_{u_2}>H-8\tau,\quad d_{u_3}>H-12\tau.
+\]
+
+2.  Disjointness at each \(u_k\) gives a local zero-face blocker \(z_k\in Z(u_k)\).
+
+3.  Hiddenness at the third hop should force a far actor in a compatible near-top slab.  This is GAP-2.
+
+4.  A value-monotonicity comparison should then force that actor, or a positive fraction of the relevant zero-face row's positive mass, to lie in \(\{h_k^*\ge\kappa\}\) for some earlier or current \(k\).  This is GAP-1.
+
+Step 4 is not available.  In fact, there are two precise obstructions to making it rigorous from the listed proved tools.
+
+First, the proved third-actor theorem is stated for a hidden top vertex.  The vertices \(u_1,u_2,u_3\) are deep and hidden, but they are not known to be hidden tops.  The metric depth estimate alone does not turn them into maximizers of \(d_i\), and the hiddenness-depth Markov proof is not directly portable to non-top vertices because the alpha part of a hiddenness witness has no universal bound.
+
+Second, even if a deep far actor at \(u_3\) were available, no proved shard converts that actor into positive coefficient mass from a zero-face row on any high slab \(\{h_k^*\ge\kappa\}\).  The available exact identity for zero-face rows is the exchange/capacity identity above, which bounds high-slab mass from above by \(4\tau\).  It supplies no lower bound.
+
+Therefore the proof stops at GAP-1/GAP-2.  Raising the height constant from \(16\) to a larger universal \(a\) gives more depth budget, but it does not create a non-top third-actor theorem, a cross-exposer comparison, or a coefficient lower bound; the same gap remains.
+
+## §3 TOOLS USED
+
+Only shards with status `proved` were used.
+
+- `def-signed-idempotent`: exact signed idempotent means \(P\mathbf 1=\mathbf 1\), \(P^2=P\), rows have total mass \(1\), and row geometry is measured in \(\ell^1\).
+
+- `def-negative-mass`: \(\delta(P)=\max_i\sum_j\max\{-P_{ij},0\}\).
+
+- `def-visible-set`: \(\tau=\sqrt\delta\), \(\rho=4\tau\), \(\kappa=\tau/4\), and \(W(P)\) is the set of \((\rho,\kappa)\)-exposed row vertices.
+
+- `def-exposed`: an admissible exposer \(h\) has \(h(p_v)=0\) and \(0\le h(p_j)\le1\) for every row; hidden means \(t^*(v)<\kappa\).
+
+- `def-height`: \(H(P)=\max_i\operatorname{dist}_1(p_i,C_W)\), and a hidden top \(v\) has \(d_v=H\).
+
+- `lem-always-tight-dual-support`: for the exposedness LP at a hidden geometrically distinct row vertex \(u\), \(T\) is nonempty, and \(O\) is nonempty iff \(t^*(u)>0\).
+
+- `lem-separator-zero-face-obstruction`: if \(0<t^*(u)<\infty\), \(h^*\) is a relative-interior optimal exposer, \(T,O\) are nonempty, and the always-tight hulls are disjoint, then there exists a nonclone row \(z\) with \(h^*(p_z)=0\).
+
+- `lem-zero-face-localization`: for a hidden geometrically distinct row vertex \(u\), every row \(z\) with \(h^*(p_z)=0\) for an optimal exposer \(h^*\) at \(u\) satisfies \(\|p_z-p_u\|_1<4\tau\).
+
+- `lem-zero-face-exchange-identity`: for a hidden geometrically distinct row vertex \(u\), optimal exposer \(h^*\), values \(g_j=h^*(p_j)\), and any row \(z\) with \(g_z=0\),
+\[
+  \sum_j\max(P_{zj},0)g_j=\sum_j\max(-P_{zj},0)g_j\le\nu_z\le\delta.
+\]
+
+- `lem-affine-exposer-row-capacity`: equivalently, for an admissible affine \(h\) with \(h(p_i)=0\), threshold \(\eta\ge0\), and \(F\subseteq\{j:h(p_j)\ge\eta\}\),
+\[
+  \eta\sum_{f\in F}\max(P_{if},0)\le\nu_i.
+\]
+
+- `lem-top-witness-third-actor`: consulted but not invoked at \(u_k\).  Its contract applies to a hidden top vertex \(v\), not to an arbitrary deep hidden chain vertex \(u_k\).
+
+## §4 HONEST ASSESSMENT
+
+The weakest point is not a minor constant loss; it is the missing structural bridge GAP-1, plus the non-top actor issue GAP-2.  The local huddle machinery is dimension-free and clone-invariant, but it remains local to each exposedness LP.  It does not order the values of \(h_1^*,h_2^*,h_3^*\) along the chain, and it does not couple hiddenness witness far actors to the positive row coefficients \(P_{zj}^+\) of a zero-face blocker.
+
+A refuter would attack exactly this point by trying to build a tall chain of mutually near hidden vertices whose zero-face rows keep all positive mass in low slabs.  The existing row-capacity identity is compatible with such starvation; it only says that high-slab mass is small when \(\delta\) is small.
+
+The decisive next step is a genuine cross-exposer monotonicity/coefficient lemma and a non-top third-actor extension: prove GAP-2, then prove GAP-1 showing that the third-hop far actor forces a universal amount of positive mass from some zero-face row in a \(\kappa\)-high slab.  Without those, L7 cannot be certified.

