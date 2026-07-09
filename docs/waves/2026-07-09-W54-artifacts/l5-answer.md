VERDICT: BLOCKED — L5 reduces cleanly to a linear minimax problem on the top dual face, but no proved shard supplies the required dimension-free mass-minimax/finite-cover claim.
sections ['## §1 THE STATEMENT(S)', '## §2 THE PROOF', '## §3 TOOLS USED', '## §4 HONEST ASSESSMENT']
conjecture False
proved-mod-audit True
numerical True
heuristic True
stated True
disproved True

diff --git a/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l5/ANSWER.md b/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l5/ANSWER.md
new file mode 100644
index 0000000000000000000000000000000000000000..55c28ee0751caa0260296c33240913b031515d5c
--- /dev/null
+++ b/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l5/ANSWER.md
@@ -0,0 +1,131 @@
+VERDICT: BLOCKED — L5 reduces cleanly to a linear minimax problem on the top dual face, but no proved shard supplies the required dimension-free mass-minimax/finite-cover claim.
+
+## §1 THE STATEMENT(S)
+
+Fix the W54 branch threshold \(c_m\in(0,1)\).  Let \(P\) be an exact signed idempotent with
+\(\delta=\delta(P)>0\), \(\tau=\sqrt\delta\), nonempty visible set \(W=W(P)\), visible hull
+\(C_W\), and hidden top vertex \(v\) of height \(H\).  Write
+\[
+  d_j=\operatorname{dist}_1(p_j,C_W),\qquad w_j=P_{vj}^+=\max(P_{vj},0).
+\]
+
+**Target L5(c_m), not proved here.**  There should exist universal constants
+\(c_5>0\) and \(\delta_0>0\) such that whenever
+\[
+  0<\delta\le\delta_0,\qquad H>16\tau,
+\]
+and
+\[
+  A\subseteq\{j:\|p_j-p_v\|_1\ge 4\tau,\ d_j>H-8\tau\},\qquad
+  S_A:=\sum_{j\in A}w_j\ge c_m,
+\]
+there is a top support functional \(\phi\) at \(v\) with
+\[
+  \sum_{j\in A} w_j\,\bigl(H-\phi(p_j)\bigr)\ge c_5\,\tau\,c_m .
+\]
+
+**Conditional cover lemma, proved here.**  Suppose there are universal constants
+\(\eta>0\), \(N\in\mathbb N\), and \(\delta_0>0\) such that every configuration satisfying the
+antecedent of L5(c_m) admits \(y_1,\ldots,y_N\in Y_v\) with the covering property
+\[
+  \forall j\in A\quad \max_{1\le r\le N} y_r\cdot(p_v-p_j)\ge \eta\tau ,
+\]
+where \(Y_v\) is the top dual face of `lem-top-support-dual-face`.  Then L5(c_m) holds
+with \(c_5=\eta/N\) and the same \(\delta_0\).
+
+## §2 THE PROOF
+
+By `lem-top-support-dual-face`, on the row set every top support functional has the form
+\[
+  \phi_y(x)=y\cdot x-h_C(y),\qquad y\in Y_v,
+\]
+where
+\[
+  Y_v=\{y:\|y\|_\infty\le 1,\ y\cdot p_v-h_C(y)=H\}.
+\]
+Therefore for every row \(j\),
+\[
+  H-\phi_y(p_j)
+  = (y\cdot p_v-h_C(y))-(y\cdot p_j-h_C(y))
+  = y\cdot(p_v-p_j).
+\]
+Thus the L5 objective for a fixed set \(A\) is exactly the linear functional
+\[
+  L_A(y):=\sum_{j\in A}w_j\,y\cdot(p_v-p_j)
+\]
+maximized over \(Y_v\).  This is the correct minimax formulation.  It also shows why
+rowwise choices \(y_j\) cannot be averaged without an additional structural claim: the desired
+quantity is \(\sup_y \sum_j w_j z_j(y)\), not \(\sum_j w_j\sup_y z_j(y)\).
+
+Now assume the conditional cover hypothesis.  For each \(j\in A\), choose one
+\(r(j)\in\{1,\ldots,N\}\) such that
+\[
+  y_{r(j)}\cdot(p_v-p_j)\ge \eta\tau.
+\]
+Let \(A_r=\{j\in A:r(j)=r\}\).  Since \(\sum_r\sum_{j\in A_r}w_j=S_A\ge c_m\), some
+\(r_0\) has
+\[
+  \sum_{j\in A_{r_0}}w_j\ge S_A/N\ge c_m/N.
+\]
+Let \(\phi_{r_0}=\phi_{y_{r_0}}\).  By `lem-top-deficit-price`, every top support
+functional has nonnegative deficits on rows:
+\[
+  H-\phi_{r_0}(p_j)\ge 0.
+\]
+Consequently,
+\[
+\begin{aligned}
+  \sum_{j\in A}w_j\bigl(H-\phi_{r_0}(p_j)\bigr)
+  &\ge \sum_{j\in A_{r_0}}w_j\bigl(H-\phi_{r_0}(p_j)\bigr)\\
+  &= \sum_{j\in A_{r_0}}w_j\,y_{r_0}\cdot(p_v-p_j)\\
+  &\ge \eta\tau \sum_{j\in A_{r_0}}w_j\\
+  &\ge (\eta/N)\tau c_m.
+\end{aligned}
+\]
+This proves the conditional cover lemma.
+
+**GAP-1 (far-deep mass minimax / universal cover).**  Prove, from exact signed
+idempotence plus the simultaneous conditions
+\[
+  \|p_j-p_v\|_1\ge4\tau,\qquad d_j>H-8\tau,\qquad j\in A,
+\]
+that there are universal \(\eta>0\), \(N<\infty\), and \(\delta_0>0\) for which the above
+covering property holds; equivalently, prove the weaker direct minimax form
+\[
+  \sup_{y\in Y_v}\sum_{j\in A}\frac{w_j}{S_A}\,y\cdot(p_v-p_j)\ge \gamma\tau
+\]
+with a universal \(\gamma>0\).
+
+I do not know how to prove GAP-1 from the available proved shards.  The pointwise
+statement \(Z_v(j)=\sup_{y\in Y_v}y\cdot(p_v-p_j)\ge c\tau\) for each \(j\in A\), even if
+assumed, only gives a serving family whose size may grow with the number of geometrically
+distinct rows in \(A\).  That is exactly the non-clone-invariant, dimension-dependent failure
+mode flagged in the L5 prompt.
+
+## §3 TOOLS USED
+
+- `lem-top-support-dual-face` (status `proved`): used the contract clause that
+  \(\Phi_v\) is exactly \(\{\phi_y(x)=y\cdot x-h_C(y):y\in Y_v\}\) on the row set, and that
+  \(Z_v(f)=\sup_{y\in Y_v}y\cdot(p_v-p_f)\).
+- `lem-top-deficit-price` (status `proved`): used the contract clause that for any top
+  support functional \(\phi\), \(z_j=H-\phi(p_j)\ge0\) for every row \(j\).
+- Definitions used for notation: `def-signed-idempotent`, `def-negative-mass`,
+  `def-visible-set`, `def-exposed`, and `def-height`.
+
+No conjectural, numerical, heuristic, stated, disproved, or `proved-mod-audit` shard is used as
+a proof input.
+
+## §4 HONEST ASSESSMENT
+
+The weakest point is not a hidden calculation; it is exactly GAP-1.  The proved dual-face
+reframe makes L5 a concrete linear program over \(Y_v\), but it does not bound the number or
+spread of exposed directions needed to see all far-deep rows carrying \(P_v^+\)-mass.
+
+A refuter should attack by constructing, inside an exact signed idempotent, many rho-far
+co-top rows whose deficits are supported on many different extreme points of \(Y_v\), so that
+each row has large pointwise \(Z_v(j)\) but every single \(y\in Y_v\) sees only a small
+\(P_v^+\)-weighted fraction.
+
+The decisive next step is a dimension-free, clone-invariant theorem saying that the far-deep
+annulus of an exact signed idempotent admits a universal-size serving family in \(Y_v\), or
+directly the normalized minimax lower bound in GAP-1.  Without that, L5 remains open.

