
from elftools.elf.elffile import ELFFile


def inspect_sections(file_path: str):
    results = []

    with open(file_path, "rb") as file:
        elf = ELFFile(file)

        for section in elf.iter_sections():
            data = section.data()

            results.append({
                "name": section.name,
                "type": section["sh_type"],
                "offset": hex(section["sh_offset"]),
                "size": section["sh_size"],
                "flags": hex(section["sh_flags"]),
                "preview": data[:64].hex(" ").upper()
            })

    return results


def read_section(file_path: str, section_name: str) -> dict:
    """
    Read the raw content of an ELF section.
    """

    with open(file_path, "rb") as file:
        elf = ELFFile(file)

        section = elf.get_section_by_name(section_name)

        if section is None:
            raise ValueError(
                f"Section not found: {section_name}"
            )

        data = section.data()

        return {
            "name": section.name,
            "offset": hex(section["sh_offset"]),
            "size": len(data),
            "hex": data.hex(" ").upper(),
            "ascii": "".join(
                chr(byte) if 32 <= byte <= 126 else "."
                for byte in data
            )
        }
