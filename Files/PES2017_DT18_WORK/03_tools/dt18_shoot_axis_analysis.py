import csv
from pathlib import Path


BASE_DIR = Path(r"C:\Games\PesModlama\Files\PES2017_DT18_WORK")
MATRIX_PATH = BASE_DIR / r"04_tests\analysis\family_matrices\constant_player_shoot_matrix.csv"
OUT_DIR = BASE_DIR / r"04_tests\analysis"

OUT_CSV = OUT_DIR / "shoot_axis_analysis.csv"
OUT_MD = OUT_DIR / "shoot_axis_analysis.md"


FAMILY_A = [1, 2, 3]
FAMILY_B = [6, 7, 8]
PAIRS = list(zip(FAMILY_A, FAMILY_B))


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


def fmt(v):
    if v is None:
        return ""

    if abs(v - round(v)) < 1e-6:
        return str(int(round(v)))

    return f"{v:.6g}"


def extract_values(row):
    fcols = sorted(
        [c for c in row.keys() if c.startswith("F")],
        key=lambda c: int(c[1:])
    )

    values = []

    for c in fcols:
        v = to_float(row[c])

        if v is None:
            continue

        if abs(v) < 1e-6:
            continue

        values.append(v)

    return values


def is_non_decreasing(values):
    return all(values[i] <= values[i + 1] for i in range(len(values) - 1))


def is_non_increasing(values):
    return all(values[i] >= values[i + 1] for i in range(len(values) - 1))


def main():
    if not MATRIX_PATH.exists():
        raise FileNotFoundError(f"Matrix bulunamadı: {MATRIX_PATH}")

    rows = read_csv(MATRIX_PATH)

    record_values = {
        int(row["record"]): extract_values(row)
        for row in rows
    }

    result_rows = []

    # 1) Record içi yatay analiz
    for family_name, records in [("A", FAMILY_A), ("B", FAMILY_B)]:
        for rec in records:
            values = record_values[rec]

            result_rows.append({
                "analysis_type": "record_horizontal_curve",
                "family": family_name,
                "record": rec,
                "field": "",
                "values": ", ".join(fmt(v) for v in values),
                "metric": "non_decreasing",
                "result": str(is_non_decreasing(values)),
                "delta": "",
                "ratio": "",
                "interpretation": "Record içindeki F0-F5 dizisinin artan curve gibi davranıp davranmadığı.",
            })

    # 2) Family içi dikey analiz: rec1→rec2→rec3 ve rec6→rec7→rec8
    max_fields = min(
        min(len(record_values[r]) for r in FAMILY_A),
        min(len(record_values[r]) for r in FAMILY_B),
    )

    for family_name, records in [("A", FAMILY_A), ("B", FAMILY_B)]:
        for field_index in range(max_fields):
            col_values = [record_values[r][field_index] for r in records]

            result_rows.append({
                "analysis_type": "family_vertical_axis",
                "family": family_name,
                "record": "->".join(str(r) for r in records),
                "field": f"F{field_index}",
                "values": ", ".join(fmt(v) for v in col_values),
                "metric": "non_increasing",
                "result": str(is_non_increasing(col_values)),
                "delta": fmt(col_values[-1] - col_values[0]),
                "ratio": fmt(col_values[-1] / col_values[0]) if abs(col_values[0]) > 1e-6 else "",
                "interpretation": "Aile içinde record ekseninde değerlerin yüksekten düşüğe gidip gitmediği.",
            })

    # 3) Family A vs B aynı field farkları
    for a_rec, b_rec in PAIRS:
        a_values = record_values[a_rec]
        b_values = record_values[b_rec]

        for field_index in range(min(len(a_values), len(b_values))):
            a = a_values[field_index]
            b = b_values[field_index]
            delta = b - a
            ratio = b / a if abs(a) > 1e-6 else None

            result_rows.append({
                "analysis_type": "family_B_minus_A",
                "family": "A_vs_B",
                "record": f"{a_rec}<->{b_rec}",
                "field": f"F{field_index}",
                "values": f"A={fmt(a)}, B={fmt(b)}",
                "metric": "B_greater_than_A",
                "result": str(b > a),
                "delta": fmt(delta),
                "ratio": fmt(ratio),
                "interpretation": "Family B’nin aynı konumdaki Family A değerinden büyük olup olmadığı.",
            })

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "analysis_type",
            "family",
            "record",
            "field",
            "values",
            "metric",
            "result",
            "delta",
            "ratio",
            "interpretation",
        ]

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(result_rows)

    lines = []
    lines.append("# shoot.o Axis Analysis")
    lines.append("")
    lines.append("Bu rapor semantik mapping vermez. Yalnızca `shoot.o` içindeki record/field eksenlerinin yapısal davranışını inceler.")
    lines.append("")
    lines.append("## 1. Record içi yatay curve kontrolü")
    lines.append("")
    lines.append("| Family | Record | Values | Non-decreasing |")
    lines.append("|---|---:|---|---|")

    for r in result_rows:
        if r["analysis_type"] == "record_horizontal_curve":
            lines.append(
                f"| {r['family']} | {r['record']} | `{r['values']}` | {r['result']} |"
            )

    lines.append("")
    lines.append("## 2. Family içi dikey eksen kontrolü")
    lines.append("")
    lines.append("| Family | Field | Values | Non-increasing | Delta last-first | Ratio last/first |")
    lines.append("|---|---:|---|---|---:|---:|")

    for r in result_rows:
        if r["analysis_type"] == "family_vertical_axis":
            lines.append(
                f"| {r['family']} | {r['field']} | `{r['values']}` | {r['result']} | {r['delta']} | {r['ratio']} |"
            )

    lines.append("")
    lines.append("## 3. Family B - Family A karşılaştırması")
    lines.append("")
    lines.append("| Pair | Field | Values | B>A | Delta | Ratio |")
    lines.append("|---|---:|---|---|---:|---:|")

    for r in result_rows:
        if r["analysis_type"] == "family_B_minus_A":
            lines.append(
                f"| {r['record']} | {r['field']} | `{r['values']}` | {r['result']} | {r['delta']} | {r['ratio']} |"
            )

    lines.append("")
    lines.append("## Structural interpretation")
    lines.append("")
    lines.append("- F0-F5 ekseni record içinde genellikle artan curve gibi davranıyor.")
    lines.append("- Aile içinde record ekseni genellikle yüksekten düşüğe gidiyor.")
    lines.append("- Family B aynı pozisyonlarda Family A’dan sistematik olarak daha yüksek.")
    lines.append("- Bu sonuçlar semantik anlam vermez; yalnızca `shoot.o` içinde iki paralel curve ailesi bulunduğunu güçlendirir.")
    lines.append("- Sonraki adım, test planı oluşturmadan önce hangi eksenin test için daha güvenli olduğunu seçmektir.")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print("shoot.o axis analysis oluşturuldu.")
    print(f"CSV     : {OUT_CSV}")
    print(f"Markdown: {OUT_MD}")

    print()
    print("Özet:")
    for r in result_rows:
        if r["analysis_type"] == "record_horizontal_curve":
            print(
                f"{r['family']} rec {r['record']}: non_decreasing={r['result']} | {r['values']}"
            )


if __name__ == "__main__":
    main()