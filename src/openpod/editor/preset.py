import json
from pathlib import Path

from .amp import Amp
from .cab import Cab


class PresetEditor:
    """
    Editor for POD Go preset (.pgp) files.
    """

    def __init__(self, filename):
        self.filename = Path(filename)
        self.data = json.loads(self.filename.read_text())

    @property
    def name(self):
        return self.data["data"]["meta"]["name"]

    @property
    def amp(self):
        return Amp(
            self.data["data"]["tone"]["dsp0"]["block3"]
        )

    @property
    def cab(self):
        return Cab(
            self.data["data"]["tone"]["dsp0"]["block4"]
        )

    def save(self, filename):
        Path(filename).write_text(
            json.dumps(
                self.data,
                indent=1
            )
        )
