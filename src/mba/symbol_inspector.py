
from elftools.elf.elffile import ELFFile


def inspect_symbols(file_path: str) -> list:
    results = []

    with open(file_path, "rb") as file:
        elf = ELFFile(file)

        symbol_table = elf.get_section_by_name(".dynsym")

        if symbol_table is None:
            return results

        for symbol in symbol_table.iter_symbols():

            name = symbol.name

            if not name:
                continue

            symbol_type = symbol["st_info"]["type"]
            binding = symbol["st_info"]["bind"]
            section_index = symbol["st_shndx"]

            if section_index == "SHN_UNDEF":
                status = "IMPORTED"
            else:
                status = "DEFINED"

            results.append({
                "name": name,
                "type": symbol_type,
                "binding": binding,
                "status": status
            })

    return results
