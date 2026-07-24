from pathlib import Path


class BinaryReader:
    """Simple binary file reader."""

    def __init__(self, filename: str):
        self.path = Path(filename)

    def read(self) -> bytes:
        return self.path.read_bytes()

    def size(self) -> int:
        return self.path.stat().st_size
