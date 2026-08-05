# DESIGN v2 — LEDGER-SETTING-RESCOPE repair

Date: 2026-08-05
Role: fresh codex repair designer
Status: **DESIGN ONLY / NON-RIGOROUS / NOT USER-RATIFIED / DO NOT LAND,
SHARD, AMEND, REWIRE, SEED, OR PROMOTE**

## 0. Disposition and architecture

**READY FOR A NEW SEPARATE HOSTILE AUDIT; NOT READY TO LAND.**

This replacement applies all eight findings of
`AUDIT-LEDGER-SETTING-RESCOPE.md` and every item of its exact redesign gate.
The repair has two layers, matching the already-ratified
`def-maincb-witness-ledger` / `lem-maincb-reset-constant-ledger` and
`def-stage1-polar-witness-data` / `lem-stage1-polar-constant-ledger` pattern:

1. `def-routef-raw-factor-setting` is only a record schema.  It names a
   global scalar header `W_RF`, a per-input datum `S`, their typed fields, and
   notation.  It contains no existence statement, no analytic estimate, no
   universality claim, and no claim that any field is supplied by a theorem.
2. `lem-routef-raw-factor-setting-formation` is the result that selects one
   global `W_RF` first and then forms an `S` for every admissible raw input.
   All AI, Kitaev, and MAIN conclusions live in this Layer-1 row.

The sixteen family rows then fix the **same global `W_RF`**, the `S` supplied
for the current input, and, where needed, one explicitly threaded
`Delta' -> Delta -> Upsilon' -> Upsilon` producer chain.  Every result id named
by a threading clause is a direct dependency.  Rows 1--13 and D2/D3 retain
the landed mathematical suffix byte-for-byte.  Row 14 is the sole exception:
its F2/F3/PRH prose is replaced by the literal scalar inequalities proved in
`DESIGN-LEDGER-DOMAINS-v2.md` section 3.5.  F2, F3, and PRH are applied only
in the future strengthened `lem-routef-k-ledger`.

Nothing here promotes a result.  The proposed formation row and all sixteen
re-scoped rows have `status: stated`; the two live workspaces remain
`af: seeded` unless and until an authorized implementation and independent
verification complete.

### 0.1 Binding audit findings disposed

| audit finding | v2 correction |
|---:|---|
| 1 BLOCKER | The definition in section 1 is data and notation only.  All words such as “supplies”, “furnishes”, and all analytic conclusions occur only in the formation result. |
| 2 BLOCKER | Section 2 adds the missing nonvacuous formation lemma with `exists W_RF, for every input, exists S` quantifier order. |
| 3 HIGH | `W_RF` is selected before any `H,Phi,eta`; every row fixes that same header.  Hence `eta_A,C_A,C_E,epsilon_E` cannot be reselected per input. |
| 4 HIGH | Sections 3.3--3.5 expand the producer chain field by field and add every missing direct edge listed by the audit. |
| 5 BLOCKER | Row 14 exports only `eta_K` positivity and the F2/F3/PRH scalar inequalities.  It no longer names or imports F2, F3, or PRH. |
| 6 MEDIUM | Rows 1, 4, D2, 7, D3, and 11 explicitly quantify the amplification index and every displayed matrix variable. |
| 7 MEDIUM | Section 5 provisions both the new definition and `def-ucp-map` in each live workspace, while retaining existing definitions without duplicate registration. |
| 8 LOW | The future landing must correct the stale row-3 body sentence: later rows retain the two-term `rho_id`; their effective domains are unchanged because they descend from `rho_T <= rho_id^corr`.  The row-3 contract suffix stays byte-identical. |

## 1. Theorem-free canonical setting definition

### 1.1 Exact proposed shard

Proposed path: `definitions/def-routef-raw-factor-setting.md`.
It stays `draft` until a separate hostile audit and explicit user
ratification.

