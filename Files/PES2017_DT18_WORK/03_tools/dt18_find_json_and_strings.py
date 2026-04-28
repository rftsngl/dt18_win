import csv
import json
import re
import sys
import zlib
from pathlib import Path
from typing import Optional, Any


BASE_DIR = Path(r"C:\Games\PesModlama\Files\PES2017_DT18_WORK")
EXTRACTED_DIR = BASE_DIR / "01_extracted"
BIN_DIR = BASE_DIR / "02_bins"
OUT_DIR = BASE_DIR / r"04_tests\analysis\json_string_scan"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_JSON = OUT_DIR / "json_scan_report.csv"
OUT_STRINGS = OUT_DIR / "string_scan_report.csv"
OUT_COMPRESSED = OUT_DIR / "compressed_object_report.csv"


def configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")  # type: ignore


TEXT_EXTENSIONS = {
    ".json",
    ".txt",
    ".xml",
    ".ini",
    ".lua",
    ".csv",
}


KEYWORDS = [
    "shoot",
    "shot",
    "pass",
    "ground",
    "fly",
    "through",
    "assist",
    "defence",
    "defense",
    "mark",
    "cover",
    "support",
    "space",
    "run",
    "dribble",
    "contact",
    "tackle",
    "sliding",
    "keeper",
    "gk",
    "cpu",
    "level",
    "ball",
    "power",
    "speed",
    "gage",
    "gauge",
    "accuracy",
    "curve",
    "distance",
    "angle",
]


def has_wesys_header(data: bytes) -> bool:
    return len(data) >= 16 and data[4:8] == b"ESYS"


def try_wesys_decompress(data: bytes) -> Optional[bytes]:
    if not has_wesys_header(data):
        return None

    try:
        return zlib.decompress(data[16:])
    except Exception:
        return None


def try_raw_zlib_at_offsets(data: bytes, max_hits: int = 20) -> list[tuple[int, bytes]]:
    """
    Raw zlib stream ihtimallerini arar.
    Zlib genelde 78 01 / 78 9C / 78 DA ile başlar.
    """
    hits = []

    signatures = [b"\x78\x01", b"\x78\x9C", b"\x78\xDA"]

    for sig in signatures:
        start = 0

        while True:
            idx = data.find(sig, start)
            if idx == -1:
                break

            try:
                obj = zlib.decompressobj()
                decompressed = obj.decompress(data[idx:])
                decompressed += obj.flush()

                if decompressed:
                    hits.append((idx, decompressed[:200000]))

                    if len(hits) >= max_hits:
                        return hits

            except Exception:
                pass

            start = idx + 1

    return hits


def decode_text(data: bytes) -> tuple[str, str]:
    for enc in ("utf-8", "utf-16le", "latin-1"):
        try:
            text = data.decode(enc)
            return text, enc
        except Exception:
            continue

    return "", ""


def looks_like_json_text(text: str) -> bool:
    stripped = text.strip()
    return stripped.startswith("{") or stripped.startswith("[")


def try_parse_json_text(text: str) -> Any:
    try:
        return json.loads(text)
    except Exception:
        return None


def extract_json_like_blocks(text: str, max_blocks: int = 50) -> list[str]:
    """
    Basit JSON-like blok arayıcı.
    Kesin parser değil. Ön tarama için.
    """
    blocks = []

    candidates = re.finditer(r"[\{\[]", text)

    for match in candidates:
        start = match.start()
        opener = text[start]
        closer = "}" if opener == "{" else "]"

        end = text.find(closer, start + 1)
        if end == -1:
            continue

        snippet = text[start:end + 1]

        if len(snippet) < 4:
            continue

        parsed = try_parse_json_text(snippet)
        if parsed is not None:
            blocks.append(snippet[:1000])

            if len(blocks) >= max_blocks:
                break

    return blocks


def extract_ascii_strings(data: bytes, min_len: int = 4) -> list[str]:
    pattern = rb"[ -~]{" + str(min_len).encode() + rb",}"
    return [m.group().decode("ascii", errors="replace") for m in re.finditer(pattern, data)]


def keyword_hits(strings: list[str]) -> list[str]:
    hits = []

    for s in strings:
        lower = s.lower()

        if any(k in lower for k in KEYWORDS):
            hits.append(s)

    return hits


def walk_files() -> list[Path]:
    paths: list[Path] = []

    if EXTRACTED_DIR.exists():
        paths.extend([p for p in EXTRACTED_DIR.rglob("*") if p.is_file()])

    if BIN_DIR.exists():
        paths.extend([p for p in BIN_DIR.rglob("*") if p.is_file()])

    # Duplicate path temizliği
    seen: set[str] = set()
    unique: list[Path] = []

    for p in paths:
        key = str(p.resolve()).lower()
        if key not in seen:
            unique.append(p)
            seen.add(key)

    return unique


