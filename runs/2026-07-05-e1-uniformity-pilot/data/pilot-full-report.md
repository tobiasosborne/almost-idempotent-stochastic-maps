Largest certified ratio seen: `sqrt(61937/32768)` (`r^2=61937/32768`), at `Hume-positive-part s=1/16` with `eta=241/32896` and `||Q-E||=241/2048`.
The `n=4..12` coupled stochastic averaging family has bounded monotone drift only: `r^2` goes from `3/23` to `11/69`; this is a bounded pilot, not evidence of a uniform theorem.

## Protocol and tier tags

[T0] means directly recomputed by the script from the printed rational matrices. [T1] means a short derivation from `E^2=E` or block/clone algebra, checked on examples. [T2] means pilot interpretation. [T3] means suggested next work.

Rerun command:

```bash
python3 runs/2026-07-05-e1-uniformity-pilot/scripts/e1_worker_b_pilot.py
```

## Task 1 -- anchors from `ex-hume`

[T1] Locus used: `argument/lemmas/ex-hume.md` gives the signed exact family `P_s=I-u_s v_s^T`, with `v_s=(1,-1+s,-s)` and `u_s=(1-s+s^2,-s,0)^T`; its status is `proved-mod-audit`, so I use it only as a calibration source, not as a rigorous theorem.

[T1] Stochastic conversion used here: rowwise positive-part normalization of that signed `P_s`. Since `P_s` has a single negative entry `-s^2`, this changes `P_s` by order `s^2`; all reported `eta`, distances, and ratios below are recomputed from the resulting nonnegative row-stochastic `Q_s` alone.

| s | true n=3 min type | eta(Q) | min_E ||Q-E|| | r^2 | r |
|---|---|---:|---:|---:|---:|
| `1/3` | `singleton 2 plus recurrent pair (0, 1)` | `7/45` | `14/27` | `140/81` | `sqrt(140/81)` |
| `1/5` | `singleton 2 plus recurrent pair (0, 1)` | `21/325` | `42/125` | `1092/625` | `sqrt(1092/625)` |
| `1/8` | `singleton 2 plus recurrent pair (0, 1)` | `57/2080` | `57/256` | `3705/2048` | `sqrt(3705/2048)` |
| `1/16` | `singleton 2 plus recurrent pair (0, 1)` | `241/32896` | `241/2048` | `61937/32768` | `sqrt(61937/32768)` |

[T0] Anchor headline matrices:

### Hume-positive-part anchor s=1/3

`eta=7/45`, `min_E ||Q-E||=14/27`, `r^2=140/81`, `r=sqrt(140/81)`.

Q:
- [2/9, 14/27, 7/27]
- [3/10, 7/10, 0]
- [0, 0, 1]

Certified minimizing E among all 3x3 stochastic idempotents:
- [2/9, 7/9, 0]
- [2/9, 7/9, 0]
- [0, 0, 1]

### Hume-positive-part anchor s=1/5

`eta=21/325`, `min_E ||Q-E||=42/125`, `r^2=1092/625`, `r=sqrt(1092/625)`.

Q:
- [4/25, 84/125, 21/125]
- [5/26, 21/26, 0]
- [0, 0, 1]

Certified minimizing E among all 3x3 stochastic idempotents:
- [4/25, 21/25, 0]
- [4/25, 21/25, 0]
- [0, 0, 1]

### Hume-positive-part anchor s=1/8

`eta=57/2080`, `min_E ||Q-E||=57/256`, `r^2=3705/2048`, `r=sqrt(3705/2048)`.

Q:
- [7/64, 399/512, 57/512]
- [8/65, 57/65, 0]
- [0, 0, 1]

Certified minimizing E among all 3x3 stochastic idempotents:
- [7/64, 57/64, 0]
- [7/64, 57/64, 0]
- [0, 0, 1]

### Hume-positive-part anchor s=1/16

`eta=241/32896`, `min_E ||Q-E||=241/2048`, `r^2=61937/32768`, `r=sqrt(61937/32768)`.

Q:
- [15/256, 3615/4096, 241/4096]
- [16/257, 241/257, 0]
- [0, 0, 1]