```markdown
---
id: def-routef-raw-factor-setting
term: Route-F raw-factor setting data
aliases: finite Route-F raw-factor setting; Route-F raw-factor scalar header; raw-factor setting datum
kind: original
status: draft
source: internal
locus: DESIGN-LEDGER-SETTING-RESCOPE-V2.md sect-1 (repair proposal; pending hostile audit and user ratification)
sha256: -
consensus: v2 repair proposal only; pending separate hostile audit and explicit user ratification
---

**Statement (data, typing, and notation only).** *Route-F raw-factor setting
data* have two levels: a scalar header `W_RF`, and a setting datum `S` over
that header.

The scalar header has four receiving real-scalar fields

\[
(\eta_A,C_A,C_E,\varepsilon_E).
\]

The following symbols are derived notation, not independent witnesses:

\[
C_\theta:=12(\sqrt2-1),\qquad
\rho_\theta:=\frac18,\qquad
\rho_{\rm AI}:=\eta_A,\qquad
\bar C_E:=\max\{1,C_E\},
\]
\[
C_V:=\bar C_EC_A,\qquad C_T:=C_\theta+3C_V,
\]
\[
\rho_T:=\min\left\{
\rho_\theta,\rho_{\rm AI},\frac{\varepsilon_E}{C_A},
\frac1{4(1+C_\theta)},\frac1{4(1+C_V)}
\right\}.
\tag{1.1}
\]

Continue, in the displayed order, with

\[
\begin{aligned}
\rho_{\rm unit}&:=\rho_T,\\
\rho_{\rm id}&:=\min\{\rho_{\rm AI},\varepsilon_E/C_A\},\\
\rho_{\rm id}^{\rm corr}
&:=\min\{\rho_\theta,\rho_{\rm AI},\varepsilon_E/C_A\},\\
\rho_{\rm prod}&:=\rho_T,\\
C_{\Delta'}&:=C_T+4C_\theta,\\
\rho_{\Delta'}&:=\min\{\rho_T,\rho_{\rm prod}\},\\
C_\Delta&:=6C_T+7C_{\Delta'},\\
\rho_\Delta&:=\min\left\{
\rho_{\rm unit},\rho_{\Delta'},[2(C_T+C_{\Delta'})]^{-1}
\right\},\\
C_2&:=C_{\Delta'}+4C_\Delta,\\
\rho_2&:=\min\{\rho_{\rm prod},\rho_{\Delta'},\rho_\Delta\},\\
\rho_{\Delta\Phi}&:=\min\{\rho_\theta,\rho_\Delta,\rho_2\},\\
C_3&:=10+20C_\Delta+12C_\theta+2C_{\Delta'},\\
\rho_3&:=\min\{\rho_\theta,\rho_{\Delta'},\rho_\Delta,\rho_2\}.
\end{aligned}
\tag{1.2}
\]

For the componentwise block, put

\[
\begin{aligned}
C_N&:=C_V+C_\Delta,\\
C_R&:=C_N+C_2=C_V+C_\Delta+C_2,\\
C_L&:=C_2+C_3+2C_R,\\
C_{\Upsilon'}&:=1+C_\theta+2C_\Delta+2C_L,
\end{aligned}
\tag{1.3}
\]
\[
\rho_{\Upsilon'}:=\min\left\{
\rho_T,\rho_{\rm id},\rho_\Delta,\rho_2,\rho_3,(2C_R)^{-1}
\right\}.
\tag{1.4}
\]

Then put

\[
\begin{aligned}
C_\Upsilon&:=6C_T+7C_{\Upsilon'},\\
\rho_\Upsilon&:=\min\left\{
\rho_{\rm unit},\rho_{\Upsilon'},
[2(C_T+C_{\Upsilon'})]^{-1}
\right\},\\
\rho_{\Delta\Upsilon}&:=\min\{
\rho_\theta,\rho_T,\rho_{\rm id},\rho_\Delta,\rho_\Upsilon\},\\
\rho_{\rm mult}&:=\min\{
\rho_T,\rho_{\rm id},\rho_{\Delta\Phi},\rho_\Upsilon\},\\
\rho_{\Upsilon\Delta}&:=\min\{
\rho_T,\rho_{\rm id},\rho_\Delta,\rho_\Upsilon\}.
\end{aligned}
\tag{1.5}
\]

Finally,

\[
K:=\max\left\{
1,
C_\theta+C_\Delta+2C_\Upsilon,
C_\Upsilon+2(C_2+C_\theta+C_\Delta),
C_\Upsilon+2C_\Delta
\right\},
\tag{1.6}
\]
\[
\rho_{\rm fac}:=\min\{
\rho_2,\rho_{\Delta\Upsilon},\rho_{\rm mult},
\rho_{\Upsilon\Delta}
\},
\tag{1.7}
\]
\[
\eta_K:=\min\{\rho_{\rm fac},(24K)^{-1},1\}.
\tag{1.8}
\]

A setting datum `S` over `W_RF` records the following typed data:

1. a nonzero finite-dimensional complex Hilbert space `H`, a
   [[def-ucp-map|UCP map]] `Phi:B(H)->B(H)`, and a real scalar `eta`;
2. a linear map `tilde-Phi:B(H)->B(H)`, its range `A:=Im(tilde-Phi)`, a
   bilinear operation `X star Y:=tilde-Phi(XY)` on `A`, and the scalar
   notation
   \[
   r:=\frac32\bigl((1-4\eta)^{-1/2}-1\bigr),
   \qquad
   \varepsilon_{\rm AI}(\eta):=
   \max\{r,20\eta+2((1+r)^5-1),3r-r^2\};
   \]
3. a finite-dimensional unital C*-algebra `B` and linear maps `v:B->A` and
   `u:A->B`; and
4. the notation
   \[
   \widetilde\Delta:=\iota_{\mathcal A\subseteq B(H)}\circ v,
   \qquad
   \widetilde\Upsilon:=u\circ\widetilde\Phi.
   \]

The displayed map `tilde-Phi` is the notation

\[
\widetilde\Phi
:=\frac12\left(I+(2\Phi-I)
\bigl(I-4(\Phi-\Phi^2)\bigr)^{-1/2}\right).
\]

For every linear map `T` occurring in a datum and every integer `q>=1`,
`T_q:=id_{M_q} tensor T`.  Registry ASCII `A` and `B` denote the two
algebras above; `I_B` denotes the unit of `B`.  An unsubscripted `I` is the
unit forced by the adjacent map types.

**Notes / provenance.** This shard asserts only the shape and notation of a
record.  In particular, it asserts none of the following: that a header or
datum exists; that any scalar is positive, finite, universal, or independent
of input data; that `||Phi^2-Phi||_cb<=eta`; that `tilde-Phi` is
idempotent; that `A` is an extended approximate C*-algebra; that `v` is an
[[def-extended-delta-inclusion|extended isomorphism]]; or any norm,
smallness, admissibility, CP, or UCP estimate for the recorded maps.  Those
assertions belong only to result rows, beginning with
`lem-routef-raw-factor-setting-formation`.  The terms “UCP map”, “extended
epsilon-C*-algebra”, and “extended delta-isomorphism” are referenced from
their canonical shards and are not redefined here.  The labels `u` and `v`
do not assert an inverse relation; that relation is a conclusion of the
formation result.
```

