# PES 2017 dt18 Review Pack

Bu rapor otomatik aday seçimi içindir. Field anlamları kesin değildir.
Patch yapılmadan önce her field için anlam, hipotez, güven ve test notu girilmelidir.

## constant_player.bin / shoot.o

- Section offset: `0x000015B0`
- Section length: `320`
- Parse mode: `record_table`
- Record count: `10`
- Field count: `68`
- Float candidate count: `52`
- Float ratio: `0.7647`
- Risk: `medium_candidate`
- Hypothesis: Shot-related section; exact field meaning unknown.

### Value summary

- Candidate field count: `52`
- Min value: `0.5`
- Max value: `120.0`
- Unique preview: `0.5, 0.8, 1.2, 2, 3, 5, 6, 10, 26.5, 28, 40, 45, 50, 56, 62, 64, 68, 70, 72, 74`

### Top candidate fields

| Score | Record | Field | Offset | Value | Class | Meaning | Confidence |
|---:|---:|---:|---|---:|---|---|---|
| 140 | 9 | 1 | `0x000016E4` | 3 | float_multiplier | unknown | none |
| 140 | 9 | 0 | `0x000016E0` | 28 | float_low_gameplay_scale | unknown | none |
| 140 | 8 | 5 | `0x000016D4` | 90 | float_gameplay_scale | unknown | none |
| 140 | 8 | 4 | `0x000016D0` | 84 | float_gameplay_scale | unknown | none |
| 140 | 8 | 3 | `0x000016CC` | 82 | float_gameplay_scale | unknown | none |
| 140 | 8 | 2 | `0x000016C8` | 68 | float_gameplay_scale | unknown | none |
| 140 | 8 | 1 | `0x000016C4` | 56 | float_gameplay_scale | unknown | none |
| 140 | 8 | 0 | `0x000016C0` | 56 | float_gameplay_scale | unknown | none |
| 140 | 7 | 5 | `0x000016B4` | 115 | float_gameplay_scale | unknown | none |
| 140 | 7 | 4 | `0x000016B0` | 115 | float_gameplay_scale | unknown | none |
| 140 | 7 | 3 | `0x000016AC` | 95 | float_gameplay_scale | unknown | none |
| 140 | 7 | 2 | `0x000016A8` | 80 | float_gameplay_scale | unknown | none |
| 140 | 7 | 1 | `0x000016A4` | 70 | float_gameplay_scale | unknown | none |
| 140 | 7 | 0 | `0x000016A0` | 70 | float_gameplay_scale | unknown | none |
| 140 | 6 | 5 | `0x00001694` | 120 | float_gameplay_scale | unknown | none |
| 140 | 6 | 4 | `0x00001690` | 120 | float_gameplay_scale | unknown | none |
| 140 | 6 | 3 | `0x0000168C` | 115 | float_gameplay_scale | unknown | none |
| 140 | 6 | 2 | `0x00001688` | 105 | float_gameplay_scale | unknown | none |
| 140 | 6 | 1 | `0x00001684` | 100 | float_gameplay_scale | unknown | none |
| 140 | 6 | 0 | `0x00001680` | 95 | float_gameplay_scale | unknown | none |

### Manual mapping notes

- Meaning: unknown
- Confidence: none
- Test status: untested
- External evidence: not assigned

## constant_player.bin / grounderpass.o

- Section offset: `0x00000BF0`
- Section length: `256`
- Parse mode: `record_table`
- Record count: `3`
- Field count: `48`
- Float candidate count: `32`
- Float ratio: `0.6667`
- Risk: `medium_candidate`
- Hypothesis: Ground pass-related section; exact field meaning unknown.

### Value summary

- Candidate field count: `32`
- Min value: `0.3`
- Max value: `40.0`
- Unique preview: `0.3, 0.4, 0.6, 0.8, 1, 1.5, 2.25, 6, 7, 10, 12, 13, 15, 20, 28, 30, 33, 38, 40`

### Top candidate fields

