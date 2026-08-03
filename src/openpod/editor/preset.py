import json
from pathlib import Path


class PresetEditor:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.data = json.loads(self.filename.read_text())

    def save(self, filename):
        Path(filename).write_text(
            json.dumps(self.data, indent=2)
        )
        