def relative_path(path: Path) -> str:
    try:
        return str(path.relative_to(BASE_DIR))
    except Exception:
        return str(path)


def main() -> None:
    files = walk_files()

    json_rows = []
    string_rows = []
    compressed_rows = []

    for path in files:
        try:
            data = path.read_bytes()
        except Exception:
            continue

        rel = relative_path(path)
        suffix = path.suffix.lower()

        candidates = []

        # 1) Dosyanın kendisi
        candidates.append(("raw_file", 0, data))

        # 2) WESYS açılmış hali
        wesys = try_wesys_decompress(data)
        if wesys is not None:
            candidates.append(("wesys_zlib", 16, wesys))
            compressed_rows.append({
                "file": rel,
                "compression_type": "WESYS/zlib",
                "offset_hex": "0x00000000",
                "compressed_size": len(data),
                "decompressed_size": len(wesys),
                "starts_with": wesys[:32].hex(" ").upper(),
            })

        # 3) Raw zlib streamler
        raw_zlib_hits = try_raw_zlib_at_offsets(data)
        for offset, decompressed in raw_zlib_hits:
            candidates.append(("raw_zlib_stream", offset, decompressed))
            compressed_rows.append({
                "file": rel,
                "compression_type": "raw_zlib_stream",
                "offset_hex": f"0x{offset:08X}",
                "compressed_size": "",
                "decompressed_size": len(decompressed),
                "starts_with": decompressed[:32].hex(" ").upper(),
            })

        for source_type, source_offset, blob in candidates:
            text, encoding = decode_text(blob)

            # JSON direkt parse
            if text and looks_like_json_text(text):
                parsed = try_parse_json_text(text)

                if parsed is not None:
                    keys_preview = ""

                    if isinstance(parsed, dict):
                        keys_preview = ", ".join(list(parsed.keys())[:30])
                    elif isinstance(parsed, list):
                        keys_preview = f"list_len={len(parsed)}"

                    json_rows.append({
                        "file": rel,
                        "source_type": source_type,
                        "source_offset_hex": f"0x{source_offset:08X}",
                        "encoding": encoding,
                        "json_type": type(parsed).__name__,
                        "keys_preview": keys_preview,
                        "text_preview": text[:500].replace("\n", "\\n"),
                    })

            # JSON-like blok arama
            if text:
                blocks = extract_json_like_blocks(text)

                for block in blocks[:10]:
                    json_rows.append({
                        "file": rel,
                        "source_type": source_type + "_embedded_json_block",
                        "source_offset_hex": f"0x{source_offset:08X}",
                        "encoding": encoding,
                        "json_type": "embedded_block",
                        "keys_preview": "",
                        "text_preview": block[:500].replace("\n", "\\n"),
                    })

            # Strings
            strings = extract_ascii_strings(blob)
            hits = keyword_hits(strings)

            if strings or hits:
                string_rows.append({
                    "file": rel,
                    "source_type": source_type,
                    "source_offset_hex": f"0x{source_offset:08X}",
                    "string_count": len(strings),
                    "keyword_hit_count": len(hits),
                    "keyword_hits_preview": " || ".join(hits[:50]),
                    "strings_preview": " || ".join(strings[:50]),
                })

    with OUT_JSON.open("w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "file",
            "source_type",
            "source_offset_hex",
            "encoding",
            "json_type",
            "keys_preview",
            "text_preview",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(json_rows)

    with OUT_STRINGS.open("w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "file",
            "source_type",
            "source_offset_hex",
            "string_count",
            "keyword_hit_count",
            "keyword_hits_preview",
            "strings_preview",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(string_rows)

    with OUT_COMPRESSED.open("w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "file",
            "compression_type",
            "offset_hex",
            "compressed_size",
            "decompressed_size",
            "starts_with",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(compressed_rows)

    print("JSON/string/compression scan tamamlandı.")
    print(f"Scanned files      : {len(files)}")
    print(f"JSON hits          : {len(json_rows)}")
    print(f"String rows        : {len(string_rows)}")
    print(f"Compressed objects : {len(compressed_rows)}")
    print()
    print(f"JSON report        : {OUT_JSON}")
    print(f"String report      : {OUT_STRINGS}")
    print(f"Compressed report  : {OUT_COMPRESSED}")

    print()
    print("İlk JSON hitleri:")
    for row in json_rows[:20]:
        print(
            f"{row['file']} | {row['source_type']} | "
            f"{row['json_type']} | {row['keys_preview']} | "
            f"{row['text_preview'][:120]}"
        )

    print()
    print("Keyword string hitleri:")
    for row in string_rows[:20]:
        if int(row["keyword_hit_count"]) > 0:
            print(
                f"{row['file']} | {row['source_type']} | "
                f"hits={row['keyword_hit_count']} | "
                f"{row['keyword_hits_preview'][:200]}"
            )


if __name__ == "__main__":
    configure_stdout()
    main()
