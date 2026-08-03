from openpod.editor import PresetEditor

preset = PresetEditor("Richie Sambora.pgp")

print("Preset :", preset.name)

print("Amp :", preset.amp.model)
print("Cab :", preset.cab.model)

print("High Cut :", preset.cab.high_cut)
print("Low Cut  :", preset.cab.low_cut)

preset.amp.drive = 0.74

preset.cab.high_cut = 7000
preset.cab.low_cut = 90

preset.save("ModernRock.pgp")

print()
print("Preset berhasil diubah.")
