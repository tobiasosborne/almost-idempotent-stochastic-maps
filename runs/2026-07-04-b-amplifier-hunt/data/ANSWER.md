# Wave 13 amplifier exact-rational answer

Status: L3 numerical evidence only; not a proof.

## Headline

Best certified clean high-self non-fan Gamma argmin found: `90516217933510287011133600/116398566910735274162898787` at `delta=590855669597640985598471/10775740230179796072754000` (`shape-a=6332623/370881409`, n=6).

This beats the prior exact record `8400000/10897843` and crosses the rounded `0.771` level, but it does **not** reach `1`.

The mass is on `U=(0, 2, 4)`, `s=2`, `r=1`, clean branch row `j=1`, with `B=42/985`, `C=0`, `A=42/985`, `D=0`.

## Required calibration

- G12: `delta=1/4`, `B=2/57`, `B/delta=8/57`.
- Bundle maximizer: `delta=55319/1000000`, `B=42/985`, `B/delta=8400000/10897843`.

## Full best instance

`L`:

```text
[1  0  0]
[0  1  0]
[0  0  1]
[2/25  -3/50  49/50]
[1/25  197/200  -1/40]
[-6332623/370881409  383546655/741762818  1/2]
```

`B`:

```text
[1  0  0  0  0  0]
[-1/50  203/400  1/80  0  1/2  0]
[-796556062476619/14527204611353000  192624471172887/29054409222706000  8129358571267217/29054409222706000  7/10  0  993725924662467/14527204611353000]
```

`P=L B`:

```text
[1  0  0  0  0  0]
[-1/50  203/400  1/80  0  1/2  0]
[-796556062476619/14527204611353000  192624471172887/29054409222706000  8129358571267217/29054409222706000  7/10  0  993725924662467/14527204611353000]
[407126605321201/14823678174850000  -355068764837739/14823678174850000  4053561527002471/14823678174850000  343/500  -3/100  993725924662467/14823678174850000]
[2518529241379051/116217636890824000  72595601892680617/145272046113530000  193123061591109/36318011528382500  -7/400  197/400  -993725924662467/581088184454120000]
[-590855669597640985598471/10775740230179796072754000  715859935186159207498251/2693935057544949018188500  98572639986169931588254/673483764386237254547125  7/20  383546655/1483525636  993725924662467/29054409222706000]
```

## Argmin and branch certificate

- Argmin `U=(0, 1, 3)`: `m=49/50`, `Phi=4053561527002471/145272046113530000`, `phi=(0, 11/2450, 4053561527002471/145272046113530000)`, pivots `[2]`.
- Argmin `U=(0, 2, 4)`: `m=197/200`, `Phi=4053561527002471/145272046113530000`, `phi=(0, 679/24625, 4053561527002471/145272046113530000)`, pivots `[2]`.
- Clean branch row `1`: `a=(-8/197, 5/197, 200/197)`, `beta_s=72595601892680617/145272046113530000`, `E_s=11/197`, `self=203/400`, `Psi=1/200`, `Gamma=7/250`.

## CI-financed comparison

Literal CI import at the Gamma transverse pivot: `Phi_r(U)=679/24625`, `I=21/9850`, so `Phi_r+I=1463/49250`.
`B - (Phi_r+I) = 637/49250`. Using the import-reduction coefficients `alpha_B=13/200`, `alpha_A=0` gives reduced total `2989/98500` and margin `1211/98500`.
G12 budget terms at the same pivot: `G_class^-=0`, `S_-^mu=7453219829275413/114474372337461640000`, `SIGMA=72595601892680617/7263602305676500000`, total `28788997641448048423/2861859308436541000000`, with `B/budget=122028518735365200000/28788997641448048423`.

## Boundary and obstruction taxonomy

- Original compensated insert switch boundary: `y*=2679363/39161780`; the one-sided/boundary ratio is `6579179040/8535088237`.
- Variable inserted-row law: for `h=(-a,1/2+a,1/2)`, the active switch is `y=2679363/(49000*(22a+799))`; the row-loss balance is irrational `a=-5500573/293216 + sqrt(757785147162145)/1466080`, giving a limiting `B/delta` about `0.777640312383967`. Certified rational points approach it from either side.
- Duplicate n=7 and n=9 inserts do not amplify: the same ratio reappears and the active loss is carried by the cloned inserted rows.
- Extra B-carrier and rotated-bridge probes lost the clean Gamma branch (Psi/mixed or low-self branch), so they produced obstructions rather than records.

## Verdict on targets

- (i) Beat prior record / rounded `0.771`: YES.
- (ii) Reach or cross `1`: NO; best certified ratio is still below `0.778`.
- (iii) Cross literal CI-financed total: YES under the G12/CI convention `Phi_r(U)+I`; also yes for the import-reduction upper bound used here.

## Honest scope

Exact full chart enumeration was run for every emitted certified point. The search is still a finite, structured L3 probe: compensated-insert boundaries, rational approximants to one algebraic shape balance, duplicate n=7/n=9 inserts, a small extra-carrier set, and a small rotated-bridge set. It is not an exhaustive rank-3 idempotent search.

Machine-readable certified points are in `certified_points.json`; row summaries are in `certified_points.csv`.
