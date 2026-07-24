from typing import Iterable


def hexdump(data: bytes, width: int = 16) -> str:
    """Return a formatted hexadecimal dump."""

    lines = []

    for offset in range(0, len(data), width):
        chunk = data[offset : offset + width]

        hex_part = " ".join(f"{b:02X}" for b in chunk)

        ascii_part = "".join(
            chr(b) if 32 <= b <= 126 else "."
            for b in chunk
        )

        lines.append(
            f"{offset:08X}  {hex_part:<{width*3}} {ascii_part}"
        )

    return "\n".join(lines)