| Score | Record | Field | Offset | Value | Class | Meaning | Confidence |
|---:|---:|---:|---|---:|---|---|---|
| 135 | 2 | 36 | `0x00000CE0` | 2.25 | float_multiplier | unknown | none |
| 135 | 2 | 35 | `0x00000CDC` | 30 | float_low_gameplay_scale | unknown | none |
| 135 | 2 | 34 | `0x00000CD8` | 1 | float_multiplier | unknown | none |
| 135 | 2 | 28 | `0x00000CC0` | 30 | float_low_gameplay_scale | unknown | none |
| 135 | 2 | 27 | `0x00000CBC` | 28 | float_low_gameplay_scale | unknown | none |
| 135 | 2 | 26 | `0x00000CB8` | 28 | float_low_gameplay_scale | unknown | none |
| 135 | 2 | 25 | `0x00000CB4` | 33 | float_gameplay_scale | unknown | none |
| 135 | 2 | 24 | `0x00000CB0` | 38 | float_gameplay_scale | unknown | none |
| 135 | 2 | 20 | `0x00000CA0` | 1 | float_multiplier | unknown | none |
| 135 | 2 | 16 | `0x00000C90` | 1 | float_multiplier | unknown | none |
| 135 | 2 | 13 | `0x00000C84` | 2.25 | float_multiplier | unknown | none |
| 135 | 2 | 12 | `0x00000C80` | 40 | float_gameplay_scale | unknown | none |
| 135 | 2 | 10 | `0x00000C78` | 20 | float_low_gameplay_scale | unknown | none |
| 135 | 2 | 9 | `0x00000C74` | 13 | float_low_gameplay_scale | unknown | none |
| 135 | 2 | 6 | `0x00000C68` | 1.5 | float_multiplier | unknown | none |
| 135 | 2 | 5 | `0x00000C64` | 1 | float_multiplier | unknown | none |
| 135 | 2 | 4 | `0x00000C60` | 6 | float_low_gameplay_scale | unknown | none |
| 135 | 2 | 3 | `0x00000C5C` | 30 | float_low_gameplay_scale | unknown | none |
| 135 | 1 | 3 | `0x00000C4C` | 10 | float_low_gameplay_scale | unknown | none |
| 135 | 1 | 2 | `0x00000C48` | 15 | float_low_gameplay_scale | unknown | none |

### Manual mapping notes

- Meaning: unknown
- Confidence: none
- Test status: untested
- External evidence: not assigned

## constant_player.bin / throughpass.o

- Section offset: `0x000017C0`
- Section length: `480`
- Parse mode: `raw_4byte_fields`
- Record count: `1`
- Field count: `120`
- Float candidate count: `88`
- Float ratio: `0.7333`
- Risk: `medium_candidate`
- Hypothesis: Through pass-related section; exact field meaning unknown.

### Value summary

- Candidate field count: `98`
- Min value: `-24.0`
- Max value: `464.0`
- Unique preview: `-24, 0.0417, 0.1, 0.2, 0.417, 0.5, 0.8, 1, 1.2, 1.5, 1.8, 2, 2.2, 3, 4, 5, 6, 7, 8, 10`

### Top candidate fields

| Score | Record | Field | Offset | Value | Class | Meaning | Confidence |
|---:|---:|---:|---|---:|---|---|---|
| 130 | 0 | 119 | `0x0000199C` | 180 | float_high_gameplay_scale | unknown | none |
| 130 | 0 | 118 | `0x00001998` | 80 | float_gameplay_scale | unknown | none |
| 130 | 0 | 117 | `0x00001994` | 65 | float_gameplay_scale | unknown | none |
| 130 | 0 | 114 | `0x00001988` | 1.5 | float_multiplier | unknown | none |
| 130 | 0 | 113 | `0x00001984` | 3 | float_multiplier | unknown | none |
| 130 | 0 | 110 | `0x00001978` | 1.5 | float_multiplier | unknown | none |
| 130 | 0 | 109 | `0x00001974` | 3 | float_multiplier | unknown | none |
| 130 | 0 | 106 | `0x00001968` | 1.5 | float_multiplier | unknown | none |
| 130 | 0 | 105 | `0x00001964` | 5 | float_multiplier | unknown | none |
| 130 | 0 | 102 | `0x00001958` | 1.5 | float_multiplier | unknown | none |
| 130 | 0 | 101 | `0x00001954` | 5 | float_multiplier | unknown | none |
| 130 | 0 | 99 | `0x0000194C` | 180 | float_high_gameplay_scale | unknown | none |
| 130 | 0 | 98 | `0x00001948` | 30 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 97 | `0x00001944` | 15 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 93 | `0x00001934` | 1 | float_multiplier | unknown | none |
| 130 | 0 | 88 | `0x00001920` | 10 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 87 | `0x0000191C` | 110 | float_gameplay_scale | unknown | none |
| 130 | 0 | 86 | `0x00001918` | 45 | float_gameplay_scale | unknown | none |
| 130 | 0 | 84 | `0x00001910` | 14 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 83 | `0x0000190C` | 20 | float_low_gameplay_scale | unknown | none |

