# shoot.o Family Comparison

Bu rapor semantik mapping vermez. Sadece `shoot.o` içindeki iki büyük curve ailesinin yapısal farklarını gösterir.

## Family A

| Record | Values |
|---:|---|
| 1 | `80, 80, 82, 84, 90, 98` |
| 2 | `62, 64, 72, 79, 84, 90` |
| 3 | `45, 45, 62, 74, 78, 82` |

## Family B

| Record | Values |
|---:|---|
| 6 | `95, 100, 105, 115, 120, 120` |
| 7 | `70, 70, 80, 95, 115, 115` |
| 8 | `56, 56, 68, 82, 84, 90` |

## A vs B paired comparison

| Pair | Field | A | B | Delta B-A | Ratio B/A |
|---|---:|---:|---:|---:|---:|
| rec 1 ↔ rec 6 | F0 | 80 | 95 | 15 | 1.1875 |
| rec 1 ↔ rec 6 | F1 | 80 | 100 | 20 | 1.25 |
| rec 1 ↔ rec 6 | F2 | 82 | 105 | 23 | 1.28049 |
| rec 1 ↔ rec 6 | F3 | 84 | 115 | 31 | 1.36905 |
| rec 1 ↔ rec 6 | F4 | 90 | 120 | 30 | 1.33333 |
| rec 1 ↔ rec 6 | F5 | 98 | 120 | 22 | 1.22449 |
| rec 2 ↔ rec 7 | F0 | 62 | 70 | 8 | 1.12903 |
| rec 2 ↔ rec 7 | F1 | 64 | 70 | 6 | 1.09375 |
| rec 2 ↔ rec 7 | F2 | 72 | 80 | 8 | 1.11111 |
| rec 2 ↔ rec 7 | F3 | 79 | 95 | 16 | 1.20253 |
| rec 2 ↔ rec 7 | F4 | 84 | 115 | 31 | 1.36905 |
| rec 2 ↔ rec 7 | F5 | 90 | 115 | 25 | 1.27778 |
| rec 3 ↔ rec 8 | F0 | 45 | 56 | 11 | 1.24444 |
| rec 3 ↔ rec 8 | F1 | 45 | 56 | 11 | 1.24444 |
| rec 3 ↔ rec 8 | F2 | 62 | 68 | 6 | 1.09677 |
| rec 3 ↔ rec 8 | F3 | 74 | 82 | 8 | 1.10811 |
| rec 3 ↔ rec 8 | F4 | 78 | 84 | 6 | 1.07692 |
| rec 3 ↔ rec 8 | F5 | 82 | 90 | 8 | 1.09756 |

## Interpretation

- `meaning` hâlâ unknown.
- Family A ve Family B benzer sütun sayısına sahip iki ayrı curve ailesi gibi duruyor.
- Family B genel olarak Family A’dan daha yüksek değerler içeriyor.
- Bu, Family B’nin daha güçlü/agresif/üst seviye bir şut davranış grubu olabileceğini düşündürür; fakat bu sadece yapısal hipotezdir.
- Patch yapılmadan önce test planı ve rollback sistemi hazırlanmalıdır.