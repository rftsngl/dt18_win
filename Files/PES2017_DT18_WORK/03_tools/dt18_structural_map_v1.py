import csv
from pathlib import Path


BASE_DIR = Path(r"C:\Games\PesModlama\Files\PES2017_DT18_WORK")
MATRIX_DIR = BASE_DIR / r"04_tests\analysis\family_matrices"
OUT_DIR = BASE_DIR / r"04_tests\analysis"

OUT_CSV = OUT_DIR / "dt18_structural_map_v1.csv"
OUT_MD = OUT_DIR / "dt18_structural_map_v1.md"


def read_csv(path: Path):
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows, fieldnames):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def to_float(value):
    if value is None:
        return None

    value = str(value).strip()

    if value == "":
        return None

    try:
        return float(value)
    except ValueError:
        return None


def fmt_num(value):
    if value is None:
        return ""

    if abs(value - round(value)) < 1e-6:
        return str(int(round(value)))

    return f"{value:.6g}"


def nonzero(values):
    return [v for v in values if v is not None and abs(v) > 1e-6]


def classify_sequence(values):
    nz = nonzero(values)

    if not nz:
        return "all_zero"

    if all(v in (0.0, 1.0) for v in values if v is not None):
        return "flag_group"

    if len(nz) == 1:
        return "single_scalar"

    increasing = all(nz[i] <= nz[i + 1] for i in range(len(nz) - 1))
    decreasing = all(nz[i] >= nz[i + 1] for i in range(len(nz) - 1))

    if increasing and len(set(nz)) > 1:
        return "monotonic_increasing_or_flat"

    if decreasing and len(set(nz)) > 1:
        return "monotonic_decreasing_or_flat"

    repeated_count = sum(1 for v in set(nz) if nz.count(v) > 1)

    if repeated_count >= 2:
        return "repeated_value_group"

    if len(nz) <= 6:
        return "small_mixed_scalar_group"

    return "mixed_numeric_group"


def structural_label(section, record, values):
    record = int(record)
    nz = nonzero(values)
    pattern = classify_sequence(values)

    # Section-specific structural labels.
    # Bunlar semantic anlam değil, sadece verideki aile/biçim adlarıdır.
    if section == "shoot.o":
        if record == 0:
            return "shoot_scalar_header_or_setup_block"
        if record in (1, 2, 3):
            return "shoot_curve_family_A"
        if record == 4:
            return "shoot_small_decreasing_block_A"
        if record == 5:
            return "shoot_scalar_block_B"
        if record in (6, 7, 8):
            return "shoot_curve_family_B"
        if record == 9:
            return "shoot_small_decreasing_block_B"

    if section == "grounderpass.o":
        if record == 0:
            return "grounderpass_small_setup_block_A"
        if record == 1:
            return "grounderpass_repeated_pair_block_B"
        if record == 2:
            return "grounderpass_long_mixed_parameter_block_C"

    if section == "contact.o":
        return "contact_single_physics_scalar_block"

    if section == "throughpass.o":
        return "throughpass_long_mixed_parameter_block"

    if section == "defence.o":
        return "defence_single_behavior_parameter_block"

    if section == "defenceMark.o":
        return "defenceMark_single_marking_parameter_block"

    if section == "support.o":
        return "support_single_positioning_parameter_block"

    if section == "spaceRun.o":
        return "spaceRun_single_offball_run_parameter_block"

    # Generic fallback
    if pattern == "monotonic_increasing_or_flat":
        return "generic_increasing_curve_block"

    if pattern == "monotonic_decreasing_or_flat":
        return "generic_decreasing_curve_block"

    if pattern == "repeated_value_group":
        return "generic_repeated_value_block"

    if pattern == "small_mixed_scalar_group":
        return "generic_small_scalar_block"

    return "generic_mixed_numeric_block"


