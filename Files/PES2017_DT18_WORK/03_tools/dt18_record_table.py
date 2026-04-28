from __future__ import annotations

import argparse
import struct
import zlib
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BIN_DIR = PROJECT_ROOT / "02_bins"


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

    return offsets


def infer_record_size(offsets: list[int], section_len: int) -> int:
    if len(offsets) >= 2:
        return offsets[1] - offsets[0]

    if len(offsets) == 1:
        return section_len - offsets[0]

    raise ValueError("Record offset tablosu bulunamadı.")


def print_record_table(
    section_data: bytes,
    offsets: list[int],
    record_size: int,
    max_records: int | None,
) -> None:
    field_count = record_size // 4

    headers = ["Rec", "LocalOff"] + [f"F{i}" for i in range(field_count)]
    widths = [5, 10] + [8 for _ in range(field_count)]

    print(" ".join(h.ljust(w) for h, w in zip(headers, widths)))
    print("-" * (sum(widths) + len(widths)))

    for rec_index, rec_offset in enumerate(offsets):
        if max_records is not None and rec_index >= max_records:
            break

        values = []

        for field_index in range(field_count):
            value_offset = rec_offset + field_index * 4
            value = read_i32(section_data, value_offset)
            values.append(value) # pyright: ignore[reportUnknownMemberType]

        row = [
            str(rec_index),
            f"0x{rec_offset:04X}",
            *[str(v) for v in values], # type: ignore
        ]

        print(" ".join(cell.ljust(w) for cell, w in zip(row, widths)))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="PES dt18 section record table reader"
    )

    parser.add_argument("--file", required=True)
    parser.add_argument("--offset", required=True, type=parse_int)
    parser.add_argument("--length", required=True, type=parse_int)
    parser.add_argument("--records", type=int, default=None)

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


if __name__ == "__main__":
    main()