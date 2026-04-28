from __future__ import annotations

import csv
from collections.abc import Mapping
from pathlib import Path
from typing import TypedDict


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_DIR = PROJECT_ROOT / "04_tests" / "analysis"
ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

CATALOG = ANALYSIS_DIR / "dt18_field_catalog_seed.csv"
OUT_WORKBOOK = ANALYSIS_DIR / "dt18_mapping_workbook.csv"


FOCUS: dict[tuple[str, str], dict[str, object]] = {
    ("constant_player.bin", "shoot.o"): {
        "max_rows": 30,
        "section_note": "Shot-related section. External clue exists for shoot gauge, but field-level mapping is not confirmed.",
    },
    ("constant_player.bin", "grounderpass.o"): {
        "max_rows": 25,
        "section_note": "Ground pass-related section. No confirmed field-level mapping yet.",
    },
    ("constant_team.bin", "defence.o"): {
        "max_rows": 25,
        "section_note": "Team defence-related section. No confirmed field-level mapping yet.",
    },
}


class CatalogRow(TypedDict):
    file: str
    section: str
    record: str
    field: str
    field_file_offset_hex: str
    bytes_hex: str
    preferred_value: str
    preferred_type: str
    value_class: str
    candidate_score: str


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[Mapping[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def infer_hypothesis(row: Mapping[str, str]) -> str:
    section = row["section"]
    record = int(row["record"])
    field = int(row["field"])
    value = row["preferred_value"]

    if section == "shoot.o":
        if record == 6 and field in (4, 5) and value == "120":
            return "Possible normal shoot gauge mid/max; external clue exists, not confirmed locally."
        if record in (6, 7, 8):
            return "Possible shoot gauge/power curve group; exact field unknown."
        return "Shot-related parameter candidate; exact field unknown."

    if section == "grounderpass.o":
        return "Ground pass parameter candidate; exact field unknown."

    if section == "defence.o":
        return "Team defence parameter candidate; exact field unknown."

    return "Unknown."


def infer_source(row: Mapping[str, str]) -> str:
    section = row["section"]
    record = int(row["record"])
    field = int(row["field"])
    value = row["preferred_value"]

    if section == "shoot.o" and record == 6 and field in (4, 5) and value == "120":
        return "local_export + Evo-Web clue"

    return "local_export"


def main() -> None:
    if not CATALOG.exists():
        raise FileNotFoundError(f"Bulunamadı: {CATALOG}")

    rows = read_csv(CATALOG)

    grouped: dict[tuple[str, str], list[dict[str, str]]] = {}

    for row in rows:
        key = (row["file"], row["section"])

        if key not in FOCUS:
            continue

        # Sadece anlamlı float adaylarını al.
        if row["preferred_type"] != "float32_candidate":
            continue

        # Sıfır/padding/çok küçük noise alanları dışarıda bırak.
        if row["value_class"] in {"padding_or_zero", "unlikely_float_noise", "float_outlier", "int_outlier"}:
            continue

        grouped.setdefault(key, []).append(row)

    workbook_rows: list[dict[str, object]] = []

    for key, items in grouped.items():
        items.sort(
            key=lambda r: (
                int(r["candidate_score"]),
                int(r["record"]),
                int(r["field"]),
            ),
            reverse=True
        )

        max_rows = FOCUS[key]["max_rows"]
        section_note = FOCUS[key]["section_note"]

        for row in items[:max_rows]:
            workbook_rows.append({
                "file": row["file"],
                "section": row["section"],
                "record": row["record"],
                "field": row["field"],
                "offset": row["field_file_offset_hex"],
                "bytes_hex": row["bytes_hex"],
                "value": row["preferred_value"],
                "type": "float32",
                "value_class": row["value_class"],
                "meaning": "unknown",
                "hypothesis": infer_hypothesis(row),
                "confidence": "none",
                "source": infer_source(row),
                "test_status": "untested",
                "section_note": section_note,
                "notes": "",
            })

    fieldnames = [
        "file",
        "section",
        "record",
        "field",
        "offset",
        "bytes_hex",
        "value",
        "type",
        "value_class",
        "meaning",
        "hypothesis",
        "confidence",
        "source",
        "test_status",
        "section_note",
        "notes",
    ]

    write_csv(OUT_WORKBOOK, workbook_rows, fieldnames) # type: ignore

    print("Mapping workbook oluşturuldu.")
    print(f"Output: {OUT_WORKBOOK}")
    print(f"Rows: {len(workbook_rows)}")

    print()
    print("İlk 15 satır:")
    for item in workbook_rows[:15]:
        print(
            f"{item['section']} | rec={item['record']} | field={item['field']} | "
            f"offset={item['offset']} | value={item['value']} | "
            f"meaning={item['meaning']} | confidence={item['confidence']}"
        )


if __name__ == "__main__":
    main()