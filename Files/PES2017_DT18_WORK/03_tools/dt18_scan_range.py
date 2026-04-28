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


def scan_range(raw: bytes, start_offset: int, length: int, rows: int):
    section_data = raw[start_offset:start_offset + length]

    print("=" * 110)
    print(f"Range offset : 0x{start_offset:08X}")
    print(f"Range length : {length} bytes")
    print(f"Total rows   : {len(section_data) // 4}")
    print("-" * 110)
    print(f"{'LocalOff':<10} {'FileOff':<10} {'Bytes':<14} {'int32':>12} {'uint32':>12} {'float32':>16}")
    print("-" * 110)

    for index, local_offset in enumerate(range(0, len(section_data) - 3, 4)):
        if index >= rows:
            break

        chunk = section_data[local_offset:local_offset + 4]

        int_value = struct.unpack("<i", chunk)[0]
        uint_value = struct.unpack("<I", chunk)[0]
        float_value = struct.unpack("<f", chunk)[0]

        file_offset = start_offset + local_offset

        print(
            f"0x{local_offset:06X} "
            f"0x{file_offset:06X} "
            f"{chunk.hex(' ').upper():<14} "
            f"{int_value:>12} "
            f"{uint_value:>12} "
            f"{float_value:>16.8g}"
        )


def main():
    parser = argparse.ArgumentParser(
        description="PES 2017 dt18 raw range scanner"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Örn: constant_match.bin"
    )

    parser.add_argument(
        "--offset",
        required=True,
        type=parse_int,
        help="Başlangıç offset'i. Örn: 0x770"
    )

    parser.add_argument(
        "--length",
        required=True,
        type=parse_int,
        help="Okunacak byte uzunluğu. Örn: 1232"
    )

    parser.add_argument(
        "--rows",
        type=int,
        default=80,
        help="Gösterilecek satır sayısı"
    )

    args = parser.parse_args()

    path = BIN_DIR / args.file

    if not path.exists():
        raise FileNotFoundError(f"Dosya bulunamadı: {path}")

    data = path.read_bytes()
    raw, compressed = decompress_if_needed(data)

    print(f"File       : {path.name}")
    print(f"Compressed : {compressed}")
    print(f"Input size : {len(data)} bytes")
    print(f"Raw size   : {len(raw)} bytes")

    scan_range(
        raw=raw,
        start_offset=args.offset,
        length=args.length,
        rows=args.rows,
    )


if __name__ == "__main__":
    main()