### Manual mapping notes

- Meaning: unknown
- Confidence: none
- Test status: untested
- External evidence: not assigned

## constant_player.bin / contact.o

- Section offset: `0x00000950`
- Section length: `80`
- Parse mode: `raw_4byte_fields`
- Record count: `1`
- Field count: `20`
- Float candidate count: `17`
- Float ratio: `0.85`
- Risk: `medium_candidate`
- Hypothesis: Physical contact/collision-related section; exact field meaning unknown.

### Value summary

- Candidate field count: `17`
- Min value: `0.03`
- Max value: `56.0`
- Unique preview: `0.03, 0.04, 0.06, 0.15, 0.2, 0.25, 0.45, 0.5, 0.6, 0.8, 27, 35, 56`

### Top candidate fields

| Score | Record | Field | Offset | Value | Class | Meaning | Confidence |
|---:|---:|---:|---|---:|---|---|---|
| 125 | 0 | 13 | `0x00000984` | 27 | float_low_gameplay_scale | unknown | none |
| 125 | 0 | 12 | `0x00000980` | 35 | float_gameplay_scale | unknown | none |
| 125 | 0 | 1 | `0x00000954` | 56 | float_gameplay_scale | unknown | none |
| 105 | 0 | 17 | `0x00000994` | 0.03 | small_float_ratio | unknown | none |
| 105 | 0 | 16 | `0x00000990` | 0.06 | small_float_ratio | unknown | none |
| 105 | 0 | 15 | `0x0000098C` | 0.04 | small_float_ratio | unknown | none |
| 105 | 0 | 14 | `0x00000988` | 0.15 | small_float_ratio | unknown | none |
| 105 | 0 | 11 | `0x0000097C` | 0.8 | small_float_ratio | unknown | none |
| 105 | 0 | 10 | `0x00000978` | 0.8 | small_float_ratio | unknown | none |
| 105 | 0 | 9 | `0x00000974` | 0.5 | small_float_ratio | unknown | none |
| 105 | 0 | 8 | `0x00000970` | 0.6 | small_float_ratio | unknown | none |
| 105 | 0 | 7 | `0x0000096C` | 0.2 | small_float_ratio | unknown | none |
| 105 | 0 | 6 | `0x00000968` | 0.15 | small_float_ratio | unknown | none |
| 105 | 0 | 5 | `0x00000964` | 0.25 | small_float_ratio | unknown | none |
| 105 | 0 | 4 | `0x00000960` | 0.5 | small_float_ratio | unknown | none |
| 105 | 0 | 3 | `0x0000095C` | 0.45 | small_float_ratio | unknown | none |
| 105 | 0 | 2 | `0x00000958` | 0.45 | small_float_ratio | unknown | none |

### Manual mapping notes

- Meaning: unknown
- Confidence: none
- Test status: untested
- External evidence: not assigned

## constant_player.bin / dribble.o

- Section offset: `0x000009A0`
- Section length: `80`
- Parse mode: `raw_4byte_fields`
- Record count: `1`
- Field count: `20`
- Float candidate count: `8`
- Float ratio: `0.4`
- Risk: `medium_candidate`
- Hypothesis: Dribbling-related section; exact field meaning unknown.

### Value summary

- Candidate field count: `8`
- Min value: `0.8`
- Max value: `180.0`
- Unique preview: `0.8, 1, 45, 50, 100, 180`

### Top candidate fields

