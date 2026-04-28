from __future__ import annotations

import csv
from collections import defaultdict
from collections.abc import Mapping, Sequence
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_DIR = PROJECT_ROOT / "04_tests" / "analysis"
ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

RECORD_PATTERNS = ANALYSIS_DIR / "dm_record_patterns.csv"
SIMILAR_RECORDS = ANALYSIS_DIR / "dm_similar_records.csv"

OUT_CURVES = ANALYSIS_DIR / "dm_focus_curve_families.csv"
OUT_SIMILAR = ANALYSIS_DIR / "dm_focus_similarity.csv"
OUT_MD = ANALYSIS_DIR / "dt18_focus_mining_report.md"


FOCUS_SECTIONS = {
    "shoot.o",
    "grounderpass.o",
    "throughpass.o",
    "flypass.o",
    "dribble.o",
    "contact.o",
    "defence.o",
    "defenceCover.o",
    "defenceMark.o",
    "spaceRun.o",
    "support.o",
    "ball.o",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(
    path: Path,
    rows: Sequence[Mapping[str, object]],
    fieldnames: Sequence[str],
) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def to_float_list(values_preview: str) -> list[float]:
    values = []

    for part in values_preview.split(","):
        part = part.strip()
        if not part:
            continue

        try:
            values.append(float(part))
        except ValueError:
            pass

    return values


def nonzero_values(values: Sequence[float]) -> list[float]:
    return [v for v in values if abs(v) > 0.000001]


def curve_family_key(row: Mapping[str, str]) -> str:
    values = nonzero_values(to_float_list(row["values_preview"]))

    if not values:
        return "empty"

    count = len(values)
    max_v = max(values)

    if row["sequence_pattern"] in {
        "monotonic_increasing_or_flat",
        "monotonic_decreasing_or_flat",
    }:
        if count >= 5 and max_v >= 80:
            return "large_skill_or_power_curve"
        if count >= 4 and max_v <= 40:
            return "small_parameter_curve"
        return "generic_curve"

    if row["sequence_pattern"] == "repeated_value_group":
        if max_v >= 80:
            return "large_repeated_gameplay_block"
        return "repeated_scalar_block"

    if row["sequence_pattern"] == "small_mixed_scalar_group":
        return "small_scalar_block"

    return row["sequence_pattern"]


def main() -> None:
    if not RECORD_PATTERNS.exists():
        raise FileNotFoundError(f"Bulunamadı: {RECORD_PATTERNS}")

    if not SIMILAR_RECORDS.exists():
        raise FileNotFoundError(f"Bulunamadı: {SIMILAR_RECORDS}")

    records = read_csv(RECORD_PATTERNS)
    similar = read_csv(SIMILAR_RECORDS)

    focus_records = [
        r for r in records
        if r["section"] in FOCUS_SECTIONS
    ]

    curve_rows: list[dict[str, object]] = []

    for r in focus_records:
        values = nonzero_values(to_float_list(r["values_preview"]))

        if not values:
            continue

        family = curve_family_key(r)

        curve_rows.append({
            "file": r["file"],
            "section": r["section"],
            "record": r["record"],
            "record_offset": r["record_file_offset_hex"],
            "field_count": r["field_count"],
            "float_ratio": r["float_ratio"],
            "sequence_pattern": r["sequence_pattern"],
            "likely_structural_role": r["likely_structural_role"],
            "family": family,
            "nonzero_count": len(values),
            "min_value": min(values),
            "max_value": max(values),
            "values_preview": r["values_preview"],
            "semantic_meaning": "unknown",
            "confidence": "structural_only",
        })

    curve_rows.sort(
        key=lambda r: (
            str(r["section"]),
            str(r["family"]),
            int(str(r["record"])),
        )
    )

    # Similarity: cpuLevel/debug gibi gürültüyü at, sadece focus section’ları tut.
    similar_rows: list[dict[str, object]] = []

    for r in similar:
        a_section = r["a_section"]
        b_section = r["b_section"]

        if a_section not in FOCUS_SECTIONS:
            continue

        if b_section not in FOCUS_SECTIONS:
            continue

        # Aynı section içindeki yakınlık daha anlamlı.
        if a_section != b_section:
            continue

        similar_rows.append({
            "distance": r["distance"],
            "a_file": r["a_file"],
            "b_file": r["b_file"],
            "section": a_section,
            "a_record": r["a_record"],
            "a_offset": r["a_offset"],
            "a_values": r["a_values"],
            "b_record": r["b_record"],
            "b_offset": r["b_offset"],
            "b_values": r["b_values"],
        })

    similar_rows.sort(key=lambda r: float(r["distance"]))

    write_csv(
        OUT_CURVES,
        curve_rows,
        [
            "file",
            "section",
            "record",
            "record_offset",
            "field_count",
            "float_ratio",
            "sequence_pattern",
            "likely_structural_role",
            "family",
            "nonzero_count",
            "min_value",
            "max_value",
            "values_preview",
            "semantic_meaning",
            "confidence",
        ],
    )

    write_csv(
        OUT_SIMILAR,
        similar_rows,
        [
            "distance",
            "a_file",
            "b_file",
            "section",
            "a_record",
            "a_offset",
            "a_values",
            "b_record",
            "b_offset",
            "b_values",
        ],
    )

    grouped_by_section: defaultdict[str, list[dict[str, object]]] = defaultdict(list)
    grouped_by_family: defaultdict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)

    for r in curve_rows:
        grouped_by_section[str(r["section"])].append(r)
        grouped_by_family[(str(r["section"]), str(r["family"]))].append(r)

    lines = []
    lines.append("# PES 2017 dt18 Focus Mining Report")
    lines.append("")
    lines.append("Bu rapor yalnızca odak gameplay section’larındaki yapısal aileleri gösterir.")
    lines.append("Semantik anlam hâlâ unknown durumdadır.")
    lines.append("")

    lines.append("## Section summary")
    lines.append("")
    lines.append("| Section | Record count | Families |")
    lines.append("|---|---:|---|")

    for section, rows in sorted(grouped_by_section.items()):
        families = sorted(set(r["family"] for r in rows))
        lines.append(
            f"| {section} | {len(rows)} | {', '.join(families)} |"
        )

    lines.append("")
    lines.append("## Curve / block families")
    lines.append("")

    for (section, family), rows in sorted(grouped_by_family.items()):
        lines.append(f"### {section} / {family}")
        lines.append("")
        lines.append("| Record | Offset | Pattern | Values |")
        lines.append("|---:|---|---|---|")

        for r in rows:
            lines.append(
                f"| {r['record']} | `{r['record_offset']}` | "
                f"{r['sequence_pattern']} | `{r['values_preview']}` |"
            )

        lines.append("")

    lines.append("## Similar records inside focus sections")
    lines.append("")
    lines.append("| Distance | Section | A | B |")
    lines.append("|---:|---|---|---|")

    for r in similar_rows[:50]:
        lines.append(
            f"| {r['distance']} | {r['section']} | "
            f"{r['a_file']} rec {r['a_record']} `{r['a_values']}` | "
            f"{r['b_file']} rec {r['b_record']} `{r['b_values']}` |"
        )

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print("Focus mining tamamlandı.")
    print(f"Curve families : {OUT_CURVES}")
    print(f"Focus similar  : {OUT_SIMILAR}")
    print(f"Markdown       : {OUT_MD}")
    print()
    print(f"Focus record rows: {len(curve_rows)}")
    print(f"Focus similar rows: {len(similar_rows)}")

    print()
    print("Öne çıkan shoot.o aileleri:")
    for r in curve_rows:
        if r["section"] == "shoot.o":
            print(
                f"shoot.o rec={r['record']} | family={r['family']} | "
                f"pattern={r['sequence_pattern']} | values={r['values_preview']}"
            )


if __name__ == "__main__":
    main()