# W69 DTR growing-rank completion decider

## Verdict

**PARTIAL.** The exact family below realizes the local growing-rank DTR
geometry, rotating tail incidence, and zero finance negativity at ranks
4, 8, 16, and 32. It does **not** enter the full hypothesis class (1.22) and
does **not** refute `conj-w67-aesc-diffuse-tail-ray-conversion`. The binding
failures are exact: the probe D population violates R0 carrier ownership by
(1/8), the proposed center is not a hidden vertex and has
(H-16\tau=-16\tau), the B4 shallow mass is (P_v^+(\mathcal L_v)=1),
ultra (\omega) is empty, B1--B5/R1 are therefore unavailable, and
(\mathcal D_{\rm leaf}>0).

This is **L3 exact constructive/numerical evidence only, never a proof**. In
particular, failure of these families is not an emptiness theorem.

The verifier is [search.py](search.py), and the generated exact certificate is
[certificates.json](certificates.json). All arithmetic is
`fractions.Fraction`; every advertised identity and inequality is asserted.

## Exact growing-rank family

For every sampled (m\in\{4,8,16,32\}), put

\[
 \tau={1\over 2^{20}m},\qquad \delta=\tau^2,\qquad
 c={1\over m}(1,\ldots,1),\qquad d_s=e_{s+1}-e_s
\]

with cyclic indices. The factor rows are

\[
 L_{a_j}=e_j,\qquad L_{u_s}=c+{\tau\over20}d_s,
 \qquad L_v=c,
\]

and (B=(I_m\ 0\ 0)). Thus (BL=I_m), (P=LB), and (P^2=P)
entrywise. The (m) anchors are distinct absorbing rows, so the certified
rank and recurrent support both equal (m); the rank increase is not caused
by clones or transient-row inflation. Every row is nonnegative, hence

\[
 \max_i\nu(P_i)=0<\tau^2
\]

at every rank.

For carrier (u_s), use the exact DTR-shaped normalization

\[
 D_s={\tau\over2}d_s,\quad \widetilde q_s=p_{u_s}+D_s,
 \quad \widetilde A_s=4,\quad
 x_s=p_{u_s}-4D_s=c-{39\tau\over20}d_s.
\]

All (m) coordinates of (x_s) are positive. Consequently (x_s) is an
exact convex combination of all (m) anchor rows, so (h_s=0). Direct
enumeration of every actual row gives

\[
 \min_f\|p_f-x_s\|_1={39\tau\over10}>3\delta.
\]

This realizes growing-rank convexification locally: the hull certificate has
support (m\), while no actual row is within (3\delta).

The normer of (D_s) has negative coordinate (s) and positive coordinate
(s+1). Hence the (m) normers rotate, their common positive-coordinate and
common negative-coordinate intersections are both empty, and their receiver
incidences are the cycle edges

\[
 \mathcal U_s=\{a_s,a_{s+1}\},\qquad
 \mathcal U_{\rm tail}=\{a_0,\ldots,a_{m-1}\}.
\]

Carrierwise and in aggregate,

\[
 \operatorname{Tail}_1(u_s)={2\over m}>{\tau\over8},\qquad
 \int\operatorname{Tail}_1\,d\eta={1\over4m},\qquad
 P_{f^*}^+(\mathcal U_{\rm tail})=1>{\tau\over2560}.
\]

Every incidence is contained in both the formal diagnostic sets
(\mathcal E_*) and (\mathcal L_v); the script prints the carrierwise
intersections exactly.

## Why this is not a DTR entrant

Give each probe carrier mass (1/(8m)), for total mass (1/8>1/160).
The strict HES guard holds formally because every hull distance is zero. The
numeric D-ledger values (M_X=M_I=0, M_D=1/8) have the requested scalar
inequalities, and the receiver foldback overflow is zero. But the prior R0.1
ownership statement fails:

\[
 \sup_{0\le g\le1}\{\eta_D^*(g)-P_{f^*}^+(g)\}={1\over8}.
\]

The public row gives no mass to the transient probe-carrier fibers. Therefore
this (\eta) is not the original D part of a selected-corner certificate.
R0's complete output is unavailable, so R1 and B1--B5 cannot legally be
invoked. The reported B5 label is `NOT_REACHED`. Even in a legal candidate,
the B5 population would be different from (\eta_D^*); the two populations
must never be identified carrierwise.

