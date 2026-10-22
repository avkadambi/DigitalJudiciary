# EC year analysis

Units: 5 (pack, seed) pairs; arms: A, B, C, D; TOST margin ±0.03; bootstrap reps 2000; provenance: ⟦measured⟧

## Arm means

| arm | runs | e2_ps | e3_og | e1_imperm | e6_recall | e7_blind_spot | e8_return |
|---|---|---|---|---|---|---|---|
| A | 5 | -0.0065 | -0.0463 | 0.2295 | 0.9404 | 0.3352 | NA |
| B | 5 | -0.0065 | -0.0463 | 0.2295 | 0.9533 | 0.0737 | NA |
| C | 5 | -0.0065 | -0.0463 | 0.2295 | 0.8784 | 0.0000 | NA |
| D | 5 | -0.0099 | -0.0563 | 0.2316 | 0.8724 | 0.0000 | -9.9079 |

## TOST equivalence across arms (paired by pack and seed)

E2 and E3 are properties of the shared proposal stream; arms should be equivalent.

| metric | arms | n | mean diff | 90% CI | p lower | p upper | equivalent |
|---|---|---|---|---|---|---|---|
| e2_ps | A-B | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-C | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | A-D | 5 | -0.0035 | [-0.0236, 0.0166] | 0.0241 | 0.0119 | yes |
| e2_ps | B-C | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e2_ps | B-D | 5 | -0.0035 | [-0.0236, 0.0166] | 0.0241 | 0.0119 | yes |
| e2_ps | C-D | 5 | -0.0035 | [-0.0236, 0.0166] | 0.0241 | 0.0119 | yes |
| e3_og | A-B | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | A-C | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | A-D | 5 | -0.0100 | [-0.0313, 0.0113] | 0.0581 | 0.0081 | no |
| e3_og | B-C | 5 | 0.0000 | [0.0000, 0.0000] | 0.0000 | 0.0000 | yes |
| e3_og | B-D | 5 | -0.0100 | [-0.0313, 0.0113] | 0.0581 | 0.0081 | no |
| e3_og | C-D | 5 | -0.0100 | [-0.0313, 0.0113] | 0.0581 | 0.0081 | no |

## Bootstrap intervals for arm differences (second minus first)

| metric | arms | n | mean diff | 2.5% | 97.5% |
|---|---|---|---|---|---|
| E1 proposal risk | A-B | 5 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | A-C | 5 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | A-D | 5 | 0.0022 | 0.0000 | 0.0065 |
| E1 proposal risk | B-C | 5 | 0.0000 | 0.0000 | 0.0000 |
| E1 proposal risk | B-D | 5 | 0.0022 | 0.0000 | 0.0065 |
| E1 proposal risk | C-D | 5 | 0.0022 | 0.0000 | 0.0065 |
| E6 disclosure recall | A-B | 5 | 0.0128 | -0.0012 | 0.0242 |
| E6 disclosure recall | A-C | 5 | -0.0620 | -0.1501 | 0.0234 |
| E6 disclosure recall | A-D | 5 | -0.0680 | -0.1594 | 0.0234 |
| E6 disclosure recall | B-C | 5 | -0.0749 | -0.1663 | 0.0153 |
| E6 disclosure recall | B-D | 5 | -0.0808 | -0.1770 | 0.0153 |
| E6 disclosure recall | C-D | 5 | -0.0060 | -0.0179 | 0.0000 |
| E7 blind spot | A-B | 5 | -0.2615 | -0.3517 | -0.1749 |
| E7 blind spot | A-C | 5 | -0.3352 | -0.4160 | -0.2544 |
| E7 blind spot | A-D | 5 | -0.3352 | -0.4160 | -0.2544 |
| E7 blind spot | B-C | 5 | -0.0737 | -0.0990 | -0.0423 |
| E7 blind spot | B-D | 5 | -0.0737 | -0.1015 | -0.0423 |
| E7 blind spot | C-D | 5 | 0.0000 | 0.0000 | 0.0000 |
| E8 doctrine return (after - before) | A-B | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | A-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-C | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | B-D | 0 | NA | NA | NA |
| E8 doctrine return (after - before) | C-D | 0 | NA | NA | NA |
