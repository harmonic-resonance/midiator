import phimidi as pm
import math as math
import subprocess as subprocess
import numpy as np

PROJECT = 'phi-midi'
NAME = 'band3'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

bpm = 30
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

vibes = pm.make_vibes(mf, 1)
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

#  horns.set_rest(4 * M)
#  strings.set_chord(pm.N.C4, M, velocity=40)
#  strings.set_chord(pm.N.G4, M, velocity=60)
#  strings.set_chord(pm.N.C5, M, velocity=80)
#  strings.set_chord(pm.N.G4, M, velocity=60)

#  strings.set_volume(0, 0)
#  for _ in range(2):
    #  strings.set_volume(0, 0)
    #  for i in range(1,17):
        #  strings.set_volume(i * 7, M/16)
    #  for i in range(16,0,-1):
        #  strings.set_volume(i * 7, M/16)

#  strings.set_volume(100, 0)
#  horns.set_rest(4 * M)
#  for _ in range(4):
    #  strings.set_chord(pm.N.C4, M, velocity=40)
#  #  strings.set_chord(pm.N.G4, M, velocity=60)
#  #  strings.set_chord(pm.N.C5, M, velocity=80)
#  #  strings.set_chord(pm.N.G4, M, velocity=60)

#  strings.set_pan(64, 4 * M)
#  strings.set_pan(0, M)
#  strings.set_pan(64, M)
#  strings.set_pan(120, M)
#  strings.set_pan(64, M)

#  vibes.set_rest(8 * M)
#  vibes.set_pan(64, 8 * M)
steps = np.arange(4, 125, 4)

chord = pm.get_chord_notes(pm.N.C4, pm.C.dominant_7)
while len(chord) < 8:
    chord.extend(chord[0:8-len(chord)])

#  vibes = horns
vibes = swell
level = 0
vibes.track_volume.append(pm.Message('control_change', channel=vibes.channel, control=65, value=127, time=0))
vibes.track_volume.append(pm.Message('control_change', channel=vibes.channel, control=84, value=100, time=0))
vibes.track_volume.append(pm.Message('control_change', channel=vibes.channel, control=5, value=level, time=0))
for _ in range(2):
    pm.add_arp_up(vibes, chord, M)
    pm.add_arp_down(vibes, chord, M)

    vibes.set_volume(0, 0)
    #  vibes.track_volume.append(pm.Message('control_change', channel=vibes.channel, control=65, value=127, time=0))
    vibes.track_volume.append(pm.Message('control_change', channel=vibes.channel, control=5, value=level, time=0))
    for val in steps:
        vibes.set_volume(val, M/len(steps))
    #  vibes.track_volume.append(pm.Message('control_change', channel=vibes.channel, control=65, value=0, time=0))
    vibes.track_volume.append(pm.Message('control_change', channel=vibes.channel, control=5, value=0, time=0))
    for val in reversed(steps):
        vibes.set_volume(val, M/len(steps))

    vibes.set_pan(0, 0)
    for val in steps:
        vibes.set_pan(val, (2*M)/len(steps))

filepath = pm.save_midi(mf, folder, filename)

#  subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
subprocess.run(["timidity", "-c", "~/.photon/timidity.cfg", filepath])
