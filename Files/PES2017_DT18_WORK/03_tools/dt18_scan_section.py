from __future__ import annotations

import argparse
import math
import struct
import zlib
from pathlib import Path
from typing import TypedDict


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BIN_DIR = PROJECT_ROOT / "02_bins"


class Layout(TypedDict):
    type: str
    head_len: int
    idx_len: int


class SectionInfo(TypedDict):
    index: int
    name: str
    offset: int
    length: int | None


LAYOUTS: dict[str, Layout] = {
    "constant_match.bin": {
        "type": "match",
        "head_len": 284,
        "idx_len": 356,
    },
    "constant_player.bin": {
        "type": "player",
        "head_len": 416,
        "idx_len": 432,
    },
    "constant_team.bin": {
        "type": "team",
        "head_len": 200,
        "idx_len": 216,
    },
}


def has_wesys_header(data: bytes) -> bool:
    return len(data) >= 16 and data[4:8] == b"ESYS"


def decompress_if_needed(data: bytes) -> tuple[bytes, bool]:
    if not has_wesys_header(data):
        return data, False

    try:
        return zlib.decompress(data[16:]), True
    except zlib.error as exc:
        raise RuntimeError(f"WESYS header var ama zlib açma başarısız: {exc}") from exc


def read_section_table(raw: bytes, head_len: int, idx_len: int) -> list[SectionInfo]:
    section_offsets: list[int] = []
    section_lengths_raw: list[int] = []

    record_count = max(0, math.ceil(head_len / 12) - 1)

    cursor = 0
    for _ in range(record_count):
        section_len, _reserved, section_offset = struct.unpack_from("<3i", raw, cursor)
        section_lengths_raw.append(section_len)
        section_offsets.append(section_offset)
        cursor += 12

    section_lengths: list[int] = section_lengths_raw[1:]

    if section_offsets:
        section_lengths.append(len(raw) - section_offsets[-1])

    names_blob = raw[head_len:head_len + idx_len]
    section_names: list[str] = [
        item.decode("utf-8", errors="replace")
        for item in names_blob.split(b"\x00")
        if item
    ]

    sections: list[SectionInfo] = []

    for index, name in enumerate(section_names):
        if index >= len(section_offsets):
            break

        sections.append(
            {
                "index": index,
                "name": name,
                "offset": section_offsets[index],
                "length": (
                    section_lengths[index] if index < len(section_lengths) else None
                ),
            }
        )

    return sections


def load_bin(filename: str) -> tuple[Path, bytes, bool, list[SectionInfo]]:
    if filename not in LAYOUTS:
        raise ValueError(f"Bilinmeyen dosya: {filename}")

    path = BIN_DIR / filename

    if not path.exists():
        raise FileNotFoundError(f"Dosya bulunamadı: {path}")

    layout = LAYOUTS[filename]
    data = path.read_bytes()
    raw, compressed = decompress_if_needed(data)

    sections = read_section_table(
        raw=raw,
        head_len=layout["head_len"],
        idx_len=layout["idx_len"],
    )

    return path, raw, compressed, sections


def find_section(sections: list[SectionInfo], section_name: str) -> SectionInfo:
    target_name = section_name.lower()

    for section in sections:
        if section["name"].lower() == target_name:
            return section

    available = ", ".join(section["name"] for section in sections)
    raise ValueError(f"Section bulunamadı: {section_name}\nMevcut sectionlar: {available}")


def scan_section(raw: bytes, section: SectionInfo, max_rows: int | None = None) -> None:
    offset = section["offset"]
    length = section["length"]

    if length is None:
        raise ValueError(f"Section length bulunamadı: {section['name']}")

    section_data = raw[offset:offset + length]

    print("=" * 100)
    print(f"Section      : {section['name']}")
    print(f"File offset  : 0x{offset:08X}")
    print(f"Length       : {length} bytes")
    print(f"Rows         : {len(section_data) // 4}")
    print("-" * 100)
    print(f"{'LocalOff':<10} {'FileOff':<10} {'Bytes':<14} {'int32':>12} {'uint32':>12} {'float32':>16}")
    print("-" * 100)

    row_count = 0

    for local_offset in range(0, len(section_data) - 3, 4):
        if max_rows is not None and row_count >= max_rows:
            break

        chunk = section_data[local_offset:local_offset + 4]

        int_value = struct.unpack("<i", chunk)[0]
        uint_value = struct.unpack("<I", chunk)[0]
        float_value = struct.unpack("<f", chunk)[0]

        file_offset = offset + local_offset

        print(
            f"0x{local_offset:06X} "
            f"0x{file_offset:06X} "
            f"{chunk.hex(' ').upper():<14} "
            f"{int_value:>12} "
            f"{uint_value:>12} "
            f"{float_value:>16.8g}"
        )

        row_count += 1


def main():
    parser = argparse.ArgumentParser(
        description="PES 2017 dt18 constant_*.bin section scanner"
    )

    parser.add_argument(
        "--file",
        required=True,
        choices=sorted(LAYOUTS),
        help="Taranacak .bin dosyası"
    )

    parser.add_argument(
        "--section",
        required=True,
        help="Taranacak section adı, örn: cpuLevel.o, shoot.o, defence.o"
    )

    parser.add_argument(
        "--rows",
        type=int,
        default=80,
        help="Gösterilecek maksimum satır sayısı"
    )

    args = parser.parse_args()

    path, raw, compressed, sections = load_bin(args.file)
    section = find_section(sections, args.section)

    print(f"File         : {path.name}")
    print(f"Compressed   : {compressed}")
    print(f"Raw size     : {len(raw)} bytes")

    scan_section(raw, section, max_rows=args.rows)


if __name__ == "__main__":
    main()