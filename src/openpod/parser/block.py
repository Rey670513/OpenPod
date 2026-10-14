"""Build typed block editors from a JSON preset's DSP block mapping."""

from collections.abc import Mapping

from openpod.editor.amp import Amp
from openpod.editor.block import Block
from openpod.editor.cab import Cab


class BlockParser:
    """Map DSP block slots to the corresponding editor types."""

    def __init__(self, dsp_blocks: Mapping):
        self.dsp_blocks = dsp_blocks

    def parse(self) -> list[Block]:
        parsed_blocks = []
        for key, block_data in self.dsp_blocks.items():
            if not key.startswith("block"):
                continue
            block_type = Amp if key == "block3" else Cab if key == "block4" else Block
            parsed_blocks.append(block_type(block_data))
        return parsed_blocks
