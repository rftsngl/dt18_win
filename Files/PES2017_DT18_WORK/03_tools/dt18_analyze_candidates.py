from __future__ import annotations

import csv
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import TypedDict, cast


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def resolve_export_dir() -> Path:
    candidates = [
        PROJECT_ROOT / "04_tests" / "bulk_export",
        PROJECT_ROOT / "04_tests" / "bulk_export-v2",
    ]

    for candidate in candidates:
        if (candidate / "section_index.csv").exists() and (candidate / "all_fields.csv").exists():
            return candidate

    return candidates[0]


EXPORT_DIR = resolve_export_dir()

SECTION_INDEX = EXPORT_DIR / "section_index.csv"
ALL_FIELDS = EXPORT_DIR / "all_fields.csv"

OUT_DIR = PROJECT_ROOT / "04_tests" / "analysis"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_SECTION_SUMMARY = OUT_DIR / "dt18_section_summary_ranked.csv"
OUT_CANDIDATES = OUT_DIR / "dt18_candidate_report.csv"
OUT_CATALOG = OUT_DIR / "dt18_field_catalog_seed.csv"


class SectionIndexRow(TypedDict):
    file: str
    section: str
    section_index: str
    section_file_offset_hex: str
    section_length: str
    parse_mode: str
    record_count: str
    field_count_total: str
    float_candidate_count: str
    csv_path: str


class FieldCsvRow(TypedDict):
    file: str
    section: str
    section_index: str
    parse_mode: str
    record: str
    record_length: str
    field: str
    section_file_offset_hex: str
    record_file_offset_hex: str
    field_file_offset_hex: str
    bytes_hex: str
    int32: str
    uint32: str
    float32: str
    preferred_type: str
    preferred_value: str


class SectionSummaryRow(TypedDict):
    file: str
    section: str
    section_index: int
    section_file_offset_hex: str
    section_length: int
    parse_mode: str
    record_count: int
    field_count_total: int
    float_candidate_count: int
    float_ratio: float
    section_priority: int
    risk: str
    hypothesis: str
    csv_path: str


class CatalogRow(TypedDict):
    file: str
    section: str
    section_index: int
    parse_mode: str
    record: int
    record_length: int
    field: int
    section_file_offset_hex: str
    record_file_offset_hex: str
    field_file_offset_hex: str
    bytes_hex: str
    int32: int
    uint32: int
    float32: float
    preferred_type: str
    preferred_value: str
    value_class: str
    candidate_score: int
    meaning: str
    hypothesis: str
    confidence: str
    source: str
    test_status: str
    risk: str
    notes: str


FOCUS_SECTIONS: dict[str, int] = {
    # Player/action behaviour
    "shoot.o": 100,
    "grounderpass.o": 95,
    "throughpass.o": 90,
    "flypass.o": 85,
    "dribble.o": 85,
    "contact.o": 85,
    "tackle.o": 80,
    "sliding.o": 75,
    "gk.o": 70,
    "freemove.o": 70,
    "trap.o": 70,
    "ballplayerShoot.o": 70,
    "ballplayerPass.o": 65,
    "ballplayerDribble.o": 65,

    # Team/AI behaviour
    "defence.o": 100,
    "defenceCover.o": 95,
    "defenceMark.o": 95,
    "spaceRun.o": 90,
    "support.o": 90,
    "diagonalRun.o": 85,
    "lineBreak.o": 85,
    "combination.o": 75,
    "basePosition.o": 70,

    # Match/AI
    "cpuLevel.o": 85,
    "ball.o": 75,
    "rating.o": 65,
    "teamEmotion.o": 60,
}


LOW_PRIORITY_KEYWORDS: list[str] = [
    "debug",
    "test",
    "screenshot",
    "guide",
    "teamid",
    "selector",
    "emotion",
]


MEDIUM_RISK_SECTIONS: set[str] = {
    "shoot.o",
    "grounderpass.o",
    "throughpass.o",
    "flypass.o",
    "dribble.o",
    "contact.o",
    "tackle.o",
    "sliding.o",
    "gk.o",
    "freemove.o",
    "trap.o",
    "ballplayerShoot.o",
    "ballplayerPass.o",
    "ballplayerDribble.o",
    "defence.o",
    "defenceCover.o",
    "defenceMark.o",
    "spaceRun.o",
    "support.o",
    "diagonalRun.o",
    "lineBreak.o",
    "combination.o",
    "ball.o",
    "rating.o",
    "teamEmotion.o",
}


HIGH_COMPLEX_SECTIONS: set[str] = {
    "cpuLevel.o",
    "basePosition.o",
    "playStyle.o",
    "reaction.o",
}


def to_float(value: str) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def is_probably_padding(row: Mapping[str, str]) -> bool:
    try:
        int32 = int(row["int32"])
        uint32 = int(row["uint32"])
        f32 = float(row["float32"])
    except (KeyError, TypeError, ValueError):
        return False

    return int32 == 0 and uint32 == 0 and abs(f32) == 0.0


