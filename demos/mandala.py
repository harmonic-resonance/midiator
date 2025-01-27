import harmonic_resonance.midiator as pm
import itertools as itertools
import random as random
from rich import print as log

PROJECT = "mandala"
title = "unfold from the center"
bpm = 53  # beats per minute
bpM = 4  # beats per Measure
root = pm.N.E3  # the root note of the key
key = "E"

part = pm.Part(PROJECT, title, bpm=bpm, root=root, key=key)
M = part.measure_ticks()

chords = pm.progressions.i_vi_ii_V(root)

choir = part.add_choir_swell()

for loop in range(8):
    part.set_marker(f"{loop}", 0)
    chord_name = chords[loop % len(chords)][0]
    chord = chords[loop % len(chords)][1]

    part.set_marker(f"{chord_name} - {chord}", 0)
    part.set_marker(f"", M)

    choir.set_notes(chord, M, offset=M / 4)
    choir.set_volume(32, 0)
    choir.ramp_volume_up(2 * M)
    choir.ramp_volume_down(2 * M)

part.save()
part.play()
part.convert()
