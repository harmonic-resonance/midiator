"""
script for generating accompaniment for Thelio videos
:bpm: based on the observed timing of the suspend light
"""
import rich
import phimidi as pm
import math as math
import subprocess as subprocess
import numpy as np
import itertools as itertools
import random as random

log = rich.print

PROJECT = 'phi-midi'
NAME = 'test_chords'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

bpm = 120  # beats per minute
tempo = int(pm.bpm2tempo(bpm))

root = pm.N.E3
octaves = 2
scale_type = pm.S.major

scale = pm.Scale(
    root=root,
    scale_type=scale_type,
    octaves=octaves)

#  perms = list(itertools.combinations(scale, 4))
#  random.shuffle(perms)

# create new midi session
mf = pm.new_midi(title=title, tempo=tempo)

bpM = 4  # beats per Measure
M = bpM * mf.ticks_per_beat  # ticks per Measure

vibes = pm.make_vibes(mf, 1)
#  bass = pm.make_bass(mf, 2)
#  horns = pm.make_horns(mf, 3)
strings = pm.make_strings(mf, 4)

#  kick = pm.make_kick(mf)
#  snare = pm.make_snare(mf)
#  ride = pm.make_ride(mf)
#  tick = pm.make_tick(mf)
#  hihat_closed = pm.make_hihat_closed(mf)

#  choir = pm.make_choir_swell(mf)
#  solo = pm.make_solo_aah(mf)

# create numpy array for volume steps
# results in 16 steps
steps = np.arange(32, 96, 4)

#  chords = pm.progressions.I_vi_ii_V(root)
#  chords.extend(pm.progressions.i_vi_ii_V(root))

#  chords = pm.progressions.ii_V_I_I(root)
#  chords.extend(pm.progressions.ii_V_i_i(root))
chords = pm.progressions.thelio(root)

log(chords)
input('paused')

for verse in range(2):
    # each cord is held for 4 measures
    for chord_num, (chord_name, chord) in enumerate(chords):

        offset = M/32
        #  vibes.set_rest(2 * M)
        #  vibes.set_text(chord_name, M)
        if verse == 1:
            vibes.set_notes([note + 12 for note in chord], M, offset=offset, velocity=55)
        else:
            vibes.set_notes(chord, M, offset=offset, velocity=55)

        strings.set_rest(M / 2)
        strings.set_notes(chord, M / 2, 0)
        #  strings.set_volume(steps[0], 4 * M)
        #  for val in steps:
            #  strings.set_volume(val, M/len(steps))
        #  for val in reversed(steps):
            #  strings.set_volume(val, 3 * M/len(steps))



filepath = pm.save_midi(mf, folder, filename)

subprocess.run(["timidity", '-in', "-c", "~/.photon/timidity.cfg", filepath])
# save to vorbis ogg
#  subprocess.run(["timidity", "-c", "~/.photon/timidity.cfg", filepath, '-Ov'])