### 1.2 Deletion test

Delete `lem-routef-raw-factor-setting-formation` and every analytic provider.
The proposed definition leaves only a possibly empty record type.  It does
not imply that any `W_RF`, `S`, `B`, or `v` exists, and it supplies no defect,
idempotence, approximate-algebra, extended-isomorphism, positivity,
universality, or norm conclusion.  A consumer can unpack only field types and
the displayed notation.  This is exactly the separation used by
`def-maincb-witness-ledger` and `def-stage1-polar-witness-data`.

Even an inverse relation between the two recorded linear maps is absent.
Nonemptiness for every admissible raw input, bijectivity of `v`, and the
identity `u=v^(-1)` are all the formation lemma's burden.

## 2. Formation lemma: global witnesses before inputs

### 2.1 Exact proposed registry shard

Proposed path:
`argument/lemmas/lem-routef-raw-factor-setting-formation.md`.

```markdown
---
id: lem-routef-raw-factor-setting-formation
kind: lemma
contract: Route F raw-factor setting formation: there exists one choice W_RF of the scalar header of def-routef-raw-factor-setting, independent of H, Phi, eta, dimension, amplification level, and block data, with C_theta=12*(sqrt(2)-1), C_A=20+(211/8)*C_theta, eta_A>0 and (C_A,eta_A) the fixed witnesses of lem-routef-ai-defect-linearization, C_E<infinity and epsilon_E>0 the fixed witnesses of lem-thmainext-conditional, rho_theta:=1/8, rho_AI:=eta_A, and all remaining named scalar quantities defined by (1.1)-(1.8), such that for every nonzero finite-dimensional Hilbert space H, every UCP map Phi:B(H)->B(H), and every eta with 0 <= eta <= rho_id^corr and ||Phi^2-Phi||_cb <= eta, there exist a finite-dimensional unital C*-algebra B, an extended C_E*epsilon_AI(eta)-isomorphism v:B->A, and a def-routef-raw-factor-setting datum S over this same W_RF whose fields are the displayed H,Phi,eta,B,v,u=v^(-1) and the canonical tilde-Phi,A,star,epsilon_AI(eta),tilde-Delta,tilde-Upsilon notation, with tilde-Phi^2=tilde-Phi, A an extended epsilon_AI(eta)-C*-algebra, and 0 <= epsilon_AI(eta) <= C_A*eta <= epsilon_E.
defs: def-routef-raw-factor-setting; def-ucp-map; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-kitaev-almost-idemp-audit; lem-routef-ai-defect-linearization; lem-thmainext-conditional
status: stated
af: none
provenance: DESIGN-LEDGER-SETTING-RESCOPE-V2.md sect-2 (design-only formation repair required by AUDIT-LEDGER-SETTING-RESCOPE.md findings 1-3 and redesign gate items 1-2)
owner: A
workspace: proofs/lem-routef-raw-factor-setting-formation
---

**Status.** Proposed `stated` row only.  It promotes no definition, provider,
or ledger result.

**Quantifier discipline.** The existential choice of `W_RF` precedes every
input quantifier.  The same `eta_A,C_A,C_E,epsilon_E`, hence the same entire
derived scalar ledger, is used for every datum `S`.  The input-specific
existential contains `B,v,S` only; it cannot reselect the global witnesses.

**Derivation obligation.** Fix the AI witnesses once and the MAIN witnesses
once.  For an input in the displayed domain, `rho_id^corr` gives
`eta<=rho_theta=1/8<1/4`, `eta<=rho_AI=eta_A`, and
`C_A*eta<=epsilon_E`.  Apply `lem-kitaev-almost-idemp-audit` for exact
idempotence, `lem-routef-ai-defect-linearization` for the extended
`epsilon_AI(eta)` structure and linear estimate, and
`lem-thmainext-conditional` to that same finite-dimensional range `A` for
one `B,v`.  Package these particular outputs as `S`; do not infer any
analytic conclusion from the definition alone.

**Projected af budget (binding design target).** Target 10 live nodes / 3
verification rounds / hard cap 14: root; one global-witness selection node;
one scalar-header assembly node; one radius extraction node; one Kitaev
application; one AI application; one finite-dimensional-range node; one MAIN
application; one same-output `S` packaging node; one quantifier/universality
assembly node.  Hitting 14 is a factoring stop, not permission to enlarge the
cap.
```

### 2.2 Why the direct dependencies are exact

- `lem-kitaev-almost-idemp-audit` is direct because the formation conclusion
  explicitly asserts `tilde-Phi^2=tilde-Phi` and uses the corrected
  `eta<1/4` domain.
