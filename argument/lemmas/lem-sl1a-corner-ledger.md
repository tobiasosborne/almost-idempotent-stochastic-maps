---
id: lem-sl1a-corner-ledger
kind: lemma
contract: For every exact signed idempotent P with 0 < delta(P) <= 2^(-16) and nonempty visible set W, every hidden top vertex v of height H > 16sqrt(delta(P)), every affine phi with phi(p_v) = H, phi <= 0 on conv{p_w:w in W}, and |phi(a)-phi(b)| <= ||a-b||_1, every admissible exposer h at v, every row point f with ||p_f-p_v||_1 >= 4sqrt(delta(P)), d_f = dist_1(p_f,conv{p_w:w in W}) > H-4sqrt(delta(P)), and 2(H-phi(p_f))/D+h(p_f) <= 12sqrt(delta(P))/13 for D = 2+4delta(P), and every family xi_x(u) of probability weights on the geometrically distinct row vertices, constant on clone fibers, with p_x = sum_u xi_x(u)p_u for every row point x and xi_u Dirac at u for every vertex point u, the coupled measure Gamma_f(x,u) = (sum_{j:p_j=p_x} max(P_fj,0))xi_x(u) assigns at least 58079731/109051904 > 1/2 mass to C_f = {(x,u):H-phi(p_x) < 4sqrt(delta(P)), h(p_x) < 4sqrt(delta(P)), H-phi(p_u) < 4sqrt(delta(P)), h(p_u) < 4sqrt(delta(P))}, every (x,u) in C_f satisfies dist_1(p_x,conv{p_w:w in W}) > H-4sqrt(delta(P)) and dist_1(p_u,conv{p_w:w in W}) > H-4sqrt(delta(P)), and its vertex coordinate u is hidden.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-top-deficit-price; lem-harmonic-affine-bridge; lem-mass-split
status: proved
af: none
provenance: W56 wave (docs/waves/2026-07-09-W56-artifacts/): extracted from the twice-hostile-verified routine material of DECOMPOSITION-v2 (verdict-round1.md, verdict-round2.md); per-shard fresh hostile codex verdict in verdict-extraction.md (4 VALID + 6 VALID-WITH-CORRECTIONS, corrections applied and re-listed in the wave doc); reviewer != author throughout.
owner: B
---

# SL1a coupled coefficient-kernel corner ledger

## Statement

Let \(P\) be an exact signed idempotent with
\(0<\delta:=\delta(P)\le2^{-16}\), and put
\[
 \tau:=\sqrt\delta,\qquad D:=2+4\delta.
\]
Suppose \(W\neq\varnothing\), \(v\) is a hidden top vertex of height \(H>16\tau\), \(\phi\) is a top support functional at \(v\), \(z:=H-\phi\), and \(h\) is an admissible exposer at \(v\).  Let \(f\) be a row point satisfying
\[
 \|p_f-p_v\|_1\ge4\tau,qquad
 d_f:=\operatorname{dist}_1(p_f,\operatorname{conv}W)>H-4\tau,qquad
 \frac{2z(p_f)}D+h(p_f)\le\frac{12\tau}{13}.
\]

A legal vertex kernel is any family \(\xi_x(u)\) of probability weights on the geometrically distinct row vertices \(u\), constant on clone fibers, such that
\[
 p_x=\sum_u\xi_x(u)p_u
\]
for every row point \(x\), and such that \(\xi_u\) is the Dirac mass at \(u\) whenever \(p_u\) is a vertex point.  Aggregate
\[
 P_{fx}^{+}:=\sum_{j:p_j=p_x}\max(P_{fj},0)
\]
over the complete fiber of \(x\), define \(P_{fx}^{-}\) analogously using \(\max(-P_{fj},0)\), and for every legal vertex kernel define
\[
 \Gamma_f(x,u):=P_{fx}^{+}\xi_x(u)
\]
and
\[
 C_f:=\{(x,u):z(p_x)<4\tau,\ h(p_x)<4\tau,\ z(p_u)<4\tau,\ h(p_u)<4\tau\}.
\]
Then
\[
 \Gamma_f(C_f)\ge
 \frac{58079731}{109051904}
 =\frac12+\frac{3553779}{109051904}>\frac12.
\]
Moreover, both coordinates of every pair in \(C_f\) have depth strictly greater than \(H-4\tau\), and its vertex coordinate \(u\) is hidden.

## Proof

The existence of legal kernels is elementary: a finite polytope is the convex hull of its geometrically distinct extreme points, so each row point has such a convex representation; at a vertex the only representation supported on vertices is its Dirac mass.  We prove the estimate for an arbitrary legal kernel.

We first consume the proved contract `lem-top-deficit-price` verbatim:

> Top-deficit price: for an exact signed idempotent P with delta(P) > 0 and nonempty visible set W(P), a hidden top vertex v of height H, there exists a top support functional phi (affine, phi(p_v) = H, phi <= 0 on conv{p_w : w in W}, 1-Lipschitz for l1), and for ANY such phi, writing a_j = P_vj and z_j = H - phi(p_j) >= 0: for every subset A of row indices, sum over j in A of max(a_j,0)*z_j <= nu_v*(2+4*delta) <= delta*(2+4*delta); consequently for m >= 0, L >= 0, if sum over A of max(a_j,0) >= m and z_j >= L on A then m*L <= delta*(2+4*delta), and for delta <= 1/4, lambda > 0, theta < 1, positive v-row mass >= 1-theta on rows with z_j >= lambda*H forces H <= 3*delta/(lambda*(1-theta)), hence H <= 4*tau whenever delta <= min(1/4, (4*lambda*(1-theta)/3)^2).

