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
preset.cab.level = -3.5
preset.snapshots[0].set_parameter(preset.amp, "Drive", 0.35)
preset.snapshots[1].set_parameter(preset.amp, "Drive", 0.65)
preset.snapshots[2].set_parameter(preset.amp, "Drive", 0.2)
preset.snapshots[3].set_parameter(preset.amp, "Drive", 0.5)
preset.snapshots[1].name = "Lead"
preset.snapshots[2].name = "Rhythm"
preset.snapshots[3].name = "Clean"

# Save a copy, keeping the input file unchanged.
preset.save("soul-blues.pgp")
```

`preset.snapshots` contains the four snapshots in order. The example assigns
and names every slot so all four snapshots are enabled in the output preset.
Assigning to `preset.name` or a snapshot's `name` converts the value to a
string. Calling
`preset.save()` without a filename writes changes back to the file that was
loaded. Setting a value such as `preset.amp.drive` changes the block's shared
base value. Use `snapshot.set_parameter(block, name, value)` to assign a
parameter to the Snapshots controller and give that snapshot its own value.
Block parameter values use the numeric scale stored in the preset (for example,
Amp Drive is typically between `0.0` and `1.0`).

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
