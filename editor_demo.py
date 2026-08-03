from openpod.editor import PresetEditor

preset = PresetEditor("Richie Sambora.pgp")

print(preset.name)

preset.save("ModernRock.pgp")

print("Selesai.")