def classify_value(row: Mapping[str, str]) -> str:
    preferred_type = row["preferred_type"]
    value = to_float(row["preferred_value"])

    if is_probably_padding(row):
        return "padding_or_zero"

    if preferred_type == "float32_candidate":
        if value is None:
            return "float_unknown"

        if 0.0 < abs(value) < 0.001:
            return "unlikely_float_noise"

        if 0.001 <= abs(value) < 1.0:
            return "small_float_ratio"

        if 1.0 <= abs(value) <= 5.0:
            return "float_multiplier"

        if 5.0 < abs(value) <= 30.0:
            return "float_low_gameplay_scale"

        if 30.0 < abs(value) <= 130.0:
            return "float_gameplay_scale"

        if 130.0 < abs(value) <= 300.0:
            return "float_high_gameplay_scale"

        return "float_outlier"

    try:
        int_val = int(row["int32"])
    except (KeyError, TypeError, ValueError):
        return "unknown"

    if int_val in (0, 1):
        return "flag_candidate"

    if 1 < abs(int_val) <= 10:
        return "small_int_candidate"

    if 10 < abs(int_val) <= 130:
        return "int_gameplay_scale"

    if 130 < abs(int_val) <= 1000:
        return "large_int_candidate"

    return "int_outlier"


def section_priority(section_name: str) -> int:
    if section_name in FOCUS_SECTIONS:
        return FOCUS_SECTIONS[section_name]

    lowered = section_name.lower()

    for keyword in LOW_PRIORITY_KEYWORDS:
        if keyword in lowered:
            return 5

    return 40


def candidate_score(row: Mapping[str, object]) -> int:
    section = str(row["section"])
    value_class = str(row["value_class"])
    preferred_type = str(row["preferred_type"])

    score = section_priority(section)

    if preferred_type == "float32_candidate":
        score += 20

    if value_class in {
        "float_multiplier",
        "float_low_gameplay_scale",
        "float_gameplay_scale",
        "float_high_gameplay_scale",
    }:
        score += 20

    if value_class in {
        "padding_or_zero",
        "unlikely_float_noise",
        "float_outlier",
        "int_outlier",
    }:
        score -= 40

    if value_class == "flag_candidate":
        score -= 10

    lowered = section.lower()
    for keyword in LOW_PRIORITY_KEYWORDS:
        if keyword in lowered:
            score -= 40

    return score


def hypothesis_for_section(section: str) -> str:
    table: dict[str, str] = {
        "ball.o": "Ball state/physics-related section; exact field meaning unknown.",
        "rating.o": "Player rating adjustment-related section; exact field meaning unknown.",
        "teamEmotion.o": "Team emotion/morale-related section; exact field meaning unknown.",
        "shoot.o": "Shot-related section; exact field meaning unknown.",
        "grounderpass.o": "Ground pass-related section; exact field meaning unknown.",
        "throughpass.o": "Through pass-related section; exact field meaning unknown.",
        "flypass.o": "Lofted pass/cross-related section; exact field meaning unknown.",
        "dribble.o": "Dribbling-related section; exact field meaning unknown.",
        "contact.o": "Physical contact/collision-related section; exact field meaning unknown.",
        "ballplayerShoot.o": "Player shoot-behaviour section; exact field meaning unknown.",
        "ballplayerPass.o": "Player pass-behaviour section; exact field meaning unknown.",
        "ballplayerDribble.o": "Player dribble-behaviour section; exact field meaning unknown.",
        "defence.o": "Team defence-related section; exact field meaning unknown.",
        "defenceCover.o": "Defensive cover-related section; exact field meaning unknown.",
        "defenceMark.o": "Marking-related section; exact field meaning unknown.",
        "spaceRun.o": "Off-ball run/space movement section; exact field meaning unknown.",
        "support.o": "Team support positioning section; exact field meaning unknown.",
        "cpuLevel.o": "CPU level/difficulty-related section; exact field meaning unknown.",
    }

    return table.get(section, "Unknown section meaning; needs mapping or test evidence.")


def risk_for_section(section: str) -> str:
    lowered = section.lower()

    if any(k in lowered for k in ["debug", "test", "screenshot", "guide"]):
        return "high_ignore"

    if section in MEDIUM_RISK_SECTIONS:
        return "medium_candidate"

    if section in HIGH_COMPLEX_SECTIONS:
        return "high_complex"

    return "unknown"


