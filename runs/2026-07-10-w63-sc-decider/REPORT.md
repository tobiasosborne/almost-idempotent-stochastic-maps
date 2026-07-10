# W63 S/C exact decider report

This is **L3 exact constructive/numerical evidence only**. It is not a proof of
S, C, a universal obstruction, or L5-GAP-1. Here BLOCKED means blocked only in
the explicitly tested factorized families.

The verifier is [search.py](search.py), and its frozen exact output is
[certificates.json](certificates.json). Every matrix is checked entrywise over
fractions.Fraction for \(P^2=P\) and row sums one. Every claimed negative mass,
fiber, visibility/hiddenness certificate, primal/dual height certificate,
quotient barycenter, ray pair, local-center bound, \(r_\omega\), scalar width,
chord, and engine payment is an exact assertion. Rejected completions are
explicitly labeled and are never reported as L5 data.

## Verdicts

- **S shallow-counterweight completion — BLOCKED.** In the W61 factorized
  family, hiddenness gives
  \[
  H=\frac{2\varepsilon t^*}{1+\varepsilon-\varepsilon t^*},
  \qquad t^*<\tau/4,
  \]
  so the legal seed has cubic height. The exact receiver attachment also binds
  at \(q+m_{\rm sh}+S\le\tau^2\): for \(S=1/4\),
  \(m_{\rm sh}=\tau S/16\) eventually exceeds the available budget
  \(\tau^2-q\). A formal height dial toward \(H/\tau=16\) leaves the convex
  closest face and makes the proposed top visible.
- **C two-prong engine-financing bouquet — BLOCKED.** The width bouquet
  satisfies C's full center-uniform antecedent, the width branch, weighted
  chord, and actual same-carrier payment, with
  \(Z_v(q_A)/\tau=2\tau\to0\). Its sole failed L5 gate is tallness:
  \(H=2\tau^2<16\tau\). The separate drift routing cannot move constant
  ballast mass to a near reusable payer because exact factorization forces
  \(\nu_b=u/4\le\tau^2\), hence \(u\le4\tau^2\).

No genuine L5 datum was found, and there was no node-I by-catch.

## 1. Shape S: W61 seed plus shallow receiver

### Exact factorization and seed

The construction uses affine coordinates \(A,C,D\). Put
\[
\varepsilon=\tau^2/2,\quad \eta=\varepsilon t^*,\quad
\alpha=1+\varepsilon-\eta,\quad q=\varepsilon/\alpha.
\]
The W61 rows have coordinates
\[
L_A=(1,0,0),\quad L_Z=(\alpha,\eta,-\varepsilon),\quad
L_C=(0,1,0),\quad L_D=(0,0,1),
\]
with \(X=(1-\theta)A+\theta C\). The script constructs \(P=LB\) and checks
\(BL=I_3\). For \(t^*=\tau/8\), it checks the exact hiddenness balance
\[
(p_D-p_A)+\varepsilon^{-1}(p_Z-p_A)=t^*(p_C-p_A),
\]
and matching primal/dual certificates give
\[
H=\frac{2\eta}{\alpha}
 =\frac{\tau^3/8}{1+\tau^2/2-\tau^3/16}.
\]

The tested seed trace is:

| \(\tau\) | \(H/\tau\) | \(H-16\tau\) |
|---|---:|---:|
| \(1/32\) | \(64/524543\) | \(-524539/1049086\) |
| \(1/64\) | \(128/4194815\) | \(-4194807/16779260\) |
| \(1/128\) | \(256/33555455\) | \(-33555439/268443640\) |
| \(1/256\) | \(512/268437503\) | \(-268437471/4295000048\) |

Thus the legal seed has \(H/\tau\to0\), not 16.

### Receiver attachment and the binding coefficient inequality

I added one clone of \(C\) as the proposed shallow receiver and one clone of
\(D\) as the far actor. In the first row of \(B\), the pairs are
\[
(-m_{\rm sh},+m_{\rm sh})\text{ on the \(C\) fiber},\qquad
(-S,+S)\text{ on the \(D\) fiber}.
\]
This preserves \(BL=I\) and idempotence exactly, while exposing the budget
\[
\nu_A=q+m_{\rm sh}+S,\qquad
m_{\rm sh}=\frac{\tau S}{16},\qquad S=\frac14.
\]