- `lem-routef-ai-defect-linearization` is direct because it supplies the one
  global `(C_A,eta_A)` pair, the extended structure, and
  `epsilon_AI(eta)<=C_A*eta`.
- `lem-thmainext-conditional` is direct because it supplies the one global
  `(C_E,epsilon_E)` pair and the input-specific `B,v`.
- `lem-routef-functional-calculus-closeness` is not direct: the formation
  contract asserts no `||tilde-Phi-Phi||_cb` estimate.  Rows that use that
  estimate retain their own direct edge.

## 3. Exact re-scoped contracts, `defs:`, and `deps:`

### 3.1 Byte and threading rules

For rows 1--13 and D2/D3, delete the new prefix through its final colon and
one following space.  The remaining bytes are the current landed `contract:`
value exactly.  Thus no landed coefficient, radius, inequality, or existing
suffix quantifier changes.

The phrase “supplied by `<id>`” is used only when `<id>` is on that row's
direct `deps:` line.  Later rows do not use the undefined adjectives
“successive” or “furnished packet”: they spell out that `Delta` comes from
the same `Delta'`, `Upsilon'` from that same pair, and `Upsilon` from that
same triple.  This is the direct-dependency option explicitly allowed by
audit finding 4; no second serial-packet definition is introduced.

Every `defs:` line drops `def-almost-idempotent`.  The finite UCP/cb setting
is not the real row-stochastic `infinity->infinity` notion.  Every row imports
the new setting definition, while CP/UCP-producing suffixes retain
`def-ucp-map` directly.

In every contract below, “the fields of `(W_RF,S)`” is compact registry
wording for the recorded fields together with the derived notation fixed by
the definition.  It does not turn the derived scalar expressions into new
existential witnesses.

### 3.2 Raw packet: rows 1--4

#### Row 1 — `lem-routef-raw-factor-norms`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result; for every integer n >= 1 and every X in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Raw factor-map norms: with C_V, C_T, rho_T from (1.1), for 0 <= eta <= rho_T, every amplification satisfies (1-C_V*eta)*||X|| <= ||tilde-Delta_n X|| <= (1+C_V*eta)*||X|| and max{||tilde-Delta||_cb, ||tilde-Upsilon||_cb} <= 1+C_T*eta.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation; lem-routef-functional-calculus-closeness; lem-routef-ai-defect-linearization; lem-thmainext-conditional
```

The explicit `n,X` binders repair finding 6.  The formation row, not the
definition, produces the same `B,v` used by both raw maps.

#### Row 2 — `lem-routef-raw-factor-units`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: Raw factor-map units: for 0 <= eta <= rho_unit := rho_T, max{||tilde-Delta(I)-I||, ||tilde-Upsilon(I)-I||} <= C_T*eta.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-norms; lem-routef-ai-defect-linearization; lem-thmainext-conditional
```

#### Row 3 — `lem-routef-raw-factor-identities`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: Raw factor-map identities: for 0 <= eta <= rho_id^corr := min{rho_theta, rho_AI, epsilon_E/C_A}, tilde-Delta tilde-Upsilon = tilde-Phi and tilde-Upsilon tilde-Delta = I_B.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation; lem-kitaev-almost-idemp-audit; lem-routef-ai-defect-linearization; lem-thmainext-conditional
```

The formation contract makes `rho_AI:=eta_A` literal, supplies the same
`B,v`, and carries the exact-idempotence conclusion from Kitaev.  During an
authorized landing, replace the stale body sentence saying later `rho_id`
means the corrected radius by: “Only this row uses `rho_id^corr`; later rows
retain the two-term `rho_id`, and their effective domains are unchanged
because they also descend from `rho_T <= rho_id^corr`.”

#### Row 4 — `lem-routef-raw-product-estimate`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result; for every integer n >= 1 and all X, Y in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Raw tilde-Delta-product estimate: for 0 <= eta <= rho_prod := rho_T, every amplification and all X, Y satisfy ||tilde-Phi_n(tilde-Delta_n X tilde-Delta_n Y) - tilde-Delta_n(XY)|| <= C_T*eta*||X||*||Y||.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-ai-defect-linearization; lem-thmainext-conditional
```

### 3.3 Delta chain, D2, row 7, and D3

#### Row 5 — `lem-routef-delta-prime-closeness`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: Delta-prime CP closeness: with C_Delta' := C_T+4*C_theta and rho_Delta' := min{rho_T, rho_prod}, for 0 <= eta <= rho_Delta', the repaired norm-one diagonal produces a CP map Delta' with ||Delta' - tilde-Delta||_cb <= C_Delta'*eta.
defs: def-routef-raw-factor-setting; def-fd-cstar-diagonal; def-ucp-map
deps: lem-routef-raw-factor-setting-formation; cor-kitaev-diagonal-cpization; lem-routef-functional-calculus-closeness; lem-thmainext-conditional; lem-routef-raw-factor-norms; lem-routef-raw-product-estimate
```

#### Row 6 — `lem-routef-delta-normalization-closeness`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result and for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Delta UCP normalization: with C_Delta := 6*C_T+7*C_Delta' and rho_Delta := min{rho_unit, rho_Delta', [2*(C_T+C_Delta')]^(-1)}, for 0 <= eta <= rho_Delta, a = Delta'(I) is invertible and Delta(X) = a^(-1/2)*Delta'(X)*a^(-1/2) is UCP with ||Delta - tilde-Delta||_cb <= C_Delta*eta.
defs: def-routef-raw-factor-setting; def-ucp-map
deps: lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-units; lem-routef-delta-prime-closeness
```

