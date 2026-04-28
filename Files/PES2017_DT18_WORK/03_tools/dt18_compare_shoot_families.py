import csv
from pathlib import Path


BASE_DIR = Path(r"C:\Games\PesModlama\Files\PES2017_DT18_WORK")
MATRIX_PATH = BASE_DIR / r"04_tests\analysis\family_matrices\constant_player_shoot_matrix.csv"
OUT_DIR = BASE_DIR / r"04_tests\analysis"

OUT_CSV = OUT_DIR / "shoot_family_comparison.csv"
OUT_MD = OUT_DIR / "shoot_family_comparison.md"


FAMILY_A = [1, 2, 3]
FAMILY_B = [6, 7, 8]


def read_csv(path: Path):
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


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


def fmt(value):
    if value is None:
        return ""

    if abs(value - round(value)) < 1e-6:
        return str(int(round(value)))

    return f"{value:.6g}"


def extract_record_values(row):
    fcols = sorted(
        [c for c in row.keys() if c.startswith("F")],
        key=lambda c: int(c[1:])
    )

    values = []

    for c in fcols:
        v = to_float(row[c])
        if v is None:
            continue

        # trailing zero/paddingleri dışarıda bırakıyoruz
        if abs(v) < 1e-6:
            continue

        values.append(v)

    return values


def main():
    if not MATRIX_PATH.exists():
        raise FileNotFoundError(f"Matrix bulunamadı: {MATRIX_PATH}")

    rows = read_csv(MATRIX_PATH)

    record_map = {
        int(row["record"]): {
            "row": row,
            "values": extract_record_values(row),
        }
        for row in rows
    }

    comparison_rows = []

    # Aile içi karşılaştırma
    for family_name, records in [("A", FAMILY_A), ("B", FAMILY_B)]:
        for rec in records:
            values = record_map[rec]["values"]

            comparison_rows.append({
                "comparison_type": "family_member",
                "family": family_name,
                "record": rec,
                "paired_record": "",
                "field": "",
                "value": ", ".join(fmt(v) for v in values),
                "delta": "",
                "ratio": "",
                "note": "family member values",
            })

    # A ve B ailelerini sırayla eşleştir:
    # rec1 ↔ rec6, rec2 ↔ rec7, rec3 ↔ rec8
    pairings = list(zip(FAMILY_A, FAMILY_B))

    for a_rec, b_rec in pairings:
        a_values = record_map[a_rec]["values"]
        b_values = record_map[b_rec]["values"]

        max_len = min(len(a_values), len(b_values))

        for i in range(max_len):
            a = a_values[i]
            b = b_values[i]
            delta = b - a
            ratio = b / a if abs(a) > 1e-6 else None

            comparison_rows.append({
                "comparison_type": "A_vs_B_pair",
                "family": "A_vs_B",
                "record": a_rec,
                "paired_record": b_rec,
                "field": f"F{i}",
                "value": f"A={fmt(a)} / B={fmt(b)}",
                "delta": fmt(delta),
                "ratio": fmt(ratio),
                "note": f"rec {a_rec} vs rec {b_rec}",
            })

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "comparison_type",
            "family",
            "record",
            "paired_record",
            "field",
            "value",
            "delta",
            "ratio",
            "note",
        ]

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(comparison_rows)

    # Markdown rapor
    lines = []
    lines.append("# shoot.o Family Comparison")
    lines.append("")
    lines.append("Bu rapor semantik mapping vermez. Sadece `shoot.o` içindeki iki büyük curve ailesinin yapısal farklarını gösterir.")
    lines.append("")
    lines.append("## Family A")
    lines.append("")
    lines.append("| Record | Values |")
    lines.append("|---:|---|")

    for rec in FAMILY_A:
        values = record_map[rec]["values"]
        lines.append(f"| {rec} | `{', '.join(fmt(v) for v in values)}` |")

    lines.append("")
    lines.append("## Family B")
    lines.append("")
    lines.append("| Record | Values |")
    lines.append("|---:|---|")

    for rec in FAMILY_B:
        values = record_map[rec]["values"]
        lines.append(f"| {rec} | `{', '.join(fmt(v) for v in values)}` |")

    lines.append("")
    lines.append("## A vs B paired comparison")
    lines.append("")
    lines.append("| Pair | Field | A | B | Delta B-A | Ratio B/A |")
    lines.append("|---|---:|---:|---:|---:|---:|")

    for a_rec, b_rec in pairings:
        a_values = record_map[a_rec]["values"]
        b_values = record_map[b_rec]["values"]

        max_len = min(len(a_values), len(b_values))

        for i in range(max_len):
            a = a_values[i]
            b = b_values[i]
            delta = b - a
            ratio = b / a if abs(a) > 1e-6 else None

            lines.append(
                f"| rec {a_rec} ↔ rec {b_rec} "
                f"| F{i} "
                f"| {fmt(a)} "
                f"| {fmt(b)} "
                f"| {fmt(delta)} "
                f"| {fmt(ratio)} |"
            )

    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("- `meaning` hâlâ unknown.")
    lines.append("- Family A ve Family B benzer sütun sayısına sahip iki ayrı curve ailesi gibi duruyor.")
    lines.append("- Family B genel olarak Family A’dan daha yüksek değerler içeriyor.")
    lines.append("- Bu, Family B’nin daha güçlü/agresif/üst seviye bir şut davranış grubu olabileceğini düşündürür; fakat bu sadece yapısal hipotezdir.")
    lines.append("- Patch yapılmadan önce test planı ve rollback sistemi hazırlanmalıdır.")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print("shoot.o family comparison oluşturuldu.")
    print(f"CSV     : {OUT_CSV}")
    print(f"Markdown: {OUT_MD}")

    print()
    print("A vs B özet:")
    for a_rec, b_rec in pairings:
        a_values = record_map[a_rec]["values"]
        b_values = record_map[b_rec]["values"]

        print(f"rec {a_rec} ↔ rec {b_rec}")
        print(f"  A: {', '.join(fmt(v) for v in a_values)}")
        print(f"  B: {', '.join(fmt(v) for v in b_values)}")


if __name__ == "__main__":
    main()