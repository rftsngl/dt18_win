import csv
import re
import struct
import zlib
from pathlib import Path
from typing import Any, TypedDict


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BIN_DIR = PROJECT_ROOT / "02_bins"
OUT_DIR = PROJECT_ROOT / "04_tests" / "bulk_export"


class Layout(TypedDict):
    type: str
    section_count: int
    name_start: int


class SectionInfo(TypedDict):
    index: int
    name: str
    offset: int
    length: int


class RecordInfo(TypedDict):
    index: int
    start: int
    end: int
    length: int
    field_count: int


LAYOUTS: dict[str, Layout] = {
    "constant_match.bin": {
        "type": "match",
        "section_count": 23,
        "name_start": 0x11C,
    },
    "constant_player.bin": {
        "type": "player",
        "section_count": 34,
        "name_start": 0x1A0,
    },
    "constant_team.bin": {
        "type": "team",
        "section_count": 16,
        "name_start": 0x0C8,
    },
}


def safe_name(value: str) -> str:
    value = value.replace(".o", "")
    value = re.sub(r"[^a-zA-Z0-9_\-]+", "_", value)
    return value.strip("_")


def has_wesys_header(data: bytes) -> bool:
    return len(data) >= 16 and data[4:8] == b"ESYS"


def decompress_if_needed(data: bytes) -> tuple[bytes, bool]:
    if has_wesys_header(data):
        return zlib.decompress(data[16:]), True
    return data, False


def read_u32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def read_i32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<i", data, offset)[0]


def read_f32(data: bytes, offset: int) -> float:
    return struct.unpack_from("<f", data, offset)[0]


def looks_like_float(raw_uint: int, float_value: float) -> bool:
    if raw_uint in (0, 1):
        return False

    if not (-10000.0 <= float_value <= 10000.0):
        return False

    if abs(float_value) < 0.000001:
        return False

    return True


def preferred_value(data: bytes, offset: int) -> tuple[str, str]:
    raw_uint = read_u32(data, offset)
    raw_int = read_i32(data, offset)
    f32 = read_f32(data, offset)

    if looks_like_float(raw_uint, f32):
        return "float32_candidate", f"{f32:g}"

    return "int32_or_flag", str(raw_int)


def read_section_table(
    raw: bytes, section_count: int, name_start: int
) -> list[SectionInfo]:
    section_offsets: list[int] = []

    cursor = 0
    for _ in range(section_count):
        _section_len, _unknown, section_offset = struct.unpack_from("<3i", raw, cursor)
        section_offsets.append(section_offset)
        cursor += 12

    sections: list[SectionInfo] = []

    if not section_offsets:
        raise ValueError("Section offset tablosu bulunamadı.")

    first_section_offset = section_offsets[0]
    names_blob = raw[name_start:first_section_offset]

    section_names: list[str] = [
        item.decode("utf-8", errors="replace")
        for item in names_blob.split(b"\x00")
        if item
    ]

    if len(section_names) != section_count:
        print(
            f"[WARN] Section name count mismatch: "
            f"expected={section_count}, actual={len(section_names)}"
        )

    for index in range(section_count):
        offset = section_offsets[index]

        if index + 1 < section_count:
            length = section_offsets[index + 1] - offset
        else:
            length = len(raw) - offset

        if index < len(section_names):
            name = section_names[index]
        else:
            name = f"UNKNOWN_{index:02d}.o"

        if length <= 0:
            continue

        if offset < 0 or offset >= len(raw):
            continue

        if offset + length > len(raw):
            length = len(raw) - offset

        sections.append(
            {
                "index": index,
                "name": name,
                "offset": offset,
                "length": length,
            }
        )

    return sections


def collect_record_offsets(section_data: bytes) -> list[int]:
    offsets: list[int] = []
    cursor = 0
    section_len = len(section_data)

    while cursor + 4 <= section_len:
        value = read_u32(section_data, cursor)

        if value == 0:
            break

        if value >= section_len:
            break

        if value % 4 != 0:
            break

        if offsets and value <= offsets[-1]:
            break

        offsets.append(value)
        cursor += 4

    # Yanlış pozitifleri azalt:
    # Gerçek offset table için en az 2 record offset bekleyelim.
    if len(offsets) < 2:
        return []

    first_offset = offsets[0]

    # Offset table veri alanının içine taşmamalı.
    # Örn: 10 offset varsa table 40 byte, ilk veri offseti genelde >= 40 olur.
    table_size = len(offsets) * 4
    if first_offset < table_size:
        return []

    return offsets


