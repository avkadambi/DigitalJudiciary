# EC year analysis

Units: 25 (pack, seed) pairs; arms: A, B, C, D; TOST margin ±0.03; bootstrap reps 2000; provenance: ⟦measured⟧

## Arm means

| arm | runs | e2_ps | e3_og | e1_imperm | e6_recall | e7_blind_spot | e8_return |
|---|---|---|---|---|---|---|---|
| A | 25 | 0.2328 | 0.0000 | 0.1465 | 0.8305 | 0.4006 | NA |
| B | 25 | 0.2328 | 0.0000 | 0.1465 | 0.8270 | 0.3711 | NA |
| C | 25 | 0.2328 | 0.0000 | 0.1465 | 0.9033 | 0.0000 | NA |
| D | 25 | 0.2333 | 0.0000 | 0.1481 | 0.9038 | 0.0000 | -2.6528 |

## TOST equivalence across arms (paired by pack and seed)

E2 and E3 are properties of the shared proposal stream; arms should be equivalent.

| metric | arms | n | mean diff | 90% CI | p lower | p upper | equivalent |
|---|---|---|---|---|---|---|---|
| e2_ps | A-B | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-D | 25 | 0.0006 | [-0.0001, 0.0013] | 0.0000 | 0.0000 | yes |
| e2_ps | B-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | B-D | 25 | 0.0006 | [-0.0001, 0.0013] | 0.0000 | 0.0000 | yes |
| e2_ps | C-D | 25 | 0.0006 | [-0.0001, 0.0013] | 0.0000 | 0.0000 | yes |
| e3_og | A-B | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | A-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | A-D | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | B-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | B-D | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | C-D | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |

## Bootstrap intervals for arm differences (second minus first)

| metric | arms | n | mean diff | 2.5% | 97.5% |
|---|---|---|---|---|---|
| E1 proposal risk | A-B | 25 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | A-C | 25 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | A-D | 25 | 0.0016 | 0.0001 | 0.0034 |
| E1 proposal risk | B-C | 25 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | B-D | 25 | 0.0016 | 0.0001 | 0.0033 |
| E1 proposal risk | C-D | 25 | 0.0016 | 0.0001 | 0.0033 |
| E6 disclosure recall | A-B | 25 | -0.0035 | -0.0074 | 0.0001 |
| E6 disclosure recall | A-C | 25 | 0.0729 | 0.0630 | 0.0827 |
| E6 disclosure recall | A-D | 25 | 0.0733 | 0.0635 | 0.0827 |
| E6 disclosure recall | B-C | 25 | 0.0764 | 0.0665 | 0.0858 |
| E6 disclosure recall | B-D | 25 | 0.0768 | 0.0670 | 0.0865 |
| E6 disclosure recall | C-D | 25 | 0.0005 | -0.0002 | 0.0014 |
| E7 blind spot | A-B | 25 | -0.0295 | -0.0380 | -0.0210 |
| E7 blind spot | A-C | 25 | -0.4006 | -0.4132 | -0.3876 |
| E7 blind spot | A-D | 25 | -0.4006 | -0.4131 | -0.3871 |
| E7 blind spot | B-C | 25 | -0.3711 | -0.3794 | -0.3623 |
| E7 blind spot | B-D | 25 | -0.3711 | -0.3794 | -0.3628 |
| E7 blind spot | C-D | 25 | 0.0000 | 0.0000 | 0.0000 |
| E8 doctrine return (after - before) | A-B | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | C-D | 0 | NA | NA | NA |
