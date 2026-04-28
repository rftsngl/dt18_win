# PES 2017 dt18 Data Mining Report

Bu rapor semantik mapping vermez; yalnızca binary veriden çıkarılan yapısal patternleri gösterir.
Meaning alanı bilinçli olarak unknown bırakılmıştır.

## Top focus sections by float ratio

| File | Section | Records | Fields | Float ratio | Dominant role |
|---|---|---:|---:|---:|---|
| constant_player.bin | contact.o | 1 | 20 | 0.8500 | gameplay_float_block_candidate |
| constant_team.bin | defenceCover.o | 1 | 36 | 0.8056 | gameplay_float_block_candidate |
| constant_team.bin | diagonalRun.o | 1 | 24 | 0.7917 | generic_numeric_block |
| constant_team.bin | defence.o | 1 | 36 | 0.7778 | gameplay_float_block_candidate |
| constant_player.bin | flypass.o | 2 | 52 | 0.7692 | gameplay_float_block_candidate |
| constant_player.bin | shoot.o | 10 | 68 | 0.7647 | curve_candidate |
| constant_team.bin | spaceRun.o | 1 | 84 | 0.7500 | gameplay_float_block_candidate |
| constant_player.bin | ballplayerShoot.o | 1 | 8 | 0.7500 | gameplay_float_block_candidate |
| constant_player.bin | throughpass.o | 1 | 120 | 0.7333 | gameplay_float_block_candidate |
| constant_team.bin | defenceMark.o | 1 | 80 | 0.6875 | generic_numeric_block |
| constant_player.bin | grounderpass.o | 3 | 48 | 0.6667 | gameplay_float_block_candidate |
| constant_player.bin | ballplayerSetplay.o | 2 | 12 | 0.6667 | generic_numeric_block |
| constant_match.bin | ball.o | 1 | 152 | 0.6513 | generic_numeric_block |
| constant_team.bin | support.o | 1 | 60 | 0.6167 | generic_numeric_block |
| constant_player.bin | ballplayerGk.o | 3 | 20 | 0.6000 | generic_numeric_block |
| constant_player.bin | ballplayerDribble.o | 7 | 64 | 0.4844 | generic_numeric_block |
| constant_player.bin | dribble.o | 1 | 20 | 0.4000 | generic_numeric_block |
| constant_player.bin | moveOnPass.o | 1 | 8 | 0.3750 | generic_numeric_block |
| constant_player.bin | passget.o | 1 | 52 | 0.3462 | generic_numeric_block |
| constant_match.bin | cpuLevel.o | 34 | 272 | 0.0551 | flag_block_candidate |

## Repeated sequences

| Count | Signature | Sections |
|---:|---|---|
| 12 | `1|1|1|1` | cpuLevel.o, selectorVision.o |
| 9 | `1|1|1` | cpuLevel.o, selectorVision.o |
| 4 | `1|1|1|1|1` | cpuLevel.o |
| 2 | `30|30|20|10|10` | cpuLevel.o |

## Similar records

| Distance | A | B |
|---:|---|---|
| 0.000000 | constant_match.bin / cpuLevel.o / rec 0 | constant_match.bin / cpuLevel.o / rec 2 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 0 | constant_match.bin / cpuLevel.o / rec 4 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 0 | constant_match.bin / cpuLevel.o / rec 7 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 0 | constant_match.bin / cpuLevel.o / rec 10 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 0 | constant_match.bin / cpuLevel.o / rec 11 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 0 | constant_match.bin / cpuLevel.o / rec 14 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 0 | constant_match.bin / cpuLevel.o / rec 16 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 0 | constant_match.bin / cpuLevel.o / rec 27 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 0 | constant_match.bin / cpuLevel.o / rec 32 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 0 | constant_match.bin / cpuLevel.o / rec 33 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 2 | constant_match.bin / cpuLevel.o / rec 4 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 2 | constant_match.bin / cpuLevel.o / rec 7 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 2 | constant_match.bin / cpuLevel.o / rec 10 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 2 | constant_match.bin / cpuLevel.o / rec 11 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 2 | constant_match.bin / cpuLevel.o / rec 14 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 2 | constant_match.bin / cpuLevel.o / rec 16 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 2 | constant_match.bin / cpuLevel.o / rec 27 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 2 | constant_match.bin / cpuLevel.o / rec 32 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 2 | constant_match.bin / cpuLevel.o / rec 33 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 3 | constant_match.bin / cpuLevel.o / rec 6 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 3 | constant_match.bin / cpuLevel.o / rec 24 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 3 | constant_match.bin / cpuLevel.o / rec 30 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 4 | constant_match.bin / cpuLevel.o / rec 7 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 4 | constant_match.bin / cpuLevel.o / rec 10 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 4 | constant_match.bin / cpuLevel.o / rec 11 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 4 | constant_match.bin / cpuLevel.o / rec 14 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 4 | constant_match.bin / cpuLevel.o / rec 16 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 4 | constant_match.bin / cpuLevel.o / rec 27 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 4 | constant_match.bin / cpuLevel.o / rec 32 |
| 0.000000 | constant_match.bin / cpuLevel.o / rec 4 | constant_match.bin / cpuLevel.o / rec 33 |