# OpenPod

OpenPod is a Python SDK for reading and editing Line 6 POD Go preset (`.pgp`) files.

## Requirements

- Python 3.12 or newer

## Install for development

From the repository root, install OpenPod in editable mode:

```bash
python -m pip install -e .
```

## Edit a preset

```python
from openpod.editor import PresetEditor

preset = PresetEditor("input.pgp")

preset.name = "Soul Blues"
preset.amp.drive = 4.25
preset.cab.level = -3.5
preset.snapshots[1].name = "Lead"

# Save a copy, keeping the input file unchanged.
preset.save("soul-blues.pgp")
```

`preset.snapshots` contains the four snapshots in order. Assigning to
`preset.name` or a snapshot's `name` converts the value to a string. Calling
`preset.save()` without a filename writes changes back to the file that was
loaded.

## Work with blocks

The editor exposes typed `Amp` and `Cab` objects for their corresponding preset
slots. Other blocks use the generic `Block` API. All three types are available
from `openpod.editor`.

```python
from openpod.editor import Amp, Block, Cab, PresetEditor

preset = PresetEditor("input.pgp")
for block in preset.blocks:
    print(block.model, block.enabled)

amp = preset.find_model("HD2_AmpBrit2204")
assert isinstance(amp, Amp)

delay = preset.find_model("HD2_DelayElephantManStereo")
delay.parameter("Mix").value = 0.5
```

`find_model()` takes the exact model identifier stored in the preset and raises
`KeyError` if it is not found. A block's generic parameter API is available
through `parameters`, `get()`, `set()`, item access, and `parameter()`.

## Run tests

Install pytest and run the suite from the repository root:

```bash
python -m pip install pytest
python -m pytest
```
