from openpod.editor import PresetEditor
from openpod.parser.snapshot import SnapshotParser


def test_snapshot_parser_builds_four_contextual_snapshot_editors():
    preset = PresetEditor("Richie Sambora.pgp")
    tone = preset.data["data"]["tone"]

    snapshots = SnapshotParser(tone).parse()

    assert len(snapshots) == 4
    assert [snapshot.name for snapshot in snapshots] == [
        "SNAPSHOT 1",
        "SNAPSHOT 2",
        "SNAPSHOT 3",
        "SNAPSHOT 4",
    ]
    snapshots[3].name = "Lead"
    assert tone["snapshot3"]["@name"] == "Lead"