#### D2 — `lem-routef-degree-two-estimate`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness; for every integer n >= 1 and all X, Y in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Route F degree-two estimate: with C_2 := C_Delta'+4*C_Delta and rho_2 := min{rho_prod, rho_Delta', rho_Delta}, for 0 <= eta <= rho_2, every amplification satisfies ||Phi_n(Delta_n X Delta_n Y) - Delta_n(XY)|| <= C_2*eta*||X||*||Y||.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation; lem-routef-functional-calculus-closeness; lem-routef-raw-factor-norms; lem-routef-raw-product-estimate; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness
```

#### Row 7 — `lem-routef-delta-phi-product`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness; for every integer n >= 1 and all X, Y in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Normalized Delta product: for rho_DeltaPhi := min{rho_theta, rho_Delta, rho_2} and 0 <= eta <= rho_DeltaPhi, every amplification satisfies ||tilde-Phi_n(Delta_n X Delta_n Y) - tilde-Delta_n(XY)|| <= (C_2+C_theta+C_Delta)*eta*||X||*||Y||.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation; lem-routef-functional-calculus-closeness; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate
```

The new direct row-5 edge is audit finding 4's exact correction.

#### D3 — `lem-routef-degree-three-estimate`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness; for every integer n >= 1 and all X, Y, Z in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Route F degree-three estimate: with C_3 := 10+20*C_Delta+12*C_theta+2*C_Delta' and rho_3 := min{rho_theta, rho_Delta', rho_Delta, rho_2}, for 0 <= eta <= rho_3, every amplification satisfies ||Phi_n(Delta_n X Delta_n Y Delta_n Z) - Delta_n(XYZ)|| <= C_3*eta*||X||*||Y||*||Z||.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation; lem-kitaev-almost-idemp-audit; lem-routef-functional-calculus-closeness; lem-routef-raw-factor-norms; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate
```

### 3.4 Upsilon chain and telescopes

#### Row 8 — `lem-routef-upsilon-prime-closeness`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Upsilon-prime CP closeness: with C_N, C_R, C_L, C_Upsilon' from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon', every Choi multiplicity space used below is nonzero and the componentwise construction produces CP Upsilon' with ||Upsilon' - tilde-Upsilon||_cb <= C_Upsilon'*eta.
defs: def-routef-raw-factor-setting; def-ucp-map
deps: lem-routef-raw-factor-setting-formation; lem-routef-functional-calculus-closeness; lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate; lem-routef-degree-three-estimate
```

The new direct row-5 edge is audit finding 4's exact correction.

#### Row 9 — `lem-routef-upsilon-normalization-closeness`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, and every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Upsilon UCP normalization: with C_Upsilon := 6*C_T+7*C_Upsilon' and rho_Upsilon := min{rho_unit, rho_Upsilon', [2*(C_T+C_Upsilon')]^(-1)}, for 0 <= eta <= rho_Upsilon, b = Upsilon'(I) is invertible and Upsilon(X) = b^(-1/2)*Upsilon'(X)*b^(-1/2) is UCP with ||Upsilon - tilde-Upsilon||_cb <= C_Upsilon*eta.
defs: def-routef-raw-factor-setting; def-ucp-map
deps: lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-units; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness
```

The new direct row-5 and row-6 edges are audit finding 4's exact corrections.

#### Row 10 — `lem-routef-delta-upsilon-telescope`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Delta-Upsilon telescope: for rho_DeltaUpsilon := min{rho_theta, rho_T, rho_id, rho_Delta, rho_Upsilon} and 0 <= eta <= rho_DeltaUpsilon, ||Delta Upsilon - Phi||_cb <= (C_theta+C_Delta+2*C_Upsilon)*eta.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation; lem-routef-functional-calculus-closeness; lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness
```

The new direct row-5 and row-8 edges are audit finding 4's exact corrections;
row 6 and row 9 were already direct.

#### Row 11 — `lem-routef-multiplicative-telescope`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness; for every integer n >= 1 and all X, Y in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Multiplicative telescope: for rho_mult := min{rho_T, rho_id, rho_DeltaPhi, rho_Upsilon} and 0 <= eta <= rho_mult, every amplification satisfies ||Upsilon_n(Delta_n X Delta_n Y) - XY|| <= [C_Upsilon+2*(C_2+C_theta+C_Delta)]*eta*||X||*||Y||.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-delta-phi-product; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness
```

The new direct row-5, row-6, and row-8 edges are audit finding 4's exact
corrections.  The `n,X,Y` binders are finding 6's exact repair.

#### Row 12 — `lem-routef-upsilon-delta-telescope`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Upsilon-Delta telescope: for rho_UpsilonDelta := min{rho_T, rho_id, rho_Delta, rho_Upsilon} and 0 <= eta <= rho_UpsilonDelta, ||Upsilon Delta - I_B||_cb <= (C_Upsilon+2*C_Delta)*eta.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness
```

The new direct row-5 and row-8 edges are audit finding 4's exact corrections.

