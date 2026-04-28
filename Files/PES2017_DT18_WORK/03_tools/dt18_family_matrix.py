import csv
from collections import defaultdict
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def resolve_export_dir() -> Path:
    candidates = [
        PROJECT_ROOT / "04_tests" / "bulk_export",
        PROJECT_ROOT / "04_tests" / "bulk_export-v2",
    ]

    for candidate in candidates:
        if (candidate / "all_fields.csv").exists():
            return candidate

    return candidates[0]


EXPORT_DIR = resolve_export_dir()
ANALYSIS_DIR = PROJECT_ROOT / "04_tests" / "analysis"

ALL_FIELDS = EXPORT_DIR / "all_fields.csv"

OUT_DIR = ANALYSIS_DIR / "family_matrices"
OUT_DIR.mkdir(parents=True, exist_ok=True)


TARGETS = [
    ("constant_player.bin", "shoot.o"),
    ("constant_player.bin", "grounderpass.o"),
    ("constant_player.bin", "throughpass.o"),
    ("constant_player.bin", "contact.o"),
    ("constant_team.bin", "defence.o"),
    ("constant_team.bin", "defenceMark.o"),
    ("constant_team.bin", "support.o"),
    ("constant_team.bin", "spaceRun.o"),
]


def read_csv(path):
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def safe_name(value):
    return value.replace(".bin", "").replace(".o", "").replace("/", "_")


def to_number(value):
    try:
        f = float(value)
        if abs(f - round(f)) < 1e-6:
            return str(int(round(f)))
        return f"{f:.6g}"
    except Exception:
        return value


def main():
    if not ALL_FIELDS.exists():
        raise FileNotFoundError(f"Bulunamadı: {ALL_FIELDS}")

    rows = read_csv(ALL_FIELDS)

    grouped = defaultdict(list)

    for row in rows:
        key = (row["file"], row["section"])

        if key not in TARGETS:
            continue

        grouped[key].append(row)

    for key, items in grouped.items():
        file_name, section = key

        record_map = defaultdict(list)

        for row in items:
            record_map[row["record"]].append(row)

        records = []

        max_field = 0

        for record, rec_rows in record_map.items():
            rec_rows.sort(key=lambda r: int(r["field"]))

            values = {
                int(r["field"]): to_number(r["preferred_value"])
                for r in rec_rows
            }

            max_field = max(max_field, max(values.keys()) if values else 0)

            records.append({
                "record": int(record),
                "record_offset": rec_rows[0]["record_file_offset_hex"],
                "record_length": rec_rows[0]["record_length"],
                "parse_mode": rec_rows[0]["parse_mode"],
                "values": values,
            })

        records.sort(key=lambda r: r["record"])

        out_path = OUT_DIR / f"{safe_name(file_name)}_{safe_name(section)}_matrix.csv"

        with out_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            header = [
                "file",
                "section",
                "record",
                "record_offset",
                "record_length",
                "parse_mode",
            ] + [f"F{i}" for i in range(max_field + 1)]

            writer.writerow(header)

            for rec in records:
                row = [
                    file_name,
                    section,
                    rec["record"],
                    rec["record_offset"],
                    rec["record_length"],
                    rec["parse_mode"],
                ]

                for i in range(max_field + 1):
                    row.append(rec["values"].get(i, ""))

                writer.writerow(row)

        print(f"Matrix yazıldı: {out_path}")

    print()
    print(f"Tüm matrisler: {OUT_DIR}")


if __name__ == "__main__":
    main()