| Score | Record | Field | Offset | Value | Class | Meaning | Confidence |
|---:|---:|---:|---|---:|---|---|---|
| 125 | 0 | 14 | `0x000009D8` | 1 | float_multiplier | unknown | none |
| 125 | 0 | 8 | `0x000009C0` | 100 | float_gameplay_scale | unknown | none |
| 125 | 0 | 7 | `0x000009BC` | 50 | float_gameplay_scale | unknown | none |
| 125 | 0 | 5 | `0x000009B4` | 1 | float_multiplier | unknown | none |
| 125 | 0 | 3 | `0x000009AC` | 180 | float_high_gameplay_scale | unknown | none |
| 125 | 0 | 2 | `0x000009A8` | 180 | float_high_gameplay_scale | unknown | none |
| 125 | 0 | 1 | `0x000009A4` | 45 | float_gameplay_scale | unknown | none |
| 105 | 0 | 17 | `0x000009E4` | 0.8 | small_float_ratio | unknown | none |

### Manual mapping notes

- Meaning: unknown
- Confidence: none
- Test status: untested
- External evidence: not assigned

## constant_team.bin / defence.o

- Section offset: `0x00000630`
- Section length: `144`
- Parse mode: `raw_4byte_fields`
- Record count: `1`
- Field count: `36`
- Float candidate count: `28`
- Float ratio: `0.7778`
- Risk: `medium_candidate`
- Hypothesis: Team defence-related section; exact field meaning unknown.

### Value summary

- Candidate field count: `36`
- Min value: `1.0`
- Max value: `80.0`
- Unique preview: `1, 1.5, 2, 3, 4, 5, 6, 8, 10, 12, 14, 20, 26, 30, 35, 40, 50, 70, 80`

### Top candidate fields

| Score | Record | Field | Offset | Value | Class | Meaning | Confidence |
|---:|---:|---:|---|---:|---|---|---|
| 140 | 0 | 35 | `0x000006BC` | 80 | float_gameplay_scale | unknown | none |
| 140 | 0 | 33 | `0x000006B4` | 30 | float_low_gameplay_scale | unknown | none |
| 140 | 0 | 32 | `0x000006B0` | 14 | float_low_gameplay_scale | unknown | none |
| 140 | 0 | 31 | `0x000006AC` | 5 | float_multiplier | unknown | none |
| 140 | 0 | 30 | `0x000006A8` | 26 | float_low_gameplay_scale | unknown | none |
| 140 | 0 | 28 | `0x000006A0` | 3 | float_multiplier | unknown | none |
| 140 | 0 | 27 | `0x0000069C` | 10 | float_low_gameplay_scale | unknown | none |
| 140 | 0 | 26 | `0x00000698` | 8 | float_low_gameplay_scale | unknown | none |
| 140 | 0 | 25 | `0x00000694` | 5 | float_multiplier | unknown | none |
| 140 | 0 | 24 | `0x00000690` | 4 | float_multiplier | unknown | none |
| 140 | 0 | 23 | `0x0000068C` | 10 | float_low_gameplay_scale | unknown | none |
| 140 | 0 | 17 | `0x00000674` | 4 | float_multiplier | unknown | none |
| 140 | 0 | 16 | `0x00000670` | 2 | float_multiplier | unknown | none |
| 140 | 0 | 15 | `0x0000066C` | 2 | float_multiplier | unknown | none |
| 140 | 0 | 14 | `0x00000668` | 2 | float_multiplier | unknown | none |
| 140 | 0 | 13 | `0x00000664` | 1.5 | float_multiplier | unknown | none |
| 140 | 0 | 12 | `0x00000660` | 10 | float_low_gameplay_scale | unknown | none |
| 140 | 0 | 10 | `0x00000658` | 70 | float_gameplay_scale | unknown | none |
| 140 | 0 | 9 | `0x00000654` | 12 | float_low_gameplay_scale | unknown | none |
| 140 | 0 | 8 | `0x00000650` | 6 | float_low_gameplay_scale | unknown | none |

### Manual mapping notes

- Meaning: unknown
- Confidence: none
- Test status: untested
- External evidence: not assigned

## constant_team.bin / defenceCover.o

- Section offset: `0x000006C0`
- Section length: `144`
- Parse mode: `raw_4byte_fields`
- Record count: `1`
- Field count: `36`
- Float candidate count: `29`
- Float ratio: `0.8056`
- Risk: `medium_candidate`
- Hypothesis: Defensive cover-related section; exact field meaning unknown.

### Value summary

- Candidate field count: `30`
- Min value: `0.3`
- Max value: `300.0`
- Unique preview: `0.3, 2, 4, 4.5, 5, 6, 7.5, 8, 9, 10, 15, 18, 20, 25, 30, 42, 50, 55, 60, 70`

### Top candidate fields