### 3.5 Aggregation and corrected scalar threshold

#### Row 13 — `lem-routef-k-finiteness`

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Route F common coefficient/domain: K in (1.6) is finite and universal, and rho_fac in (1.7) is positive and is a common domain for the degree-two estimate and the three Route-F factorization estimates.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness; lem-routef-delta-upsilon-telescope; lem-routef-multiplicative-telescope; lem-routef-upsilon-delta-telescope
```

The new direct row-5, row-6, row-8, and row-9 edges are audit finding 4's
exact corrections.  Global-before-input selection of `W_RF` makes “universal
K” literal rather than a per-`S` reselection.

#### Row 14 — `lem-routef-threshold-minimum` — revised contract

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Route F scalar threshold: let eta_K := min{rho_fac, (24*K)^(-1), 1}; then eta_K > 0, and every 0 <= eta <= eta_K satisfies eta <= rho_fac, 0 <= eta <= min{(24*K)^(-1),1}, 3*K*eta <= 1/8 < 1, and 3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6 < 1/2.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness; lem-routef-k-finiteness
```

This is the only mathematical suffix change in the family.  It is exactly
the arithmetic in `DESIGN-LEDGER-DOMAINS-v2.md` section 3.5:

- `eta<=eta_K` gives the common factor domain, the F2 threshold, and
  `eta<=1`;
- `3*K*eta<=1/8<1` makes the F3 denominator positive; and
- `3*K*eta/(1-3*K*eta)<=4*K*eta<=1/6<1/2` is the rational retract bound
  used at the PRH seam.

It asserts no `Q,D,J,Q_C,A,M`, no F2/F3 map hypotheses, and no PRH
admissibility.  Consequently `lem-routef-f2-positive-unital-compression`,
`lem-routef-f3-retract-defect`, `lem-routef-prh-finish`,
`def-stochastic`, and `def-positive-approximate-retract` all leave this
row.  The direct row-5, row-6, row-8, and row-9 edges are retained because
this row instantiates row 13 on one nonvacuously produced packet; they are
the audit finding-4 corrections, not hidden F2/F3/PRH imports.

### 3.6 Complete `defs:` summary

| order | id | exact corrected `defs:` line |
|---:|---|---|
| 1 | `lem-routef-raw-factor-norms` | `defs: def-routef-raw-factor-setting` |
| 2 | `lem-routef-raw-factor-units` | `defs: def-routef-raw-factor-setting` |
| 3 | `lem-routef-raw-factor-identities` | `defs: def-routef-raw-factor-setting` |
| 4 | `lem-routef-raw-product-estimate` | `defs: def-routef-raw-factor-setting` |
| 5 | `lem-routef-delta-prime-closeness` | `defs: def-routef-raw-factor-setting; def-fd-cstar-diagonal; def-ucp-map` |
| 6 | `lem-routef-delta-normalization-closeness` | `defs: def-routef-raw-factor-setting; def-ucp-map` |
| D2 | `lem-routef-degree-two-estimate` | `defs: def-routef-raw-factor-setting` |
| 7 | `lem-routef-delta-phi-product` | `defs: def-routef-raw-factor-setting` |
| D3 | `lem-routef-degree-three-estimate` | `defs: def-routef-raw-factor-setting` |
| 8 | `lem-routef-upsilon-prime-closeness` | `defs: def-routef-raw-factor-setting; def-ucp-map` |
| 9 | `lem-routef-upsilon-normalization-closeness` | `defs: def-routef-raw-factor-setting; def-ucp-map` |
| 10 | `lem-routef-delta-upsilon-telescope` | `defs: def-routef-raw-factor-setting` |
| 11 | `lem-routef-multiplicative-telescope` | `defs: def-routef-raw-factor-setting` |
| 12 | `lem-routef-upsilon-delta-telescope` | `defs: def-routef-raw-factor-setting` |
| 13 | `lem-routef-k-finiteness` | `defs: def-routef-raw-factor-setting` |
| 14 | `lem-routef-threshold-minimum` | `defs: def-routef-raw-factor-setting` |

## 4. Acyclicity, nonvacuity, and scalar-domain checks

The formation row precedes all sixteen rows.  With external leaves omitted,
the corrected internal order remains

```text
formation, 1, 2, 3, 4, 5, 6, D2, 7, D3, 8, 9, 10, 11, 12, 13, 14.
```

Every new direct edge points left in this order.  The finding-4 additions do
not create a cycle.

The family is not narrowed to a possibly empty datum class.  Formation says
that after one `W_RF` is fixed, **every** nonzero finite-dimensional UCP/cb
input on `0<=eta<=rho_id^corr` has an `S`.  The serial producer conclusions
then construct at least one `Delta'`, `Delta`, `Upsilon'`, and `Upsilon` on
their respective smaller radii.  Later contracts choose that same chain.

The v1 radius check remains valid and is adopted without change:

```text
rho_T <= rho_id^corr <= rho_id,
```

every later analytic radius is at most `rho_T`, and
`eta_K<=rho_fac<=rho_2<=rho_T`.  Thus formation on
`rho_id^corr` covers every family row.  The definition introduces no radius
hypothesis; these are conclusions/hypotheses of the formation and result
contracts.

## 5. Revised continuation plans for the two live af trees