def next_action_for(section, label):
    if section == "shoot.o":
        return "Compare curve families A/B; do not patch before controlled test plan."

    if section in {"grounderpass.o", "throughpass.o"}:
        return "Compare pass-related blocks; search for repeated value groups and external clues."

    if section in {"defence.o", "defenceMark.o", "support.o", "spaceRun.o"}:
        return "Keep as structural AI/team-behavior block; avoid patch until subgroups are split."

    if section == "contact.o":
        return "Potential physics scalar block; high effect risk, avoid early patch."

    return "Keep for catalog only."


def main():
    if not MATRIX_DIR.exists():
        raise FileNotFoundError(f"Matrix klasörü bulunamadı: {MATRIX_DIR}")

    matrix_files = sorted(MATRIX_DIR.glob("*_matrix.csv"))

    rows_out = []

    for path in matrix_files:
        rows = read_csv(path)

        for row in rows:
            file_name = row["file"]
            section = row["section"]
            record = row["record"]

            f_columns = sorted(
                [c for c in row.keys() if c.startswith("F")],
                key=lambda x: int(x[1:])
            )

            values = [to_float(row[c]) for c in f_columns]
            nz = nonzero(values)

            pattern = classify_sequence(values)
            label = structural_label(section, record, values)

            rows_out.append({
                "file": file_name,
                "section": section,
                "record": record,
                "record_offset": row["record_offset"],
                "record_length": row["record_length"],
                "parse_mode": row["parse_mode"],
                "values_nonzero": ", ".join(fmt_num(v) for v in nz),
                "nonzero_count": len(nz),
                "min_value": fmt_num(min(nz)) if nz else "",
                "max_value": fmt_num(max(nz)) if nz else "",
                "sequence_pattern": pattern,
                "structural_label": label,
                "semantic_meaning": "unknown",
                "confidence": "structural_only",
                "next_action": next_action_for(section, label),
                "notes": "",
            })

    rows_out.sort(
        key=lambda r: (
            r["file"],
            r["section"],
            int(r["record"]),
        )
    )

    fieldnames = [
        "file",
        "section",
        "record",
        "record_offset",
        "record_length",
        "parse_mode",
        "values_nonzero",
        "nonzero_count",
        "min_value",
        "max_value",
        "sequence_pattern",
        "structural_label",
        "semantic_meaning",
        "confidence",
        "next_action",
        "notes",
    ]

    write_csv(OUT_CSV, rows_out, fieldnames)

    lines = []
    lines.append("# PES 2017 dt18 Structural Map v1")
    lines.append("")
    lines.append("Bu dosya semantik mapping değildir. Yalnızca binary veriden çıkarılan yapısal record ailelerini gösterir.")
    lines.append("`semantic_meaning` alanı bilinçli olarak `unknown` bırakılmıştır.")
    lines.append("")

    current_section = None

    for r in rows_out:
        section_title = f"{r['file']} / {r['section']}"

        if section_title != current_section:
            current_section = section_title
            lines.append(f"## {section_title}")
            lines.append("")
            lines.append("| Rec | Offset | Pattern | Structural label | Values |")
            lines.append("|---:|---|---|---|---|")

        lines.append(
            f"| {r['record']} "
            f"| `{r['record_offset']}` "
            f"| {r['sequence_pattern']} "
            f"| `{r['structural_label']}` "
            f"| `{r['values_nonzero']}` |"
        )

        # Section bitişlerini markdown'da görsel olarak ayırmak için sonradan boşluk eklemiyoruz;
        # başlık geldiğinde ayrılacak.

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print("Structural map v1 oluşturuldu.")
    print(f"CSV     : {OUT_CSV}")
    print(f"Markdown: {OUT_MD}")
    print(f"Rows    : {len(rows_out)}")

    print()
    print("shoot.o structural map:")
    for r in rows_out:
        if r["section"] == "shoot.o":
            print(
                f"rec={r['record']} | {r['structural_label']} | "
                f"{r['sequence_pattern']} | {r['values_nonzero']}"
            )


if __name__ == "__main__":
    main()