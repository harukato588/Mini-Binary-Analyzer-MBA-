from elftools.elf.elffile import ELFFile


def check_nx(elf: ELFFile) -> str:
    for segment in elf.iter_segments():
        if segment["p_type"] == "PT_GNU_STACK":
            executable = bool(segment["p_flags"] & 0x1)
            return "NX Disabled" if executable else "Enabled"

    return "Unknown"


def check_pie(elf: ELFFile) -> str:
    elf_type = elf.header["e_type"]

    has_interpreter = any(
        segment["p_type"] == "PT_INTERP"
        for segment in elf.iter_segments()
    )

    if elf_type == "ET_EXEC":
        return "Disabled"

    if elf_type == "ET_DYN" and has_interpreter:
        return "Enabled"

    return "Unknown"


def check_relro(elf: ELFFile) -> str:
    has_relro = any(
        segment["p_type"] == "PT_GNU_RELRO"
        for segment in elf.iter_segments()
    )

    if not has_relro:
        return "No RELRO"

    dynamic_section = elf.get_section_by_name(".dynamic")
    if dynamic_section is None:
        return "Partial RELRO"

    bind_now = False

    for tag in dynamic_section.iter_tags():
        tag_name = tag.entry.d_tag

        if tag_name == "DT_BIND_NOW":
            bind_now = True
        elif tag_name == "DT_FLAGS":
            bind_now = bind_now or bool(tag.entry.d_val & 0x8)
        elif tag_name == "DT_FLAGS_1":
            bind_now = bind_now or bool(tag.entry.d_val & 0x1)

    return "Full RELRO" if bind_now else "Partial RELRO"


def check_stack_canary(elf: ELFFile) -> str:
    symbol_tables = [
        elf.get_section_by_name(".dynsym"),
        elf.get_section_by_name(".symtab"),
    ]
    has_symbol_table = False

    for table in symbol_tables:
        if table is None:
            continue

        has_symbol_table = True
        for symbol in table.iter_symbols():
            if symbol.name == "__stack_chk_fail":
                return "Detected"

    return "Not Detected" if has_symbol_table else "Unknown"


def analyze_security(file_path: str) -> dict[str, str]:
    with open(file_path, "rb") as file:
        elf = ELFFile(file)

        return {
            "NX": check_nx(elf),
            "PIE": check_pie(elf),
            "RELRO": check_relro(elf),
            "stack_canary": check_stack_canary(elf),
        }
