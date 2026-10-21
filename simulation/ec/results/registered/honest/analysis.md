# EC year analysis

Units: 25 (pack, seed) pairs; arms: A, B, C, D; TOST margin ±0.03; bootstrap reps 2000; provenance: ⟦measured⟧

## Arm means

| arm | runs | e2_ps | e3_og | e1_imperm | e6_recall | e7_blind_spot | e8_return |
|---|---|---|---|---|---|---|---|
| A | 25 | 0.0018 | 0.0000 | 0.0246 | 0.9489 | 0.9424 | NA |
| B | 25 | 0.0018 | 0.0000 | 0.0246 | 0.9514 | 0.7298 | NA |
| C | 25 | 0.0018 | 0.0000 | 0.0246 | 0.9483 | 0.0000 | NA |
| D | 25 | 0.0018 | 0.0000 | 0.0246 | 0.9483 | 0.0000 | -0.8897 |

## TOST equivalence across arms (paired by pack and seed)

E2 and E3 are properties of the shared proposal stream; arms should be equivalent.

| metric | arms | n | mean diff | 90% CI | p lower | p upper | equivalent |
|---|---|---|---|---|---|---|---|
| e2_ps | A-B | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-D | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | B-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | B-D | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | C-D | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
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
| E1 proposal risk | A-D | 25 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | B-C | 25 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | B-D | 25 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | C-D | 25 | 0.0000 | 0.0000 | 0.0000 |
| E6 disclosure recall | A-B | 25 | 0.0025 | 0.0009 | 0.0040 |
| E6 disclosure recall | A-C | 25 | -0.0007 | -0.0030 | 0.0019 |
| E6 disclosure recall | A-D | 25 | -0.0007 | -0.0032 | 0.0018 |
| E6 disclosure recall | B-C | 25 | -0.0031 | -0.0062 | 0.0000 |
| E6 disclosure recall | B-D | 25 | -0.0031 | -0.0063 | 0.0000 |
| E6 disclosure recall | C-D | 25 | 0.0000 | 0.0000 | 0.0000 |
| E7 blind spot | A-B | 25 | -0.2126 | -0.2256 | -0.1997 |
| E7 blind spot | A-C | 25 | -0.9424 | -0.9492 | -0.9345 |
| E7 blind spot | A-D | 25 | -0.9424 | -0.9490 | -0.9349 |
| E7 blind spot | B-C | 25 | -0.7298 | -0.7426 | -0.7155 |
| E7 blind spot | B-D | 25 | -0.7298 | -0.7436 | -0.7163 |
| E7 blind spot | C-D | 25 | 0.0000 | 0.0000 | 0.0000 |
| E8 doctrine return (after - before) | A-B | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | C-D | 0 | NA | NA | NA |
