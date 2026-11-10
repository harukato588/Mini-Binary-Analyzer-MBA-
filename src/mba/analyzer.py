from pathlib import Path
import re


def detect_format(file_path: str) -> dict[str, str | int]:
    """
    Detect binary file format using magic bytes.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if not path.is_file():
        raise ValueError("Input must be a file.")

    with path.open('rb') as file:
        header = file.read(64)

    if len(header) < 2:
        file_format = "Unknown"
    elif header.startswith(b'\x7fELF'):
        file_format = "ELF"
    elif header.startswith(b"MZ"):
        file_format = "PE (DOS/Windows Executable)"
    elif header.startswith(b"\x89PNG\r\n\x1a\n"):
        file_format = "PNG"
    elif header.startswith(b"%PDF"):
        file_format = "PDF"
    else:
        file_format = "Unknown"

    return {
        "filename": path.name,
        "file_size": path.stat().st_size,
        "format": file_format,
        "magic_bytes": header[:16].hex(" ").upper(),
    }


def extract_strings(file_path: str, min_length: int = 4) -> list[dict[str, str]]:
    """
    Extract printable ASCII strings from a binary file.
    Returns each string with its hexadecimal offset.
    """
    if min_length < 1:
        raise ValueError("min_length must be at least 1.")

    with open(file_path, "rb") as file:
        data = file.read()

    pattern = rb"[\x20-\x7E]{" + str(min_length).encode("ascii") + rb",}"

    results = []

    for match in re.finditer(pattern, data):
        results.append({
            "offset": hex(match.start()),
            "string": match.group().decode("ascii"),
        })

    return results