| Score | Record | Field | Offset | Value | Class | Meaning | Confidence |
|---:|---:|---:|---|---:|---|---|---|
| 135 | 0 | 32 | `0x00000740` | 5 | float_multiplier | unknown | none |
| 135 | 0 | 31 | `0x0000073C` | 70 | float_gameplay_scale | unknown | none |
| 135 | 0 | 30 | `0x00000738` | 8 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 27 | `0x0000072C` | 6 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 26 | `0x00000728` | 9 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 25 | `0x00000724` | 50 | float_gameplay_scale | unknown | none |
| 135 | 0 | 24 | `0x00000720` | 4.5 | float_multiplier | unknown | none |
| 135 | 0 | 23 | `0x0000071C` | 18 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 22 | `0x00000718` | 55 | float_gameplay_scale | unknown | none |
| 135 | 0 | 21 | `0x00000714` | 42 | float_gameplay_scale | unknown | none |
| 135 | 0 | 20 | `0x00000710` | 4 | float_multiplier | unknown | none |
| 135 | 0 | 19 | `0x0000070C` | 10 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 18 | `0x00000708` | 7.5 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 17 | `0x00000704` | 10 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 16 | `0x00000700` | 120 | float_gameplay_scale | unknown | none |
| 135 | 0 | 15 | `0x000006FC` | 60 | float_gameplay_scale | unknown | none |
| 135 | 0 | 14 | `0x000006F8` | 30 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 13 | `0x000006F4` | 7.5 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 12 | `0x000006F0` | 6 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 11 | `0x000006EC` | 25 | float_low_gameplay_scale | unknown | none |

### Manual mapping notes

- Meaning: unknown
- Confidence: none
- Test status: untested
- External evidence: not assigned

## constant_team.bin / defenceMark.o

- Section offset: `0x00000750`
- Section length: `320`
- Parse mode: `raw_4byte_fields`
- Record count: `1`
- Field count: `80`
- Float candidate count: `55`
- Float ratio: `0.6875`
- Risk: `medium_candidate`
- Hypothesis: Marking-related section; exact field meaning unknown.

### Value summary

- Candidate field count: `76`
- Min value: `0.1`
- Max value: `135.0`
- Unique preview: `0.1, 0.3, 0.7, 1, 2, 2.5, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15, 18, 20, 22.5, 25`

### Top candidate fields

| Score | Record | Field | Offset | Value | Class | Meaning | Confidence |
|---:|---:|---:|---|---:|---|---|---|
| 135 | 0 | 75 | `0x0000087C` | 2.5 | float_multiplier | unknown | none |
| 135 | 0 | 74 | `0x00000878` | 18 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 73 | `0x00000874` | 15 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 72 | `0x00000870` | 18 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 71 | `0x0000086C` | 15 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 68 | `0x00000860` | 4 | float_multiplier | unknown | none |
| 135 | 0 | 67 | `0x0000085C` | 20 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 66 | `0x00000858` | 2 | float_multiplier | unknown | none |
| 135 | 0 | 65 | `0x00000854` | 30 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 64 | `0x00000850` | 135 | float_high_gameplay_scale | unknown | none |
| 135 | 0 | 62 | `0x00000848` | 18 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 61 | `0x00000844` | 12 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 60 | `0x00000840` | 13 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 59 | `0x0000083C` | 10 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 56 | `0x00000830` | 22.5 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 55 | `0x0000082C` | 15 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 54 | `0x00000828` | 29.15 | float_low_gameplay_scale | unknown | none |
| 135 | 0 | 52 | `0x00000820` | 4 | float_multiplier | unknown | none |
| 135 | 0 | 50 | `0x00000818` | 2 | float_multiplier | unknown | none |
| 135 | 0 | 49 | `0x00000814` | 25 | float_low_gameplay_scale | unknown | none |

### Manual mapping notes

- Meaning: unknown
- Confidence: none
- Test status: untested
- External evidence: not assigned

## constant_team.bin / spaceRun.o

- Section offset: `0x00000B30`
- Section length: `336`
- Parse mode: `raw_4byte_fields`
- Record count: `1`
- Field count: `84`
- Float candidate count: `63`
- Float ratio: `0.75`
- Risk: `medium_candidate`
- Hypothesis: Off-ball run/space movement section; exact field meaning unknown.

