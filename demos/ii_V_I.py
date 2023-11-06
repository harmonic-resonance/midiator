import phimidi as pm
import math as math
import subprocess as subprocess
import numpy as np
import itertools as itertools
import random as random

PROJECT = 'phi-midi'
NAME = 'ii_V_I'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

bpm = 120
tempo = int(pm.bpm2tempo(bpm))

root = pm.N.A3
octaves = 2
scale_type = pm.S.dorian
scale_type = pm.S.pentatonic_major

scale = pm.build_scale(
    root=root,
    scale_type=scale_type,
    octaves=octaves)

#  perms = list(itertools.combinations(scale, 4))
#  random.shuffle(perms)

mf = pm.new_midi(title=title, tempo=tempo)
M = 4 * mf.ticks_per_beat

piano = pm.make_piano(mf, 0)
vibes = pm.make_vibes(mf, 1)
bass = pm.make_bass(mf, 2)
horns = pm.make_horns(mf, 3)
strings = pm.make_strings(mf, 4)

kick = pm.make_kick(mf)
snare = pm.make_snare(mf)
ride = pm.make_ride(mf)

choir = pm.make_choir_swell(mf)
solo = pm.make_solo_aah(mf)
#  choir = strings

steps = np.arange(32, 96, 4)
print(f'steps: {len(steps)}')
print(steps)

chords = pm.progressions.ii_V_i(root)
#  chords = pm.progressions.i_vi_ii_V(root)
while len(chords) < 4:
    chords.append(chords[-1])

def comp_1(inst, chords, dur):
    b = dur / 4 / 8
    while len(chords) < 4:
        chords.append(chords[-1])

    for chord in chords:
        for _ in range(4):
            inst.set_notes(chord, 3 * b)
            inst.set_notes(chord, 1 * b)
            inst.set_rest(4 * b)

for cycle in range(4):
    #  comp_1(piano, chords, 4 * M)
    for chord in chords:
        for _ in range(4):
            pm.patterns.swing.swing(M, kick, ride)
            bass.set_note(chord[0] - 12, M/2, velocity=80)
            bass.set_note(chord[2] - 24, M/2, velocity=50)
            if cycle > 0:
                horns.set_rest(M/4)
                horns.set_note(chord[1], M/4)
                horns.set_rest(M/4)
                horns.set_note(chord[3], M/4)
            else:
                horns.set_rest(M)
        for val in steps:
            horns.set_volume(val, 4 * M/len(steps))

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

        #  for val in reversed(steps): #  vibes.set_volume(val, 2 * M/len(steps))

        # strings
        if cycle > 1:
            pm.add_arp_down(strings, chord, 4 * M)
        else:
            strings.set_rest(4 * M)
        for val in steps:
            strings.set_volume(val, 1 * M/len(steps))
        for val in reversed(steps):
            strings.set_volume(val, 3 * M/len(steps))

        if cycle > 2:
            solo.set_rest(M/4)
            solo.set_note(chord[0], M/4)
            solo.set_note(chord[2], 2 * M/4)
            solo.set_rest(M/4)
            solo.set_note(chord[3], M/4)
            solo.set_note(chord[1], 2 * M/4)
            solo.set_rest(M/4)
            solo.set_note(chord[0], M/4)
            solo.set_note(chord[2], 2 * M/4)
            solo.set_rest(M/4)
            solo.set_note(chord[1], M/4)
            solo.set_note(chord[3], 2 * M/4)
        else:
            solo.set_rest(4 * M)

filepath = pm.save_midi(mf, folder, filename)

proc  = ["timidity", 
        '-in', 
        "-c", "~/.photon/timidity.cfg", 
        '-A', '120', 
        filepath]
subprocess.run(proc)
