# EC year analysis

Units: 5 (pack, seed) pairs; arms: A, B, C, D; TOST margin ±0.03; bootstrap reps 2000; provenance: ⟦measured⟧

## Arm means

| arm | runs | e2_ps | e3_og | e1_imperm | e6_recall | e7_blind_spot | e8_return |
|---|---|---|---|---|---|---|---|
| A | 5 | -0.0005 | 0.0000 | 0.0011 | 0.9912 | 0.0138 | NA |
| B | 5 | -0.0005 | 0.0000 | 0.0011 | 1.0000 | 0.0000 | NA |
| C | 5 | -0.0005 | 0.0000 | 0.0011 | 1.0000 | 0.0000 | NA |
| D | 5 | -0.0003 | 0.0000 | 0.0012 | 1.0000 | 0.0000 | -2.2450 |

## TOST equivalence across arms (paired by pack and seed)

E2 and E3 are properties of the shared proposal stream; arms should be equivalent.

| metric | arms | n | mean diff | 90% CI | p lower | p upper | equivalent |
|---|---|---|---|---|---|---|---|
| e2_ps | A-B | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-C | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-D | 5 | 0.0002 | [-0.0002, 0.0005] | 0.0000 | 0.0000 | yes |
| e2_ps | B-C | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | B-D | 5 | 0.0002 | [-0.0002, 0.0005] | 0.0000 | 0.0000 | yes |
| e2_ps | C-D | 5 | 0.0002 | [-0.0002, 0.0005] | 0.0000 | 0.0000 | yes |
| e3_og | A-B | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | A-C | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | A-D | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | B-C | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | B-D | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | C-D | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |

## Bootstrap intervals for arm differences (second minus first)

| metric | arms | n | mean diff | 2.5% | 97.5% |
|---|---|---|---|---|---|
| E1 proposal risk | A-B | 5 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | A-C | 5 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | A-D | 5 | 0.0001 | 0.0000 | 0.0002 |
| E1 proposal risk | B-C | 5 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | B-D | 5 | 0.0001 | 0.0000 | 0.0002 |
| E1 proposal risk | C-D | 5 | 0.0001 | 0.0000 | 0.0002 |
| E6 disclosure recall | A-B | 5 | 0.0088 | 0.0000 | 0.0208 |
| E6 disclosure recall | A-C | 5 | 0.0088 | 0.0000 | 0.0208 |
| E6 disclosure recall | A-D | 5 | 0.0088 | 0.0000 | 0.0208 |
| E6 disclosure recall | B-C | 5 | 0.0000 | 0.0000 | 0.0000 |
| E6 disclosure recall | B-D | 5 | 0.0000 | 0.0000 | 0.0000 |
| E6 disclosure recall | C-D | 5 | 0.0000 | 0.0000 | 0.0000 |
| E7 blind spot | A-B | 5 | -0.0138 | -0.0277 | 0.0000 |
| E7 blind spot | A-C | 5 | -0.0138 | -0.0290 | 0.0000 |
| E7 blind spot | A-D | 5 | -0.0138 | -0.0290 | 0.0000 |
| E7 blind spot | B-C | 5 | 0.0000 | 0.0000 | 0.0000 |
| E7 blind spot | B-D | 5 | 0.0000 | 0.0000 | 0.0000 |
| E7 blind spot | C-D | 5 | 0.0000 | 0.0000 | 0.0000 |
| E8 doctrine return (after - before) | A-B | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | C-D | 0 | NA | NA | NA |
