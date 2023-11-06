import phimidi as pm
import math as math
import subprocess as subprocess

root = pm.N.C3
octaves = 3
scale_type = pm.S.pentatonic_major
tempo = int(pm.bpm2tempo(120))
M = 1920

scale = pm.build_scale(
    root=root, 
    scale_type=scale_type, 
    octaves=octaves)

PROJECT = 'phi-midi'
NAME = 'comp1'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

mf = pm.new_midi(title=title, tempo=tempo)

vibes = pm.Instrument(mf, pm.I.vibraphone, 1)
bass = pm.Instrument(mf, pm.I.acoustic_bass, 2)

vibes.set_note(pm.N.C4, M/4)
vibes.set_note(pm.N.E4, M/4)
vibes.set_note(pm.N.G4, M/2)

vibes.set_note(pm.N.C4, M/4)
vibes.set_note(pm.N.E4, M/4)
vibes.set_note(pm.N.G4, M/2)

vibes.set_note(pm.N.C4, M/4)
vibes.set_note(pm.N.E4, M/4)
vibes.set_note(pm.N.G4, M/2)

vibes.set_chord(pm.N.C4, M/2)
vibes.set_chord(pm.N.F4, M/2)

vibes.set_chord(pm.N.C4, M/2)
vibes.set_chord(pm.N.F4, M/2)

vibes.set_chord(pm.N.C4, M/2)
vibes.set_chord(pm.N.F4, M/2)
vibes.set_chord(pm.N.G4, M)

#  vibes.set_volume(30, 0)
#  for i in range(10,128):
    #  vibes.set_volume(i, 30)

bass.set_rest(3 * M)

bass.set_note(pm.N.C3, M/4)
bass.set_note(pm.N.C3, M/8)
bass.set_note(pm.N.G3, M/8)
bass.set_rest(M/2)

bass.set_note(pm.N.C3, M/4)
bass.set_note(pm.N.C3, M/8)
bass.set_note(pm.N.G3, M/8)
bass.set_rest(M/2)

bass.set_note(pm.N.C3, M/4)
bass.set_note(pm.N.C3, M/8)
bass.set_note(pm.N.G3, M/8)
bass.set_rest(M/2)

#  bass.set_note(pm.N.C3, M/4)
#  bass.set_note(57, M/8)
#  bass.set_note(57, M/8)
#  bass.set_note(pm.N.C3, M/4)
#  bass.set_note(57, M/8)
#  bass.set_note(57, M/8)

filepath = pm.save_midi(mf, folder, filename)

mf.print_tracks()

subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
subprocess.run(["timidity", "-c", "voices.cfg", filepath])
