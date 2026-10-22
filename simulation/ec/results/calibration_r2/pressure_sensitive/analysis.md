# EC year analysis

Units: 25 (pack, seed) pairs; arms: A, B, C, D; TOST margin ±0.03; bootstrap reps 2000; provenance: ⟦measured⟧

## Arm means

| arm | runs | e2_ps | e3_og | e1_imperm | e6_recall | e7_blind_spot | e8_return |
|---|---|---|---|---|---|---|---|
| A | 25 | 0.2313 | 0.0000 | 0.1421 | 0.8331 | 0.3903 | NA |
| B | 25 | 0.2313 | 0.0000 | 0.1421 | 0.8270 | 0.3774 | NA |
| C | 25 | 0.2313 | 0.0000 | 0.1421 | 0.9039 | 0.0000 | NA |
| D | 25 | 0.2319 | 0.0000 | 0.1436 | 0.9044 | 0.0000 | -2.6479 |

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
| E6 disclosure recall | A-B | 25 | -0.0061 | -0.0097 | -0.0027 |
| E6 disclosure recall | A-C | 25 | 0.0708 | 0.0617 | 0.0796 |
| E6 disclosure recall | A-D | 25 | 0.0713 | 0.0622 | 0.0798 |
| E6 disclosure recall | B-C | 25 | 0.0769 | 0.0679 | 0.0852 |
| E6 disclosure recall | B-D | 25 | 0.0774 | 0.0687 | 0.0859 |
| E6 disclosure recall | C-D | 25 | 0.0005 | -0.0002 | 0.0015 |
| E7 blind spot | A-B | 25 | -0.0129 | -0.0210 | -0.0046 |
| E7 blind spot | A-C | 25 | -0.3903 | -0.4023 | -0.3781 |
| E7 blind spot | A-D | 25 | -0.3903 | -0.4025 | -0.3774 |
| E7 blind spot | B-C | 25 | -0.3774 | -0.3864 | -0.3681 |
| E7 blind spot | B-D | 25 | -0.3774 | -0.3863 | -0.3684 |
| E7 blind spot | C-D | 25 | 0.0000 | 0.0000 | 0.0000 |
| E8 doctrine return (after - before) | A-B | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | C-D | 0 | NA | NA | NA |