At \(\tau=1/256\),
\[
m_{\rm sh}=\frac1{16384},\qquad
\tau^2-q=\frac{134219775}{17592320196608},
\]
so the shallow floor alone exceeds the spare top-row budget by
\[
\frac{939530237}{17592320196608}>0.
\]
With the actor clone included, the completed exact projection has
\[
\delta(P)-\tau^2=\frac{1099788433407}{4398046511104}>0.
\]
At \(\tau=1/32\), the shallow term alone is below the spare budget by only
\(255/1074264064\), but the \(S=1/4\) actor term already violates it. For every
tested \(\tau\le1/64\), the shallow term alone violates it.

This is clone-safe for this ansatz: positive mass is counted before fiber
aggregation, while the compensating negative clone is charged to the row's
true negative mass.

### Sweep toward \(H/\tau=16\)

At \(\tau=1/256\), I solved the formal W61 face equation
\[
\frac{2\eta}{1+\varepsilon-\eta}=R\tau.
\]
The old \(Z,D\) closest-point weights would be
\((1/\alpha,1-1/\alpha)\). Every tall target has negative \(D\)-weight, so
the primal certificate has left the convex face. Independently, the exact
fixed affine values
\[
h(A)=0,\ h(Z)=\eta-\varepsilon,\ h(C)=h(D)=1,\ h(X)=1/64
\]
give an admissible exposer with far margin \(1/64>\kappa=1/1024\), proving
that the proposed top is visible in every dialed matrix.

| requested \(R\) | formal \(R\tau\) | failed \(D\)-weight | \(\eta/\varepsilon-\kappa\) | far margin |
|---:|---:|---:|---:|---:|
| \(20\) | \(5/64\) | \(-5119/131073\) | \(671093627/136192\) | \(1/64\) |
| \(18\) | \(9/128\) | \(-4607/131073\) | \(1207968503/271360\) | \(1/64\) |
| \(17\) | \(17/256\) | \(-4351/131073\) | \(2281718255/541696\) | \(1/64\) |
| \(33/2\) | \(33/512\) | \(-4223/131073\) | \(4429217759/1082368\) | \(1/64\) |
| \(16\) | \(1/16\) | \(-1365/43691\) | \(44739573/11264\) | \(1/64\) |

The exact first failures are therefore a negative closest-face weight and a
visible rather than hidden top. The attachment independently fails the
global \(\tau^2\) negativity budget.

## 2. Shape C: width bouquet and drift routing

### Width branch: complete near-refuter except tallness

For even \(m\), use indices \(v,q_1,\ldots,q_m,b,f\), make every row except
\(v\) a coordinate row, and set
\[
P_{vq_i}=\frac1{4m},\qquad P_{vb}=\frac34+\delta,\qquad
P_{vf}=-\delta,\qquad\delta=\tau^2.
\]
The script tests \(m=4\) and
\(\tau=1/32,1/64,1/128,1/256\). Full exact visibility certificates are
recorded. The hiddenness value is \(t^*(v)=\delta/(1+\delta)<\kappa\), and
matching closest-point/dual certificates give \(H=2\delta\).

Take \(A=\{q_1,\ldots,q_m\}\). Then \(S=1/4\),
\(q_A=m^{-1}\sum_i p_{q_i}\), and all selected fibers lie in \(G_v\).
Because \(H-8\tau<0\), \(\mathrm{Sh}_v=\varnothing\). For every local center
\(\|c-p_v\|_1\le1/4\), reverse triangle inequality puts every selected actor
strictly outside \(B_1(c,1/2)\). Thus
\[
P_v^+(E_c\cap G_v)\ge\frac14>\frac{\tau S}{16},\qquad
P_v^+(E_c\cap\mathrm{Sh}_v)=0<\frac{\tau S}{16}.
\]
This checks C's for-all-local-centers antecedent and exceeds R3's floor.

