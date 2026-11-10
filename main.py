
import argparse

from src.mba.cli import (
    run_cli,
    run_strings,
    run_sections,
    run_symbols,
    run_dependencies
)


def main():
    parser = argparse.ArgumentParser(
        description="Mini Binary Analyzer"
    )

    parser.add_argument(
        "file",
        help="Path to the binary file"
    )

    parser.add_argument(
        "--strings",
        action="store_true",
        help="Extract printable ASCII strings"
    )

    parser.add_argument(
        "--sections",
        action="store_true",
        help="Inspect ELF sections"
    )

    parser.add_argument(
        "--symbols",
        action="store_true",
        help="Inspect ELF symbols"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all available analysis modules"
    )

    parser.add_argument(
        "--dependencies",
        action="store_true",
        help="Inspect ELF dynamic dependencies"
    )

    args = parser.parse_args()

    if args.all:
        run_cli(args.file)
        run_strings(args.file)
        run_sections(args.file)
        run_symbols(args.file)
        run_dependencies(args.file)

    elif args.sections:
        run_sections(args.file)

    elif args.symbols:
        run_symbols(args.file)

    elif args.strings:
        run_strings(args.file)

    elif args.dependencies:
        run_dependencies(args.file)

    else:
        run_cli(args.file)


if __name__ == "__main__":
    main()