Certified minimizing E among all 3x3 stochastic idempotents:
- [15/256, 241/256, 0]
- [15/256, 241/256, 0]
- [0, 0, 1]

## Task 2 -- exact minimum at n=3

[T1] Structure derived from `E^2=E`: each row `e_i` is stationary for `E` because `e_iE=e_i`. Recurrent communicating classes are closed; inside one recurrent class all rows must be the same stationary distribution on that class, while every transient row is a convex mixture of those recurrent-class stationary rows. For `n=3`, this leaves only: identity; one rank-one class; one singleton plus one two-state recurrent class; or two singleton classes plus one transient row.

[T0] The script enumerates exactly those `n=3` structures. The rank-one case is a 2-variable exact LP. The other nontrivial cases are 1-variable exact LPs. The objective is `max_i ||Q_i-E_i||_1`, encoded by all `2^3` sign inequalities per row and solved by exact rational vertex enumeration.

Additional exact-minimum instances:

| instance | true n=3 min type | eta(Q) | min_E ||Q-E|| | r^2 | r |
|---|---|---:|---:|---:|---:|
| `lazy-cycle a=1/10` | `I_3` | `9/50` | `1/5` | `2/9` | `sqrt(2/9)` |
| `uniform-cycle a=1/10` | `rank-one all rows equal p` | `7/50` | `2/15` | `8/63` | `sqrt(8/63)` |

### lazy-cycle a=1/10

`eta=9/50`, `min_E ||Q-E||=1/5`, `r^2=2/9`, `r=sqrt(2/9)`.

Q:
- [9/10, 1/10, 0]
- [0, 9/10, 1/10]
- [1/10, 0, 9/10]

Certified minimizing E among all 3x3 stochastic idempotents:
- [1, 0, 0]
- [0, 1, 0]
- [0, 0, 1]

### uniform-cycle a=1/10

`eta=7/50`, `min_E ||Q-E||=2/15`, `r^2=8/63`, `r=sqrt(8/63)`.

Q:
- [3/10, 2/5, 3/10]
- [3/10, 3/10, 2/5]
- [2/5, 3/10, 3/10]

Certified minimizing E among all 3x3 stochastic idempotents:
- [1/3, 1/3, 1/3]
- [1/3, 1/3, 1/3]
- [1/3, 1/3, 1/3]

## Task 3 -- clone and block invariance sanity checks

[T1] Cloning one state with split weights `alpha_b` replaces every cloned column entry by `alpha_b` times the old entry and duplicates the cloned row pattern. Matrix multiplication commutes with this split operation, so `Q^2-Q` clones exactly and its max row `l1` norm is unchanged. Cloning an idempotent candidate `E` gives an idempotent candidate with exactly the same distance.

[T0] Clone example: state 2 of the `s=1/3` Hume-positive-part anchor is split with weights `2/5,3/5`.

`eta=7/45`, `||Q_clone-E_clone||=14/27`, `r^2=140/81`, `r=sqrt(140/81)`.

Q_clone:
- [2/9, 14/27, 14/135, 7/45]
- [3/10, 7/10, 0, 0]
- [0, 0, 2/5, 3/5]
- [0, 0, 2/5, 3/5]

E_clone:
- [2/9, 7/9, 0, 0]
- [2/9, 7/9, 0, 0]
- [0, 0, 2/5, 3/5]
- [0, 0, 2/5, 3/5]

[T1] For block direct sums, `(Q_1⊕Q_2)^2-(Q_1⊕Q_2)` is the block sum of the two defects, so `eta` is the maximum of the block etas. A block-sum candidate `E_1⊕E_2` is idempotent stochastic and its distance is the maximum of the two block distances. This gives a no-growth construction; it is not a proof about arbitrary cross-block idempotents.

[T0] Block example: `Hume s=1/5` block-summed with `lazy-cycle a=1/10`.

`eta=9/50`, `||Q_block-E_block||=42/125`, `r^2=392/625`, `r=sqrt(392/625)`.

Q_block:
- [4/25, 84/125, 21/125, 0, 0, 0]
- [5/26, 21/26, 0, 0, 0, 0]
- [0, 0, 1, 0, 0, 0]
- [0, 0, 0, 9/10, 1/10, 0]
- [0, 0, 0, 0, 9/10, 1/10]
- [0, 0, 0, 1/10, 0, 9/10]

