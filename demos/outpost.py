import phimidi as pm
import math as math
import subprocess as subprocess
import numpy as np
import itertools as itertools
import random as random

PROJECT = 'phi-midi'
NAME = 'outpost'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

bpm = 120
tempo = int(pm.bpm2tempo(bpm))

root = pm.N.D3
octaves = 2
scale_type = pm.S.dorian
#  scale_type = pm.S.major
scale_type = pm.S.pentatonic_major

scale = pm.build_scale(
    root=root, 
    scale_type=scale_type, 
    octaves=octaves)

perms = list(itertools.combinations(scale, 4))
random.shuffle(perms)

mf = pm.new_midi(title=title, tempo=tempo)
M = 4 * mf.ticks_per_beat

vibes = pm.make_vibes(mf, 1)
horns = pm.make_horns(mf, 3)
strings = pm.make_strings(mf, 4)

#  kick = pm.make_kick(mf)
#  snare = pm.make_snare(mf)
#  tick = pm.make_tick(mf)

choir = pm.make_choir_swell(mf)
#  choir = strings

steps = np.arange(32, 96, 4)
print(f'steps: {len(steps)}')
print(steps)


for chord in perms:
    #choir
    choir.set_volume(steps[0], 0)
    choir.set_notes(chord, 15 * M/4)
    choir.set_rest(M/4)
    for val in steps:
        choir.set_volume(val, 2 * M/len(steps))
    for val in reversed(steps):
        choir.set_volume(val, 2 * M/len(steps))

    #vibes
    vibes.set_volume(steps[0], 0)
    chord = [note + 12 for note in chord]
    pm.add_arp_up(vibes, chord, M)
    pm.add_arp_down(vibes, chord, M)
    pm.add_arp_up(vibes, chord, M)
    pm.add_arp_down(vibes, chord, M)

    for val in steps:
        vibes.set_volume(val, 4 * M/len(steps))
    #  for val in reversed(steps):
        #  vibes.set_volume(val, 2 * M/len(steps))


filepath = pm.save_midi(mf, folder, filename)

#  subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
subprocess.run(["timidity", '-in', "-c", "~/.photon/timidity.cfg", filepath])