def build_records(section_data: bytes) -> tuple[str, list[RecordInfo]]:
    section_len = len(section_data)
    offsets = collect_record_offsets(section_data)

    records: list[RecordInfo] = []

    if offsets:
        parse_mode = "record_table"

        for index, start in enumerate(offsets):
            if index + 1 < len(offsets):
                end = offsets[index + 1]
            else:
                end = section_len

            length = end - start

            if length <= 0:
                continue

            records.append(
                {
                    "index": index,
                    "start": start,
                    "end": end,
                    "length": length,
                    "field_count": length // 4,
                }
            )

    else:
        parse_mode = "raw_4byte_fields"
        records.append(
            {
                "index": 0,
                "start": 0,
                "end": section_len,
                "length": section_len,
                "field_count": section_len // 4,
            }
        )

    return parse_mode, records


def export_section_csv(
    file_name: str,
    section: SectionInfo,
    section_data: bytes,
    parse_mode: str,
    records: list[RecordInfo],
    out_path: Path,
) -> None:
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(
            [
                "file",
                "section",
                "section_index",
                "section_file_offset_hex",
                "section_length",
                "parse_mode",
                "record",
                "record_local_offset_hex",
                "record_file_offset_hex",
                "record_length",
                "field",
                "field_local_offset_hex",
                "field_file_offset_hex",
                "bytes_hex",
                "int32",
                "uint32",
                "float32",
                "preferred_type",
                "preferred_value",
            ]
        )

        for rec in records:
            for field_index in range(rec["field_count"]):
                local_offset = rec["start"] + field_index * 4

                if local_offset + 4 > len(section_data):
                    continue

                file_offset = section["offset"] + local_offset
                chunk = section_data[local_offset : local_offset + 4]

                int32 = read_i32(section_data, local_offset)
                uint32 = read_u32(section_data, local_offset)
                float32 = read_f32(section_data, local_offset)
                p_type, p_value = preferred_value(section_data, local_offset)

                writer.writerow(
                    [
                        file_name,
                        section["name"],
                        section["index"],
                        f"0x{section['offset']:08X}",
                        section["length"],
                        parse_mode,
                        rec["index"],
                        f"0x{rec['start']:04X}",
                        f"0x{section['offset'] + rec['start']:08X}",
                        rec["length"],
                        field_index,
                        f"0x{local_offset:04X}",
                        f"0x{file_offset:08X}",
                        chunk.hex(" ").upper(),
                        int32,
                        uint32,
                        float32,
                        p_type,
                        p_value,
                    ]
                )


