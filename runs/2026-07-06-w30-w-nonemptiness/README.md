# Run bundle: W30 — W-nonemptiness (Kernel(i)) prove-or-refute pair (2026-07-06, session 11)

## Hypothesis

Sketch v7 ledger item 6 / bd `aism-jwg`: is there a universal delta_0 > 0 such that every exact
signed idempotent P with delta(P) <= delta_0 has W(P) nonempty? Mutually-blind pair: worker T
(prove) vs worker U (refute: hunt an exact instance with EMPTY visible set).

## Finding

- Worker T (verbatim first line): `PARTIAL (proved: δ=0 endpoint, and δ≤1/4 W-nonemptiness when
  the row polytope is a simplex, in particular affine dimension ≤1 / rank≤2; gap: no
  dimension-free mechanism found forcing a simplex/sharp vertex from P²=P and small δ)` —
  hostile verifier VT dispatched on the simplex-visibility / sharp-vertex / rank<=2 claims;
  VT verdict: `VALID-WITH-CORRECTIONS` — codified as `lem-simplex-visibility`,
  `lem-sharp-vertex-visibility` (corrected hull), `cor-rank-two-visible`.
- Worker U (verbatim first line): `NOT-REFUTED (searched: exact audits + 297 admissible random
  Lambda-C idempotents; sharpest obstruction: hiddenness forces a far-row barycenter near each
  hidden vertex, and all constructions needed visible anchors for that barycenter)`.
- Convergent structural diagnosis (T's gap == U's obstruction, and it matches W26's witness):
  hiddenness NEEDS visible anchors — the candidate mechanism for the missing dimension-free
  production theorem is "an empty W leaves every witness anchorless" (next W-nonemptiness wave).

## Command

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -u runs/2026-07-06-w30-w-nonemptiness/scripts/w30_worker_u_audit.py --samples 2000 --seed 30031
```

(Worker U's script, recovered verbatim from its /tmp scratch into `scripts/` before expiry.)

## Invariant / checkable

Exact rational audits inside the script: W25 3×3 canonical geometry (no hidden vertices,
t*(1) = 100/101, t*(2) = 1); the rank-5 calibration (W = {0,1,2}, hidden rows 3,4 with
t* = 1/41 — matching the independently banked W26 values exactly); random pass
samples=2000/seed=30031 → audited=297, hidden_vertex_records=15, found_W_empty=False.

## Next

DONE: the trio codified on VT's verdict (see `docs/waves/2026-07-06-W30-w-nonemptiness.md`).
Next wave: the anchorless-witness contradiction attempt (assume W = ∅, apply the hiddenness
dual witness at an extremal vertex, derive contradiction) — the first mechanism candidate for
the dimension-free production theorem at rank >= 3.

## Honest scope (L3)

Worker U's search is bounded evidence ONLY (n-bounded ΛC sampling; NO emptiness claim). The
[T0] lines are exact facts about the audited instances. Worker T's claims are worker-T1 until
VT reports; nothing here is af-validated or L0-rigorous.
