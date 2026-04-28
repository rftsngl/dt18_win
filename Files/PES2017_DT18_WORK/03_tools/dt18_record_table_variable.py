import argparse
import struct
import zlib
from pathlib import Path


BIN_DIR = Path(r"C:\Games\PesModlama\Files\PES2017_DT18_WORK\02_bins")


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


def looks_like_float(raw_uint: int, float_value: float) -> bool:
    if raw_uint in (0, 1):
        return False

    if not (-10000.0 <= float_value <= 10000.0):
        return False

    if abs(float_value) < 0.000001:
        return False

    return True


def format_value(section_data: bytes, offset: int) -> str:
    raw_uint = read_u32(section_data, offset)
    raw_int = read_i32(section_data, offset)
    f32 = read_f32(section_data, offset)

    if looks_like_float(raw_uint, f32):
        return f"{f32:g}f"

    return str(raw_int)


def print_records(section_data: bytes, records: list[dict], max_records: int | None):
    print(f"{'Rec':<5} {'LocalOff':<10} {'Len':<6} {'Fields'}")
    print("-" * 120)

    for rec in records:
        if max_records is not None and rec["index"] >= max_records:
            break

        values = []

        for i in range(rec["field_count"]):
            value_offset = rec["start"] + i * 4
            values.append(format_value(section_data, value_offset))

        print(
            f"{rec['index']:<5} "
            f"0x{rec['start']:04X}   "
            f"{rec['length']:<6} "
            f"{values}"
        )


def print_detail(section_data: bytes, records: list[dict], detail_index: int):
    rec = records[detail_index]

    print()
    print("=" * 100)
    print(
        f"Raw detail for record {detail_index}, "
        f"local offset 0x{rec['start']:04X}, "
        f"length {rec['length']} bytes"
    )
    print("-" * 100)
    print(f"{'Field':<8} {'LocalOff':<10} {'Bytes':<14} {'int32':>12} {'uint32':>12} {'float32':>16}")
    print("-" * 100)

    for i in range(rec["field_count"]):
        local_offset = rec["start"] + i * 4
        chunk = section_data[local_offset:local_offset + 4]

        int_value = read_i32(section_data, local_offset)
        uint_value = read_u32(section_data, local_offset)
        float_value = read_f32(section_data, local_offset)

        print(
            f"F{i:<7} "
            f"0x{local_offset:04X}   "
            f"{chunk.hex(' ').upper():<14} "
            f"{int_value:>12} "
            f"{uint_value:>12} "
            f"{float_value:>16.8g}"
        )


def main():
    parser = argparse.ArgumentParser(
        description="PES dt18 variable-size record table reader"
    )

    parser.add_argument("--file", required=True)
    parser.add_argument("--offset", required=True, type=parse_int)
    parser.add_argument("--length", required=True, type=parse_int)
    parser.add_argument("--records", type=int, default=None)
    parser.add_argument("--detail-record", type=int, default=None)

    args = parser.parse_args()

    path = BIN_DIR / args.file

    if not path.exists():
        raise FileNotFoundError(f"Dosya bulunamadı: {path}")

    data = path.read_bytes()
    raw, compressed = decompress_if_needed(data)

    section_data = raw[args.offset:args.offset + args.length]

    offsets = collect_record_offsets(section_data)
    records = build_records(offsets, len(section_data))

    print(f"File          : {path.name}")
    print(f"Compressed    : {compressed}")
    print(f"Section offset: 0x{args.offset:08X}")
    print(f"Section length: {args.length}")
    print(f"Record count  : {len(records)}")
    print()

    print_records(section_data, records, args.records)

    if args.detail_record is not None:
        if args.detail_record < 0 or args.detail_record >= len(records):
            raise ValueError("Geçersiz detail record index.")
        print_detail(section_data, records, args.detail_record)


if __name__ == "__main__":
    main()