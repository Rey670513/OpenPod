import argparse

from openpod import __version__


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
        print(f"Inspecting: {args.filename}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
    