The ray formula is minimized by \(\Lambda=3,c=p_b\). Its objective and a
feasible top-face value both equal
\[
Z_v(q_A)=2\delta,\qquad Z_v(q_A)/\tau=2\tau\to0.
\]
For \(\omega=P_v^+|_{G_v}\), exact extreme-sign enumeration gives
\[
\|r_\omega-p_v\|_1=2\delta<\frac18,\qquad
\Omega(\omega)=\frac{3+4\delta}{4(1+\delta)^2}>\frac1{16}.
\]
This enters C through width, not drift. Its optimizer constructs conditional
barycenters satisfying
\[
s_+s_-\|q_+-q_-\|_1=\frac12\Omega(\omega)\ge\frac1{32}.
\]

The verifier also reconstructs C(b)'s engine level set. At \(\tau=1/256\),
\(F=\{v,b,f\}\), and the single ballast fiber \(b\) supplies
\[
T_\omega(F)=P_v^+(F)=\frac{49153}{65536}
\]
against pre-foldback demand
\[
\frac{547616620543}{70370891661312}.
\]
The exact payment margin is
\(52231625900033/70370891661312\), while the ray value remains \(2\delta\).

At this endpoint:
\[
\begin{aligned}
H-16\tau&=-\frac{2047}{32768},&
Z_v(q_A)/\tau&=\frac1{128},\\
\Omega(\omega)&=\frac{3221291008}{4295098369},&
s_+s_-\|q_+-q_-\|_1&=\frac{1610645504}{4295098369},\\
P_v^+(E_c\cap G_v)-\tau S/16&\ge\frac{4095}{16384}.&&
\end{aligned}
\]
Tallness is the only failed L5/C gate in this width family.

### Drift branch: transient-ballast routing

To test drift separately, I added
\[
L_x=(1/8,1/8,3/4,0)
\]
near \(L_v=(1/8,1/8,3/4+\delta,-\delta)\), routing ballast to it through a
column of weight \(u\). Exact \(BL=I_4\) forces the ballast anchor row to have
coefficients \(-u/8\) on both actor columns. Therefore
\[
\nu_b=u/4.
\]
Keeping \(\delta(P)=\tau^2\) forces \(u\le4\tau^2\), so only
\(O(\tau^2)\) mass reaches the near transient row; the drift branch is not
entered. At \(\tau=1/256,u=4\tau^2\), the exact projection has
\[
\delta(P)=\frac1{65536},\quad
\|p_v-p_x\|_1=\frac{65537}{2147483648}<4\tau,\quad
P_v^+(x)=\frac{49153}{1073741824}.
\]
Forcing \(u=1\) moves \(49153/65536\) mass to \(x\), but gives
\(\delta(P)=1/4\), exceeding the target by \(16383/65536\). This is the
binding drift inequality for this completion, not a universal obstruction.

## Scope and dead ends

- All quantities use full equal-row fibers. No raw-index path floor or clone
  multiplicity is used.
- The C center condition is proved uniformly by a metric certificate, not by
  sampling. Width is the exact affine-Lipschitz supremum for these coordinate
  points, computed by complete extreme-sign enumeration.
- \(Z_v(q_A)\) is bracketed by an exact minimizing ray pair and a feasible
  top-face vector, never inferred from pointwise values.
- The S formal tall dials are not called heights after their closest-face
  coefficient becomes negative and the proposed top becomes visible.
- The rejected S and drift completions are exact idempotents, but fail their
  target \(\tau^2\) negativity claim. They are rejection certificates.
- No probabilistic reading, Jensen step, favorable minimizer, or witness
  averaging is used.

## Reproduction

Run:

~~~text
python3 search.py
~~~

Expected final lines:

~~~text
S: BLOCKED — hiddenness/negative-mass inequalities bind exactly.
C: BLOCKED — width near-refuter fails only tallness; drift routing fails negativity.
EXACT CHECKS PASSED; L3 EVIDENCE ONLY — this computation is not a proof.
~~~
