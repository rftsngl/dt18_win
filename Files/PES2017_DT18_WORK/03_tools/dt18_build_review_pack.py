from __future__ import annotations

import csv
from collections import defaultdict
from collections.abc import Mapping, Sequence
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_DIR = PROJECT_ROOT / "04_tests" / "analysis"
ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

CANDIDATE_REPORT = ANALYSIS_DIR / "dt18_candidate_report.csv"
SECTION_SUMMARY = ANALYSIS_DIR / "dt18_section_summary_ranked.csv"

OUT_MD = ANALYSIS_DIR / "dt18_review_pack.md"
OUT_SHORTLIST = ANALYSIS_DIR / "dt18_shortlist_by_section.csv"


FOCUS_SECTIONS: list[tuple[str, str]] = [
    ("constant_player.bin", "shoot.o"),
    ("constant_player.bin", "grounderpass.o"),
    ("constant_player.bin", "throughpass.o"),
    ("constant_player.bin", "contact.o"),
    ("constant_player.bin", "dribble.o"),
    ("constant_team.bin", "defence.o"),
    ("constant_team.bin", "defenceCover.o"),
    ("constant_team.bin", "defenceMark.o"),
    ("constant_team.bin", "spaceRun.o"),
    ("constant_team.bin", "support.o"),
    ("constant_match.bin", "cpuLevel.o"),
    ("constant_match.bin", "ball.o"),
]


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


def as_float(value: str) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def summarize_values(rows: Sequence[Mapping[str, str]]) -> dict[str, object]:
    values: list[float] = []

    for row in rows:
        v = as_float(row["preferred_value"])
        if v is not None:
            values.append(v)

    if not values:
        return {
            "count": 0,
            "min": "",
            "max": "",
            "unique_preview": "",
        }

    unique = sorted(set(values))
    preview = ", ".join(str(v).rstrip("0").rstrip(".") for v in unique[:20])

    return {
        "count": len(values),
        "min": min(values),
        "max": max(values),
        "unique_preview": preview,
    }


def main() -> None:
    if not CANDIDATE_REPORT.exists():
        raise FileNotFoundError(f"Bulunamadı: {CANDIDATE_REPORT}")

    if not SECTION_SUMMARY.exists():
        raise FileNotFoundError(f"Bulunamadı: {SECTION_SUMMARY}")

    candidate_rows = read_csv(CANDIDATE_REPORT)
    section_rows = read_csv(SECTION_SUMMARY)

    section_summary_map: dict[tuple[str, str], dict[str, str]] = {
        (row["file"], row["section"]): row
        for row in section_rows
    }

    grouped: defaultdict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)

    for row in candidate_rows:
        key = (row["file"], row["section"])
        grouped[key].append(row)

    shortlist_rows: list[dict[str, object]] = []

    md_lines: list[str] = []
    md_lines.append("# PES 2017 dt18 Review Pack")
    md_lines.append("")
    md_lines.append("Bu rapor otomatik aday seçimi içindir. Field anlamları kesin değildir.")
    md_lines.append("Patch yapılmadan önce her field için anlam, hipotez, güven ve test notu girilmelidir.")
    md_lines.append("")

    for file_name, section_name in FOCUS_SECTIONS:
        key = (file_name, section_name)
        rows = grouped.get(key, [])
        summary = section_summary_map.get(key)

        md_lines.append(f"## {file_name} / {section_name}")
        md_lines.append("")

        if summary:
            md_lines.append(f"- Section offset: `{summary['section_file_offset_hex']}`")
            md_lines.append(f"- Section length: `{summary['section_length']}`")
            md_lines.append(f"- Parse mode: `{summary['parse_mode']}`")
            md_lines.append(f"- Record count: `{summary['record_count']}`")
            md_lines.append(f"- Field count: `{summary['field_count_total']}`")
            md_lines.append(f"- Float candidate count: `{summary['float_candidate_count']}`")
            md_lines.append(f"- Float ratio: `{summary['float_ratio']}`")
            md_lines.append(f"- Risk: `{summary['risk']}`")
            md_lines.append(f"- Hypothesis: {summary['hypothesis']}")
            md_lines.append("")

        if not rows:
            md_lines.append("Aday field bulunamadı.")
            md_lines.append("")
            continue

        rows = sorted(
            rows,
            key=lambda r: (
                int(r["candidate_score"]),
                int(r["record"]),
                int(r["field"]),
            ),
            reverse=True
        )

        value_summary = summarize_values(rows)

        md_lines.append("### Value summary")
        md_lines.append("")
        md_lines.append(f"- Candidate field count: `{len(rows)}`")
        md_lines.append(f"- Min value: `{value_summary['min']}`")
        md_lines.append(f"- Max value: `{value_summary['max']}`")
        md_lines.append(f"- Unique preview: `{value_summary['unique_preview']}`")
        md_lines.append("")

        md_lines.append("### Top candidate fields")
        md_lines.append("")
        md_lines.append("| Score | Record | Field | Offset | Value | Class | Meaning | Confidence |")
        md_lines.append("|---:|---:|---:|---|---:|---|---|---|")

        for row in rows[:20]:
            md_lines.append(
                f"| {row['candidate_score']} "
                f"| {row['record']} "
                f"| {row['field']} "
                f"| `{row['field_file_offset_hex']}` "
                f"| {row['preferred_value']} "
                f"| {row['value_class']} "
                f"| unknown "
                f"| none |"
            )

            shortlist_rows.append({
                "file": row["file"],
                "section": row["section"],
                "record": row["record"],
                "field": row["field"],
                "offset": row["field_file_offset_hex"],
                "value": row["preferred_value"],
                "value_class": row["value_class"],
                "candidate_score": row["candidate_score"],
                "meaning": "unknown",
                "hypothesis": row["hypothesis"],
                "confidence": "none",
                "test_status": "untested",
                "notes": "",
            })

        md_lines.append("")
        md_lines.append("### Manual mapping notes")
        md_lines.append("")
        md_lines.append("- Meaning: unknown")
        md_lines.append("- Confidence: none")
        md_lines.append("- Test status: untested")
        md_lines.append("- External evidence: not assigned")
        md_lines.append("")

    OUT_MD.write_text("\n".join(md_lines), encoding="utf-8")

    write_csv(
        OUT_SHORTLIST,
        shortlist_rows,
        [
            "file",
            "section",
            "record",
            "field",
            "offset",
            "value",
            "value_class",
            "candidate_score",
            "meaning",
            "hypothesis",
            "confidence",
            "test_status",
            "notes",
        ]
    )

    print("Review pack oluşturuldu.")
    print(f"Markdown : {OUT_MD}")
    print(f"Shortlist: {OUT_SHORTLIST}")
    print(f"Shortlist row count: {len(shortlist_rows)}")


if __name__ == "__main__":
    main()