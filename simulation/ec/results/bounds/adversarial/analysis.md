# EC year analysis

Units: 5 (pack, seed) pairs; arms: A, B, C, D; TOST margin ±0.03; bootstrap reps 2000; provenance: ⟦measured⟧

## Arm means

| arm | runs | e2_ps | e3_og | e1_imperm | e6_recall | e7_blind_spot | e8_return |
|---|---|---|---|---|---|---|---|
| A | 5 | -0.0230 | 0.0000 | 0.4202 | 0.0000 | 0.9033 | NA |
| B | 5 | -0.0230 | 0.0000 | 0.4202 | 0.0000 | 0.6986 | NA |
| C | 5 | -0.0230 | 0.0000 | 0.4202 | 0.0000 | 0.0000 | NA |
| D | 5 | -0.0227 | 0.0000 | 0.4217 | 0.0000 | 0.0000 | -4.1689 |

## TOST equivalence across arms (paired by pack and seed)

E2 and E3 are properties of the shared proposal stream; arms should be equivalent.

| metric | arms | n | mean diff | 90% CI | p lower | p upper | equivalent |
|---|---|---|---|---|---|---|---|
| e2_ps | A-B | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-C | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-D | 5 | 0.0004 | [-0.0025, 0.0033] | 0.0000 | 0.0000 | yes |
| e2_ps | B-C | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | B-D | 5 | 0.0004 | [-0.0025, 0.0033] | 0.0000 | 0.0000 | yes |
| e2_ps | C-D | 5 | 0.0004 | [-0.0025, 0.0033] | 0.0000 | 0.0000 | yes |
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
| E1 proposal risk | A-D | 5 | 0.0016 | 0.0001 | 0.0037 |
| E1 proposal risk | B-C | 5 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | B-D | 5 | 0.0016 | 0.0001 | 0.0037 |
| E1 proposal risk | C-D | 5 | 0.0016 | 0.0001 | 0.0037 |
| E6 disclosure recall | A-B | 5 | 0.0000 | 0.0000 | 0.0000 |
| E6 disclosure recall | A-C | 5 | 0.0000 | 0.0000 | 0.0000 |
| E6 disclosure recall | A-D | 5 | 0.0000 | 0.0000 | 0.0000 |
| E6 disclosure recall | B-C | 5 | 0.0000 | 0.0000 | 0.0000 |
| E6 disclosure recall | B-D | 5 | 0.0000 | 0.0000 | 0.0000 |
| E6 disclosure recall | C-D | 5 | 0.0000 | 0.0000 | 0.0000 |
| E7 blind spot | A-B | 5 | -0.2046 | -0.2208 | -0.1879 |
| E7 blind spot | A-C | 5 | -0.9033 | -0.9111 | -0.8953 |
| E7 blind spot | A-D | 5 | -0.9033 | -0.9113 | -0.8953 |
| E7 blind spot | B-C | 5 | -0.6986 | -0.7153 | -0.6827 |
| E7 blind spot | B-D | 5 | -0.6986 | -0.7153 | -0.6831 |
| E7 blind spot | C-D | 5 | 0.0000 | 0.0000 | 0.0000 |
| E8 doctrine return (after - before) | A-B | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | C-D | 0 | NA | NA | NA |