The audit already established the mechanics: on af 0.1.6, `af amend` changes
only a pending node and preserves validated descendants byte-for-byte.  A
preserved badge is not validation of an amended ancestor; all amended nodes
must return bottom-up to fresh hostile verifiers.

Both live trees must pause until
`lem-routef-raw-factor-setting-formation` itself is landed and validated.
Otherwise an amended root would depend on a non-rigorous external and could
not bank under status propagation.

### 5.1 Workspace vocabulary and external provisioning

In **both** workspaces, after authorized landing:

1. add `def-routef-raw-factor-setting` exactly once;
2. add `def-ucp-map` exactly once (audit finding 7);
3. retain the already registered `def-extended-epsilon-cstar-algebra` and
   `def-extended-delta-inclusion`; do not duplicate them;
4. retain unused historical `def-almost-idempotent` rather than destructively
   rewriting the append-only ledger, but do not cite it in amended nodes; and
5. add one external named
   `lem-routef-raw-factor-setting-formation` with the literal
   `proofs/lem-routef-raw-factor-setting-formation` path and exact validated
   contract.

Preflight must check name uniqueness because `af def-add` accepts duplicate
names.

### 5.2 `lem-routef-raw-factor-norms`

Current state: 20 nodes, 13 validated, 7 pending.  Preserve every validated
node.  Amend exactly the seven pending nodes:

| node | v2 amendment |
|---|---|
| `1` | Replace by the exact row-1 contract in section 3.2 for linker contract match. |
| `1.1` | Fix the root's global `W_RF`, formation-produced `S`, and its particular `v`; identify `tilde-Delta=v` only by the data notation, while citing formation for existence and the provider relation. |
| `1.1.1` | Derive the radius and domain facts from the `W_RF` formulas plus the formation external.  Do not obtain an estimate by unpacking the definition. |
| `1.1.1.1` | Replace the unsupported ambient `local_assume` by the root-bound `(H,Phi,eta)` and the formation-produced `S`; cite formation for admissibility and provider conclusions, and unpack only field types/notation from the definition.  Then resolve `ch-7d5f34bdc70447b1`. |
| `1.2` | Bind `tilde-Upsilon=u tilde-Phi` by the data notation, and cite formation for `u=v^(-1)` for the same `S` and the same `v` used in `1.1`. |
| `1.2.3` | Use the fixed same-output `v` and the already validated extended-isomorphism lower-bound branch; remove “reapplying the ambient setup”. |
| `1.2.3.2` | Cite the data-only notation field for `tilde-Upsilon=u tilde-Phi`, cite formation for `u=v^(-1)`, and retain validated child `1.2.3.2.1` for the estimates. |

The validated children already contain the substantive AI, MAIN,
finite-dimensionality, inverse, complete-contractivity, and scalar
arithmetic arguments.  The amendments repair only root scope, formation, and
same-output identity; they may not replace those arguments by a definition
unpack.

**Revised budget:** target 20 total nodes; hard stop 22; at most 6 resumed
rounds.  Four bottom-up waves remain forced by
`1.1.1.1 -> 1.1.1 -> 1.1 -> 1`, while the inverse branch can run in
parallel.  Exceeding 22 or 6 rounds is a factoring stop.

### 5.3 `lem-routef-raw-factor-identities`

Current state: 5 nodes, 4 validated, root `1` pending.  Add the vocabulary and
formation external above, then amend only root `1` to the exact row-3
contract in section 3.2.

Validated node `1.1` remains a conditional analytic setup lemma and validated
node `1.2` remains the abstract algebraic identity.  The amended root uses
the formation external to instantiate `1.1` on the root's same `W_RF,S,B,v`,
then applies `1.2`.  The definition supplies only the notation; formation
supplies exact idempotence, the AI structure, and the MAIN output.  Resolve
`ch-fe50a1d47d30ca64` only after the root amendment and external
registration.

**Revised budget:** target 5 total nodes / one fresh root-review round.  If a
verifier requires an explicit bridge matching the formation-produced `v` to
the conditional setup's `v`, add one pending child and stop at 6 total nodes
/ 2 rounds.  Do not unvalidate or amend nodes `1.1` or `1.2`.

Neither continuation changes registry status by itself.  Both rows remain
`stated` / `seeded` until the normal fresh-verifier and banking protocol
finishes.

## 6. Blast radius and future strengthened K-ledger

### 6.1 Authorized future landing surface

An eventual implementation of this package would touch:

- one new locked definition after ratification;
- one new `stated` formation shard;
- the `contract:`, `defs:`, and `deps:` lines of the sixteen `stated` rows;
- the row-3 explanatory body sentence from audit finding 8;
- the two live af ledgers exactly as section 5 specifies; and
- generated definition/argument/report artifacts required by the gates.

No scalar-ledger formula changes.  No row 1--13 or D2/D3 mathematical suffix
changes.  Only row 14's contract is replaced by the conservative scalar
interface in section 3.5.  No status is promoted.

### 6.2 Strengthened `lem-routef-k-ledger`

The future strengthened parent must add
`lem-routef-raw-factor-setting-formation` as a direct dependency.  It uses
the T0 F0 seam to obtain `(H,Phi,eta)`, checks
`eta<=eta_K<=rho_T<=rho_id^corr`, applies formation to the **same** `Phi` and
`eta`, and receives one `S` over the already fixed global `W_RF`.

