from pathlib import Path


class Preset:
    """Represents a POD Go preset."""

    def __init__(self, data: bytes):
        self._data = data

    @classmethod
    def load(cls, filename: str) -> "Preset":
        """Load a preset from a .pgp file."""
        data = Path(filename).read_bytes()
        return cls(data)

    @property
    def size(self) -> int:
        return len(self._data)

    @property
    def raw(self) -> bytes:
        return self._data

    def summary(self) -> str:
        return (
            f"Preset\n"
            f"Size : {self.size} bytes"
        )
    