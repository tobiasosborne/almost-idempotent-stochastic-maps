VERDICT: VALID-AS-CONDITIONAL / INVALID

For `lem-low-slab-cap-implies-min-a`, the mass split and constants are correct once the contract explicitly assumes the low-slab cap with \(a=4\), \(\theta=1/2\), and \(\delta_0\ge(17-12\sqrt2)/2\). Without these additions, the source conjecture supplies only existential constants, and the bridge covers merely \(\delta\le\min(\delta_0,(17-12\sqrt2)/2)\), not the full MIN-A interval.

For `lem-huddle-charge-assembly`, the consumed contracts do not close Branch II: `lem-l2-core-collapse` proves only an equivalence with intersection-branch emptiness, while no registered contract derives the SL1a-or-SL1b configurations from intersecting hulls. L5 is also unregistered and not a quantified premise. AG-1 and AG-2 are individually repairable from proved contracts, but that does not cure the silent Branch-II gap.

Full audit: [VERDICT-BRIDGES.md](/tmp/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/d1b58f04-639e-4098-8f70-3061c0e4323e/scratchpad/bridges-verify/ws/VERDICT-BRIDGES.md)