def append_all_fields_rows(
    all_writer: Any,
    file_name: str,
    section: SectionInfo,
    section_data: bytes,
    parse_mode: str,
    records: list[RecordInfo],
) -> None:
    for rec in records:
        for field_index in range(rec["field_count"]):
            local_offset = rec["start"] + field_index * 4

            if local_offset + 4 > len(section_data):
                continue

            file_offset = section["offset"] + local_offset
            chunk = section_data[local_offset : local_offset + 4]

            int32 = read_i32(section_data, local_offset)
            uint32 = read_u32(section_data, local_offset)
            float32 = read_f32(section_data, local_offset)
            p_type, p_value = preferred_value(section_data, local_offset)

            all_writer.writerow(
                [
                    file_name,
                    section["name"],
                    section["index"],
                    f"0x{section['offset']:08X}",
                    section["length"],
                    parse_mode,
                    rec["index"],
                    f"0x{rec['start']:04X}",
                    f"0x{section['offset'] + rec['start']:08X}",
                    rec["length"],
                    field_index,
                    f"0x{local_offset:04X}",
                    f"0x{file_offset:08X}",
                    chunk.hex(" ").upper(),
                    int32,
                    uint32,
                    float32,
                    p_type,
                    p_value,
                ]
            )


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    section_index_path = OUT_DIR / "section_index.csv"
    all_fields_path = OUT_DIR / "all_fields.csv"

    with section_index_path.open(
        "w", newline="", encoding="utf-8"
    ) as section_index_file, all_fields_path.open(
        "w", newline="", encoding="utf-8"
    ) as all_fields_file:

        section_index_writer = csv.writer(section_index_file)
        all_fields_writer = csv.writer(all_fields_file)

        section_index_writer.writerow(
            [
                "file",
                "compressed",
                "raw_size",
                "section_index",
                "section",
                "section_file_offset_hex",
                "section_length",
                "parse_mode",
                "record_count",
                "field_count_total",
                "float_candidate_count",
                "csv_path",
            ]
        )

        all_fields_writer.writerow(
            [
                "file",
                "section",
                "section_index",
                "section_file_offset_hex",
                "section_length",
                "parse_mode",
                "record",
                "record_local_offset_hex",
                "record_file_offset_hex",
                "record_length",
                "field",
                "field_local_offset_hex",
                "field_file_offset_hex",
                "bytes_hex",
                "int32",
                "uint32",
                "float32",
                "preferred_type",
                "preferred_value",
            ]
        )

        for file_name, layout in LAYOUTS.items():
            path = BIN_DIR / file_name

            if not path.exists():
                print(f"[MISSING] {path}")
                continue

            data = path.read_bytes()
            raw, compressed = decompress_if_needed(data)

            sections = read_section_table(
                raw=raw,
                section_count=layout["section_count"],
                name_start=layout["name_start"],
            )

            file_out_dir = OUT_DIR / path.stem
            file_out_dir.mkdir(parents=True, exist_ok=True)

            print("=" * 100)
            print(f"File       : {file_name}")
            print(f"Compressed : {compressed}")
            print(f"Raw size   : {len(raw)}")
            print(f"Sections   : {len(sections)}")
            print("-" * 100)

            for section in sections:
                section_data = raw[
                    section["offset"] : section["offset"] + section["length"]
                ]
                parse_mode, records = build_records(section_data)

                out_path = (
                    file_out_dir
                    / f"{section['index']:02d}_{safe_name(section['name'])}.csv"
                )

                export_section_csv(
                    file_name=file_name,
                    section=section,
                    section_data=section_data,
                    parse_mode=parse_mode,
                    records=records,
                    out_path=out_path,
                )

                append_all_fields_rows(
                    all_writer=all_fields_writer,
                    file_name=file_name,
                    section=section,
                    section_data=section_data,
                    parse_mode=parse_mode,
                    records=records,
                )

                field_count_total = sum(rec["field_count"] for rec in records)

                float_candidate_count = 0
                for rec in records:
                    for field_index in range(rec["field_count"]):
                        local_offset = rec["start"] + field_index * 4
                        if local_offset + 4 > len(section_data):
                            continue
                        p_type, _ = preferred_value(section_data, local_offset)
                        if p_type == "float32_candidate":
                            float_candidate_count += 1

                section_index_writer.writerow(
                    [
                        file_name,
                        compressed,
                        len(raw),
                        section["index"],
                        section["name"],
                        f"0x{section['offset']:08X}",
                        section["length"],
                        parse_mode,
                        len(records),
                        field_count_total,
                        float_candidate_count,
                        str(out_path),
                    ]
                )

                print(
                    f"{section['index']:02d} | "
                    f"{section['name']:<32} | "
                    f"offset=0x{section['offset']:08X} | "
                    f"len={section['length']:<5} | "
                    f"{parse_mode:<16} | "
                    f"records={len(records):<3} | "
                    f"fields={field_count_total:<4} | "
                    f"floats={float_candidate_count:<4}"
                )

    print()
    print("BULK EXPORT TAMAMLANDI")
    print(f"Section index : {section_index_path}")
    print(f"All fields    : {all_fields_path}")
    print(f"Section CSVs  : {OUT_DIR}")


if __name__ == "__main__":
    main()
