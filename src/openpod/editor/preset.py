from .amp import Amp
from .cab import Cab
from .snapshot import Snapshot
from .block import Block
import json
from pathlib import Path

from .amp import Amp
from .cab import Cab
from .snapshot import Snapshot


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

    @property
    def blocks(self):
        dsp0 = self.data["data"]["tone"]["dsp0"]

        return [
            Block(block)
            for key, block in dsp0.items()
            if key.startswith("block")
        ]
    @property
    def snapshots(self):
        tone = self.data["data"]["tone"]

        return [
            Snapshot(tone["snapshot0"]),
            Snapshot(tone["snapshot1"]),
            Snapshot(tone["snapshot2"]),
            Snapshot(tone["snapshot3"]),
        ]

    def save(self, filename):
        Path(filename).write_text(
            json.dumps(
                self.data,
                indent=1
            )
        )
