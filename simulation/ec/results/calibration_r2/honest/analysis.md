# EC year analysis

Units: 25 (pack, seed) pairs; arms: A, B, C, D; TOST margin ±0.03; bootstrap reps 2000; provenance: ⟦measured⟧

## Arm means

| arm | runs | e2_ps | e3_og | e1_imperm | e6_recall | e7_blind_spot | e8_return |
|---|---|---|---|---|---|---|---|
| A | 25 | -0.0012 | 0.0000 | 0.0312 | 0.9439 | 0.1175 | NA |
| B | 25 | -0.0012 | 0.0000 | 0.0312 | 0.9523 | 0.1395 | NA |
| C | 25 | -0.0012 | 0.0000 | 0.0312 | 0.9526 | 0.0000 | NA |
| D | 25 | -0.0012 | 0.0000 | 0.0313 | 0.9525 | 0.0000 | -2.3209 |

## TOST equivalence across arms (paired by pack and seed)

E2 and E3 are properties of the shared proposal stream; arms should be equivalent.

| metric | arms | n | mean diff | 90% CI | p lower | p upper | equivalent |
|---|---|---|---|---|---|---|---|
| e2_ps | A-B | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-D | 25 | 0.0000 | [-0.0001, 0.0001] | 0.0000 | 0.0000 | yes |
| e2_ps | B-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | B-D | 25 | 0.0000 | [-0.0001, 0.0001] | 0.0000 | 0.0000 | yes |
| e2_ps | C-D | 25 | 0.0000 | [-0.0001, 0.0001] | 0.0000 | 0.0000 | yes |
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
| E6 disclosure recall | A-B | 25 | 0.0084 | 0.0027 | 0.0138 |
| E6 disclosure recall | A-C | 25 | 0.0087 | 0.0037 | 0.0141 |
| E6 disclosure recall | A-D | 25 | 0.0086 | 0.0037 | 0.0137 |
| E6 disclosure recall | B-C | 25 | 0.0003 | -0.0049 | 0.0056 |
| E6 disclosure recall | B-D | 25 | 0.0002 | -0.0048 | 0.0057 |
| E6 disclosure recall | C-D | 25 | -0.0000 | -0.0001 | 0.0000 |
| E7 blind spot | A-B | 25 | 0.0219 | 0.0144 | 0.0294 |
| E7 blind spot | A-C | 25 | -0.1175 | -0.1259 | -0.1089 |
| E7 blind spot | A-D | 25 | -0.1175 | -0.1267 | -0.1094 |
| E7 blind spot | B-C | 25 | -0.1395 | -0.1459 | -0.1331 |
| E7 blind spot | B-D | 25 | -0.1395 | -0.1461 | -0.1331 |
| E7 blind spot | C-D | 25 | 0.0000 | 0.0000 | 0.0000 |
| E8 doctrine return (after - before) | A-B | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | C-D | 0 | NA | NA | NA |
