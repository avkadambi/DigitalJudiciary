# EC year analysis

Units: 25 (pack, seed) pairs; arms: A, B, C, D; TOST margin ±0.03; bootstrap reps 2000; provenance: ⟦measured⟧

## Arm means

| arm | runs | e2_ps | e3_og | e1_imperm | e6_recall | e7_blind_spot | e8_return |
|---|---|---|---|---|---|---|---|
| A | 25 | 0.0080 | -0.1297 | 0.1515 | 0.8365 | 0.9359 | NA |
| B | 25 | 0.0080 | -0.1297 | 0.1515 | 0.8300 | 0.7296 | NA |
| C | 25 | 0.0080 | -0.1297 | 0.1515 | 0.9013 | 0.0000 | NA |
| D | 25 | 0.0077 | -0.1297 | 0.1516 | 0.9013 | 0.0000 | -1.9821 |

## TOST equivalence across arms (paired by pack and seed)

E2 and E3 are properties of the shared proposal stream; arms should be equivalent.

| metric | arms | n | mean diff | 90% CI | p lower | p upper | equivalent |
|---|---|---|---|---|---|---|---|
| e2_ps | A-B | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-D | 25 | -0.0002 | [-0.0005, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | B-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | B-D | 25 | -0.0002 | [-0.0005, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | C-D | 25 | -0.0002 | [-0.0005, 0.0000] | 0.0000 | 0.0000 | yes |
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
| E1 proposal risk | A-D | 25 | 0.0000 | 0.0000 | 0.0001 |
| E1 proposal risk | B-C | 25 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | B-D | 25 | 0.0000 | 0.0000 | 0.0001 |
| E1 proposal risk | C-D | 25 | 0.0000 | 0.0000 | 0.0001 |
| E6 disclosure recall | A-B | 25 | -0.0064 | -0.0101 | -0.0031 |
| E6 disclosure recall | A-C | 25 | 0.0648 | 0.0605 | 0.0694 |
| E6 disclosure recall | A-D | 25 | 0.0648 | 0.0601 | 0.0691 |
| E6 disclosure recall | B-C | 25 | 0.0713 | 0.0651 | 0.0772 |
| E6 disclosure recall | B-D | 25 | 0.0712 | 0.0649 | 0.0772 |
| E6 disclosure recall | C-D | 25 | -0.0000 | -0.0001 | 0.0000 |
| E7 blind spot | A-B | 25 | -0.2063 | -0.2125 | -0.2000 |
| E7 blind spot | A-C | 25 | -0.9359 | -0.9400 | -0.9317 |
| E7 blind spot | A-D | 25 | -0.9359 | -0.9399 | -0.9316 |
| E7 blind spot | B-C | 25 | -0.7296 | -0.7370 | -0.7219 |
| E7 blind spot | B-D | 25 | -0.7296 | -0.7369 | -0.7222 |
| E7 blind spot | C-D | 25 | 0.0000 | 0.0000 | 0.0000 |
| E8 doctrine return (after - before) | A-B | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | C-D | 0 | NA | NA | NA |
