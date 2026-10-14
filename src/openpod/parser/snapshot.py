"""Parse snapshot entries from a JSON preset's tone object."""

from collections.abc import Mapping

from openpod.editor.snapshot import Snapshot


class SnapshotParser:
    """Build four context-aware snapshot editors from the preset tone."""

    def __init__(self, tone: Mapping):
        self.tone = tone

    def parse(self) -> list[Snapshot]:
        return [
            Snapshot(
                self.tone[f"snapshot{index}"],
                tone=self.tone,
                key=f"snapshot{index}",
            )
            for index in range(4)
        ]
