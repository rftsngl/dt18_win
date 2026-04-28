from __future__ import annotations

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
    """
    PES WESYS/zlib kontrolü.
    Header içinde 4-7 byte aralığında ESYS magic değeri beklenir.
    """
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

    names_blob = raw[head_len : head_len + idx_len]
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


def probe_file(path: Path):
    layout = LAYOUTS[path.name]

    data = path.read_bytes()
    raw, compressed = decompress_if_needed(data)

    sections = read_section_table(
        raw=raw,
        head_len=layout["head_len"],
        idx_len=layout["idx_len"],
    )

    print("=" * 80)
    print(f"File        : {path.name}")
    print(f"Type        : {layout['type']}")
    print(f"Input size  : {len(data)} bytes")
    print(f"Raw size    : {len(raw)} bytes")
    print(f"Compressed  : {compressed}")
    print(f"Sections    : {len(sections)}")
    print("-" * 80)

    for section in sections[:40]:
        print(
            f"{section['index']:02d} | "
            f"{section['name']:<32} | "
            f"offset=0x{section['offset']:08X} | "
            f"length={section['length']}"
        )

    print()


def main():
    for filename in LAYOUTS:
        path = BIN_DIR / filename

        if not path.exists():
            print(f"[MISSING] {path}")
            continue

        try:
            probe_file(path)
        except (KeyError, OSError, RuntimeError, struct.error) as exc:
            print("=" * 80)
            print(f"[ERROR] {path.name}")
            print(exc)
            print()


if __name__ == "__main__":
    main()
