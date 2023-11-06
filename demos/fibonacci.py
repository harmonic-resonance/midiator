"""
Music for Fibonacci
"""
import phimidi as pm
import itertools as itertools
import random as random
from rich import print as log

PROJECT = 'fibonacci'
bpm = 120  # beats per minute
bpM = 4  # beats per Measure
key = "E"
root = pm.N.E3
octaves = 2
scale_type = pm.S.major
#  scale_type = pm.S.dorian


scale = pm.build_scale(
    root=root, 
    scale_type=scale_type, 
    octaves=octaves)

scale = reversed(scale)

F1 = 1
F2 = 1

part = pm.Part(PROJECT, f'01-{scale_type}', bpm=bpm, root=root, key=key)
b = part.ticks_per_beat
M = bpM * part.ticks_per_beat  # ticks per Measure

limit = 377
#  limit = 233


#  chord = pm.chords.get_chord_notes(pm.N.G3, pm.C.dominant_13)
#  scale = chord

threshold = 5

#  inst = part.add_choir_swell()
#  inst.set_note(root, limit * b, velocity=30)

for i, note in enumerate(scale):

    if F2 > threshold:
        inst = part.add_choir_swell()
        #  note += 12
        velocity = 60
    else:
        inst = part.add_vibes()
        #  inst = part.add_bass()
        velocity = 30

    for _ in range(int(limit/(F1 + F2))):
        inst.set_rest(F2 * b)
        inst.set_note(note, F1 * b, velocity=velocity)

        if F2 > threshold:
            inst.ramp_volume_up(F2 * b, lo=16)
            inst.ramp_volume_down(F1 * b, lo=16)

    F1, F2 = F2, F1 + F2

#  part.save()
part.play()
#  part.convert()
    
