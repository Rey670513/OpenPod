from pathlib import Path

from openpod.parser.preset import Preset


def test_load_preset(tmp_path: Path):
    sample = tmp_path / "sample.pgp"
    sample.write_bytes(b"OpenPod")

    preset = Preset.load(str(sample))

    assert preset.size == 7
    assert preset.raw == b"OpenPod"
    