E_block:
- [4/25, 21/25, 0, 0, 0, 0]
- [4/25, 21/25, 0, 0, 0, 0]
- [0, 0, 1, 0, 0, 0]
- [0, 0, 0, 1, 0, 0]
- [0, 0, 0, 0, 1, 0]
- [0, 0, 0, 0, 0, 1]

## Task 4 -- one coupled n-growing stochastic family

[T1] Family: levels `0,...,n-1`, state 0 absorbing; for `i>0`, row `i` puts `1-i/(12n)` on state 0 and `1/(12n)` on each level `1,...,i`. This is not a clone or direct sum: increasing `n` changes the coupling pattern of every high-level row and all high levels send mass through a shared lower-level chain. Candidate `E_n` collapses every row to state 0.

[T2] These are constructed-candidate ratios only. They do not lower-bound the true error-bound constant; a larger value could mean the construction is bad, and a bounded value only says this family did not visibly break uniformity.

| n | eta(Q_n) | ||Q_n-E_n|| | r^2 | r |
|---:|---:|---:|---:|---:|
| 4 | `23/192` | `1/8` | `3/23` | `sqrt(3/23)` |
| 5 | `23/180` | `2/15` | `16/115` | `sqrt(16/115)` |
| 6 | `115/864` | `5/36` | `10/69` | `sqrt(10/69)` |
| 7 | `23/168` | `1/7` | `24/161` | `sqrt(24/161)` |
| 8 | `161/1152` | `7/48` | `7/46` | `sqrt(7/46)` |
| 9 | `23/162` | `4/27` | `32/207` | `sqrt(32/207)` |
| 10 | `23/160` | `3/20` | `18/115` | `sqrt(18/115)` |
| 11 | `115/792` | `5/33` | `40/253` | `sqrt(40/253)` |
| 12 | `253/1728` | `11/72` | `11/69` | `sqrt(11/69)` |

[T0] Coupled-family matrices for every reported `n`:

### level-coupled n=4

`eta=23/192`, `||Q-E||=1/8`, `r^2=3/23`, `r=sqrt(3/23)`.

Q:
- [1, 0, 0, 0]
- [47/48, 1/48, 0, 0]
- [23/24, 1/48, 1/48, 0]
- [15/16, 1/48, 1/48, 1/48]

E:
- [1, 0, 0, 0]
- [1, 0, 0, 0]
- [1, 0, 0, 0]
- [1, 0, 0, 0]

### level-coupled n=5

`eta=23/180`, `||Q-E||=2/15`, `r^2=16/115`, `r=sqrt(16/115)`.

Q:
- [1, 0, 0, 0, 0]
- [59/60, 1/60, 0, 0, 0]
- [29/30, 1/60, 1/60, 0, 0]
- [19/20, 1/60, 1/60, 1/60, 0]
- [14/15, 1/60, 1/60, 1/60, 1/60]

E:
- [1, 0, 0, 0, 0]
- [1, 0, 0, 0, 0]
- [1, 0, 0, 0, 0]
- [1, 0, 0, 0, 0]
- [1, 0, 0, 0, 0]

### level-coupled n=6

`eta=115/864`, `||Q-E||=5/36`, `r^2=10/69`, `r=sqrt(10/69)`.

Q:
- [1, 0, 0, 0, 0, 0]
- [71/72, 1/72, 0, 0, 0, 0]
- [35/36, 1/72, 1/72, 0, 0, 0]
- [23/24, 1/72, 1/72, 1/72, 0, 0]
- [17/18, 1/72, 1/72, 1/72, 1/72, 0]
- [67/72, 1/72, 1/72, 1/72, 1/72, 1/72]

E:
- [1, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0]

### level-coupled n=7

`eta=23/168`, `||Q-E||=1/7`, `r^2=24/161`, `r=sqrt(24/161)`.

