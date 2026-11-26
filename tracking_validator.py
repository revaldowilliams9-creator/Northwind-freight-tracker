import re
import zlib
from pathlib import Path

# Pre-compile the regex pattern once for better performance on large batches
TRACKING_PATTERN = re.compile(r"[A-Z]{3}\d{4}")


def clean_code(code: str) -> str:
    """Removes all whitespace and converts the tracking code to uppercase."""
    return "".join(code.split()).upper()


def is_valid_code(code: str) -> bool:
    """Checks if a cleaned code matches 3 uppercase letters followed by 4 digits."""
    return bool(TRACKING_PATTERN.fullmatch(code))


def load_codes_from_file(filepath: str) -> list[str]:
    """Reads raw tracking codes line-by-line from a text file, with fallback sample data."""
    path = Path(filepath)
    if not path.exists():
        print(f"Notice: '{filepath}' not found. Running with built-in sample data.\n")
        return ["abc 1234", "XYZ9999", "12ab567", "  def-5678 ", "GHI 0001"]

    with path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def archive_codes(codes: list[str], archive_path: str = "archived_codes.bin") -> None:
    """Compresses and saves a list of valid tracking codes to a binary file."""
    if not codes:
        print("No valid codes to archive.")
        return

    payload = ", ".join(codes)
    compressed = zlib.compress(payload.encode("utf-8"))

    with open(archive_path, "wb") as f:
        f.write(compressed)

    print(f"Successfully archived {len(codes)} valid codes to '{archive_path}'.")


def read_archive(archive_path: str = "archived_codes.bin") -> list[str]:
    """Reads and decompresses tracking codes back from the binary archive."""
    try:
        with open(archive_path, "rb") as f:
            compressed_data = f.read()
        decompressed = zlib.decompress(compressed_data).decode("utf-8")
        return decompressed.split(", ")
    except FileNotFoundError:
        print(f"Error: Archive '{archive_path}' does not exist.")
        return []


def log_rejected_codes(codes: list[str], log_path: str = "rejected_codes.log") -> None:
    """Saves invalid codes to a separate log file for auditing."""
    if not codes:
        return

    with open(log_path, "w", encoding="utf-8") as f:
        for code in codes:
            f.write(f"{code}\n")

    print(f"Logged {len(codes)} invalid codes to '{log_path}'.")


def main() -> None:
    input_file = "incoming_codes.txt"
    archive_file = "archived_codes.bin"
    rejected_file = "rejected_codes.log"

    raw_codes = load_codes_from_file(input_file)

    valid_codes = []
    invalid_codes = []

    # 1. Clean and validate
    for raw in raw_codes:
        cleaned = clean_code(raw)
        if is_valid_code(cleaned):
            valid_codes.append(cleaned)
            print(f"[VALID]   {cleaned}")
        else:
            invalid_codes.append(cleaned)
            print(f"[INVALID] {cleaned}")

    print("-" * 40)

    # 2. Archive valid codes and log rejected ones
    archive_codes(valid_codes, archive_file)
    log_rejected_codes(invalid_codes, rejected_file)

    # 3. Verify archive integrity by reading it back
    restored = read_archive(archive_file)
    print(f"Verified archive contents: {restored}")


if __name__ == "__main__":
    main()
