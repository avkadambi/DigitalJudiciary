# EC year analysis

Units: 25 (pack, seed) pairs; arms: A, B, C, D; TOST margin ±0.03; bootstrap reps 2000; provenance: ⟦measured⟧

## Arm means

| arm | runs | e2_ps | e3_og | e1_imperm | e6_recall | e7_blind_spot | e8_return |
|---|---|---|---|---|---|---|---|
| A | 25 | -0.0025 | -0.1549 | 0.1869 | 0.8359 | 0.3080 | NA |
| B | 25 | -0.0025 | -0.1549 | 0.1869 | 0.8222 | 0.3959 | NA |
| C | 25 | -0.0025 | -0.1549 | 0.1869 | 0.9031 | 0.0000 | NA |
| D | 25 | -0.0019 | -0.1549 | 0.1881 | 0.9036 | 0.0000 | -3.0260 |

## TOST equivalence across arms (paired by pack and seed)

E2 and E3 are properties of the shared proposal stream; arms should be equivalent.

| metric | arms | n | mean diff | 90% CI | p lower | p upper | equivalent |
|---|---|---|---|---|---|---|---|
| e2_ps | A-B | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-D | 25 | 0.0006 | [0.0000, 0.0013] | 0.0000 | 0.0000 | yes |
| e2_ps | B-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | B-D | 25 | 0.0006 | [0.0000, 0.0013] | 0.0000 | 0.0000 | yes |
| e2_ps | C-D | 25 | 0.0006 | [0.0000, 0.0013] | 0.0000 | 0.0000 | yes |
| e3_og | A-B | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | A-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | A-D | 25 | -0.0001 | [-0.0002, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | B-C | 25 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | B-D | 25 | -0.0001 | [-0.0002, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | C-D | 25 | -0.0001 | [-0.0002, 0.0000] | 0.0000 | 0.0000 | yes |

## Bootstrap intervals for arm differences (second minus first)

| metric | arms | n | mean diff | 2.5% | 97.5% |
|---|---|---|---|---|---|
| E1 proposal risk | A-B | 25 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | A-C | 25 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | A-D | 25 | 0.0013 | 0.0000 | 0.0030 |
| E1 proposal risk | B-C | 25 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | B-D | 25 | 0.0013 | 0.0000 | 0.0030 |
| E1 proposal risk | C-D | 25 | 0.0013 | 0.0000 | 0.0031 |
| E6 disclosure recall | A-B | 25 | -0.0136 | -0.0175 | -0.0096 |
| E6 disclosure recall | A-C | 25 | 0.0673 | 0.0588 | 0.0763 |
| E6 disclosure recall | A-D | 25 | 0.0677 | 0.0593 | 0.0760 |
| E6 disclosure recall | B-C | 25 | 0.0809 | 0.0723 | 0.0894 |
| E6 disclosure recall | B-D | 25 | 0.0813 | 0.0732 | 0.0894 |
| E6 disclosure recall | C-D | 25 | 0.0004 | -0.0006 | 0.0017 |
| E7 blind spot | A-B | 25 | 0.0879 | 0.0818 | 0.0942 |
| E7 blind spot | A-C | 25 | -0.3080 | -0.3155 | -0.3000 |
| E7 blind spot | A-D | 25 | -0.3080 | -0.3160 | -0.3001 |
| E7 blind spot | B-C | 25 | -0.3959 | -0.4046 | -0.3876 |
| E7 blind spot | B-D | 25 | -0.3959 | -0.4042 | -0.3878 |
| E7 blind spot | C-D | 25 | 0.0000 | 0.0000 | 0.0000 |
| E8 doctrine return (after - before) | A-B | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | C-D | 0 | NA | NA | NA |