Independently, (p_v=c) is an interior convex combination of the anchors,
not a hidden row-point vertex. The exact height diagnostic is (H=0), hence
(H-16\tau=-16\tau). A far selected mass of one exists and has
(q_A=p_v), giving the exact ray-formula diagnostic (Z_v(q_A)=0), but the
all-center package fails: the shallow exterior countervalue is (1), its
strict upper threshold is (\tau/16), the far-(G_v) mass is zero, and the
ultra (\omega) package is empty. These diagnostics are not promoted to an
I-base datum.

## Rank trend and exact margins

The local finance vector is distributed over a convex hull of (m) genuine
recurrent rows, and the maximum single-row negativity is exactly zero. This
does drive it below (\tau^2), but only outside the legal D/I-base package.
The ownership defect stays (1/8), (H/\tau) stays zero, the shallow mass
stays one, and the pinned leaf deficit stays positive. Thus increasing rank
does not improve the binding gates.

| rank (m) | (\tau) | max row negativity | min-row margin over (3\delta) | tail margin over (\tau/8) | (H-16\tau) | R0 ownership excess | (\ell_T-P_v^+(\mathcal L_v)) | (\mathcal D_{\rm leaf}) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 1/4194304 | 0 | 81788913/87960930222080 | 16777215/33554432 | -1/262144 | 1/8 | -290536210364815638527/290536219160925437952 | 16777215/1073741824 |
| 8 | 1/8388608 | 0 | 163577841/351843720888320 | 16777215/67108864 | -1/524288 | 1/8 | -2324289718102997860351/2324289753287403503616 | 33554431/2147483648 |
| 16 | 1/16777216 | 0 | 327155697/1407374883553280 | 16777215/134217728 | -1/1048576 | 1/8 | -18594317885561672564735/18594318026299228028928 | 67108863/4294967296 |
| 32 | 1/33554432 | 0 | 654311409/5629499534213120 | 16777215/268435456 | -1/2097152 | 1/8 | -148754543647443736592383/148754544210393824231424 | 134217727/8589934592 |

The family laws are exact:

\[
 \begin{aligned}
 \min_f\|p_f-x_u\|_1-3\delta&={39\tau\over10}-3\tau^2,\\
 \min_u\operatorname{Tail}_1(u)-{\tau\over8}&={2\over m}-{\tau\over8},\\
 H-16\tau&=-16\tau,\\
 \mathcal D_{\rm leaf}&={1\over64}-{\tau\over256}>0.
 \end{aligned}
\]

## EC and pinned leaf diagnostics

The formal panel has (P_v^+(\mathcal E_*)=P_v^+(\mathcal L_v)=1) and
(Z_v(q_A)=0). Therefore, at every rank,

\[
 \mathcal D_{\rm EC}=-{1\over8}+{1\over64}=-{7\over64}<0,
\]

whereas

\[
 \mathcal D_{\rm leaf}={1\over64}-{\tau\over256}>0.
\]

These are reported separately. Negative (\mathcal D_{\rm EC}) is only a
failure of the stronger residual contract in this already illegal diagnostic;
it is not a refutation of the pinned A-esc/DTR leaf. A genuine refuter needs
the full priority package and negative (\mathcal D_{\rm leaf}), neither of
which occurs here.

## Mandatory regressions

- **W66/W63 plateau — PASS.** At (k=2048), the exact factorization has
  (M_I=0, M_D=1023/1024), (\ell/\tau=1/1024=2\tau), and routes to C0.
  Tallness fails and (\mathcal D_{\rm leaf}=8191/524288>0).
- **W55 (A_0=5) — PASS.** The finance row has exact negativity
  (21475229695/4294967296>\tau^2=1/65536). Its actual actor residual is at
  most (3\delta), so the minimum actual-row distance is also at most
  (3\delta): it routes away from DTR before the finance rejection is even
  considered.

## By-catch and scope

The sole by-catch is a parametric, growing-rank entrant to the **local**
convex-hull/actor-distance/tail-incidence shape. It is not an entrant to DTR,
HES, A-esc, T-esc, or any other full creative-leaf hypothesis class. The
family identifies a sharp experimental lesson: convexification, normer
rotation, common-union incidence, and even zero finance negativity are cheap
once root-owned D carriers and hidden tall geometry are dropped. The next
constructive search must preserve R0.1 and hidden tallness while adding rank;
adding more recurrent support to this retraction spine cannot repair either
fixed defect.

Reproduce with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -u search.py
```

The script exits nonzero on any mismatch and ends with the verdict, rank
trend, two unit-test lines, and the explicit L3/non-proof warning.
