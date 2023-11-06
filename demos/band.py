import phimidi as pm
import math as math
import subprocess as subprocess

PROJECT = 'phi-midi'
NAME = 'band'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

bpm = 120
tempo = int(pm.bpm2tempo(bpm))

root = pm.N.D3
octaves = 3
scale_type = pm.S.dorian

scale = pm.build_scale(
    root=root, 
    scale_type=scale_type, 
    octaves=octaves)

mf = pm.new_midi(title=title, tempo=tempo)
M = 4 * mf.ticks_per_beat

piano = pm.make_piano(mf, 0)
vibes = pm.make_vibes(mf, 1)
bass = pm.make_bass(mf, 2)
horns = pm.make_horns(mf, 3)
strings = pm.make_strings(mf, 4)

kick = pm.make_kick(mf)
snare = pm.make_snare(mf)
tick = pm.make_tick(mf)

swell = pm.make_choir_swell(mf)

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

#  bass.set_rest(3 * M)

for _ in range(3):
    bass.set_note(pm.N.C3, M/4)
    bass.set_note(pm.N.C3, M/8)
    bass.set_note(pm.N.G3, M/8)
    bass.set_rest(M/2)

horns.set_rest(4 * M)
horns.set_chord(pm.N.C4, M, velocity=20)
horns.set_chord(pm.N.G4, M, velocity=40)
horns.set_chord(pm.N.C5, M, velocity=60)

piano.set_rest(5 * M)
for _ in range(3):
    piano.set_chord(pm.N.C5, M/2)
    piano.set_chord(pm.N.C6, M/2)

swell.set_rest(4 * M)
swell.set_chord(pm.N.C4, M*2, chord_type=pm.C.major)
swell.set_chord(pm.N.G4, M*2, chord_type=pm.C.major_7)
swell.set_chord(pm.N.F4, M*2, chord_type=pm.C.major_7)
swell.set_chord(pm.N.C4, M*2, chord_type=pm.C.sus2)

filepath = pm.save_midi(mf, folder, filename)

#  mf.print_tracks()

subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
subprocess.run(["timidity", "-c", "voices.cfg", filepath])
