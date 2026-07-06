FORCED-STRUCTURE (statement: `t*(v)<kappa` forces a convex combination of `rho`-far rows within `kappa*(2+4*delta)` of `p_v`; W25’s self-loop model lacks this and becomes visible)

Created the Worker Q outputs:

- [w26_worker_q.py](/home/tobias/Projects/almost-idempotent-stochastic-maps/runs/2026-07-06-w26-hiddenness/scripts/w26_worker_q.py)
- [worker-q-report.md](/home/tobias/Projects/almost-idempotent-stochastic-maps/runs/2026-07-06-w26-hiddenness/data/worker-q-report.md)

Key result: no second F0-F10 insufficiency certificate was found. The exact output is the hiddenness dual/gauge structure, verified against W25 and a true-hidden rank-5 calibration. The bounded exact search (`n <= 10`, 1000 Lambda-C samples) found 0 tall `H > 13*tau` sustained webs; this is tagged [T3], not an emptiness claim.

Validation run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 runs/2026-07-06-w26-hiddenness/scripts/w26_worker_q.py --samples 1000
```

I did not run `fr`, `bd`, commit, or modify the forbidden core paths.