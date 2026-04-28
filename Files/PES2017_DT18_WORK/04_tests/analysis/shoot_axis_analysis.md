# shoot.o Axis Analysis

Bu rapor semantik mapping vermez. Yalnızca `shoot.o` içindeki record/field eksenlerinin yapısal davranışını inceler.

## 1. Record içi yatay curve kontrolü

| Family | Record | Values | Non-decreasing |
|---|---:|---|---|
| A | 1 | `80, 80, 82, 84, 90, 98` | True |
| A | 2 | `62, 64, 72, 79, 84, 90` | True |
| A | 3 | `45, 45, 62, 74, 78, 82` | True |
| B | 6 | `95, 100, 105, 115, 120, 120` | True |
| B | 7 | `70, 70, 80, 95, 115, 115` | True |
| B | 8 | `56, 56, 68, 82, 84, 90` | True |

## 2. Family içi dikey eksen kontrolü

| Family | Field | Values | Non-increasing | Delta last-first | Ratio last/first |
|---|---:|---|---|---:|---:|
| A | F0 | `80, 62, 45` | True | -35 | 0.5625 |
| A | F1 | `80, 64, 45` | True | -35 | 0.5625 |
| A | F2 | `82, 72, 62` | True | -20 | 0.756098 |
| A | F3 | `84, 79, 74` | True | -10 | 0.880952 |
| A | F4 | `90, 84, 78` | True | -12 | 0.866667 |
| A | F5 | `98, 90, 82` | True | -16 | 0.836735 |
| B | F0 | `95, 70, 56` | True | -39 | 0.589474 |
| B | F1 | `100, 70, 56` | True | -44 | 0.56 |
| B | F2 | `105, 80, 68` | True | -37 | 0.647619 |
| B | F3 | `115, 95, 82` | True | -33 | 0.713043 |
| B | F4 | `120, 115, 84` | True | -36 | 0.7 |
| B | F5 | `120, 115, 90` | True | -30 | 0.75 |

## 3. Family B - Family A karşılaştırması

| Pair | Field | Values | B>A | Delta | Ratio |
|---|---:|---|---|---:|---:|
| 1<->6 | F0 | `A=80, B=95` | True | 15 | 1.1875 |
| 1<->6 | F1 | `A=80, B=100` | True | 20 | 1.25 |
| 1<->6 | F2 | `A=82, B=105` | True | 23 | 1.28049 |
| 1<->6 | F3 | `A=84, B=115` | True | 31 | 1.36905 |
| 1<->6 | F4 | `A=90, B=120` | True | 30 | 1.33333 |
| 1<->6 | F5 | `A=98, B=120` | True | 22 | 1.22449 |
| 2<->7 | F0 | `A=62, B=70` | True | 8 | 1.12903 |
| 2<->7 | F1 | `A=64, B=70` | True | 6 | 1.09375 |
| 2<->7 | F2 | `A=72, B=80` | True | 8 | 1.11111 |
| 2<->7 | F3 | `A=79, B=95` | True | 16 | 1.20253 |
| 2<->7 | F4 | `A=84, B=115` | True | 31 | 1.36905 |
| 2<->7 | F5 | `A=90, B=115` | True | 25 | 1.27778 |
| 3<->8 | F0 | `A=45, B=56` | True | 11 | 1.24444 |
| 3<->8 | F1 | `A=45, B=56` | True | 11 | 1.24444 |
| 3<->8 | F2 | `A=62, B=68` | True | 6 | 1.09677 |
| 3<->8 | F3 | `A=74, B=82` | True | 8 | 1.10811 |
| 3<->8 | F4 | `A=78, B=84` | True | 6 | 1.07692 |
| 3<->8 | F5 | `A=82, B=90` | True | 8 | 1.09756 |

## Structural interpretation

- F0-F5 ekseni record içinde genellikle artan curve gibi davranıyor.
- Aile içinde record ekseni genellikle yüksekten düşüğe gidiyor.
- Family B aynı pozisyonlarda Family A’dan sistematik olarak daha yüksek.
- Bu sonuçlar semantik anlam vermez; yalnızca `shoot.o` içinde iki paralel curve ailesi bulunduğunu güçlendirir.
- Sonraki adım, test planı oluşturmadan önce hangi eksenin test için daha güvenli olduğunu seçmektir.