Q:
- [1, 0, 0, 0, 0, 0, 0]
- [83/84, 1/84, 0, 0, 0, 0, 0]
- [41/42, 1/84, 1/84, 0, 0, 0, 0]
- [27/28, 1/84, 1/84, 1/84, 0, 0, 0]
- [20/21, 1/84, 1/84, 1/84, 1/84, 0, 0]
- [79/84, 1/84, 1/84, 1/84, 1/84, 1/84, 0]
- [13/14, 1/84, 1/84, 1/84, 1/84, 1/84, 1/84]

E:
- [1, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0]

### level-coupled n=8

`eta=161/1152`, `||Q-E||=7/48`, `r^2=7/46`, `r=sqrt(7/46)`.

Q:
- [1, 0, 0, 0, 0, 0, 0, 0]
- [95/96, 1/96, 0, 0, 0, 0, 0, 0]
- [47/48, 1/96, 1/96, 0, 0, 0, 0, 0]
- [31/32, 1/96, 1/96, 1/96, 0, 0, 0, 0]
- [23/24, 1/96, 1/96, 1/96, 1/96, 0, 0, 0]
- [91/96, 1/96, 1/96, 1/96, 1/96, 1/96, 0, 0]
- [15/16, 1/96, 1/96, 1/96, 1/96, 1/96, 1/96, 0]
- [89/96, 1/96, 1/96, 1/96, 1/96, 1/96, 1/96, 1/96]

E:
- [1, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0]

### level-coupled n=9

`eta=23/162`, `||Q-E||=4/27`, `r^2=32/207`, `r=sqrt(32/207)`.

Q:
- [1, 0, 0, 0, 0, 0, 0, 0, 0]
- [107/108, 1/108, 0, 0, 0, 0, 0, 0, 0]
- [53/54, 1/108, 1/108, 0, 0, 0, 0, 0, 0]
- [35/36, 1/108, 1/108, 1/108, 0, 0, 0, 0, 0]
- [26/27, 1/108, 1/108, 1/108, 1/108, 0, 0, 0, 0]
- [103/108, 1/108, 1/108, 1/108, 1/108, 1/108, 0, 0, 0]
- [17/18, 1/108, 1/108, 1/108, 1/108, 1/108, 1/108, 0, 0]
- [101/108, 1/108, 1/108, 1/108, 1/108, 1/108, 1/108, 1/108, 0]
- [25/27, 1/108, 1/108, 1/108, 1/108, 1/108, 1/108, 1/108, 1/108]

E:
- [1, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0]

### level-coupled n=10

`eta=23/160`, `||Q-E||=3/20`, `r^2=18/115`, `r=sqrt(18/115)`.

Q:
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [119/120, 1/120, 0, 0, 0, 0, 0, 0, 0, 0]
- [59/60, 1/120, 1/120, 0, 0, 0, 0, 0, 0, 0]
- [39/40, 1/120, 1/120, 1/120, 0, 0, 0, 0, 0, 0]
- [29/30, 1/120, 1/120, 1/120, 1/120, 0, 0, 0, 0, 0]
- [23/24, 1/120, 1/120, 1/120, 1/120, 1/120, 0, 0, 0, 0]
- [19/20, 1/120, 1/120, 1/120, 1/120, 1/120, 1/120, 0, 0, 0]
- [113/120, 1/120, 1/120, 1/120, 1/120, 1/120, 1/120, 1/120, 0, 0]
- [14/15, 1/120, 1/120, 1/120, 1/120, 1/120, 1/120, 1/120, 1/120, 0]
- [37/40, 1/120, 1/120, 1/120, 1/120, 1/120, 1/120, 1/120, 1/120, 1/120]

E:
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

### level-coupled n=11

`eta=115/792`, `||Q-E||=5/33`, `r^2=40/253`, `r=sqrt(40/253)`.

