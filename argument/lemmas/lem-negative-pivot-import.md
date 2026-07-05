---
id: lem-negative-pivot-import
kind: lemma
contract: Negative-pivot collateral import bound: let P be a rank-3 exact signed idempotent (square real matrix with P^2 = P and all row sums equal to 1), let U = (u_0,u_1,u_2) be an actual-row chart whose rows p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space, define coordinates a_q(i) by p_i = sum_q a_q(i)p_{u_q}, beta_r(i) = P_{u_r i}, E_r(i) = max(sum_{q != r} max(-a_q(i),0) - (1 - a_r(i)), 0), and Phi_r(U) = sum_i max(beta_r(i),0)E_r(i); fix a pivot index s, a non-chart row j with c = a_s(j) < 0, a transverse index r != s, and let t be the remaining index, writing d_r = a_r(j) and d_t = a_t(j); on the pivot-removing chart V_j = U - u_s + j define new coordinates a_s^j(i) = a_s(i)/c and a_q^j(i) = a_q(i) - a_s(i)a_q(j)/c for q != s, E_r^j(i) = max(sum_{q != r} max(-a_q^j(i),0) - (1 - a_r^j(i)), 0), and Phi_r(V_j) = sum_i max(beta_r(i),0)E_r^j(i) (the transverse left-inverse row at r is unchanged by the move); define R^-_{r,j}(i) = max(a_s(i),0)/(-c) - max(-a_s(i),0) + max(a_s(i)*d_t/c, 0) - a_s(i)*d_r/c and I^-_{r,j}(U) = sum_i max(beta_r(i),0)*max(R^-_{r,j}(i),0); then Phi_r(V_j) <= Phi_r(U) + I^-_{r,j}(U).
defs: def-signed-idempotent
deps: lem-pivot-removing-move
status: proved-mod-audit
af: seeded
provenance: docs/waves/2026-07-04-G13-b-lemma-conditional.md §1 (sign-agnostic coordinate transform) and §2 (pointwise bound E_r^j(i) <= E_r(i) + (R^-_{r,j}(i))^+ and summed import bound); independent codex review APPROVE docs/waves/2026-07-04-G13-review.md §§1-2 (adversarial exact rational grid over every case split, 0 failures)
owner: A
workspace: proofs/lem-negative-pivot-import
---

**The c<0 companion to the validated (CI) inequality** [[lem-collateral-import]] (which covers only
`c = a_s(j) > 0`). The coordinate transform of [[lem-pivot-removing-move]] is sign-agnostic; with
`c = -k < 0`, `x = a_s(i)`, the per-row step is

```text
E_r^j(i) <= E_r(i) + max(R^-_{r,j}(i), 0),
```

proved via `(-x/c)^+ = x^+/k` and the four-case inequality `(-y+w)^+ <= y^- + w^+`, then
`(A+B)^+ <= A^+ + B^+`; summing against `max(beta_r(i),0)` (transverse left-inverse row unchanged)
gives the contract inequality.

**Exact split (G13 §2, review-checked).** For `x = a_s(i)`:

```text
x >= 0:  R^-_{r,j}(i) = x * (1 + d_t^- + d_r)/(-c),
x <  0:  R^-_{r,j}(i) = x^- * ((d_t^+ - d_r)/(-c) - 1).
```

Consequently, with the cross-pivot masses `A_{r,s} = sum_i beta_r(i)^+ a_s(i)^+` and
`B_{r,s} = sum_i beta_r(i)^+ a_s(i)^-` of [[lem-cross-pivot-cancellation]],

```text
I^-_{r,j}(U) <= ((1+d_t^-+d_r)^+/(-c)) A_{r,s} + (((d_t^+-d_r)/(-c)-1)^+) B_{r,s},
```

and per the reviewer's sharpening this displayed bound is an **equality** under the exact split and
the standard definitions of `A_{r,s}` and `B_{r,s}` (the written `<=` is safe).

**Not the same algebra as (CI).** The `1/|c|` term now lands on `A_{r,s}` (not `B_{r,s}`), and the
B-side coefficient carries a subtractive `-1`.

**Role and limits (G13 §3).** For a Gamma-blocked admissible `c<0` carrier `i` this gives the
lower forcing `Phi_s(U) - Phi_q(U) <= I^-_{q,i}(U)` — a diagnostic, not an upper charge on the
carrier mass `beta_r(i)^+ a_s(i)^-`. Psi-blocked moves are NOT controlled (the new left-inverse
row for coordinate `s` is `P_i`, not an unchanged transverse row). The missing reverse principle
is exactly [[conj-nsc]].

**Status honesty.** Review-approved paper proof (reviewer != author, G13 review APPROVE,
exact-verified on 3 certified instances with `min_row_slack = 0` somewhere); NOT af-validated.
Elevation decision deferred to the wave-14 harvest per the session-7 audit policy (elevate what a
proof leans on under adversarial pressure).
