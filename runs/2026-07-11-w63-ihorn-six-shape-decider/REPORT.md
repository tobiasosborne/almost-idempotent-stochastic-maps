# W63 I-horn six-shape exact decider report

This is **L3 exact constructive/numerical evidence only**. It is not a proof of
any creative leaf, not a proof of emptiness, and not a proof of L5-GAP-1.
`BLOCKED` means blocked only in the explicitly tested family. No genuine
I-base datum was constructed.

The executable verifier is [`search.py`](search.py), and its frozen output is
[`certificates.json`](certificates.json). Every matrix identity, row sum,
negative mass, displayed height/ray certificate, scalar width, chord, kernel,
corner ledger, and margin is asserted with `fractions.Fraction`. A failed
precondition is never silently promoted to a theorem conclusion.

## Verdicts

- **D — BLOCKED.** At \(\tau=1/1024\), the coordinate calibration reaches
  \(\|r_\omega-p_v\|_1=b\tau=1/524288\), but
  \(\Omega-1/16=12094642585599/17592219598864>0\) and
  \(H-16\tau=-8191/524288\). Thus it is the old wide fan, not a D candidate.
- **W — BLOCKED.** At \(\tau=1/2048\), drift is strictly below \(b\tau\), and
  the exact weighted chord is
  \(6597071863808/17592194433025\), paid by one common receiver with mass
  \(3145729/4194304\). But \(\Omega\) is about \(3/4\), above the parent
  ceiling \(1/16\), and \(H-16\tau=-16383/2097152\).
- **Sh — BLOCKED.** The W61 receiver attachment binds at
  \(q+m_{\rm sh}+S\le\tau^2\). Already
  \(m_{\rm sh}-(\tau^2-q)=939530237/17592320196608>0\), while the base height
  has \(H-16\tau=-268437471/4295000048\).
- **X — PARTIAL.** A definition-level selected-corner configuration has
  \(\eta(1)=4194304/4194305\) and
  \(M_X=12582911/16777220>1/8\). The large-gap freight mass is
  \(4194303/16777220\), and the remaining near-freight mass is
  \(2097152/4194305\). It is not an output of
  `lem-ihorn-selected-corner-extraction`: no I-base/L0 input exists, and
  \(H-16\tau=-1125900439535615/144115256795332608\).
- **I-cap — BLOCKED.** The exact diagonal definition-level ledger has
  \(M_X=0\), \(M_I=0\), and \(M_D=1023/1024\). It therefore misses the I-cell
  threshold by exactly \(1/16\) and routes to D. It is also short, so the SC
  extraction preconditions are unavailable.
- **D-cap — BLOCKED.** The diagonal ledger is rank three, short, and has the
  one-point distribution \(g_u/\tau=4194305/1048576\) with mass
  \(1023/1024\); it does not escape the
  rank-three obstruction. The separate W55 \(A_0=5\) canonical completion has
  \(\nu_f=21475229695/4294967296\), exceeding \(\tau^2\) by
  \(21475164159/4294967296\).

## What was checked

### D and W: true ray values and the forbidden fan

The coordinate family is an exact corank-one projection with \(S=1/4\), a
nonempty visible set, a hidden top, and the uniform all-local-center bounds.
For both endpoints the exhibited ray pair \((\Lambda,c)=(3,p_b)\) and a
feasible top-face vector agree exactly, so this is the true value from
`lem-l5-top-face-ray-formula`:

\[
 Z_v(q_A)=2\tau^2,
 \qquad Z_v(q_A)/\tau=2\tau.
\]

At the D endpoint this ratio is \(1/512\); at the W endpoint it is \(1/1024\).
The family nevertheless never enters the I parent because its exact width is

\[
 \Omega(\omega)=\frac{3+4\tau^2}{4(1+\tau^2)^2}\longrightarrow\frac34.
\]

The ED level set was constructed exactly at the D calibration, but ED is not
legally invocable: the parent width and routine ceiling fail. Directly,
\(F_\chi=\{f\}\) and \(P_v^+(F_\chi)=0\). This is recorded as an
inapplicable-contract diagnostic, not as a contradiction to the proved shard.

### Sh: tallness and negativity bind independently

The W61 factorization has

\[
 H=\frac{2}{268437503},
 \qquad H/\tau\to0.
\]

Adding the required shallow clone and selected mass preserves \(P^2=P\) and
row sums exactly, but changes the actual global negativity. At \(\tau=1/256\)
the exact excess over the target \(\tau^2\) is
\(1099788433407/4398046511104\). Thus this attempted counterweight is rejected
before \(\theta\), the universal exposer shadow, or a downward tallness sweep
can be claimed for it.

### X and the corner boundary

For the W61 graft at \(\tau=1/2048\), the script constructs \(\phi\), the zero
admissible exposer \(h\), selected row \(f=a\), an explicit legal vertex
kernel, \(\Gamma_f\), the radial block \(B_F\), and
\(\eta=\Gamma_f|_{B_F}\). It asserts the corner score, all block inequalities,
\(\eta(1)\ge1/4\), and the strict X boundary.

This is useful local by-catch, but not a public SC certificate: the score row
was not obtained from L0's \(\lambda_A\), because the construction is not a
genuine I-base datum. Calling it an SC extraction would reverse the lemma's
logic.

### I-cap and D-cap: exact diagonal type, wrong leaf

A transient row \(f=(1-2\tau)u+2\tau y\) produces a definition-level
\(B_N\) ledger of mass \(1-2\tau=1023/1024\) on \((u,u)\). The exposedness LP
at \(u\) is solved algebraically: \(h(z)\ge0\) forces
\(h(a)\le t_0h(o)\le t_0\), while \(h(f)=2\tau h(y)\). Hence the appended
row becomes the unique far-tight family \(T=\{f\}\), with \(O=\{o\}\).
Their hulls are disjoint, giving the exact D
classification and the recorded \(g_u/\tau\).

This kills neither leaf. It shows only that this attempted diagonal plateau
routes to D rather than I. It remains rank three and has the same cubic-height
failure. The W55 calculation independently confirms that the canonical
\(A_0=5\) left inverse fails the all-row negativity requirement and lies
inside, rather than outside, the hypotheses targeted by
`lem-starvation-completion-obstruction`.

## Scope and by-catch

- No family passed \(H>16\tau\); tallness remains the binding wall for a fifth
  exact batch.
- No matrix passed the full I-base package, so \(\omega,\theta,\lambda_A\), and
  a public SC certificate are not assigned where their antecedents fail.
- The only cell by-catch is at the definition-level corner interface: one X
  ledger and one D ledger. There is no entrant to any creative leaf's full
  hypothesis class and no I-cell ledger.
- All objects are clone-invariant full fibers and row points; no probabilistic
  reading, raw-index floor, Jensen step, favorable ray minimizer, or witness
  averaging is used.

Reproduce with:

```text
python3 search.py
```

The final line must state that the exact checks passed, zero genuine I-base
data were found, and the output is L3 evidence only.
