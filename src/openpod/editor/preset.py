import json
import tempfile
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

    @name.setter
    def name(self, value):
        self.data["data"]["meta"]["name"] = str(value)

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
        from openpod.parser.block import BlockParser

        return BlockParser(dsp0).parse()

    def find_model(self, model):
        for block in self.blocks:
            if block.model == model:
                return block

        raise KeyError(model)

    @property
    def snapshots(self):
        tone = self.data["data"]["tone"]
        from openpod.parser.snapshot import SnapshotParser

        return SnapshotParser(tone).parse()

    def save(self, filename=None):
        target = self.filename if filename is None else Path(filename)
        temp_path = None

        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=target.parent,
                prefix=f".{target.name}.",
                suffix=".tmp",
                delete=False,
            ) as temp_file:
                temp_path = Path(temp_file.name)
                json.dump(self.data, temp_file, indent=1)
                temp_file.flush()

            temp_path.replace(target)
        finally:
            if temp_path is not None:
                temp_path.unlink(missing_ok=True)