### Value summary

- Candidate field count: `76`
- Min value: `2.0`
- Max value: `130.0`
- Unique preview: `2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25`

### Top candidate fields

| Score | Record | Field | Offset | Value | Class | Meaning | Confidence |
|---:|---:|---:|---|---:|---|---|---|
| 130 | 0 | 79 | `0x00000C6C` | 15 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 78 | `0x00000C68` | 10 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 77 | `0x00000C64` | 20 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 76 | `0x00000C60` | 17 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 75 | `0x00000C5C` | 25 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 74 | `0x00000C58` | 25 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 70 | `0x00000C48` | 30 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 69 | `0x00000C44` | 20 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 68 | `0x00000C40` | 40 | float_gameplay_scale | unknown | none |
| 130 | 0 | 67 | `0x00000C3C` | 20 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 66 | `0x00000C38` | 15 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 65 | `0x00000C34` | 18 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 64 | `0x00000C30` | 13 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 63 | `0x00000C2C` | 40 | float_gameplay_scale | unknown | none |
| 130 | 0 | 56 | `0x00000C10` | 40 | float_gameplay_scale | unknown | none |
| 130 | 0 | 55 | `0x00000C0C` | 24 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 54 | `0x00000C08` | 20 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 53 | `0x00000C04` | 40 | float_gameplay_scale | unknown | none |
| 130 | 0 | 52 | `0x00000C00` | 18 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 51 | `0x00000BFC` | 2 | float_multiplier | unknown | none |

### Manual mapping notes

- Meaning: unknown
- Confidence: none
- Test status: untested
- External evidence: not assigned

## constant_team.bin / support.o

- Section offset: `0x00000D50`
- Section length: `240`
- Parse mode: `raw_4byte_fields`
- Record count: `1`
- Field count: `60`
- Float candidate count: `37`
- Float ratio: `0.6167`
- Risk: `medium_candidate`
- Hypothesis: Team support positioning section; exact field meaning unknown.

### Value summary

- Candidate field count: `38`
- Min value: `1.0`
- Max value: `160.0`
- Unique preview: `1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 16, 20, 22.5, 45, 50, 70, 90, 135, 160`

### Top candidate fields

| Score | Record | Field | Offset | Value | Class | Meaning | Confidence |
|---:|---:|---:|---|---:|---|---|---|
| 130 | 0 | 38 | `0x00000DE8` | 1 | float_multiplier | unknown | none |
| 130 | 0 | 37 | `0x00000DE4` | 70 | float_gameplay_scale | unknown | none |
| 130 | 0 | 36 | `0x00000DE0` | 16 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 35 | `0x00000DDC` | 12 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 34 | `0x00000DD8` | 8 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 33 | `0x00000DD4` | 5 | float_multiplier | unknown | none |
| 130 | 0 | 32 | `0x00000DD0` | 3 | float_multiplier | unknown | none |
| 130 | 0 | 31 | `0x00000DCC` | 3 | float_multiplier | unknown | none |
| 130 | 0 | 30 | `0x00000DC8` | 6 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 28 | `0x00000DC0` | 6 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 27 | `0x00000DBC` | 50 | float_gameplay_scale | unknown | none |
| 130 | 0 | 26 | `0x00000DB8` | 10 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 25 | `0x00000DB4` | 1 | float_multiplier | unknown | none |
| 130 | 0 | 24 | `0x00000DB0` | 4 | float_multiplier | unknown | none |
| 130 | 0 | 23 | `0x00000DAC` | 3 | float_multiplier | unknown | none |
| 130 | 0 | 22 | `0x00000DA8` | 5 | float_multiplier | unknown | none |
| 130 | 0 | 21 | `0x00000DA4` | 15 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 20 | `0x00000DA0` | 20 | float_low_gameplay_scale | unknown | none |
| 130 | 0 | 19 | `0x00000D9C` | 1 | float_multiplier | unknown | none |
| 130 | 0 | 18 | `0x00000D98` | 2 | float_multiplier | unknown | none |

### Manual mapping notes

- Meaning: unknown
- Confidence: none
- Test status: untested
- External evidence: not assigned

## constant_match.bin / cpuLevel.o

- Section offset: `0x00000770`
- Section length: `1232`
- Parse mode: `record_table`
- Record count: `34`
- Field count: `272`
- Float candidate count: `15`
- Float ratio: `0.0551`
- Risk: `high_complex`
- Hypothesis: CPU level/difficulty-related section; exact field meaning unknown.

