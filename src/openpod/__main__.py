import argparse
import json
from pathlib import Path

from openpod import __version__
from openpod.editor import PresetEditor


def _inspect(filename):
    preset = PresetEditor(filename)
    print(f"Preset: {preset.name}")
    print("Blocks:")
    for block in preset.blocks:
        state = "enabled" if block.enabled else "bypassed"
        print(f"  {block.model or 'Unknown model'} ({state})")
    print("Snapshots:")
    for index, snapshot in enumerate(preset.snapshots, start=1):
        print(f"  {index}. {snapshot.name}")


def main():
    parser = argparse.ArgumentParser(
        prog="openpod",
        description="Open source SDK for Line 6 POD Go preset files.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"OpenPod {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command")

    inspect_parser = subparsers.add_parser(
        "inspect",
        help="Inspect a POD Go preset file.",
    )
    inspect_parser.add_argument("filename", nargs="?")

    args = parser.parse_args()

    if args.command == "inspect":
        if not args.filename:
            parser.error("inspect membutuhkan nama file.")
        try:
            _inspect(args.filename)
        except FileNotFoundError:
            parser.error(f"file tidak ditemukan: {args.filename}")
        except (json.JSONDecodeError, UnicodeDecodeError):
            parser.error(f"JSON preset tidak valid: {args.filename}")
        except (KeyError, TypeError) as error:
            parser.error(f"struktur preset tidak valid: {error}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
