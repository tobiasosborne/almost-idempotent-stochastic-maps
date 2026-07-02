A = **REPAIR CONFIRMED**, but **`V=0` at argmin is refuted**, not proved.

B = **RANK-2 THEOREM**: both rank-2 horns close with explicit `C=2`; higher-rank NDG remains open.

Saved artifacts:

- [proof.md](/tmp/codex-sigma-wall/w40_ndg/proof.md): verdict-first long form.
- [progress.md](/tmp/codex-sigma-wall/w40_ndg/progress.md): stage log.
- [verify_part_a.py](/tmp/codex-sigma-wall/w40_ndg/verify_part_a.py), [part_a_results.txt](/tmp/codex-sigma-wall/w40_ndg/part_a_results.txt): independent exact Part A audit.
- [rank2_explorer.py](/tmp/codex-sigma-wall/w40_ndg/rank2_explorer.py), [rank2_results.txt](/tmp/codex-sigma-wall/w40_ndg/rank2_results.txt): exact rank-2 random/adversarial checks.

Key findings:

- `(P1)` is proved by sign split and exact-checked on all mandatory families.
- `(SB*)` numerics reproduce: mandatory selected charts have `S*/delta <= 3`.
- Literal `V=0` fails on perturbed staircase `m=5, eps=1/1000`: selected argmin has `V/delta = 1/500000`.
- `(DEF)` coupling is confirmed: `Dpos - V = Dneg`, but it is not a free bound on `V`.
- Rank 2: max-diameter chart has `Phi=0`, hence every `Phi`-argmin has no positive-beta overshoot and `S*_s <= 2 delta`.

Verification run:

```text
python3 verify_part_a.py
python3 rank2_explorer.py
python3 -m py_compile verify_part_a.py rank2_explorer.py
```

No `answer.md` was created.