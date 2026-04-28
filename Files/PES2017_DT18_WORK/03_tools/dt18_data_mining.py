from __future__ import annotations

import csv
import math
from collections import Counter, defaultdict
from collections.abc import Mapping, Sequence
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def resolve_export_dir() -> Path:
    candidates = [
        PROJECT_ROOT / "04_tests" / "bulk_export",
        PROJECT_ROOT / "04_tests" / "bulk_export-v2",
    ]

    for candidate in candidates:
        if (candidate / "all_fields.csv").exists() and (candidate / "section_index.csv").exists():
            return candidate

    return candidates[0]


EXPORT_DIR = resolve_export_dir()
ANALYSIS_DIR = PROJECT_ROOT / "04_tests" / "analysis"
ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

ALL_FIELDS = EXPORT_DIR / "all_fields.csv"
SECTION_INDEX = EXPORT_DIR / "section_index.csv"

OUT_RECORD_PATTERNS = ANALYSIS_DIR / "dm_record_patterns.csv"
OUT_SECTION_PATTERNS = ANALYSIS_DIR / "dm_section_patterns.csv"
OUT_REPEATED_SEQUENCES = ANALYSIS_DIR / "dm_repeated_sequences.csv"
OUT_SIMILAR_RECORDS = ANALYSIS_DIR / "dm_similar_records.csv"
OUT_VALUE_FREQUENCIES = ANALYSIS_DIR / "dm_value_frequencies.csv"
OUT_MARKDOWN = ANALYSIS_DIR / "dt18_data_mining_report.md"


