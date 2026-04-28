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


def collect_record_offsets(section_data: bytes):
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


def infer_record_size(offsets: list[int], section_len: int) -> int:
    if len(offsets) >= 2:
        return offsets[1] - offsets[0]

    if len(offsets) == 1:
        return section_len - offsets[0]

    raise ValueError("Record offset tablosu bulunamadı.")


def looks_like_float(raw_int: int, float_value: float) -> bool:
    """
    PES gameplay değerleri için kaba sezgisel kontrol.
    Amaç kesin tip kararı vermek değil, şüpheli float alanları yakalamak.
    """
    if raw_int in (0, 1):
        return False

    if not (-10000.0 <= float_value <= 10000.0):
        return False

    # Çok küçük scientific değerler genelde int'in float gibi yanlış okunmasıdır.
    if abs(float_value) < 0.000001:
        return False

    # 0.5, 1.0, 1.5, 2.0, 30.0, 100.0 gibi okunabilir değerler.
    return True


def format_field(section_data: bytes, offset: int) -> str:
    raw_bytes = section_data[offset:offset + 4]
    int_value = read_i32(section_data, offset)
    uint_value = read_u32(section_data, offset)
    float_value = read_f32(section_data, offset)

    if looks_like_float(uint_value, float_value):
        return f"{float_value:g}f"

    return str(int_value)


def print_record_table(section_data: bytes, offsets: list[int], record_size: int, max_records: int | None):
    field_count = record_size // 4

    headers = ["Rec", "LocalOff"] + [f"F{i}" for i in range(field_count)]
    widths = [5, 10] + [12 for _ in range(field_count)]

    print(" ".join(h.ljust(w) for h, w in zip(headers, widths)))
    print("-" * (sum(widths) + len(widths)))

    for rec_index, rec_offset in enumerate(offsets):
        if max_records is not None and rec_index >= max_records:
            break

        values = []

        for field_index in range(field_count):
            value_offset = rec_offset + field_index * 4
            values.append(format_field(section_data, value_offset))

        row = [
            str(rec_index),
            f"0x{rec_offset:04X}",
            *values,
        ]

        print(" ".join(cell.ljust(w) for cell, w in zip(row, widths)))


def print_raw_detail(section_data: bytes, offsets: list[int], record_index: int, record_size: int):
    rec_offset = offsets[record_index]
    field_count = record_size // 4

    print()
    print("=" * 100)
    print(f"Raw detail for record {record_index}, local offset 0x{rec_offset:04X}")
    print("-" * 100)
    print(f"{'Field':<8} {'LocalOff':<10} {'Bytes':<14} {'int32':>12} {'uint32':>12} {'float32':>16}")
    print("-" * 100)

    for field_index in range(field_count):
        local_offset = rec_offset + field_index * 4
        chunk = section_data[local_offset:local_offset + 4]

        int_value = read_i32(section_data, local_offset)
        uint_value = read_u32(section_data, local_offset)
        float_value = read_f32(section_data, local_offset)

        print(
            f"F{field_index:<7} "
            f"0x{local_offset:04X}   "
            f"{chunk.hex(' ').upper():<14} "
            f"{int_value:>12} "
            f"{uint_value:>12} "
            f"{float_value:>16.8g}"
        )


def main():
    parser = argparse.ArgumentParser(
        description="PES dt18 section record table reader with int/float detection"
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
    record_size = infer_record_size(offsets, len(section_data))

    print(f"File          : {path.name}")
    print(f"Compressed    : {compressed}")
    print(f"Section offset: 0x{args.offset:08X}")
    print(f"Section length: {args.length}")
    print(f"Record count  : {len(offsets)}")
    print(f"Record size   : {record_size} bytes")
    print()

    print_record_table(
        section_data=section_data,
        offsets=offsets,
        record_size=record_size,
        max_records=args.records,
    )

    if args.detail_record is not None:
        if args.detail_record < 0 or args.detail_record >= len(offsets):
            raise ValueError("Geçersiz detail record index.")
        print_raw_detail(section_data, offsets, args.detail_record, record_size)


if __name__ == "__main__":
    main()