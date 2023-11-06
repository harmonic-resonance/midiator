import phimidi as pm
import math as math
import subprocess as subprocess

PROJECT = 'phi-midi'
NAME = 'band'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

bpm = 60
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

#  horns.set_rest(1 * M)
#  strings.set_rest(4 * M)
#  horns.set_chord(pm.N.C4, M)
#  horns.set_chord(pm.N.G4, M)
#  horns.set_chord(pm.N.C5, M)
#  horns.set_chord(pm.N.G4, M)

#  for _ in range(4):
    #  horns.set_volume(0, 0)
    #  for i in range(1,17):
        #  horns.set_volume(i * 7, M/16)

horns.set_rest(4 * M)
strings.set_chord(pm.N.C4, M, velocity=40)
strings.set_chord(pm.N.G4, M, velocity=60)
strings.set_chord(pm.N.C5, M, velocity=80)
strings.set_chord(pm.N.G4, M, velocity=60)

strings.set_volume(0, 0)
for _ in range(2):
    strings.set_volume(0, 0)
    for i in range(1,17):
        strings.set_volume(i * 7, M/16)
    for i in range(16,0,-1):
        strings.set_volume(i * 7, M/16)

strings.set_volume(100, 0)
horns.set_rest(4 * M)
for _ in range(4):
    strings.set_chord(pm.N.C4, M, velocity=40)
#  strings.set_chord(pm.N.G4, M, velocity=60)
#  strings.set_chord(pm.N.C5, M, velocity=80)
#  strings.set_chord(pm.N.G4, M, velocity=60)

strings.set_pan(64, 4 * M)
strings.set_pan(0, M)
strings.set_pan(64, M)
strings.set_pan(120, M)
strings.set_pan(64, M)

vibes.set_rest(8 * M)
vibes.set_pan(64, 8 * M)
for _ in range(2):
    chord = pm.get_chord_notes(pm.N.C4, pm.C.dominant_13)
    while len(chord) < 8:
        chord.extend(chord[0:8-len(chord)])
    pm.add_arp_up(vibes, chord, M)
    pm.add_arp_down(vibes, chord, M)

swell.set_rest(9 * M)
#  swell.set_chord(pm.N.C4, M*2, chord_type=pm.C.major)
#  swell.set_chord(pm.N.G4, M*2, chord_type=pm.C.major_7)
#  swell.set_chord(pm.N.F4, M*2, chord_type=pm.C.major_7)
#  swell.set_chord(pm.N.C4, M*2, chord_type=pm.C.sus2)

filepath = pm.save_midi(mf, folder, filename)

#  subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
subprocess.run(["timidity", "-c", "voices.cfg", filepath])
