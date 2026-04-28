# PES 2017 dt18 Focus Mining Report

Bu rapor yalnızca odak gameplay section’larındaki yapısal aileleri gösterir.
Semantik anlam hâlâ unknown durumdadır.

## Section summary

| Section | Record count | Families |
|---|---:|---|
| ball.o | 1 | large_repeated_gameplay_block |
| contact.o | 1 | mixed_numeric_group |
| defence.o | 1 | repeated_scalar_block |
| defenceCover.o | 1 | mixed_numeric_group |
| defenceMark.o | 1 | large_repeated_gameplay_block |
| dribble.o | 1 | large_repeated_gameplay_block |
| flypass.o | 2 | generic_curve, repeated_scalar_block |
| grounderpass.o | 3 | repeated_scalar_block, small_scalar_block |
| shoot.o | 10 | generic_curve, large_skill_or_power_curve, small_scalar_block |
| spaceRun.o | 1 | large_repeated_gameplay_block |
| support.o | 1 | large_repeated_gameplay_block |
| throughpass.o | 1 | large_repeated_gameplay_block |

## Curve / block families

### ball.o / large_repeated_gameplay_block

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 0 | `0x00000280` | repeated_value_group | `1, 1, 7, 12, 2, 256, 288, 0, 25, 10, 320, 7.5, 20, 5, 352, 0.07, 384, 0.03, 0.7, 0.7, 0.1, 0.1, 0, 6.6` |

### contact.o / mixed_numeric_group

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 0 | `0x00000950` | mixed_numeric_group | `0, 56, 0.45, 0.45, 0.5, 0.25, 0.15, 0.2, 0.6, 0.5, 0.8, 0.8, 35, 27, 0.15, 0.04, 0.06, 0.03, 0, 0` |

### defence.o / repeated_scalar_block

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 0 | `0x00000630` | repeated_value_group | `10, 10, 5, 3, 50, 35, 6, 20, 6, 12, 70, 20, 10, 1.5, 2, 2, 2, 4, 1, 1, 1, 1, 1, 10` |

### defenceCover.o / mixed_numeric_group

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 0 | `0x000006C0` | mixed_numeric_group | `20, 50, 5, 0, 0, 2, 0.3, 165, 15, 240, 300, 25, 6, 7.5, 30, 60, 120, 10, 7.5, 10, 4, 42, 55, 18` |

### defenceMark.o / large_repeated_gameplay_block

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 0 | `0x00000750` | repeated_value_group | `22.5, 3, 20, 5, 3, 3, 50, 30, 40, 60, 90, 67.5, 0.7, 0.7, 15, 18, 1, 2, 10, 8, 2, 25, 20, 20` |

### dribble.o / large_repeated_gameplay_block

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 0 | `0x000009A0` | repeated_value_group | `1, 45, 180, 180, 0, 1, 0, 50, 100, 48, 64, 0, 256, 0, 1, 0, 256, 0.8, 0, 0` |

### flypass.o / generic_curve

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 0 | `0x00000A20` | monotonic_decreasing_or_flat | `1, 1, 0.5, 0` |

### flypass.o / repeated_scalar_block

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 1 | `0x00000A30` | repeated_value_group | `1, 0.25, 0.125, 0, 50, 50, 0, 0, 4.5, 6, 2, 8, 1.2, 1.2, 1.5, 1.75, 60, 10, 0.3, 0, 1, 0.6, 0.6, 0` |

### grounderpass.o / repeated_scalar_block

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 1 | `0x00000C40` | repeated_value_group | `15, 10, 15, 10` |
| 2 | `0x00000C50` | repeated_value_group | `0, 0, 0, 30, 6, 1, 1.5, 0.6, 0.4, 13, 20, 0, 40, 2.25, 0, 0, 1, 0.8, 0.8, 0, 1, 0.3, 0.3, 0` |

### grounderpass.o / small_scalar_block

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 0 | `0x00000C30` | small_mixed_scalar_group | `7, 0, 40, 12` |

### shoot.o / generic_curve

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 4 | `0x00001660` | monotonic_decreasing_or_flat | `26.5, 3, 0.5, 0` |
| 9 | `0x000016E0` | monotonic_decreasing_or_flat | `28, 3, 0.5, 0` |