It must also import rows 5, 6, 8, and 9 directly.  The telescope contracts
prove estimates for an explicitly threaded packet; they do not by themselves
export that a packet exists.  The strengthened parent must construct the
packet before instantiating rows 10--14.  Its corrected future dependency
block is therefore:

```text
deps: lem-routef-f0-ucp-lift; lem-routef-f0-defect-identity; lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness; lem-routef-delta-upsilon-telescope; lem-routef-multiplicative-telescope; lem-routef-upsilon-delta-telescope; lem-routef-k-finiteness; lem-routef-threshold-minimum; lem-routef-f2-positive-unital-compression; lem-routef-f3-retract-defect; lem-routef-prh-finish
```

The application order is:

```text
F0 -> formation -> row 5 -> row 6 -> row 8 -> row 9
   -> rows 10,11,12 -> row 13 -> row 14
   -> F2 -> F3 -> PRH.
```

Row 14 now supplies exactly the scalar facts needed at the last line.  The
parent, where `Q,D,J,Q_C,A,M` and the same map packet are bound, performs the
actual F2/F3/PRH applications.

The old 11-node parent estimate is no longer an honest budget because it
omitted formation and packet construction.  A conservative replacement
projection is target 17 nodes / 4 rounds / hard cap 22, to be re-audited with
the strengthened-parent landing package.

### 6.3 F0 assembly and guard

`lem-routef-f0-assembly` still consumes only the future strengthened
`lem-routef-k-ledger`; it does not duplicate formation, packet, F2, F3, or
PRH edges.  Its contract does not change in this repair.

**The DO-NOT-REWIRE guard remains untouched.**  This design does not edit the
landed `lem-routef-k-ledger`, `lem-routef-f0-assembly`, `op-classical`, any
root route, or any status.  The strengthened dependency block above is a
future landing requirement, not an enacted rewire.

## 7. Ranked risks for the v2 hostile re-audit

1. **Formation still too strong or too weak.**  Attack both directions:
   delete the formation row and confirm the definition proves nothing; then
   retain formation and verify it really derives one `S` for every input on
   `rho_id^corr` from the three direct provider contracts.
2. **Global-witness quantifier drift.**  Try to reselect
   `eta_A,C_A,C_E,epsilon_E` after seeing `(H,Phi,eta)`.  The contract must
   forbid this, and every later row must use the same `W_RF`.
3. **Same-output drift.**  Attempt to take `Delta` from a different `Delta'`,
   `Upsilon'` from a different normalized map, or `Upsilon` from a different
   triple.  Each contract and each direct edge must force the one displayed
   chain.
4. **Hidden vacuity in row 13 or row 14.**  Verify that formation plus rows
   5, 6, 8, and 9 actually produce the packet used to instantiate row 13,
   rather than merely quantifying over an empty class.
5. **Row-14 overreach.**  Confirm that the new contract asserts only the
   section-3.5 scalar inequalities.  It must not mention F2/F3/PRH
   admissibility or infer any stochastic/map data.
6. **Direct-edge incompleteness.**  Re-run audit finding 4 row by row.  In
   particular check additions: row 7 `+5`; row 8 `+5`; row 9 `+5,+6`; row 10
   `+5,+8`; row 11 `+5,+6,+8`; row 12 `+5,+8`; rows 13 and 14
   `+5,+6,+8,+9`.
7. **Matrix-variable scope.**  Inspect rows 1, 4, D2, 7, D3, and 11 for a
   literal `n>=1` binder and universal `X,Y,Z` domains; do not rely on “every
   amplification” to bind vectors.
8. **Suffix or scalar drift.**  Strip each prefix for the fifteen unchanged
   rows and byte-compare with the landed contracts.  Separately compare row
   14's inequalities with `DESIGN-LEDGER-DOMAINS-v2.md` section 3.5.
9. **L2 duplication or missing vocabulary.**  Check that the setting shard
   references, rather than redefines, UCP/extended-algebra/extended-isomorphism
   terms, and that both live workspaces provision `def-ucp-map` once.
10. **Mechanical preservation mistaken for validation.**  An amended node
    and every amended ancestor require fresh hostile review even when all
    descendants retain their validated state.
11. **Strengthened-parent underwiring.**  Delete formation or any of rows 5,
    6, 8, 9 from the future K-ledger block and verify that construction of the
    same packet fails.  Telescope imports alone are not existential packet
    producers.
12. **Premature guard release or promotion.**  A repository diff for this
    design round must contain only this file.  All sixteen rows remain
    `stated`, both live roots remain pending, and DO-NOT-REWIRE remains in
    force.

## 8. Audit and ratification gate

A separate fresh hostile auditor should return one of `LAND`,
`LAND-WITH-EXACT-CORRECTIONS`, or `DESIGN-REJECTED`, explicitly disposing
all twelve risks and all eight binding findings.  Only a subsequent explicit
user ratification authorizes implementation.

Until then:

- no definition or formation row is added;
- no registry contract, `defs:`, `deps:`, body, or status is changed;
- no af definition/external is registered and no node is amended;
- all sixteen rows remain `status: stated`;
- the two live workspaces remain `af: seeded`; and
- the strengthened K-ledger and DO-NOT-REWIRE guard remain untouched.
