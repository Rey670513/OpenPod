"""
Binary reading utilities for OpenPod.
"""

from __future__ import annotations

from io import BytesIO
import struct


class BinaryReader:
    """Little-endian binary reader."""

    def __init__(self, data: bytes):
        self._stream = BytesIO(data)

    def tell(self) -> int:
        return self._stream.tell()

    def seek(self, offset: int) -> None:
        self._stream.seek(offset)

    def skip(self, length: int) -> None:
        self._stream.seek(length, 1)

    def remaining(self) -> int:
        current = self.tell()
        self._stream.seek(0, 2)
        end = self.tell()
        self.seek(current)
        return end - current

    def read_bytes(self, size: int) -> bytes:
        data = self._stream.read(size)

        if len(data) != size:
            raise EOFError("Unexpected end of file")

        return data

    def read_u8(self) -> int:
        return struct.unpack("<B", self.read_bytes(1))[0]

    def read_u16(self) -> int:
        return struct.unpack("<H", self.read_bytes(2))[0]

    def read_u32(self) -> int:
        return struct.unpack("<I", self.read_bytes(4))[0]

    def read_i32(self) -> int:
        return struct.unpack("<i", self.read_bytes(4))[0]

    def read_float(self) -> float:
        return struct.unpack("<f", self.read_bytes(4))[0]

    def read_string(self, size: int, encoding: str = "utf-8") -> str:
        raw = self.read_bytes(size)
        return raw.split(b"\x00", 1)[0].decode(encoding)

    def peek(self, size: int) -> bytes:
        pos = self.tell()
        data = self.read_bytes(size)
        self.seek(pos)
        return data
    