### Value summary

- Candidate field count: `15`
- Min value: `0.5`
- Max value: `100.0`
- Unique preview: `0.5, 1, 1.5, 2, 3, 4, 30, 50, 95, 100`

### Top candidate fields

| Score | Record | Field | Offset | Value | Class | Meaning | Confidence |
|---:|---:|---:|---|---:|---|---|---|
| 125 | 21 | 5 | `0x00000AB4` | 100 | float_gameplay_scale | unknown | none |
| 125 | 21 | 4 | `0x00000AB0` | 100 | float_gameplay_scale | unknown | none |
| 125 | 21 | 3 | `0x00000AAC` | 100 | float_gameplay_scale | unknown | none |
| 125 | 21 | 2 | `0x00000AA8` | 95 | float_gameplay_scale | unknown | none |
| 125 | 21 | 1 | `0x00000AA4` | 50 | float_gameplay_scale | unknown | none |
| 125 | 21 | 0 | `0x00000AA0` | 30 | float_low_gameplay_scale | unknown | none |
| 125 | 20 | 4 | `0x00000A90` | 1 | float_multiplier | unknown | none |
| 125 | 20 | 3 | `0x00000A8C` | 1.5 | float_multiplier | unknown | none |
| 125 | 20 | 2 | `0x00000A88` | 2 | float_multiplier | unknown | none |
| 125 | 20 | 1 | `0x00000A84` | 3 | float_multiplier | unknown | none |
| 125 | 20 | 0 | `0x00000A80` | 4 | float_multiplier | unknown | none |
| 125 | 15 | 2 | `0x000009E8` | 1 | float_multiplier | unknown | none |
| 125 | 15 | 1 | `0x000009E4` | 1.5 | float_multiplier | unknown | none |
| 125 | 15 | 0 | `0x000009E0` | 2 | float_multiplier | unknown | none |
| 105 | 15 | 3 | `0x000009EC` | 0.5 | small_float_ratio | unknown | none |

### Manual mapping notes

- Meaning: unknown
- Confidence: none
- Test status: untested
- External evidence: not assigned

## constant_match.bin / ball.o

- Section offset: `0x00000280`
- Section length: `608`
- Parse mode: `raw_4byte_fields`
- Record count: `1`
- Field count: `152`
- Float candidate count: `99`
- Float ratio: `0.6513`
- Risk: `medium_candidate`
- Hypothesis: Ball state/physics-related section; exact field meaning unknown.

### Value summary

- Candidate field count: `99`
- Min value: `-2.0`
- Max value: `105.0`
- Unique preview: `-2, 0.03, 0.035, 0.045, 0.055, 0.065, 0.07, 0.085, 0.1, 0.13, 0.16, 0.175, 0.2, 0.22, 0.24, 0.4, 0.5, 0.6, 0.62, 0.64`

### Top candidate fields

| Score | Record | Field | Offset | Value | Class | Meaning | Confidence |
|---:|---:|---:|---|---:|---|---|---|
| 115 | 0 | 148 | `0x000004D0` | 18 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 147 | `0x000004CC` | 9 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 146 | `0x000004C8` | 18 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 145 | `0x000004C4` | 18 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 144 | `0x000004C0` | 18 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 132 | `0x00000490` | 2 | float_multiplier | unknown | none |
| 115 | 0 | 131 | `0x0000048C` | 30 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 130 | `0x00000488` | 15 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 129 | `0x00000484` | 15 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 128 | `0x00000480` | 15 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 124 | `0x00000470` | 8 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 123 | `0x0000046C` | 70 | float_gameplay_scale | unknown | none |
| 115 | 0 | 122 | `0x00000468` | 25 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 121 | `0x00000464` | 25 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 120 | `0x00000460` | 25 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 76 | `0x000003B0` | 15 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 74 | `0x000003A8` | 15 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 73 | `0x000003A4` | 7.5 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 68 | `0x00000390` | 10 | float_low_gameplay_scale | unknown | none |
| 115 | 0 | 65 | `0x00000384` | 5 | float_multiplier | unknown | none |

### Manual mapping notes

- Meaning: unknown
- Confidence: none
- Test status: untested
- External evidence: not assigned
