# PES 2017 dt18 Structural Map v1

Bu dosya semantik mapping değildir. Yalnızca binary veriden çıkarılan yapısal record ailelerini gösterir.
`semantic_meaning` alanı bilinçli olarak `unknown` bırakılmıştır.

## constant_player.bin / contact.o

| Rec | Offset | Pattern | Structural label | Values |
|---:|---|---|---|---|
| 0 | `0x00000950` | repeated_value_group | `contact_single_physics_scalar_block` | `56, 0.45, 0.45, 0.5, 0.25, 0.15, 0.2, 0.6, 0.5, 0.8, 0.8, 35, 27, 0.15, 0.04, 0.06, 0.03` |
## constant_player.bin / grounderpass.o

| Rec | Offset | Pattern | Structural label | Values |
|---:|---|---|---|---|
| 0 | `0x00000C30` | small_mixed_scalar_group | `grounderpass_small_setup_block_A` | `7, 40, 12` |
| 1 | `0x00000C40` | repeated_value_group | `grounderpass_repeated_pair_block_B` | `15, 10, 15, 10` |
| 2 | `0x00000C50` | repeated_value_group | `grounderpass_long_mixed_parameter_block_C` | `30, 6, 1, 1.5, 0.6, 0.4, 13, 20, 40, 2.25, 1, 0.8, 0.8, 1, 0.3, 0.3, 38, 33, 28, 28, 30, 0.4, 1, 30, 2.25` |
## constant_player.bin / shoot.o

| Rec | Offset | Pattern | Structural label | Values |
|---:|---|---|---|---|
| 0 | `0x000015E0` | small_mixed_scalar_group | `shoot_scalar_header_or_setup_block` | `50, 5, 10, 6, 2, 1.2` |
| 1 | `0x00001600` | monotonic_increasing_or_flat | `shoot_curve_family_A` | `80, 80, 82, 84, 90, 98` |
| 2 | `0x00001620` | monotonic_increasing_or_flat | `shoot_curve_family_A` | `62, 64, 72, 79, 84, 90` |
| 3 | `0x00001640` | monotonic_increasing_or_flat | `shoot_curve_family_A` | `45, 45, 62, 74, 78, 82` |
| 4 | `0x00001660` | monotonic_decreasing_or_flat | `shoot_small_decreasing_block_A` | `26.5, 3, 0.5` |
| 5 | `0x00001670` | small_mixed_scalar_group | `shoot_scalar_block_B` | `28, 0.8, 80, 40` |
| 6 | `0x00001680` | monotonic_increasing_or_flat | `shoot_curve_family_B` | `95, 100, 105, 115, 120, 120` |
| 7 | `0x000016A0` | monotonic_increasing_or_flat | `shoot_curve_family_B` | `70, 70, 80, 95, 115, 115` |
| 8 | `0x000016C0` | monotonic_increasing_or_flat | `shoot_curve_family_B` | `56, 56, 68, 82, 84, 90` |
| 9 | `0x000016E0` | monotonic_decreasing_or_flat | `shoot_small_decreasing_block_B` | `28, 3, 0.5` |
## constant_player.bin / throughpass.o

| Rec | Offset | Pattern | Structural label | Values |
|---:|---|---|---|---|
| 0 | `0x000017C0` | repeated_value_group | `throughpass_long_mixed_parameter_block` | `0.8, 1.2, 15, 368, 10, 25, 35, 50, 1, 384, 4, 120, 120, 85, 85, 16, 3, 60, 0.417, 52, 30, 0.417, 35, 45, 30, 23, 40, 0.5, 40, 12, 3, 45, 1, 400, 416, 432, 448, 5, 3, 16843009, 36, 25, 6, 4, 35, 35, 80, 30, 6, 10, 15, 50, 25, 0.0417, 1, 7, 5, 2, 4, -24, 70, 2.2, 1.8, 40, 1.2, 96, 93, 464, 25, 30, 1, 50, 60, 2, 6, 16843009, 30, 8, 1, 20, 14, 1, 45, 110, 10, 0.2, 1, 0.1, 15, 30, 180, 5, 1.5, 5, 1.5, 3, 1.5, 3, 1.5, 65, 80, 180` |
## constant_team.bin / defence.o

| Rec | Offset | Pattern | Structural label | Values |
|---:|---|---|---|---|
| 0 | `0x00000630` | repeated_value_group | `defence_single_behavior_parameter_block` | `10, 10, 5, 3, 50, 35, 6, 20, 6, 12, 70, 20, 10, 1.5, 2, 2, 2, 4, 1, 1, 1, 1, 1, 10, 4, 5, 8, 10, 3, 10, 26, 5, 14, 30, 40, 80` |
## constant_team.bin / defenceMark.o

| Rec | Offset | Pattern | Structural label | Values |
|---:|---|---|---|---|
| 0 | `0x00000750` | repeated_value_group | `defenceMark_single_marking_parameter_block` | `22.5, 3, 20, 5, 3, 3, 50, 30, 40, 60, 90, 67.5, 0.7, 0.7, 15, 18, 1, 2, 10, 8, 2, 25, 20, 20, 15, 40, 0.1, 0.3, 22.5, 2, 2, 4, 2.5, 6, 2, 4, 2, 2, 2, 3, 2, 3, 4, 5, 7, 15, 20, 5, 90, 25, 2, 7, 4, 20, 29.15, 15, 22.5, 6, 5, 10, 13, 12, 18, 10, 135, 30, 2, 20, 4, 1, 10, 15, 18, 15, 18, 2.5, 5` |
## constant_team.bin / spaceRun.o

| Rec | Offset | Pattern | Structural label | Values |
|---:|---|---|---|---|
| 0 | `0x00000B30` | repeated_value_group | `spaceRun_single_offball_run_parameter_block` | `90, 110, 60, 90, 130, 130, 15, 15, 17, 21, 20, 25, 1, 100, 85, 30, 50, 2, 4, 12, 17, 25, 28, 16, 20, 25, 30, 90, 110, 1, 2, 5, 4, 6, 5, 7, 6, 27, 32, 10, 19, 23, 5, 10, 4, 8, 82, 100, 15, 2, 2, 18, 40, 20, 24, 40, 100, 95, 80, 90, 1, 1, 40, 13, 18, 15, 20, 40, 20, 30, 16777473, 4, 6, 25, 25, 17, 20, 10, 15, 1, 3, 2, 1` |
## constant_team.bin / support.o

| Rec | Offset | Pattern | Structural label | Values |
|---:|---|---|---|---|
| 0 | `0x00000D50` | repeated_value_group | `support_single_positioning_parameter_block` | `45, 22.5, 90, 22.5, 135, 20, 5, 5, 15, 5, 5, 15, 5, 5, 12, 1, 8, 2, 1, 20, 15, 5, 3, 4, 1, 10, 50, 6, 160, 6, 3, 3, 5, 8, 12, 16, 70, 1` |