Thus \(0\le z(p_x)\le D\) on the row set: the upper bound follows from the \(1\)-Lipschitz property and the row-diameter bound \(\|p_x-p_v\|_1\le D\).  Also \(0\le h(p_x)\le1\).

We next consume the proved shard `lem-harmonic-affine-bridge` verbatim:

> “Harmonic-affine bridge: for an exact signed idempotent P with rows p_i = (P_ij)_j, a vector g satisfies Pg = g if and only if there exists u with g_i = u . p_i for every row index i; in the forward direction u = g works (g_i = p_i . g), and the constant term of any affine representation is absorbable into u since all row sums equal 1.”

Both \(z\) and \(h\) are affine functions of row position, so their row-value vectors are \(P\)-harmonic.  Write
\[
 \nu_f:=\sum_j\max(-P_{fj},0),
 \qquad
 S_f:=\sum_xP_{fx}^{+}\bigl(z(p_x)+h(p_x)\bigr).
\]
Reproduction at the row \(f\), split into positive and negative coefficients, gives
\[
 \begin{aligned}
 S_f
 &=z(p_f)+h(p_f)
   +\sum_xP_{fx}^{-}\bigl(z(p_x)+h(p_x)\bigr)\\
 &\le z(p_f)+h(p_f)+\nu_f(D+1).
 \end{aligned}
\]
Since \(D\ge2\),
\[
 z(p_f)+h(p_f)
 \le\frac D2\left(\frac{2z(p_f)}D+h(p_f)\right)
 \le\frac{6D\tau}{13},
\]
and hence
\[
 S_f\le\frac{6D\tau}{13}+\nu_f(D+1). \tag{1}
\]

We also consume the proved shard `lem-mass-split` verbatim:

> “Mass split: for an exact signed idempotent P and any row index v, writing a_j = P_{vj}, a_j^+ = max(a_j, 0), a_j^- = max(-a_j, 0), and nu_v = sum_j a_j^-, one has sum_j a_j^+ = 1 + nu_v.”

Applied at \(f\), this says
\[
 \Gamma_f(1)=\sum_xP_{fx}^{+}=1+\nu_f. \tag{2}
\]
Put \(q:=z+h\).  The \(x\)-marginal has \(q\)-moment \(S_f\).  For the \(u\)-marginal, affinity and the defining barycentric identity for \(\xi_x\) give
\[
 \begin{aligned}
 \int q(p_u)\,d\Gamma_f(x,u)
 &=\sum_xP_{fx}^{+}\sum_u\xi_x(u)q(p_u)\\
 &=\sum_xP_{fx}^{+}q(p_x)=S_f. \tag{3}
 \end{aligned}
\]

If the \(x\)-coordinate fails its two corner inequalities, then \(q(p_x)\ge4\tau\); hence that bad-coordinate mass is at most \(S_f/(4\tau)\).  Equation (3) gives the same bound for failure on the \(u\)-coordinate.  The union bound, (1), and (2) yield
\[
 \begin{aligned}
 \Gamma_f(C_f)
 &\ge1+\nu_f-\frac{S_f}{2\tau}\\
 &\ge1-\frac{3D}{13}-\frac{\nu_f(D+1)}{2\tau}\\
 &\ge1-\frac{3D}{13}-\frac{\tau(D+1)}2, \tag{4}
 \end{aligned}
\]
where the last step uses \(\nu_f\le\delta=\tau^2\).  The right side decreases with \(\tau\) on the stated interval.  At \(\tau=1/256\) and \(D=2+2^{-14}=32769/16384\), it equals
\[
 1-\frac3{13}\frac{32769}{16384}
   -\frac1{512}\left(\frac{32769}{16384}+1\right)
 =\frac{58079731}{109051904}>\frac12.
\]

Finally, for any row point \(y\), the support and Lipschitz properties of \(\phi\) give \(\phi(p_y)\le d_y\): for every \(c\in\operatorname{conv}W\),
\(\phi(p_y)\le\phi(c)+\|p_y-c\|_1\le\|p_y-c\|_1\), and one takes the infimum.  Therefore
\[
 H-d_y\le z(p_y).
\]
The inequality \(z(p_y)<4\tau\) implies \(d_y>H-4\tau\) strictly.  This applies to both coordinates in \(C_f\).  Since \(H-4\tau>12\tau>0\), its vertex coordinate has positive distance from \(\operatorname{conv}W\), so it is not visible and is therefore hidden.

## Notes

The proof is universal over legal kernels and never replaces the \(u\)-marginal by literal transition mass off the diagonal.  All coefficient masses are full-fiber sums, so the statement is clone-invariant.  Under the standard transient-row extension, old coefficient fibers acquire a zero new column and the same two-marginal proof applies; the appended row is already a convex combination of the embedded old row points.