FOCUS_SECTION_KEYWORDS = [
    "shoot",
    "pass",
    "dribble",
    "contact",
    "defence",
    "mark",
    "cover",
    "support",
    "space",
    "run",
    "ball",
    "cpu",
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


def to_float(value: str) -> float | None:
    try:
        return float(value)
    except Exception:
        return None


def fmt_num(v: float | str | None) -> str:
    if isinstance(v, str):
        return v

    if v is None:
        return ""

    if abs(v - round(v)) < 1e-6:
        return str(int(round(v)))

    return f"{v:.6g}"


def is_zero(v: float) -> bool:
    return abs(v) < 1e-6


def classify_numeric_sequence(values: Sequence[float]) -> str:
    if not values:
        return "empty"

    non_zero = [v for v in values if not is_zero(v)]

    if not non_zero:
        return "all_zero"

    if all(v in (0.0, 1.0) for v in values):
        return "flag_group"

    if len(non_zero) == 1:
        return "single_scalar"

    increasing = all(non_zero[i] <= non_zero[i + 1] for i in range(len(non_zero) - 1))
    decreasing = all(non_zero[i] >= non_zero[i + 1] for i in range(len(non_zero) - 1))

    if increasing and len(set(non_zero)) > 1:
        return "monotonic_increasing_or_flat"

    if decreasing and len(set(non_zero)) > 1:
        return "monotonic_decreasing_or_flat"

    if len(set(non_zero)) == 1:
        return "constant_repeated_nonzero"

    # Alternating or grouped repeated check
    counts = Counter(non_zero)
    repeated_ratio = sum(c for c in counts.values() if c > 1) / len(non_zero)

    if repeated_ratio >= 0.5:
        return "repeated_value_group"

    if len(non_zero) <= 6:
        return "small_mixed_scalar_group"

    return "mixed_numeric_group"


def classify_record_role(
    section: str,
    values: Sequence[float],
    preferred_types: Sequence[str],
) -> str:
    section_l = section.lower()
    pattern = classify_numeric_sequence(values)

    float_ratio = preferred_types.count("float32_candidate") / len(preferred_types) if preferred_types else 0.0

    if pattern in {"monotonic_increasing_or_flat", "monotonic_decreasing_or_flat"}:
        if len([v for v in values if not is_zero(v)]) >= 4:
            return "curve_candidate"

    if pattern == "flag_group":
        return "flag_block_candidate"

    if float_ratio >= 0.7 and any(k in section_l for k in ["shoot", "pass", "defence", "mark", "support", "space", "ball", "contact", "dribble"]):
        return "gameplay_float_block_candidate"

    if float_ratio < 0.2 and pattern in {"mixed_numeric_group", "flag_group"}:
        return "int_or_flag_block_candidate"

    return "generic_numeric_block"


def vector_distance(a: Sequence[float], b: Sequence[float]) -> float | None:
    n = min(len(a), len(b))

    if n == 0:
        return None

    aa = a[:n]
    bb = b[:n]

    scale = max(
        max(abs(x) for x in aa) if aa else 1.0,
        max(abs(x) for x in bb) if bb else 1.0,
        1.0,
    )

    mse = sum((aa[i] - bb[i]) ** 2 for i in range(n)) / n
    return math.sqrt(mse) / scale


def signature(values: Sequence[float]) -> str:
    # 0 değerleri çoğu record sonunda padding olduğu için imzaya sınırlı dahil ediyoruz.
    cleaned = [v for v in values if not is_zero(v)]
    return "|".join(fmt_num(v) for v in cleaned)


def is_focus_section(section: str) -> bool:
    section_l = section.lower()
    return any(k in section_l for k in FOCUS_SECTION_KEYWORDS)


def main():
    if not ALL_FIELDS.exists():
        raise FileNotFoundError(f"Bulunamadı: {ALL_FIELDS}")

    if not SECTION_INDEX.exists():
        raise FileNotFoundError(f"Bulunamadı: {SECTION_INDEX}")

    field_rows = read_csv(ALL_FIELDS)
    section_rows = read_csv(SECTION_INDEX)

    grouped_records = defaultdict(list)

    for row in field_rows:
        key = (
            row["file"],
            row["section"],
            row["parse_mode"],
            row["record"],
            row["record_length"],
            row["record_file_offset_hex"],
        )
        grouped_records[key].append(row)

    record_reports = []

    for key, items in grouped_records.items():
        file_name, section, parse_mode, record, record_length, record_offset = key
        items.sort(key=lambda r: int(r["field"]))

        values = []
        preferred_types = []

        for item in items:
            v = to_float(item["preferred_value"])
            if v is None:
                continue

            values.append(v)
            preferred_types.append(item["preferred_type"])

        nonzero = [v for v in values if not is_zero(v)]
        float_count = preferred_types.count("float32_candidate")
        field_count = len(values)
        float_ratio = float_count / field_count if field_count else 0.0
        pattern = classify_numeric_sequence(values)
        role = classify_record_role(section, values, preferred_types)
        sig = signature(values)

        record_reports.append({
            "file": file_name,
            "section": section,
            "parse_mode": parse_mode,
            "record": record,
            "record_length": record_length,
            "record_file_offset_hex": record_offset,
            "field_count": field_count,
            "float_count": float_count,
            "float_ratio": f"{float_ratio:.4f}",
            "nonzero_count": len(nonzero),
            "min_value": fmt_num(min(values)) if values else "",
            "max_value": fmt_num(max(values)) if values else "",
            "unique_count": len(set(values)),
            "values_preview": ", ".join(fmt_num(v) for v in values[:24]),
            "nonzero_signature": sig,
            "sequence_pattern": pattern,
            "likely_structural_role": role,
            "semantic_meaning": "unknown",
            "confidence": "structural_only",
            "focus_section": is_focus_section(section),
        })

    # Section summaries
    section_group = defaultdict(list)
    for row in record_reports:
        section_group[(row["file"], row["section"])].append(row)

    section_reports = []
    section_index_map = {
        (r["file"], r["section"]): r
        for r in section_rows
    }

    for key, records in section_group.items():
        file_name, section = key
        idx = section_index_map.get(key, {})

        patterns = Counter(r["sequence_pattern"] for r in records)
        roles = Counter(r["likely_structural_role"] for r in records)

        field_total = sum(int(r["field_count"]) for r in records)
        float_total = sum(int(r["float_count"]) for r in records)
        float_ratio = float_total / field_total if field_total else 0.0

        section_reports.append({
            "file": file_name,
            "section": section,
            "section_offset": idx.get("section_file_offset_hex", ""),
            "section_length": idx.get("section_length", ""),
            "parse_mode": idx.get("parse_mode", ""),
            "record_count": len(records),
            "field_total": field_total,
            "float_total": float_total,
            "float_ratio": f"{float_ratio:.4f}",
            "dominant_pattern": patterns.most_common(1)[0][0] if patterns else "",
            "dominant_role": roles.most_common(1)[0][0] if roles else "",
            "pattern_counts": "; ".join(f"{k}:{v}" for k, v in patterns.most_common()),
            "role_counts": "; ".join(f"{k}:{v}" for k, v in roles.most_common()),
            "focus_section": is_focus_section(section),
        })

    # Repeated sequences
    sig_groups = defaultdict(list)
    for row in record_reports:
        sig = row["nonzero_signature"]
        if sig:
            sig_groups[sig].append(row)

    repeated_rows = []

    for sig, rows in sig_groups.items():
        if len(rows) < 2:
            continue

        repeated_rows.append({
            "signature": sig,
            "occurrence_count": len(rows),
            "locations": " || ".join(
                f"{r['file']}:{r['section']}:rec{r['record']}@{r['record_file_offset_hex']}"
                for r in rows[:20]
            ),
            "sections": ", ".join(sorted(set(r["section"] for r in rows))),
        })

    # Similar records, only within focus sections and manageable size
    focus_records = [r for r in record_reports if r["focus_section"]]

    # Need value vectors lookup
    vector_map = {}
    for key, items in grouped_records.items():
        file_name, section, parse_mode, record, record_length, record_offset = key
        values = []
        for item in sorted(items, key=lambda r: int(r["field"])):
            v = to_float(item["preferred_value"])
            if v is not None:
                values.append(v)
        vector_map[(file_name, section, record, record_offset)] = values

    similar_rows = []
    nonzero_counts = {
        key: len([x for x in values if not is_zero(x)])
        for key, values in vector_map.items()
    }

    for i in range(len(focus_records)):
        a = focus_records[i]
        key_a = (a["file"], a["section"], a["record"], a["record_file_offset_hex"])
        va = vector_map.get(key_a, [])

        for j in range(i + 1, len(focus_records)):
            b = focus_records[j]

            # Aynı file içindeki farklı section'ları karşılaştırmıyoruz.
            # Farklı file'larda ise yalnızca aynı section'ı eşleştiriyoruz.
            if a["file"] == b["file"] and a["section"] != b["section"]:
                continue
            if a["file"] != b["file"] and a["section"] != b["section"]:
                continue

            key_b = (b["file"], b["section"], b["record"], b["record_file_offset_hex"])
            vb = vector_map.get(key_b, [])

            if nonzero_counts.get(key_a, 0) < 3:
                continue
            if nonzero_counts.get(key_b, 0) < 3:
                continue

            d = vector_distance(va, vb)
            if d is None:
                continue

            if d <= 0.20:
                similar_rows.append({
                    "distance": f"{d:.6f}",
                    "a_file": a["file"],
                    "a_section": a["section"],
                    "a_record": a["record"],
                    "a_offset": a["record_file_offset_hex"],
                    "a_values": a["values_preview"],
                    "b_file": b["file"],
                    "b_section": b["section"],
                    "b_record": b["record"],
                    "b_offset": b["record_file_offset_hex"],
                    "b_values": b["values_preview"],
                })

    # Value frequencies
    value_counter = Counter()
    value_locations = defaultdict(list)

    for row in field_rows:
        val = row["preferred_value"]
        try:
            fval = float(val)
            val_norm = fmt_num(fval)
        except Exception:
            val_norm = val

        if val_norm in {"0", "1"}:
            continue

        value_counter[val_norm] += 1

        if len(value_locations[val_norm]) < 12:
            value_locations[val_norm].append(
                f"{row['file']}:{row['section']}:rec{row['record']}:field{row['field']}@{row['field_file_offset_hex']}"
            )

    freq_rows = []
    for value, count in value_counter.most_common(200):
        freq_rows.append({
            "value": value,
            "count": count,
            "sample_locations": " || ".join(value_locations[value]),
        })

    # Sort outputs
    record_reports.sort(key=lambda r: (r["file"], r["section"], int(r["record"])))
    section_reports.sort(
        key=lambda r: (
            bool(r["focus_section"]),
            float(r["float_ratio"]),
            int(r["field_total"]),
        ),
        reverse=True,
    )
    repeated_rows.sort(key=lambda r: int(r["occurrence_count"]), reverse=True)
    similar_rows.sort(key=lambda r: float(r["distance"]))

    write_csv(OUT_RECORD_PATTERNS, record_reports, [
        "file",
        "section",
        "parse_mode",
        "record",
        "record_length",
        "record_file_offset_hex",
        "field_count",
        "float_count",
        "float_ratio",
        "nonzero_count",
        "min_value",
        "max_value",
        "unique_count",
        "values_preview",
        "nonzero_signature",
        "sequence_pattern",
        "likely_structural_role",
        "semantic_meaning",
        "confidence",
        "focus_section",
    ])

    write_csv(OUT_SECTION_PATTERNS, section_reports, [
        "file",
        "section",
        "section_offset",
        "section_length",
        "parse_mode",
        "record_count",
        "field_total",
        "float_total",
        "float_ratio",
        "dominant_pattern",
        "dominant_role",
        "pattern_counts",
        "role_counts",
        "focus_section",
    ])

    write_csv(OUT_REPEATED_SEQUENCES, repeated_rows, [
        "signature",
        "occurrence_count",
        "locations",
        "sections",
    ])

    write_csv(OUT_SIMILAR_RECORDS, similar_rows, [
        "distance",
        "a_file",
        "a_section",
        "a_record",
        "a_offset",
        "a_values",
        "b_file",
        "b_section",
        "b_record",
        "b_offset",
        "b_values",
    ])

    write_csv(OUT_VALUE_FREQUENCIES, freq_rows, [
        "value",
        "count",
        "sample_locations",
    ])

    # Markdown report
    lines = []
    lines.append("# PES 2017 dt18 Data Mining Report")
    lines.append("")
    lines.append("Bu rapor semantik mapping vermez; yalnızca binary veriden çıkarılan yapısal patternleri gösterir.")
    lines.append("Meaning alanı bilinçli olarak unknown bırakılmıştır.")
    lines.append("")
    lines.append("## Top focus sections by float ratio")
    lines.append("")
    lines.append("| File | Section | Records | Fields | Float ratio | Dominant role |")
    lines.append("|---|---|---:|---:|---:|---|")

    for row in section_reports[:20]:
        lines.append(
            f"| {row['file']} | {row['section']} | {row['record_count']} | "
            f"{row['field_total']} | {row['float_ratio']} | {row['dominant_role']} |"
        )

    lines.append("")
    lines.append("## Repeated sequences")
    lines.append("")
    lines.append("| Count | Signature | Sections |")
    lines.append("|---:|---|---|")

    for row in repeated_rows[:20]:
        lines.append(
            f"| {row['occurrence_count']} | `{row['signature']}` | {row['sections']} |"
        )

    lines.append("")
    lines.append("## Similar records")
    lines.append("")
    lines.append("| Distance | A | B |")
    lines.append("|---:|---|---|")

    for row in similar_rows[:30]:
        lines.append(
            f"| {row['distance']} | "
            f"{row['a_file']} / {row['a_section']} / rec {row['a_record']} | "
            f"{row['b_file']} / {row['b_section']} / rec {row['b_record']} |"
        )

    OUT_MARKDOWN.write_text("\n".join(lines), encoding="utf-8")

    print("Data mining tamamlandı.")
    print(f"Record patterns    : {OUT_RECORD_PATTERNS}")
    print(f"Section patterns   : {OUT_SECTION_PATTERNS}")
    print(f"Repeated sequences : {OUT_REPEATED_SEQUENCES}")
    print(f"Similar records    : {OUT_SIMILAR_RECORDS}")
    print(f"Value frequencies  : {OUT_VALUE_FREQUENCIES}")
    print(f"Markdown report    : {OUT_MARKDOWN}")
    print()
    print(f"Record pattern rows: {len(record_reports)}")
    print(f"Section rows       : {len(section_reports)}")
    print(f"Repeated sequences : {len(repeated_rows)}")
    print(f"Similar pairs      : {len(similar_rows)}")
    print()
    print("Örnek odak kayıtları:")
    for row in record_reports:
        if row["section"] in {"shoot.o", "grounderpass.o", "defence.o", "defenceMark.o"}:
            print(
                f"{row['file']} | {row['section']} | rec={row['record']} | "
                f"{row['sequence_pattern']} | {row['likely_structural_role']} | "
                f"{row['values_preview']}"
            )


if __name__ == "__main__":
    main()