def read_csv_dict(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv_dict(
    path: Path,
    rows: Sequence[Mapping[str, object]],
    fieldnames: Sequence[str],
) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if not SECTION_INDEX.exists():
        raise FileNotFoundError(f"Bulunamadı: {SECTION_INDEX}")

    if not ALL_FIELDS.exists():
        raise FileNotFoundError(f"Bulunamadı: {ALL_FIELDS}")

    section_rows = cast(list[SectionIndexRow], read_csv_dict(SECTION_INDEX))
    field_rows = cast(list[FieldCsvRow], read_csv_dict(ALL_FIELDS))

    # 1) Section summary
    summary_rows: list[SectionSummaryRow] = []

    for row in section_rows:
        section = row["section"]
        field_count = int(row["field_count_total"])
        float_count = int(row["float_candidate_count"])
        float_ratio = float_count / field_count if field_count else 0.0

        priority = section_priority(section)

        summary_rows.append(
            {
                "file": row["file"],
                "section": section,
                "section_index": int(row["section_index"]),
                "section_file_offset_hex": row["section_file_offset_hex"],
                "section_length": int(row["section_length"]),
                "parse_mode": row["parse_mode"],
                "record_count": int(row["record_count"]),
                "field_count_total": field_count,
                "float_candidate_count": float_count,
                "float_ratio": round(float_ratio, 4),
                "section_priority": priority,
                "risk": risk_for_section(section),
                "hypothesis": hypothesis_for_section(section),
                "csv_path": row["csv_path"],
            }
        )

    summary_rows.sort(
        key=lambda row: (
            row["section_priority"],
            row["float_ratio"],
            row["float_candidate_count"],
        ),
        reverse=True,
    )

    write_csv_dict(
        OUT_SECTION_SUMMARY,
        summary_rows,
        [
            "file",
            "section",
            "section_index",
            "section_file_offset_hex",
            "section_length",
            "parse_mode",
            "record_count",
            "field_count_total",
            "float_candidate_count",
            "float_ratio",
            "section_priority",
            "risk",
            "hypothesis",
            "csv_path",
        ]
    )

    # 2) Candidate fields
    candidate_rows: list[CatalogRow] = []
    catalog_rows: list[CatalogRow] = []

    for row in field_rows:
        value_class = classify_value(row) # type: ignore
        candidate_context: dict[str, object] = dict(row)
        candidate_context["value_class"] = value_class

        score = candidate_score(candidate_context)

        section = row["section"]

        catalog_item: CatalogRow = {
            "file": row["file"],
            "section": section,
            "section_index": int(row["section_index"]),
            "parse_mode": row["parse_mode"],
            "record": int(row["record"]),
            "record_length": int(row["record_length"]),
            "field": int(row["field"]),
            "section_file_offset_hex": row["section_file_offset_hex"],
            "record_file_offset_hex": row["record_file_offset_hex"],
            "field_file_offset_hex": row["field_file_offset_hex"],
            "bytes_hex": row["bytes_hex"],
            "int32": int(row["int32"]),
            "uint32": int(row["uint32"]),
            "float32": float(row["float32"]),
            "preferred_type": row["preferred_type"],
            "preferred_value": row["preferred_value"],
            "value_class": value_class,
            "candidate_score": score,
            "meaning": "unknown",
            "hypothesis": hypothesis_for_section(section),
            "confidence": "none",
            "source": EXPORT_DIR.name,
            "test_status": "untested",
            "risk": risk_for_section(section),
            "notes": "",
        }

        catalog_rows.append(catalog_item)

        if score >= 90:
            candidate_rows.append(catalog_item)

    candidate_rows.sort(
        key=lambda row: (
            row["candidate_score"],
            row["file"],
            row["section"],
            row["record"],
            row["field"],
        ),
        reverse=True,
    )

    catalog_rows.sort(
        key=lambda row: (
            row["file"],
            row["section"],
            row["record"],
            row["field"],
        )
    )

    fieldnames = [
        "file",
        "section",
        "section_index",
        "parse_mode",
        "record",
        "record_length",
        "field",
        "section_file_offset_hex",
        "record_file_offset_hex",
        "field_file_offset_hex",
        "bytes_hex",
        "int32",
        "uint32",
        "float32",
        "preferred_type",
        "preferred_value",
        "value_class",
        "candidate_score",
        "meaning",
        "hypothesis",
        "confidence",
        "source",
        "test_status",
        "risk",
        "notes",
    ]

    write_csv_dict(OUT_CANDIDATES, candidate_rows, fieldnames)
    write_csv_dict(OUT_CATALOG, catalog_rows, fieldnames)

    print("Analiz tamamlandı.")
    print(f"Section summary : {OUT_SECTION_SUMMARY}")
    print(f"Candidate report: {OUT_CANDIDATES}")
    print(f"Field catalog   : {OUT_CATALOG}")
    print()
    print(f"Section count   : {len(summary_rows)}")
    print(f"Field count     : {len(catalog_rows)}")
    print(f"Candidate count : {len(candidate_rows)}")

    print()
    print("İlk 20 aday:")
    for item in candidate_rows[:20]:
        print(
            f"{item['candidate_score']:>3} | "
            f"{item['file']} | "
            f"{item['section']} | "
            f"rec={item['record']} | "
            f"field={item['field']} | "
            f"offset={item['field_file_offset_hex']} | "
            f"value={item['preferred_value']} | "
            f"{item['value_class']}"
        )


if __name__ == "__main__":
    main()