codex
One wording issue in the gap statement overstated an equivalence between the finite-cover version and the direct minimax version. I’m tightening that so the file does not claim more than was proved.
apply patch
patch: completed
/tmp/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l5/ANSWER.md
diff --git a/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l5/ANSWER.md b/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l5/ANSWER.md
new file mode 100644
index 0000000000000000000000000000000000000000..c8abe882f1fffc270c0c7d025f4ba9d688cd5ac3
--- /dev/null
+++ b/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l5/ANSWER.md
@@ -0,0 +1,131 @@
+VERDICT: BLOCKED — L5 reduces cleanly to a linear minimax problem on the top dual face, but no proved shard supplies the required dimension-free mass-minimax/finite-cover claim.
+
+## §1 THE STATEMENT(S)
+
+Fix the W54 branch threshold \(c_m\in(0,1)\).  Let \(P\) be an exact signed idempotent with
+\(\delta=\delta(P)>0\), \(\tau=\sqrt\delta\), nonempty visible set \(W=W(P)\), visible hull
+\(C_W\), and hidden top vertex \(v\) of height \(H\).  Write
+\[
+  d_j=\operatorname{dist}_1(p_j,C_W),\qquad w_j=P_{vj}^+=\max(P_{vj},0).
+\]
+
+**Target L5(c_m), not proved here.**  There should exist universal constants
+\(c_5>0\) and \(\delta_0>0\) such that whenever
+\[
+  0<\delta\le\delta_0,\qquad H>16\tau,
+\]
+and
+\[
+  A\subseteq\{j:\|p_j-p_v\|_1\ge 4\tau,\ d_j>H-8\tau\},\qquad
+  S_A:=\sum_{j\in A}w_j\ge c_m,
+\]
+there is a top support functional \(\phi\) at \(v\) with
+\[
+  \sum_{j\in A} w_j\,\bigl(H-\phi(p_j)\bigr)\ge c_5\,\tau\,c_m .
+\]
+
+**Conditional cover lemma, proved here.**  Suppose there are universal constants
+\(\eta>0\), \(N\in\mathbb N\), and \(\delta_0>0\) such that every configuration satisfying the
+antecedent of L5(c_m) admits \(y_1,\ldots,y_N\in Y_v\) with the covering property
+\[
+  \forall j\in A\quad \max_{1\le r\le N} y_r\cdot(p_v-p_j)\ge \eta\tau ,
+\]
+where \(Y_v\) is the top dual face of `lem-top-support-dual-face`.  Then L5(c_m) holds
+with \(c_5=\eta/N\) and the same \(\delta_0\).
+
+## §2 THE PROOF
+
+By `lem-top-support-dual-face`, on the row set every top support functional has the form
+\[
+  \phi_y(x)=y\cdot x-h_C(y),\qquad y\in Y_v,
+\]
+where
+\[
+  Y_v=\{y:\|y\|_\infty\le 1,\ y\cdot p_v-h_C(y)=H\}.
+\]
+Therefore for every row \(j\),
+\[
+  H-\phi_y(p_j)
+  = (y\cdot p_v-h_C(y))-(y\cdot p_j-h_C(y))
+  = y\cdot(p_v-p_j).
+\]
+Thus the L5 objective for a fixed set \(A\) is exactly the linear functional
+\[
+  L_A(y):=\sum_{j\in A}w_j\,y\cdot(p_v-p_j)
+\]
+maximized over \(Y_v\).  This is the correct minimax formulation.  It also shows why
+rowwise choices \(y_j\) cannot be averaged without an additional structural claim: the desired
+quantity is \(\sup_y \sum_j w_j z_j(y)\), not \(\sum_j w_j\sup_y z_j(y)\).
+
+Now assume the conditional cover hypothesis.  For each \(j\in A\), choose one
+\(r(j)\in\{1,\ldots,N\}\) such that
+\[
+  y_{r(j)}\cdot(p_v-p_j)\ge \eta\tau.
+\]
+Let \(A_r=\{j\in A:r(j)=r\}\).  Since \(\sum_r\sum_{j\in A_r}w_j=S_A\ge c_m\), some
+\(r_0\) has
+\[
+  \sum_{j\in A_{r_0}}w_j\ge S_A/N\ge c_m/N.
+\]
+Let \(\phi_{r_0}=\phi_{y_{r_0}}\).  By `lem-top-deficit-price`, every top support
+functional has nonnegative deficits on rows:
+\[
+  H-\phi_{r_0}(p_j)\ge 0.
+\]
+Consequently,
+\[
+\begin{aligned}
+  \sum_{j\in A}w_j\bigl(H-\phi_{r_0}(p_j)\bigr)
+  &\ge \sum_{j\in A_{r_0}}w_j\bigl(H-\phi_{r_0}(p_j)\bigr)\\
+  &= \sum_{j\in A_{r_0}}w_j\,y_{r_0}\cdot(p_v-p_j)\\
+  &\ge \eta\tau \sum_{j\in A_{r_0}}w_j\\
+  &\ge (\eta/N)\tau c_m.
+\end{aligned}
+\]
+This proves the conditional cover lemma.
+
+**GAP-1 (far-deep mass minimax / universal cover).**  Prove, from exact signed
+idempotence plus the simultaneous conditions
+\[
+  \|p_j-p_v\|_1\ge4\tau,\qquad d_j>H-8\tau,\qquad j\in A,
+\]
+that there are universal \(\eta>0\), \(N<\infty\), and \(\delta_0>0\) for which the above
+covering property holds.  A weaker, still sufficient direct minimax form is
+\[
+  \sup_{y\in Y_v}\sum_{j\in A}\frac{w_j}{S_A}\,y\cdot(p_v-p_j)\ge \gamma\tau
+\]
+with a universal \(\gamma>0\).
+
+I do not know how to prove GAP-1 from the available proved shards.  The pointwise
+statement \(Z_v(j)=\sup_{y\in Y_v}y\cdot(p_v-p_j)\ge c\tau\) for each \(j\in A\), even if
+assumed, only gives a serving family whose size may grow with the number of geometrically
+distinct rows in \(A\).  That is exactly the non-clone-invariant, dimension-dependent failure
+mode flagged in the L5 prompt.
+
+## §3 TOOLS USED
+
+- `lem-top-support-dual-face` (status `proved`): used the contract clause that
+  \(\Phi_v\) is exactly \(\{\phi_y(x)=y\cdot x-h_C(y):y\in Y_v\}\) on the row set, and that
+  \(Z_v(f)=\sup_{y\in Y_v}y\cdot(p_v-p_f)\).
+- `lem-top-deficit-price` (status `proved`): used the contract clause that for any top
+  support functional \(\phi\), \(z_j=H-\phi(p_j)\ge0\) for every row \(j\).
+- Definitions used for notation: `def-signed-idempotent`, `def-negative-mass`,
+  `def-visible-set`, `def-exposed`, and `def-height`.
+
+No conjectural, numerical, heuristic, stated, disproved, or `proved-mod-audit` shard is used as
+a proof input.
+
+## §4 HONEST ASSESSMENT
+
+The weakest point is not a hidden calculation; it is exactly GAP-1.  The proved dual-face
+reframe makes L5 a concrete linear program over \(Y_v\), but it does not bound the number or
+spread of exposed directions needed to see all far-deep rows carrying \(P_v^+\)-mass.
+
+A refuter should attack by constructing, inside an exact signed idempotent, many rho-far
+co-top rows whose deficits are supported on many different extreme points of \(Y_v\), so that
+each row has large pointwise \(Z_v(j)\) but every single \(y\in Y_v\) sees only a small
+\(P_v^+\)-weighted fraction.
+
+The decisive next step is a dimension-free, clone-invariant theorem saying that the far-deep
+annulus of an exact signed idempotent admits a universal-size serving family in \(Y_v\), or
+directly the normalized minimax lower bound in GAP-1.  Without that, L5 remains open.

