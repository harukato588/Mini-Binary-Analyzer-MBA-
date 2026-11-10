
from rich.console import Console
from rich.table import Table
from .dependency_inspector import inspect_dependencies
from .symbol_inspector import inspect_symbols
from .analyzer import detect_format, extract_strings
from .elf_inspector import inspect_sections

console = Console()


def run_cli(file_path: str) -> None:
    try:
        result = detect_format(file_path)

        table = Table(title="Mini Binary Analyzer")

        table.add_column("Property", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Filename", result["filename"])
        table.add_row("File Size", f'{result["file_size"]} bytes')
        table.add_row("Format", result["format"])
        table.add_row("Magic Bytes", result["magic_bytes"])

        console.print(table)

    except (FileNotFoundError, ValueError, OSError) as error:
        console.print(f"[bold red]Error:[/] {error}")


def run_strings(file_path: str) -> None:
    try:
        results = extract_strings(file_path)

        table = Table(title="STRINGS EXTRACTOR")

        table.add_column("Offset", style="cyan")
        table.add_column("Extracted String", style="green")

        for item in results:
            table.add_row(item["offset"], item["string"])

        console.print(table)
        console.print(f"\nTotal strings found: {len(results)}")

    except (FileNotFoundError, ValueError, OSError) as error:
        console.print(f"[bold red]Error:[/] {error}")


def run_sections(file_path: str) -> None:
    try:
        results = inspect_sections(file_path)

        table = Table(title="ELF SECTION INSPECTOR")

        table.add_column("Name", style="cyan")
        table.add_column("Type", style="yellow")
        table.add_column("Offset", style="green")
        table.add_column("Size", justify="right")
        table.add_column("Flags")
        table.add_column("Preview (Hex)")

        for item in results:
            table.add_row(
                item["name"] or "<unnamed>",
                item["type"],
                item["offset"],
                str(item["size"]),
                item["flags"],
                item["preview"]
            )

        console.print(table)
        console.print(f"\nTotal sections found: {len(results)}")

    except (FileNotFoundError, ValueError, OSError) as error:
        console.print(f"[bold red]Error:[/] {error}")


def run_symbols(file_path: str) -> None:
    try:
        results = inspect_symbols(file_path)

        table = Table(title="ELF SYMBOL INSPECTOR")

        table.add_column("Name", style="cyan")
        table.add_column("Type", style="yellow")
        table.add_column("Binding", style="green")
        table.add_column("Status", style="magenta")

        for item in results:
            table.add_row(
                item["name"],
                item["type"],
                item["binding"],
                item["status"]
            )

        console.print(table)
        console.print(f"\nTotal symbols found: {len(results)}")

    except (FileNotFoundError, ValueError, OSError) as error:
        console.print(f"[bold red]Error:[/] {error}")


def run_dependencies(file_path: str) -> None:
    try:
        results = inspect_dependencies(file_path)

        table = Table(title="ELF DEPENDENCY INSPECTOR")

        table.add_column("No.", style="cyan")
        table.add_column("Library", style="green")

        for index, item in enumerate(results, start=1):
            table.add_row(
                str(index),
                item["library"]
            )

        console.print(table)
        console.print(
            f"\nTotal dependencies found: {len(results)}"
        )

    except (FileNotFoundError, ValueError, OSError) as error:
        console.print(f"[bold red]Error:[/] {error}")