### shoot.o / large_skill_or_power_curve

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 1 | `0x00001600` | monotonic_increasing_or_flat | `80, 80, 82, 84, 90, 98, 0, 0` |
| 2 | `0x00001620` | monotonic_increasing_or_flat | `62, 64, 72, 79, 84, 90, 0, 0` |
| 3 | `0x00001640` | monotonic_increasing_or_flat | `45, 45, 62, 74, 78, 82, 0, 0` |
| 6 | `0x00001680` | monotonic_increasing_or_flat | `95, 100, 105, 115, 120, 120, 0, 0` |
| 7 | `0x000016A0` | monotonic_increasing_or_flat | `70, 70, 80, 95, 115, 115, 0, 0` |
| 8 | `0x000016C0` | monotonic_increasing_or_flat | `56, 56, 68, 82, 84, 90, 0, 0` |

### shoot.o / small_scalar_block

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 0 | `0x000015E0` | small_mixed_scalar_group | `50, 5, 10, 6, 2, 1.2, 0, 0` |
| 5 | `0x00001670` | small_mixed_scalar_group | `28, 0.8, 80, 40` |

### spaceRun.o / large_repeated_gameplay_block

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 0 | `0x00000B30` | repeated_value_group | `90, 110, 60, 90, 130, 130, 15, 15, 17, 21, 20, 25, 1, 100, 85, 30, 50, 2, 4, 12, 17, 25, 28, 16` |

### support.o / large_repeated_gameplay_block

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 0 | `0x00000D50` | repeated_value_group | `45, 22.5, 90, 22.5, 135, 0, 20, 5, 5, 15, 5, 5, 15, 5, 5, 12, 1, 8, 2, 1, 20, 15, 5, 3` |

### throughpass.o / large_repeated_gameplay_block

| Record | Offset | Pattern | Values |
|---:|---|---|---|
| 0 | `0x000017C0` | repeated_value_group | `0.8, 1.2, 15, 368, 0, 10, 25, 35, 50, 1, 384, 4, 120, 120, 85, 85, 16, 3, 60, 0.417, 52, 30, 0.417, 35` |

## Similar records inside focus sections

| Distance | Section | A | B |
|---:|---|---|---|
| 0.026786 | shoot.o | constant_player.bin rec 4 `26.5, 3, 0.5, 0` | constant_player.bin rec 9 `28, 3, 0.5, 0` |
| 0.043921 | shoot.o | constant_player.bin rec 2 `62, 64, 72, 79, 84, 90, 0, 0` | constant_player.bin rec 8 `56, 56, 68, 82, 84, 90, 0, 0` |
| 0.082589 | shoot.o | constant_player.bin rec 3 `45, 45, 62, 74, 78, 82, 0, 0` | constant_player.bin rec 8 `56, 56, 68, 82, 84, 90, 0, 0` |
| 0.102359 | shoot.o | constant_player.bin rec 1 `80, 80, 82, 84, 90, 98, 0, 0` | constant_player.bin rec 2 `62, 64, 72, 79, 84, 90, 0, 0` |
| 0.108216 | shoot.o | constant_player.bin rec 1 `80, 80, 82, 84, 90, 98, 0, 0` | constant_player.bin rec 7 `70, 70, 80, 95, 115, 115, 0, 0` |
| 0.116203 | shoot.o | constant_player.bin rec 2 `62, 64, 72, 79, 84, 90, 0, 0` | constant_player.bin rec 3 `45, 45, 62, 74, 78, 82, 0, 0` |
| 0.137471 | shoot.o | constant_player.bin rec 1 `80, 80, 82, 84, 90, 98, 0, 0` | constant_player.bin rec 8 `56, 56, 68, 82, 84, 90, 0, 0` |
| 0.137696 | shoot.o | constant_player.bin rec 2 `62, 64, 72, 79, 84, 90, 0, 0` | constant_player.bin rec 7 `70, 70, 80, 95, 115, 115, 0, 0` |
| 0.147153 | shoot.o | constant_player.bin rec 7 `70, 70, 80, 95, 115, 115, 0, 0` | constant_player.bin rec 8 `56, 56, 68, 82, 84, 90, 0, 0` |
| 0.150231 | shoot.o | constant_player.bin rec 6 `95, 100, 105, 115, 120, 120, 0, 0` | constant_player.bin rec 7 `70, 70, 80, 95, 115, 115, 0, 0` |
| 0.174279 | shoot.o | constant_player.bin rec 1 `80, 80, 82, 84, 90, 98, 0, 0` | constant_player.bin rec 6 `95, 100, 105, 115, 120, 120, 0, 0` |