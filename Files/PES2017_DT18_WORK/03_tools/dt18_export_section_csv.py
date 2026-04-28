import argparse
import csv
import struct
import zlib
from pathlib import Path


BIN_DIR = Path(r"C:\Games\PesModlama\Files\PES2017_DT18_WORK\02_bins")
OUT_DIR = Path(r"C:\Games\PesModlama\Files\PES2017_DT18_WORK\04_tests")


def has_wesys_header(data: bytes) -> bool:
    return len(data) >= 16 and data[4:8] == b"ESYS"


def decompress_if_needed(data: bytes) -> tuple[bytes, bool]:
    if has_wesys_header(data):
        return zlib.decompress(data[16:]), True
    return data, False


def parse_int(value: str) -> int:
    return int(value, 0)


def read_u32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def read_i32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<i", data, offset)[0]


def read_f32(data: bytes, offset: int) -> float:
    return struct.unpack_from("<f", data, offset)[0]


def collect_record_offsets(section_data: bytes) -> list[int]:
    offsets = []
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

    return offsets


def build_records(offsets: list[int], section_len: int):
    records = []

    for index, start in enumerate(offsets):
        if index + 1 < len(offsets):
            end = offsets[index + 1]
        else:
            end = section_len

        length = end - start

        if length <= 0:
            continue

        records.append({
            "index": index,
            "start": start,
            "end": end,
            "length": length,
            "field_count": length // 4,
        })

    return records


def main():
    parser = argparse.ArgumentParser(
        description="Export PES dt18 section records to CSV"
    )

    parser.add_argument("--file", required=True)
    parser.add_argument("--section-name", required=True)
    parser.add_argument("--offset", required=True, type=parse_int)
    parser.add_argument("--length", required=True, type=parse_int)

    args = parser.parse_args()

    path = BIN_DIR / args.file

    if not path.exists():
        raise FileNotFoundError(f"Dosya bulunamadı: {path}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    data = path.read_bytes()
    raw, compressed = decompress_if_needed(data)

    section_data = raw[args.offset:args.offset + args.length]
    offsets = collect_record_offsets(section_data)
    records = build_records(offsets, len(section_data))

    out_path = OUT_DIR / f"{path.stem}_{args.section_name}_records.csv"

    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "file",
            "section",
            "record",
            "record_local_offset_hex",
            "record_length",
            "field",
            "field_local_offset_hex",
            "field_file_offset_hex",
            "bytes_hex",
            "int32",
            "uint32",
            "float32",
        ])

        for rec in records:
            for field_index in range(rec["field_count"]):
                local_offset = rec["start"] + field_index * 4
                file_offset = args.offset + local_offset
                chunk = section_data[local_offset:local_offset + 4]

                writer.writerow([
                    path.name,
                    args.section_name,
                    rec["index"],
                    f"0x{rec['start']:04X}",
                    rec["length"],
                    field_index,
                    f"0x{local_offset:04X}",
                    f"0x{file_offset:08X}",
                    chunk.hex(" ").upper(),
                    read_i32(section_data, local_offset),
                    read_u32(section_data, local_offset),
                    read_f32(section_data, local_offset),
                ])

    print(f"CSV export edildi: {out_path}")
    print(f"Compressed: {compressed}")
    print(f"Record count: {len(records)}")


if __name__ == "__main__":
    main()