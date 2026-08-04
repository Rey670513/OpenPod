from openpod.editor import PresetEditor

preset = PresetEditor("Richie Sambora.pgp")

print("== Sebelum ==")
print("Preset :", preset.name)
print("Drive  :", preset.amp.drive)
print("HighCut:", preset.cab.high_cut)

# Ubah parameter
preset.snapshots[0].name = "Crystal Clean"
preset.snapshots[1].name = "Warm Crunch"
preset.snapshots[2].name = "Arena Rhythm"
preset.snapshots[3].name = "Arena Lead"

preset.amp.drive = 0.74
preset.cab.high_cut = 7000

preset.save("ModernRock.pgp")

print("\n== Sesudah ==")
print("Drive  :", preset.amp.drive)
print("HighCut:", preset.cab.high_cut)
print("File ModernRock.pgp berhasil dibuat.")