Q:
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [131/132, 1/132, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [65/66, 1/132, 1/132, 0, 0, 0, 0, 0, 0, 0, 0]
- [43/44, 1/132, 1/132, 1/132, 0, 0, 0, 0, 0, 0, 0]
- [32/33, 1/132, 1/132, 1/132, 1/132, 0, 0, 0, 0, 0, 0]
- [127/132, 1/132, 1/132, 1/132, 1/132, 1/132, 0, 0, 0, 0, 0]
- [21/22, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 0, 0, 0, 0]
- [125/132, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 0, 0, 0]
- [31/33, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 0, 0]
- [41/44, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 0]
- [61/66, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132, 1/132]

E:
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

### level-coupled n=12

`eta=253/1728`, `||Q-E||=11/72`, `r^2=11/69`, `r=sqrt(11/69)`.

Q:
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [143/144, 1/144, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [71/72, 1/144, 1/144, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [47/48, 1/144, 1/144, 1/144, 0, 0, 0, 0, 0, 0, 0, 0]
- [35/36, 1/144, 1/144, 1/144, 1/144, 0, 0, 0, 0, 0, 0, 0]
- [139/144, 1/144, 1/144, 1/144, 1/144, 1/144, 0, 0, 0, 0, 0, 0]
- [23/24, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 0, 0, 0, 0, 0]
- [137/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 0, 0, 0, 0]
- [17/18, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 0, 0, 0]
- [15/16, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 0, 0]
- [67/72, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 0]
- [133/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144, 1/144]

E:
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
- [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

## Assert list

[T0] The script exits nonzero unless every item below is recomputed from the printed matrices/candidates:

- Hume-positive-part s=1/3: eta=7/45, dist=14/27, r^2=140/81
- Hume-positive-part s=1/5: eta=21/325, dist=42/125, r^2=1092/625
- Hume-positive-part s=1/8: eta=57/2080, dist=57/256, r^2=3705/2048
- Hume-positive-part s=1/16: eta=241/32896, dist=241/2048, r^2=61937/32768
- lazy-cycle a=1/10: eta=9/50, dist=1/5, r^2=2/9
- uniform-cycle a=1/10: eta=7/50, dist=2/15, r^2=8/63
- clone of Hume-positive-part s=1/3: eta=7/45, dist=14/27, r^2=140/81
- block sum Hume s=1/5 with lazy-cycle a=1/10: eta=9/50, dist=42/125, r^2=392/625
- level-coupled n=4: eta=23/192, dist=1/8, r^2=3/23
- level-coupled n=5: eta=23/180, dist=2/15, r^2=16/115
- level-coupled n=6: eta=115/864, dist=5/36, r^2=10/69
- level-coupled n=7: eta=23/168, dist=1/7, r^2=24/161
- level-coupled n=8: eta=161/1152, dist=7/48, r^2=7/46
- level-coupled n=9: eta=23/162, dist=4/27, r^2=32/207
- level-coupled n=10: eta=23/160, dist=3/20, r^2=18/115
- level-coupled n=11: eta=115/792, dist=5/33, r^2=40/253
- level-coupled n=12: eta=253/1728, dist=11/72, r^2=11/69

## Task 5 -- protocol for wave 2

[T2] This pilot saw no obvious dimension blowup. The largest exact ratio came from the stochasticized `ex-hume` anchor, not from the `n`-growing coupled chain. That is consistent with the known sharp `sqrt` mechanism but does not address uniformity.

[T3] A decision-grade kill wave should not spend time on clones or direct sums. It should search genuinely coupled, quotient-many-class families: the `FINDINGS.md` 2026-07-02 web-regime entry says the plausible wall is dimension-many genuine outside quotient classes, and `argument/lemmas/obs-fwr-gap.md` says common-pattern web rigidity cannot give a dimension-free shallow-class count.

[T3] Concrete wave-2 computation: generate exact signed idempotents with `build_from_LambdaC`-style rank-growing webs, convert to stochastic almost-idempotents by a fixed audited projection rule, and for each `n<=8` compute a certified two-sided bracket on `min_E ||Q-E||` using an exact LP/MILP over stochastic-idempotent support structures. For `n=9..12`, keep constructed candidates but add independent lower bounds from quotient/lumping certificates.

[T3] Decision-grade support would be: all quotient-web families tested have true or tightly bracketed ratios bounded by a small constant, with the worst cases collapsing to Hume-like local obstructions. Decision-grade kill would be: a coupled rank-growing family with exact matrices, `eta -> 0`, and certified lower bounds on `min_E ||Q-E||/sqrt(eta)` increasing with `n`, not just a poor constructed `E`.