diff --git a/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l5/ANSWER.md b/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l5/ANSWER.md
new file mode 100644
index 0000000000000000000000000000000000000000..c8abe882f1fffc270c0c7d025f4ba9d688cd5ac3
--- /dev/null
+++ b/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/097b0b37-ee98-4b04-b67a-fda0147d95df/scratchpad/w54/l5/ANSWER.md
@@ -0,0 +1,131 @@
+VERDICT: BLOCKED — L5 reduces cleanly to a linear minimax problem on the top dual face, but no proved shard supplies the required dimension-free mass-minimax/finite-cover claim.
+
+## §1 THE STATEMENT(S)
+
+Fix the W54 branch threshold \(c_m\in(0,1)\).  Let \(P\) be an exact signed idempotent with
+\(\delta=\delta(P)>0\), \(\tau=\sqrt\delta\), nonempty visible set \(W=W(P)\), visible hull
+\(C_W\), and hidden top vertex \(v\) of height \(H\).  Write
+\[
+  d_j=\operatorname{dist}_1(p_j,C_W),\qquad w_j=P_{vj}^+=\max(P_{vj},0).
+\]
+
+**Target L5(c_m), not proved here.**  There should exist universal constants
+\(c_5>0\) and \(\delta_0>0\) such that whenever
+\[
+  0<\delta\le\delta_0,\qquad H>16\tau,
+\]
+and
+\[
+  A\subseteq\{j:\|p_j-p_v\|_1\ge 4\tau,\ d_j>H-8\tau\},\qquad
+  S_A:=\sum_{j\in A}w_j\ge c_m,
+\]
+there is a top support functional \(\phi\) at \(v\) with
+\[
+  \sum_{j\in A} w_j\,\bigl(H-\phi(p_j)\bigr)\ge c_5\,\tau\,c_m .
+\]
+
+**Conditional cover lemma, proved here.**  Suppose there are universal constants
+\(\eta>0\), \(N\in\mathbb N\), and \(\delta_0>0\) such that every configuration satisfying the
+antecedent of L5(c_m) admits \(y_1,\ldots,y_N\in Y_v\) with the covering property
+\[
+  \forall j\in A\quad \max_{1\le r\le N} y_r\cdot(p_v-p_j)\ge \eta\tau ,
+\]
+where \(Y_v\) is the top dual face of `lem-top-support-dual-face`.  Then L5(c_m) holds
+with \(c_5=\eta/N\) and the same \(\delta_0\).
+
+## §2 THE PROOF
+
+By `lem-top-support-dual-face`, on the row set every top support functional has the form
+\[
+  \phi_y(x)=y\cdot x-h_C(y),\qquad y\in Y_v,
+\]
+where
+\[
+  Y_v=\{y:\|y\|_\infty\le 1,\ y\cdot p_v-h_C(y)=H\}.
+\]
+Therefore for every row \(j\),
+\[
+  H-\phi_y(p_j)
+  = (y\cdot p_v-h_C(y))-(y\cdot p_j-h_C(y))
+  = y\cdot(p_v-p_j).
+\]
+Thus the L5 objective for a fixed set \(A\) is exactly the linear functional
+\[
+  L_A(y):=\sum_{j\in A}w_j\,y\cdot(p_v-p_j)
+\]
+maximized over \(Y_v\).  This is the correct minimax formulation.  It also shows why
+rowwise choices \(y_j\) cannot be averaged without an additional structural claim: the desired
+quantity is \(\sup_y \sum_j w_j z_j(y)\), not \(\sum_j w_j\sup_y z_j(y)\).
+
+Now assume the conditional cover hypothesis.  For each \(j\in A\), choose one
+\(r(j)\in\{1,\ldots,N\}\) such that
+\[
+  y_{r(j)}\cdot(p_v-p_j)\ge \eta\tau.
+\]
+Let \(A_r=\{j\in A:r(j)=r\}\).  Since \(\sum_r\sum_{j\in A_r}w_j=S_A\ge c_m\), some
+\(r_0\) has
+\[
+  \sum_{j\in A_{r_0}}w_j\ge S_A/N\ge c_m/N.
+\]
+Let \(\phi_{r_0}=\phi_{y_{r_0}}\).  By `lem-top-deficit-price`, every top support
+functional has nonnegative deficits on rows:
+\[
+  H-\phi_{r_0}(p_j)\ge 0.
+\]
+Consequently,
+\[
+\begin{aligned}
+  \sum_{j\in A}w_j\bigl(H-\phi_{r_0}(p_j)\bigr)
+  &\ge \sum_{j\in A_{r_0}}w_j\bigl(H-\phi_{r_0}(p_j)\bigr)\\
+  &= \sum_{j\in A_{r_0}}w_j\,y_{r_0}\cdot(p_v-p_j)\\
+  &\ge \eta\tau \sum_{j\in A_{r_0}}w_j\\
+  &\ge (\eta/N)\tau c_m.
+\end{aligned}
+\]
+This proves the conditional cover lemma.
+
+**GAP-1 (far-deep mass minimax / universal cover).**  Prove, from exact signed
+idempotence plus the simultaneous conditions
+\[
+  \|p_j-p_v\|_1\ge4\tau,\qquad d_j>H-8\tau,\qquad j\in A,
+\]
+that there are universal \(\eta>0\), \(N<\infty\), and \(\delta_0>0\) for which the above
+covering property holds.  A weaker, still sufficient direct minimax form is
+\[
+  \sup_{y\in Y_v}\sum_{j\in A}\frac{w_j}{S_A}\,y\cdot(p_v-p_j)\ge \gamma\tau
+\]
+with a universal \(\gamma>0\).
+
+I do not know how to prove GAP-1 from the available proved shards.  The pointwise
+statement \(Z_v(j)=\sup_{y\in Y_v}y\cdot(p_v-p_j)\ge c\tau\) for each \(j\in A\), even if
+assumed, only gives a serving family whose size may grow with the number of geometrically
+distinct rows in \(A\).  That is exactly the non-clone-invariant, dimension-dependent failure
+mode flagged in the L5 prompt.
+
+## §3 TOOLS USED
+
+- `lem-top-support-dual-face` (status `proved`): used the contract clause that
+  \(\Phi_v\) is exactly \(\{\phi_y(x)=y\cdot x-h_C(y):y\in Y_v\}\) on the row set, and that
+  \(Z_v(f)=\sup_{y\in Y_v}y\cdot(p_v-p_f)\).
+- `lem-top-deficit-price` (status `proved`): used the contract clause that for any top
+  support functional \(\phi\), \(z_j=H-\phi(p_j)\ge0\) for every row \(j\).
+- Definitions used for notation: `def-signed-idempotent`, `def-negative-mass`,
+  `def-visible-set`, `def-exposed`, and `def-height`.
+
+No conjectural, numerical, heuristic, stated, disproved, or `proved-mod-audit` shard is used as
+a proof input.
+
+## §4 HONEST ASSESSMENT
+
+The weakest point is not a hidden calculation; it is exactly GAP-1.  The proved dual-face
+reframe makes L5 a concrete linear program over \(Y_v\), but it does not bound the number or
+spread of exposed directions needed to see all far-deep rows carrying \(P_v^+\)-mass.
+
+A refuter should attack by constructing, inside an exact signed idempotent, many rho-far
+co-top rows whose deficits are supported on many different extreme points of \(Y_v\), so that
+each row has large pointwise \(Z_v(j)\) but every single \(y\in Y_v\) sees only a small
+\(P_v^+\)-weighted fraction.
+
+The decisive next step is a dimension-free, clone-invariant theorem saying that the far-deep
+annulus of an exact signed idempotent admits a universal-size serving family in \(Y_v\), or
+directly the normalized minimax lower bound in GAP-1.  Without that, L5 remains open.

