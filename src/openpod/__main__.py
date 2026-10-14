import argparse
import json

from openpod import __version__
from openpod.editor import PresetEditor


def _load_preset(filename, parser):
    try:
        return PresetEditor(filename)
    except FileNotFoundError:
        parser.error(f"file tidak ditemukan: {filename}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        parser.error(f"JSON preset tidak valid: {filename}")
    except (KeyError, TypeError) as error:
        parser.error(f"struktur preset tidak valid: {error}")


def _inspect(filename, parser):
    preset = _load_preset(filename, parser)
    print(f"Preset: {preset.name}")
    print("Blocks:")
    for block in preset.blocks:
        state = "enabled" if block.enabled else "bypassed"
        print(f"  {block.model or 'Unknown model'} ({state})")
    print("Snapshots:")
    for index, snapshot in enumerate(preset.snapshots, start=1):
        print(f"  {index}. {snapshot.name}")


def _export_json(filename, output, parser):
    preset = _load_preset(filename, parser)
    try:
        preset.save(output)
    except OSError as error:
        parser.error(f"gagal menulis file JSON: {error}")


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

    export_parser = subparsers.add_parser(
        "export-json",
        help="Export a preset as JSON.",
    )
    export_parser.add_argument("filename")
    export_parser.add_argument("output")

    args = parser.parse_args()

    if args.command == "inspect":
        if not args.filename:
            parser.error("inspect membutuhkan nama file.")
        _inspect(args.filename, parser)
        return

    if args.command == "export-json":
        _export_json(args.filename, args.output, parser)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
