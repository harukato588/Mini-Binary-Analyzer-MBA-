
from elftools.elf.elffile import ELFFile


def inspect_dependencies(file_path: str) -> list:
    results = []

    with open(file_path, "rb") as file:
        elf = ELFFile(file)

        dynamic_section = elf.get_section_by_name(".dynamic")

        if dynamic_section is None:
            return results

        for tag in dynamic_section.iter_tags():
            if tag.entry.d_tag == "DT_NEEDED":
                results.append({
                    "library": tag.needed
                })

    return results
